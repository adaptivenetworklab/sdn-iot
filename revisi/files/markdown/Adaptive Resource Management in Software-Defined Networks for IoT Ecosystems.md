# Adaptive Resource Management in Software-Defined Networks for IoT Ecosystems

> Source file: `Adaptive Resource Management in Software-Defined Networks for IoT Ecosystems.pdf`

---

Adaptive Resource Management in
Software-Defined Networks for IoT Ecosystems
Okwudili Mathew Ugochukwu Muhammad Shoaib Ayub, Renata Lopes Rosa
Department of Computer Science Pablo Adasme Department of Computer Science
Federal University of Lavras Department of Electrical Engineering Federal University of Lavras
Lavras, Minas Gerais, Brazil Universidad de Santiago de Chile Lavras, Minas Gerais, Brazil
ugochukwu.matthew@estudante.ufla.br Santiago, Chile renata.rosa@ufla.br
{muhammad.shoaib, pablo.adasme}@usach.cl
Demostenes Zegarra Rodriguez Muhammad Saadi Frederico Gadelha Guimaraes
Computer Science Department Department of Electrical Enginnering Department of Computer Science
Federal University of Lavras University of Central Punjab, Federal University of Minas Gerais
Lavras, Minas Gerais, Brazil Punjab, Pakistan Belo Horizonte, Minas Gerais, Brazil
demostenes.zegarra@ufla.br muhammad.saadi@ucp.edu.pk fredericoguimaraes@ufmg.br
Abstract—TheproliferationofInternetofThings(IoT)devices Software-DefinedNetworking(SDN)hasemergedasarev-
hasimposedsomechallengesontraditionalnetworkmanagement olutionary paradigm that decouples the control plane from the
systems, necessitating diverse approaches for efficient resource
data plane, enabling centralized and programmable network
allocation. In this paper, we present a framework for adaptive
management [4]. This separation allows for more granular
resource management in Software-Defined Networks (SDNs)
tailored to IoT ecosystems. Leveraging the inherent flexibility control over network resources, making SDN a promising so-
and programmabilityof SDNs, our methodologyintegrates rein- lutionforaddressingtheuniquechallengesofIoTecosystems.
forcement learning techniques to dynamically allocate network The programmability of SDN facilitates dynamic resource
resources based on real-time demands of IoT applications.
allocation, which is essential for maintaining the Quality
Our approach introduces a dual-stage Deep Q-Network (DQN)
of Service (QoS) in IoT applications that demand real-time
architecture,enhancingstabilityandaccuracyinlearningoptimal
resource allocation policies. This dual-stage DQN, combined processingandlowlatency[5].Effectiveresourcemanagement
with a multi-agent reinforcement learning strategy, maximizes inSDN-basedIoTecosystemsinvolvesthedynamicallocation
network performance while ensuring fairness and Quality of of bandwidth, processing capacity, and memory resources to
Service (QoS). The proposed system is evaluated in a simulated
meetthespecificrequirementsofIoTdevicesandapplications.
IoTenvironmentusingtheOpenDaylight(ODL)SDNcontroller.
Traditional resource allocation methods often fall short in
Theexperimentalresultsdemonstrateasignificantimprovement
in key performance metrics, including increased throughput, these environments due to their static nature and inability
reducedlatency,anddecreasedenergyconsumptioncomparedto to adapt to real-time changes in network conditions. This
traditional methods. These enhancements highlight the potential inadequacy can lead to resource underutilization or over-
of our adaptive resource management framework in addressing
provisioning, negatively impacting network performance and
the complex requirements of modern IoT ecosystems.
energyefficiency[6].Toaddressthesechallenges,wepropose
Index Terms—Internet of Things, network resource allocation
and management, Software-Defined Networks. an adaptive resource management framework that leverages
reinforcement learning (RL) within the SDN architecture.
I. INTRODUCTION Specifically, our methodology employs a dual-stage Deep Q-
Network (DQN) architecture. This enhancement involves a
ThegrowthofInternetofThings(IoT)deviceshasledtoan
combination of primary and target networks, facilitating the
increase in network traffic and complexity, posing significant
learning and handling of the temporal correlations in network
challengestotraditionalnetworkmanagementsystems[1],[2].
state observations. The previous work [7] primarily utilized
Thesesystemsoftenlacktheflexibilityandscalabilityrequired
a single DQN model without this sophisticated separation,
to efficiently handle the dynamic and heterogeneous nature of
leading to potential instability and less accurate resource allo-
IoT environments. The surge in IoT deployments necessitates
cation decisions. The proposed framework introduces a multi-
innovative approaches to resource management that can adapt
agent reinforcement learning approach, enhancing scalability
to varying demands and optimize network performance [3].
and efficiency by optimizing local resource allocation while
coordinating globally. It uses advanced techniques for state
Authorized licensed use limited to: UNIVERSIDADE FEDERAL DE LAVRAS. Downloaded on November 05,2024 at 15:15:22 UTC from IEEE Xplore. Restrictions apply.

