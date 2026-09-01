"""
Auteur: Origamia
Interface: python
Nom du projet: 177 - Rosace à quatre cercles
Description: Solution Turtle de l'exercice 177 : quatre cercles identiques partant du même point dans quatre directions.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="turtle_circle" id="ex177_circle1" x="30" y="30"><value name="RADIUS"><shadow type="math_number" id="ex177_r1"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex177_turn1"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex177_a1"><field name="NUM">90</field></shadow></value><next><block type="turtle_circle" id="ex177_circle2"><value name="RADIUS"><shadow type="math_number" id="ex177_r2"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex177_turn2"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex177_a2"><field name="NUM">90</field></shadow></value><next><block type="turtle_circle" id="ex177_circle3"><value name="RADIUS"><shadow type="math_number" id="ex177_r3"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex177_turn3"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex177_a3"><field name="NUM">90</field></shadow></value><next><block type="turtle_circle" id="ex177_circle4"><value name="RADIUS"><shadow type="math_number" id="ex177_r4"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex177_turn4"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex177_a4"><field name="NUM">90</field></shadow></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>

Projet généré pour import dans Vittascience.
Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau
sur l'interface http://vittascience.com/python

"""

import turtle

turtle.circle(50)
turtle.right(90)
turtle.circle(50)
turtle.right(90)
turtle.circle(50)
turtle.right(90)
turtle.circle(50)
turtle.right(90)
