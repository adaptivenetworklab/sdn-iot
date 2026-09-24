# Toward an Efficient and Dynamic Allocation of Radio Access Network Slicing Resources for 5G Era

> Source file: `Toward an Efficient and Dynamic Allocation of Radio Access Network Slicing Resources for 5G Era.pdf`

---

Received2August2023,accepted19August2023,dateofpublication28August2023,dateofcurrentversion7September2023.
DigitalObjectIdentifier10.1109/ACCESS.2023.3309294
Toward an Efficient and Dynamic Allocation
of Radio Access Network Slicing Resources
for 5G Era
XIAOLEICHANG 1,2,TIANJI1,2,RUNSUZHU3,ZHENZHOUWU2,CHENXILI 2,
ANDYONGJIANG 4
1TsinghuaUniversity,Beijing100000,China
2ResearchInstituteofTsinghuaUniversityinShenzhen,Shenzhen518000,China
3LonghuaDistrictGovernmentServiceDataAdministration,Shenzhen518000,China
4TsinghuaShenzhenInternationalGraduateSchool,Shenzhen518000,China
Correspondingauthor:ZhenzhouWu(wuzhenzhou@qzcloud.com)
ThisworkwassupportedinpartbytheShenzhenScienceandTechnologyProgramunderGrantSGDX20190917160803729.
ABSTRACT Withthedevelopmentof5GtechnologyandInternetofThings(IoT),moreandmoredevices
areconnectedthrough5Gwirelessly.Radioaccessnetwork(RAN)slicing,asakeyfeatureof5G,enables
a flexible bandwidth resource allocation policy, and facilitates various types of services to operate on
differentnetworkslices.However,RANslicingresourcesisscarce,thuseffectivemanagementofwireless
bandwidthresourcesinRANslicingbecomesindispensabletoimproveusersatisfaction.Extensiveresearch
has investigated into RAN slicing, but they do not take user mobility into consideration. While RAN
slicingallocationhasagreatimpactonuserexperienceinmobile5Gscenarios,usermobilityposesgreat
challengestonetworkmanagementandcausingunsatisfactionofusers.Inthispaper,weproposeanewRAN
slicingallocationstrategybasedonmachinelearning,tomaximizespectrumefficiencywhileguaranteeing
the Service Satisfaction Ratio (SSR) of various slicing services. To further alleviate the SSR fluctuation
brought by user mobility, we study into the temporal characteristics of user mobility and preprocess the
state sequences using Long Short-Term Memory (LSTM) networks. Finally, these sequences are taken as
the input of an Advantage Actor Critic (A2C) reinforcement learning network to develop a RAN slicing
allocationpolicy.Weconductcomprehensivesimulations,andtheresultsshowthattheperformanceofthe
proposedmechanismoutperformsthetraditionalmechanisminensuringSSRandenhancingthespectrum
efficiency.
INDEXTERMS InternetofThings,networkslicing,reinforcementlearning,radioaccessnetworks.
I. INTRODUCTION typesofuserdemandsthroughdifferentnetworkslices,which
ThedevelopmentofIoThasledtomoreandmoreIoTuser canbeseenasvirtualizedbandwidthresourcesbasedonthe
devicesconnectingtothenetwork,eachwithdifferentservice same physical connection. Network slices can ensure trans-
qualityrequirements.Traditional4Gnetworkprovidesband- mission rate, latency, and security, and can be customized
widthresourcestousersuniformly,whichisnotefficientand accordingtouserrequirements,whichismuchmoreflexible
dynamic. The current 5G network brings new opportunities thanpreviouswirelesscommunicationtechnology.
withmanynewproposedtechnologies,suchasMobileEdge However, RAN slicing resource is still very expensive
Computing(MEC),andRANslicingtechnologyinthelatest and needs to be efficiently orchestrated. However, due to
3GPP standard [1]. Among them, RAN slicing technology the various types of user requirements, it is difficult to
provides room for future innovation by addressing various efficiently allocate slices while satisfying user demands.
Although many previous works studied slice resource allo-
The associate editor coordinating the review of this manuscript and cations[2],moreandmoremobiledevicesappearin5Gsce-
approvingitforpublicationwasRentaoGu . nariosandtheyposegreaterchallengesforslicingallocation
2023TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
VOLUME11,2023 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 95037

X.Changetal.:TowardanEfficientandDynamicAllocationofRANSlicingResourcesfor5GEra
becauseuserexperiencewillfluctuateinmobilestates.Thus, totransitiontos k+1 ,andtheagentreceivesarewardr k forthis
an efficient and dynamic allocation mechanism for RAN action.Sincethedecisionfortakinganactiondependsonly
slicingresourcesisbadlyneededinthe5Gera. onthecurrentstate,thisprocesscanbeviewedasaMarkov
In this paper, we take user mobility into consideration decision process (MDP). M =< S,A,P ,R >, where S
r
while allocating 5G slice resources to multiple users from represents the set of states, A represents the set of actions,
a wireless base station. The system needs to meet two P (cid:0) s′|s,a (cid:1) represents the probability of taking action a to
r
different goals, 1) to maximize the system utility, which transition from state s to state s′, and R(s,a) represents the
indicates the overall SSR, and 2) to predicate the future rewardfortakingactionainstates.BecauseoftheMarkov
movement of mobile users and be adaptive when allocating property of the reinforcement learning process, it naturally
slices to them. To achieve the best of two worlds, we first applies to decision-making tasks based on environmental
formulatetheproblemasanoptimizationproblemthatmax- states, such as industrial control, scheduling decisions, and
imizes overall user utility while satisfying bandwidth and gameAI.
mobilityconstraints.ThenweutilizeanA2Creinforcement Reinforcement learning can be divided into two cate-
learning-basedalgorithm,whichcombinestheadvantagesof gories based on the environmental model: model-based and
value-based and policy-based approaches to train the agent. model-free. Model-based reinforcement learning can obtain
Throughtrainingthedecisionmodelinasimulationenviron- the state transition probability of the environmental model
ment,thisapproachcanefficientlyallocatewirelessnetwork to plan decision-making, i.e., the environmental model is
bandwidthwhenenvironmentanduserdemandchange. known. Model-free reinforcement learning does not predict
Although A2C is adaptive to state changes, user mobil- the state, but constantly optimizes the model through envi-
ity patterns are difficult to learn. To further improve the ronmental reward feedback. Currently, most of the research
performance of the proposed system, we record the final on reinforcement learning focuses on model-free reinforce-
statesequenceunderusermobilityandthenapplyanLSTM ment learning, which includes two types: value-based and
network to extract the temporal characteristics of these policy-basedreinforcementlearningalgorithms.Value-based
sequencesandpredicatethefuturestates. reinforcementlearningismainlyrepresentedbyQ-learning,
We conduct comprehensive simulations, and the results DQN [3], Dueling DQN [4] and Double DQN [5] algo-
show that the A2C algorithm model integrated with the rithms.Comparedwithvalue-basedalgorithms,policy-based
LSTM network can accurately allocate wireless bandwidth algorithms can handle discrete/continuous space problems
resources after efficient training, while ensuring the SSR of and have better convergence. Moreover, policy-based algo-
differentusers. rithms tend to fall into the dilemma of local optima due to
The paper is structured as follows: Section II introduces theirlargetrajectoryvarianceandlowsampleutilization[6].
relevant research works, including 5G network slicing and The reinforcement learning algorithms used in this paper
reinforcement learning for resource allocation. Section III are mainly policy-based reinforcement learning algorithms,
describes the framework of our RAN slicing allocation sys- such as REINFORCE, A2C [7], DDPG [8], PPO [9], and
tem.SectionIVformulatestheoptimizationproblemforthe SAC[10].Themainfeatureofpolicygradientmethodsisto
wireless network slicing allocation model. Section V pro- directly model and optimize policies. The policy is usually
poses the algorithm design, integrating the LSTM network defined as a function π θ (a|s) with parameter θ. Since the
and A2C reinforcement learning. Section VI simulates var- objective function’s value is directly affected by the policy,
ious scenarios to validate the performance of the proposed manyreinforcementlearningalgorithmscanbeemployedto
algorithm. Finally, Section VII summarized the paper and optimizeθ tomaximizetheobjectivefunction.
futurework.
B. NETWORKSLICING
II. RELATEDWORK With the growing maturity of 5G networks, a variety of
A. REINFORCEMENTLEARNING terminaldevicesareaccessingwirelessnetworksthrough5G
Reinforcement learning (RL) is one of the paradigms of technology. These devices generate varying user demands
machine learning. Data plays a crucial role in the final for network services with regard to bandwidth, latency,
performance results of machine learning models. Unlike and reliability. The International Telecommunication Union
supervised and unsupervised learning, reinforcement learn- has identified three distinct categories of 5G application
ing depends mainly on interacting with the environment to requirements: Enhanced Mobile Broadband (eMBB), Mas-
generate data for learning and continually optimizing the sive Machine-Type Communications (mMTC), and Ultra-
modelthroughtrialanderror.Specifically,inreinforcement Reliable Low-Latency Communications (URLLC). The
learning,anagentgeneratesanactionbasedontheobserved diverse task requirements and a growing number of device
environmental state and policy, which affects the environ- connections raise new challenges to the existing network
mentalstate,andreceivesrewardsforoptimizingthepolicy architecturesandresourcemanagement.
model through this interactive process. At the kth step, the Network slicing integrates Software-Defined Networking
agent observes the environmental state s and returns an (SDN)andNetworkFunctionVirtualization(NFV)technolo-
k
actiona totheenvironment,causingtheenvironmentalstate giestoofferindependentnetworkresourcestodifferentusers
k
95038 VOLUME11,2023

