"""
Auteur: Origamia
Interface: microbit
Nom du projet: 118 - Quiz sur la bonne note
Description: Choisir la commande qui fait jouer le signal de depart du quiz.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex118_start_0" deletable="false" x="20" y="20" /><block type="microbit_audio_play" id="ex118_play_0" x="400" y="20"><field name="SONG">GIGGLE</field></block><block type="microbit_audio_stop" id="ex118_stop_0" x="400" y="140" /><block type="actuators_music_setVolume" id="ex118_volume_0" x="400" y="260"><value name="VOL"><shadow type="math_number" id="ex118_volume_1"><field name="NUM">255</field></shadow></value></block></xml>
"""
# Le programme est volontairement incomplet : un bloc candidat doit etre
# connecte sous "Au demarrage" dans l'espace de travail Vittascience.
from microbit import *

# Blocs candidats, laisses non connectes dans l'espace de travail.
audio.play(Sound.GIGGLE)
audio.stop()
set_volume(255)
