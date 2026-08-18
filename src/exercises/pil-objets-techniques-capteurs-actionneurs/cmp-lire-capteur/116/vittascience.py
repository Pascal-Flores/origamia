"""
Auteur: Origamia
Interface: microbit
Nom du projet: 116 - SOS vieux papiers
Description: Observer les lectures de luminosite, de temperature et de CO2 dans un centre d'archives.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex116_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex116_forever_0" x="350" y="20"><statement name="DO"><block type="communication_serialWrite" id="ex116_reading1_0"><mutation newlines="false" /><value name="TEXT"><block type="sensors_getLight" id="ex116_sensor1_0" /></value><next><block type="communication_serialWrite" id="ex116_reading2_0"><mutation newlines="false" /><value name="TEXT"><block type="sensors_getTemperature" id="ex116_sensor2_0"><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="ex116_reading3_0"><mutation newlines="false" /><value name="TEXT"><block type="sensors_getSgp30Gas" id="ex116_sensor3_0"><field name="GAS">CO2</field></block></value><next><block type="io_pause" id="ex116_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex116_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></next></block></next></block></statement></block></xml>
"""
# Le programme est genere a partir des blocs du projet Vittascience.
from microbit import *
import utime

from sgp30 import SGP30

sgp30 = SGP30()

while True:
    print(str(display.read_light_level()))
    print(str(temperature()))
    print(str(sgp30.eCO2()))
    utime.sleep(1)

