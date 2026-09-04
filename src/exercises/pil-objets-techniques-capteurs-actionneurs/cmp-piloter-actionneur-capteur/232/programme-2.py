"""
Auteur: Origamia
Interface: microbit
Nom du projet: 232 - Programme 2
Description: Comparer une liaison entre un capteur de qualité de l'air et un ventilateur.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex232_p2_start" deletable="false" x="20" y="20" /><block type="forever" id="ex232_p2_forever" x="350" y="20"><statement name="DO"><block type="actuators_setFanPower" id="ex232_p2_fan"><field name="PIN">pin2</field><value name="POWER"><block type="sensors_getAirQualityValue" id="ex232_p2_air"><field name="PIN">pin1</field></block></value><next><block type="communication_serialWrite" id="ex232_p2_console"><mutation newlines="false" /><value name="TEXT"><shadow type="math_number" id="ex232_p2_console_value"><field name="NUM">512</field></shadow></value><next><block type="io_pause" id="ex232_p2_pause"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex232_p2_pause_value"><field name="NUM">1</field></shadow></value></block></next></block></next></block></statement></block></xml>
"""
from microbit import *
import utime

while True:
    pin2.write_analog(pin1.read_analog())
    print(str(512))
    utime.sleep(1)
