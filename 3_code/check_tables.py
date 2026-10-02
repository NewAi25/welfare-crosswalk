"""CHECK TABLES: the mechanical checks on the four research tables in 2_research/.

In plain words
    The research lives in four spreadsheet files (CSV). This script checks that they are
    well formed and agree with each other. It does not check that a value is TRUE; that
    is the job of the auditor and of a person reading the source page. It checks that
    nothing is missing, misspelled, duplicated or out of date.

What it checks
    1. Every file has exactly the expected columns, in order.
    2. Every coded value is one of the allowed codes listed in 2_research/rules.md
       (for example sensor_evidence can only be validated_commercial,
       commercial_unvalidated, research_only, none or unsure).
    3. No indicator appears twice; every indicator id used anywhere exists in indicators.csv.
    4. Rows obey the rules that can be checked mechanically:
       a product is named whenever the sensor evidence is commercial;
       study numbers and validated products are given whenever it is validated_commercial;
       every product named exists, either as a P number in products.csv or as a
       Provider|Name pair in the Stygar list of 129;
       vendors_naming_it equals a fresh count from the Stygar spreadsheet;
       maroto_molina_rating is copied correctly from indicators.csv;
       listed_by follows from which source columns are filled;
       every cell coded unsure (in any column that allows it) has a line for its indicator
       in 2_research/open_questions.md;
       a scheme row that quotes a requirement gives the section, page and how it is checked.

How to run it
    python 3_code/check_tables.py
    It prints OK or the first problem for each file, and exits with an error if any
    file has a problem. The push gate runs it before every push.
"""
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import count_vendors  # noqa: E402  (same folder)

ROOT = Path(__file__).resolve().parent.parent
TABLES = ROOT / "2_research"
YES_NO = {"yes", "no"}
RATINGS = {"yes", "partial", "no", "not_covered"}

SCHEMAS = {
    "indicators.csv": {
        "columns": ["indicator_id", "efsa_welfare_consequence", "efsa_measure", "wq_principle", "wq_criterion",
                    "wq_measure", "measure_type", "maroto_molina_technology", "maroto_molina_rating", "notes", "listed_by"],
        "codes": {"maroto_molina_rating": RATINGS, "listed_by": {"joined", "efsa_only", "wq_only"},
                  "measure_type": {"animal_based", "resource_based", "management_based", "none"}},
        "must_fill": ["indicator_id", "listed_by", "measure_type", "maroto_molina_rating"],
        "key": ["indicator_id"],
    },
    "products.csv": {
        "columns": ["product_id", "vendor", "product", "appendix_name", "sensor_type", "vendor_description", "country",
                    "in_stygar_list", "validation_found", "icar_validated", "link", "notes"],
        "codes": {"sensor_type": {"collar_accelerometer", "ear_tag", "bolus", "camera", "milking_system", "other"},
                  "in_stygar_list": YES_NO, "icar_validated": YES_NO,
                  "validation_found": {"none", "external_self", "external_independent", "not_listed"}},
        "must_fill": ["product_id", "vendor", "product", "sensor_type", "vendor_description", "in_stygar_list",
                      "validation_found", "icar_validated", "notes"],
        "key": ["product_id"],
    },
    "sensor_coverage.csv": {
        "columns": ["indicator_id", "sensor_evidence", "products", "validated_products", "validated_trait",
                    "study_numbers", "maroto_molina_rating", "device_needed", "vendors_naming_it", "search_words",
                    "where_to_check", "reasoning"],
        "codes": {"sensor_evidence": {"validated_commercial", "commercial_unvalidated", "research_only", "none", "unsure"},
                  "device_needed": {"routine_data", "farm_fixed", "animal_mounted", "sample_or_procedure", "none", "unsure"},
                  "maroto_molina_rating": RATINGS},
        "must_fill": ["indicator_id", "sensor_evidence", "device_needed", "vendors_naming_it", "search_words",
                      "where_to_check"],
        "whole_numbers": ["vendors_naming_it"],
        "key": ["indicator_id"],
    },
    "crosswalk.csv": {
        "columns": ["indicator_id", "scheme", "requirement_quote", "section", "page", "number_in_requirement",
                    "how_checked", "farm_naming", "reasoning"],
        "codes": {"scheme": {"RSPCA_Assured", "FARM_v5", "GAP_dairy", "Certified_Humane"},
                  "how_checked": {"visual_inspection", "records_review", "sensor_accepted", "unspecified", "unsure"},
                  "farm_naming": {"named_with_threshold", "named", "related_resource", "not_named", "unsure"}},
        "may_be_empty": {"how_checked", "farm_naming"},
        "must_fill": ["indicator_id", "scheme"],
        "key": ["indicator_id", "scheme"],
    },
}


