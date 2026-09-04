"""
Auteur: Origamia
Interface: microbit
Nom du projet: 233 - Trois montages à reconstruire
Description: Planche de blocs pour associer trois capteurs à trois actionneurs.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex233_start" deletable="false" x="20" y="20" /><block type="sensors_dhtReadData" id="ex233_humidity" x="350" y="20"><mutation temp="false" /><field name="DATA">HUM</field><field name="PIN">pin1</field><field name="BOARD">v1</field></block><block type="actuators_continuousServo_setSpeed" id="ex233_servo_continu" x="850" y="20"><field name="DIR">1</field><field name="PIN">pin2</field></block><block type="sensors_getRotation" id="ex233_tilt" x="350" y="170"><field name="AXIS">pitch</field></block><block type="actuators_setServoAngle" id="ex233_servo_angle" x="850" y="170"><field name="PIN">pin8</field></block><block type="sensors_getRainGauge" id="ex233_rain" x="350" y="320"><field name="PIN">pin1</field></block><block type="actuators_setGroveRelayState" id="ex233_relay" x="850" y="320"><field name="PIN">pin0</field></block></xml>
"""
# Cette planche sert uniquement à produire les captures des blocs proposés.
from microbit import *
import math
from dht11 import DHT11

dht11_1 = DHT11(pin1)

def setServoSpeed(pin, direction, speed=0):
    pin.set_analog_period(20)
    speed_ms = speed * direction * 0.5 / 100 + 1.5
    pin.write_analog(1023 * speed_ms / 20)

def setServoAngle(pin, angle=0):
    pin.write_analog(int(0.025 * 1023 + (angle * 0.1 * 1023) / 180))

# Six blocs isolés dans l'espace de travail.
dht11_1.getData(d=2)
setServoSpeed(pin2, 1)
math.atan2(accelerometer.get_y(), -accelerometer.get_z()) * 180.0 / math.pi
setServoAngle(pin8)
pin1.read_digital()
pin0.write_digital(0)
