#!/usr/bin/env python3
"""Generate importable Vittascience projects for the sensor-reading exercises."""

from __future__ import annotations

import argparse
import ast
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
import re
import xml.etree.ElementTree as ET


BLOCKLY_NAMESPACE = "https://developers.google.com/blockly/xml"
ET.register_namespace("", BLOCKLY_NAMESPACE)

DEFAULT_OUTPUT_ROOT = Path(
    "src/exercises/pil-objets-techniques-capteurs-actionneurs/cmp-lire-capteur"
)


@dataclass(frozen=True)
class CandidateSpec:
    block_type: str
    python: str
    fields: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class ProjectSpec:
    number: int
    name: str
    description: str
    candidates: tuple[CandidateSpec, ...]
    repeat_forever: bool = False
    pause_seconds: int = 1
    observation_program: bool = False
    python_imports: tuple[str, ...] = ()
    python_setup: tuple[str, ...] = ()
    python_helpers: str = ""


WEATHERBIT_HELPERS = """def weathercock_getDirection(pin):
    wind_dir = pin.read_analog()
    if 886 < wind_dir < 906:
        return "N"
    if 692 < wind_dir < 712:
        return "NE"
    if 395 < wind_dir < 415:
        return "E"
    if 478 < wind_dir < 498:
        return "SE"
    if 564 < wind_dir < 584:
        return "S"
    if 799 < wind_dir < 819:
        return "SW"
    if 968 < wind_dir < 988:
        return "W"
    if 939 < wind_dir < 959:
        return "NW"
    return "???"


def pulseIn(pin, pulse_state, max_duration=2000000):
    initial_time = utime.ticks_us()
    while pin.read_digital() is not pulse_state:
        if utime.ticks_us() - initial_time > max_duration:
            return 0
    start = utime.ticks_us()
    while pin.read_digital() == pulse_state:
        if utime.ticks_us() - initial_time > max_duration:
            return 0
    return utime.ticks_us() - start


def anemometer_getWindSpeed(pin, unit="m/s", pulse_per_revolution=1):
    speed_of_one_pulse = 0.66666667 / pulse_per_revolution
    pulse_microseconds = pulseIn(pin, 1, max_duration=1000000)
    if pulse_microseconds <= 0:
        return 0
    pulses_per_second = pulse_per_revolution / (pulse_microseconds / 1e6)
    speed = speed_of_one_pulse * pulses_per_second
    if unit == "km/h":
        return speed * 3600 / 1e3
    if unit == "inch/s":
        return speed / 2.54
    if unit == "knot":
        return speed / 0.514444444
    return speed
"""