class Problem(Exception):
    pass


def load(name):
    schema = SCHEMAS[name]
    path = TABLES / name
    if not path.exists():
        raise Problem("file missing")
    with path.open(newline="", encoding="utf-8-sig") as f:
        lines = list(csv.reader(f))
    if not lines or lines[0] != schema["columns"]:
        raise Problem("columns do not match; expected " + ",".join(schema["columns"]))
    rows = []
    for number, values in enumerate(lines[1:], start=2):
        if not any(v.strip() for v in values):
            continue
        if len(values) != len(lines[0]):
            raise Problem(f"line {number}: {len(values)} cells, expected {len(lines[0])}")
        rows.append((number, dict(zip(lines[0], values))))
    return rows


def check_basic(name, rows):
    schema = SCHEMAS[name]
    may_be_empty = schema.get("may_be_empty", set())
    seen = set()
    for number, r in rows:
        for column in schema["must_fill"]:
            if not r[column].strip():
                raise Problem(f"line {number}: {column} is empty")
        for column, allowed in schema["codes"].items():
            if r[column] == "" and (column in may_be_empty or column not in schema["must_fill"]):
                continue
            if r[column] not in allowed:
                raise Problem(f"line {number}: {column} = {r[column]!r}; allowed {sorted(allowed)}")
        for column in schema.get("whole_numbers", []):
            if not r[column].isdigit():
                raise Problem(f"line {number}: {column} = {r[column]!r}; expected a whole number")
        key = tuple(r[k] for k in schema["key"])
        if key in seen:
            raise Problem(f"line {number}: {'/'.join(key)} appears twice")
        seen.add(key)


def product_tokens(text):
    """Split the products cell into P numbers and appendix:Provider|Name references."""
    return [t.strip() for t in re.split(r"\s+(?=P\d{3}\b|appendix:)", text.strip()) if t.strip()]


