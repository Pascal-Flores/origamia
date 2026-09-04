"""
Auteur: Origamia
Interface: microbit
Nom du projet: 221 - Quai sous surveillance
Description: Observer la température, le niveau sonore et la luminosité sur une maquette de quai.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex221_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex221_forever_0" x="350" y="20"><statement name="DO"><block type="communication_serialWrite" id="ex221_reading1_0"><mutation newlines="false" /><value name="TEXT"><block type="sensors_getTemperature" id="ex221_sensor1_0"><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="ex221_reading2_0"><mutation newlines="false" /><value name="TEXT"><block type="io_micro_getSoundLevel" id="ex221_sensor2_0" /></value><next><block type="communication_serialWrite" id="ex221_reading3_0"><mutation newlines="false" /><value name="TEXT"><block type="sensors_getLight" id="ex221_sensor3_0" /></value><next><block type="io_pause" id="ex221_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex221_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></next></block></next></block></statement></block></xml>
"""
# Le programme est genere a partir des blocs du projet Vittascience.
from microbit import *
import utime

while True:
    print(str(temperature()))
    print(str(microphone.sound_level()))
    print(str(display.read_light_level()))
    utime.sleep(1)