representationwithrecurrentneuralnetwork(RNN)tocapture average completion time of jobs and the average number of
temporalpatterns,andimprovestherewardfunctiontoinclude requestedresources.Nevertheless,theexperimentsarefocused
QoS metrics, energy efficiency, and fairness. The proposed only on the convergence performance of the DQN. Some
DQN architecture, consisting of primary and target network, networkparametersarenottreated,suchasthepacketlossrate
inwhichtheprimarynetworkisresponsibleforpredictingthe and energy consumption. In [7], another resource allocation
Q-values for the current state-action pairs, while the target method is utilized. However, in it a single DQN model
network is used to provide stable target Q-values for the and centralized approach is developed, leading to potential
| learning | process. |     |     |     |     |     |     |     | instability | and scalability | challenges. |     |
| -------- | -------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | ----------- | --- |
In this system, multiple DQN agents are deployed across Eachapproachoftherelatedstudiesaddressedonlyspecific
various segments of the network, each tasked with optimizing challengesandrequirementsofIoTapplications.Ourproposed
resource allocation within its respective domain. framework incorporates a dual-stage DQN architecture and
Thispaperisorganizedasfollows:SectionIIreviewsrelated a multi-agent reinforcement learning approach, resulting in
works in the field of SDN-based IoT resource management. more stable learning and better scalability in large-scale IoT
| Section    | III details | the           | proposed | methodology, |             |           | including | the | environments. |     |     |     |
| ---------- | ----------- | ------------- | -------- | ------------ | ----------- | --------- | --------- | --- | ------------- | --- | --- | --- |
| dual-stage | DQN         | architecture, |          | the          | multi-agent | approach, |           | and |               |     |     |     |
III. METHODOLOGY
| the dynamic     | resource |             | allocation | process.     |     | Section | IV presents  |     |              |          |             |                     |
| --------------- | -------- | ----------- | ---------- | ------------ | --- | ------- | ------------ | --- | ------------ | -------- | ----------- | ------------------- |
|                 |          |             |            |              |     |         |              |     | This section | provides | an overview | of the methodology, |
| the performance |          | evaluation, |            | highlighting |     | the     | experimental |     |              |          |             |                     |
setup and results. Section V discusses the findings and their includingthearchitecture,softwaretoolsused,algorithms,and
implications. Finally, Section VI concludes the paper and the detailed steps involved in the resource allocation process.
| outlines              | directions    | for              | future           | research.    |             |            |               |        |     |     |     |     |
| --------------------- | ------------- | ---------------- | ---------------- | ------------ | ----------- | ---------- | ------------- | ------ | --- | --- | --- | --- |
|                       |               | II.              | RELATEDWORK      |              |             |            |               |        |     |     |     |     |
| This section          |               | presents         | a review         |              | of the      | current    | state-of-the- |        |     |     |     |     |
| art resource          | allocation    |                  | for IoT          | applications |             | in         | SDNs.         | In [8] |     |     |     |     |
| an intelligent        | SDN-based     |                  | Intelligent      |              | Decision    | Support    |               | System |     |     |     |     |
| for IoT               | (SDN-IDSSIoT) |                  | is               | proposed.    | This        | system     | is            | com-   |     |     |     |     |
| posed of              | two           | core components: |                  | the          | IDSS        | conceptual |               | model  |     |     |     |     |
| and the               | SDN-based     |                  | architecture,    |              | designed    | to         | ensure        | seam-  |     |     |     |     |
| less interoperability |               | among            |                  | diverse      | smart       | home       | devices.      | The    |     |     |     |     |
| proposed              | system        | is evaluated     |                  | through      | experiments |            | measuring     |        |     |     |     |     |
| average               | throughput    | and              | round            | trip         | time.       | However,   | there         | are    |     |     |     |     |
| some limitations      |               | as               | the number       | of           | devices.    | In         | [9] a         | SDN-   |     |     |     |     |
| based IIoT            | architecture  |                  | is               | proposed     | with        | edge       | computing     |        |     |     |     |     |
| (EC) outperforming    |               |                  | some traditional |              | methods     |            | over adaptive |        |     |     |     |     |
| computation,          | effective     |                  | resource         | management,  |             | and        | latency       | in     |     |     |     |     |
| industrial            | wireless      | networks         |                  | (IWNs).      | However,    |            | in [9],       | only   |     |     |     |     |
| some parameters       |               | of               | the network      |              | are         | measured,  | such          | as     |     |     |     |     |
throughput,andoveralldelay.Moreover,JavadpourandWang
| [10] examined |         | one issue | in        | network        | virtualization |            | to  | provide |                                                                  |     |     |     |
| ------------- | ------- | --------- | --------- | -------------- | -------------- | ---------- | --- | ------- | ---------------------------------------------------------------- | --- | --- | --- |
|               |         |           |           |                |                |            |     |         | Fig.1. ProposedadaptiveresourcemanagementinSDNsforIoTecosystems. |     |     |     |
| an efficient  | dynamic |           | resources | infrastructure |                | management |     | on      |                                                                  |     |     |     |
Software-Based Networks, in which the method (cTMvSDN) Fig. 1 provides a high-level overview of the proposed
improves resource management based on the combination of solutionarchitecture,illustratingtheinteractionbetweenmulti-
Markov-Process and Time Division Multiple Access (TDMA) agents for localized resource management, the DRL agent
protocols.Amoduletoinitializetheresourcemappingisused for optimizing performance metrics, and the SDN controller
into it. Thus, the Markov-Pattern and TDMA slicing model is for overall network infrastructure management. Initially, IoT
used for predicting the next time gaps, but only the response devices continuously generate data and it is sent to the SDN
time and SDN Quality of service are optimized. In [11], a controller, which dynamically manages network resources
flow-splittingschemeisusedtosplittheincomingflowsinthe basedonthereceivedinformation.TheRLagentreceivesdata
network.Thus,acostfunctionisusedwiththeaimtoroutethe and state information from the SDN controller and applies
splittable sub-flows, formulating a min-cost routing problem, the RL algorithm to optimize resource allocation within the
known as an integer linear program (ILP) through a detailed network. The RL agent sends updated resource allocation
greedy heuristic approach. The experimental results show that strategiesbacktotheSDNcontroller,whichimplementsthese
theproposedschemepresentsahighernetworkthroughputby changes in the network. Arrows in the figure indicate the
22% compared to other schemes. continuous flow of data and control signals between IoT
Another proposal [12] improves the RL algorithm to per- devices, the SDN controller, and the RL agent, ensuring that
form a resource allocation with the aim to minimize the the network adapts in real-time to changing conditions and
Authorized licensed use limited to: UNIVERSIDADE FEDERAL DE LAVRAS. Downloaded on November 05,2024 at 15:15:22 UTC from IEEE Xplore.  Restrictions apply.

