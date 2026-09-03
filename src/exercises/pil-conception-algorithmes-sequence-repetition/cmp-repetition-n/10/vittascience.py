"""
Auteur: Origamia
Interface: python
Nom du projet: 10 - L'escalier vers l'étage
Description: Programme Turtle développé sans boucle : un motif de quatre instructions est répété trois fois pour tracer un escalier.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="turtle_direction" id="ex10_forward1" x="30" y="30"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex10_dist1"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex10_left1"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="ex10_angle1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex10_forward2"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex10_dist2"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex10_right1"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex10_angle2"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex10_forward3"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex10_dist3"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex10_left2"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="ex10_angle3"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex10_forward4"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex10_dist4"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex10_right2"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex10_angle4"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex10_forward5"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex10_dist5"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex10_left3"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="ex10_angle5"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex10_forward6"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex10_dist6"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex10_right3"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex10_angle6"><field name="NUM">90</field></shadow></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>

Projet généré pour import dans Vittascience.
Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau
sur l'interface http://vittascience.com/python

"""

import turtle

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
