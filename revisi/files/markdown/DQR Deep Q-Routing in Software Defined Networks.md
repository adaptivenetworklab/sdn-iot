# DQR Deep Q-Routing in Software Defined Networks

> Source file: `DQR Deep Q-Routing in Software Defined Networks.pdf`

---

DQR: Deep Q-Routing in Software Defined
Networks
Syed Qaisar Jalil, Mubashir Husain Rehmani, and Stephan Chalup
Abstract—In this paper, we investigate the task of quality of add a new traffic flow in the network while maintaining the
service (QoS) routing in software defined networks (SDN). We QoSrequirementsofongoingflows.Ontheotherhand,global
consider delay, bandwidth, loss, and cost as QoS parameters.
offlineQoSroutingconsidersasetofongoingtrafficflowsand
We propose a new deep reinforcement learning solution for
triestodeterminetherouteswhichfulfiltheQoSrequirements
greedy online QoS routing in SDN and call it Deep Q-Routing
(DQR). DQR utilises a dueling deep Q-network with prioritised for the selected set of flows. For QoS routing, extensive
experience replay to compute a path for any source-destination research efforts have been made for different network settings
pairrequestinthepresenceofmultipleQoSmetrics.Incontrast suchaspresentedinthefollowingsurveys[1],[2].Mostofthis
to existing DRL-based routing methods, the proposed DQR
work is model-based where the underlying assumption is that
methodregardsthetaskofroutingasadiscretecontrolproblem
user demand and network environment can be well modelled.
andusesarewardfunctioncomprisingweightedQoSparameters.
Our simulation results show that DQR substantially improves Also, it requires high computational resources to deal with
end-to-endthroughputcomparedtootherexistinglearningbased multiple QoS parameters. On the other hand, communication
methods. networks have evolved into highly dynamic and complicated
Index Terms—Quality-of-service Routing, Deep-Q Learning, networks which makes them hard to model and control.
Software defined network. SincetheproposalofdeepQ-network(DQN)byDeepMind
[3],deepreinforcementlearning(DRL)methodshavebecome
I. INTRODUCTION very popular to be used for complex problems where their
ability to learn from experience allows to avoid the develop-
Software-definednetwork(SDN)isanemergingnetworking
ment of large accurate mathematical models. DRL combines
paradigm that provides features, such as on-demand resource
reinforcementlearning(RL)anddeeplearningtoovercomethe
allocation, easy reconfiguration, and programmable network
limitations faced by RL methods such as dealing with large-
management, which significantly improves network perfor-
scale systems. Specifically, DRL uses deep neural networks
mance.InSDN,networkfunctionalitiesarelogicallyseparated
(DNN) in combination with reinforcement learning methods
into a control plane and data plane. This is one of the key
toimprovethelearningprocess.DRLhasattractedresearchers
featuresthatdifferentiatesSDNfromtraditionalnetworks.The
from various disciplines due to its ability to solve large-scale
control plane includes the SDN controller which is responsi-
complexproblems,forexample,inthefieldofcommunication
ble for implementing all control functionalities required for
and networking [4].
operational decision making. While the data plane includes
In the context of RL based routing, Boyan and Littman
hardware devices (such as switches) responsible for the exe-
proposed in their 1994 paper [5] a Q-learning based packet
cution of the instructions received from SDN controller. The
routing approach called Q-routing. A more recent study by
logically centralised SDN controller has a global view of the
Lin et al. [6] uses RL in a software-defined network and pro-
network that enables network administrators to dynamically
posed a QoS-aware adaptive greedy online routing algorithm.
optimise network resources and provide flow-level quality of
However, due to the use of Q-learning, these approaches do
service (QoS) provisioning.
not perform well when the routing complexity increases, i.e.,
The SDN controller provides application-oriented services
when a larger number of QoS metrics has to be optimised
by running different modules inside the controller for various
in large-scale problems. Some recent studies used DRL for
taskssuchasQoSrouting,resourcereservation,networkmon-
routing in communication networks, e.g., [7]–[9]. These stud-
itoring, and queue management. The QoS routing module is
ies considered global offline routing. They take an ongoing
responsible for providing flow-level QoS in terms of different
traffic flow traffic matrix (TM) and find the solution for TM
parameters such as delay, loss, and bandwidth. It collects
using shortest paths. Specifically, they optimise TM using the
network statistics in real-time and determines the routes for
deepdeterministicpolicygradient(DDPG)algorithmwhichis
different source-destination pairs which satisfy QoS require-
widely used for continuous control problems. However, these
ments. Broadly speaking, QoS routing can be divided into
DRL methods for global offline routing are limited in their
two types: greedy online and global offline [1]. Greedy online
performance because they only consider k-shortest paths for
QoS routing considers individual traffic flows, i.e., it tries to
each source destination pair, whereas there can be other paths
S.Q. Jalil and S. Chalup are with the School of Electrical Engi- which can provide better performance.
neering and Computing, The University of Newcastle, Australia. E-mail: Instead of formulating the routing problem as continuous
syedqaisar.jalil@uon.edu.auandstephan.chalup@newcastle.edu.au
control problem and using k-shortest paths, we formulate it
M.H.RehmaniiswiththeDepartmentofComputerScience,CorkInstitute
ofTechnology(CIT),Ireland.E-mail:dr.m.rehmani@ieee.org as discrete control problem. Specifically, we propose a DQN
978-1-7281-6926-2/20/$31.00 ©2020 IEEE
Authorized licensed use limited to: University of Canberra. Downloaded on October 03,2020 at 12:05:41 UTC from IEEE Xplore. Restrictions apply.

