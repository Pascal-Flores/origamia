"""
Auteur: Origamia
Interface: microbit
Nom du projet: 218 - Bouton d'urgence surveillé
Description: Choisir l'état réellement lu sur le bouton A.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex218_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex218_forever_0" x="350" y="20"><statement name="DO"><block type="communication_serialWrite" id="ex218_display_0"><mutation newlines="false" /><next><block type="io_pause" id="ex218_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex218_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></statement></block><block type="io_isButtonPressed" id="ex218_candidate1_0" x="850" y="20"><field name="BUTTON">a</field><field name="STATE">is_</field></block><block type="math_number" id="ex218_candidate2_0" x="850" y="130"><field name="NUM">1</field></block><block type="text" id="ex218_candidate3_0" x="850" y="240"><field name="TEXT">Urgence</field></block></xml>
"""
# Le programme est genere a partir des blocs du projet Vittascience.
# Le programme est volontairement incomplet : un bloc doit etre place dans print().
from microbit import *
import utime

while True:
    print()
    utime.sleep(1)

# Blocs candidats, laisses non connectes dans l'espace de travail.
button_a.is_pressed()
1
'Urgence'
