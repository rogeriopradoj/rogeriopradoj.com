#!/usr/bin/env python3
import os
import re
import shutil
import yaml
from datetime import datetime
from pathlib import Path

SCULPIN_POSTS = Path("source/_posts")
HUGO_POSTS = Path("hugo/content/posts")

# ------------------------
# Utils
# ------------------------

def clean_hugo_posts():
    if HUGO_POSTS.exists():
        shutil.rmtree(HUGO_POSTS)
    HUGO_POSTS.mkdir(parents=True, exist_ok=True)


def split_front_matter(raw: str):
    if not raw.startswith("---"):
        return None, raw

    parts = raw.split("---", 2)
    fm = yaml.safe_load(parts[1])
    body = parts[2].lstrip()
    return fm, body


def normalize_assets(content: str) -> str:
    # assets -> /assets
    content = re.sub(r'(?<!/)assets/', '/assets/', content)
    return content


def fix_html_caption_spacing(content: str) -> str:
    patterns = [
        r'(</iframe>)\n(\*.+?\*)',
        r'(<img[^>]+>)\n(\*.+?\*)',
    ]
    for p in patterns:
        content = re.sub(p, r'\1\n\n\2', content, flags=re.DOTALL)
    return content


def extract_date_and_slug(filename: str):
    """
    2019-09-30-metodo-1+3---slug.md
    """
    m = re.match(r'(\d{4}-\d{2}-\d{2})-(.+)\.md$', filename)
    if not m:
        raise ValueError(f"Nome inválido: {filename}")

    date = datetime.strptime(m.group(1), "%Y-%m-%d")
    slug = m.group(2)
    return date, slug


def build_hugo_front_matter(fm, date, slug):
    return {
        "title": fm.get("title"),
        "date": date.strftime("%Y-%m-%d %H:%M:%S"),
        "categories": fm.get("categories", []),
        "tags": fm.get("tags", []),
        "slug": slug,
        "url": f"/{date:%Y/%m/%d}/{slug}/",
        "draft": False,
    }


# ------------------------
# Main migration
# ------------------------

def migrate():
    clean_hugo_posts()

    for src in SCULPIN_POSTS.glob("*.md"):
        raw = src.read_text(encoding="utf-8")

        fm, body = split_front_matter(raw)
        if not fm:
            print(f"⚠️  Sem front matter: {src.name}")
            continue

        date, slug = extract_date_and_slug(src.name)

        body = normalize_assets(body)
        body = fix_html_caption_spacing(body)

        hugo_fm = build_hugo_front_matter(fm, date, slug)

        dest = HUGO_POSTS / src.name
        with dest.open("w", encoding="utf-8") as f:
            f.write("---\n")
            yaml.dump(hugo_fm, f, sort_keys=False, allow_unicode=True)
            f.write("---\n\n")
            f.write(body)

        print(f"✅ {src.name}")

    print("\n🎉 Migração concluída com sucesso.")


if __name__ == "__main__":
    migrate()