PROJECTS = (
    ProjectSpec(
        number=109,
        name="Météo en direct",
        description="Choisir la valeur mesurée par le thermomètre.",
        candidates=(
            CandidateSpec("sensors_getTemperature", "temperature()"),
            CandidateSpec("math_number", "20", (("NUM", "20"),)),
            CandidateSpec("text", repr("Température"), (("TEXT", "Température"),)),
        ),
        repeat_forever=True,
    ),
    ProjectSpec(
        number=110,
        name="Le son du moment",
        description="Choisir le niveau sonore mesuré par le microphone.",
        candidates=(
            CandidateSpec("io_micro_getSoundLevel", "microphone.sound_level()"),
            CandidateSpec("math_number", "50", (("NUM", "50"),)),
            CandidateSpec("text", repr("Bruit"), (("TEXT", "Bruit"),)),
        ),
        repeat_forever=True,
    ),
    ProjectSpec(
        number=111,
        name="Cap sur le nord",
        description="Choisir la direction mesurée par la boussole.",
        candidates=(
            CandidateSpec("sensors_getCompass", "compass.heading()"),
            CandidateSpec("math_number", "90", (("NUM", "90"),)),
            CandidateSpec("text", repr("Nord"), (("TEXT", "Nord"),)),
        ),
        repeat_forever=True,
    ),
    ProjectSpec(
        number=112,
        name="Basilic sous surveillance",
        description="Choisir le capteur qui mesure l'humidité de la terre.",
        candidates=(
            CandidateSpec("sensors_getGroveMoisture", "pin1.read_analog()"),
            CandidateSpec("sensors_getGroveWaterAmount", "pin1.read_analog()"),
        ),
        repeat_forever=True,
    ),
    ProjectSpec(
        number=113,
        name="Cerf-volant, vent devant !",
        description="Choisir le capteur qui mesure la vitesse du vent.",
        candidates=(
            CandidateSpec(
                "sensors_weatherbit_anemometer_getSpeed",
                "anemometer_getWindSpeed(pin8, unit='m/s')",
            ),
            CandidateSpec(
                "sensors_weatherbit_weathercock_getDirection",
                "weathercock_getDirection(pin1)",
            ),
        ),
        repeat_forever=True,
    ),
    ProjectSpec(
        number=114,
        name="Panique dans la glaciere",
        description="Choisir le capteur qui mesure la temperature de la glaciere.",
        candidates=(
            CandidateSpec("sensors_getTemperature", "temperature()"),
            CandidateSpec("io_micro_getSoundLevel", "microphone.sound_level()"),
        ),
        repeat_forever=True,
    ),
    ProjectSpec(
        number=115,
        name="Concert sous controle",
        description=(
            "Observer les lectures du microphone, du thermometre et du capteur "
            "de luminosite."
        ),
        candidates=(
            CandidateSpec("io_micro_getSoundLevel", "microphone.sound_level()"),
            CandidateSpec("sensors_getTemperature", "temperature()"),
            CandidateSpec("sensors_getLight", "display.read_light_level()"),
        ),
        repeat_forever=True,
        observation_program=True,
    ),
    ProjectSpec(
        number=116,
        name="SOS vieux papiers",
        description=(
            "Observer les lectures de luminosite, de temperature et de CO2 "
            "dans un centre d'archives."
        ),
        candidates=(
            CandidateSpec("sensors_getLight", "display.read_light_level()"),
            CandidateSpec("sensors_getTemperature", "temperature()"),
            CandidateSpec(
                "sensors_getSgp30Gas",
                "sgp30.eCO2()",
                (("GAS", "CO2"),),
            ),
        ),
        repeat_forever=True,
        observation_program=True,
        python_imports=("from sgp30 import SGP30",),
        python_setup=("sgp30 = SGP30()",),
    ),
    ProjectSpec(
        number=117,
        name="Vent dans les voiles",
        description=(
            "Observer la vitesse du vent, sa direction et le cap mesure "
            "par la boussole."
        ),
        candidates=(
            CandidateSpec(
                "sensors_weatherbit_anemometer_getSpeed",
                "anemometer_getWindSpeed(pin8, unit='m/s')",
            ),
            CandidateSpec(
                "sensors_weatherbit_weathercock_getDirection",
                "weathercock_getDirection(pin1)",
            ),
            CandidateSpec("sensors_getCompass", "compass.heading()"),
        ),
        repeat_forever=True,
        observation_program=True,
        python_setup=("pin8.set_pull(pin8.PULL_UP)",),
        python_helpers=WEATHERBIT_HELPERS,
    ),
)


def qname(local_name: str) -> str:
    return f"{{{BLOCKLY_NAMESPACE}}}{local_name}"


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def discover_source(root: Path) -> Path:
    candidates = []
    for path in root.glob("*.py"):
        try:
            source = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "Blocks: <xml" in source:
            candidates.append(path)

    if len(candidates) != 1:
        names = ", ".join(path.name for path in candidates) or "aucun"
        raise ValueError(
            "Un unique export Vittascience est attendu a la racine "
            f"(trouves : {names}). Utiliser --source pour le preciser."
        )
    return candidates[0]


