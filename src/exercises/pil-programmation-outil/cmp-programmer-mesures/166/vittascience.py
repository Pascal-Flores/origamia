"""
Auteur: Origamia
Interface: microbit
Nom du projet: 166 - Fenêtre ouverte, journal ouvert
Description: Planche de capture des cinq groupes de blocs a classer.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex166_start" deletable="false" x="20" y="20" /><block type="forever" id="ex166_forever" x="20" y="300" /><block type="communication_log_setLabel" id="ex166_item1_labels" x="650" y="20"><mutation items="2" /><field name="TIMESTAMP">MILLISECONDS</field><value name="ADD0"><shadow type="text" id="ex166_item1_temperature_label"><field name="TEXT">temperature</field></shadow></value><value name="ADD1"><shadow type="text" id="ex166_item1_sound_label"><field name="TEXT">niveau_sonore</field></shadow></value></block><block type="communication_log_addData" id="ex166_item2_measure" x="650" y="220"><mutation items="2" /><value name="ADD0"><block type="communication_log_data" id="ex166_item2_temperature_data"><value name="LABEL"><shadow type="text" id="ex166_item2_temperature_label"><field name="TEXT">temperature</field></shadow></value><value name="DATA"><block type="sensors_getTemperature" id="ex166_item2_temperature"><field name="UNIT">CELSIUS</field></block></value></block></value><value name="ADD1"><block type="communication_log_data" id="ex166_item2_sound_data"><value name="LABEL"><shadow type="text" id="ex166_item2_sound_label"><field name="TEXT">niveau_sonore</field></shadow></value><value name="DATA"><block type="io_micro_getSoundLevel" id="ex166_item2_sound" /></value></block></value></block><block type="io_pause" id="ex166_item3_pause" x="650" y="460"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex166_item3_pause_time"><field name="NUM">1</field></shadow></value></block><block type="communication_serialWrite" id="ex166_item4_console_temperature" x="650" y="620"><mutation newlines="false" /><value name="TEXT"><block type="sensors_getTemperature" id="ex166_item4_temperature"><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="ex166_item4_console_sound"><mutation newlines="false" /><value name="TEXT"><block type="io_micro_getSoundLevel" id="ex166_item4_sound" /></value></block></next></block><block type="communication_log_addData" id="ex166_item5_fixed" x="650" y="900"><mutation items="2" /><value name="ADD0"><block type="communication_log_data" id="ex166_item5_temperature_data"><value name="LABEL"><shadow type="text" id="ex166_item5_temperature_label"><field name="TEXT">temperature</field></shadow></value><value name="DATA"><shadow type="math_number" id="ex166_item5_temperature"><field name="NUM">20</field></shadow></value></block></value><value name="ADD1"><block type="communication_log_data" id="ex166_item5_sound_data"><value name="LABEL"><shadow type="text" id="ex166_item5_sound_label"><field name="TEXT">niveau_sonore</field></shadow></value><value name="DATA"><shadow type="math_number" id="ex166_item5_sound"><field name="NUM">50</field></shadow></value></block></value></block></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Les groupes restent deconnectes dans l'espace de travail pour les captures.
from microbit import *
import log

log.set_labels('temperature', 'niveau_sonore', timestamp=log.MILLISECONDS)

log.add(temperature=temperature(), niveau_sonore=microphone.sound_level())

sleep(1000)

print(temperature())
print(microphone.sound_level())

log.add(temperature=20, niveau_sonore=50)
