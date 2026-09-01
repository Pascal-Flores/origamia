"""
Auteur: Origamia
Interface: microbit
Nom du projet: 171 - La bibliothèque change d'air
Description: Programme initial à adapter au nouveau protocole de mesure.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex171_start" deletable="false" x="20" y="20"><statement name="DO"><block type="communication_log_setLabel" id="ex171_labels"><mutation items="3" /><field name="TIMESTAMP">MILLISECONDS</field><value name="ADD0"><shadow type="text" id="ex171_label_temp"><field name="TEXT">temperature</field></shadow></value><value name="ADD1"><shadow type="text" id="ex171_label_light"><field name="TEXT">luminosite</field></shadow></value><value name="ADD2"><shadow type="text" id="ex171_label_sound"><field name="TEXT">niveau_sonore</field></shadow></value><next><block type="controls_repeat" id="ex171_repeat"><value name="TIMES"><shadow type="math_number" id="ex171_times"><field name="NUM">8</field></shadow></value><statement name="DO"><block type="communication_log_addData" id="ex171_log"><mutation items="3" /><value name="ADD0"><block type="communication_log_data" id="ex171_data_temp"><value name="LABEL"><shadow type="text" id="ex171_data_label_temp"><field name="TEXT">temperature</field></shadow></value><value name="DATA"><block type="sensors_getTemperature" id="ex171_temp"><field name="UNIT">CELSIUS</field></block></value></block></value><value name="ADD1"><block type="communication_log_data" id="ex171_data_light"><value name="LABEL"><shadow type="text" id="ex171_data_label_light"><field name="TEXT">luminosite</field></shadow></value><value name="DATA"><block type="sensors_getLight" id="ex171_light" /></value></block></value><value name="ADD2"><block type="communication_log_data" id="ex171_data_sound"><value name="LABEL"><shadow type="text" id="ex171_data_label_sound"><field name="TEXT">niveau_sonore</field></shadow></value><value name="DATA"><block type="io_micro_getSoundLevel" id="ex171_sound" /></value></block></value><next><block type="io_pause" id="ex171_pause"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex171_pause_time"><field name="NUM">5</field></shadow></value></block></next></block></statement></block></next></block></statement></block><block type="forever" id="ex171_forever" x="20" y="700" /></xml>
"""
from microbit import *
import log

log.set_labels('temperature', 'luminosite', 'niveau_sonore', timestamp=log.MILLISECONDS)

for _ in range(8):
    log.add(
        temperature=temperature(),
        luminosite=display.read_light_level(),
        niveau_sonore=microphone.sound_level(),
    )
    sleep(5000)
