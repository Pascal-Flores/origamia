"""
Auteur: Origamia
Interface: python
Nom du projet: 180 - L'échelle de la cabane
Description: Programme Turtle développé sans boucle : le motif avancer puis reculer est répété six fois pour tracer six barreaux d'une échelle.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="turtle_direction" id="b1a" x="30" y="30"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="b1an"><field name="NUM">50</field></shadow></value><next><block type="turtle_direction" id="b1b"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="b1bn"><field name="NUM">50</field></shadow></value><next><block type="turtle_goto" id="g1"><value name="X"><shadow type="math_number" id="g1xn"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number" id="g1yn"><field name="NUM">30</field></shadow></value><next><block type="turtle_direction" id="b2a"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="b2an"><field name="NUM">50</field></shadow></value><next><block type="turtle_direction" id="b2b"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="b2bn"><field name="NUM">50</field></shadow></value><next><block type="turtle_goto" id="g2"><value name="X"><shadow type="math_number" id="g2xn"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number" id="g2yn"><field name="NUM">60</field></shadow></value><next><block type="turtle_direction" id="b3a"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="b3an"><field name="NUM">50</field></shadow></value><next><block type="turtle_direction" id="b3b"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="b3bn"><field name="NUM">50</field></shadow></value><next><block type="turtle_goto" id="g3"><value name="X"><shadow type="math_number" id="g3xn"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number" id="g3yn"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="b4a"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="b4an"><field name="NUM">50</field></shadow></value><next><block type="turtle_direction" id="b4b"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="b4bn"><field name="NUM">50</field></shadow></value><next><block type="turtle_goto" id="g4"><value name="X"><shadow type="math_number" id="g4xn"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number" id="g4yn"><field name="NUM">120</field></shadow></value><next><block type="turtle_direction" id="b5a"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="b5an"><field name="NUM">50</field></shadow></value><next><block type="turtle_direction" id="b5b"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="b5bn"><field name="NUM">50</field></shadow></value><next><block type="turtle_goto" id="g5"><value name="X"><shadow type="math_number" id="g5xn"><field name="NUM">0</field></shadow></value><value name="Y"><shadow type="math_number" id="g5yn"><field name="NUM">150</field></shadow></value><next><block type="turtle_direction" id="b6a"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="b6an"><field name="NUM">50</field></shadow></value><next><block type="turtle_direction" id="b6b"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="b6bn"><field name="NUM">50</field></shadow></value><next><block type="turtle_goto" id="gtop"><value name="X"><shadow type="math_number" id="gtopxn"><field name="NUM">50</field></shadow></value><value name="Y"><shadow type="math_number" id="gtopyn"><field name="NUM">150</field></shadow></value><next><block type="turtle_goto" id="gbot"><value name="X"><shadow type="math_number" id="gbotxn"><field name="NUM">50</field></shadow></value><value name="Y"><shadow type="math_number" id="gbotyn"><field name="NUM">0</field></shadow></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>

Projet généré pour import dans Vittascience.
Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau
sur l'interface http://vittascience.com/python

"""

import turtle

turtle.forward(50)
turtle.backward(50)
turtle.goto(0,30)
turtle.forward(50)
turtle.backward(50)
turtle.goto(0,60)
turtle.forward(50)
turtle.backward(50)
turtle.goto(0,90)
turtle.forward(50)
turtle.backward(50)
turtle.goto(0,120)
turtle.forward(50)
turtle.backward(50)
turtle.goto(0,150)
turtle.forward(50)
turtle.backward(50)
turtle.goto(50,150)
turtle.goto(50,0)
