"""
Auteur: Origamia
Interface: microbit
Nom du projet: 165 - La lumière passe au journal
Description: Planche de capture du programme incomplet et de ses trois blocs candidats.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex165_start" deletable="false" x="20" y="20"><statement name="DO"><block type="communication_log_setLabel" id="ex165_labels"><mutation items="1" /><field name="TIMESTAMP">MILLISECONDS</field><value name="ADD0"><shadow type="text" id="ex165_label_text"><field name="TEXT">luminosite</field></shadow></value></block></statement></block><block type="forever" id="ex165_forever" x="20" y="300" /><block type="communication_log_addData" id="ex165_answer_correct" x="700" y="20"><mutation items="1" /><value name="ADD0"><block type="communication_log_data" id="ex165_correct_data"><value name="LABEL"><shadow type="text" id="ex165_correct_label"><field name="TEXT">luminosite</field></shadow></value><value name="DATA"><block type="sensors_getLight" id="ex165_correct_light" /></value></block></value></block><block type="communication_serialWrite" id="ex165_answer_console" x="700" y="220"><mutation newlines="false" /><value name="TEXT"><block type="sensors_getLight" id="ex165_console_light" /></value></block><block type="communication_log_addData" id="ex165_answer_fixed" x="700" y="420"><mutation items="1" /><value name="ADD0"><block type="communication_log_data" id="ex165_fixed_data"><value name="LABEL"><shadow type="text" id="ex165_fixed_label"><field name="TEXT">luminosite</field></shadow></value><value name="DATA"><shadow type="math_number" id="ex165_fixed_value"><field name="NUM">500</field></shadow></value></block></value></block></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Le programme est volontairement incomplet ; les blocs candidats restent
# deconnectes dans l'espace de travail afin de produire les captures.
from microbit import *
import log

log.set_labels('luminosite', timestamp=log.MILLISECONDS)

# Blocs candidats, laisses non connectes dans l'espace de travail.
log.add(luminosite=display.read_light_level())
print(display.read_light_level())
log.add(luminosite=500)
