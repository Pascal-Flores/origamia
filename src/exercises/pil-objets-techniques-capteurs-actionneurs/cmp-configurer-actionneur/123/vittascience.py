"""
Auteur: Origamia
Interface: microbit
Nom du projet: 123 - Des bulles, pas la tempete !
Description: Corriger la puissance du ventilateur de la machine a bulles.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex123_start_0" deletable="false" x="20" y="20"><statement name="DO"><block type="actuators_setFanPower" id="ex123_fan_0"><field name="PIN">pin2</field><value name="POWER"><shadow type="math_number" id="ex123_power_0"><field name="NUM">1023</field></shadow></value></block></statement></block></xml>
"""
from microbit import *


# Valeur provisoire a remplacer par l'eleve dans l'interface.
pin2.write_analog(1023)
