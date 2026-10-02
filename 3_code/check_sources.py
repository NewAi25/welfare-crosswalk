"""CHECK SOURCES: prove that every document in 1_sources is exactly the one the research read.

In plain words
    1_sources/manifest.csv lists every source document with the web address its file came
    from and a fingerprint (a SHA256 hash: a long code computed from the file's bytes; if
    one character of the file changes, the fingerprint changes completely). This script
    recomputes the fingerprints and compares them, so anyone can confirm they are reading
    the identical file. Documents not stored here (in_repository = no), for licence or privacy
    reasons, can be downloaded from their link and saved in 1_sources/ under the file name
    given. For an ordinary file this script then confirms the copy is byte for byte identical.
    For the one paper whose publisher stamps every download with the date, time and
    downloader's IP address (kind binary_stamped), it compares the text with the stamp lines
    removed. For the two web pages saved as text (kind text), a fresh copy cannot match; the
    network check confirms only that the live page still contains a set phrase.

Technical detail follows.


1_sources/manifest.csv records, for each file, the exact URL its bytes came from
and the SHA256 of those bytes. This script checks three things:

  1. the local file exists and its SHA256 matches the manifest; for a binary_stamped row
     whose bytes differ, its text with the stamp lines removed must match text_sha256
     (needs pypdf); for a text row (a saved web page) whose copy is absent or differs, the
     snapshot cannot be compared, so the network check looks for the check phrase on the
     live page instead;
  2. the URL is live, and for binary files the bytes it serves today hash to
     the same value, so the link points at exactly the document in 1_sources.
     Some publishers stamp every download with the date and IP address, so the
     bytes differ each time; those rows have kind "binary_stamped" and are
     compared on their extracted text with the stamp lines removed (needs pypdf);
  3. for pasted text files, the URL is live and the recorded check phrase
     appears in the local file.

A URL that answers without a PDF (a bot protection page, a login page) is a
WARN, not a FAIL: the link is not proven, and must be opened in a browser.

    python 3_code/check_sources.py                 verify everything, exit 1 on any FAIL
    python 3_code/check_sources.py --local         local check only (hash, or stamped text), no network
    python 3_code/check_sources.py --record        write current local hashes into the manifest
    python 3_code/check_sources.py --only a.pdf b.pdf   restrict to named files

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
CORPUS = ROOT / "1_sources"
MANIFEST = CORPUS / "manifest.csv"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
KEVIN_FILES = {"kevin_item_13.md", "kevin_slack_2026-09-25.md", "kevin_call_2026-09-22.md"}
FIELDS = ["filename", "title", "used_for", "licence", "in_repository", "kind", "url", "zip_member", "check_phrase",
          "sha256", "text_sha256", "retrieved", "status", "doi_or_landing"]
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
    try:
        reader = PdfReader(io.BytesIO(data))
        lines = []
        for page in reader.pages:
            for line in (page.extract_text() or "").splitlines():
                if not STAMP.search(line):
                    lines.append(re.sub(r"\s+", " ", line).strip())
    except Exception as e:  # a damaged or non PDF file is reported, not a crash
        raise ValueError(f"could not read the PDF text: {e}")
    return sha256("\n".join(lines).encode("utf-8"))


def load_manifest():
    with MANIFEST.open(newline="", encoding="utf-8-sig") as f:
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
    if r["kind"] not in ("binary", "binary_stamped", "text"):
        return "FAIL", f"unknown kind {r['kind']!r}"
    if r["status"] == "missing":
        return "missing", "not downloaded, needs a browser (see 1_sources/README.md)"
    browser_note = ""
    if r["status"] == "browser_only" and network:
        network = False
        browser_note = "; source refuses scripted requests, retrieved in a browser, so only the local hash is checked"
    if r["kind"] == "text" and not r["check_phrase"]:
        return "FAIL", "text source with no check phrase"
    if r["kind"] == "text" and (not path.exists() or sha256(path.read_bytes()) != r["sha256"]):
        # A saved web page: a copy saved today cannot match the snapshot, so check the live page.
        if not network:
            return "absent", "saved web page not here or not the snapshot; run without --local to check the live page"
        try:
            status, remote = fetch(r["url"])
        except Exception as e:
            return "WARN", f"url not reachable: {e}"
        if r["check_phrase"].encode("utf-8") in remote:
            return "ok", "live page contains the check phrase; the snapshot itself was not compared"
        return "WARN", "url live but the check phrase no longer appears on the page"
    if not path.exists():
        if r.get("in_repository") == "no":
            return "absent", "not stored here (licence or privacy); download it from the url to check it"
        return "FAIL", "file not in 1_sources/"
    local = path.read_bytes()
    if not r["sha256"]:
        return "FAIL", "no sha256 recorded; run --record"
    if sha256(local) != r["sha256"]:
        if r["kind"] != "binary_stamped":
            return "FAIL", "local file has changed since the manifest was recorded"
        # A fresh download of a stamped paper carries a new stamp, so compare the text without it.
        if not local.startswith(b"%PDF"):
            return "FAIL", "stamped file is not a PDF"
        try:
            local_text = pdf_text_hash(local)
        except ValueError as e:
            return "FAIL", str(e)
        if local_text is None:
            return "WARN", "stamped download; pypdf not installed, so the text could not be compared"
        if not r["text_sha256"]:
            return "FAIL", "stamped download; no text_sha256 recorded, run --record"
        if local_text != r["text_sha256"]:
            return "FAIL", "the document text differs from the one the research read"
        if not network:
            return "ok", "stamped copy; the document text, without the stamp, matches the manifest"
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
            try:
                remote_hash = pdf_text_hash(remote)
            except ValueError as e:
                return "FAIL", f"url serves a file whose text could not be read: {e}"
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
        unknown = names - {r["filename"] for r in rows}
        if unknown:
            print(f"not in the manifest: {' '.join(sorted(unknown))}")
            return 1
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
                if r["status"] in ("", "missing"):
                    r["status"] = "ok"  # keep browser_only: those sites refuse scripted downloads
        save_manifest(rows)
        print(f"recorded hashes for {sum(1 for r in rows if r['sha256'])} files")
        return 0
    network = "--local" not in argv
    failures = 0
    listed = {r["filename"] for r in rows} | {"README.md", "manifest.csv"}
    for path in sorted(CORPUS.iterdir()):
        if path.is_file() and path.name not in listed and path.name not in KEVIN_FILES:
            failures += 1
            print(f"{'FAIL':8} {path.name:40} in 1_sources but not in the manifest")
    for r in rows_to_check:
        verdict, why = check_row(r, network)
        failures += verdict == "FAIL"
        print(f"{verdict:8} {r['filename']:40} {why}")
    print(f"\n{len(rows_to_check)} entries, {failures} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
