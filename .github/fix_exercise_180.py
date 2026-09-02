import re
import xml.etree.ElementTree as E
from pathlib import Path

p = Path("src/exercises/pil-conception-algorithmes-sequence-repetition/cmp-repetition-n/180/vittascience.py")
ops = [
("turn","LEFT",90),("direction","FORWARD",150),("turn","RIGHT",90),
("direction","FORWARD",70),("turn","RIGHT",90),("direction","FORWARD",150),
("turn","RIGHT",90),("direction","FORWARD",70),("turn","RIGHT",90)]
motif = [("pen","UP",0),("direction","FORWARD",30),("turn","RIGHT",90),
("pen","DOWN",0),("direction","FORWARD",70),("direction","BACKWARD",70),
("turn","LEFT",90)]
ops += motif * 4 + [("pen","UP",0),("turn","RIGHT",90),("direction","FORWARD",90)]

def block(i, op):
    kind, action, value = op
    typ = {"turn":"turtle_turn","direction":"turtle_direction","pen":"turtle_pen"}[kind]
    attrs = {"type":typ,"id":f"b{i}"}
    if i == 1:
        attrs.update(x="30", y="30")
    b = E.Element("block", attrs)
    if kind == "pen":
        f = E.SubElement(b, "field", name="PEN")
        f.text = action
    else:
        f = E.SubElement(b, "field", name="DIR")
        f.text = action
        v = E.SubElement(b, "value", name="DISTANCE")
        s = E.SubElement(v, "shadow", type="math_number", id=f"n{i}")
        n = E.SubElement(s, "field", name="NUM")
        n.text = str(value)
    return b

root = E.Element("xml", xmlns="https://developers.google.com/blockly/xml")
bs = [block(i, op) for i, op in enumerate(ops, 1)]
for a, b in zip(bs, bs[1:]):
    E.SubElement(a, "next").append(b)
root.append(bs[0])
xml = E.tostring(root, encoding="unicode")
E.fromstring(xml)

code = ["import turtle", ""]
for kind, action, value in ops:
    if kind == "direction":
        code.append(f"turtle.{'forward' if action == 'FORWARD' else 'backward'}({value})")
    elif kind == "turn":
        code.append(f"turtle.{'left' if action == 'LEFT' else 'right'}({value})")
    else:
        code.append("turtle.penup()" if action == "UP" else "turtle.pendown()")
code = "\n".join(code) + "\n"

q = chr(34) * 3
out = (
    q + "\n"
    "Auteur: Origamia\n"
    "Interface: python\n"
    "Nom du projet: 180 - L'échelle de la cabane\n"
    "Description: Cadre d'échelle puis quatre barreaux intermédiaires tracés par un motif répété.\n"
    "Toolbox: vittascience\n"
    "Mode: mixed\n\n"
    "Blocks: " + xml + "\n\n"
    "Projet généré pour import dans Vittascience.\n"
    "Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau\n"
    "sur l'interface http://vittascience.com/python\n\n"
    + q + "\n\n" + code
)
saved_xml = re.search(r"^Blocks: (.+)$", out, re.M).group(1)
E.fromstring(saved_xml)
assert saved_xml.count("<block") == saved_xml.count("</block>") == 40
assert saved_xml.count("<next>") == saved_xml.count("</next>") == 39
p.write_text(out, encoding="utf-8", newline="\n")