based greedy online QoS routing method. Our formulation dealing with invalid actions, avoiding network loops, and
enables the DRL agent to find a path for each source- optimising different QoS metrics together. To deal with these
destination pair request while optimising QoS metrics. We challenges, we propose DQR which is a dueling DQN with
do not restrict the DRL agent to k-shortest paths rather it PER based greedy online QoS routing method. DQR not only
constructstheroutingpathconsideringthecurrentstateofthe cope with these challenges but also has a flexible design that
networkalongwith anoptimisationofthe QoSmetrics.Thus, makes it topology and network state independent.
| our agent | learns  | the network |     | topology | and | simultaneously |     |     |     |     |     |     |     |
| --------- | ------- | ----------- | --- | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| optimises | the QoS | metrics.    |     |          |     |                |     |     |     |     |     |     |     |
III. DEEPREINFORCEMENTLEARNING
| The organisation |         | of           | the paper  | is        | as follows: | Section         | II        |           |               |         |          |           |                    |
| ---------------- | ------- | ------------ | ---------- | --------- | ----------- | --------------- | --------- | --------- | ------------- | ------- | -------- | --------- | ------------------ |
|                  |         |              |            |           |             |                 | In this   | section,  | we            | present | a brief  | overview  | of deep rein-      |
| provides         | related | work.        | In Section | III       | we          | present a brief |           |           |               |         |          |           |                    |
|                  |         |              |            |           |             |                 | forcement | learning. | Reinforcement |         | learning |           | (RL) is a field of |
| overview         | of DRL. | Section      | IV         | describes | the         | system model    |           |           |               |         |          |           |                    |
|                  |         |              |            |           |             |                 | machine   | learning  | in which      | an      | agent    | interacts | with the system    |
| and the problem  |         | formulation. | In         | Section   | V, we       | present design  |           |           |               |         |          |           |                    |
(environment)andtriestolearnitsbehaviour[18].Particularly,
detailsofDQR.Simulationresultsarepresentedanddiscussed
in Section VI and finally Section VII concludes the paper. at each iteration t, the agent senses the current state s t of
|     |     |     |     |     |     |     | the system, | takes | an action |     | a based | on its | past experience |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --------- | --- | ------- | ------ | --------------- |
t
|     |     |     |     |     |     |     | and receives | a   | reward | r . The | goal | of the | agent is to learn |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | ------- | ---- | ------ | ----------------- |
t
|     |     | II. | RELATEDWORK |     |     |     |            |      |       |          |     |          |               |
| --- | --- | --- | ----------- | --- | --- | --- | ---------- | ---- | ----- | -------- | --- | -------- | ------------- |
|     |     |     |             |     |     |     | the policy | π(s) | which | maximise | the | longterm | reward, i.e., |
(cid:80)T
|     |     |     |     |     |     |     | highest | accumulated | reward | over | time | R = | γtr(s ,a ) |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ------ | ---- | ---- | --- | ---------- |
Recently various methods related to DRL based routing 0 t=0 t t
|     |     |     |     |     |     |     | γ   | ∈[0,1] | r(·) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | --- | --- | --- | --- |
have been proposed. The study [10] proposed supervised where and represent discount factor and reward
function respectively.
| learning | and DRL | based | routing | methods | to optimise | demand |            |     |        |          |         |     |                 |
| -------- | ------- | ----- | ------- | ------- | ----------- | ------ | ---------- | --- | ------ | -------- | ------- | --- | --------------- |
|          |         |       |         |         |             |        | Q-learning | is  | one of | the most | popular | RL  | algorithms that |
matrix.OneoftheearlierstudiesthatutilisedDDPGalgorithm
for routing optimisation was by Stampa et al. [7]. The goal of aims at finding an optimal policy [19]. It can be implemented
|           |       |        |        |          |         |             | using a | Q-table | which | is updated | using |     |     |
| --------- | ----- | ------ | ------ | -------- | ------- | ----------- | ------- | ------- | ----- | ---------- | ----- | --- | --- |
| their DRL | agent | was to | reduce | the mean | network | delay. They |         |         |       |            |       |     |     |
trainedtheirDRLagentona14-nodetopologyfor10different Q (s ,a ):=Q (s ,a )
|     |     |     |     |     |     |     | t+ | t t | t   | t t |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(1)
traffic intensity levels and demonstrated its performance im- +α[R +γmaxQ (s ,a)−Q (s ,a )]
|             |         |       |            |     |           |            |     |     | t   |     | t   | t+1 | t t t |
| ----------- | ------- | ----- | ---------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | ----- |
| provements. | Various | later | approaches |     | using the | DDPG algo- |     |     |     | a   |     |     |       |
rithmaddresseddifferentapplicationsanddifferentobjectives. where α is the learning rate and γ ∈ [0,1] represents
Forinstance,Huangetal.[11]proposedaDDPGbasedquality the discount factor which is used to control the effect of
of experience optimisation method for multimedia traffic. Xu immediate and later rewards. The main idea is to find the
et al. [8] proposed experience driven routing. They proposed temporal difference between predicted and current Q-values.
traffic engineering (TE) aware exploration and actor-critic In a state s, the true value of an action a under policy π is
basedprioritisedexperiencereplayinconjunctionwithDDPG Q (s,a)≡E[R +γR +...|S =s,A =a,π].Ineachstate,
|     |     |     |     |     |     |     | π   |     | 1   | 2   | 0   | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
algorithm for optimising delay. Later they proposed another optimal value is calculated by selecting the highest valued
DRL method for multi-path TCP congestion control [12]. action, i.e., Q (s,a) = max Q (s,a), and therefore, these
|     |     |     |     |     |     |     |     | ∗   |     |     | π π |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Deep-Q
Xiao et al. [13] proposed in which they used deep optimalvaluesareusedtoderivetheoptimalpolicy.However,
generativenetworkstoinferQoSmetricsfromrealtrafficdata. Q-learningisonlyeffectivewhenthestateandactionspaceis
Chenetal.[14]proposedDeepRSMAwhichisaDRLrouting small. To overcome the scalability issue, DeepMind presented
framework for optical networks. In [15], an intelligent and groundbreakingwork[3]inwhichdeepneuralnetwork(DNN)
scalable framework for routing optimisation, named SINET, was used to approximate Q (s,a) value instead of using Q-
∗
has been proposed. SINET optimises routing policies using table, called deep Q-network (DQN).
TM to reduce flow completion time. For SDN-IoT, Guo et A DQN is a multi-layered neural network which takes state
al. [16] proposed DQSP which is a DDPG based secure and space vector as input and gives a vector of action values
QoS aware routing method. In the domain of knowledge de- Q(s,·;θ) as output, where θ represents the parameters of the
finednetworking,aconvolutionalneuralnetwork(CNN)based network. DQN learns an optimal policy based on the received
QoS aware routing was proposed by [9]. They considered reward from the environment. This means that the policy can
loss and delay as QoS metrics and presented a performance become affected even with a minor change in Q-values which
comparison of the proposed DDPG with CNN with dense results in varied correlations and data distributions between
neural networks for different network settings. Suarez-Varela target values and Q-values.
etal.[17]proposedfeatureengineeringforDRL-basedrouting To solve this issue, [3] proposed two methods. Firstly, the
in the context of optical transport networks and IP networks. useofanexperiencereplaybufferthatenablestheDRLagent
However, the drawback of their proposed method is that their to store past experiences and update DNN by using mini-
action space consists of predefined k-shortest paths and the batches randomly sampled from replay memory. The use of
problemcomplexityincreasesexponentiallywhentheyuseall the experience replay mechanism allows the agent to learn
valid paths between every source-destination pair. from both new and old experiences. Also, these experiences
Despite many research efforts, DRL methods are only used are independent and identically distributed which removes
for global offline routing. This is due to the fact that greedy correlations between observations. Secondly, DQN is trained
online QoS routing poses several challenges such as learning through a separate target Q-network, with parameters θ−,
end-to-endpathsfordifferentsource-destinationpairrequests, whichestimatestargetvalues.Butthisnetworkistrainedafter
Authorized licensed use limited to: University of Canberra. Downloaded on October 03,2020 at 12:05:41 UTC from IEEE Xplore.  Restrictions apply.

