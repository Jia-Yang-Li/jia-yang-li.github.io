#!/usr/bin/env python3
"""Generate _bibliography/papers.bib from _data/publications.yml.

The publication list is edited as a simple form (title, authors, venue, ...).
The theme renders publications from BibTeX, so the deploy and preview
workflows run this script before the Jekyll build.
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_data" / "publications.yml"
TARGET = ROOT / "_bibliography" / "papers.bib"

STATUSES = {"published", "preprint", "under_review"}


def text(value):
    """Return a trimmed string; empty for missing values."""
    return "" if value is None else str(value).strip()


def escape(value):
    """Escape the characters BibTeX treats specially in field values."""
    for char in "&%#_":
        value = value.replace(char, "\\" + char)
    return value


def bibtex_author(name):
    """Turn 'First Middle Last' into 'Last, First Middle'."""
    name = name.strip()
    if "," in name or " " not in name:
        return name
    first, last = name.rsplit(" ", 1)
    return f"{last}, {first}"


def split_authors(value):
    """Accept authors separated by commas, semicolons, 'and', or Chinese commas."""
    parts = re.split(r"\s*(?:,|;|，|、|\band\b)\s*", value)
    return [part for part in (p.strip() for p in parts) if part]


def make_key(authors, year, title, used):
    last = bibtex_author(authors[0]).split(",")[0] if authors else "paper"
    word = next((w for w in re.findall(r"[A-Za-z]+", title) if len(w) > 3), "paper")
    base = re.sub(r"[^a-z0-9]", "", f"{last}{year}{word}".lower()) or "paper"
    key, n = base, 2
    while key in used:
        key, n = f"{base}{n}", n + 1
    used.add(key)
    return key


def entry(item, index, used):
    title = text(item.get("title"))
    authors = split_authors(text(item.get("authors")))
    year = text(item.get("year"))
    if not title or not authors or not year:
        raise ValueError(f"publication #{index}: title, authors and year are required")

    status = text(item.get("status")) or "published"
    if status not in STATUSES:
        raise ValueError(f"publication #{index}: unknown status '{status}'")

    venue = text(item.get("venue"))
    abbr = text(item.get("abbr"))
    arxiv = text(item.get("arxiv"))
    doi = text(item.get("doi"))
    kind = text(item.get("type")) or "journal"

    if status == "under_review":
        venue, abbr, kind = "Under review", "", "journal"
    elif status == "preprint":
        venue = venue or (f"arXiv preprint arXiv:{arxiv}" if arxiv else "Preprint")
        abbr = abbr or ("arXiv" if arxiv else "")
        kind = "journal"
    elif not venue:
        raise ValueError(f"publication #{index}: a published paper needs a venue")

    fields = []
    if abbr:
        fields.append(("abbr", abbr))
    if status == "published":
        fields.append(("bibtex_show", "true"))
    fields.append(("title", escape(title)))
    fields.append(("author", " and ".join(bibtex_author(a) for a in authors)))
    fields.append(("booktitle" if kind == "conference" else "journal", escape(venue)))
    fields.append(("year", year))
    if doi:
        fields.append(("doi", doi))
    if arxiv:
        fields.append(("arxiv", arxiv))
    for name, source in (("html", "link"), ("code", "code")):
        if text(item.get(source)):
            fields.append((name, text(item.get(source))))

    entry_type = "inproceedings" if kind == "conference" else "article"
    key = make_key(authors, year, title, used)
    width = max(len(name) for name, _ in fields)
    body = ",\n".join(f"  {name.ljust(width)} = {{{value}}}" for name, value in fields)
    return f"@{entry_type}{{{key},\n{body}\n}}"


def main():
    data = yaml.safe_load(SOURCE.read_text(encoding="utf-8")) or {}
    items = data.get("items") or []
    used = set()
    entries = [entry(item, i, used) for i, item in enumerate(items, start=1)]
    header = "---\n---\n\n% Generated from _data/publications.yml by bin/build_bib.py. Do not edit.\n\n"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    with open(TARGET, "w", encoding="utf-8", newline="\n") as file:
        file.write(header + "\n\n".join(entries) + "\n")
    print(f"Wrote {len(entries)} publications to {TARGET.relative_to(ROOT)}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        sys.exit(f"Error in _data/publications.yml: {error}")
