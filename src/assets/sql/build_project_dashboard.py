#!/usr/bin/env python3
"""Build a static project dashboard from the project SQLite database."""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT_DB = Path(__file__).resolve().parent / "referentiel.sqlite"
DEFAULT_OUTPUT_DIR = ROOT / "out" / "dashboard"
DEFAULT_TOTAL_TARGET = 230
DEFAULT_COMPETENCE_TARGET = 9
DEFAULT_ATTENDU_TARGET = 3
STATUS_CONFIG = {
    "todo": {"label": "TODO", "tone": "todo"},
    "wip": {"label": "WIP", "tone": "wip"},
    "bug": {"label": "BUG", "tone": "bug"},
    "testing": {"label": "TESTING", "tone": "testing"},
    "done": {"label": "DONE", "tone": "done"},
    "drop": {"label": "DROP", "tone": "drop"},
    "unspecified": {"label": "Non renseigné", "tone": "unspecified"},
    "other": {"label": "Autre", "tone": "other"},
    "remaining": {"label": "Non créé", "tone": "remaining"},
}
STATUS_ORDER = ["todo", "wip", "bug", "testing", "done", "drop", "other", "unspecified"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--db",
        default=str(PROJECT_DB),
        help="Path to the project SQLite database",
    )
    parser.add_argument(
        "--out-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Directory where the static dashboard will be written",
    )
    return parser.parse_args()


def read_meta(conn: sqlite3.Connection, key: str, default: str = "") -> str:
    row = conn.execute(
        "SELECT value FROM project_meta WHERE key = ?",
        [key],
    ).fetchone()
    if not row or row[0] is None:
        return default
    return str(row[0])


def fetch_rows(conn: sqlite3.Connection, query: str, params: list | tuple | None = None) -> list[dict]:
    cursor = conn.execute(query, params or [])
    return [dict(row) for row in cursor.fetchall()]


def add_percentages(rows: list[dict], total: int) -> list[dict]:
    enriched = []
    for row in rows:
        value = int(row.get("value", 0) or 0)
        enriched.append(
            {
                **row,
                "value": value,
                "ratio": round((value / total) * 100, 1) if total else 0.0,
            }
        )
    return enriched


def normalize_target_value(value: float) -> int | float:
    return int(value) if float(value).is_integer() else round(value, 2)


def normalize_status_key(value: str | None) -> str:
    raw = str(value or "").strip()
    if not raw:
        return "unspecified"

    lowered = raw.lower()
    if lowered in STATUS_CONFIG:
        return lowered
    return "other"


def build_status_data(conn: sqlite3.Connection, built_count: int, target_count: int) -> dict:
    rows = fetch_rows(
        conn,
        """
        SELECT statut
        FROM exercices
        """,
    )

    counts = {key: 0 for key in STATUS_ORDER}
    for row in rows:
        counts[normalize_status_key(row.get("statut"))] += 1

    distribution_rows = []
    for key in STATUS_ORDER:
        value = counts[key]
        if value <= 0:
            continue
        distribution_rows.append(
            {
                "key": key,
                "label": STATUS_CONFIG[key]["label"],
                "tone": STATUS_CONFIG[key]["tone"],
                "value": value,
            }
        )

    distribution = add_percentages(distribution_rows, built_count)

    segments = []
    for key in STATUS_ORDER:
        value = counts[key]
        if value <= 0:
            continue
        segments.append(
            {
                "key": key,
                "label": STATUS_CONFIG[key]["label"],
                "tone": STATUS_CONFIG[key]["tone"],
                "value": value,
                "ratio": round((value / target_count) * 100, 1) if target_count else 0.0,
            }
        )

    remaining_count = max(target_count - built_count, 0)
    if remaining_count > 0:
        segments.append(
            {
                "key": "remaining",
                "label": STATUS_CONFIG["remaining"]["label"],
                "tone": STATUS_CONFIG["remaining"]["tone"],
                "value": remaining_count,
                "ratio": round((remaining_count / target_count) * 100, 1) if target_count else 0.0,
            }
        )

    completed_count = counts["done"] + counts["drop"]
    active_count = counts["todo"] + counts["wip"] + counts["bug"] + counts["testing"]

    return {
        "counts": counts,
        "distribution": distribution,
        "segments": segments,
        "completed_count": completed_count,
        "completed_ratio": round((completed_count / target_count) * 100, 1) if target_count else 0.0,
        "tracked_ratio": round((built_count / target_count) * 100, 1) if target_count else 0.0,
        "active_count": active_count,
        "remaining_count": remaining_count,
    }


def build_distribution_data(conn: sqlite3.Connection, built_count: int, status_data: dict) -> dict:
    distributions = {
        "type": """
            SELECT
                COALESCE(NULLIF(TRIM(type), ''), 'Non renseigné') AS label,
                COUNT(*) AS value
            FROM exercices
            GROUP BY label
            ORDER BY value DESC, label ASC
        """,
        "pillar": """
            SELECT
                COALESCE(NULLIF(TRIM(pilier_intitule), ''), NULLIF(TRIM(pilier_id_slug), ''), 'Non renseigné') AS label,
                COUNT(*) AS value
            FROM exercices_enrichis
            GROUP BY label
            ORDER BY value DESC, label ASC
        """,
        "competence": """
            SELECT
                COALESCE(NULLIF(TRIM(competence_nom), ''), NULLIF(TRIM(competence), ''), 'Non renseigné') AS label,
                COUNT(*) AS value
            FROM exercices_enrichis
            GROUP BY label
            ORDER BY value DESC, label ASC
        """,
        "attendu": """
            SELECT
                COALESCE(NULLIF(TRIM(attendu_intitule), ''), NULLIF(TRIM(attendu), ''), 'Non renseigné') AS label,
                COUNT(*) AS value
            FROM exercices_enrichis
            GROUP BY label
            ORDER BY value DESC, label ASC
        """,
        "situation": """
            SELECT
                COALESCE(NULLIF(TRIM(mise_en_situation_nom), ''), NULLIF(TRIM(mise_en_situation), ''), 'Non renseigné') AS label,
                COUNT(*) AS value
            FROM exercices_enrichis
            GROUP BY label
            ORDER BY value DESC, label ASC
        """,
    }

    distribution_data = {
        key: add_percentages(fetch_rows(conn, query), built_count)
        for key, query in distributions.items()
    }
    distribution_data["status"] = status_data["distribution"]
    return distribution_data


