# [26] QoS Aware Slice Resource Management Using Deep Reinforcement Learning in IoT Networks

> Source file: `[26] QoS Aware Slice Resource Management Using Deep Reinforcement Learning in IoT Networks.pdf`

---

2023 19th International Conference on Distributed Computing in Smart Systems and the Internet of Things (DCOSS-
IoT)
QoS Aware Slice Resource Management using Deep
Reinforcement Learning in IoT Networks
+ + + +
Kamran Zia , Alessandro Chiumento , Paul Havinga , Roberto Riggio*, Yanqiu Huang
+Pervasive Systems Group, EEMCS University of Twente, Enschede Netherlands
*Information Engineering Department, Polytechnic University of Marche, Ancona Italy
[k.zia, a.chiumento, p.j.m.havinga, yanqiu.huang]@utwente.nl, *r.riggio@univpm.it
Abstract—WiFi, a widely used technology in IoT, provides QoS (AIFS),whichprimarilycontrolservicedifferentiation,aredefined
through IEEE 802.11e EDCA Access Categories (AC) which have onlyfortheproposed4EDCAcategories.Moreover,mostofthe
fixed configuration with strict priorities. This makes WiFi QoS un- channelaccessisconsumedbyvoiceandvideotraffic,duetovery
suitabletotherisingQoSdiversity,changingwirelessconditionsand
smallcontentionwindowscomparedtobesteffortandbackground
networkdynamics.QoSslicing,wherenetworkresourcesaredivided
into chinks for diverse QoS requirements, is a potent technology traffic, thus affecting best effort traffic flows which are mostly
that can provide more flexible, adaptable and highly configurable being used by IoT sensors and devices. As a result, their QoS is
QoS in WiFi based IoT networks. However, resource management adversely affected.
of QoS slices with diverse IoT applications, limited network capac- Many research works have proposed throughput enhance-
ity and varying channel conditions is a complex and challenging
ment [4] and delay reduction [5] schemes in WiFi based IoT
task.Traditionalqueuingtheoreticandoptimizationmodelsbecome
intractabletosolvesuchcomplexanddynamicproblem.Therefore, networks for IoT QoS. Some works have even employed AI and
wehavedevelopedaDeepReinforcementLearning(DRL)basedslice ML as well in their works for QoS satisfaction and they always
resourcemanagementschemetomeetIoTQoSrequirementsinareal relyonEDCAaccesscategoriestoprovideQoSinWiFibasedIoT
world 5GEmpower controlled SDN network. Our proposed scheme networks[4][6].However,theproblemisthatEDCAhaslimited
outperformsAirtimeExcessRoundRobin(ATERR)schemeandno
numberofaccesscategorieswithfixedconfigurations.Therefore,
slicing-basedschemeintermsofslicethroughput(QoS)satisfaction.
Moreover,ourproposedschemeistestedinrealworldenvironment in order to dynamically manage the varying range of IoT QoS
andcanadapttothechangingslicerequirementsinanIoTnetwork. requirements with in the available resources, a more flexible and
highly configurable QoS framework is required in WiFi based
IndexTerms—WiFiSlicing,DeepReinforcementLearning,QoSin
IoTnetworksthatcanalsoprioritizeQoSflowsoveroneanother.
WiFi,AdaptiveSliceManagement,AirtimeManagement Moreover, WiFi QoS mechanism needs to have more granular
controlovernetworkresourcesthroughmoreaccesscategoriesto
I. INTRODUCTION
support large number of applications/services.
Internet of Things (IoT) has been build upon interconnection To address the shortcomings in present WiFi based networks,
of physical devices, sensors, medical appliances and Radio Fre- Software Defined Networking (SDN) provides a flexible frame-
quency Identification Tags. In the last few years, IoT networks work to perform QoS slicing in the network where network
have expanded at a fast pace in different industry verticals [1] resourcesareslicedintomultiplechinks.Eachresourcechinkcan
including smart factories, healthcare, smart cities and agricul- thenbeassignedtoQoSslicesandcanthenbemanagedthrough
ture sectors. Many new applications have been developed that SDN controller to provide desired connectivities (QoS) in the
employ machine learning algorithms by collecting data from network[7][8].Thisframework,ontheonehand,enablescreation
distributedsensors,appliancesandmachinesanddrawintelligent ofmoreaccesscategoriesinWiFinetworksandontheotherhand,
inferences[2].ToenableIoTusecases,therearevariousQuality helps preserve QoS information while traffic traversing from dif-
ofService(QoS)requirementsofIoTsensorsandapplicationsin ferentiatedservicestoaccesscategoriesinwirelessmedium.How-
termsof throughput,latency, andreliability.More often,meeting ever, managing network resources for access categories or QoS
these QoS requirements is crucial for the success of the IoT use slices is a complex and challenging task. It involves a dynamic
cases. and adaptive management of network resources while keeping
DuetorequirementofreliableQoSinpresentdayIoTnetworks, in view the channel conditions, applications QoS requirements
accessandcorenetworkshaveincorporatedvarioustechniquesto and available network capacity. To address this challenge, we
provide QoS to the different IoT traffic in the network. Wired haveproposedaDeepReinforcementLearning(DRL)basedslice
networksenableQoSthroughDifferentiatedServices(DS)where resource management scheme that can learn network dynamics
flows are classified and managed separately as Voice, Video or andprovideimprovedQoStotheapplicationsandsensorsinthe
Best Effort (BE) flows. Similarly, IEEE 802.11e based networks wireless IoT network. Our main contributions in this paper are:
(WiFi) use Enhanced Distributed Channel Access (EDCA) Ac- • We have developed a slice throughput requirement estima-
cess Categories (AC) to differentiate between different types of tion algorithm in 5GEmpower SDN controller to determine
traffic[3].TheQoSinWiFinetworksthroughEDCAhas4QoS different QoS slice throughput requirements autonomously.
categoriesandhasfixedconfigurationofeachcategory;therefore, • We have proposed an DRL based dynamic slice resource
it cannot support the rising diversity in QoS requirements and management algorithm that runs in a SDN controller and
varyingdynamicsoftheIoTnetworks.Although,IEEE802.11aa provides desired throughput to all slices in the WiFi based
defines further segregation of video and voice traffic to two IoT network.
classes and uses credit based schedulers to emulate a total of • Our algorithm is able to adapt to the changing through-
6 access categories in WiFi however, channel access parameters put requirements and wireless conditions to provide desired
likeContentionWindow(CW)andArbitraryInterFrameSpacing throughput to the QoS slices
2325-2944/23/$31.00 ©2023 IEEE 150
DOI 10.1109/DCOSS-IoT58021.2023.00035
53000.3202.12085TOI-SSOCD/9011.01
:IOD
|
EEEI
3202©
00.13$/32/7-9464-3053-8-979
|
)ToI-SSOCD(
sgnihT
fo
tenretnI
eht
dna
smetsyS
tramS
ni
gnitupmoC
detubirtsiD
no
ecnerefnoC
lanoitanretnI
ht91
3202
Authorized licensed use limited to: UNIVERSITY OF TWENTE.. Downloaded on October 10,2023 at 06:27:15 UTC from IEEE Xplore. Restrictions apply.

Ourproposedalgorithmsaretestedinrealworldexperimental
•
| test                 | bed for     | validation.     |             |            |            |            |     |     |     |     |     |
| -------------------- | ----------- | --------------- | ----------- | ---------- | ---------- | ---------- | --- | --- | --- | --- | --- |
|                      |             | II. RELATEDWORK |             |            |            |            |     |     |     |     |     |
| QoS in               | wireless    | networks        | is          | an ongoing | research   | problem    |     |     |     |     |     |
| that poses           | significant | challenges      |             | compared   | to wired   | networks   |     |     |     |     |     |
| due to unpredictable |             | nature          | of wireless | medium.    | As         | such, many |     |     |     |     |     |
| techniques           | have        | been proposed   | in          | literature | to address | the QoS    |     |     |     |     |     |
probleminWiFibasednetworks.Authorsin[9]haveproposeda
| QoS slicing | based | solution | in WiFi | networks | using | 5GEmpower |     |     |     |     |     |
| ----------- | ----- | -------- | ------- | -------- | ----- | --------- | --- | --- | --- | --- | --- |
SDNcontrollertoprovideQoStotwodifferenttypesofflows.The
systemisabletoprovidemoreresourcestoQoSslicestoprovide
| better QoS | to  | the applications |     | compared | to BE | applications. |     |     |     |     |     |
| ---------- | --- | ---------------- | --- | -------- | ----- | ------------- | --- | --- | --- | --- | --- |
However,theyonlyconsideredtwoslicesinthenetwork.Authors
| in [10] proposed |                 | a Quadratically | Constrained  |         | Quadratic    | Program |     |     |     |     |     |
| ---------------- | --------------- | --------------- | ------------ | ------- | ------------ | ------- | --- | --- | --- | --- | --- |
| (QCQP)           | based algorithm |                 | to assign    | airtime | to different | network |     |     |     |     |     |
| slices to        | meet the        | latency         | requirements | of      | applications | in the  |     |     |     |     |     |
network.Theproposedschemehowever,haslimitationstoemploy
| such techniques |         | in real-time | to meet      | QoS requirements. |              |               |     |     |     |     |     |
| --------------- | ------- | ------------ | ------------ | ----------------- | ------------ | ------------- | --- | --- | --- | --- | --- |
| Authors         | in [11] | proposed     | a Proportion |                   | Time Deficit | Round         |     |     |     |     |     |
| Robin (PT-DRR)  |         | based slice  | resource     | assignment        |              | algorithm and |     |     |     |     |     |
usedairtimeallocationtonetworkslicesforQoSprovisioningin Fig.1. NetworkModel
| the network. | The     | proposed    | scheme    | is based | on queuing       | theory       |           |           |             |                         |             |
| ------------ | ------- | ----------- | --------- | -------- | ---------------- | ------------ | --------- | --------- | ----------- | ----------------------- | ----------- |
| and employs  | quantum | assignments |           | to the   | network          | slices based |           |           |             |                         |             |
|              |         |             |           |          |                  |              | to enable | a dynamic | and         | evolving QoS management | [6] [12].   |
| on airtime   | being   | used by     | different | queues.  | However,         | airtime      |           |           |             |                         |             |
|              |         |             |           |          |                  |              | Owing to  | AI and    | ML benefits | and their adaptive      | and dynamic |
| for packets  | also    | depends     | on the    | physical | layer parameters | like         |           |           |             |                         |             |
nature,wehaveproposedaDRLbasedsliceresourcemanagement
| Modulation | and | Coding Scheme |     | (MCS) and | CW  | etc therefore, |     |     |     |     |     |
| ---------- | --- | ------------- | --- | --------- | --- | -------------- | --- | --- | --- | --- | --- |
quantumassignmentscanonlyindirectlycontrolthetotalairtime schemeformeetingvaryingthroughputrequirementsofIoTtraffic
ofeachslice.Theproposedschemecalculatestheratioofquantum flows in a SDN controlled wireless IoT network.
for each slice based on available channel capacity and slice III. NETWORKSETUPANDQOSSLICING
requirements and allocates them to the available slices. Since In order to develop the DRL based resource management for
wireless medium and application requirements are a continually QoSslices,wehaveusedthe5GEmpowerSDNframework[13].
|          |             |       |         |             |     |             | 5GEmpower | is a | multi-RAT | SDN framework | that supports both |
| -------- | ----------- | ----- | ------- | ----------- | --- | ----------- | --------- | ---- | --------- | ------------- | ------------------ |
| changing | phenomenon, | fixed | quantum | assignments |     | can lead to |           |      |           |               |                    |
poor QoS in the network. WiFi and LTE networks. It provides a web based user interface
Similar to PT-DRR, authors in [7] have proposed Adaptive to interact with the network applications, create access control
Time Excess (ATERR) based resource allocation in QoS slicing listsandcreate/deleteQoSslices.ItalsoprovidesaPythonbased
framework to enable QoS in a WiFi network. In this work, the SoftwareDevelopmentKit(SDK)todevelopnetworkapplications
authors calculate the quantum assignments to the slice based on whichrunasservicesontheSDNcontroller.Thenetworkstatistics
time excess and requested airtime rather than deficit [11] for the are collected from the empower agent running inside the Access
available network slices. The time excess is calculated based to Points(AP)beingcontrolledbythe5GEmpowerSDNcontroller.
consumedairtimebypacketsandremainingquantumfortheslice The pictorial representation of the network model is given in
| (airtimeconsumed-remainingquantum).Anegativetimeexcess |     |     |     |     |     |     | Figure 1. |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
will let slice transmit its packets while packet transmission stops ThenetworkmodelcomprisesofanSDNcontrollercommuni-
as soon as time excess become positive, indicating all quantum catingwithanAP.TheIoTdevicesaresimulatedusingRaspberry
has been consumed in that round of scheduling. PiboardsthatareassociatedwiththeAPoverIEEE802.11nbased
Although quantum assignments can indirectly control the air- WiFi standard. IoT devices are randomly distributed around the
timeeachslicegetsinthewirelessmedium,therearevariousother AP and are receiving traffic from the AP in the downlink. Each
factors that affect the airtime a device gets in the WiFi network. device is running multiple IoT applications requiring different
There factors include Modulation and Coding Schemes (MCS), levelsofthroughputsfortheQoSflowsinthedownlink.Asingle
CWandACKpolicyetc.AlowerMCSwillconsumemoreairtime SDN controller is controlling multiple APs inside the network.
in the wireless medium to transmit packets (because of low bit In order to implement QoS slicing, we have considered M
rate) and hence the assigned quantum value will not be able to distinct applications/services in the network with different QoS
provide the desired QoS (throughput or latency) to the network requirements where M=[1,2,3,....,m]. To provide QoS to these M
slice. For these reasons, quantum assignments cannot be done distinctapplications,SslicesarecreatedwhereS=[1,2,3,....,s]and
based on requested airtime as it may vary based on MCS being S can be equal to or less than M. Applications requiring same
|     |     |     |     |     |     |     | level of throughput |     | or latency | are considered | similar and belong |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ---------- | -------------- | ------------------ |
usedatthephysicallayerofthenetwork.Therefore,knowingthe
MCS being used at the physical layer is also important during to the same QoS slice. To prioritize similar applications in the
quantum assignments. same slice over one another, we have developed a traffic rule
Although network slicing and slice resource management has abstractionthatenablesQoSflowstobemovedfromlowpriority
beenproposedinliterature,itlacksadaptiveresourcemanagement slicetothehighprioritysliceandviceversatoreliablymeettheir
| tocontinuallymeetQoSinIoTnetworks.Inthiscontext,AIand |     |     |     |     |     |     | QoS requirements. |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
ML based approaches can help develop algorithms that can effi- In order to understand the slice throughput requirements, the
cientlyutilizenetworkresourcesandcanlearnnetworkdynamics SDN controller collects statistics like packet arrival rate and
151
Authorized licensed use limited to: UNIVERSITY OF TWENTE.. Downloaded on October 10,2023 at 06:27:15 UTC from IEEE Xplore.  Restrictions apply.

average packet size, for fixed time intervals, from different QoS B. DRL Framework
slices created in the AP. In this way, it can employ time interval To employ DRL in this problem, the wireless environment
basedestimatortoautomaticallyestimatetheslicethroughputre- and QoS requirements are represented with the help of envi-
quirements.Subsequentlythecontrollerassignsnetworkresources ronment state. There are numerous variables that can define the
to the slices to meet these requirements. In case of traffic flows environment state but they eventually have an effect on achieved
exceedingtheavailablecapacityattheAPs,thelowpriorityslices throughout.Therefore,wehavedefinedthestateofourDRLagent
are affected thus ensuring QoS for high priority slices. To avoid withthehelpofachievedthroughputineachofthecreatedslices
suchsituations,admissioncontrolalgorithmscanbeemployedto in the network. For meeting slice’s throughputs, our DRL agent
ensure that traffic flows does not exceed the available network assignsquantumvaluestothesliceschedulersandfollowsAirtime
capacity. Deficit Round Robin (ADRR) scheduling policy defined by [14]
toprioritizetheslices.ADRRusesairtimedeficitinitsscheduling
IV. DRLFRAMEWORKFORQOSSLICERESOURCE
whichiscalculatedbasedontheMCSbeingusedatthephysical
MANAGEMENT
layertherefore,MCSindirectlybecomespartoftheDRLagent’s
InordertoaddressthechallengesofdiverseapplicationsQoS,
state space. For better understanding of our DRL framework, the
varying channel conditions and changing network dynamics, we
states,actionsandrewardsofouragentaredescribedasfollows:
have employed Deep Reinforcement Learning (DRL) to develop
1) State: The DRL agent defines its state with the help of
an adaptive slice resource management scheme. In our proposed
throughput being achieved by each slice and their estimated
scheme, a DRL agent is deployed inside the SDN controller that
throughput requirements as follows:
runs as a network application and takes the resource assignment
decisions for the QoS slices. The primary objective of our DRL s t =(Th 1 ,TH e1 ,Th 2 ,TH e2 ,...,Th s ,TH es ) (4)
agent is to manage resource assignments to QoS slices such that
slice throughput requirements are met under all conditions. where Th s represents the throughput achieved by slice s and
TH es represents the required throughput thresholds for slice s
A. Problem Formulation
estimated by the SDN controller.
SincethereisasingleDRLagentthatislearningoptimalslice 2) Action: The action that DRL agent can take is either to
configuration for multiple slices, this slice resource management increase the quantum (resource) of the slice, keep the quantum
problem becomes a Multi-Objective problem where each slice sameordecreasethequantumoftheslicedependingonthestate
satisfaction is a separate objective for the DRL agent. This of the agent. The action can be represented as follows:
is done through weight vector which contains weight of each
of the objectives of DRL agent. Therefore, our problem can
a
t
=(Q
increase
,Q
decrease
,Q
neutral
)(5)
be represented by Multi Objective Markov Decision Process
(MOMDP).The throughput of each slice would be the sum of
throughputs of all users present in that slice and the quantum
assignment to the slice. So we can represent it as follows:
(cid:2)
Th s = Th k =f(Q s ,MCS,TX−Power,ACK) (1)
ks∈Ks
where k represents the number of users belonging to slice s.
ThethroughputofeachslicewilldependontheQuantumvalues,
MCS,transmitpowerandACKpolicyetcbeingusedbytheusers
in the slice. Therefore, the slice throughput would be a function
of many OSI layer parameters in addition to quantum values as
represented by the function in equation 1. The total achievable
throughput, bounded by the network capacity, is given by:
(cid:2)
Th total = Th s (2)
s∈S
TheobjectiveofourDRLagentistosatisfythethroughputsof
alltheslicesinthenetworkwhilealsotryingtomaximizetheag-
gregatethroughput.Ouroptimizationproblemcanberepresented
with the following objective function:
(cid:2)S
max Th s (3) Fig.2. FlowChartofDDQNbasedSliceResourceManagementAlgorithm
s∈S
s=1
3) Reward: The reward function is defined on the basis
subjected to,
throughput satiisfaction level in each of the slice, represented as
C.1 Th s >TH es ∀s∈S R t 1(s t ,a t) and is given ⎧ by:
s
Q
li
t
c
w o
e
t h a
s.
e l r
T
r e e
h
p
e
T re
v
H s
a
e
l
e
u
n s
e
ts r
i
e
s
th p
k
e r
C
e
e
p
.
t s
2
o e
t
t n
a
Q
a t
t
l s
t
1
o
q
0
t
t u
a
h
0
a
l
e
0
n
≤
0
t e u
μ
s
1
m t
s
0
i
e
m
0
v
c
0
a a
0
t
t l
o
e u
μ
d e
s
k
e
e
d s
c
e
i l
p
s ic tr
s
e i
c
b
h
u t
e
h t
d
e ro d
u
u
li
a g
n
m h
g
p o
l
u n
a
t
t
g
e
a
n
t n h
cy
d e R t s(s t ,a t )=
⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎩
1
7 4
1
0 i
i i
i
f
f f
f
R
R R
R
t
t t
t
s
s s
s
≤
≥ ≥
≥
1
7 5
3
1
0 0
0
0
% %
%
%
s s
s
a a
a
s
t t
t
a
i i
i
t
s s
s
i
f f
f
s
a a
a
f
c c
c
a
t t
t
c
i i
i
t
o o
o
io
n n
n
n
(6)
of the QoS flows under 10 ms.
−5 otherwise.
152
Authorized licensed use limited to: UNIVERSITY OF TWENTE.. Downloaded on October 10,2023 at 06:27:15 UTC from IEEE Xplore. Restrictions apply.

