"""
Auteur: Origamia
Interface: microbit
Nom du projet: 229 - La lumière fait tourner le mobile
Description: Relier directement la lumière mesurée à la puissance du ventilateur.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex229_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex229_forever_0" x="350" y="20"><statement name="DO"><block type="actuators_setFanPower" id="ex229_fan_0"><field name="PIN">pin2</field><next><block type="io_pause" id="ex229_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex229_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></statement></block><block type="sensors_getGroveLight" id="ex229_light_0" x="850" y="20"><field name="PIN">pin1</field></block></xml>
"""
# Le programme est volontairement incomplet : la lumière doit régler la puissance.
from microbit import *
import utime

while True:
    pin2.write_analog()
    utime.sleep(1)

# Bloc fourni, laissé non connecté dans l'espace de travail.
pin1.read_analog()