def build_coverage_data(conn: sqlite3.Connection, built_count: int) -> tuple[list[dict], float]:
    fields = [
        ("nom", "Nom"),
        ("description", "Description"),
        ("competence", "Compétence"),
        ("attendu", "Attendu"),
        ("statut", "Statut"),
        ("max_attempts", "Essais"),
        ("mise_en_situation", "Mise en situation"),
        ("media", "Média"),
        ("link", "Lien média"),
    ]

    coverage = []
    overall_complete = 0

    for column_name, label in fields:
        query = f"""
            SELECT
                SUM(
                    CASE
                        WHEN {column_name} IS NOT NULL
                         AND TRIM({column_name}) <> ''
                         AND UPPER(TRIM({column_name})) <> 'N/A'
                        THEN 1
                        ELSE 0
                    END
                ) AS filled,
                SUM(
                    CASE
                        WHEN UPPER(TRIM(COALESCE({column_name}, ''))) = 'N/A'
                        THEN 1
                        ELSE 0
                    END
                ) AS na_value,
                SUM(
                    CASE
                        WHEN {column_name} IS NULL OR TRIM({column_name}) = ''
                        THEN 1
                        ELSE 0
                    END
                ) AS missing
            FROM exercices
        """
        row = conn.execute(query).fetchone()
        filled = int(row[0] or 0)
        na_value = int(row[1] or 0)
        missing = int(row[2] or 0)
        complete = filled + na_value
        overall_complete += complete
        coverage.append(
            {
                "label": label,
                "filled": filled,
                "na_value": na_value,
                "complete": complete,
                "missing": missing,
                "ratio": round((complete / built_count) * 100, 1) if built_count else 0.0,
            }
        )

    total_slots = built_count * len(fields)
    overall_ratio = round((overall_complete / total_slots) * 100, 1) if total_slots else 0.0
    return coverage, overall_ratio


def build_plan_data(conn: sqlite3.Connection, total_target_count: int) -> dict:
    competence_count = int(conn.execute("SELECT COUNT(*) FROM competences_referentiel").fetchone()[0])
    attendu_count = int(conn.execute("SELECT COUNT(*) FROM attendus_referentiel").fetchone()[0])
    pillar_count = int(conn.execute("SELECT COUNT(*) FROM pillars").fetchone()[0])

    structured_target_count = competence_count * DEFAULT_COMPETENCE_TARGET
    pillar_target_count = (
        normalize_target_value(structured_target_count / pillar_count) if pillar_count else 0
    )
    overflow_target_count = max(total_target_count - structured_target_count, 0)

    return {
        "total_target_count": total_target_count,
        "structured_target_count": structured_target_count,
        "overflow_target_count": overflow_target_count,
        "competence_count": competence_count,
        "competence_target_count": DEFAULT_COMPETENCE_TARGET,
        "attendu_count": attendu_count,
        "attendu_target_count": DEFAULT_ATTENDU_TARGET,
        "pillar_count": pillar_count,
        "pillar_target_count": pillar_target_count,
    }


def build_target_progress_rows(
    reference_labels: list[str],
    count_rows: list[dict],
    target_value: int | float,
) -> list[dict]:
    counts_by_label: dict[str, dict[str, int]] = {}
    known_labels = set(reference_labels)

    for row in count_rows:
        label = row["label"]
        status_key = normalize_status_key(row.get("statut"))
        value = int(row.get("value", 0) or 0)
        counts_by_label.setdefault(label, {key: 0 for key in STATUS_ORDER})
        counts_by_label[label][status_key] += value
        known_labels.add(label)

    ordered_labels = [label for label in reference_labels if label in known_labels]
    extras = sorted(set(counts_by_label.keys()) - set(reference_labels), key=lambda item: item.lower())
    ordered_labels.extend(extras)

    progress_rows = []
    for label in ordered_labels:
        status_counts = counts_by_label.get(label, {key: 0 for key in STATUS_ORDER})
        built = sum(status_counts.values())
        completed = status_counts["done"] + status_counts["drop"]
        remaining = max(float(target_value) - built, 0.0)

        segments = []
        for key in STATUS_ORDER:
            value = status_counts[key]
            if value <= 0:
                continue
            segments.append(
                {
                    "key": key,
                    "label": STATUS_CONFIG[key]["label"],
                    "tone": STATUS_CONFIG[key]["tone"],
                    "value": value,
                    "ratio": round((value / target_value) * 100, 1) if target_value else 0.0,
                }
            )

        if remaining > 0:
            segments.append(
                {
                    "key": "remaining",
                    "label": STATUS_CONFIG["remaining"]["label"],
                    "tone": STATUS_CONFIG["remaining"]["tone"],
                    "value": normalize_target_value(remaining),
                    "ratio": round((remaining / target_value) * 100, 1) if target_value else 0.0,
                }
            )

        progress_rows.append(
            {
                "label": label,
                "built": built,
                "completed": completed,
                "target": target_value,
                "remaining": normalize_target_value(remaining),
                "tracked_ratio": round((built / target_value) * 100, 1) if target_value else 0.0,
                "completion_ratio": round((completed / target_value) * 100, 1) if target_value else 0.0,
                "segments": segments,
            }
        )

    return progress_rows


def build_progress_data(conn: sqlite3.Connection, plan_data: dict) -> dict:
    pillar_reference_rows = fetch_rows(
        conn,
        """
        SELECT
            COALESCE(NULLIF(TRIM(intitule), ''), id_slug) AS label
        FROM pillars
        ORDER BY label ASC
        """,
    )
    pillar_count_rows = fetch_rows(
        conn,
        """
        SELECT
            COALESCE(NULLIF(TRIM(pilier_intitule), ''), NULLIF(TRIM(pilier_id_slug), ''), 'Non renseigné') AS label,
            COALESCE(NULLIF(TRIM(statut), ''), 'Non renseigné') AS statut,
            COUNT(*) AS value
        FROM exercices_enrichis
        GROUP BY label, statut
        ORDER BY label ASC, statut ASC
        """,
    )
    competence_reference_rows = fetch_rows(
        conn,
        """
        SELECT
            COALESCE(NULLIF(TRIM(nom), ''), id_slug) AS label
        FROM competences_referentiel
        ORDER BY label ASC
        """,
    )
    competence_count_rows = fetch_rows(
        conn,
        """
        SELECT
            COALESCE(NULLIF(TRIM(competence_nom), ''), NULLIF(TRIM(competence), ''), 'Non renseigné') AS label,
            COALESCE(NULLIF(TRIM(statut), ''), 'Non renseigné') AS statut,
            COUNT(*) AS value
        FROM exercices_enrichis
        GROUP BY label, statut
        ORDER BY label ASC, statut ASC
        """,
    )

    return {
        "pillar": build_target_progress_rows(
            [row["label"] for row in pillar_reference_rows],
            pillar_count_rows,
            plan_data["pillar_target_count"],
        ),
        "competence": build_target_progress_rows(
            [row["label"] for row in competence_reference_rows],
            competence_count_rows,
            plan_data["competence_target_count"],
        ),
    }


