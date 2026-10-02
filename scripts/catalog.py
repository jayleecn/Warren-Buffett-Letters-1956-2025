#!/usr/bin/env python3
"""Validate the document catalog and render its human-readable index."""
import argparse
import collections
import datetime
import json
from pathlib import Path
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
README_FILES = ("README.md", "README.zh-CN.md")
SOURCE_MARKERS = {
    "gurufocus": "gurufocus.com",
    "ivey": "ivey.uwo.ca",
    "rbcpa": "rbcpa.com",
    "epub": "1965-2012_Berkshire_Hathaway_Letters_to_Shareholders.epub",
    "berkshire": "berkshirehathaway.com",
}


def link(label, path):
    # Encode parentheses/spaces so filenames remain valid Markdown destinations.
    return f"[{label}]({quote(path, safe='/')})"


def validate(documents):
    ids, paths = set(), set()
    for doc in documents:
        if doc["id"] in ids:
            raise ValueError(f"Duplicate document: {doc['id']}")
        ids.add(doc["id"])
        if doc["primary"] != (doc["author"] == "Warren E. Buffett"):
            raise ValueError(f"Primary-author mismatch: {doc['id']}")
        if doc["fiscal_year"] != int(doc["id"][:4]):
            raise ValueError(f"Fiscal-year mismatch: {doc['id']}")
        date = doc["signing_date"]
        precision = doc["signing_date_precision"]
        expected_date = date.replace("-", "")
        if precision == "day":
            datetime.date.fromisoformat(date)
        elif precision == "month":
            if not re.fullmatch(r"\d{4}-\d{2}", date):
                raise ValueError(f"Invalid month: {date}")
            datetime.date.fromisoformat(date + "-01")
        else:
            raise ValueError(f"Unknown date precision: {precision}")
        filename_date = re.search(r"_(\d{6}(?:\d{2})?)(?:_|$)", doc["id"])
        if filename_date is None or filename_date.group(1) != expected_date:
            raise ValueError(f"Filename-date mismatch: {doc['id']}")
        for field, folder, suffix in (("markdown_path", "letters-en-md", ".md"), ("pdf_path", "letters-en-pdf", ".pdf")):
            path = doc[field]
            candidate = Path(path)
            if candidate.is_absolute() or ".." in candidate.parts or candidate.parts[0] != folder:
                raise ValueError(f"Invalid document path: {path}")
            if candidate.suffix != suffix or candidate.stem != doc["id"]:
                raise ValueError(f"Invalid document filename: {path}")
            if path in paths or not (ROOT / path).is_file():
                raise ValueError(f"Missing/duplicate document file: {path}")
            if ("non-buffett" in candidate.parts) == doc["primary"]:
                raise ValueError(f"Author-directory mismatch: {path}")
            paths.add(path)
        for source in doc["source_paths"]:
            candidate = Path(source)
            if candidate.is_absolute() or ".." in candidate.parts or not (ROOT / candidate).is_file():
                raise ValueError(f"Missing/invalid source file: {source}")
        if doc["primary"] and doc["source_group"] not in SOURCE_MARKERS:
            raise ValueError(f"Unknown source group: {doc['id']}")
    actual = {str(p.relative_to(ROOT)) for folder, suffix in (("letters-en-md", "*.md"), ("letters-en-pdf", "*.pdf")) for p in (ROOT / folder).rglob(suffix)}
    if paths != actual:
        raise ValueError(f"Catalog/file mismatch: {sorted(paths ^ actual)}")


def source_cell(doc):
    source = doc.get("source_url")
    if source:
        return link("Original source", source) if not source.startswith("http") else f"[Original source]({source})"
    sources = doc["source_paths"]
    return link("Local source", sources[0]) if sources else "Not recorded"


def render_index(documents):
    primary = [d for d in documents if d["primary"]]
    other = [d for d in documents if not d["primary"]]
    lines = ["# Warren Buffett Letters — Index", "", f"Total: {len(primary)} Buffett documents; {len(other)} non-Buffett documents listed separately below.", "",
             "Generated from [catalog.json](catalog.json). Update the catalog, then run `python3 scripts/catalog.py --write`; verify with `python3 scripts/catalog.py --check`.", "",
             "Fiscal year and signing date are different fields. A month-only signing date is intentionally not expanded to a guessed day; date notes are recorded in the catalog and explained in the README.", "",
             "| # | Fiscal Year | Document / Markdown | PDF | Summary | Signing Date | Source |",
             "|---|---|---|---|---|---|---|"]
    for number, doc in enumerate(primary, 1):
        summary = doc["summary"].replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {number} | {doc['fiscal_year']} | {link(doc['id'], doc['markdown_path'])} | {link('PDF', doc['pdf_path'])} | {summary} | {doc['signing_date']} | {source_cell(doc)} |")
    lines.extend(["", "## Non-Buffett documents", "", f"These {len(other)} documents are excluded from the {len(primary)}-document Buffett count.", "",
                  "| Author | Fiscal Year | Document / Markdown | PDF | Signing Date | Source |", "|---|---|---|---|---|---|"])
    for doc in other:
        lines.append(f"| {doc['author']} | {doc['fiscal_year']} | {link(doc['id'], doc['markdown_path'])} | {link('PDF', doc['pdf_path'])} | {doc['signing_date']} | {source_cell(doc)} |")
    return "\n".join(lines) + "\n"


def render_readme_counts(text, counts):
    lines = text.splitlines()
    for group, marker in SOURCE_MARKERS.items():
        matches = [i for i, line in enumerate(lines) if line.startswith("| ") and marker in line and re.search(r"\| \d+ \|", line)]
        if len(matches) != 1:
            raise ValueError(f"Expected one README source-count row: {group}")
        i = matches[0]
        lines[i] = re.sub(r"\| \d+ \|", f"| {counts[group]} |", lines[i], count=1)
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--check", action="store_true", help="validate paths, metadata and generated documents")
    action.add_argument("--write", action="store_true", help="regenerate INDEX.md and both README source counts")
    action.add_argument("--year", type=int, help="print JSON records for one fiscal year")
    action.add_argument("--date", help="print JSON records for one signing date (YYYY-MM-DD or YYYY-MM)")
    args = parser.parse_args()
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    if catalog["schema_version"] != 1:
        raise ValueError("Unsupported catalog schema")
    documents = catalog["documents"]
    validate(documents)
    if args.year is not None or args.date is not None:
        matches = [d for d in documents if d["fiscal_year"] == args.year] if args.year is not None else [d for d in documents if d["signing_date"] == args.date]
        print(json.dumps(matches, ensure_ascii=False, indent=2))
        return
    primary = [d for d in documents if d["primary"]]
    counts = collections.Counter(d["source_group"] for d in primary)
    generated = {"INDEX.md": render_index(documents)}
    for name in README_FILES:
        generated[name] = render_readme_counts((ROOT / name).read_text(encoding="utf-8"), counts)
    for name, body in generated.items():
        path = ROOT / name
        if args.write:
            path.write_text(body, encoding="utf-8")
        elif path.read_text(encoding="utf-8") != body:
            raise ValueError(f"Generated document is stale: {name}; run --write")
    print(f"Catalog OK: {len(primary)} Buffett + {len(documents) - len(primary)} non-Buffett documents; all Markdown/PDF pairs exist.")


if __name__ == "__main__":
    main()
