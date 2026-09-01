"""
Auteur: Origamia
Interface: microbit
Nom du projet: 164 - Le bruit laisse une trace
Description: Planche de capture du programme incomplet et de ses trois blocs candidats.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex164_start" deletable="false" x="20" y="20"><statement name="DO"><block type="communication_log_setLabel" id="ex164_labels"><mutation items="1" /><field name="TIMESTAMP">MILLISECONDS</field><value name="ADD0"><shadow type="text" id="ex164_label_text"><field name="TEXT">niveau_sonore</field></shadow></value></block></statement></block><block type="forever" id="ex164_forever" x="20" y="300" /><block type="communication_log_addData" id="ex164_answer_correct" x="700" y="20"><mutation items="1" /><value name="ADD0"><block type="communication_log_data" id="ex164_correct_data"><value name="LABEL"><shadow type="text" id="ex164_correct_label"><field name="TEXT">niveau_sonore</field></shadow></value><value name="DATA"><block type="io_micro_getSoundLevel" id="ex164_correct_sound" /></value></block></value></block><block type="communication_serialWrite" id="ex164_answer_console" x="700" y="220"><mutation newlines="false" /><value name="TEXT"><block type="io_micro_getSoundLevel" id="ex164_console_sound" /></value></block><block type="communication_log_addData" id="ex164_answer_fixed" x="700" y="420"><mutation items="1" /><value name="ADD0"><block type="communication_log_data" id="ex164_fixed_data"><value name="LABEL"><shadow type="text" id="ex164_fixed_label"><field name="TEXT">niveau_sonore</field></shadow></value><value name="DATA"><shadow type="math_number" id="ex164_fixed_value"><field name="NUM">50</field></shadow></value></block></value></block></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Le programme est volontairement incomplet ; les blocs candidats restent
# deconnectes dans l'espace de travail afin de produire les captures.
from microbit import *
import log

log.set_labels('niveau_sonore', timestamp=log.MILLISECONDS)

# Blocs candidats, laisses non connectes dans l'espace de travail.
log.add(niveau_sonore=microphone.sound_level())
print(microphone.sound_level())
log.add(niveau_sonore=50)
