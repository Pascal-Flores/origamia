"""
Auteur: Origamia
Interface: microbit
Nom du projet: 223 - Antivol bien verrouillé
Description: Choisir la commande qui met en marche le moteur vibrant du boîtier d'antivol.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex223_start_0" deletable="false" x="20" y="20" /><block type="actuators_setVibrationMotorState" id="ex223_vibration_on_0" x="400" y="20"><field name="PIN">pin2</field><value name="STATE"><shadow type="io_digital_signal" id="ex223_vibration_on_1"><field name="BOOL">HIGH</field></shadow></value></block><block type="actuators_setVibrationMotorState" id="ex223_vibration_off_0" x="400" y="150"><field name="PIN">pin2</field><value name="STATE"><shadow type="io_digital_signal" id="ex223_vibration_off_1"><field name="BOOL">LOW</field></shadow></value></block><block type="actuators_setFanPower" id="ex223_fan_0" x="400" y="280"><field name="PIN">pin2</field><value name="POWER"><shadow type="math_number" id="ex223_fan_1"><field name="NUM">1023</field></shadow></value></block></xml>
"""
# Le programme est volontairement incomplet : un bloc candidat doit etre
# connecte sous "Au demarrage" dans l'espace de travail Vittascience.
from microbit import *

# Blocs candidats, laisses non connectes dans l'espace de travail.
pin2.write_digital(1)
pin2.write_digital(0)
pin2.write_analog(1023)
