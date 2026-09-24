# A Novel Energy-Conscious Access Point eAP System With Cross-Layer Design in Wi-Fi Networks for Reliable IoT Services

> Source file: `A Novel Energy-Conscious Access Point eAP System With Cross-Layer Design in Wi-Fi Networks for Reliable IoT Services.pdf`

---

ReceivedMay24,2022,acceptedMay31,2022,dateofpublicationJune8,2022,dateofcurrentversionJune14,2022.
DigitalObjectIdentifier10.1109/ACCESS.2022.3181304
A Novel Energy-Conscious Access Point (eAP)
System With Cross-Layer Design in Wi-Fi
Networks for Reliable IoT Services
SEUNGJINLEE 1,(GraduateStudentMember,IEEE),HYUNGWOOCHOI 2,(Member,IEEE),
TAEHWAKIM1,(StudentMember,IEEE),HONG-SHIKPARK 2,(Member,IEEE),
ANDJUNKYUNCHOI2,(SeniorMember,IEEE)
1SchoolofInformationandCommunicationEngineering,KoreaAdvancedInstituteofScienceandTechnology(KAIST),Daejeon34141,SouthKorea
2SchoolofElectricalEngineering,KoreaAdvancedInstituteofScienceandTechnology(KAIST),Daejeon34141,SouthKorea
Correspondingauthor:HyungwooChoi(neojoey@kaist.ac.kr)
ThisworkwaspartlysupportedbyInstituteofInformation&communicationsTechnologyPlanning&Evaluation(IITP)grantfundedby
theKoreagovernment[MinistryofScienceandICT(MSIT)](No.2018-0-00691,DevelopmentofAutonomousCollaborativeSwarm
IntelligenceTechnologiesforDisposableIoTDevices,50%)andInstituteofInformation&communicationsTechnologyPlanning&
Evaluation(IITP)grantfundedbytheKoreagovernment[MinistryofScienceandICT(MSIT)](No.2020-0-00833,Astudyof5Gbased
intelligentIoTTrustEnabler,50%)
ABSTRACT This paper proposes a novel energy-conscious access point (eAP) system with cross-layer
design to increase the energy efficiency of IoT devices in IEEE 802.11 Wi-Fi networks for reliable IoT
services.TheproposedeAPsystemcontrolstheenergyresourcesofIoTdevicestoextendthelifetimeofthe
IoTdevice.Forthispurpose,wedevelopaneweAPsystemthatconsidersacross-layerdesignwithaprompt
TCPACKtransmitfunction,acaching-and-retransmitIoTdatafunction,andamultipleIoTdataaggregate
functiontoimprovetheenergyefficiencyoftheIoTdevice.Inaddition,theproposedeAPsystemhasadevice
energy management module that precisely controls operating parameters, such as the transmission period
ofIoTpackets,thedeliveryoftrafficindicationmessage(DTIM)valueofIoTdevices,andthetransmitting
powerofIoTdevices.Thesefeaturesextendthelifetimeofthebattery-poweredIoTdeviceswhilesatisfying
service requirements for reliable IoT services. The long listening time of TCP ACK messages in receive
mode (Rx) results in the high energy consumption of IoT devices due to the large round trip time. The
proposedeAPsystemreducesthereceptiontimeofTCPACKmessagesintheIoTdevice,usingtheprompt
TCPACKtransmitfunctionintheeAP.ThisreducesthelongRxmodetimeforTCPACKreception,and
increasestheshortsleepmodetime,whichresultsinincreaseoftheenergyefficiencyoftheIoTdevice.Inthe
energy-savinganalyses,weformulateanenergyconsumptionmodelfortheIoTdevice,anddeterminethe
energy-savinggainwhentheIoTdeviceusestheeAPsystemmodel,comparedtoalegacyAPsystemmodel.
OurperformanceevaluationresultsverifythattheproposedeAPsystemachievesamaximumimprovement
inenergyefficiencyofapproximately88%,and8.4timesimprovementintheexpectedlifetimeoftheIoT
device,comparedtothelegacyAPsystemmodel.
INDEX TERMS Energy consumption of IoT devices, energy-conscious AP, cross-layer design, energy-
saving,Wi-Finetworks,reliableIoTservices.
I. INTRODUCTION technologiesthatreduceenergyconsumptionthroughproto-
Wi-Fi is the most common global wireless access tech- cols, such as IEEE 802.11ax. [1], [2]. In particular, as IoT
nology, and the robust Wi-Fi infrastructure can be used services using Wi-Fi networks continue to expand, increas-
anywhere in the world for high-speed data transmission. ing the energy efficiency of IoT devices in Wi-Fi networks
Wi-Fi network protocols have primarily focused on opti- has become one of the field’s key issues [3]. Among these
mizing bandwidth, transmission distance, and transmission efforts,reducingtheenergyconsumptionofbattery-powered
rate, but recently, there has been an increasing interest in IoTdevicesisincreasinglyessentialforreliablewirelessIoT
services in indoor environments such as hospitals [4], [5].
The associate editor coordinating the review of this manuscript and Asbattery-poweredIoTdevicesincreaseintheindoorWi-Fi
approvingitforpublicationwasXiaolongLi . network, it is considered as the most important problem to
61228 ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME10,2022

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
increase the energy efficiency of IoT devices by utilizing battery-poweredIoTdevices,andthereliabilityofbiometric
networkprotocolsandhardwareaspectsultimately. informationtransmission.
Typically,awirelessaccesspoint(AP)relaysdatabetween The energy-saving of battery-powered IoT devices is the
a wired network and wireless devices, allowing wireless mostimportanttechnicalissuetobesolvedinordertoprovide
devices to access the Internet. Wireless APs are connected convenient services using cordless patient monitoring IoT
to routers using Ethernet cables and are primarily used by devices.Ifthisissueisnotsolved,itwouldrequirefrequent
medium and large organizations, where organizations typi- battery replacement due to the short operating lifetime of
callyhavemultipleAPstocovertheentirebuilding.Wireless battery-powered IoT devices. Therefore, it is essential to
APs are managed by a single router and, which is one of significantlyimprovetheenergyefficiencyofIoTdevices.
themainreasonswhylargerorganizationsusewirelessAPs Secondly, the reliable transmission of biometric
instead of Wi-Fi routers. Until now, wireless APs have had information must also be ensured to provide reliable health
simplefunctionssuchasrelaysoperatingatthebottomlayers monitoring IoT services for patients. Patient biometric
(Physical, MAC, Network). However, these days even tiny information includes critical personal medical information,
sensor devices work beyond the bottom layers (Transport, which requires high reliability, and this information must
Application),sowirelessAPsneedtogetsmarterwithmore be delivered to medical staff promptly without data loss
functionsusinginformationobtainedfromcross-layer,even or contamination. An agreement method which confirms
if they are a little more complex. For example, hospitals messagesare‘‘sent’’and‘‘arrived’’toeachothercanensure
alreadyhavemultiplewirelessAPsinstalled,andtheseAPs reliable transmission between the sender and the receiver.
are simply wireless devices that only relay wireless data The TCP (transmission control protocol) protocol with the
transmissionwithinthehospital.However,ifthewirelessAP ACK(acknowledgement)messagetoensurethereceptionof
utilizessomeinformationobtainedfromotherlayersandadds sending data is a common and global protocol for reliable
some functions, APs can control numerous stations or IoT transmission. Therefore, transmitting measured data using
devicesconnectedtotheAPtosaveenergyorachievereliable the TCP protocol by IoT devices can be the most suitable
datatransmission.Therefore,weconsiderhowtosaveenergy solution to ensure the reliable transmission of biometric
for IoT devices by developing a smarter AP system model informationforIoTservices.
withcross-layerdesignfortheWi-Finetworksinanindoor Fig.1showsanexampleofareliableandenergy-efficient
environmentsuchasahospital. IoT service using Wi-Fi networks in a hospital to provide
Mosthospitalscurrentlyusemedicaldevicescalledpatient real-time health monitoring. First, several battery-powered
monitors, which monitor and collect patients’ biometric IoT sensors are attached to the patient to measure the
information using multiple sensors attached to the patient’s patient’s biometric information (heart rate, electrocardio-
body, connected with wired cables. These legacy patient gram, body temperature, oxygen saturation, etc.). Then, the
monitors are very inconvenient for both patients and medi- datasensedbytheIoTdeviceistransmittedtoourproposed
cal staff. First, it is very inconvenient for patients to move energy-consciousAP(eAP)andforwardedtotheapplication
while attached to several cables connected to the patient server to be recorded and analyzed. The eAP uses informa-
monitor. In addition, the nurse’s visit at night to obtain the tion or energy-saving models from other layers to transmit
patient’s biometric information from the patient monitors controlmessagestomanagetheoperatingparametersofIoT
interferes with the patient’s comfortable sleep. Second, it is devices, such as the transmission period of the IoT packets,
very inconvenient for medical staff to manually record and thedeliveryoftrafficindicationmessage(DTIM)values,and
manageeverypatients’biometricinformationfromnumerous thetransmittingpoweroftheIoTdevicesforenergy-saving.
patientmonitors.Moreover,itisdifficulttocollectsufficient These three operating parameters are the main components
datatoaccuratelycheckthepatient’scondition,becausethe thataffecttheenergyconsumptionofIoTdevices[10],[11].
biometricinformationonthepatientmonitorisonlycollected Inadditiontothesethreeoperatingparameters,theeAPcan
intermittentlybythenurse.Thereisalsoariskofmissingor also control the IoT devices by adding another operating
incorrectrecordswhenrelyingonmanualrecords. parameters,suchasthetransmissionburstsize.
Battery-powered IoT devices can conveniently serve as a The proposed device energy management module in the
cordlesspatientmonitoringsystemforbothpatientsandmed- eAP optimizes the operating parameters of the IoT devices
ical staff. Some wireless patient monitoring systems using according to each patient’s level. The patient’s levels are
IoT devices have recently been researched and utilized in dividedintothreelevelsaccordingtothepatient’sconditions,
academic institutions, and actual devices have been devel- andtheenergymanagementoftheIoTdevicesvariesdepend-
oped to improve real-time heath monitoring IoT services ingonthepatient’slevels.Typically,hospitalsorhealthcare
[6]–[8]. Recently, Chungnam national university in Sejong, institutionsclassifypatientsinthreeorfourlevelstoincrease
SouthKorea, built a smart hospital using a cordless dis- controllabilityandpatientmanagement[12],[13].Forexam-
posable patch-type IoT sensor that can measure a patient’s ple,formildpatients(level1patients),theenergyefficiency
electrocardiogram[9]. oftheIoTdevicescanbeimprovedbysettingalargetrans-
However, a cordless patient monitoring system raises mission period for IoT packets, a large DTIM value, and
two important technical concerns: the energy-saving of the a small transmitting power value. On the other hand, for
VOLUME10,2022 61229

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
FIGURE1. Anexampleofareliableandenergy-efficientIoTserviceusingWi-Finetworksinahospitalforreal-timehealthmonitoring.
severeandcriticalpatients(level2and3patients),asmaller value may increase the Wi-Fi data rate (speed) because fast
IoT packet transmission period, smaller DTIM value, and modulation/codingcombinationsareavailable.
largertransmittingpowercanbeset.Eventhoughtheenergy Themaincontributionsofthispaperareasfollows:
efficiencyoftheIoTdevicesfortheselevelsisslightlylower • Thispaperproposesanovelenergy-consciousAP(eAP)
thanthatformildpatients,theexactconditionofthepatient systemmodelwithcross-layerdesigninWi-Finetworks
canbedeliveredmorefrequentlytomedicalstaff.Inaddition, toincreasetheenergyefficiencyofIoTdevices.Thepro-
thepatient’sbiometricinformation,recordedandanalyzedin posedeAPsystemmodelaimstoincreasethelifetimeof
theapplicationserver,istransmittedtothedisplayatthenurse battery-poweredIoTdevicesforreliableIoTservices.
desk in real-time so that the nurse can monitor the patient’s • To achieve this, we designed a new functional
condition, schedule appropriate treatment, and call a doctor architecture for the eAP system model considering the
asneeded. cross-layer design. We defined a new device energy
TheDTIMvalue(alsocalled‘‘theDTIMintervalvalue’’) management module in the eAP, which optimally con-
controlsthebeaconreceptiontimeoftheIoTdevice,which trolstheoperatingparameters,suchasthetransmission
allows a sleep mode for multiple beacons. Increasing the periodofIoTpackets,theDTIMvalues,andthetrans-
DTIMvaluehelpssaveenergybecauselisteningtoeachbea- mittingpoweroftheIoTdevicestoincreasetheenergy
conmessageconsumesalotofreceivingpowerandgenerally efficiencyofIoTdevices.
occupiesalargeportionoftheaverageenergyconsumption • To the best of our knowledge, combining the
oftheIoTdevice.ThelongertheDTIMvalueis,thehigher transport-layer three functions; the prompt TCP ACK
the energy-saving effect is. However, the high DTIM value transmit function, the caching-and-retransmit IoT data
hasatradeoffrelationshipwiththehighlatencyofdownlink function,andthemultipleIoTdataaggregationfunction;
packets,becauseanIoTdeviceinsleepmodecannotreceive withthebottom-layerfunctionsofanAPasacross-layer
thedownlinkpackets. design is the first attempt for the energy saving of IoT
The IoT device transmits a signal with a transmitting devices.
poweratoraboveacertainlevelwhichthereceiverAPcan • Through extensive simulations, the proposed eAP sys-
decode, considering the influence of noise and interference temmodelexhibitednotableimprovementsintheenergy
inthewirelesschannels.Ingeneral,Wi-Fidatarate(speed) efficiency of IoT devices in terms of energy-saving
depends on modulation and coding schemes, and an signal- gains, the expected lifetime of the IoT devices, and
to-interference-plus-noise ratio (SINR) value of a certain round-tripdelay.Specifically,theproposedeAPsystem
levelorhigherisrequiredforfastmodulation/coding.Similar modelachievedamaximumimprovementintheenergy
toincreasingtransmittingpower,increasingthetargetSINR efficiency of approximately 88%, and an 8.4 times
61230 VOLUME10,2022

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
improvementintheexpectedlifetimeofapatientlevel3 The TWT function is useful for IoT devices that commu-
IoT device, which communicated frequently with the nicate infrequently, but it has a heavy overhead to establish
eAP(thetransmissionperiodofIoTpackets=0.9s,the an agreed wake-up schedule between AP and IoT devices.
DTIMvalue= 3),respectively,comparedtothelegacy In [17], the authors modeled and analyzed the performance
APsystemmodel. ofIEEE802.11ahrestrictedaccesswindow(RAW)andTWT
Insummary,weproposetheenergy-consciousAPsystem function. RAW is a channel access protocol that uses sta-
with cross-layer design to increase the energy efficiency of tion grouping to increase energy efficiency and reduce con-
IoT devices. In particular, since the eAP sends ACK to IoT tention and collisions. The authors showed that RAW has
devicesdirectlywithoutreceivingACKfromtheserver,the better energy efficient performance in many stations (more
prompt TCP ACK transmit function and the caching-and- than 1250 stations) or high traffic scenarios, while RAW is
retransmit IoTdata function of theeAP mustbe considered not suitable for critical latency applications or low traffic
together in order to handle packet losses. The aggregation scenarios. And the evaluation also showed that the TWT
functionisalsoconsideredtocompensatefortheeAPenergy functioniseffectiveinenergysavingwhenthetransmission
burdenandimprovenetworkperformancebythereducingthe periodisatleast5minutes.In[18],theauthorsproposedan
number of packet transmissions. The proposed eAP system appropriateschedulingalgorithmforuplinkmulti-userbased
controls the transmission period of IoT packets, the DTIM on TWT function to dramatically reduce collisions in IEEE
value,andthetransmittingpowerofIoTdevicesaccordingto 802.11ax to maximize throughput and reduce energy con-
theapplicationlayermodelconsideringthephysicallayer. sumption. In [19], the authors reviewed several approaches
The rest of the paper is organized as follows. Section II based on TWT and wake-up radio (WUR) to reduce sen-
briefly explains the background and reviews related works. sorenergyconsumptionintheWi-Finetworkandevaluated
Section III explains the proposed energy-conscious AP sys- theirefficiency.TheWURmechanismusesaseparatetrigger
temmodelwithfunctionalarchitectureandthenewlydefined frametowakeuptheIEEE802.11axtransceiverchip-setto
eAP functions for improving the energy efficiency of IoT significantly reduce the energy consumption of IoT devices
devices.InSectionIV,weanalyzetheenergyconsumptionof whentrafficissparseinIEEE802.11ba.In[20],theauthors
the IoT devices using numerical analyses. Section V details presentedan802.11ba-basedWURreceiverthatisfullyinte-
theperformanceevaluationofIoTdeviceswiththeproposed grated within an IEEE 802.11a/b/g/n/ac Wi-Fi transceiver.
eAPsystem.Finally,conclusionsaredrawninSectionVI. TheWURreceiver,whichconsumesverytinyenergy,oper-
ates when the Wi-Fi system is in sleep mode and turns on
II. RELATEDWORKS the Wi-Fi radio upon receiving an 802.11ba-based wake-up
Energy-savingmethodsusedinIoTdevicesoverWi-Finet- packet. In [21], the authors reported that increasing listen
workshaveasimilarprinciple:Adjustthepower-savemode interval to reduce beacon reception wake-up instances may
accordingtotheservicesituation.Theadaptivepower-saving negativelyimpactenergyefficiencybecauseitrequiresmain-
modeinIoTdevicesfocusesonmaintainingthelowestpower taininganassociationoverheadinIEEE802.11IoTsystems
consumptionmodeasmuchaspossiblewhilemeetingservice using empirical evaluation. In [22], the authors proposed a
requirements.Inaddition,therehavebeenstudiestoreduce Wi-Fi AP that prioritized packets according to the power
the number of retransmissions and to control link manage- status of the IoT device to reduce the duty cycle. The duty
ment. In Wi-Fi networks, access points typically broadcast cyclerepresentstheratioofactivation(awake)timeduringa
a beacon frame every 100ms to announce the presence of cycle in an IoT station. Therefore, reducing the duty cycle
a wireless LAN. It contains information about the network alsoreducestheenergyconsumptionoftheIoTstation.The
and synchronizes members of the service set. The energy proposedAPusedtheIoTqueueallocationalgorithmforhigh
consumedbyIoTdevicesforbeaconreceptionaccountsfor priorities, using the remaining tail time of the IoT packet
a considerable portion of the total energy. There have been (permissible delay time of each packet before expiration).
variousstudiesonhowtoeffectivelyreducetheenergycon- However, the proposed AP needs more dedicated queues
sumedtoreceivethesebeacons.In[14],theauthorsproposed for IoT traffic and only focuses on downlink scheduling.
anadaptivebeaconlisteningprotocolthatdynamicallydeter- Moreover, the proposed AP is not suitable for services that
minedthebeaconlisteningintervalofamobilestationbased areinsensitivetodelay,suchasthermostatservices.In[23],
on the PDF (probability density function) of the estimated the portion of energy consumed for the TCP ACK message
round trip time. They reduced the number of beacon recep- reception of measured data transmission by an IoT device
tions while satisfying the required average delay. In [15], wasalmost17%foratemperaturesensor.Furthermore,this
the DTIM value was used to reduce the beacon reception portionofenergyconsumedbytheIoTdeviceforTCPACK
energy.ThehighertheDTIMwas,thelongertheIoTdevice reception can be increased to more than 17% in the event
went into sleep mode for multiple beacons, which poten- offrequentdatatransmission,suchasaheartratesensorfor
tially saved more energy. However, this was accompanied sensitiveservices.
by high latency in the downlink packets. In [16], the tar- Inaddition,therehavealsobeenseveralstudiesthatcon-
get wake time (TWT) scheme was used for energy-saving sidercross-layerinteractionstoincreasethethroughputand
in IEEE 802.11ah when data transmission was infrequent. energy efficiency of endpoint devices. In [24], the authors
VOLUME10,2022 61231

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
proposed a cross-layered quick UDP internet connection III. ENERGY-CONSCIOUSAP(eAP)SYSTEMMODEL
(C-QUIC) handover migration scheme that considers In this section, we propose an IEEE 802.11 eAP sys-
dynamic network conditions such as SINR to increase tem model for reliable and energy-efficient IoT services.
throughput and reduce power consumption in mobile net- First,wepresentthefunctionalarchitectureoftheproposed
works. C-QUIC performs early migration using predictive eAP system considering cross-layer design. The eAP sys-
SINR-based handover modeling using channel score and tem adopts a modular architecture that can be implemented
estimatedsmoothedroundtriptime(RTT)parameter.How- through software updates to legacy AP systems. Secondly,
ever, they focused on increasing throughput through early wepresentanovelmethodtoincreasetheenergyefficiencyof
handover migration in heterogeneous networks, rather than IoTdevicesinWi-Finetworksbyreducingthereceivingtime
saving energy on devices. In [25], the authors presented ofTCPACKusingthepromptTCPACKtransmitfunction
an xStream platform to increase the download rate of vari- intheeAP.
able applications using xNodes, which are logical entities
between the core network and the endpoint devices. The A. FUNCTIONALARCHITECTURE
xNodehasreal-timenetworkinformation(e.g.,availablelink Fig.2showsthefunctionalarchitectureoftheproposedeAP
capacity, round trip time, etc.) and controls the endpoint system model with cross-layer design. The proposed eAP
devices using the proposed scheduler and appropriate set- has a device energy management module, local cache, and
tings of TCP initial congestion window size to increase the threenewlydefinedtransportlayerfunctions;apromptTCP
download rate. In [26], the authors presented a cross-layer ACK transmit function, a caching-and-retransmit IoT data
approachforTCPuplinkflowsinmmWavenetworkstosolve function,andamultipleIoTdataaggregatefunction.
highpacketlossesandTCPtimertimeout&retransmission The device energy management module optimally con-
problems under non-line of sight conditions (NLOS). The trols the operating parameters of IoT devices, such as the
author used information gathered from multiple layers of transmission period of IoT packets, the DTIM value, and
user equipment (UE), such as round-trip time, SINR, and thetransmittingpowerofIoTdevices.Thecontrolmessages
available resource, to obtain an optimal congestion widow are delivered to the IoT devices via the message queueing
value,whichminimizedqueuingdelayswithoutcompromis- telemetrytransport(MQTT)protocol.MQTTisalightweight
ing throughput. In [27], the authors proposed an adaptive application-layer protocol that transports messages between
orthogonal frequency division multiplexing (OFDM) time devicesbasedonthepublish/subscribe(pub/sub)model.This
slot configuration algorithm depending on the amount of protocolusuallyrunsovertheTCP/IPprotocolandrequires
userdataenqueuedatthebasestationtoincreasedownload amessagebrokercalledtheMQTTbroker.Thecontrolmes-
rate compared to the fixed size slot configuration in 5G sage published by the device energy management module
networks.Theproposedalgorithmstartswithashortslotfor in the eAP is delivered to the IoT device using the MQTT
delay quality after connection establishment, and switches broker, and the IoT device subscribes the control message
slot configuration from a short slot to a long slot according forenergymanagementusingtheMQTT.Ontheotherhand,
to the buffered data and RTT of the base station to increase the measured biometric data published by the IoT device is
downloadthroughput. deliveredtotheeAPusingtheMQTT,andtheeAPsubscribes
In summary, the related works for energy-saving of themeasureddataoftheIoTdeviceusingtheMQTTbroker.
IoT devices have studied how to effectively reduce the ThelocalcacheintheeAPtemporarilystoresthemeasured
operating times that consume high energy in IoT devices dataoftheIoTdeviceforforwardingtotheapplicationserver.
[14]–[22]. In particular, they focused on reducing the trans- Thethreenewtransportlayerfunctionsaredefinedinthe
mission time of IoT packets and the reception time of eAP to save energy in the IoT system. Firstly, the prompt
beacon packets, which consume a lot of energy in IoT TCPACKtransmitfunctionistotransmititsownTCPACK
devices. However, research to reduce the energy consumed to the IoT device as soon as the eAP receives the uplink
forTCPACKreceptionofIoTpacketsisinsufficient.Also, packetfromtheIoTdevice.ThelegacyAPreceivestheTCP
research on cross-layer interaction AP to reduce energy ACKfromtheTCPserverandforwardsittotheIoTdevice,
consumption of IoT devices is insufficient in Wi-Fi net- whichrequirestheIoTdevicetostayawakeforalongtime
works. They mainly focused on increasing the throughput inreceive(Rx)modetoreceivetheTCPACK.However,the
anddownloadratebyusinginformationfromthecross-layer eAPtransmitspromptlyitsownTCPACKtotheIoTdevice
[24]–[27]. However, there are insufficient studies to reduce withoutwaitingforaTCPACKfromtheTCPserver,which
theenergyconsumptionofendpointdevicesusingcross-layer enablestheIoTdevicetoawakeforashorttimeinRxmode.
designs in Wi-Fi networks. Therefore, our study focuses This new function allows the IoT device to reduce energy
on efficiently reducing the energy consumed for TCP ACK consumption by reducing the Rx mode time and increasing
reception and retransmission in IoT devices using a novel thesleepmodetime.
eAPsystemwithcross-layerdesign.TheproposedeAPsys- Secondly,thecaching-and-retransmitIoTdatafunctionis
tem presented in the next section can be a solution to this toretransmitcachedIoTdatatotheTCPserverwhentheeAP
problem. doesnotreceiveTCPACKfromtheTCPserverwithintheset
61232 VOLUME10,2022

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
FIGURE2. Functionalarchitectureoftheproposedenergy-consciousAP(eAP)systemmodelwithcross-layerdesign.
time called TCP timer timeout. The eAP temporarily stores TheIoTdeviceshavemultiplebio-sensorsthatarebattery-
the measured data from the IoT device in the local cache. powered.Themeasureddataaresavedinmemoryduringthe
This retransmission occurs when the TCP ACK message transmissionperiod,andpublishedbytheapplicationMQTT
doesnotarrivewithintheTCPtimertimeoutduetonetwork protocol.Forreliabletransmission,themeasuredIoTdatais
congestion or other reasons. When the TCP timer timeout delivered by TCP protocol. The energy management in the
occurs, the eAP can undertake the retransmission burden of IoT devices receives a control message from the eAP and
the IoT device by retransmitting stored data in the cache to optimally controls operating parameters of the IoT device,
the TCP server without a retransmission request to the IoT suchasthetransmissionperiodoftheIoTpackets,theDTIM
device.Withthisnewfunction,theIoTdevicedoesnothave value,andthetransmittingpower.
theretransmissionburdenandcanstayinsleepmodeandsave These functional architectures can be easily constructed
energywhentheTCPtimertimeoutoccurs. andimplementedusingjustsoftwareupdateswithoutadding
Thirdly, the multiple IoT data aggregate function is to otherequipmenttothelegacy802.11Wi-Finetworksystem.
assemble IoT packets from multiple IoT devices into some
bursts.MostofthemeasuredIoTdatatransmittedfrommul- B. REDUCINGTCPACKRECEPTIONTIME
tipleIoTdevicestoAPsaredeliveredviasmallsizedatapack- We consider an uplink (UL) data transmission of the TCP
etscomparedtoaTCPmaximumsegmentsize(1460bytes). protocolforreliabletransmission.Wealsoonlyconsiderthe
WhenevertheAPreceivesdatafromtheIoTdeviceandsends datatransmissionmodelbetweenanAPandIoTdevices,not
data to the application server, there are many short-length the transmission model between IoT devices. Fig. 3 shows
packetsandACKsbetweentheAPandtheapplicationserver, acomparisonbetweenthelegacyandproposedprocedurein
whichgeneratesunnecessaryandheavytrafficload.Withthis 802.11Wi-Finetworks.
newaggregatefunction,theeAPcollectsdatareceivedfrom In the legacy procedure, the AP receives measured data
multiple IoT devices for a particular duration, then makes fromtheIoTdevicesanddeliversittotheTCPserver.After
someburstsandsendsthemtotheapplicationservertoreduce the network response time, the AP receives a TCP ACK
network traffic between the eAP and the application server. message from the TCP server and forwards it to the IoT
Inaddition,decreaseinthenumberoftransmissionsreduces devices. Meanwhile, after sending measured data in TCP
thetransmissionenergyconsumptionoftheeAP. packets,theIoTdeviceswitchestoRxmodetoreceiveACK
The application server for IoT services can be located and stays in Rx mode until receiving a TCP ACK message
remotelyorlocally.Theapplicationserverreceivesthemea- from the TCP server via the AP. However, the waiting time
sureddatafromtheIoTdevicesbysubscribingtotheMQTT toreceiveaTCPACKmessageintheRxmodeislong,due
broker and records them in the database. Then, the stored to the network response time between the AP and the TCP
dataisanalyzedintheapplicationserveranddeliveredtothe server. The network response time is caused by processing
medicalstafftomonitorthepatient’sconditioninreal-time. time,propagationtime,andnetworkcongestion.Becauseof
VOLUME10,2022 61233

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
ACKgenerationtimeislongerthantheSIFS,theprocedure
may be changed to transmit the Wi-Fi ACK first, and then
transmit the TCP ACK using random channel access. The
IoTdevicecanreceivetheTCPACKmessagefromtheeAP
withinashortertimebecausetheTCPACKmessagedoesnot
havearoundtriptimebetweentheeAPandtheTCPserver.
As such, the eAP reduces the waiting time for the IoT
devicetoreceivetheTCPACKmessage,asshowninFig.3b,
comparedtothelegacyprocedureinFig.3a.TheIoTdevice
that receives the TCP ACK message with a short listening
time switches to transmit (Tx) mode to send the L2 ACK
message to the eAP and then switches to sleep mode until
the next beacon reception. Fig. 5 shows the increased sleep
timeofanIoTdevicebeforereceivingthefollowingbeacon
message,comparedtothelegacyprocedureinFig.4.
If the eAP does not receive a TCP ACK from the TCP
server within a certain period of time (TCP timer timeout
interval), the measured data cached by the eAP is retrans-
mitted on behalf of the IoT device. In addition, the eAP
aggregates data received from multiple IoT devices, makes
themintosomebursts,andsendsthemtotheTCPserver.That
is,theeAPservesasavirtualTCPserverfortheIoTdevices,
andservesasavirtualclientfortheTCPserver.
C. CONTROLLINGOPERATINGPARAMETERSOFIoT
DEVICES
Some patients require frequent biometric data transmission
fortimelyandappropriatetreatment,whilesomepatientsdo
not need frequent biometric data transmission. Since each
patient’s health status is different, appropriate controlling
operatingparametervaluesofIoTdevicesareneededaccord-
ingtothepatient’sconditiontoincreasetheenergyefficiency
of IoT device. As mentioned in the application case study
FIGURE3. Acomparisonofthelegacyandtheproposedprocedures.
oftheintroduction,wedividedallpatientsintothreepatient
levels based on the health condition to provide real-time
health monitoring IoT services. Mild patients can tolerate
thelongawaketimerequiredtoreceiveaTCPACKmessage, infrequentanddelayedtransmissionofbiometricdatacom-
the IoT device has a short sleep time before receiving the pared to critical patients. For example, for mild patients
followingbeaconmessage,asshowninFig.4. (level1patients),theenergyefficiencyoftheIoTdevicescan
In the proposed approach, the eAP receives and caches be improved by setting a large transmission period for IoT
measured data from the IoT devices. After that, the eAP packets,alargeDTIMvalue,andasmalltransmittingpower
generates a TCP ACK message of its own and immediately value. On the other hand, for severe and critical patients
sendstheTCPACKmessagetotheIoTdeviceonbehalfof (level 2 and 3 patients), a smaller IoT packet transmission
theTCPserver.TheTCPACKframesizeis54byteswhich period, smaller DTIM value, and larger transmitting power
contains40bytesofTCP/IPheader,6bytesofsourceMAC, can be set. Even though the energy efficiency of the IoT
6bytesofdestinationMAC,and2bytesofframetype.Also, devices for these levels is lower than that for mild patients,
Wi-FiACKwithTCPACKcontains54bytesofTCPACK the exact condition of the patient can be delivered more
and30bytesofWi-FiMACheader,sotheWi-FiACKframe frequently to medical staff. There is a tradeoff relationship
sizeis84bytesinoursystemmodel.TheSIFS(shortinter- between frequent data transmission and improvement the
framespace)is10µsand16µsinIEEE802.11n(2.4GHz) energyefficiencyofIoTdevices.Therefore,findingoptimal
andIEEE802.11ac/ax,respectively.Theprocessingtimefor operating parameters of IoT devices while satisfying QoS
TCP ACK frame generation is from 2µs to 100µs [28]. requirementsofhealthmonitoringIoTservicescanimprove
Ingeneral,thepacketgenerationtimedependsonthenetwork theenergyefficiencyofIoTdevices.
equipment such as CPU, the network traffic loads, and etc. TheproposedeAPsystemoptimallycontrolstheoperating
In our evaluation model, we assumed the TCP ACK frame parameters of IoT devices, such as the transmission period
generation time is less than 10µs. However, when the TCP ofIoTpackets,theDTIMvalue,andthetransmittingpower
61234 VOLUME10,2022

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
| FIGURE4. | PowerconsumptionoftheIoTdeviceinthelegacyAPsystemmodel. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of IoT devices, according to the patient’s level. Now we delay because the IoT device cannot receive downlink data
formulate the optimization problem to increase the energy during the next promised trigger reception in sleep mode.
efficiencyofIoTdevices. Timelinessandshortdownlinkdelayareessentialfordeliv-
|     |     |     |     |     |     |     |     | ering reliable | healthcare | service. |     | For example, | timeliness |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------- | -------- | --- | ------------ | ---------- | --- |
andshortdownlinkdelayareimportantfactorsforchanging
IV. ENERGYCONSUMPTIONANALYSIS
|     |     |     |     |     |     |     |     | the uplink | transmission | period | due | to a sudden | change | in a |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | ------ | --- | ----------- | ------ | ---- |
Inthissection,weanalyzetheenergyconsumptionoftheIoT
deviceusingtheproposedeAPsystemmodel.Wefirstlyfind patient’s condition or for quickly delivering an appropriate
|             |          |     |       |        |            |     |           | treatment | order from | a doctor. | Therefore, |     | the TWT | scheme |
| ----------- | -------- | --- | ----- | ------ | ---------- | --- | --------- | --------- | ---------- | --------- | ---------- | --- | ------- | ------ |
| the optimal | transmit |     | power | of the | IoT device | in  | an indoor |           |            |           |            |     |         |        |
islessappropriateforfrequentframeexchangescenariosthat
| environment | where | noise | and | interference |     | exist. | Secondly, |     |     |     |     |     |     |     |
| ----------- | ----- | ----- | --- | ------------ | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
we analyze the operating time for each mode of the IoT haveashortperiodoftransmission,suchasthehealthmoni-
toringservice.Nevertheless,astheTWTschemecanreduce
devicetocalculatetheenergyconsumptionoftheIoTdevice.
Finally,wedeterminetheenergy-savinggainwhenusingthe furtherenergyconsumptionforbeaconreceptioncomparedto
eAPsystemmodel. theDTIMscheme,weaddedtheTWTschemeasanoptional
usecaseintheeAP.Inaddition,sincetheenergyconsumption
| We assumed |     | an IEEE | 802.11ax |     | network | system, | which |     |     |     |     |     |     |     |
| ---------- | --- | ------- | -------- | --- | ------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
is the latest standard for Wi-Fi networks. We also assumed fortheinitialTCPconnectionprocedure,whichisaone-time
procedure,isnegligibleamongthetotalenergyconsumption
| a service | scenario | in  | which | IoT | packets | are transmitted |     |     |     |     |     |     |     |     |
| --------- | -------- | --- | ----- | --- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
periodically and frequently with short transmission period of the IoT device, the initial TCP connection establishment
(e.g., wireless patient’s health monitoring service). We con- procedure is not considered in the IoT energy consumption
analysis.TheinitialsetuptimeofTWTagreementsbetween
| sidered | the DTIM | scheme | as  | an energy | saving | method | for |     |     |     |     |     |     |     |
| ------- | -------- | ------ | --- | --------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
IoTdevicesbyreducingthenumberofbeaconreceptionsin IoTdevicesandAPsisalsonotconsideredintheIoTenergy
consumptionanalysis.ThisisbecausetheinitialTWTagree-
| 802.11 | networks. | As  | mentioned | earlier, | high | DTIM | values |     |     |     |     |     |     |     |
| ------ | --------- | --- | --------- | -------- | ---- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
mentscanbesetupinanimplicitmodethatdoesnotrequire
| helpto | reducetheenergy |     | consumedto |     | receivebeacons,but |     |     |     |     |     |     |     |     |     |
| ------ | --------------- | --- | ---------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
it increases the latency of downlink IoT packets. Therefore, repetitionoftheTWTsetupframes.Also,weonlyassumed
|                 |     |        |                |     |      |       |          | a transmission | scenario | between |     | AP and | IoT devices, | not |
| --------------- | --- | ------ | -------------- | --- | ---- | ----- | -------- | -------------- | -------- | ------- | --- | ------ | ------------ | --- |
| it is important |     | to use | an appropriate |     | DTIM | value | based on |                |          |         |     |        |              |     |
thecontextoftheapplicationlayer.Also,weaddedthecase betweenIoTdevices.
| of using | the TWT | scheme | instead |     | of the | DTIM | scheme in |     |     |     |     |     |     |     |
| -------- | ------- | ------ | ------- | --- | ------ | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
theeAP.TheTWTschemeisanenergysavingmechanismof A. OPTIMALTRANSMITPOWEROFTHEIoTDEVICE
802.11axforIoTdeviceswithlongtransmissioncycles.The In the proposed eAP system model with cross-layer design,
TWTschemeisusuallyusedforlongperiodictransmissions, we assume that the IoT device can change the transmitting
suchastensofseconds,minutes,anddays.However,thecons power according to the channel condition for guarantee-
oftheTWTschemearelackoftimelinessandlongdownlink ing variable QoS requirements [29]. The following formula
| VOLUME10,2022 |     |     |     |     |     |     |     |     |     |     |     |     |     | 61235 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
FIGURE5. PowerconsumptionoftheIoTdeviceintheeAPsystemmodelwithDTIMscheme.
developmentisrequiredtocalculatetheoptimaltransmitting IoTdevice,P istheelectronicpowerconsumptionoverhead
O
poweroftheIoTdevice. incurredinthecommunicationmoduletoencodeamessage,
The signal-to-interference-plus-noise ratio (SINR) at the and T is the shortest time for transmitting a fixed-length
m
eAPisgivenby, message[31].UsingShannon’sinformationcapacitytheorem
γ = P R , (1) C =Wlog 2 (1+SNR),thetransmittingtimeofafixed-length
P +P messageisgivenby,
I N
where γ is the SINR seen by the eAP, P R is the received N
powerattheeAP,P I isthemeasuredinterferencepoweratthe T m = Blog (1 m +γ) , (4)
2
eAP,andP isthemeasurednoisepowerattheeAP.Usually,
N
interference power P I and noise power P N are measured where N m is a fixed message length, B is the bandwidth of
together at the AP as P I + P N . We assume the value of the channel, and γ is the SINR. By substituting the above
P I +P N is −90dBm which is a suitable value in an indoor relationships, the energy consumption of the IoT device in
wirelessenvironment.ThereceivedpowerattheeAP,P R can thetransmittingmodeisgivenby[31],
becalculatedby,
(cid:104)µ (cid:105) N
P =L·P , (2) E = (P +P )γ +P m . (5)
R TX TX L I N O Blog (1+γ)
2
where L is the total loss factor between the IoT device and
the eAP, P is the transmit power of the IoT device. The Fromtheaboverelation,allparametersexceptγ arerelated
TX
loss factor can be modeled, for example, by using the dis- to channel limitations and hardware. However, we note that
tance path-loss model with a fading component, i.e., L = thetargetSINRγ isafreevariablethatthesystemcancontrol
1 d−ah[30],whereL isaconstantdependingonthetrans- byadjustingthetransmitpoweroftheIoTdevice.
m
Lo
ission frequency an
o
d the antenna gains. Also, d is the We also consider the retransmission probability due to
distance between transmitter and receiver, a is the path-loss transmissionerrorstocalculatethetransmittingenergycon-
exponent,andhisarandomvariablerepresentingthechannel sumed by the IoT device. The retransmission probability p e
fading[30],[31]. isgivenby,
The energy consumed by the IoT device to transmit a
specificlengthmessageisgivenby, p e =p c +p l , (6)
E =(µP +P )·T , (3)
TX TX O m where p is the probability of packet collision, and p is
c l
where µ is the conversion factor of a power amplifier from the probability of wireless link fail between the IoT device
electricpowertoRFpower,P isthetransmitpowerofthe and the AP. The packet collision probability p can be
TX c
61236 VOLUME10,2022

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
approximatedbybelow[32], whenusingtheLambert-Wfunction,thatis,W[z]eW[z] = z,
wecansubstitutetheoptimaltransmitpoweroftheIoTdevice
(cid:32)
1
(cid:33)n−1 (cid:18)
1
(cid:19)n−1
asbelow,
p =1− 1− =1− 1− ,
c (cid:98)(W 2 +1)(cid:99) W backoff P ∗ = P I +P N (cid:20) exp (cid:18) 1+W (cid:20) A 2 /A 1 −1 (cid:21)(cid:19) −1 (cid:21)
TX L e
where,
P +P
= I Nγ∗. (11)
W 2W
W = (1−p) +p(1−p) +... L
backoff
2 2 Accordingly, the target SINR γ∗ at the minimum bound is
2mW 2mW
+pm(1−p) +pm+1 givenby,
2 2
= 1−p−p(2p)m · W , (7) γ∗ =exp (cid:18) 1+W (cid:20) A 2 /A 1 −1 (cid:21)(cid:19) −1. (12)
1−2p 2 e
where W is the minimum window size, n is the number of B. ENERGYCONSUMPTIONOFTHEIoTDEVICE
IoTdevices,W backoff istheoverallaveragebackoffwindow In the proposed eAP system model, a cycle is defined as a
size,pisthepacketcollisionprobabilityofeachtransmission, period between the start time of the IoT data transmission
misthemaximumrecursivetimesthatincreaseW,and2mW
and the start time of the subsequent IoT data transmission,
isthemaximumwindowsize.Thisapproximationofpacket asshowninFig.5.Thetimeforeachoperatingmodeinthe
collisionprobability,p c ,isbasedontheassumptionthateach IoTdeviceinacyclecanbeobtainedusingtheaboveequa-
packetcollideswithconstantandindependentprobabilityp, tions.Inthissection,weanalyzethetimeforeachoperation
anditisalsoindependentofthechannelstatus. modeinacycleandtheenergyconsumptionoftheIoTdevice
From[33],[34],theprobabilityofpacketcollision,p c can whenusingtheDTIMschemeandtheTWTscheme.
beapproximatedby, The Tx mode time of the IoT device considering the
 (cid:115)  retransmissionprobabilityinacycle,T tx ,isgivenby,
