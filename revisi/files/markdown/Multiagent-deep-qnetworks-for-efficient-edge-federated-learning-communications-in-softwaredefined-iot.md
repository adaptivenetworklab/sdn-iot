# Multiagent-deep-qnetworks-for-efficient-edge-federated-learning-communications-in-softwaredefined-iot

> Source file: `Multiagent-deep-qnetworks-for-efficient-edge-federated-learning-communications-in-softwaredefined-iot.pdf`

---

| Computers,Materials&Continua |     |     |     |     |     |     |     |     |     |     | TechScience | Press |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- |
DOI:10.32604/cmc.2022.023215
Article
Multi-Agent Deep Q-Networks for Efficient Edge Federated Learning
|     |                                | Communications |     |     |     | in Software-Defined |     |                     |     | IoT |     |     |
| --- | ------------------------------ | -------------- | --- | --- | --- | ------------------- | --- | ------------------- | --- | --- | --- | --- |
|     | ProhimTam1,SaMath1,AhyoungLee2 |                |     |     |     |                     |     | andSeokhoonKim1,3,* |     |     |     |     |
1DepartmentofSoftwareConvergence,SoonchunhyangUniversity,Asan,31538,Korea
2DepartmentofComputerScience,KennesawStateUniversity,Marietta,GA30060,USA
3DepartmentofComputerSoftwareEngineering,SoonchunhyangUniversity,Asan,31538,Korea
*CorrespondingAuthor:SeokhoonKim.Email:seokhoon@sch.ac.kr
Received:31August2021;Accepted:15October2021
|     | Abstract: | Federated  |       | learning | (FL)     | activates | distributed |               | on-device | computa-       |          |     |
| --- | --------- | ---------- | ----- | -------- | -------- | --------- | ----------- | ------------- | --------- | -------------- | -------- | --- |
|     | tion      | techniques | to    | model    | a better | algorithm | performance |               |           | with the       | interac- |     |
|     | tion      | of local   | model | updates  | and      | global    | model       | distributions |           | in aggregation |          |     |
averagingprocesses.However,inlarge-scaleheterogeneousInternetofThings
|     | (IoT) | cellular             | networks, | massive |             | multi-dimensional |                 | model |         | update iterations |         |     |
| --- | ----- | -------------------- | --------- | ------- | ----------- | ----------------- | --------------- | ----- | ------- | ----------------- | ------- | --- |
|     | and   | resource-constrained |           |         | computation |                   | are challenging |       | aspects | to be             | tackled |     |
significantly.Thispaperintroducesthesystemmodelofconvergingsoftware-
|     | defined | networking |     | (SDN) | and | network | functions | virtualization |     | (NFV) | to  |     |
| --- | ------- | ---------- | --- | ----- | --- | ------- | --------- | -------------- | --- | ----- | --- | --- |
enabledevice/resourceabstractionsandprovideNFV-enablededgeFL(eFL)
aggregationserversforadvancingautomationandcontrollability.Multi-agent
deepQ-networks(MADQNs)targettoenforceaself-learningsoftwarization,
|     | optimize   | resource | allocation    |         | policies, | and        | advocate | computation |     | offloading |          |     |
| --- | ---------- | -------- | ------------- | ------- | --------- | ---------- | -------- | ----------- | --- | ---------- | -------- | --- |
|     | decisions. |          | With gathered |         | network   | conditions | and      | resource    |     | states,    | the pro- |     |
|     | posed      | agent    | aims to       | explore | various   | actions    | for      | estimating  |     | expected   | long-    |     |
termrewardsinaparticularstateobservation.Inexplorationphase,optimal
|     | actions  | for    | joint resource |          | allocation | and     | offloading |             | decisions | in           | different |     |
| --- | -------- | ------ | -------------- | -------- | ---------- | ------- | ---------- | ----------- | --------- | ------------ | --------- | --- |
|     | possible | states | are            | obtained | by         | maximum | Q-value    | selections. |           | Action-based |           |     |
virtualnetworkfunctions(VNF)forwardinggraph(VNFFG)isorchestrated
|     | to map | VNFs            | towards | eFL       | aggregation |        | server         | with | sufficient | communica- |      |     |
| --- | ------ | --------------- | ------- | --------- | ----------- | ------ | -------------- | ---- | ---------- | ---------- | ---- | --- |
|     | tion   | and computation |         | resources |             | in NFV | infrastructure |      | (NFVI).    | The        | pro- |     |
posedschemeindicatesdeficientallocationactions,modifiestheVNFbackup
|     | instances, |     | and reallocates |     | the virtual | resource |     | for exploitation |     | phase. | Deep |     |
| --- | ---------- | --- | --------------- | --- | ----------- | -------- | --- | ---------------- | --- | ------ | ---- | --- |
neuralnetwork(DNN)isusedasavaluefunctionapproximator,andepsilon-
greedyalgorithmbalancesexplorationandexploitation.Theschemeprimarily
|     | considers |           | the criticalities |         | of FL      | model | services          | and | congestion |                | states to |     |
| --- | --------- | --------- | ----------------- | ------- | ---------- | ----- | ----------------- | --- | ---------- | -------------- | --------- | --- |
|     | optimize  | long-term |                   | policy. | Simulation |       | results presented |     | the        | outperformance |           |     |
oftheproposedschemeoverreferenceschemesintermsofQualityofService
(QoS)performancemetrics,includingpacketdropratio,packetdropcounts,
packetdeliveryratio,delay,andthroughput.
|     | Keywords: |     | Deep | Q-networks; |     | federated | learning; |     | network | functions |     |     |
| --- | --------- | --- | ---- | ----------- | --- | --------- | --------- | --- | ------- | --------- | --- | --- |
virtualization;qualityofservice;software-definednetworking
This work is licensed under a Creative Commons Attribution 4.0 International License,
which permits unrestricted use, distribution, and reproduction in any medium, provided
theoriginalworkisproperlycited.

