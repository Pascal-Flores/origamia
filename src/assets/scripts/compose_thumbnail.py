#!/usr/bin/env python3
"""Compose an isolated transparent illustration on Origamia's fixed template."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw

ASSETS = Path(__file__).resolve().parents[1]
LAYOUT = ASSETS / "thumbnails" / "layout.json"


def template(layout: dict) -> Image.Image:
    scale = layout["supersampling"]
    size = (layout["width"], layout["height"])
    circle = layout["circle"]
    radius = circle["diameter"] / 2
    mask = Image.new("L", (size[0] * scale, size[1] * scale))
    ImageDraw.Draw(mask).ellipse(
        (
            round((circle["center_x"] - radius) * scale),
            round((circle["center_y"] - radius) * scale),
            round((circle["center_x"] + radius) * scale) - 1,
            round((circle["center_y"] + radius) * scale) - 1,
        ),
        fill=255,
    )
    mask = mask.resize(size, Image.Resampling.LANCZOS)
    result = Image.new("RGB", size, layout["background"])
    result.paste(circle["fill"], (0, 0), mask)
    return result


def compose(illustration: Image.Image, background: Image.Image, layout: dict) -> Image.Image:
    illustration = illustration.convert("RGBA")
    alpha = illustration.getchannel("A")
    if alpha.getextrema()[0] != 0:
        raise ValueError("L’illustration doit avoir un fond transparent (canal alpha).")
    # Generated PNGs can contain nearly invisible pixels far outside the object.
    # Ignore that alpha noise when measuring its visible size and center.
    threshold = layout.get("alpha_bounds_threshold", 8)
    bounds = alpha.point(lambda value: 255 if value >= threshold else 0).getbbox()
    if bounds is None:
        raise ValueError("L’illustration ne contient aucun pixel suffisamment visible.")
    illustration = illustration.crop(bounds)
    box = layout["illustration_box"]
    scale = layout["supersampling"]
    ratio = min(box["width"] / illustration.width, box["height"] / illustration.height)
    size = (max(1, round(illustration.width * ratio * scale)),
            max(1, round(illustration.height * ratio * scale)))
    illustration = illustration.resize(size, Image.Resampling.LANCZOS)
    layer = Image.new("RGBA", (background.width * scale, background.height * scale))
    circle = layout["circle"]
    position = (round(circle["center_x"] * scale - size[0] / 2),
                round(circle["center_y"] * scale - size[1] / 2))
    layer.paste(illustration, position)
    layer = layer.resize(background.size, Image.Resampling.LANCZOS)
    return Image.alpha_composite(background.convert("RGBA"), layer).convert("RGB")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("illustration", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--save-template", type=Path, help="Exporter aussi le fond seul.")
    args = parser.parse_args()
    layout = json.loads(LAYOUT.read_text())
    background = template(layout)
    with Image.open(args.illustration) as illustration:
        result = compose(illustration, background, layout)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result.save(args.output)
    if args.save_template:
        args.save_template.parent.mkdir(parents=True, exist_ok=True)
        background.save(args.save_template)
    print(args.output)


if __name__ == "__main__":
    main()
