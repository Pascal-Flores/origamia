"""
Auteur: Pascal Flores
Interface: microbit
Nom du projet: Nouveau projet
Description: 
Toolbox: vittascience
Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><variables><variable id="i0}4x2%.Pzj`YrDCRn09">variable</variable></variables><block type="on_start" id="G[=T#8yqB70`NFgYq}GP" deletable="false" x="0" y="0"><statement name="DO"><block type="io_pause" id="%6sfF0C33|TcPF|a`LTZ"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="VMUCrBB-qAL#z({YpZO_"><field name="NUM">1</field></shadow></value><next><block type="show_number" id="~M[Ne,.*4fRGMEpGp{mX"><value name="VALUE"><shadow type="text" id="NpbH}5:e[;-J](H|Xt__"><field name="TEXT">Bonjour !</field></shadow></value><next><block type="io_initChronometer" id="u`(l/WBN:SE}.otklDSL"><next><block type="text_append" id="j0SZH-1jbZ9=LFZ!mS3S"><field name="VAR" id="i0}4x2%.Pzj`YrDCRn09">variable</field><value name="TEXT"><shadow type="text" id="F#k8yH]ha;e_`#.|dhD+"><field name="TEXT"></field></shadow><block type="math_single" id="R}{~_`tF-CP)+8__/Mu]"><field name="OP">ROOT</field><value name="NUM"><shadow type="math_number" id=")I^uq(::)t6OtsGU/cq1"><field name="NUM">9</field></shadow></value></block></value><next><block type="controls_repeat" id="vkZ|3Q./6/w8;lP7s.*k"><value name="TIMES"><shadow type="math_number" id="|2Nxu#JK!Z^.{r{:p4=G"><field name="NUM">10</field></shadow></value><statement name="DO"><block type="controls_if" id="9QL2D.2ZpI_gNK^zEx@c"><value name="IF0"><block type="logic_compare" id="Jy:l.jJ;Sr?2+kuGr+7x"><field name="OP">EQ</field><value name="A"><block type="math_number" id="SpWM%**t4B.9+V.DW%WG"><field name="NUM">42</field></block></value><value name="B"><shadow type="math_number" id="vLF.Y5G:I:NsgDNk`!$O"><field name="NUM">1</field></shadow></value></block></value><statement name="DO0"><block type="io_pause" id="}Fr(*_87GlHXt?=z}OJq"><field name="UNIT">SEC</field><value name="TIME"><shadow type="math_number" id="g_MbiP5AvGUDiibO(E3P"><field name="NUM">1</field></shadow></value></block></statement></block></statement></block></next></block></next></block></next></block></next></block></statement></block><block type="forever" id="o[WN]+eeF.OUxGch67@8" x="463" y="-13"><statement name="DO"><block type="communication_serialWrite" id="!SimO*I9f9:oPX?%-5o|"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="3T)c,ZRHtnJqRKg`K1/["><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getLight" id="?k*C/;MU5h3j,KIXsJ:V"></block></value><next><block type="communication_serialWrite" id="8#MRn4K3?sOG:-p^z)bq"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="x1)RLCq5=q.5vL,vVju8"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getTemperature" id="T9hW#itYyb{il$w,,;,|"><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="(*Q31`(HE8SnL8R!QRZZ"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="[-o}Zd~nt8I[7rySmis0"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getAcceleration" id=".Wm[k;Ah8|dp:X/VZ_;="><field name="AXIS">x</field></block></value><next><block type="communication_serialWrite" id="rZbdvtp^;LXOMj?xJ00;"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="|9-q$-@blO~Z|b9KEY29"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getRotation" id="p/*}Ru17YAPMO$UJiw,U"><field name="AXIS">pitch</field></block></value><next><block type="communication_serialWrite" id="1EB.)P]K7%)JONPn8I.^"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id=")KWmQ1|u!wb3q/@H}%gd"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getCompass" id=";5p)*J*{T]5rF%s7`G8@"></block></value><next><block type="sensors_calibrateCompass" id="9AWb/J_f!J=;bXzblCK$"><next><block type="communication_serialWrite" id="QmkH:`Az/.ucvhx]CpJI"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="#TDWL_[Orj+MckebImd9"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_isCompassCalibrated" id="{dk:V:YDsdan(HhNH?Q~"></block></value><next><block type="communication_serialWrite" id="Kpa%uAJa}U=6j;I@[B|D"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="O,A,8=[q2?`~=4@nQXWY"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getMagneticForce" id="wo1w({*8m-Bzu0^0X;Ml"><field name="AXIS">x</field></block></value><next><block type="io_micro_onSoundDetected" id="_HfZdxt.iVpL1_83s-mI"><field name="STATE">LOUD</field><field name="TYPE">IS</field><statement name="DO"><block type="communication_serialWrite" id="Dv1x/UK/mPAd#%wv9n-E"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="S4Na6?2ENV{78bVw7t_S"><field name="TEXT">Bonjour !</field></shadow><block type="io_micro_getCurrentSound" id=";,ArAlKEtUt1Ed1[x/%P"></block></value></block></statement><next><block type="communication_serialWrite" id="QHgPMn$^hhJ$H#!lFr4q"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="D(vKb%On-]vvPPMl[;Qy"><field name="TEXT">Bonjour !</field></shadow><block type="io_micro_wasSoundDetected" id="Ei!sKC2?2N[mYC*_VFU3"><field name="STATE">LOUD</field></block></value><next><block type="communication_serialWrite" id="-mH$v-|AjyFc=9,{Y0;7"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="mTK%lMsG2uqY@gw/So2n"><field name="TEXT">Bonjour !</field></shadow><block type="io_micro_getSoundLevel" id="p+MZ2]dR*UPuVQ;[t1i~"></block></value><next><block type="communication_serialWrite" id="hm5LyhfGF)|p(+YBU1%a"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="`g?xIMHpv]KKyr@GvqcJ"><field name="TEXT">Bonjour !</field></shadow><block type="io_micro_getHistorySounds" id="UZfBPl}B8S9UBI$yt?I0"></block></value><next><block type="io_micro_setSoundThreshold" id="0^bGAE5?Zf9]WPP?;=g6"><field name="STATE">LOUD</field><value name="THRESH"><shadow type="math_number" id="L1^15h12sLddWtY9ej-N"><field name="NUM">255</field></shadow></value><next><block type="communication_serialWrite" id="U[FE:(T=i7]RWj_s6}}!"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="XEf/HA^Fdh!x)v!88yU;"><field name="TEXT">Bonjour !</field></shadow><block type="io_micro_soundCondition" id="9FfZoF0YDh/uhv]?~,,n"><field name="STATE">LOUD</field></block></value><next><block type="communication_serialWrite" id="GnSY-mexFPtW/Vg^gJzA"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="t]J.+,]Oe!KnFKK!L-#("><field name="TEXT">Bonjour !</field></shadow><block type="sensors_envirobit_tcs3472_getRGB" id="{=V0@E:aqG%IX{$cC56I"><field name="DATA">0</field></block></value><next><block type="communication_serialWrite" id="2l2!Pk*Ziid)F1@.eW/`"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="w0;s-NP{neghI[`x?ISv"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_envirobit_tcs3472_getBrightness" id="B0}1,__SB[q6:e6]Jg-|"></block></value><next><block type="sensors_envirobit_tcs3472_setLED" id="{^p[!lSQro~_+N|46)+4"><value name="STATE"><shadow type="io_digital_signal" id="e3mc]tB*RjRzgJr_C~rx"><field name="BOOL">HIGH</field></shadow></value><next><block type="communication_serialWrite" id="mTpMI)H2Q?FWXK#XqjT)"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="F8g/|;P1d+MgUxU-51xA"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_weatherbit_weathercock_getDirection" id="rOOXzwh{n`UmN=mzr*a2"></block></value><next><block type="communication_serialWrite" id=":370{*Z:oF9CA[ce)b.i"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="R)3-C@(!UV92TRvlpXVu"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_envirobit_bme280_getData" id="Sq-C={.-B`ddc{|KqI9="><mutation temp="true"></mutation><field name="DATA">TEMP</field><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="g[V}s0q||6dy)=?!RAt@"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="Ww8Lm|u9_--0+#qQXGS5"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_envirobit_getSoundLevel" id="1gkJ/Jh;(AMP4CGe_7Zm"></block></value><next><block type="communication_serialWrite" id="kVV*t)T,r1M4;/ij___t"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="wXJcsV@:T75G(W)-F8dK"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_envirobit_waitForClaps" id="?#q}~zq7SFB-L+#_(P,i"><field name="CLAPS">1</field><value name="DURATION"><shadow type="math_number" id="lDIak$i;okwF+-+V2I{*"><field name="NUM">1</field></shadow></value></block></value><next><block type="communication_serialWrite" id="|@dPeig|$WHP4eoz$EeM"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="mr!gDS{YUmkhKNlE0;~x"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_weatherbit_bme280_getData" id="_OyqT-dp%4{Bx.3##eON"><mutation temp="true"></mutation><field name="DATA">TEMP</field><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="?3cm;Yz-o}c4N(_RtNhF"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="EcVZm{UbY)}^Q1m;D|DX"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_weatherbit_anemometer_getSpeed" id="ZDV{[V0;Re}F_X-pkY%V"><field name="UNIT">M_S</field></block></value><next><block type="communication_serialWrite" id="/091~QEzHq#fmA_7C/wu"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id=";3(G0(ErM=5C6X_:e1)n"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_weatherbit_rainGauge_getDumps" id="Pz9WsKE7UADTvPlX!G~A"></block></value><next><block type="communication_serialWrite" id="6/,V2JokAgo?`A@XuSOW"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="esgDu3#P/(hyaZO{Pq8c"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_weatherbit_getSoilMoisture" id="+yHW1:lCbQK9kj{=~QK_"></block></value><next><block type="communication_serialWrite" id="M[eIUV10ldrr^xfRnQ$$"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="BG`GHBrnbvaijn@VpU]["><field name="TEXT">Bonjour !</field></shadow><block type="sensors_kitronik_bme280_getData" id="^falQy]z^`B^Zbpi%VR;"><mutation temp="true"></mutation><field name="DATA">TEMP</field><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="jb{IvC11J[4KzV[ECs#W"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="siNExF)u@}}Dp]=/,[H|"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_kitronik_klimate_bme280_getData" id="pm=uknI}^l`$qO4F5q20"><mutation temp="true"></mutation><field name="DATA">TEMP</field><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="IzUQm3j($wm;aeQ3y{wV"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="LD~Jc+$=!UBP`E2/Bb[f"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getSgp30Gas" id="=GGai{W+,wzGKw_.y;bF"><field name="GAS">CO2</field></block></value><next><block type="communication_serialWrite" id=":J1hqi1E]^ssy/g)#$|x"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="HY%sn-Rw;(Yt.y^|Qtp!"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getMultichannelGas" id="Uq4AJw+%xIEF_27!FD7P"><field name="GAS">CO</field></block></value><next><block type="communication_serialWrite" id="YTKP!BDh(-vY-6m.Y.CE"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="r0gkRi@P:cklLkOh%%RI"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getMultichannelGasV2" id="*UtDy3/-.7UI%wUB^~I!"><field name="GAS">NO2</field></block></value><next><block type="communication_serialWrite" id="QXxIYX%I.KJFvRO9xzxa"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="e2[1W_:pZ6qceIWioJ*Y"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getO2gas" id="aso,u9~G}skR?uuv$:C;"><field name="PIN">pin1</field></block></value><next><block type="communication_serialWrite" id="6W8[F_(OByr$yd:zTo[p"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="kVr;1LzD?Th5q!Rowa=l"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_SCD30_readData" id="d#6V4W/Q|jxhuP1hphj@"><mutation temp="false"></mutation><field name="DATA">CO2</field></block></value><next><block type="sensors_SCD30_forcedCalibration" id="jm9%={?7wS}FTRF|c]R%"><value name="DEFAULT"><shadow type="math_number" id="RefFNZ%r@%~?{^SdOM@c"><field name="NUM">420</field></shadow></value><next><block type="communication_serialWrite" id="q)4!*/B}amY6=`#a^ZVl"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="(NH1-f}X@#p=W.iGB|IP"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getAirQualityValue" id="JtA)5IPvE@|(yK:ELO!!"><field name="PIN">pin1</field></block></value><next><block type="communication_serialWrite" id="{6dKH5TD~Q?UI^x?+jBH"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="Sf#3Cn/}8,Jb;jldW[#1"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getParticulateMatter" id="uZ4D}2oDt/K?o=/,kx-b"><field name="TYPE">3</field></block></value><next><block type="communication_serialWrite" id=",b=Q`5Hn,s+}~B][rc$Y"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id=".5(u4BD4P7Kn81s9^,h="><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getBmp280Data" id="bOa:vYHvIdQ`!D?S=CLD"><mutation temp="true"></mutation><field name="ADDR">0x76</field><field name="DATA">TEMP</field><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="BW#?cu7gO/ObVyli0;c-"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="SMO9A$5~fEc1Ez/sJ@v@"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_bme280_getData" id=".l@1E{y/a0N69Q30CIw`"><mutation temp="true"></mutation><field name="DATA">TEMP</field><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="}ra.ys_61P#EB5kaBi2x"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="B9;2w(9RPpQz{:|Kn|?q"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getGroveMoisture" id="#xw$[K5=^vUo5IY:6`Gh"><field name="PIN">pin1</field></block></value><next><block type="communication_serialWrite" id="Z#c;AaoDvH@O0av9[)q~"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="i,!UFfT1%;|mMDTOVUl_"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getGroveCapacitiveMoisture" id="e[mqQkLe.T3Ca@0;.U!t"><field name="PIN">pin1</field></block></value><next><block type="communication_serialWrite" id="D#K9c.USfkR6tDJ8nf:Z"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="4.8ki`z5Z`~!m{g:2I,2"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getGroveTemperature" id="6rLk(z?b*-siKJ2?zT31"><field name="UNIT">CELSIUS</field><field name="PIN">pin1</field></block></value><next><block type="communication_serialWrite" id=".U8:KX7U+e0q+ng[$NTH"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="z`}[Q6u6Ll-y/}[M[piR"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getGroveHighTemperature" id="0%[7zi.$Z~5c;JKl{XpL"><field name="UNIT">CELSIUS</field><field name="A0">pin0</field><field name="A1">pin1</field></block></value><next><block type="communication_serialWrite" id="=wdDI~mZl9DusO(]JV!;"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="PtjG/|[7S%A[ZoVOR?h,"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_barometerReadData" id="AQr8?/8f8Z,UR[`sM=ZH"><mutation temp="true"></mutation><field name="DATA">TEMP</field><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="lD$Tf1rbkP]neNNDxRBr"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="9f.B+.7JXC5Xz|SWNki("><field name="TEXT">Bonjour !</field></shadow><block type="sensors_dhtReadData" id="r_KG5U=W{uIHY,]Myi)v"><mutation temp="true"></mutation><field name="DATA">TEMP</field><field name="PIN">pin1</field><field name="BOARD">v1</field><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="@c6u]CbXEI*,O#:xP(:o"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="P%{Y7B(7if%}tY$W{*m%"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_TH02readData" id="scA*csRFLI{Qb:%e:y[$"><mutation temp="true"></mutation><field name="DATA">TEMP</field><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="j#/D7faWD)6^o=T56)0j"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="@.yMR2:P{C_=m(!RALJT"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_SHT31readData" id="kAX*Q3}i=KWVHC5;_*3q"><mutation temp="true"></mutation><field name="DATA">TEMP</field><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="fnBmgCXFLNqY)/`9USej"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="hI[?r-N.{Cyi3f^1U^C$"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_SHT35readData" id="Y`)e:[ENFaKUb?Yb6LR?"><mutation temp="true"></mutation><field name="DATA">TEMP</field><field name="UNIT">CELSIUS</field></block></value><next><block type="communication_serialWrite" id="dy)#-5VY|gL-%,t})$FA"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="f`%n?pXWP1N*}F1?uEj%"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_mpx5700ap_getPressure" id="h=+j9_tD2W7dsS3^-q0?"><field name="PIN">pin0</field></block></value><next><block type="communication_serialWrite" id="yq,h2iS{;y2=XWM;A#ne"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="Z$Q5mG0,h?iWdqt$IyK^"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getGroveWaterAmount" id="bXCK`{me=)Op(1-1~{ox"><field name="PIN">pin1</field></block></value><next><block type="communication_serialWrite" id="GgEM]=(,bvc,-[B6`%zy"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="IfcZ,YUo^1aX,TitXtM?"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getRainGauge" id="xUP52s37r~8g2^j%dj4["><field name="PIN">pin1</field></block></value><next><block type="communication_serialWrite" id="Z_AM/:W*LG]%KGGb_N)+"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="-`ad2K{Aae!k0*)?hpc/"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getAnemometer" id="x^8ZIzXPIu0]`,frd1)c"><field name="PIN">pin1</field></block></value><next><block type="communication_serialWrite" id="}6KRZ|NWtxgU5U,9Cp?Z"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="eiwNiC`$%wv/x_[_!{bH"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getGroveLight" id="*7Io5nppqpy!stdQju0C"><field name="PIN">pin1</field></block></value><next><block type="communication_serialWrite" id="d^P$^=H{+8SdSSu#:yv["><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="mcCbK^-E?HA}A_#-x|-L"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getSunlightData" id="6{}[qCR#iG+X#y#!~G0y"><field name="VERSION">SI1145</field><field name="LIGHT">VIS</field></block></value><next><block type="communication_serialWrite" id="h0an6CfD~o%Xct[@VL9t"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="SFV%nbnVkCZMU]9Eb2~a"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_getUVindex" id="NL)roo::`Il5Ro7r/OJt"><field name="PIN">pin1</field></block></value><next><block type="communication_serialWrite" id="N~-8Lv_uaN!|w88tM3kT"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="Ntk97Y}V$$k43scRw0kp"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_colorSensor_getData" id="*^HxIS_:$7`J,@xouJ|Q"><field name="DATA">0</field></block></value><next><block type="communication_serialWrite" id="Sgq-Zb;`{lCTsmfHid97"><mutation newlines="false"></mutation><value name="TEXT"><shadow type="text" id="(#H5g9bJSu/v!/nqJs3B"><field name="TEXT">Bonjour !</field></shadow><block type="sensors_colorSensorV3_getData" id="%b%gzu::nbk8y05W06Gt"><field name="DATA">red</field></block></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></statement></block></xml>

Projet généré par Vittascience.
Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau
sur l'interface http://vittascience.com/microbit

"""