def check_links(tables, open_questions):  # noqa: C901 (one check per rule, kept flat on purpose)
    indicators = {r["indicator_id"]: r for _, r in tables["indicators.csv"]}
    product_ids = {r["product_id"] for _, r in tables["products.csv"]}
    stygar = count_vendors.appendix_products()
    stygar_keys = {p["key"] for p in stygar}
    stygar_names = {p["name"] for p in stygar}
    problems = {}

    for number, r in tables["indicators.csv"]:
        expected = ("joined" if r["efsa_measure"].strip() and r["wq_measure"].strip()
                    else "efsa_only" if r["efsa_measure"].strip()
                    else "wq_only" if (r["wq_measure"].strip() or r["wq_criterion"].strip()) else "no source")
        if r["listed_by"] != expected:
            problems.setdefault("indicators.csv", f"line {number}: listed_by is {r['listed_by']}, the sources give {expected}")
        elif r["efsa_measure"].strip() and r["measure_type"] != "animal_based":
            problems.setdefault("indicators.csv", f"line {number}: an EFSA measure is animal_based by definition")

    for number, r in tables["products.csv"]:
        if r["in_stygar_list"] == "yes" and r["appendix_name"] not in stygar_names:
            problems.setdefault("products.csv", f"line {number}: appendix_name {r['appendix_name']!r} is not in the Stygar list")

    name = "sensor_coverage.csv"
    for number, r in tables[name]:
        iid, grade = r["indicator_id"], r["sensor_evidence"]
        problem = None
        if iid not in indicators:
            problem = f"{iid} is not in indicators.csv"
        elif r["maroto_molina_rating"] != indicators[iid]["maroto_molina_rating"]:
            problem = f"maroto_molina_rating {r['maroto_molina_rating']} differs from indicators.csv ({indicators[iid]['maroto_molina_rating']})"
        elif grade in {"validated_commercial", "commercial_unvalidated"} and not r["products"].strip():
            problem = f"sensor_evidence {grade} needs at least one product"
        elif grade == "validated_commercial" and not (r["study_numbers"].strip() and r["validated_products"].strip()):
            problem = "validated_commercial needs study_numbers and validated_products"
        elif grade != "validated_commercial" and r["validated_products"].strip():
            problem = "validated_products is only filled when sensor_evidence is validated_commercial"
        elif "unsure" in (grade, r["device_needed"]) and not re.search(rf"\b{iid}\b", open_questions):
            problem = "a cell is unsure, but there is no line for it in open_questions.md"
        if problem is None:
            for token in product_tokens(r["products"]):
                if token.startswith("appendix:"):
                    if token[len("appendix:"):] not in stygar_keys:
                        problem = f"product {token!r} is not in the Stygar list"
                elif token not in product_ids:
                    problem = f"product {token!r} is not in products.csv"
            for key in filter(None, (k.strip() for k in r["validated_products"].split(";"))):
                if key not in stygar_keys:
                    problem = f"validated product {key!r} is not in the Stygar list"
        if problem is None:
            fresh = sum(count_vendors.names_it(p, count_vendors.search_words(r["search_words"])) for p in stygar)
            if str(fresh) != r["vendors_naming_it"]:
                problem = (f"vendors_naming_it is {r['vendors_naming_it']} but a fresh count gives {fresh}; "
                           f"run python 3_code/count_vendors.py {iid}")
        if problem:
            problems.setdefault(name, f"line {number}: {problem}")

    for number, r in tables["crosswalk.csv"]:
        problem = None
        quoted = bool(r["requirement_quote"].strip())
        if r["indicator_id"] not in indicators:
            problem = f"{r['indicator_id']} is not in indicators.csv"
        elif quoted and not r["how_checked"]:
            problem = "a quoted requirement needs how_checked"
        elif not quoted and r["how_checked"]:
            problem = "how_checked is filled but no requirement is quoted"
        elif quoted and not (r["section"].strip() and r["page"].strip()):
            problem = "a quoted requirement needs section and page"
        elif r["farm_naming"] and r["scheme"] != "FARM_v5":
            problem = "farm_naming is only filled on FARM_v5 rows"
        elif r["scheme"] == "FARM_v5" and not r["farm_naming"]:
            problem = "farm_naming must be filled on every FARM_v5 row"
        elif r["scheme"] == "FARM_v5" and quoted and r["farm_naming"] not in ("named", "named_with_threshold", "unsure"):
            problem = "a FARM requirement is quoted, so farm_naming must be named or named_with_threshold"
        elif r["scheme"] == "FARM_v5" and not quoted and r["farm_naming"] in ("named", "named_with_threshold"):
            problem = "farm_naming says named, but no FARM requirement is quoted"
        elif "unsure" in (r["how_checked"], r["farm_naming"]) and not re.search(rf"\b{r['indicator_id']}\b", open_questions):
            problem = "a cell is unsure, but there is no line for it in open_questions.md"
        elif r["farm_naming"] == "named_with_threshold" and not r["number_in_requirement"].strip():
            problem = "named_with_threshold needs the number in number_in_requirement"
        if problem:
            problems.setdefault("crosswalk.csv", f"line {number}: {problem}")
    return problems


def main():
    tables, problems = {}, {}
    for name in SCHEMAS:
        try:
            tables[name] = load(name)
            check_basic(name, tables[name])
        except Problem as e:
            problems[name] = str(e)
    if not problems:
        open_questions = (TABLES / "open_questions.md").read_text(encoding="utf-8")
        problems.update(check_links(tables, open_questions))
    for name in SCHEMAS:
        print(f"{name}: {problems.get(name, 'OK')}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
