#!/usr/bin/env python3
"""Generate the AdaCraft projects used by exercises 145 to 151."""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REFERENCE_PROJECT = ROOT / "Projet.sb3"
OUTPUT_DIR = (
    ROOT
    / "src"
    / "exercises"
    / "pil-programmation-outil"
    / "cmp-programmer-simulations"
)


SHADOW_STAGE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#69bce8"/>
      <stop offset="0.7" stop-color="#bfe7f3"/>
      <stop offset="1" stop-color="#f5e6bd"/>
    </linearGradient>
    <linearGradient id="court" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#d9c9a7"/>
      <stop offset="1" stop-color="#ae9877"/>
    </linearGradient>
    <linearGradient id="post" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#204f69"/>
      <stop offset="0.45" stop-color="#4387a6"/>
      <stop offset="1" stop-color="#173d55"/>
    </linearGradient>
  </defs>

  <rect width="480" height="225" fill="url(#sky)"/>
  <path d="M0 163c55-35 104-20 147 5 54 31 91 17 139-7 69-35 128-20 194 17v58H0z" fill="#7aae70"/>
  <path d="M0 187c68-28 119 1 173 17 63 19 107-17 163-22 54-5 97 13 144 42v25H0z" fill="#5f965e"/>

  <g fill="#ffffff" opacity="0.82">
    <path d="M34 73c5-15 25-20 36-8 7-13 29-12 36 3 15-4 27 7 28 19H30c-1-6 0-10 4-14z"/>
    <path d="M334 55c5-13 21-17 31-7 8-12 27-10 32 4 14-3 24 7 25 17h-91c-1-6 0-10 3-14z"/>
  </g>

  <g transform="translate(24 142)">
    <rect x="0" y="24" width="104" height="61" rx="3" fill="#e8d7ba" stroke="#8b7560" stroke-width="4"/>
    <path d="M-5 27L52 0l57 27z" fill="#bd614e" stroke="#7d4039" stroke-width="4"/>
    <rect x="14" y="44" width="22" height="23" fill="#88bed2" stroke="#55798c" stroke-width="3"/>
    <rect x="67" y="44" width="22" height="23" fill="#88bed2" stroke="#55798c" stroke-width="3"/>
    <rect x="44" y="52" width="17" height="33" fill="#765b4b"/>
  </g>

  <rect y="222" width="480" height="138" fill="url(#court)"/>
  <path d="M0 222h480" stroke="#7c8d68" stroke-width="7"/>
  <g fill="none" stroke="#c1af8f" stroke-width="2" opacity="0.8">
    <path d="M0 271h480M0 324h480"/>
    <path d="M74 222L39 360M164 222l-9 138M316 222l9 138M406 222l35 138"/>
  </g>

  <g transform="translate(395 196)">
    <rect x="0" y="24" width="55" height="9" rx="4" fill="#80523d"/>
    <path d="M8 32v24M47 32v24" stroke="#4f4f4f" stroke-width="5"/>
    <path d="M4 19h47" stroke="#80523d" stroke-width="8" stroke-linecap="round"/>
  </g>
  <g fill="#467d4a" stroke="#35673c" stroke-width="3">
    <circle cx="151" cy="213" r="18"/><circle cx="174" cy="213" r="22"/><circle cx="199" cy="214" r="16"/>
  </g>

  <ellipse cx="240" cy="306" rx="25" ry="8" fill="#8f7d64" opacity="0.45"/>
  <rect x="233" y="151" width="14" height="150" rx="7" fill="url(#post)" stroke="#153a50" stroke-width="3"/>
  <circle cx="240" cy="145" r="15" fill="#f2b84a" stroke="#a66d20" stroke-width="4"/>
  <path d="M231 140c4-5 11-7 17-3" fill="none" stroke="#ffe29a" stroke-width="4" stroke-linecap="round"/>
</svg>
"""


SUN_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="82" height="82" viewBox="0 0 82 82">
  <g stroke="#f7b928" stroke-width="5" stroke-linecap="round">
    <path d="M41 3v11M41 68v11M3 41h11M68 41h11M14 14l8 8M60 60l8 8M68 14l-8 8M22 60l-8 8"/>
  </g>
  <circle cx="41" cy="41" r="25" fill="#ffd65b" stroke="#f3a928" stroke-width="4"/>
</svg>
"""


GROUND_SHADOW_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="150" height="36" viewBox="0 0 150 36">
  <defs>
    <radialGradient id="shade" cx="50%" cy="50%" r="55%">
      <stop offset="0" stop-color="#263238" stop-opacity="0.66"/>
      <stop offset="0.75" stop-color="#344047" stop-opacity="0.52"/>
      <stop offset="1" stop-color="#3d464a" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <ellipse cx="75" cy="18" rx="74" ry="17" fill="url(#shade)"/>
</svg>
"""


THEATER_STAGE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <defs>
    <linearGradient id="wall" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#2f315f"/>
      <stop offset="1" stop-color="#171831"/>
    </linearGradient>
  </defs>
  <rect width="480" height="360" fill="url(#wall)"/>
  <rect x="302" y="36" width="158" height="270" rx="8" fill="#f7f2dd" stroke="#c9bfa3" stroke-width="7"/>
  <path d="M0 306h480v54H0z" fill="#5d3f38"/>
  <path d="M0 306h480" stroke="#8a6257" stroke-width="5"/>
  <circle cx="240" cy="296" r="5" fill="#c89c6c"/>
</svg>
"""


LAMP_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="100" height="96" viewBox="0 0 100 96">
  <path d="M62 30L96 10v40z" fill="#ffe184" opacity="0.55"/>
  <path d="M15 69h44l-7 17H22z" fill="#697184" stroke="#3e4657" stroke-width="4"/>
  <path d="M37 67V45" stroke="#4c5567" stroke-width="7" stroke-linecap="round"/>
  <path d="M21 16h47l-9 31H29z" fill="#ffd45e" stroke="#ad7b20" stroke-width="4"/>
  <circle cx="45" cy="31" r="8" fill="#fff5b8"/>
</svg>
"""


PUPPET_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="76" height="126" viewBox="0 0 76 126">
  <path d="M24 31L17 5l20 17L55 5l-4 28" fill="#57413b" stroke="#302724" stroke-width="4" stroke-linejoin="round"/>
  <circle cx="38" cy="39" r="23" fill="#6d5149" stroke="#302724" stroke-width="4"/>
  <path d="M21 65c6-8 28-8 34 0l7 44H14z" fill="#76564d" stroke="#302724" stroke-width="4"/>
  <path d="M24 109l-7 13M52 109l7 13" stroke="#302724" stroke-width="6" stroke-linecap="round"/>
</svg>
"""


PUPPET_SHADOW_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="76" height="126" viewBox="0 0 76 126">
  <path d="M24 31L17 5l20 17L55 5l-4 28" fill="#34343e"/>
  <circle cx="38" cy="39" r="23" fill="#34343e"/>
  <path d="M21 65c6-8 28-8 34 0l7 44H14z" fill="#34343e"/>
  <path d="M24 109l-7 13M52 109l7 13" stroke="#34343e" stroke-width="6" stroke-linecap="round"/>
</svg>
"""


TRACK_STAGE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <defs>
    <linearGradient id="trackSky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#78c8f1"/>
      <stop offset="1" stop-color="#dff3fb"/>
    </linearGradient>
  </defs>
  <rect width="480" height="230" fill="url(#trackSky)"/>
  <rect y="230" width="480" height="130" fill="#77b95c"/>
  <rect y="255" width="480" height="80" fill="#555b63"/>
  <path d="M0 295h480" stroke="#f7e36b" stroke-width="5" stroke-dasharray="22 18"/>
  <path d="M44 245v100M52 245v100" stroke="#ffffff" stroke-width="5"/>
  <path d="M428 245v100M436 245v100" stroke="#ffffff" stroke-width="5"/>
  <g transform="translate(430 220)">
    <path d="M0 25V-35" stroke="#3a3a3a" stroke-width="4"/>
    <path d="M2-33h42v28H2z" fill="#ffffff"/>
    <path d="M2-33h14v10H2zM30-33h14v10H30zM16-23h14v10H16zM2-13h14v8H2zM30-13h14v8H30z" fill="#252525"/>
  </g>
  <g fill="#ffffff" opacity="0.8"><circle cx="92" cy="66" r="22"/><circle cx="118" cy="64" r="30"/><circle cx="149" cy="70" r="20"/></g>
</svg>
"""


