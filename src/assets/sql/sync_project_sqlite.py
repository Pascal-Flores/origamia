#!/usr/bin/env python3
"""Sync the project SQLite database with referential tables and exercises."""

from __future__ import annotations

import argparse
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC_DB = Path(__file__).resolve().parent / "doc_referentiel.sqlite"
PROJECT_DB = Path(__file__).resolve().parent / "referentiel.sqlite"

REFERENTIAL_TABLES = [
    "competences_referentiel",
    "attendus_referentiel",
    "rituels_mise_en_situation",
    "variables_pedagogiques",
    "attendus_variables_pedagogiques",
]

EXCLUDED_PILLARS = {"pil-programmation-outil"}
EXCLUDED_COMPETENCES = {
    "cmp-programmer-traces-deplacements",
    "cmp-programmer-mesures",
    "cmp-programmer-simulations",
    "cmp-mise-en-forme-resultats",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        default="-",
        help="JSON manifest path, or - to read from stdin",
    )
    parser.add_argument(
        "--doc-db",
        default=str(DOC_DB),
        help="Path to the source referential SQLite database",
    )
    parser.add_argument(
        "--project-db",
        default=str(PROJECT_DB),
        help="Path to the target project SQLite database",
    )
    parser.add_argument(
        "--target-exercise-count",
        type=int,
        default=240,
        help="Planned total number of exercises",
    )
    return parser.parse_args()


def load_manifest(path: str) -> dict:
    if path == "-":
        import sys

        return json.load(sys.stdin)
    return json.loads(Path(path).read_text(encoding="utf-8"))


def copy_referential_tables(conn: sqlite3.Connection) -> None:
    conn.execute("DROP VIEW IF EXISTS main.exercices_enrichis")

    for table in REFERENTIAL_TABLES:
        row = conn.execute(
            """
            SELECT sql
            FROM doc.sqlite_master
            WHERE type = 'table' AND name = ?
            """,
            [table],
        ).fetchone()
        if not row or not row[0]:
            raise RuntimeError(f"Missing source table schema for {table}")

        conn.execute(f'DROP TABLE IF EXISTS main."{table}"')
        conn.execute(row[0])
        conn.execute(f'INSERT INTO "{table}" SELECT * FROM doc."{table}"')

    source_has_pillars = conn.execute(
        """
        SELECT 1
        FROM doc.sqlite_master
        WHERE type = 'table' AND name = 'pillars'
        """
    ).fetchone()

    conn.execute('DROP TABLE IF EXISTS main."pillars"')
    if source_has_pillars:
        row = conn.execute(
            """
            SELECT sql
            FROM doc.sqlite_master
            WHERE type = 'table' AND name = 'pillars'
            """,
        ).fetchone()
        if not row or not row[0]:
            raise RuntimeError("Missing source table schema for pillars")
        conn.execute(row[0])
        conn.execute('INSERT INTO "pillars" SELECT * FROM doc."pillars"')
    else:
        conn.execute(
            """
            CREATE TABLE "pillars" (
                id_slug TEXT PRIMARY KEY,
                intitule TEXT,
                description TEXT,
                place TEXT
            )
            """
        )
        conn.execute(
            """
            INSERT INTO "pillars" (id_slug, intitule, description, place)
            SELECT DISTINCT
                pilier AS id_slug,
                pilier AS intitule,
                '' AS description,
                '' AS place
            FROM competences_referentiel
            WHERE pilier IS NOT NULL AND TRIM(pilier) <> ''
            """
        )

    remove_excluded_pillars(conn)


def remove_excluded_pillars(conn: sqlite3.Connection) -> None:
    """Defensively remove competencies/attendus from retired pillars.

    This keeps sync correct even if an older doc_referentiel.sqlite is used.
    """
    for competence in EXCLUDED_COMPETENCES:
        conn.execute(
            "DELETE FROM attendus_variables_pedagogiques WHERE attendu_id_slug IN "
            "(SELECT id_slug FROM attendus_referentiel WHERE competence = ?)",
            [competence],
        )
        conn.execute(
            "DELETE FROM attendus_referentiel WHERE competence = ?",
            [competence],
        )
        conn.execute(
            "DELETE FROM competences_referentiel WHERE id_slug = ?",
            [competence],
        )

    for pillar in EXCLUDED_PILLARS:
        conn.execute(
            "DELETE FROM competences_referentiel WHERE pilier = ?",
            [pillar],
        )
        conn.execute(
            "DELETE FROM pillars WHERE id_slug = ?",
            [pillar],
        )


