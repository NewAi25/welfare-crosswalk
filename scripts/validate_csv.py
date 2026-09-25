"""Validate every CSV in data/ against the schemas in standard/definitions.md and data/README.md.

Prints one line per file, OK or the first error found, and exits non zero if any
file has an error. Standard library only.

    python scripts/validate_csv.py
"""
import csv
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
YES_NO = {"yes", "no"}

SCHEMAS = {
    "indicators.csv": {
        "header": ["indicator_id", "efsa_consequence", "efsa_abm", "wq_principle", "wq_criterion", "wq_measure",
                   "maroto_molina_technology", "maroto_molina_feasible", "notes", "tier"],
        "enums": {"maroto_molina_feasible": {"yes", "partial", "no", "not_covered"},
                  "tier": {"joined", "efsa_only", "wq_only"}},
        "optional": {"tier"},
        "required": ["indicator_id"],
        "key": ["indicator_id"],
    },
    "products.csv": {
        "header": ["product_id", "vendor", "product", "sensor_type", "measures_claimed", "species", "country",
                   "stygar_listed", "stygar_validation", "icar_validated", "source", "marketing_url", "manual_url",
                   "devdocs_url", "patent_urls", "comparator", "notes"],
        "enums": {"sensor_type": {"collar_accelerometer", "ear_tag", "bolus", "camera", "milking_system", "other"},
                  "stygar_listed": YES_NO,
                  "stygar_validation": {"none", "external_self", "external_independent", "not_listed"},
                  "icar_validated": YES_NO, "source": {"stygar", "icar", "market_scan", "course"},
                  "comparator": YES_NO},
        "required": ["product_id", "vendor", "product"],
        "key": ["product_id"],
    },
    "sensor_coverage.csv": {
        "header": ["indicator_id", "ai_grade", "product_ids", "stygar_trait", "stygar_refs", "maroto_feasible",
                   "hardware_class", "market_breadth", "market_keywords", "evidence_note", "notes"],
        "enums": {"ai_grade": {"validated_commercial", "commercial_unvalidated", "research_only", "none", "unsure"},
                  "hardware_class": {"routine_data", "farm_fixed", "animal_mounted", "sample_or_procedure", "none", "unsure"},
                  "maroto_feasible": {"yes", "partial", "no", "not_covered"}},
        "optional": {"market_breadth"},
        "ints": ["market_breadth"],
        "required": ["indicator_id", "ai_grade", "hardware_class", "evidence_note"],
        "key": ["indicator_id"],
    },
    "crosswalk.csv": {
        "header": ["indicator_id", "scheme", "requirement_text", "section_ref", "page", "numeric_threshold",
                   "audit_method", "industry_naming", "notes"],
        "enums": {"scheme": {"RSPCA_Assured", "FARM_v5", "GAP_dairy", "Certified_Humane"},
                  "audit_method": {"visual_inspection", "records_review", "sensor_accepted", "unspecified"},
                  "industry_naming": {"named_with_threshold", "named", "related_resource", "not_named"}},
        "optional": {"audit_method", "industry_naming"},
        "required": ["indicator_id", "scheme"],
        "key": ["indicator_id", "scheme"],
    },
}

REFERENCES = [
    ("sensor_coverage.csv", "indicator_id", "indicators.csv", "indicator_id"),
    ("crosswalk.csv", "indicator_id", "indicators.csv", "indicator_id"),
]


class Invalid(Exception):
    pass


def load(name, schema):
    path = DATA / name
    if not path.exists():
        raise Invalid("file missing")
    with path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    if not rows or rows[0] != schema["header"]:
        raise Invalid(f"header does not match schema; expected {','.join(schema['header'])}")
    records = []
    for line, values in enumerate(rows[1:], start=2):
        if not any(v.strip() for v in values):
            continue
        if len(values) != len(rows[0]):
            raise Invalid(f"line {line}: {len(values)} fields, header has {len(rows[0])}")
        records.append((line, dict(zip(rows[0], values))))
    return records


def check_rows(name, schema, records):
    optional = schema.get("optional", set())
    seen = set()
    for line, row in records:
        for field in schema["required"]:
            if not row[field].strip():
                raise Invalid(f"line {line}: {field} is empty")
        for field, allowed in schema["enums"].items():
            value = row[field]
            if value == "" and field in optional:
                continue
            if value not in allowed:
                raise Invalid(f"line {line}: {field} = {value!r}, allowed {sorted(allowed)}")
        for field in schema.get("ints", []):
            if row[field] and not row[field].isdigit():
                raise Invalid(f"line {line}: {field} = {row[field]!r}, expected a whole number")
        key = tuple(row[k] for k in schema["key"])
        if key in seen:
            raise Invalid(f"line {line}: duplicate {'/'.join(key)}")
        seen.add(key)
        if name == "crosswalk.csv":
            has_req = bool(row["requirement_text"].strip())
            if has_req and not row["audit_method"]:
                raise Invalid(f"line {line}: audit_method empty on a row with a requirement")
            if not has_req and row["audit_method"]:
                raise Invalid(f"line {line}: audit_method set on a row with no requirement")
            if has_req and not (row["section_ref"].strip() and row["page"].strip()):
                raise Invalid(f"line {line}: a quoted requirement needs section_ref and page")
            if row["industry_naming"] and row["scheme"] != "FARM_v5":
                raise Invalid(f"line {line}: industry_naming is only set on FARM_v5 rows")
        if name == "sensor_coverage.csv":
            if row["ai_grade"] in {"validated_commercial", "commercial_unvalidated"} and not row["product_ids"].strip():
                raise Invalid(f"line {line}: grade {row['ai_grade']} needs product_ids")
            if row["ai_grade"] == "validated_commercial" and not row["stygar_refs"].strip():
                raise Invalid(f"line {line}: validated_commercial needs stygar_refs")


def main():
    loaded, errors = {}, {}
    for name, schema in SCHEMAS.items():
        try:
            records = load(name, schema)
            check_rows(name, schema, records)
            loaded[name] = records
        except Invalid as e:
            errors[name] = str(e)
    for name, field, target, key in REFERENCES:
        if name in errors or target not in loaded:
            continue
        known = {r[key] for _, r in loaded[target]}
        for line, r in loaded[name]:
            if r[field] and r[field] not in known:
                errors[name] = f"line {line}: {field} {r[field]!r} not found in {target}"
                break
    for name in SCHEMAS:
        print(f"{name}: {errors.get(name, 'OK')}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