CAR_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="110" height="58" viewBox="0 0 110 58">
  <path d="M14 38l8-22h48l19 15h12c5 0 7 4 7 9v5H5v-7z" fill="#ed4f4f" stroke="#9e2b32" stroke-width="4" stroke-linejoin="round"/>
  <path d="M32 20h33l13 11H27z" fill="#bde7f5" stroke="#70424a" stroke-width="3"/>
  <circle cx="27" cy="45" r="10" fill="#30333a" stroke="#111319" stroke-width="3"/>
  <circle cx="86" cy="45" r="10" fill="#30333a" stroke="#111319" stroke-width="3"/>
  <circle cx="27" cy="45" r="4" fill="#b9c2ca"/><circle cx="86" cy="45" r="4" fill="#b9c2ca"/>
</svg>
"""


EVAPORATION_STAGE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <defs>
    <linearGradient id="labWall" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#d9eef5"/>
      <stop offset="1" stop-color="#f4ead5"/>
    </linearGradient>
    <linearGradient id="bench" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#b97950"/>
      <stop offset="1" stop-color="#815035"/>
    </linearGradient>
  </defs>
  <rect width="480" height="270" fill="url(#labWall)"/>
  <rect y="270" width="480" height="90" fill="url(#bench)"/>
  <path d="M0 272h480" stroke="#633c2b" stroke-width="6"/>

  <g transform="translate(30 36)">
    <rect width="115" height="92" rx="5" fill="#f9fcfd" stroke="#6590a1" stroke-width="6"/>
    <path d="M57 4v84M4 47h107" stroke="#8bb4c3" stroke-width="4"/>
    <path d="M16 72c18-10 29-9 45 0 15 9 27 7 41-3" fill="none" stroke="#b9d9e3" stroke-width="5"/>
  </g>

  <g transform="translate(190 112)">
    <path d="M8 5h84l-7 190c-1 12-8 18-20 18H35c-12 0-19-6-20-18z" fill="#ffffff" fill-opacity="0.25" stroke="#526f7b" stroke-width="7"/>
    <path d="M12 6h76" stroke="#d6eef4" stroke-width="4"/>
    <g stroke="#6f8993" stroke-width="3">
      <path d="M77 42h13M77 76h12M77 110h11M77 144h10M77 178h9"/>
    </g>
  </g>

  <g fill="#ffffff" opacity="0.55">
    <path d="M221 88c-8-10-5-23 3-31 8 10 5 23-3 31z"/>
    <path d="M245 78c-7-9-4-20 3-27 7 9 4 20-3 27z"/>
    <path d="M267 91c-8-10-5-23 3-31 8 10 5 23-3 31z"/>
  </g>

  <g transform="translate(354 229)">
    <ellipse cx="30" cy="40" rx="36" ry="8" fill="#69432f" opacity="0.35"/>
    <path d="M8 38h45l-5 18H13z" fill="#637482"/>
    <path d="M30 38V14" stroke="#53616d" stroke-width="7"/>
  </g>
</svg>
"""


WATER_GAUGE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="70" height="150" viewBox="0 0 70 150">
  <defs>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#61d6ee"/>
      <stop offset="1" stop-color="#2588c9"/>
    </linearGradient>
  </defs>
  <path d="M2 13c10-8 19 7 31 0 13-8 23 7 35 0v132H2z" fill="url(#water)" opacity="0.88"/>
  <path d="M2 13c10-8 19 7 31 0 13-8 23 7 35 0" fill="none" stroke="#b7f3ff" stroke-width="4"/>
</svg>
"""


FAN_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="110" height="128" viewBox="0 0 110 128">
  <circle cx="55" cy="48" r="43" fill="#edf5f7" stroke="#607985" stroke-width="6"/>
  <circle cx="55" cy="48" r="8" fill="#526a75"/>
  <g fill="#7ab7c8" stroke="#527c89" stroke-width="2">
    <path d="M55 43C42 25 46 10 58 7c12 12 10 26 2 38z"/>
    <path d="M60 49c20-7 33 1 31 14-15 8-28 2-34-9z"/>
    <path d="M53 54c-5 21-19 27-29 19-1-17 10-26 25-27z"/>
  </g>
  <path d="M55 92v23M32 123h46" stroke="#607985" stroke-width="8" stroke-linecap="round"/>
</svg>
"""


VOLUME_LAB_STAGE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <defs>
    <linearGradient id="volumeWall" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#d9f0f4"/>
      <stop offset="1" stop-color="#f7f1df"/>
    </linearGradient>
    <linearGradient id="volumeBench" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#b87852"/>
      <stop offset="1" stop-color="#7c4b33"/>
    </linearGradient>
  </defs>
  <rect width="480" height="268" fill="url(#volumeWall)"/>
  <rect y="268" width="480" height="92" fill="url(#volumeBench)"/>
  <path d="M0 270h480" stroke="#5c392b" stroke-width="7"/>
  <g transform="translate(30 38)">
    <rect width="122" height="82" rx="6" fill="#f9fcfd" stroke="#6c98a8" stroke-width="5"/>
    <path d="M14 62L39 38l22 15 28-31 20 19" fill="none" stroke="#65a9be" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="39" cy="38" r="4" fill="#e6a74b"/><circle cx="89" cy="22" r="4" fill="#e6a74b"/>
  </g>
  <g transform="translate(360 58)" fill="none" stroke="#6f8f9b" stroke-width="5">
    <path d="M12 0v68c0 16 12 28 28 28s28-12 28-28V0"/>
    <path d="M5 0h70M17 58h46"/>
  </g>
  <ellipse cx="240" cy="307" rx="116" ry="18" fill="#4d2e25" opacity="0.22"/>
</svg>
"""


def immersion_costume_svg(level: int) -> str:
    water_y = 164 - level * 16
    water_height = 248 - water_y
    rock_rx = 12 + level * 5
    rock_ry = 9 + level * 4
    volume = 100 + level * 20
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="240" height="260" viewBox="0 0 240 260">
  <defs>
    <linearGradient id="immersedWater" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#72d9f0" stop-opacity="0.8"/>
      <stop offset="1" stop-color="#278fc8" stop-opacity="0.92"/>
    </linearGradient>
    <linearGradient id="stone" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#9aa5aa"/>
      <stop offset="1" stop-color="#58646a"/>
    </linearGradient>
    <clipPath id="tubeClip"><path d="M62 25h116l-8 202c-1 14-10 21-24 21H94c-14 0-23-7-24-21z"/></clipPath>
  </defs>
  <ellipse cx="120" cy="242" rx="76" ry="12" fill="#3e5862" opacity="0.18"/>
  <g clip-path="url(#tubeClip)">
    <rect x="64" y="{water_y}" width="112" height="{water_height}" fill="url(#immersedWater)"/>
    <path d="M64 {water_y}c20-7 34 7 56 0 22-7 39 7 56 0" fill="none" stroke="#c7f5ff" stroke-width="4"/>
    <ellipse cx="120" cy="222" rx="{rock_rx}" ry="{rock_ry}" fill="url(#stone)" stroke="#455158" stroke-width="4"/>
    <path d="M{120-rock_rx+5} {218-rock_ry//2}c8-5 16-4 23 0" fill="none" stroke="#c3cccf" stroke-width="3" stroke-linecap="round" opacity="0.65"/>
  </g>
  <path d="M62 25h116l-8 202c-1 14-10 21-24 21H94c-14 0-23-7-24-21z" fill="#ffffff" fill-opacity="0.09" stroke="#526f7b" stroke-width="7"/>
  <path d="M54 25h132" stroke="#526f7b" stroke-width="8" stroke-linecap="round"/>
  <g stroke="#66838e" stroke-width="3">
    <path d="M154 68h24M160 100h17M154 132h22M160 164h15M154 196h19"/>
  </g>
  <path d="M64 164h112" stroke="#f4a742" stroke-width="3" stroke-dasharray="7 6" opacity="0.9"/>
  <rect x="81" y="38" width="78" height="32" rx="16" fill="#ffffff" stroke="#337f9f" stroke-width="3"/>
  <text x="120" y="60" text-anchor="middle" font-family="Arial, sans-serif" font-size="17" font-weight="700" fill="#245d75">{volume} mL</text>
</svg>"""