def ensure_project_meta(conn: sqlite3.Connection, target_count: int, built_count: int) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS project_meta (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
        """
    )
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    rows = [
        ("target_exercise_count", str(target_count)),
        ("built_exercise_count", str(built_count)),
        ("last_build_at", now),
    ]
    conn.executemany(
        "INSERT OR REPLACE INTO project_meta (key, value) VALUES (?, ?)",
        rows,
    )


def ensure_column(
    conn: sqlite3.Connection, table: str, column: str, definition: str
) -> None:
    columns = {row[1] for row in conn.execute(f'PRAGMA table_info("{table}")')}
    if column not in columns:
        conn.execute(f'ALTER TABLE "{table}" ADD COLUMN {definition}')


def ensure_exercices_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS exercices (
            number INTEGER PRIMARY KEY,
            nom TEXT NOT NULL,
            description TEXT,
            competence TEXT,
            attendu TEXT,
            type TEXT NOT NULL,
            statut TEXT,
            mise_en_situation TEXT,
            media TEXT,
            link TEXT,
            max_attempts INTEGER,
            source_path TEXT NOT NULL,
            generated_json TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
        """
    )
    ensure_column(conn, "exercices", "description", "description TEXT")
    ensure_column(conn, "exercices", "max_attempts", "max_attempts INTEGER")
    conn.execute("DELETE FROM exercices")
    conn.execute("DROP INDEX IF EXISTS main.idx_exercices_competence")
    conn.execute("DROP INDEX IF EXISTS main.idx_exercices_attendu")
    conn.execute("DROP INDEX IF EXISTS main.idx_exercices_type")
    conn.execute("DROP INDEX IF EXISTS main.idx_exercices_statut")
    conn.execute("DROP INDEX IF EXISTS main.idx_exercices_mise_en_situation")


def insert_exercices(conn: sqlite3.Connection, exercices: list[dict]) -> None:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    rows = [
        (
            exercice["number"],
            exercice["nom"],
            exercice.get("description"),
            exercice.get("competence"),
            exercice.get("attendu"),
            exercice["type"],
            exercice.get("statut"),
            exercice.get("mise_en_situation"),
            exercice.get("media"),
            exercice.get("link"),
            exercice.get("max_attempts", 1),
            exercice["source_path"],
            exercice["generated_json"],
            now,
        )
        for exercice in exercices
    ]

    conn.executemany(
        """
        INSERT INTO exercices (
            number,
            nom,
            description,
            competence,
            attendu,
            type,
            statut,
            mise_en_situation,
            media,
            link,
            max_attempts,
            source_path,
            generated_json,
            updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        rows,
    )

    conn.execute("CREATE INDEX idx_exercices_competence ON exercices (competence)")
    conn.execute("CREATE INDEX idx_exercices_attendu ON exercices (attendu)")
    conn.execute("CREATE INDEX idx_exercices_type ON exercices (type)")
    conn.execute("CREATE INDEX idx_exercices_statut ON exercices (statut)")
    conn.execute(
        "CREATE INDEX idx_exercices_mise_en_situation ON exercices (mise_en_situation)"
    )


def create_views(conn: sqlite3.Connection) -> None:
    conn.execute("DROP VIEW IF EXISTS main.exercices_enrichis")
    conn.execute(
        """
        CREATE VIEW exercices_enrichis AS
        SELECT
            e.number,
            e.nom,
            e.description,
            e.competence,
            c.nom AS competence_nom,
            c.description AS competence_description,
            c.pilier AS pilier_id_slug,
            p.intitule AS pilier_intitule,
            e.attendu,
            a.intitule AS attendu_intitule,
            a.niveau AS attendu_niveau,
            e.type,
            e.statut,
            e.mise_en_situation,
            r.nom AS mise_en_situation_nom,
            r.categorie AS mise_en_situation_categorie,
            e.media,
            e.link,
            e.max_attempts,
            e.source_path,
            e.generated_json,
            e.updated_at
        FROM exercices AS e
        LEFT JOIN competences_referentiel AS c
            ON c.id_slug = e.competence
        LEFT JOIN pillars AS p
            ON p.id_slug = c.pilier
        LEFT JOIN attendus_referentiel AS a
            ON a.id_slug = e.attendu
        LEFT JOIN rituels_mise_en_situation AS r
            ON r.id_slug = e.mise_en_situation
        """
    )


def main() -> None:
    args = parse_args()
    manifest = load_manifest(args.manifest)
    exercices = manifest.get("exercises", [])

    project_db = Path(args.project_db)
    project_db.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(project_db)
    try:
        conn.execute("PRAGMA foreign_keys = OFF")
        conn.execute("ATTACH DATABASE ? AS doc", [str(Path(args.doc_db))])

        copy_referential_tables(conn)
        ensure_project_meta(conn, args.target_exercise_count, len(exercices))
        ensure_exercices_table(conn)
        insert_exercices(conn, exercices)
        create_views(conn)

        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    main()