| every τ | steps from | the | primary | network | such | that | θ− = | θ . |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ------- | ------- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|         |            |     |         |         |      |      | t    | t   |     |     |     |     |     |     |     |
Routing
| Therefore, | parameters  |     | are updated | as    | follows    |        |       |     |     |     | DQR |     |     |     |     |
| ---------- | ----------- | --- | ----------- | ----- | ---------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| θ =θ       | +α(yDQN−Q(s |     |             | ,a ;θ | ))(cid:53) | Q(s ,a | ;θ ), | (2) |     |     |     |     |     |     |     |
| t+1        | t           | t   |             | t t   | t θt       | t      | t t   |     |     |     |     |     |     |     |     |
Path
| where α | represents | a scalar |     | step size | and | the target | yDQN | is  |     | State |     |     |     |     |     |
| ------- | ---------- | -------- | --- | --------- | --- | ---------- | ---- | --- | --- | ----- | --- | --- | --- | --- | --- |
t
| defined | as: |     |     |     |     |     |     |     | Application  layer |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
yDQN =r +γmaxQ(s ,a;θ−) (3) Security Monitoring Routing Network Analytics
|     | t        | t+1        |     |       | t+1         | t   |             |     |               |     |     |     |     |     |     |
| --- | -------- | ---------- | --- | ----- | ----------- | --- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
|     |          |            |     | a     |             |     |             |     |               |     |     |     |     | NBI |     |
| DQN | was able | to achieve |     | super | human-level |     | performance |     |               |     |     |     |     |     |     |
|     |          |            |     |       |             |     |             |     | Control layer | NBI |     |     |     |     |     |
onAtarigames.InthesequelseveralextensionsofDQNhave SDN Controller
| been proposed |     | that led | to further | enhanced |     | performance. |     | For |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ---------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SBI
instance,toconvergefasterandwithbetterstability,authorsin SBI
Data layer
| [20] proposed | a           | dueling     | architecture |           | for DQN.   | In     | the dueling |      |     |     |     |     |     |     |     |
| ------------- | ----------- | ----------- | ------------ | --------- | ---------- | ------ | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| architecture, | a           | state value | function     |           | V(s)       | and an | associated  |      |     |     |     |     |     |     |     |
| advantage     | function    | A(s,a)      | are          | estimated | separately |        | and         | then |     |     |     |     |     |     |     |
| combined      | to estimate |             | an action    | value     | function   |        | Q(s,a).     | In   |     |     |     |     |     |     |     |
| DQN, Q(s,a)   |             | is obtained | by:          |           |            |        |             |      |     |     |     |     |     |     |     |
Q(s,a;θ,η,ζ):=V(s;θ,ζ)
|     |     | (cid:0) |     |     |     |     | (cid:1) | (4) |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
+ A(s,a;θ,η)−maxA(s,a(cid:48);θ,η)
a(cid:48)
Fig.1:Asoftwaredefinednetworkframeworkconsistsofdata,
| where η        | and ζ | are parameters |     | of two        | streams | of     | fully       | con- |         |                 |        |         |               |      |     |
| -------------- | ----- | -------------- | --- | ------------- | ------- | ------ | ----------- | ---- | ------- | --------------- | ------ | ------- | ------------- | ---- | --- |
|                |       |                |     |               |         |        |             |      | control | and application | layer. | Various | applications, | such | as  |
| nected layers. | In    | the dueling    |     | architecture, |         | Q(s,a) | is obtained |      |         |                 |        |         |               |      |     |
routing,arerunninginsidetheapplicationlayer.Theproposed
by:
|     |     |     |     |     |     |     |     |     | DQR runs | inside the routing |     | module | where it | takes network |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------------ | --- | ------ | -------- | ------------- | --- |
Q(s,a;θ,η,ζ):=V(s;θ,ζ)
|     |     |     |     |     |     |     |     |     | state as | input and gives | path as | output | which | is then installed |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | ------- | ------ | ----- | ----------------- | --- |
a
|     |     | (cid:0)       |     |     |                    |     | (cid:1) | (5) | into the | switches by SDN | controller. |     |     |     |     |
| --- | --- | ------------- | --- | --- | ------------------ | --- | ------- | --- | -------- | --------------- | ----------- | --- | --- | --- | --- |
|     |     | + A(s,a;θ,η)− |     |     | A(s,a(cid:48);θ,η) |     |         |     |          |                 |             |     |     |     |     |
|A|
AnotherimprovementtotheperformanceofDQNwasmade
by using prioritised experience replay (PER) [21] instead of by various network applications such as network monitoring,
simple ER. The use of ER plays a vital role in the learning network security, and routing.
of DQN. In ER, experience transitions are uniformly sampled Routingapplicationisresponsiblefordeterminingthepaths
withoutconsideringtheirimportance.TheideabehindthePER for source-destination pair requests. It collects network statis-
istosampleexperiencetransitionsbasedontheirsignificance. tics periodically such that the path found for each source-
Temporaldifferenceerrorsareusedtomeasuretheimportance destination pair request is based on the current state of the
oftransitions.TheuseofPERenabledDQNtolearnefficiently network. The proposed DQR method runs inside the routing
by frequently replaying important experience transitions. We application where it takes the current state of the network
used dueling DQN along with PER as a core algorithm as input and provides a path as the output (more details in
| for DQR. |     |     |     |     |     |     |     |     | Sec. V).    |                |     |               |     |               |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | --- | ------------- | --- | ------------- | --- |
|          |     |     |     |     |     |     |     |     | The network | is represented |     | as a directed |     | graph G(V,E), |     |
IV. SYSTEMMODELANDPROBLEMFORMULATION where V denotes the set of all switches and E denotes the
We consider a SDN which consists of three layers as set of links between them such that E = {(i,j)|(i,j) ∈ V ×
|                |        |          |      |             |      |           |       |     | V,i(cid:54)=j}. | For any link   | (i,j)∈E,    | the    | delay, loss, | bandwidth,  |     |
| -------------- | ------ | -------- | ---- | ----------- | ---- | --------- | ----- | --- | --------------- | -------------- | ----------- | ------ | ------------ | ----------- | --- |
| shown in       | Fig.   | 1. The   | data | layer       | also | referred  | to as | the |                 |                |             |        |              |             |     |
|                |        |          |      |             |      |           |       |     | and cost        | (also referred | as metrics) | values | are          | represented | by  |
| infrastructure | layer, | consists |      | of hardware |      | equipment | such  | as  |                 |                |             |        |              |             |     |
R
|     |     |     |     |     |     |     |     |     | {d ,l ,b | ,c } ∈ | , respectively. |     | Here, cost | is a | general |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --------------- | --- | ---------- | ---- | ------- |
switches. The main responsibility of the data layer is to ij ij ij i,j +
|         |                 |     |       |         |           |     |             |     | metric which | can be used | for | any QoS | parameter | such | as  |
| ------- | --------------- | --- | ----- | ------- | --------- | --- | ----------- | --- | ------------ | ----------- | --- | ------- | --------- | ---- | --- |
| perform | data forwarding |     | among | network | clusters. |     | The control |     |              |             |     |         |           |      |     |
layer provides a logically centralised controller which enables jitter [2]. Given a source node x with flow f for destination
|     |     |     |     |     |     |     |     |     | node y, | we want to find | a path | that minimises |     | delay, loss, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | ------ | -------------- | --- | ------------ | --- |
thecommunicationbetweentheapplicationandthedatalayer.
|     |     |     |     |     |     |     |     |     | cost while | maximising the | bandwidth. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | ---------- | --- | --- | --- | --- |
Thecontrollayerprovidesfunctionalitieslikedynamicallyup-
| dating forwarding |     | rules   | and | programming |     | network | resources. |       |     |     |     |     |     |     |     |
| ----------------- | --- | ------- | --- | ----------- | --- | ------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| The communication |     | between |     | the control |     | and the | data       | layer |     |     |     |     |     |     |     |
V. DEEP-QROUTING(DQR)
| is achieved | through | southbound |     | interfaces |     | (SBIs) | whereas, |     |     |     |     |     |     |     |     |
| ----------- | ------- | ---------- | --- | ---------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
communication between the control and the application layer Inthissection,wepresentdeep-Qrouting(DQR)forfinding
is achieved through northbound interfaces (NBIs). The appli- a path from x to y while optimising QoS parameters. DQR is
cation layer is the highest level layer of SDN which includes adeepreinforcementlearningmechanismthatutilisesdueling
storage,servers,datacentres,andapplications.Theconceptof deep Q learning with PER as its core algorithm to find QoS
application-orientedservicesisachievedinthislayer.Network optimised paths. In the following, we present design and
state information is collected through the data layer and used implementation details of DQR.
Authorized licensed use limited to: University of Canberra. Downloaded on October 03,2020 at 12:05:41 UTC from IEEE Xplore.  Restrictions apply.

| A. State | Space |     |     |     |     |     |     | where, |     |     |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
(cid:40) (cid:0) (cid:1)
We design the state space in such a way that it captures (cid:0) (cid:1) g (i,j) (i,j)∈E z
|     |     |     |     |     |     |     |     |     | f (i,j) | =   |     |     |     | v alid |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | ------ | --- |
the current state of the network without including any un- −|V|
otherwise
| necessaryinformation.ForeachQoSmetric,wedefineatwo-  |     |     |     |     |     |     |     |         |              |     | 2       |          |         |      |         |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ------- | -------- | ------- | ---- | ------- |
|                                                      |     |     |     |     |     |     |     | where E | z represents |     | the set | of valid | actions | from | node z, |
| dimensionalmatrixofsize|V|×|V|.Sincewehaverealvalues |     |     |     |     |     |     |     |         | v alid       |     |         |          |         |      |         |
z
for each metric and their range varies depending upon the i.e., only outgoing links from node are valid. If the selected
−|V|,
current state of the network, we use a rescaling function that action is invalid then the agent receives a reward of
2
|     |     |     |     |     |     |     |     | i.e., a penalty. | Otherwise, |     | reward | is obtained |     | by the | function |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ---------- | --- | ------ | ----------- | --- | ------ | -------- |
rescalesthevaluesofeachmetricto[0,1].Thisnotonlyhelps
theagenttoconvergefasterbutitalsoenablestheagenttodeal g((i,j)) which is defined as follows:
with a variable range of values for each metric in real-time.  −|V| (i,j)∈E
|     |     |     |     |     |     |     |     |     |  |     |     |     |     |     | visited |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | ------- |
For any metric, w e d e fi n e t he r e s c al in g f u n c ti on as 3
|     |     |             |     |                    |                      |     |     |         | |       | V |             |     |     | j = | y    |     |
| --- | --- | ----------- | --- | ------------------ | -------------------- | --- | --- | ------- | ------- | --------------- | --- | --- | --- | ---- | --- |
|     |     |             | u   | i j − m            | i n( (cid:126)u )    |     |     |         | −       | | V |           |     |     | t=  | | E| |     |
|     | u r | e sc al e d | =   |                    |                      | ,   | (6) |         |         |                 |     |     |     |      |     |
|     | ij  |             | m a | x ( (cid:126)u ) − | m i n ( (cid:126)u ) |     |     | (cid:0) | (cid:1) |                 |     |     |     |      |     |
|     |     |             |     |                    |                      |     |     | g (i,j) | = (     | − d r escaled·φ |     | )   |     |      |     |
|     |     |             |     |                    |                      |     |     |         |         | ij              |     | 1   |     |      |     |

