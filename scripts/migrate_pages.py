#!/usr/bin/env python3
from pathlib import Path
import yaml
import re

SRC_DIR = Path("source")
DST_DIR = Path("hugo/content")

DST_DIR.mkdir(parents=True, exist_ok=True)

FRONTMATTER_RE = re.compile(
    r"\A---\s*\n(.*?)\n---\s*\n",
    re.DOTALL
)

def parse_frontmatter(text):
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    meta = yaml.safe_load(match.group(1)) or {}
    body = text[match.end():].lstrip("\n")
    return meta, body

def map_metadata(meta):
    hugo = {}

    if "title" in meta:
        hugo["title"] = meta["title"]

    if "date" in meta:
        hugo["date"] = meta["date"]

    if "author" in meta:
        hugo["author"] = meta["author"]

    if "redirect" in meta:
        hugo["aliases"] = [f"/{r.strip('/')}/" for r in meta["redirect"]]

    # páginas fixas no Hugo
    hugo["layout"] = "page"

    return hugo

def migrate_file(src):
    raw = src.read_text(encoding="utf-8")

    meta, body = parse_frontmatter(raw)
    hugo_meta = map_metadata(meta)

    frontmatter = "---\n"
    frontmatter += yaml.safe_dump(
        hugo_meta,
        sort_keys=False,
        allow_unicode=True
    )
    frontmatter += "---\n\n"

    out = DST_DIR / src.name
    out.write_text(frontmatter + body, encoding="utf-8")

    print(f"[OK] {src.name}")

def main():
    for md in SRC_DIR.glob("*.md"):
        migrate_file(md)

if __name__ == "__main__":
    main()