X.Changetal.:TowardanEfficientandDynamicAllocationofRANSlicingResourcesfor5GEra
withdiverserequirementsinaflexiblemanner.Asakeytech- to users in eMBB and URLLC service slices for short time
nologyof5G,networkslicingmeetsaplethoraofuserservice slots.Wangetal.[19]jointlyoptimizedthecommunication,
demands. Specifically, operators create multiple logically computing, and caching resource allocation in MEC. The
independent networks on a shared physical network infras- optimization objective of this research was to maximize a
tructure,whichformsalogicalisolationofnetworkresources utility function while ensuring user service quality. A twin-
among different network slices, ensuring that services on actorDeepDeterministicPolicyGradient(twin-actorDDPG)
different network slices do not mutually interfere. Besides, algorithm was proposed to solve the problem. According to
inresponsetovaryingnetworkresourcedemandsofdifferent thecharacteristicsof5GNewRadio(NR),Boutibaetal.[20]
slices, network slicing technology can dynamically allocate used deep reinforcement learning to allocate network slice
resourcesflexiblytodifferentslicesonthesamephysicalnet- bandwidthtomaximizethroughputandensureservicequal-
work.Torealizeend-to-endnetworkslicingservices,network ity satisfaction, which verified the effectiveness of their
slicing can be divided into core network slicing and RAN algorithms in larger bandwidth and more user scenarios.
slicing. The core network is mainly composed of network Boutibaetal.[21] proposed a flexible slicing resource allo-
servers and their links, abstracting the underlying physical cation framework for 5G NR. For industrial IoT scenarios,
network resources (link bandwidth, CPU resources, storage Maietal.[22]adjustedthetransmissionpowerandspreading
resources) with SDN and NFV technologies and providing factor to satisfy service quality. Messaoudetal.[23] exam-
different network services with varying quality of service ined the computing resources, service quality satisfaction,
toupper-layerapplications.RANslicing,ontheotherhand, and privacy data of industrial IoT and used federated rein-
primarilyallocatesnetworkbandwidthtouserswithdifferent forcement learning to adjust the transmission power and
demands,consideringthelimitednetworkbandwidthofbase
spreadingfactor.Fordiscretechannelassignmentsandcon-
stations.Balancingmaximumbandwidthefficiencyanduser tinuousenergyharvestingtimedivision,Xuetal.[24]useda
servicequalityofdifferentsliceswithinthelimitedwireless discrete-hybridSoftActor-Critic(SAC)algorithmtoallocate
networkcommunicationbandwidthisamajorresearchfocus resources. To optimize the SSR and SE of RAN slicing
ofRANslicing.Theresearchonnetworkslicinginthispaper services, Li et al. utilized various reinforcement learning
isalsofocusedontheaspectofRANslicing.
|     |     |     |     |     |     |     | algorithms,         | such | as Deep     | Q-Network | (DQN)     | [25],     | multi- |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | ---- | ----------- | --------- | --------- | --------- | ------ |
|     |     |     |     |     |     |     | agent reinforcement |      | learning    | based     | on graph  | attention | net-   |
|     |     |     |     |     |     |     | work [26],          | and  | distributed | DQN       | algorithm | based     | on the |
C. RESEARCHSTATUEOFNETWORKSLICINGINMEC
|     |     |     |     |     |     |     | generative | adversarial |     | network | [27]. Some | other | studies |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ------- | ---------- | ----- | ------- |
Asacriticaltechnologyfor5G,networkslicingplaysavital usedmulti-agentreinforcementlearningmethodsforparallel
| role in meeting |     | a variety | of service | demands. | While | ensur- |          |          |        |       |                  |       |       |
| --------------- | --- | --------- | ---------- | -------- | ----- | ------ | -------- | -------- | ------ | ----- | ---------------- | ----- | ----- |
|                 |     |           |            |          |       |        | training | to speed | up the | model | training process | [28], | [29]. |
ing the isolation of services, dynamically allocating RAN Regardingthetimeseriesproblemcausedbythemobilechar-
bandwidth resources to ensure service satisfaction poses acteristics of users in MEC, Cuietal.[30] and Lietal.[31]
| challenges. | Khamse-Ashari |     | et  | al. [11] conducted |     | resource |          |      |          |      |               |          |     |
| ----------- | ------------- | --- | --- | ------------------ | --- | -------- | -------- | ---- | -------- | ---- | ------------- | -------- | --- |
|             |               |     |     |                    |     |          | combined | LSTM | networks | with | reinforcement | learning | to  |
allocationwithinaparticularnetworkslicetomaximizeuser allocatenetwork-slicingresourcestoensuretheserviceSSR
| SSRs in | it. Based | on  | a distributed | mechanism, |     | the study |     |     |     |     |     |     |     |
| ------- | --------- | --- | ------------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
amongmobileusers.Liuetal.[32]combinedthealternating
performedaniterativeauctioninthenetworksliceandoffered directionmultipliermethodwithdeepreinforcementlearning
| price acceptance |     | to service | providers | to solve       | the | problem.  | toaddressit. |     |     |     |     |     |     |
| ---------------- | --- | ---------- | --------- | -------------- | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- |
| Lietoetal.[12]   |     | asked      | users to  | make automated |     | decisions |              |     |     |     |     |     |     |
Theallocationofnetwork-slicingresourcesrequiresadap-
basedontheirownneedsandadoptedaslice-awarescheduler tive and dynamic resource allocation decisions, and the
toachieveNashequilibriumindecision-making.Somestud-
|     |     |     |     |     |     |     | features | of MDP | in reinforcement |     | learning | algorithms | sug- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---------------- | --- | -------- | ---------- | ---- |
iesuseddeepneuralnetworkstopredictunknownuserinput gest that they are naturally suited for solving such prob-
trafficandallocateittoappropriatenetworkslices[13].Some lems. Therefore, the aforementioned research proposed a
| other studies | adopted |     | blockchain | technology | to  | enhance |              |     |               |     |                     |     |          |
| ------------- | ------- | --- | ---------- | ---------- | --- | ------- | ------------ | --- | ------------- | --- | ------------------- | --- | -------- |
|               |         |     |            |            |     |         | large number | of  | reinforcement |     | learning algorithms |     | for net- |
securityintheprocessofnetworkslicing[14],[15],[16]. workslicingresourceallocationbasedonthecharacteristics
ExistingresearchonRANnetworkslicingmainlyfocuses
|     |     |     |     |     |     |     | of different | reinforcement |     | learning | algorithms | to  | achieve |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | -------- | ---------- | --- | ------- |
on network resource sharing, resource virtualization, slice high performance. This study also adopts a reinforcement
isolation,mobilitymanagement,resourceefficiency,security learning-based approach to address the dynamic allocation
| and privacy, | dynamic | slice | creation | and management |     | [17], |     |     |     |     |     |     |     |
| ------------ | ------- | ----- | -------- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
ofbandwidthresourcesinRAN,withaviewtoensuringthe
wherereinforcementlearning-basedmethodsarewidelyused service SSR of multiple network slicing and improving the
| to seek | solutions. | Setayeshetal.[18] |     | adopted | layered | rein- |     |     |     |     |     |     |     |
| ------- | ---------- | ----------------- | --- | ------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
SEofwirelessbandwidth.
| forcement | learning | to improve |     | the throughput | and | Service |     |     |     |     |     |     |     |
| --------- | -------- | ---------- | --- | -------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
LevelAgreement(SLA)SSRofeMBBandURLLCservice III. SYSTEMSCENARIO
slices. In the research, deep reinforcement learning algo- Inordertoprovideuserswithend-to-endnetworkslicing,itis
rithms were used to adjust slice configuration parameters necessarytosimultaneouslyimplementcorenetworkslicing
for long time slots, and a deep neural network based on an and RAN slicing. With the rapid increase in 5G network
attentionmechanismwasusedtoallocatewirelessresources coverage and the exponential growth of IoT devices, more
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     | 95039 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

