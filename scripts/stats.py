"""Fill the tier column, build the adoption table and the two item #13 views.

Reads data/, writes results/adoption_table.csv, results/instrumented_not_required.csv
and results/required_manual_only.csv, and prints counts. The 0 to 3 mapping for
each factor is the one in standard/definitions.md; it is the only place a
decisions entry can change the ranking. Works on empty files. Standard library only.

    python scripts/stats.py
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA, RESULTS = ROOT / "data", ROOT / "results"
SCHEMES = ["RSPCA_Assured", "FARM_v5", "GAP_dairy", "Certified_Humane"]

GRADE = {"validated_commercial": 3, "commercial_unvalidated": 2, "research_only": 1}
HARDWARE = {"routine_data": 3, "farm_fixed": 2, "animal_mounted": 1}
NAMING = {"named_with_threshold": 3, "named": 2, "related_resource": 1}


def breadth_points(n):
    return 3 if n >= 10 else 2 if n >= 3 else 1 if n >= 1 else 0


def coverage_points(n):
    return 3 if n >= 4 else 2 if n >= 2 else 1 if n == 1 else 0


def load(name):
    with (DATA / name).open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), [r for r in reader if any((v or "").strip() for v in r.values())]


def save(path, header, rows):
    path.parent.mkdir(exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def fill_tier(header, rows):
    for r in rows:
        r["tier"] = "joined" if r["efsa_abm"] and r["wq_measure"] else "efsa_only" if r["efsa_abm"] else "wq_only"
    save(DATA / "indicators.csv", header, rows)


def main():
    ih, indicators = load("indicators.csv")
    fill_tier(ih, indicators)
    _, coverage = load("sensor_coverage.csv")
    _, crosswalk = load("crosswalk.csv")
    cov = {r["indicator_id"]: r for r in coverage}
    by_ind = defaultdict(dict)
    for r in crosswalk:
        by_ind[r["indicator_id"]][r["scheme"]] = r

    table = []
    for ind in indicators:
        iid = ind["indicator_id"]
        c = cov.get(iid, {})
        schemes = by_ind.get(iid, {})
        required = [s for s in SCHEMES if schemes.get(s, {}).get("requirement_text", "").strip()]
        farm = schemes.get("FARM_v5", {})
        naming = farm.get("industry_naming", "") or ("not_named" if "FARM_v5" in schemes else "")
        breadth = int(c["market_breadth"]) if c.get("market_breadth", "").isdigit() else 0
        points = {
            "sensor_points": GRADE.get(c.get("ai_grade", ""), 0),
            "hardware_points": HARDWARE.get(c.get("hardware_class", ""), 0),
            "breadth_points": breadth_points(breadth),
            "naming_points": NAMING.get(naming, 0),
            "coverage_points": coverage_points(len(required)),
        }
        table.append({
            "indicator_id": iid, "tier": ind["tier"], "efsa_abm": ind["efsa_abm"], "wq_measure": ind["wq_measure"],
            "ai_grade": c.get("ai_grade", ""), "hardware_class": c.get("hardware_class", ""),
            "market_breadth": breadth, "industry_naming": naming, "scheme_count": len(required),
            "schemes_requiring": " ".join(required),
            "audit_methods": " ".join(f"{s}:{schemes[s]['audit_method']}" for s in required),
            **points, "adoption_score_heuristic": sum(points.values()),
        })
    table.sort(key=lambda r: (-r["adoption_score_heuristic"], r["indicator_id"]))
    for rank, r in enumerate(table, start=1):
        r["rank"] = rank
    header = list(table[0].keys()) if table else ["indicator_id"]
    save(RESULTS / "adoption_table.csv", header, table)

    instrumented = [r for r in table if r["ai_grade"] in GRADE and r["ai_grade"] != "research_only" and r["scheme_count"] == 0]
    save(RESULTS / "instrumented_not_required.csv", header, instrumented)
    manual = []
    for r in crosswalk:
        c = cov.get(r["indicator_id"], {})
        if r["requirement_text"].strip() and r["audit_method"] == "visual_inspection" and c.get("ai_grade") == "validated_commercial":
            manual.append({"indicator_id": r["indicator_id"], "scheme": r["scheme"], "section_ref": r["section_ref"],
                           "page": r["page"], "requirement_text": r["requirement_text"], "product_ids": c.get("product_ids", "")})
    save(RESULTS / "required_manual_only.csv",
         ["indicator_id", "scheme", "section_ref", "page", "requirement_text", "product_ids"], manual)

    print(f"indicators: {len(indicators)} by tier {dict(Counter(r['tier'] for r in indicators))}")
    print(f"sensor_coverage rows: {len(coverage)} by grade {dict(Counter(r['ai_grade'] for r in coverage))}")
    print(f"  by hardware class {dict(Counter(r['hardware_class'] for r in coverage))}")
    print(f"crosswalk rows: {len(crosswalk)}, with a requirement: {sum(1 for r in crosswalk if r['requirement_text'].strip())}")
    print(f"adoption table: {len(table)} rows; scored 8 or more: {sum(1 for r in table if r['adoption_score_heuristic'] >= 8)}")
    print(f"instrumented but not required: {len(instrumented)}; required but manually audited: {len(manual)} scheme rows")
    print("the adoption score is a heuristic sort order, see standard/definitions.md")


if __name__ == "__main__":
    main()