w h e r e (cid:126)u i s a v e c t o r t h a t c o n s i s t s o f s e l e c t e d m e t r ic li n k v a lu e s . + ( ( b r e s c a le d − 1 ) ·φ )
|     |     |     |     |     |     |     |     |     |     | i j |     |     | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
T h e r e sc a le d v a l u e s o f d e l a y , l o s s , b a n d w i d t h , a n d c o s t a r e r e s c a l e d
|     |           |           |             |           |                 |       |     |     | +   | ( − l |     | · φ 3 ) |     |     |     |
| --- | --------- | --------- | ----------- | --------- | --------------- | ----- | --- | --- | --- | ----- | --- | ------- | --- | --- | --- |
|     | r e s c a | l e d r e | s c a l e d | r e s c a | l e d r e s c a | l e d |     |     |     | i j   |     |         |     |     |     |
d e n o t e d a s d , l , b , c r e s p e c t i v e l y . r e s c a l e d
|           | i j    | i j            |     | i j | i , j |     |     |         | +          | ( − c |       | · φ 4 ) | otherwise  |     |          |
| --------- | ------ | -------------- | --- | --- | ----- | --- | --- | ------- | ---------- | ----- | ----- | ------- | ---------- | --- | -------- |
| The delay | matrix | is constructed |     | as  |       |     |     |         |            | ij    |       |         |            |     |          |
|           |        |                |     |     |       |     |     | where E | represents |       | a set | that    | is defined | as  | empty at |
visited
|     |     |     |     |     |     |     |     | the start | of each | episode | and | then becomes |     | populated | with |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------- | --- | ------------ | --- | --------- | ---- |

|     |     | −dr | escaled | (i  | ,j) ∈ E |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 ij t h e v is i te d li n k s. If th e s e l ec te d li n k w a s al re a d y vi s it e d t h e n
2 i = j = y t h e ag e n t re c e iv es a re w a r d o f − | V |. T h is e n s u res t h a t a g e n t
3
D =[D(G)] ij = −2 i=j =x (7) does not get stuck in network loops by repeatedly selecting
 t h e s a m e lin k s i n an e p is o d e. If th e se l e c te d l i nk i nc l u de s th e
|     |     | 0   |     | i   | = j ,x (cid:54)= | i=j (cid:54)=y |     |                |              |        |           |         |              |          |                |
| --- | --- | --- | --- | --- | ---------------- | -------------- | --- | -------------- | ------------ | ------ | --------- | ------- | ------------ | -------- | -------------- |
|     |     |     |     |     |                  |                |     | d e st in a ti | on n o d e y | th e n | t h is is | a te rm | i n a l s ta | t e an d | t h e a ge n t |
−1
|     |     |     |     | o t | he rw is e |     |     |          |                |       |     |       |           |     |          |
| --- | --- | --- | --- | --- | ---------- | --- | --- | -------- | -------------- | ----- | --- | ----- | --------- | --- | -------- |
|     |     |     |     |     |            |     |     | receives | |V| as reward, | i.e., | the | agent | has found | the | path for |
The loss matrix L and the cost matrix C are constructed in this source-destination pair request. We limit each episode to
|          |            |           |     |       |       |            |     | T timesteps | to avoid | that | the agent | gets | stuck | in infinite | loops |
| -------- | ---------- | --------- | --- | ----- | ----- | ---------- | --- | ----------- | -------- | ---- | --------- | ---- | ----- | ----------- | ----- |
| the same | way. Since | bandwidth |     | needs | to be | maximised, | the |             |          |      |           |      |       |             |       |
bandwidth matrix B is constructed as follows: while exploring the action space. If the current timestep is
greaterthanthetotalnumberofedgesthentheagentislostand
|     |     |  br escaled−1 |     |     |           |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |         |     | (   | i ,j) ∈ E |     |     |     |     |     |     |     |     |     |     |
ij t h e e p i s o de i s e n d ed w it h a hi g h p en a lty o f − |V | . O the r w i s e ,
2 i = j = y t h e a g e n t re c e iv e s a re w a rd b a se d o n th e w e ig h t ed c u rr e n t
B =[B(G)] = −2 i=j =x (8) rescaled values of the network. Here, φ ,φ ,φ ,φ ∈ (0,1]
|     | ij  |     |     |     |     |     |     |     |     |     |     |     | 1   | 2 3 | 4   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
− 0 i = j ,x (cid:54)= i=j (cid:54)=y a r e t u ne a b le w e i g h ts whichcanbeusedtoprioritiseanymetric
|     |     |     |     |     |            |     |     | d u ri n g l | in k s el e c t io | n.    |       |              |         |        |          |
| --- | --- | --- | --- | --- | ---------- | --- | --- | ------------ | ------------------ | ----- | ----- | ------------ | ------- | ------ | -------- |
|     |     | 1   |     | ot  | he rw is e |     |     |              |                    |       |       |              |         |        |          |
|     |     |     |     |     |            |     |     | The goal     | of the             | agent | is to | accumulate   | maximum |        | positive |
|     |     |     |     |     |            |     |     | reward       | in each episode.   |       | This  | is supported |         | by the | design   |
B. Action Space of the reward function. It penalises the agent most strongly
The action space consists of all edges of the network. if the agent selects an invalid action because this can lead
|               |     |        |       |        |            |     |     | to divergence. | Since | agent | can | select | actions | from | a large |
| ------------- | --- | ------ | ----- | ------ | ---------- | --- | --- | -------------- | ----- | ----- | --- | ------ | ------- | ---- | ------- |
| Specifically, | the | action | space | vector | is defined | as  | A = |                |       |       |     |        |         |      |         |
[a ,a ,...,a ] where each action corresponds to a link in action space where only a handful actions are valid at each
| 1 2 | |E| |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the network (i,j)∈E. timestep, the agent should first learn to choose valid actions.
|           |          |     |     |     |     |     |     | Using this    | knowledge,   | valid  | actions | are       | selected | and      | network    |
| --------- | -------- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | ------ | ------- | --------- | -------- | -------- | ---------- |
|           |          |     |     |     |     |     |     | loops are     | avoided      | due to | high    | penalty   | compared | to       | first time |
| C. Reward | Function |     |     |     |     |     |     |               |              |        |         |           |          |          |            |
|           |          |     |     |     |     |     |     | selected      | actions. The | agent  | further | optimises |          | selected | actions    |
|           |          |     |     |     |     |     |     | by minimising | negative     |        | reward  | (finding  | a path   | that     | optimises  |
TherewardfunctiondirectlyaffectsthelearningoftheDRL
algorithmandshouldbedesignedcarefully.Inourcase,reward the QoS parameters). Lastly, if the agent is stuck between
functionincorporatessignalstocopewithinvalidactions,net- invalid actions and network loops then the episode is ended
work loops, and the optimisation of multiple metrics. Invalid by a large penalty of −|V|. The reward function has been
actions or network loops can occur because the agent is free designed to encourage the agent to reach the destination node
|           |            |                 |     |               |           |     |         | quickly | while optimising |     | the QoS | parameters. |     |     |     |
| --------- | ---------- | --------------- | --- | ------------- | --------- | --- | ------- | ------- | ---------------- | --- | ------- | ----------- | --- | --- | --- |
| to choose | any action | (edge)          | at  | any timestep. |           |     |         |         |                  |     |         |             |     |     |     |
| In an     | episode    | of T timesteps, |     | the           | DRL agent | has | to find |         |                  |     |         |             |     |     |     |
a path from the source node x to the destination node y. At D. DRL-agent and Environment Implementation
any node z, the agent selects action a at timestep t which We used the above-defined state space, action space, and
t
corresponds to link (i,j) and receives the reward r by the reward function for DQR. RLlib1 was used for the implemen-
t
|     |     | (cid:0) | (cid:1) |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reward function f (i,j) as follows: tationofDQR.Theinputlayerwasofdimension|V|×|V|×4.
|     |     |     |      | (cid:0) | (cid:1) |     |     |                                                  |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | ------- | ------- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     |     | r   | t =f | (i,j)   | ,       |     | (9) | 1https://ray.readthedocs.io/en/latest/rllib.html |     |     |     |     |     |     |     |
Authorized licensed use limited to: University of Canberra. Downloaded on October 03,2020 at 12:05:41 UTC from IEEE Xplore.  Restrictions apply.