def recipient_costume_svg(level: int) -> str:
    if level == 1:
        vessel = """
  <path d="M78 20h84l-7 210c-1 12-9 18-21 18h-28c-12 0-20-6-21-18z" fill="#ffffff" fill-opacity="0.12" stroke="#526f7b" stroke-width="7"/>
  <path d="M84 72h72l-5 158c0 8-5 12-14 12h-34c-9 0-14-4-14-12z" fill="#3ba9dc" fill-opacity="0.86"/>
  <path d="M84 72c18-7 30 7 48 0 10-4 17-3 24 0" fill="none" stroke="#c7f5ff" stroke-width="4"/>
  <path d="M70 20h100" stroke="#526f7b" stroke-width="8" stroke-linecap="round"/>"""
    elif level == 2:
        vessel = """
  <path d="M30 76h180l-12 151c-1 14-10 21-25 21H67c-15 0-24-7-25-21z" fill="#ffffff" fill-opacity="0.12" stroke="#526f7b" stroke-width="7"/>
  <path d="M40 170h160l-5 59c-1 8-6 13-17 13H62c-11 0-16-5-17-13z" fill="#3ba9dc" fill-opacity="0.86"/>
  <path d="M40 170c33-7 52 7 81 0 29-7 51 7 79 0" fill="none" stroke="#c7f5ff" stroke-width="4"/>
  <path d="M22 76h196" stroke="#526f7b" stroke-width="8" stroke-linecap="round"/>"""
    elif level == 3:
        vessel = """
  <path d="M95 20h50v61l61 133c8 18-4 34-25 34H59c-21 0-33-16-25-34L95 81z" fill="#ffffff" fill-opacity="0.12" stroke="#526f7b" stroke-width="7" stroke-linejoin="round"/>
  <path d="M58 169h124l25 53c5 11-4 20-18 20H51c-14 0-23-9-18-20z" fill="#3ba9dc" fill-opacity="0.86"/>
  <path d="M58 169c25-7 39 7 62 0 23-7 39 7 62 0" fill="none" stroke="#c7f5ff" stroke-width="4"/>
  <path d="M88 20h64" stroke="#526f7b" stroke-width="8" stroke-linecap="round"/>"""
    else:
        vessel = """
  <path d="M99 20h42v57c45 11 76 47 76 91 0 51-43 80-97 80s-97-29-97-80c0-44 31-80 76-91z" fill="#ffffff" fill-opacity="0.12" stroke="#526f7b" stroke-width="7"/>
  <path d="M31 184c23-7 39 7 62 0 23-7 40 7 64 0 21-6 36 4 50 1-8 39-44 57-87 57-45 0-81-19-89-58z" fill="#3ba9dc" fill-opacity="0.86"/>
  <path d="M31 184c23-7 39 7 62 0 23-7 40 7 64 0 21-6 36 4 50 1" fill="none" stroke="#c7f5ff" stroke-width="4"/>
  <path d="M92 20h56" stroke="#526f7b" stroke-width="8" stroke-linecap="round"/>"""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="240" height="260" viewBox="0 0 240 260">
  <ellipse cx="120" cy="244" rx="102" ry="12" fill="#3e5862" opacity="0.18"/>
  {vessel}
</svg>"""


COOLING_STAGE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <defs>
    <linearGradient id="coolingWall" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#e7f3f8"/>
      <stop offset="1" stop-color="#fff8ea"/>
    </linearGradient>
  </defs>
  <rect width="480" height="360" fill="url(#coolingWall)"/>
  <rect y="294" width="480" height="66" fill="#b98661"/>
  <path d="M0 294h480" stroke="#754d35" stroke-width="7"/>
  <g font-family="Arial, sans-serif" font-weight="700">
    <rect x="22" y="12" width="436" height="46" rx="15" fill="#ffffff" stroke="#aac5d1" stroke-width="4"/>
    <text x="240" y="43" text-anchor="middle" font-size="23" fill="#2b5366">Une boisson se refroidit</text>
    <text x="42" y="103" font-size="16" fill="#506d7a">Température de la pièce : 20 °C</text>
  </g>
  <g transform="translate(76 154)">
    <path d="M0 28h122v88c0 25-16 39-40 39H40c-24 0-40-14-40-39z" fill="#f2f5f6" stroke="#5e7884" stroke-width="6"/>
    <path d="M9 40h104v67c0 22-12 34-32 34H41c-20 0-32-12-32-34z" fill="#b86a3d"/>
    <path d="M122 48h20c33 0 33 58 0 58h-20" fill="none" stroke="#5e7884" stroke-width="11"/>
    <path d="M28 12c-13-18 14-20 1-39M62 12c-13-18 14-20 1-39M96 12c-13-18 14-20 1-39" fill="none" stroke="#ffffff" stroke-width="8" stroke-linecap="round" opacity="0.75"/>
  </g>
  <g font-family="Arial, sans-serif" font-size="15" font-weight="700" fill="#385868">
    <rect x="314" y="72" width="14" height="102" rx="7" fill="#ffffff" stroke="#5d7a87" stroke-width="4"/>
    <circle cx="321" cy="181" r="18" fill="#e85d4a" stroke="#9e382e" stroke-width="4"/>
    <path d="M321 81v96" stroke="#e85d4a" stroke-width="8" stroke-linecap="round"/>
    <g stroke="#5d7a87" stroke-width="3">
      <path d="M330 80h18M330 100h18M330 120h18M330 140h18M330 160h18"/>
    </g>
    <text x="356" y="85">100 °C</text>
    <text x="356" y="105">80 °C</text>
    <text x="356" y="125">60 °C</text>
    <text x="356" y="145">40 °C</text>
    <text x="356" y="165">20 °C</text>
  </g>
  <rect x="292" y="203" width="151" height="42" rx="12" fill="#ffffff" stroke="#b7cbd4" stroke-width="3"/>
  <text x="367" y="230" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" font-weight="700" fill="#506d7a">modèle simplifié</text>
</svg>
"""


COOLING_MARKER_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="96" height="46" viewBox="0 0 96 46">
  <path d="M6 23l18-16v9h61a8 8 0 0 1 8 8v6a8 8 0 0 1-8 8H24v9z" fill="#ef634f" stroke="#9d352b" stroke-width="5" stroke-linejoin="round"/>
  <circle cx="74" cy="27" r="6" fill="#ffffff" opacity="0.82"/>
</svg>
"""


THERMAL_STAGE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#f7fbff"/>
      <stop offset="1" stop-color="#e8f1f5"/>
    </linearGradient>
    <linearGradient id="warm" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffd879"/>
      <stop offset="1" stop-color="#f58c52"/>
    </linearGradient>
    <linearGradient id="cold" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#94e3ff"/>
      <stop offset="1" stop-color="#4f9ee8"/>
    </linearGradient>
  </defs>
  <rect width="480" height="360" fill="url(#bg)"/>
  <rect x="14" y="12" width="452" height="42" rx="14" fill="#173f55"/>
  <text x="240" y="40" text-anchor="middle" font-family="Arial, sans-serif" font-size="21" font-weight="700" fill="#ffffff">ÉCHANGE THERMIQUE ENTRE DEUX MILIEUX</text>
  <g font-family="Arial, sans-serif" font-weight="700" fill="#173f55">
    <text x="133" y="82" text-anchor="middle" font-size="19">MILIEU A</text>
    <text x="347" y="82" text-anchor="middle" font-size="19">MILIEU B</text>
    <text x="240" y="334" text-anchor="middle" font-size="14">Même quantité d'eau dans chaque compartiment</text>
  </g>
  <rect x="51" y="92" width="164" height="208" rx="18" fill="#ffffff" stroke="#315e72" stroke-width="6"/>
  <rect x="265" y="92" width="164" height="208" rx="18" fill="#ffffff" stroke="#315e72" stroke-width="6"/>
  <rect x="61" y="102" width="144" height="188" rx="10" fill="url(#warm)" opacity="0.78"/>
  <rect x="275" y="102" width="144" height="188" rx="10" fill="url(#cold)" opacity="0.78"/>
  <rect x="225" y="87" width="30" height="218" rx="8" fill="#d6e0e5" stroke="#6c8793" stroke-width="4"/>
  <path d="M211 167h58" stroke="#e25645" stroke-width="8" stroke-linecap="round"/>
  <path d="M259 154l16 13-16 13" fill="none" stroke="#e25645" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M269 226h-58" stroke="#3184c6" stroke-width="8" stroke-linecap="round"/>
  <path d="M221 213l-16 13 16 13" fill="none" stroke="#3184c6" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <g stroke="#173f55" stroke-width="2" font-family="Arial, sans-serif" font-size="11" font-weight="700" fill="#173f55">
    <path d="M67 80v220M281 80v220" opacity="0.55"/>
    <path d="M62 80h14M62 120h14M62 160h14M62 200h14M62 240h14M62 280h14"/>
    <path d="M276 80h14M276 120h14M276 160h14M276 200h14M276 240h14M276 280h14"/>
    <text x="44" y="84">100</text><text x="50" y="124">80</text><text x="50" y="164">60</text><text x="50" y="204">40</text><text x="50" y="244">20</text><text x="56" y="284">0</text>
    <text x="294" y="84">100</text><text x="294" y="124">80</text><text x="294" y="164">60</text><text x="294" y="204">40</text><text x="294" y="244">20</text><text x="294" y="284">0</text>
  </g>
</svg>
"""


