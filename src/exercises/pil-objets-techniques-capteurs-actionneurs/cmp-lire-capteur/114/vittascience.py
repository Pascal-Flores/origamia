"""
Auteur: Origamia
Interface: microbit
Nom du projet: 114 - Panique dans la glaciere
Description: Choisir le capteur qui mesure la temperature de la glaciere.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex114_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex114_forever_0" x="350" y="20"><statement name="DO"><block type="communication_serialWrite" id="ex114_display_0"><mutation newlines="false" /><next><block type="io_pause" id="ex114_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex114_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></statement></block><block type="sensors_getTemperature" id="ex114_candidate1_0" x="850" y="20"><field name="UNIT">CELSIUS</field></block><block type="io_micro_getSoundLevel" id="ex114_candidate2_0" x="850" y="130" /></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Le programme est volontairement incomplet : un bloc doit etre place dans print().
from microbit import *

import utime

while True:
    print()
    utime.sleep(1)

# Blocs candidats, laisses non connectes dans l'espace de travail.
temperature()
microphone.sound_level()
