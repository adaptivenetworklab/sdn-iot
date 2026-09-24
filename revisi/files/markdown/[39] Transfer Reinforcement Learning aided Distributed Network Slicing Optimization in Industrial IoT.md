# [39] Transfer Reinforcement Learning aided Distributed Network Slicing Optimization in Industrial IoT

> Source file: `[39] Transfer Reinforcement Learning aided Distributed Network Slicing Optimization in Industrial IoT.pdf`

---

1
Transfer Reinforcement Learning aided Distributed
Network Slicing Optimization in Industrial IoT
Tianle Mai, Student Member, IEEE, Haipeng Yao, Senior Member, IEEE, Ni Zhang, Wenji He, Student
Member, IEEE, Dong Guo, and Mohsen Guizani, Fellow, IEEE
Abstract—With the growth of the number of IoT devices and to provide low cost, low power, and long-range communica-
the emergence of new applications, satisfying distinct QoS in tion. Such appealing characteristics enable LoRaWAN suited
the same physical network becomes more challenging. Recently,
for a wide range of industrial applications, particularly in
with the advance of network functions virtualization (NFV)
distantareaswherebusinesseslikepetroleumdrilling,mining,
and software-defined networking (SDN) technologies, the net-
work slicing technique has emerged as a promising solution. It and construction operate. However, with the emergence of
can divide a physical network into multiple virtual networks, new applications, providing the QoS to different IoT devices
therefore providing different network services. In this paper, becomes a critical challenge in LoRaWAN [3].
to meet distinct QoS in industrial IoT, we design a network Recently, network slicing technology has emerged as a
slicing architecture over the SDN-based Long-Range Wide Area
viablesolutiontoaddressthischallenge.Networkslicingisthe
Network(LoRaWAN).TheSDNcontrollercandynamicallysplit
thenetworkintomultiplevirtualnetworksaccordingtodifferent processofdividingasinglephysicalnetworkintomanylogical
business requirements. On this basis, we proposed a Deep (virtual) networks using network virtualization (i.e., NFV and
Deterministic Policy Gradient (DDPG) based slice optimization SDN) [4]. Different slices have different logical topology,
algorithm. It enables LoRa gateways to intelligently configure security rules, and performance characteristics for the sake of
slice parameters (e.g., Transmission Power, Spreading Factor) to
fulfilling different business purposes. In this paper, we design
improvethesliceperformanceintermsofQoS,energyefficiency,
and reliability. In addition, to accelerate the training process a network slicing architecture over SDN based LoRaWAN,
acrossmultipleLoRagateways,weleveragethetransferlearning where the SDN controller can dynamically partition LoRa
framework and design a transfer learning-based multi-agent gateways’resources(e.g.,physicalchannel)intoseveralvirtual
DDPG (TMDDPG) algorithm. networks on the fly.
Index Terms—Network Slicing, Transfer Learning, Industrial Meanwhile, considering the limited resources on each gate-
IoT, Multi-agent Reinforcement Learning. way,designinganefficientsliceresourceoptimizationscheme
is another crucial problem. The gateway should be able to
I. INTRODUCTION configure slice parameters (e.g., Bandwidth (BW), Spreading
INDUSTRIAL IoT as the most powerful and exciting tech- Factor (SF), Transmission Power (TP)) to satisfy the distinct
QoS[5].Toaddressthisissue,weproposeaDDPGbasedslice
nology, has quickly become a disruptive force reshaping
resourceoptimizationalgorithm[6].TheLoRagatewaysusing
how we live and work [1]. Massive industrial devices are
the DDPG are able to improve the performance by exploring
now connected to the network, allowing for data collecting,
the environment and learning directly from their experiences.
exchanging, and analyzing. According to the Juniper’s report,
Whilesuchlearningmechanismcanconvergetotheoptimal
there will be 37 billion industrial IoT devices by 2025. Faced
policy, in the end, it has to take a large number of training
with such massive devices, IoT network technology is now
episodes. Especially in our scenario, each slice agent on each
confronted with unprecedented challenges.
LoRa gateway has to learn from scratch (i.e., randomized
Currently, the industrial IoT network market is dominated
policy), thereby resulting in a long learning time to reach
by the Long-Range Wide Area Network (LoRaWAN) tech-
the system’s optimal performance. To accelerate the training
nology [2]. It is a non-cellular wireless wide area network
process, we introduce the transfer learning framework [7].
technology,whichusestheLoRaradiomodulationtechnology
Transfer learning is a machine learning technique where
T.Mai,H.Yao,andW.HearewithStateKeyLaboratoryofNetworking experience gained acquired from one task can be transferred
and Switching Technology, Beijing University of Posts and Telecommuni-
to other related tasks. Therefore, to accelerate the learning
cations, Beijing 100876, China. E-mail: yaohaipeng@bupt.edu.cn, macheal-
mai@gmail.com,hewenji@bupt.edu.cn. processacrossmultipleLoRagateways,weproposeaTransfer
N.ZhangiswithSixthResearchInstituteofChinaElectronicCorporation, learning-based Multi-agent DDPG (TMDDPG) algorithm.
Beijing,China.Email:Zhangni@ncse.com.cn.
The major contributions of this paper are summarized as
D.GuoiswithSchoolofInformationandElectronics,BeijingInstituteof
Technology,Beijing100081,China.E-mail:7520190141@bit.edu.cn. follows.
M.GuizaniiswithMachineLearningDepartment,MBZUAI,AbuDhabi, • We design a network slicing architecture over the SDN-
UAE.E-mail:mguizani@gmail.com.
basedLoRaWAN,wheretheSDNcontrollerdynamically
This research was supported by the funding from the National Key R&D
Program of China under grant 2018YFB1800805, Artificial Intelligence and split physical resources into multiple virtual networks.
SmartCityJointLaboratory(BUPT-TGSTII)(B2020001),FutureIntelligent • We discuss the network slice optimization problem. A
Networking and Intelligent Transportation Joint Laboratory (BUPTCTTIC)
DDPG based slice optimization algorithm is designed
(B2019007),IntelligentNetworkJointLaboratory(BUPTIN)(B2021006),and
theBUPTExcellentPh.DStudentFoundationunderGrantCX2020108. for the sake of searching the optimal slice’s parameters