X.Changetal.:TowardanEfficientandDynamicAllocationofRANSlicingResourcesfor5GEra
| user devices | are   | accessing   | the       | network        | via wireless | means.   |     |     |     |     |     |     |     |     |
| ------------ | ----- | ----------- | --------- | -------------- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Therefore,   | the   | intelligent | network   | slicing        | system       | scenario |     |     |     |     |     |     |     |     |
| in this      | paper | mainly      | considers | the deployment |              | of RANs. |     |     |     |     |     |     |     |     |
Fig.1showsawirelessnetworkresourcedynamicallocation
frameworkbasedonSDNarchitectureintheRANscenario.
Thesystemscenariomainlyincludesthefollowingelements:
1) User:ThroughtheRANbandwidthsignalofthebase
| station, |          | users generate | different         |            | applications | accord-        |     |     |     |     |     |     |     |     |
| -------- | -------- | -------------- | ----------------- | ---------- | ------------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ing      | to their | own            | needs. Therefore, |            | wireless     | networks       |     |     |     |     |     |     |     |     |
| should   | provide  | network        | resources         |            | of different | quality        |     |     |     |     |     |     |     |     |
| levels.  | At       | the same       | time,             | users move | at           | a certain rate |     |     |     |     |     |     |     |     |
| within   | the      | range          | of wireless       | signals    | of           | the base sta-  |     |     |     |     |     |     |     |     |
tion,anddifferentusershavedifferentrequirementsfor
| data | packets | based | on the | distribution | of  | their spatial |     |     |     |     |     |     |     |     |
| ---- | ------- | ----- | ------ | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
locations.
| 2) Wireless |     | base station: | Providing |     | RAN | services to |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------- | --------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
FIGURE1. Systemscenarioofnetworkslicing.
| users | within | a certain | range, | offering | data | transmis- |     |     |     |     |     |     |     |     |
| ----- | ------ | --------- | ------ | -------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
sionserviceswithlimitedwirelessbandwidthresources
demanddofslicesvariesaccordingtothedistributionofuser
(e.g.10MHz).
mobility.
| 3) Network |     | slicing: | Abstracting |     | wireless | bandwidth |     |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ----------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
resourcestodividethemintologicallyindependentnet-
IV. PROBLEMMODEL
works,withslicesnotaffectingeachother.According
|     |             |       |           |        |         |         | The system | aims        | to maximize |       | system  | utility, | which  | is  |
| --- | ----------- | ----- | --------- | ------ | ------- | ------- | ---------- | ----------- | ----------- | ----- | ------- | -------- | ------ | --- |
| to  | the service | type, | different | slices | provide | network |            |             |             |       |         |          |        |     |
|     |             |       |           |        |         |         | a weighted | combination |             | of SE | and SLA | SSR.     | First, | the |
resourceservicesofdifferentlevels,i.e.differentallo-
Shannontheoremcanbeemployedtocalculatethedownlink
cated resources. Based on changes in slice service rater ofuseru inslicen:
|               |     |     |         |          |            |         | un  |     | n       |     |          |     |     |     |
| ------------- | --- | --- | ------- | -------- | ---------- | ------- | --- | --- | ------- | --- | -------- | --- | --- | --- |
| requirements, |     | the | network | resource | allocation | in time |     |     |         |     |          |     |     |     |
|               |     |     |         |          |            |         |     |     | (cid:0) |     | (cid:1), |     |     |     |
seriesisadjustedtomeetdifferentserviceneeds. r =w log 1+SNR ∀u ∈U (1)
|             |     |             |     |          |          |           |           | un                                     | n   |     | un  | n   |     |        |
| ----------- | --- | ----------- | --- | -------- | -------- | --------- | --------- | -------------------------------------- | --- | --- | --- | --- | --- | ------ |
| 4) Service: |     | Classifying | the | services | provided | by slices |           |                                        |     |     |     |     |     |        |
|             |     |             |     |          |          |           | where,SNR | un isthesignal-to-noiseratiooftheuseru |     |     |     |     |     | n with |
basedonthenetworkservicerequirementsoftheuser’s
thebasestation.Throughthedownlinkrateoftheuser,SEcan
| application |     | type, | such as | VoLTE | providing | call ser- |     |     |     |     |     |     |     |     |
| ----------- | --- | ----- | ------- | ----- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
becalculatedusingthefollowingformula:
| vices,                                         | eMBB        | providing |             | online | video, | VR, AR and   |         |     |         |                 |     |                |     |     |
| ---------------------------------------------- | ----------- | --------- | ----------- | ------ | ------ | ------------ | ------- | --- | ------- | --------------- | --- | -------------- | --- | --- |
|                                                |             |           |             |        |        |              |         |     |         | P P             |     |                |     |     |
| otherservices,URLLCprovidingautonomousdriving, |             |           |             |        |        |              |         |     |         | n∈N             | ∈U  | r un           |     |     |
|                                                |             |           |             |        |        |              |         |     | SE =    |                 | un  |                |     | (2) |
| remotemedicalandotherservices.                 |             |           |             |        |        |              |         |     |         | W               |     |                |     |     |
|                                                |             |           |             |        |        |              | The SSR | of  | slice n | can be obtained |     | by calculating |     | the |
| Central                                        | controller: |           | Maintaining | user   | state  | information, |         |     |         |                 |     |                |     |     |
totalnumberofsuccessfullytransmitteddatapacketsandthe
| base station | wireless | network | resource |     | information, | service |              |     |          |               |     |         |          |     |
| ------------ | -------- | ------- | -------- | --- | ------------ | ------- | ------------ | --- | -------- | ------------- | --- | ------- | -------- | --- |
|              |          |         |          |     |              |         | total number | of  | received | data packets. |     | In this | section, | P   |
information, etc. as the system’s global information collec- un
|     |     |     |     |     |     |     | is defined | as the | data packet | transmitted |     | by the | base | station |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ----------- | ----------- | --- | ------ | ---- | ------- |
tor.Servingasthecontrollerinthewirelessnetworkslicing
|     |     |     |     |     |     |     | for user | u , and | a is | used to | indicate | whether | a   | specific |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ---- | ------- | -------- | ------- | --- | -------- |
scenario, sending control signals based on the allocation n pun
|           |             |         |            |     |     |              | data packet | p   | is successfully | transmitted. |     | Only | when | the |
| --------- | ----------- | ------- | ---------- | --- | --- | ------------ | ----------- | --- | --------------- | ------------ | --- | ---- | ---- | --- |
| decisions | of wireless | network | resources, |     | and | managing and |             | un  |                 |              |     |      |      |     |
user’stransmissionrateisgreaterthantherequiredrateforthe
schedulingwirelessresources.Theintelligentnetworkslicing
|                                                        |     |     |     |     |     |     | servicelevelr | ,andtheresponselatencyofthedatapacketis |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
| algorithminthissectionisdeployedinthecentralcontroller |     |     |     |     |     |     |               | n                                       |     |     |     |     |     |     |
to realize the bandwidth resource decision-making function lessthanthemaximumlatencythattheservicelevelcanbear
|                   |     |     |     |     |     |     | l ,thatis,r | ≥r  | and | l ≤l | ,a    | =1.Therefore,SSR |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ---- | ----- | ---------------- | --- | --- |
| ofnetworkslicing. |     |     |     |     |     |     | n           | un  | n   | pun  | n pun |                  |     |     |
canbecalculatedusingthefollowingformula:
Thissectionmainlyadoptsthefrequencydivisionduplex-
|     |     |     |     |     |     |     |     |     | P   | P   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ing (FDD) scheme to allocate network bandwidth for the un ∈U pun ∈Pun a pun
|                                                     |     |     |     |     |     |     |     | SSR= |     |     |     |     |     | (3) |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
| downlink,wherethetransmissionoftheuplinkanddownlink |     |     |     |     |     |     |     |      |     | P   |     |     |     |     |
∈U P un
| arecarriedoutatdifferentfrequencies.Besides,itisassumed |     |         |        |           |     |               |                               |     |     | un  |     |     |     |     |
| ------------------------------------------------------- | --- | ------- | ------ | --------- | --- | ------------- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                                                         |     |         |        | 1,2,...,N |     |               | Sotheproblemcanbedescribedas: |     |     |     |     |     |     |     |
| that a series                                           | of  | network | slices |           |     | share limited |                               |     |     |     |     |     |     |     |
wireless bandwidth W, with each slice providing network maxα·SE(d,w)+β·SSR(d,w)
(4)
| resourcesforacertaintypeofuserU |     |     |     |     |     |     |     | w   |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
.Thechangingdemand
|     |     |     |     |     |     |     |     |     | P   |     | P   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofeachsliceisrepresentedbyvectord = {d ,d ,...,d }. Anditfollows w = W, P = d ,w =
|     |     |     |     |     | 1   | 2 N |     |     | n ∈ N | n   | u n ∈ | U u | n   | n i |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- |
Basedonthequantityofdemand,servicetype ,an ddecisi on k ·ω,∀i ∈ [1,2,... , N ].W here,α an d β are w eight fact ors
|     |     |     |     |     |     |     |     |     |     |     | β   | [β  | ,β ,...,β |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
algorithms of different slices, the system allocates differ- for SE and SSR, respectively, and = 1 2 N ]
ent bandwidth resources = {w ,w ,...,w } to them, with representstheweightfactorsforeachslice.ωistheminimum
|     |     |     |     | 1 2 | n   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the bandwidth allocated to slices represented by w n . The unitofbandwidthallocation.
| 95040 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

X.Changetal.:TowardanEfficientandDynamicAllocationofRANSlicingResourcesfor5GEra
Duringthecourseofthisresearch,severaltechnicalchal- A(s ,a )=Q(s ,a )−V (s ), which can usually be com-
t t t t t
lenges were encountered. On one hand, users exhibit a putedwithminimalbiasusingtheTDerror:
multitude of characteristic attributes, making feature selec-
tionsomewhatintricate.WeemployedLSTMtocapturethe
temporal features of user mobility, facilitating the devel-
A(s t ,a t )≈r t +γV (s t+1 |s t ,a t )−V (s t )=δ(s t ) (5)
opment of slice allocation strategies. On the other hand, Thegradientoftheactornetworkis∇θlogπ(a t |s t ;θ)δ(s t ),
achieving realistic simulation of slice application scenar- andthelossfunctionofthecriticnetworkisL critic =δ(s t )2.
ios posed certain challenges. We established a model for
wireless network slice applications and devised various B. LSTM
simulation scenarios encompassing extensive user popula- Duetothemobilityofuserswithinthewirelessaccessrange,
tions, rapid connections, high bandwidth, and mixed-use and the position distribution resulting from user mobility
environments. affectingtheamountoftransmitteddatapacketsP ,thedata
un
packet demand of each slice d undergoes dynamic changes
as users move. Recurrent neural networks (RNNs) are a
V. REINFORCEMENTLEARNING-BASEDRESOURCE type of neural network used to process serial data. Com-
ALLOCATIONALGORITHMFORNETWORKSLICING pared with general neural networks, they are more capable
A. A2CALGORITHM ofhandlingserialdatawithchanges.Tocapturethemoving
Similartootherreinforcementlearningmethods,theAdvan- features of users in the time series, this section uses an
tage Actor-Critic (A2C) algorithm [7]used in this section LSTM network [33] to preprocess the environmental state.
also continuously optimizes the model through interactive LSTMeffectivelycapturestemporalfeaturesofusermobility
trial and error with the environment, which can be viewed statesthroughinternalgatingmechanismsandmemoryunits.
as an MDP. At the core of A2C lies an actor-critic frame- Itselectivelyretainsandforgetsinformation,accommodating
work, where the actor is responsible for decision-making, varyingmobilepatternsacrossdifferenttimesteps,managing
determining which action (i.e., resource allocation strategy) intricate temporal sequence dependencies, and preserving
to take given a state, while the critic estimates the value of bothlong-termandshort-termmobilitypatterns.Specifically,
this decision. In the context of resource slicing, the actor a queue is used to store the observed state of the environ-
can be represented as a neural network that takes environ- ment at each step in the time series, the past two observed
mental states as input and outputs a probability distribution sequences are extracted and preprocessed by an LSTM net-
representing the allocation probabilities for different slices. work, and then the preprocessed states of the two observed
Thecriticcanbeanotherneuralnetworkusedtoestimatethe sequences are concatenated as inputs to the actor and critic
valuefunctionofthecurrentstate.Ateachtimestep,anallo- networks.Bypreprocessingpastobservedstatesthroughan
cation action for resource slicing is sampled based on the LSTM network, historical state information is encoded into
actor’s output probability distribution. Subsequently, using cellstates,facilitatingamoreaccuratecaptureofusermobil-
environmentalfeedbackincludingrewardsignalsandthenext itypatternsandtrends.Thesetemporalfeatures’influenceis
state, the advantage is computed, reflecting the superiority thentakenintoaccountduringthedecision-makingprocess.
ofthecurrentactionrelativetotheaveragepolicy.Withthe As a variation of RNNs, the core concept of LSTM lies
advantage, policy gradients for the actor and value function in its cell state and ‘‘gate’’ structure. The cell state serves
gradients for the critic are calculated. The neural network as a path for information transmission, allowing informa-
parameters of both the actor and critic are updated using tion to be propagated throughout the sequence, and can be
thesecomputedgradients.Thisgradualupdateofparameters viewedasthe‘‘memory’’ofthenetwork.Intheory,thecell
causes the actor’s policy to gradually adjust towards bet- statecancarryrelevantinformationthroughoutthesequence
ter slice allocation strategies, and the critic’s value function processing, so even earlier time steps can carry information
estimation to progressively converge to more accurate state to later time steps in the cell, overcoming the influence of
values. By iteratively executing the aforementioned steps, short-term memory. The addition and removal of informa-
continuouslyinteracting withthe environmentandupdating tion can be achieved through the ‘‘gate’’ structure, which
actorandcriticparameters,theresourceallocationstrategyis learnswhichinformationtokeeporforgetduringthetraining
optimized. process. Fig. 2 shows the structure of LSTM. Where, c t−1
Reinforcement learning algorithms aim to achieve max- representsthepreviousLSTMcellstate,h t−1 representsthe
imum cumulative expected reward R = P∞ γkr . previousLSTMcellhiddenstate,⊗representstheproductof
k=0 k
The action value at step t can be evaluated through positions of matrices of the same size, ⊕ represents matrix
Q(s ,a )=E[R |s =s,a =a], while the state value additionandσ representsactivationfunctionsigmoid.There
t t t t t
V (s )=E[R |s =s] can only be estimated based on are three gates in LSTM: the forget gate, the input gate,
t t t
the current transitional state. A2C only adopts the state and the output gate. The forget gate selectively forgets the
value function V for training, thereby reducing the num- inputfromthepreviousstage,thatis,itchoosestoremember
ber of parameters and simplifying the training pro- important information and forget unimportant information.
cess. The advantage in A2C can be obtained through Theinputgateupdatesthecurrentcellstate,decidingwhich
VOLUME11,2023 95041