3320 CMC,2022,vol.71,no.2
1 Introduction
The fast-growing deployment of Internet of Things (IoT) in cellular networks has exponentially
increased in massive data volumes and heterogeneous service types with the requirement of ultra-
reliablelow-latencycommunication(URLLC).By2025,InternationalDataCorporation(IDC)fore-
caststhatthegrowthofdatageneratedfrom41.6billionIoTdeviceswillreach79.4ZB,whichrequires
big data orchestration and network automation to be intelligent and adequate in future scenarios
[1,2]. To control abundant IoT taxonomies and provide sufficient resources, machine learning and
deeplearningalgorithmshavebeenappliedtodevelopsmartsolutionsinedgeintelligenceforvarious
service purposes by gathering local data for model training and testing [3,4]. Meanwhile, because
IoTdeploymenthasgrownrapidlyinvariousprivacy-sensitivesectorssuchasInternetofHealthcare
Things (IoHT), Internet of Vehicles (IoV), and Internet of People (IoP), the uses of local raw data
have to be user-consented and legally authorized before being transmitted to the central cloud [5,6].
Withthesechallengingissues,anintelligentprovisioningschemenecessitatesconsideringthesecurity
oflocaldataprivacy,communicationreliability,andadequatecomputationresources.
Federated learning (FL) secures local data privacy, reduces communication costs, and provides
a latency-efficient approach by distributing global model selection and primary hyperparameters,
denotedasW0,fromcentralparameterservertolocalkclientsforlocalmodelcomputation[7,8].Int
G
iterations,Wt obtainstheoptimalmodelperformancebyaggregationaveragingofmulti-dimensional
G
local model updates in a single parameter server. However, over numerous iterations, the client
and parameter server communications generate heavy traffic congestions and unreliable processes,
particularlyinpeakhourintervals.EdgeFL(eFL)partitionstheiterationsofroundcommunications
in two preeminent steps: (1) The local models wn on n data batch from selected k participants are
k
aggregated in optimal edge server selection, and (2) Global communications are orchestrated to
transmit between edge servers and a central parameter server in an appropriate interval [9–11]. This
techniquereducescloud-centriccommunicationsandimproveslearningprecision.Therefore,asystem
model for offering edge aggregation servers based on specific service-learning model criticalities is
applicabletoenhanceresource-constrainedIoTenvironments.
Multi-access edge computing (MEC) leverages computation powers and storage capacities of
the central cloud to provide a latency-efficient system, adequate Quality of Service (QoS) perfor-
mance, and additional serving resources in edge networks [12,13]. 5G radio access networks (RAN)
support stable connectivity and adaptability between massive users and MEC entities for driving
big data communication traffics with the deployment of millimeter-Wave (mmWave), multiple-input
and multiple-output (MIMO) antennas, device-to-device (D2D), and radio resource management
(RRM)functions.Moreover,toextendaglobalviewofnetworkenvironmentsandefficientlycontrol
heterogeneous MEC entities, software-defined networking (SDN) has been adopted. An adaptive
transmission architecture in IoT networks is advanced by joint SDN and MEC federation to enable
anintelligentedgeoptimizationforlow-deadlineoptimalpathselection[14].SDNseparatesthedata
plane (DP) and control plane (CP) to enable programmable functions, which adequately control
the policies, flow tables, and actions on domain resources management within RAN, core side,
network functions virtualization (NFV), and MEC [15,16]. The convergence of MEC, SDN, and
NFV enables the networking application programming interfaces (API), sufficient resource pools,
flexibleorchestration,andprogrammabilityforlogicallyenablingresourcesharingvirtualizationinan
adaptiveapproach.Tooptimallyallocatetheresourcesandrecommendtheoffloadingdecisionswithin
NFV infrastructure (NFVI)-MEC, an intelligent agent or deep reinforcement learning approaches
haveacapabilitytoapplyasenablersfornetworkautomation(eNA)inordertointeractwithparticular
IoTdevicestatuses,resourceutilization,andnetworkcongestionstates.

CMC,2022,vol.71,no.2 3321
Deep Q-network (DQN) has notably been used for addressing resource allocation and com-
putation offloading problems in massive IoT networks [17]. There are three main procedures to
constructDQN-basedmodel,includingepsilon-greedystrategy,deepneuralnetwork(DNN)function
approximator, and q-learning algorithm based on Bellman equation for handling Markov decision
process(MDP)problem.S,A,R,andγ representthebatchofpotentialstates,actions,rewards,and
discount factors for future rewards, respectively [18,19]. In the initial step t, the agent explores by
epsilon-greedy method and randomly selects an action a for sampling the reward r(s,a) in order
t t t t
to further calculate q-value of that particular s. At time t+1, the environment feedbacks the next-
t
stateobservations basedonthetransitionp(.|s,a).Thisexplorationstrategywilliterativelyexecute
t+1 t t
untiltheoptimalq-valueandpolicyaredefined.Algorithmdesignbasedonreinforcementprinciples
feasibly observes scheduler states and explores rule actions to propose scheduling rules for adaptive
resource management and enabling QoS provisioning scheme. Moreover, a model-free multi-agent
approachfeasiblytacklestheheterogeneityofcorebackbonenetworkforefficienttrafficcontroland
channelreassignmentinSDN-basedIoTnetworks[20].
1.1 PaperContributions
Inthispaper,theproposedsystemarchitectureisadoptedtodeploymulti-controllerplacementin
NFV architecture for observing various state abstractions. Multi-agent DQNs (MADQNs) explores
actionsonresourceplacementandcomputationdecisionsforoffloadingwn towardsappropriateeFL
k
aggregation server. Centralized controller abstracts IoT device and resource statuses to gather state
spaces for the proposed adaptive resource allocation agent (PARAA). Decentralized controllers as
a virtualized infrastructure manager (VIM) and VNFs are presented to abstract NFVI states for
proposedintelligentcomputationoffloadingagent(PICOA).MADQNsobtainthemaximumfuture
long-termrewardexpectationofjointstatespacesbyusingq-valuefunctionandDNNapproximator.
Theoptimalpolicyisdefinedbeforeexploitationphaseandobtainedbyacentralizedcontroller.The
proposedschemeextendsMADQNsbyrenderingvirtualnetworkfunctions(VNF)forwardinggraph
(VNFFG)andupgradingthedeficientallocationactionstoapproachsufficientservingMECresource
pools. The proposed controller updates the forwarding rule reactively for long-term sufficiency. An
experimental simulation is conducted to illustrate the performance of proposed scheme. The custom
environmentandDQNagentweredevelopedbyusingOpenAIGymlibrary,TensorFlow,Keras,and
the concept of Bellman equation. To evaluate the QoS metrics in SDN/NFV aspects, Mininet and
RYU SDN controller are conducted. In NFV management and orchestration (MANO), mini-nfv
framework is applied on top of Mininet to develop the descriptors using TOSCA NFV template.
Finally, simulation on 5G new radio (NR) networks is conducted to present an end-to-end (E2E)
perspectivebyusingns-3,adiscrete-eventnetworksimulator.
1.2 PaperOrganizations
The rest of the paper is organized as follows. The system models, including architectural frame-
workandpreliminariesofproposedMADQNscomponents,arepresentedinSection2.Theproposed
approach is thoroughly described in Section 3. In Section 4, simulation setup, performance metrics,
referenceschemes,andresultdiscussionsareshown.Section5presentsthefinalconclusion.