THERMAL_CONTROLLER_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="74" height="46" viewBox="0 0 74 46">
  <rect x="2" y="2" width="70" height="42" rx="17" fill="#173f55" stroke="#ffffff" stroke-width="4"/>
  <path d="M15 17h40l-7-7M59 29H19l7 7" fill="none" stroke="#ffd166" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""


THERMAL_MARKER_A_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="132" height="18" viewBox="0 0 132 18">
  <rect x="2" y="4" width="128" height="10" rx="5" fill="#e74836" stroke="#8e281f" stroke-width="3"/>
</svg>
"""


THERMAL_MARKER_B_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="132" height="18" viewBox="0 0 132 18">
  <rect x="2" y="4" width="128" height="10" rx="5" fill="#1979c5" stroke="#0e4f87" stroke-width="3"/>
</svg>
"""


COFFEE_EXCHANGE_STAGE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
  <defs>
    <linearGradient id="wall" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#e9f5fb"/>
      <stop offset="1" stop-color="#fff7ea"/>
    </linearGradient>
    <linearGradient id="coffee" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#b86738"/>
      <stop offset="1" stop-color="#6e3825"/>
    </linearGradient>
  </defs>
  <rect width="480" height="360" fill="url(#wall)"/>
  <rect x="14" y="12" width="452" height="42" rx="14" fill="#173f55"/>
  <text x="240" y="40" text-anchor="middle" font-family="Arial, sans-serif" font-size="21" font-weight="700" fill="#ffffff">ÉCHANGE DE CHALEUR : CAFÉ ET AIR</text>
  <rect y="292" width="480" height="68" fill="#b9805b"/>
  <path d="M0 292h480" stroke="#774d34" stroke-width="7"/>

  <g transform="translate(52 138)">
    <ellipse cx="96" cy="145" rx="91" ry="13" fill="#4b3428" opacity="0.2"/>
    <path d="M8 20h150v91c0 31-21 48-52 48H60c-31 0-52-17-52-48z" fill="#f7fbfc" stroke="#315e72" stroke-width="7"/>
    <path d="M19 42h128v63c0 27-16 39-43 39H62c-27 0-43-12-43-39z" fill="url(#coffee)"/>
    <path d="M158 48h23c41 0 41 70 0 70h-23" fill="none" stroke="#315e72" stroke-width="12"/>
    <path d="M45 8c-13-20 14-24 1-45M82 8c-13-20 14-24 1-45M119 8c-13-20 14-24 1-45" fill="none" stroke="#ffffff" stroke-width="8" stroke-linecap="round" opacity="0.8"/>
  </g>

  <g font-family="Arial, sans-serif" font-weight="700" fill="#173f55">
    <text x="148" y="95" text-anchor="middle" font-size="18">CAFÉ</text>
    <text x="337" y="82" text-anchor="middle" font-size="16" fill="#b53429">CAFÉ</text>
    <text x="415" y="82" text-anchor="middle" font-size="16" fill="#1769a8">AIR</text>
    <text x="375" y="327" text-anchor="middle" font-size="13">Températures en °C</text>
  </g>

  <g stroke="#315e72" stroke-width="3" fill="#ffffff">
    <rect x="319" y="94" width="36" height="204" rx="15"/>
    <rect x="397" y="94" width="36" height="204" rx="15"/>
  </g>
  <g stroke="#315e72" stroke-width="2" font-family="Arial, sans-serif" font-size="11" font-weight="700" fill="#173f55">
    <path d="M311 90h14M311 130h14M311 170h14M311 210h14M311 250h14M311 290h14"/>
    <path d="M389 90h14M389 140h14M389 190h14M389 240h14M389 290h14"/>
    <text x="287" y="94">100</text><text x="294" y="134">80</text><text x="294" y="174">60</text><text x="294" y="214">40</text><text x="294" y="254">20</text><text x="301" y="294">0</text>
    <text x="438" y="94">40</text><text x="438" y="144">30</text><text x="438" y="194">20</text><text x="438" y="244">10</text><text x="445" y="294">0</text>
  </g>
</svg>
"""


COFFEE_MARKER_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="46" height="16" viewBox="0 0 46 16">
  <rect x="2" y="3" width="42" height="10" rx="5" fill="#e74836" stroke="#8e281f" stroke-width="3"/>
</svg>
"""


AIR_MARKER_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="46" height="16" viewBox="0 0 46 16">
  <rect x="2" y="3" width="42" height="10" rx="5" fill="#1979c5" stroke="#0e4f87" stroke-width="3"/>