demands.Thefigureintegratesadual-stageDQNarchitecture, 2) DeepQ-Network(DQN)Architecture: TheDQNusedin
consistingofprimaryandtargetnetwork.Theprimarynetwork ourframeworkemploysadual-stagearchitecturewithprimary
makespredictionsbasedoncurrentnetworkstateobservations, andtargetnetworkstoenhancelearningstability.Theprimary
whilethetargetnetworkisperiodicallyupdatedwiththeinput network is updated at every step, while the target network is
oftheprimarynetworktoenhancelearningstability.Addition- updated at regular intervals to match the primary network’s
ally, the figure illustrates a multi-agent RL approach, where input. The hyperparameters used are a learning rate of 0.01, a
multiple RL agents operate in different parts of the network. discountfactorof0.95,areplaymemorysizeof5000,abatch
Each RL agent optimizes local resource allocation based on size of 64, a target network update frequency of 1000 steps,
the specific conditions and demands of its network segment. and an exploration factor that decays from 1.0 to 0.1 over
These agents coordinate with each other to achieve global 10000 steps. Both the primary and target networks consist
optimization of the network, ensuring that local optimizations of three hidden layers, each with 128 neurons, using ReLU
contribute to the overall performance and efficiency of the activation functions. The output layer uses a linear activation
entire network. function to predict Q-values for each possible action.
|     |     |     |     |     |     |     |     | 3) State | Representation: | The | state | representation |     | includes |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ----- | -------------- | --- | -------- |
A. Architecture Overview bothstaticandtemporalfeaturesofthenetwork.Staticfeatures
|     |     |     |     |     |     |     |     | consist of | the current traffic | load, | device | priorities, |     | and avail- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------- | ----- | ------ | ----------- | --- | ---------- |
In the architecture of our proposed framework are used able resources. Temporal features are captured using a RNN
the OpenDaylight (ODL) SDN controller for robust network withLongShort-TermMemory(LSTM)cells,configuredwith
management,adual-stageDeepQ-Network(DQN)usingTen- 2 LSTM layers, 64 units per layer, and a sequence length of
| sorFlow | 2.6 and | TF-Agents | for | stable | learning, | a multi-agent |     |         |                     |     |                      |     |     |             |
| ------- | ------- | --------- | --- | ------ | --------- | ------------- | --- | ------- | ------------------- | --- | -------------------- | --- | --- | ----------- |
|         |         |           |     |        |           |               |     | 10 time | steps. The combined |     | state representation |     |     | is a vector |
system for optimizing local and global resource allocation, concatenating the outputs of the LSTM layers and the static
advanced state representation with RNNs to capture temporal features, providing a comprehensive view of the network’s
| traffic | patterns, | an enhanced |     | reward | function | incorporating |     | status over | time. |     |     |     |     |     |
| ------- | --------- | ----------- | --- | ------ | -------- | ------------- | --- | ----------- | ----- | --- | --- | --- | --- | --- |
QoS metrics, energy efficiency, and fairness, simulated IoT 4) Performance Evaluation and Simulation Setup: To im-
devices generating network traffic, and an environment simu- plement and evaluate our proposed framework, we used sev-
lator to evaluate performance. eral software tools: OpenDaylight (ODL) SDN Controller for
The IEEE 802.11 standard with the Distributed Coordi- modular and programmable SDN control, TensorFlow 2.6 for
nation Function (DCF) is used for the MAC layer, sim- building and training the dual-stage DQN, TF-Agents for
ulating a CSMA/CA environment. This setup ensures fair reinforcement learning algorithms in TensorFlow, Python for
|        |        |       |          |          |               |     |        | implementing | the simulation |     | environment |     | and reinforcement |     |
| ------ | ------ | ----- | -------- | -------- | ------------- | --- | ------ | ------------ | -------------- | --- | ----------- | --- | ----------------- | --- |
| medium | access | among | multiple | devices, | significantly |     | influ- |              |                |     |             |     |                   |     |
encing throughput and latency. learning agent, and Matplotlib for visualizing experimental
|     |     |     |     |     |     |     |     | results. | The simulation | setup | included | 200 | IoT devices | with |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | ----- | -------- | --- | ----------- | ---- |
varyingtrafficpatternsandresourcedemands.Thekeyparam-
| B. Methodological |     | Clarifications |     | for Reproducibility |     |     |     |           |                |            |     |          |     |     |
| ----------------- | --- | -------------- | --- | ------------------- | --- | --- | --- | --------- | -------------- | ---------- | --- | -------- | --- | --- |
|                   |     |                |     |                     |     |     |     | eters for | the simulation | are listed | in  | Table I. |     |     |
1) Reward Function Calculation: The reward function in A job arrival rate of 30 jobs per second, and ran for 10,000
our dual-stage DQN architecture combines several perfor- episodes are configured. Key parameters included an explo-
mance metrics, including throughput, latency, energy con- rationfactorof0.1,replaymemorysizeof5000,andbatchsize
|           |     |           |     |           |      |           |      | of 64. The | target network | update | frequency |     | was | set to 1000 |
| --------- | --- | --------- | --- | --------- | ---- | --------- | ---- | ---------- | -------------- | ------ | --------- | --- | --- | ----------- |
| sumption, | and | fairness. | The | reward at | each | time step | t is |            |                |        |           |     |     |             |
computed as follows: steps. The simulation lasted 24 hours, high latency sensitivity,
|        |     |          |     |                   |     |          |     | and enabled                                        | energy consumption  |          | monitoring.   |                | Traffic     | patterns |
| ------ | --- | -------- | --- | ----------------- | --- | -------- | --- | -------------------------------------------------- | ------------------- | -------- | ------------- | -------------- | ----------- | -------- |
|        |     |          |     |                   |     |          |     | varied greatly,                                    | initial             | resource | allocation    |                | was random, | and      |
|        | T   | (cid:18) | L   | (cid:19) (cid:18) | E   | (cid:19) |     |                                                    |                     |          |               |                |             |          |
|        | t   |          | t   |                   |     | t        |     | adaptive                                           | resource allocation | was      | enabled.      |                |             |          |
| R =α·  |     | +β· 1−   |     | +γ·               | 1−  | +δ·F     | (1) |                                                    |                     |          |               |                |             |          |
| t      | T   |          | L   |                   | E   |          | t   | TheIoTdevicesgenerateddatapacketsthatwereprocessed |                     |          |               |                |             |          |
|        | max |          | max |                   | max |          |     |                                                    |                     |          |               |                |             |          |
|        |     |          |     |                   |     |          |     | as computational                                   | jobs by             | the      | Mobile        | Edge Computing |             | (MEC)    |
| where: |     |          |     |                   |     |          |     | system.                                            | The performance     | of       | our framework |                | was         | assessed |
• T is the throughput at time step t, normalized by the across multiple episodes to ensure robustness and general-
t
maximum achievable throughput T . izability. The detailed steps of our proposed method are as
max
follows:
| • L | t is the | latency | at time | step | t, normalized | by  | the |     |     |     |     |     |     |     |
| --- | -------- | ------- | ------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
maximum tolerable latency L . • IoT Device Requests Resources: IoT devices generate
max
E is the energy consumption at time step t, normalized datapacketsandrequestnetworkresourcesfromtheSDN
• t
by the maximum possible energy consumption E . controller based on their current requirements.
max
F is the fairness index at time step t. NetworkStateObservation:TheSDNcontrollercontin-
| •   | t   |     |     |     |     |     |     | •   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• α, β, γ, and δ are the factors for each metric, set to uously monitors the network state, including traffic load,
balance their contributions to the overall reward. In our device requirements, and current resource utilization.
experiments, we set α = 0.4, β = 0.3, γ = 0.2, and State Representation: This involves capturing relevant
•
δ =0.1. features such as historical traffic patterns, device pri-
Authorized licensed use limited to: UNIVERSIDADE FEDERAL DE LAVRAS. Downloaded on November 05,2024 at 15:15:22 UTC from IEEE Xplore.  Restrictions apply.