1 4
(cid:18)
4
(cid:19)2
W
p c ≈ 2 1+ g − 1+ g  , where g= n−1 . T tx = (1+p e )t data +t L2ack
(1+p )N N
= e data + L2ack , (13)
(8) Blog (1+γ) Blog (1+γ)
2 2
where t is the time taken to transmit the measured data
By applying the above retransmission probability, data
from the IoT device, t is the transmitting time of the
p ,theenergyconsumptionoftheIoTdeviceconsideringthe L2ack
e
L2 ACK message from the IoT device, N is the length
retransmissionprobabilityinthetransmittingmodeisgiven data
oftransmittingdata,andN isthelengthoftheL2ACK
by, L2ack
message.
(cid:18) (cid:19)
E = µ P R +P T IntheDTIMscheme,theRxmodetimeoftheIoTdevice
TX L O m in a cycle consists of several beacon reception times and a
(cid:104)µ (cid:105) N (1+p ) TCPACKreceptiontime.Thisisbecauseweassumedonly
= (P +P )γ +P m e
L I N O Blog (1+γ) the data transmission scenario between the IoT devices and
2
(cid:20)µL (cid:21) N (1+p ) theAP,notbetweentheIoTdevices.TheTCPACKreception
= d−α O h (P I +P N )γ +P O Blo m g (1+ e γ) timecanbereducedusingtheproposedeAPsystem.Accord-
2 ingto[23],theportionofenergyconsumedfortheTCPACK
A γ +A
= 1 2 , reception time is about 17 percent in a 60-second transmis-
log (1+γ)
2 sioncycleforatemperaturesensor.Otherbio-sensors,such
where, as heartbeat, electrocardiogram and blood pressure sensors,
requiremorefrequenttransmissionofmeasureddata,sothe
µL N (1+p )
A = O m e (P +P ), portionofenergyconsumedforTCPACKreceptiontimeis
1 Bd−ah I N
greaterthanthatforthetemperaturesensor.Thisisbecause
N (1+p )P
A = m e O. (9) morefrequentdatatransmissionrequiresmorefrequentTCP
2
B ACK reception. The Rx mode time of the IoT device in a
WecanobtaintheoptimaltransmitpoweroftheIoTdevice cycle,T rx ,isgivenby,
consideringtheretransmissionprobabilityinthetransmitting  I
modeasbelow, T rx =  n dtim pe · r I io b d eacon ·t beacon +t ack (DTIM) (14)
P ∗ = argmin[E ] t tri +t ack (TWT),
TX TX
PTX
whereI istheperiodfortransmissiondata,n isthe
(cid:20) d A γ +A (cid:21) period dtim
= Solutionof 1 2 =0 , (10) DTIM value, I beacon is the beacon interval that is broadcast
dP TX log 2 (1+γ) by the AP (typically 100ms), t beacon is the reception time
VOLUME10,2022 61237

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
| FIGURE6. |     | PowerconsumptionoftheIoTdeviceintheeAPsystemmodelwiththeTWTscheme. |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of one beacon message, t is the reception time of one modetimeoftheIoTdeviceinacycle,T ,isgivenby,
|                   |         |      |                               | tri |     |     |     |            |          |        |          | trans    |        |     |
| ----------------- | ------- | ---- | ----------------------------- | --- | --- | --- | --- | ---------- | -------- | ------ | -------- | -------- | ------ | --- |
| triggerframe,andt |         |      | isthereceptiontimeofoneTCPACK |     |     |     |     |            |          |        |          |          |        |     |
|                   |         | a ck |                               |     |     |     |     |  (cid:20) | (cid:18) |        | (cid:19) | (cid:21) |        |     |
| me ss             | a g e . |      |                               |     |     |     |     |            | I pe     | r io d |          |          |        |     |
|                   |         |      |                               |     |     |     |     |          | 2        |        | −1 +α    | ·t       | (DTIM) |     |
|                   |         |      |                               |     |     |     |     |            |          | ·      |          | trans    |        |     |
E a c h R xmodeti m eoftheIoTdeviceinacyclethatuses T = n dtim I b eacon
trans
| thelegacyAPsystemandtheeAPsystemisgivenby, |     |     |     |     |     |     |     | (2+β)·t |     |     |     |     | (TWT), |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | ------ | --- |
trans
(16)
|     |    | I         |     |       |          |        |     |     |     |     |     | (cid:16) |              | (cid:17) |
| --- | --- | --------- | --- | ----- | -------- | ------ | --- | --- | --- | --- | --- | -------- | ------------ | -------- |
|     |     | pe r io d | ·t  | +t Io | T↔server | (DTIM) |     |     |     |     |     |          | I p e r io d | − ·      |
 · beacon a ck w her e th e le f t p a r t o f th e a b o v e e q u a t io n , 2 1
