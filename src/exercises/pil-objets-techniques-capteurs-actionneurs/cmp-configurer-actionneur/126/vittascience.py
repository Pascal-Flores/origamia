"""
Auteur: Origamia
Interface: microbit
Nom du projet: 126 - Trois tours et puis s'arrete !
Description: Corriger le sens et le nombre de rotations du moteur de la roue des defis.
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="ex126_start_0" deletable="false" x="20" y="20"><statement name="DO"><block type="actuators_stepperMotor_uln2003driver_init" id="ex126_stepper_init_0"><field name="MOTOR">A</field><field name="IN1">pin0</field><field name="IN2">pin14</field><field name="IN3">pin1</field><field name="IN4">pin15</field><next><block type="actuators_stepperMotor_uln2003driver_moveSteps" id="ex126_stepper_move_0"><field name="MOTOR">A</field><field name="UNIT">ROTATIONS</field><field name="DIR">1</field><value name="STEPS"><shadow type="math_number" id="ex126_rotations_0"><field name="NUM">1</field></shadow></value></block></next></block></statement></block></xml>
"""
from microbit import *
from stepper import StepperMotor


motorA = StepperMotor(pin0, pin14, pin1, pin15)

# Reglages provisoires a corriger par l'eleve dans l'interface.
motorA.moveClockwise(1, motorA.ROTATIONS)