2
configuration. In [14], Park et al. used the DRL algorithm to address the
• To accelerate the learning process across multiple LoRa resources allocation problem in LoRaWAN. The experiment
gateways, we proposed a transfer learning-based multi- results demonstrate that the DRL-based scheme is 15% better
agent DDPG (TMDDPG) algorithm. than the current ADR algorithm in terms of throughput and
Therestofthispaperisorganizedasfollows.InSectionII, energyefficiency.In[15],Reyndersetal.proposedatwo-step
we first review the related work. In Section III, we design lightweight SF-TP scheduling scheme. The simulation results
a network slicing architecture over SDN based LoRaWAN demonstratethattheproposedschemecaneffectivelyimprove
network and present the system model. We design the T- the reliability and scalability of LoRaWAN.
MDDPG based slices optimization algorithm in Section IV.
In Section V, we present the simulation results. Finally,
III. SYSTEMMODEL
Section VI discusses the conclusion.
In this section, we design a SDN-based network slicing
II. RELATEDWORK architectureinLoRaWAN.Then,wepresentthesystemmodel
and problem formulation of slice optimization.
Recently, a considerable amount of literature has been
published on network slicing in LoRa-based networks. In [8],
Afolabi et al. presented a comprehensive survey on network A. Network Slicing Architecture
slicing, and discussed the research challenges of these tech-
A typical LoRaWAN architecture consists of end devices,
nologies. In the following, we will briefly discuss related
LoRa gateways, network servers, and application servers. The
works from the perspective of the network slicing and the
gateways are responsible for forwarding messages from end
resource allocation.
devices to network servers. The network servers are respon-
sible for network management functions, including Over-The-
A. Network Slicing
Air-Activation, message routing, acknowledgment of mes-
MuchofthecurrentliteratureonLoRa-basednetworkspays sages, and adaptive data rate control. The application servers
particular attention to network slicing optimization schemes. areusedtoprocessapplication-specificdatamessagesreceived
Duringthedesignofthealgorithm,itinvolvesthreeproblems, from end devices.
including1)slicingadmissionanddefinitionproblem;2)Inter-
In this paper, we leverage SDN and NFV technologies to
slicingresourcesreservation;3)Intra-sliceresourcesoptimiza-
enhancetheflexibilityandprogrammabilityoftheLoRaWAN.
tion[9].In[10],Dawalibyetal.formulatedtheslicingadmis-
As shown in Fig. 1, we present a network slicing architec-
sionanddefinitionasaone-to-manymatchinggame,theinter-
ture over SDN-based LoRaWAN. The architecture runs on
slicing problem as a Bankruptcy resource reservation game,
open-speccommoditycomputeandnetworkinghardware,and
and the intra slice resource allocation as a multi-objective
connects with the LoRa gateways. All the network functions
optimization problem. In [8], the author uses the maximum
are built on micro-services, hosted into containers, and or-
likelihoodestimation(MLE)algorithmtodynamicallyreserve
chestrated with Kubernetes. In our architecture, it contains
LoRa gateways’ bandwidth resource for each slice (i.e., inter-
three layers, named Application Plane, Control Plane, and
slicing resources reservation). In [11], the author proposed a
Infrastructure Plane.
GMMandTOPSISalgorithmtooptimizeintra-sliceresources
Application Plane: In this plane, the applications can issue
(i.e., SF and TP configuration). The experiment result shows
their QoS requirements and desired network behavior to the
that the TOPSIS can effectively enhance slice utility in terms
control plane via northbound application program interfaces.
of throughput, reliability, and delay. In [10], Messaoud et al.
Meanwhile, it can leverage network information (e.g., net-
proposedadeepfederatedQ-Learning(DFQL)baseddynamic
work topology, network state) for its internal decision-making
slices approach to maximize self-QoS requirements. In this
purposes. According to different QoS, the applications can
paper, considering that LoRaWAN is mainly used in fixed
be classified into three types, including best effort (BE),
IoT devices, we assume the previous two problems can be
reliabilityaware(RA),andurgencyandreliabilityaware(UR).
well solved by a general solution (e.g., convex optimization
The URA application requires the highest priority. Examples
method).Therefore,weonlyfocusontheintra-sliceresources
include emergency alerting and robot arm control. The RA
allocation problem.
applications require lower priority (e.g., security systems),
while the BE require the lowest priority (e.g., smart metering
B. Resource Allocation applications) [16].
Recently,alargeandgrowingbodyofliteraturehasinvesti- Control Plane: The control plane is composed of multiple
gatedtheresourceallocationprobleminLoRaWAN.Research- SDN controllers. The controller can translate the application
es always employ the Adaptive Data Rate (ADR) scheme to requirements to the infrastructure plane and provide global
minimize energy consumption and maximize throughput by network abstractions of the LoRaWAN to the application
adjusting the SF and TP configuration. In [12], Kufakunesu plane [17]. According to the complete knowledge of network
et al. present a comprehensive survey on ADR Optimization state and applications QoS, the controller can split physical
in LoRaWAN. In [13], Ilahi et al. proposed a LoRaDRL network resources (e.g., channels on LoRa gateways) for
algorithm. It leverages the deep reinforcement learning al- different slices, and assign IoT devices to the corresponding
gorithm to dynamically optimize parameters configuration. slice.