def build_exercise_rows(conn: sqlite3.Connection, output_dir: Path) -> list[dict]:
    rows = fetch_rows(
        conn,
        """
        SELECT
            number,
            nom,
            COALESCE(NULLIF(TRIM(description), ''), '') AS description,
            COALESCE(NULLIF(TRIM(statut), ''), 'Non renseigné') AS statut,
            COALESCE(NULLIF(TRIM(type), ''), 'Non renseigné') AS type,
            COALESCE(NULLIF(TRIM(competence_nom), ''), NULLIF(TRIM(competence), ''), 'Non renseigné') AS competence,
            COALESCE(NULLIF(TRIM(pilier_intitule), ''), NULLIF(TRIM(pilier_id_slug), ''), 'Non renseigné') AS pilier,
            COALESCE(NULLIF(TRIM(attendu_intitule), ''), NULLIF(TRIM(attendu), ''), 'Non renseigné') AS attendu,
            COALESCE(NULLIF(TRIM(mise_en_situation_nom), ''), NULLIF(TRIM(mise_en_situation), ''), 'Non renseigné') AS situation,
            COALESCE(max_attempts, 1) AS max_attempts,
            source_path
        FROM exercices_enrichis
        ORDER BY number ASC
        """,
    )

    exercises = []
    for row in rows:
        row["statut"] = STATUS_CONFIG[normalize_status_key(row.get("statut"))]["label"]
        row["source_href"] = os.path.relpath(ROOT / row["source_path"], output_dir).replace("\\", "/")
        exercises.append(row)
    return exercises


def build_dashboard_data(conn: sqlite3.Connection, output_dir: Path) -> dict:
    built_count = int(conn.execute("SELECT COUNT(*) FROM exercices").fetchone()[0])
    target_count = int(read_meta(conn, "target_exercise_count", str(DEFAULT_TOTAL_TARGET)) or 0)
    last_build_at = read_meta(conn, "last_build_at", "")
    status_data = build_status_data(conn, built_count, target_count)

    plan_data = build_plan_data(conn, target_count)
    coverage, overall_metadata_ratio = build_coverage_data(conn, built_count)

    return {
        "summary": {
            "built_count": built_count,
            "target_count": target_count,
            "remaining_count": status_data["remaining_count"],
            "completion_ratio": status_data["completed_ratio"],
            "tracked_ratio": status_data["tracked_ratio"],
            "completed_count": status_data["completed_count"],
            "active_count": status_data["active_count"],
            "overall_metadata_ratio": overall_metadata_ratio,
            "last_build_at": last_build_at,
        },
        "status_summary": status_data,
        "plan": plan_data,
        "coverage": coverage,
        "distributions": build_distribution_data(conn, built_count, status_data),
        "progressions": build_progress_data(conn, plan_data),
        "exercises": build_exercise_rows(conn, output_dir),
    }


