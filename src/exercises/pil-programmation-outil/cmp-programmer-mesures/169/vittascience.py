"""
Auteur: Origamia
Interface: microbit
Nom du projet: 169 - L'expo change de rythme
Description: Programme initial à adapter au nouveau protocole de mesure.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex169_start" deletable="false" x="20" y="20"><statement name="DO"><block type="communication_log_setLabel" id="ex169_labels"><mutation items="2" /><field name="TIMESTAMP">MILLISECONDS</field><value name="ADD0"><shadow type="text" id="ex169_label_temp"><field name="TEXT">temperature</field></shadow></value><value name="ADD1"><shadow type="text" id="ex169_label_light"><field name="TEXT">luminosite</field></shadow></value><next><block type="controls_repeat" id="ex169_repeat"><value name="TIMES"><shadow type="math_number" id="ex169_times"><field name="NUM">8</field></shadow></value><statement name="DO"><block type="communication_log_addData" id="ex169_log"><mutation items="2" /><value name="ADD0"><block type="communication_log_data" id="ex169_data_temp"><value name="LABEL"><shadow type="text" id="ex169_data_label_temp"><field name="TEXT">temperature</field></shadow></value><value name="DATA"><block type="sensors_getTemperature" id="ex169_temp"><field name="UNIT">CELSIUS</field></block></value></block></value><value name="ADD1"><block type="communication_log_data" id="ex169_data_light"><value name="LABEL"><shadow type="text" id="ex169_data_label_light"><field name="TEXT">luminosite</field></shadow></value><value name="DATA"><block type="sensors_getLight" id="ex169_light" /></value></block></value><next><block type="io_pause" id="ex169_pause"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex169_pause_time"><field name="NUM">5</field></shadow></value></block></next></block></statement></block></next></block></statement></block><block type="forever" id="ex169_forever" x="20" y="650" /></xml>
"""
from microbit import *
import log

log.set_labels('temperature', 'luminosite', timestamp=log.MILLISECONDS)

for _ in range(8):
    log.add(
        temperature=temperature(),
        luminosite=display.read_light_level(),
    )
    sleep(5000)
