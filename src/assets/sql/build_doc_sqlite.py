#!/usr/bin/env python3
"""Build an SQLite database from CSV files in src/doc.

Rules:
- One table per CSV file.
- If CSV contains Slug/id_slug, it is used as-is for id_slug.
- Otherwise id_slug is derived from Nom/Intitule columns.
- id_slug must be unique per table.
- CSV slug columns are not duplicated in table columns (id_slug is the source of truth).
- All CSV columns are imported as TEXT after normalization.
"""

from __future__ import annotations

import csv
import re
import sqlite3
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC_DIR = ROOT / "doc"
OUT_DB = Path(__file__).resolve().parent / "doc_referentiel.sqlite"

HEX32_SUFFIX_RE = re.compile(r"\s+[0-9a-f]{32}_all$", re.IGNORECASE)
CSV_COMPETENCES_NAME = "competences_referentiel"
CSV_ATTENDUS_NAME = "attendus_referentiel"

# Columns kept in CSV but excluded from `competences_referentiel` table.
COMPETENCES_EXCLUDED_COLUMNS = {
    "Compétences du programme scolaire",
    "Concepts",
    "Variables pédagogiques",
    "supports compatibles",
}


def slugify(value: str) -> str:
    text = unicodedata.normalize("NFKD", value)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def snake_case(value: str) -> str:
    text = unicodedata.normalize("NFKD", value)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = text.strip("_")
    return text or "col"


def table_name_from_filename(path: Path) -> str:
    name = path.stem
    name = HEX32_SUFFIX_RE.sub("", name)
    name = name.replace("referentiel", "referentiel")
    base = snake_case(name)
    if not base:
        base = "table_csv"
    if base[0].isdigit():
        base = f"t_{base}"
    return base


def choose_slug_source(row: dict[str, str], ordered_keys: list[str]) -> str:
    explicit_slug_keys = ["Slug", "slug", "id_slug", "ID Slug", "Id Slug"]
    for key in explicit_slug_keys:
        if key in row and (row.get(key) or "").strip():
            return (row.get(key) or "").strip()

    preferred = [
        "Nom",
        "Intitulé",
        "Intitule",
        "Title",
        "Titre",
    ]

    for key in preferred:
        if key in row and (row.get(key) or "").strip():
            return row[key].strip()

    for key in ordered_keys:
        value = (row.get(key) or "").strip()
        if value:
            return value

    return "ligne"


def has_explicit_slug_column(headers: list[str]) -> bool:
    keys = {h.strip().lower() for h in headers if h}
    return any(k in keys for k in ["slug", "id_slug", "id slug"])


def unique_slug_or_fail(slug: str, seen: set[str], table: str, row_num: int) -> str:
    clean = slug.strip()
    if not clean:
        raise ValueError(f"[{table}] Empty slug at row {row_num}")
    if clean in seen:
        raise ValueError(f"[{table}] Duplicate slug '{clean}' at row {row_num}")
    seen.add(clean)
    return clean


def normalized_columns(headers: list[str]) -> list[tuple[str, str]]:
    """Return list of (source_header, db_column_name) preserving order."""
    used: set[str] = set()
    cols: list[tuple[str, str]] = []

    for header in headers:
        if (header or "").strip().lower() in {"slug", "id_slug", "id slug"}:
            continue
        candidate = snake_case(header)
        if not candidate:
            candidate = "col"
        name = candidate
        n = 2
        while name in used or name in {"id_slug"}:
            name = f"{candidate}_{n}"
            n += 1
        used.add(name)
        cols.append((header, name))

    return cols


def normalized_columns_for_table(
    table: str, headers: list[str]
) -> list[tuple[str, str]]:
    cols = normalized_columns(headers)
    if table != CSV_COMPETENCES_NAME:
        if table == CSV_ATTENDUS_NAME:
            return [(src, db) for src, db in cols if src.strip() != "Variables pédagogiques"]
        return cols

    excluded = {h.strip() for h in COMPETENCES_EXCLUDED_COLUMNS}
    return [(src, db) for src, db in cols if src.strip() not in excluded]


def split_variables_pedagogiques(raw: str) -> list[str]:
    text = (raw or "").strip()
    if not text:
        return []

    # Cells are comma-separated (either labels, links, or "label (link)").
    parts = [p.strip() for p in re.split(r"\s*,\s*", text) if p.strip()]
    if not parts:
        return [text]
    return parts


def parse_variable_label_and_link(entry: str) -> tuple[str, str]:
    text = (entry or "").strip()
    if not text:
        return "", ""

    if re.match(r"^https?://", text):
        return "", text

    # Extract trailing notion link if present in the common format:
    # "Nom variable (https://... )"
    m = re.match(r"^(.*?)\s*\((https?://[^)]*)\)\s*$", text)
    if m:
        return m.group(1).strip(), m.group(2).strip()

    return text, ""


def notion_link_key(url: str) -> str:
    text = (url or "").strip()
    if not text:
        return ""

    # Match the canonical 32-hex Notion page identifier used across URL variants.
    m = re.search(r"([0-9a-f]{32})", text, re.IGNORECASE)
    if m:
        return m.group(1).lower()

    return text