def build_html(data: dict) -> str:
    stats_json = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Origamia - Avancée du projet</title>
  <style>
    :root {{
      --bg: #f7f1e7;
      --bg-accent: #efe6d5;
      --panel: rgba(255, 252, 246, 0.9);
      --panel-strong: #fffdf8;
      --border: rgba(52, 79, 108, 0.18);
      --text: #18212b;
      --muted: #5d6a79;
      --accent: #0f7c86;
      --accent-soft: #d8eef0;
      --warm: #e59a52;
      --warm-soft: #fde8cf;
      --danger: #c75b39;
      --shadow: 0 18px 45px rgba(22, 34, 47, 0.08);
      --radius: 24px;
    }}

    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      min-height: 100vh;
      font-family: "Avenir Next", "Segoe UI", sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at top left, rgba(15, 124, 134, 0.12), transparent 35%),
        radial-gradient(circle at top right, rgba(229, 154, 82, 0.18), transparent 30%),
        linear-gradient(180deg, var(--bg) 0%, #fbf8f1 100%);
    }}

    .shell {{
      width: min(1220px, calc(100vw - 32px));
      margin: 0 auto;
      padding: 28px 0 48px;
    }}

    .hero {{
      position: relative;
      overflow: hidden;
      background: linear-gradient(135deg, rgba(15, 124, 134, 0.96), rgba(32, 58, 87, 0.96));
      color: white;
      border-radius: 32px;
      padding: 28px;
      box-shadow: var(--shadow);
    }}

    .hero::after {{
      content: "";
      position: absolute;
      width: 240px;
      height: 240px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.1);
      top: -70px;
      right: -60px;
    }}

    .eyebrow {{
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      opacity: 0.86;
    }}

    h1, h2, h3 {{
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      font-weight: 700;
      letter-spacing: -0.02em;
    }}

    h1 {{
      font-size: clamp(2.3rem, 5vw, 4rem);
      line-height: 0.95;
      max-width: 12ch;
      margin-top: 8px;
    }}

    .subtitle {{
      max-width: 58ch;
      color: rgba(255, 255, 255, 0.88);
      font-size: 1.02rem;
      line-height: 1.55;
      margin: 14px 0 0;
    }}

    .hero-grid {{
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 18px;
      margin-top: 26px;
      position: relative;
      z-index: 1;
    }}

    .hero-card, .panel {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      backdrop-filter: blur(12px);
    }}

    .hero-card {{
      background: rgba(255, 255, 255, 0.12);
      border-color: rgba(255, 255, 255, 0.14);
      color: white;
      padding: 20px;
    }}

    .progress-bar {{
      display: flex;
      height: 14px;
      background: rgba(255, 255, 255, 0.14);
      border-radius: 999px;
      overflow: hidden;
      margin-top: 14px;
    }}

    .progress-bar > span,
    .progress-bar > div {{
      height: 100%;
      min-width: 0;
    }}

    .progress-segment.todo {{
      background: #7f8c99;
    }}

    .progress-segment.wip {{
      background: #e59a52;
    }}

    .progress-segment.bug {{
      background: #d95f59;
    }}

    .progress-segment.testing {{
      background: #4c97ff;
    }}

    .progress-segment.done {{
      background: #22b573;
    }}

    .progress-segment.drop {{
      background: #c75b39;
    }}

    .progress-segment.other {{
      background: #8d6ccf;
    }}

    .progress-segment.unspecified {{
      background: #c9b89d;
    }}

    .progress-segment.remaining {{
      background: rgba(255, 255, 255, 0.18);
    }}

    .legend-list {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 12px;
    }}

    .legend-item {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 10px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: rgba(255, 255, 255, 0.92);
      font-size: 0.82rem;
      white-space: nowrap;
    }}

    .legend-dot {{
      width: 10px;
      height: 10px;
      border-radius: 999px;
      flex: 0 0 10px;
    }}

    .status-todo {{
      background: #7f8c99;
      color: #ffffff;
    }}

    .status-wip {{
      background: #f4debf;
      color: #8d5d29;
    }}

    .status-bug {{
      background: #f7d0cc;
      color: #963a35;
    }}

    .status-testing {{
      background: #dceaff;
      color: #225a9a;
    }}

    .status-done {{
      background: #dcf6e8;
      color: #14734a;
    }}

    .status-drop {{
      background: #f8ddd7;
      color: #983d23;
    }}

    .status-other {{
      background: #efe3ff;
      color: #6542a9;
    }}

    .status-unspecified {{
      background: #efe6d5;
      color: #835d27;
    }}

    .status-remaining {{
      background: rgba(255, 255, 255, 0.16);
      color: rgba(255, 255, 255, 0.92);
    }}

    .hero-stats {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
    }}

    .hero-stat {{
      background: rgba(255, 255, 255, 0.12);
      border-radius: 20px;
      padding: 16px;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }}

    .hero-stat-label {{
      display: block;
      font-size: 0.83rem;
      color: rgba(255, 255, 255, 0.8);
    }}

    .hero-stat-value {{
      display: block;
      margin-top: 8px;
      font-size: 1.8rem;
      font-weight: 700;
      letter-spacing: -0.03em;
    }}

    .section-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 18px;
      margin-top: 18px;
    }}

    .section-grid.single {{
      grid-template-columns: 1fr;
    }}

    .panel {{
      padding: 22px;
    }}

    .panel-header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 16px;
    }}

    .panel-title {{
      font-size: 1.45rem;
    }}

    .panel-meta {{
      color: var(--muted);
      font-size: 0.92rem;
      text-align: right;
    }}

    .panel-meta-stack {{
      display: grid;
      gap: 10px;
      justify-items: end;
    }}

    .sort-control {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-size: 0.84rem;
      color: var(--muted);
    }}

    .sort-control select {{
      border: 1px solid var(--border);
      background: var(--panel-strong);
      color: var(--text);
      border-radius: 12px;
      padding: 8px 10px;
      font: inherit;
    }}

    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 14px;
    }}

    .kpi {{
      background: var(--panel-strong);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 18px;
    }}

    .kpi-label {{
      font-size: 0.84rem;
      color: var(--muted);
    }}

    .kpi-value {{
      display: block;
      margin-top: 8px;
      font-size: 1.9rem;
      font-weight: 700;
      letter-spacing: -0.04em;
    }}

    .kpi-note {{
      margin-top: 10px;
      font-size: 0.86rem;
      color: var(--muted);
    }}

    .bar-list {{
      display: grid;
      gap: 12px;
    }}

    .bar-row {{
      display: grid;
      gap: 6px;
    }}

    .bar-row header {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      font-size: 0.95rem;
    }}

    .bar-track {{
      position: relative;
      display: flex;
      height: 12px;
      border-radius: 999px;
      overflow: hidden;
      background: var(--bg-accent);
    }}

    .bar-fill {{
      height: 100%;
      border-radius: inherit;
      background: linear-gradient(90deg, var(--accent), #35a7b2);
    }}

    .bar-fill.warm {{
      background: linear-gradient(90deg, var(--warm), #f0b46f);
    }}

    .bar-fill.todo {{
      background: #7f8c99;
    }}

    .bar-fill.wip {{
      background: #e59a52;
    }}

    .bar-fill.bug {{
      background: #d95f59;
    }}

    .bar-fill.testing {{
      background: #4c97ff;
    }}

    .bar-fill.done {{
      background: #22b573;
    }}

    .bar-fill.drop {{
      background: #c75b39;
    }}

    .bar-fill.other {{
      background: #8d6ccf;
    }}

    .bar-fill.unspecified {{
      background: #c9b89d;
    }}

    .bar-fill.remaining {{
      background: rgba(24, 33, 43, 0.18);
    }}

    .coverage-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
    }}

    .coverage-item {{
      background: var(--panel-strong);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 16px;
    }}

    .coverage-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 8px;
      font-size: 0.93rem;
    }}

    .coverage-meta {{
      color: var(--muted);
      font-size: 0.86rem;
      margin-top: 8px;
    }}

    .row-legend {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 8px;
    }}

    .filters {{
      display: grid;
      grid-template-columns: minmax(240px, 1.4fr) repeat(2, minmax(180px, 0.8fr));
      gap: 12px;
      margin-bottom: 16px;
    }}

    .filters input,
    .filters select {{
      width: 100%;
      border: 1px solid var(--border);
      background: var(--panel-strong);
      color: var(--text);
      border-radius: 14px;
      padding: 12px 14px;
      font: inherit;
    }}

    .table-shell {{
      overflow: auto;
      border-radius: 18px;
      border: 1px solid var(--border);
      background: var(--panel-strong);
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      min-width: 920px;
    }}

    th, td {{
      text-align: left;
      padding: 12px 14px;
      border-bottom: 1px solid rgba(24, 33, 43, 0.08);
      vertical-align: top;
      font-size: 0.94rem;
    }}

    th {{
      position: sticky;
      top: 0;
      background: #fffaf2;
      z-index: 1;
      font-size: 0.78rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
    }}

    td.number {{
      font-weight: 700;
      white-space: nowrap;
    }}

    .pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 10px;
      border-radius: 999px;
      background: var(--accent-soft);
      color: #0f5b62;
      font-size: 0.82rem;
      white-space: nowrap;
    }}

    .pill.muted {{
      background: var(--warm-soft);
      color: #8d5d29;
    }}

    .pill.na {{
      background: #efe6d5;
      color: #835d27;
    }}

    .pill.status-todo,
    .legend-item.status-todo {{
      background: #7f8c99;
      color: #ffffff;
    }}

    .pill.status-wip,
    .legend-item.status-wip {{
      background: #f4debf;
      color: #8d5d29;
    }}

    .pill.status-bug,
    .legend-item.status-bug {{
      background: #f7d0cc;
      color: #963a35;
    }}

    .pill.status-testing,
    .legend-item.status-testing {{
      background: #dceaff;
      color: #225a9a;
    }}

    .pill.status-done,
    .legend-item.status-done {{
      background: #dcf6e8;
      color: #14734a;
    }}

    .pill.status-drop,
    .legend-item.status-drop {{
      background: #f8ddd7;
      color: #983d23;
    }}

    .pill.status-other,
    .legend-item.status-other {{
      background: #efe3ff;
      color: #6542a9;
    }}

    .pill.status-unspecified,
    .legend-item.status-unspecified {{
      background: #efe6d5;
      color: #835d27;
    }}

    .pill.status-remaining,
    .legend-item.status-remaining {{
      background: rgba(24, 33, 43, 0.12);
      color: #42505f;
    }}

    .text-muted {{
      color: var(--muted);
    }}

    .empty-state {{
      color: var(--muted);
      padding: 18px 4px 4px;
    }}

    a {{
      color: var(--accent);
      text-decoration: none;
    }}

    a:hover {{
      text-decoration: underline;
    }}

    @media (max-width: 980px) {{
      .hero-grid,
      .section-grid,
      .kpi-grid,
      .coverage-grid {{
        grid-template-columns: 1fr;
      }}

      .filters {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <main class="shell">
    <section class="hero">
      <div class="eyebrow">Origamia</div>
      <h1>Avancée du projet</h1>
      <p class="subtitle">Suivi de production des exercices, de la qualité des métadonnées et de la couverture pédagogique à partir de la base SQLite du projet.</p>
      <div class="hero-grid">
        <article class="hero-card">
          <h2>Progression globale</h2>
          <div id="hero-progress-text" class="panel-meta" style="margin-top: 8px; color: rgba(255,255,255,0.86); text-align: left;"></div>
          <div class="progress-bar" id="hero-progress-bar"></div>
          <div id="hero-status-legend" class="legend-list"></div>
          <div id="hero-progress-note" class="panel-meta" style="margin-top: 12px; color: rgba(255,255,255,0.8); text-align: left;"></div>
        </article>
        <div class="hero-stats" id="hero-stats"></div>
      </div>
    </section>

    <section class="panel" style="margin-top: 18px;">
      <div class="panel-header">
        <div>
          <h2 class="panel-title">Repères rapides</h2>
          <div class="panel-meta" id="summary-meta" style="text-align: left;"></div>
        </div>
      </div>
      <div class="kpi-grid" id="kpi-grid"></div>
    </section>

    <section class="panel" style="margin-top: 18px;">
      <div class="panel-header">
        <div>
          <h2 class="panel-title">Cadre de répartition</h2>
          <div class="panel-meta" id="plan-meta" style="text-align: left;"></div>
        </div>
      </div>
      <div class="kpi-grid" id="plan-grid"></div>
    </section>

    <div class="section-grid">
      <section class="panel">
        <div class="panel-header">
          <h2 class="panel-title">Statuts</h2>
          <div class="panel-meta">Répartition des exercices produits</div>
        </div>
        <div id="status-bars" class="bar-list"></div>
      </section>

      <section class="panel">
        <div class="panel-header">
          <h2 class="panel-title">Types</h2>
          <div class="panel-meta">Formats d’exercices</div>
        </div>
        <div id="type-bars" class="bar-list"></div>
      </section>
    </div>

    <div class="section-grid">
      <section class="panel">
        <div class="panel-header">
          <h2 class="panel-title">Piliers vs objectif</h2>
          <div class="panel-meta panel-meta-stack">
            <div>Progression vers la cible prévue pour chaque pilier</div>
            <label class="sort-control">Tri
              <select id="pillar-progress-sort">
                <option value="alpha">Alphabétique</option>
                <option value="completion_desc">Complétion décroissante</option>
              </select>
            </label>
          </div>
        </div>
        <div id="pillar-progress" class="bar-list"></div>
      </section>

      <section class="panel">
        <div class="panel-header">
          <h2 class="panel-title">Métadonnées</h2>
          <div class="panel-meta">Les valeurs `N/A` sont comptées comme volontairement non applicables</div>
        </div>
        <div id="coverage-grid" class="coverage-grid"></div>
      </section>
    </div>

    <section class="panel" style="margin-top: 18px;">
      <div class="panel-header">
        <h2 class="panel-title">Compétences vs objectif</h2>
        <div class="panel-meta panel-meta-stack">
          <div>Progression vers la cible prévue pour chaque compétence</div>
          <label class="sort-control">Tri
            <select id="competence-progress-sort">
              <option value="alpha">Alphabétique</option>
              <option value="completion_desc">Complétion décroissante</option>
            </select>
          </label>
        </div>
      </div>
      <div id="competence-progress" class="bar-list"></div>
    </section>

    <div class="section-grid">
      <section class="panel">
        <div class="panel-header">
          <h2 class="panel-title">Attendus</h2>
          <div class="panel-meta">Répartition actuelle des exercices produits</div>
        </div>
        <div id="attendu-bars" class="bar-list"></div>
      </section>

      <section class="panel">
        <div class="panel-header">
          <h2 class="panel-title">Mises en situation</h2>
          <div class="panel-meta">Rituels mobilisés</div>
        </div>
        <div id="situation-bars" class="bar-list"></div>
      </section>
    </div>

    <div class="section-grid">
      <section class="panel">
        <div class="panel-header">
          <h2 class="panel-title">Répartition par pilier</h2>
          <div class="panel-meta">Part des exercices produits dans chaque pilier</div>
        </div>
        <div id="pillar-bars" class="bar-list"></div>
      </section>

      <section class="panel">
        <div class="panel-header">
          <h2 class="panel-title">Répartition par compétence</h2>
          <div class="panel-meta">Part des exercices produits dans chaque compétence</div>
        </div>
        <div id="competence-bars" class="bar-list"></div>
      </section>
    </div>

    <section class="panel" style="margin-top: 18px;">
      <div class="panel-header">
        <h2 class="panel-title">Catalogue des exercices</h2>
        <div class="panel-meta" id="table-meta" style="text-align: left;"></div>
      </div>
      <div class="filters">
        <input id="search-input" type="search" placeholder="Rechercher un exercice, une compétence, un attendu...">
        <select id="status-filter"></select>
        <select id="pillar-filter"></select>
      </div>
      <div class="table-shell">
        <table>
          <thead>
            <tr>
              <th>N°</th>
              <th>Nom</th>
              <th>Description</th>
              <th>Statut</th>
              <th>Type</th>
              <th>Compétence</th>
              <th>Pilier</th>
              <th>Attendu</th>
              <th>Situation</th>
              <th>Essais</th>
              <th>Source</th>
            </tr>
          </thead>
          <tbody id="exercise-table-body"></tbody>
        </table>
      </div>
      <div id="table-empty" class="empty-state" hidden>Aucun exercice ne correspond aux filtres actuels.</div>
    </section>
  </main>

  <script id="dashboard-data" type="application/json">{stats_json}</script>
  <script>
    const data = JSON.parse(document.getElementById('dashboard-data').textContent);
    const summary = data.summary;
    const statusSummary = data.status_summary;
    const plan = data.plan;
    const allExercises = data.exercises;
    const statusToneMap = {{
      'TODO': 'todo',
      'WIP': 'wip',
      'BUG': 'bug',
      'TESTING': 'testing',
      'DONE': 'done',
      'DROP': 'drop',
      'Autre': 'other',
      'Non renseigné': 'unspecified',
      'Non créé': 'remaining',
    }};

    const numberFormatter = new Intl.NumberFormat('fr-FR');
    const dateFormatter = new Intl.DateTimeFormat('fr-FR', {{
      dateStyle: 'long',
      timeStyle: 'short'
    }});

    function formatNumber(value) {{
      return numberFormatter.format(value || 0);
    }}

    function formatRatio(value) {{
      return `${{(value || 0).toFixed(1)}} %`;
    }}

    function formatDate(value) {{
      if (!value) {{
        return 'Date inconnue';
      }}

      const date = new Date(value);
      if (Number.isNaN(date.getTime())) {{
        return value;
      }}

      return dateFormatter.format(date);
    }}

    function getStatusTone(label, fallback = 'other') {{
      return statusToneMap[label] || fallback;
    }}

    function createStatusPill(label, tone = null) {{
      const pill = document.createElement('span');
      pill.className = `pill status-${{tone || getStatusTone(label)}}`;
      pill.textContent = label;
      return pill;
    }}

    function renderHeroProgress() {{
      const bar = document.getElementById('hero-progress-bar');
      const legend = document.getElementById('hero-status-legend');
      bar.innerHTML = '';
      legend.innerHTML = '';

      for (const segment of statusSummary.segments) {{
        const block = document.createElement('div');
        block.className = `progress-segment ${{segment.tone}}`;
        block.style.flexBasis = `${{Math.max(segment.ratio, 0)}}%`;
        block.title = `${{segment.label}} : ${{formatNumber(segment.value)}}`;
        bar.appendChild(block);

        const legendItem = document.createElement('div');
        legendItem.className = `legend-item status-${{segment.tone}}`;

        const dot = document.createElement('span');
        dot.className = `legend-dot progress-segment ${{segment.tone}}`;

        const text = document.createElement('span');
        text.textContent = `${{segment.label}} · ${{formatNumber(segment.value)}}`;

        legendItem.append(dot, text);
        legend.appendChild(legendItem);
      }}
    }}

    function createBarList(targetId, rows, variant = 'accent') {{
      const container = document.getElementById(targetId);
      container.innerHTML = '';

      if (!rows.length) {{
        container.innerHTML = '<div class="empty-state">Aucune donnée disponible.</div>';
        return;
      }}

      const max = Math.max(...rows.map((row) => row.value), 1);

      for (const row of rows) {{
        const item = document.createElement('article');
        item.className = 'bar-row';

        const header = document.createElement('header');

        const label = document.createElement('strong');
        label.textContent = row.label;

        const value = document.createElement('span');
        value.textContent = `${{formatNumber(row.value)}} (${{
          formatRatio(row.ratio)
        }})`;

        const track = document.createElement('div');
        track.className = 'bar-track';

        const fill = document.createElement('div');
        if (row.tone) {{
          fill.className = `bar-fill ${{row.tone}}`;
        }} else {{
          fill.className = `bar-fill${{variant === 'warm' ? ' warm' : ''}}`;
        }}
        fill.style.width = `${{(row.value / max) * 100}}%`;

        track.appendChild(fill);
        header.append(label, value);
        item.append(header, track);
        container.appendChild(item);
      }}
    }}

    function sortProgressRows(rows, mode) {{
      const items = [...rows];
      if (mode === 'completion_desc') {{
        items.sort((left, right) => {{
          if (right.completion_ratio !== left.completion_ratio) {{
            return right.completion_ratio - left.completion_ratio;
          }}
          if (right.tracked_ratio !== left.tracked_ratio) {{
            return right.tracked_ratio - left.tracked_ratio;
          }}
          return left.label.localeCompare(right.label, 'fr');
        }});
        return items;
      }}

      items.sort((left, right) => left.label.localeCompare(right.label, 'fr'));
      return items;
    }}

    function createProgressList(targetId, rows, sortMode = 'alpha') {{
      const container = document.getElementById(targetId);
      container.innerHTML = '';

      if (!rows.length) {{
        container.innerHTML = '<div class="empty-state">Aucune donnée disponible.</div>';
        return;
      }}

      for (const row of sortProgressRows(rows, sortMode)) {{
        const item = document.createElement('article');
        item.className = 'bar-row';

        const header = document.createElement('header');

        const label = document.createElement('strong');
        label.textContent = row.label;

        const value = document.createElement('span');
        value.textContent = `${{formatNumber(row.built)}} / ${{
          formatNumber(row.target)
        }}`;

        const track = document.createElement('div');
        track.className = 'bar-track';

        for (const segment of row.segments) {{
          const fill = document.createElement('div');
          fill.className = `bar-fill ${{segment.tone}}`;
          fill.style.flex = `0 1 ${{Math.max(segment.ratio, 0)}}%`;
          fill.title = `${{segment.label}} : ${{formatNumber(segment.value)}}`;
          track.appendChild(fill);
        }}

        const legend = document.createElement('div');
        legend.className = 'row-legend';

        for (const segment of row.segments) {{
          legend.appendChild(
            createStatusPill(`${{segment.label}} · ${{formatNumber(segment.value)}}`, segment.tone)
          );
        }}

        const meta = document.createElement('div');
        meta.className = 'coverage-meta';
        meta.textContent = `Complétion : ${{
          formatRatio(row.completion_ratio)
        }} · Exercices saisis : ${{
          formatRatio(row.tracked_ratio)
        }}.`;

        header.append(label, value);
        item.append(header, track, legend, meta);
        container.appendChild(item);
      }}
    }}

    function renderProgressSections() {{
      createProgressList(
        'pillar-progress',
        data.progressions.pillar,
        document.getElementById('pillar-progress-sort').value
      );
      createProgressList(
        'competence-progress',
        data.progressions.competence,
        document.getElementById('competence-progress-sort').value
      );
    }}

    function renderCoverage() {{
      const container = document.getElementById('coverage-grid');
      container.innerHTML = '';

      for (const entry of data.coverage) {{
        const card = document.createElement('article');
        card.className = 'coverage-item';

        const top = document.createElement('div');
        top.className = 'coverage-top';

        const label = document.createElement('strong');
        label.textContent = entry.label;

        const ratio = document.createElement('span');
        ratio.textContent = formatRatio(entry.ratio);

        const track = document.createElement('div');
        track.className = 'bar-track';

        const fill = document.createElement('div');
        fill.className = 'bar-fill warm';
        fill.style.width = `${{entry.ratio}}%`;

        const meta = document.createElement('div');
        meta.className = 'coverage-meta';
        meta.textContent = `${{formatNumber(entry.filled)}} renseigné(s), ${{
          formatNumber(entry.na_value)
        }} en N/A, ${{
          formatNumber(entry.missing)
        }} manquant(s)`;

        top.append(label, ratio);
        track.appendChild(fill);
        card.append(top, track, meta);
        container.appendChild(card);
      }}
    }}

    function renderHero() {{
      document.getElementById('hero-progress-text').textContent =
        `${{formatNumber(summary.built_count)}} exercice(s) saisis sur ${{
          formatNumber(summary.target_count)
        }}, dont ${{formatNumber(summary.completed_count)}} clôturé(s).`;
      document.getElementById('hero-progress-note').textContent =
        `${{formatNumber(summary.active_count)}} encore actif(s) (TODO, WIP, BUG, TESTING) et ${{
          formatNumber(summary.remaining_count)
        }} encore non créé(s) pour atteindre l’objectif global.`;
      renderHeroProgress();

      const heroStats = [
        ['Clôturés', `${{formatNumber(summary.completed_count)}} (${{
          formatRatio(summary.completion_ratio)
        }})`],
        ['Exercices saisis', `${{formatNumber(summary.built_count)}} (${{
          formatRatio(summary.tracked_ratio)
        }})`],
        ['Métadonnées complètes', formatRatio(summary.overall_metadata_ratio)],
        ['Dernier build', formatDate(summary.last_build_at)],
      ];

      const container = document.getElementById('hero-stats');
      container.innerHTML = '';

      for (const [labelText, valueText] of heroStats) {{
        const card = document.createElement('article');
        card.className = 'hero-stat';

        const label = document.createElement('span');
        label.className = 'hero-stat-label';
        label.textContent = labelText;

        const value = document.createElement('span');
        value.className = 'hero-stat-value';
        value.textContent = valueText;

        card.append(label, value);
        container.appendChild(card);
      }}
    }}

    function renderKpis() {{
      const items = [
        {{
          label: 'Exercices saisis',
          value: formatNumber(summary.built_count),
          note: 'Nombre d’entrées actuellement présentes dans la base projet, quel que soit leur statut.'
        }},
        {{
          label: 'Exercices clôturés',
          value: formatNumber(summary.completed_count),
          note: 'Exercices passés en DONE ou DROP dans le suivi éditorial.'
        }},
        {{
          label: 'Exercices non créés',
          value: formatNumber(summary.remaining_count),
          note: 'Exercices encore absents de la base par rapport à la cible projet.'
        }},
        {{
          label: 'Qualité métadonnées',
          value: formatRatio(summary.overall_metadata_ratio),
          note: 'Taux de champs renseignés ou explicitement marqués N/A dans le dashboard.'
        }},
      ];

      const container = document.getElementById('kpi-grid');
      container.innerHTML = '';

      for (const itemData of items) {{
        const card = document.createElement('article');
        card.className = 'kpi';

        const label = document.createElement('div');
        label.className = 'kpi-label';
        label.textContent = itemData.label;

        const value = document.createElement('span');
        value.className = 'kpi-value';
        value.textContent = itemData.value;

        const note = document.createElement('div');
        note.className = 'kpi-note';
        note.textContent = itemData.note;

        card.append(label, value, note);
        container.appendChild(card);
      }}

      document.getElementById('summary-meta').textContent =
        `La barre principale représente la cible totale, segmentée par statut plutôt que par simple existence d’un fichier.`;
    }}

    function renderPlan() {{
      const items = [
        {{
          label: 'Cible projet',
          value: formatNumber(plan.total_target_count),
          note: 'Nombre total d’exercices visés à ce stade du projet.'
        }},
        {{
          label: 'Répartition cadrée',
          value: formatNumber(plan.structured_target_count),
          note: 'Volume déjà réparti entre piliers, compétences et attendus.'
        }},
        {{
          label: 'Hors répartition',
          value: formatNumber(plan.overflow_target_count),
          note: 'Exercices prévus mais pas encore affectés à la répartition détaillée.'
        }},
        {{
          label: 'Piliers',
          value: `${{formatNumber(plan.pillar_count)}} x ${{formatNumber(plan.pillar_target_count)}}`,
          note: 'Objectif uniforme par pilier dans la partie répartie.'
        }},
        {{
          label: 'Compétences',
          value: `${{formatNumber(plan.competence_count)}} x ${{formatNumber(plan.competence_target_count)}}`,
          note: 'Chaque compétence vise 9 exercices.'
        }},
        {{
          label: 'Attendus',
          value: `${{formatNumber(plan.attendu_count)}} x ${{formatNumber(plan.attendu_target_count)}}`,
          note: 'Chaque attendu vise 3 exercices.'
        }},
      ];

      const container = document.getElementById('plan-grid');
      container.innerHTML = '';

      for (const itemData of items) {{
        const card = document.createElement('article');
        card.className = 'kpi';

        const label = document.createElement('div');
        label.className = 'kpi-label';
        label.textContent = itemData.label;

        const value = document.createElement('span');
        value.className = 'kpi-value';
        value.textContent = itemData.value;

        const note = document.createElement('div');
        note.className = 'kpi-note';
        note.textContent = itemData.note;

        card.append(label, value, note);
        container.appendChild(card);
      }}

      document.getElementById('plan-meta').textContent =
        `La répartition détaillée couvre ${{
          formatNumber(plan.structured_target_count)
        }} exercices; ${{
          formatNumber(plan.overflow_target_count)
        }} seront suivis à part pour l’instant.`;
    }}

    function appendValueContent(cell, value) {{
      if (value === 'N/A') {{
        const pill = document.createElement('span');
        pill.className = 'pill na';
        pill.textContent = value;
        cell.appendChild(pill);
        return;
      }}

      if (value === 'Non renseigné') {{
        const text = document.createElement('span');
        text.className = 'text-muted';
        text.textContent = value;
        cell.appendChild(text);
        return;
      }}

      cell.textContent = value;
    }}

    function populateSelect(selectId, values, placeholder) {{
      const select = document.getElementById(selectId);
      select.innerHTML = '';

      const firstOption = document.createElement('option');
      firstOption.value = '';
      firstOption.textContent = placeholder;
      select.appendChild(firstOption);

      for (const value of values) {{
        const option = document.createElement('option');
        option.value = value;
        option.textContent = value;
        select.appendChild(option);
      }}
    }}

    function renderTable(rows) {{
      const body = document.getElementById('exercise-table-body');
      const empty = document.getElementById('table-empty');
      body.innerHTML = '';

      if (!rows.length) {{
        empty.hidden = false;
        return;
      }}

      empty.hidden = true;

      for (const row of rows) {{
        const tr = document.createElement('tr');

        const numberCell = document.createElement('td');
        numberCell.className = 'number';
        numberCell.textContent = row.number;

        const nameCell = document.createElement('td');
        nameCell.textContent = row.nom;

        const descriptionCell = document.createElement('td');
        appendValueContent(descriptionCell, row.description);

        const statusCell = document.createElement('td');
        const statusPill = createStatusPill(row.statut);
        statusCell.appendChild(statusPill);

        const typeCell = document.createElement('td');
        const typePill = document.createElement('span');
        typePill.className = 'pill muted';
        typePill.textContent = row.type;
        typeCell.appendChild(typePill);

        const competenceCell = document.createElement('td');
        appendValueContent(competenceCell, row.competence);

        const pillarCell = document.createElement('td');
        appendValueContent(pillarCell, row.pilier);

        const attenduCell = document.createElement('td');
        appendValueContent(attenduCell, row.attendu);

        const situationCell = document.createElement('td');
        appendValueContent(situationCell, row.situation);

        const attemptsCell = document.createElement('td');
        attemptsCell.textContent = row.max_attempts || 1;

        const sourceCell = document.createElement('td');
        if (row.source_href) {{
          const link = document.createElement('a');
          link.href = row.source_href;
          link.textContent = row.source_path;
          sourceCell.appendChild(link);
        }} else {{
          sourceCell.textContent = row.source_path;
        }}

        tr.append(
          numberCell,
          nameCell,
          descriptionCell,
          statusCell,
          typeCell,
          competenceCell,
          pillarCell,
          attenduCell,
          situationCell,
          attemptsCell,
          sourceCell
        );

        body.appendChild(tr);
      }}

      document.getElementById('table-meta').textContent =
        `${{formatNumber(rows.length)}} exercice(s) affiché(s)`;
    }}

    function applyFilters() {{
      const query = document.getElementById('search-input').value.trim().toLowerCase();
      const status = document.getElementById('status-filter').value;
      const pillar = document.getElementById('pillar-filter').value;

      const filtered = allExercises.filter((exercise) => {{
        if (status && exercise.statut !== status) {{
          return false;
        }}

        if (pillar && exercise.pilier !== pillar) {{
          return false;
        }}

        if (!query) {{
          return true;
        }}

        const haystack = [
          exercise.number,
          exercise.nom,
          exercise.description,
          exercise.statut,
          exercise.type,
          exercise.competence,
          exercise.pilier,
          exercise.attendu,
          exercise.situation,
          exercise.max_attempts,
          exercise.source_path,
        ].join(' ').toLowerCase();

        return haystack.includes(query);
      }});

      renderTable(filtered);
    }}

    function initFilters() {{
      const statuses = [...new Set(allExercises.map((item) => item.statut))].sort((a, b) => a.localeCompare(b, 'fr'));
      const pillars = [...new Set(allExercises.map((item) => item.pilier))].sort((a, b) => a.localeCompare(b, 'fr'));

      populateSelect('status-filter', statuses, 'Tous les statuts');
      populateSelect('pillar-filter', pillars, 'Tous les piliers');

      document.getElementById('search-input').addEventListener('input', applyFilters);
      document.getElementById('status-filter').addEventListener('change', applyFilters);
      document.getElementById('pillar-filter').addEventListener('change', applyFilters);
      document.getElementById('pillar-progress-sort').addEventListener('change', renderProgressSections);
      document.getElementById('competence-progress-sort').addEventListener('change', renderProgressSections);
    }}

    renderHero();
    renderKpis();
    renderPlan();
    renderCoverage();
    createBarList('status-bars', data.distributions.status, 'accent');
    createBarList('type-bars', data.distributions.type, 'warm');
    createBarList('pillar-bars', data.distributions.pillar, 'accent');
    createBarList('competence-bars', data.distributions.competence, 'accent');
    createBarList('attendu-bars', data.distributions.attendu, 'warm');
    createBarList('situation-bars', data.distributions.situation, 'accent');
    renderProgressSections();
    initFilters();
    applyFilters();
  </script>
</body>
</html>
"""


def main() -> None:
    args = parse_args()
    project_db = Path(args.db)
    output_dir = Path(args.out_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(project_db)
    conn.row_factory = sqlite3.Row
    try:
        data = build_dashboard_data(conn, output_dir)
    finally:
        conn.close()

    stats_path = output_dir / "stats.json"
    html_path = output_dir / "index.html"

    stats_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    html_path.write_text(build_html(data), encoding="utf-8")

    print(f"Wrote dashboard to {html_path}")


if __name__ == "__main__":
    main()
