"""
Interface: microbit
Nom du projet: Nouveau projet
Description: 
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><variables><variable id="{vNhKTKTZRpd3yWlm$]J">messageData</variable><variable id="JQktKXvh=0^UzEkv:`uP">serialData</variable><variable id="p8[jEl;4`(BZ_I7h~K9Y">stringData</variable><variable id="J-G5:bM_UrpYEdrCV~[s">numberData</variable><variable id="uq.3:U[3V}wh{ftv(0jf">name</variable><variable id="@b-%cJesn~jAfyY0OwHy">value</variable><variable id=")dwT`zaVFa#GJ5o:$E_?">HC05Data</variable><variable id="!oi(?@RzyW4E@Rus`B9Y">HM10Data</variable></variables><block type="on_start" id="G[=T#8yqB70`NFgYq}GP" deletable="false" x="0" y="0"></block><block type="forever" id="o[WN]+eeF.OUxGch67@8" x="200" y="0"><statement name="DO"><block type="communication_serialWrite" id="[9(yrN3k@tUKjlpGpkNe"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="|[{LV%}r92UVit=oPlpN"><field name="TEXT">Bonjour !</field></shadow></value><next><block type="communication_graphSerialWrite" id="RXG?}|3#2*]yh|QZ*]1H"><mutation items="1"></mutation><value name="ADD0"><block type="communication_graphSerialWrite_datasFormat" id="f!r);]L:?%Kj:y+If_]O"><field name="NAME">Donnée1</field></block></value><next><block type="communication_onSerialMessageReceived" id="u=Bb!.)u[I]L^_z.];7L"><field name="VAR" id="{vNhKTKTZRpd3yWlm$]J">messageData</field><next><block type="communication_onSerialDataReceived" id=".of=X|/0s`|Ig;gD-?rS"><field name="VAR" id="JQktKXvh=0^UzEkv:`uP">serialData</field><next><block type="communication_playComputerMusic" id="gz607g|6!Kst?m:x,sDs"><field name="NOTE">261.63</field><next><block type="communication_playComputerFrequency" id="#xSG%AAV_([F$qp;AS0F"><value name="FREQUENCY"><shadow type="math_number" id="*/+yqR`~``=?z.%g6|0("><field name="NUM">440</field></shadow></value><next><block type="communication_stopComputerMusic" id="g6GtI{(:f#,@nKB[Vm4^"><next><block type="communication_radioSendString" id="BWDhYyP[}V;9)C[;!D@^"><value name="STR"><shadow type="text" id=",-%myf|]4$~eHO[,MKq}"><field name="TEXT">Je suis le message radio !</field></shadow></value><next><block type="communication_radioSendNumber" id=":S+?d3b.B!CRV(=R4zCc"><value name="N"><shadow type="math_number" id="P27Td@K)K#KoGut8Xm=G"><field name="NUM">1</field></shadow></value><next><block type="communication_radioSendValue" id="W-s=gDZKv[BCc8:Po*Er"><value name="NAME"><shadow type="text" id="5{bD`o2cw/Cw%tJ6_Z=8"><field name="TEXT">pi</field></shadow></value><value name="VALUE"><shadow type="math_number" id="|3]y?O@X:tnB1UUs!e4v"><field name="NUM">3.14</field></shadow></value><next><block type="communication_onRadioDataReceived" id="0n@|npBn{2M/dDv|)@DQ"><field name="VAR" id="p8[jEl;4`(BZ_I7h~K9Y">stringData</field><next><block type="communication_onRadioNumberReceived" id="JYgqDfo!Q*,vdG9HIYrA"><field name="VAR" id="J-G5:bM_UrpYEdrCV~[s">numberData</field><next><block type="communication_onRadioValueReceived" id="H8/:U2/LTqDqBG:tb{=F"><field name="NAME" id="uq.3:U[3V}wh{ftv(0jf">name</field><field name="VALUE" id="@b-%cJesn~jAfyY0OwHy">value</field><next><block type="communication_radioConfig" id="tttZ6Vm}I.GFcvx.T#E*"><value name="CANAL"><shadow type="math_number" id="-AytltA4nFDb`(3,UVv/"><field name="NUM">7</field></shadow><block type="communication_radioReceiveFull" id="w@3b+OPA;XTgkFcl2D1y"><field name="DATA">msg</field></block></value><value name="POWER"><shadow type="math_number" id="1_*U^F(e3dnjfZYQ6:z|"><field name="NUM">6</field></shadow></value><value name="LEN"><shadow type="math_number" id="obei@:EJKmq`$GHhO0cg"><field name="NUM">32</field></shadow></value><value name="GROUP"><shadow type="math_number" id="[x@u2cAhtT?0U5VqYjp*"><field name="NUM">0</field></shadow></value><next><block type="communication_log_deleteLogs" id="hfl,lUk5sZkSL2A^329S"><next><block type="communication_log_serial" id="}f).]ixK;?|RFr:5ns`Z"><next><block type="communication_log_setLabel" id="EO)]eL6#*l1tgb~_R~|3"><mutation items="1"></mutation><field name="TIMESTAMP">MILLISECONDS</field><value name="ADD0"><shadow type="text" id="%~tCUJeog~!q!X[;h5g$"><field name="TEXT">Label1</field></shadow></value><next><block type="communication_log_addData" id=",`pB[k1]LxAYgd5sYSQ$"><mutation items="1"></mutation><value name="ADD0"><block type="communication_log_data" id="]f4lq-tE8EN|,}!Di)r%"><value name="LABEL"><shadow type="text" id="u6_u{/gnG)cTaC:X9PaC"><field name="TEXT">label</field></shadow></value><value name="DATA"><shadow type="math_number" id="J!=KBJ6g/%|aVj/ekQ`{"><field name="NUM">0</field></shadow></value></block></value><next><block type="communication_writeOpenLogSd" id="X1!1IG4i:NNh5|Deu|4h"><field name="BAUD">9600</field><field name="TX">pin0</field><field name="RX">pin14</field><value name="DATA"><block type="text_join" id=")PU#mq$ZaF~C%7Q!xnhn"><mutation items="3"></mutation><value name="ADD0"><shadow type="text" id=";SZYCW5#[V6@{U3m1}_-"><field name="TEXT">Donnée1</field></shadow></value><value name="ADD1"><shadow type="text" id="_GF*XcW?v9;.LCPT2klE"><field name="TEXT">;</field></shadow></value><value name="ADD2"><shadow type="text" id="4d@xRai=jhJpQVWhnZlN"><field name="TEXT">Donnée2</field></shadow></value></block></value><next><block type="communication_hc05_sendBluetoothData" id="NF0dt_CnTtf4$iVU;W00"><field name="RX">pin14</field><field name="TX">pin0</field><value name="DATA"><shadow type="text" id="x?k=lT}(`E]PW84f6F`s"><field name="TEXT"></field></shadow><block type="communication_hm10_getATCommand" id="]FTKOkJVkgh/(kLuzpU]"><field name="COMMAND">AT+HELP</field><field name="TXD">pin14</field><field name="RXD">pin0</field></block></value><next><block type="communication_hc05_onBluetoothDataReceived" id="5a2|0C}bPI0,^EYjYcSK"><field name="RX">pin14</field><field name="TX">pin0</field><field name="VAR" id=")dwT`zaVFa#GJ5o:$E_?">HC05Data</field><next><block type="communication_hm10_setATCommand" id="Z:./pQjYz37!QC!a$@]L"><field name="COMMAND">AT+NAME</field><field name="TXD">pin14</field><field name="RXD">pin0</field><value name="VALUE"><shadow type="text" id="K5e.e2+*9#Z-obSj%?TV"><field name="TEXT"></field></shadow></value><next><block type="communication_hm10_onBluetoothDataReceived" id="B3b^AdB`]$L8M^_JbudU"><field name="TXD">pin14</field><field name="RXD">pin0</field><field name="VAR" id="!oi(?@RzyW4E@Rus`B9Y">HM10Data</field></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></statement></block></xml>

Projet généré par Vittascience.
Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau
sur l'interface http://vittascience.com/microbit

"""