def create_variables_pedagogiques_table(
    conn: sqlite3.Connection,
    competence_variables: list[tuple[str, str]],
) -> dict[str, list[str]]:
    variables_table = "variables_pedagogiques"
    conn.execute(f'DROP TABLE IF EXISTS "{variables_table}"')

    conn.execute(
        f'CREATE TABLE "{variables_table}" ('
        '"id_slug" TEXT PRIMARY KEY, '
        '"nom" TEXT NOT NULL)'
    )

    insert_var_sql = f'INSERT INTO "{variables_table}" ("id_slug", "nom") VALUES (?, ?)'

    # Deduplicate globally by variable name; each variable gets a unique slug from its name.
    slug_by_name: dict[str, str] = {}
    used_slugs: set[str] = set()
    competence_to_variables: dict[str, list[str]] = {}

    for competence_slug, raw in competence_variables:
        seen_for_competence: set[str] = set()
        variables = split_variables_pedagogiques(raw)
        for var in variables:
            nom, lien = parse_variable_label_and_link(var)
            if not nom:
                continue

            key = nom.lower()
            var_slug = slug_by_name.get(key)
            if not var_slug:
                base = f"vp-{slugify(nom)}"
                candidate = base or "vp-variable"
                idx = 2
                while candidate in used_slugs:
                    candidate = f"{base}-{idx}"
                    idx += 1

                var_slug = candidate
                slug_by_name[key] = var_slug
                used_slugs.add(var_slug)
                conn.execute(insert_var_sql, [var_slug, nom])

            if var_slug not in seen_for_competence:
                competence_to_variables.setdefault(competence_slug, []).append(var_slug)
                seen_for_competence.add(var_slug)

    return competence_to_variables


def create_attendus_variables_pedagogiques_table(
    conn: sqlite3.Connection,
    attendu_competences: list[tuple[str, str]],
    competence_to_variables: dict[str, list[str]],
) -> None:
    table = "attendus_variables_pedagogiques"
    conn.execute(f'DROP TABLE IF EXISTS "{table}"')
    conn.execute(
        f'CREATE TABLE "{table}" ('
        '"attendu_id_slug" TEXT NOT NULL, '
        '"variable_pedagogique_id_slug" TEXT NOT NULL, '
        'PRIMARY KEY ("attendu_id_slug", "variable_pedagogique_id_slug"))'
    )

    insert_link_sql = (
        f'INSERT OR IGNORE INTO "{table}" ("attendu_id_slug", "variable_pedagogique_id_slug") '
        'VALUES (?, ?)'
    )

    for attendu_slug, competence_slug in attendu_competences:
        for var_slug in competence_to_variables.get(competence_slug, []):
            conn.execute(insert_link_sql, [attendu_slug, var_slug])


def import_csv_to_table(
    conn: sqlite3.Connection, csv_path: Path
) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]:
    table = table_name_from_filename(csv_path)
    competence_variables: list[tuple[str, str]] = []
    attendu_competences: list[tuple[str, str]] = []

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return [], []

        headers = [h.strip() if h else "" for h in reader.fieldnames]
        col_map = normalized_columns_for_table(table, headers)

        conn.execute(f'DROP TABLE IF EXISTS "{table}"')

        col_defs = ['"id_slug" TEXT PRIMARY KEY']
        col_defs.extend(f'"{db_col}" TEXT' for _, db_col in col_map)

        conn.execute(f'CREATE TABLE "{table}" ({", ".join(col_defs)})')

        db_cols = ["id_slug"] + [db_col for _, db_col in col_map]
        placeholders = ", ".join(["?"] * len(db_cols))
        insert_sql = (
            f'INSERT INTO "{table}" ({", ".join(f"\"{c}\"" for c in db_cols)}) '
            f"VALUES ({placeholders})"
        )

        explicit_slug = has_explicit_slug_column(headers)
        seen: set[str] = set()
        for row_num, row in enumerate(reader, start=2):
            slug_source = choose_slug_source(row, headers)
            row_slug = slug_source if explicit_slug else slugify(slug_source)

            row_slug = unique_slug_or_fail(row_slug, seen, table, row_num)

            values: list[object] = [row_slug]
            for src_col, _ in col_map:
                values.append((row.get(src_col) or "").strip())

            conn.execute(insert_sql, values)

            if table == CSV_COMPETENCES_NAME:
                competence_variables.append((row_slug, (row.get("Variables pédagogiques") or "").strip()))
            elif table == CSV_ATTENDUS_NAME:
                attendu_competences.append((row_slug, (row.get("Compétence") or "").strip()))

    return competence_variables, attendu_competences


def main() -> None:
    csv_files = sorted(DOC_DIR.glob("*.csv"))
    if not csv_files:
        raise SystemExit(f"No CSV files found in {DOC_DIR}")

    OUT_DB.parent.mkdir(parents=True, exist_ok=True)
    if OUT_DB.exists():
        OUT_DB.unlink()

    conn = sqlite3.connect(OUT_DB)
    try:
        all_attendu_variables: list[tuple[str, str]] = []
        all_competence_variables: list[tuple[str, str]] = []
        for csv_path in csv_files:
            comp_vars, att_vars = import_csv_to_table(conn, csv_path)
            all_competence_variables.extend(comp_vars)
            all_attendu_variables.extend(att_vars)

        competence_to_variables = create_variables_pedagogiques_table(conn, all_competence_variables)

        create_attendus_variables_pedagogiques_table(conn, all_attendu_variables, competence_to_variables)
        conn.commit()
    finally:
        conn.close()

    print(f"SQLite database generated: {OUT_DB}")
    for p in csv_files:
        print(f"- imported: {p.name}")


if __name__ == "__main__":
    main()
