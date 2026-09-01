"""
Auteur: Origamia
Interface: microbit
Nom du projet: 134 - Le musée prend vie
Description: Planche de blocs pour associer trois capteurs à trois actionneurs.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex134_start" deletable="false" x="20" y="20" /><block type="sensors_dhtReadData" id="ex134_humidity" x="350" y="20"><mutation temp="false" /><field name="DATA">HUM</field><field name="PIN">pin1</field><field name="BOARD">v1</field></block><block type="actuators_kitronik_controlMotor" id="ex134_motor" x="850" y="20"><field name="MOTOR">1</field><field name="DIR">1</field></block><block type="sensors_getSgp30Gas" id="ex134_co2" x="350" y="170"><field name="GAS">CO2</field></block><block type="actuators_music_playFrequency" id="ex134_buzzer" x="850" y="170"><field name="PIN">pin_speaker</field><value name="DURATION"><shadow type="math_number" id="ex134_duration"><field name="NUM">500</field></shadow></value></block><block type="sensors_getRotation" id="ex134_tilt" x="350" y="320"><field name="AXIS">pitch</field></block><block type="actuators_setServoAngle" id="ex134_servo" x="850" y="320"><field name="PIN">pin8</field></block></xml>
"""
# Cette planche sert uniquement a produire les captures des blocs proposes.
from microbit import *
import music
import math
from dht11 import DHT11
from sgp30 import SGP30


dht11_1 = DHT11(pin1)
sgp30 = SGP30()


# Six blocs isoles dans l'espace de travail.
dht11_1.getData(d=2)
kitronik_controlMotor(1, 1)
sgp30.eCO2()
music.pitch(duration=500)
math.atan2(accelerometer.get_y(), -accelerometer.get_z()) * 180.0 / math.pi
setServoAngle(pin8)
