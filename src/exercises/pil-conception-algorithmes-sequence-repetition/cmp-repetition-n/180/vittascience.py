"""
Auteur: Origamia
Interface: python
Nom du projet: 180 - L'échelle de la cabane
Description: Programme Turtle développé sans boucle : un motif de cinq instructions est répété six fois pour tracer six barreaux et le montant gauche d'une échelle, puis le second montant est tracé.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="turtle_turn" id="b1" x="30" y="30"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="n1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b2"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n2"><field name="NUM">20</field></shadow></value><next><block type="turtle_direction" id="b3"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="n3"><field name="NUM">20</field></shadow></value><next><block type="turtle_turn" id="b4"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="n4"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b5"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n5"><field name="NUM">80</field></shadow></value><next><block type="turtle_direction" id="b6"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="n6"><field name="NUM">80</field></shadow></value><next><block type="turtle_turn" id="b7"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="n7"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b8"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n8"><field name="NUM">35</field></shadow></value><next><block type="turtle_turn" id="b9"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="n9"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b10"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n10"><field name="NUM">80</field></shadow></value><next><block type="turtle_direction" id="b11"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="n11"><field name="NUM">80</field></shadow></value><next><block type="turtle_turn" id="b12"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="n12"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b13"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n13"><field name="NUM">35</field></shadow></value><next><block type="turtle_turn" id="b14"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="n14"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b15"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n15"><field name="NUM">80</field></shadow></value><next><block type="turtle_direction" id="b16"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="n16"><field name="NUM">80</field></shadow></value><next><block type="turtle_turn" id="b17"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="n17"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b18"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n18"><field name="NUM">35</field></shadow></value><next><block type="turtle_turn" id="b19"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="n19"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b20"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n20"><field name="NUM">80</field></shadow></value><next><block type="turtle_direction" id="b21"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="n21"><field name="NUM">80</field></shadow></value><next><block type="turtle_turn" id="b22"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="n22"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b23"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n23"><field name="NUM">35</field></shadow></value><next><block type="turtle_turn" id="b24"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="n24"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b25"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n25"><field name="NUM">80</field></shadow></value><next><block type="turtle_direction" id="b26"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="n26"><field name="NUM">80</field></shadow></value><next><block type="turtle_turn" id="b27"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="n27"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b28"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n28"><field name="NUM">35</field></shadow></value><next><block type="turtle_turn" id="b29"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="n29"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b30"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n30"><field name="NUM">80</field></shadow></value><next><block type="turtle_direction" id="b31"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="n31"><field name="NUM">80</field></shadow></value><next><block type="turtle_turn" id="b32"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="n32"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b33"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n33"><field name="NUM">35</field></shadow></value><next><block type="turtle_turn" id="b34"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="n34"><field name="NUM">90</field></shadow></value><next><block type="turtle_pen" id="b35"><field name="PEN">UP</field><next><block type="turtle_direction" id="b36"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n35"><field name="NUM">80</field></shadow></value><next><block type="turtle_pen" id="b37"><field name="PEN">DOWN</field><next><block type="turtle_turn" id="b38"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="n36"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b39"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="n37"><field name="NUM">230</field></shadow></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>

Projet généré pour import dans Vittascience.
Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau
sur l'interface http://vittascience.com/python

"""

import turtle

turtle.right(90)
turtle.forward(20)
turtle.backward(20)
turtle.left(90)
turtle.forward(80)
turtle.backward(80)
turtle.left(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(80)
turtle.backward(80)
turtle.left(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(80)
turtle.backward(80)
turtle.left(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(80)
turtle.backward(80)
turtle.left(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(80)
turtle.backward(80)
turtle.left(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(80)
turtle.backward(80)
turtle.left(90)
turtle.forward(35)
turtle.right(90)
turtle.penup()
turtle.forward(80)
turtle.pendown()
turtle.right(90)
turtle.forward(230)