3
where L is the packet length. Based on this, we define a QoS
ApplicationPlane
metric uDj,g to measure the delay and throughput of slice j,
emergency robot arm security smart QoS
alerting control systems …… metering which can be formulated as:
Northbound uDj,g = (cid:88) (r¯ +(1−t¯)),
QoS d d (3)
Control Plane
C c on SD trC N ool ln S e D tr Cr N ool ln S e D trr N ol ler where r¯ and t¯ indicate d∈ t D h j e ,g normalized value of throughput
d d
and transmission delay respectively.
Southbound
2) Energy Efficiency Metric: Another evaluation metric of
Slice 1 CNF1 CNF2 CNF3 APP
slice performance is energy efficiency. The energy consump-
Slice 1 CNF1 CNF2 APP tionconsistsoftwostates,includingactivemodeconsumption
Slice 3 CNF1 CNF2 CNF3 APP P j a ,g c and sleep mode P j s , l g eep. Hence, the energy consumption
ofslicej duringaslicingintervaltimeT canbedescribedas:
Infrastructure Plane
Ptt =PacT +PsleepT , (4)
j,g j,g active j,g sleep
IoT Devices LoRaGateway Network Server Application Server where T active is related to the r d and P j a ,g c is related to the
transmission power. According to pervious works [19], we
formulate the unit power consumption as:
Fig.1. NetworkSlicingArchitectureoverSDN-basedLoRaWAN
uDj,g = (cid:88) (1−P ¯tt), (5)
EE j,g
Infrastructure Plane: The infrastructure plane consists of d∈Dj,g
enddevices,LoRagateways,networkservers,andapplications
where P
¯tt
is the normalized energy consumption.
j,g
servers. The LoRa gateways are connected in a star of stars
3) Reliability Metric: The third evaluation indicator is re-
network topology. And the network servers, and applications
liability. Configuring low SF and TP values may cause packet
servers are hosted into containers. Each gateway will reserve
loss due to sensitivity, inter-SF, and intra-SF interference. To
channels resources for each slice according to the configura-
evaluate the reliability of transmission, we design the packet
tion issued by the SDN controller. And the container-based
success rate metric
uDj,g
, which can be formulated as:
REL
network server will be dynamically orchestrated according to
controller commands [18]. uDj,g = (cid:88) PSR ,
REL d,j
d∈Dj,g (6)
B. System Model with PSR =PRtra+PRtre+PRsen,
d,j d,j d,j d,j
Consider a network consisting of a set of LoRa gate- wherePSR ,PRtra,PRtre andPRsen arebinaryvariable.
ways G = {1,...,G}, and a set of industrial IoT devices ThePRtra i d n ,j dicate d s ,j thepac d k ,j etslostca d u ,j sedbycollisionsthat
D ={1,...,D}. We assume that each device will be assigned d,j
occurbetweentwoenddevicesconfiguredwiththesameSF.
to a specified network slice j ∈ J = {1,...,J} of the According to the random access formula, the PRtra can be
closest gateway according to its QoS. Each gateway will d,j
described as:
reserve its channel resource C = {1,...,C} for each slice, PRtra =1−e−2GSF, (7)
where c denote the channel associated to the slice j on d,j
j,g
the gateway g. Each channel has its corresponding bandwidth where G SF is the number of packets generated when one
b ∈ B = {1,...,B}. To evaluate the slice performance, we packet is transmitted.
design three evaluation metrics, named Throughput&Delay The PRtre indicates the packets lost due to the inter SF
d,j
Metric, Energy Efficiency Metric, and Reliability Metric. We interference. The devices experience a Signal-to-interference-
will detail the design in the following. plus-noise ratio (SINR), which can be described as:
1) Throughput&Delay Metric: The first evaluation indi- Prx
cator is throughput and delay. In LoRaWAN, each device SINR i,j = σ2+ (cid:80) i Prx , (8)
adopts a specific spreading factor (varying between 7 and 12) n∈∂j n,j
for message transmission, which means each symbol will be where Pac is the transmission power with SF = i, and
i
encoded into 2SF signals (chips). Thus, the LoRa modulation σ2 is the white Gaussian Noise. The below matrix denotes
data rate can be formulated as: the minimum signal power margin threshold with other SF
b configuration [10].
r =SF · j,g ·CR bits/s,∀d∈D , (1)
d 2SF j,g SF SF SF SF SF SF
7 8 9 10 11 12
where r d denotes the LoRa modulation bit rate of device d, SF 7  −6 16 18 19 19 20 
CR denotes the code rate, and b j,g denotes the bandwidth SF 8  24 −6 20 22 22 22 
assigned for slice j on the gateway g. Then, the transmission SF 9   27 27 −6 23 25 25  
delay can be expressed as: SF 10   30 30 30 −6 26 28  
 
L SF 11 33 33 33 33 −6 29 
t = seconds,∀d∈D , (2)
d r d j,g SF 12 36 36 36 36 36 −6

