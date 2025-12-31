#!/usr/bin/env python3

import re
from pathlib import Path

CONTENT_DIR = Path("hugo/content")

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*", re.DOTALL)
UNQUOTED_COLON_RE = re.compile(r'^(title|description|summary):\s*[^"\n].*:', re.MULTILINE)

issues = []

def audit_file(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")

    # Contagem de delimitadores ---
    fm_markers = text.count("\n---")
    if fm_markers > 2:
        issues.append((path, "Frontmatter duplicado (mais de um bloco ---)"))

    # Extrair frontmatter
    m = FRONTMATTER_RE.match(text)
    if not m:
        issues.append((path, "Frontmatter ausente ou malformado"))
        return

    fm = m.group(1)

    # layout: default (PaperMod não usa)
    if re.search(r"^layout:\s*default\b", fm, re.MULTILINE):
        issues.append((path, "layout: default (remover — PaperMod ignora)"))

    # redirect legado do Sculpin
    if re.search(r"^redirect:\b", fm, re.MULTILINE):
        issues.append((path, "redirect: encontrado (usar aliases: no Hugo)"))

    # url: geralmente desnecessário
    if re.search(r"^url:\b", fm, re.MULTILINE):
        issues.append((path, "url: definido (ver se é realmente necessário)"))

    # Títulos perigosos com :
    if UNQUOTED_COLON_RE.search(fm):
        issues.append((path, "Campo com ':' sem aspas (title/summary/description)"))

    # Datas suspeitas
    if re.search(r"^date:\s*\d{4}-\d{2}-\d{2}(?!T)", fm, re.MULTILINE):
        issues.append((path, "date sem horário ISO (recomenda-se ISO 8601 completo)"))

    # HTML indevido no corpo
    body = text[m.end():]

    if "<link " in body:
        issues.append((path, "Tag <link> no corpo do Markdown (CSS deve ir para assets/static)"))

    if "<script" in body:
        issues.append((path, "Tag <script> no corpo do Markdown"))

    if re.search(r'href="/assets/', body):
        issues.append((path, "Uso direto de /assets no Markdown (prefira static/)"))

def main():
    for md in CONTENT_DIR.rglob("*.md"):
        audit_file(md)

    if not issues:
        print("✅ Nenhum problema encontrado. Conteúdo OK.")
        return

    print("\n⚠️ PROBLEMAS ENCONTRADOS:\n")
    for path, msg in issues:
        print(f"- {path}: {msg}")

    print(f"\nTotal de arquivos com alertas: {len(set(p for p, _ in issues))}")

if __name__ == "__main__":
    main()