def extract_workspace(source_path: Path) -> ET.Element:
    source = source_path.read_text(encoding="utf-8")
    module = ast.parse(source, filename=str(source_path))
    docstring = ast.get_docstring(module, clean=False)
    if not docstring:
        raise ValueError(f"En-tete Vittascience absent de {source_path}")

    match = re.search(
        r"^Blocks:\s*(<xml\b.*</xml>)$",
        docstring,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise ValueError(f"Workspace Blockly absent de {source_path}")
    return ET.fromstring(match.group(1))


def find_prototype(workspace: ET.Element, block_type: str) -> ET.Element:
    for node in workspace.iter():
        if (
            local_name(node.tag) in {"block", "shadow"}
            and node.get("type") == block_type
        ):
            return node
    raise ValueError(f"Bloc {block_type!r} absent du projet source")


def assign_ids(node: ET.Element, prefix: str) -> None:
    index = 0
    for descendant in node.iter():
        if local_name(descendant.tag) in {"block", "shadow"}:
            descendant.set("id", f"{prefix}_{index}")
            index += 1


def clone_block(
    prototypes: dict[str, ET.Element],
    block_type: str,
    block_id: str,
) -> ET.Element:
    block = deepcopy(prototypes[block_type])
    if local_name(block.tag) == "shadow":
        block.tag = qname("block")
    block.attrib.pop("x", None)
    block.attrib.pop("y", None)
    block.attrib.pop("deletable", None)
    assign_ids(block, block_id)
    return block


def set_field(block: ET.Element, field_name: str, value: str) -> None:
    for field in block.iter(qname("field")):
        if field.get("name") == field_name:
            field.text = value
            return
    raise ValueError(
        f"Champ {field_name!r} absent du bloc {block.get('type')!r}"
    )


def build_workspace(
    source_workspace: ET.Element,
    spec: ProjectSpec,
) -> ET.Element:
    required_types = {
        "on_start",
        "communication_serialWrite",
        *(candidate.block_type for candidate in spec.candidates),
    }
    if spec.repeat_forever:
        required_types.update({"forever", "io_pause"})
    prototypes = {
        block_type: find_prototype(source_workspace, block_type)
        for block_type in required_types
    }

    workspace = ET.Element(qname("xml"))

    start = clone_block(prototypes, "on_start", f"ex{spec.number}_start")
    for child in list(start):
        start.remove(child)
    start.set("deletable", "false")
    start.set("x", "20")
    start.set("y", "20")

    workspace.append(start)

    if spec.repeat_forever:
        forever = clone_block(prototypes, "forever", f"ex{spec.number}_forever")
        for child in list(forever):
            forever.remove(child)
        forever.set("x", "350")
        forever.set("y", "20")

        pause = clone_block(prototypes, "io_pause", f"ex{spec.number}_pause")
        for child in list(pause):
            if local_name(child.tag) == "next":
                pause.remove(child)
        set_field(pause, "UNIT", "SEC")
        set_field(pause, "NUM", str(spec.pause_seconds))

        statement = ET.SubElement(forever, qname("statement"), {"name": "DO"})
        if spec.observation_program:
            readings = []
            for index, candidate_spec in enumerate(spec.candidates, start=1):
                serial_write = clone_block(
                    prototypes,
                    "communication_serialWrite",
                    f"ex{spec.number}_reading{index}",
                )
                for child in list(serial_write):
                    if local_name(child.tag) != "mutation":
                        serial_write.remove(child)

                sensor = clone_block(
                    prototypes,
                    candidate_spec.block_type,
                    f"ex{spec.number}_sensor{index}",
                )
                for field_name, field_value in candidate_spec.fields:
                    set_field(sensor, field_name, field_value)
                value = ET.SubElement(
                    serial_write,
                    qname("value"),
                    {"name": "TEXT"},
                )
                value.append(sensor)
                readings.append(serial_write)

            for current, following in zip(readings, readings[1:]):
                next_node = ET.SubElement(current, qname("next"))
                next_node.append(following)
            final_next = ET.SubElement(readings[-1], qname("next"))
            final_next.append(pause)
            statement.append(readings[0])
        else:
            serial_write = clone_block(
                prototypes,
                "communication_serialWrite",
                f"ex{spec.number}_display",
            )
            for child in list(serial_write):
                if local_name(child.tag) != "mutation":
                    serial_write.remove(child)
            serial_next = ET.SubElement(serial_write, qname("next"))
            serial_next.append(pause)
            statement.append(serial_write)
        workspace.append(forever)
    else:
        if spec.observation_program:
            raise ValueError(
                "Un programme d'observation doit utiliser Repeter indefiniment"
            )
        serial_write = clone_block(
            prototypes,
            "communication_serialWrite",
            f"ex{spec.number}_display",
        )
        for child in list(serial_write):
            if local_name(child.tag) != "mutation":
                serial_write.remove(child)
        statement = ET.SubElement(start, qname("statement"), {"name": "DO"})
        statement.append(serial_write)

    if not spec.observation_program:
        for index, candidate_spec in enumerate(spec.candidates, start=1):
            candidate = clone_block(
                prototypes,
                candidate_spec.block_type,
                f"ex{spec.number}_candidate{index}",
            )
            for field_name, field_value in candidate_spec.fields:
                set_field(candidate, field_name, field_value)
            candidate.set("x", "850" if spec.repeat_forever else "620")
            candidate.set("y", str(20 + (index - 1) * 110))
            workspace.append(candidate)

    return workspace


def render_project(spec: ProjectSpec, workspace: ET.Element) -> str:
    workspace_xml = ET.tostring(workspace, encoding="unicode", short_empty_elements=True)
    candidates_python = "\n".join(candidate.python for candidate in spec.candidates)
    if spec.observation_program:
        readings_python = "\n".join(
            f"    print(str({candidate.python}))"
            for candidate in spec.candidates
        )
        program = f"""while True:
{readings_python}
    utime.sleep({spec.pause_seconds})"""
        candidates_section = ""
    elif spec.repeat_forever:
        program = f"""while True:
    print()
    utime.sleep({spec.pause_seconds})"""
        candidates_section = (
            "\n# Blocs candidats, laisses non connectes dans l'espace de travail.\n"
            f"{candidates_python}\n"
        )
    else:
        program = "print()"
        candidates_section = (
            "\n# Blocs candidats, laisses non connectes dans l'espace de travail.\n"
            f"{candidates_python}\n"
        )
    supporting_code = "\n\n".join(
        section
        for section in (
            "\n".join(spec.python_imports),
            spec.python_helpers.strip(),
            "\n".join(spec.python_setup),
        )
        if section
    )
    if supporting_code:
        supporting_code += "\n\n"

    return f'''"""
Auteur: Origamia
Interface: microbit
Nom du projet: {spec.number} - {spec.name}
Description: {spec.description}
Toolbox: vittascience
Mode: mixed

Blocks: {workspace_xml}
"""
# Le programme est genere a partir des blocs du projet Vittascience.
from microbit import *
import utime

{supporting_code}{program}
{candidates_section}
'''


def validate_project(project_text: str, spec: ProjectSpec) -> None:
    module = ast.parse(project_text, filename=f"{spec.number}/vittascience.py")
    docstring = ast.get_docstring(module, clean=False)
    if not docstring:
        raise ValueError(f"En-tete absent du projet {spec.number}")
    match = re.search(
        r"^Blocks:\s*(<xml\b.*</xml>)$",
        docstring,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise ValueError(f"Workspace absent du projet {spec.number}")

    workspace = ET.fromstring(match.group(1))
    top_level = [node.get("type") for node in workspace.findall(qname("block"))]
    expected = ["on_start"]
    if spec.repeat_forever:
        expected.append("forever")
    if not spec.observation_program:
        expected.extend(candidate.block_type for candidate in spec.candidates)
    if top_level != expected:
        raise ValueError(
            f"Blocs de premier niveau invalides pour {spec.number}: {top_level}"
        )

    if spec.repeat_forever:
        forever = find_prototype(workspace, "forever")
        first_repeated = forever.find(
            f"{qname('statement')}[@name='DO']/{qname('block')}"
        )
        if spec.observation_program:
            current = first_repeated
            for candidate_spec in spec.candidates:
                if current is None or current.get("type") != "communication_serialWrite":
                    raise ValueError(
                        f"Une lecture de capteur manque dans le projet {spec.number}"
                    )
                sensor = current.find(
                    f"{qname('value')}[@name='TEXT']/{qname('block')}"
                )
                if sensor is None or sensor.get("type") != candidate_spec.block_type:
                    raise ValueError(
                        f"La lecture {candidate_spec.block_type} est invalide "
                        f"dans le projet {spec.number}"
                    )
                current = current.find(f"{qname('next')}/{qname('block')}")
            pause = current
        else:
            serial = first_repeated
            if serial is None or serial.get("type") != "communication_serialWrite":
                raise ValueError(
                    f"L'ecriture de {spec.number} n'est pas dans Repeter indefiniment"
                )
            if serial.find(qname("value")) is not None:
                raise ValueError(
                    f"L'emplacement de reponse de {spec.number} n'est pas vide"
                )
            pause = serial.find(f"{qname('next')}/{qname('block')}")
        if pause is None or pause.get("type") != "io_pause":
            raise ValueError(f"La pause de {spec.number} est absente")
        set_field(pause, "UNIT", "SEC")
        set_field(pause, "NUM", str(spec.pause_seconds))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        help="Export Vittascience de reference. Par defaut, detection a la racine.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
    )
    parser.add_argument(
        "--exercise",
        type=int,
        action="append",
        help="Numero a generer. Peut etre repete. Par defaut : tous les projets connus.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source_path = args.source or discover_source(Path.cwd())
    source_workspace = extract_workspace(source_path)
    selected = set(args.exercise or [spec.number for spec in PROJECTS])

    unknown = selected - {spec.number for spec in PROJECTS}
    if unknown:
        raise ValueError(f"Exercice(s) non pris en charge : {sorted(unknown)}")

    for spec in PROJECTS:
        if spec.number not in selected:
            continue
        workspace = build_workspace(source_workspace, spec)
        project_text = render_project(spec, workspace)
        validate_project(project_text, spec)

        output_path = args.output_root / str(spec.number) / "vittascience.py"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(project_text, encoding="utf-8", newline="\n")
        print(f"Projet {spec.number} genere : {output_path}")


if __name__ == "__main__":
    main()