4
TABLEI
LISTOFMAINNOTATIONS
IV. TRANSFERMULTI-AGENTREINFORCEMENT
LEARNING
Parameter Definition
In this paper, we introduce the DDPG algorithm to search
SF SpreadingFactor
TP TransmissionPower the optimal SF and TP parameters of each slice. Then, to
G Numberofgateways acceleratethelearningrate,thetransferlearningframeworkis
J Numberofslices
introduced.
C Numberofchannel
D NumberofindustrialIoTdevices
r
d
ThetheLoRamodulationdatarateofdeviced
bj,g Thebandwidthassignedforslicej onthegatewayg A. Markov Decision Process
Ptt Thetheenergyconsumptionofslicejduringaslicinginterval
j,g The slice optimization problem can be described as an
timeT
PRtra Thepacketslostcausedbyintra-SFcollisions independent Markov Decision Process (MDP) [21]. Formally,
d,j
PRtre Thepacketslostcausedbyintre-SFcollisions anMDPcanbeformalizedasa4-tuple<S,A,π,R>,where
d,j
PRsen Thepacketslostwhenapacketistransmittedtothegateways S is the state space, A is the action space, Π is the policy
d,j
belowsensitivity
space,andR istheimmediaterewards.Ateachstep,theslice
u
Dj,g
Thesatisfactionrateofslicejintermsofdelayandthrough-
QoS agenttakesanactiona∈Aaccordingtocurrentpolicyπ(a|s)
put
u
Dj,g
Thesatisfactionrateofslicej intermsofenergyefficiency
and its observation s ∈ S. Then, the underlying environment
u E D E j,g Thesatisfactionrateofslicej intermsofreliability will generate an immediate reward R, and the state s will
REL transit to a new state s(cid:48) ∈S. Specifically, in our scenario, we
will define the three components of MDP in the following.
Hence, the PRtre can be formulated as: 1) State Definition: In this paper, we define the environ-
d,j ment state as the device information and packet information.
(cid:40) The device information includes spreading factors, transmis-
0, if packet survives interference
PRtre = sion power, bandwidth, and energy consumed (ENY). And
d,g 1, Otherwise
the packet information includes signal-to-noise ratio (SNR),
receivedsignalstrengthindicator(RSSI),andthetotalnumber
In addition, the PRsen indicates the packets lost when a
d,j ofpacketsduringaunittime(Num).Thesevaluesareencoded
packet is transmitted to the gateways below sensitivity, which
in an one-hot format, which can be represented as:
can be expressed as:
S =(S¯F,T¯P,B¯W,EN¯Y,SN¯R,RS¯SI,Nu¯m). (11)
(cid:40)
0, if packet successfully reaches j ∈J
PRsen =
d,g 1, Otherwise All the values are average values over an interval period.
2) ActionDefinition: Inthispaper,wedefinetheactionas:
A=(SF,TP). (12)
C. Problem Formulation
In LoRa, the SF’s value range is {7,8,9,10,11,12}, and T-
At this stage, we can formulate a multi-objective opti-
P’s value range is {2dBm,5dBm,8dBm,11dBm,14dBm}.
mization problem. We search for the optimum SF and TP
Therefore, there exist 30 actions in the action space.
configurationthatcansimultaneouslyenhancetheslice’sQoS,
3) Reward Function: In this paper, the optimization goal
energy efficiency, and reliability. This optimization problem
needstoconsiderthroughput,energyefficiency,andreliability
can be formulated as:
simultaneously. Thus, we define the reward function as:
maxuDj,g =uD Q j o , S g +uD E j E ,g +uD RE j,g L , (9) R(a,s)=uDj,g =αuDj,g +βuDj,g +γuDj,g , (13)
QoS EE REL
subject to the following constraints: where α, β, and γ are system weight parameters. Different
(cid:92) values indicate different preferences of the slice QoS require-
C1:d d =∅,∀j,j(cid:48)∈J,∀g ∈G (10a)
j,g j(cid:48),g ment. For example, a larger γ should be adopted in the URA
C2:d (cid:92) d =∅,∀j ∈J,∀g,g(cid:48)∈G (10b) slice for the sake of better transmission reliability.
j,g j,g(cid:48)
C3:0≤Pac ≤Pmax, (10c)
j,g
(cid:88) B. Deep Deterministic Policy Gradient
C4: r ≤Rmax. (10d)
d j,g
In this paper, we introduce the DDPG to learn the optimal
d∈Dj,g
slice configuration policy. DDPG is a model-free off-policy
The constraint C1 ensures that one device can only be RLalgorithmthatcombinesthedeepQ-Network(DQN)algo-
allocated to one slice. C2 ensures that one device can only rithm and deterministic policy gradient (DPG) algorithm [22].
be allocated to one gateway. C3 ensures that the transmission As shown in Fig. 2, it is composed of two neural network
power is limited to the maximum power. And C4 ensures components, termed as critic and actor. The actor function
that the total transmission power is limited to the maximum µ(s|θµ) specifies action a given the current state s of the
rate [20]. As shown in Table I, we list the notations of this environments. Critic value function Q(s,a|θQ) specifies a
paper. signal (TD Error) to criticize the action made by the actor.

5
Critic Network Actor Network
Data Policy Config
Optimizer Optimizer
update Q-value update policy a
gradient gradient
Training
𝑄𝑄 Online 𝜇𝜇 Online Controller
𝜃𝜃 𝜃𝜃 action Slice
Network: Network:
𝑄𝑄 gra𝑎𝑎dient 𝑄𝑄 Well- Transfer Learning
Soft𝜃𝜃 Soft 𝜃𝜃 Data trained
update update Models
𝑦𝑦𝑡𝑡
Target Target a
Network: Network: Training
𝑄𝑄′ 𝑎𝑎𝑎 𝑄𝑄′
𝜃𝜃 𝜃𝜃 Slice1
𝑎𝑎
Sample Mini-batch Gateway
a
Environment Training
E(x𝑠𝑠p𝑡𝑡e,r𝑎𝑎ie𝑡𝑡n,c𝑟𝑟e𝑡𝑡, b𝑠𝑠u𝑡𝑡+ff1er) s Slice2
Fig.2. TheDDPGAlgorithm.
Fig.3. TransferReinforcementLearning
For the actor-network, the objective function can be de-
scribed as:
J(θµ)=E θµ [r 1 +γr 2 +γ2r 3 +...]. (14) (cid:40) online:Q(s,a|θQ):gradientupdateθQ
The actor-network will update the parameters θµ toward the Qnetwork (cid:48) (cid:48) (19)
target:Q(s,a|θQ ):softupdateθQ
direction of increasing J(θ). The gradient of the objective
J(θµ) can be expressed as:
In DDPG, the weights of targets are updated based on the
∂J(θµ) ∂Q(s,a|θQ)∂µ(s|θµ) main networks periodically, which can be formulated as:
=E [ ]. (15)
∂θµ s ∂a ∂θµ  (cid:48) (cid:48)
θQ ←τθQ+(1−τ)θQ
For the critic network, it calculates the Q-value of the softupdate: (20)
observation-actionpair(s,a)tomeasuretheprofitofactiona θµ (cid:48) ←τθµ+(1−τ)θµ (cid:48)
under a specific state s. The update of the critic network θQ
can be described as:
∂L(θQ) ∂Q(s,a|θQ) C. Transfer Reinforcement Learning
∂θQ
=E s,a,r,s(cid:48)[(TargetQ−Q(s,a|θQ))
∂θQ
], (16)
As discussed above, the DDPG agent can learn from its
where experience and improve its performance by exploring the
TargetQ=r+γQ (cid:48) (s (cid:48) ,µ(s (cid:48) |θµ (cid:48) )|θQ (cid:48) ). (17) environment. However, such learning mechanism has to take
a large number of training episodes to converge the optimal
Besides, to stabilize the training process, DDPG adopts the value. Especially in our scenario, multiple slice agents are co-
Experience Replay and Target Networks scheme. existed.EachRLagenthastolearnfromscratch,andtherefore
Experience Reply: Experience Replay is a replay memory reduce the system utility.
technique, where agent’s experiences are stored as a tuple of To accelerate the learning process across multiple agents,
[s t ,a t ,r t ,s t+1 ] in a replay buffer D. During the training, the thetransferlearningtechniquesareintegratedintoourmethod
RL agent randomly drew a mini-batch of experience from to facilitate the learning process. Transfer learning is a ma-
D to train the network. Such storage-sampling act effectively chinelearningmethodthatthelearnedmodels’trainedfroma
addresses the unstable training problem caused by the auto- taskarereusedasthestartingpointfornewmodelsonanother
correlation among training data [23]. task[24].Differentfromtheisolatedlearningparadigm,trans-
Target Network: During the training, since the learning fer learning exploits the knowledge acquired from previous
objectconstantlychanges,thevalueTDestimationscaneasily taskstoimprovegeneralizationandlearningrateaboutrelated
spiral out of control. To mitigate that risk, the target network ones.
is introduced. The target network’s weights are fixed during Combining with the transfer learning methods, as shown
the learning process, and periodically reset to the original in Fig. 3, we propose a transfer multi-agent Deep Deter-
network’s values. ministic Policy Gradient (TMDDPG) scheme. At the first
In DDPG, we define the target critic network and target
stage, the centralized controller gathers the data experience
actor-network to calculate the Q-value for the next state in
[s ,a ,r ,s ] from the distributed gateways to construct a
TD-error computations: t t t t+1
replaybufferandtrainthemodel.Afterconvergence,thewell-
(cid:40)online:µ(s|θµ):gradientupdateθµ
trained networks models will be issued to each gateway and
policynetwork (cid:48) (cid:48) (18)
target:µ(s|θµ ):softupdateθµ used as the starting point on local slice optimization tasks.