X.Changetal.:TowardanEfficientandDynamicAllocationofRANSlicingResourcesfor5GEra
FIGURE2. StructureofLSTM.
informationneedstobeupdated.Theoutputgatedetermines
the next hidden state output based on the current input and
theprevioushiddenstate.
InLSTM,c representsthecurrentcellstate,h represents
t t
the current hidden state, and x represents the current input
t
state.Thetreegatestatesaredefinedasz,z ,andz .Theyare
i f o FIGURE3. FrameworkofA2CalgorithmwithLSTMpreprocessing
numbers between 0 and 1 obtained by concatenating x and network.
t
h t−1 , multiplying by weight matrix w, adding bias factor b,
andoutputtingthroughthesigmoid function.Thethreestates representspastL andL states,andprovidedinputto
1 2
canberepresentedbythefollowingformulas: thepolicynetworkandvaluenetwork.
2) Policynetwork:Thisnetworkmainlyupdatesdecision
z i =σ(w i [x t ,h t−1 ]+b i ) (6) policiesandgeneratesactions.Thepreprocessedstate
z f =σ(cid:0) w f [x t ,h t−1 ]+b f (cid:1) (7) features t ′isusedasinputandpassedthroughtwofully
z o =σ(w o [x t ,h t−1 ]+b o ) (8) connectedlayers.Thesizeoftheneuronsinthesecond
fully connected layer is the size of the action space
Based on the above gate states, c t , h t can be obtained by |A|.Then,theactionprobabilitydistribution,orpolicy
thefollowingformulas: π(a |s ), is obtained through the softmax function.
t t
c t =z f ⊗c t−1 +z i ⊗tanh(w c [x t ,h t−1 ]+b c ) (9) Finally,actiona t isselectedbysamplingandexecuted
intheenvironment.
h =z ⊗tanh(c ) (10)
t o t Value Network: This network mainly evaluates the value
Thefinaloutputy t canfrequentlybeobtainedthroughy t = of the current state. The preprocessed state feature s t ′ is
σ(cid:0) w h +b (cid:1) used as input and is outputted through two fully connected
y t y
layers to obtain the value V (s ) of the current state. In the
t
C. ALGORITHM A2Calgorithm,thevaluenetworkalsoneedstocalculatethe
Based on the introduction of the A2C algorithm and the value V (s t+1 |s t ,a t ) of the next state based on the changed
role and structure of LSTM described above, the reinforce- environmental state after the action is executed, in order to
mentlearningalgorithmframeworkadoptedinthissectionis calculatetheTDerror.
shown in Fig. 3. The structure of the algorithm consists of In the actor network, an entropy term with a factor β of
threeparts: 0.01isaddedtoencouragethepolicynetworktoexploreand
1) State sequence preprocessing network: This network select other actions in the action space for better policies.
mainly captures the temporal features of various ser- According to the gradient of the actor network described in
vicerequeststatesequences,includingtwoqueuesthat section V, the loss function for the actor network can be
holdthestates,afullyconnectedlayer,andanLSTM
deducedasfollows:
layer. Specifically, the two queues store two state
L =−δ (s ;θ )logπ(a |s ;θ )−βH(π(a |s ;θ ))
sequences of different lengths in chronological order, actor t t c t t a t t a
enabling the LSTM network to process state features (11)
atdifferenttimeintervals.Thetwostatesequencesare
The parameter update of the actor network can be
input to the fully connected layer to extract features,
describedas:
and then serve as input to the LSTM layer, which
updatesthecellstateandhiddenstatethroughL and
L iterations. The final hidden states h of the
1
two
θ
a
←θ
a
+δ
t
(s
t
;θ
c
)∇θ
a
logπ(a
t
|s
t
;θ
a
)
se 2 quences can be concatenated as a fea t ture s t ′ that + β∇θ a H(π(a t |s t ;θ a )) (12)
95042 VOLUME11,2023

X.Changetal.:TowardanEfficientandDynamicAllocationofRANSlicingResourcesfor5GEra
ThecriticnetworkadoptsthesquaredTDerrorastheloss the SSR of all slices meets the threshold, moderate positive
function,expressedbythefollowingformula: feedback rewards will be given. When the SSR of VoLTE
and eMBB services meets the threshold but the SSR of the
URLLCservicedoesnotmeetthethreshold,therewardwill
L critic =δ t 2 =(r t +γV (s t+1 ;θ c )−V (s t ;θ c ))2 (13) be calculated based on the SSR of URLLC. If q > 0.7,
u
The parameter update of the critic network can be positive feedback rewards will still be given, but when q u
describedas: is small, negative feedback rewards even smaller than −5
will be given. This is because the URLLC service has high
θ
c
←θ
c
+δ
t
(s
t
;θ
c
)∇θ
c
(s
t
;θ
c
) (14)
requirements for latency and relatively large data packets,
making it difficult to guarantee its SSR in limited wireless
Considering the aim of maximizing system utility, the
networkresources.Thus,whenq > 0.7,positivefeedback
system is composed of a weighted combination of SE and u
rewardswillstillbegiven,andwhenq = 0,themaximum
SSR from each slice. To prevent policies in the algorithm u
negativefeedbackpenaltywillbegiven.SinceURLLCtasks
from sacrificing the SSR of certain slices in order to maxi-
are usually critical tasks that require high quality of service
mize SE, the reward during training is set to be segmented.
andhighpriority(e.g.remotemedical,autonomousdriving,
Only when the SSR of all slices exceeds the set threshold
and remote industrial control), their SSR should be ensured
will additional rewards for SE optimization be reflected in
as much as possible. When the SSR of either VoLTE or
therewardfunction.Inthissection’straining,threenetwork
eMBBserviceisbelowthethreshold,relativelylownegative
slicesareusedtoprovidecorrespondingresourcesforVoLTE,
eMBB, and URLLC services. q ,q , and q are defined as feedbackpenaltieswillbegivendirectly.
v e u
As described in the previous section, in order to quickly
the SSR of the VoLTE, eMBB, and URLLC service slices,
map the environmental state to bandwidth allocation deci-
respectively. The reward function can be represented by the
sions, this paper adopts a reinforcement learning algorithm
followingformula:
A2C to train the agent. Also, to achieve better performance
Algorithm1A2CTrainingAlgorithmWithLSTM whentherearefluctuationsinthedatapacketdemandvector
d generated by user mobility, the algorithm in this section
01 Initializingparametersθ aandθ cofactorandcritic
networks incorporates an LSTM network to preprocess the observed
02 InitializingtwoqueuesQ1andQ2oflengthsL1 environmental state to obtain temporal information. The
andL2
training process of the algorithm is shown in The training
03 for1toL2do
04 Randomlysamplingactionarandinactionspace process of the algorithm is shown in Algorithm 1. First,
Aandfeedingitbacktotheenvironment in lines 1-2 of the algorithm, parameters θ and θ of the
a c
05 Observingtheenvironmenttoobtainobsiand
actorandcriticnetworksareinitialized,andtwoqueuesare
insertingitintoQ2
06 ifi<L1thenobsiandinsertingitintoQ1 set up with different lengths (L 1 = 10, L 2 = 100) to
07 endfor storethe observedenvironmental state.Next,L actionsare
2
08 fort=1 tothemaximumnumberofiterationsdo
randomlysampledandexecutedintheenvironmenttoobtain
09 LS P T r M oce n s e s t i w ng o , r t k he an s d ta c te o s n i c n at q e u n e a u ti e n s g Q th 1 e a m nd to Q o 2 bt b a y ins , t L 2 environmental states stored in Q 2 , and L 1 environmental
10 act I i n o p n u p ti r n o g ba s b , t i i l n it t y o d th is e tr a i c b t u o t r io n n et π w ( o a r t k |s t t o ) obtainthe a st c a c t o e r s d s in to g re to d t i h n ei Q r 1 te . m T p h o e r s a e ls s e ta q t u e e s n a c r e e ( s li t n o e re s d 3- i 7 n ). tw Li o ne q s u 8 e - u 2 e 1 s
11 Inputingstintotheactornetworktoobtainthe
statevalue V(st ) representthetrainingprocessofthealgorithm.Thestatesin
12 Samplingtoobtainactionataccordingtoaction thetwoqueuesarefirstpreprocessedbytheLSTMnetwork,
probabilitydistributionπ(at|st )andexecutingitin
whichareconcatenatedtoobtainthetemporalsequencestate
theenvironment ,
13 Environmentfeedbackrewardrtand s t of the past L 1 and L 2 environmental states. The state
newenvironmentalstateobst is then used as input to the actor and critic networks to
14 RemovingthefirstelementsinqueuesQ1and obtain the action probability distribution π(a |s ) and the
15 Q2 P , ro a c n e d ss i i n n s g er t t h i e ng st o a b te s s t i i n nt q o u Q eu 1 es an Q d 1 Q a 2 ndQ2by , statevalueV (s t ).Theactionisthensampledfro t m t theaction
LSTMnetwo , rkandconcatenatingthemtoobtains t+1 probabilitydistributionandexecutedintheenvironment.The
16 sta I t n e p v u a t l i u n e gs V t+ (cid:0)1 st+ in 1 to (cid:1) thecriticnetworktoobtainthe environmental state changes after implementing the action,
17 CalculatingtheTDerrorδ t (st )=rt+γV(cid:0)st+1 (cid:1)−V(st ) returning to the environmental state obs t and the reward r t
18 θ c←θ c+δ t (st;θ c )∇θc (st;θ c ) at time step t. The new environmental state is inserted into
19 θ a←θ a+δ t (st;θ c )∇θa logπ(at|st;θ a )+β∇θa H(π(at|st;θ a )) queues Q and Q , and the first elements in the queues
20 t←t+1 1 2
21 endfor (the environmental state farthest from step t) are removed.
Thestatesinthetwoqueuesareconcatenatedandprocessed
,
According to the formula, the reward function is divided throughtheLSTMnetworktoobtainthetemporalstates ,
t+1
into four segments. When the SSR of all slices meets the andV (s t+1 )iscalculatedthroughthecriticnetwork.Using
setthresholdandSEisgreaterthanorequalto280,positive theformulaforTDerror,δ (s )canbecalculated,andparam-
t t
feedback rewards greater than 4 will be given based on the eters θ and θ of actor and critic networks can be updated
a c
degree of SE optimization. When SE is less than 280 but according to the TD error. Finally, it moves on to the next
VOLUME11,2023 95043