| T A | P = | n dtim I b eacon |     |     |     |     |     |     |     |     |     | n dt | i m ·I b e a co n |     |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----------------- | --- |
r x t , is t he t r a n s i ti o n ti m e f o r b e a c o n r e c ep t io n s w h e n us in g
|     | t  | +tIoT↔server |     |     |     |       | trans                             |     |     |     |     |                        |     |     |
| --- | --- | ------------ | --- | --- | --- | ----- | --------------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- |
|     |     | tri          |     |     |     | (TWT) | theDTIMscheme,andtherightpart,α·t |     |     |     |     |                        |     |     |
|     |     | ack          |     |     |     |       |                                   |     |     |     |     | trans ,isthetransition |     |     |
|     |    | I            |     |     |     |       |                                   |     |     |     |     |                        |     |     |
pe r io d Io T↔eAP t i m e fo r d a t a tr an s m i s s io n , T C P A C K r e c e pt i o n , an d L2 A C K
|      |    |       | ·t  | +t          | (DTIM) |     |     |     |     |     |     |     |     |     |
| ---- | --- | ----- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| e AP | =   | n · I |     | beacon a ck |        |     |     |     | t   |     |     |     |     | α   |
T r x dtim b eacon t r an sm i s si o n . T h e t ra n s i s o n e tr a nsi t i o n t i m e , a nd ( th e
t +tIoT↔eAP (TWT), transientnumberfordatatransmission,TCPACKreception,
tri ack
|     |     |     |     |     |     |     | and | L2 ACK | transmission | in  | a cycle | when using | the | DTIM |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | ------- | ---------- | --- | ---- |
(15)
|     |     |     |     |     |     |     | scheme)                  | is 7 | in our system |     | model assumption,      |     | as shown | in  |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | ---- | ------------- | --- | ---------------------- | --- | -------- | --- |
|     |     |     |     |     |     |     | Fig.5.IntheTWTscheme,2·t |      |               |     | isthetransitiontimefor |     |          |     |
trans
|     |     |     |     |     |     |     | triggerreception,andβ |     |     | ·t  | isthetransitiontimefordata |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | -------------------------- | --- | --- | --- |
where TAP is the receiving time of the IoT device that uses trans
rx
|      |          | TeAP      |        |                |            |            | transmission, |     | TCP ACK                                    | reception, | and | L2 ACK | transmis- |     |
| ---- | -------- | --------- | ------ | -------------- | ---------- | ---------- | ------------- | --- | ------------------------------------------ | ---------- | --- | ------ | --------- | --- |
| the  | legacy   | AP,       | is the | receiving time | of the     | IoT device |               |     |                                            |            |     |        |           |     |
|      |          | rx        |        |                |            |            | sion,andβ     |     | (thetransientnumberfordatatransmission,TCP |            |     |        |           |     |
| that | uses the | prop osed | eAP,   | tIoT↔server    | is the RTT | between    |               |     |                                            |            |     |        |           |     |
ack
|          |            |         |         |            |            |          | ACK                                              | reception, | and L2 | ACK | transmission | in  | a cycle | when |
| -------- | ---------- | ------- | ------- | ---------- | ---------- | -------- | ------------------------------------------------ | ---------- | ------ | --- | ------------ | --- | ------- | ---- |
| the      | IoT device | and     | the TCP | server via | the legacy | AP, and  |                                                  |            |        |     |              |     |         |      |
| tIoT↔eAP |            |         |         |            |            |          | usingtheTWTscheme)is3inoursystemmodelassumption, |            |        |     |              |     |         |      |
|          | is         | the RTT | between | the IoT    | device and | the eAP. |                                                  |            |        |     |              |     |         |      |
| ack      |            |         |         |            |            |          | asshowninFig.6.                                  |            |        |     |              |     |         |      |
Ingeneral,theRxmodetimeforreceivingtheTCPACKin
|     |     |     |     |     |     |     | The | total | sleep mode | time | of the | IoT device | in  | a cycle |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | ---- | ------ | ---------- | --- | ------- |
theeAPsystemmodelissignificantlylessthanthelegacyAP
|     |     |     |     |     |     |     | can | be obtained | by subtracting |     | the Tx | mode | time, | the Rx |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | --- | ------ | ---- | ----- | ------ |
systemmodel.ThisisbecausetIoT↔eAPismuchsmallerthan
a ck
| tIoT↔server      |     |                    |     |         |             |        | modetime,andtotaltransientmodetimefromacycle.The |            |      |        |            |     |          |       |
| ---------------- | --- | ------------------ | --- | ------- | ----------- | ------ | ------------------------------------------------ | ---------- | ---- | ------ | ---------- | --- | -------- | ----- |
|                  |     | and is independent |     | o f the | RTT between | the AP |                                                  |            |      |        |            |     |          |       |
| ack              |     |                    |     |         |             |        | total                                            | sleep mode | time | of the | IoT device | in  | a cycle, | T ,   |
| andtheTCPserver. |     |                    |     |         |             |        |                                                  |            |      |        |            |     |          | Sleep |
isgivenby,
ThetotaltransientmodetimeoftheIoTdeviceinacycle
| is obtained |     | by multiplying |     | by the number | of mode | changes |     |     |     |     |        |     |     |     |
| ----------- | --- | -------------- | --- | ------------- | ------- | ------- | --- | --- | --- | --- | ------ | --- | --- | --- |
|             |     |                |     |               |         |         |     | TAP | = I | −T  | −TAP−T |     |     |     |
andonetransitiontime.Weassumethatallofthetransition sleep period tx rx trans
|     |     |     |     |     |     |     |     | T   | e A P = I | −T  | −T e | AP−T | ,   | (17) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---- | ---- | --- | ---- |
timesintheoperatingmodearethesame.Thetotaltransient s l ee p period tx r x trans
| 61238 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME10,2022 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
whereTAP isthetotalsleepmodetimeofanIoTdevicethat TheenergyconsumptionoftheIoTdeviceduringacycle
usesthe
s
l
le
e
e
g
p
acyAP,andTeAP isthetotalsleepmodetimeof
withtheproposedeAPsystemwiththeTWTscheme,EeAP,T,
sleep cycle
anIoTdevicethatusestheproposedeAP. whichisgivenby,
Usingtheaboveequations,theenergyconsumptionofthe EeAP,T = P adaptive·T +P ·TeAP
IoT device during a cycle in the legacy AP system with the cycle tx tx rx rx
DTIMscheme,E c A y P cl , e D,whichisgivenby, +P sleep ·T s e l A ee P p +P trans ·T trans
P +P (cid:20) (1+p )N N (cid:21)
E c A y P cl , e D = Ps tx tatic·T tx +P rx ·T r A x P = I L Nγ∗· Blog ( e 1+ da γ ta ) + Blog L ( 2 1 ac + k γ)
2 2
+P sleep ·T s A le P ep +P trans ·T trans +P · (cid:16) t +tIoT↔eAP (cid:17)
(cid:20) (1+p )N N (cid:21) rx tri ack
= Ps tx tatic· Blog ( e 1+ da γ ta ) + Blog L ( 2 1 ac + k γ) +P sleep ·(I period −T tx −T r e x AP−T trans )
2 2
(cid:18) I (cid:19) +P trans ·[(2+β)·t trans ]. (19b)
+P · period ·t +tIoT↔server
rx n dtim ·I beacon beacon ack Usingtheaboveequations,theenergyconsumptionofthe
+P ·(I −T −TAP−T ) IoTdeviceduring1secondinthelegacyAPsystem,EAP,and
sleep period tx rx trans IoT
(cid:20) (cid:18) I (cid:19) (cid:21) theenergyconsumptionoftheIoTdeviceduring1secondin
+P trans · 2 n dtim pe · r I io b d eacon −1 +a ·t trans , theproposedAPsystem,E I e o A T P,aregivenby,
(18a)   E
c
A
y
P
cl
,
e
D·
I
1 (DTIM)
wherePstaticisthestatictransmittingpoweroftheIoTdevice, EAP = period
whichh t a x safixedvalue,P
rx
istheoperationalpowerofthe IoT  E
c
A
y
P
cl
,
e
T ·
I
1 (TWT)
Rxmode,P istheoperationalpowerofthesleepmode, period
andP trans is s t le h e e p operationalpowerofthetransitionmode.   E
c
e
y
A
c
P
le
,D·
I
1 (DTIM)
TheenergyconsumptionoftheIoTdeviceduringacycle EeAP = period (20)
inthelegacyAPsystemwiththeTWTscheme,E
c
A
y
P
cl
,
e
T,which IoT  E
c
e
y
A
c
P
le
,T ·
I
1 (TWT).
isgivenby, period
EAP,T = Pstatic·T +P ·TAP C. ENERGY-SAVINGGAINBYeAP
cycle tx tx rx rx
+P ·TAP +P ·T
Theenergy-savinggain(G)usingtheproposedeAPsystem
sleep sleep trans trans modelcanbedefinedas,
(cid:20) (1+p )N N (cid:21)
= Pstatic· e data + L2ack E −E
tx Blog (1+γ) Blog (1+γ) G(cid:44) legacy proposed, (21)
2 2
(cid:16) (cid:17) E legacy
+P · t +tIoT↔server
rx tri ack where E is the energy consumption of the IoT device
legacy
+P ·(I −T −TAP−T ) usingthelegacyAPsystemmodel,andE istheenergy
sleep period tx rx trans proposed
+P ·[(2+β)·t ], (18b) consumptionoftheIoTdeviceusingtheproposedeAPsys-
trans trans
tem model. The energy-saving gain, G, using the proposed
We can also obtain the energy consumption of the IoT eAPconsistsoftwocomponents,G ,andG .
1 2
deviceduringacyclewiththeproposedeAPsystemwiththe Firstly,G isobtainedenergy-savinggainmainlyfromthe
1
DTIMscheme,EeAP,D,whichisgivenby,
prompt TCP ACK transmit function in the proposed eAP
cycle
system model, and this G is defined as below based on
E c e y A c P le ,D = P a tx daptive·T tx +P rx ·T r e x AP equation(20), 1
= + P I P + sle P ep N · γ T ∗ s e l A e · e P (cid:20) p ( + 1+ P tr p an e s )N · d T a t t r a an + s N L2ack (cid:21) G 1 (cid:44) E I A o P T E − I A o P T E I e o A T P , (22)
L Blog (1+γ) Blog (1+γ)
2 2 where G is obtained by decreasing the Rx mode time and
(cid:18) I (cid:19) 1
+P · period ·t +tIoT↔eAP increasing the sleep mode time of the IoT device using the
rx n dtim ·I beacon beacon ack promptTCPACKtransmitfunctionintheeAPsystemmodel.
+P ·(I −T −TeAP−T ) Secondly, G is obtained by transferring the retransmis-
sleep period tx rx trans 2
(cid:20) (cid:18) I (cid:19) (cid:21) sion burden of the TCP timer timeout to the eAP using
+P · 2 period −1 +a ·t ,
trans n ·I trans the caching IoT data retransmit function in the eAP system
dtim beacon
model. Thus, an IoT device using the eAP system has no
(19a)
retransmissionburdenduetotheTCPtimertimeout,andonly
adaptive
whereP istheadaptivetransmittingpoweroftheIoT hasaretransmissionburdenforwirelesslinkfailuresbetween
tx
device which has a flexible value controlled by the target the IoT device and the eAP. When the TCP timer timeout
SINRγ∗. occurs, the eAP retransmits the cached IoT measured data
VOLUME10,2022 61239

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
to the TCP server without requesting retransmission to the TABLE1. Simulationparameters.
| IoTdevice.G | isobtainedbythecachingIoTdataretransmit |     |     |     |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
2
| functionintheeAP,andthisG |     | isdefinedasbelowbasedon |     |     |     |     |     |
| ------------------------- | --- | ----------------------- | --- | --- | --- | --- | --- |
2
equation(20),
|     | (1+p | )EeAP−EeAP |     |     |     |     |     |
| --- | ---- | ---------- | --- | --- | --- | --- | --- |
timeout
|     | G (cid:44) | IoT        | IoT , | (23) |     |     |     |
| --- | ---------- | ---------- | ----- | ---- | --- | --- | --- |
|     | 2          | (1+p )EeAP |       |      |     |     |     |
timeout
IoT
| wherep     | timeout istheprobabilityofTCPtimertimeoutcaused |                  |                 |     |     |     |     |
| ---------- | ----------------------------------------------- | ---------------- | --------------- | --- | --- | --- | --- |
| by network | congestion                                      | or missing data. | The probability | of  |     |     |     |
TCPtimertimeoutisaffectedbythenumberofTCPconnec-
| tions, buffer | capacity, | TCP timer timeout | value, packet | loss |     |     |     |
| ------------- | --------- | ----------------- | ------------- | ---- | --- | --- | --- |
probability,etc.Ingeneral,whenthenumberofTCPconnec-
tionsis100,theprobabilityoftheTCPtimertimeoutoccur-
| ring is   | almost 2% to 5%         | empirically. | Using equations | (22) |     |     |     |
| --------- | ----------------------- | ------------ | --------------- | ---- | --- | --- | --- |
| and (23), | the total energy-saving | gain         | by the proposed | eAP  |     |     |     |
| system,G  | ,isgivenby,             |              |                 |      |     |     |     |
total
|     | =         | ∪G ∼ =G          |         |      |     |     |     |
| --- | --------- | ---------------- | ------- | ---- | --- | --- | --- |
|     | G total G | 1 2 1∪2          |         |      |     |     |     |
|     | (1+p      | )EAP             | −EeAP   |      |     |     |     |
|     | =         | timeout          | IoT IoT |      |     |     |     |
|     |           | (1+p             | )EAP    |      |     |     |     |
|     |           | timeout          | IoT     |      |     |     |     |
|     | EAP       | − 1              | ·EeAP   |      |     |     |     |
|     |           | IoT (1+ptimeout) | IoT     |      |     |     |     |
|     | =         |                  | ,       | (24) |     |     |     |
EAP
IoT
| whereG | 1∪2 isthecombinedgainobtainedfromtheprompt |     |     |     |     |     |     |
| ------ | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
TCPACKtransmitfunctionandthecaching-and-retransmit
| functionintheeAPsystemmodel.G |     |     | 1 andG 2 arenotmutu- |     |     |     |     |
| ----------------------------- | --- | --- | -------------------- | --- | --- | --- | --- |
allyexclusivebecausetheyhaveanintersectionbetweenG
1
| and G | . Therefore, we | should consider | the combined | gain |     |     |     |
| ----- | --------------- | --------------- | ------------ | ---- | --- | --- | --- |
2
| with G | and G based | on equation | (21) by considering | the |     |     |     |
| ------ | ----------- | ----------- | ------------------- | --- | --- | --- | --- |
| 1      | 2           |             |                     |     |     |     |     |
TCPtimertimeoutprobabilityforthecalculationofG . anda6-bytePHYheaderinanIoTpacket.TheIoTpackets
total
2.4GHz
We do not consider the gain from the multiple IoT data are transmitted to the AP in a channel band of the
aggregate function in the eAP. Because they are related to IEEE 802.11ax network with static or adaptive transmitting
| the energy-saving | of  | eAPs, not the | energy-saving | of IoT       |              |                   |                |
| ----------------- | --- | ------------- | ------------- | ------------ | ------------ | ----------------- | -------------- |
|                   |     |               |               | power. It is | also assumed | that the measured | power of noise |
devices. In addition, the gain from the optimal operating andinterferenceis−90dBmintheAP[31].Asachannelfad-
parameters of IoT devices according the patient’s level by ingmodel,weusea‘‘Ricianfadingmodel’’,whichhasboth
EeAP
the eAP is considered by the value, in equation (22), non-lineofsight(NLOS)andlineofsight(LOS)paths,com-
IoT
whichistheenergyconsumptionoftheIoTdeviceusingthe monly used in indoor environments [35]. The transmission
eAP.Therefore,thetotalenergy-savinggainforthepatient’s periodofIoTpacketsrangedfrom0.9secondsto60seconds,
and0.9secondsindicatesamultipleoftheDTIMof300ms,
leveldependsonthevalueoftheoperatingparametersofIoT
| devices. |     |     |     | whichisadefaultvalueofDTIM[36],asshowninFig.4and |     |     |     |
| -------- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
Fig.5.TheDTIMvaluerangedfrom1to10,andthetarget
V. PERFORMANCEEVALUATION SINRrangedfrom30dBmto40dBm,whicharecommonly
A. PARAMETERSFORANALYSISANDSIMULATION used in the empirical fields of IEEE 802.11 networks [37].
In this section, we present a performance evaluation of the Wealsoaddedsimulationresultsfortheenergyconsumption
proposed eAP system model compared with the legacy AP of IoT devices using the TWT scheme as an optional case.
systemmodel.WedevelopaWLANsimulatorusingPython The contention window size ranged from 16 (slot times) to
for the proposed eAP system and the legacy AP system. 256 (slot times), and the default value was 64 (slot times).
Specifically, we consider a wireless health monitoring IoT The contention window size doubles when a collision of
serviceforpatientsinahospitalasacasestudy. transmission data occurs. The number of IoT devices on an
We assume that 10 IoT devices communicate on an AP, AP ranged from 1 to 30, and we assumed the default value
andeachIoTdevicegenerates64bytesofdataeverysecond was10onanAP.Itwasalsoassumedthattherewereatotal
at a constant bit rate (CBR), and that the IoT device has no of100APsinahospitalbuilding.WealsoassumedtheTCP
mobility.TheAPcoverageradiusis20mandthelocationof ACK frame generation time in the eAP is less than 10µs.
the IoT device is random. The generated traffic is buffered We considered saturated network scenarios in our system
andforwardedtoaTCPpayloadofupto1460byteswitha modelbyconsideringbackgroundtrafficsuchasWi-Fitraffic
40-byteTCP/IPheader,a30-byteIEEE802.11MACheader, fromsmartphones,laptops,tablets,andetc.
| 61240 |     |     |     |     |     |     | VOLUME10,2022 |
| ----- | --- | --- | --- | --- | --- | --- | ------------- |

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
| It was | assumed that | a patient | level 1 (mild) | sensor | has |     |     |     |     |
| ------ | ------------ | --------- | -------------- | ------ | --- | --- | --- | --- | --- |
60secondsoftransmissionperiodforIoTpackets,10forthe
DTIMvalue,and30dBforthetargetSINR.Also,thepatient
| level 2 (severe) | sensor     | was assumed  | to have   | 10 seconds | of     |     |     |     |     |
| ---------------- | ---------- | ------------ | --------- | ---------- | ------ | --- | --- | --- | --- |
| transmission     | period for | IoT packets, | 5 for the | DTIM       | value, |     |     |     |     |
and32dBforthetargetSINR.Finally,thepatientlevel3(crit-
ical)sensorwasassumedtohave0.9secondsoftransmission
periodforIoTpackets,3fortheDTIMvalue,and34dBfor
thetargetSINR,respectively.
Thesimulationresultswereaveragedover100iterations.
Table1liststhedetailedparametersbasedon[23],[31],[38].
B. ENERGYCONSUMPTIONOFTHEIoTDEVICE
TheIoTdeviceaccumulatesthemeasureddatainthebuffer
andtransmitsittotheAPinavariabledatasizedIoTpacket.
DuetothehighdatatransmissionrateoftheWi-Finetwork, FIGURE7. EnergyconsumptionoftheIoTdeviceaccordingtothe
the transmission time of IoT packets is very short, and the transmissionperiod.
energyconsumedbytheIoTdeviceisalsoinsignificantwhen
transmittingIoTpackets.Ontheotherhand,whenthenumber
oftransmissionsincreases,theenergyconsumptionoftheIoT
deviceincreasesbecauseoftheincreasinglisteningtimesfor
receptionsoftheTCPACK.
Fig.7presentstheenergyconsumptionoftheIoTdevice
| using different | two AP    | system models  | with   | three different |     |     |     |     |     |
| --------------- | --------- | -------------- | ------ | --------------- | --- | --- | --- | --- | --- |
| DTIM values     | according | to the changes | in the | transmission    |     |     |     |     |     |
periodoftheIoTpackets.Inbothsystemmodels,theenergy
consumptionoftheIoTdevicedecreasesasthetransmission
periodvalueincreases.Asthetransmissionperiodincreases,
thedatasizeoftheIoTpacketstransmittedatonceincreases,
| and the | number of transmissions |     | decreases | within | a cer- |     |     |     |     |
| ------- | ----------------------- | --- | --------- | ------ | ------ | --- | --- | --- | --- |
tainperiod(whichmeansthattransmissionoccurssparsely),
sotheenergyconsumptionoftheIoTdevicealsodecreases.
| Furthermore,  | when the    | transmission | period | increases, | TCP      |                                                   |     |     |     |
| ------------- | ----------- | ------------ | ------ | ---------- | -------- | ------------------------------------------------- | --- | --- | --- |
| ACK reception | also occurs | sparsely,    | so the | effect     | on the   |                                                   |     |     |     |
|               |             |              |        |            | FIGURE8. | EnergyconsumptionratiooftheIoTdevicebyusingtheeAP |     |     |     |
energy consumption of the IoT device by using the eAP accordingtothetransmissionperiod.
decreases,becausetherearerelativelyfeweropportunities.
| Fig. 8 | presents the energy | consumption | ratio | of the | IoT |     |     |     |     |
| ------ | ------------------- | ----------- | ----- | ------ | --- | --- | --- | --- | --- |
deviceusingtheeAPcomparedtothecaseoftheIoTdevice
|     |     |     |     |     | On the other | hand, as | the DTIM value | increases, | the effect |
| --- | --- | --- | --- | --- | ------------ | -------- | -------------- | ---------- | ---------- |
using the legacy AP, according to the changes in the trans- ontheenergyconsumptionoftheIoTdeviceusingtheeAP
mission period of IoT packets. Fig. 8 shows that the energy increases.WhentheDTIMvalueincreases,theenergycon-
consumptionratiooftheIoTdeviceusingtheeAPincreases sumption portion for transmitting the IoT packet, receiving
sharplywhenthetransmissionperiodincreases.Forexample, theTCPACKreception,andsleepintheIoTdeviceismore
for the eAP with a DTIM value of 3, the energy consump- significant than the energy consumption portion for beacon
|     | 8.9% |     | 81.8% |     |     |     |     |     |     |
| --- | ---- | --- | ----- | --- | --- | --- | --- | --- | --- |
tion ratio is (the best case), (the worst case) reception,sotheeffectivenessoftheeAPusageisrelatively
| whenthetransmissionperiodis0.9seconds,and60seconds, |     |     |     |     | increased. |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
respectively.ThatmeanstheproposedeAPsystemmodelhas Fig. 10 presents the energy consumption ratio of the IoT
abetterenergy-savingeffectwhenIoTdeviceusesashorter device using the eAP compared to the IoT device using the
transmissionperiod. legacyAPintermsofchangesinDTIMvalue.Fig.10shows
Fig.9presentstheenergyconsumptionoftheIoTdevice thattheenergyconsumptionratiooftheIoTdeviceusingthe
using different two AP system models with three different eAP decreases gradually as the DTIM value increases. For
transmission period values, in terms of changes in DTIM example, in the case of eAP with a transmission period of
value.Inbothsystemmodels,theenergyconsumptionofthe 0.9seconds,theenergyconsumptionratiowas16.05%(the
IoT device decreases as the DTIM value increases. As the worstcase),6.09%(thebestcase)whentheDTIMvaluewas
DTIMvalueincreases,thenumberofawakeningsforbeacon 1and10,respectively.
reception in the Rx mode of the IoT device decreases, and Ontheotherhand,Fig.8andFig.10showthattheeAPsys-
thustheenergyconsumptionoftheIoTdevicealsodecreases. temmodelwasmoreaffectedbythechangesintransmission
| VOLUME10,2022 |     |     |     |     |     |     |     |     | 61241 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
FIGURE9. EnergyconsumptionoftheIoTdeviceaccordingtotheDTIM FIGURE11. EnergyconsumptionoftheIoTdeviceaccordingtothetarget
value. SINRvaluewiththefollowingparameters:thetransmissionperiodofIoT
packets=0.9s,theDTIMvalue=3.
FIGURE10. EnergyconsumptionratiooftheIoTdevicebyusingtheeAP
FIGURE12. EnergyconsumptionratiooftheIoTdevicebyusingtheeAP
accordingtotheDTIMvalue.
accordingtothetargetSINRvalue.
period than DTIM values for the energy efficiency of the Fig. 12 shows the energy consumption ratio of the IoT
IoT device. Therefore, to optimize the energy consumption device with the eAP compared to the static transmitting
of the IoT device, it is more important to find the optimal powered IoT device with the legacy AP, according to the
transmissionperiodvaluethantheoptimalDTIMvalue. targetSINRvalues.InFig.12,theenergyconsumptionratio
Fig.11presentstheenergyconsumptionoftheIoTdevice of the adaptive transmitting powered IoT device with the
using different AP system models with static transmitting eAP increases gradually as the target SINR increases. For
powerandadaptivetransmittingpoweraccordingtothetar- example, for the adaptive transmitting powered IoT device
get SINR values. With static transmitting power, the IoT using eAP with a transmission period of 0.9 seconds and a
devicetransmitsafixedTxpowerofapredeterminedsignal DTIM value of 3, the energy consumption ratio is 11.79%
strength regardless of noise and interference channel condi- (the best case) ∼ 23.4% (the worst case), and the energy
tions.Therefore,asshowninFig.11,thestatictransmitting consumption ratio is 73.48% (the best case) ∼ 74.7% (the
poweredIoTdeviceusingthelegacyAPhasaconstantenergy worstcase)whenthetransmissionperiodis60secondsand
consumption value of about 6.4∗10−3joules regardless of theDTIMvalueis10.
the change in value of the target SINR. On the other hand, Fig. 13 presents the collision probability of transmission
fortheIoTdevicewithadaptivetransmitting,powerdepends data according to the number of IoT devices on an AP and
onthecurrentchannelSINRconditionandthepatient’slevel, the contention window size. It shows that as the number of
and the energy consumption increases as the target SINR IoT devices communicating with the AP increases, and the
valueincreases. contention window size decreases, the collision probability
61242 VOLUME10,2022

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
FIGURE13. CollisionprobabilityaccordingtothenumberofIoTdevices FIGURE15. EnergyconsumptionoftheIoTdeviceaccordingtothe
| onanAPandthecontentionwindowsize. |     |     |     | patient’slevel. |                 |          |       |         |           |
| --------------------------------- | --- | --- | --- | --------------- | --------------- | -------- | ----- | ------- | --------- |
|                                   |     |     |     | patient’s       | level are shown | in Table | 1. We | assumed | that mild |
patientscouldacceptdelaysresultingfrominfrequenttrans-
mission,andlowertransmissionpowerthancriticalpatients.
Fig.15presentstheenergyconsumptionoftheIoTdevice
|     |     |     |     | based on | the patient’s | level. It | shows | that the | IoT device |
| --- | --- | --- | --- | -------- | ------------- | --------- | ----- | -------- | ---------- |
consumedmoreenergywithhigherpatientlevelsbecauseof
|     |     |     |     | the more   | frequent transmission |            | and higher | Tx   | power. The |
| --- | --- | --- | --- | ---------- | --------------------- | ---------- | ---------- | ---- | ---------- |
|     |     |     |     | IoT device | using the             | eAP system | consumed   | only | 1/3 to     |
1/9theenergyoftheIoTdeviceusingthelegacyAPsystem.
|     |     |     |     | In particular, | the energy | consumed | by the     | IoT device | using   |
| --- | --- | --- | --- | -------------- | ---------- | -------- | ---------- | ---------- | ------- |
|     |     |     |     | the proposed   | eAP system | was      | reduced to | 36.92%,    | 30.89%, |
and11.90%comparedtotheIoTdeviceusingthelegacyAP
systemforpatientlevel1,patientlevel2,andpatientlevel3,
respectively,asshowninFig.15andFig.16b.
FIGURE14. EnergyconsumptionoftheIoTdeviceaccordingtothe Assumingthat1,000IoTdevicesareneededforIoTser-
collisionprobabilitywiththefollowingparameters:thetransmission
|     |     |     |     | vices in | a hospital and | the ratio | of the | number | of patients |
| --- | --- | --- | --- | -------- | -------------- | --------- | ------ | ------ | ----------- |
periodofIoTpackets=0.9s,theDTIMvalue=3.
|            |                  |                        |           | for each      | level is 7:2:1, | the total | energy             | consumption | of IoT  |
| ---------- | ---------------- | ---------------------- | --------- | ------------- | --------------- | --------- | ------------------ | ----------- | ------- |
|            |                  |                        |           | devices using | the eAP         | system is | only 0.3108joules. |             | This is |
| increases. | As the collision | probability increases, | the prob- |               |                 |           |                    |             |         |
lessthanaquarterofthetotalenergyconsumedbythelegacy
APsystemmodel,whichrequired1.3142joules.
| ability of | IoT data retransmission | increases, | so the energy |     |     |     |     |     |     |
| ---------- | ----------------------- | ---------- | ------------- | --- | --- | --- | --- | --- | --- |
consumptionoftheIoTdevicealsoincreases,buttheamount Fig. 16 presents the portion of energy consumed by the
isveryinsignificant.
IoTdeviceusingthelegacyAPsystemandtheproposedeAP
Inaddition,theenergyconsumptionratiooftheIoTdevice system model according to the patient’s level. In the legacy
with the eAP system model is not significantly affected APsystem,theportionofenergyconsumedfortheTCPACK
because the portion of energy consumed by retransmission receptionisverylarge,thatisalmost12%∼80%according
is tiny, as shown in Fig. 14. It is almost 10% compared to to the patient’s level in Fig. 16a. On the other hand, the
thelegacyAPsystemmodelwhenthetransmissionperiodis
|     |     |     |     | portion of | energy consumed | for | TCP ACKreception |     | by the |
| --- | --- | --- | --- | ---------- | --------------- | --- | ---------------- | --- | ------ |
0.9s,andtheDTIMvalueis3.
IoTdeviceusingtheeAPwasdramaticallyreducedto1%∼
|     |     |     |     | 22% compared | the IoT | device | using the | legacy | AP system |
| --- | --- | --- | --- | ------------ | ------- | ------ | --------- | ------ | --------- |
C. ENERGY-SAVINGGAINANDEXPECTEDLIFETIME accordingtothepatient’slevelinFig.16b.Inaddition,wecan
In the introduction section, we presented a service scenario see that the portion of energy consumed for the sleep mode
in which the energy consumption of the IoT device varies bytheIoTdeviceusingtheeAPwasincreasedcomparedto
according to the patient’s level by controlling operating theIoTdeviceusingthelegacyAPsystem,becausethesleep
parameters,suchasthetransmissionperiodoftheIoTpack- opportunity increased due to the reduced reception time for
ets, the DTIM value, and the transmitting power. We con- theTCPACKinFig.16b.
sideredthreepatientlevelsbasedonthepatient’sconditions; The energy-saving gain of the IoT device that uses the
theoperatingparametersoftheIoTsensoraccordingtoeach eAP system model is defined in equation (24). The higher
| VOLUME10,2022 |     |     |     |     |     |     |     |     | 61243 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
FIGURE16. PortionofenergyconsumedbytheIoTdeviceusingthelegacyAPsystemandtheeAPsystemaccordingtothepatient’slevel.
TABLE2. Energy-savinggainoftheIoTdeviceaccordingtopatient’slevel.
the patient’s level, the greater the energy consumed by the
IoTdeviceduetofrequentdatatransmissions,andthegreater
the energy-saving gain by the eAP system model. The total
energy-saving gain, G , of the IoT device according to
total
patient’slevelsisgiveninTable2.G is63.81%,69.71%,
total
and 88.34% for patient level 1, patient level 2, and patient
FIGURE17. ExpectedlifetimeoftheIoTdeviceaccordingtothepatient’s
level3,respectively. level.
Fig. 17 presents the expected lifetime of the IoT device
accordingtothepatient’slevel.AssumingthattheIoTdevice
ispoweredby3V and120mAhbatteries,theexpectedlife-
achievesa2.7times,3.2times,and8.4timesimprovementin
time of the IoT device with the legacy AP system model theexpectedIoTdevicelifetimecomparedtothelegacyAP
is 566 hours, 317 hours, and 56 hours for patient level 1, systemmodelforpatientlevel1,2,and3,respectively.
patientlevel2,andpatientlevel3,respectively.Ontheother
hand, the expected lifetime of the IoT device with the pro- D. ROUND-TRIPDELAY
posed eAP system model is 1533 hours, 1028 hours, and Round-tripdelay(RTD)istheelapsedtimebetweenwhenthe
471 hours for patient level 1, patient level 2, and patient IoTdevicetransmitsadatapacketandreceivesitsACK.This
level 3, respectively. That means the eAP system model time delay includes processing delay, transmission delay,
61244 VOLUME10,2022

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
FIGURE18. Round-tripdelayoftheIoTpacketsaccordingthenumberof FIGURE20. Round-tripdelayoftheIoTpacketsaccordingthenumberof
IoTdevicesonanAP. IoTdevicesusingtheenergy-consciousAP.
FIGURE19. Round-tripdelayoftheIoTpacketsaccordingthenumberof FIGURE21. EnergyconsumptionoftheIoTdeviceaccordingtothe
IoTdevicesusingthelegacyAP. transmissionperiod(includingtheTWTscheme).
andpropagationdelaybetweenthetwocommunicatingend- APincreasesandthevalueofcontentwindowsizedecreases,
points.Thetransmissiondelayisaserializationdelaycaused the collision probability of the IoT packet increases, and
by the transmission packet’s length and the data rate of the the probability of retransmission increases. As a result, the
link.Inthesimulation,weassumedthedatapacketlengthwas averageRTDvalueincreasesslightly.
104bytes(a64-bytepayloadplusa40-byteTCP/IPheader).
Also, we considered retransmission due to data packet col- E. EVALUATIONWITHTHETWTSCHEME
lisions. The IoT device receives TCP ACKs from the TCP Asafurtherevaluation,wesimulatedtheenergyconsumption
server via several routing nodes in the legacy AP system oftheIoTdeviceusingtheTWTschemeinsteadoftheDTIM
model.Ontheotherhand,theIoTdevicereceivesTCPACKs scheme.TheTWTschemeislessappropriateforthehealth
directly from the eAP without going through any routing monitoring service because it has shortcomings of lack of
nodes,andtheTCPserverintheeAPsystemmodel. timelinessandlongdownlinkdelays.Nevertheless,theTWT
Fig. 18 presents the average round-trip delay of the IoT schemecanreducefurthertheenergyconsumptionoftheIoT
packets according to the number of IoT devices on an AP. devicecomparedtotheDTIMscheme,becauseitreducesthe
ItcanbeseenthattheaverageRTDsintheeAPsystemmodel consumedenergyforbeaconreceptions.
areverylow,around2∼3milliseconds,comparedtoaverage Fig. 21 shows the energy consumption of the IoT device
RTDsinthelegacyAPsystemmodel. using different two AP system models with three different
In Fig. 19 and Fig. 20, the average RTDs are zoomed-in DTIM values and with the TWT scheme according to the
and shown for the legacy AP system and the eAP system changes in the transmission period of the IoT packets. the
models, respectively. As the number of IoT devices on the energyconsumptionoftheIoTdevicewiththeTWTscheme
VOLUME10,2022 61245

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
respectively.Ontheotherhand,theexpectedlifetimeofthe
|     |     |     |     | IoT device    | with  | the      | proposed | eAP system |        | model   | with the |
| --- | --- | --- | --- | ------------- | ----- | -------- | -------- | ---------- | ------ | ------- | -------- |
|     |     |     |     | TWT scheme    |       | is 2268  | hours,   | 1819       | hours, | and 705 | hours,   |
|     |     |     |     | for patient   | level | 1,       | patient  | level 2,   | and    | patient | level 3, |
|     |     |     |     | respectively. | That  | means    | the      | eAP system |        | model   | with the |
|     |     |     |     | TWT scheme    |       | achieves | 3.5      | times, 4.9 | times, | and     | 12 times |
improvementintheexpectedIoTdevicelifetimecomparedto
thelegacyAPsystemmodelwiththeTWTschemeforpatient
level1,2,and3,respectively.Althoughthereisameaningful
improvementcomparedtotheabsenceoftheTWTscheme,
|     |     |     |     | as mentioned | earlier, |     | the TWT | scheme | is  | less appropriate |     |
| --- | --- | --- | --- | ------------ | -------- | --- | ------- | ------ | --- | ---------------- | --- |
forthehealthmonitoringservice,duetotheshortcomingsof
timelinessanddownlinkdelaywhicharetheessentialfactors
toprovidereliableIoThealthcareservices.However,theeAP
systemwiththeTWTschemecanbeanexcellentlow-energy-
FIGURE22. EnergyconsumptionoftheIoTdeviceaccordingtothe consumption solution for providing latency-insensitive ser-
patient’slevel(includingtheTWTscheme). vicessuchasthermostatservices.
VI. CONCLUSION
|     |     |     |     | This work | proposed |     | a novel | energy-conscious |     | AP  | (eAP) |
| --- | --- | --- | --- | --------- | -------- | --- | ------- | ---------------- | --- | --- | ----- |
systemmodelwithcross-layerdesigntoimprovetheenergy
|     |     |     |     | efficiency | of IoT | devices | in  | Wi-Fi networks. |     | The | proposed |
| --- | --- | --- | --- | ---------- | ------ | ------- | --- | --------------- | --- | --- | -------- |
eAPsystemmodelsignificantlyreducestheenergyconsumed
|     |     |     |     | by the IoT | device | by  | reducing | TCP | ACK | reception | time. |
| --- | --- | --- | --- | ---------- | ------ | --- | -------- | --- | --- | --------- | ----- |
Toachievethis,threenewlydefinedfunctionsandthedevice
|     |     |     |     | energy | management |     | module | were developed |     | with | a local |
| --- | --- | --- | --- | ------ | ---------- | --- | ------ | -------------- | --- | ---- | ------- |
cacheintheeAPoftheIoTdevice.Thedeviceenergyman-
agementmoduleoptimallycontrolsoperatingparametersof
IoTdevices,suchasthetransmissionperiodofIoTpackets,
theDTIMvalue,andthetransmittingpoweroftheIoTdevice,
accordingtothepatient’slevelinreal-timehealthmonitoring
|     |     |     |     | IoT service | scenario. |            | Also,       | the optimal | transmit |         | power of |
| --- | --- | --- | --- | ----------- | --------- | ---------- | ----------- | ----------- | -------- | ------- | -------- |
|     |     |     |     | the IoT     | device,   | the energy | consumption |             | of       | the IoT | device,  |
eAP
FIGURE23. ExpectedlifetimeoftheIoTdeviceaccordingtothepatient’s and the energy-saving gain with the were analyzed
level(includingtheTWTscheme).
|     |     |     |     | for increasing |     | the energy | efficiency |     | of IoT | devices | using a |
| --- | --- | --- | --- | -------------- | --- | ---------- | ---------- | --- | ------ | ------- | ------- |
numericalmethod.Throughextensivesimulations,wefound
|     |     |     |     | that the | proposed | eAP | system | model | achieved | a maximum |     |
| --- | --- | --- | --- | -------- | -------- | --- | ------ | ----- | -------- | --------- | --- |
shows slightly better performance compared to the DTIM of approximately 88% improvement in IoT device energy
scheme, as the IoT device with the TWT scheme consumes efficiency, and increased the expected lifetime of the IoT
littleenergytoreceivetriggerssparsely. devicebyalmost8.4timescomparedtothelegacyAPsystem
Fig. 22 shows the energy consumption of the IoT device model.Inaddition,theaverageround-tripdelayofIoTdata
basedonthepatient’slevel.InFig.22,theenergyconsump-
packetswasalsoimprovedbyalmost90%intheeAPsystem
tionoftheIoTdevicewiththeTWTschemeshowsslightly
model.
| better performance | compared        | to the IoT device | without the |     |     |     |     |     |     |     |     |
| ------------------ | --------------- | ----------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| TWT scheme.        | This is because | the IoT device    | with TWT    |     |     |     |     |     |     |     |     |
REFERENCES
schemecansaveenergyconsumptionforreceivingnumerous
beacons.However,asmentionedearlier,theTWTschemeis [1] M.NurchisandB.Bellalta,‘‘Targetwaketime:ScheduledaccessinIEEE
802.11axWLANs,’’IEEEWirelessCommun.,vol.26,no.2,pp.142–150,
| less appropriate | for the health | monitoring service, | because |     |     |     |     |     |     |     |     |
| ---------------- | -------------- | ------------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Mar.2019.
ofthedisadvantagesoflackoftimelinessandlongdownlink [2] H. Yang, D.-J. Deng, and K.-C. Chen, ‘‘On energy saving in IEEE
| delays. |                       |             |                | 802.11ax,’’IEEEAccess,vol.6,pp.47546–47556,2018. |      |              |     |          |        |              |     |
| ------- | --------------------- | ----------- | -------------- | ------------------------------------------------ | ---- | ------------ | --- | -------- | ------ | ------------ | --- |
|         |                       |             |                | [3] D. P.                                        | Van, | B. P. Rimal, | J.  | Chen, P. | Monti, | L. Wosinska, | and |
| Fig. 23 | presents the expected | lifetime of | the IoT device |                                                  |      |              |     |          |        |              |     |
M.Maier,‘‘Power-savingmethodsforInternetofThingsoverconverged
accordingtothepatient’slevel.AssumingthattheIoTdevice
fiber-wirelessaccessnetworks,’’IEEECommun.Mag.,vol.54,no.11,
is powered by 3 V and 120 mAh batteries, the expected pp.166–175,Nov.2016.
lifetimeoftheIoTdevicewiththelegacyAPsystemmodel [4] J. Wan, M. A. A. H. Al-awlaqi, M. Li, M. O’Grady, X. Gu, J. Wang,
|     |     |     |     | and | N. Cao, | ‘‘Wearable | IoT enabled | real-time | health | monitoring | sys- |
| --- | --- | --- | --- | --- | ------- | ---------- | ----------- | --------- | ------ | ---------- | ---- |
withtheTWTschemeis642hours,367hours,and58hours,
tem,’’EURASIPJ.WirelessCommun.Netw.,vol.2018,no.1,pp.1–10,
| for patient | level 1, patient | level 2, and | patient level 3, | Dec.2018. |     |     |     |     |     |               |     |
| ----------- | ---------------- | ------------ | ---------------- | --------- | --- | --- | --- | --- | --- | ------------- | --- |
| 61246       |                  |              |                  |           |     |     |     |     |     | VOLUME10,2022 |     |

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
[5] M.A.Hanson,H.C.Powell,andA.T.Barth,‘‘Bodyareasensornetworks: [29] T. Poongodi, A. Rathee, R. Indrakumari, and P. Suresh, ‘‘IoT sensing
Challengesandopportunities,’’Computer,vol.42,no.1,pp.58–65,2009. capabilities: Sensor deployment and node discovery, wearable sensors,
[6] S.D.Mamdiwar,R.Akshith,Z.Shakruwala,U.Chadha,K.Srinivasan,and wirelessbodyareanetwork(WBAN),dataacquisition,’’inPrinciplesof
C.Y.Chang,‘‘RecentadvancesonIoT-assistedwearablesensorsystems InternetofThings(IoT)Ecosystem:InsightParadigm.Berlin,Germany:
forhealthcaremonitoring,’’Biosensors,vol.11,no.10,p.372,2021. Springer,2020,pp.127–151,doi:10.1007/978-3-030-33596-0_5.
[30] A.Al-Hourani,S.Kandeepan,andE.Hossain,‘‘Relay-assisteddevice-
| [7] M. Poongodi, | A.  | Sharma, M. | Hamdi, M. Maode, | and | N. Chilamkurti, |     |     |     |     |     |     |     |
| ---------------- | --- | ---------- | ---------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
‘‘Smart healthcare in smart cities: Wireless patient monitoring system to-devicecommunication:Astochasticanalysisofenergysaving,’’IEEE
usingIoT,’’J.Supercomput.,vol.77,no.11,pp.12230–12255,Nov.2021. Trans.MobileComput.,vol.15,no.12,pp.3129–3141,Dec.2016.
[8] M.A.Akkai,R.Sokullu,andH.E.Çetin,‘‘Healthcareandpatientmoni- [31] B.AlHomssi,A.Al-Hourani,S.Chandrasekharan,K.M.Gomez,and
toringusingIoT,’’InternetThings,vol.11,Sep.2020,Art.no.100173. S. Kandeepan, ‘‘On the bound of energy consumption in cellular IoT
networks,’’IEEETrans.GreenCommun.Netw.,vol.4,no.2,pp.355–364,
| [9] ATsens. | (2022). | AT-Patch, | Heart Solution. | [Online]. | Available: |     |     |     |     |     |     |     |
| ----------- | ------- | --------- | --------------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Jun.2020.
https://atsens.com/en/
[10] S. K. Venkateswaran, C.-L. Tai, Y. Ben-Yehezkel, Y. Alpert, and [32] H.VuandT.Saukurai,‘‘CollisionprobabilityinsaturatedIEEE802.11
R.Sivakumar,‘‘ExtendingbatterylifeforWi-Fi-basedIoTdevices:Mod- networks,’’inProc.Austral.Telecommun.Netw.Appl.Conf.,Dec.2006,
| eling,strategies,andalgorithm,’’inProc.19thACMInt.Symp.Mobility |     |     |     |     |     | pp.21–25. |     |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
[33] Y.C.TayandK.C.Chua,‘‘AcapacityanalysisfortheIEEE802.11MAC
Manage.WirelessAccess,Nov.2021,pp.147–156.
protocol,’’WirelessNetw.,vol.7,no.2,pp.159–171,2001.
[11] Z.Zheng,W.Cui,L.Qiao,andJ.Guo,‘‘Performanceandpowerconsump-
[34] H.-J.JinandM.-L.Song,‘‘Throughputanalysisbasedoncollisionprob-
tionanalysisofIEEE802.11ahforsmartgrid,’’WirelessCommun.Mobile
Comput.,vol.2018,pp.1–8,Jul.2018. abilityin802.11networks,’’J.Inst.Webcasting,InternetTelecommun.,
vol.14,no.2,pp.93–100,Apr.2014.
[12] H.Hou,T.Wang,B.Zhang,Y.Luo,L.Mao,F.Wang,S.Wu,andZ.Sun,
[35] Z.Li,Z.Tian,M.Zhou,Z.Zhang,andY.Jin,‘‘Awarenessofline-of-sight
‘‘DetectionofIgMandIgGantibodiesinpatientswithcoronavirusdisease
propagationforindoorlocalizationusingHopkinsstatistic,’’IEEESensors
2019,’’Clin.Transl.Immunol.,vol.9,no.5,pp.1–8,Jan.2020.
J.,vol.18,no.9,pp.3864–3874,May2018.
[13] J.-H.Kim,J.A.-R.An,P.-K.Min,A.Bitton,andA.A.Gawande,‘‘How
SouthKorearespondedtothecovid-19outbreakindaegu,’’NEJMCata- [36] R. Guide, ‘‘DTIM interval (period) best setting,’’ Router Guide,
USA,Tech.Rep.,2015.[Online].Available:https://routerguide.net/dtim-
lyst,vol.1,no.4,pp.1–14,Jul.2020.
interval-period-best-setting
[14] J.-R.Lee,S.-W.Kwon,andD.-H.Cho,‘‘Adaptivebeaconlisteningproto-
|     |     |     |     |     |     | [37] M. Heath, | ‘‘Wi-Fi | setup | guide: | What | is  | a good signal |
| --- | --- | --- | --- | --- | --- | -------------- | ------- | ----- | ------ | ---- | --- | ------------- |
colforaTCPconnectioninslow-startphaseinWLAN,’’IEEECommun.
|     |     |     |     |     |     | level or | signal-to-noise |     | ratio | (SNR) | for Wi-Fi,’’ | Increase |
| --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ----- | ----- | ------------ | -------- |
Lett.,vol.9,no.9,pp.853–855,Sep.2005.
|     |     |     |     |     |     | Broadband | Speed, | U.K., | Tech. | Rep., | 2020. [Online]. | Available: |
| --- | --- | --- | --- | --- | --- | --------- | ------ | ----- | ----- | ----- | --------------- | ---------- |
[15] T.Adame,A.Bel,B.Bellalta,J.Barcelo,andM.Oliver,‘‘IEEE802.11ah: https://www.increasebroadbandspeed.co.U.K./what-is-a-good-signal-
TheWiFiapproachforM2Mcommunications,’’IEEEWirelessCommun.,
level-or-signal-to-noise-ratio-snr-for-wi-fi
vol.21,no.6,pp.144–152,Dec.2014.
|     |     |     |     |     |     | [38] S. Sundar, | ‘‘Driving |     | Wi-Fi | based | connectivity | for low- |
| --- | --- | --- | --- | --- | --- | --------------- | --------- | --- | ----- | ----- | ------------ | -------- |
[16] A.Bel,T.Adame,andB.Bellalta,‘‘Anenergyconsumptionmodelfor
|     |     |     |     |     |     | power | IoT applications,’’ |     | Silicon | Labs, | Austin, | TX, USA, |
| --- | --- | --- | --- | --- | --- | ----- | ------------------- | --- | ------- | ----- | ------- | -------- |
IEEE802.11ahWLANs,’’AdHocNetw.,vol.72,pp.14–26,Apr.2018.
|     |     |     |     |     |     | Tech. Rep., | 2021. | [Online]. |     | Available: | https://www.silabs.com/ |     |
| --- | --- | --- | --- | --- | --- | ----------- | ----- | --------- | --- | ---------- | ----------------------- | --- |
[17] S.Santi,L.Tian,E.Khorov,andJ.Famaey,‘‘Accurateenergymodeling whitepapers/driving-wi-fi-based-connectivity-for-low-power-iot-
| andcharacterizationofIEEE802.11ahRAWandTWT,’’Sensors,vol.19, |     |     |     |     |     | applications |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
no.11,p.2614,2019.
[18] Q.Chen,Z.Weng,X.Xu,andG.Chen,‘‘Atargetwaketimescheduling
schemeforuplinkmultiusertransmissioninIEEE802.11ax-basednext
generationWLANs,’’IEEEAccess,vol.7,pp.158207–158222,2019.
[19] E.Stepanova,D.Bankov,E.Khorov,andA.Lyakhov,‘‘Onthejointusage
oftargetwaketimeand802.11bawake-upradio,’’IEEEAccess,vol.8,
pp.221061–221076,2020.
[20] R.Liu,R.Dorrance,D.Dasalukunte,V.Kristem,M.A.S.Lopez,A.W.
|     |     |     |     |     |     |     |     | SEUNGJIN |     | LEE (Graduate | Student | Member, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- | ------- | ------- |
Min,S.Azizi,M.Park,andB.R.Carlton,‘‘An802.11ba-basedwake-
IEEE)receivedtheB.S.degreefromInformation
upradioreceiverwithWi-Fitransceiverintegration,’’IEEEJ.Solid-State andCommunicationsUniversity(ICU),Daejeon,
Circuits,vol.55,no.5,pp.1151–1164,May2019. SouthKorea,in2005,andtheM.S.degreeininfor-
[21] S.Liu,V.K.Ramanna,andB.Dezfouli,‘‘Empiricalstudyandenhance- mationandcommunicationengineeringfromthe
mentofassociationandlongsleepin802.11IoTsystems,’’inProc.IEEE
|     |     |     |     |     |     |     |     | Korea | Advanced | Institute | of Science | and Tech- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --------- | ---------- | --------- |
GlobalCommun.Conf.(GLOBECOM),Dec.2020,pp.1–7.
|     |     |     |     |     |     |     |     | nology | (KAIST), | Daejeon, | in 2008, | where he is |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | -------- | -------- | ----------- |
[22] J.ShethandB.Dezfouli,‘‘Enhancingtheenergy-efficiencyandtimeliness
|     |     |     |     |     |     |     |     | currently | pursuing | the | Ph.D. degree | in informa- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | ------------ | ----------- |
ofIoTcommunicationinWiFinetworks,’’IEEEInternetThingsJ.,vol.6,
tionandcommunicationengineering.Hisresearch
no.5,pp.9085–9097,Oct.2019.
interestsincludetrafficengineering,resourceman-
[23] E.Dekel,‘‘Low-powerinternetconnectivityoverWi-Fi,’’TexasInstrum.,
Dallas, TX, USA, Tech. Rep. SWRY019a, 2019. [Online]. Available: agement,theInternetofThings,andmachinelearningfornetworking.
https://www.ti.com/lit/wp/swry019a/swry019a.pdf
[24] G.Sinha,M.R.Kanagarathinam,S.R.Jayaseelan,andG.K.Choudhary,
| ‘‘CQUIC: | Cross-layer   | QUIC    | for next generation | mobile  | networks,’’ |     |     |     |     |     |     |     |
| -------- | ------------- | ------- | ------------------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| in Proc. | IEEE Wireless | Commun. | Netw. Conf.         | (WCNC), | May 2020,   |     |     |     |     |     |     |     |
pp.1–8.
| [25] I. F. Akyildiz, | E.  | Khorov, | A. Kiryanov, | D. Kovkov, | A. Krasilov, |     |     |     |     |     |     |     |
| -------------------- | --- | ------- | ------------ | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
M.Liubogoshchev,D.Shmelkin,andS.Tang,‘‘XStream:Anewplatform
|     |     |     |     |     |     |     |     | HYUNGWOO |     | CHOI | (Member, | IEEE) received |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---- | -------- | -------------- |
enablingcommunicationbetweenapplicationsandthe5Gnetwork,’’in
|     |     |     |     |     |     |     |     | the B.S. | degree | from | Chungnam | National Uni- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---- | -------- | ------------- |
Proc.IEEEGlobecomWorkshops(GCWkshps),Dec.2018,pp.1–6.
|     |     |     |     |     |     |     |     | versity, | Daejeon, | SouthKorea, |     | in 2005, and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ----------- | --- | ------------ |
[26] T.Azzino,M.Drago,M.Polese,A.Zanella,andM.Zorzi,‘‘X-TCP:A
crosslayerapproachforTCPuplinkflowsinmmwavenetworks,’’inProc. the M.S. and Ph.D. degrees in information
|     |     |     |     |     |     |     |     | and communication |     | engineering |     | from the Korea |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ----------- | --- | -------------- |
16thAnnu.Medit.AdHocNetw.Workshop(Med-Hoc-Net),Jun.2017,
|     |     |     |     |     |     |     |     | Advanced | Institute | of  | Science | and Technology |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | ------- | -------------- |
pp.1–6.
(KAIST),Daejeon,in2007and2021,respectively.
[27] I.GerasinandA.Krasilov,‘‘Improvingperformanceofwebservicesin5G
HeiscurrentlyaPost-Ph.D.Researcherwiththe
newradiosystems,’’inProc.IEEEInt.BlackSeaConf.Commun.Netw.
(BlackSeaCom),Jun.2019,pp.1–3. SchoolofElectricalandElectronicsEngineering,
[28] S.Geissler,S.Lange,F.Wamser,T.Zinner,andT.Hoßfeld,‘‘KOMon— KAIST.Hisresearchinterestsincludetrafficengi-
Kernel-basedonlinemonitoringofVNFpacketprocessingtimes,’’inProc. neering,resourcemanagement,theInternetofThings,andmachinelearning
| Int.Conf.Netw.Syst.(NetSys),Mar.2019,pp.1–8. |     |     |     |     |     | fornetworking. |     |     |     |     |     |       |
| -------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | ----- |
| VOLUME10,2022                                |     |     |     |     |     |                |     |     |     |     |     | 61247 |