TABLEI Algorithm 1: Enhanced DQN-Based Resource Allocation
SIMULATIONPARAMETERS
Data: Initialize replay memory D to capacity N
Parameter Value Data: Initialize primary action-value function Q with
NumberofIoTDevices 200 random weights
ComputingResourceLevels 250 Data: Initialize target action-value function Qˆ with
JobArrivalRate 30jobs/second
NumberofEpisodes 10000 θ− =θ
ExplorationFactor 0.1 Data: Initialize multiple agents for decentralized
LearningRate 0.01
communic.
DiscountFactor 0.95
ReplayMemorySize 5000 1 for agent i=1 to n do
BatchSize 64 2 for episode = 1 to M do
TargetNetworkUpdateFrequency 1000steps
SimulationDuration 24hours 3 Initialize state s i1 from the environment;
LatencySensitivity High 4 for t = 1 to T do
EnergyConsumptionMonitoring Enabled 5 if random number <ϵ then
TrafficPatternVariability High
InitialResourceAllocation Random 6 Select a random action a it ;
AdaptiveResourceAllocation Enabled 7 else
8 Select a it =argmax a Q(s it ,a;θ i );
9 end
orities, and resource availability. Advanced state rep- 10 Execute action a it and observe reward r it
resentation techniques, including the use of recurrent and next state s ;
i(t+1)
neural networks (RNNs), are employed to capture time- 11 Store transition (s it ,a it ,r it ,s i(t+1) ) in D i ;
dependent patterns in network traffic. 12 Sample random mini-batch of transitions
• Action Selection: Using an epsilon-greedy strategy, the (s ij ,a ij ,r ij ,s i(j+1) ) from D i ;
reinforcement learning agent selects an action that rep- 13 Set y ij =
resents a resource allocation decision, which represent (cid:40)
r if step j+1
ij
specific resource allocation decisions in the network.
r +γmax Qˆ(s ,a′;θ−) otherwise
• Reward Calculation: The reward function evaluates the ij a′ i(j+1) i
Perform a gradient descent step on
selectedactionbasedonnetworkperformancemetrics,as
(y −Q(s ,a ;θ ))2 with respect to the
throughput, latency, energy consumption, and fairness. ij ij ij i
network parameters;
• P its oli p c o y li U cy pd u a s t in e: g T t h h e e r o e b in s f e o rv rc e e d m r e e n w t a l r e d a s r . ni T ng hi a s g i e s nt ac u h p i d e a v t e e d s 14 Every C steps reset Qˆ i =Q i ;
bytrainingthedual-stageDeepQ-Network(DQN)using 15 end
experience replay and target network updates to stabilize 16 end
the learning process. 17 end
Data: Combine local policies to form a global policy
• Resource Allocation: Based on the updated policy, the
SDN controller allocates resources to the IoT devices,
optimizing network performance. The updated network
state is then fed back into the system for continuous Energy consumption E is given by:
learning and adaptation.
E =P ×TPT (3)
MEC
The algorithm for our proposal includes multiple agents
operating in different parts of the network (reflecting the where P MEC is the power consumption of the MEC system,
multi-agentapproach),utilizesadual-stageDQNwithseparate and TPT is the total processing time.
primary and target networks for stability, and incorporates Fairness F is calculated using the Jain’s Fairness Index:
advancedstaterepresentationandrewardcalculationprocesses ( (cid:80)n x )2
to capture complex network dynamics. F = n (cid:80) i= n 1 x i 2 (4)
i=1 i
C. Performance Evaluation where x is the resource allocated to the i-th device and n is
i
The performance evaluation used in our methodology are the number of devices.
as follows. Jain’s index is chosen for its widespread acceptance and
Throughput T is calculated as: effectivenessinevaluatingresourcedistributionfairnessinIoT
networks, providing a comprehensive measure compared to
TJ
T = (2) indices like the Gini coefficient and Theil index.
TT
D. Use Case Scenario
where TJ is the total data size of all jobs processed, and TT
is the total time taken. To evaluate the effectiveness of our proposed framework,
Latencyismeasuredastheaveragetimeajobspendsinthe we conducted experiments in a simulated IoT environment.
system, including both waiting and processing time. The simulation involves 200 IoT devices distributed within
Authorized licensed use limited to: UNIVERSIDADE FEDERAL DE LAVRAS. Downloaded on November 05,2024 at 15:15:22 UTC from IEEE Xplore. Restrictions apply.

