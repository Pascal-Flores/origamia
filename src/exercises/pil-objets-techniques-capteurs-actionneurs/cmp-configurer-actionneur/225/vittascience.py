"""
Auteur: Origamia
Interface: microbit
Nom du projet: 225 - Passage piéton ouvert
Description: Régler l'angle du servomoteur pour lever le bras de la maquette.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex225_start_0" deletable="false" x="20" y="20"><statement name="DO"><block type="actuators_setServoAngle" id="ex225_servo_0"><field name="PIN">pin2</field><value name="ANGLE"><shadow type="math_number" id="ex225_angle_0"><field name="NUM">0</field></shadow></value></block></statement></block></xml>
"""
from microbit import *


def setServoAngle(pin, angle):
    if 0 <= angle <= 180:
        pin.write_analog(int(0.025 * 1023 + (angle * 0.1 * 1023) / 180))
    else:
        raise ValueError("Servomotor angle has to be between 0 and 180")


# Valeur provisoire a remplacer par l'eleve dans l'interface.
setServoAngle(pin2, 0)
