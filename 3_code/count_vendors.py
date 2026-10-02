"""COUNT VENDORS: how many products on the market say they measure each welfare indicator.

In plain words
    Stygar et al. 2021 listed 129 sensor products sold for dairy cows. For each product
    they copied the vendor's own one line description of what it does (the AIM column of
    their spreadsheet). For each welfare indicator we wrote down a few search words in
    2_research/sensor_coverage.csv (column search_words). This script counts how many of
    the 129 descriptions contain at least one of those words and compares the count with
    the column vendors_naming_it. It saves a new count only when asked to with --write.

Where the inputs come from
    1_sources/stygar_2021_supplementary.xlsx, sheet 1, column E (AIM). Only column E is
    searched, never the product name, the sensor type or the web link.

How to check it by hand, without running anything
    Open the spreadsheet in Excel, select column E, use Find (Ctrl+F) for each search word
    of a row, and count the products that match at least one word. Upper and lower case
    are treated the same. The count must equal vendors_naming_it.

How to run it
    python 3_code/count_vendors.py                  compare every stored count with a fresh count
    python 3_code/count_vendors.py I001 I008        compare only these rows
    python 3_code/count_vendors.py --write I027     save the fresh count for these rows
    It prints the matching products for each row, so the count can be compared by eye.
    Without --write it changes nothing, so it is safe to run when checking someone else's work.

Other scripts import appendix_products() and names_it() from here, so the matrix in the
Excel file and this count always use the same matching rule.
"""
import csv
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
SPREADSHEET = ROOT / "1_sources" / "stygar_2021_supplementary.xlsx"
SENSOR_TABLE = ROOT / "2_research" / "sensor_coverage.csv"
XML = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"


def appendix_products():
    """Return the 129 products from sheet 1 of the Stygar spreadsheet, in spreadsheet order.

    The spreadsheet's first row is the column headings and its last filled row is a total
    ("Number of providers"); both are left out, leaving exactly 129 products.
    """
    book = zipfile.ZipFile(SPREADSHEET)
    shared = ["".join(t.text or "" for t in s.iter(XML + "t"))
              for s in ET.fromstring(book.read("xl/sharedStrings.xml"))]
    products = []
    for row in ET.fromstring(book.read("xl/worksheets/sheet1.xml")).iter(XML + "row"):
        cells = {}
        for cell in row.iter(XML + "c"):
            column = re.match(r"[A-Z]+", cell.get("r")).group()
            value = cell.find(XML + "v")
            if value is not None:
                cells[column] = shared[int(value.text)] if cell.get("t") == "s" else value.text
        name = (cells.get("A") or "").strip()
        if not name or name in ("NAME", "129") or name.startswith("Number of"):
            continue
        provider = (cells.get("B") or "").strip()
        products.append({
            "row": int(row.get("r")), "name": name, "provider": provider,
            "key": f"{provider}|{name}", "link": (cells.get("C") or "").strip(),
            "sensor_type": (cells.get("D") or "").strip(), "aim": (cells.get("E") or "").strip(),
            "country": (cells.get("F") or "").strip(), "has_study": (cells.get("G") or "").strip(),
        })
    if len(products) != 129:
        raise SystemExit(f"expected 129 products in the Stygar spreadsheet, found {len(products)}")
    return products


def search_words(text):
    """Split the search_words cell on ';' into lower case words."""
    return [w.strip().lower() for w in (text or "").split(";") if w.strip()]


def names_it(product, words):
    """True when the product's AIM text contains any of the words, ignoring case."""
    aim = product["aim"].lower()
    return any(w in aim for w in words)


def main(argv):
    write = "--write" in argv
    only = {a for a in argv if a != "--write"}
    products = appendix_products()
    print(f"products in the Stygar list: {len(products)}")
    with SENSOR_TABLE.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        header, rows = list(reader.fieldnames), list(reader)
    mismatches = []
    for r in rows:
        if only and r["indicator_id"] not in only:
            continue
        words = search_words(r["search_words"])
        if not words:
            continue
        hits = [p for p in products if names_it(p, words)]
        stored = r["vendors_naming_it"]
        if stored != str(len(hits)):
            mismatches.append(r["indicator_id"])
        r["vendors_naming_it"] = str(len(hits))
        print(f"\n{r['indicator_id']} search words {words}: {len(hits)} (stored: {stored or 'empty'})")
        for p in hits:
            print(f"   {p['provider']} | {p['name']} | {p['aim'][:70]}")
    if write:
        with SENSOR_TABLE.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=header, lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
        print(f"\nsaved the fresh counts to {SENSOR_TABLE.relative_to(ROOT)}")
        return 0
    if mismatches:
        print(f"\nstored count differs from a fresh count for: {' '.join(mismatches)}")
        return 1
    print("\nevery stored count matches a fresh count")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