from microbit import *
import utime
import math
from tcs3472 import TCS3472
from bme280 import BME280
from sgp30 import SGP30
from multichannel_gas import GAS
from gas_gmxxx import GAS_GMXXX
from scd30 import SCD30
from hm330x import HM330X
from bmp280 import BMP280
from hp206c import HP206C
from dht11 import DHT11
from th02 import TH02
from sht31 import SHT31
from sht3x import SHT35
from si1145 import SI1145
from veml6040 import PiicoDev_VEML6040

t0 = 0
ENVIROBIT_SOUND_OFFSET = 580
RAIN_HEIGHT_RATIO = 0.2794

Var_VtoT_K = [[0, 2.5173462e1, -1.1662878, -1.0833638, -8.9773540/1e1, -3.7342377/1e1, -8.6632643/1e2, -1.0450598/1e2, -5.1920577/1e4],
              [0, 2.508355e1, 7.860106/1e2, -2.503131/1e1, 8.315270/1e2, -1.228034/1e2, 9.804036/1e4, -4.413030/1e5, 1.057734/1e6, -1.052755/1e8],
              [-1.318058e2, 4.830222e1, -1.646031, 5.464731/1e2, -9.650715/1e4, 8.802193/1e6, -3.110810/1e8]]

tcs3472 = TCS3472(pin8)
bme280 = BME280()
rainGauge_dumps = 0
# Soil Moisture Sensor on pin0
sgp30 = SGP30()
multichannel = GAS()
multichannel_v2 = GAS_GMXXX(0x08)
# Dioxygen Sensor on pin1
scd30_data = [0, 0, 0]
t_scd = running_time()
scd30 = SCD30(0x61)
# Air Quality Sensor on pin1
hm3301 = HM330X()
bmp280 = BMP280(0x76)
# Moisture Sensor on pin1
# Capacitive Moisture Sensor on pin1
# Temperature Sensor on pin1
# High Temperature thmc on pin0
# High Temperature room on pin1
hp206c = HP206C()
# DHT11 Sensor on pin1
dht11_1 = DHT11(pin1)
th02 = TH02()
sht31 = SHT31()
sht35 = SHT35()
# MPX5700 on pin0
# Water Sensor on pin1
# Rain Gauge on pin1
# Anemometer on pin1
# Light Sensor on pin1
si1145 = SI1145()
# UV Sensor on pin1
veml6040 = PiicoDev_VEML6040()

