"""
Auteur: Origamia
Interface: python
Nom du projet: 180 - L'échelle de la cabane
Description: Programme Turtle développé sans boucle : les deux montants sont tracés séparément puis le motif avancer 80 / reculer 80 est répété six fois pour tracer les barreaux.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="turtle_pen" id="b1" x="30" y="30"><field name="PEN">UP</field><next><block type="turtle_goto" id="b2"><value name="X"><shadow type="math_number" id="b2x"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number" id="b2y"><field name="NUM">-110</field></shadow></value><next><block type="turtle_pen" id="b3"><field name="PEN">DOWN</field><next><block type="turtle_goto" id="b4"><value name="X"><shadow type="math_number" id="b4x"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number" id="b4y"><field name="NUM">110</field></shadow></value><next><block type="turtle_pen" id="b5"><field name="PEN">UP</field><next><block type="turtle_goto" id="b6"><value name="X"><shadow type="math_number" id="b6x"><field name="NUM">80</field></shadow></value><value name="Y"><shadow type="math_number" id="b6y"><field name="NUM">-110</field></shadow></value><next><block type="turtle_pen" id="b7"><field name="PEN">DOWN</field><next><block type="turtle_goto" id="b8"><value name="X"><shadow type="math_number" id="b8x"><field name="NUM">80</field></shadow></value><value name="Y"><shadow type="math_number" id="b8y"><field name="NUM">110</field></shadow></value><next><block type="turtle_pen" id="b9"><field name="PEN">UP</field><next><block type="turtle_goto" id="b10"><value name="X"><shadow type="math_number" id="b10x"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number" id="b10y"><field name="NUM">-80</field></shadow></value><next><block type="turtle_pen" id="b11"><field name="PEN">DOWN</field><next><block type="turtle_direction" id="b12"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="b12n"><field name="NUM">80</field></shadow></value><next><block type="turtle_direction" id="b13"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="b13n"><field name="NUM">80</field></shadow></value><next><block type="turtle_pen" id="b14"><field name="PEN">UP</field><next><block type="turtle_goto" id="b15"><value name="X"><shadow type="math_number" id="b15x"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number" id="b15y"><field name="NUM">-48</field></shadow></value><next><block type="turtle_pen" id="b16"><field name="PEN">DOWN</field><next><block type="turtle_direction" id="b17"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="b17n"><field name="NUM">80</field></shadow></value><next><block type="turtle_direction" id="b18"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="b18n"><field name="NUM">80</field></shadow></value><next><block type="turtle_pen" id="b19"><field name="PEN">UP</field><next><block type="turtle_goto" id="b20"><value name="X"><shadow type="math_number" id="b20x"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number" id="b20y"><field name="NUM">-16</field></shadow></value><next><block type="turtle_pen" id="b21"><field name="PEN">DOWN</field><next><block type="turtle_direction" id="b22"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="b22n"><field name="NUM">80</field></shadow></value><next><block type="turtle_direction" id="b23"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="b23n"><field name="NUM">80</field></shadow></value><next><block type="turtle_pen" id="b24"><field name="PEN">UP</field><next><block type="turtle_goto" id="b25"><value name="X"><shadow type="math_number" id="b25x"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number" id="b25y"><field name="NUM">16</field></shadow></value><next><block type="turtle_pen" id="b26"><field name="PEN">DOWN</field><next><block type="turtle_direction" id="b27"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="b27n"><field name="NUM">80</field></shadow></value><next><block type="turtle_direction" id="b28"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="b28n"><field name="NUM">80</field></shadow></value><next><block type="turtle_pen" id="b29"><field name="PEN">UP</field><next><block type="turtle_goto" id="b30"><value name="X"><shadow type="math_number" id="b30x"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number" id="b30y"><field name="NUM">48</field></shadow></value><next><block type="turtle_pen" id="b31"><field name="PEN">DOWN</field><next><block type="turtle_direction" id="b32"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="b32n"><field name="NUM">80</field></shadow></value><next><block type="turtle_direction" id="b33"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="b33n"><field name="NUM">80</field></shadow></value><next><block type="turtle_pen" id="b34"><field name="PEN">UP</field><next><block type="turtle_goto" id="b35"><value name="X"><shadow type="math_number" id="b35x"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number" id="b35y"><field name="NUM">80</field></shadow></value><next><block type="turtle_pen" id="b36"><field name="PEN">DOWN</field><next><block type="turtle_direction" id="b37"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="b37n"><field name="NUM">80</field></shadow></value><next><block type="turtle_direction" id="b38"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="b38n"><field name="NUM">80</field></shadow></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>

Projet généré pour import dans Vittascience.
Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau
sur l'interface http://vittascience.com/python

"""

import turtle

turtle.penup()
turtle.goto(0,-110)
turtle.pendown()
turtle.goto(0,110)
turtle.penup()
turtle.goto(80,-110)
turtle.pendown()
turtle.goto(80,110)
turtle.penup()
turtle.goto(0,-80)
turtle.pendown()
turtle.forward(80)
turtle.backward(80)
turtle.penup()
turtle.goto(0,-48)
turtle.pendown()
turtle.forward(80)
turtle.backward(80)
turtle.penup()
turtle.goto(0,-16)
turtle.pendown()
turtle.forward(80)
turtle.backward(80)
turtle.penup()
turtle.goto(0,16)
turtle.pendown()
turtle.forward(80)
turtle.backward(80)
turtle.penup()
turtle.goto(0,48)
turtle.pendown()
turtle.forward(80)
turtle.backward(80)
turtle.penup()
turtle.goto(0,80)
turtle.pendown()
turtle.forward(80)
turtle.backward(80)
