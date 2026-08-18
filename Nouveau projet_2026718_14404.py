"""
Auteur: Pascal Flores
Interface: microbit
Nom du projet: Nouveau projet
Description: 
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="G[=T#8yqB70`NFgYq}GP" deletable="false" x="0" y="0"><statement name="DO"><block type="actuators_setServoAngle" id="Uz;a:`S5p?mmC`!D18DC"><field name="PIN">pin2</field><value name="ANGLE"><shadow type="math_number" id="T;Od}gH#8`_-FX0q5#do"><field name="NUM">90</field></shadow></value><next><block type="actuators_continuousServo_setSpeed" id="Tg:8%fe(O_IWQlQ((4mc"><field name="DIR">1</field><field name="PIN">pin2</field><value name="SPEED"><shadow type="math_number" id="2mcc~NyC)T$j)L`4FQC+"><field name="NUM">100</field></shadow></value><next><block type="actuators_stepperMotor_uln2003driver_init" id="q9mx-l?W[6YYsdU-.GVf"><field name="MOTOR">A</field><field name="IN1">pin0</field><field name="IN2">pin14</field><field name="IN3">pin1</field><field name="IN4">pin15</field><next><block type="actuators_stepperMotor_uln2003driver_moveSteps" id="AP=:y6[3fTwu{dsQ*#uO"><field name="MOTOR">A</field><field name="UNIT">ROTATIONS</field><field name="DIR">1</field><value name="STEPS"><shadow type="math_number" id="l/8Guc3?Z2JtU2$v/D:`"><field name="NUM">1</field></shadow></value><next><block type="actuators_stepperMotor_uln2003driver_setDelay" id="v[fK2at/(O;0Ak}W7r:+"><field name="MOTOR">A</field><value name="DELAY"><shadow type="math_number" id="zSF{2%DXKHW~ryl@Q|Cl"><field name="NUM">3</field></shadow></value><next><block type="actuators_setFanPower" id="0BS?_5lC9s){FfP-[`h4"><field name="PIN">pin2</field><value name="POWER"><shadow type="math_number" id="V^Bc1XS]wi-qa~j;6dqY"><field name="NUM">1023</field></shadow></value><next><block type="actuators_setVibrationMotorState" id="Xd%yiNX@W5pGo!#]DsK|"><field name="PIN">pin2</field><value name="STATE"><shadow type="io_digital_signal" id="(DJa$#DdpgL3HC5/_Qpu"><field name="BOOL">HIGH</field></shadow></value><next><block type="actuators_setGroveRelayState" id="Fq.0HTXYRk!CaxRV7Vl]"><field name="PIN">pin2</field><value name="STATE"><shadow type="io_digital_signal" id="rzypVo)WIcoI0STwt4/L"><field name="BOOL">HIGH</field></shadow></value><next><block type="actuators_mosfet_setState" id="TM/$N2hXHLFII[Yz|v$E"><field name="PIN">pin0</field><value name="STATE"><shadow type="io_digital_signal" id="JOss#qNK{`.Qf5U[GeJ*"><field name="BOOL">HIGH</field></shadow></value><next><block type="actuators_mosfet_setPercentValue" id="?577a`:TH^|B/@/)~OC9"><field name="PIN">pin0</field><value name="VALUE"><shadow type="math_number" id="?TM9dEfUx=M~;al~{^6m"><field name="NUM">100</field></shadow></value><next><block type="actuators_controlAccessBitBarrier" id="svs3Tl3`=T@$-TM2-yg."><field name="ACTION">RAISE</field><next><block type="actuators_controlAccessBitBuzzer" id="(e/OO}g9z}C`@G(Qaa]V"><value name="VALUE"><shadow type="math_number" id="J+3W4C(2R]Tw)+P1[*4-"><field name="NUM">500</field></shadow></value><next><block type="actuators_kitronik_controlMotor" id="Cn}B?|:4LDAN:/2d3Fc5"><field name="MOTOR">1</field><field name="DIR">1</field><value name="SPEED"><shadow type="math_number" id="YPqXTw%ot.N@i}DkvZP$"><field name="NUM">100</field></shadow></value><next><block type="actuators_kitronik_stopMotor" id="6SK/92*D6TK)$s,c{.XP"><field name="MOTOR">1</field><next><block type="actuators_kitronikShield_setServoAngle" id="IX/[#n[}tSSP-Etne)w!"><value name="SERVO"><shadow type="math_number" id="bOONjA_HzW7#}5v-|unT"><field name="NUM">1</field></shadow></value><value name="ANGLE"><shadow type="math_number" id="?4f{g5|h]Gv=lL{9bTH_"><field name="NUM">90</field></shadow></value><next><block type="actuators_kitronik_playFrequency" id="hccD.B`jLAoelus)ldBA"><value name="FREQUENCY"><shadow type="math_number" id="}RJn#O%X?[7IJg*dL`bF"><field name="NUM">440</field></shadow></value><value name="DURATION"><shadow type="math_number" id="#ipQ.93+_hmo?]fvaS*4"><field name="NUM">500</field></shadow></value><next><block type="actuators_rekabit_runMotor" id="Ptt`:b4h+#64]-W3~=;p"><field name="MOTOR">M1</field><field name="DIR">Forward</field><value name="SPEED"><shadow type="math_number" id="418wK$dY.E02dcsOW1|8"><field name="NUM">125</field></shadow></value><next><block type="actuators_rekabit_setServoPosition" id="SU:9_gr=Y_;raG_r)aJH"><field name="SERVO">S1</field><value name="ANGLE"><shadow type="math_number" id="l55}9dlQul.wV]:A$55("><field name="NUM">90</field></shadow></value><next><block type="microbit_audio_play" id="L}aeOj15~0d`vnfI]X{}"><field name="SONG">GIGGLE</field><next><block type="microbit_audio_stop" id="C|;BoQWX0A2w#?{RQduw"><next><block type="actuators_playMusicGroveBuzzer" id="6xn9^!T,#F|uo=}owKOt"><field name="MUSIC">CARRIBEAN_PIRATES</field><field name="PIN">pin_speaker</field><next><block type="actuators_music_playSong" id="cc/yMV8[KANbzV/ZpEN,"><field name="SONG">DADADADUM</field><field name="LOOP">ONCE</field><field name="PIN">pin_speaker</field><next><block type="actuators_music_playNotes" id="VJX2T6|G$HizLkj|Lb^4"><mutation items="3"></mutation><field name="PIN">pin_speaker</field><value name="ADD0"><block type="actuators_music_note" id="teDR]FV^=nu[:*eSC*`$"><field name="NOTE">d</field><field name="OCTAVE">4</field><field name="DURATION">1</field></block></value><value name="ADD1"><block type="actuators_music_note" id="%B?C|Z}X_9KH%95;LP?;"><field name="NOTE">f#</field><field name="OCTAVE">4</field><field name="DURATION">1</field></block></value><value name="ADD2"><block type="actuators_music_note" id="IDJ_Jn=tNf|2nIve6Q$s"><field name="NOTE">g</field><field name="OCTAVE">4</field><field name="DURATION">1</field></block></value><next><block type="actuators_music_playFrequency" id="uS!wEV3hbuy:FPxSo-7q"><field name="PIN">pin_speaker</field><value name="FREQUENCY"><shadow type="math_number" id="rCz=z0N#Amd:vb_vvvKy"><field name="NUM">440</field></shadow></value><value name="DURATION"><shadow type="math_number" id="]I*qX+A*STtLnEgj7P_v"><field name="NUM">500</field></shadow></value><next><block type="actuators_music_stop" id="Fxs}NKH~oDU/^v42S==Q"><field name="PIN">pin_speaker</field><next><block type="actuators_music_setVolume" id="(bYkd.Yo~E~4IZ!XLU@`"><value name="VOL"><shadow type="math_number" id="mdDs3hMD#CqbTg*3ehku"><field name="NUM">255</field></shadow></value><next><block type="actuators_music_setTempo" id="vuOnBN%pLPd~PGIR,4z["><value name="TICKS"><shadow type="math_number" id="L45}AMl/~`+c;_fxfT)]"><field name="NUM">4</field></shadow></value><value name="BPM"><shadow type="math_number" id="(D#DLR//R+dr%K@L+4k4"><field name="NUM">120</field></shadow></value><next><block type="actuators_speech_saySomething" id="ktNPl6u]%Ks]9xa^Z8j["><value name="TEXT"><shadow type="text" id="Bjv5BsD~DyMSrUeZVkSm"><field name="TEXT">Bonjour !</field></shadow></value><value name="SPEED"><shadow type="math_number" id="SaJOigj%VNUo9OXFjFrL"><field name="NUM">100</field></shadow></value><value name="PITCH"><shadow type="math_number" id="GZ$L66b;K!ue@DO$eKdt"><field name="NUM">100</field></shadow></value><next><block type="actuators_setElectromagnetState" id="PR}0u,/|r2f/Q4uJ8/8!"><field name="PIN">pin0</field><value name="STATE"><shadow type="io_digital_signal" id="I3.M!GEGRT%G/}Jdrk~8"><field name="BOOL">HIGH</field></shadow></value><next><block type="actuators_setWaterAtomizerState" id="!J7EJHwRS`^f#GRH5wl-"><field name="PIN">pin0</field><value name="STATE"><shadow type="io_digital_signal" id="ViBENk8^MzS+8SJ2ew}p"><field name="BOOL">HIGH</field></shadow></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></statement></block><block type="forever" id="o[WN]+eeF.OUxGch67@8" x="200" y="0"></block></xml>

Projet généré par Vittascience.
Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau
sur l'interface http://vittascience.com/microbit

"""

