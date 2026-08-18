"""
Auteur: Origamia
Interface: microbit
Nom du projet: 112 - Basilic sous surveillance
Description: Choisir le capteur qui mesure l'humidité de la terre.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex112_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex112_forever_0" x="350" y="20"><statement name="DO"><block type="communication_serialWrite" id="ex112_display_0"><mutation newlines="false" /><next><block type="io_pause" id="ex112_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex112_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></statement></block><block type="sensors_getGroveMoisture" id="ex112_candidate1_0" x="850" y="20"><field name="PIN">pin1</field></block><block type="sensors_getGroveWaterAmount" id="ex112_candidate2_0" x="850" y="130"><field name="PIN">pin1</field></block></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Le programme est volontairement incomplet : un bloc doit etre place dans print().
from microbit import *

import utime

while True:
    print()
    utime.sleep(1)

# Blocs candidats, laisses non connectes dans l'espace de travail.
pin1.read_analog()
pin1.read_analog()