| the network’s |     | service | region. | Each | device | generates data |     |     |     |     |     |     |     |
| ------------- | --- | ------- | ------- | ---- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- |
)spbG(
20
| packets | that are | processed | as  | computational |     | jobs by the MEC |     |     |     |     |     |     |     |
| ------- | -------- | --------- | --- | ------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
system. The resource allocation process is evaluated over 15 11.7 12.15
|          |          |            |     |                 |     |              |            |     | 10  | 10.33 | 10.98 |     |     |
| -------- | -------- | ---------- | --- | --------------- | --- | ------------ | ---------- | --- | --- | ----- | ----- | --- | --- |
| multiple | episodes | to measure |     | key performance |     | metrics such | tuphguorhT |     |     |       |       |     |     |
10
| as throughput, |     | latency, | energy | consumption, |     | and fairness. |     |     |     |     |     |     |     |
| -------------- | --- | -------- | ------ | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
5
0
IV. RESULTSANDDISCUSSIONS
|          |          |           |     |              |        |                  |     | DQN |     | cTMvSDNQoS-aware | DQN1 |     | DQN2 |
| -------- | -------- | --------- | --- | ------------ | ------ | ---------------- | --- | --- | --- | ---------------- | ---- | --- | ---- |
| This     | section  | presents  | an  | analysis     | of the | results obtained |     |     |     |                  |      |     |      |
| from our | proposed | framework |     | for adaptive |        | resource manage- |     |     |     |                  |      |     |      |
Fig.2. Throughputcomparisonofdifferentmethods.Thebarsrepresentthe
ment in SDNs tailored to IoT ecosystems. We evaluate the meanthroughput,andtheerrorbarsrepresentthestandarddeviation.
performanceofourframeworkintermsofthroughput,latency,
| energy consumption, |                   |             | and fairness. | The           | results  | are compared     |         |                |     |                |                      |     |             |
| ------------------- | ----------------- | ----------- | ------------- | ------------- | -------- | ---------------- | ------- | -------------- | --- | -------------- | -------------------- | --- | ----------- |
|                     |                   |             |               |               |          |                  |         | The throughput |     | of 12.15       | Gbps in our proposed |     | framework,  |
| with traditional    |                   | methods     | and           | recent        | advanced | algorithms       | to      |                |     |                |                      |     |             |
|                     |                   |             |               |               |          |                  | DQN2,   | simulates      |     | a high-density | IoT environment      |     | with mixed  |
| highlight           | the effectiveness |             | of            | our approach. |          |                  |         |                |     |                |                      |     |             |
|                     |                   |             |               |               |          |                  | traffic | conditions,    |     | demonstrating  | its applicability    |     | to both low |
| The simulation      |                   | environment |               | was           | designed | to capture the   |         |                |     |                |                      |     |             |
|                     |                   |             |               |               |          |                  | and     | high-data-rate |     | IoT devices    | and its robustness   |     | in various  |
| dynamic             | and unpredictable |             | behavior      |               | typical  | of IoT networks. |         |                |     |                |                      |     |             |
IoT settings.
| Several     | factors | contribute | to  | the stochastic |     | nature of the |     |         |          |     |     |     |     |
| ----------- | ------- | ---------- | --- | -------------- | --- | ------------- | --- | ------- | -------- | --- | --- | --- | --- |
| simulation: |         |            |     |                |     |               | B.  | Latency | Analysis |     |     |     |     |
• IoT Device Behavior: Each IoT device generates data The latency values reported bellow are the averages over
packets at random intervals, following a Poisson distri- multiple simulation runs. As shown in Figure 3, our proposed
butionwithanaveragearrivalrateof30jobspersecond.
|     |     |     |     |     |     |     | framework, |     | DQN2, | achieves | the lowest latency | of  | 13.8 ms on |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | -------- | ------------------ | --- | ---------- |
This randomness in job generation simulates the variable average, with a standard deviation of 0.6 ms. This significant
| nature  | of  | IoT traffic. |     |     |     |     |             |     |      |                |           |       |           |
| ------- | --- | ------------ | --- | --- | --- | --- | ----------- | --- | ---- | -------------- | --------- | ----- | --------- |
|         |     |              |     |     |     |     | improvement |     | over | other methods, | including | a 31% | reduction |
| Network |     | Conditions:  |     |     |     |     |             |     |      |                |           |       |           |
• The network conditions, such as compared to the DQN (20 ms), underscores the effectiveness
latency and bandwidth availability, vary over time based of our dual-stage in which the RL agents can make more
| on  | real-time | demands | and | traffic | patterns, | which are also |          |     |           |       |                      |      |         |
| --- | --------- | ------- | --- | ------- | --------- | -------------- | -------- | --- | --------- | ----- | -------------------- | ---- | ------- |
|     |           |         |     |         |           |                | informed |     | decisions | about | resource allocation. | This | precise |
randomly generated to reflect realistic scenarios. understandinghelpstoavoidunnecessarydelaysandoptimizes
Reinforcement Learning Exploration: The reinforce- the flow of data through the network.
•
| ment   | learning   | agent       | uses | an epsilon-greedy |     | strategy for     |     |     |     |     |     |     |     |
| ------ | ---------- | ----------- | ---- | ----------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
| action | selection, | introducing |      | randomness        |     | in the decision- |     |     |     |     |     |     |     |
30
| making | process. |     | This helps | the | agent | explore different | )sm( |     |     |     |     |     |     |
| ------ | -------- | --- | ---------- | --- | ----- | ----------------- | ---- | --- | --- | --- | --- | --- | --- |
20
|     |     |     |     |     |     |     |     | 20  |     | 18  | 17  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
resource allocation strategies and avoid local optima. 15 13.8
ycnetaL
| To ensure        | the      | robustness | and    | reliability  | of  | our results, each |     | 10  |     |                  |      |     |      |
| ---------------- | -------- | ---------- | ------ | ------------ | --- | ----------------- | --- | --- | --- | ---------------- | ---- | --- | ---- |
| simulation       | used     | different  | random | seeds.       | The | results presented |     |     |     |                  |      |     |      |
| in the following |          | sections   | are    | the averages | of  | 10,000 episodes,  |     | 0   |     |                  |      |     |      |
|                  |          |            |        |              |     |                   |     | DQN |     | cTMvSDNQoS-aware | DQN1 |     | DQN2 |
| and the          | standard | deviations | are    | included     | to  | provide a measure |     |     |     |                  |      |     |      |
of variability.
Fig.3. Latencycomparisonofdifferentmethods.Thebarsrepresentthemean
A. Throughput Analysis throughput,andtheerrorbarsrepresentthestandarddeviation.
| Our proposed |     | DQN-based |     | resource | allocation | framework |     |     |     |     |     |     |     |
| ------------ | --- | --------- | --- | -------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
shows significant improvements in throughput compared to C. Energy Consumption Analysis
traditional methods. The throughput values reported are the The energy consumption values reported are the averages
averages over multiple simulation runs. In the figures, our over multiple simulation runs. Figure 4 illustrates the energy
proposed method is referred to as DQN2, while the others, consumption of different methods. Our proposed framework,
DQN [12] and DQN1 [7], are methods from related works. DQN2, achieves the lowest energy consumption of 128 mJ
Figure 2 shows the throughput achieved by different meth- on average, with a standard deviation of 6.4 mJ. This re-
ods. Our proposed framework, DQN2, achieves a throughput duction, achieved through advanced state representation and
of 12.15 Gbps on average, with a standard deviation of 0.3 a comprehensive reward function, demonstrates the efficiency
Gbps. This is significantly higher than advanced methods like of our resource management approach in reducing the energy
DQN (10 Gbps), cTMvSDN (10.33 Gbps), and QoS-aware footprint of IoT networks.
(10.98 Gbps). The integration of dual-stage DQN and multi- The reward function incentivizes the RL agents to make
agent reinforcement learning contributed to this improvement decisions that optimize the use of resources while minimizing
forthereasontheagentscoordinatewitheachothertoachieve energy consumption. By balancing performance and energy
globalnetworkoptimization,ensuringthatlocalimprovements efficiency, the framework ensures that energy is used only
| contribute | to the | overall | network | performance. |     |     | when | necessary. |     |     |     |     |     |
| ---------- | ------ | ------- | ------- | ------------ | --- | --- | ---- | ---------- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: UNIVERSIDADE FEDERAL DE LAVRAS. Downloaded on November 05,2024 at 15:15:22 UTC from IEEE Xplore.  Restrictions apply.

200
150 140 138 130 128
100
0
DQN cTMvSDNQoS-aware DQN1 DQN2
)Jm(
noitpmusnoC
ygrenE
Fig. 4. Energy consumption comparison of different methods. The bars
represent the mean throughput, and the error bars represent the standard
deviation.
D. Fairness Analysis
1.5
1 0.85 0.88 0.89 0.91 0.93
0.5
0
DQN cTMvSDNQoS-aware DQN1 DQN2
xednI
ssenriaF
state representation with RNNs allows for better capturing of
temporal traffic patterns, and the multi-agent reinforcement
learning approach optimizes local and global resource alloca-
tion.Theresultshighlightthepotentialoftheproposedframe-
work to be extended to other network scenarios, including
more complex and large-scale IoT deployments. Future work
will focus on exploring these extensions and further refining
the reinforcement learning algorithms to achieve even better
performance. Future research will explore the application of
our framework to diverse IoT scenarios and investigate the
integrationofothermachinelearningtechniquestoenhanceits
robustness and scalability. Additionally the proposed method
will be compared to other multi-agent deep reinforcement
learning methods.
REFERENCES
[1] M.O.Akinsanya,C.C.Ekechi,andC.D.Okeke,“Securityparadigms
for iot in telecom networks: conceptual challenges and solution path-
ways,” Engineering Science & Technology Journal, vol. 5, no. 4, pp.
1431–1451,2024.
[2] R.L.Rosa,D.Z.Rodriguez,andG.Bressan,“Sentimeter-br:Asocial
webanalysistooltodiscoverconsumers’sentiment,”in2013IEEE14th
international conference on mobile data management, vol. 2. IEEE,
2013,pp.122–124.
[3] R. Jeyaraj, A. Balasubramaniam, A. K. MA, N. Guizani, and A. Paul,
“Resourcemanagementincloudandcloud-influencedtechnologiesfor
internetofthingsapplications,”ACMComputingSurveys,vol.55,no.12,
pp.1–37,2023.
Fig. 5. Fairness comparison of different methods. The bars represent the [4] A. Narwaria and A. P. Mazumdar, “Software-defined wireless sensor
meanfairnessindexandtheerrorbarsrepresentthestandarddeviation. network:Acomprehensivesurvey,”JournalofNetworkandComputer
Applications,p.103636,2023.
As depicted in Figure 5, our proposed framework achieves [5] N.N.Josbert,M.Wei,W.Ping,andA.Rafiq,“Alookintosmartfactory
the highest fairness index of 0.93 on average, with a standard forindustrialiotdrivenbysdntechnology:Acomprehensivesurveyof
taxonomy,architectures,issuesandfutureresearchorientations,”Journal
deviation of 0.03. This indicates a more equitable distribution
ofKingSaudUniversity-ComputerandInformationSciences,p.102069,
of resources among IoT devices compared to DQN (0.85), 2024.
cTMvSDN (0.88), QoS-aware (0.89), and DQN1 (0.91). The [6] M. A. Zormati and H. Lakhlef, “An overview of machine learning-
enabled network softwarization for the internet of things,” in 2023 In-
multi-agentapproachandenhancedrewardfunctioncontribute
ternationalConferenceonSoftware,TelecommunicationsandComputer
to this improvement by ensuring fairness in resource allo- Networks(SoftCOM). IEEE,2023,pp.1–6.
cation. The fairness values reported are the averages over [7] A. L. de Sousa, O. D. OKey, R. L. Rosa, M. Saadi, and D. Z.
Rodriguez, “A novel resource allocation in software-defined networks
multiple simulation runs.
for iot application,” in 2023 International Conference on Software,
TelecommunicationsandComputerNetworks(SoftCOM). IEEE,2023,
V. CONCLUSION pp.1–5.
[8] K.N.Qureshi,A.Alhudhaif,M.Azahar,I. T.Javed,andG.Jeon,“A
The experimental results validate our proposed dual-stage
software-defined network-based intelligent decision support system for
DQN-based resource allocation framework in enhancing net- theinternetofthingsnetworks,”WirelessPersonalCommunications,vol.
work performance across key metrics. By integrating rein- 126,no.4,pp.2825–2839,2022.
[9] S. Chandramohan, M. Senthilkumaran, and M. Sivakumar, “Adaptive
forcement learning into the SDN architecture, our framework
computing optimization for industrial IoT using sdn with edge com-
enables continuous adaptation and optimization of resource puting,”inInternationalConferenceonComputingMethodologiesand
allocation strategies based on real-time network conditions. Communication,2022,pp.360–365.
[10] A. Javadpour and G. Wang, “cTMvSDN: improving resource manage-
This adaptability is essential for maintaining high perfor-
ment using combination of Markov-process and TDMA in software-
mance in ever-changing IoT environments. The enhancements definednetworking,”TheJournalofSupercomputing,pp.1–23,2022.
introduced in our framework, such as the dual-stage DQN [11] P.Kamboj,S.Pal,S.Bera,andS.Misra,“QoS-awaremultipathrouting
in software-defined networks,” IEEE Transactions on Network Science
architecture,multi-agentreinforcementlearningapproach,and
andEngineering,vol.10,no.2,pp.723–732,2023.
advanced state representation with RNNs, contribute to the [12] X.Xiong,K.Zheng,L.Lei,andH.Lu,“Resourceallocationbasedon
observed performance gains. These innovations ensure more deepreinforcementlearninginIoTedgecomputing,”IEEEJournalon
SelectedAreasinCommunications,vol.PP,pp.1–1,042020.
stable learning, better handling of temporal correlations, and
more holistic optimization of network performance. DQN2
outperforms DQN [12] and DQN1 [7] due to the integration
of a dual-stage DQN architecture, which enhances learning
stabilityandhandlestemporalcorrelationsinnetworkstateob-
servations more effectively. Furthermore, the use of advanced
Authorized licensed use limited to: UNIVERSIDADE FEDERAL DE LAVRAS. Downloaded on November 05,2024 at 15:15:22 UTC from IEEE Xplore. Restrictions apply.