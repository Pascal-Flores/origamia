"""
Auteur: Origamia
Interface: microbit
Nom du projet: 163 - Le thermomètre prend note
Description: Planche de capture du programme incomplet et de ses trois blocs candidats.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex163_start" deletable="false" x="20" y="20"><statement name="DO"><block type="communication_log_setLabel" id="ex163_labels"><mutation items="1" /><field name="TIMESTAMP">MILLISECONDS</field><value name="ADD0"><shadow type="text" id="ex163_label_text"><field name="TEXT">temperature</field></shadow></value></block></statement></block><block type="forever" id="ex163_forever" x="20" y="300" /><block type="communication_log_addData" id="ex163_answer_correct" x="700" y="20"><mutation items="1" /><value name="ADD0"><block type="communication_log_data" id="ex163_correct_data"><value name="LABEL"><shadow type="text" id="ex163_correct_label"><field name="TEXT">temperature</field></shadow></value><value name="DATA"><block type="sensors_getTemperature" id="ex163_correct_temperature"><field name="UNIT">CELSIUS</field></block></value></block></value></block><block type="communication_serialWrite" id="ex163_answer_console" x="700" y="220"><mutation newlines="false" /><value name="TEXT"><block type="sensors_getTemperature" id="ex163_console_temperature"><field name="UNIT">CELSIUS</field></block></value></block><block type="communication_log_addData" id="ex163_answer_fixed" x="700" y="420"><mutation items="1" /><value name="ADD0"><block type="communication_log_data" id="ex163_fixed_data"><value name="LABEL"><shadow type="text" id="ex163_fixed_label"><field name="TEXT">temperature</field></shadow></value><value name="DATA"><shadow type="math_number" id="ex163_fixed_value"><field name="NUM">20</field></shadow></value></block></value></block></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Le programme est volontairement incomplet ; les blocs candidats restent
# deconnectes dans l'espace de travail afin de produire les captures.
from microbit import *
import log

log.set_labels('temperature', timestamp=log.MILLISECONDS)

# Blocs candidats, laisses non connectes dans l'espace de travail.
log.add(temperature=temperature())
print(temperature())
log.add(temperature=20)