</svg>
"""


def asset(svg: str, name: str, center_x: int, center_y: int) -> tuple[dict, str, bytes]:
    data = svg.encode("utf-8")
    asset_id = hashlib.md5(data).hexdigest()
    filename = f"{asset_id}.svg"
    costume = {
        "assetId": asset_id,
        "name": name,
        "bitmapResolution": 1,
        "md5ext": filename,
        "dataFormat": "svg",
        "rotationCenterX": center_x,
        "rotationCenterY": center_y,
    }
    return costume, filename, data


def base_target(name: str, costume: dict, *, is_stage: bool, layer_order: int) -> dict:
    target = {
        "isStage": is_stage,
        "name": name,
        "variables": {},
        "lists": {},
        "broadcasts": {},
        "blocks": {},
        "comments": {},
        "currentCostume": 0,
        "costumes": [costume],
        "sounds": [],
        "volume": 100,
        "layerOrder": layer_order,
    }
    if is_stage:
        target.update(
            {
                "tempo": 60,
                "videoTransparency": 50,
                "videoState": "on",
                "textToSpeechLanguage": None,
            }
        )
    else:
        target.update(
            {
                "visible": True,
                "x": 0,
                "y": 0,
                "size": 100,
                "direction": 90,
                "draggable": False,
                "rotationStyle": "don't rotate",
            }
        )
    return target


def assert_reference_opcodes() -> dict:
    if not REFERENCE_PROJECT.exists():
        raise FileNotFoundError(f"Missing reference project: {REFERENCE_PROJECT}")

    with zipfile.ZipFile(REFERENCE_PROJECT) as archive:
        reference = json.loads(archive.read("project.json"))

    available = {
        block["opcode"]
        for target in reference["targets"]
        for block in target.get("blocks", {}).values()
    }
    required = {
        "event_whenflagclicked",
        "motion_gotoxy",
        "motion_movesteps",
        "motion_pointindirection",
        "control_wait",
        "control_repeat",
        "looks_changesizeby",
        "looks_costume",
        "looks_nextcostume",
        "looks_setsizeto",
        "looks_say",
        "looks_switchcostumeto",
        "sensing_of",
        "sensing_of_object_menu",
        "operator_add",
        "operator_divide",
        "operator_multiply",
        "operator_subtract",
    }
    missing = required - available
    if missing:
        raise ValueError(f"Reference project is missing opcodes: {sorted(missing)}")
    return reference


def project_with(reference: dict, targets: list[dict]) -> dict:
    return {
        "targets": targets,
        "monitors": [],
        "extensions": [],
        "meta": reference.get(
            "meta", {"semver": "3.0.0", "vm": "0.2.0", "agent": "Origamia"}
        ),
    }


def build_exercise_145() -> tuple[dict, list[tuple[str, bytes]]]:
    reference = assert_reference_opcodes()
    stage_costume, stage_file, stage_data = asset(
        SHADOW_STAGE_SVG, "Cour", 240, 180
    )
    sun_costume, sun_file, sun_data = asset(SUN_SVG, "Soleil", 41, 41)
    shadow_costume, shadow_file, shadow_data = asset(
        GROUND_SHADOW_SVG, "Ombre", 75, 18
    )

    stage = base_target("Stage", stage_costume, is_stage=True, layer_order=0)
    sun = base_target("Soleil", sun_costume, is_stage=False, layer_order=2)
    sun.update({"x": -150, "y": 105, "size": 100})
    shadow = base_target("Ombre", shadow_costume, is_stage=False, layer_order=1)
    shadow.update({"x": 75, "y": -112, "size": 100})

    sun["blocks"] = {
        "145_sun_flag": {
            "opcode": "event_whenflagclicked",
            "next": "145_sun_position",
            "parent": None,
            "inputs": {},
            "fields": {},
            "shadow": False,
            "topLevel": True,
            "x": 80,
            "y": 80,
        },
        "145_sun_position": {
            "opcode": "motion_gotoxy",
            "next": None,
            "parent": "145_sun_flag",
            "inputs": {"X": [1, [4, "-150"]], "Y": [1, [4, "105"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
    }

    shadow["blocks"] = {
        "145_shadow_flag": {
            "opcode": "event_whenflagclicked",
            "next": "145_shadow_wait",
            "parent": None,
            "inputs": {},
            "fields": {},
            "shadow": False,
            "topLevel": True,
            "x": 80,
            "y": 80,
        },
        "145_shadow_wait": {
            "opcode": "control_wait",
            "next": "145_shadow_position",
            "parent": "145_shadow_flag",
            "inputs": {"DURATION": [1, [5, "0.1"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "145_shadow_position": {
            "opcode": "motion_gotoxy",
            "next": None,
            "parent": "145_shadow_wait",
            "inputs": {
                "X": [3, "145_opposite", [4, "0"]],
                "Y": [1, [4, "-112"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "145_opposite": {
            "opcode": "operator_subtract",
            "next": None,
            "parent": "145_shadow_position",
            "inputs": {
                "NUM1": [1, [4, "0"]],
                "NUM2": [3, "145_half_sun_x", [4, "0"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "145_half_sun_x": {
            "opcode": "operator_divide",
            "next": None,
            "parent": "145_opposite",
            "inputs": {
                "NUM1": [3, "145_sun_x", [4, "0"]],
                "NUM2": [1, [4, "2"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "145_sun_x": {
            "opcode": "sensing_of",
            "next": None,
            "parent": "145_half_sun_x",
            "inputs": {"OBJECT": [1, "145_sun_menu"]},
            "fields": {"PROPERTY": ["x position", None]},
            "shadow": False,
            "topLevel": False,
        },
        "145_sun_menu": {
            "opcode": "sensing_of_object_menu",
            "next": None,
            "parent": "145_sun_x",
            "inputs": {},
            "fields": {"OBJECT": ["Soleil", None]},
            "shadow": True,
            "topLevel": False,
        },
    }

    # AdaCraft opens the first sprite's script after import.
    project = project_with(reference, [stage, sun, shadow])
    return project, [
        (stage_file, stage_data),
        (sun_file, sun_data),
        (shadow_file, shadow_data),
    ]


def build_exercise_146() -> tuple[dict, list[tuple[str, bytes]]]:
    reference = assert_reference_opcodes()
    stage_costume, stage_file, stage_data = asset(
        THEATER_STAGE_SVG, "Theatre", 240, 180
    )
    lamp_costume, lamp_file, lamp_data = asset(LAMP_SVG, "Lampe", 50, 48)
    puppet_costume, puppet_file, puppet_data = asset(
        PUPPET_SVG, "Marionnette", 38, 63
    )
    shadow_costume, shadow_file, shadow_data = asset(
        PUPPET_SHADOW_SVG, "Ombre", 38, 63
    )

    stage = base_target("Stage", stage_costume, is_stage=True, layer_order=0)
    lamp = base_target("Lampe", lamp_costume, is_stage=False, layer_order=3)
    lamp.update({"x": -160, "y": -35, "size": 75})
    puppet = base_target(
        "Marionnette", puppet_costume, is_stage=False, layer_order=2
    )
    puppet.update({"x": 0, "y": -30, "size": 65})
    shadow = base_target("Ombre", shadow_costume, is_stage=False, layer_order=1)
    shadow.update({"x": 145, "y": 0, "size": 80})

    lamp["blocks"] = {
        "146_lamp_flag": {
            "opcode": "event_whenflagclicked",
            "next": "146_lamp_position",
            "parent": None,
            "inputs": {},
            "fields": {},
            "shadow": False,
            "topLevel": True,
            "x": 80,
            "y": 80,
        },
        "146_lamp_position": {
            "opcode": "motion_gotoxy",
            "next": None,
            "parent": "146_lamp_flag",
            "inputs": {"X": [1, [4, "-160"]], "Y": [1, [4, "-35"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
    }

    shadow["blocks"] = {
        "146_shadow_flag": {
            "opcode": "event_whenflagclicked",
            "next": "146_shadow_wait",
            "parent": None,
            "inputs": {},
            "fields": {},
            "shadow": False,
            "topLevel": True,
            "x": 80,
            "y": 80,
        },
        "146_shadow_wait": {
            "opcode": "control_wait",
            "next": "146_shadow_size",
            "parent": "146_shadow_flag",
            "inputs": {"DURATION": [1, [5, "0.1"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "146_shadow_size": {
            "opcode": "looks_setsizeto",
            "next": None,
            "parent": "146_shadow_wait",
            "inputs": {"SIZE": [3, "146_size_formula", [4, "100"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "146_size_formula": {
            "opcode": "operator_add",
            "next": None,
            "parent": "146_shadow_size",
            "inputs": {
                "NUM1": [1, [4, "240"]],
                "NUM2": [3, "146_lamp_x", [4, "0"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "146_lamp_x": {
            "opcode": "sensing_of",
            "next": None,
            "parent": "146_size_formula",
            "inputs": {"OBJECT": [1, "146_lamp_menu"]},
            "fields": {"PROPERTY": ["x position", None]},
            "shadow": False,
            "topLevel": False,
        },
        "146_lamp_menu": {
            "opcode": "sensing_of_object_menu",
            "next": None,
            "parent": "146_lamp_x",
            "inputs": {},
            "fields": {"OBJECT": ["Lampe", None]},
            "shadow": True,
            "topLevel": False,
        },
    }

    project = project_with(reference, [stage, lamp, shadow, puppet])
    return project, [
        (stage_file, stage_data),
        (lamp_file, lamp_data),
        (puppet_file, puppet_data),
        (shadow_file, shadow_data),
    ]


def build_exercise_147() -> tuple[dict, list[tuple[str, bytes]]]:
    reference = assert_reference_opcodes()
    stage_costume, stage_file, stage_data = asset(
        TRACK_STAGE_SVG, "Piste", 240, 180
    )
    car_costume, car_file, car_data = asset(CAR_SVG, "Voiture", 55, 29)

    stage = base_target("Stage", stage_costume, is_stage=True, layer_order=0)
    car = base_target("Voiture", car_costume, is_stage=False, layer_order=1)
    car.update(
        {
            "x": -190,
            "y": -105,
            "size": 72,
            "direction": 90,
            "rotationStyle": "left-right",
        }
    )

    car["blocks"] = {
        "147_flag": {
            "opcode": "event_whenflagclicked",
            "next": "147_start",
            "parent": None,
            "inputs": {},
            "fields": {},
            "shadow": False,
            "topLevel": True,
            "x": 80,
            "y": 80,
        },
        "147_start": {
            "opcode": "motion_gotoxy",
            "next": "147_direction",
            "parent": "147_flag",
            "inputs": {"X": [1, [4, "-190"]], "Y": [1, [4, "-105"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "147_direction": {
            "opcode": "motion_pointindirection",
            "next": "147_repeat",
            "parent": "147_start",
            "inputs": {"DIRECTION": [1, [8, "90"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "147_repeat": {
            "opcode": "control_repeat",
            "next": None,
            "parent": "147_direction",
            "inputs": {"TIMES": [1, [6, "15"]], "SUBSTACK": [2, "147_move"]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "147_move": {
            "opcode": "motion_movesteps",
            "next": "147_wait",
            "parent": "147_repeat",
            "inputs": {"STEPS": [1, [4, "24"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "147_wait": {
            "opcode": "control_wait",
            "next": None,
            "parent": "147_move",
            "inputs": {"DURATION": [1, [5, "0.2"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
    }

    project = project_with(reference, [stage, car])
    return project, [(stage_file, stage_data), (car_file, car_data)]


def build_exercise_148() -> tuple[dict, list[tuple[str, bytes]]]:
    reference = assert_reference_opcodes()
    stage_costume, stage_file, stage_data = asset(
        EVAPORATION_STAGE_SVG, "Laboratoire", 240, 180
    )
    water_costume, water_file, water_data = asset(
        WATER_GAUGE_SVG, "Eau", 35, 145
    )
    fan_costume, fan_file, fan_data = asset(FAN_SVG, "Ventilateur", 55, 120)

    stage = base_target("Stage", stage_costume, is_stage=True, layer_order=0)
    water = base_target("Eau", water_costume, is_stage=False, layer_order=1)
    water.update({"x": 0, "y": -125, "size": 100})
    fan = base_target("Ventilateur", fan_costume, is_stage=False, layer_order=2)
    fan.update({"x": 145, "y": -112, "size": 72})

    water["blocks"] = {
        "148_flag": {
            "opcode": "event_whenflagclicked",
            "next": "148_reset_size",
            "parent": None,
            "inputs": {},
            "fields": {},
            "shadow": False,
            "topLevel": True,
            "x": 80,
            "y": 80,
        },
        "148_reset_size": {
            "opcode": "looks_setsizeto",
            "next": "148_repeat",
            "parent": "148_flag",
            "inputs": {"SIZE": [1, [4, "100"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "148_repeat": {
            "opcode": "control_repeat",
            "next": "148_say_result",
            "parent": "148_reset_size",
            "inputs": {"TIMES": [1, [6, "5"]], "SUBSTACK": [2, "148_evaporate"]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "148_evaporate": {
            "opcode": "looks_changesizeby",
            "next": "148_wait",
            "parent": "148_repeat",
            "inputs": {"CHANGE": [3, "148_rate", [4, "-5"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "148_rate": {
            "opcode": "operator_multiply",
            "next": None,
            "parent": "148_evaporate",
            "inputs": {
                "NUM1": [1, [4, "-4"]],
                "NUM2": [1, [4, "1"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "148_wait": {
            "opcode": "control_wait",
            "next": None,
            "parent": "148_evaporate",
            "inputs": {"DURATION": [1, [5, "0.25"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "148_say_result": {
            "opcode": "looks_say",
            "next": None,
            "parent": "148_repeat",
            "inputs": {"MESSAGE": [3, "148_water_size", [10, "100"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "148_water_size": {
            "opcode": "sensing_of",
            "next": None,
            "parent": "148_say_result",
            "inputs": {"OBJECT": [1, "148_water_menu"]},
            "fields": {"PROPERTY": ["size", None]},
            "shadow": False,
            "topLevel": False,
        },
        "148_water_menu": {
            "opcode": "sensing_of_object_menu",
            "next": None,
            "parent": "148_water_size",
            "inputs": {},
            "fields": {"OBJECT": ["Eau", None]},
            "shadow": True,
            "topLevel": False,
        },
    }

    project = project_with(reference, [stage, water, fan])
    return project, [
        (stage_file, stage_data),
        (water_file, water_data),
        (fan_file, fan_data),
    ]


def build_exercise_149() -> tuple[dict, list[tuple[str, bytes]]]:
    reference = assert_reference_opcodes()
    stage_costume, stage_file, stage_data = asset(
        VOLUME_LAB_STAGE_SVG, "Laboratoire des volumes", 240, 180
    )
    costume_assets = [
        asset(immersion_costume_svg(level), f"Solide {level}", 120, 130)
        for level in range(1, 5)
    ]
    costumes = [costume for costume, _, _ in costume_assets]

    stage = base_target("Stage", stage_costume, is_stage=True, layer_order=0)
    cylinder = base_target(
        "Éprouvette", costumes[0], is_stage=False, layer_order=1
    )
    cylinder["costumes"] = costumes
    cylinder.update({"x": 0, "y": -12, "size": 92})
    cylinder["blocks"] = {
        "149_flag": {
            "opcode": "event_whenflagclicked",
            "next": "149_switch_costume",
            "parent": None,
            "inputs": {},
            "fields": {},
            "shadow": False,
            "topLevel": True,
            "x": 80,
            "y": 80,
        },
        "149_switch_costume": {
            "opcode": "looks_switchcostumeto",
            "next": None,
            "parent": "149_flag",
            "inputs": {"COSTUME": [1, "149_costume_menu"]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "149_costume_menu": {
            "opcode": "looks_costume",
            "next": None,
            "parent": "149_switch_costume",
            "inputs": {},
            "fields": {"COSTUME": ["Solide 1", None]},
            "shadow": True,
            "topLevel": False,
        },
    }

    project = project_with(reference, [stage, cylinder])
    assets = [(stage_file, stage_data)] + [
        (filename, data) for _, filename, data in costume_assets
    ]
    return project, assets


def build_exercise_150() -> tuple[dict, list[tuple[str, bytes]]]:
    reference = assert_reference_opcodes()
    stage_costume, stage_file, stage_data = asset(
        VOLUME_LAB_STAGE_SVG, "Paillasse", 240, 180
    )
    costume_assets = [
        asset(recipient_costume_svg(level), f"Récipient {level}", 120, 130)
        for level in range(1, 5)
    ]
    costumes = [costume for costume, _, _ in costume_assets]

    stage = base_target("Stage", stage_costume, is_stage=True, layer_order=0)
    recipient = base_target(
        "Récipient", costumes[0], is_stage=False, layer_order=1
    )
    recipient["costumes"] = costumes
    recipient.update({"x": 0, "y": -12, "size": 92})
    recipient["blocks"] = {
        "150_flag": {
            "opcode": "event_whenflagclicked",
            "next": "150_switch_costume",
            "parent": None,
            "inputs": {},
            "fields": {},
            "shadow": False,
            "topLevel": True,
            "x": 80,
            "y": 80,
        },
        "150_switch_costume": {
            "opcode": "looks_switchcostumeto",
            "next": "150_say_result",
            "parent": "150_flag",
            "inputs": {"COSTUME": [1, "150_costume_menu"]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "150_costume_menu": {
            "opcode": "looks_costume",
            "next": None,
            "parent": "150_switch_costume",
            "inputs": {},
            "fields": {"COSTUME": ["Récipient 1", None]},
            "shadow": True,
            "topLevel": False,
        },
        "150_say_result": {
            "opcode": "looks_say",
            "next": None,
            "parent": "150_switch_costume",
            "inputs": {"MESSAGE": [1, [10, "100"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
    }

    project = project_with(reference, [stage, recipient])
    assets = [(stage_file, stage_data)] + [
        (filename, data) for _, filename, data in costume_assets
    ]
    return project, assets


def build_exercise_151_legacy() -> tuple[dict, list[tuple[str, bytes]]]:
    reference = assert_reference_opcodes()
    stage_costume, stage_file, stage_data = asset(
        COOLING_STAGE_SVG, "Laboratoire", 240, 180
    )
    marker_costume, marker_file, marker_data = asset(
        COOLING_MARKER_SVG, "Repère", 48, 23
    )

    stage = base_target("Stage", stage_costume, is_stage=True, layer_order=0)
    marker = base_target(
        "Thermomètre", marker_costume, is_stage=False, layer_order=1
    )
    marker.update(
        {
            "x": 80,
            "y": 100,
            "size": 55,
            "direction": 90,
            "rotationStyle": "don't rotate",
        }
    )
    marker["blocks"] = {
        "151_flag": {
            "opcode": "event_whenflagclicked",
            "next": "151_reset",
            "parent": None,
            "inputs": {},
            "fields": {},
            "shadow": False,
            "topLevel": True,
            "x": 80,
            "y": 80,
        },
        "151_reset": {
            "opcode": "motion_gotoxy",
            "next": "151_repeat",
            "parent": "151_flag",
            "inputs": {"X": [1, [4, "80"]], "Y": [1, [4, "100"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_repeat": {
            "opcode": "control_repeat",
            "next": None,
            "parent": "151_reset",
            "inputs": {"TIMES": [1, [6, "5"]], "SUBSTACK": [2, "151_correct"]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_say": {
            "opcode": "looks_sayforsecs",
            "next": None,
            "parent": "151_correct",
            "inputs": {
                "MESSAGE": [3, "151_round_display", [10, "100"]],
                "SECS": [1, [4, "0.7"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_round_display": {
            "opcode": "operator_round",
            "next": None,
            "parent": "151_say",
            "inputs": {"NUM": [3, "151_display_y", [4, "0"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_display_y": {
            "opcode": "sensing_of",
            "next": None,
            "parent": "151_round_display",
            "inputs": {"OBJECT": [1, "151_display_menu"]},
            "fields": {"PROPERTY": ["y position", None]},
            "shadow": False,
            "topLevel": False,
        },
        "151_display_menu": {
            "opcode": "sensing_of_object_menu",
            "next": None,
            "parent": "151_display_y",
            "inputs": {},
            "fields": {"OBJECT": ["Thermomètre", None]},
            "shadow": True,
            "topLevel": False,
        },
        "151_correct": {
            "opcode": "motion_sety",
            "next": "151_say",
            "parent": "151_repeat",
            "inputs": {"Y": [3, "151_correct_add", [4, "0"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_correct_add": {
            "opcode": "operator_add",
            "next": None,
            "parent": "151_correct",
            "inputs": {
                "NUM1": [1, [4, "20"]],
                "NUM2": [3, "151_correct_scale", [4, "0"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_correct_scale": {
            "opcode": "operator_multiply",
            "next": None,
            "parent": "151_correct_add",
            "inputs": {
                "NUM1": [3, "151_correct_gap", [4, "0"]],
                "NUM2": [1, [4, "0.8"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_correct_gap": {
            "opcode": "operator_subtract",
            "next": None,
            "parent": "151_correct_scale",
            "inputs": {
                "NUM1": [3, "151_correct_y", [4, "0"]],
                "NUM2": [1, [4, "20"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_correct_y": {
            "opcode": "sensing_of",
            "next": None,
            "parent": "151_correct_gap",
            "inputs": {"OBJECT": [1, "151_correct_menu"]},
            "fields": {"PROPERTY": ["y position", None]},
            "shadow": False,
            "topLevel": False,
        },
        "151_correct_menu": {
            "opcode": "sensing_of_object_menu",
            "next": None,
            "parent": "151_correct_y",
            "inputs": {},
            "fields": {"OBJECT": ["Thermomètre", None]},
            "shadow": True,
            "topLevel": False,
        },
    }

    project = project_with(reference, [stage, marker])
    return project, [(stage_file, stage_data), (marker_file, marker_data)]


def build_exercise_151() -> tuple[dict, list[tuple[str, bytes]]]:
    """Build a coffee-to-room heat exchange model with editable temperatures."""
    reference = assert_reference_opcodes()
    stage_costume, stage_file, stage_data = asset(
        COFFEE_EXCHANGE_STAGE_SVG, "Refroidissement du cafe", 240, 180
    )
    controller_costume, controller_file, controller_data = asset(
        THERMAL_CONTROLLER_SVG, "Simulation", 37, 23
    )
    marker_a_costume, marker_a_file, marker_a_data = asset(
        COFFEE_MARKER_SVG, "Temperature du cafe", 23, 8
    )
    marker_b_costume, marker_b_file, marker_b_data = asset(
        AIR_MARKER_SVG, "Temperature de l'air", 23, 8
    )

    temperature_a_id = "151_temperature_a"
    temperature_b_id = "151_temperature_b"
    transfer_id = "151_transfert"
    temperature_a_name = "température du café"
    temperature_b_name = "température de l'air"
    transfer_name = "transfert thermique"

    stage = base_target("Stage", stage_costume, is_stage=True, layer_order=0)
    stage["variables"] = {
        temperature_a_id: [temperature_a_name, 80],
        temperature_b_id: [temperature_b_name, 20],
        transfer_id: [transfer_name, 0],
    }

    controller = base_target(
        "Simulation", controller_costume, is_stage=False, layer_order=3
    )
    controller.update({"x": -5, "y": 108, "size": 72})
    marker_a = base_target(
        "Café", marker_a_costume, is_stage=False, layer_order=1
    )
    marker_a.update({"x": 97, "y": 60, "size": 100})
    marker_b = base_target(
        "Air", marker_b_costume, is_stage=False, layer_order=2
    )
    marker_b.update({"x": 175, "y": -60, "size": 100})

    controller["blocks"] = {
        "151_flag": {
            "opcode": "event_whenflagclicked",
            "next": "151_set_a",
            "parent": None,
            "inputs": {},
            "fields": {},
            "shadow": False,
            "topLevel": True,
            "x": 80,
            "y": 80,
        },
        "151_set_a": {
            "opcode": "data_setvariableto",
            "next": "151_set_b",
            "parent": "151_flag",
            "inputs": {"VALUE": [1, [4, "80"]]},
            "fields": {"VARIABLE": [temperature_a_name, temperature_a_id]},
            "shadow": False,
            "topLevel": False,
        },
        "151_set_b": {
            "opcode": "data_setvariableto",
            "next": "151_repeat",
            "parent": "151_set_a",
            "inputs": {"VALUE": [1, [4, "20"]]},
            "fields": {"VARIABLE": [temperature_b_name, temperature_b_id]},
            "shadow": False,
            "topLevel": False,
        },
        "151_repeat": {
            "opcode": "control_repeat_until",
            "next": "151_done",
            "parent": "151_set_b",
            "inputs": {
                "CONDITION": [2, "151_equilibrium_test"],
                "SUBSTACK": [2, "151_set_transfer"],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_equilibrium_test": {
            "opcode": "operator_lt",
            "next": None,
            "parent": "151_repeat",
            "inputs": {
                "OPERAND1": [3, "151_absolute_gap", [4, "0"]],
                "OPERAND2": [1, [4, "0.1"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_absolute_gap": {
            "opcode": "operator_mathop",
            "next": None,
            "parent": "151_equilibrium_test",
            "inputs": {"NUM": [3, "151_gap_for_stop", [4, "0"]]},
            "fields": {"OPERATOR": ["abs", None]},
            "shadow": False,
            "topLevel": False,
        },
        "151_gap_for_stop": {
            "opcode": "operator_subtract",
            "next": None,
            "parent": "151_absolute_gap",
            "inputs": {
                "NUM1": [3, "151_read_a_for_stop", [4, "0"]],
                "NUM2": [3, "151_read_b_for_stop", [4, "0"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_read_a_for_stop": {
            "opcode": "data_variable",
            "next": None,
            "parent": "151_gap_for_stop",
            "inputs": {},
            "fields": {"VARIABLE": [temperature_a_name, temperature_a_id]},
            "shadow": False,
            "topLevel": False,
        },
        "151_read_b_for_stop": {
            "opcode": "data_variable",
            "next": None,
            "parent": "151_gap_for_stop",
            "inputs": {},
            "fields": {"VARIABLE": [temperature_b_name, temperature_b_id]},
            "shadow": False,
            "topLevel": False,
        },
        "151_set_transfer": {
            "opcode": "data_setvariableto",
            "next": "151_change_a",
            "parent": "151_repeat",
            "inputs": {"VALUE": [3, "151_transfer_scale", [4, "0"]]},
            "fields": {"VARIABLE": [transfer_name, transfer_id]},
            "shadow": False,
            "topLevel": False,
        },
        "151_transfer_scale": {
            "opcode": "operator_multiply",
            "next": None,
            "parent": "151_set_transfer",
            "inputs": {
                "NUM1": [3, "151_temperature_gap", [4, "0"]],
                "NUM2": [1, [4, "0.02"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_temperature_gap": {
            "opcode": "operator_subtract",
            "next": None,
            "parent": "151_transfer_scale",
            "inputs": {
                "NUM1": [3, "151_read_a_for_gap", [4, "0"]],
                "NUM2": [3, "151_read_b_for_gap", [4, "0"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_read_a_for_gap": {
            "opcode": "data_variable",
            "next": None,
            "parent": "151_temperature_gap",
            "inputs": {},
            "fields": {"VARIABLE": [temperature_a_name, temperature_a_id]},
            "shadow": False,
            "topLevel": False,
        },
        "151_read_b_for_gap": {
            "opcode": "data_variable",
            "next": None,
            "parent": "151_temperature_gap",
            "inputs": {},
            "fields": {"VARIABLE": [temperature_b_name, temperature_b_id]},
            "shadow": False,
            "topLevel": False,
        },
        "151_change_a": {
            "opcode": "data_changevariableby",
            "next": "151_change_b",
            "parent": "151_set_transfer",
            "inputs": {"VALUE": [3, "151_negative_transfer", [4, "0"]]},
            "fields": {"VARIABLE": [temperature_a_name, temperature_a_id]},
            "shadow": False,
            "topLevel": False,
        },
        "151_negative_transfer": {
            "opcode": "operator_multiply",
            "next": None,
            "parent": "151_change_a",
            "inputs": {
                "NUM1": [3, "151_read_transfer_for_a", [4, "0"]],
                "NUM2": [1, [4, "-1"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_read_transfer_for_a": {
            "opcode": "data_variable",
            "next": None,
            "parent": "151_negative_transfer",
            "inputs": {},
            "fields": {"VARIABLE": [transfer_name, transfer_id]},
            "shadow": False,
            "topLevel": False,
        },
        "151_change_b": {
            "opcode": "data_changevariableby",
            "next": "151_wait",
            "parent": "151_change_a",
            "inputs": {"VALUE": [3, "151_air_share", [4, "0"]]},
            "fields": {"VARIABLE": [temperature_b_name, temperature_b_id]},
            "shadow": False,
            "topLevel": False,
        },
        "151_air_share": {
            "opcode": "operator_divide",
            "next": None,
            "parent": "151_change_b",
            "inputs": {
                "NUM1": [3, "151_read_transfer_for_b", [4, "0"]],
                "NUM2": [1, [4, "10"]],
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_read_transfer_for_b": {
            "opcode": "data_variable",
            "next": None,
            "parent": "151_air_share",
            "inputs": {},
            "fields": {"VARIABLE": [transfer_name, transfer_id]},
            "shadow": False,
            "topLevel": False,
        },
        "151_wait": {
            "opcode": "control_wait",
            "next": None,
            "parent": "151_change_b",
            "inputs": {"DURATION": [1, [5, "0.03"]]},
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
        "151_done": {
            "opcode": "looks_say",
            "next": None,
            "parent": "151_repeat",
            "inputs": {
                "MESSAGE": [
                    1,
                    [10, "Fin de l'essai : relève les deux températures."],
                ]
            },
            "fields": {},
            "shadow": False,
            "topLevel": False,
        },
    }

    def marker_blocks(
        prefix: str,
        variable_name: str,
        variable_id: str,
        scale: str,
    ) -> dict:
        return {
            f"{prefix}_flag": {
                "opcode": "event_whenflagclicked",
                "next": f"{prefix}_forever",
                "parent": None,
                "inputs": {},
                "fields": {},
                "shadow": False,
                "topLevel": True,
                "x": 70,
                "y": 70,
            },
            f"{prefix}_forever": {
                "opcode": "control_forever",
                "next": None,
                "parent": f"{prefix}_flag",
                "inputs": {"SUBSTACK": [2, f"{prefix}_set_y"]},
                "fields": {},
                "shadow": False,
                "topLevel": False,
            },
            f"{prefix}_set_y": {
                "opcode": "motion_sety",
                "next": f"{prefix}_wait",
                "parent": f"{prefix}_forever",
                "inputs": {"Y": [3, f"{prefix}_map_y", [4, "0"]]},
                "fields": {},
                "shadow": False,
                "topLevel": False,
            },
            f"{prefix}_map_y": {
                "opcode": "operator_subtract",
                "next": None,
                "parent": f"{prefix}_set_y",
                "inputs": {
                    "NUM1": [3, f"{prefix}_scale_y", [4, "0"]],
                    "NUM2": [1, [4, "110"]],
                },
                "fields": {},
                "shadow": False,
                "topLevel": False,
            },
            f"{prefix}_scale_y": {
                "opcode": "operator_multiply",
                "next": None,
                "parent": f"{prefix}_map_y",
                "inputs": {
                    "NUM1": [3, f"{prefix}_read_temperature", [4, "0"]],
                    "NUM2": [1, [4, scale]],
                },
                "fields": {},
                "shadow": False,
                "topLevel": False,
            },
            f"{prefix}_read_temperature": {
                "opcode": "data_variable",
                "next": None,
                "parent": f"{prefix}_scale_y",
                "inputs": {},
                "fields": {"VARIABLE": [variable_name, variable_id]},
                "shadow": False,
                "topLevel": False,
            },
            f"{prefix}_wait": {
                "opcode": "control_wait",
                "next": None,
                "parent": f"{prefix}_set_y",
                "inputs": {"DURATION": [1, [5, "0.05"]]},
                "fields": {},
                "shadow": False,
                "topLevel": False,
            },
        }

    marker_a["blocks"] = marker_blocks(
        "151_marker_a", temperature_a_name, temperature_a_id, "2"
    )
    marker_b["blocks"] = marker_blocks(
        "151_marker_b", temperature_b_name, temperature_b_id, "5"
    )

    project = project_with(reference, [stage, controller, marker_a, marker_b])
    project["monitors"] = [
        {
            "id": temperature_a_id,
            "mode": "default",
            "opcode": "data_variable",
            "params": {"VARIABLE": temperature_a_name},
            "spriteName": None,
            "value": 80,
            "width": 0,
            "height": 0,
            "x": 12,
            "y": 58,
            "visible": True,
            "sliderMin": 0,
            "sliderMax": 100,
            "isDiscrete": True,
        },
        {
            "id": temperature_b_id,
            "mode": "default",
            "opcode": "data_variable",
            "params": {"VARIABLE": temperature_b_name},
            "spriteName": None,
            "value": 20,
            "width": 0,
            "height": 0,
            "x": 294,
            "y": 58,
            "visible": True,
            "sliderMin": 0,
            "sliderMax": 100,
            "isDiscrete": True,
        },
    ]
    assets = [
        (stage_file, stage_data),
        (controller_file, controller_data),
        (marker_a_file, marker_a_data),
        (marker_b_file, marker_b_data),
    ]
    return project, assets


BUILDERS = {
    "145": build_exercise_145,
    "146": build_exercise_146,
    "147": build_exercise_147,
    "148": build_exercise_148,
    "149": build_exercise_149,
    "150": build_exercise_150,
    "151": build_exercise_151,
}


def write_project(exercise: str, output: Path) -> None:
    project, assets = BUILDERS[exercise]()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(
            "project.json",
            json.dumps(project, ensure_ascii=False, separators=(",", ":")),
        )
        for filename, data in assets:
            archive.writestr(filename, data)
    print(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exercise", choices=[*BUILDERS, "all"], default="all")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output and args.exercise == "all":
        parser.error("--output requires a single --exercise")

    exercises = list(BUILDERS) if args.exercise == "all" else [args.exercise]
    for exercise in exercises:
        output = (
            args.output.resolve()
            if args.output
            else OUTPUT_DIR / exercise / "projet.sb3"
        )
        write_project(exercise, output)


if __name__ == "__main__":
    main()