from microbit import *
from stepper import StepperMotor
import utime
import music
from kitronik_servo_driver import KitronikServoBoard
from rekabit import *
import speech

# Servo on pin2
# Continuous Servo on pin2
motorA = StepperMotor(pin0, pin14, pin1, pin15)
# Fan on pin2
# Vibration Motor on pin2
# MOSFET on pin0
# Servo on pin0
# Buzzer on pin1
servoBoard = KitronikServoBoard()
# Buzzer on pin_speaker
# Electromagnet on pin0

def setServoAngle(pin, angle):
  if (angle >= 0 and angle <= 180):
    pin.write_analog(int(0.025*1023 + (angle*0.1*1023)/180))
  else:
    raise ValueError("Servomotor angle have to be set between 0 and 180")

def setServoSpeed(pin, direction, speed):
  pin.set_analog_period(20)
  if (speed >= 0 and speed <= 100):
    if direction is 1 or direction is -1:
      #clockwise: 1.5 ms to 1 ms | anticlockwise: 1.5ms to 2 ms (0 to 100%)
      speed_ms = speed * direction * 0.5 / 100 + 1.5
      pin.write_analog(1023 * speed_ms / 20)
    else:
      raise ValueError("continuous servomotor has no direction: '" + str(direction) + "'")
  else:
    raise ValueError("continuous servomotor speed is out of range: '" + str(speed) + "'")