def weathercock_getDirection(pin):
  windDir = pin.read_analog()
  if windDir < 906 and windDir > 886:
    s = "N"
  elif windDir < 712 and windDir > 692:
    s = "NE"
  elif windDir < 415 and windDir > 395:
    s = "E"
  elif windDir < 498 and windDir > 478:
    s = "SE"
  elif windDir < 584 and windDir > 564:
    s = "S"
  elif windDir < 819 and windDir > 799:
    s = "SW"
  elif windDir < 988 and windDir > 968:
    s = "W"
  elif windDir < 959 and windDir > 939:
    s = "NW"
  else:
    s = "???"
  return s

def envirobit_readSound():
  return max(0, pin2.read_analog() - ENVIROBIT_SOUND_OFFSET)

def envirobit_waitForClap(timeout=1000, sensitivity=75):
  sensitivity = 105 - sensitivity
  start_time = running_time()
  while running_time() - start_time < timeout:
    if envirobit_readSound() > sensitivity:
      return True
  return False

def pulseIn(pin, pulseState, maxDuration = 2000000):
  t_init = utime.ticks_us()
  while (pin.read_digital() is not pulseState):
    if(utime.ticks_us() - t_init > maxDuration):
      return 0
  start = utime.ticks_us()
  while (pin.read_digital() == pulseState):
    if(utime.ticks_us() - t_init > maxDuration):
      return 0
  end =  utime.ticks_us()
  return end - start