X.Changetal.:TowardanEfficientandDynamicAllocationofRANSlicingResourcesfor5GEra
TABLE1. Trainingparameters. TABLE2. Parametersofsimulationenvironment.
roundoftraininguntilthemaximumnumberofiterationsis
reached.
| Table 1       | lists the | parameters | trained      | by Algo.  | 1, with    | a   |     |     |     |
| ------------- | --------- | ---------- | ------------ | --------- | ---------- | --- | --- | --- | --- |
| small entropy | weight    | set        | to encourage | the agent | to explore |     |     |     |     |
theactionspace.Alargerlearningrateforthecriticnetwork
| is used to | learn the | value | function, which | guides | actor opti- |     |     |     |     |
| ---------- | --------- | ----- | --------------- | ------ | ----------- | --- | --- | --- | --- |
mizationthroughadvantagecalculation.Thealgorithmisset
todefaultto10,000trainingiterations.Thenumberofinput
featuresforthenetworkis3,representingthenumberofser-
vicepacketsover3slices.Theactionspacesizeis[1128,3],
with1128beingthemaximumassignablebandwidthdivided
| by the minimum | bandwidth |     | allocation | unit, | which makes |     |     |     |     |
| -------------- | --------- | --- | ---------- | ----- | ----------- | --- | --- | --- | --- |
the decision for the number of allocated bandwidths of the driving. The available total bandwidth of the network is
threeslices.TheinputstateisfirstpreprocessedbyanLSTM 10MHz, and the minimum allocation unit is 200kHz. The
networkofsize64,thenpassedthroughtwofullyconnected resourceallocationalgorithmfornetworkslicingmakesdeci-
layers in both the actor and the critic networks. The actor sions(adjustments)every1,000ms.Thetotalnumberofusers
networkfinallyobtainstheprobabilitydistributionofactions is1,200,whomoveindifferentsettings.Theenvironmentsize
throughasoftmax function.Twoqueuesofdifferentlengths is240m*240m.Itisassumedthatusersofthesametypehave
|     |     |     |     |     |     | the same moving | direction | and speed, and change | direction |
| --- | --- | --- | --- | --- | --- | --------------- | --------- | --------------------- | --------- |
areusedtostoreenvironmentstatesforLSTMpreprocessing,
includingthelast10and100rounds.Ifthenumberofslices by reflection when encountering the system boundary. The
andtotalbandwidthsetbytheenvironmentchange,thecor- user mobility patterns in the table are set as default. In the
responding parameters should be adjusted accordingly. The experiment,thenumberofuserdevicescanbeincreased,and
simulation experiment uses the parameter training model in theusermovementspeedcanbesettofluctuatewithcertain
Table1bydefault. distributions. The size distribution of data packets and SLA
aresetaccordingto3GPPTR36.814[34]andTS22.261[35].
Thewirelessbasestationcoversaradiusof40m.Thesystem
VI. SIMULATIONANDPERFORMANCEANALYSIS
A. SIMULATIONCNVIRONMENTSETTINGS aims to maximize the utility function of the base station.
Table2showstheconfigurationparametersofthesimulation
ThissectionmainlyfocusesonresourceallocationforRAN
environment.
| network slicing. | In            | the simulation |       | experiment, | this paper |     |     |     |     |
| ---------------- | ------------- | -------------- | ----- | ----------- | ---------- | --- | --- | --- | --- |
| considers        | three typical | service        | types | in wireless | networks:  |     |     |     |     |
VoLTE, which provides wireless network call services; B. EXPERIMENTALRESULTSANDPERFORMANCE
| eMBB, which | provides | high | bandwidth | network | services, | ANALYSIS |     |     |     |
| ----------- | -------- | ---- | --------- | ------- | --------- | -------- | --- | --- | --- |
such as mobile entertainment and augmented reality; and The weight α of the objective function is set to 0.01 by
β
URLLCS, which provides low latency and high-reliability default, and the SSR weight vector for each type of slic-
network services, such as remote control and autonomous ing service is set to [1,1,1] to indicate equal importance.
|     |     |    | 4+(SE −280)∗0.1, |     | ≥0.98and | ≥0.98and | ≥0.95and | ≥280 |     |
| --- | --- | --- | ---------------- | --- | -------- | -------- | -------- | ---- | --- |
|     |     |     |                  |     | q v      | q e      | q u      | SE   |     |
4,
|       |     |       |              |     | ≥0.98and  | ≥0.98and             | ≥0.95and | <280 |               |
| ----- | --- | ----- | ------------ | --- | --------- | -------------------- | -------- | ---- | ------------- |
|       |     |       |              |     | q v       | q e                  | q u      | SE   |               |
|       |     | r =   |              |     |           |                      |          |      | (15)          |
|       |     |       | (q −0.7)∗10, |     | q ≥ 0 . 9 | 8 a n d q ≥ 0 .98and | q <0.95  |      |               |
|       |     | − | u            |     | v         | e                    | u        |      |               |
|       |     |       | 5 ,          |     | q < 0 . 9 | 8 o r q < 0.9 8      |          |      |               |
|       |     |       |              |     | v         | e                    |          |      |               |
| 95044 |     |       |              |     |           |                      |          |      | VOLUME11,2023 |

X.Changetal.:TowardanEfficientandDynamicAllocationofRANSlicingResourcesfor5GEra
As there is a gap between the magnitudes of SE (usually
above200bps/Hz)andSSR,α issetsmalltoscaleSEtothe
same level as SSR. Otherwise, the agent would essentially
optimizeonlyforSE,astheimpactofSSRontheobjective
function is negligible. In the comparative experiments, the
followingalgorithmsareusedforperformancecomparison:
1) EVEN: Distributing total bandwidth evenly to each
slice;
2) DQN[25]:abandwidthallocationpolicygeneratedby
trainingamodelusingtheDQNreinforcementlearning
algorithmfor10,000rounds;
3) A2C [7]: A bandwidth allocation policy generated by FIGURE4. Comparisonofalgorithmrewards.
trainingamodelusingtheA2Creinforcementlearning
algorithmfor10,000rounds;
4) A2C with LSTM (the algorithm designed in this
section): A A2C reinforcement learning method that
uses two queues to store environmental states, pro-
cessesthemthroughLSTMnetworksandconcatenates
thestatefeatures.
BasedonthesimulationenvironmentsettingsinSectionVI
andthetrainingprocessofAlgo.1,Fig.4showsacomparison
oftherewardfeedbackobtainedbydifferentalgorithmsafter
10,000 rounds of training. Overall, reinforcement learning
algorithmscanachievehigherrewardfeedbackthroughsuf-
FIGURE5. Comparisonofsystemutilityperformance.
ficienttraining.Inthelatterhalfofthetrainingprocesswhen
the algorithm model tends to converge, the A2C algorithm
with LSTM achieves the highest average reward, followed explorationintheactionspace.TheEVENallocationpolicy
by the A2C algorithm and DQN. According to the reward maintainsthesamebandwidthresourcesforeachslice,rather
trendofeachalgorithminthefigure,thealgorithmthatpre- than dynamically allocating bandwidth resources according
processesthestatebypassingtwolong-andshort-termstate totheirchangingservicerequirements,whichexplainsitslow
queuesthroughanLSTMnetworkcanachievehigherrewards rewardvaluesandasmallfluctuationrange.
duringtrainingthantheA2Calgorithm.After6,000roundsof Fig.5showsthesystemutilityachievedbydifferentalgo-
training,theA2CalgorithmwithLSTMcanachievereward rithmsduringatrainingperiodof10,000rounds.Thesystem
values of 8-10, while the A2C algorithm can only achieve utilityfunctionisdefinedinSectionIV,andtheoptimization
reward values lower than around 8. As this implies, the objectiveofthissectionisthesystemutilityindicator,which
mobilitycharacteristicsofusersdoaffecttheenvironmental consistsofSEandSSRofeachsliceservice.Systemutility
state, and the LSTM network can indeed extract features of can comprehensively reflect the overall performance of an
servicerequeststatestimeseries.Thelargefluctuationrange algorithm. In general, the trend of changes in the system
of the reward obtained by the DQN algorithm is due to its utilityofalgorithmsisthesameastheperformancetrendin
learningprocess,whichinvolvessamplingexperiencesfrom the reward function experiment, indicating that the reward
theexperiencepoolforupdates.Inbandwidthresourceallo- function set in Section V can guide the model to optimize
cation decisions, slight differences in bandwidth allocation thesystemutilityobjective.Asshowninthefigure,theA2C
can lead to significant fluctuations in the SSR of a network algorithm with the LSTM network still achieves the best
slice. These poor bandwidth allocation policies are stored systemutility.TheDQNalgorithmachievesthesecond-best
as experience in the memory pool, affecting the stability of performance in the later stage of training, but the system
policy. Plus, the DQN algorithm has a slow convergence utility value fluctuates greatly and converges slowly. After
rate. The A2C algorithm achieves the fastest convergence rapid trial and error, the A2C algorithm enters the con-
rate, and after 1,000 rounds of training, its reward remains vergence state after 1,000 rounds, but the achieved system
at around 7.8. The convergence rate of the A2C algorithm utilitylagsbehindthatoftheA2CnetworkwithLSTM.The
withLSTMisslowerthanthatoftheA2Calgorithmbecause experimental results show that user mobility has an impact
itsinputincludesfeaturesofpaststatesequences.Although ontheirservicerequirementsandhascertaintemporalchar-
unstable state sequence features delay the convergence rate acteristics. Adding the LSTM network to the processing of
of the algorithm, they help make better bandwidth resource state sequences can effectively help the algorithm improve
allocationdecisionstoobtainhigherrewards.Inaddition,the thesystemutilityinarealandvalidway.
A2C algorithm with LSTM introduces an entropy term in Fig. 6 presents a comparison of SEs for different algo-
the loss function of the actor network to encourage policy rithms. Considering the preciousness of wireless bandwidth
VOLUME11,2023 95045

