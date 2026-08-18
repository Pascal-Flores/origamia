"""
Auteur: Origamia
Interface: microbit
Nom du projet: 122 - Decollage sans vacarme !
Description: Corriger le volume du haut-parleur de la maquette de fusee.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex122_start_0" deletable="false" x="20" y="20"><statement name="DO"><block type="actuators_music_setVolume" id="ex122_volume_0"><value name="VOL"><shadow type="math_number" id="ex122_volume_1"><field name="NUM">255</field></shadow></value><next><block type="microbit_audio_play" id="ex122_sound_0"><field name="SONG">SOARING</field></block></next></block></statement></block></xml>
"""
from microbit import *


# Valeur provisoire a remplacer par l'eleve dans l'interface.
set_volume(255)
audio.play(Sound.SOARING)