3322 CMC,2022,vol.71,no.2
2 SystemModels
2.1 ArchitecturalFramework
In the system architecture, SDN CP allows a programmable DQN-based mechanism to observe
states of the network environment via OpenFlow (OF) protocol in southbound interface (SBI),
which allows the cluster head to contribute significant roles for data of IoT nodes and resource
utilization collection [21]. The proposed SDN/NFV-enabled architecture for supporting MADQNs
programmabilityandofferingmultipleeFLserverswithinNFVI-MECenvironmentisshowninFig.1.
Intheproposedsystemarchitecture,thecentralizedSDNcontrollercommunicateswithNFV-MANO
layerformanagementfunctionsinVNFmanager(VNFM)andVIMthroughorchestrationinterfaces
[22]. Ve-Vnfm interface interacts between SDN controller as VNFs and VNFM for operating the
lifecycle network services and resources management. Nf-Vi interface allows the controllability of
NFVI resource pools for central SDN controller as a VIM [23]. To activate connectivity services
betweenvirtualmachine(VM)andVNFs,Vn-Nflogicalinterfaceisusedintheproposedarchitecture
to adjust the virtual storage and computing resources based on VNFs mapping orchestration.
To configure resource allocation based on optimal PARAA policy, decentralized SDN controllers
as a VIM and VNFs are proposed in this scheme to formulate the parameterization of action-
based VNFFG rendering for service function chaining (SFC) management system. The proposed
MANO manages the VNF placement with appropriate element management system (EMS), virtual
deploymentunit(VDU),andVMcapabilitiesbasedonallocationpolicyinparticularcongestionstate
spaces. The resource-constrained state observation leads to a prior for agents to adjust the backup
instances with model service prioritization. After the resources are adjusted, PICOA computes the
policy to advocate eFL server for local model aggregation offloading. Within multi-controllers, the
flow entry installation process is configured reactively in the centralized entity. Each cluster head is
commandedbyOFprotocolwithaflowruleinstallation.Sinceproactivemodehasthecapabilityfor
eachOF-enabledswitchtosetuptheflowrulesinternally,theproposedagentcontrollerwillprioritize
the reactive rule installation to ensure the proposed central policy configuration. Agent controller
checksthepacketflowwithalltheglobaltablesandupdatescountersforinstructionsetexecutions.In
ourproposedscheme,theflowpriority,hardtimeout,andidletimeoutaremeasuredbytheremaining
MEC resources, time intervals, and criticalities of FL model services. However, if there is no match
withinglobaltables,theagentcontrollerexecutestheadd-flowmethodbasedontheparticularstate-
action approximation to accordingly append datapath id, match details, actions, priority, and buffer
id. With different dimensional features and scale values, SDN database entity is expected to handle
the storage and preprocessing phases. For the proposed agent model, the data requiring from SDN
database is uplink/downlink resource adjustment statuses, resource of eFL MEC nodes, and default
coreresourceutilizationsystem.Withthesefeatures,theagentfeasiblyacquiresthestateobservation
spacesforsamplingandexploringthepotentialactions.
2.2 ProposedDQNComponents
In this context, main components of MADQNs consist of state, action, reward, and transition
probability. For the hyperparameters, the values are optimized by standard parameterization for
controllingthebehaviorofthelearningmodelsuchaslearningrateα,discountfactorγ,epsilonε,and
mini-batchsizesq .Insoftware-definedIoTnetworks,thelocal,distributed,andcentralizedresources
m
forcommunicationandcomputationarecomplextomeasurethoroughly.Moreover,theobservation
anddiscretevalueswillbechallengingtocapture.Therefore,eachelementwasassignedinpercentile
scales.

CMC,2022,vol.71,no.2 3323
Figure1:ThesystemarchitectureforMADQNsapproachandvirtualizationofeFLservers
State: in MADQNs environment, the state spaces are comprised of two main observations for
PARAAandPICOA.ForPARAA,thestateconsistsofcontrolstatusesandaglobalfunctionalview,
including the extant maximum and minimum resources denoted as res and res , respectively. For
max min
PICOA,thestatespacesareabstractedbydecentralizedcontrollers,includingthemaximumeFLnode
i capacities, cost of VNF m placement at eFL node i, and computation cost of local model wn at
k
eFL node i, denoted as resi , cvnfi, and cpi, respectively. The joint state observation contains two
mec m w
significant spaces such as uplink/downlink resource statuses and resource increment/decrement dis-
creteadjustmentindefaultresourceutilizationsystem,whichisdenotedasres andres ,respectively.
c pace
Eqs.(1) and (2) presents the expression of state spaces. The increment/decrement level was indicated
according to the positive and negative weights, denoted as ω+ and ω−, of a particular peak/off-peak
networkcongestion.Basedontheexperiencereplay,optimalresourcetargetsaredefined.
S = {res , res , res ,res } (1)
PARAA max min c pace
S = {resi ,cvnfi,cpi,res ,res } (2)
PICOA mec m w c pace
Action: in this environment, the batch of potential actions refers to the resource updates and
SFC, which are collectively mapped by VNFFG parameterization towards virtual MEC resource
poolsintheNFVIentity.Numerically,theactionspacesaspecifythediscretizationoperationscaleof
increment,decrement,andstatic,denotedasA (cid:6) {0,1,2}.Thepercentageofappliedactionvalues
PARAA
issetwithinarestrainedallocationsteptoreachanoptimalbalanceofdownlinkanduplinkcapacities.
TheschemeforecastscomputingandstorageresourcesforprocessingVNFmandallocationindexin
serving eFL node i, denoted as (cp ,sr ) and aii , respectively. In the proposed system architecture, i
m m m
eFLaggregationserverdecisionsareprovidedinPICOAasA (cid:6) {1,2,...,i}byevaluatingthetask
PICOA
executionefficiency.

3324 CMC,2022,vol.71,no.2
Reward: the intermediate reward in a particular time t, denoted as r(s,a), is maximized when
t t t
the agent reaches the optimal resource allocation res , which is adaptable based on three essential
oe
conditions, including transmission intervals, experienced q-value, and the remaining resource per-
centile. Moreover, in IoT peak hour congestion, the resource increment requires the extra serving
available resources in virtual computational blocks, denoted as res . The output of computational
xt
capabilities from the selected action towards virtual MEC resource pools in each VNF is the main
component for model aggregation completion. The reward considers the number of VNF requests
andthecomputationalcostsofeachVNFinthatparticularselectedVNFFGrendering.Theoutput
of reward determines the efficiency of resource allocation and eFL server selection from actions of
PARAAandPICOAagentsinadefinedstate.
Transition Probability: different policy determines distinct transition step for sampling the next
stateobservation.Intheearlystage,therandomnessoftransitionpolicyallowstheagentstoexplore
theactionswithoutspecifiedprobabilities.However,oncetheexplorationstrategyreachesanoptimal
goalofresourceallocationrewards,epsilon-greedypolicyexecutesthetransition,denotesasp(.|s,a),
t t
byperformingtheexploitationstrategyfollowsthegivenactiontoitsstatepair.Thereafter,whenthe
agentreceivesthenextstatespacess fromenvironmentfeedback,theagentwillcheckthevariation
t+1
anddiversityintheexperiencepoolstoenforceaparticularactionforthatstatespace.
3 Multi-AgentDeepQ-NetworksforEfficientEdgeFederatedLearningCommunications
To describe the MADQNs softwarization framework with the proposed controllers towards
virtual resource allocation and eFL aggregation server selection, this section delivers two primary
aspects of the proposed scheme, including the algorithm flows for multi-agent in NFVI-MEC and
self-organizingagentcontrollersforcollaborativeupdatesinNFV-enabledeFL.
3.1 AlgorithmFlowforMADQNsinProposedEnvironment
To optimize the policy of the model, q-table and DNN are computing in parallel behavior to
support the trade-off between time-critical and precision. However, DNN acts as a central control
which structures as a prime approximator. Each potential state-action pair has a q-value that
accumulatesinbothq-tableandapproximatedDNNoutputlayeraftertheexplorationstrategy.With
a feedforward network, numerous weight initializations, neurons, and multiple layers of perceptron,
theq-valuedecision-makingismoreaccurate,yetexecutiontimeissimultaneouslyhigh.Tooptimize
a policy for a long-term self-learning environment, the randomness in exploration processes of the
networking environment has to be handled. The hyperparameters are required to be well-assigned
andrelatedtothefine-grainedscenario.Theoptimalpolicyforexploitationstrategyastheendgoalis
denotedasπ∗,whichfurtherexpressesinEqs.(3)–(6).Eachpolicyinterpretstheagentandobservation
differentlybasedonthevaluefunctionandq-valuefunctionwithdistincttransitionprobabilityp.The
requiredparameterconsistsofthebeginningstateresourceconditionss ,currentstates,nextstates
0 t t+1
observation of [resi ,cvnfi,cpi, res , res ], criticality intervals, and sample action a. Subsequently,
mec m w c pace t
the working process of MADQNs elements in NFVI-MEC environment is described in three major
functional phases, including value and q-value functions, function approximator, and experience
replay.
(cid:2) (cid:4)
(cid:3)endT
π∗ = argmaxE γtr | π (3)
π t
π t=0

