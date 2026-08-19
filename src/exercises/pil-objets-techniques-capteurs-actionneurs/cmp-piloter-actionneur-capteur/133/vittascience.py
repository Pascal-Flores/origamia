"""
Auteur: Origamia
Interface: microbit
Nom du projet: 133 - Qui commande quoi ?
Description: Associer trois capteurs aux trois actionneurs qu'ils doivent commander directement.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex133_start" deletable="false" x="20" y="20" /><block type="forever" id="ex133_forever" x="350" y="20"><statement name="DO"><block type="actuators_setServoAngle" id="ex133_servo_angle"><field name="PIN">pin0</field><next><block type="actuators_setFanPower" id="ex133_fan"><field name="PIN">pin2</field><next><block type="actuators_continuousServo_setSpeed" id="ex133_servo_speed"><field name="DIR">1</field><field name="PIN">pin8</field><next><block type="io_pause" id="ex133_pause"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex133_pause_value"><field name="NUM">1</field></shadow></value></block></next></block></next></block></next></block></statement></block><block type="sensors_getTemperature" id="ex133_temperature" x="1020" y="20"><field name="UNIT">CELSIUS</field></block><block type="io_micro_getSoundLevel" id="ex133_sound" x="1020" y="140" /><block type="sensors_dhtReadData" id="ex133_humidity" x="1020" y="260"><mutation temp="false" /><field name="DATA">HUM</field><field name="PIN">pin1</field><field name="BOARD">v1</field><field name="UNIT">CELSIUS</field></block></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Les trois capteurs doivent etre relies aux trois actionneurs.
from microbit import *
import utime
from dht11 import DHT11


dht11_1 = DHT11(pin1)


def setServoAngle(pin, angle):
    if 0 <= angle <= 180:
        pin.write_analog(int(0.025 * 1023 + (angle * 0.1 * 1023) / 180))
    else:
        raise ValueError("Servomotor angle has to be between 0 and 180")


def setServoSpeed(pin, direction, speed):
    pin.set_analog_period(20)
    if 0 <= speed <= 100:
        duty = 1.3 * speed + 26
        if direction == 1:
            pin.write_analog(duty)
        elif direction == -1:
            pin.write_analog(154 - (duty - 26))
        else:
            raise ValueError("continuous servomotor has no direction: '" + str(direction) + "'")
    else:
        raise ValueError("continuous servomotor speed is out of range: '" + str(speed) + "'")


while True:
    setServoAngle(pin0)
    pin2.write_analog()
    setServoSpeed(pin8, 1)
    utime.sleep(1)

# Blocs fournis, laisses non connectes dans l'espace de travail.
temperature()
microphone.sound_level()
dht11_1.getData(d=2)
