"""
Auteur: Origamia
Interface: microbit
Nom du projet: 133 - Qui commande quoi ?
Description: Planche de blocs pour associer trois capteurs à trois actionneurs.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex133_start" deletable="false" x="20" y="20" /><block type="sensors_getTemperature" id="ex133_temperature" x="350" y="20"><field name="UNIT">CELSIUS</field></block><block type="actuators_setServoAngle" id="ex133_servo_angle" x="800" y="20"><field name="PIN">pin0</field></block><block type="sensors_getGroveWaterAmount" id="ex133_water" x="350" y="160"><field name="PIN">pin1</field></block><block type="actuators_setFanPower" id="ex133_fan" x="800" y="160"><field name="PIN">pin2</field></block><block type="io_micro_wasSoundDetected" id="ex133_sound" x="350" y="300"><field name="STATE">LOUD</field></block><block type="actuators_setVibrationMotorState" id="ex133_vibration" x="800" y="300"><field name="PIN">pin8</field></block></xml>
"""
# Cette planche sert uniquement a produire les captures des blocs proposes.
from microbit import *


def setServoAngle(pin, angle):
    if 0 <= angle <= 180:
        pin.write_analog(int(0.025 * 1023 + (angle * 0.1 * 1023) / 180))
    else:
        raise ValueError("Servomotor angle has to be between 0 and 180")


# Six blocs isoles dans l'espace de travail.
temperature()
setServoAngle(pin0)
pin1.read_analog()
pin2.write_analog()
microphone.was_event(SoundEvent.LOUD)
pin8.write_digital()