X.Changetal.:TowardanEfficientandDynamicAllocationofRANSlicingResourcesfor5GEra
FIGURE6. ComparisonofSE.
FIGURE7. ComparisonofSSRsforVoLTEservice.
resources, improving SE can not only provide higher trans-
mission rates for users but also save wireless spectrum
resources. As shown in the figure, the A2C algorithm with
LSTMtendstoconvergeat2,000rounds,whileSEremains
around 330. The DQN algorithm achieves the second-best
performance but has significant fluctuations. In the subse-
quent bandwidth resource allocation diagram of the DQN
algorithm, the reasons for the large range of fluctuations in
the DQN algorithm will be analyzed from the perspective
of allocation policies. According to the calculation formula
of SE, even if the same total bandwidth is allocated to all
slices, due to the impact of user mobility on the signal-to- FIGURE8. ComparisonofSSRsforeMBBService.
noise ratio, although the algorithm’s calculation model for
thesignal-to-noiseratioisunknown,amodelthattakesinto
accounttheimpactofdemandchangesduetousermobility 8,000-10,000 rounds of training, which obviously cannot
isobtainedthroughtrainingandinputtingthestatesequence meet the demand of guaranteeing the multiservice SSR in
into the LSTM network, and the SE performance indicator network slicing. URLLC is the typical request with high
canbeoptimizedaccordingly. requirements for latency and reliability. In the experiment,
Fig. 7 depicts a comparison of SSRs for VoLTE service. the weight vector β for different services is set as [1,1,1],
As shown in the figure, almost all algorithms can meet the but there remain some services that cannot be satisfied.
requirements of this service. The SSR of VoLTE service In subsequent experiments, the weight factor for URLLC
forreinforcementlearningalgorithmshasslightfluctuations, servicecanbeincreasedtocontributemoretosystemutility
with a small amount of packet loss and transmission fail- and ensure that all URLLC service requests are met. In the
ures,butthesecanbealmostignored.TheEVENallocation Evenallocationpolicy,althoughtheURLLCservicesliceis
policy maintains an SSR of 1.0, as one-third of the total allocated one-third of the total bandwidth, it only achieves
bandwidthresourcesaresufficienttomeettherequirements an SSR between 0.7 and 0.8. Obviously, more bandwidth
of VoLTE service. In fact, according to the VoLTE settings resources should be allocated to the URLLC service slice.
in Section VI , VoLTE service has low requirements and its AlthoughURLLCservicerequiresalowertransmissionrate,
SSRcanbemetbyasmallamountofbandwidthallocation. they require extremely high latency, so the packets must be
Subsequentexperimentalresultsshowthatonlytheminimum transmittedquicklytoavoidpacketlossduetoexceedingthe
bandwidthallocationunit(0.2MHz)isrequiredtoensurethe responselatency.
SSRofthisservice. Toinvestigatethereasonsfortheperformancedifferences
Fig. 8 shows the SSRs of different algorithms for eMBB amongthealgorithms,theexperimentwilltrainA2C,DQN,
serviceslicing.Overall,allreinforcementlearningalgorithms and A2C algorithms with LSTM for 20,000 rounds, and
canimprovetheSSRofeMBBserviceslicingaftertraining, analyze their performance differences by observing their
buttheDQNalgorithmfailstoguaranteea0.98SSRthresh- bandwidth allocation policies (i.e., actions in each round).
old even after 10,000 rounds of training. Both the EVEN The simulation environment and training configuration are
allocationpolicyandtwoA2C-basedalgorithmscanensure kept default, and the maximum number of iterations is set
theSSRofthisserviceslicingisabove0.98. to20,000rounds.Fig.10showsthebandwidthallocationof
Fig. 9 shows a comparison of SSRs for URLLC service. theA2Calgorithmduringthe20,000-roundtrainingprocess.
Overall,theA2CalgorithmandA2CalgorithmwithLSTM It can be seen that the bandwidth allocation policy of the
can maintain an SSR of around 0.98 after training, while A2Calgorithmfluctuatesoveralargerangeinthefirst1,000
theDQNalgorithmstillwidelyexhibitsSSRbelow0.9after rounds of training. After 1,000 rounds, the model begins to
95046 VOLUME11,2023

X.Changetal.:TowardanEfficientandDynamicAllocationofRANSlicingResourcesfor5GEra
FIGURE9. ComparisonofSSRsforURLLCservice. FIGURE11. BandwidthallocationofDQNalgorithm.
|     |     |     |     | actions     | based on     | the      | Q-value,        | which         | undermines | the            | sta-    |
| --- | --- | --- | --- | ----------- | ------------ | -------- | --------------- | ------------- | ---------- | -------------- | ------- |
|     |     |     |     | bilization  | of the       | policy   | in a particular |               | direction. | Moreover,      |         |
|     |     |     |     | because     | the learning | of       | the DQN         | algorithm     |            | at each        | step is |
|     |     |     |     | based on    | the batch    | learning |                 | of experience | in         | the memory     |         |
|     |     |     |     | pool, its   | convergence  |          | is slow,        | as it becomes |            | more difficult |         |
|     |     |     |     | to optimize | the          | model    | towards         | a ‘‘better’’  | direction  |                | due to  |
previouspoorfeedbackexperiencesinthebatch.After12,000
|     |     |     |     | rounds | of training, | the | bandwidth | allocation |     | of the | DQN |
| --- | --- | --- | --- | ------ | ------------ | --- | --------- | ---------- | --- | ------ | --- |
algorithmcanbestabilizedwithinasmallrange.Compared
|     |     |     |     | to Fig.   | 12, the DQN | algorithm |       | allocates | about    | 0.2 MHz | of  |
| --- | --- | --- | --- | --------- | ----------- | --------- | ----- | --------- | -------- | ------- | --- |
|     |     |     |     | bandwidth | to the      | network   | slice | of VoLTE  | service, | 4.2     | MHz |
FIGURE10. BandwidthallocationofA2Calgorithm. to the slice of eMBB service, and 5.4 MHz to the slice of
|     |     |     |     | URLLC | service. | However, | there | are | still fluctuations |     | in a |
| --- | --- | --- | --- | ----- | -------- | -------- | ----- | --- | ------------------ | --- | ---- |
converge. VoLTE service maintains a bandwidth allocation certainrange,sotheSEperformanceoftheDQNalgorithm
of 0.4 MHz, eMBB service 3.8MHz, and URLLC service is comparable to that of the A2C algorithm with the LSTM
5.6MHz.AccordingtothecomparisonwithFig.12,theA2C network. Due to the volatility of the bandwidth allocation
algorithm and the A2C algorithm with LSTM stabilize the policy, the SSR of network slicing services cannot be guar-
bandwidth allocation policy at the same level after conver- anteed, as shown in Figs 8 and 9. From above, because
gence.Therefore,theA2Calgorithmcanobtainmorestable of the instability of the DQN algorithm’s decision-making,
system utility than the DQN algorithm after convergence. itcannotensuretheSSRofnetworkslicingservices,result-
As shown in Fig. 6, the A2C algorithm with LSTM obtains ing in the performance gap between the DQN algorithm
higher SE because it allocates 4.2 MHz for the eMBB ser- and the A2C algorithm with LSTM in terms of system
| vice slice, while | A2C allocates | only 3.8 MHz. | The eMBB | utility. |     |     |     |     |     |     |     |
| ----------------- | ------------- | ------------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
service requires a higher transmission rate, which helps to Fig. 12 shows the bandwidth allocation of the A2C
achieveahigherSE.Therefore,allocatingmorebandwidthto algorithm with the LSTM network during 20,000 rounds of
eMBBleadstodifferencesinSEbetweentheA2Calgorithm training. In general, the bandwidth allocation policy of this
withLSTMandtheA2Calgorithm.Furthermore,asshown algorithm tends to be stable after 2,000 rounds of training,
in Fig. 9, allocating more bandwidth for URLLC service consistent with the rewards, system utility, and SE perfor-
does not improve its SSR, as the service’s un-SSR is more mance of the algorithm shown in Figs 4, 5, and 6 after
triggered by the higher packet loss rate caused by its high 2,000roundsoftraining.Thebandwidthresourceallocation
latency requirement. In fact, allocating only 0.2 MHz of for the VoLTE service’s network slice eventually stabilizes
bandwidth to VoLTE service is sufficient to meet its SSR, at 0.2 MHz, because the service’s data packet size is con-
and allocating more bandwidth resources does not improve stant, the user reach interval is uniformly distributed, and
itsSE. the service requires a low transmission rate and insensitive
Fig. 11 shows the bandwidth resource allocation by the latency (as shown in Section VI simulation environment
DQN algorithm for three network slicing services during settings). The bandwidth allocation for the eMBB service’s
20,000roundsoftraining.Inthefirst8,000roundsoftrain- network slice eventually stabilizes at 4.2 MHz, because the
ing, the bandwidth allocation policy of the DQN algorithm servicerequiresahighertransmissionrateofdatapacketsand
fluctuatessignificantly,resultinginoscillationsintherewards needs more bandwidth allocation. The URLLC service has
itobtains.Also,thisverifiesthattherewards,systemutility, largerdatapacketsandmoreusersinthesimulationsettings
and SE achieved by the DQN algorithm in Figs 4, 5, and 6 and requires high latency. Therefore, in the experimental
allfluctuateinawiderange.Thisisbecauseasavalue-based configuration, the algorithm allocates the most bandwidth
reinforcement learning algorithm, DQN judges the value of resources,whichis5.4MHz,tothenetworksliceofURLLC
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     | 95047 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