CMC,2022,vol.71,no.2 3325
s ∼ p(s ) (4)
0 0
a ∼ π(.|s[resi ,cvnfi,cpi,res , res ]) (5)
t t mec m w c pace
s [(resi ) ,(cvnfi) ,(cpi) , (res ) ,(res ) ] ∼ p(.|s,a) (6)
t+1 mec t+1 m t+1 w t+1 c t+1 pace t+1 t t
Thevaluefunctioniscomputedforpolicytransformationandlow-dimensionalperspectivetoget
the value of state s and create sample paths. It is significant to identify the resource condition at a
particular time. To differentiate between each random exploration policy, the cumulative reward is a
keyvaluetomaximizetheexpectation.Valuefunctioncapturesavectorofrewardtofollowaparticular
policyπ forevaluatingtheperformanceofanagentbydefiningtheexpectedfuturerewards.Thevalue
functiondenotedasVπ(s[resi ,cvnfi,cpi,res , res ])ofaninputstateobservationsintoapolicyπ is
mec m w c pace
usedforreturningtheexpectedoutcomefollowingtheMDP.Inourproposedenvironment,thevalue
functionisexecutedinexploitationstrategyfollowingthepolicy.Theq-valuefunctioncanbeexpressed
inordertoadapttoaspecificcomputationstate,whichfollowstheBellmanEquationtolabeltheq-
value for state-action pairs. Towards the optimal q-value Q∗(s,a), the formulation with proposed
t t
stateobservationsandactionspacesinoursetupenvironmentfeaturesispresented(seeEq.(7)).The
expected main requirements are the rewards of that particular state-action pair and the value of the
nextstatethattheenvironmentendsupin,whichisexpressedass(cid:4)[(resi )(cid:4),(cvnfi)(cid:4),(cpi)(cid:4), res(cid:4), res(cid:4) ].
mec m w c pace
TheexpectationE
s(cid:4)∼ε
expressestherandomnessofstates(cid:4)observation.Tosolvefortheoptimalpolicy,
theiterative updatehas to beexecuted. With knownoptimalpolicy,the bestaction will bechosenat
states(cid:4)tomaximizetheq-value.However,thisprocessisonlysupportedintheshort-periodnetworking
simulationprocess,butnotsupportedinlong-termsustainabilityanditerativeexecution;therefore,the
functionapproximatorcomestotakeplace.
(cid:5) (cid:6)
Q∗(s,a) = E s(cid:4)∼ε r+γ m
a
a
(cid:4)
xQ∗(s(cid:4)[(resi
mec
)(cid:4),(cvnf
m
i)(cid:4),(cpi
w
)(cid:4), res (cid:4)
c
, res (cid:4)
pace
],a(cid:4)) (7)
DNN estimates the functions Q(s,a;θ,b) based on biases b and weights θ on each neuron
connector between each perceptron which is equivalent to peak hour and off-peak hour intervals in
networking priority. The input processing of each possible state observation from time 0 to initial
time t, including the resource conditions of the network environment, towards an optimal action-
value selection is based on the congestion status. And weights and bias in one sample perceptron
are adjusted. The rectified linear unit (ReLU) activation function is used to transform the sum of
each connector weight and bias intervals from input until the output layer. Algorithm 1 presents the
MADQNs flow towards the optimal resource allocation policy and eFL selection in the proposed
framework. Agent execution starts with hyperparameters and parameters initialization. The total
reward container per episode, particular reward in each episode, the number of episodes, discrete
statespaces,q-table,thestartingepsilonvalue,thefinalepsilonvalue,andparticularepsilon-decaying
value are denoted as r , e, num , s , q , εs, εe, and ε−, respectively. The scheme targets the
e r e discrete table
gathered state observations for applying agent learning. The joint allocation and computation costs
areconsideredforcalculatingexpected rewards,includingthenumberofVNFsto attaineFL node i
decision,denotedasnvnf.However,todetailthearchitecturalstackofappliedDNN,aTensorFlow-
i
based implementation is designed to reach the optimal model with accurate parameter estimation.

3326 CMC,2022,vol.71,no.2
The experience replay, denoted as e = (s,a,r,s ), feeds the online and target networks for
t t t t t+1
choosing the actions and approximating its q-value. Since there are numerous possible continuous
networkingstates,thediscretestateobservationsareutilizedtoinputinthefirstlayerasamini-batchof
resourceconditionsforapproximatinganoptimalincrement/decrementbetweenuplinkanddownlink
communications. However, if ω+ is high, the resource utilization system is also increasingly enlarged
to solve the bottleneck issues. The double dense layers with ReLU are applied to analyze the state
differentiationandsuitableactionstomaximizetheupcomingreward.Fortheoutputlayerwithlinear,
theactionq-valueistriggeredbasedonthedenselayerconditions.Ifthegradientupdateevaluatesan
unsatisfiedprecision,themodelwillbereprocessed.Untilthemodelisaccepted,thecompilingprocess
isexecutedwithAdamoptimizerandmeansquarederror(MSE)metric.
Algorithm1:PseudocodefortheproposedMADQNstowardsoptimalactionselection
Require:s [resi ,cvnfi,cpi,res ,res ],res ,res ,A,res ,res ,ω−,ω+
mec j w c pace min max oe xt
Ensure: optimal actions on allocation policies and eFL server selection from each episode for
orchestratingNFVI-MECresourcepools
1: Initializer ,γ,α,num ,q ,s ,q ,ε,εs,εe,ε−
e e m discrete table
2: foreachepisodeinrange(num )do
e
3: Initializeeachepisoderewarde
r
4: Transformthestate s tos
discrete
5: whiletruedo
6: ifrandom()>ε then
7: Agentselectsactionabya = argmax(q [s ])/DNN
table discrete
8: else
9: Agentselectsrandomaction a
10: endif
11: Calculaterewardrbasedoncomputationandplacementcosts
12. Performselectedaction a,thenenternext-states(cid:4) by p(.|s,a)
13: Addthedefinedrewardrtotheinitializedepisoderewarde
r
14: Transformthenext-states(cid:4) totheclusteringchunks(cid:4)
discrete
15: ifthenext-stateresourceres hasastableandoptimalallocationstatusesdo
c
16: Inputthemaximumq-valueforstate-actionpair
17: else
18: Initializefuturemaximumq-valuebymax(q [s(cid:4) ])
table discrete
19: Initializecurrent-q-valueQ forstate-actionpair
c
20: Q ← (1−α)Q + α·(Q∗(s,a)−Q )(seeEq.(7))
NEW c c
21: Inputnewq-valueQ forthestate-actionpair
NEW
22: endif
23: Updates tos(cid:4)
discrete discrete
24: endwhile
25: ifεe ≥ episode ≥ εs then
26: ε− = ε−
27: endif
28: r .append(e)
e r
29: endfor
By applying the proposed MADQNs model, the average reward aggregation for the resource
allocationenvironmentisobtained.Theaveragerewardoutputofoptimalresourceallocationissteady

