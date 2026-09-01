#!/usr/bin/env python3
"""Generate a functional-chain diagram as a standalone SVG."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


ICON_SYMBOLS = {
    "water-level": """
      <symbol id="icon-water-level" viewBox="0 0 140 190">
        <rect x="24" y="12" width="92" height="48" rx="12" fill="#e0f2fe" stroke="#0369a1" stroke-width="6"/>
        <circle cx="43" cy="36" r="7" fill="#22c55e"/>
        <path d="M65 36h30" stroke="#0369a1" stroke-width="6" stroke-linecap="round"/>
        <path d="M47 60v112M93 60v88" stroke="#64748b" stroke-width="10" stroke-linecap="round"/>
        <path d="M47 151v21M93 127v21" stroke="#fbbf24" stroke-width="10" stroke-linecap="round"/>
      </symbol>
    """,
    "controller": """
      <symbol id="icon-controller" viewBox="0 0 160 150">
        <rect x="16" y="8" width="128" height="112" rx="20" fill="#14b8a6" stroke="#0f766e" stroke-width="6"/>
        <g fill="#f8fafc">
          <circle cx="52" cy="42" r="6"/><circle cx="80" cy="42" r="6"/><circle cx="108" cy="42" r="6"/>
          <circle cx="52" cy="66" r="6"/><circle cx="80" cy="66" r="6"/><circle cx="108" cy="66" r="6"/>
          <circle cx="52" cy="90" r="6"/><circle cx="80" cy="90" r="6"/><circle cx="108" cy="90" r="6"/>
        </g>
        <circle cx="38" cy="129" r="11" fill="#fbbf24" stroke="#a16207" stroke-width="4"/>
        <circle cx="80" cy="129" r="11" fill="#fbbf24" stroke="#a16207" stroke-width="4"/>
        <circle cx="122" cy="129" r="11" fill="#fbbf24" stroke="#a16207" stroke-width="4"/>
      </symbol>
    """,
    "pump": """
      <symbol id="icon-pump" viewBox="0 0 180 150">
        <path d="M28 64h20M132 64h20" stroke="#475569" stroke-width="16" stroke-linecap="round"/>
        <rect x="44" y="28" width="92" height="92" rx="22" fill="#fb923c" stroke="#c2410c" stroke-width="7"/>
        <circle cx="90" cy="74" r="29" fill="#fff7ed" stroke="#c2410c" stroke-width="6"/>
        <path d="M90 49v50M65 74h50" stroke="#ea580c" stroke-width="7" stroke-linecap="round"/>
        <path d="M61 121h58l13 18H48z" fill="#475569"/>
      </symbol>
    """,
    "bird": """
      <symbol id="icon-bird" viewBox="0 0 150 110">
        <ellipse cx="70" cy="67" rx="48" ry="32" fill="#fbbf24" stroke="#92400e" stroke-width="5"/>
        <circle cx="106" cy="39" r="25" fill="#fde68a" stroke="#92400e" stroke-width="5"/>
        <path d="M130 38l18 9-18 8z" fill="#f97316" stroke="#9a3412" stroke-width="3"/>
        <circle cx="112" cy="33" r="4" fill="#0f172a"/>
        <path d="M54 59c18-18 40 3 28 25-19 8-34-6-28-25z" fill="#f59e0b" stroke="#92400e" stroke-width="4"/>
        <path d="M28 65L7 48l8 30z" fill="#f59e0b" stroke="#92400e" stroke-width="4"/>
        <path d="M66 96v12M91 94v14" stroke="#92400e" stroke-width="4" stroke-linecap="round"/>
      </symbol>
    """,
}


def escape(value: object) -> str:
    return html.escape(str(value), quote=True)


def load_spec(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    nodes = data.get("nodes")
    arrows = data.get("arrows")
    if not isinstance(nodes, list) or len(nodes) < 2:
        raise ValueError("The specification must contain at least two nodes.")
    if not isinstance(arrows, list) or len(arrows) != len(nodes) - 1:
        raise ValueError("The specification must contain one arrow between each pair of nodes.")
    for node in nodes:
        if node.get("icon") not in ICON_SYMBOLS:
            raise ValueError(f"Unknown icon: {node.get('icon')}")
        if not node.get("ref"):
            raise ValueError("Every node must have a ref.")
    return data


def badge(letter: str, x: int, y: int) -> str:
    return (
        f'<circle cx="{x}" cy="{y}" r="25" fill="#0f172a" stroke="#ffffff" stroke-width="5"/>'
        f'<text x="{x}" y="{y + 9}" text-anchor="middle" font-family="Arial, sans-serif" '
        f'font-size="27" font-weight="700" fill="#ffffff">{escape(letter)}</text>'
    )


def build_birdbath_svg(spec: dict[str, object]) -> str:
    title = escape(spec.get("title", "Abreuvoir automatique"))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="640" viewBox="0 0 1200 640" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">Schema d'un abreuvoir automatique montrant une sonde dans l'eau, une carte programmable et une pompe reliee a un reservoir.</desc>
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eff6ff"/><stop offset="1" stop-color="#f8fafc"/></linearGradient>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7dd3fc"/><stop offset="1" stop-color="#0284c7"/></linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="8" stdDeviation="7" flood-color="#0f172a" flood-opacity="0.16"/></filter>
    <marker id="arrow-information" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0l10 5-10 5z" fill="#2563eb"/></marker>
    <marker id="arrow-action" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0l10 5-10 5z" fill="#ea580c"/></marker>
    {''.join(ICON_SYMBOLS.values())}
  </defs>

  <rect width="1200" height="640" rx="28" fill="url(#sky)"/>
  <circle cx="1080" cy="92" r="52" fill="#fde68a" opacity="0.75"/>
  <path d="M0 530Q190 495 380 530t380 0 440 0v110H0z" fill="#dcfce7"/>
  <path d="M0 557Q220 525 430 555t390 0 380 0" fill="none" stroke="#86efac" stroke-width="5"/>

  <!-- Water circuit behind the components. -->
  <path d="M1020 448H948" fill="none" stroke="#0284c7" stroke-width="14" stroke-linecap="round"/>
  <path d="M790 448H730V510H440" fill="none" stroke="#0284c7" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Reservoir. -->
  <g filter="url(#shadow)">
    <rect x="1010" y="305" width="142" height="234" rx="24" fill="#e2e8f0" stroke="#475569" stroke-width="7"/>
    <path d="M1020 378h122v146a10 10 0 0 1-10 10h-102a10 10 0 0 1-10-10z" fill="url(#water)" opacity="0.9"/>
    <path d="M1022 379c20-13 39 13 59 0s39 13 59 0" fill="none" stroke="#bae6fd" stroke-width="7"/>
    <rect x="1043" y="283" width="76" height="28" rx="10" fill="#64748b"/>
  </g>

  <!-- Bird bath. -->
  <g filter="url(#shadow)">
    <path d="M115 390Q300 445 485 390l-34 107q-151 75-302 0z" fill="#e2e8f0" stroke="#64748b" stroke-width="8"/>
    <ellipse cx="300" cy="390" rx="185" ry="48" fill="url(#water)" stroke="#0369a1" stroke-width="8"/>
    <path d="M153 386c44-25 86 25 130 0s86 25 130 0 55 3 67 0" fill="none" stroke="#bae6fd" stroke-width="8" stroke-linecap="round"/>
    <path d="M250 510h100l22 83H228z" fill="#cbd5e1" stroke="#64748b" stroke-width="8"/>
  </g>
  <use href="#icon-bird" x="112" y="260" width="150" height="110"/>

  <!-- Sensor A is physically immersed in the bath. -->
  <use href="#icon-water-level" x="320" y="190" width="140" height="190" filter="url(#shadow)"/>
  {badge('A', 342, 182)}

  <!-- Controller B is mounted next to the bath. -->
  <rect x="563" y="381" width="18" height="172" rx="9" fill="#64748b"/>
  <use href="#icon-controller" x="490" y="225" width="160" height="150" filter="url(#shadow)"/>
  {badge('B', 492, 216)}

  <!-- Pump C connects the reservoir to the bath. -->
  <use href="#icon-pump" x="780" y="372" width="180" height="150" filter="url(#shadow)"/>
  {badge('C', 850, 356)}

  <!-- Information and command paths. -->
  <path d="M430 225C462 166 493 169 513 229" fill="none" stroke="#2563eb" stroke-width="6" stroke-linecap="round" marker-end="url(#arrow-information)"/>
  <rect x="434" y="118" width="133" height="38" rx="19" fill="#ffffff" opacity="0.94"/>
  <text x="500" y="145" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#1d4ed8">information</text>

  <path d="M638 292C716 280 755 322 815 398" fill="none" stroke="#ea580c" stroke-width="6" stroke-linecap="round" marker-end="url(#arrow-action)"/>
  <rect x="680" y="264" width="125" height="38" rx="19" fill="#ffffff" opacity="0.94"/>
  <text x="742" y="291" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#c2410c">commande</text>
</svg>
'''


def build_svg(spec: dict[str, object]) -> str:
    scene = spec.get("scene")
    if scene == "birdbath":
        return build_birdbath_svg(spec)
    raise ValueError(f"Unknown scene: {scene}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    spec = load_spec(args.spec)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_svg(spec), encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