X.Changetal.:TowardanEfficientandDynamicAllocationofRANSlicingResourcesfor5GEra
|     |     |     |     |     |     |     |     | solution | in this | section | can effectively |     | solve | the defined |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------- | --------------- | --- | ----- | ----------- |
problem.
|     |     |     |     |     |     |     |     | VII. CONCLUSIONANDFUTUREWORK |           |                |         |                |         |            |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --------- | -------------- | ------- | -------------- | ------- | ---------- |
|     |     |     |     |     |     |     |     | Existing                     | research  | on wireless    |         | network        | slicing | has insuf- |
|     |     |     |     |     |     |     |     | ficiently                    | accounted | for            | the     | impact of      | users’  | mobility   |
|     |     |     |     |     |     |     |     | characteristics              |           | on their       | service | requirements.  |         | This lack  |
|     |     |     |     |     |     |     |     | of consideration             |           | in dynamically |         | allocating     | network | slice      |
|     |     |     |     |     |     |     |     | resources                    | to        | mobile users   | results | in unfulfilled |         | service    |
demands.InthescenarioofMEC,thispapersystematically
examinesthebandwidthallocationpolicyforRANnetwork
| FIGURE12. | BandwidthallocationofA2CalgorithmwithLSTMnetwork. |     |     |     |     |     |     |          |           |           |         |          |         |             |
| --------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --------- | --------- | ------- | -------- | ------- | ----------- |
|           |                                                   |     |     |     |     |     |     | slicing, | realizing | wireless  | network | service  | and     | a guarantee |
|           |                                                   |     |     |     |     |     |     | for user | network   | services. | Based   | on three | typical | service     |
service. It can be seen that in the simulation environment types, the study dynamically allocates wireless bandwidth
settings, the total bandwidth resource of the wireless base resources to slices to meet different service requirements
station is 10 MHz, while the total allocated resources for and improve the SE of wireless bandwidth. Besides, user
| the three | slices is | 9.8 MHz. | This | is  | because | the bandwidth |     |     |     |     |     |     |     |     |
| --------- | --------- | -------- | ---- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
mobilityistakenintoconsiderationforbandwidthallocation
allocated to them can already meet their service quality decision-making,soastosupportchangesinnetworkslicing
requirements. According to the SE formula, the larger the servicerequirementsintheMECscenario.Asolutionbased
| allocated | bandwidth, | the | larger | the denominator |     | of  | the for- |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ------ | --------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
onreinforcementlearningandotheradvancedneuralnetwork
mula and the lower the SE, as long as the service rate modules is adopted to achieve specific feature extraction,
| requirement | is met. | Therefore, |     | the algorithm |     | will not | allo- |           |             |          |     |                  |     |           |
| ----------- | ------- | ---------- | --- | ------------- | --- | -------- | ----- | --------- | ----------- | -------- | --- | ---------------- | --- | --------- |
|             |         |            |     |               |     |          |       | which can | effectively | allocate |     | limited wireless |     | bandwidth |
cateanextra0.2MHzbandwidthtootherslicestoimprove resources and improve wireless SE while ensuring slice
| the SE,           | i.e. the utilization |             | of wireless |          | bandwidth | resources. |        | serviceSE. |        |        |        |           |           |         |
| ----------------- | -------------------- | ----------- | ----------- | -------- | --------- | ---------- | ------ | ---------- | ------ | ------ | ------ | --------- | --------- | ------- |
| In the simulation |                      | environment |             | settings | and       | system     | model, |            |        |        |        |           |           |         |
|                   |                      |             |             |          |           |            |        | As the     | system | models | in the | study are | all based | on real |
whenusersmove,theirpositionschange,resultinginchanges scenarios, they have great practical significance. The opti-
| in the data | demands | of  | each | slice service. |     | However, | after |          |           |            |     |             |            |      |
| ----------- | ------- | --- | ---- | -------------- | --- | -------- | ----- | -------- | --------- | ---------- | --- | ----------- | ---------- | ---- |
|             |         |     |      |                |     |          |       | mization | of system | objectives |     | is expected | to improve | user |
2,000 rounds of training, the algorithm maintains the same experience.Theresultsofsimulationexperimentsverifythe
bandwidth allocation policy. The reasons for this include: effectivenessofthesolution.Therefore,whileapplyingitto
| first, after | 2,000 | rounds | of training, |     | the algorithm |     | learns a |     |     |     |     |     |     |     |
| ------------ | ----- | ------ | ------------ | --- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
real-worldsystemsrequiresaddressingpracticalengineering
policythatcanlargelyobtainbetterrewardfeedback,which challenges such as data collection, algorithm implementa-
| means the | algorithm | has | learned | how | the changes |     | in users |           |             |             |     |            |          |     |
| --------- | --------- | --- | ------- | --- | ----------- | --- | -------- | --------- | ----------- | ----------- | --- | ---------- | -------- | --- |
|           |           |     |         |     |             |     |          | tion, and | performance | evaluation, |     | the method | proposed | in  |
affect the changes in service demands in the environment. this paper has demonstrated practical applicability in both
Moreover,thisisconsideredthateveniftheusersmoveand theoretical optimization of wireless network slice resource
causechangesinservicedemands,maintainingthisallocation
allocationandexperimentalsimulations.
schemecanensuretheSSRofeachsliceserviceandobtain Regarding network slicing in MEC, future research may
a higher SE. In fact, according to the SSR threshold set adoptthefollowingperspectives:first,introducingothertech-
in the reward function, it is only necessary to ensure that nologies (e.g., blockchain-based technologies) to enhance
,q ,andq
q are higher than 0.98, 0.98, and 0.95, respec- network resource security; second, incorporating network
| v e | u   |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tively.Second,duringenvironmentalchanges,twoqueuesare
|     |     |     |     |     |     |     |     | resource | allocation | for | different | users within |     | the slice to |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --------- | ------------ | --- | ------------ |
usedtostorethestatesequenceandpreprocessthemwithan achieveintra-sliceutilityoptimization.
| LSTM network | to  | obtain | temporal | features. |     | When | the past |     |     |     |     |     |     |     |
| ------------ | --- | ------ | -------- | --------- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
policybecomesstable,theenvironmentalstatesequencealso
REFERENCES
tendstobestableunderthatpolicy,makingiteasiertomake
|     |     |     |     |     |     |     |     | [1] S.Ahmadi,5GNR:Architecture,Technology,Implementation,andOper- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
thesamedecisionsincaseofasimilarlengthofthepaststate
ationof3GPPNewRadioStandards.NewYork,NY,USA:Academic,
| sequence. |     |     |     |     |     |     |     | 2019. |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
Through comparison of the experimental results, it can [2] A. Banchs, G. de Veciana, V. Sciancalepore, and X.Costa-Perez,
be concluded that the proposed solution in this section ‘‘Resource allocation for network slicing in mobile net-
|     |     |     |     |     |     |     |     | works,’’ | IEEE | Access, | vol. 8, | pp.214696–214706, |     | 2020, doi: |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------- | ------- | ----------------- | --- | ---------- |
can support various types of services with different needs 10.1109/ACCESS.2020.3040949.
in network slicing and guarantee their SSR. Meanwhile, [3] V. Mnih, K. Kavukcuoglu, D. Silver, A. Graves, I. Antonoglou,
D.Wierstra,andM.Riedmiller,‘‘PlayingAtariwithdeepreinforcement
| to address | the changing |     | service | demand | caused |     | by user |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------- | ------ | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
learning,’’2013,arXiv:1312.5602.
| mobility | in the   | MEC   | scenario,   | the | solution | adopts   | an  |                                                                |     |     |     |     |     |     |
| -------- | -------- | ----- | ----------- | --- | -------- | -------- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|          |          |       |             |     |          |          |     | [4] Z.Wang,T.Schaul,M.Hessel,H.Hasselt,M.Lanctot,andN.Freitas, |     |     |     |     |     |     |
| LSTM     | network, | which | can extract |     | temporal | features | to  |                                                                |     |     |     |     |     |     |
‘‘Duelingnetworkarchitecturesfordeepreinforcementlearning,’’inProc.
Int.Conf.Mach.Learn.,2016,pp.1995–2003.
| help the | A2C algorithm |          | achieve | better | performance. |            | Plus, |                                                                     |     |     |     |     |     |     |
| -------- | ------------- | -------- | ------- | ------ | ------------ | ---------- | ----- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|          |               |          |         |        |              |            |       | [5] H.VanHasselt,A.Guez,andD.Silver,‘‘Deepreinforcementlearningwith |     |     |     |     |     |     |
| the SE   | of the        | wireless | network | can    | be           | maintained | at    |                                                                     |     |     |     |     |     |     |
doubleQ-learning,’’inProc.AAAIConf.Artif.Intell.,2016,vol.30,no.1,
| a relatively | high | level. | All | of these | indicate | that | the | pp.1–7. |     |     |     |     |               |     |
| ------------ | ---- | ------ | --- | -------- | -------- | ---- | --- | ------- | --- | --- | --- | --- | ------------- | --- |
| 95048        |      |        |     |          |          |      |     |         |     |     |     |     | VOLUME11,2023 |     |

