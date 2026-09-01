"""
Auteur: Origamia
Interface: microbit
Nom du projet: 168 - Des nouvelles du pot
Description: Planche de capture des cinq groupes de blocs a classer.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex168_start" deletable="false" x="20" y="20" /><block type="forever" id="ex168_forever" x="20" y="300" /><block type="communication_log_setLabel" id="ex168_item1_labels" x="650" y="20"><mutation items="2" /><field name="TIMESTAMP">MILLISECONDS</field><value name="ADD0"><shadow type="text" id="ex168_item1_moisture_label"><field name="TEXT">humidite_sol</field></shadow></value><value name="ADD1"><shadow type="text" id="ex168_item1_light_label"><field name="TEXT">luminosite</field></shadow></value></block><block type="communication_log_addData" id="ex168_item2_measure" x="650" y="220"><mutation items="2" /><value name="ADD0"><block type="communication_log_data" id="ex168_item2_moisture_data"><value name="LABEL"><shadow type="text" id="ex168_item2_moisture_label"><field name="TEXT">humidite_sol</field></shadow></value><value name="DATA"><block type="sensors_getGroveMoisture" id="ex168_item2_moisture"><field name="PIN">pin1</field></block></value></block></value><value name="ADD1"><block type="communication_log_data" id="ex168_item2_light_data"><value name="LABEL"><shadow type="text" id="ex168_item2_light_label"><field name="TEXT">luminosite</field></shadow></value><value name="DATA"><block type="sensors_getLight" id="ex168_item2_light" /></value></block></value></block><block type="io_pause" id="ex168_item3_pause" x="650" y="460"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex168_item3_pause_time"><field name="NUM">2</field></shadow></value></block><block type="communication_log_addData" id="ex168_item4_swapped" x="650" y="620"><mutation items="2" /><value name="ADD0"><block type="communication_log_data" id="ex168_item4_moisture_data"><value name="LABEL"><shadow type="text" id="ex168_item4_moisture_label"><field name="TEXT">humidite_sol</field></shadow></value><value name="DATA"><block type="sensors_getLight" id="ex168_item4_wrong_light" /></value></block></value><value name="ADD1"><block type="communication_log_data" id="ex168_item4_light_data"><value name="LABEL"><shadow type="text" id="ex168_item4_light_label"><field name="TEXT">luminosite</field></shadow></value><value name="DATA"><block type="sensors_getGroveMoisture" id="ex168_item4_wrong_moisture"><field name="PIN">pin1</field></block></value></block></value></block><block type="communication_log_addData" id="ex168_item5_fixed_light" x="650" y="880"><mutation items="2" /><value name="ADD0"><block type="communication_log_data" id="ex168_item5_moisture_data"><value name="LABEL"><shadow type="text" id="ex168_item5_moisture_label"><field name="TEXT">humidite_sol</field></shadow></value><value name="DATA"><block type="sensors_getGroveMoisture" id="ex168_item5_moisture"><field name="PIN">pin1</field></block></value></block></value><value name="ADD1"><block type="communication_log_data" id="ex168_item5_light_data"><value name="LABEL"><shadow type="text" id="ex168_item5_light_label"><field name="TEXT">luminosite</field></shadow></value><value name="DATA"><shadow type="math_number" id="ex168_item5_fixed_light_value"><field name="NUM">500</field></shadow></value></block></value></block></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Les groupes restent deconnectes dans l'espace de travail pour les captures.
from microbit import *
import log

log.set_labels('humidite_sol', 'luminosite', timestamp=log.MILLISECONDS)

log.add(humidite_sol=pin1.read_analog(), luminosite=display.read_light_level())

sleep(2000)

log.add(humidite_sol=display.read_light_level(), luminosite=pin1.read_analog())

log.add(humidite_sol=pin1.read_analog(), luminosite=500)