6
simulation environment, and PyTorch 1.4.0 for implementing
neural networks.
A. Simulation Settings
In our experiment, we simulate a LoRa-based network
with 4 gateways (i.e., G = 4). The number of slices on
each gateway is 3, and the number of industrial IoT device
assigned to each slice range from 100 to 1000. We assume
that gateways and devices are uniformly distributed in a
cell of a 10KM radius. In addition, the number of channels
per slice varies from 1−3 and each channel Bandwidth is
125kHz.TheSF’svaluerangeis{7,8,9,10,11,12},andTP’s
valuerangeis{2dBm,5dBm,8dBm,11dBm,14dBm}.The
detailed parameters setting can be found in Table II.
Fig.4. TheConvergenceAnalysis TABLEII
SIMULATIONPARAMETERS
Algorithm 1 The TMDDPG based slicing optimization algo-
Parameter Value
rithm
Numberofgateways 4
Import pre-trained model and replay buffer data from SDN Numberofslice 3
controller Numberofdevicesperslice 100to1000
Initialized online network weights θQ,θµ NumberofChannelsperslice 1to3
(cid:48) (cid:48) ChannelBandwidth 125kHz
Initialized target network weights θQ ←θQ,θµ ←θµ Gatewaysanddevicesdistribution Uniformdistribution
for step = 1 to maximum episode length do do Trainingbatchsize 25000 steps
SpreadingFactor 7to12
Observe initial state s
0 Transmitpower 2to14dBm
for step = 1 to maximum episode duration do
Takes an action according to the current policy:
a =µ(s |θµ)+N
t t t
Execute action a and receive a new state s
t t+1 B. Convergence Analysis
Storage the transition in R
First, we evaluate the convergence of our proposed algo-
Sample a batch of experiences
R×(s,a,r,s(cid:48)) from replay buffer rithm. We adopt two other reinforcement learning algorithms,
DDPGandDQN,asthebaselinealgorithms.Theconfiguration
Calculate TD target of Q-network:
y =r +γQ(cid:48)(s ,µ(cid:48)(s |θµ (cid:48) )|θQ (cid:48) ) of TMDDPG, DDPG, and DQN are shown in Table. III.
i i i+1 i+1 AsshowninFig.4,thelearningprocessofthreealgorithms
Update online Q-network by minimizing the loss:
L= 1 (cid:80) (y −Q(s ,a |θQ))2 is demonstrated. We notice that three algorithms can all con-
N i i i verge to a near reward. This demonstrates that reinforcement
i
Update online policy network with: learning is capable of improving policy performance through
∇ θµ J ≈ N 1 (cid:80) ∇ a Q(s,a|θQ)∇ θµ | s=si,a=µsi µ(s|θµ)| si interacting with the environment. Also, we notice that TMD-
i DPGexhibitsabetterconvergencecomparedtotheDDPGand
Update the target networks by:
(cid:48) (cid:48) theDQN.TheTMDDPGcanobtainstablerewardaround500
θQ ←τθQ+(1−τ)θQ
(cid:48) (cid:48) episodes,whileDQNaround1300episodesandDDPGaround
θµ ←τθµ+(1−τ)θµ
1700episodes.ThisisbecauseTMDDPGacquiresknowledge
end for
fromprevioustasks,withouthavingtorestarttrainingfromthe
end for
scratch.
TABLEIII
Moreover, the experience memory pool of each slice agent TMDDPG&DDPG&DQNCONFIGURATION
is imported by well-trained model experience in the SDN
Parameter Value
controller.
Episodemaximumduration 100s(100steps)
The slice optimization policy of the TMDDPG algorithm is Maximumepisode 20000episodes
shown in detail in Algorithm 1. Discountfactor(γ) 0.95
Learningrate(α) 0.01
Trainingbatchsize 25000 steps
V. SIMULATIONRESULTS
Replaybuffersize 100
Inthissection,wepresentthesimulationresultstoevaluate Minibatchsize 10
Hiddenlayersize 64
thevalidityoftheproposedalgorithm.Ourexperimentssimu-
Stepduration(τ) 1s
lateUbuntu16.04with32gRAM,NvidiaRTX2060,andintel
i7-10875H. We use OMNET++ for building the LoRaWAN