X.Changetal.:TowardanEfficientandDynamicAllocationofRANSlicingResourcesfor5GEra
[6] R.Y.Li,H.M.Peng,R.G.Li,andK.Zhao,‘‘Overviewonalgorithms [27] Y.Hua,R.Li,Z.Zhao,X.Chen,andH.Zhang,‘‘GAN-powereddeep
andapplicationsforreinforcementlearning,’’Comput.Syst.Appl.,vol.29, distributional reinforcement learning for resource management in net-
no.12,pp.13–25,2020. workslicing,’’IEEEJ.Sel.AreasCommun.,vol.38,no.2,pp.334–349,
| [7] V.Mnih,A.P.Badia,M.Mirza,A.Graves,T.Lillicrap,T.Harley,D.Silver, |     |     |     |     |     |     |     | Feb.2020. |     |     |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
and K. Kavukcuoglu, ‘‘Asynchronous methods for deep reinforcement [28] Y. Abiko, T. Saito, D. Ikeda, K. Ohta, T. Mizuno, and H. Mineno,
|     |     |     |     |     |     |     |     | ‘‘Flexible | resource | block allocation | to multiple | slices | for | radio access |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---------------- | ----------- | ------ | --- | ------------ |
learning,’’inProc.Int.Conf.Mach.Learn.,2016,pp.1928–1937.
networkslicingusingdeepreinforcementlearning,’’IEEEAccess,vol.8,
[8] T.P.Lillicrap,J.J.Hunt,A.Pritzel,N.Heess,T.Erez,Y.Tassa,D.Silver,
andD.Wierstra,‘‘Continuouscontrolwithdeepreinforcementlearning,’’ pp.68183–68198,2020.
2015,arXiv:1509.02971. [29] Y.KimandH.Lim,‘‘Multi-agentreinforcementlearning-basedresource
[9] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov,‘‘Proxi- management for end-to-end network slicing,’’ IEEE Access, vol. 9,
pp.56178–56190,2021.
malpolicyoptimizationalgorithms,’’2017,arXiv:1707.06347.
|     |     |     |     |     |     |     |     | [30] Y.Cui,X.Huang,P.He,D.Wu,andR.Wang,‘‘QoSguaranteednetwork |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
[10] T.Haarnoja,A.Zhou,P.Abbeel,andS.Levine,‘‘Softactor-critic:Off-
slicingorchestrationforInternetofVehicles,’’IEEEInternetThingsJ.,
policymaximumentropydeepreinforcementlearningwithastochastic
vol.9,no.16,pp.15215–15227,Aug.2022.
actor,’’inProc.Int.Conf.Mach.Learn.,2018,pp.1861–1870.
|     |     |     |     |     |     |     |     | [31] R. Li, | C. Wang, | Z. Zhao, R. | Guo, and | H. Zhang, | ‘‘The | LSTM-based |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ----------- | -------- | --------- | ----- | ---------- |
[11] J. Khamse-Ashari, G. Senarath, I. Bor-Yaliniz, and H. Yanikomeroglu, advantageactor-criticlearningforresourcemanagementinnetworkslicing
‘‘Anagileanddistributedmechanismforinter-domainnetworkslicingin
withusermobility,’’IEEECommun.Lett.,vol.24,no.9,pp.2005–2009,
nextgenerationmobilenetworks,’’IEEETrans.MobileComput.,vol.21,
Sep.2020.
no.10,pp.3486–3501,Oct.2022.
|     |     |     |     |     |     |     |     | [32] Q.Liu,T.Han,N.Zhang,andY.Wang,‘‘DeepSlicing:Deepreinforcement |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
[12] A.Lieto,I.Malanchini,S.Mandelli,E.Moro,andA.Capone,‘‘Strate-
learningassistedresourceallocationfornetworkslicing,’’inProc.IEEE
gicnetworkslicingmanagementinradioaccessnetworks,’’IEEETrans. GlobalCommun.Conf.(GLOBECOM),Dec.2020,pp.1–6.
MobileComput.,vol.21,no.4,pp.1434–1448,Apr.2022. [33] S.HochreiterandJ.Schmidhuber,‘‘Longshort-termmemory,’’Neural
[13] A.Thantharate,R.Paropkari,V.Walunj,andC.Beard,‘‘DeepSlice:A Comput.,vol.9,no.8,pp.1735–1780,Nov.1997.
deeplearningapproachtowardsanefficientandreliablenetworkslicingin
|     |     |     |     |     |     |     |     | [34] EvolvedUniversalTerrestrialRadioAccess(E-UTRA);FurtherAdvance- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
5Gnetworks,’’inProc.IEEE10thAnnu.UbiquitousComput.,Electron.
mentsforE-UTRAPhysicalLayerAspect,documentTR36.814,3GPP,
MobileCommun.Conf.(UEMCON),Oct.2019,pp.762–767.
2015.
[14] L.Zanzi,A.Albanese,V.Sciancalepore,andX.Costa-Pérez,‘‘NSBchain: [35] Service Requirements for the 5G System, document TS 22.261, 3GPP,
| Asecureblockchainframeworkfornetworkslicingbrokerage,’’inProc. |     |     |     |     |     |     |     | 2017. |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
IEEEInt.Conf.Commun.(ICC),Jun.2020,pp.1–7.
| [15] M. A. | Togou, | T. Bi, K. | Dev, K. | McDonnell, | A. Milenovic, |     | H. Tewari, |     |     |     |     |     |     |     |
| ---------- | ------ | --------- | ------- | ---------- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
andG.-M.Muntean,‘‘DBNS:Adistributedblockchain-enablednetwork
slicingframeworkfor5Gnetworks,’’IEEECommun.Mag.,vol.58,no.11,
pp.90–96,Nov.2020.
| [16] I. H. | Abdulqadder | and        | S. Zhou, | ‘‘SliceBlock: | Context-aware |                | authenti- |     |     |     |     |     |     |     |
| ---------- | ----------- | ---------- | -------- | ------------- | ------------- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| cation     | handover    | and secure | network  | slicing       | using         | DAG-blockchain | in        |     |     |     |     |     |     |     |
edge-assistedSDN/NFV-6Genvironment,’’IEEEInternetThingsJ.,vol.9, XIAOLEI CHANG was born in China, in 1975.
no.18,pp.18079–18097,Sep.2022. He received the bachelor’s degree in computer
[17] Y.Azimi,S.Yousefi,H.Kalbkhani,andT.Kunz,‘‘Applicationsofmachine science and technology, the master’s degree in
learning in resource management for RAN-slicing in 5G and beyond management science and engineering, and the
networks:Asurvey,’’IEEEAccess,vol.10,pp.106581–106612,2022. Ph.D.degreeinengineering(electronicinforma-
[18] M.Setayesh,S.Bahrami,andV.W.S.Wong,‘‘ResourceslicingforeMBB tion)fromTsinghuaUniversity,in1999and2001,
respectively.
| and | URLLC | services | in radio | access network | using | hierarchical | deep |     |     |     |     |     |     |     |
| --- | ----- | -------- | -------- | -------------- | ----- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
learning,’’IEEETrans.WirelessCommun.,vol.21,no.11,pp.8950–8966, HeiscurrentlyaSeniorEngineerwiththeInfor-
| Nov.2022. |     |     |     |     |     |     |     |     |     | mation Technology |     | Center/Network |     | Research |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------------- | --- | -------- |
[19] Z. Wang, Y. Wei, F. R. Yu, and Z. Han, ‘‘Utility optimization for Institute, Tsinghua University. He is also the
resourceallocationinmulti-accessedgenetworkslicing:Atwin-actordeep DeputyDirectoroftheNextGenerationInternetResearchandDevelopment
deterministicpolicygradientapproach,’’IEEETrans.WirelessCommun., Center,ResearchInstituteofTsinghuaUniversityinShenzhen.Hehasbeen
vol.21,no.8,pp.5842–5856,Aug.2022. engaged in information technology application research and engineering
[20] K.Boutiba,M.Bagaa,andA.Ksentini,‘‘Radioresourcemanagementin practice,transformationofscientificandtechnologicalachievements,and
multi-numerology5Gnewradiofeaturingnetworkslicing,’’inProc.IEEE
technologyenterpriseincubationforalongtime.Hehascompletedmore
Int.Conf.Commun.(ICC),May2022,pp.359–364.
than20researchprojects.Hehaspublishedmorethan20papersandtwo
| [21] K. Boutiba, | A.  | Ksentini, | B. Brik, | Y. Challal, | and | A. Balla, | ‘‘NRflex: |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | -------- | ----------- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
books.Hisresearchinterestsincludegreendatacenter,cloudcomputingand
Enforcingnetworkslicingin5Gnewradio,’’Comput.Commun.,vol.181, edgecomputing,andcyberspacesecurity.
pp.284–292,Jan.2022.
[22] T.Mai,H.Yao,N.Zhang,W.He,D.Guo,andM.Guizani,‘‘Transfer
reinforcementlearningaideddistributednetworkslicingoptimizationin
industrialIoT,’’IEEETrans.Ind.Informat.,vol.18,no.6,pp.4308–4316,
Jun.2022.
| [23] S. Messaoud, |     | A. Bradai, | O. B.     | Ahmed,           | P. T. A. Quang, | M.      | Atri, and   |     |     |     |     |     |     |     |
| ----------------- | --- | ---------- | --------- | ---------------- | --------------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| M.S.Hossain,      |     | ‘‘Deep     | federated | Q-learning-based |                 | network | slicing for |     |     |     |     |     |     |     |
TIANJIwasborninJingdezhen,China,in1989.
industrialIoT,’’IEEETrans.Ind.Informat.,vol.17,no.8,pp.5572–5582,
|     |     |     |     |     |     |     |     |     |     | He received | the M.S. | degree | in big | data from |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ------ | ------ | --------- |
Aug.2021.
|             |          |           |          |     |          |          |            |     |     | Tsinghua | University, | in 2023. | He is | currently a |
| ----------- | -------- | --------- | -------- | --- | -------- | -------- | ---------- | --- | --- | -------- | ----------- | -------- | ----- | ----------- |
| [24] Y. Xu, | Z. Zhao, | P. Cheng, | Z. Chen, | M.  | Ding, B. | Vucetic, | and Y. Li, |     |     |          |             |          |       |             |
‘‘Constrained reinforcement learning for resource allocation in net- corememberoftheFutureInternetResearchCen-
work slicing,’’ IEEE Commun. Lett., vol. 25, no. 5, pp.1554–1558, ter,ResearchInstituteofTsinghuaUniversityin
Shenzhen.Hisresearchinterestsincludetheappli-
May2021.
|               |         |               |           |          |              |            |     |     |     | cation of  | big data,      | cloud     | computing,  | and edge     |
| ------------- | ------- | ------------- | --------- | -------- | ------------ | ---------- | --- | --- | --- | ---------- | -------------- | --------- | ----------- | ------------ |
| [25] R. Li,Z. | Zhao,Q. | Sun,I.        | Chih-Lin, | C.Yang,  | X.Chen,      | M.Zhao,    | and |     |     |            |                |           |             |              |
|               |         |               |           |          |              |            |     |     |     | computing  | technologies   | in        | areas, such | as smart     |
| H.Zhang,      | ‘‘Deep  | reinforcement |           | learning | for resource | management | in  |     |     |            |                |           |             |              |
|               |         |               |           |          |              |            |     |     |     | cities and | the industrial | internet. | He          | has partici- |
networkslicing,’’IEEEAccess,vol.6,pp.74429–74441,2018.
patedindigitaltransformationprojectsformulti-
[26] Y.Shao,R.Li,B.Hu,Y.Wu,Z.Zhao,andH.Zhang,‘‘Graphattention
network-based multi-agent reinforcement learning for slicing resource plelocalgovernmentsandleadingstate-ownedenterprises,coveringvarious
management in dense cellular network,’’ IEEE Trans. Veh. Technol., aspects,includingbutnotlimitedtodatamanagementandanalysis,system
vol.70,no.10,pp.10792–10803,Oct.2021. integration,networkarchitecture,andapplicationdevelopment.
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     |     | 95049 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

X.Changetal.:TowardanEfficientandDynamicAllocationofRANSlicingResourcesfor5GEra
RUNSU ZHU was born in Guangdong, China, CHENXILIwasborninChenzhou,Hunan,China,
in1981.HereceivedtheGraduatedegreewitha in 1999. She received the bachelor’s degree in
major in computer science and technology from materialsscienceandengineeringfromtheChina
SunYat-senUniversity,in2003,andthemaster’s University of Mining and Technology, in 2020.
degreefromXiamenUniversity,in2010. Since 2021, she has been a Research Assis-
HehasbeenwithShenzhen’sCivilServiceSys- tant with the Next Generation Internet Research
tem, since May 2004. He is currently the Party and Development Center, Research Institute of
SecretaryandtheDirectorofShenzhenLonghua Tsinghua University in Shenzhen. Her research
DistrictGovernmentServiceDataAdministration. interestsincludethedevelopmentandapplication
Hehaspublishedtwomonographs,threepapers, of5G,edgecomputing,andothernewgeneration
undertookeightprojects,andparticipatedintheformulationofonenational informationtechnologies.
standard.Hehasaprofessionaltitleofseniorengineer.Hisresearchinterest
| includes electronic | information     | field. He can | make innovative | scientific    |     |     |     |
| ------------------- | --------------- | ------------- | --------------- | ------------- | --- | --- | --- |
| research results    | and effectively | promote the   | transformation  | of scientific |     |     |     |
researchresultsintheindustry.
ZHENZHOUWUreceivedthebachelor’sdegree
|     | in  | software engineering | from Jilin | University, |     |     |     |
| --- | --- | -------------------- | ---------- | ----------- | --- | --- | --- |
in2009.From2009to2011,hewasaSearchEngi-
neerwithAvePoint,responsibleforthecompany’s YONG JIANG received the M.S. and Ph.D.
|     | full-text | search department.From | 2011 | to 2014, |     |     |     |
| --- | --------- | ---------------------- | ---- | -------- | --- | --- | --- |
degreesincomputersciencefromTsinghuaUni-
|     | he  | was the Background | Architect | with Fenglin |                     |           |                |
| --- | --- | ------------------ | --------- | ------------ | ------------------- | --------- | -------------- |
|     |     |                    |           |              | versity, Guangdong, | China, in | 1998 and 2002, |
Volcano Technology Company Ltd., supporting respectively. Since 2002, he has been with
thegameplatformwithtensofmillionsofusers the Tsinghua Shenzhen International Graduate
and millions of users online at the same time. School, Tsinghua University, where he is cur-
From 2014 to 2017, he was the Research and rently a Full Professor. His research interests
DevelopmentDirectorofOudmonTechnologyCompanyLtd.,todevelopthe includecomputervision,machinelearning,inter-
IoTplatform,whichhasaccesstomorethan50millionwearabledevices. netarchitectureanditsprotocols,andIProuting
Heiscurrentlyaseniorarchitect,alispprogrammer,andtheresearchand technology. His research has published in mul-
developmentdirectorofseveralinternetcompanies.Since2017,hehasbeen tiple top-tier journals and conferences, including IEEE TRANSACTIONSON
the Research and Development Director of the Next Generation Internet COMPUTERS, IEEE TRANSACTIONS ON MULTIMEDIA, IEEE TRANSACTIONS ON
ResearchandDevelopmentCenter,ResearchInstituteofTsinghuaUniver- SIGNALPROCESSING,CVPR,andICLR.Hehasreceivedseveralbestpaper
| sity in Shenzhen. | His research | interests include | cloud native, | distributed |     |     |     |
| ----------------- | ------------ | ----------------- | ------------- | ----------- | --- | --- | --- |
awards(e.g.,IWQoS2018)fromtop-tierconferences.
networks,anddistributedcomputing.
| 95050 |     |     |     |     |     |     | VOLUME11,2023 |
| ----- | --- | --- | --- | --- | --- | --- | ------------- |