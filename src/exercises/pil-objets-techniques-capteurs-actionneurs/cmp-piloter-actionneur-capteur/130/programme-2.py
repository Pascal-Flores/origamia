"""
Auteur: Origamia
Interface: microbit
Nom du projet: 130 - Programme 2
Description: Comparer une liaison entre un capteur de lumiere et un ventilateur.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex130_p2_start" deletable="false" x="20" y="20" /><block type="forever" id="ex130_p2_forever" x="350" y="20"><statement name="DO"><block type="actuators_setFanPower" id="ex130_p2_fan"><field name="PIN">pin2</field><value name="POWER"><shadow type="math_number" id="ex130_p2_fan_value"><field name="NUM">512</field></shadow></value><next><block type="communication_serialWrite" id="ex130_p2_console"><mutation newlines="false" /><value name="TEXT"><block type="sensors_getGroveLight" id="ex130_p2_light"><field name="PIN">pin1</field></block></value><next><block type="io_pause" id="ex130_p2_pause"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex130_p2_pause_value"><field name="NUM">1</field></shadow></value></block></next></block></next></block></statement></block></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
from microbit import *
import utime


while True:
    pin2.write_analog(512)
    print(str(pin1.read_analog()))
    utime.sleep(1)