from microbit import *
import radio
import log
import utime

# Serial Receive used
# Lecteur SD on pin0

def radio_send(data):
  type = None
  if isinstance(data, int):
    type = "int:"
  elif isinstance(data, float):
    type = "float:"
  elif isinstance(data, bool):
    data = int(data)
    type = "bool:"
  if type is not None:
    radio.send("&&&" + type + str(data) + "&&&")
  else:
    raise ValueError("Unable to send number: '" + str(data) + "'")

def radio_sendValue(name, value):
  type = ""
  if isinstance(value, int):
    type = "int:"
  elif isinstance(value, float):
    type = "float:"
  elif isinstance(value, bool):
    value = int(value)
    type = "bool:"
  elif isinstance(value, list):
    type = "list:"
  elif isinstance(value, str):
    type = "str:"
  radio.send("&&&" + type + "[" + name + ";" + str(value) + "]&&&")

def radio_receiveData():
  data = radio.receive()
  if data:
    if data.find('&&&int:') != -1:
      return int(data[7:-3])
    elif data.find('&&&float:') != -1:
      return float(data[9:-3])
    elif data.find('&&&bool:') != -1:
      value = data[8:-3]
      if len(value) == 1: return bool(int(value))
      if value is 'False': return bool(0)
      else: return bool(1)
    elif data.find('&&&list:') != -1:
      return data[8:-3].strip('][').split(', ')
    else:
      return data
  else:
    return None