S.Leeetal.:NoveleAPSystemWithCross-LayerDesigninWi-FiNetworksforReliableIoTServices
TAEHWAKIM(StudentMember,IEEE)received JUN KYUN CHOI (Senior Member, IEEE)
the B.S. degree from Jeonbuk National Univer- received the B.Sc. (Eng.) degree in electron-
sity, Jeonju-si, SouthKorea, in 2005, and the ics engineering from Seoul National University,
M.S. degree from the Korea Advanced Institute Seoul,SouthKorea,in1982,andtheM.Sc.(Eng.)
of Science and Technology (KAIST), Daejeon, andPh.D.degreesinelectronicsengineeringfrom
SouthKorea,in2007,allininformationandcom- theKoreaAdvancedInstituteofScienceandTech-
municationengineering.Sheiscurrentlypursuing nology(KAIST),in1985and1988,respectively.
thePh.D.degreeininformationandcommunica- FromJune1986toDecember1997,hewaswith
tionengineeringwithKAIST.Herresearchinter- theElectronicsandTelecommunicationsResearch
estsincludenetworkscodingandvideostreaming Institute(ETRI).InJanuary1998,hejoinedInfor-
protocols,theInternetofThings,andmachinelearningfornetworking. mationandCommunicationsUniversity(ICU),Daejeon,SouthKorea,asa
Professor.In2009,hemovedtotheKoreaAdvancedInstituteofScience
and Technology (KAIST) as a Professor. He is an Executive Member of
TheInstituteofElectronicsEngineersofKorea(IEEK),aEditorBoardof
MemberoftheKoreaInformationProcessingSociety(KIPS),andaLife
MemberoftheKoreaInstituteofCommunicationScience(KICS).
HONG-SHIK PARK (Member, IEEE) received
the B.S. degree from Seoul National University,
Seoul, SouthKorea, in 1977, and the M.S. and
Ph.D.degreesfromtheKoreaAdvancedInstitute
of Science and Technology (KAIST), Daejeon,
SouthKorea, in 1986 and 1995, respectively,
all in electrical engineering. In 1977, he joined
theElectronicsandTelecommunicationsResearch
Institute(ETRI)andwasinvolvedinthedevelop-
mentoftheTDXdigitalswitchingsystemsfamily,
includingTDX-1,TDX-1A,TDX-1B,TDX10,andATMswitchingsystems.
In1998,hemovedtoInformationandCommunicationsUniversity,Daejeon,
asaFacultyMember.In2009,hebecameaProfessorwiththeSchoolof
ElectricalandElectronicsEngineering,KAIST.From2004to2012,hewas
theDirectoroftheBcNEngineeringResearchCentersponsoredbyKEIT,
SouthKorea.Currently,heisanEmeritusProfessorofKAIST.Hisresearch
interestsincludenetworksarchitecturesandprotocols,trafficengineering,
andperformanceanalysisoftelecommunicationsystems.Heisamember
ofTheInstituteofElectronicsEngineersofKorea(IEEK)andtheKorea
InstituteofCommunicationScience(KICS).
61248 VOLUME10,2022