7
Fig.5. ThePerformanceEvaluation. Fig.6. TheDelayinDifferentSlices.
| C. Performance |     | Analysis |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Inthispart,weevaluatethealgorithmperformanceinterms
| of network | reliability. | Two | classical | SF-TP | adjust | algorithm, |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --------- | ----- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
termeddynamicrandom(DR)algorithmanddynamicadaptive
| (DA), are | set as           | the baseline, | where  | the       | DR configure |     | the SF |     |     |     |     |     |     |     |
| --------- | ---------------- | ------------- | ------ | --------- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
| and TP    | values randomly, |               | and DA | configure | the          | SF  | and TP |     |     |     |     |     |     |     |
valuesbasedonlinkqualitywithspecificSF-TPpair,including
| (7,2dbm), | (8,5dbm), | (9,8dbm), |     | (10,11dbm), | (11,14dbm) |     | and |     |     |     |     |     |     |     |
| --------- | --------- | --------- | --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(12,14dbm).
| As shown          | in            | Fig. 5,      | we present |           | the packet  | loss   | rate   |     |     |     |     |     |     |     |
| ----------------- | ------------- | ------------ | ---------- | --------- | ----------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| (PLR) of          | the different | algorithms.  |            | With      | the         | number | of de- |     |     |     |     |     |     |     |
| vices increasing, |               | the PLR      | increase.  | This      | is          | mainly | caused |     |     |     |     |     |     |     |
| by the increase   |               | of inter-and | intra-     | collision | probability |        | with   |     |     |     |     |     |     |     |
the number of devices increasing. Besides, we notice that Fig.7. TheEnergyConsumptioninDifferentSlices.
| reinforcement | learning | algorithms  |      | exhibit      | better | performance |          |     |     |     |     |     |     |     |
| ------------- | -------- | ----------- | ---- | ------------ | ------ | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| than DA       | and DR   | algorithms. | This | demonstrates |        | the         | validity |     |     |     |     |     |     |     |
and effectiveness of our proposed algorithm. enhance system reliability. Hence, the data rate will decrease
|     |     |     |     |     |     |     |     | and the transmission |     | delay | will increase. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----- | -------------- | --- | --- | --- |
Also,wenoticethattheURandRA’sdelayisalwayslower
| D. Slice | Performance | Analysis |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thantheBEslice.ThereasonisthatURandRAslices’reward
In this part, we will evaluate the different kinds of slice’s functions are configured with the higher α and γ. The agent
performance in terms of delay, energy efficiency, and packet will gain more profit with the higher throughput and lower
| loss rate. | As discussed | above, | we  | define | three | types of | slices, | delay. |     |     |     |     |     |     |
| ---------- | ------------ | ------ | --- | ------ | ----- | -------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
i.e., UR, RA, and BE. Each type agent adopts different 2) Energy Evaluation: Then, we present the energy con-
weightparametersintherewardfunctionformeetingtheQoS sumption of different slices. As shown in Fig. 7, with the
|     |     | α   |     |     |     | β   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
preference, where indicates the QoS weight, indicates the number of devices increasing, the total energy consumption
energyefficiencyweight,andγ indicatesthereliabilityweight. alsoincreases.That’sbecausethatmoreparticipantswillbring
| We detail | the parameter’s |     | value   | in Table. | IV. |     |     |                                                    |             |        |              |              |     |              |
| --------- | --------------- | --- | ------- | --------- | --- | --- | --- | -------------------------------------------------- | ----------- | ------ | ------------ | ------------ | --- | ------------ |
|           |                 |     |         |           |     |     |     | more energy                                        | consumption |        | to the total | consumption. |     | Besides,     |
|           |                 |     |         |           |     |     |     | we notice                                          | that the    | energy | consumption  | of UR        | is  | always lower |
|           |                 |     | TABLEIV |           |     |     |     | thantheRAandBE.ThisisbecausethatUR’srewardfunction |             |        |              |              |     |              |
SLICEPARAMETERSCONFIGURATION
|     |       |        |     |       |         |     |     | adopts a | higher   | value of | γ, which | forces | the agent | to take    |
| --- | ----- | ------ | --- | ----- | ------- | --- | --- | -------- | -------- | -------- | -------- | ------ | --------- | ---------- |
|     |       |        |     |       |         |     |     | a higher | TP value | compared | to the   | RA     | and BE    | for higher |
|     | Slice | αvalue | β   | value | γ value |     |     |          |          |          |          |        |           |            |
UR 0.4 0.1 0.5 reliability. And increasing SF and TP values will increase
|     | RA  | 0.4 | 0.2 |     | 0.4 |     |     |                     |       |              |           |           |        |               |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | ----- | ------------ | --------- | --------- | ------ | ------------- |
|     |     |     |     |     |     |     |     | energy consumption. |       | In addition, | the       | BE’s      | reward | adopts the    |
|     | BE  | 0.3 | 0.4 |     | 0.3 |     |     |                     |       |              |           |           |        |               |
|     |     |     |     |     |     |     |     | highest β,          | which | drives       | the agent | to adjust | its    | policy to the |
|     |     |     |     |     |     |     |     | lower consumptions  |       | direction.   |           |           |        |               |
1) Delay Evaluation: Firstly, we evaluate the delay perfor- 3) Packet Loss Rate Evaluation: We plot the PLR perfor-
manceofdifferentslices.AsshowninFig.6,withthenumber mance in Fig. 8. With the devices increasing, the PLR will
of devices increasing, the delay also increases. This is caused also increase subsequently. This is because that more packets
by inter-and intra- interference. With the collision probability will be transferred at the same time, and therefore aggravated
increasing, the gateway has to set higher SF and TP values to the inter-and intra- problem. Besides, the PRL of UR is lower

