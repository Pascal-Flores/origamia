"""
Auteur: Origamia
Interface: microbit
Nom du projet: 120 - Le manege se reveille
Description: Choisir la commande qui met en marche le moteur du manege.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex120_start_0" deletable="false" x="20" y="20" /><block type="actuators_kitronik_controlMotor" id="ex120_motor_run_0" x="400" y="20"><field name="MOTOR">1</field><field name="DIR">1</field><value name="SPEED"><shadow type="math_number" id="ex120_motor_run_1"><field name="NUM">100</field></shadow></value></block><block type="actuators_kitronik_stopMotor" id="ex120_motor_stop_0" x="400" y="150"><field name="MOTOR">1</field></block><block type="microbit_audio_play" id="ex120_sound_0" x="400" y="280"><field name="SONG">GIGGLE</field></block></xml>
"""
# Le programme est volontairement incomplet : un bloc candidat doit etre
# connecte sous "Au demarrage" dans l'espace de travail Vittascience.
from microbit import *


def kitronik_controlMotor(motor, direction, speed=100):
    value = speed / 100.0 * 1023
    if motor == 1:
        if direction == 1:
            pin8.write_analog(value)
            pin12.write_digital(0)
        elif direction == -1:
            pin12.write_analog(value)
            pin8.write_digital(0)
    elif motor == 2:
        if direction == 1:
            pin0.write_analog(value)
            pin16.write_digital(0)
        elif direction == -1:
            pin16.write_analog(value)
            pin0.write_digital(0)


def kitronik_stopMotor(motor):
    if motor == 1:
        pin8.write_digital(0)
        pin12.write_digital(0)
    elif motor == 2:
        pin0.write_digital(0)
        pin16.write_digital(0)


# Blocs candidats, laisses non connectes dans l'espace de travail.
kitronik_controlMotor(1, 1, 100)
kitronik_stopMotor(1)
audio.play(Sound.GIGGLE)
