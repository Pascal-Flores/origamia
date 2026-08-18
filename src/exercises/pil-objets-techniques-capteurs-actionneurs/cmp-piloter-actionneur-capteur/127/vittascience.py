"""
Auteur: Origamia
Interface: microbit
Nom du projet: 127 - Lumiere, son, action !
Description: Relier directement la luminosite au volume du haut-parleur.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex127_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex127_forever_0" x="350" y="20"><statement name="DO"><block type="actuators_music_setVolume" id="ex127_volume_0"><next><block type="microbit_audio_play" id="ex127_sound_0"><field name="SONG">GIGGLE</field><next><block type="io_pause" id="ex127_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex127_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></next></block></statement></block><block type="sensors_getLight" id="ex127_light_0" x="850" y="20" /></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Le programme est volontairement incomplet : la luminosite doit regler le volume.
from microbit import *
import utime


while True:
    set_volume()
    audio.play(Sound.GIGGLE)
    utime.sleep(1)

# Bloc fourni, laisse non connecte dans l'espace de travail.
display.read_light_level()
