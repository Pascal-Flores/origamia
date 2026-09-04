"""
Auteur: Origamia
Interface: microbit
Nom du projet: 227 - Store du matin
Description: Corriger le sens et la vitesse du servomoteur continu du store miniature.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex227_start_0" deletable="false" x="20" y="20"><statement name="DO"><block type="actuators_continuousServo_setSpeed" id="ex227_servo_0"><field name="DIR">-1</field><field name="PIN">pin2</field><value name="SPEED"><shadow type="math_number" id="ex227_speed_0"><field name="NUM">100</field></shadow></value></block></statement></block></xml>
"""
from microbit import *


def setServoSpeed(pin, direction, speed):
    pin.set_analog_period(20)
    if 0 <= speed <= 100:
        if direction is 1 or direction is -1:
            speed_ms = speed * direction * 0.5 / 100 + 1.5
            pin.write_analog(1023 * speed_ms / 20)
        else:
            raise ValueError("continuous servomotor has no direction: '" + str(direction) + "'")
    else:
        raise ValueError("continuous servomotor speed is out of range: '" + str(speed) + "'")


# Reglages provisoires a corriger par l'eleve dans l'interface.
setServoSpeed(pin2, -1, 100)
