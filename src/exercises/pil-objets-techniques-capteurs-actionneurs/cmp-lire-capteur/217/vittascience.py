"""
Auteur: Origamia
Interface: microbit
Nom du projet: 217 - Lumière dans le casier
Description: Choisir la luminosité réellement mesurée par le capteur.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex217_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex217_forever_0" x="350" y="20"><statement name="DO"><block type="communication_serialWrite" id="ex217_display_0"><mutation newlines="false" /><next><block type="io_pause" id="ex217_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex217_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></statement></block><block type="sensors_getLight" id="ex217_candidate1_0" x="850" y="20" /><block type="math_number" id="ex217_candidate2_0" x="850" y="130"><field name="NUM">100</field></block><block type="text" id="ex217_candidate3_0" x="850" y="240"><field name="TEXT">Lumière</field></block></xml>
"""
# Le programme est genere a partir des blocs du projet Vittascience.
# Le programme est volontairement incomplet : un bloc doit etre place dans print().
from microbit import *
import utime

while True:
    print()
    utime.sleep(1)

# Blocs candidats, laisses non connectes dans l'espace de travail.
display.read_light_level()
100
'Lumière'