CMC,2022,vol.71,no.2 3327
formostoftheepisodesbutremainssomedownwardmarkstowardslimitedresourceutilization,which
leadstounstablemanagement.Thesteadyandunsteadystate-actionpairsaredetectedandneededto
besignificantlyenhancedforavoidinghighpacketdropscenariosinheterogeneouslocalmodelupdate
communications.
3.2 Self-OrganizingAgentControllersforOptimalEdgeAggregationDecisions
The implicit algorithm flow is proposed to handle the instability of MADQNs model in NFVI-
MEC environment by leveraging the capabilities of the agent controllers and orchestrator. The
proposedmethodinstallsflowrulesforeachIoTclusterheadwiththeadjustmentofuplink/downlink
resource utilization priority. The orchestrator configures VNFFG descriptors following the resource
allocationpolicyfromAlgorithm1towardseFLaggregationwithoptimalMECresourcepools.The
proposedagentcontrollerrequirestoorchestratetheflowentrytablesofmultipleIoTclusterheadsby
applyingtheconvergenceofresourceallocationpolicyandOFcontrollerflowstats.Eachstate-action
(s, a) pair from MADQNs-based model is transformed into the flow configuration pair (s , a ) by
f f
updatingtheuplink/downlinkresourcestatusesandpeakhour/off-peakhourintervalsintoinstruction
sets and priority of the entries, respectively. Based on the priority and instruction sets of each traffic
flow,orchestratorgainsthepriorinformationtohandlethevirtualresourcepooladjustmentinNFVI.
Fig.2presentsthestatetransitionofMADQNsandcontrollermanagementwithinSDN/NFVsystem.
Whentheclientupdatesthelocalmodel,thepipelineprocessingisperformed.IntegratedPARAAand
PICOAalgorithmsoptimizetheresourceallocationpoliciesandeFLaggregationMECselectionsas
describedinAlgorithm1.Withintheinspecteddeficientactionsintrainingphase,theproposedscheme
adjuststhepolicyandappendssufficientvirtualresourcepoolsforoptimizingtheservingcapacityof
theselectedeFLnode,asdescribedinAlgorithm2.
4 PerformanceEvaluation
NFV-enabled eFL- Centralized SDN Decentralized SDN
Open vSwitch gNB
Aggregation MEC Controller Controllers (VIM and VNFs)
1. OFPT_PACKET_IN
2. Initial Context Setup Request
3. Initial Context Setup Response
4. Executing DQN Agent 1: Optimizing
Resource Allocation Policies
5. Action-based VNF Placement
and VNFFG Creation
6. Executing DQN Agent 2: Optimizing eFL
Aggregation MEC Offloading Decisions
7. Render VNFFG for SFC
Management on each eFL service
8. Install or update the forwarding rule and execute the update process
9. OFPT_PACKET_OUT
Figure2:Thestatetransitionforproposedcontrollerstoinstallforwardingruleoflocalmodelupdates

3328 CMC,2022,vol.71,no.2
4.1 SimulationSetup
To prove the theoretical approach, this section describes the three main simulation adoption
environments,includingMADQNsmodelconstruction,SDN/NFVcontrolperformance,and5GNR
networkexperimenttocapturetheE2EQoSperformances.
By using OpenAI Gym library [24], the environment setup requires four primary functions. The
initialization(init)functiondeclarestheavailablecharacteristicsofstateobservations(seeEqs.(1)and
(2))inthesetupenvironment.Theinitexploress withintheepsilon-greedyrandomexploration.The
0
allocation step function updates the new state environment, gives a reward, and completes statutes
after the agent controller performs any specific actions. Finally, whether restarting the simulation,
changing the network circumstances, or starting a new episode, the reset function is used. The goal
of the MADQNs model is to interact with the setup environment and choose the optimal action
for a specific networking state in order to optimize eFL offloading server decisions. To train and
testthemodels,weusedTensorFlowandKeras [25,26]. Fig.3presentsthetotalaverage rewardsper
100episodeswiththreeα performances,including0.01,0.05,and0.09.Therewardsareoutputtedin
negative numbers since the setup assigned the non-optimal reward as −0.5, which was cumulatively
summeduntiltheendofepisodes.Ineachepisode,theQ∗(s,a)aregathered.Inthisenvironmentsetup,
theoptimalα is0.09,whichfluctuatesaround−128.3075.
Algorithm2:Proposedself-organizingagentcontrollersforoptimizingeFLaggregationselection
Require:PARAAandPICOAdecisionsbasedonoptimalactions
Ensure:optimalflowentryinstallation,resourceorchestration,andeFLserverselection
1: foreachlocalmodelupdateintiterationdo
2: Transformthediscretestates tomatchwiththeflowcriteria(s)
t t f
3: foreachOFPT_PACKET_INinrangeofclusterheadsCH do
4: ifnomatchfoundinlocalCH tablesdo
5: ApplyoptimalpoliciesofPARAAandPICOAtobridgetrafficthroughVNFs
6: Transformtheoptimaldiscreteactiona toadaptwiththeflowstats(a)
t t f
7: VNFFGcreationforrenderingtoSFC,then,installtheflowentryforexecution
8: else
9: Executetheinstructionsetsofthefoundflowentry
10: endif
11: foreachselectedeFLserverinrange(i)do
12: Performedgeaggregationforoptimalwt
i
13: endfor[edgeaggregation]
14: endfor[OFPT_PACKET_OUT]
15: [GlobalServer]
16: Computeaveragingaggregationon[wt, wt,...wt]forglobalmodelWt+1
1 2 i G
17: endfor[titeration]
To capture the particular QoS performance metrics of the proposed controllers and NFV
modules,mini-nfvontopofMininetisusedtocreatethedataplanetopology,VNFdescriptors,and
VNFFG descriptors. Mini-nfv supports the external SDN controller platform for experimentation.
The forwarding rule installation is configured by FlowManager and RYU-based platform [27–31].
The descriptors set the VDU and VM capabilities based on selected actions from the optimal policy
table. Each flow entry is configured following the forwarding graph. Fig.4 presents the interaction