8
[6] J. Wang, C. Jiang, H. Zhang, Y. Ren, K.-C. Chen, and L. Hanzo,
“Thirtyyearsofmachinelearning:Theroadtopareto-optimalwireless
networks,” IEEE Communications Surveys & Tutorials, vol. 22, no. 3,
pp.1472–1514,2020.
[7] S. J. Pan and Q. Yang, “A survey on transfer learning,” IEEE Trans-
actionsonknowledgeanddataengineering,vol.22,no.10,pp.1345–
1359,2009.
[8] I.Afolabi,T.Taleb,K.Samdanis,A.Ksentini,andH.Flinck,“Network
slicing and softwarization: A survey on principles, enabling technolo-
gies,andsolutions,”IEEECommunicationsSurveys&Tutorials,vol.20,
no.3,pp.2429–2453,2018.
[9] S. Dawaliby, A. Bradai, and Y. Pousset, “Adaptive dynamic network
slicinginloranetworks,”Futuregenerationcomputersystems,vol.98,
pp.697–707,2019.
[10] S.Dawaliby,A.Bradai,andY.Pousset,“Distributednetworkslicingin
largescaleiotbasedoncoalitionalmulti-gametheory,”IEEETransac-
tions on Network and Service Management, vol. 16, no. 4, pp. 1567–
1580,2019.
[11] S. Dawaliby, A. Bradai, and Y. Pousset, “Joint slice-based spreading
Fig.8. PacketLossRateinDifferentSlices.
factorandtransmissionpoweroptimizationinlorasmartcitynetworks,”
InternetofThings,p.100121,2019.
[12] R.Kufakunesu,G.P.Hancke,andA.M.Abu-Mahfouz,“Asurveyon
than the RA and BE, and there are obvious reasons for that. adaptivedatarateoptimizationinlorawan:Recentsolutionsandmajor
challenges,”Sensors,vol.20,no.18,p.5044,2020.
These results demonstrate that the TMDDPG can dynam-
[13] I.Ilahi,M.Usama,M.O.Farooq,M.U.Janjua,andJ.Qadir,“Intelligent
ically optimize slice performance by adjusting the SF and resource allocation in dense lora networks using deep reinforcement
TP parameters configuration. Besides, the reward function learning,”arXivpreprintarXiv:2012.11867,2020.
[14] G. Park, W. Lee, and I. Joe, “Network resource optimization with
design can directly affect the performance in terms of delay,
reinforcement learning for low power wide area networks,” EURASIP
energy efficiency, and reliability. The slice agent can adjust JournalonWirelessCommunicationsandNetworking,vol.2020,no.1,
the reward’s weights (i.e., α, β, γ) for acquiring different pp.1–20,2020.
[15] B. Reynders, Q. Wang, P. Tuset-Peiro, X. Vilajosana, and S. Pollin,
performance preferences.
“Improving reliability and scalability of lorawans through lightweight
scheduling,”IEEEInternetofThingsJournal,vol.5,no.3,pp.1830–
1842,2018.
VI. CONCLUSION [16] B. K. Al-Shammari, N. Al-Aboody, and H. S. Al-Raweshidy, “Iot
trafficmanagementandintegrationintheqossupportednetwork,”IEEE
Inthispaper,wediscussanetworkslicingarchitectureover InternetofThingsJournal,vol.5,no.1,pp.352–370,2017.
SDN-based LoRaWAN, where an SDN controller divides Lo- [17] K. Benzekki, A. El Fergougui, and A. Elbelrhiti Elalaoui, “Software-
defined networking (sdn): a survey,” Security and communication net-
Ragateways’physicalresourcesintomultiplevirtualnetworks
works,vol.9,no.18,pp.5803–5833,2016.
to provide different QoS guarantees. In addition, considering [18] C.Qiu,H.Yao,C.Jiang,S.Guo,andF.Xu,“Cloudcomputingassisted
the limited number of available channels on each LoRa blockchain-enabled internet of things,” IEEE Transactions on Cloud
Computing,2019.
gateway, slices may suffer from performance degradation
[19] O.GeorgiouandU.Raza,“Lowpowerwideareanetworkanalysis:Can
and resource starvation. To tackle this problem, we propose lora scale?” IEEE Wireless Communications Letters, vol. 6, no. 2, pp.
a DDPG based slice optimization algorithm to search the 162–165,2017.
[20] K. Xue, B. Zhu, Q. Yang, N. Gai, D. S. Wei, and N. Yu, “Inpptd:
optimal SF and TP parameters configurations. In addition, to
A lightweight incentive-based privacy-preserving truth discovery for
acceleratethelearningprocessacrossmultipleLoRagateways, crowdsensingsystems,”IEEEInternetofThingsJournal,vol.8,no.6,
a multi-regional intelligent slicing optimization algorithm that pp.4305–4316,2020.
[21] T. Mai, H. Yao, N. Zhang, L. Xu, M. Guizani, and S. Guo, “Cloud
utilizes transferred knowledge from network service is pro-
miningpoolaidedblockchain-enabledinternetofthings:Anevolution-
posed. The experimental results show that the TMDDPG can arygameapproach,”IEEETransactionsonCloudComputing,pp.1–1,
dynamically optimize slice performance by adjusting the SF 2021.
[22] Y. He, G. Han, J. Jiang, H. Wang, and M. Martinez-Garcia, “A
and TP parameters configurations.
trustupdatemechanismbasedonreinforcementlearninginunderwater
acoustic sensor networks,” IEEE Transactions on Mobile Computing,
2020.
REFERENCES [23] B.Eysenbach,R.Salakhutdinov,andS.Levine,“Searchonthereplay
buffer: Bridging planning and reinforcement learning,” arXiv preprint
[1] G.Han,J.Tu,L.Liu,M.Martinez-Garcia,andC.Choi,“Anintelligent arXiv:1906.05253,2019.
signalprocessingdatadenoisingmethodforcontrolsystemsprotection [24] M.E.TaylorandP.Stone,“Transferlearningforreinforcementlearning
in the industrial internet of things,” IEEE Transactions on Industrial domains: A survey.” Journal of Machine Learning Research, vol. 10,
Informatics,2021. no.7,2009.
[2] A. Lavric and V. Popa, “Internet of things and lora low-power wide-
areanetworks:asurvey,”in2017InternationalSymposiumonSignals,
CircuitsandSystems(ISSCS),pp.1–5. IEEE,2017.
[3] G. Han, J. Tu, L. Liu, M. Mart´ınez-Garc´ıa, and Y. Peng, “Anomaly
detectionbasedonmultidimensionaldataprocessingforprotectingvital
devices in 6g-enabled massive iiot,” IEEE Internet of Things Journal,
vol.8,no.7,pp.5219–5229,2021.
[4] S.WijethilakaandM.Liyanage,“Surveyonnetworkslicingforinternet
ofthingsrealizationin5gnetworks,”IEEECommunicationsSurveys&
Tutorials,vol.23,no.2,pp.957–994,2021.
[5] M. Bor, J. E. Vidler, and U. Roedig, “Lora for the internet of things,”
2016.

