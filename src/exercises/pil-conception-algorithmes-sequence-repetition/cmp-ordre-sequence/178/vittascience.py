"""
Auteur: Origamia
Interface: python
Nom du projet: 178 - Le pictogramme de la clé
Description: Solution Turtle de l'exercice 178 : un anneau rond, une tige et un panneton en angle droit.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="turtle_circle" id="ex178_circle" x="30" y="30"><value name="RADIUS"><shadow type="math_number" id="ex178_radius"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex178_turn1"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex178_angle1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex178_forward1"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex178_dist1"><field name="NUM">50</field></shadow></value><next><block type="turtle_direction" id="ex178_forward2"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex178_dist2"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex178_turn2"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="ex178_angle2"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex178_forward3"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex178_dist3"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex178_turn3"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex178_angle3"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex178_forward4"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex178_dist4"><field name="NUM">50</field></shadow></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>

Projet généré pour import dans Vittascience.
Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau
sur l'interface http://vittascience.com/python

"""

import turtle

turtle.circle(50)
turtle.right(90)
turtle.forward(50)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
