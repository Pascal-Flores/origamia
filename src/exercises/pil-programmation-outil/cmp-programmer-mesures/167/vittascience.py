"""
Auteur: Origamia
Interface: microbit
Nom du projet: 167 - Debout, les capteurs !
Description: Planche de capture des cinq groupes de blocs a classer.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex167_start" deletable="false" x="20" y="20" /><block type="forever" id="ex167_forever" x="20" y="300" /><block type="communication_log_setLabel" id="ex167_item1_labels" x="650" y="20"><mutation items="2" /><field name="TIMESTAMP">MILLISECONDS</field><value name="ADD0"><shadow type="text" id="ex167_item1_temperature_label"><field name="TEXT">temperature</field></shadow></value><value name="ADD1"><shadow type="text" id="ex167_item1_light_label"><field name="TEXT">luminosite</field></shadow></value></block><block type="communication_log_addData" id="ex167_item2_measure" x="650" y="220"><mutation items="2" /><value name="ADD0"><block type="communication_log_data" id="ex167_item2_temperature_data"><value name="LABEL"><shadow type="text" id="ex167_item2_temperature_label"><field name="TEXT">temperature</field></shadow></value><value name="DATA"><block type="sensors_getTemperature" id="ex167_item2_temperature"><field name="UNIT">CELSIUS</field></block></value></block></value><value name="ADD1"><block type="communication_log_data" id="ex167_item2_light_data"><value name="LABEL"><shadow type="text" id="ex167_item2_light_label"><field name="TEXT">luminosite</field></shadow></value><value name="DATA"><block type="sensors_getLight" id="ex167_item2_light" /></value></block></value></block><block type="io_pause" id="ex167_item3_pause" x="650" y="460"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex167_item3_pause_time"><field name="NUM">2</field></shadow></value></block><block type="communication_log_addData" id="ex167_item4_incomplete" x="650" y="620"><mutation items="1" /><value name="ADD0"><block type="communication_log_data" id="ex167_item4_temperature_data"><value name="LABEL"><shadow type="text" id="ex167_item4_temperature_label"><field name="TEXT">temperature</field></shadow></value><value name="DATA"><block type="sensors_getTemperature" id="ex167_item4_temperature"><field name="UNIT">CELSIUS</field></block></value></block></value></block><block type="communication_serialWrite" id="ex167_item5_console_temperature" x="650" y="840"><mutation newlines="false" /><value name="TEXT"><block type="sensors_getTemperature" id="ex167_item5_temperature"><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="ex167_item5_console_light"><mutation newlines="false" /><value name="TEXT"><block type="sensors_getLight" id="ex167_item5_light" /></value></block></next></block></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Les groupes restent deconnectes dans l'espace de travail pour les captures.
from microbit import *
import log

log.set_labels('temperature', 'luminosite', timestamp=log.MILLISECONDS)

log.add(temperature=temperature(), luminosite=display.read_light_level())

sleep(2000)

log.add(temperature=temperature())

print(temperature())
print(display.read_light_level())