CMC,2022,vol.71,no.2 3329
of the convergence; however, the virtual links for communication perspective are still restricted for
explicitfine-grainedperformance.
Figure3:Thetotalaveragerewardsper100episodeswithinMADQNsmodelconstruction
OpenAI Gym and TensorFlow
|     |     |     | (2) select action a | (3) new state,  |
| --- | --- | --- | ------------------- | --------------- |
allocation step function
reward, and
|                     | (1) sample s (with   |     |                          | done statuses |
| ------------------- | -------------------- | --- | ------------------------ | ------------- |
| init function       | randomness function) |     | multi-agent approach     |               |
| (4) reset the state | reset function       |     | optimized policy outputs |               |
Mininet, Mini-NFV, and RYU Controller
| Data plane topology   | VNF                      | VNF      |     | VNFFG       |
| --------------------- | ------------------------ | -------- | --- | ----------- |
| configuration         | descriptors              | creation |     | descriptors |
| Execute and capture   | FlowManager: forwarding  |          |     | VNFFG       |
| QoS metrics           | rule installation        |          |     | Creation    |
Figure4:TheinteractionofoptimalpolicyoutputsforSDN/NFV-basedcontrolentities
Adiscrete-eventnetworksimulator,namelyns-3,isusedinthisenvironmenttoperformtheE2E
convergence[32–34].Thesimulationwasexecutedfor430s,whichadjustedinto4consecutivenetwork
congestion conditions to reflect the service-learning criticalities of FL communication reliability. In
thissetup,thereare4eFLnodes,andthevirtualextendednetworksloadingwasconfiguredbetween
0to250.Additionally,thereare4remoteradioheads(RRHs),andtheuserdatarateisbetween20to
72Mbps.Themodelupdateswillrelyonthenetworksituation,andthecongestionenvironmentwill
increasethelossprobabilitybetweenclientsandaggregationservers.Thecongestionstatesloweredthe
modelaccuracyandreducedglobalmodelreliability.Thepayloadsizewassetto1024bytes,andQoS
classidentifier(QCI)mechanismissetasuserdatagramprotocol(UDP).Atthecoreside,thepoint-to-
point(P2P)linkbandwidthwasconfiguredto9Gb/s,andthebufferqueuingdisciplinewasoperated
by random early detection (RED) queue algorithm. The default link delay of MEC was configured
as 2 ms. The hyperparameters of MADQNs are prior configured to conduct the experiments with
maximizedoutputexpectationsintermsofcomputationintensityandtimeconstraints.Thelearning
rateαissetto0.09inthisenvironment.γ,num ,andεvaluesaresetto0.95,1000,and0.5,respectively.
e
ThemainhyperparametersandparametersconfigurationusedinoverallsimulationisshowninTab.1.

3330 CMC,2022,vol.71,no.2
Table1: Simulationparameters
Parameters Specifications
Simulationtime 430s
NumberofRRHs 4
Virtualextendednetworks 0to250
loading
VirtualeFLMECserver 4
Userdatarate 20to72Mbps
Payloadsize 1024Bytes
P2Plinkbandwidth 9Gbps
MEClinkdelay 2ms
α 0.09
γ 0.95
num 1000
e
ε value 0.5
4.2 ReferenceSchemesandPerformanceMetrics
To illustrate the proposed and reference approaches in overall performances, four different
resource control and eFL selection policies were simulated. The resource pools represented the
capacities extraction by the proposed actions of the model. Each scheme triggered different actions,
which contained the VNFFG mapping to particular virtual resources. Reference schemes were
simulated in control policy for IoT congestion scenarios, including maximal rate experienced-
based eFL selection (MRES), single-agent DQN-control (SADQN), and MADQNs. The proposed
scheme extended PARAA and PICOA policies by enhancing the deficient actions as described in
Algorithm2.
TheQoSmetricswhichwereusedtoevaluatethecomparisonbetweenthereferenceandproposed
approachesarepresentedasfollows[35,36].Delayspecifiesthelatencytimeofdatacommunications
fromthesendingnodetothereceivernode,includingpropagation,queueing,transmission,andcontrol
atthecoresystem,whicharedenotedasDprop,Dqueue,Dtr ,andDct ,respectively,asdescribedinEq.(8).
(J) (J) (J) (J)
Inthenetworksimulationarchitecture,J = {1, 2,...,j}denotesthenumberofqueueingbuffers.
(cid:3)j
Delay = (Dprop+ Dqueue+Dtr +Dct ) (8)
(J) (J) (J) (J)
J=1
TP refers to the communication throughput, which expresses the successful packets delivery
ratio over a given communication bandwidth bw (see Eq.(9)). The total, propagation, control, and
processinglatenciesofqueuedj entitiesaredenotedasTt ,Tprop,Tct,andTproc,respectively.
(J) (J) (J) (J)
(cid:7)
j (Tt )×bw
TP = (cid:7) J=1 (J) (9)
j (Tt +Tprop+Tct +Tproc)
J=1 (J) (J) (J) (J)

CMC,2022,vol.71,no.2 3331
Thepacketdropratiointheexperimentalsimulationistheratioformulationbetweentotalpacket
lost and total packet successfully transmitted. The packet drop counts are illustrated to specifically
compareinthisparticularexperimentalsetup.Thepacketdeliveryratiointhesimulationenvironment
iscalculatedbythesubtractionbetweenthetotalratioandpacketdropratio.
4.3 ResultsandDiscussions
The proposed agent outputted the offloading decisions of 142, 117, 371, and 370 local model
updatestoward4eFLservers,respectively.InSDN/NFV-enabledarchitecture,theprimaryconsider-
ation is the QoS metrics after installing and executing the forwarding rules [37,38]. The comparison
between proposed and reference schemes is shown in Fig.5. Within 430 s of 4 consecutive network
congestionconditions,theaveragecontroldelayis8.4723ms,whichwas28.2833,25.6824,and11.7175
mslowerthanMRES,SADQN,andMADQNs,respectively.
Figure5:ComparisonofaveragedelaybetweenproposedandreferenceschemesinSDN/NFVmodel
In E2E simulation, the emphasis of FL model reliability in real-time routing networks was
considered.Fig.6adepictedtheaveragedelaysofE2Ecommunicationsintheedgecloudsystems.The
data communication between the aggregation servers were utilized the IP network communications.
The graph presented the comparisons between the proposed and reference methods with various
possibilities of forwarding paths. The proposed scheme performed an average delay of 12.8948
ms, which was 64.3321, 150.9983, and 169.9983 ms lower than MADQNs, SADQN, and MRES,
respectively. The proposed scheme distinguished the loading metrics of every possible serving MEC
server. The predicted metrics represented the loading statuses of MEC server; therefore, the MEC,
which has the lowest loading metrics, will be considered as an optimal server for serving incoming
local model update requests. TP comparison is presented in Fig.6b, which illustrated the notable
outperformance over other approaches. The proposed scheme, MADQNs, SADQN, and MRES
reached an average throughput of 659.0801, 113.7167, 50.8434, and 47.2032 bps, respectively. The
proposed scheme utilized the integrated multi-agent to predict the optimal route with the lowest
loadingmetrics for efficient eFL offloading. The average packet drops ratio of the proposed scheme
significantlyreached0.0284%within430ssimulation,whichis0.1068%,0.1482%,and0.1446%lower
than MADQNs, SADQN, and MRES, respectively. In contrast, the proposed, MADQNs, SADQN,
and MRES schemes achieved a closing packet delivery ratio of 99.9965%, 99.9853%, 99.9501%, and
99.9384%,respectively.Figs.6c,and6dshowthegraphicalcomparisonofpacketdropratioandpacket
deliveryratio,respectively.Moreover,withinaparticularsimulationsetup,thepacketdropcountsof
theproposedschemereachedatotalof1309packets,whichwas4083,9746,and10847packetslower
thanMADQNs,SADQN,andMRES,respectively.

