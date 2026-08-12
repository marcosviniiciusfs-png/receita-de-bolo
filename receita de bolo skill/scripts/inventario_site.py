#!/usr/bin/env python3
"""
Inventaria uma pasta de cliente para reconstruir site.

Uso:
  python inventario_site.py .
  python inventario_site.py "C:/caminho/da/pasta"
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

TEXT_EXTENSIONS = {".txt", ".md", ".csv", ".json", ".rtf", ".html", ".htm", ".tsx", ".ts", ".jsx", ".js"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".avif", ".svg"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".webm", ".avi"}

KEYWORDS = {
    "whatsapp": re.compile(r"(wa\.me|api\.whatsapp\.com|whatsapp|wpp|zap|\+?55|\(?\d{2}\)?\s?\d{4,5}[-\s]?\d{4})", re.I),
    "location": re.compile(r"(endereco|endereço|localizacao|localização|cidade|bairro|rua|avenida|av\.|estado|atendimento)", re.I),
    "social_proof": re.compile(r"(cliente|contemplado|depoimento|resultado|case|prova social|print|entrega|avaliacao|avaliação)", re.I),
    "benefits": re.compile(r"(beneficio|benefício|diferencial|vantagem|garantia|seguranca|segurança|rapido|rápido|transparente)", re.I),
    "form": re.compile(r"(formulario|formulário|simulador|pergunta|lead|webhook|api|obrigado|thank)", re.I),
}

PHONE_RE = re.compile(r"(?:\+?55\s*)?(?:\(?\d{2}\)?\s*)?\d{4,5}[-\s]?\d{4}")
WHATSAPP_LINK_RE = re.compile(r"https?://(?:wa\.me|api\.whatsapp\.com)[^\s\"')<>]+", re.I)


def safe_read(path: Path, limit: int = 250_000) -> str:
    try:
        data = path.read_bytes()[:limit]
    except OSError:
        return ""

    for encoding in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            return data.decode(encoding, errors="ignore")
        except UnicodeError:
            continue
    return ""


def normalize_phone(raw: str) -> str:
    digits = re.sub(r"\D+", "", raw)
    if len(digits) in (10, 11):
        return "55" + digits
    return digits


def classify_path(path: Path) -> list[str]:
    haystack = str(path).lower()
    tags: list[str] = []
    if any(term in haystack for term in ("cliente", "contemplado", "depoimento", "resultado", "print")):
        tags.append("prova_social")
    if any(term in haystack for term in ("logo", "marca", "brand")):
        tags.append("logo_marca")
    if any(term in haystack for term in ("nota", "anot", "texto", "conteudo", "conteúdo")):
        tags.append("notas_conteudo")
    if any(term in haystack for term in ("whatsapp", "wpp", "zap", "contato", "telefone")):
        tags.append("contato")
    if any(term in haystack for term in ("endereco", "endereço", "localizacao", "localização", "cidade")):
        tags.append("localizacao")
    return tags


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not root.exists():
        print(json.dumps({"error": f"Pasta nao encontrada: {root}"}, ensure_ascii=False, indent=2))
        return 1

    result = {
        "root": str(root),
        "folders_of_interest": [],
        "text_files": [],
        "images": [],
        "videos": [],
        "possible_whatsapp_links": [],
        "possible_phone_numbers": [],
        "matches": {key: [] for key in KEYWORDS},
        "recommended_next_steps": [
            "Confirmar nome da marca e oferta principal.",
            "Confirmar WhatsApp final antes de publicar.",
            "Usar imagens reais encontradas antes de buscar imagens externas.",
            "Preservar APIs, webhooks, pixels e dominios existentes.",
        ],
    }

    phones: set[str] = set()
    links: set[str] = set()

    for path in root.rglob("*"):
        if any(part.startswith(".git") or part == "node_modules" or part == "dist" for part in path.parts):
            continue

        rel = path.relative_to(root)
        tags = classify_path(rel)

        if path.is_dir():
            if tags:
                result["folders_of_interest"].append({"path": str(rel), "tags": tags})
            continue

        suffix = path.suffix.lower()
        item = {"path": str(rel), "tags": tags}

        if suffix in IMAGE_EXTENSIONS:
            result["images"].append(item)
            continue

        if suffix in VIDEO_EXTENSIONS:
            result["videos"].append(item)
            continue

        if suffix not in TEXT_EXTENSIONS:
            continue

        text = safe_read(path)
        result["text_files"].append(item)

        for link in WHATSAPP_LINK_RE.findall(text):
            links.add(link)

        for phone in PHONE_RE.findall(text):
            normalized = normalize_phone(phone)
            if len(normalized) >= 10:
                phones.add(normalized)

        for key, pattern in KEYWORDS.items():
            if pattern.search(text) or pattern.search(str(rel)):
                snippets = []
                for match in pattern.finditer(text):
                    start = max(0, match.start() - 70)
                    end = min(len(text), match.end() + 90)
                    snippet = re.sub(r"\s+", " ", text[start:end]).strip()
                    snippets.append(snippet)
                    if len(snippets) >= 3:
                        break
                result["matches"][key].append({"path": str(rel), "snippets": snippets})

    result["possible_whatsapp_links"] = sorted(links)
    result["possible_phone_numbers"] = sorted(phones)

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
