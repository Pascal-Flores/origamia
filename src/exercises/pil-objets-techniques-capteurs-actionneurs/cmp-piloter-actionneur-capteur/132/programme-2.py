"""
Auteur: Origamia
Interface: microbit
Nom du projet: 132 - Programme 2
Description: Comparer une liaison entre un capteur d'humidite et un servomoteur continu.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex132_p2_start" deletable="false" x="20" y="20" /><block type="forever" id="ex132_p2_forever" x="350" y="20"><statement name="DO"><block type="actuators_continuousServo_setSpeed" id="ex132_p2_servo"><field name="DIR">1</field><field name="PIN">pin2</field><value name="SPEED"><shadow type="math_number" id="ex132_p2_speed"><field name="NUM">50</field></shadow></value><next><block type="communication_serialWrite" id="ex132_p2_console"><mutation newlines="false" /><value name="TEXT"><shadow type="math_number" id="ex132_p2_console_value"><field name="NUM">50</field></shadow></value><next><block type="io_pause" id="ex132_p2_pause"><field name="UNIT">SEC</field><value name="TIME"><block type="sensors_dhtReadData" id="ex132_p2_humidity"><mutation temp="false" /><field name="DATA">HUM</field><field name="PIN">pin1</field><field name="BOARD">v1</field></block></value></block></next></block></next></block></statement></block></xml>
"""
# Ce code est genere a partir des blocs du projet Vittascience.
from microbit import *
import utime
from dht11 import DHT11


dht11_1 = DHT11(pin1)


def setServoSpeed(pin, direction, speed):
    pin.set_analog_period(20)
    if speed >= 0 and speed <= 100:
        if direction is 1 or direction is -1:
            speed_ms = speed * direction * 0.5 / 100 + 1.5
            pin.write_analog(1023 * speed_ms / 20)
        else:
            raise ValueError("continuous servomotor has no direction: '" + str(direction) + "'")
    else:
        raise ValueError("continuous servomotor speed is out of range: '" + str(speed) + "'")


while True:
    setServoSpeed(pin2, 1, 50)
    print(str(50))
    utime.sleep(dht11_1.getData(d=2))
