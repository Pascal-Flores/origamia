"""
Auteur: Origamia
Interface: microbit
Nom du projet: 113 - Cerf-volant, vent devant !
Description: Choisir le capteur qui mesure la vitesse du vent.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex113_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex113_forever_0" x="350" y="20"><statement name="DO"><block type="communication_serialWrite" id="ex113_display_0"><mutation newlines="false" /><next><block type="io_pause" id="ex113_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex113_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></statement></block><block type="sensors_weatherbit_anemometer_getSpeed" id="ex113_candidate1_0" x="850" y="20"><field name="UNIT">M_S</field></block><block type="sensors_weatherbit_weathercock_getDirection" id="ex113_candidate2_0" x="850" y="130" /></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Le programme est volontairement incomplet : un bloc doit etre place dans print().
from microbit import *

import utime

while True:
    print()
    utime.sleep(1)

# Blocs candidats, laisses non connectes dans l'espace de travail.
anemometer_getWindSpeed(pin8, unit='m/s')
weathercock_getDirection(pin1)
