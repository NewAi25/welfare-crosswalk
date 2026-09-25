"""Verify that every corpus file is the document its manifest says it is.

corpus/manifest.csv records, for each file, the exact URL its bytes came from
and the SHA256 of those bytes. This script checks three things:

  1. the local file exists and its SHA256 matches the manifest;
  2. the URL is live, and for binary files the bytes it serves today hash to
     the same value, so the link points at exactly the document in the corpus.
     Some publishers stamp every download with the date and IP address, so the
     bytes differ each time; those rows have kind "binary_stamped" and are
     compared on their extracted text with the stamp lines removed (needs pypdf);
  3. for pasted text files, the URL is live and the recorded check phrase
     appears in the local file.

A URL that answers without a PDF (a bot protection page, a login page) is a
WARN, not a FAIL: the link is not proven, and must be opened in a browser.

    python scripts/check_corpus.py                 verify everything, exit 1 on any FAIL
    python scripts/check_corpus.py --local         hash check only, no network
    python scripts/check_corpus.py --record        write current local hashes into the manifest
    python scripts/check_corpus.py --only a.pdf b.pdf   restrict to named files

Standard library only, except pypdf for binary_stamped rows. A file with
status "missing" in the manifest is reported but does not fail the check. Status
"browser_only" marks a file retrieved by hand from a site that refuses scripted
requests; it gets the local hash check only.
"""
import csv
import hashlib
import io
import re
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
MANIFEST = CORPUS / "manifest.csv"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
FIELDS = ["filename", "kind", "url", "zip_member", "check_phrase", "sha256", "text_sha256",
          "retrieved", "status", "doi_or_landing"]
STAMP = re.compile(r"Downloaded from|IP address|subject to the Cambridge Core terms|Utrecht University Repository|"
                   r"\d{1,2} [A-Z][a-z]{2} \d{4} at \d{2}:\d{2}:\d{2}")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Referer": "https://www.google.com/"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.status, resp.read()


def pdf_text_hash(data):
    """Hash of the PDF text with download stamp lines removed. None if pypdf is absent."""
    try:
        from pypdf import PdfReader
    except ImportError:
        return None
    reader = PdfReader(io.BytesIO(data))
    lines = []
    for page in reader.pages:
        for line in (page.extract_text() or "").splitlines():
            if not STAMP.search(line):
                lines.append(re.sub(r"\s+", " ", line).strip())
    return sha256("\n".join(lines).encode("utf-8"))


def load_manifest():
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for k in FIELDS:
            r.setdefault(k, "")
    return rows


def save_manifest(rows):
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def check_row(r, network):
    path = CORPUS / r["filename"]
    if r["status"] == "missing":
        return "missing", "not downloaded, needs a browser (see corpus/README.md)"
    browser_note = ""
    if r["status"] == "browser_only" and network:
        network = False
        browser_note = "; source refuses scripted requests, retrieved in a browser, so only the local hash is checked"
    if not path.exists():
        return "FAIL", "file not in corpus/"
    local = path.read_bytes()
    if not r["sha256"]:
        return "FAIL", "no sha256 recorded; run --record"
    if sha256(local) != r["sha256"]:
        return "FAIL", "local file has changed since the manifest was recorded"
    if not network:
        return "ok", "local hash matches" + browser_note
    try:
        status, remote = fetch(r["url"])
    except Exception as e:
        return "FAIL", f"url not reachable: {e}"
    if r["kind"] in ("binary", "binary_stamped"):
        if r["zip_member"]:
            try:
                remote = zipfile.ZipFile(io.BytesIO(remote)).read(r["zip_member"])
            except Exception as e:
                return "FAIL", f"zip member {r['zip_member']} not found: {e}"
        elif path.suffix.lower() == ".pdf" and not remote.startswith(b"%PDF"):
            return "WARN", f"url answered but did not serve a PDF ({len(remote)} bytes, bot protection or login); open it in a browser to confirm"
        if sha256(remote) == r["sha256"]:
            return "ok", "url live and serves the exact same bytes"
        if r["kind"] == "binary_stamped":
            remote_hash = pdf_text_hash(remote)
            if remote_hash is None:
                return "WARN", "stamped download; pypdf not installed so the text could not be compared"
            if not r["text_sha256"]:
                return "FAIL", "stamped download; no text_sha256 recorded, run --record"
            if remote_hash == r["text_sha256"]:
                return "ok", "url live; bytes carry a per download stamp but the document text is identical"
            return "FAIL", "url serves a document whose text differs from the local copy"
        return "FAIL", f"url serves different bytes now ({len(remote)} bytes); check whether the document was revised"
    text = local.decode("utf-8", "replace")
    if r["check_phrase"] and r["check_phrase"] not in text:
        return "FAIL", "check phrase not found in the local text"
    if r["check_phrase"] and r["check_phrase"].encode("utf-8") not in remote:
        return "WARN", "url live but the check phrase no longer appears on the page"
    return "ok", "url live and check phrase present"


def main(argv):
    rows = load_manifest()
    if "--only" in argv:
        names = set(argv[argv.index("--only") + 1:])
        rows_to_check = [r for r in rows if r["filename"] in names]
    else:
        rows_to_check = rows
    if "--record" in argv:
        for r in rows_to_check:
            path = CORPUS / r["filename"]
            if path.exists():
                data = path.read_bytes()
                r["sha256"] = sha256(data)
                if r["kind"] == "binary_stamped":
                    r["text_sha256"] = pdf_text_hash(data) or ""
                r["status"] = "ok"
        save_manifest(rows)
        print(f"recorded hashes for {sum(1 for r in rows if r['sha256'])} files")
        return 0
    network = "--local" not in argv
    failures = 0
    for r in rows_to_check:
        verdict, why = check_row(r, network)
        failures += verdict == "FAIL"
        print(f"{verdict:8} {r['filename']:40} {why}")
    print(f"\n{len(rows_to_check)} entries, {failures} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
