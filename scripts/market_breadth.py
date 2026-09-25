"""Count, for each indicator, the Stygar appendix products whose stated aim names the measurement.

Reads the keywords in data/sensor_coverage.csv (market_keywords, separated by ;),
matches them without regard to case against the AIM column of Appendix table 1 in
corpus/stygar_2021_supplementary.xlsx, and writes the count into market_breadth.
Prints the matching product names for each indicator so the count can be checked.
Standard library only; the spreadsheet is parsed as a zip of XML.

    python scripts/market_breadth.py            fill every row that has keywords
    python scripts/market_breadth.py I001 I008  restrict to named indicators
"""
import csv
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "corpus" / "stygar_2021_supplementary.xlsx"
COVERAGE = ROOT / "data" / "sensor_coverage.csv"
M = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"


def appendix_rows():
    z = zipfile.ZipFile(XLSX)
    shared = ["".join(t.text or "" for t in si.iter(M + "t")) for si in ET.fromstring(z.read("xl/sharedStrings.xml"))]
    root = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
    rows = []
    for row in root.iter(M + "row"):
        d = {}
        for c in row.iter(M + "c"):
            ref = re.match(r"([A-Z]+)", c.get("r")).group(1)
            v = c.find(M + "v")
            if v is not None:
                d[ref] = shared[int(v.text)] if c.get("t") == "s" else v.text
        name = (d.get("A") or "").strip()
        if name and name != "NAME" and name != "129" and not name.startswith("Number of"):
            rows.append({"name": d.get("A", ""), "provider": d.get("B", ""), "aim": d.get("E", "")})
    return rows


def main(argv):
    products = appendix_rows()
    print(f"appendix products: {len(products)}")
    with COVERAGE.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        header, rows = list(reader.fieldnames), list(reader)
    only = set(argv)
    for r in rows:
        if only and r["indicator_id"] not in only:
            continue
        keys = [k.strip().lower() for k in r["market_keywords"].split(";") if k.strip()]
        if not keys:
            continue
        hits = [p for p in products if any(k in p["aim"].lower() for k in keys)]
        r["market_breadth"] = str(len(hits))
        print(f"\n{r['indicator_id']} keywords {keys}: {len(hits)}")
        for p in hits:
            print(f"   {p['provider']} | {p['name']} | {p['aim'][:70]}")
    with COVERAGE.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main(sys.argv[1:])
