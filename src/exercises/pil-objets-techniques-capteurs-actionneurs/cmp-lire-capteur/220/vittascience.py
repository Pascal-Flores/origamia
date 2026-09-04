"""
Auteur: Origamia
Interface: microbit
Nom du projet: 220 - Arrêt demandé
Description: Choisir entre l'état du bouton A et le niveau sonore.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex220_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex220_forever_0" x="350" y="20"><statement name="DO"><block type="communication_serialWrite" id="ex220_display_0"><mutation newlines="false" /><next><block type="io_pause" id="ex220_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex220_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></statement></block><block type="io_isButtonPressed" id="ex220_candidate1_0" x="850" y="20"><field name="BUTTON">a</field><field name="STATE">is_</field></block><block type="io_micro_getSoundLevel" id="ex220_candidate2_0" x="850" y="130" /></xml>
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
microphone.sound_level()
