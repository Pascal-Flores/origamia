"""
Auteur: Origamia
Interface: microbit
Nom du projet: 117 - Vent dans les voiles
Description: Observer la vitesse du vent, sa direction et le cap mesure par la boussole.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex117_start_0" deletable="false" x="20" y="20" /><block type="forever" id="ex117_forever_0" x="350" y="20"><statement name="DO"><block type="communication_serialWrite" id="ex117_reading1_0"><mutation newlines="false" /><value name="TEXT"><block type="sensors_weatherbit_anemometer_getSpeed" id="ex117_sensor1_0"><field name="UNIT">M_S</field></block></value><next><block type="communication_serialWrite" id="ex117_reading2_0"><mutation newlines="false" /><value name="TEXT"><block type="sensors_weatherbit_weathercock_getDirection" id="ex117_sensor2_0" /></value><next><block type="communication_serialWrite" id="ex117_reading3_0"><mutation newlines="false" /><value name="TEXT"><block type="sensors_getCompass" id="ex117_sensor3_0" /></value><next><block type="io_pause" id="ex117_pause_0"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="ex117_pause_1"><field name="NUM">1</field></shadow></value></block></next></block></next></block></next></block></statement></block></xml>
"""
# Le programme est genere a partir des blocs du projet Vittascience.
from microbit import *
import utime

def weathercock_getDirection(pin):
    wind_dir = pin.read_analog()
    if 886 < wind_dir < 906:
        return "N"
    if 692 < wind_dir < 712:
        return "NE"
    if 395 < wind_dir < 415:
        return "E"
    if 478 < wind_dir < 498:
        return "SE"
    if 564 < wind_dir < 584:
        return "S"
    if 799 < wind_dir < 819:
        return "SW"
    if 968 < wind_dir < 988:
        return "W"
    if 939 < wind_dir < 959:
        return "NW"
    return "???"


def pulseIn(pin, pulse_state, max_duration=2000000):
    initial_time = utime.ticks_us()
    while pin.read_digital() is not pulse_state:
        if utime.ticks_us() - initial_time > max_duration:
            return 0
    start = utime.ticks_us()
    while pin.read_digital() == pulse_state:
        if utime.ticks_us() - initial_time > max_duration:
            return 0
    return utime.ticks_us() - start


def anemometer_getWindSpeed(pin, unit="m/s", pulse_per_revolution=1):
    speed_of_one_pulse = 0.66666667 / pulse_per_revolution
    pulse_microseconds = pulseIn(pin, 1, max_duration=1000000)
    if pulse_microseconds <= 0:
        return 0
    pulses_per_second = pulse_per_revolution / (pulse_microseconds / 1e6)
    speed = speed_of_one_pulse * pulses_per_second
    if unit == "km/h":
        return speed * 3600 / 1e3
    if unit == "inch/s":
        return speed / 2.54
    if unit == "knot":
        return speed / 0.514444444
    return speed

pin8.set_pull(pin8.PULL_UP)

while True:
    print(str(anemometer_getWindSpeed(pin8, unit='m/s')))
    print(str(weathercock_getDirection(pin1)))
    print(str(compass.heading()))
    utime.sleep(1)

