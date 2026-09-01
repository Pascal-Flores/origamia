"""
Auteur: Origamia
Interface: microbit
Nom du projet: 170 - La répétition change de tempo
Description: Programme initial à adapter au nouveau protocole de mesure.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex170_start" deletable="false" x="20" y="20"><statement name="DO"><block type="communication_log_setLabel" id="ex170_labels"><mutation items="1" /><field name="TIMESTAMP">MILLISECONDS</field><value name="ADD0"><shadow type="text" id="ex170_label_sound"><field name="TEXT">niveau_sonore</field></shadow></value><next><block type="controls_repeat" id="ex170_repeat"><value name="TIMES"><shadow type="math_number" id="ex170_times"><field name="NUM">12</field></shadow></value><statement name="DO"><block type="communication_log_addData" id="ex170_log"><mutation items="1" /><value name="ADD0"><block type="communication_log_data" id="ex170_data_sound"><value name="LABEL"><shadow type="text" id="ex170_data_label_sound"><field name="TEXT">niveau_sonore</field></shadow></value><value name="DATA"><block type="io_micro_getSoundLevel" id="ex170_sound" /></value></block></value><next><block type="io_pause" id="ex170_pause"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex170_pause_time"><field name="NUM">1</field></shadow></value></block></next></block></statement></block></next></block></statement></block><block type="forever" id="ex170_forever" x="20" y="600" /></xml>
"""
from microbit import *
import log

log.set_labels('niveau_sonore', timestamp=log.MILLISECONDS)

for _ in range(12):
    log.add(niveau_sonore=microphone.sound_level())
    sleep(1000)

