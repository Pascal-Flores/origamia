"""
Auteur: Origamia
Interface: microbit
Nom du projet: 224 - Casque ventilé
Description: Choisir la commande qui met en marche le ventilateur du casque de démonstration.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex224_start_0" deletable="false" x="20" y="20" /><block type="actuators_setFanPower" id="ex224_fan_on_0" x="400" y="20"><field name="PIN">pin2</field><value name="POWER"><shadow type="math_number" id="ex224_fan_on_1"><field name="NUM">1023</field></shadow></value></block><block type="actuators_setFanPower" id="ex224_fan_off_0" x="400" y="150"><field name="PIN">pin2</field><value name="POWER"><shadow type="math_number" id="ex224_fan_off_1"><field name="NUM">0</field></shadow></value></block><block type="actuators_setVibrationMotorState" id="ex224_vibration_0" x="400" y="280"><field name="PIN">pin2</field><value name="STATE"><shadow type="io_digital_signal" id="ex224_vibration_1"><field name="BOOL">HIGH</field></shadow></value></block></xml>
"""
# Le programme est volontairement incomplet : un bloc candidat doit etre
# connecte sous "Au demarrage" dans l'espace de travail Vittascience.
from microbit import *

# Blocs candidats, laisses non connectes dans l'espace de travail.
pin2.write_analog(1023)
pin2.write_analog(0)
pin2.write_digital(1)