3332 CMC,2022,vol.71,no.2
Figure6:Comparisonof(a)E2Eaveragedelay,(b)throughput,(c)packetdropratio,and(d)packet
deliveryratiobetweenproposedandreferenceschemesinE2Ecommunicationperspective
MADQNs deployed the control policies of both deficient and efficient output episodes. The
downlinkanduplinktransmissionarestronglycongestedinheavymulti-dimensionalmodelupdates,
while multiple virtual MEC is offloaded and reallocated deficiently. To gain unoccupied resource
pools for QoS assurances, the proposed scheme extended MADQNs and considered the optimal
resource pools for high mission-critical FL model traffics, which covers the networking states with
over-bottleneckpeakhourcircumstances.Whiletheextantcommunicationandcomputationresources
are used, the proposed controllers and orchestrator advance the positive weights ω+ to accelerate
the serving resources from NFVI. The conditional configuration and orchestration trigger a flexible
servingbackupinstancecapacity.
InthecongestedFLcommunicationnetworks,thelocalmodelwn updatesandglobalmodelW
k G
distributions have to transmit through long-time queueing before entering the ingress buffer of the
routing or switching devices. During the heavy loading networks, the waiting time of the incoming
packets can be expired and discarded before forwarding to another network. Therefore, an eNA of
optimalresourceallocationandsufficienteFLaggregationserveroffloadingisapplicableforenhanc-
ingreliability.Inproposedschemeframework,thetransmissionfromwn toeFLnodeiwasenhanced
k
toaggregatereliablew modelsbasedontheproposedPARAAandPICOApolicies.Theaggregation
i
averaging procedures between edge w and parameter server were executed in appropriate intervals
i
or off-peak hours. Furthermore, the proposed approach is capable of alleviating the communication
overhead for both computation and communication latency since the proposed method determined
the optimal network interface with minimum cost for updating model parameters during congested
situations. The proposed scheme considered the serving cost of joint entities which are efficient to
eachservingpath.ThequeuingsystemofeachSDNentityattheDPnetworkandVNFentitieswere
handledseparately.ThecomputationoverheadandqueuingsysteminCPwereconsidered.Therefore,
the proposed scheme avoided the data forwarding overhead from high computation intensity. In the
proposed system, SDN controller was scheduled for the optimal path local model computation with
adequaterequests.Basedonthecomparisons,theproposedschemesignificantlyhandledtherouting
congestioninFLcommunicationsinordertomeetthecriteriaofURLLCkeyperformanceindicators.

CMC,2022,vol.71,no.2 3333
5 Conclusion
This paper proposed a multi-agent approach, including PARAA for optimizing virtual resource
allocation and PICOA for recommending eFL aggregation server offloading, in order to meet the
significance of URLLC for mission-critical IoT model services. SDN/NFV-enabled architectural
frameworkforcontrollingtheproposedforwardingrulesandvirtualresourceorchestrationisadopted
in software-defined IoT networks. MADQNs model interacted with the gathered state observations
and contributed a collection of exploration policies for sampling the allocation rules under the
expansion of edge intelligence. To obtain deficient policies, the proposed algorithms targeted weak
episodes with low aggregated rewards of optimal learning rate hyperparameter. The proposed agent
controller outputs a setup of long-term self-organizing flow entry with sufficient computation and
communications resource placement. The optimal actions are used to correspondingly configure the
VNFFGdescriptorsandmaptowardsadequatevirtualMECresourcepoolswithfourexperimental
congestion states. The simulation was conducted in three main aspects. Based on the validation, the
proposed scheme contributed a promising approach for achieving efficient eFL communications in
futuremassiveIoTcongestionstates.
Funding Statement: This work was funded by BK21 FOUR (Fostering Outstanding Universities for
Research)(No.5199990914048),andthisresearchwassupportedbyBasicScienceResearchProgram
through the National Research Foundation of Korea (NRF) funded by the Ministry of Education
(NRF-2020R1I1A3066543).Inaddition,thisworkwassupportedbytheSoonchunhyangUniversity
ResearchFund.
ConflictsofInterest:Theauthorsdeclarethattheyhavenoconflictsofinteresttoreportregardingthe
presentstudy.
References
[1] F. Hussain, S. A. Hassan, R. Hussain and E. Hossain, “Machine learning for resource management in
cellular and IoT networks: Potentials, current solutions, and open challenges,” IEEE Communications
Surveys&Tutorials,vol.22,no.2,pp.1251–1275,2020.
[2] D.Reinsel,J.GantzandJ.Rydning,“Thedigitalizationoftheworld:Fromedgetocore,”inIDCWhite
Paper,SeagateInc.,Framingham,MA,USA,vol.1,pp.1–28,2018.
[3] S.KimandD.-Y.Kim,“Adaptivedatatransmissionmethodaccordingtowirelessstateinlongrangewide
areanetworks,”Computers,Materials&Continua,vol.64,no.1,pp.1–15,2020.
[4] T.K.Rodrigues,K.Suto,H.Nishiyama,J.LiuandN.Kato,“Machinelearningmeetscomputationand
communicationcontrolinevolvingedgeandcloud:Challengesandfutureperspective,”IEEECommuni-
cationsSurveys&Tutorials,vol.22,no.1,pp.38–67,2020.
[5] B. Custers, A. Sears, F. Dechesne, I. Georgieva, T. Tani et al., EU Personal Data Protection
in Policy and Practice. Heidelberg, BE, DEU: Springer, 2019. [Online]. Available: https://doi.o
rg/10.1007/978-94-6265-282-8.
[6] W.Saeed,Z.Ahmad,A.I.Jehangiri,N.Mohamed,A.I.Umaretal.,“Afaulttolerantdatamanagement
schemeforhealthcareinternetofthingsinfogcomputing,”KSIITransactionsonInternetandInformation
Systems,vol.15,no.1,pp.35–57,2021.
[7] B.McMahan,E.Moore,D.Ramage,S.HampsonandB.A.Y.Arcas,“Communication-efficientlearning
of deep networks from decentralized data,” in Proc. of the 20th Int. Conf. on Artificial Intelligence and
Statistics,FortLauderdale,FL,USA,vol.54,pp.1273–1282,2017.
[8] W. Y. B. Lim, N. C. Luong, D. T. Hoang, Y. Jiao, Y. Liang et al., “Federated learning in mobile edge
networks:Acomprehensivesurvey,”IEEECommunicationsSurveys&Tutorials,vol.22,no.3,pp.2031–
2063,2020.

