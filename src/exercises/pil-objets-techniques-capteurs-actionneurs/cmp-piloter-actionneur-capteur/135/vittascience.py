"""
Auteur: Origamia
Interface: microbit
Nom du projet: 135 - Les mesures font le show
Description: Planche de blocs pour associer trois capteurs à trois actionneurs.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex135_start" deletable="false" x="20" y="20" /><block type="sensors_getAirQualityValue" id="ex135_air" x="350" y="20"><field name="PIN">pin1</field></block><block type="actuators_setFanPower" id="ex135_fan" x="850" y="20"><field name="PIN">pin2</field></block><block type="sensors_weatherbit_anemometer_getSpeed" id="ex135_wind" x="350" y="170"><field name="UNIT">M_S</field></block><block type="actuators_continuousServo_setSpeed" id="ex135_servo" x="850" y="170"><field name="DIR">1</field><field name="PIN">pin0</field></block><block type="sensors_getRainGauge" id="ex135_rain" x="350" y="320"><field name="PIN">pin1</field></block><block type="actuators_setGroveRelayState" id="ex135_relay" x="850" y="320"><field name="PIN">pin8</field></block></xml>
"""
# Cette planche sert uniquement a produire les captures des blocs proposes.
from microbit import *


def setServoSpeed(pin, direction, speed):
    pin.set_analog_period(20)
    speed_ms = speed * direction * 0.5 / 100 + 1.5
    pin.write_analog(1023 * speed_ms / 20)


# Six blocs isoles dans l'espace de travail.
pin1.read_analog()
pin2.write_analog()
anemometer_getWindSpeed(pin1, unit='m/s')
setServoSpeed(pin0, 1)
pin1.read_digital()
pin8.write_digital()
