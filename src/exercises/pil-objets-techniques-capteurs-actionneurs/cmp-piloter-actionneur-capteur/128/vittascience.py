"""
Auteur: Origamia
Interface: microbit
Nom du projet: 128 - L'aiguille prend la temperature
Description: Relier directement la temperature a l'angle du servomoteur du cadran.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex128_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex128_forever_0" x="350" y="20"><statement name="DO"><block type="actuators_setServoAngle" id="ex128_servo_0"><field name="PIN">pin2</field><next><block type="io_pause" id="ex128_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex128_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></statement></block><block type="sensors_getTemperature" id="ex128_temperature_0" x="850" y="20"><field name="UNIT">CELSIUS</field></block></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
# Le programme est volontairement incomplet : la temperature doit regler l'angle.
from microbit import *
import utime


def setServoAngle(pin, angle):
    if 0 <= angle <= 180:
        pin.write_analog(int(0.025 * 1023 + (angle * 0.1 * 1023) / 180))
    else:
        raise ValueError("Servomotor angle has to be between 0 and 180")


while True:
    setServoAngle(pin2)
    utime.sleep(1)

# Bloc fourni, laisse non connecte dans l'espace de travail.
temperature()