Algorithm 1: DQR training algorithm
Initialise Environment
Initialise replay memory
Initialise main deep-Q network with weights θ
0
Initialise target deep-Q network with weights θ− =θ
for episode =1 to N do
Reset edge’s metrics value 20
Normalise each metric value according to eqn. (6)
Select a random source-destination pair (x,y)
40
Create state space s according to Sec. V-A
t
Create an empty set E
visited
for t=1 to T do 60
With probability (cid:15) select random action a
t
Otherwise select a ={argmaxQ(s,a;θ)}
t
Get valid actions set Ex 80
valid
if a ∈Ex then 0 1 2 3 4 5
t valid Episodes 1e5
Execute action a in the environment
t
Obtain reward r according to eqn. (9)
t
Update E
visited
x=z (where z is the new selected node)
Update state space s
t+1
else
Obtain reward r according to eqn. (9)
t
s = s
t+1 t
end
Store transition (s ,a ,r ,s ) in PER with max
t t t t+1
priority
Sample random mini-batch of transitions
(s ,a ,r ,s ) from PER according to their
j j j j+1
priority
Set yDQN using eqn. (3)
j
Perform gradient descent step
(yDQN −Q(s ,a ;θ ,η ,ζ ))2 w.r.t. θ
j j j t t t
Update target network weights every τ time-steps
if x==y then
break
end
end
Two hidden layers with 512 neurons and rectified linear units
asactivationfunctionswereused.Theoutputlayerwasofsize
|A|,whereateachtimestepmaximumQ-valuewasselectedas
action.Inaddition,weusedthefollowinghyper-parametersin
thetrainingprocessofourDRL-agent:batchsize64,learning
rate = 0.001, epsilon = 0.9, epsilon decay = 0.99, and buffer
size = 50000.
We developed a custom environment using the NetworkX
library [22] to train the DRL agents. Using a custom envi-
ronment not only gave us the flexibility to use it for any
size of the network graph but it also sped up the training
process. We defined a range of values for each QoS metric
(delay,bandwidth,lossandcost)fromwhichedgevalueswere
selected uniformly. Note that once the agent is trained with a
custom environment, the saved neural network model can be
used with any network simulator.
drawer
detnuocsiD
DQR
Fig. 2: DQR training performance
E. Training Algorithm
The training process of DQR (utilising DQN as DRL
algorithm) is given in the above listing Algorithm 1. At
the start of the algorithm, an instance of the environment is
created by specifying the number of nodes and edges of the
graph.Then,thereplaybuffer,mainQ-network,andtargetQ-
network are initialised. The algorithm runs for a total of N
episodes.Atthestartofeachepisode,theedges’metricvalues
(delay, bandwidth, loss, and cost) are reset and normalised
according to equation (6). Then, a random source-destination
pairisselectedandastatespacevectoriscreatedasdescribed
in Section V-A. An empty set E is created that later
visited
is used to inform the reward function about already visited
edges. Each episode has a duration of T time-steps (where
T = |E|). At each time-step t, an action a is selected using
t
an epsilon-greedy approach. If the selected action is a valid
action, then it is executed in the environment and reward r t
is obtained using equation (9), a is included in E , and
t visited
the state space vector is updated. Otherwise, if the selected
action is not a valid action, r is obtained using equation (9)
t
and the same state space is used unchanged for the next
iteration.Afterobtainings ,a ,r ,s ,thetransitionisstored
t t t t+1
in the experience replay buffer. Then, a random mini-batch of
transitionsissampledfromthereplaybufferandtheweightsof
the deep neural network are optimised using gradient descent
with respect to θ to minimise the loss. The target Q-network
is updated after every τ steps. The iteration of episodes ends
when the destination node has been found or if t>|E|.
Figure 2 shows the training performance of DQR in
our experiments on a widely used 14-node 21-bidirectional
NSFNET communication topology [17]. The y-axis presents
the discounted reward while the x-axis shows the number of
episodes. It can be observed that, at the start of training, the
agent spends most of its time on exploring the environment
while it receives penalties for invalid or already selected
actions. Once the agent starts exploiting its knowledge, it
tries to maximise the reward by avoiding invalid actions and
network loops. As the discounted reward gets closer to 0, the
Authorized licensed use limited to: University of Canberra. Downloaded on October 03,2020 at 12:05:41 UTC from IEEE Xplore. Restrictions apply.