def anemometer_getWindSpeed(pin, unit = 'm/s', pulse_per_revolution = 1):
  SPEED_OF_ONE_PULSE = 0.66666667/pulse_per_revolution # m/s
  pulse_s = pulseIn(pin, 1, maxDuration = 1000000) # us
  if pulse_s > 0:
    imp_per_sec = pulse_per_revolution/(pulse_s/1e6) # impulsions/s
    speed = SPEED_OF_ONE_PULSE*imp_per_sec #m/s
    if unit is 'km/h':
      return speed*3600/1e3
    elif unit is 'inch/s':
      return speed/2.54
    elif unit is 'knot':
      return speed/0.514444444
    else:
      return speed
  else: return 0

def rainGauge_getDumps(pin):
  global rainGauge_dumps
  pulse_us = pulseIn(pin, 1, maxDuration = 1000000) # us
  if pulse_us > 0:
    rainGauge_dumps += 1
  elif pulse_us == 0:
    rainGauge_dumps = 0
  return rainGauge_dumps * RAIN_HEIGHT_RATIO

def getAnalogMean(pin, n = 32):
  sum = 0
  for i in range(n):
    sum += pin.read_analog()
  return int(sum/n)

def readO2(pin, volt=False, Vref=3.3):
  measure = getAnalogMean(pin)
  return measure*(Vref/1023) if volt else measure*(Vref/1023)*0.21/2*100