(a)ProposedDRLbasedSliceResourceAssignment (b)ATERRBasedSliceResourceAssignment (c)ThroughputwithoutQoSSlicing
Fig.3. ComparisonofSliceResourceAssignmentforQoSinWiFibasedIoTNetwork
Each slice will get its own reward represented as R t 1(s t ,a t), V. PERFORMANCEEVALUATION
R t 2(s t ,a t) and R t s(s t ,a t). The total reward that the agent gets at InordertoevaluatetheproposedDRLbasedQoSsliceresource
each time is calculated as follows:
management solution, a 5GEmpower based real world test bed
hasbeenused.ForWiFiconnectivity,IEEE802.11nstandardhas
R t =W∗[R t 1,R t 2,...,R t s]T (7) been used with 2.4 GHz band in real world environment where
otherWiFiaccesspointsanddevicesaresharingthechannelwith
where W is the weight vector representing the throughput
our setup to capture real world network effects. Iperf3 has been
requirements of the slices. The weight vector is calculated based
usedtogenerateTCPandUDPtrafficinthedownlinktoemulate
ontheavailablechannelcapacitythattheAPestimatesfromtime
differentapplications.ForapplicationQoS,Network(QoS)slicing
totimeandslicethroughputrequirements.Thecalculationofthe
was employed where slice requirements can be predefined in the
weight is done by the DRL using the available channel capacity
network considering the service level agreements. In our evalua-
agent as follows:
tionframework,theslicerequirementswereestimatedusingtime
interval based packet estimator. The time interval of 5 seconds
W=[W s1 /ζ,W s2 /ζ,....,W sm /ζ] (8) wasusedtomakethethroughputestimates.Theslicethroughput
requirements were were kept such that all available network
whereζ representsthetotalAPcapacitythatitestimatesfrom capacity is utilized to create a resource constrained environment.
time to time. The slice requirements were changed in run time by generating
differenttrafficstreamswithdifferentratesduringthetrainingand
C. DRL Model: Neural Network Architecture evaluationofalgorithms.Fortheperformanceevaluation,wehave
consideredthreedifferentslicesinourstudyalongwiththedefault
Becauseofthelargenumberofstates,actionsandrequirement
slicehowever,morenumberofslicescanalsobeconsideredinthe
of efficient quantum assignments to the slices, we have used
proposedframeworkdependingonQoSclasses.TheDRLagentis
deep neural network as the function approximator for our DRL
deployedasNetworkApplicationintheSDNcontrollerthattakes
agent. Such a function approximator learns the function ”f”
input from the InfluxDB, where 5GEmpower stores its statistics,
given in equation 1 through environment exploration. We have
to observe its state and take suitable action as per learnt policy.
employed Double Deep Q Network (DDQN) with two hidden
layers in our framework. The size of hidden layers are 256 and A. Slice Throughput Performance
128 respectively for both the evaluation and target Q-Network. InordertoobservetheperformanceoftheDRLagent,wehave
We have used Relu activation function. As an optimizer for NN, includedthresholdrequirementsoftheslicesinourframeworkto
Adam optimizer with a learning rate of 0.001 is used and value measure performance of our resource assignments by the DRL
of discount factor (gamma) was kept at 0.8. To train the Q- agent. These threshold requirements are estimated in real time
Network, a random batch of 64 samples is read from the replay to create a dynamic and autonomous QoS delivery. The SDN
bufferofsize100000tode-correlatethelearningsamplesandto controller continuously estimates slice throughput requirements
improve the learning efficiency. The hyper parameters including and DRL agent learns the environment through exploration and
learning rate, layers sizes, discount factor and batch size were exploitation.TheDRLagentexplorestheenvironmentduringthe
empiricallychosenafterrunningmultipleexperimentationsunder trainingphaseanduseslargerquantumvaluechanges(700μsec)
differentQoSrequirementsandscenarios(theiruniversalityisleft toquicklylearntheslicerequirementsandwirelessenvironment.
forfurtherstudy).Thesizeoftheinputtoneuralnetworkisequal Afterwards, the quantum changes are done in small steps (200
tothenumberoftheslicesinthenetworkhowever,neuralnetwork μsec) to stabilize the slice throughputs. In this way, the DRL
canbetrainedwithanynumberofslicesdependingonQoSclasses agentisabletomeettheslicethroughputrequirementsasshown
in the network. After taking the optimal action (correct quantum in Figure 3(a).
assignment to slices) represented by equation 5, the agent gets a The large variations in throughputs in start are due to large
feedback from the environment in the form of reward calculated quantum changes. Our proposed scheme is tested in real world
using equation ?? and moves into the new state. During this scenario where other WiFi APs were being operated in the same
time step, Q-values of actions are calculated using the Bellman frequency bands, our system faced interferences from other APs.
OptimalityequationAfterwards,theneuralnetworkperformsthe The DRL agent is able to achieve the desired throughput by
update while minimizing the loss function. The flow chart of the continually adapting the resource assignments as per channel
DDQN algorithm used in our DRL based QoS Slice Resource conditions.FromFigure3(a),wecanseethatchannelconditions
Management framework is given in Figure 2. at95secand130secgoesbadfortheslice1andsystemquickly
153
Authorized licensed use limited to: UNIVERSITY OF TWENTE.. Downloaded on October 10,2023 at 06:27:15 UTC from IEEE Xplore. Restrictions apply.