| agent  | has already | learnt         | the topology. |        | Now     | it tries | to optimise |       |     |     |     |         |     |     |     |
| ------ | ----------- | -------------- | ------------- | ------ | ------- | -------- | ----------- | ----- | --- | --- | --- | ------- | --- | --- | --- |
| QoS    | metrics     | for different  | network       |        | states. | It can   | be seen     | in    |     |     |     |         |     |     |     |
|        |             |                |               |        |         |          |             |       |     |     |     | DQR QAR |     | SP  |     |
| Figure | 2 that      | the discounted |               | reward | becomes |          | positive    | after |     |     |     |         |     |     |     |
)sm( seulav yaleD
| this stage | after | about | 120 episodes. |     | At  | this stage | the | agent |     |     |     |     |     |     |     |
| ---------- | ----- | ----- | ------------- | --- | --- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
100
| has successfully |                    | learnt  | the        | communication |       | topology  |       | and is |     |     |     |     |     |     |     |
| ---------------- | ------------------ | ------- | ---------- | ------------- | ----- | --------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
| also             | optimising         | the QoS | parameters |               | while | selecting | paths | for    |     |     |     |     |     |     |     |
| different        | source-destination |         | pair       | requests.     |       |           |       |        | 50  |     |     |     |     |     |     |
0
5
|     |     |     |     |     |     |     |     |     |     | 1 2     | 3          | 4 5          | 6 7      | 8     | 9 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ------------ | -------- | ----- | ---- |
|     | 2   |     |     |     |     |     | 8   |     |     |         |            | Source nodes |          |       |      |
|     |     |     |     |     |     |     |     |     |     | (a) Avg | end-to-end | delay of     | selected | paths |      |
|     |     |     |     |     |     |     |     |     |     |         |            | DQR QAR      |          | SP    |      |
)spbM( htdiwdnaB
| 1   |     | 4   |     |     | 7   |     |     | 10  | 40  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 3   |     |     |     |     |     | 9   |     | 30  |     |     |     |     |     |     |
6
20
| Fig. | 3: 10-node | communication |     | topology |     | adopted | from | [1] |     |     |     |     |     |     |     |
| ---- | ---------- | ------------- | --- | -------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
10
0
|             |               |                           |         |         |            |           |         |        |     | 1 2             | 3         | 4 5          | 6 7     | 8        | 9 10  |
| ----------- | ------------- | ------------------------- | ------- | ------- | ---------- | --------- | ------- | ------ | --- | --------------- | --------- | ------------ | ------- | -------- | ----- |
|             |               | VI. PERFORMANCEEVALUATION |         |         |            |           |         |        |     |                 |           | Source nodes |         |          |       |
|             |               |                           |         |         |            |           |         |        |     | (b) Avg minimum | bandwidth | of a         | link in | selected | paths |
| In          | this section, | we                        | present | our     | simulation |           | results | that   |     |                 |           |              |         |          |       |
| show        | how           | well the proposed         |         | DQR     | method     | performs. |         | The    |     |                 |           |              |         |          |       |
|             |               |                           |         |         |            |           |         |        |     |                 |           | DQR QAR      |         | SP       |       |
| experiments |               | benchmark                 | DQR     | against | two        | other     | greedy  | online |     |                 |           |              |         |          |       |
| routing     | methods.      | The                       | first   | method  | is a       | shortest  | path    | (SP)   | 1.0 |                 |           |              |         |          |       |
etar ssoL
| approach | where  | the path  | length | is       | measured  | by  | delay.        | The  |     |     |     |     |     |     |     |
| -------- | ------ | --------- | ------ | -------- | --------- | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| second   | method | is QAR    | which  | is an    | on-policy |     | reinforcement |      |     |     |     |     |     |     |     |
| learning | based  | QoS-aware |        | adaptive | algorithm |     | [6]. It       | uses | 0.5 |     |     |     |     |     |     |
softmaxforactionselectionanditsQ-valuesareupdatedusing
SARSA [18].
0.0
|     |            |             |     |          |     |           |        |     |     | 1 2 | 3   | 4 5 | 6 7 | 8   | 9 10 |
| --- | ---------- | ----------- | --- | -------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | ---- |
| Our | simulation | experiments |     | utilised | two | different | commu- |     |     |     |     |     |     |     |      |
Source nodes
| nication | topologies. | The  | first | topology | is    | a 10-node | topology |     |     |         |            |           |             |       |     |
| -------- | ----------- | ---- | ----- | -------- | ----- | --------- | -------- | --- | --- | ------- | ---------- | --------- | ----------- | ----- | --- |
|          |             |      |       |          |       |           |          |     |     | (c) Avg | end-to-end | loss rate | of selected | paths |     |
| which    | is adopted  | from | [1]   | and is   | shown | in Figure | 3.       | The |     |         |            |           |             |       |     |
second topology is a widely used 14-node NSFNET topology DQR QAR SP
| [17].     | Link     | delay, bandwidth, |               | loss  | rate, and     | cost | values    | were |                 |     |     |     |     |     |     |
| --------- | -------- | ----------------- | ------------- | ----- | ------------- | ---- | --------- | ---- | --------------- | --- | --- | --- | --- | --- | --- |
| uniformly | selected | in                | the following |       | ranges        | (1,  | 100) ms,  | (50, | seulav tsoC 100 |     |     |     |     |     |     |
| 100)      | Mbps,    | (0.01, 1),        | and (1,       | 100), | respectively. |      | For the   | cost |                 |     |     |     |     |     |     |
| metric,   | lower    | values are        | better.       | The   | reason        | for  | selecting | link |                 |     |     |     |     |     |     |
50
| values    | from    | the above         | mentioned |          | ranges       | is that  | it allowed |     |     |     |     |     |     |     |     |
| --------- | ------- | ----------------- | --------- | -------- | ------------ | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| us to     | verify  | the effectiveness |           | of       | the proposed |          | method     | for |     |     |     |     |     |     |     |
| different | network | conditions        |           | (varying | network      | states). | We         | ran |     |     |     |     |     |     |     |
0
|             |     |               |           |     |          |           |     |        |     | 1 2 | 3   | 4 5 | 6 7 | 8   | 9 10 |
| ----------- | --- | ------------- | --------- | --- | -------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | ---- |
| simulations |     | for the three | different |     | settings | presented |     | in the |     |     |     |     |     |     |      |
Source nodes
| following | paragraphs. |          |     |           |           |     |             |     |     |         |            |         |          |       |     |
| --------- | ----------- | -------- | --- | --------- | --------- | --- | ----------- | --- | --- | ------- | ---------- | ------- | -------- | ----- | --- |
|           |             |          |     |           |           |     |             |     |     | (d) Avg | end-to-end | cost of | selected | paths |     |
| In        | the first   | case, we | run | extensive | numerical |     | simulations |     |     |         |            |         |          |       |     |
using the 10-node communication topology. Figure 4 pro- detavitca sknil gvA DQR QAR SP
| vides | an overview | of  | the | analysis | of the | QoS | metrics | at  |     |     |     |     |     |     |     |
| ----- | ----------- | --- | --- | -------- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
2
| each       | communication | node        | in                 | our simulation |       | experiments. |            | For    |     |     |     |     |     |     |     |
| ---------- | ------------- | ----------- | ------------------ | -------------- | ----- | ------------ | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| each       | source        | node we     | selected           | a destination  |       | node         | 1000-times |        |     |     |     |     |     |     |     |
| randomly,  | where         | every       | source-destination |                |       | pair         | selection  | was    |     | 1   |     |     |     |     |     |
| associated | with          | a different | network            |                | state | (link        | metric     | values |     |     |     |     |     |     |     |
| were       | uniformly     | selected    | from               | the ranges     |       | listed       | above).    |        |     |     |     |     |     |     |     |
0
Figure 4a depicts the average end-to-end delay for each ap- 1 2 3 4 5 6 7 8 9 10
proach.QARhastheworstperformanceintermsofdelay.This Source nodes
| is due | to the | use of Q-tables |     | for the | optimisation |     | of multiple |     |     |                    |     |                 |     |          |       |
| ------ | ------ | --------------- | --- | ------- | ------------ | --- | ----------- | --- | --- | ------------------ | --- | --------------- | --- | -------- | ----- |
|        |        |                 |     |         |              |     |             |     |     | (e) Average number | of  | links activated | for | selected | paths |
QoSmetricssimultaneously.TheperformancelimitationofQ-
|        |         |             |     |          |           |          |              |     |     | Fig. 4: Simulation |     | results for | 10-node | topology |     |
| ------ | ------- | ----------- | --- | -------- | --------- | -------- | ------------ | --- | --- | ------------------ | --- | ----------- | ------- | -------- | --- |
| tables | did not | allow QAR   | to  | optimise | delay.    | However, |              | QAR |     |                    |     |             |         |          |     |
| showed | better  | performance |     | for the  | remaining |          | QoS metrics. |     |     |                    |     |             |         |          |     |
Authorized licensed use limited to: University of Canberra. Downloaded on October 03,2020 at 12:05:41 UTC from IEEE Xplore.  Restrictions apply.

1.2
1.0
0.8
0.6
0.4
0.2
20 40 60 80 100
No. of communicating pairs
)sm(
seulav
yaleD
1e4 DQR QAR SP
3.0
2.5
2.0
1.5
1.0
20 40 60 80 100
No. of communicating pairs
(a) Avg end-to-end delay
)spbM(
htdiwdnaB
1e3 DQR QAR SP
1.2
1.0
0.8
0.6
0.4
0.2
20 40 60 80 100
No. of communicating pairs
(b) Avg bandwidth
seulav
tsoC
1e4 DQR QAR SP
(c) Avg end-to-end cost
Fig. 5: Simulation results for NSFNET topology
DQR performed better compared to QAR. SP was the best
performer in terms of delay which is plausible because SP
100
only considers delay while selecting a path. Figure 4b shows
the average minimum bandwidth of a link in selected paths. 90
It can be seen that DQR has a higher bandwidth than QAR
80
and SP. Figures 4c and 4d present the average end-to-end
70 loss and the cost of the selected paths. For both metrics, SP
shows the worst performance, followed by QAR, while DQR 60
significantly outperforms SP and QAR. Finally, Figure 4e
50
shows the average number of links activated in selected paths
for each source node. DQR has the least number of link 40
activations when compared to QAR and SP. This shows that 30
DQR can achieve better performance in comparison to QAR
5 10 15 20 25 30
and SP even if it selects a lower number of links.
Traffic demand (Mbps)
As the results of Figure 4 show, SP only performs well
in the case of end-to-end delay. The reason is that SP only
considers the delay metric while selecting a path and ignores
otherQoSmetrics.Thus,SPshouldbeusedforthosenetwork
applications which only have delay requirements. This also
applies to global offline DRL based routing methods where
only SP paths are considered. The performance of QAR in
Figure 4 shows that it is able to optimise QoS parameters
while selecting paths. QAR does not select paths based on a
single parameter like SP but it tries to optimise multiple QoS
metrics.ComparedtoSP,QARshowedfarbetterperformance
with respect to all QoS metrics except delay. However, when
compared to DQR, QAR only achieved limited performance.
ThereasonisthatQARusesQ-tablesforlearningthecomplex
task of QoS routing. As the problem complexity increases (in
this case it depends on the number of QoS metrics), Q-table
based Q-learning suffers performance issues.
In our experiments DQR performed better than SP and
QAR. One of the reasons is that DQR uses a dueling DQN
network at its core. However, using a dueling DQN alone is
not sufficient to solve the complex task of greedy online QoS
routing. There are multiple factors that can lead to divergence
such as learning the communication topology, dealing with
invalid actions, avoiding network loops, and optimising QoS
parameters. The proposed design of the state space, action
space,and,mostimportantly,thedesignoftherewardfunction
made sure that the DRL agent was able to overcome these
challenges. It should be emphasised that the design of DQR
)spbM(
tuphguorhT
DQR
QAR
Fig. 6: End-to-end throughput of DQR vs DQR
isnottopologydependentandthenumberofQoSmetricscan
be varied.
In the second case of the 14-node NSFNET [17] com-
munication topology, we ran numerical simulations for dif-
ferent numbers of communicating source-destination pairs.
Figure 5 presents our results using the NSFNET topology
networksimulationfordelay,bandwidth,andcost.Thex-axis
represents the number of communicating source-destination
pairs while the y-axis represents the QoS metrics. It can be
seenthatwithanincreasingnumberofsource-destinationpair
requests, the overall network usage also increases in each
case. In this second case that uses a different communica-
tion topology (14-node) and different network settings, we
obtained similar results as in the first case (10-node) that was
discussed above. Figure 5a shows the average delay achieved
byDQR,QARandSPfordifferentnumbersofcommunicating
source-destination pairs. As explained earlier, again QAR
has maximum average delay for all communicating source-
destination pairs. While DQR performs better than QAR, it
is outperformed by SP in terms of delay. Again SP can only
performbetterinthecaseofdelayanditsuffersforotherQoS
metrics. Figures 5b and 5c show the results for the bandwidth
and cost metrics and that DQR performs better than QAR
and SP.
Authorized licensed use limited to: University of Canberra. Downloaded on October 03,2020 at 12:05:41 UTC from IEEE Xplore. Restrictions apply.

Finally,weransimulationsforvaryingtrafficdemandsusing
|             |               |     |             |          |         |                 |         | [4] N. C.         | Luong, | D. T. Hoang,          | S.  | Gong, D.   | Niyato,       | P. Wang,       | Y.-C.    |
| ----------- | ------------- | --- | ----------- | -------- | ------- | --------------- | ------- | ----------------- | ------ | --------------------- | --- | ---------- | ------------- | -------------- | -------- |
|             |               |     |             |          |         |                 |         | Liang,            | and D. | I. Kim, “Applications |     | of deep    | reinforcement |                | learning |
| the 10-node | communication |     | topology    |          | (Figure | 3).             | We used |                   |        |                       |     |            |               |                |          |
|             |               |     |             |          |         |                 |         | in communications |        | and networking:       |     | A survey,” | IEEE          | Communications |          |
| Mininet     | [23] and      | Ryu | [24] as SDN | emulator |         | and controller, |         |                   |        |                       |     |            |               |                |          |
Surveys&Tutorials,2019.
| respectively. | We  | generated | network | traffic | using | iPerf3 | [25]. |                                                                 |     |     |     |     |     |     |     |
| ------------- | --- | --------- | ------- | ------- | ----- | ------ | ----- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|               |     |           |         |         |       |        |       | [5] J.A.BoyanandM.L.Littman,“Packetroutingindynamicallychanging |     |     |     |     |     |     |     |
The link metric values were selected uniformly within given networks: A reinforcement learning approach,” in Advances in Neural
|     |     |     |     |     |     |     |     | Information | Processing | Systems |     | 6, J. D. | Cowan, | G. Tesauro, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------- | --- | -------- | ------ | ----------- | --- |
ranges,specifically:delay(50,100)ms,bandwidth(100,150)
|     |     |     |     |     |     |     |     | J.Alspector,Eds. |     | Morgan-Kaufmann,1994,pp.671–678. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------------------------------- | --- | --- | --- | --- | --- |
Mbps, loss rate (0.001, 0.1), and cost (50, 100). We selected [6] S.-C. Lin, I. F. Akyildiz, P. Wang, and M. Luo, “QoS-aware adaptive
9 random source-destination pairs that started communicating routing in multi-layer hierarchical software defined networks: A rein-
with 5Mbps traffic demand. During simulation, the traffic forcementlearningapproach,”inServicesComputing(SCC),2016IEEE
|     |     |     |     |     |     |     |     | InternationalConferenceon. |     |     | IEEE,2016,pp.25–33. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | ------------------- | --- | --- | --- | --- |
demand for each pair was increased in steps of 5Mbps until [7] G. Stampa, M. Arias, D. Sanchez-Charles, V. Munte´s-Mulero,
it reached 30Mbps. We used end-to-end throughput as the and A. Cabellos, “A deep-reinforcement learning approach for
|             |        |     |             |     |               |     |       | software-defined |     | networking | routing | optimization,” |     | arXiv | preprint |
| ----------- | ------ | --- | ----------- | --- | ------------- | --- | ----- | ---------------- | --- | ---------- | ------- | -------------- | --- | ----- | -------- |
| performance | metric | for | comparison. | The | corresponding |     | simu- |                  |     |            |         |                |     |       |          |
arXiv:1709.07080,2017.
lation results for DQR and QAR are shown in Figure 6 where [8] Z.Xu,J.Tang,J.Meng,W.Zhang,Y.Wang,C.H.Liu,andD.Yang,
the x-axis shows the traffic demand of each communication “Experience-driven networking: A deep reinforcement learning based
approach,”inIEEEINFOCOM2018-IEEEConferenceonComputer
sessionandthey-axispresentsthetotalend-to-endthroughput
Communications,2018,pp.1871–1879.
| for each       | traffic | demand.    | It can     | be seen | that | DQR | is able  |                                                                  |           |           |               |                      |     |                  |     |
| -------------- | ------- | ---------- | ---------- | ------- | ---- | --- | -------- | ---------------------------------------------------------------- | --------- | --------- | ------------- | -------------------- | --- | ---------------- | --- |
|                |         |            |            |         |      |     |          | [9] Q.T.A.Pham,Y.Hadjadj-Aoul,andA.Outtagarts,“Deepreinforcement |           |           |               |                      |     |                  |     |
|                |         |            |            |         |      |     |          | learning                                                         | based     | QoS-aware | routing       | in knowledge-defined |     | networking,”     |     |
| to achieve     | higher  | end-to-end | throughput |         | than | QAR | for each |                                                                  |           |           |               |                      |     |                  |     |
|                |         |            |            |         |      |     |          | in Qshine                                                        | 2018-14th | EAI       | International | Conference           |     | on Heterogeneous |     |
| traffic demand |         | level.     |            |         |      |     |          |                                                                  |           |           |               |                      |     |                  |     |
NetworkingforQuality,Reliability,SecurityandRobustness,2018,pp.
| The above | presented |     | results | show | that DQR | can | be used |     |     |     |     |     |     |     |     |
| --------- | --------- | --- | ------- | ---- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
1–13.
|            |        |     |         |     |         |          |        | [10] A. Valadarsky, |     | M. Schapira, | D. Shahaf, | and | A. Tamar, | “Learning | to  |
| ---------- | ------ | --- | ------- | --- | ------- | -------- | ------ | ------------------- | --- | ------------ | ---------- | --- | --------- | --------- | --- |
| for greedy | online | QoS | routing | and | that it | achieves | better |                     |     |              |            |     |           |           |     |
routewithdeeprl,”inNIPSDeepReinforcementLearningSymposium,
| performance | than | QAR | and SP | with respect |     | to different | QoS |     |     |     |     |     |     |     |     |
| ----------- | ---- | --- | ------ | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2017.
metrics by efficiently utilising network resources. The design [11] X.Huang,T.Yuan,G.Qiao,andY.Ren,“Deepreinforcementlearning
ofDQRisflexibleenoughthatitcanbeusedforanynetwork for multimedia traffic control in software defined networking,” IEEE
Network,vol.32,no.6,pp.35–41,2018.
| topology | and | it can be | used for | different |     | number | of QoS |             |          |         |          |        |                         |     |     |
| -------- | --- | --------- | -------- | --------- | --- | ------ | ------ | ----------- | -------- | ------- | -------- | ------ | ----------------------- | --- | --- |
|          |     |           |          |           |     |        |        | [12] Z. Xu, | J. Tang, | C. Yin, | Y. Wang, | and G. | Xue, “Experience-driven |     |     |
metrics. The normalisation of the QoS metrics while training congestion control: When multi-path tcp meets deep reinforcement
enables DQR to be applicable in any real world scenario. In learning,”IEEEJournalonSelectedAreasinCommunications,vol.37,
summary, our results indicate that DQR can be used for a no.6,pp.1325–1336,2019.
|     |     |     |     |     |     |     |     | [13] S. Xiao, | D. He, | and Z. | Gong, “Deep-q: | Traffic-driven |     | qos | inference |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ------ | -------------- | -------------- | --- | --- | --------- |
variety of real world network applications, while efficiently using deep generative network,” in Proceedings of the 2018 Workshop
utilising network resources. onNetworkMeetsAI&ML,2018,pp.67–73.
|     |     |     |     |     |     |     |     | [14] X.Chen,B.Li,R.Proietti,H.Lu,Z.Zhu,andS.B.Yoo,“Deeprmsa: |               |          |           |     |          |            |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | ------------- | -------- | --------- | --- | -------- | ---------- | --- |
|     |     |     |     |     |     |     |     | a deep                                                       | reinforcement | learning | framework | for | routing, | modulation | and |
VII. CONCLUSION spectrumassignmentinelasticopticalnetworks,”JournalofLightwave
Technology,vol.37,no.16,pp.4155–4163,2019.
| In this    | paper, | we proposed | DQR            | for | greedy | online    | QoS  |                                                                  |         |           |               |          |     |            |         |
| ---------- | ------ | ----------- | -------------- | --- | ------ | --------- | ---- | ---------------------------------------------------------------- | ------- | --------- | ------------- | -------- | --- | ---------- | ------- |
|            |        |             |                |     |        |           |      | [15] P.Sun,J.Li,Z.Guo,Y.Xu,J.Lan,andY.Hu,“Sinet:Enablingscalable |         |           |               |          |     |            |         |
| routing in | SDN.   | DQR         | uses a dueling |     | deep   | Q-network | with |                                                                  |         |           |               |          |     |            |         |
|            |        |             |                |     |        |           |      | network                                                          | routing | with deep | reinforcement | learning |     | on partial | nodes,” |
prioritised experience replay to learn the network topology in Proceedings of the ACM SIGCOMM 2019 Conference Posters and
Demos,2019,pp.88–89.
| in the presence |        | of multiple | QoS  | metrics  | (delay,   | bandwidth, |         |                                                                 |     |     |     |     |     |     |     |
| --------------- | ------ | ----------- | ---- | -------- | --------- | ---------- | ------- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                 |        |             |      |          |           |            |         | [16] X.Guo,H.Lin,Z.Li,andM.Peng,“Deepreinforcementlearningbased |     |     |     |     |     |     |     |
| loss, and       | cost). | Different   | from | existing | DRL-based |            | routing |                                                                 |     |     |     |     |     |     |     |
qos-awaresecureroutingforsdn-iot,”IEEEInternetofThingsJournal,
| methods | which | use shortest | paths, | DQR | learns | the | network | 2019. |     |     |     |     |     |     |     |
| ------- | ----- | ------------ | ------ | --- | ------ | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
topology. The flexible design of the reward function allows [17] J.Suarez-Varela,A.Mestres,J.Yu,L.Kuang,H.Feng,P.Barlet-Ros,
andA.Cabellos-Aparicio,“Featureengineeringfordeepreinforcement
DQR to optimise QoS metrics while routing and to avoid learningbasedrouting,”inIEEEInternationalConferenceonCommu-
invalid actions and network loops. Our simulation results nications(ICC). IEEE,2019,pp.1–6.
demonstrated that DQR can significantly reduce delay, cost, [18] R.S.SuttonandA.G.Barto,Reinforcementlearning:Anintroduction.
MITpressCambridge,1998.
andloss,whilemaximisingbandwidthwhencomparedtoother [19] C.J.C.H.Watkins,“Learningfromdelayedrewards,”King’sCollege,
existing learning methods for greedy online routing. CambridgeUniversity,UK,1989.
|     |     |     |     |     |     |     |     | [20] Z.Wang,T.Schaul,M.Hessel,H.Hasselt,M.Lanctot,andN.Freitas, |         |               |     |                    |     |            |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | ------- | ------------- | --- | ------------------ | --- | ---------- | --- |
|     |     |     |     |     |     |     |     | “Dueling                                                        | network | architectures | for | deep reinforcement |     | learning,” | in  |
ACKNOWLEDGEMENTS InternationalConferenceonMachineLearning,vol.48,2016,pp.1995–
2003.
| SQJ was        | supported | by            | a UNRSC50:50 |     | PhD | scholarship |     | at                                                                   |     |     |     |     |     |     |     |
| -------------- | --------- | ------------- | ------------ | --- | --- | ----------- | --- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                |           |               |              |     |     |             |     | [21] T.Schaul,J.Quan,I.Antonoglou,andD.Silver,“Prioritizedexperience |     |     |     |     |     |     |     |
| the University |           | of Newcastle, | Australia.   |     |     |             |     |                                                                      |     |     |     |     |     |     |     |
replay,”arXivpreprintarXiv:1511.05952,2015.
|     |     |     |     |     |     |     |     | [22] D.A.S.AricA.HagbergandP.J.Swart,“Exploringnetworkstructure, |     |          |                  |     |               |     |         |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | -------- | ---------------- | --- | ------------- | --- | ------- |
|     |     |     |     |     |     |     |     | dynamics,                                                        | and | function | using networkx,” |     | in 7th Python | in  | Science |
REFERENCES
Conference(SciPy),2008,pp.11–15.
[1] J.W.Guck,A.V.Bemten,M.Reisslein,andW.Kellerer,“UnicastQoS [23] Mininet,Availableat,http://mininet.org/,AccessedSeptember2018.
routingalgorithmsforSDN:Acomprehensivesurveyandperformance [24] Ryu,Availableat,http://osrg.github.io/ryu/,AccessedSeptember2018.
evaluation,”IEEECommunicationsSurveysTutorials,vol.20,no.1,pp. [25] iPerf3,Availableat,https://iperf.fr/,AccessedSeptember2018.
388–415,2018.
| [2] M. Karakus |     | and A. Durresi, | “Quality | of  | service | (qos) | in software |     |     |     |     |     |     |     |     |
| -------------- | --- | --------------- | -------- | --- | ------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
definednetworking(sdn):Asurvey,”JournalofNetworkandComputer
Applications,vol.80,pp.200–218,2017.
| [3] V. Mnih, | K.           | Kavukcuoglu, | D. Silver,     | A.   | A. Rusu,      | J. Veness, | M.         | G.  |     |     |     |     |     |     |     |
| ------------ | ------------ | ------------ | -------------- | ---- | ------------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bellemare,   | A.           | Graves,      | M. Riedmiller, | A.   | K. Fidjeland, | G.         | Ostrovski  |     |     |     |     |     |     |     |     |
| et al.,      | “Human-level | control      | through        | deep | reinforcement |            | learning,” |     |     |     |     |     |     |     |     |
Nature,vol.518,no.7540,p.529,2015.
Authorized licensed use limited to: University of Canberra. Downloaded on October 03,2020 at 12:05:41 UTC from IEEE Xplore.  Restrictions apply.