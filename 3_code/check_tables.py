"""CHECK TABLES: the mechanical checks on the six research tables in 2_research/.

In plain words
    The research lives in six spreadsheet files (CSV). This script checks that they are
    well formed and agree with each other. It does not check that a value is TRUE; that
    is the job of the auditor and of a person reading the source page. It checks that
    nothing is missing, misspelled, duplicated or out of date.

What it checks
    1. Every file has exactly the expected columns, in order.
    2. Every coded value is one of the allowed codes listed in 2_research/rules.md
       (for example sensor_evidence can only be validated_commercial,
       commercial_unvalidated, research_demonstrated, theoretically_measurable, none or unsure).
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
       a scheme row's requirement_status (required, unsure, not_required) agrees with what it
       quotes: a required row quotes the requirement with section, page and how it is checked;
       an unsure row quotes its candidate and has a line in open_questions.md naming the
       indicator and the scheme; a not_required row quotes nothing;
       EFSA's three ratings are filled exactly on the rows that come from EFSA;
       product_links.csv has one row for each of the 129 products in the Stygar list, with
       the maker, name and 2021 link copied exactly, and a current link exactly where one
       was found;
       every since_2021_grade is a sensor evidence code, every evidence key it cites exists in
       evidence_since_2021.csv and names that indicator, and a commercial grade since 2021
       cites at least one piece of evidence.

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
EFSA_LEVELS = {"high", "medium", "low", "mixed", "not_stated"}  # the level word EFSA's own ABM table uses

SCHEMAS = {
    "indicators.csv": {
        "columns": ["indicator_id", "efsa_welfare_consequence", "efsa_measure", "wq_principle", "wq_criterion",
                    "wq_measure", "measure_type", "maroto_molina_technology", "maroto_molina_rating", "notes", "listed_by",
                    "efsa_sensitivity", "efsa_specificity", "efsa_feasibility", "efsa_ratings_quoted"],
        "codes": {"maroto_molina_rating": RATINGS, "listed_by": {"joined", "efsa_only", "wq_only"},
                  "measure_type": {"animal_based", "resource_based", "management_based", "none"},
                  "efsa_sensitivity": EFSA_LEVELS, "efsa_specificity": EFSA_LEVELS, "efsa_feasibility": EFSA_LEVELS},
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
                    "where_to_check", "reasoning", "since_2021_grade", "since_2021_evidence", "since_2021_reasoning"],
        "codes": {"sensor_evidence": {"validated_commercial", "commercial_unvalidated", "research_demonstrated",
                                    "theoretically_measurable", "none", "unsure"},
                  "since_2021_grade": {"validated_commercial", "commercial_unvalidated", "research_demonstrated",
                                    "theoretically_measurable", "none", "unsure"},
                  "device_needed": {"routine_data", "farm_fixed", "animal_mounted", "sample_or_procedure", "none", "unsure"},
                  "maroto_molina_rating": RATINGS},
        "must_fill": ["indicator_id", "sensor_evidence", "device_needed", "vendors_naming_it", "search_words",
                      "where_to_check", "since_2021_grade", "since_2021_reasoning"],
        "whole_numbers": ["vendors_naming_it"],
        "key": ["indicator_id"],
    },
    "crosswalk.csv": {
        "columns": ["indicator_id", "scheme", "requirement_status", "requirement_quote", "section", "page",
                    "number_in_requirement", "how_checked", "farm_naming", "reasoning"],
        "codes": {"scheme": {"RSPCA_Assured", "FARM_v5", "GAP_dairy", "Certified_Humane"},
                  "requirement_status": {"required", "unsure", "not_required"},
                  "how_checked": {"visual_inspection", "records_review", "sensor_accepted", "unspecified", "unsure"},
                  "farm_naming": {"named_with_threshold", "named", "related_resource", "not_named", "unsure"}},
        "may_be_empty": {"how_checked", "farm_naming"},
        "must_fill": ["indicator_id", "scheme", "requirement_status", "reasoning"],
        "key": ["indicator_id", "scheme"],
    },
    "evidence_since_2021.csv": {
        "columns": ["evidence_key", "kind", "citation", "doi_or_url", "year", "found_via", "indicator_ids", "product",
                    "on_sale", "technology", "setting", "n_animals", "authors_independent", "maker_involvement",
                    "measure", "reference_method", "statistic", "sections_read", "source_file", "notes"],
        "codes": {"kind": {"study", "review", "maker_page"},
                  "on_sale": {"yes", "no", "not_stated"},
                  "setting": {"laboratory", "research_farm", "commercial_farm", "mixed", "not_stated", "not_applicable"},
                  "authors_independent": {"yes", "no", "not_stated", "not_applicable"}},
        "must_fill": ["evidence_key", "kind", "citation", "doi_or_url", "year", "found_via", "indicator_ids", "on_sale",
                      "setting", "authors_independent", "measure", "sections_read", "source_file"],
        "key": ["evidence_key"],
    },
    "product_links.csv": {
        "columns": ["appendix_row", "vendor", "product", "link_2021", "link_2021_today", "current_link",
                    "current_link_shows", "page_says", "checked", "notes"],
        "codes": {"link_2021_today": {"works", "moved", "wrong_page", "broken"},
                  "current_link_shows": {"product_page", "related_page", "product_not_listed", "none_found"}},
        "must_fill": ["appendix_row", "vendor", "product", "link_2021", "link_2021_today", "current_link_shows",
                      "checked"],
        "whole_numbers": ["appendix_row"],
        "key": ["appendix_row"],
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
        elif r["efsa_measure"].strip() and not (r["efsa_sensitivity"] and r["efsa_specificity"]
                                                and r["efsa_feasibility"] and r["efsa_ratings_quoted"].strip()):
            problems.setdefault("indicators.csv", f"line {number}: an EFSA row needs its three EFSA ratings and their quotes")
        elif not r["efsa_measure"].strip() and (r["efsa_sensitivity"] or r["efsa_specificity"]
                                                or r["efsa_feasibility"] or r["efsa_ratings_quoted"].strip()):
            problems.setdefault("indicators.csv", f"line {number}: EFSA ratings are only filled on EFSA rows")

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
        status = r["requirement_status"]
        scheme_question = any(r["indicator_id"] in line and r["scheme"] in line for line in open_questions.splitlines())
        if r["indicator_id"] not in indicators:
            problem = f"{r['indicator_id']} is not in indicators.csv"
        elif status in ("required", "unsure") and not (quoted and r["section"].strip() and r["page"].strip()):
            problem = f"a {status} row needs the quoted requirement with its section and page"
        elif status == "required" and not r["how_checked"]:
            problem = "a required row needs how_checked"
        elif status == "not_required" and (quoted or r["section"].strip() or r["page"].strip()
                                           or r["number_in_requirement"].strip() or r["how_checked"]):
            problem = "a not_required row quotes nothing and has no section, page, number or how_checked"
        elif status == "unsure" and not scheme_question:
            problem = "an unsure row needs a line in open_questions.md naming the indicator and the scheme"
        elif r["scheme"] == "FARM_v5" and status == "required" and r["farm_naming"] not in ("named", "named_with_threshold"):
            problem = "a required FARM row is named or named_with_threshold"
        elif r["scheme"] == "FARM_v5" and status == "unsure" and r["farm_naming"] != "unsure":
            problem = "an unsure FARM row has farm_naming unsure"
        elif r["scheme"] == "FARM_v5" and status == "not_required" and r["farm_naming"] not in ("related_resource", "not_named"):
            problem = "a not_required FARM row is related_resource or not_named"
        elif r["farm_naming"] and r["scheme"] != "FARM_v5":
            problem = "farm_naming is only filled on FARM_v5 rows"
        elif r["scheme"] == "FARM_v5" and not r["farm_naming"]:
            problem = "farm_naming must be filled on every FARM_v5 row"
        elif r["how_checked"] == "unsure" and not scheme_question:
            problem = "how_checked is unsure, but open_questions.md has no line naming the indicator and the scheme"
        elif r["farm_naming"] == "named_with_threshold" and not r["number_in_requirement"].strip():
            problem = "named_with_threshold needs the number in number_in_requirement"
        if problem:
            problems.setdefault("crosswalk.csv", f"line {number}: {problem}")
    evidence = {r["evidence_key"]: r for _, r in tables["evidence_since_2021.csv"]}
    for number, r in tables["evidence_since_2021.csv"]:
        for iid in filter(None, (x.strip() for x in r["indicator_ids"].split(";"))):
            if iid not in indicators:
                problems.setdefault("evidence_since_2021.csv", f"line {number}: unknown indicator {iid}")
        if r["kind"] != "maker_page" and not re.fullmatch(r"20(2[1-9])", r["year"]):
            problems.setdefault("evidence_since_2021.csv", f"line {number}: a study or review must be from 2021 or later")
        if not (ROOT / "1_sources" / r["source_file"]).name == r["source_file"]:
            problems.setdefault("evidence_since_2021.csv", f"line {number}: source_file must be a file name in 1_sources")
    for number, r in tables["sensor_coverage.csv"]:
        keys = [k.strip() for k in r["since_2021_evidence"].split(";") if k.strip()]
        for k in keys:
            if k not in evidence:
                problems.setdefault("sensor_coverage.csv", f"line {number}: since_2021_evidence cites unknown key {k}")
            elif r["indicator_id"] not in [x.strip() for x in evidence[k]["indicator_ids"].split(";")]:
                problems.setdefault("sensor_coverage.csv",
                                    f"line {number}: evidence {k} does not list {r['indicator_id']} in its indicator_ids")
        if r["since_2021_grade"] in ("validated_commercial", "commercial_unvalidated", "research_demonstrated") and not keys:
            problems.setdefault("sensor_coverage.csv", f"line {number}: a since 2021 grade above proposed needs evidence keys")
        since_line = any(c[2].startswith(r["indicator_id"]) and c[3] == "sensor evidence since 2021"
                         for c in ([x.strip() for x in l.split("|")] for l in open_questions.splitlines()) if len(c) > 4)
        if r["since_2021_grade"] == "unsure" and not since_line:
            problems.setdefault("sensor_coverage.csv", f"line {number}: since_2021_grade is unsure but has no open question")

    stygar_rows = {p["row"]: p for p in stygar}
    links = tables["product_links.csv"]
    if sorted(int(r["appendix_row"]) for _, r in links) != sorted(stygar_rows):
        problems.setdefault("product_links.csv", "the rows are not exactly the 129 products of the Stygar list")
    for number, r in links:
        p = stygar_rows.get(int(r["appendix_row"]))
        if p is None:
            continue
        problem = None
        if (r["vendor"], r["product"], r["link_2021"]) != (p["provider"], p["name"], p["link"]):
            problem = "vendor, product or link_2021 differs from the Stygar list"
        elif (r["current_link_shows"] == "none_found") != (not r["current_link"].strip()):
            problem = "current_link must be empty exactly when current_link_shows is none_found"
        elif r["current_link"].strip() and not r["current_link"].startswith("http"):
            problem = "current_link is not a web address"
        elif r["current_link_shows"] in ("product_page", "related_page") and not r["page_says"].strip():
            problem = "a product_page or related_page row must quote what the page says in page_says"
        elif r["link_2021_today"] in ("works", "moved") and r["current_link_shows"] != "product_page":
            problem = "a link that works or moved must open a page naming this exact product (product_page)"
        elif r["current_link_shows"] == "related_page" and not r["notes"].strip():
            problem = "a related_page row must say in notes what the page names instead"
        elif not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["checked"]):
            problem = "checked must be a date written YYYY-MM-DD"
        if problem:
            problems.setdefault("product_links.csv", f"line {number}: {problem}")
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