def scd30_read(dataSelect):
  global t_scd
  global scd30_data
  t_scd = running_time() - t_scd
  if t_scd > 1000:
    scd30.readMeasurement()
    if not math.isnan(scd30.co2):
      scd30_data = [scd30.co2, scd30.t, scd30.h]
  return scd30_data[dataSelect]

def scd30_calibrateSensor(co2ppm):
  print("[SCD30_INFO] Go outside, and wait for 2 minutes. You can reset the board to restart program and redo calibration.\n")
  print("[SCD30_INFO] Start sensor calibration...\n")
  for i in range(60):
    scd30.readMeasurement()
    utime.sleep_ms(2000)
  scd30.setForcedRecalibration(co2ppm)
  print("[SCD30_INFO] End of calibration forced to " + str(co2ppm) + " ppm.\n")
  display.show(Image.YES)

def getGroveTemperature(pin, unit='celsius'):
  R = 1023.0/(pin.read_analog()+1e-3) - 1
  t = 1/(math.log(R)/4250+1/298.15) - 273.15 # celsius
  if unit == 'fahrenheit':
    t = t * 9/5 + 32
  elif unit == 'kelvin':
    t += 273.15
  return round(t, 2)

def getThmcTemp(pinA0, tempRoom):
  vout = pinA0.read_analog()/1023.0 * 5.0 * 1000.0
  vol  = (vout-350) / 54.16
  return K_VtoT(vol) + tempRoom