9
Tianle Mai is pursuing his Ph.D. degree in the Mohsen Guizani (S’85-M’89-SM’99-F’09) re-
School of Information and Communication Engi- ceived the BS (with distinction), MS and PhD de-
neering, Beijing University of Posts and Telecom- grees in Electrical and Computer engineering from
munications,Beijing.Hisresearchinterestsinclude Syracuse University, Syracuse, NY, USA, in 1984,
future network architecture, network artificial in- 1986, and 1990, respectively. He is currently a
telligence, multi-agent system, space-terrestrial in- Professor and Associate Provost at MBZUAI, Abu
tegrated network, network resource allocation and Dhabi, UAE. Previously, he worked in different
dedicatednetworks. institutionsintheUSA:UniversityofIdaho,Western
|     |     |     |     |     |     |     |     |     | Michigan   | University,  | University | of         | West Florida, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | ---------- | ---------- | ------------- |
|     |     |     |     |     |     |     |     |     | University | of Missouri, |            | University | of Colorado-  |
Boulder,andSyracuseUniversity.Hisresearchinter-
estsincludewirelesscommunicationsandmobilecomputing,appliedmachine
learning,cloudcomputing,securityanditsapplicationtohealthcaresystems.
|     |     |     |     |     |     |     | He was elevated | to  | the IEEE | Fellow in 2009. | He  | was listed | as a Clarivate |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | --------------- | --- | ---------- | -------------- |
Haipeng Yao (M’16, SM’20) is an Associate Pro- Analytics Highly Cited Researcher in Computer Science in 2019, 2020 and
fessor in Beijing University of Posts and Telecom- 2021.Dr.Guizanihaswonseveralresearchawardsincludingthe2015IEEE
|     |     |              |     |         |              |     | Communications | Society | Best | Survey Paper | Award | as well | 4 Best Paper |
| --- | --- | ------------ | --- | ------- | ------------ | --- | -------------- | ------- | ---- | ------------ | ----- | ------- | ------------ |
|     |     | munications. |     | Haipeng | Yao received | his | Ph.D. in       |         |      |              |       |         |              |
AwardsfromICCandGlobecomConferences.Heistheauthorofninebooks
|     |     | the | Department | of Telecommunication |            | Engineering |          |          |               |            |               |     |               |
| --- | --- | --- | ---------- | -------------------- | ---------- | ----------- | -------- | -------- | ------------- | ---------- | ------------- | --- | ------------- |
|     |     |     |            |                      |            |             | and more | than 800 | publications. | He is also | the recipient | of  | the 2017 IEEE |
|     |     | at  | University | of Beijing           | University | of Posts    | and      |          |               |            |               |     |               |
Telecommunications in 2011. His research inter- CommunicationsSocietyWirelessTechnicalCommittee(WTC)Recognition
ests include future network architecture, network Award, the 2018 AdHoc Technical Committee Recognition Award, and the
2019IEEECommunicationsandInformationSecurityTechnicalRecognition
|     |     | artificial | intelligence, |     | networking, | space-terrestrial |                |     |        |                        |     |         |                |
| --- | --- | ---------- | ------------- | --- | ----------- | ----------------- | -------------- | --- | ------ | ---------------------- | --- | ------- | -------------- |
|     |     |            |               |     |             |                   | (CISTC) Award. | He  | served | as the Editor-in-Chief |     | of IEEE | Network and is |
integratednetwork,networkresourceallocationand
|     |     |           |           |     |               |      | currently | serving on | the Editorial | Boards | of many | IEEE | Transactions and |
| --- | --- | --------- | --------- | --- | ------------- | ---- | --------- | ---------- | ------------- | ------ | ------- | ---- | ---------------- |
|     |     | dedicated | networks. | He  | has published | more | than      |            |               |        |         |      |                  |
100papersinprestigiouspeer-reviewedjournalsand Magazines.HewastheChairoftheIEEECommunicationsSocietyWireless
conferences.Dr.YaohasservedasanEditorofIEEENetwork,IEEEAccess, Technical Committee and the Chair of the TAOS Technical Committee. He
servedastheIEEEComputerSocietyDistinguishedSpeakerandiscurrently
| and a Guest | Editor | of IEEE | Open | Journal of | the Computer | Society | and |     |     |     |     |     |     |
| ----------- | ------ | ------- | ---- | ---------- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- |
theIEEEComSocDistinguishedLecturer.
| Springer Journal | of  | Network | and Systems | Management. |     | He has also | served |     |     |     |     |     |     |
| ---------------- | --- | ------- | ----------- | ----------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- |
asamemberofthetechnicalprogramcommitteeaswellastheSymposium
| Chair for a | number | of international |     | conferences, | including | IWCMC | 2019 |     |     |     |     |     |     |
| ----------- | ------ | ---------------- | --- | ------------ | --------- | ----- | ---- | --- | --- | --- | --- | --- | --- |
SymposiumChair,ACMTUR-CSIGSAC2020PublicationChair.
|     |     | Ni        | Zhang | currently serves | at           | the Sixth        | Research |     |     |     |     |     |     |
| --- | --- | --------- | ----- | ---------------- | ------------ | ---------------- | -------- | --- | --- | --- | --- | --- | --- |
|     |     | Institute | of    | China Electronic | Corporation, |                  | Beijing, |     |     |     |     |     |     |
|     |     | China.    | He    | received his     | Ph. D.       | at the Institute | of       |     |     |     |     |     |     |
|     |     | Computing |       | Technology,      | Chinese      | Academy          | of Sci-  |     |     |     |     |     |     |
encesin2007.Hisresearchinterestsareinthearea
offutureInternetarchitecture,networksecurityand
artificialintelligence.
|     |     | Wenji | He is | currently | an undergraduate | student | at  |     |     |     |     |     |     |
| --- | --- | ----- | ----- | --------- | ---------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
BeijingUniversityofPostsandTelecommunication-
s.Herresearchinterestsareintheareasofcomputer
workingandthesecurityoftheInternet.
|     |     | Dong   | Guo         | received the | B.S.       | degree in communi- |     |     |     |     |     |     |     |
| --- | --- | ------ | ----------- | ------------ | ---------- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
|     |     | cation | engineering | with         | the School | of information     |     |     |     |     |     |     |     |
andCommunicationEngineering,BeijingUniversity
ofPostsandTelecommunication,Beijing,China,in
|     |     | 2012, | and the     | Ph.D. degree | in  | optical engineering |          |     |     |     |     |     |     |
| --- | --- | ----- | ----------- | ------------ | --- | ------------------- | -------- | --- | --- | --- | --- | --- | --- |
|     |     | from  | the Beijing | University   | of  | Posts and           | Telecom- |     |     |     |     |     |     |
munication,in2019.Since2019,hehasbeenapost-
|     |     | doctoral | researcher | with | the School | of Information |     |     |     |     |     |     |     |
| --- | --- | -------- | ---------- | ---- | ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Electronics,BeijingInstituteofTechnology,Beijing.
|     |     | His         | research | interests     | include     | optical fiber | com-   |     |     |     |     |     |     |
| --- | --- | ----------- | -------- | ------------- | ----------- | ------------- | ------ | --- | --- | --- | --- | --- | --- |
|     |     | munication, |          | forward error | correction, | digital       | signal |     |     |     |     |     |     |
processingandhigh-ordermodulation.