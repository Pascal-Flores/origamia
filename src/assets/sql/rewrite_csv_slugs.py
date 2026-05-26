#!/usr/bin/env python3
"""Rewrite Slug values in src/doc CSV files with short readable slugs.

Style:
- att-... for attendus
- cmp-... for competences
- rit-... for rituels
- pil-... for pillars
"""

from __future__ import annotations

import csv
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "doc"

STOPWORDS = {
    "le",
    "la",
    "les",
    "un",
    "une",
    "des",
    "de",
    "du",
    "d",
    "et",
    "ou",
    "a",
    "au",
    "aux",
    "en",
    "sur",
    "sous",
    "pour",
    "par",
    "avec",
    "dans",
    "que",
    "qui",
    "se",
    "son",
    "sa",
    "ses",
    "leur",
    "leurs",
    "l",
    "il",
    "elle",
    "on",
    "ne",
    "pas",
    "plus",
    "moins",
    "quand",
    "comme",
    "vers",
    "afin",
    "tout",
    "tous",
    "toutes",
    "chaque",
    "entre",
    "sans",
    "mais",
    "donc",
    "or",
    "ni",
    "car",
    "est",
    "sont",
    "etre",
    "fait",
    "faire",
    "fois",
}

REMAP = {
    "dalgorithme": "algo",
    "dalgorithmes": "algo",
    "programme": "prog",
    "programmes": "progs",
    "repetition": "repeat",
    "repetitions": "repeat",
    "entrees": "entree",
    "sorties": "sortie",
}

FILES = [
    (
        DOC / "Attendus référentiel 2a5e829b367e806eb43af26f0aae5642_all.csv",
        "Intitulé",
        "att",
    ),
    (
        DOC / "Compétences référentiel 2a5e829b367e809d9940d14b66cdfeb5_all.csv",
        "Nom",
        "cmp",
    ),
    (
        DOC / "Rituels mise en situation 2fde829b367e8096b257d7b5168f2fc4_all.csv",
        "Nom",
        "rit",
    ),
    (
        DOC / "pillars.csv",
        "Intitulé",
        "pil",
    ),
]


def normalize_text(text: str) -> str:
    out = unicodedata.normalize("NFKD", text)
    out = out.encode("ascii", "ignore").decode("ascii")
    out = out.lower()
    out = re.sub(r"https?://\\S+", " ", out)
    out = re.sub(r"[^a-z0-9]+", " ", out)
    return out.strip()


def build_short_slug(label: str, prefix: str) -> str:
    tokens: list[str] = []
    for token in normalize_text(label).split():
        if not token or token.isdigit() or token in STOPWORDS:
            continue
        token = REMAP.get(token, token)
        if len(token) <= 2:
            continue
        tokens.append(token)

    if not tokens:
        tokens = ["item"]

    return f"{prefix}-" + "-".join(tokens[:3])


def find_slug_header(headers: list[str]) -> str:
    for h in headers:
        if (h or "").strip().lower() in {"slug", "id_slug", "id slug"}:
            return h
    return "Slug"


def rewrite_file(path: Path, label_col: str, prefix: str) -> None:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        headers = list(reader.fieldnames or [])

    if not rows:
        return

    slug_header = find_slug_header(headers)
    if slug_header not in headers:
        headers = [slug_header] + headers

    seen: dict[str, int] = {}
    for row in rows:
        label = (row.get(label_col) or "").strip()
        base = build_short_slug(label, prefix)
        n = seen.get(base, 0) + 1
        seen[base] = n
        row[slug_header] = base if n == 1 else f"{base}-{n}"

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"updated {path.name}: {len(rows)} rows")


def main() -> None:
    for path, col, prefix in FILES:
        rewrite_file(path, col, prefix)


if __name__ == "__main__":
    main()
