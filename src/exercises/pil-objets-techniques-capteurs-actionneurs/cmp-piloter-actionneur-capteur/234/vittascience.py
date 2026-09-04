"""
Auteur: Origamia
Interface: microbit
Nom du projet: 234 - Trois réactions automatiques
Description: Planche de blocs pour associer trois capteurs à trois actionneurs.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex234_start" deletable="false" x="20" y="20" /><block type="sensors_getAirQualityValue" id="ex234_air" x="350" y="20"><field name="PIN">pin1</field></block><block type="actuators_setFanPower" id="ex234_fan" x="850" y="20"><field name="PIN">pin2</field></block><block type="sensors_getSgp30Gas" id="ex234_co2" x="350" y="170"><field name="GAS">CO2</field></block><block type="actuators_music_playFrequency" id="ex234_buzzer" x="850" y="170"><field name="PIN">pin_speaker</field><value name="DURATION"><shadow type="math_number" id="ex234_duration"><field name="NUM">500</field></shadow></value></block><block type="io_micro_wasSoundDetected" id="ex234_sound" x="350" y="320"><field name="STATE">LOUD</field></block><block type="actuators_setVibrationMotorState" id="ex234_vibration" x="850" y="320"><field name="PIN">pin8</field></block></xml>
"""
# Cette planche sert uniquement à produire les captures des blocs proposés.
from microbit import *
import music
from sgp30 import SGP30

sgp30 = SGP30()

# Six blocs isolés dans l'espace de travail.
pin1.read_analog()
pin2.write_analog(0)
sgp30.eCO2()
music.pitch(440, duration=500)
microphone.was_sound(SoundEvent.LOUD)
pin8.write_digital(0)