def getRoomTemp(pinA1):
  somme = 0
  for i in range(32):
    somme += pinA1.read_analog()
  a = ((somme>>5))*50.0/33.0
  res = (1023.0-a)*10000.0/a
  return 1/(math.log(res/10000.0)/3975.0+1/298.15)-273.15

def K_VtoT(mV):
  i = 0
  value = 0
  if mV >= -6.478 and mV < 0 :
    value = Var_VtoT_K[0][8]
    for i in range(8, 0, -1):
      value = mV * value + Var_VtoT_K[0][i-1]
  elif mV >= 0 and mV < 20.644 :
    value = Var_VtoT_K[1][9]
    for i in range(9, 0, -1):
      value = mV * value + Var_VtoT_K[1][i-1]
  elif mV >= 20.644 and mV <= 54.900 :
    value = Var_VtoT_K[2][6]
    for i in range(6, 0, -1):
      value = mV * value + Var_VtoT_K[2][i-1]
  return value

def mpx5700_readPressure(pin, n = 10):
  rawValue = 0;
  for i in range(n):
    rawValue += pin.read_analog()
  return (rawValue - 410) * 700 / float(n*1023)

def getUVindex(pin, n=15):
  somme = 0
  for i in range(n):
    somme += pin.read_analog()
    sleep(2)
  return (somme/n/4.3*1000 - 83) / 21

