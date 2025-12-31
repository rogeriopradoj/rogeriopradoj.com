#!/usr/bin/env python3

import re
from pathlib import Path
from datetime import datetime

CONTENT_DIR = Path("hugo/content")
BACKUP_DIR = Path("scripts/_backup_frontmatter")

BACKUP_DIR.mkdir(parents=True, exist_ok=True)

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*", re.DOTALL)
LINK_TAG_RE = re.compile(r'<link[^>]+rel=["\']stylesheet["\'][^>]*>\n?', re.IGNORECASE)

def backup(path: Path):
    ts = datetime.now().strftime("%Y%m%d%H%M%S")
    dest = BACKUP_DIR / f"{path.name}.{ts}.bak"
    dest.write_text(path.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")

def fix_file(path: Path):
    original = path.read_text(encoding="utf-8", errors="ignore")

    # Remove múltiplos --- no topo
    parts = original.split("\n---")
    if parts[0].strip() == "" and len(parts) > 2:
        original = "---\n" + "\n---".join(parts[1:])

    m = FRONTMATTER_RE.match(original)
    if not m:
        return False

    fm = m.group(1)
    body = original[m.end():]

    changed = False
    new_fm_lines = []

    redirect_block = []
    in_redirect = False

    for line in fm.splitlines():
        # Remove layout: default
        if re.match(r"layout:\s*default\b", line):
            changed = True
            continue

        # Converter redirect: → aliases:
        if re.match(r"redirect:\s*$", line):
            in_redirect = True
            redirect_block = []
            changed = True
            continue

        if in_redirect:
            if re.match(r"\s*-\s*", line):
                redirect_block.append(line.strip().lstrip("- ").strip())
                continue
            else:
                # Finaliza bloco redirect
                if redirect_block:
                    new_fm_lines.append("aliases:")
                    for r in redirect_block:
                        new_fm_lines.append(f"  - {r}")
                in_redirect = False

        new_fm_lines.append(line)

    # Fecha redirect se terminar no fim
    if in_redirect and redirect_block:
        new_fm_lines.append("aliases:")
        for r in redirect_block:
            new_fm_lines.append(f"  - {r}")

    # Remove <link rel="stylesheet"> do corpo
    new_body, n = LINK_TAG_RE.subn("", body)
    if n > 0:
        changed = True

    if not changed:
        return False

    backup(path)

    fixed = "---\n" + "\n".join(new_fm_lines).strip() + "\n---\n" + new_body.lstrip()
    path.write_text(fixed, encoding="utf-8")

    return True

def main():
    modified = 0

    for md in CONTENT_DIR.rglob("*.md"):
        if fix_file(md):
            print(f"[FIXED] {md}")
            modified += 1

    if modified == 0:
        print("✅ Nenhum arquivo precisou de correção.")
    else:
        print(f"\n✅ Correções aplicadas em {modified} arquivos.")
        print(f"📦 Backups salvos em: {BACKUP_DIR}")

if __name__ == "__main__":
    main()