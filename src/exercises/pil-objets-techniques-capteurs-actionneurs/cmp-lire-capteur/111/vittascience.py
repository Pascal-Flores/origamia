"""
Auteur: Origamia
Interface: microbit
Nom du projet: 111 - Cap sur le nord
Description: Choisir la direction mesurée par la boussole.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex111_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex111_forever_0" x="350" y="20"><statement name="DO"><block type="communication_serialWrite" id="ex111_display_0"><mutation newlines="false" /><next><block type="io_pause" id="ex111_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex111_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></statement></block><block type="sensors_getCompass" id="ex111_sensor_0" x="850" y="20" /><block type="math_number" id="ex111_number_0" x="850" y="130"><field name="NUM">90</field></block><block type="text" id="ex111_text_0" x="850" y="240"><field name="TEXT">Nord</field></block></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Le programme est volontairement incomplet : un bloc doit etre place dans print().
from microbit import *

import utime

while True:
    print()
    utime.sleep(1)

# Blocs candidats, laisses non connectes dans l'espace de travail.
compass.heading()
90
'Nord'