pin8.set_pull(pin8.PULL_UP)
pin2.set_pull(pin2.PULL_UP)
multichannel.power_on()
tempRoom_0 = getRoomTemp(pin1)

utime.sleep(1)
display.show('Bonjour !')
t0 = running_time()
variable = str(variable) + str(math.sqrt(9))
for count in range(10):
  if 42 == 1:
    utime.sleep(1)

while True:
  print(str(display.read_light_level()))
  print(str(temperature()))
  print(str(accelerometer.get_x()))
  print(str(math.atan2(accelerometer.get_y(), -accelerometer.get_z()) * 180.0/math.pi))
  print(str(compass.heading()))
  compass.calibrate()
  print(str(compass.is_calibrated()))
  print(str(compass.get_x()))
  if microphone.current_event() == SoundEvent.LOUD:
    print(str(microphone.current_event()))
  print(str(microphone.was_sound(SoundEvent.LOUD)))
  print(str(microphone.sound_level()))
  print(str(microphone.get_sounds()))
  microphone.set_threshold(SoundEvent.LOUD, 255)
  print(str(SoundEvent.LOUD))
  print(str(tcs3472.rgb()[0]))
  print(str(tcs3472.brightness()))
  tcs3472.set_leds(1)
  print(str(weathercock_getDirection(pin1)))
  print(str(bme280.temperature()))
  print(str(envirobit_readSound()))
  print(str(envirobit_waitForClap(timeout=1*1000)))
  print(str(bme280.temperature()))
  print(str(anemometer_getWindSpeed(pin8, unit='m/s')))
  print(str(rainGauge_getDumps(pin2)))
  print(str(pin0.read_analog()))
  print(str(bme280.temperature()))
  print(str(bme280.temperature()))
  print(str(sgp30.eCO2()))
  print(str(multichannel.get_gas(0)))
  print(str(multichannel_v2.calcVol(multichannel_v2.measure_NO2())))
  print(str(readO2(pin1)))
  print(str(scd30_read(0)))
  scd30_calibrateSensor(420)
  print(str(pin1.read_analog()))
  print(str(hm3301.getData(3)))
  print(str(bmp280.Temperature()))
  print(str(bme280.temperature()))
  print(str(pin1.read_analog()))
  print(str(pin1.read_analog()))
  print(str(getGroveTemperature(pin1)))
  print(str(getThmcTemp(pin0, tempRoom_0)))
  print(str(hp206c.get_measurement('temp_celsius')))
  print(str(dht11_1.getData(d=1)))
  print(str(th02.ReadTemperature()))
  print(str(sht31.get_temp_humi(data='t')))
  print(str(sht35.get_measurement('temp_celsius')))
  print(str(mpx5700_readPressure(pin0)))
  print(str(pin1.read_analog()))
  print(str(pin1.read_digital()))
  print(str(pin1.read_digital()))
  print(str(pin1.read_analog()))
  print(str(si1145.readVisible()))
  print(str(getUVindex(pin1)))
  print(str(tcs3472.rgb()[0]))
  print(str(veml6040.readRGB()['red']))