3334 CMC,2022,vol.71,no.2
[9] X. Mo and J. Xu, “Energy-efficient federated edge learning with joint communication and computation
design,”JournalofCommunicationsandInformationNetworks,vol.6,no.2,pp.110–124,2021.
[10] Y.Ye,S.Li,F.Liu,Y.TangandW.Hu,“EdgeFed:Optimizedfederatedlearningbasedonedgecomputing,”
IEEEAccess,vol.8,pp.209191–209198,2020.
[11] J.Ren,G.YuandG.Ding,“AcceleratingDNNtraininginwirelessfederatededgelearningsystems,”IEEE
JournalonSelectedAreasinCommunications,vol.39,no.1,pp.219–232,2021.
[12] D.-Y.Kim,S.KimandJ.H.Park,“AcombinednetworkcontrolapproachfortheedgecloudandLPWAN-
basedIoTservices,”ConcurrencyandComputation:PracticeandExperience,vol.32,no.1,2020.[Online].
Available:https://doi.org/10.1002/cpe.4406.
[13] Z.LiandQ.Zhu,“Anoffloadingstrategyformulti-userenergyconsumptionoptimizationinmulti-MEC
scene,”KSIITransactionsonInternetandInformationSystems,vol.14,no.10,pp.4025–4041,2020.
[14] X.Li,D.Li,J.Wan,C.LiuandM.Imran,“AdaptivetransmissionoptimizationinSDN-basedindustrial
internet of things with edge computing,”IEEE Internet of Things Journal, vol. 5, no. 3, pp. 1351–1360,
2018.
[15] S. Shahzadi, F. Ahmad, A. Basharat, M. Alruwaili, S. Alanazi et al., “Machine learning empowered
securitymanagementandqualityofserviceprovisioninSDN-NFVenvironment,”Computers,Materials
&Continua,vol.66,no.3,pp.2723–2749,2021.
[16] D.-Y. Kim and S. Kim, “Network-aided intelligent traffic steering in 5G mobile networks,”Computers,
Materials&Continua,vol.65,no.1,pp.243–261,2020.
[17] W.Chen,X.Qiu,T.Cai,H.-N.Dai,Z.Zhengetal.,“Deepreinforcementlearningforinternetofthings:
Acomprehensivesurvey,”IEEECommunicationsSurveys&Tutorials,vol.23,no.3,pp.1659–1692,2021.
[18] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness et al., “Human-level control through deep
reinforcementlearning,”Nature,vol.518,no.7540,pp.529–533,2015.
[19] N. Yuan, C. Jia, J. Lu, S. Gua, W. Li et al., “A DRL-based container placement scheme with auxiliary
tasks,”Computers,Materials&Continua,vol.64,no.3,pp.1657–1671,2020.
[20] T.Wu,P.Zhou,B.Wang,A.Li,X.Tangetal.,“Jointtrafficcontrolandmulti-channelreassignmentforcore
backbonenetworkinSDN-IoT:Amulti-agentdeepreinforcementlearningapproach,”IEEETransactions
onNetworkScienceandEngineering,vol.8,no.1,pp.231–245,2021.
[21] “OpenFlowswitchspecifications,”Opennetworkingfoundation,2014.[Online].Available:https://openne
tworking.org/wp-content/uploads/2014/10/openflow-switch-v1.3.4.pdf.
[22] “Networkfunctionsvirtualisation(NFV);ecosystem;reportonSDNusageinNFVarchitecturalframe-
work,”WhitePaper,ETSI,SophiaAntipolis,France,2015.[Online].Available:https://www.etsi.org/delive
r/etsi_gs/NFV-EVE/001_099/005/01.01.01_60/gs_nfv-eve005v010101p.pdf.
[23] “Network functions virtualisation (NFV) release 2; management and orchestration; architectural frame-
workspecification,”WhitePaper,ETSI,SophiaAntipolis,France,2021.[Online].Available:https://www.e
tsi.org/deliver/etsi_gs/NFV/001_099/006/02.01.01_60/gs_NFV006v020101p.pdf.
[24] G. Brockman, V. Cheung, L. Petterson, J. Schneider, J. Schulman et al., “OpenAI gym,”arXiv preprint
arXiv:1606.01540,2016.
[25] M.Abadi,A.Agarwal,P.Barham,E.Brevdo,Z.Chenetal.,“TensorFlow:Large-scalemachinelearning
onheterogeneousdistributedsystems,”arXivpreprintarXiv:1603.04467,2016.
[26] F.Chollet,“Keras,”2015.[Online].Available:https://github.com/fchollet/keras.
[27] B. Lantz, B. Heller and N. McKeown, “A network in a laptop: Rapidprototyping for software-defined
networks,”in Proc. of the 9th ACM SIGCOMM Workshop on Hot Topics in Networks, New York, NY,
USA,2010.[Online].Available:http://doi.acm.org/10.1145/1868447.1868466.
[28] “Ryu,”FaucetOrganisation.[Online].Available:https://github.com/faucetsdn/ryu.
[29] J.Castillo,“Mini-nfvframework,”2018.[Online].Available:https://github.com/josecastillolema/mini-nfv.
[30] H. Babbar, S. Rani, M. Masud, S. Verma, D. Anand et al., “Load balancing algorithm for migrating
switches in software-defined vehicular networks,” Computers, Materials & Continua, vol. 67, no. 1, pp.
1301–1316,2021.

CMC,2022,vol.71,no.2 3335
[31] J.Ali,G.-M.Lee,B.Roh,D.K.RyuandG.Park,“Software-definednetworkingapproachesforlinkfailure
recovery:Asurvey,”Sustainability,vol.12,no.10,2020.
[32] G.F.RileyandT.R.Henderson,“Thens-3networksimulator,”inModelingandToolsforNetworkSimula-
tion,Berlin,Heidelberg:Springer,2010.[Online].Available:https://doi.org/10.1007/978-3-642-12331-3_2.
[33] J.AliandB.Roh,“Aneffectivehierarchicalcontrolplaneforsoftware-definednetworksleveragingTOPSIS
forend-to-endQoSclass-mapping,”IEEEAccess,vol.8,pp.88990–89006,2020.
[34] S.Math,P.TamandS.Kim,“Intelligentreal-timeIoTtrafficsteeringin5Gedgenetworks,”Computers,
Materials&Continua,vol.67,no.3,pp.3433–3450,2021.
[35] J. Ali, B. Roh and S. Lee, “Qos improvement with an optimum controller selection for software-defined
networks,”PLoSONE,vol.14,no.5,pp.1–37,2019.
[36] P. Tam, S. Math and S. Kim, “Intelligent massive traffic handling scheme in 5G bottleneck backhaul
networks,”KSIITransactionsonInternetandInformationSystems,vol.15,no.3,pp.874–890,2021.
[37] J.AliandB.Roh,“Qualityofserviceimprovement withoptimalsoftware-definednetworking controller
andcontrolplaneclustering,”Computers,Materials&Continua,vol.67,no.1,pp.849–875,2021.
[38] M.Beshley,N.Kryvinska,H.Beshley,M.MedvetskyiandL.Barolli,“CentralizedQoSroutingmodelfor
delay/losssensitiveflowsattheSDN-ioTinfrastructure,”Computers,Materials&Continua,vol.69,no.3,
pp.3727–3748,2021.