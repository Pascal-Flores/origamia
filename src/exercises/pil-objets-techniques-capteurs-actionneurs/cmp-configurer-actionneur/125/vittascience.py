"""
Auteur: Origamia
Interface: microbit
Nom du projet: 125 - Bip vers le futur
Description: Corriger la frequence et la duree du signal sonore de la maquette.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex125_start_0" deletable="false" x="20" y="20"><statement name="DO"><block type="actuators_music_playFrequency" id="ex125_sound_0"><field name="PIN">pin_speaker</field><value name="FREQUENCY"><shadow type="math_number" id="ex125_frequency_0"><field name="NUM">440</field></shadow></value><value name="DURATION"><shadow type="math_number" id="ex125_duration_0"><field name="NUM">500</field></shadow></value></block></statement></block></xml>
"""
from microbit import *
import music


# Reglages provisoires a corriger par l'eleve dans l'interface.
music.pitch(440, duration=500)
