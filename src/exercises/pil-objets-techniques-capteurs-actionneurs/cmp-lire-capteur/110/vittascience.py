"""
Auteur: Origamia
Interface: microbit
Nom du projet: 110 - Le son du moment
Description: Choisir le niveau sonore mesuré par le microphone.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex110_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex110_forever_0" x="350" y="20"><statement name="DO"><block type="communication_serialWrite" id="ex110_display_0"><mutation newlines="false" /><next><block type="io_pause" id="ex110_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex110_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></statement></block><block type="io_micro_getSoundLevel" id="ex110_sensor_0" x="850" y="20" /><block type="math_number" id="ex110_number_0" x="850" y="130"><field name="NUM">50</field></block><block type="text" id="ex110_text_0" x="850" y="240"><field name="TEXT">Bruit</field></block></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Le programme est volontairement incomplet : un bloc doit etre place dans print().
from microbit import *

import utime

while True:
    print()
    utime.sleep(1)

# Blocs candidats, laisses non connectes dans l'espace de travail.
microphone.sound_level()
50
'Bruit'