def radio_receiveValue():
  data = radio.receive()
  if data:
    if data.find('&&&int:[') != -1:
      parseData = data[8:-4].split(';')
      return parseData[0], int(parseData[1])
    elif data.find('&&&float:[') != -1:
      parseData = data[10:-4].split(';')
      return parseData[0], float(parseData[1])
    elif data.find('&&&bool:[') != -1:
      parseData = data[9:-4].split(';')
      return parseData[0], bool(parseData[1])
    elif data.find('&&&list:[') != -1:
      parseData = data[9:-4].split(';')
      return parseData[0], parseData[1].strip('][').split(', ')
    elif data.find('&&&str:[') != -1:
      parseData = data[8:-4].split(';', 1)
      return parseData[0], str(parseData[1])
    else:
      return None, None
  else:
    return None, None

def radio_receiveFull(data):
  details = radio.receive_full()
  if details:
    details = list(details)
    if data == 'msg':
      return details[0]  # The message
    elif data == 'rssi':
      return details[1]  # The RSSI value
    elif data == 'timestamp':
      return details[2]  # The timestamp
    else:
      raise ValueError("Data option '" + data + "' is not valid")
  else:
    return -1

def uart_switchTo(rx = None, tx = None, baudrate = 9600):
  if rx is None and tx is None:
    uart.init(baudrate=115200, bits=8, parity=None, stop=1)
  else:
    uart.init(baudrate=baudrate, bits=8, parity=None, stop=1, tx=tx, rx=rx)

def hm10_bluetooth_sendCommandAT(rx, tx, command, value = ""):
  data = command + (value if len(value) > 0 else "") + "\r\n"
  print("[HM10 INFOS] Command sent: " + data)
  uart_switchTo(rx, tx)
  uart.write(data)
  utime.sleep_ms(200)
  if not uart.any():
    uart_switchTo()
    print("Check connection wires. Invert RXD and TXD if necessary. Additionally, it is not possible to interact with AT mode when the module is connected to another device.\n")
    print("Waiting HM10 module in AT Mode...\n")
    uart_switchTo(rx, tx)
    while not uart.any():
      utime.sleep_ms(100)
  raw = uart.read()
  uart_switchTo()
  if raw is None:
    return ""
  response = raw.decode().replace("\r", "").strip()
  if len(value) > 0:
    print(response)
  return response

radio.on()

while True:
  print('Bonjour !')
  print('@Graph:Donnée1:' + str() + '|')
  sleep(50)
  if uart.any():
    messageData = uart.read().decode('utf-8')
    while uart.any():
      messageData += uart.read().decode('utf-8')
    pass
  if uart.any():
    serialData = uart.read()
    pass
  print('@music:261.63|')
  print('@music:' + str(440) + '|')
  print('@music:stop|')
  radio.send('Je suis le message radio !')
  radio_send(1)
  radio_sendValue('pi', 3.14)
  stringData = radio.receive()
  if stringData:
    pass
  numberData = radio_receiveData()
  if numberData is not None:
    pass
  name, value = radio_receiveValue()
  if name is not None and value is not None:
    pass
  radio.config(channel = radio_receiveFull('msg'), power = 6, length = 32, group=0)
  log.delete(full=True)
  log.set_mirroring(True)
  log.set_labels('Label1', timestamp=log.MILLISECONDS)
  log.add(label = 0)
  uart_switchTo(pin14, pin0, 9600)
  uart.write(('{}' * 3).format('Donnée1', ';', 'Donnée2') + '\n')
  uart_switchTo()
  uart_switchTo(pin14, pin0)
  uart.write(str(hm10_bluetooth_sendCommandAT(pin14, pin0, "AT+HELP")))
  uart_switchTo()
  uart_switchTo(pin14, pin0)
  if uart.any():
    HC05Data = uart.read()
    uart_switchTo()
    pass
  hm10_bluetooth_sendCommandAT(pin14, pin0, "AT+NAME", '');
  uart_switchTo(pin14, pin0)
  if uart.any():
    HM10Data = uart.read().decode()
    uart_switchTo()
    pass
