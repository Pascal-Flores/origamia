"""
Auteur: Origamia
Interface: microbit
Nom du projet: 129 - Applaudis, ca tourne !
Description: Relier directement le niveau sonore a la puissance du ventilateur.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex129_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex129_forever_0" x="350" y="20"><statement name="DO"><block type="actuators_setFanPower" id="ex129_fan_0"><field name="PIN">pin2</field><next><block type="io_pause" id="ex129_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex129_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></statement></block><block type="io_micro_getSoundLevel" id="ex129_sound_0" x="850" y="20" /></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Le programme est volontairement incomplet : le niveau sonore doit regler la puissance.
from microbit import *
import utime


while True:
    pin2.write_analog()
    utime.sleep(1)

# Bloc fourni, laisse non connecte dans l'espace de travail.
microphone.sound_level()
