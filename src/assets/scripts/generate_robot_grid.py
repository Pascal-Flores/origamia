#!/usr/bin/env python3
"""Generate a minimal SVG grid for robot displacement exercises."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

COLORS = {
    "bleu": ("#dbeafe", "#2563eb"),
    "green": ("#dcfce7", "#16a34a"),
    "vert": ("#dcfce7", "#16a34a"),
    "jaune": ("#fef3c7", "#d97706"),
    "orange": ("#ffedd5", "#ea580c"),
    "rouge": ("#fee2e2", "#dc2626"),
    "violet": ("#ede9fe", "#7c3aed"),
}
DIRECTION_ANGLES = {
    "n": 0,
    "nord": 0,
    "e": 90,
    "est": 90,
    "s": 180,
    "sud": 180,
    "o": 270,
    "ouest": 270,
}


def parse_cell(value: str, columns: int, rows: int) -> tuple[int, int]:
    cell = value.strip().upper()
    if len(cell) < 2 or not cell[0].isalpha() or not cell[1:].isdigit():
        raise argparse.ArgumentTypeError(f"Invalid cell: {value}")
    col = ord(cell[0]) - ord("A")
    row = int(cell[1:]) - 1
    if col < 0 or col >= columns or row < 0 or row >= rows:
        raise argparse.ArgumentTypeError(f"Cell outside grid: {value}")
    return col, row


def parse_target(raw: str, columns: int, rows: int) -> tuple[int, int, str]:
    parts = raw.split(":") if ":" in raw else raw.split(maxsplit=2)
    if len(parts) not in {2, 3}:
        raise argparse.ArgumentTypeError(
            "Target must be CASE:COLOR or CASE COLOR, with an optional label."
        )
    color = parts[1].lower()
    if color not in COLORS:
        raise argparse.ArgumentTypeError(f"Unknown color: {parts[1]}")
    col, row = parse_cell(parts[0], columns, rows)
    return col, row, color


def parse_spec(source: str) -> dict[str, object]:
    values: dict[str, object] = {"targets": []}
    for line_number, raw_line in enumerate(source.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Line {line_number}: expected 'key: value'")
        key, raw_value = line.split(":", 1)
        key = key.strip().lower()
        value = raw_value.strip()
        if key in {"target", "arrival", "arrivee"}:
            values["targets"].append(value)
        else:
            values[key] = value

    if "grid" in values:
        match = re.fullmatch(r"(\d+)\s*[xX]\s*(\d+)", str(values["grid"]))
        if not match:
            raise ValueError("grid must be formatted as COLUMNSxROWS, for example 5x4")
        values["columns"] = int(match.group(1))
        values["rows"] = int(match.group(2))

    if "start" in values:
        parts = str(values["start"]).rsplit(maxsplit=1)
        if len(parts) != 2:
            raise ValueError("start must contain a cell and a direction, for example B4 nord")
        values["start"], values["direction"] = parts

    return values


def build_svg(args: argparse.Namespace) -> str:
    cell = args.cell_size
    padding = 8
    width = args.columns * cell + padding * 2
    height = args.rows * cell + padding * 2
    start_col, start_row = parse_cell(args.start, args.columns, args.rows)
    targets = [parse_target(raw, args.columns, args.rows) for raw in args.targets]

    pieces = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
    ]

    for row in range(args.rows):
        for col in range(args.columns):
            x = padding + col * cell
            y = padding + row * cell
            pieces.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" '
                'fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>'
            )

    for col, row, color in targets:
        fill, stroke = COLORS[color]
        x = padding + col * cell + 4
        y = padding + row * cell + 4
        pieces.append(
            f'<rect x="{x}" y="{y}" width="{cell - 8}" height="{cell - 8}" '
            f'rx="6" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
        )

    center_x = padding + start_col * cell + cell / 2
    center_y = padding + start_row * cell + cell / 2
    arrow_size = cell * 0.34
    tip_y = center_y - arrow_size
    base_y = center_y + arrow_size * 0.55
    wing = arrow_size * 0.62
    stem = arrow_size * 0.24
    points = (
        f"{center_x},{tip_y} "
        f"{center_x + wing},{center_y} "
        f"{center_x + stem},{center_y} "
        f"{center_x + stem},{base_y} "
        f"{center_x - stem},{base_y} "
        f"{center_x - stem},{center_y} "
        f"{center_x - wing},{center_y}"
    )
    angle = DIRECTION_ANGLES[args.direction.lower()]
    pieces.append(
        f'<polygon points="{points}" fill="#111827" '
        f'transform="rotate({angle} {center_x} {center_y})"/>'
    )
    pieces.append("</svg>")
    return "\n".join(pieces) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--spec",
        help="Read a robot-grid specification from this file, or use '-' for standard input.",
    )
    parser.add_argument("--title", help="Accepted for compatibility; not rendered.")
    parser.add_argument("--columns", type=int)
    parser.add_argument("--rows", type=int)
    parser.add_argument("--cell-size", type=int)
    parser.add_argument("--start")
    parser.add_argument("--direction", choices=sorted(DIRECTION_ANGLES))
    parser.add_argument(
        "--target",
        dest="targets",
        action="append",
        help="Colored cell in the form CASE:COLOR or CASE COLOR.",
    )
    args = parser.parse_args()
    if args.spec:
        source = sys.stdin.read() if args.spec == "-" else Path(args.spec).read_text(encoding="utf-8")
        try:
            values = parse_spec(source)
        except ValueError as error:
            parser.error(str(error))
        for field in ("columns", "rows", "start", "direction", "cell_size"):
            spec_field = field.replace("_", "-")
            value = values.get(field, values.get(spec_field))
            if getattr(args, field) is None and value is not None:
                setattr(args, field, value)
        if args.targets is None:
            args.targets = list(values["targets"])

    args.columns = args.columns or 5
    args.rows = args.rows or 4
    args.cell_size = args.cell_size or 66
    args.direction = args.direction or "nord"
    if not args.start:
        parser.error("a start cell is required")
    if not args.targets:
        parser.error("at least one target cell is required")
    if args.columns < 1 or args.columns > 26 or args.rows < 1:
        parser.error("Grid dimensions must be positive, with at most 26 columns.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_svg(args), encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