Fig.4. DRLAgentAdaptationtoChangingSliceRequirements Fig.5. ComparisonofEmpiricalCDFsofSliceThroughputs
recovers it back to optimal configuration. When the channel slices and up to any number of slices. In our future work we
conditions worsen such that the desired threshold requirements plantotargetlowerlayerparametersattheMACandPHYlayers
cannotbemet,theAPdividestheavailablecapacityproportional like Contention Window (CW) size, Inter Frame Spacing (IFS),
to the overall slice requirements. On the contrary, ATERR [8] MCS,buffersizesandtransmitpoweretctodevelopbettercontrol
basedresourceassignmentcalculatesquantumassignmentsasper over slice resources. These parameters can bring change in slice
available number of slices without looking at channel conditions throughputsandpacketdelaysatfastertimescalesoftheorderof
and hence cannot always meet desired threshold requirements. milliseconds therefore, they can make system more adaptable to
|     |     |     |     |     |     |     | quick changes | in slice requirements. |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---------------------- | --- | --- |
B. AdaptationofDRLAgenttochangingThresholdRequirements
The throughput requirements of QoS flows in the network are REFERENCES
notfixedandkeeponchangingwithtime.Moreover,keepingthe [1] P.Karweletal.,“Ericssonmobilityreport,”EricssonAB,Technol.Emerg.
throughput assignments fixed for different slices is also not wise Business,Stockholm,Sweden,Tech.Rep.EAB-21,2021.
[2] W.Li,Y.Chai,F.Khan,S.R.U.Jan,S.Verma,V.G.Menon,X.Li,etal.,
as throughput from slice 1 can be assigned to other slices when “Acomprehensivesurveyonmachinelearning-basedbigdataanalyticsfor
therearenoQoSflowspresentinslice1.Inordertotesttheper- iot-enabled smart healthcare system,” Mobile Networks and Applications,
vol.26,no.1,pp.234–252,2021.
formanceoftheDRLagentanditscapabilitytoadapttochanging
|                                                               |     |     |     |     |     |     | [3] IEEE, | “Ieee 802.11e-2005,” | IEEE Standard for Information | Technology, |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | -------------------- | ----------------------------- | ----------- |
| slicethroughputrequirements,varyingtrafficwithdifferentpacket |     |     |     |     |     |     | 2005.     |                      |                               |             |
sizes was generated in different slices. As our DRL agent was [4] W. Wydman´ski and S. Szott, “Contention window optimization in ieee
trainedbasedfordifferentslicerequirementstherefore,itquickly 802.11axnetworkswithdeepreinforcementlearning,”in2021IEEEWireless
CommunicationsandNetworkingConference(WCNC),pp.1–6,2021.
determinesoptimalsliceresourceconfigurationstomeettheirnew
[5] X.Jiang,H.Shokri-Ghadikolaei,G.Fodor,E.Modiano,Z.Pang,M.Zorzi,
requirementsasshowninFigure4.ThisisbecausetheDRLagent andC.Fischione,“Low-latencynetworking:Wherelatencylurksandhow
learns the network dynamics and slice throughput requirements totameit,”ProceedingsoftheIEEE,vol.107,no.2,pp.280–306,2019.
[6] S.Szott,K.Kosek-Szott,P.Gawx0142;owicz,J.T.Gx00F3;mez,B.Bellalta,
| and tries | to maximize | the | long term reward. | This | enables | agent |     |     |     |     |
| --------- | ----------- | --- | ----------------- | ---- | ------- | ----- | --- | --- | --- | --- |
A.Zubow,andF.Dressler,“Wi-fimeetsml:Asurveyonimprovingieee
tokeeppastactionsandslicerequirementsinconsiderationwhile
802.11performancewithmachinelearning,”IEEECommunicationsSurveys
Tutorials,pp.1–1,2022.
| taking resource | allocation |     | decisions and | hence it | quickly | adapts |     |     |     |     |
| --------------- | ---------- | --- | ------------- | -------- | ------- | ------ | --- | --- | --- | --- |
[7] M.Richart,J.Baliosian,J.Serrat,J.-L.Gorricho,andR.Agu¨ero,“Slicingin
to the changing throughput requirements. wifinetworksthroughairtime-basedresourceallocation,”JournalofNetwork
C. Maximizing Aggregate Network Throughput andSystemsManagement,vol.27,no.3,pp.784–814,2019.
[8] M.Richart,J.Baliosian,J.Serrat,J.-L.Gorricho,andR.Agu¨ero,“Slicing
Optimal quantum assignments to the QoS slices in a dynamic withguaranteedqualityofserviceinwifinetworks,”IEEETransactionson
wirelessenvironment,specificallywheremultipleAPsfromother NetworkandServiceManagement,vol.17,no.3,pp.1822–1837,2020.
|         |          |           |             |               |         |     | [9] P. H. Isolani, | N. Cardona, C. | Donato, J. Marquez-Barja, | L. Z. Granville, |
| ------- | -------- | --------- | ----------- | ------------- | ------- | --- | ------------------ | -------------- | ------------------------- | ---------------- |
| network | are also | operating | can improve | the aggregate | network |     |                    |                |                           |                  |
andS.Latre´,“Sdn-basedsliceorchestrationandmacmanagementforqos
capacity and can provide higher throughput to the users in the deliveryinieee802.11networks,”in2019SixthInternationalConference
slices.Sinceourproposedschemetriestomaximizetheaggregate onSoftwareDefinedSystems(SDS),pp.260–265,2019.
|     |     |     |     |     |     |     | [10] P. H. Isolani, | N. Cardona, C. | Donato, G. A. Pe´rez, | J. M. Marquez-Barja, |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | -------------- | --------------------- | -------------------- |
networkthroughputalongwithsatisfyingslicethroughputrequire-
L.Z.Granville,andS.Latre´,“Airtime-basedresourceallocationmodelingfor
| ments, we | are able | to achieve | higher throughputs |     | of slices | and |     |     |     |     |
| --------- | -------- | ---------- | ------------------ | --- | --------- | --- | --- | --- | --- | --- |
networkslicinginieee802.11rans,”IEEECommunicationsLetters,vol.24,
aggregate throughput compared to the ATERR scheme as shown no.5,pp.1077–1080,2020.
in CDFs in Fig 5. [11] M.Richart,J.Baliosian,J.Serrati,J.-L.Gorricho,R.Agu¨ero,andN.Agoul-
mine,“Resourceallocationfornetworkslicinginwifiaccesspoints,”in2017
VI. CONCLUSIONANDFUTUREDIRECTIONS 13thInternationalConferenceonNetworkandServiceManagement(CNSM),
pp.1–4,2017.
| To address | the | shortcomings | in present | WiFi QoS | mechanism |     |                   |               |                        |               |
| ---------- | --- | ------------ | ---------- | -------- | --------- | --- | ----------------- | ------------- | ---------------------- | ------------- |
|            |     |              |            |          |           |     | [12] E. Coronado, | S. Bayhan, A. | Thomas, and R. Riggio, | “Ai-empowered |
andimprovingQoSsatisfactionofIoTapplications,wehavepro- software-defined wlans,” IEEE Communications Magazine, vol. 59, no. 3,
pp.54–60,2021.
posedaDeepReinforcementLearningbasedsliceresourceman-
[13] E.Coronado,S.N.Khan,andR.Riggio,“5g-empower:Asoftware-defined
agement algorithm that assigns efficient and dynamic resources networkingplatformfor5gradioaccessnetworks,”IEEETransactionson
to QoS slices for meeting their throughput requirements. The NetworkandServiceManagement,vol.16,no.2,pp.715–728,2019.
[14] E.Coronado,R.Riggio,J.Villa1o´n,andA.Garrido,“Lasagna:Programming
| DRL agent | adapts | to changing | slice requirements |     | by employing |     |              |                        |                     |                 |
| --------- | ------ | ----------- | ------------------ | --- | ------------ | --- | ------------ | ---------------------- | ------------------- | --------------- |
|           |        |             |                    |     |              |     | abstractions | for end-to-end slicing | in software-defined | wlans,” in 2018 |
feedbacksintheformofrewardsandisabletomeetthedynamic IEEE19thInternationalSymposiumon”AWorldofWireless,Mobileand
QoS needs in a wireless IoT network. Our frameworks provides MultimediaNetworks”(WoWMoM),pp.14–15,2018.
moreefficient,flexibleandgranularcontroloverQoSprovisioning
| in future     | IoT networks. | In       | this work, we    | have tested | the  | system |     |     |     |     |
| ------------- | ------------- | -------- | ---------------- | ----------- | ---- | ------ | --- | --- | --- | --- |
| with 3 slices | only          | however, | it can be tested | with        | more | than 3 |     |     |     |     |
154
Authorized licensed use limited to: UNIVERSITY OF TWENTE.. Downloaded on October 10,2023 at 06:27:15 UTC from IEEE Xplore.  Restrictions apply.