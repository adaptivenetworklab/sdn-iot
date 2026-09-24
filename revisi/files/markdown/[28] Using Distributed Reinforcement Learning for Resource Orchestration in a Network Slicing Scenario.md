# [28] Using Distributed Reinforcement Learning for Resource Orchestration in a Network Slicing Scenario

> Source file: `[28] Using Distributed Reinforcement Learning for Resource Orchestration in a Network Slicing Scenario.pdf`

---

©2021 IEEE. This paper is under review at IEEE Transaction on Networking. Personal use of this material is permitted. Permission from IEEE must be
obtainedforallotheruses,inanycurrentorfuturemedia,includingreprinting/republishingthismaterialforadvertisingorpromotionalpurposes,creating
newcollectiveworks,forresaleorredistributiontoserversorlists,orreuseofanycopyrightedcomponentofthisworkinotherworks.
Using Distributed Reinforcement Learning for
Resource Orchestration in a Network Slicing
Scenario
Federico Mason∗, Gianfranco Nencioni†, Andrea Zanella∗
∗{masonfed, zanella}@dei.unipd.it, †gianfranco.nencioni@uis.no
∗ Department of Information Engineering, University of Padova - Padova, Italy
† Department of Electrical Engineering and Computer Science, University of Stavanger - Stavanger, Norway
Abstract—The Network Slicing (NS) paradigm enables the Inparticular,theSDNandNFVconceptsarekeyenablersof
partitionofphysicalandvirtualresourcesamongmultiplelogical the Network Slicing (NS) paradigm, which makes it possible
networks, possibly managed by different tenants. In such a
to define multiple virtual networks over the same physical
scenario, network resources need to be dynamically allocated
infrastructure [5], [6]. Under this vision, a slice consists
according to the slices’ requirements. In this paper, we attack
theaboveproblembyexploitingaDeepReinforcementLearning of a virtual overlay network designed to support commu-
approach.Ourframeworkisbasedonadistributedarchitecture, nication services with similar characteristics [7]. Hence, a
where multiple agents cooperate towards a common goal. The slice supporting eMBB applications (e.g., video streaming) is
agents’ training is carried out following the Advantage Actor characterized by very high bit rate, while a slice supporting
Critic algorithm, which allows to handle continuous action
URLLC applications (e.g., telesurgery) guarantees extremely
spaces. By means of extensive simulations, we show that our
approachyieldsbetterperformancethanbothastaticallocation high reliability and low latency.
of system resources and an efficient empirical strategy. At the If defined over the same infrastructure, different slices
same time, the proposed system ensures high adaptability to will contend for the same resources, which can be both
different scenarios without the need for additional training.
physical (e.g., optical links) and virtual (e.g., virtual baseband
IndexTerms—Networkslicing;resourceallocation;distributed processing units) [8]. In general, such resources are acquired
machine learning; deep reinforcement learning. by the slice broker (i.e., the body in charge of initializing
andorchestratingslices)fromtheinfrastructureproviders(i.e.,
the owners of the physical elements of the network) [9].
I. INTRODUCTION Then, slices are assigned to the slice tenants (e.g., virtual
THE fifth generation of cellular networks (5G) aims at network operators), which offer slice services to the end-
supporting different applications with very specific re- users. The amount of resources that are needed to support the
quirements over the same infrastructure. In this perspective, slice services are determined by the so-called Service Level
the3GPPconsortiumhasidentifiedthreemainserviceclasses, Agreement (SLA) between the slice tenant and broker [10].
namely enhanced Mobile BroadBand (eMBB), Ultra Reliable Therefore, a fundamental challenge in NS systems is how to
LowLatencyCommunication(URLLC)andmassiveMachine distribute resources among the different slices in an efficient
Type Communication (mMTC) [1]. Specifically, eMBB is way, ensuring that all the SLAs are satisfied [11].
expected to provide very high throughput in both downlink Inthiswork,weconsiderascenariowheretwosliceclasses
and uplink, while URLLC appeals to applications with strict (i.e.,eMBBandURLLC),withdynamicrequirementsinterm
latencyandreliabilityconstraints,likeroboticsurgeries,tactile ofthroughput,computationalpower,memorycapacity,andde-
Internet, and emergency communications [2]. lay,areinstantiatedoverthesamenetworkinfrastructure.Each
Traditional telecommunication networks are often based slice is composed by multiple information flows (with static
on a rigid architecture and are not apt to support such ser- routes) that contend for the bandwidth provided by network
vices [3]. To overcome this problem, the research community links, and the computational and memory resources provided
has introduced the concepts of Software Defined Networking bythecomputingfacilitiesconnectedwiththenetworknodes.
(SDN) and Network Function Virtualization (NFV), which Theproblemistodynamicallydistributethenetworkresources
can make networks more flexible and adaptable to different among the active information flows, in accordance to the
requirements [4]. The NFV principle makes it possible to characteristic of the slices which they belong to.
executenetworkfunctionsovervirtualmachinesintheCloud. Thenaiveapproachconsistsinstaticallyallocatingcommu-
Instead, SDN separates the control plane from the forwarding nication and computational resources to the different slices.
plane, enabling the dynamic routing of data flows. However, this method cannot exploit the statistical multiplex-
ing of the information flows and, consequently, may lead
ThisworkwassupportedbyConsortiumGARRthroughthe“OrioCarlini” to greater over-provisioning costs and low utilization of the
scholarship2019.Apreliminaryandreducedversionofthismanuscripthas
available resources. On the other hand, conventional resource
been submitted to the IEEE Mediterranean Communication and Computer
NetworkingConference,June2021. allocation strategies are often unsuitable because cannot un-
1202
yaM
71
]AM.sc[
1v64970.5012:viXra

derstand the specific features of different slices, neither deal problem of offloading user tasks to edge computing facilities
with the high complexity of NS environments. and design a novel algorithm to optimize resource utilization.
Here, we propose a machine-learning based approach and Finally,Fossatietal.proposeaframeworktogeneralizemulti-
|            |         |     |               |     |          |               |     | resource | allocation | techniques | according |     | to different |     | fairness |
| ---------- | ------- | --- | ------------- | --- | -------- | ------------- | --- | -------- | ---------- | ---------- | --------- | --- | ------------ | --- | -------- |
| attack the | problem |     | by exploiting |     | the Deep | Reinforcement |     |          |            |            |           |     |              |     |          |
Learning (DRL) paradigm, which combines Reinforcement goals, considering also the critical scenario where resources
Learning (RL) algorithms and Neural Networks (NNs) to find are not sufficient to satisfy all the slices’ demands [18].
strategies for the management of complex environments [12]. To address the many challenges related to the NS man-
Morespecifically,wedesignadistributedDRLsystem,where agement, the scientific community has shown great interest
multiple agents collaborate to allocate network resources in implementing Machine Learning (ML) techniques in such
among the different slices running over the same infrastruc- scenarios. In [19], the authors exploit NNs to predict the
ture. The continuous interaction between such learning units traffic evolution in a mobile core-network, thus optimizing
makes it possible to increase both the system efficiency and the routing and the wavelength assignment according to the
adaptability to different scenarios. The main contributions of SDNprinciples.Anotherexamplecanbefoundin[20],where
our work consists in the following points: generative adversarial NNs are used to minimize the noise in
We introduce a general network model that makes it the measurement of SLA satisfaction. Instead, the authors of
•
|     |     |     |     |     |     |     |     | [21] design | a system | based | on convolutional |     | NNs | to associate |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ----- | ---------------- | --- | --- | ------------ | --- |
possibletomodelmultiplecommunicationslicesrunning
over the same infrastructure in different configurations, users with network slices according to the required Quality of
and is apt to represent a large variety of scenarios. Service(QoS).Finally,in[22],itisimplementedadistributed
architecturepredictingtheamountofdatathathastobecached
| • We | develop | a novel | DRL-based |     | strategy | to dynamically |     |     |     |     |     |     |     |     |     |
| ---- | ------- | ------- | --------- | --- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
orchestrate resource allocation to multiple slices. The in the network edge to address the user demands.
|          |     |          |     |               |     |         |             | Among | all | the ML | techniques | that | are | used for | slice |
| -------- | --- | -------- | --- | ------------- | --- | ------- | ----------- | ----- | --- | ------ | ---------- | ---- | --- | -------- | ----- |
| proposed |     | approach | is  | characterized |     | by high | flexibility |       |     |        |            |      |     |          |       |
and can be implemented in different network topologies orchestration, DRL is particularly appreciated since its ability
without the need for additional training. tolearncomplexstrategiesbytrialanderror,withouttheneed
oflabeleddata.In[23],itisdefinedanovelresourceallocation
| • We | show | how transfer |     | learning | can improve |     | the perfor- |     |     |     |     |     |     |     |     |
| ---- | ---- | ------------ | --- | -------- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
manceofthesystem,byspecializingthestrategylearned policy, based on Q-Learning [24], that jointly handles the
|                 |            |     |            |          |          |     |          | bandwidth,      | computational |                | and storage  |           | requirements |              | of slice |
| --------------- | ---------- | --- | ---------- | -------- | -------- | --- | -------- | --------------- | ------------- | -------------- | ------------ | --------- | ------------ | ------------ | -------- |
| by              | the agents | in  | a scalable | fashion. |          |     |          |                 |               |                |              |           |              |              |          |
|                 |            |     |            |          |          |     |          | users. Instead, |               | in [25],       | Ayala-Romero |           | et al.       | investigates | the      |
| The performance |            |     | of the     | proposed | strategy | is  | assessed | in              |               |                |              |           |              |              |          |
|                 |            |     |            |          |          |     |          | orchestration   |               | of virtualized | radio        | resources |              | by means     | of a     |
multiplescenarios,includingalsoarealnetworktopology,and
DRLframeworkthatencodestrafficdatafeaturesintoresource
| against | a Meta-Heuristic |     | technique |     | and an | efficient | empirical |         |            |           |          |     |               |     |          |
| ------- | ---------------- | --- | --------- | --- | ------ | --------- | --------- | ------- | ---------- | --------- | -------- | --- | ------------- | --- | -------- |
|         |                  |     |           |     |        |           |           | control | decisions. | A similar | approach |     | is considered |     | in [26], |
algorithm.
|               |     |      |          |              |        |             |        | where virtual |             | network | functions | are dynamically |       | reconfigured |     |
| ------------- | --- | ---- | -------- | ------------ | ------ | ----------- | ------ | ------------- | ----------- | ------- | --------- | --------------- | ----- | ------------ | --- |
| The remainder |     | of   | the work | is organized |        | as follows. | Sec.   | II            |             |         |           |                 |       |              |     |
|               |     |      |          |              |        |             |        | in order      | to maximize |         | the QoS   | of slice        | users | and minimize |     |
| discusses     | the | most | relevant | works        | in the | considered  | field. |               |             |         |           |                 |       |              |     |
theoverallsystemcost.Besides,Abikoetal.developamulti-
| Sec. III | describes | the | system | model | used | for our | analysis. |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | ------ | ----- | ---- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
agentarchitecturetodistributeradioresourceblocksandprove
| Sec. IV    | recalls       | the fundamentals |           |          | of DRL       | and describes | our         |                  |               |               |                   |            |         |             |          |
| ---------- | ------------- | ---------------- | --------- | -------- | ------------ | ------------- | ----------- | ---------------- | ------------- | ------------- | ----------------- | ---------- | ------- | ----------- | -------- |
|            |               |                  |           |          |              |               |             | its adaptability |               | to a variable | number            | of         | slices  | [27].       | Finally, |
| learning   | architecture. |                  | Sec. V    | presents | the          | resource      | allocation  |                  |               |               |                   |            |         |             |          |
|            |               |                  |           |          |              |               |             | the authors      | of            | [28] propose  | a                 | DRL system |         | to balance  | the      |
| strategies | used          | a benchmark.     |           | Sec.     | VI describes | the           | simulation  |                  |               |               |                   |            |         |             |          |
|            |               |                  |           |          |              |               |             | communication    |               | requirements  | of                | eMBB       | and     | URLLC       | slices;  |
| scenario   | and           | presents         | the       | results  | of our       | research.     | Finally,    |                  |               |               |                   |            |         |             |          |
|            |               |                  |           |          |              |               |             | particularly,    | an            | Actor-Critic  | algorithm         |            | is used | to schedule |          |
| Sec. VII   | concludes     |                  | the paper | with     | a recap      | of            | the lessons |                  |               |               |                   |            |         |             |          |
|            |               |                  |           |          |              |               |             | URLLC            | transmissions |               | without degrading |            | the     | performance | of       |
| learned    | and some      | ideas            | for       | future   | work.        |               |             |                  |               |               |                   |            |         |             |          |
|            |               |                  |           |          |              |               |             | the eMBB         | flows.        |               |                   |            |         |             |          |
|            |               |                  |           |          |              |               |             | Despite          | the           | growing       | interest          | in this    | domain, | many        | open     |
II. RELATEDWORK questions still need investigation. Most of the aforementioned
Future telecommunication systems will be characterized approaches,indeed,considerthatitisalwayspossibletoman-
by the progressive softwarization of network functionalities age the network in a centralized fashion, without addressing
and increase of service heterogeneity. To deal with such a theproblemofoptimizedistributedsystemswherethenetwork
scenario, it is necessary to design new strategies enabling status is only partially observable. For instance, the authors
the fully sharing of physical and virtual resources by means of [23] assume that the slice requirements can be always
of the NS paradigm. In this respect, the authors of [13] satisfied by the network infrastructure, which is seen as an
analyze a 5G scenario with end-to-end slices contending for unique element with an aggregated rate, computational and
the virtual resources offered by data centers, proposing a storage capacity. Instead, the work presented in [26] focuses
fully distributed algorithm to maximize system performance. on the allocation of virtual network functions, considering a
In [14], Leconte et al. design a NS model where multiple standardized system that can be hardly be adapted to different
traffic flows share network bandwidth and cloud processing scenarios.Besides,theauthorsof[28]analyzethedistribution
units;hence,theyimplementtheAlternatingDirectionMethod of the radio frequency blocks in the access network, without
of Multipliers [15] to determine the best resource allocation takingintoaccounttheinteractionbetweentheotherelements
scheme. In [16] it is adopted a similar approach in a system ofthenetwork.Finally,neitheroftheaboveworksthoroughly
where multiple network operators share both licensed and investigate the adaptability of the proposed solutions to dif-
unlicensedspectrum.Besides,theauthorsof[17]focusonthe ferent network topologies, which is a key aspect of slice

orchestration. processed in the computing facilities, and expressed it in bits
The great heterogeneity of future telecommunication sys- per second [bps].
tems requires the implementation of more flexible strategies, In our framework, the time is discretized in timeslots of T
which enable the coexistence of multiple services and can seconds,andtheinformationflowparameterscanchangeonly
promptly adapt to new resource demands. A very promis- slot by slot. We write r (t) to indicate the resource demand
φ
ing solution is to exploit hierarchical reinforcement learning, vector of φ during timeslot t, while we write ˆr (t)=[ηˆ (t),
φ φ
whichisanapproachthathasnotyetbeenfullyinvestigatedin cˆ (t), mˆ (t), δˆ (t)], to indicate the resources assigned to φ
φ φ φ
this context. Moreover, the transfer learning paradigm can be during timeslot t. Note that r (t) is determined by the slice
φ
used to improve the training of the learning agents [29], thus class σ that φ belongs to, while ˆr (t) is determined by the
φ
increasing the system adaptability to multiple scenarios. Our resource allocation strategy.
work develops along with these directions, with the final aim As mentioned, we consider two different slice classes:
ofdesigningafullyscalableDRLsystemthatcanbeseparated eMBB(e)andURLLC(u).Inparticular,givenΦ (i.e.,theset
e
into smaller units, capable of both acting autonomously and oftheeMBBflows)andΦ (i.e.,thesetoftheURLLCflows),
u
cooperating to orchestrate network resources under multiple we have Φ=Φ ∪Φ and Φ ∩Φ =∅. Hence, all the infor-
e u e u
working conditions. mation flows belonging to the same slice σ shares the same
performance function F (·), i.e., ∀φ∈Φ , F (·)=F (·). In
σ σ φ σ
general, F (·) depends on both r and ˆr, and returns a value
III. SYSTEMMODEL σ
in [0,1], where 1 means that the SLA has been completely
Inthissection,wemodelaNSenvironmentwheremultiple
fulfilled. We assume that F (·) is a combination of four
σ
information flows contend for the same physical and virtual
functions f (·), each of those returns the flow performance
σ
network resources. We adopt a fluid traffic model, where the
for a specif resource ρ∈{δ,η,c,m}. Particularly, f (·) takes
σ
traffic through a link is viewed as a fluid stream of data with
as input x , which is the level of fulfillment of the flow
ρ
a certain flow rate. In particular, we assume that network
demand,andcantakeadifferentshapeaslongasf (x)=1∀
σ
slices are organized hierarchically, so that more flows can
x≥1,i.e.,theperformanceismaximizedanytimetheallotted
be compound into an aggregate slice, possibly managed by a
resource equals or exceeds the request.
differenttenant.Theresultingframeworkisthusveryflexible,
and can model the interactions among slice tenants, and with
slice brokers. For the reader convenience, we report the main
1.0
parameters of our model in Tab. I.
0.8
A. Slice Model
0.6
Inoursystem,wedefineanetworksliceasanaggregationof
informationflowswithsimilarbehaviorsandrequirements.We
denotebyΣthesetincludingallthedifferentclassesofslices, 0.4
and by Φ the set including all the information flows. Given
σ ∈ Σ, we indicate by Φ the set of all information flows 0.2
σ
belonging to σ. Each information flow φ∈Φ is characterized
0.0
by a tuple of parameters, namely:
• theflowendpointsE φ =((cid:15)i φ ,(cid:15)e φ ),whichcorrespondtothe 0.0 0.2 0.4 0.6 0.8 1.0
network nodes where the users’ data enter/exit the slice x
and usually correspond to base stations, edge routers of
autonomous systems, or servers;
• theresourcedemandvector r φ =[η φ ,c φ ,m φ ,δ φ ],whose
elements are the requirements in terms of throughput
(η), computational power (c), memory capacity (m), and
delay (δ) of the flow;
• the performance function F φ (·), which describes the per-
formance of the considered information flow according
to the level the SLA is fulfilled.
We assume that E , F (·) and δ do not change for the
φ φ φ
whole duration of flow Φ, while η , c and m may change φ φ φ
in time depending on the dynamic of the data source. Note
that the throughput is measured in bits per second [b/s],
the memory capacity in bits [b], and the delay in seconds
[s]. Finally, we assume the computational requirements are
somehow related to data generated by the source. We hence
definethecomputationalpowerasthespeedatwhichdataare
)x(σf
eMBB
URLLC
Fig. 1: Resource performance function.
For what concerns the eMBB slice, we assume
(cid:18) (cid:19) (cid:18) (cid:19)
δ (cid:88) ρˆ
F (r,ˆr)=α f + α f (1)
e δ e δˆ ρ e ρ
ρ∈{η,c,m}
where α ,α ,α , and α are non negative and add up to 1. η c m δ
Hence,F (·)istheweightedsumoff (x ),whichisaconvex e e ρ
function defined as
(cid:40)
β x+β x2+β x3, x∈[0,1); f (x)= 1 2 3 (2)
e
1, x≥1.
Particularly, β , β and β are scalar parameters ensuring that
1 2 3
f (·) is concave and monotonic increasing for x ∈ [0,1].
e
The smooth and concave shape of f (·) shown in Fig. 1
e
embodiestheflexibilityoftheSLAforeMBBservices.Hence,

TABLE I: Model parameters.
Parameter Description Parameter Description Parameter Description
φ∈Φ Informationflow (cid:15)i φ ,(cid:15)e φ Flowendpoints B l Linkratecapacity[bps]
σ∈Σ Sliceclass r φ Flowdemandvector C n c Nodecomputationalcapacity[bps]
l∈L Link ρ φ Resourcerequiredbyφ C n m Nodememorycapacity[b]
n∈N Node ρˆ φ Resourceassignedtoφ bi l,φ Inputflowrate[bps]
η Throughput[bps] fσ(·) Resourceperformancefunction bo
l,φ
Outputflowrate[bps]
c Computationalpower[bps] Fσ(·) Flowperformancefunction τn Noderoutingdelay[s]
m Memorycapacity[b] Ω Systemutility D l,φ Dataofφqueuedinl[b]
δ Delay[s] b l,φ Bitrateassignedbyltoφ[bps] τ l q ,φ Queuingdelayofφinl[s]
t Discretetime c n,φ Computationassignedbyntoφ[bps] τ l τ ,φ Transmissiondelayofφinl[s]
T Timeslotduration[s] m n,φ Memoryassignedbyntoφ[b] τ l p Linkpropagationdelay[s]
we assume that the quality of experience of the slice users B. Network Model
degradesrathergraciouslywhentheSLAisviolated,asinthe
case of video-streaming applications [30].
Our model is based on two different network elements,
Conversely, URLLC flows have very strict requirements
namely node and link, as detailed below.
that, if infringed, cause the sudden degradation of the re-
lated services. This is intended to represent the fragility of
applications such as robotic surgery, which do not tolerate • We distinguish two types of nodes: access nodes are
any increase in the communication delay. For this reason, the located at the network edge and connect users with the
performance function for this class of services is defined as rest of the network; core nodes are located in the core
the product of step functions f (·) (shown in Fig. 1): of the network and forward the aggregated data flows
u
coming from the access nodes. Each node n is equipped
(cid:18) (cid:19) (cid:18) (cid:19)
F u (r,ˆr)=f u δ δˆ × (cid:89) f u ρ ρˆ , (3) w C i m th r a es c o e u r r t c a e in s, a w m h o ic u h nt m o a f y c d o i m ff p e u r t b a e ti t o w n e a e l n C a n c cc a e n s d sa m n e d m c o o r r y e
ρ∈{η,c,m} n
nodes.
where
(cid:40) 0, x∈[0,1); • Wecalllinkanyconnectionlbetweentwodifferentnodes
f (x)= (4) of the network (fronthaul or backhaul). This element
u
1, x≥1.
is provided with a certain bit rate B to support the
l
In this case, F (·) drops to zero as soon one single resource communications between the connected nodes.
u
requirement is not met.
We remark that our system can be easily extended by Fromnowon,wedenotebyN andLthesetofnetworknodes
definingothersliceswithdifferentperformancefunctions.Par- and links, respectively. Particularly, N can be partitioned into
ticularly, the slice broker can take advantage of the generality N a , which includes the access nodes, and N c , which includes
ofoursystemand,forinstance,changethecompositionofthe the core nodes.
slice set, in order to address the requirements of new tenants
In our model, each information flow φ ∈ Φ is initialized
in different scenarios.
betweentwoaccessnodesandpassesthroughacertainnumber
Given the functions F (·) of all slices σ ∈ Σ, the system
σ of core nodes and links. Let Φ and Φ be the set of
l n
utility is obtained as
information flows that cross link l ∈ L and node n ∈ N,
|Φ | |Φ | respectively.Weassumethateachflowφalwaysgoesthrough
Ω= e Ω + u Ω , (5)
|Φ| e |Φ| u the same network elements from (cid:15)i to (cid:15)e, which implies that
φ φ
Φ and Φ do not change in time ∀ l∈L, n∈N.
where l n
1 (cid:88)
Ω = F (r ,ˆr ), σ ∈Σ, (6) We observe that, in general, slices can be activated and
σ |Φ | σ φ φ
σ deactivated on-demand, thus varying the number of flows in
φ∈Φσ
the network. Nonetheless, once established, the path of an in-
and|X|representsthecardinalityofX.WeobservethatF (·)
σ formation flow is generally maintained for the whole duration
always takes values in [0,1], so that we also have Ω∈[0,1].
oftheconnection,unlesssomelinksbecomeunavailableorthe
Besides, we can define the system utility for a specific type
communication end points change. In this case, the resource
of resource ρ as
allocation framework will react as if the flow was interrupted
Ωρ = |Φ e | Ωρ+ |Φ u | Ωρ, (7) an a new one was started along the new path. We assume that
|Φ| e |Φ| u such events are rare and do not impact significantly on the
where performance of the proposed scheme.
Ωρ σ = (cid:40) |Φ 1 1 σ| (cid:80) (cid:80) φ∈Φσ f f σ ( ( ρ ρˆ / /ρ ρˆ ) ) , , o if th ρ er = wh δ i ; se; (8) b l,φ G o iv f e t n he a l l i i n n k k b l i ∈ tr L at , e e B ac l h .S fl i o m w ila φ rl ∈ y, Φ ea l c g h et n s o a d s e si n gn ∈ ed N a a p s o s r i t g io n n s
|Φσ| φ∈Φσ σ toφanamountc
n,φ
andm
n,φ
ofitscomputationalandstorage
and, as before, σ ∈Σ. resources. Consequently, any resource allocation pattern must

comply with the following feasibility conditions: Instead, ττ (t) is the reciprocal of bo (t), i.e.,
l,φ l,φ
(cid:88)
b ≤B , ∀ l∈L; (9) 1
l,φ l τt (t)= . (19)
φ∈Φl l,φ bo
l,φ
(t)
(cid:88)
ρ ≤Cρ, ∀ n∈N,ρ∈{c,m}. (10)
n,φ n Finally, τp is a positive and constant value that depends on
φ∈Φn
the physi
l
cal characteristic of the communication link. We
Givenacertainallocationofnetworkresources,wewantto highlight that, despite we consider a discrete time-frame, δˆ
φ
compute ˆr , ∀ φ∈Φ. We denote by N and L the ordered
φ φ φ is a continuous value.
set of network nodes and links crossed by φ, respectively.
Our aim is to determine the best resource allocation to
In particular, the first and the last element of N constitute
φ maximize the system utility as given in (5). Mathematically,
the flow endpoints. We assume that the computational and we want to determine ˆr , b , c , m , bi , bo , τq , and
memory requests of a flow φ ∈ Φ can be distributed among ττ , ∀ φ ∈ Φ, n ∈ N φ , l l ∈ ,φ L n t , h φ at m n a ,φ xim l i , z φ e Ω l, , φ un l d ,φ er the
all the nodes in N , so that l,φ
φ constraints given in (9)-(19).
ρˆ = (cid:88) ρ , ∀ ρ∈{c,m}. (11) The many constraints and the non-convexity of Ω make
φ n,φ
the problem very complex to solve. In particular, the optimal
n∈Nφ
solution can be determined only if a central controller is
To determine the throughput ηˆ , instead, we need to con-
φ provided with all the system variables at any timeslot. Then,
sidertheoutputflowratebo (t)attimetfromeachlinkl∈L.
l,φ conventional optimization tools or meta heuristic techniques
Indeed,thethroughputcorrespondstotheoutputratefromthe
can be used to identify the best resource allocations scheme.
last link λ along the path:
However, the first may converge on local maxima, while the
ηˆ (t)=bo (t). (12) latter can be unable to find a solution within a reasonable
φ λ,φ
time frame. If the resource demands of the information flows
In turn, bo (t) depends on both the bit rate b (t) assigned
l,φ l,φ evolve quickly in time, a valuable approach is to implement
to φ by l, the input flow rate bi (t) from the upstream link,
l,φ distributed control algorithms that can promptly take new
and the amount of data of φ queued at node n at the end of
actions, albeit with a partial view on the overall network. In
the previous slot, which is denoted by D (t−1). The input
l,φ particular, the DRL paradigm is particularly suitable for this
flow rate bi (t) is given by
l,φ problem since it can provide high-performance solutions to
(cid:40)
bo (t), if (cid:96) is the upstream link of l in L ; carry our complex control tasks also when the environment is
bi (t)= (cid:96),φ φ
l,φ η (t), if l is the first link in L . partially observable.
φ φ
(13)
The output flow rate bo (t) is then given by the minimum IV. LEARNINGSTRATEGY
l,φ
betweentheallocatedrateb (t)andthesumoftheincoming
l,φ In order to efficiently orchestrate communication resources
and queued traffic, i.e.,
in a NS scenario, we develop a distributed architecture based
(cid:26) (cid:27)
bo (t)=min b (t), D l,φ (t−1) +bi (t) . (14) on multiple learning units, named local controllers, that col-
l,φ l,φ T l,φ laborate to maximize the overall system utility given by (5).
In the rest of the section, we will recall the main principles
The variable D (t) is set to 0 for any time t before the
l,φ
of DRL, and present the framework used to train the learning
initialization of the flow, and then it is updated as
agents of our architecture.
D (t)=max (cid:8) 0,D (t−1)+T(bi (t)−b (t)) (cid:9) .
l,φ l,φ l,φ l,φ
(15)
A. Deep Reinforcement Learning
Note that the value of D increases as the assigned rate b
l,φ l,φ
is lower than the input rate bi . The RL paradigm is one of the main branches of ML.
l,φ
For what concerns the delay experienced by φ, we have Particularly, RL does not solely aim at solving classification
δˆ (t)= (cid:88) τ + (cid:88) τ (t), (16) or regression problems, but it enables the development of
φ n l,φ complex strategies to maximize the long-term performance of
n∈Nφ l∈Lφ
a target system [31]. Moreover, RL algorithms do not need
where τ n is a positive value representing the delay due to to have labeled data to carry out the training phase, but they
routing operations at node n, and it is assumed constant over interact with a learning environment where agent actions are
time. Instead, τ l,φ (t) is computed as associated to specific rewards.
τ (t)=τq (t)+ττ (t)+τp, (17) InaRLscenario,thetargetsystemismodeledasaMarkov
l,φ l,φ l,φ l
Decision Process (MDP), which is a powerful mathematical
where τq , ττ , and τp represent the queuing, transmission,
l,φ l,φ l tool used to represent decision-making problems [32]. This
and propagation delays of φ through link l, respectively. In
framework requires to define a state space S of the environ-
particular, τq (t) is the average queuing time of a bit in l
l,φ ment, an action space A of the learning agent, and a reward
during t, and is given by (see the Appendix) function r : S ×A → R. During any timeslot t, the learning
2D (t−1)−T(bo (t)−bi (t)) agent observes the system state s ∈ S, performs an action
τ l q ,φ (t)= l,φ 2b (t l, ) φ l,φ . (18) a t ∈A and receives a reward r t ∈ t R. Hence, the future state
l,φ

s depends uniquely on the previous state s and the agent in state s . Conversely, the actor is trained to minimize the
t+1 t t
decision a . function
t
The agent chooses new action according to a policy π :
L (s ,a )=−∇ logπ (s ,a )A(s ,a )2−κH(π ), (24)
S ×A → [0,1], where π(s,a) is the probability to take the a t t θ θ t t t t θ
action a when the state s is observed. The aim of any RL where ∇ is the gradient with respect to θ, π (s ,a ) is the
θ θ t t
algorithm is to determine a policy that maximizes the system probabilityoftakingactiona instates ,H(π )istheentropy
t t θ
long-term reward, which is of π , and κ is a scalar value. As suggested in [35], the
θ
actor loss function depends linearly on the policy entropy
∞
R= (cid:88) λtr , (20) H(π θ ). Particularly, we can promote the exploration of the
t
action space by increasing κ since, in such a case, the actor
t=0
gain benefits to take random actions. Instead, as κ → 0, the
where λ ∈ [0,1] is the so-called discount factor. Particularly,
actorwillchooseactionsthatareexpectedtobringthehighest
if λ → 0, the algorithm favors the actions that can acquire
reward according to the current experience.
high reward in a short time; instead, if λ → 1, the algorithm
WehighlightthatA2Cenablestoconsidercontinuousaction
aims at determining the actions that bring more benefit in the
spaces: this is not possible with traditional Reinforcement
future.
learning algorithms (e.g., Q-Learning) that, instead, can only
Given a policy π, a RL algorithm associates each possible take actions from discrete sets. Besides, the A2C algorithm
state s with a value V π (s). The function V π (·) is called state supports an online training phase and, consequently, allows
value function and represents the expected cumulative reward the agents to continuously refine the target policy while it is
that is achieved following the actions of π from state s. In beingusedintherealsystem.Therefore,theslicebroker does
other words, we have not need to train a new system from scratch every time the
network conditions change since the policy will dynamically
V (s)=E[R|s,π]. (21)
π adapt to the new conditions as time passes by.
As the agent explores the learning environment, the values of
V (s) and the policy itself are updated. In this perspective,
π
the optimal policy π∗ provides the maximum value of V (s)
π Node
∀ s∈S, i.e., Training controllers
Link
manager V (s)=maxV (s), ∀ s∈S. (22) controllers
π∗ π π
Ifthestateandactionspacesgettoocomplex,conventional
RLapproachesfailtodeterminetheoptimalpolicybecauseof
the curse of dimensionality [33]. To address such a problem,
eMBB
the DRL paradigm allows to approximate the state value
agents
function and the optimal policy by deep NNs. In particular,
DRL algorithms are capable of handling continuous state and
URLLC
action spaces, which means that |S×A|→∞. agents Network
B. Learning Architecture
In this work, we adopt an Actor Critic (AC) approach [34],
which involves the learning of the optimal policy by two
different units. The first is named actor and approximates the
optimal policy π , parameterized by θ; the latter is named
θ
critic and approximates the value function V , parameterized
γ
by γ. Hence, the actor is trained to compute the action a that
t
thepolicyπ takesinastates ;thecriticistrainedtocompute
θ t
the expected long term reward that is obtained following the
policy π from s .
θ t
To carry out the system training, we exploit the Advantage
ActorCritic(A2C)algorithm,whichhasshowntoprovidesta-
ble DRL solutions in very complex scenarios [35]. The critic
is trained to minimize the function L (s ,a ) = A(s ,a )2,
c t t t t
where
A(s ,a )=r +λV (s )−V (s ). (23) t t t γ t+1 γ t
Particularly, the function A:S×A→R is called advantage
and returns the reward gain obtained by choosing action a
t
BBMe wolf CLLRU wolf
BBMe
wolf
BBMe
wolf
CLLRU
wolf
Agent
training
•Controller
deploym
en
t
•
Γe m
Γe c ΓΓe ccΓΓe m ΓΓu ccΓΓu m
Γe b
Γu m
ΓΓe b ΓΓe b ΓΓu b
•Distributed
Γu c execution
Γu b
Fig. 2: Learning Architecture.
Our learning architecture (shown in Fig. 2) provides a
different controller for each information flow and network
element. From an operational point of view, the total number
of local controllers depends on the network topology and
the cardinality of Φ. Practically, the local controllers are all
replicas of 3×|Σ| learning agents. During the training phase,
we design a tuples of agents (Γb, Γc, Γm) for each different
σ σ σ
sliceσ ∈Σ:theagentΓb istrainedtoorchestratethebitrateof
σ
each information flow φ∈Φ in each link l∈L; instead, Γc
σ σ
andΓmaretrainedtoorchestratethecomputationandmemory
σ
resources of each information flow φ ∈ Φ in each node σ
n∈N.Practically,thetrainingphaseisperformedbyacentral
entity, named training manager, which collect the system
information and update the learning architecture accordingly.
Then, copies of Γb, Γc, and Γm will be instantiated in each σ σ σ
network element crossed by any flow φ∈Φ .
σ
According to the A2C algorithm, each learning agent is
composedbytwounits,i.e.,theactorandthecritic,whichare

implemented by means of NNs. Particularly, we consider an t−1. As before, the node controller takes s (t) and sρ (t)
φ n,φ
architecture with two hidden layers and the Rectifier Linear as input and returns ρ∗ (t), with ρ ∈ {c,m}, which is the
n,φ
Unit (ReLU) as activation function [36]. The output of the amount of computational (or memory) capacity demanded by
actor is the amount ρ∗ of resources that the local controller φ in n during t.
demands,whilethatforthecriticistheexpectedfuturereward.
The size of the NN input varies according to the type of D. Reward Function
resources that has to be managed, as explained in the next
In accordance to the RL paradigm, we need to define a
subsection.
reward function r(·) that represents the benefit generated by
each possible state-action pair of the policy. In particular,
C. Observations and Actions
to maximize the overall utility, each local controller should
In our system, each local controller has full knowledge of demand enough resources to maximize the performance of
the element where it is installed, while it has a limited view the flow φ it is in charge of, without subtracting too many
on the network, which implies that the system state is only resources to the other flows. In our system, given a controller
partially observable [37]. Let us consider a local controller associated to a link l ∈ L and a flow φ ∈ Φ , the reward at
l
managing the rate resources of a flow φ in a link l. At the time t is given by
beginning of each timeslot, such a controller is provided with (cid:32) (cid:18) η (t) (cid:19) (cid:32) δˆ (t) (cid:33)(cid:33)
twovectorsrepresentingthestatusoftheinformationflowand r (t)=γ f φ +f φ +
l,φ 0 σφ ηˆ (t) σφ δ (t)
the network element that is associated with. φ φ
tim T e h s e lot fi t rs : t vector gives the state of φ at the beginning of |Φ γ 1 | (cid:88) (cid:32) f σψ (cid:18) η ηˆ ψ ( ( t t ) ) (cid:19) +f σψ (cid:32) δ δˆ ψ ( ( t t ) ) (cid:33)(cid:33) , (28)
s φ (t)=[r φ (t),ˆr φ (t−1)], (25) l ψ∈Φl ψ ψ
wherer (t)andˆr (t−1),definedinSec.III,aretheresources where σ φ is the slice class that φ belongs to, while γ 0 and
φ φ
γ are positive scalar values. In particular, γ weights the
requested and granted by φ at the beginning of timeslot t and 1 0
t−1,respectively.Weobservethatˆr (t−1)canbecomputed throughputanddelayperformanceofflowφ,whileγ 1 weights
φ
the average throughput and delay performance of all the other
only knowing the aggregate amount of network resources
flows crossing link l.
assigned to φ by the network elements of its routing path.
Similarly, a controller assigned to a node n and a flow φ is
Therefore, s (t) needs to be shared among all the controllers
φ
rewarded according to
assignedtoφatthebeginningofeachtimeslott.However,the
sizeofs φ (t)isnegligiblewithrespecttotheraterequirements rρ (t)=γ f (cid:18) ρ φ (t) (cid:19) + γ 1 (cid:88) f (cid:18) ρ ψ (t) (cid:19) , (29)
oftheslices,and,therefore,canbetransmittedwithintheuser n,φ 0 σφ ρˆ (t) |Φ | σψ ρˆ (t)
φ n ψ
data plane of φ, without degrading the performance of our ψ∈Φn
system. where ρ∈{c,m}, while the scalar values γ 0 and γ 1 have the
The second vector provides the state of the rate resources same role as before.
of φ in l at the beginning of timeslot t: Therefore, the reward function consists of the weighted
sum of two terms: the first reflects the performance of the
s (t)=[B ,τ (t−1),D (t−1),b∗ (t−1),
l,φ l l,φ l,φ l,φ (26) flow targeted by the agent, while the second represents the
b (t−1),be(t−1),bu(t−1)],
l,φ l l aggregate performance of all flows that share that network
where bσ(t − 1) is the aggregate rate demanded in l by element. With such a mixed reward function, the agent will
l
all the flows of class σ during timeslot t − 1, while the hence attempt to improve the quality of the targeted flow, but
other parameters were defined in Sec. III. We highlight that without unduly penalizing other flows.
this information is provided by the considered link l and,
consequently, the knowing of s (t) does not require any V. BENCHMARKSTRATEGIES
l,φ
additional communication within the network. Hence, at the Inthissection,wedescribetheresourceallocationstrategies
beginning of timeslot t, the link controller takes s (t) and that we use as benchmark for our model. The first is an em-
φ
s (t) as input and returns b∗ (t), which is the bit rate piricalalgorithm,whichtriestofairlyallocatecommunication
l,φ l,φ
demanded by φ in l during t. andprocessingresourcesineachnetworkallocation.Thelatter
When considering a controller associated to a node n and is based on meta-heuristic optimization and performs a static
a flow φ we use the same approach and, depending on the allocation of network resources.
resource ρ ∈ {c,m} we want to allocate, we substitute (26)
withsc (t)orsm (t),whicharethestatesofthecomputation A. Empirical Strategy
n,φ n,φ
and memory resources assigned to φ by node n. In particular,
Similarlytoourapproach,theempiricalstrategyimplements
sc (t) or sm (t) are defined as
n,φ n,φ a distributed resource allocation scheme. At the beginning of
sρ (t)=[Cρ,ρ∗ (t−1),ρ (t−1), timeslot t, each flow φ crossing link l demands a bit rate
n,φ n n,φ n,φ (27) sufficient to both satisfy the current throughput requirement
ρe(t−1),ρu(t−1)],
n n and transmit any buffered data, i.e.,
where ρσ(t − 1) is the aggregate amount of resource ρ
n D (t−1)
demandedinnodenbyalltheflowsofclassσ duringtimeslot b∗ l,φ (t)=η φ (t)+ l,φ T . (30)

For what concerns the computation and memory allocation,
each flow φ distributes its requests among the nodes along its
path, proportionally to their capacity. More specifically, the
amount of resources required to node n is equal to
ρ∗ (t)=χ ρ (t), (31)
n,φ n,φ φ
where ρ∈{c,m}, and χ is computed as
n,φ
0 1020304050
Cρ Timeslot
χ = n . (32)
n,φ (cid:80) Cρ
k∈Nφ k
Wehighlightthat,tocomputeχ ,itisnecessarytoknown
n,φ
the computation and storage capacities of each node n∈N .
φ
Such an information is not provided to the local controllers
of the DRL strategy. Hence, the empirical strategy has an
advantagewithrespecttoourlearningframeworksinceituses
informationthatisgenerallynotavailableinafullydistributed
approach.
We observe that, either using the empirical or the DRL
strategy, network elements may be not able to satisfy all the
requeststheyreceive.Particularly,thetotalaggregatedamount
of resources that is demanded to a link l (or a node n)
may exceed its overall capacity. Hence, we need to map the
demandedresourcesb∗ ,c∗ ,m∗ totheassignedresources
l,φ n,φ n,φ
b , c , m , ∀ l∈L, n∈N, ensuring that the feasibility
l,φ n,φ n,φ
constraints (9) and (10) are always satisfied.
Let us consider a link l ∈L during a timeslot t. If the total
amount of resources demanded at the link is lower than B ,
l
the feasibility constraints are already met: consequently, we
can set b (t) = b∗ (t). In the other case, the rate b (t)
l,φ l,φ l,φ
assigned by the link to each flow φ ∈ Φ is proportional to
l
the flow demand b∗ (t):
l,φ
(cid:40) (cid:41)
B
b (t)=b∗ (t)min 1, l . (33) l,φ l,φ (cid:80) b∗ (t)
ψ∈Φl l,ψ
Using the same principle for the computational and memory
resources, we can write
(cid:40) (cid:41)
Cc
c (t)=c∗ (t)min 1, n , (34)
n,φ n,φ (cid:80) c∗ (t) ψ∈Φn n,ψ
and
(cid:40) (cid:41)
Cm
m (t)=m∗ (t)min 1, n . (35)
n,φ n,φ (cid:80) m∗ (t) ψ∈Φn n,ψ
B. Static Strategy
Meta-heuristic techniques have been shown to determine
theoptimalsolutionofhighlycomplexoptimizationproblems
with non-convex constraints [38]. In our system, a Genetic
Algorithm(GA)maybeusedtoapproximatethebestresource
allocation pattern, thus outperforming both the DRL and
empirical strategies. However, meta-heuristic algorithms are
basedonarandomizedsearchofthetargetsolutionandrequire
an extremely long calculation time, which makes it unfeasible
to execute them at each timeslot. At the same time, it is
reasonable to exploit meta-heuristic techniques if the resource
requirements do not vary in time.
LRD
0 1020304050
Timeslot
laciripmE
0 1020304050
Timeslot
citatS
eMBB URLLC
Fig. 3: Link resource allocation.
In the static strategy we consider in this work, the network
resources are statically divided among the different slices.
Practically, each traffic flow φ is assumed to have fixed re-
quirements,correspondingtotheaverageamountofresources
it demands, i.e., ra. Hence, a GA is used to determine the
φ
optimalresourceallocationpatternundersuchconditions[39].
We observe that, using the static strategy, the values of
b ,c ,m ∀ φ∈Φ, l ∈L, n∈N are maintained fixed.
l,φ n,φ n,φ
Inotherwords,thevariabilityofinformationflowsisnottaken
into account, and the performance of each flow is expected
to deteriorate as soon as its requirements exceed the average
values. This is a big issue, especially for the URLLC slice,
whose performance function suddenly drops if any resource
requirements is not satisfied.
To better highlight the characteristics of the benchmark
strategies, we analyze the bit rate allocation in a network link
during a period of 50 timeslots. In Fig. 3, we represent the
share of link resources assigned to the eMBB and URLLC
services, using the different strategies. In particular, we con-
siderascenariowherethecapacityislowerthantheaggregate
resource demand, which means that all the strategies fully
exploit the link rate. As expected, GA distributes network
resources in a static fashion: the bitrate assigned to the
different slices does not vary in time. Instead, the empirical
algorithmisabletoadapttotheslicerequirementsand,hence,
thebitratedistributionchangesateachtimeslot.AlsotheDRL
strategyfollowsadynamictrendbutitassignsalargeramount
of resources to the URLLC services than the benchmarks.
VI. SIMULATIONSETTINGANDRESULTS
In this section, we first describe the scenarios where our
algorithms are tested as well as the setting of our simulations.
Then,weinvestigatetheperformanceofourDRLarchitecture
against the benchmark strategies and under different work-
ing conditions. Finally, we show how the transfer learning
paradigm can be used to further improve the performance of
our system.
A. Setting
We consider three different network scenarios, named
Dumbbell(D),Triangle(T),andPyramidNetwork (P),whose
topologies are reported in Fig. 4. In all the cases, the number
of information flows in the network is N ∈ {2,...,6}. The
Φ
capacities of each network element are fixed; specifically, we
set B = 50 Gbps, Cc = 60 Gbps and Cm = 60 Gb for the
l n n

|     |     |     |     |     |     |     | scenarios | where           | there | is a lack | of       | network | resources, | or to      |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | ----- | --------- | -------- | ------- | ---------- | ---------- |
|     |     |     |     |     |     |     | estimate  | the reliability |       | of a      | specific | set of  | network    | slices. In |
thefuture,wewillinvestigatecall-admissioncontrolstrategies
|              |     |         |      |              |     |              | to avoid    | system   | overloading. |            |                |          |           |         |
| ------------ | --- | ------- | ---- | ------------ | --- | ------------ | ----------- | -------- | ------------ | ---------- | -------------- | -------- | --------- | ------- |
|              |     |         |      |              |     |              |             | TABLE    |              | III: Agent | architectures. |          |           |         |
|              |     |         |      |              |     |              |             |          | Γb           |            |                | Γc       |           | Γm      |
|              |     |         |      |              |     |              |             |          | σ            |            |                | σ        |           | σ       |
|              |     |         |      |              |     |              | Parameter   | Actor    |              | Critic     | Actor          | Critic   | Actor     | Critic  |
| (a) Dumbbell |     | Network | (D). | (b) Triangle |     | Network (T). |             |          |              |            |                |          |           |         |
|              |     |         |      |              |     |              | Inputsize   |          | 11           | 11         | 7              | 7        | 7         | 7       |
|              |     |         |      |              |     |              | Activation  | ReLU     |              | ReLU       | ReLU           | ReLU     | ReLU      | ReLU    |
|              |     |         |      |              |     |              | Hiddensize  |          | 12           | 12         | 8              | 8        | 8         | 8       |
|              |     |         |      |              |     |              | Activation  | ReLU     |              | ReLU       | ReLU           | ReLU     | ReLU      | ReLU    |
|              |     |         |      |              |     |              | Hiddensize  |          | 6            | 6          | 4              | 4        | 4         | 4       |
|              |     |         |      |              |     |              | Activation  | Linear   |              | Linear     | Linear         | Linear   | Linear    | Linear  |
|              |     |         |      |              |     |              | Outputsize  |          | 1            | 1          | 1              | 1        | 1         | 1       |
|              |     |         |      |              |     |              |             |          |              |            |                |          | N         | = 5·104 |
|              |     |         |      |              |     |              | To train    | the      | learning     | agents,    | we             | generate | train     |         |
|              |     |         |      |              |     |              | independent | episodes |              | using the  | same           | network  | topology. | Each    |
|              |     |         |      |              |     |              | episode     | lasts N  | =50          | timeslots  | of             | T =0.1   | seconds.  | At the  |
slot
|     |     | (c) Pyramid |     | Network | (P). |     |           |         |          |     |        |        |                |     |
| --- | --- | ----------- | --- | ------- | ---- | --- | --------- | ------- | -------- | --- | ------ | ------ | -------------- | --- |
|     |     |             |     |         |      |     | beginning | of each | episode, | a   | random | number | of information |     |
flowsisgenerated;then,eachflowφisassociatedwithastatic
|     |     | Fig. 4: | Network | topologies. |     |     |                       |     |     |                |     |        |        |            |
| --- | --- | ------- | ------- | ----------- | --- | --- | --------------------- | --- | --- | -------------- | --- | ------ | ------ | ---------- |
|     |     |         |         |             |     |     | route interconnecting |     |     | its endpoints. |     | Hence, | at the | end of the |
episode,theA2Calgorithmisusedtotrainthelearningagents
core nodes, Cc = 20 Gbps and Cm = 20 Gb for the access Γb, Γc, Γm, ∀ σ ∈ Σ. We exploit the Adaptive moment
|               | n   |             |      | n    |           |             | σ σ        | σ      |           |     |             |     |        |          |
| ------------- | --- | ----------- | ---- | ---- | --------- | ----------- | ---------- | ------ | --------- | --- | ----------- | --- | ------ | -------- |
| nodes. Hence, |     | we consider | that | most | computing | and storage |            |        |           |     |             |     |        |          |
|               |     |             |      |      |           |             | estimation | (Adam) | algorithm |     | to optimize |     | the NN | weights, |
resources are concentrated in the core network. Concerning considering ζ = 10−5 and ζ = 10−5 as learning rates of
|     |     |     |     |     |     |     |     | a   |     |     | c   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the delay, we assume that τp = 0.1 ms, ∀ l ∈ L, and the actor and the critic, respectively. We summarize the main
l
τ n =0.001ms,∀n∈N.Althougharbitrary,thesevaluesare settingsofthelearningarchitecturesinTab.III,whiletheother
well-aligned with the features of modern network elements. simulation parameters are given in Tab. IV
| To model | the | information | flow | requirements, |     | we consider |       |       |          |     |           |         |     |          |
| -------- | --- | ----------- | ---- | ------------- | --- | ----------- | ----- | ----- | -------- | --- | --------- | ------- | --- | -------- |
|          |     |             |      |               |     |             | To be | noted | that the | A2C | algorithm | updates | the | policies |
a Markov Model (MM) [40] M with transition probability applied by the different agents only at the end of a training
σ
matrix P for each slice σ ∈Σ. The model include N = episode (i.e., after a predetermined number of time slots).
|     | σ   |     |     |     |     | state |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
10 states and is designed in such a way that transitions can In the period between two subsequent episodes, the differ-
only occur between adjacent states; mathematically, P =0 ent network elements collect local observations in a central
i,j
| ∀(i,j):|i−j|>1.EachstateofM |     |     |     | representsacombination |     |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
σ database, which is then used to carry out the training phase.
of resources requirements, i.e., a different realization of the Hence,thenewversionsofthelearningagentsissharedwithin
vectorr.Hence,eachinformationflowφ∈Φ isassociatedto the network, and the resource allocation strategy is updated
σ
anindependentcopyofM
σ thatchangesstateateachtimeslot consequently. In a practical scenario, the described process
t, thus altering the vector r . The minimum and maximum can be performed offline and, therefore, does not have any
φ
| value of     | the resource | requirements |               | are                | summarized | in Tab. II. |                     |       |          |          |              |     |                 |         |
| ------------ | ------------ | ------------ | ------------- | ------------------ | ---------- | ----------- | ------------------- | ----- | -------- | -------- | ------------ | --- | --------------- | ------- |
|              |              |              |               |                    |            |             | delay requirements. |       | Besides, |          | the exchange |     | of a control    | traffic |
|              |              |              |               |                    |            |             | among network       |       | elements | is       | required     | by  | the SDN         | and NFV |
|              | TABLE        | II:          | Traffic       | flow requirements. |            |             |                     |       |          |          |              |     |                 |         |
|              |              |              |               |                    |            |             | paradigms,          | which | are      | becoming | more         | and | more widespread |         |
| Serviceclass |              | Parameter    | Rangeofvalues |                    | Unit       | Sources     |                     |       |          |          |              |     |                 |         |
inmodernnetworks.Therefore,thecommunicationwithinthe
η 0.30÷42.5 Gbps [41],[42] learning units should not represent a limiting factor for the
eMBB c 50÷100 Gbps [43],[44] practical implementation of our approach.
|       |     | m   |         | 50÷100 | Gb   | [43],[44] |              |              |     |          |         |          |         |          |
| ----- | --- | --- | ------- | ------ | ---- | --------- | ------------ | ------------ | --- | -------- | ------- | -------- | ------- | -------- |
|       |     | δ   |         | 20     |      |           |              |              |     |          |         |          |         |          |
|       |     |     |         |        | ms   | [45]–[48] |              |              |     |          |         |          |         |          |
|       |     | η   | 2.08÷10 |        | Gbps | [41],[42] | B. Results   |              |     |          |         |          |         |          |
| URLLC |     | c   |         | 50−100 | Gbps | [43],[44] |              |              |     |          |         |          |         |          |
|       |     |     |         |        |      |           | We consider  |              | two | versions | of our  | learning | system, | one      |
|       |     | m   |         | 50÷100 | Gb   | [43],[44] |              |              |     |          |         |          |         |          |
|       |     |     |         |        |      |           | trained in   | the Dumbbell |     | Network  | (DRL-D) |          | and the | other in |
|       |     | δ   |         | 1      | ms   | [45]–[48] |              |              |     |          |         |          |         |          |
|       |     |     |         |        |      |           | the Triangle | Network      |     | (DRL-T). |         |          |         |          |
To be noted that, in our simulations, the number of flows In Fig. 5 we plot the utility (for the eMBB and URLLC
andtheirrequirementschangerandomly,sothattheaggregate slices)obtainedduringthetrainingphaseinthetwoscenarios.
resource requests can exceed the capacity of the network. In that the performance of eMBB slices (Ω ) increases slowly,
e
such conditions, some flows will unavoidably experience very but smoothly during the training phase, ranging from 0.6
low performance; hence, the allocation strategy should decide to 0.8 in 50% of the cases. Conversely, the performance of
whichflowtopenalize,inordertomaximizetheoverallutility. URLLC slices (Ω ) remains very low at the beginning of the
u
Therefore, our system can be exploited to handle critical training phase and suddenly increases after a certain number

|     |           |     |     |       |     | TABLE       | IV: Simulation | settings. |     |       |     |     |             |     |     |
| --- | --------- | --- | --- | ----- | --- | ----------- | -------------- | --------- | --- | ----- | --- | --- | ----------- | --- | --- |
|     | Parameter |     |     | Value |     | Description |                | Parameter |     | Value |     |     | Description |     |     |
c
B l 50Gbps Linkratecapacity C n {10,20,30,60}Gbps Nodecomputationalcapacity
|     | C   | m   | {10,20,30,60}Gb |     |     | Nodememorycapacity |     | Nstate |     | 10  |     |     | Statenumber |     |     |
| --- | --- | --- | --------------- | --- | --- | ------------------ | --- | ------ | --- | --- | --- | --- | ----------- | --- | --- |
n
|     | τn  |     |     | 0.001ms |     | Noderoutingdelay |     | τ   | p   | 0.1ms |     |     | Linkpropagationdelay |     |     |
| --- | --- | --- | --- | ------- | --- | ---------------- | --- | --- | --- | ----- | --- | --- | -------------------- | --- | --- |
l
|     | Ntrain |     |     | {3,5}·104 |     | Trainingepisodes         |     | Ntest |     | 500       |     |     | Testingepisodes |     |     |
| --- | ------ | --- | --- | --------- | --- | ------------------------ | --- | ----- | --- | --------- | --- | --- | --------------- | --- | --- |
|     | N      |     |     | 2·104     |     | Transferlearningepisodes |     | NΦ    |     | {2,...,6} |     |     | Numberofflows   |     |     |
transfer
|     | ζa  |     |     | 10−5 |     | Actorlearningrate |     | ζc  |      | 10−5 |     |     | Criticlearningrate  |     |     |
| --- | --- | --- | --- | ---- | --- | ----------------- | --- | --- | ---- | ---- | --- | --- | ------------------- | --- | --- |
|     | λ   |     |     | 0.9  |     | Discountfactor    |     |     | κ    | 10−4 |     |     | Entropyweight       |     |     |
|     | T   |     |     | 0.1s |     | Timeslotduration  |     | N   | slot | 50   |     |     | Timeslotsperepisode |     |     |
{αη,αc,αm,α } {0.25,0.25,0.25,0.25} eMBBperformanceweights {γ0,γ1} {0.1,1} Rewardweights
δ
|     | 1.0 |     |     |     |     |     |     | 1.0  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     | 0.8 |     |     |     |     |     |     | 0.8  |     |     |     |     |     |     |     |
|     | 0.6 |     |     |     |     |     |     | 0.6  |     |     |     |     |     |     |     |
|     | σΩ  |     |     |     |     |     |     | ]Ω[E |     |     |     |     |     |     |     |
0.4
0.4
|     | 0.2 |     |     |     |     | eMΩΩ |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.2
|     |     |     |     |     |     |     |     |     |     | DRLΩD |     | Empirical |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --------- | --- | --- | --- |
URLLC
|     |     |     |     |     |     |     |     |     |     | DRLΩT |     | Static |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------ | --- | --- | --- |
0.0
|     |     | 10000 |     | 20000 30000 |     | 40000 50000 |     | 0.0 |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Episode           Ω                    Ω  e                    Ω  u
|     |     |     |              |          |     |     |     |     |     | (a) | Dumbbell | Network. |     |     |     |
| --- | --- | --- | ------------ | -------- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --- | --- |
|     |     |     | (a) Dumbbell | Network. |     |     |     |     |     |     |          |          |     |     |     |
|     | 1.0 |     |              |          |     |     |     | 1.0 |     |     |          |          |     |     |     |
|     | 0.8 |     |              |          |     |     |     | 0.8 |     |     |          |          |     |     |     |
0.6
0.6
]Ω[E
σΩ
|     | 0.4 |     |     |     |     |     |     | 0.4 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.2
|     |     |     |     |     |     | eMΩΩ  |     | 0.2 |     |       |     |           |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ----- | --- | --------- | --- | --- | --- |
|     |     |     |     |     |     |       |     |     |     | DRLΩD |     | Empirical |     |     |     |
|     |     |     |     |     |     | URLLC |     |     |     | DRLΩT |     | Static    |     |     |     |
0.0
|     |     | 10000 |     | 20000 30000 |     | 40000 50000 |     | 0.0 |                       |     |             |             |             |             |     |
| --- | --- | ----- | --- | ----------- | --- | ----------- | --- | --- | --------------------- | --- | ----------- | ----------- | ----------- | ----------- | --- |
|     |     |       |     |             |     |             |     |     |           Ω           |     |          Ω  | e           |          Ω  | u           |     |
Episode
|     |           |      | (b)   | Triangle Network.  |      |           |     |                  |     | (b)     | Triangle    | Network. |           |        |      |
| --- | --------- | ---- | ----- | ------------------ | ---- | --------- | --- | ---------------- | --- | ------- | ----------- | -------- | --------- | ------ | ---- |
|     |           |      |       |                    |      |           |     |                  |     | Fig.    | 6: Expected |          | utility.  |        |      |
|     |           |      | Fig.  | 5: Training phase. |      |           |     |                  |     |         |             |          |           |        |      |
|     |           |      |       |                    |      |           |     | utility achieved |     | by each | slice,      | and by   | the whole | system | (see |
| of  | episodes. | This | means | that the agents    | need | more time | to  |                  |     |         |             |          |           |        |      |
(6)and(5)),intheDumbbellandTriangleNetworkforallthe
learn how to address the URLLC requirements. In particular, consideredstrategies.Wecannoticethat,inboththescenarios,
at the end of the training phase in the Triangle Network, the empirical algorithm tends to favor eMBB slices at the
| Ω   | spans | the full | range | of possible | values, | which indicates |     |          |          |        |       |     |          |             |     |
| --- | ----- | -------- | ----- | ----------- | ------- | --------------- | --- | -------- | -------- | ------ | ----- | --- | -------- | ----------- | --- |
| u   |       |          |       |             |         |                 |     | expenses | of URLLC | flows, | whose |     | expected | performance | is  |
that the URLLC flows either get maximum or zero reward in alwayslowerthan0.2.Thestaticstrategybehavessimilarlybut
| accordance |         | the step-like |     | shape of their | performance  | function. |     |          |           | Ω        |               |        |                 |              |        |
| ---------- | ------- | ------------- | --- | -------------- | ------------ | --------- | --- | -------- | --------- | -------- | ------------- | ------ | --------------- | ------------ | ------ |
|            |         |               |     |                |              |           |     | provides | lower     | e than   | the empirical |        | algorithm.      | In contrast, |        |
| A          | similar | phenomenon    |     | occurs in      | the Dumbbell | Network   |     |          |           |          |               |        |                 |              |        |
|            |         |               |     |                |              |           |     | DRL-D    | and DRL-T | slightly |               | reduce | the performance |              | of the |
where, however, the URLLC utility is lower due to the fewer eMBB services in order to double the fraction of satisfied
available resources.
|     |     |     |     |     |     |     |     | URLLC | flows, | increasing | the | total utility. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ---------- | --- | -------------- | --- | --- | --- |
Totesttheperformanceofourstrategies,wecarryoutaddi- In Fig. 7 we analyze the distribution of the system utility
tional N test =300 episodes. In Fig. 6, we report the expected forallthedifferentstrategiesandnetworkscenarios.Weadopt

1.0
0.8
0.6
0.4
0.2
0.0
D u m b be l l T r i a n gl e P y r a mid
Ω
1.0
0.8
0.6
0.4
0.2
DRLΩD Empirical
DRLΩT Static
0.0
η δ δ
Fig. 7: Utility distribution.
the boxplot representation, where the white line at the center
of the box is the median of the distribution, while the box
edges represent the 25th and the 75th percentile, respectively.
It is clear that the static strategy always yield to the worst
performance: this is because it does not handle the variability
of service demands, which is very critical for the URLLC
traffic flows, whose performance goes to zero as soon as one
of the requirements is not satisfied. The empirical algorithm
worksbetterbutitisstilloutperformedbytheDRLstrategies,
both when considering the median and the 25th and 75th
percentilesofΩ.IntheDumbbellNetwork,DRL-DandDRL-
T ensure that Ω > 0.45 in almost 50% of the test episodes,
with a 10% gain over the empirical algorithm. In the Triangle
and Pyramid scenario, the lack of network resources is less
strikingand,consequently,theperformanceofallthestrategies
increases. Using the empirical algorithm, 50% of the test
episodes experience Ω > 0.5 while, with the DRL strategies,
this threshold is raised to 0.65 and 0.7, respectively.
We observe that DRL-D and DRL-T achieve similar results
in all the testing scenarios, including the Pyramid Network,
which is a different environment from those seen during the
training. This means that our architecture can suit multiple
network topologies without the need of an additional learning
phase. At the same time, we expect that a more specific train-
ing can further improve the behavior of the local controllers;
in the rest of the section, we will show how to leverage the
transfer learning paradigm to this purpose.
C. Transfer Learning
Transfer learning aims at speeding up the training of a
ML algorithm in a certain scenario by exploiting the structure
learned by other ML algorithms trained in similar scenarios.
In what follows, we exploit this technique to adapt our DRL
strategy to different network topologies and traffic loads.
Hence, we consider two additional learning architectures that
we named DRL-DP and DRL-TP. These systems are first
trained for N = 3×104 episodes in the Dumbbell and
train
Triangle Network, respectively, according to the framework
described in Sec. IV. Then, we perform an additional training
of N =2×104 episodes in the Pyramid Network.
transfer
]ρΩ[E
DRLΩD Empirical
DRLΩDP Static
(a) Pyramid Network.
1.0
0.8
0.6
0.4
0.2
0.0
η δ δ
]ρΩ[E
DRLΩT Empirical
DRLΩTP Static
(b) Pyramid+ Network.
Fig. 8: Expected resource utility.
During the additional training phase, each controller is
updated with experience related to the network element it is
associated to. For instance, a controller Γ designed to manage
slice σ in a link l is trained using only the state-action pairs
for link l and information flows φ ∈ Φ . Therefore, each
σ
controller has to deal with a new scenario with different
characteristics than the original one. Particularly, the training
operations can be performed online in each network element,
withoutinvolvingthecentralmanagershowninFig.2.Hence,
this stage does not require any communication within the
network and can be executed after the learning architecture
have been deployed in a real scenario. From a practical
perspective, the described framework makes local controllers
learn how to carry out more precise actions, thus increasing
theoverallutility.Thedrawbackisthateachcontrollerwillbe
able to operate only in a specific location and, therefore, the
learned strategy cannot be implemented in different network
topologies.
The transfer learning stage is repeated two times, consid-
ering different configurations for the URLLC services. First,
we implement the same statistics presented in Tab. II: in this
case, the throughout required by each URLLC flow is in
[2.08,10] Gbps. Then, we double the rate requirements of the
URLLCslice(whoserangeofvaluesbecomes[4.16,20]Gbps)

|     | DRLΩD |     |     | DRLΩDP |     | Empirical |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | DRLΩT |     |     | DRLΩTP |     | Static    |     |     |     |     |     |     |     |     |
1.0
0.8
0.6
Ω
0.4
0.2
0.0
|                 |            P  y  r amid                 |              |              |               |          P   y  r a mid+                 |           |             |     |     |          |              |     |          |     |
| --------------- | --------------------------------------- | ------------ | ------------ | ------------- | ---------------------------------------- | --------- | ----------- | --- | --- | -------- | ------------ | --- | -------- | --- |
|                 |                                         | Fig.         | 9: Utility   | distribution. |                                          |           |             |     |     |          |              |     |          |     |
| to asses        | the ability                             | of           | our strategy |               | to adapt                                 | to        | new service |     |     |          |              |     |          |     |
|                 |                                         |              |              |               |                                          |           |             |     |     | Fig. 10: | GARR Network |     | (Italy). |     |
| specifications. | In                                      | particular,  |              | we denote     | by                                       | Pyramid+  | the sce-    |     |     |          |              |     |          |     |
| nario in        | which                                   | the required |              | throughput    | of                                       | the URLLC | flows       |     |     |          |              |     |          |     |
is increased.
|         |        |           |     |          |             |     |          |     |     | ΩeΦΩDRL) | ΩeΦΩEmpirical) |     |     | ΩeΦΩStatic) |
| ------- | ------ | --------- | --- | -------- | ----------- | --- | -------- | --- | --- | -------- | -------------- | --- | --- | ----------- |
| In Fig. | 8a, we | represent | the | expected | performance |     | obtained |     |     |          |                |     |     |             |
in the Pyramid Network by DRL-D and DRL-DP, and the ΩuΦΩDRL) ΩuΦΩEmpirical) ΩuΦΩStatic)
| benchmark   | strategies, |         | while    | considering | specific  |            | network re- |     | 1.0 |     |     |     |     |     |
| ----------- | ----------- | ------- | -------- | ----------- | --------- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| sources.    | Hence,      | instead | of using | Ω           | to asses  | the system | utility,    |     |     |     |     |     |     |     |
| we consider | Ωρ,         | defined | in       | (8). As     | expected, | the        | algorithms  |     |     |     |     |     |     |     |
0.8
| obtained                                        | by exploiting |           | the transfer  |                 | learning  | approach       | perform       |     |      |     |     |     |     |     |
| ----------------------------------------------- | ------------- | --------- | ------------- | --------------- | --------- | -------------- | ------------- | --- | ---- | --- | --- | --- | --- | --- |
| better than                                     | those         | trained   | on the        | other           | networks. |                | For instance, |     |      |     |     |     |     |     |
|                                                 |               |           |               |                 |           |                | Ωc            |     | 0.6  |     |     |     |     |     |
| using the                                       | DRL-DP        | strategy, |               | the expectation |           | of             | increases     |     | ]Ω[E |     |     |     |     |     |
| by more                                         | than 5%.      |           |               |                 |           |                |               |     |      |     |     |     |     |     |
| InFig.8b,weshowtheoutcomesobtainedinthePyramid+ |               |           |               |                 |           |                |               |     | 0.4  |     |     |     |     |     |
| network                                         | scenario.     | We        | first observe |                 | that all  | the strategies | yield         |     |      |     |     |     |     |     |
| to a lower                                      | performance   |           | since         | the new         | URLLC     |                | requirements  |     | 0.2  |     |     |     |     |     |
aremoredifficulttofulfill.Theempiricalstrategyslightlyout-
| performs | DRL-T | for what | concerns |     | the throughput |     | and delay |     |     |     |     |     |     |     |
| -------- | ----- | -------- | -------- | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
0.0
requirements.Nevertheless,DRL-Tstillprovidesgoodresults, 2 3 4 5 6 7 8 9 10
|Φ|
| which means | that | the | DRL | approach | is resilient |     | to different |     |     |     |     |     |     |     |
| ----------- | ---- | --- | --- | -------- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
traffic loads. Also in this case, transfer learning proves to be Fig. 11: Expected utility vs flows’ number.
| a worthwhile | approach |       | since           | DRL-TP | outperforms |     | the other |     |     |     |     |     |     |     |
| ------------ | -------- | ----- | --------------- | ------ | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
| algorithms   | in all   | three | key performance |        | indicators. |     |           |     |     |     |     |     |     |     |
In Fig. 9, we report the distribution of the system utility in nodes,10edgenodesand40links.Weassumethateachlinkis
|             |     |          |            |     |     |                |     | provided | with | B =50 | Gbps of | bandwidth | capacity; | besides, |
| ----------- | --- | -------- | ---------- | --- | --- | -------------- | --- | -------- | ---- | ----- | ------- | --------- | --------- | -------- |
| the Pyramid | and | Pyramid+ | scenarios. |     | We  | can appreciate | how |          |      | l     |         |           |           |          |
thethealgorithmsgivenbytransferlearningalwaysensurethe we set the computational and memory capacities of the core
|     |     |     |     |     |     |     |     | nodes | to Cc | = 30 Gbps | and Cm | = 30 | Gb, respectively, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --------- | ------ | ---- | ----------------- | --- |
best utility, both considering the median and the percentiles n n
|     |     |     |     |     |     |     |     |     |     |     | Cc  |     | Cm  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of Ω.In particular,DRL-DPand DRL-TPoutperformDRL-D those of the edge nodes to n =10 Gbps and n =10 Gb,
and DRL-T, respectively, despite the total number of training respectively. Finally, we relax the delay requirements of the
|          |        |          |         |            |     |             |     | eMBB  | and           | URLLC | services, which | are         | set to  | 100 ms and |
| -------- | ------ | -------- | ------- | ---------- | --- | ----------- | --- | ----- | ------------- | ----- | --------------- | ----------- | ------- | ---------- |
| episodes | is the | same for | all the | considered |     | strategies. |     |       |               |       |                 |             |         |            |
|          |        |          |         |            |     |             |     | 5 ms, | respectively. | We    | make            | this choice | to deal | with the   |
increasedlengthoftheroutingpaths,whichresultsinahigher
| D. Practical | Implementation |     |     |     |     |     |     |             |     |           |            |     |     |     |
| ------------ | -------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ---------- | --- | --- | --- |
|              |                |     |     |     |     |     |     | propagation |     | delay for | the flows. |     |     |     |
To provide an overview on how implement our system in a To implement our DRL strategy in the new scenario, we
realisticscenario,weconsiderasectionoftheGARRhighca- carry out two consecutive learning stages: first, we train our
pacitynetwork[49],whichistheinfrastructureinterconnecting system for 2 × 104 episodes using a centralized learning
the main Italian universities and research centers. As depicted approach (as done for the DRL-D and DRL-T strategies). We
in Fig. 10, the considered network topology includes 19 core recall that this phase can be achieved offline, i.e., without

time constraints, using all the experience gathered all the slot t. Let T∗ be the minimum between the slot boundary T
networklocations.Then,wecarryoutanadditionaltrainingof and the time at which the queue empties, i.e.,
104 episodes, defining a specific tuple of learning agents for
(cid:32) (cid:33)
each network element (as done for the DRL-DP and DRL-TP T∗ =min T, D l,φ (t−1) . (36)
strategies). As already stated, this stage is performed online b (t)−bi (t)
l,φ l,φ
and does not require any communication within the network.
In Fig. 11, we plot the expected performance of the eMBB Furthermore, let D l,φ (t,u) denote the residual backlog of
and URLLC slices (i.e., E[Ω ] and E[Ω ]) as a function of flow φ in link l, u seconds after the beginning of timeslot t.
e u
thenumberofinformationflowsintheGARRscenario.When
Therefore,foranyu∈[0,T∗]wehaveD
l,φ
(t,u)=D
l,φ
(t)−
considering the eMBB flows, all the strategies have a similar
u(b
l,φ
(t)−bi
l,φ
(t)),whileD
l,φ
(t,u)=0foru∈(T∗,T].Now,
behavior since E[Ω ] declines gradually as the cardinality the queuing delay experienced by the incoming flow at time
e
of Φ increases. Instead, E[Ω ] deceases very quickly: it is u ∈ [0,T] is zero if the queue is empty, and otherwise equal
u
maximized when |Φ|=2 and approaches 0 as more flows are to δ(u,t) = Dl,φ(u,t). The average delay over the timeslot is
bl,φ(t)
initialized over the network. hence
In particular, the empirical algorithm outperforms the other
strategies when the number of information flows is limited 1 (cid:90) T 1 (cid:90) T∗ D (u,t)
(|Φ| ≤ 3). Beyond this point, it becomes more convenient to τq (t)= δ(u,t)du= l,φ du (37)
l,φ T T b (t)
maintain a static allocation of the system resources to prevent 0 0 l,φ
2T∗D (t)−T∗2(b (t)−bi (t))
the degradation of E[Ω u ]. However, both the benchmarks = l,φ l,φ l,φ . (38)
are outperformed by the learning-based approach, which has 2Tb l,φ (t)
learned to give priority to the URLLC services, ensuring a For T∗ =T, we obtain
better total utility. In particular, using the empirical and the
2D (t)−T(b (t)−bi (t))
staticstrategies,E[Ω u ]fallsbelow0.3for|Φ|=6,whileDRL τq (t)= l,φ l,φ l,φ . (39)
ensures E[Ω u ]>0.6 in the same conditions. l,φ 2b l,φ (t)
ForT∗ <T,instead,wehaveT∗(b (t)−bi (t))=D (t),
VII. CONCLUSION l,φ l,φ l,φ
so that (38) yields
In this work, we investigated the potentials of DRL to
T∗D (t) D (t)
orchestrate network resources in a NS scenario. Specifically, τq (t)= l,φ < l,φ . (40)
we developed a distributed DRL system where different units l,φ 2Tb l,φ (t) 2b l,φ (t)
interact to meet the resource demands of multiple information Recallingthatbo (t)usedin(18)isdefinedastheminimum
flows. The training of such an architecture was undertaken l,φ
between b (t), and 2Dl,φ(t−1)+bi (t), we can see that (18)
following an A2C approach, which enables an online training l,φ T l,φ
is indeed a compact expression for τq (t), provided that it is
phaseandallowsoursystemtodynamicallyadapttodifferent l,φ
approximated by its upper bound when T∗ <T.
working conditions.
By means of simulations, we showed that the designed
strategy can consistently improve the management of network
REFERENCES
resources, especially when the system complexity, both in [1] 3GPP, “Service requirements for next generation new services and
terms of network topology and service heterogeneity, in- markets,”3rdGenerationPartnershipProject(3GPP),TechnicalSpeci-
fication(TS)22.261,March2020,version17.2.0.
creases.Inparticular,ourapproachmakesitpossibletodouble
[2] J.Navarro-Ortiz,P.Romero-Diaz,S.Sendra,P.Ameigeiras,J.J.Ramos-
the number of URLLC flows supported by the network, Munoz, and J. M. Lopez-Soler, “A survey on 5G usage scenarios and
without significantly degrading the performance of the eMBB traffic models,” IEEE Communications Surveys & Tutorials, vol. 22,
no.2,pp.905–929,February2020.
flows, and can suit different network topologies without the
[3] M.Yang,Y.Li,D.Jin,L.Zeng,X.Wu,andA.V.Vasilakos,“Software-
need for additional training. Besides, transfer learning can be definedandvirtualizedfuturemobileandwirelessnetworks:asurvey,”
used to further improve the behavior of the learning agents, MobileNetworksandApplications,vol.20,no.1,pp.4–18,September
2015.
thus increasing the overall utility at the cost of a reduced
[4] P. Zhang, H. Yao, and Y. Liu, “Virtual network embedding based on
adaptability of the agents to different network topologies. computing,network,andstorageresourceconstraints,”IEEEInternetof
As part of future work, we are interested in extending our ThingsJournal,vol.5,no.5,pp.3298–3304,2017.
[5] P.Rost,C.Mannweiler,D.S.Michalopoulos,C.Sartori,V.Sciancale-
NS model by considering more slice classes with different
pore,N.Sastry,O.Holland,S.Tayade,B.Han,D.Begaetal.,“Network
specifications. Particularly, we want to test our framework slicingtoenablescalabilityandflexibilityin5Gmobilenetworks,”IEEE
with real communication traces, with the aim of identifying Communicationsmagazine,vol.55,no.5,pp.72–79,May2017.
[6] I.Afolabi,T.Taleb,K.Samdanis,A.Ksentini,andH.Flinck,“Network
potential limits. Finally, we will investigate the possibility
slicing and softwarization: A survey on principles, enabling technolo-
of introducing additional learning units, which are trained to gies,andsolutions,”IEEECommunicationsSurveys&Tutorials,vol.20,
coordinate the local controllers of our architecture, e.g., by no.3,pp.2429–2453,March2018.
[7] P.Popovski,K.F.Trillingsgaard,O.Simeone,andG.Durisi,“5Gwire-
varying the routing paths of the traffic flows.
lessnetworkslicingforeMBB,URLLC,andmMTC:Acommunication-
theoretic view,” IEEE Access, vol. 6, pp. 55765–55779, September
APPENDIX 2018.
[8] M.Richart,J.Baliosian,J.Serrat,andJ.-L.Gorricho,“Resourceslicing
Inwhatfollows,wederiveequation(18),whichdetermines
invirtualwirelessnetworks:Asurvey,”IEEETransactionsonNetwork
theaveragequeuingtimeτq (t)ofφinlinkl duringthetime andServiceManagement,vol.13,no.3,pp.462–476,2016.
l,φ

[9] P. Caballero, A. Banchs, G. de Veciana, and X. Costa-Pe´rez, “Multi- [30] T. Kimura, T. Kimura, A. Matsumoto, and K. Yamagishi, “Balancing
tenant radio access network slicing: Statistical multiplexing of spatial qualityofexperienceandtrafficvolumeinadaptivebitratestreaming,”
loads,”IEEE/ACMTransactionsonNetworking,vol.25,no.5,pp.3044– IEEEAccess,vol.9,pp.15530–15547,2021.
3058,July2017. [31] R.S.SuttonandA.G.Barto,Reinforcementlearning:Anintroduction.
[10] K. Samdanis, X. Costa-Perez, and V. Sciancalepore, “From network MITpress,2018.
sharing to multi-tenancy: The 5G network slice broker,” IEEE Com- [32] M.L.Puterman,Markovdecisionprocesses:discretestochasticdynamic
municationsMagazine,vol.54,no.7,pp.32–39,July2016. programming. JohnWiley&Sons,2014.
[11] R. Trivisonno, R. Guerzoni, I. Vaishnavi, and A. Frimpong, “Network [33] P. Indyk and R. Motwani, “Approximate nearest neighbors: towards
resource management and QoS in SDN-enabled 5G systems,” in 2015 removing the curse of dimensionality,” in Proceedings of the thirtieth
IEEEGlobalCommunicationsConference,December2015. annualACMsymposiumonTheoryofcomputing,1998,pp.604–613.
[12] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. [34] V.R.KondaandJ.N.Tsitsiklis,“Actor-criticalgorithms,”inAdvances
Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski inneuralinformationprocessingsystems,2000,pp.1008–1014.
et al., “Human-level control through deep reinforcement learning,” [35] V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. Lillicrap, T. Harley,
Nature,vol.518,no.7540,pp.529–533,February2015. D.Silver,andK.Kavukcuoglu,“Asynchronousmethodsfordeeprein-
[13] H.Halabian,“Distributedresourceallocationoptimizationin5Gvirtu- forcement learning,” in International conference on machine learning,
alizednetworks,”IEEEJournalonSelectedAreasinCommunications, February2016,pp.1928–1937.
vol.37,no.3,pp.627–642,2019. [36] H.Zhang,T.-W.Weng,P.-Y.Chen,C.-J.Hsieh,andL.Daniel,“Efficient
[14] M. Leconte, G. S. Paschos, P. Mertikopoulos, and U. C. Kozat, “A neuralworkrobustnesscertificationwithgeneralactivationfunctions,”in
resourceallocationframeworkfornetworkslicing,”inIEEEConference Advancesinneuralinformationprocessingsystems,December2018,pp.
onComputerCommunications. IEEE,2018,pp.2177–2185. 4939–4948.
[15] S. Boyd, N. Parikh, E. Chu, B. Peleato, and J. Eckstein, “Distributed [37] T.Jaakkola,S.P.Singh,andM.I.Jordan,“Reinforcementlearningalgo-
optimizationandstatisticallearningviathealternatingdirectionmethod rithmforpartiallyobservableMarkovdecisionproblems,”inAdvances
ofmultipliers,”2011. inneuralinformationprocessingsystems,1995,pp.345–352.
[16] Y. Xiao, M. Hirzallah, and M. Krunz, “Distributed resource allocation [38] X.-S. Yang, Nature-inspired metaheuristic algorithms. Luniver press,
fornetworkslicingoverlicensedandunlicensedbands,”IEEEJournal 2010.
onSelectedAreasinCommunications,vol.36,no.10,pp.2260–2274, [39] D. Whitley, “A genetic algorithm tutorial,” Statistics and computing,
2018. vol.4,no.2,pp.65–85,1994.
[17] M.Hu,L.Zhuang,D.Wu,Y.Zhou,X.Chen,andL.Xiao,“Learning [40] C.J.Geyer,“PracticalMarkovchainMonteCarlo,”Statisticalscience,
driven computation offloading for asymmetrically informed edge com- pp.473–483,1992.
puting,”IEEETransactionsonParallelandDistributedSystems,vol.30, [41] L. Cominardi, L. M. Contreras, C. J. Bcrnardos, and I. Berberana,
no.8,pp.1802–1815,2019. “Understanding QoS applicability in 5G transport networks,” in 2018
[18] F.Fossati,S.Moretti,P.Perny,andS.Secci,“Multi-resourceallocation IEEEInternationalSymposiumonBroadbandMultimediaSystemsand
for network slicing,” IEEE/ACM Transactions on Networking, vol. 28, Broadcasting(BMSB). IEEE,2018,pp.1–5.
no.3,pp.1311–1324,2020. [42] 3GPP,“Systemarchitectureforthe5GSystem(5GS),”3rdGeneration
[19] R. Alvizu, S. Troia, G. Maier, and A. Pattavina, “Matheuristic with PartnershipProject(3GPP),TechnicalSpecification(TS)23.501,March
machine-learning-based prediction for software-defined mobile metro- 2020,version16.4.0.
core networks,” Journal of Optical Communications and Networking, [43] D.SattarandA.Matrawy,“DSAF:Dynamicsliceallocationframework
vol.9,no.9,pp.19–30,2017. for5Gcorenetwork,”arXivpreprintarXiv:1905.03873,2019.
[20] Y. Hua, R. Li, Z. Zhao, X. Chen, and H. Zhang, “GAN-powered [44] A.Chiha,M.VanderWee,D.Colle,andS.Verbrugge,“Networkslicing
deep distributional reinforcement learning for resource management in cost allocation model,” Journal of Network and Systems Management,
networkslicing,”IEEEJournalonSelectedAreasinCommunications, pp.1–33,2020.
vol.38,no.2,pp.334–349,2020. [45] F. Voigtla¨nder, A. Ramadan, J. Eichinger, C. Lenz, D. Pensky, and
[21] A. Thantharate, R. Paropkari, V. Walunj, and C. Beard, “Deepslice: A. Knoll, “5G for robotics: Ultra-low latency control of distributed
A deep learning approach towards an efficient and reliable network roboticsystems,”in2017InternationalSymposiumonComputerScience
slicing in 5G networks,” in IEEE 10th Annual Ubiquitous Computing, andIntelligentControls(ISCSIC). IEEE,2017,pp.69–72.
Electronics Mobile Communication Conference (UEMCON), October [46] J.Sachs,L.A.Andersson,J.Arau´jo,C.Curescu,J.Lundsjo¨,G.Rune,
2019,pp.0762–0767. E. Steinbach, and G. Wikstro¨m, “Adaptive 5G low-latency communi-
[22] Y.M.Saputra,D.T.Hoang,D.N.Nguyen,E.Dutkiewicz,D.Niyato, cationfortactileinternetservices,”ProceedingsoftheIEEE,vol.107,
andD.I.Kim,“Distributeddeeplearningattheedge:Anovelproactive no.2,pp.325–349,2018.
and cooperative caching framework for mobile edge networks,” IEEE [47] X. Jiang, H. Shokri-Ghadikolaei, G. Fodor, E. Modiano, Z. Pang,
WirelessCommunicationsLetters,vol.8,no.4,pp.1220–1223,2019. M. Zorzi, and C. Fischione, “Low-latency networking: Where latency
[23] N. Van Huynh, D. Thai Hoang, D. N. Nguyen, and E. Dutkiewicz, lurksandhowtotameit,”ProceedingsoftheIEEE,vol.107,no.2,pp.
“Optimal and fast real-time resource slicing with deep dueling neural 280–306,2018.
networks,”IEEEJournalonSelectedAreasinCommunications,vol.37, [48] 3GPP,“Policyandchargingcontrolarchitecture,”3rdGenerationPart-
no.6,pp.1455–1470,2019. nershipProject(3GPP),TechnicalSpecification(TS)23.203,December
[24] C.J.WatkinsandP.Dayan,“Q-learning,”Machinelearning,vol.8,no. 2019,version16.2.0.
3-4,pp.279–292,1992. [49] “GARR high capacity network,” https://www.garr.it/en/infrastructures/
[25] J.A.Ayala-Romero,A.Garcia-Saavedra,M.Gramaglia,X.Costa-Perez, network-infrastructure/network-map,accessed:2021-03-31.
A.Banchs,andJ.J.Alcaraz,“vrAIn:Adeeplearningapproachtailoring
computingandradioresourcesinvirtualizedRANs,”inThe25thAnnual
InternationalConferenceonMobileComputingandNetworking,2019,
pp.1–16.
[26] J. S. P. Roig, D. M. Gutierrez-Estevez, and D. Gu¨ndu¨z, “Management
and orchestration of virtual network functions via deep reinforcement
learning,”IEEEJournalonSelectedAreasinCommunications,vol.38,
no.2,pp.304–317,2019.
[27] Y. Abiko, T. Saito, D. Ikeda, K. Ohta, T. Mizuno, and H. Mineno,
“Flexible resource block allocation to multiple slices for radio access
networkslicingusingdeepreinforcementlearning,”IEEEAccess,vol.8,
pp.68183–68198,2020.
[28] M. Alsenwi, N. H. Tran, M. Bennis, S. R. Pandey, A. K. Bairagi,
and C. S. Hong, “Intelligent resource slicing for eMBB and URLLC
coexistence in 5G and beyond: A deep reinforcement learning based
approach,”arXivpreprintarXiv:2003.07651,2020.
[29] S. J. Pan and Q. Yang, “A survey on transfer learning,” IEEE Trans-
actionsonknowledgeanddataengineering,vol.22,no.10,pp.1345–
1359,2009.