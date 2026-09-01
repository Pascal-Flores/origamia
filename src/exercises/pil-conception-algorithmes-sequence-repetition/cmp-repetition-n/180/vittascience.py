"""
Auteur: Origamia
Interface: python
Nom du projet: 180 - L'échelle de la cabane
Description: Programme Turtle développé sans boucle : un motif de cinq instructions est répété six fois pour tracer six barreaux, puis le programme rejoint le montant droit stylo levé et le termine.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="turtle_direction" id="ex180_r1_out_0" x="30" y="30"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r1_out_1"><field name="NUM">50</field></shadow></value><next><block type="turtle_direction" id="ex180_r1_back_0"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r1_back_1"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex180_r1_left_0"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r1_left_1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex180_r1_up_0"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r1_up_1"><field name="NUM">30</field></shadow></value><next><block type="turtle_turn" id="ex180_r1_right_0"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r1_right_1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex180_r2_out_0"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r2_out_1"><field name="NUM">50</field></shadow></value><next><block type="turtle_direction" id="ex180_r2_back_0"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r2_back_1"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex180_r2_left_0"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r2_left_1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex180_r2_up_0"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r2_up_1"><field name="NUM">30</field></shadow></value><next><block type="turtle_turn" id="ex180_r2_right_0"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r2_right_1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex180_r3_out_0"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r3_out_1"><field name="NUM">50</field></shadow></value><next><block type="turtle_direction" id="ex180_r3_back_0"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r3_back_1"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex180_r3_left_0"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r3_left_1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex180_r3_up_0"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r3_up_1"><field name="NUM">30</field></shadow></value><next><block type="turtle_turn" id="ex180_r3_right_0"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r3_right_1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex180_r4_out_0"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r4_out_1"><field name="NUM">50</field></shadow></value><next><block type="turtle_direction" id="ex180_r4_back_0"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r4_back_1"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex180_r4_left_0"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r4_left_1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex180_r4_up_0"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r4_up_1"><field name="NUM">30</field></shadow></value><next><block type="turtle_turn" id="ex180_r4_right_0"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r4_right_1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex180_r5_out_0"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r5_out_1"><field name="NUM">50</field></shadow></value><next><block type="turtle_direction" id="ex180_r5_back_0"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r5_back_1"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex180_r5_left_0"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r5_left_1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex180_r5_up_0"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r5_up_1"><field name="NUM">30</field></shadow></value><next><block type="turtle_turn" id="ex180_r5_right_0"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r5_right_1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex180_r6_out_0"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r6_out_1"><field name="NUM">50</field></shadow></value><next><block type="turtle_direction" id="ex180_r6_back_0"><field name="DIR">BACKWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r6_back_1"><field name="NUM">50</field></shadow></value><next><block type="turtle_turn" id="ex180_r6_left_0"><field name="DIR">LEFT</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r6_left_1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex180_r6_up_0"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r6_up_1"><field name="NUM">30</field></shadow></value><next><block type="turtle_turn" id="ex180_r6_right_0"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex180_r6_right_1"><field name="NUM">90</field></shadow></value><next><block type="turtle_pen" id="ex180_tail_penup_0"><field name="PEN">UP</field><next><block type="turtle_direction" id="ex180_tail_cross_0"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_tail_cross_1"><field name="NUM">50</field></shadow></value><next><block type="turtle_pen" id="ex180_tail_pendown_0"><field name="PEN">DOWN</field><next><block type="turtle_turn" id="ex180_tail_down_0"><field name="DIR">RIGHT</field><value name="DISTANCE"><shadow type="math_number" id="ex180_tail_down_1"><field name="NUM">90</field></shadow></value><next><block type="turtle_direction" id="ex180_tail_rail_0"><field name="DIR">FORWARD</field><value name="DISTANCE"><shadow type="math_number" id="ex180_tail_rail_1"><field name="NUM">180</field></shadow></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></xml>

Projet généré pour import dans Vittascience.
Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau
sur l'interface http://vittascience.com/python

"""

import turtle

turtle.forward(50)
turtle.backward(50)
turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(50)
turtle.backward(50)
turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(50)
turtle.backward(50)
turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(50)
turtle.backward(50)
turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(50)
turtle.backward(50)
turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(50)
turtle.backward(50)
turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.right(90)
turtle.forward(180)