def pitch(pin, noteFrequency, noteDuration, silence_ms = 10):
  if noteFrequency is not 0:
    microsecondsPerWave = 1e6 / noteFrequency
    millisecondsPerCycle = 1000 / (microsecondsPerWave * 2)
    loopTime = noteDuration * millisecondsPerCycle
    for x in range(loopTime):
      pin.write_digital(1)
      utime.sleep_us(int(microsecondsPerWave))
      pin.write_digital(0)
      utime.sleep_us(int(microsecondsPerWave))
  else:
    utime.sleep_ms(noteDuration)
  utime.sleep_ms(silence_ms)

def kitronik_controlMotor(motor, direction, speed = 100):
  value = speed/100.0*1023
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

def BuzzerCarribeanPirates(pin):
  NOTES_1 = [330, 392, 440, 440, 0, 440, 494, 523, 523, 0, 523, 587, 494, 494, 0, 440, 392, 440, 0]
  DURATIONS_1 = [125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 375, 125]
  NOTES_2 = [330, 392, 440, 440, 0, 440, 523, 587, 587, 0, 587, 659, 698, 698, 0, 659, 587, 659, 440, 0, 440, 494, 523, 523, 0, 587, 659, 440, 0, 440, 523, 494, 494, 0, 523, 440, 494, 0]
  DURATIONS_2 = [125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 125, 250, 125, 125, 125, 250, 125, 125, 250, 125, 250, 125, 125, 125, 250, 125, 125, 125, 125, 375, 375]
  for j in range(2):
    for i in range(len(NOTES_1)):
      pitch(pin, NOTES_1[i], DURATIONS_1[i])
  for k in range(len(NOTES_2)):
    pitch(pin, NOTES_2[k], DURATIONS_2[k])

setServoAngle(pin2, 90)
setServoSpeed(pin2, 1, 100)

motorA.moveClockwise(1, motorA.ROTATIONS)
motorA.setDelay(3)
pin2.write_analog(1023)
pin2.write_digital(1)
pin2.write_digital(1)
pin0.write_analog(1023 if 1 else  0)
pin0.write_analog(1023*100/100)
setServoAngle(pin0, 0)
music.pitch(440, duration=500, pin=pin1)
kitronik_controlMotor(1, 1, 100)
kitronik_stopMotor(1)
servoBoard.servo_write(1, 90)
music.pitch(440, duration=500, pin=pin12)
run_motor(Motor_M1, Direction_Forward, 125)
sets_servo_position(Servo_S1, 90)
audio.play(Sound.GIGGLE)
audio.stop()
BuzzerCarribeanPirates(pin_speaker)
music.play(music.DADADADUM, loop=False)
music.play(['d', 'f#', 'g'])
music.pitch(440, duration=500)
music.stop()
set_volume(255)
music.set_tempo(ticks=4, bpm=120)
speech.say('Bonjour !', speed=100, pitch=100)
pin0.write_digital(1)
pin0.write_digital(1)

while True:
  pass
