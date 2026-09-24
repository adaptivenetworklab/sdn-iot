# Efficient Routing for Software-Defined Wireless Sensor Networks A Nave Bayes Approach

> Source file: `Efficient Routing for Software-Defined Wireless Sensor Networks A Nave Bayes Approach.pdf`

---

Received12November2025,accepted25November2025,dateofpublication3December2025,
dateofcurrentversion11December2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3638863
Efficient Routing for Software-Defined Wireless
Sensor Networks: A Naïve Bayes Approach
AMINETCHERAK 1,SAMIALOUCIF 2,(SeniorMember,IEEE),
ANDMOHAMEDOULDKHAOUA 1
1LRDSI,DepartmentofComputerScience,UniversityofBlida1,Blida09000,Algeria
2CollegeofTechnologicalInnovation,ZayedUniversity,AbuDhabi,UnitedArabEmirates
Correspondingauthor:AmineTcherak(tcherak_amine@univ-blida.dz)
ABSTRACT WirelessSensorNetworks(WSNs)formthebackboneofInternetofThings(IoT)applications.
Software-Defined Networking (SDN) is an emerging networking paradigm that extends the lifetime of
WSNs by transferring the resource-intensive routing task from sensor nodes to a centralized controller.
However, many SDN-based routing schemes for WSNs employ inefficient algorithms at the controller.
Traditionalshortest-pathmethodsoftencreatetrafficimbalancesacrossneighboringnodes,whileReinforce-
ment Learning (RL)-based approaches typically generate excessive control traffic. Both issues accelerate
energy depletion and reduce network lifetime. Moreover, existing algorithms frequently overlook critical
factors, such as buffer occupancy, when selecting relay nodes, which can lead to congestion, packet loss,
and increased latency. To address these limitations, this paper proposes NBSDN, a Naïve Bayes–based
routingalgorithmforSDN-enabledWSNs.NBSDNextendsourearlierenergy-anddistance-awaresolution
(referredtoasNB-SDWSN)byincorporatinglinkqualityandnodebuffercapacityintotheroutingdecision
process. The controller periodically rotates relay node assignments among neighboring nodes based on
their residual energy, distance to the sink, link quality, and buffer occupancy, thereby balancing load
and preventing congestion. Extensive simulations conducted in the COOJA environment demonstrate that
NBSDNsignificantlyoutperformsbenchmarkalgorithms—includingtheDijkstra-basedShortestPathSDN
(SPSDN),Energy-AwareSDN(EASDN),NB-SDWSN,andRL-basedSDN(RLSDN)routing—intermsof
networklifetime,controloverhead,packetloss,latency,andthroughput.
INDEXTERMS WSNs,IoT,SDN,NaïveBayesalgorithm,loadbalancing,congestionavoidance,COOJA
simulator,performanceanalysis.
I. INTRODUCTION smarthomes,smartagriculture,healthcaremonitoring,envi-
The Internet of Things (IoT) refers to a network of phys- ronmentalsurveillance,andnaturaldisasterdetection[1].
ical items embedded with sensors, actuators, electronics, At the core of IoT lies the Wireless Sensor Network
software, and network capabilities, enabling them to col- (WSN), which is composed of small, wirelessly connected
lect and exchange data with each other and with other devices called sensor nodes, as depicted in Fig. 1. These
devicesandsystemsviatheInternet.Theseitemsspanfrom nodes, equipped with embedded sensors, are distributed
vehicles and household appliances to wearable devices and throughoutadesignatedareaandaretaskedwithperiodically
industrial machinery. By connecting these objects to the capturing diverse environmental and physical parameters
Internet, they acquire enhanced functionalities, becoming such as temperature, humidity, heartbeat, and blood pres-
increasingly intelligent and responsive, thereby offering a sure. Depending on the IoT application, the collected data
spectrum of applications across various domains, including originates either from the surrounding environment where
the sensor nodes are deployed or from the entities to which
The associate editor coordinating the review of this manuscript and the nodes are attached. Subsequently, the gathered data is
approvingitforpublicationwasChanHwangSee . transmitted,eitherdirectlyorviaintermediarynodes,tothe
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
VOLUME13,2025 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 207277

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
TABLE1. Listofacronyms. either through their sensors or via data shared by adjacent
nodes. Second, they periodically execute a routing protocol
to identify and select the best neighbor to act as a relay
nodefortransmittingdatatothesink.Thisprocessinvolves
identifyingthenearestneighboringnodetothesink,i.e.,the
neighboringnodethatrequirespassingthroughtheminimum
number of hops or intermediate sensor nodes to reach the
sink.Third,thesensornodesareresponsibleforrelayingthe
collecteddatatothesinkviatheidentifiedrelaynode.
Theroutingprocessfrequentlydemandssignificantutiliza-
tionofthesensornode’scomputationalpowerandmemory,
thus hastening the depletion of its battery. Energy exhaus-
tionleadstonodeshutdown,therebyshorteningthenetwork
lifespan.Additionally,thefailureofasensornodecanresult
in the isolation of its neighboring nodes, particularly if it
servesastheirexclusivepathwaytothesink.Consequently,
they are unable to transmit their data to the sink, escalating
packetlossanddiminishingtheoverallnetworkthroughput.
To mitigate this challenge, researchers have introduced a
newnetworkingparadigmtoWSNscalledSoftware-Defined
Networking (SDN) [2], resulting in a centralized network,
widely referred to as the Software-Defined Wireless Sensor
Network(SDWSN).TheSDWSNismadeupoftwologically
separatedlayersnamedplanes:thecontrolplaneandthedata
plane. The control plane represents the central point of the
SDWSNandentirelymanagesandcontrolstheWSN,which
isthedataplane.Thecontrolplaneconsistsofaserverknown
as the controller. The controller continuously maintains an
entire view of the WSN topology through control packets
thataresentbythenodeswithintheWSN.Thisenablesthe
controllertohandletheroutingprocessinsteadofthesensor
nodesbyperiodicallycalculatingandassigningtoeachnode
itsbestrelaynode(bestneighbor)responsibleforforwarding
its packets toward the sink. The sensor nodes then learn
theirrelaynodeviacontrolpacketssentfromthecontroller.
Consequently,theheavyroutingprocessisremovedfromthe
nodes,preservingtheirresourcesandprolongingthenetwork
sinknode.Thispivotalnode,functioningasagateway,trans- lifetime.
mitsthereceiveddataoverestablishedinfrastructureslikethe Several SDWSN studies have proposed controller-side
Internet to a remote server where it is stored. Through ded- routing algorithms. In [3], [4], and [5], the authors used
icated applications, users can remotely access and visualize shortest-path algorithms such as Dijkstra or Bellman–Ford.
therecordeddata,offeringreal-timeremotemonitoringofthe Thesemethodsassumethatasensor’sbestrelayistheneigh-
conditionsandstatusofthesubjectsorareaswherethenodes bor closest to the sink. However, when a node has many
areplaced. neighbors,thischoiceforcesalltrafficthroughasinglerelay.
Sensornodes,whichareoftencharacterizedbytheircon- As a result, that relay must receive, store, process, and for-
strained resources, operate within energy limitations due to wardallpackets,rapidlydepletingitsenergyandshortening
theirrelianceonnon-replaceablebatteries.Thispredicament network lifetime. Concentratingtraffic on one neighborcan
primarilystemsfromthedeploymentofthesenodesinharsh alsocausecongestion:onceitsbufferbecomesfull,additional
andinaccessibleenvironments,therebyrestrictingtheiroper- packetsaredropped.Thisincreasespacketlossandultimately
ational capacities. Moreover, their communication range is reducesoverallnetworkthroughput.
confinedtoalimitednumberofneighboringnodesduetothe Other studies have introduced controller-based routing
restrictedcoverageoftheirwirelesscommunicationmodules. algorithms, including the Energy-Aware SDN (EASDN)
Additionally, the processing power and memory of these method[6]andseveralReinforcementLearning(RL)-driven
nodesareconstrained,resultinginreducedcomputationaland schemes [7], [8], [9], [10] based on the principles in [11].
storagecapabilities.Functionally,sensornodesperformthree Unlike shortest-path routing, these approaches rotate the
primary tasks: first, they continuously acquire sensory data, relay role among a node’s neighbors according to their
207278 VOLUME13,2025

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
FIGURE1. AnIoTarchitectureintegratingaWSN.
residualenergy.Thisdistributestrafficmoreevenlyandhelps wirelesslinkquality—duringtheroutingprocess,i.e.,during
extend network lifetime. However, EASDN and RL-based theselectionofthemostsuitableneighboringnode,foreach
methods generate significantly more control traffic than sensornode,toserveasitsrelay.Thislimitationisparticularly
shortest-pathrouting.Theyrequirefrequentinteractionswith significant in WSNs, which are characterized by inherently
theWSNtoselectrelaynodesandrelyonbroadcastcontrol lowlinkqualityandlimitednodebuffercapacityasspecified
packets,whichcancongestthenetworkandcausecollisions intheIEEE802.15.4standard[23].Neglectingtheseparam-
with both control and data traffic. This leads to packet loss etersmayleadtotheselectionofrelaynodeswithdegraded
andacceleratesthedepletionofnodes’batteries,leavingless link quality or an overloaded buffer, thereby increasing the
energy for sensing and data forwarding. As a result, data probabilityofcongestion,packetloss,andelevatednetwork
throughput decreases, and fewer packets reach end users, latency.
reducingthequalityofthemonitoredinformation. Motivatedbytheaforementionedobservations,thispaper
Additionally, RL-based routing algorithms, as well as proposesanenhancedcongestion-andenergy-awarerouting
those relying on meta-heuristics [12], [13], [14], [15], [16] approachbasedontheNaïveBayesalgorithmtoimprovethe
andgeneticalgorithms[17],[18],imposehighcomputational controller’sroutingdecisionsinSDWSNs.IncontrasttoNB-
overheadonthecontrollerandexhibitslowconvergence[19], SDWSN, the proposed approach selects the best relay node
particularly in large-scale WSNs. As the network grows, foreachnodefromitslistofneighbors,takingintoaccount
thesemethodsrequiremoretimetoidentifyanddisseminate multiple features, including the neighbor’s battery level, its
thebestrelaynodeforeachsensornode.Consequently,each distancetothesink,itsbufferoccupancy,andthelinkquality
sensornodecontinuestouseitspreviouslyassignedrelayfor thatconnectsittothesensornode.Thismulti-criteriaselec-
longerperiods,leadingtoacceleratedbatterydepletionanda tion process mitigates congestion, reduces network latency,
shorteroverallnetworklifetime. and minimizes packet loss. Another key aspect of our pro-
In a previous study [20], we introduced NB-SDWSN, posedroutingalgorithmisthatitperiodicallyrotatestherole
the first routing mechanism for Software-Defined Wireless of the relay node among the sensor node’s neighbors, as it
SensorNetworks(SDWSNs)thatleveragestheNaïveBayes is based on time-varying features, such as the battery level.
algorithm, widely recognized for its effectiveness in clas- This fosters equitable traffic distribution among neighbors,
sification tasks within Machine Learning (ML) [21]. The resulting in balanced energy consumption and significantly
algorithmisgroundedinBayes’theorem,awell-established extendingtheoverallnetworklifespan.
probabilisticmodelalsoknownastheconditionalprobability In addition to our main contribution, our study makes
theorem.Owingtoitslightweightnatureandcomputational severaladditionalresearchcontributions,summarizedasfol-
efficiency[22],theNaïveBayes–basedapproachenablesthe lows:
SDNcontrollertomakeroutingdecisionsmorerapidlythan
conventionalalgorithms,therebyimprovingnetworkrespon- • Wepresentacomprehensivereviewoftheroutingpro-
sivenessandenergyefficiency. tocolsproposedforSDWSNs,analyzingtheirstrengths,
NB-SDWSN achieved notable improvements in overall weaknesses, and key design factors such as load bal-
network performance [20]. However, similar to most exist- ancing, energy efficiency, and congestion avoidance.
ing routing algorithms developed for SDWSNs, it did not In contrast to prior surveys that focus mainly on
considertwocriticalparameters—nodebufferoccupancyand algorithms sharing a similar concept to the proposed
VOLUME13,2025 207279

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
method, our review spans a broad spectrum of rout- TABLE2. Anexampleofaflowtable.
| ing approaches   | based      | on various | design      | principles. |     |     |     |     |     |
| ---------------- | ---------- | ---------- | ----------- | ----------- | --- | --- | --- | --- | --- |
| Furthermore,     | we examine | these      | algorithms  | based on    |     |     |     |     |     |
| often-overlooked | factors    | in the     | literature, | such as the |     |     |     |     |     |
volumeofcontroltraffictheygeneratewithintheWSN.
Thisthoroughreviewoffersresearchersandpractition-
erswell-informedguidanceforselectingandoptimizing
routingprotocolsforSDWSNsacrossdiversescenarios
andtrafficconditions.
•
| We undertake  | one of     | the first  | investigations | into the |     |     |     |     |     |
| ------------- | ---------- | ---------- | -------------- | -------- | --- | --- | --- | --- | --- |
| effectiveness | of routing | algorithms | based          | on Naïve |     |     |     |     |     |
Bayes theory for SDWSNs. Our primary contribution II. SOFTWARE-DEFINEDWIRELESSSENSORNETWORKS
| lies in the | design and | implementation | of  | a novel rout- | (SDWSNS) |     |     |     |     |
| ----------- | ---------- | -------------- | --- | ------------- | -------- | --- | --- | --- | --- |
ing algorithm within a framework that combines SDN SDWSNs consist of two main components: the data plane
|     |     |     |     |     | and the control |     | plane, as shown | in Fig. 2. | The data plane |
| --- | --- | --- | --- | --- | --------------- | --- | --------------- | ---------- | -------------- |
withWSNs.Tothisend,weselectedSoftwareDefined
|     |     |     |     |     | encompasses | the | WSN, consisting | of sensor | nodes respon- |
| --- | --- | --- | --- | --- | ----------- | --- | --------------- | --------- | ------------- |
NetworkinginWIrelessSensornEtworks(SDN-WISE)
[3], one of the most widely used platforms for SDN- sible for collecting and forwarding data to the sink, which
|     |     |     |     |     | then transmits | the | received data | via the Internet | to a remote |
| --- | --- | --- | --- | --- | -------------- | --- | ------------- | ---------------- | ----------- |
basedWSNs.Weintroduceminimalmodificationstothe
originalSDN-WISEdatastructuresandpacketformats server,allowingtheendusertoaccessit.Thecontrolplane,
tohandlethefundamentaloperationalprinciplesofour on the other hand, houses the centralized controller. Both
|     |     |     |     |     | planes communicate |     | with each | other using | control packets |
| --- | --- | --- | --- | --- | ------------------ | --- | --------- | ----------- | --------------- |
proposedroutingalgorithm.
• Whilemostroutingalgorithmshavebeenevaluatedonly defined by the OpenFlow protocol [24]. Unlike traditional
|                |       |            |          |             | WSNs, where | nodes | independently | determine | routes to the |
| -------------- | ----- | ---------- | -------- | ----------- | ----------- | ----- | ------------- | --------- | ------------- |
| in small-scale | WSNs, | this study | examines | the perfor- |             |       |               |           |               |
manceofexistingapproaches—alongwiththeproposed sink,SDWSNsleveragethecontrolplanetoproactivelycom-
algorithm—insmallaswellaslarge-scaleWSNdeploy- pute and communicate, for each node, its path to the sink.
Thisapproachalleviatessensornodesfromtheburdenofthe
ments.
• Weperformextensivesimulationsanduseseveralmet- routing process, conserving their energy and consequently
extendingthenetwork’slifetime.
| rics to evaluate | and compare | the | performance | of our |     |     |     |     |     |
| ---------------- | ----------- | --- | ----------- | ------ | --- | --- | --- | --- | --- |
proposedroutingalgorithmwithothersbasedondiverse
| designparadigms.Thiscontrastswithmostpriorstudies, |     |     |     |     | A. DATAPLANE |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
whichtypicallybenchmarktheiralgorithmsonlyagainst Thedataplane,whichcomprisesthesensornodes,isrespon-
methodsbuiltonsimilarunderlyingconcepts. sible for executing packet processing and forwarding based
•
Nearlyallresearchworksproposingroutingalgorithms on locally stored rules. Each node in the WSN maintains a
for SDWSNs have omitted evaluating the amount of flowtable(routingtable)initsmemory,asshowninTable2.
control traffic generated by their approaches in WSNs. Thistablecontainsmultiplepre-installedentries,referred
Acknowledgingthecriticalimpactofcontroltrafficon toasfloworroutingrules.Aflowruleconsistsoffourfields:
overall network performance, we conduct a thorough packettype,action,relaynode,andcounter.Thefieldpacket
assessment and comparison of the control traffic intro- type specifies the type of packet (control or data) that the
duced by our proposed routing algorithm relative to routing rule handles. The action field defines the operation
existingsolutions. (forward,drop,ormodify)tobeperformedonapacketwhen
itstypematchesthatoftheroutingrule.Iftheforwardaction
The remainder of the paper is structured as follows. is specified in the routing rule, the packet is sent through
Section II introduces the SDN paradigm in the context of the neighbor indicated in the relay node field. This field is
WSNs. Section III presents a comprehensive review of the periodically updated as the controller regularly selects the
routing algorithms designed for controllers in SDWSNs. bestneighbortoactastherelaynodeforthesensornode.The
SectionIVprovidesanoverviewoftheNaïveBayestheory, counterfieldcollectsstatistics,suchasthenumberoftimesa
theprobabilisticframeworkemployedbytheproposedrout- packetmatchestheflowruleorthenumberoftimestheflow
ing algorithm to make routing decisions under uncertainty. rulehasbeenupdated.
SectionVdescribesthedesignandoperationsoftheproposed Whenanodegeneratesorreceivesapacket,itfirstdeter-
routingalgorithm.SectionVIoutlinesthesimulationmodel, mines the packet type and checks its flow table for a rule
system parameters, and metrics used in our performance specifying how to handle that type. If a match is found, the
evaluation. It then presents a performance evaluation of our actiondefinedintheroutingruleisappliedtothepacket,and
routing algorithm, comparing it with the well-established the flow rule’s counter is incremented by one. In rare cases
shortest path, EASDN, NB-SDWSN, and RL-based routing where no match exists (e.g., a new traffic type), the node
algorithms. Finally, Section VII concludes the paper and requestsanupdatedflowrulefromthecontrollerviathesink.
proposespotentialavenuesforfutureresearch. Thecontrollerrespondsbysendinganewflowrule,whichis
| 207280 |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
|     |     |     | FIGURE2. | TheSDWSNsystemarchitecture. |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
storedinthenode’sflowtabletohandlefuturepacketsofthat gratingacentralizedSDNcontroller,accessibleviaanetwork
type. (e.g., the Internet), into WSNs, administrators can remotely
|     |     |     |     |     |     |     | manage sensor   | nodes | by   | writing   | configuration |      | programs | at     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | ---- | --------- | ------------- | ---- | -------- | ------ |
|     |     |     |     |     |     |     | the controller, | which | then | transmits |               | them | directly | to the |
B. CONTROLPLANE
nodes,eliminatingtheneedforphysicalaccesstoeachnode.
Thecontrolplaneiscomposedofacentralizedcontrollerthat AnotherdrawbackoftraditionalWSNsthatSDNcanover-
overseesthenetworkandmakeshigh-levelroutingdecisions.
|                 |         |         |             |         |                    |            | come is their | weak        | security. | In          | conventional |                 | WSNs, | data is  |
| --------------- | ------- | ------- | ----------- | ------- | ------------------ | ---------- | ------------- | ----------- | --------- | ----------- | ------------ | --------------- | ----- | -------- |
| The controller, |         | unlike  | the sensor  | nodes,  | is a resource-rich |            |               |             |           |             |              |                 |       |          |
|                 |         |         |             |         |                    |            | typically     | transmitted | without   |             | encryption,  | allowing        |       | unautho- |
| device with     | no      | energy  | constraints | and     | can efficiently    | man-       |               |             |           |             |              |                 |       |          |
|                 |         |         |             |         |                    |            | rized devices | to          | access    | the network |              | and communicate |       | with     |
| age the         | complex | routing | task.       | To this | end, the           | controller |               |             |           |             |              |                 |       |          |
sensornodes.Thisexposesthenetworktoattacks,including
periodically receives status updates from the sensor nodes theinterceptionandmodificationofpackets.SDNmitigates
| via the      | sink. These | updates    |          | include vital | metrics           | such as |                 |              |     |             |          |     |             |            |
| ------------ | ----------- | ---------- | -------- | ------------- | ----------------- | ------- | --------------- | ------------ | --- | ----------- | -------- | --- | ----------- | ---------- |
|              |             |            |          |               |                   |         | these risks     | by enforcing |     | security    | policies |     | at the      | controller |
| the distance | to the      | sink       | and the  | battery       | level. Based      | on this |                 |              |     |             |          |     |             |            |
|              |             |            |          |               |                   |         | level, enabling | end-to-end   |     | encryption, |          | and | restricting | com-       |
| information, | the         | controller | executes | a             | routing algorithm | to      |                 |              |     |             |          |     |             |            |
municationtoauthorizeddevicesonly[25],[26].
| determine | the best | neighbor |     | for each | node to | serve as its |        |           |          |     |            |     |               |     |
| --------- | -------- | -------- | --- | -------- | ------- | ------------ | ------ | --------- | -------- | --- | ---------- | --- | ------------- | --- |
|           |          |          |     |          |         |              | In the | following | section, |     | we present | a   | comprehensive |     |
relay for forwarding packets toward the sink. For example, reviewofexistingstudiesintheliteraturethathaveexplored
| when the | controller | runs | a shortest | path | routing | algorithm, |     |     |     |     |     |     |     |     |
| -------- | ---------- | ---- | ---------- | ---- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
theSDWSNconceptintroducedabove.
| it focuses | exclusively |     | on the | distance | to the sink. | It then |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ------ | -------- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
selectsthemostsuitableneighborastherelaynodeforeach
node, specifically the one that requires the fewest hops to III. RELATEDWORK
reach the sink. A routing table, mapping each node to its This section provides a comprehensive review of existing
selected relay node, is then disseminated by the controller routing solutions developed specifically for SDWSNs, with
tothesinkandsubsequentlytothesensornodes.Eachnode a focus on approaches that leverage the centralized control
extracts and learns its assigned relay node from the routing paradigm to optimize routing performance and energy effi-
tableandupdatesitspre-installedflowrulesaccordingly.This ciency.Notethattheacronymsusedinthissection,aswellas
approachensuresthatnodesalwayshaveup-to-daterouting thoseusedthroughoutthemanuscript,arelistedinTable1.
information,enhancingnetworkefficiency. Several studies [3], [4], [5] have proposed shortest-path
In addition to offloading and relieving sensor nodes routing algorithms to be executed by the controller. In this
from the resource-heavy routing tasks, SDWSNs offer sig- approach, each sensor node consistently uses the neighbor
nificant advantages by simplifying node management and closesttothesinkasitsrelay.Thisensuresthatdatapackets
programming. Traditional WSNs are challenging to man- traversetheminimumnumberofintermediatenodes,thereby
age, as administrators must manually configure each node minimizing network latency. However, this strategy leads
toperformspecifictasks.Thisprocessbecomesincreasingly to traffic concentration on a single relay node, resulting in
tediousinlarge-scaleWSNswithnumerousnodes.Byinte- rapid energy depletion of that node. Consequently, while
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 207281 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
shortest-path routing improves latency, it adversely affects control overhead, increasing communication between the
energybalancingandreducestheoverallnetworklifetime. data and control planes, which may introduce delays and
The authors of [6] proposed EASDN, an opportunistic degradenetworkperformance.
routing approach that periodically updates routing paths by The study in [15] proposed five clustering-based rout-
selecting relay nodes based on their distance to the sink ing algorithms for SDN-based WSNs with mixed mobil-
andresidualenergy.Specifically,thecontrolleridentifiesthe ity, incorporating both stationary and mobile nodes. These
neighbors of a sensor node that are closest to the sink and algorithms use five meta-heuristic techniques—Genetic
selects the one with the highest battery level to serve as its Algorithm(GA),ParticleSwarmOptimization(PSO),Impe-
relay. A routing table is then constructed and disseminated rialist Competitive Algorithm (ICA), Grey Wolf Optimizer
via control packets through the sink to the entire network. (GWO),andWOA[29]—andrelyonthreefitnessfunctions
This periodic reassignment of relay nodes enables dynamic to optimize clustering and routing. The first determines the
routing and contributes to extending the network lifetime optimalnumberofclusters,thesecondselectsclusterheads
by avoiding fixed paths. However, the primary reliance basedonresidualenergyandproximity(favoringstationary
on proximity-based neighbor selection limits the potential nodes for stability), and the third identifies energy-efficient
for effective load balancing, especially in cases where a pathsfromclusterheadstothesink.Toreducecontroltraffic,
sensor node has only one suitable neighbor, reducing the thealgorithmsintroducealoyaltymechanismthatstabilizes
algorithm’sbehaviortothatofshortest-pathrouting.Further- clustermembershipformobilenodesbyassuminglowmobil-
more,EASDNincurssubstantialcontroloverheadduetothe ity(0.5m/s).Thisreducesclusterreformationandtherelated
broadcastofroutingtablesforallnodes,leadingtoincreased message exchanges. Overall, the algorithms help maintain
energy consumption, processing delays, and network con- balanced clusters, reduce packet loss by avoiding mobile
gestion. The resulting degradation in efficiency and rise in clusterheads,andimproveenergyefficiencythroughperiodic
latency ultimately counteract the intended improvements in cluster-headrotation.However,theyconvergeslowly,delay-
networklongevityandperformance. ingroutingdecisions,andtheirdependenceonlowmobility
The researchers in [27] introduced another opportunis- limitstheirapplicabilityinhighlydynamicIoTenvironments.
tic routing algorithm where the controller selects optimal In [30], the authors proposed a clustering-based routing
relaynodestothesink,consideringfactorssuchastransmis- algorithm for SDWSNs utilizing the Artificial Bee Colony
siondistance,residualenergy,andhopcount.Theproposed (ABC) algorithm [31], a swarm intelligence optimization
approachmanagestoextendthenetworklifespanbyimple- technique.Initially,sensornodeswiththehighestbatterylev-
mentingarotationalrelaynodestrategyamongagivensensor elsareselectedasclusterheads,andtheremainingnodesare
node’s neighbors, thereby ensuring load balance. Neverthe- assigned to the nearest cluster head based on the Euclidean
less, a limitation of this approach is its reliance on the distance.Subsequently,anewclusterheadisselectedwithin
Euclideandistancefortransmissioncalculations,necessitat- each cluster by identifying the node closest to the cluster’s
ing the knowledge of actual sensor node coordinates. This geometric center, using an ABC-based fitness function that
requirement for geolocation equipment leads to increased minimizesthesumofthedistancestoallotherclustermem-
energy consumption, which can be a drawback in practi- bers. Finally, the algorithm identifies the optimal path from
caldeploymentsofSDWSNs,whichareoftencomposedof eachclusterheadtothesinkbyevaluatingallpossiblepaths
constraineddevicescharacterizedbylimitedbattery,compu- and selecting the one with the lowest energy consumption.
tation,storage,andcommunicationresources. Although this approach reduces latency by favoring geo-
The work in [12] presents a clustering-based routing graphicallyproximatenodes,itintroducesseverallimitations.
algorithm for SDN-based WSNs that leverages the Whale The repeated use of the same path depletes the energy of
Optimization Algorithm (WOA) [28], a metaheuristic opti- theintermediatenodes,therebyshorteningthenetworklife-
mization technique. The algorithm periodically organizes time. Furthermore, since cluster head selection prioritizes
the network into clusters, each managed by a cluster head centrality over battery level, the same node is repeatedly
selected using a fitness function that considers the battery chosen, leading to rapid energy exhaustion and potential
level,localnodedensity,andinter-nodedistances.Theclus- cluster disconnection. This results in increased packet loss,
ter heads act as relay nodes, forwarding data and control reduced throughput, and degraded overall network perfor-
packets from their respective cluster members to the sink. mance. Additionally, the frequent communication between
This approach promotes energy efficiency and extends the nodes and the SDN controller, combined with the compu-
network lifetime by rotating the cluster head role among tational demands of the ABC algorithm, introduces routing
nodes,therebydistributingthecommunicationload.Despite delays,particularlyinlarge-scaleWSNdeployments.
thesebenefits,theapproachsuffersfromhighcomputational The first fuzzy logic-based routing algorithm for
complexity due to its hybrid design, which combines WOA SDWSNs, as proposed in [32], uses multiple node
with genetic mutation operations. This complexity limits parameters—remainingenergy,bufferoccupancy,andnum-
scalability, particularly in large-scale WSNs. Moreover, the berofneighbors—toinformroutingdecisions.Thealgorithm
repeated cluster formation process generates considerable employsasetofIF-THENrulestoassessnodesuitabilityas
207282 VOLUME13,2025

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
arelay,translatingnumericalparametervaluesintolinguistic identifyenergy-efficientroutes,prioritizingnodeswithhigh
fuzzy values (e.g., low, medium, high) based on predefined residual energy and avoiding those with low energy levels,
thresholds. Each neighbor’s parameters are evaluated using thusextendingthenetworklifespan.However,thisproposed
theserules,andacorrespondingnumericalcostiscomputed method might opt for longer routes compared to traditional
to determine the most suitable relay node. This approach shortest-path algorithms, potentially increasing the packet’s
enables periodic reassignment of relay roles among neigh- journeytothesinkintermsofhopcounts.Additionally,the
bors,promotingbalancedtrafficdistribution,uniformenergy scalabilityofthemodelislimitedbyitstrainingonaspecific
consumption,andimprovednetworklifetime.Byincorporat- setofWSNtopologies,leadingtopotentiallyinaccurateroute
ingbufferoccupancy,thealgorithmalsohelpspreventnode predictionsforunencounterednetworklayouts.
overload and congestion, thereby reducing packet loss and Thestudyin[38]suggestedaroutingalgorithmdesigned
latency. However, it does not consider the distance to the tominimizeend-to-enddelaybyleveragingMLtechniques,
sink,potentiallyselectingdistantrelaynodesandincreasing specificallyRLandArtificialNeuralNetworks(ANNs)[39].
end-to-end latency. Moreover, as the WSN size increases, Thisalgorithmtrainsamodelonadatasettopredictrouting
fuzzy computations and associated control traffic impose pathsforsensornodesinactualnetworkenvironments,aim-
significant computational and communication overheads on ingtoreducedelayandenhancethroughput,whichiscrucial
the controller, delaying routing decisions. These delays can forreal-timeIoTapplications.However,anotablelimitation
resultintheprolongeduseofthesamerelaynode,leadingto of this approach is its lack of consideration for the energy
energydepletionandreducednetworklongevity. levelsofthenodesinthepredictedpaths.Thisoversightmay
Several studies [7], [8], [9], [10] have proposed routing resultintheselectionofnodeswithlowresidualenergy,risk-
algorithms for SDWSNs using RL, particularly the Q- ing premature energy depletion and potentially diminishing
learningalgorithm[33].Thesealgorithmsperiodicallyupdate thenetworklifespan.
routingconfigurationsthroughatwo-phaseprocessinvolving Inourpreviouswork[20],weintroducedapreliminaryver-
routingtablegenerationanditerativelearning.Thecontroller sionofaroutingalgorithmbasedonNaïveBayestheory.The
first generates all possible combinations of routing tables, initialapproachconsideredonlytwonodefeatures—battery
each mapping sensor nodes to relay nodes based on their levelanddistancetothesink—forrelaynodeselection.This
neighborhoodinformation.Aroutingtableisthenrandomly studyextendsthatworkbyincorporatingtwoadditionalfea-
selected and disseminated across the network via the sink. tures: buffer occupancy and link quality. These features are
Sensornodesusetheassignedrelaynodestotransmitdatafor criticalbecausetheyenablethealgorithmtoavoidselecting
a fixed duration, during which performance metrics—such relay nodes that are either overloaded or exhibit poor link
as packet delivery success, delay, and residual energy— quality, thereby mitigating network congestion, minimizing
are collected and aggregated into a reward value. Based on latency, and reducing packet loss. Furthermore, the litera-
this reward, the controller either retains the current routing ture review in the previous study of [20] was limited, as it
configuration or initiates another iteration to select a new covered only four studies that proposed routing algorithms
routing table. This periodic adjustment promotes load bal- for SDWSNs. The present study addresses this limitation
ancingbyrotatingtherelayresponsibilitiesamongneighbors, by providing a comprehensive review of the existing rout-
resultinginmoreuniformenergyconsumptionandextended ing algorithms for SDWSNs based on various underlying
network lifetime. However, the RL-based approach suffers concepts. In addition, the evaluation in the earlier work
from several limitations. During the learning phase, nodes was restricted to a comparison with a single routing pro-
continuouslyexchangestateinformationwiththecontroller, tocol. In contrast, the present study evaluates the proposed
which in turn sends action updates (i.e., routing tables) and algorithm against multiple routing protocols, each based on
reward feedback. This process generates significant con- a different paradigm. Moreover, the previous study did not
trol traffic, leading to increased energy consumption at the analyzethecontroloverheadintroducedwithintheWSNby
nodesandcontributingtonetworkcongestion,higherlatency, theproposedroutingprotocolortheoneusedforcomparison.
and packet loss. Moreover, the convergence process is slow The current work incorporates an analysis of the generated
andscalespoorlywithnetworksize,oftenrequiringnumer- controltraffic,recognizingitssubstantialimpactontheover-
ous iterations to identify an optimal routing configuration. allWSNperformance.
Inlargernetworks,thealgorithmmayfailtoconverge,caus- Table 3 provides a summary of the various routing algo-
ing certain nodes to be repeatedly selected as relays, which rithmsproposedforSDWSNs,evaluatingeachbasedonthe
accelerates their energy depletion and reduces overall net- followingkeyaspects:
workperformance.
The work of [34] presented a routing algorithm using
DeepReinforcementLearning(DRL)[35],whichcombines • Loadbalancingawareness:assesseswhethertherout-
principles of RL and Deep Learning (DL) [36], specifi- ingalgorithmensuresthatsensornodesevenlydistribute
cally through the use of Convolutional Neural Networks traffic among neighboring nodes, promoting uniform
(CNNs) [37]. This algorithm uses a trained CNN model energy consumption and extending network lifetime.
based on a dataset comprising various WSN topologies to Additionally,itdetermineswhetherthealgorithmrotates
VOLUME13,2025 207283

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
TABLE3. AsummaryoftheroutingalgorithmsproposedforSDWSNs,comparedusingeightcriteria.
theroleoftherelaynodeamongasensornode’sneigh- WSN. Minimizing communication overhead between the
bors. controllerand sensornodesiscrucial, asexcessivecommu-
• Energy awareness: examines whether the routing nicationdegradesnetworkperformancebyincreasingenergy
algorithm considers the battery level when making a consumption, reducing longevity, overloading nodes, and
routing decision, specifically when selecting the most causingcongestion.Theseissuesleadtopacketloss,delaysat
suitableneighbortoactasarelaynodeforagivensensor thenodes,andultimatelyhighernetworklatency.Moreover,
node. most existing studies have not provided a comprehensive
• Congestion awareness: evaluates whether the routing performance evaluation of their routing algorithms for both
algorithm considers the buffer occupancy during the small- and large-scale network deployments. Assessing a
routingprocess. routingalgorithmundervariousscenariosisvital,asithelps
• Latency awareness: determines whether the routing identify its limitations and determine the conditions under
algorithmconsidersthedistancetothesinkwhenchoos- which it performs well and those under which it does not
ingarelaynode. performwell.This,inturn,allowsforabetterunderstanding
• Linkqualityawareness:indicateswhethertherouting of the WSN applications for which the routing algorithm is
algorithmtakesthelinkqualityintoconsiderationinthe mostsuitable.
routingdecision. AnotherimportantobservationfromTable3isthatseveral
• Generatedcontroltraffic:reflectstheamountofcon- studies have overlooked the buffer status of the interme-
troltrafficgeneratedbytheroutingalgorithmwithinthe diate nodes when making routing decisions. This omission
WSN. increasesthelikelihoodofthecontrollerselectingpathsthat
• Networksize:definesthesizeoftheWSNunderwhich traverse overloaded or congested nodes, resulting in higher
thealgorithmisevaluated.Asin[3]and[6],aWSNwith network latency, increased packet loss, and reduced overall
more than 32 nodes is considered large, while a WSN throughput.Moreover,thesestudiesoftenneglectlinkquality
with32nodesorfewerisconsideredsmall. when determining routes to the sink, frequently producing
• Convergence time: indicates how quickly the routing paths with poor-quality links that further exacerbate packet
algorithm determines the relay nodes for all sensor loss.Toillustratetheimpactofconsideringthesefeatureson
nodes. WSNperformance,Table4isprovided.Additionally,many
existing routing protocols do not incorporate probabilistic
Table 3 reveals that only a few routing approaches for models for real-time adaptation to dynamic network condi-
SDWSNseffectivelyachieveloadbalancingandensureuni- tions,leadingtosuboptimalroutingdecisionsthatadversely
form energy consumption across nodes to extend network affectnetworkreliability,energyefficiency,andoveralllifes-
lifespan while generating minimal control traffic within the pan.
207284 VOLUME13,2025

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
TABLE4. NodefeaturesandtheirroleinroutingandimpactonWSN approach enables the computation of posterior probabili-
performance. ties in closed form, thereby avoiding iterative optimization
|     |     |     |     |     |     |     | or  | model | training. | Such | analytical |     | efficiency | is  | particu- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | ---- | ---------- | --- | ---------- | --- | -------- |
larlyadvantageousinSDWSNs,wherenodesoperateunder
|     |     |     |     |     |     |     | severe | constraintsin |     | termsof |     | computation,communication, |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------- | --- | ------- | --- | -------------------------- | --- | --- | --- |
memory,andenergy.Comparedwithalternativeapproaches
|     |     |     |     |     |     |     | such     | as  | linear regression, |     | which  | relies         | on  | numerical | opti- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------------ | --- | ------ | -------------- | --- | --------- | ----- |
|     |     |     |     |     |     |     | mization |     | and assumes        |     | linear | relationships, | or  | decision  | tree  |
algorithms,whichrequirerecursivepartitioningandstorage
|     |     |     |     |     |     |     | of  | hierarchical | structures, |     | the | analytical | Naïve | Bayes | model |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | --- | ---------- | ----- | ----- | ----- |
achievesfasterinferencewithminimaloverhead[40].More
|     |     |     |     |     |     |     | complex |     | methods | like | support | vector | machines | and | deep |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | ---- | ------- | ------ | -------- | --- | ---- |
learningmodelsdemandsubstantialcomputationalresources
andlargetrainingdatasets,makingthemimpracticalincon-
|     |     |     |     |     |     |     | strained |     | environments |     | [41]. | Similarly, | fuzzy | logic | systems |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------ | --- | ----- | ---------- | ----- | ----- | ------- |
requireextensiveruledefinitionandparametertuning,which
|     |     |     |     |     |     |     | increases |     | implementation |     | complexity |     | [42]. | Therefore, | the |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------------- | --- | ---------- | --- | ----- | ---------- | --- |
analyticalNaïveBayesmodelprovidesaneffectivetrade-off
|     |     |     |     |     |     |     | between |     | accuracy, | computational |     | efficiency, |     | and scalability, |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --------- | ------------- | --- | ----------- | --- | ---------------- | --- |
enablingreal-timeprobabilisticdecision-makinginresource-
constrainedSDWSNs.
|     |     |     |     |     |     |     |       | The Naïve | Bayes | algorithm |                | is a probabilistic |       | reasoning |         |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | ----- | --------- | -------------- | ------------------ | ----- | --------- | ------- |
|     |     |     |     |     |     |     | model | widely    | used  | for       | classification |                    | tasks | across    | various |
Motivatedbytheaforementionedobservations,thispaper domains, including medical diagnosis, spam filtering, and
| presents | a novel | routing | algorithm | for | SDWSNs | based on |                                          |     |     |     |     |     |     |             |          |
| -------- | ------- | ------- | --------- | --- | ------ | -------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | -------- |
|          |         |         |           |     |        |          | decision-makingunderuncertainty[43].Letc |     |     |     |     |     |     | 1 ,c 2 ,c 3 | ,...,c i |
NaïveBayestheory,whichleveragesprobabilisticinference denotetheipossibleclasses.TheobjectiveoftheNaïveBayes
capabilities well-suited for classification tasks under uncer- algorithmistodeterminethemostprobableandappropriate
tainconditions.Unliketheexistingapproachesdiscussedin class c i for a given instance, based on a set of observed
the literature review, the proposed algorithm aims to mini- features X = {x , x , x , ..., x}. This classification prob-
|     |     |     |     |     |     |     |     |     |     | 1 2 | 3   | j   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mizecommunicationoverhead,preventnetworkcongestion,
|     |     |     |     |     |     |     | lem | is addressed |     | using | Bayes’ | theorem | [44], | also known | as  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | ------ | ------- | ----- | ---------- | --- |
improveoverallthroughput,andreducenetworklatencyand the conditional probability theorem, which provides a for-
packetlossbyincorporatingfeaturesoftenomittedinprevi-
|     |     |     |     |     |     |     | mal | mathematical |     | framework |     | for computing |     | the probability |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | --- | ------------- | --- | --------------- | --- |
ousstudies,namelylinkqualityandnodebufferoccupancy.
|     |     |     |     |     |     |     | P(c|X), |     | i.e., the | probability |     | of class | c given | the observed |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --------- | ----------- | --- | -------- | ------- | ------------ | --- |
|     |     |     |     |     |     |     |         | i   |           |             |     |          | i       |              |     |
Moreover, it enhances the overall network lifespan through features X. Assuming the conditional independence of the
effectiveloadbalancing.
|     |     |     |     |     |     |     | features |     | x 1 , x 2 , | x 3 , ..., | x j given | the class | c, i | the probability |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------- | ---------- | --------- | --------- | ---- | --------------- | --- |
Owing to the lightweight and computationally efficient P(c|X)iscomputedasfollows:
i
| characteristics |     | of the | Naïve Bayes | algorithm, |     | the proposed |     |     |     |     |     |     |     |         |         |
| --------------- | --- | ------ | ----------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | ------- | ------- |
|                 |     |        |             |            |     |              |     |     |     |     |     |     |     | (cid:0) | (cid:1) |
algorithmprovidesapracticalsolutionforreal-timedecision- P(c |X)=P(c |x )×P(c |x )×...×P c |x (1)
|     |     |     |     |     |     |     |     | i   |     | i   | 1   | i 2 |     | i   | j   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
making,therebyenhancingresourceallocationandensuring
TheconditionalprobabilityP(c|x)iscalculatedasfollows:
| reliable data | transmission |     | within | SDWSNs. | By  | integrating |     |     |     |     |     | i j |     |     |     |
| ------------- | ------------ | --- | ------ | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a probabilistic approach, the proposed algorithm not only (cid:0) (cid:1)= P(x |c )×P(c )
|     |     |     |     |     |     |     |     |     |     | P c |x |     | j i | i   |     | (2) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
mitigates the inefficiencies of traditional routing techniques i j
|            |          |         |             |     |          |             |     |       |                                                 |     |     | P(x) | j   |     |     |
| ---------- | -------- | ------- | ----------- | --- | -------- | ----------- | --- | ----- | ----------------------------------------------- | --- | --- | ---- | --- | --- | --- |
| but also   | improves | network | performance |     | by       | dynamically |     |       |                                                 |     |     |      |     |     |     |
|            |          |         |             |     |          |             |     | • P(c | |x )istheposteriorprobability,whichindicateshow |     |     |      |     |     |     |
| optimizing | routing  | paths   | in response | to  | changing | network     |     | i     | j                                               |     |     |      |     |     |     |
conditions. To better understand the underlying principles likely the class c i is to be selected given the observed
|     |     |     |     |     |     |     |     | featurex | .   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
that enable such adaptability and efficiency, the following j
• |c
sectionpresentsthetheoreticalfoundationoftheNaïveBayes P(x j i )isthelikelihoodofobservingthefeaturex j given
algorithm, detailing its probabilistic model and relevance to thattheclassc hasbeenselected.
i
|                              |     |     |     |     |     |     |     | • P(c | )isthepriorprobabilityofclassc |     |     |     | ,independentof |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------------------------ | --- | --- | --- | -------------- | --- | --- |
| theproposedroutingmechanism. |     |     |     |     |     |     |     | i     |                                |     |     |     | i              |     |     |
anyobservedfeatures.
• P(x)isthemarginalprobabilityofobservingthefeature
| IV. NAÏVEBAYESTHEORY |     |     |     |     |     |     |     | j   |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x
| Inthisstudy,theNaïveBayesformulationisemployednotas |     |     |     |     |     |     |     | j . |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a data-driven ML classifier but as an analytical probabilis- InthecontextofroutinginSDWSNs,weemploytheNaïve
tic inference model. The likelihood and prior probabilities Bayes algorithm to select the most appropriate neighbor
areexpressedusingmathematicalformulationsderivedfrom (class) from a set of candidate neighbors (classes) to serve
node features rather than from empirical training data. This asarelaynodeforagivensensornodeinforwardingpackets
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 207285 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
toward the sink. This selection process involves computing TABLE5. Listofsymbols.
theposteriorprobabilityofeachneighborbeingchosenasa
| relay node | given | its features, |     | namely | battery | level, | distance |     |     |     |     |
| ---------- | ----- | ------------- | --- | ------ | ------- | ------ | -------- | --- | --- | --- | --- |
tothesink,bufferoccupancy,andlinkquality.Thesefeatures
| serve as               | prior   | knowledge | in the                        | computation. |              | The neighbor |        |     |     |     |     |
| ---------------------- | ------- | --------- | ----------------------------- | ------------ | ------------ | ------------ | ------ | --- | --- | --- | --- |
| with the               | highest | posterior | probability                   |              | is then      | assigned     | as     |     |     |     |     |
| the best               | relay   | node for  | the sensor                    | node.        | For          | example,     | the    |     |     |     |     |
| probabilityofneighborN |         |           | 1 beingdesignatedasarelaynode |              |              |              |        |     |     |     |     |
| for sensor             | node    | S , given | N ’s                          | features,    | is expressed |              | as the |     |     |     |     |
|                        |         | 3         | 1                             |              |              |              |        |     |     |     |     |
|battery
| posterior             | probability: | P(N              | 1            | level | N1 ,            | distance      | to the |     |     |     |     |
| --------------------- | ------------ | ---------------- | ------------ | ----- | --------------- | ------------- | ------ | --- | --- | --- | --- |
| sink ,bufferoccupancy |              |                  | ,linkquality |       | N1,S3           | ).Thedetailed |        |     |     |     |     |
| N1                    |              |                  | N1           |       |                 |               |        |     |     |     |     |
| computation           | of           | this probability |              | and   | the integration |               | of the |     |     |     |     |
NaïveBayesalgorithmintotheproposedroutingframework
aredescribedinthefollowingsection.
V. PROPOSEDROUTINGALGORITHM
| Our routing   | algorithm, |                      | which | we denote  | as  | Naïve    | Bayes- |     |     |     |     |
| ------------- | ---------- | -------------------- | ----- | ---------- | --- | -------- | ------ | --- | --- | --- | --- |
| based routing |            | for Software-Defined |       | Networking |     | (NBSDN), |        |     |     |     |     |
hasbeenimplementedwithintheSDN-WISEframework[3].
Inthissection,wepresentacomprehensiveoverviewofthe
processesandoperationsperformedbythenodes(dataplane)
| and the         | controller | (control      | plane) | in            | SDN-WISE. |           | We also |     |     |     |     |
| --------------- | ---------- | ------------- | ------ | ------------- | --------- | --------- | ------- | --- | --- | --- | --- |
| provide         | a detailed | description   |        | of our        | routing   | algorithm | and     |     |     |     |     |
| its two phases: |            | (1) selecting | the    | best neighbor |           | for each  | sen-    |     |     |     |     |
| sor node        | to serve   | as its        | relay  | node using    | the       | Naïve     | Bayes   |     |     |     |     |
algorithmwithmultiplefeatures,includingthebatterylevel,
and(2)utilizingtheoutputofthefirstphasetoconstructand
transmitroutingpathstothesensornodes,enablingthemto
learntheirrelaynodesforforwardingpacketstowardthesink.
Lastly,inthissection,astep-by-stepexampleoftherouting
| algorithm  | operating | in  | a WSN   | with four | nodes | is provided |        |     |     |     |     |
| ---------- | --------- | --- | ------- | --------- | ----- | ----------- | ------ | --- | --- | --- | --- |
| to clearly | highlight | the | way our | approach  | works | for         | better |     |     |     |     |
understanding.
Forreference,Table5providesacomprehensivelistofthe
symbolsusedthroughoutthisstudy,orderedalphabetically.
A. DATAPLANE
1) DISCOVERINGNEIGHBORINGNODES
| Each node,                  | whether | it  | is a sensor | or sink      | node, | creates       | and |     |     |     |     |
| --------------------------- | ------- | --- | ----------- | ------------ | ----- | ------------- | --- | --- | --- | --- | --- |
| sendsabeaconpacket[3]everyT |         |     |             | beaconpacket |       | secondstoeach |     |     |     |     |     |
nodewithinitscommunicationrange.Inthisbeaconpacket,
thenodeincludesitsaddress,itsdistancetothesink,andthe
| address | of the  | sink. The | representation |       | of a         | node’s | address |     |     |     |     |
| ------- | ------- | --------- | -------------- | ----- | ------------ | ------ | ------- | --- | --- | --- | --- |
| (sensor | or sink | node) is  | presented      | below | in ‘‘Address |        | of the  |     |     |     |     |
node’’.Notethatinthebeaconpacketsgeneratedbythesink,
| it sets its | own | address | in the | field designated |     | for the | sink’s |     |     |     |     |
| ----------- | --- | ------- | ------ | ---------------- | --- | ------- | ------ | --- | --- | --- | --- |
addressandsets0inthefielddesignatedforthedistanceto
• ItverifieswhethernodeB’sdistancetothesink,asindi-
thesink.
|      |      |            |     |        |        |      |         | cated in | the received beacon | packet, is | less than its |
| ---- | ---- | ---------- | --- | ------ | ------ | ---- | ------- | -------- | ------------------- | ---------- | ------------- |
| When | node | A receives | a   | beacon | packet | from | node B, |          |                     |            |               |
distancetothesink,whichissavedinitsmemory.Iftrue,
itperformsthefollowingtasks:
|     |     |     |     |     |     |     |     | it updates | the stored distance | to node B’s | distance plus |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------- | ----------- | ------------- |
• It checks whether node B’s address is already listed in one. It also updates a variable kept in its memory that
itsneighbortable.Ifnot,itaddsnodeB’saddresstothe containsitsclosestneighboringnodetothesink,setting
| table. |     |     |     |     |     |     |     | it to node | B’s address. Node | A utilizes | the neighbor |
| ------ | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | ---------- | ------------ |
• Itacquiresthesink’saddressfromthebeaconpacketand stored in this variable as its relay node to send its data
storesitinitsmemory. and control packets to the sink during the period 0
| 207286 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
≤ T < T , where T denotes the field specifies the address of a neighboring node, retrieved
|     | now | controller | routing |     | now |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
actual time, and T represents the time at from the node’s neighbors list, which was populated during
|     |     |     | controller | routing |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
which the controller begins performing routing opera- the phase ‘‘discovering neighboring nodes’’. Note that the
tions. This behavior occurs because, during this initial address of a node’s neighbor is represented in its dedicated
period, the controller has not yet started performing 2-byte segment in the same manner as described earlier in
routing, as it is in the process of collecting informa- the‘‘Addressofthenode’’field.
| tion | about | the WSN | topology. | However, | from | T ≥ |     |     |     |     |     |     |     |     |
| ---- | ----- | ------- | --------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
now
T controller routing , node A consistently obtains its relay c: BATTERYLEVELOFTHENODE
nodefromthecontrollerandusesittotransmititsdata The battery level field is 1 byte in size and holds an inte-
andcontrolpackets. ger value ranging from 0 to 255, where 0 indicates a fully
depletedbatteryand255representsafullychargedstate.This
Attheendofthisprocess,everynodeintheWSNhasits
neighbor table populated with neighboring nodes within its field serves as a crucial indicator of the node’s remaining
communication range. It has also learned the address of the batterycapacity.
Asstatedin[3],uponactivation,eachsensornode’sbattery
sinkanditsdistancefromit.
hasamaximumcapacityof5000milliCoulombs(mC),and
|     |     |     |     |     |     |     | its energy | consumption |     | results | from | three | primary | activ- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ------- | ---- | ----- | ------- | ------ |
2) REPORTINGNODE’SNEIGHBORSANDFEATURESTOTHE
|     |     |     |     |     |     |     | ities: baseline |     | operation, | packet | transmission, |     | and | packet |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | ------ | ------------- | --- | --- | ------ |
CONTROLLER
|        |     |                                  |     |     |     |     | reception. | Equations |     | (3) to | (5) represent |     | the energy | con- |
| ------ | --- | -------------------------------- | --- | --- | --- | --- | ---------- | --------- | --- | ------ | ------------- | --- | ---------- | ---- |
| EveryT |     | seconds,eachnodewithintheWSNgen- |     |     |     |     |            |           |     |        |               |     |            |      |
report packet sumption model adopted in this study, as defined in [3],
eratesandtransmitsareportpacket[3]tothesinkviaitsbest
|     |     |     |     |     |     |     | which quantifies |     | the | reductions | in  | the node’s | battery | level |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ---------- | --- | ---------- | ------- | ----- |
relaynodethatleadstowardthatnode.Thesinkthenforwards
|     |     |     |     |     |     |     | resulting | from | these | activities. | As  | shown | in equation | (3), |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ----- | ----------- | --- | ----- | ----------- | ---- |
thereceivedreportpacketstothecontroller.Itisimportantto
|               |     |               |                               |     |     |     | the sensor | node   | consumes  |         | 6.8 mC   | per second | to         | perform |
| ------------- | --- | ------------- | ----------------------------- | --- | --- | --- | ---------- | ------ | --------- | ------- | -------- | ---------- | ---------- | ------- |
| notethateachT |     | report packet | seconds,thesinkalsocreatesits |     |     |     |            |        |           |         |          |            |            |         |
|               |     |               |                               |     |     |     | baseline   | tasks, | including | sensing | physical |            | quantities | from    |
ownreportpacket.However,unlikethesensornodes,itsends
|     |     |     |     |     |     |     | the surrounding |     | environment, |     | storing | and | processing | col- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------ | --- | ------- | --- | ---------- | ---- |
thispacketdirectlytothecontrollerwithoutpassingitthrough
|     |     |     |     |     |     |     | lected sensory |     | data and | received | packets |     | from neighboring |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | -------- | ------- | --- | ---------------- | --- |
intermediatenodes,asithasadirectlinkwiththecontroller.
|        |          |                  |         |        |               |          | nodes, and                                         | forming | packets. |     | Additionally, |     | sending | a 1-byte |
| ------ | -------- | ---------------- | ------- | ------ | ------------- | -------- | -------------------------------------------------- | ------- | -------- | --- | ------------- | --- | ------- | -------- |
| Within | a report | packet,          | a given | node   | enumerates    | the list |                                                    |         |          |     |               |     |         |          |
|        |          |                  |         |        | ‘‘discovering |          | packetconsumes0.0027mC,whilereceivinga1-bytepacket |         |          |     |               |     |         |          |
| of its | adjacent | nodes identified |         | in the | phase         |          |                                                    |         |          |     |               |     |         |          |
requires0.00094mC.Consequently,transmittingapacketof
| neighboring |     | nodes’’. Thus, | by  | periodically | receiving | all the |     |     |     |     |     |     |     |     |
| ----------- | --- | -------------- | --- | ------------ | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
sizeLbytesdepletesthesensornode’sbatteryby0.0027×L
| report | packets | transmitted | by  | the nodes | in the | WSN, the |     |     |     |     |     |     |     |     |
| ------ | ------- | ----------- | --- | --------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
mC,asdescribedinequation(4).Likewise,receivingapacket
controllercanestablishandmaintainanup-to-daterepresen-
oflengthLbytesreducesthebatterylevelby0.00094×LmC,
tationoftheWSN’stopology.Additionally,thenodesfurnish
asspecifiedinequation(5).
| in the | report | packets details |     | such as their | residual | energy, |     |     |     |     |     |     |     |     |
| ------ | ------ | --------------- | --- | ------------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
bufferoccupancy,distancetothesink,andthequalityoflinks =Batterylevel−6.8
|      |             |        |       |          |              |         | Batterylevel |     |     |     |     |     |     | (3) |
| ---- | ----------- | ------ | ----- | -------- | ------------ | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| with | neighboring | nodes. | These | features | are critical | for the |              |     |     |     |     |     |     |     |
=Batterylevel−0.0027×L
|     |     |     |     |     |     |     | Batterylevel |     |     |     |     |     |     | (4) |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
proposedroutingalgorithm,whichleveragesthemtoidentify
=Batterylevel−0.00094×L
the most suitable neighboring node for each sensor node to Batterylevel (5)
serveasitsrelaynodetowardthesink.Theaforementioned
|     |     |     |     |     |     |     | Initially, | the | battery | level | is a | double-precision |     | value, |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | ----- | ---- | ---------------- | --- | ------ |
fieldsareincludedinthereportpacket.Itisworthnotingthat
|       |             |         |         |        |               |        | requiring     | an 8-byte | field | in the     | report | packet.    | However, | this  |
| ----- | ----------- | ------- | ------- | ------ | ------------- | ------ | ------------- | --------- | ----- | ---------- | ------ | ---------- | -------- | ----- |
| these | fields were | already | present | in the | report packet | of the |               |           |       |            |        |            |          |       |
|       |             |         |         |        |               |        | significantly | increases |       | the length | of     | the report | packet,  | lead- |
originalSDN-WISEimplementation,exceptforthe‘‘Buffer
ingtohigherenergyconsumptionforbothtransmissionand
occupancyofthenode’’field,whichwehaveintroduced.
|     |     |     |     |     |     |     | reception,  | as indicated |     | in equations |     | (4) and | (5).            | To address |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ------------ | --- | ------- | --------------- | ---------- |
|     |     |     |     |     |     |     | this issue, | the nodes    | in  | SDN-WISE     |     | convert | and proportion- |            |
a: ADDRESSOFTHENODE
|     |     |     |     |     |     |     | ally scale | the battery |     | level from | its | original | decimal | range |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ---------- | --- | -------- | ------- | ----- |
Thenode’saddressisrepresentedusing2bytesandhelpsin of 0 to 5000 into an integer (byte) value within the range
| differentiating |          | and distinguishing |      | the node | from           | the others |             |       |          |      |      |         |             |       |
| --------------- | -------- | ------------------ | ---- | -------- | -------------- | ---------- | ----------- | ----- | -------- | ---- | ---- | ------- | ----------- | ----- |
|                 |          |                    |      |          |                |            | of 0 to 255 | using | equation | (6). | As a | result, | the battery | level |
| within          | the WSN. | The first          | byte | serves   | as the address | prefix     |             |       |          |      |      |         |             |       |
nowoccupiesonlyonebyteinthereportpacket,reducingits
andisalwayssetto0.Thesecondbyteisanintegerrepresent-
overalllength.
ingthenode’sidentifier,whichisassignedtothenodeatthe
Batterylevel
startupoftheWSN.Thissecondbyteensurestheuniqueness Batterylevel =Integer part of( ×255) (6)
| ofthenode’saddress,aseachnodeintheWSNhasadistinct |     |     |     |     |     |     |     |     |     |     |     | 5000 |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
identifier.
|     |     |     |     |     |     |     | In this   | equation, | the  | battery | level | is normalized |       | from the |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---- | ------- | ----- | ------------- | ----- | -------- |
|     |     |     |     |     |     |     | range [0, | 5000]     | to a | decimal | value | between       | 0 and | 1, then  |
b: ADDRESSESOFTHENODE’SNEIGHBORINGNODES scaled to the range [0, 255]. The obtained value is passed
This field has a size of 2 × l bytes, where l indicates the throughatruncationfunctiontoremovethedecimalportion,
numberofthenode’sneighbors.Each2-bytesegmentofthis ensuringthatthefinalvalueisaninteger.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 207287 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
|     |     |     | FIGURE3. | AWSNtopologywith5nodesbuiltbythecontrollerbasedonthereceived |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
reportpackets.
Importantly, the sink, in contrast to the sensor nodes, field‘‘Addressesofthenode’sneighboringnodes’’.Avalue
isconstantlypluggedintoanunlimitedpowersource.Thus, of 0 represents the best link quality, while 100 represents
it consistently reports a battery level of 255 in its report the poorest. Each byte of this field functions as a metric
| packets. |     |     |     |     |     |     | indicatinghowfartheneighborisfromthenode.Alowerbyte |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- |
valuecorrespondstoashorterdistancebetweenthenodeand
theneighbor,andviceversa.
d: DISTANCEOFTHENODEFROMTHESINK
|             |       |        |            |        |          |        | To determine | the quality | of the | link | with its ith neighbor, |     |
| ----------- | ----- | ------ | ---------- | ------ | -------- | ------ | ------------ | ----------- | ------ | ---- | ---------------------- | --- |
| This 1-byte | field | stores | an integer | value, | computed | during |              |             |        |      |                        |     |
the phase ‘‘discovering neighboring nodes’’, indicating the thenodeusestheReceivedSignalStrengthIndicator(RSSI)
|     |     |     |     |     |     |     | [45], a widely | used method | for | assessing | the strength | of  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | --- | --------- | ------------ | --- |
numberofhopsrequiredforapackettotraversefromasensor
node to the sink. It serves as a crucial metric, enabling the a received signal in wireless communication systems. The
|     |     |     |     |     |     |     | node measures | the power | of the | signal | received from | its ith |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ------ | ------ | ------------- | ------- |
controllertoassessthenode’sproximitytothesink.
neighbor.Thismeasurementreflectsfactorssuchasdistance,
|     |     |     |     |     |     |     | obstacles, | and environmental | conditions |     | that affect | signal |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | ---------- | --- | ----------- | ------ |
e: BUFFEROCCUPANCYOFTHENODE
|            |          |            |         |            |            |           | propagation. | The measured   | RSSI   | is represented | as a                   | nega- |
| ---------- | -------- | ---------- | ------- | ---------- | ---------- | --------- | ------------ | -------------- | ------ | -------------- | ---------------------- | ----- |
| This field | occupies | one        | byte in | the report | packet     | and con-  |              |                |        |                |                        |       |
|            |          |            |         |            |            |           | tive value,  | where a higher | value  | (i.e.,         | closer to 0) signifies |       |
| tains an   | integer  | reflecting | the     | number     | of packets | currently |              |                |        |                |                        |       |
|            |          |            |         |            |            |           | a stronger   | signal and a   | nearer | neighbor       | to the node.           | The   |
storedinthenode’sreceivingqueue.Incomingpacketsfrom
|             |       |                 |     |          |     |               | obtained  | RSSI value is  | then converted |     | to a positive  | value |
| ----------- | ----- | --------------- | --- | -------- | --- | ------------- | --------- | -------------- | -------------- | --- | -------------- | ----- |
| neighboring | nodes | are temporarily |     | buffered | in  | this queue in |           |                |                |     |                |       |
|             |       |                 |     |          |     |               | using the | absolute value | function       | to  | fit within one | byte, |
theorderofarrivalbeforebeingprocessedandsubsequently
asillustratedintheequationbelow.
forwardedordropped.Themorepacketsanode’sreceiving
|     |     |     |     |     |     |     |     |     |     | =|RSSI | ithneighbor| |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- |
queuecontains,thelongernewincomingpacketsaredelayed Link qualityithneighbor (7)
beforebeingprocessed,increasingnetworklatency.
| The value | of  | this field | is a | key indicator |     | of the node’s |     |     |     |     |     |     |
| --------- | --- | ---------- | ---- | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
B. CONTROLPLANE
workload.Itrangesfrom0to100(themaximumcapacityof 1) CONSTRUCTINGTHEWSNTOPOLOGY
| the node’s | receiving | queue | in  | SDN-WISE, | measured | in the |     |     |     |     |     |     |
| ---------- | --------- | ----- | --- | --------- | -------- | ------ | --- | --- | --- | --- | --- | --- |
UponreceivingareportpacketfromallthenodesintheWSN,
number of packets), where 0 indicates an empty queue and thecontrollerconstructstheWSNtopologyandassignseach
100 indicates a full queue, meaning the node is congested. node its features based on its report packet. These features
Anyadditionalreceivedpacketscannotbehandledandmust
includebatterylevel,distancetothesink,bufferoccupancy,
bedropped,increasingpacketloss. andthequalityoflinkswithneighboringnodes.Anexample
ofaWSNtopologybuiltbythecontrollerisshowninFig.3.
f: LINKSQUALITYWITHNEIGHBORINGNODES
Thisfieldhasalengthoflbytes.Theithbyte,wherei=1,2, 2) EXECUTINGTHENBSDNROUTINGALGORITHM
...,l,holdsanintegervalueintherange[0,100],representing Ourproposedroutingalgorithmconsistsoftwomainphases.
the quality of the wireless link between the node and its Inthefirstphase,thecontrolleridentifiesandselects,foreach
ith neighboring node in its neighbor table, as well as in the sensornodeintheWSN,thebestneighbortoactasitsrelay
| 207288 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
nodetoforwarditspacketstothesink.Inthesecondphase, The value of the feature ‘‘battery level’’ (BL ) is nor-
Nj
the controller constructs routing paths based on the results malized using equation (8). The normalized battery level is
of the first phase and then transmits them to the data plane labeledasbl .
Nj
(WSN), enabling the sensor nodes to learn their best relay
1
node selected by the controller. Both phases are executed bl Nj = 255−BL (8)
periodically every T seconds. Consequently, Nj
controller routing
after each T controller routing second, a different neighboring Intheaboveequation,theexpression255-BL Nj computes
node may serve as the relay node for a given sensor node. the amount of battery consumed by the neighbor N j . The
This mechanism enables a sensor node to evenly distribute obtained valueis then invertedso thatthe neighbor thathas
its traffic among its neighbors, leading to balanced energy consumed the least amount of its battery has the highest
consumptionandanextendednetworklifetime. normalizedbatterylevelvalueandconsequentlythehighest
LetusconsideraWSNcomprisingnnodes:onesinknode, probability of being selected as the relay node for node S i .
referredtoasS ,andasetofsensornodesdenotedasSensor Avoidingtheselectionofaneighborwithalowbatterylevel
1
nodes, where Sensor nodes = {S , S , ..., S }. Each node asarelaynodepreventsitsbatteryfromdrainingcompletely,
2 3 n
S, where i = 1, 2, 3, ..., n, possesses a set of neighboring whichwouldcauseittoswitchoff.Thismaintainstheneigh-
i
nodes labeled as Neighboring nodes , where Neighboring boringnodeforanextendeddurationandextendstheoverall
Si
nodes ={N ,N ,N ,...,N },withl beingthetotalcount networklifespan.
Si 1 2 3 l
of the node’s adjacent nodes, and Neighboring nodes Si ⊂ The value of the feature ‘‘distance to the sink’’ (DS Nj )
Sensor nodes ∪S . Node S has four features: battery level is normalized using equation (9). The normalized value is
1 i
(BL Si ),distancetothesink(DS Si ),bufferoccupancy(BO Si ), denotedasds Nj .
andthequalityofthelinkwitheachofitsneighbors(LQ N1,Si , 1
LQ N2,Si ,LQ N3,Si ,...,LQ Nl,Si ). ds Nj = DS (9)
Nj
In equation (9), the distance to the sink is inverted to
ensurethattheclosestneighbortothesink,whichrequiresthe
a: BESTRELAYNODEIDENTIFICATION
minimumnumberofhopstodeliverpacketstothesink,has
The first input to this phase is a complete WSN topology
thehighestnormalizeddistancetothesinkand,therefore,the
graph constructed by the controller during the phase ‘‘con-
highestlikelihoodofbeingchosenastherelaynodefornode
structingtheWSNtopology’’.Thesecondinputtothisphase
is a set of pairs < S, N >, denoted as Selection history, S i .ThisselectionprincipleensuresthatS i ’spacketsreachthe
i
sinkwithlowerdelay,resultinginlownetworklatency.
where N represents the number of times node S has been
i
The value of the feature ‘‘buffer occupancy’’ (BO ) is
selectedasarelaynodeforothernodesbythecontroller.This Nj
normalizedusingequation(10).Thenormalizedbufferoccu-
set can be valuable if multiple neighboring nodes have the
pancyisrepresentedasbo .
sameprobabilityofbeingselectedasthebestrelaynodefor Nj
agivensensornode.Insuchcases,thecontrollerresolvesthe 1
bo = (10)
tie by selecting the neighboring node that has been chosen Nj BO
Nj
leastfrequentlyasarelayforothernodes,ensuringbalanced
In this equation, the buffer occupancy value is inverted
trafficdistributionacrosstheWSNandtherebyextendingthe
toguaranteethattheneighborwiththefewestpacketsinits
network lifetime. The output of the phase ‘‘best relay node
receivingqueuehasthehighestnormalizedbufferoccupancy
identification’’ is a set of pairs < S, Best relay node >,
i Si value,therebymaximizingitsprobabilityofbeingdesignated
denotedasNBSDNoutput,whereS ∈SensornodesandBest
i as the relay node for node S. Choosing the neighbor with
relaynode ∈Neighboringnodes . i
Si Si the lowest buffer occupancy as the relay node ensures that
ForeachnodeS (S ∈Sensornodes),thecontrollerchecks
i i S’s packets experience minimal waiting time in the relay
if it has the sink S as a neighbor, i.e., S ∈ Neighboring i
1 1 node’s receiving queue before being processed and either
nodes . If true, the controller immediately designates S as
Si 1 forwardedordropped,ornowaitingtimeatallifthequeueis
itsbestrelaynodeandaddsthepair<S,S >totheNBSDN
i 1 empty, thereby reducing overall network latency. Moreover,
output set. It also increments N by one in the pair < S ,
1 thisselectioncriterionavoidsdesignatingasrelaynodesthe
N >storedintheSelectionhistoryset.Otherwise,foreach
neighbors that have a significant number of packets in their
neighbor N of node S (N ∈ Neighboring nodes ), where
j i j Si queue. This prevents overloading them, helps preserve their
j=1,2,3,...,l,thecontrollerperformsthefollowingsteps
energy,andincreasesnetworklifetime.Additionally,itmiti-
1to4:
gatesnodecongestion,therebyminimizingpacketloss.
STEP1:NormalizethefeaturesofneighborN .
ThevaluesofthefeaturesofN arenormalizedt
j
oacom-
The feature ‘‘link quality’’ LQ Nj,Si is normalized using
j equation(11),andtheresultingnormalizedvalueisexpressed
mon scale range of 0 to 1 to prevent any single feature
fromexertingdisproportionateinfluenceduetoitsnumerical
aslq Nj,Si .
range.Thisensuresbalancedcontributionsfromallfeatures, 1
eliminatingbiastowardthosewithlargervalues.
lq Nj,Si =
LQ Nj,Si
(11)
VOLUME13,2025 207289

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
lq
In e q u a t io n ( 1 1) , t he v a l u e o f L Q , i s i nv e rte d s o t h a t (cid:0) |N (cid:1)= Nj ,S i
|     |     |     |     |     |     | N j S i |     |     | P   | lq Nj,Si | j   |     |     |     | (21) |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | -------- | --- | --- | --- | --- | ---- |
the ne i g h b o r w i th t h e lo w e s t li n k q u a l i t y ( R S S I) to S ( i .e . , bl +ds + b o +lq
|     |         |          |     |            |      |     |           | i       |     |     |     | Nj Nj | Nj  | Nj,Si |     |
| --- | ------- | -------- | --- | ---------- | ---- | --- | --------- | ------- | --- | --- | --- | ----- | --- | ----- | --- |
| the | closest | neighbor | to  | the sensor | node | S)  | i has the | highest |     |     |     |       |     |       |     |
Eachlikelihoodiscomputedastheratioofagivenfeature
| normalized |     | link | quality | value, | thus | increasing | its | chance of |     |     |     |     |     |     |     |
| ---------- | --- | ---- | ------- | ------ | ---- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
tothesumofallfeaturesofN,ensuringthatthetotalcontri-
j
| being | assigned |     | as the | relay | node | for S. i | This | guarantees |     |     |     |     |     |     |     |
| ----- | -------- | --- | ------ | ----- | ---- | -------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
butionofallfeaturessumsto1.Thisnormalizationprovides
| the   | reliable   | transmission |        | of    | S’s packets   | to  | its chosen | relay |                                                       |          |       |          |          |          |         |
| ----- | ---------- | ------------ | ------ | ----- | ------------- | --- | ---------- | ----- | ----------------------------------------------------- | -------- | ----- | -------- | -------- | -------- | ------- |
|       |            |              |        |       | i             |     |            |       | arelativemeasureofeachfeature’sinfluenceonthedecision |          |       |          |          |          |         |
| node, | minimizing |              | packet | loss. | Additionally, |     | it ensures | that  |                                                       |          |       |          |          |          |         |
|       |            |              |        |       |               |     |            |       | to select                                             | N as the | relay | node for | S, while | ensuring | that no |
|       |            |              |        |       |               |     |            |       |                                                       | j        |       |          | i        |          |         |
S’spacketsaretransmittedwithlowerdelaytotherelaynode, i
singlefeatureunfairlydominatesorbiasestherelayselection
reducingoverallnetworklatency.
process.
|     | STEP | 2: Compute |            | the   | conditional | probabilityP( |     | N j      |           |      |         |        |              |               |     |
| --- | ---- | ---------- | ---------- | ----- | ----------- | ------------- | --- | -------- | --------- | ---- | ------- | ------ | ------------ | ------------- | --- |
|     |      |            |            |       |             |               |     |          | Equations | (22) | to (25) | define | the marginal | probabilities |     |
| |bl | , ds | , bo       | , lq Nj,Si | ) and | store       | the resulting |     | value in |           |      |         |        |              |               |     |
Nj Nj Nj of the features bl , ds , bo , and lq Nj,Si for the neighbor
| anarraydenotedasProbabilities. |     |     |     |     |     |     |     |     |     |     | Nj Nj | Nj  |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
N.Theseprobabilitiesrepresenttherelativecontributionof
|            |                  |              |     | |bl      |        |              |                |            | j                       |      |            |        |              |     |           |
| ---------- | ---------------- | ------------ | --- | -------- | ------ | ------------ | -------------- | ---------- | ----------------------- | ---- | ---------- | ------ | ------------ | --- | --------- |
|            | TheexpressionP(N |              | j   | Nj ,ds   | Nj ,bo | Nj ,lq Nj,Si | )quantifiesthe |            |                         |      |            |        |              |     |           |
|            |                  |              |     |          |        |              |                |            | ea ch feature           | of N | j compared | to the | same feature |     | among all |
| likelihood |                  | of selecting |     | neighbor | N      | as the       | best           | relay node |                         |      |            |        |              |     |           |
|            |                  |              |     |          | j      |              |                |            | neighborsofsensornodeS. |      |            |        |              |     |           |
i
| forsensornodeS,givenN’snormalizedfeatures.Notethat |     |     | i   | j   |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
each feature is independent of the others and depends only (cid:0) (cid:1)= bl Nj
|     |                                                 |     |     |     |     |     |     |     |     |     | P bl |       |       |     | (22) |
| --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | ----- | --- | ---- |
| onN | ,sothisprobabilitycanbecalculatedasfollowsusing |     |     |     |     |     |     |     |     |     |      | Nj Pl |       |     |      |
|     | j                                               |     |     |     |     |     |     |     |     |     |      |       | bl Nk |     |      |
k=1
| equation(12). |         |         |           |         |           |         |          |         |     |     |         | ds       |     |     |      |
| ------------- | ------- | ------- | --------- | ------- | --------- | ------- | -------- | ------- | --- | --- | ------- | -------- | --- | --- | ---- |
|               |         |         |           |         |           |         |          |         |     |     | (cid:0) | (cid:1)= | Nj  |     |      |
|               |         |         |           |         |           |         |          |         |     |     | P ds    | Nj       |     |     | (23) |
|               | (cid:0) | ,ds     | ,bo       | ,lq     | (cid:1)=P | (cid:0) | (cid:1)  |         |     |     |         | Pl       | ds  |     |      |
|               | P N j   | |bl Nj  | Nj        | Nj      | Nj,Si     | N       | j |bl Nj |         |     |     |         | k=1      | Nk  |     |      |
|               |         | (cid:0) | (cid:1)×P | (cid:0) | (cid:1)×P | (cid:0) |          | (cid:1) |     |     |         | bo       |     |     |      |
×P N |ds N |bo N |lq Nj,Si (12) P (cid:0) bo (cid:1)= N j (24)
|     |     | j   | Nj  | j   | Nj  |     | j   |     |     |     |     | Nj Pl |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
b o
|     |                                 |     |     |     |     |          |     |     |     |     |         | k=1        | Nk   |     |     |
| --- | ------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | ------- | ---------- | ---- | --- | --- |
|     | TheposteriorprobabilitiesP(N|bl |     |     |     |     | ),P(N|ds |     | ),  |     |     |         |            |      |     |     |
|     |                                 |     |     |     | j   | N j      | j N | j   |     |     | (cid:0) | (cid:1)= l | q j, |     |     |
P ( N | b o ) , a n d P (N | lq ) a re d e t e r m in e d u s i n g B a y e s ’ P lq N S i (25)
|     | j N j |     | j   | N j, S i |     |     |     |     |     |     | Nj,Si | Pl  |     |     |     |
| --- | ----- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
l q
th e o r e m a n d a r eg iv en b y e q u at io n s ( 1 3 ) to ( 1 6 ), r e sp ec ti v e l y . k = 1 N k,Si
P(bl |N )× P(N ) E a c h m a r g i n a l p ro b a b i li ty is c o m p u te d a s t h e r a tio o f a
|     |     | (cid:0) | |bl | (cid:1)= | Nj  | j   | j   |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P N j Nj (13) spe c i fi c fe a t u r e o f N t o t h e su m o f t h e s am e f e a tu r e ac ro s s
|     |     |     |     |     | P (b | l ) |     |     |     |     | j   |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Nj
|     |     |         |     |               | |N  | )×P(N |     |     | allneighborsofS.Thisnormalizationensuresthattheinflu- |     | i   |     |     |     |     |
| --- | --- | ------- | --- | ------------- | --- | ----- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     | (cid:0) |     | (cid:1)= P(ds | Nj  | j     | j ) |     |                                                       |     |     |     |     |     |     |
P N |ds (14) ence of each feat ure is assessed in a comparative manner
|     |     |     | j Nj |     | P(ds | )   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Nj rather than in isolation, meaning it is evaluated through an
|     |     |     |     | P(bo | |N  | )×P(N | )   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P (cid:0) N |bo (cid:1)= Nj j j (15) inter-nodecomparisonratherthananintra-nodecomparison.
j Nj
P(bo ) Inthisapproach,theinfluenceofagivenfeatureisconsidered
Nj
|     |     |     |     | P(lq |     | | N ) × | P(N ) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:0) (cid:1)= Nj ,S i j j a m o n g a ll n ei g h b o rs o f S i r at h er th a n b e in g li m it e d t o n o d e
|     |     | P N | |lq |     |     |     |     | (16) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
j Nj,Si P ( l q ) N a lo ne , a s i n t h e li k el ih o o d s ex p re ss e d i n e qu a t io n s ( 1 8 )
|     |     |     |     |     |     | N j,S i |     |     | j        |              |     |                 |     |       |          |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | -------- | ------------ | --- | --------------- | --- | ----- | -------- |
|     |     |     |     |     |     |         |     |     | to (21). | This ensures | a   | fair assessment | of  | how N | ranks as |
j
|     | The prior | probability |     | P(N | ) refers | to the | likelihood | that, |             |       |      |               |               |     |        |
| --- | --------- | ----------- | --- | --- | -------- | ------ | ---------- | ----- | ----------- | ----- | ---- | ------------- | ------------- | --- | ------ |
|     |           |             |     |     | j        |        |            |       | a potential | relay | node | for S i among | its competing |     | nodes, |
amongthel neighborsofsensornodeS i ,neighborN j isdes- allowingtherelayselectionprocesstoaccountfortherelative
ignatedasitsrelaynode.Itiscomputedusingequation(17).
strengthsandweaknessesofallcandidateneighbors.
OncethecontrollercompletestheexecutionofSTEP1and
|     |     |     |     | (cid:0) | (cid:1)= 1 |     |     |      |                               |     |     |     |                    |     |     |
| --- | --- | --- | --- | ------- | ---------- | --- | --- | ---- | ----------------------------- | --- | --- | --- | ------------------ | --- | --- |
|     |     |     |     | P N     |            |     |     | (17) | STEP2onallneighboringnodesofS |     |     |     | ,itproceedswiththe |     |     |
|     |     |     |     |         | j l        |     |     |      |                               |     |     |     | i                  |     |     |
followingSTEPS3and4:
|     | The likelihoods |     | P(bl | |N), | P(ds | |N), | P(bo | |N), and |                                   |     |     |     |     |     |     |
| --- | --------------- | --- | ---- | ---- | ---- | ---- | ---- | -------- | --------------------------------- | --- | --- | --- | --- | --- | --- |
|     |                 |     |      | Nj   | j    | Nj j | Nj   | j        | STEP3:SelectthebestrelaynodeforS. |     |     |     |     |     |     |
i
P(lq Nj,Si |N j )representtheprobabilitiesofobservingthefea- Before describing the operations performed in this step,
| ture | values | bl  | , ds , | bo , | and lq | , given | that | neighbor |     |     |     |     |     |     |     |
| ---- | ------ | --- | ------ | ---- | ------ | ------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
Nj Nj Nj Nj,Si it is important to highlight that the optimal neighbor, which
N j has already been chosen as the relay node for sensor hasthehighestnormalizedfeaturevaluesforthebatterylevel,
nodeS.Theselikelihoodsquantifytherelativecontribution
|     | i            |     |      |        |         |             |     |          | distancetothesink,bufferoccupancy,andlinkquality,yields |     |     |     |     |     |     |
| --- | ------------ | --- | ---- | ------ | ------- | ----------- | --- | -------- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| of  | each feature |     | of N | to the | overall | probability | of  | choosing |                                                         |     |     |     |     |     |     |
|     |              |     | j    |        |         |             |     |          | thehighestnumeratorintheposteriorprobabilitiescomputed  |     |     |     |     |     |     |
N j as the best relay node for S. i They are calculated using in(13)to(16),resultinginthelowestconditionalprobability
equations(18)to(21),respectively.
|     |     |     |     |     |     |     |     |     | P(N j |bl Nj | , ds Nj , | bo Nj , lq | Nj,Si ) among | the | candidate | neigh- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | ---------- | ------------- | --- | --------- | ------ |
bors,andviceversa.Consequently,intheProbabilitiesarray,
|     |     | (cid:0) | (cid:1)= |     | bl  | N j |     |      |     |     |     |     |     |     |     |
| --- | --- | ------- | -------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     | P   | bl |N   |          |     |     |     |     | (18) |     |     |     |     |     |     | |b  |
Nj j bl +ds + b o +lq w e i nv e r t t h e va l u e o f t h e co n d i tio n a l p r o b a b il it y P ( N j l N j ,
|     |     |     |     | Nj  | Nj  | Nj  | Nj,Si |     |           |          |            |             |             |        |               |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --------- | -------- | ---------- | ----------- | ----------- | ------ | ------------- |
|     |     |     |     |     |     |     |       |     | d s , b o | , l q j, | ) ( i .e . | , 1 / P ( N | | b l , d s | , b o  | , l q j,S ) ) |
|     |     |     |     |     | ds  |     |       |     | Nj        | N j N S  | i          | j           | N j         | N j Nj | N i           |
(cid:0) |N (cid:1)= Nj for each neighbor to ensure that the neighbor with the best
|     | P   | ds Nj | j   |        |     |     |     | (19) |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | ------ | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     |     |       |     | bl +ds | +bo | +lq |     |      |     |     |     |     |     |     |     |
Nj Nj Nj Nj,Si features (i.e., the one with the lowest P(N j |bl Nj , ds Nj , bo Nj ,
(cid:0) (cid:1)= bo Nj lq ))isassignedthehighestvalue,whiletheleastoptimal
|     | P   | bo |N |     |     |     |     |     | (20) | Nj,Si |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- |
|     |     | Nj    | j   | +ds | +bo | +lq |     |      |       |     |     |     |     |     |     |
bl Nj Nj Nj Nj,Si neighbor,withtheworstfeatures,isassignedthelowestvalue.
| 207290 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
Algorithm1RelayNodeSelection
| Inputs:WSNtopologygraphandSelectionhistory:setofpairs<S,N |     |     |     |     | >   |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
| Output:NBSDNoutputconsistingofasetofpairs<S,Bestrelaynode |     |     |     |     | >   |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i Si
1 InitializetheNBSDNoutputsetasempty
2 InitializeanarraylabeledProbabilitiesasempty
| 3 ForeachS | (S  | ∈Sensornodes)do |     |     |     |     |     |     |     |     |
| ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
i i
| 4 IfS | ∈Neighboringnodes |     | then                 |     |     |     |     |     |     |     |
| ----- | ----------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
|       | 1                 |     | Si                   |     |     |     |     |     |     |     |
|       | Addthepair<S,S    |     | >totheNBSDNoutputset |     |     |     |     |     |     |     |
| 5     |                   |     | i 1                  |     |     |     |     |     |     |     |
6 Findthepair<S ,N >intheSelectionhistorysetandincrementN byone
1
7 EndIf
8 Else
| 9   | ForeachN | (N  | ∈Neighboringnodes | )do |     |     |     |     |     |     |
| --- | -------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
|     |          | j j |                   | Si  |     |     |     |     |     |     |
10 NormalizeBL Nj ,DS Nj ,BO Nj ,andLQ Nj,Si usingequations(8)to(11),respectively,andstoretheresultingvalues
|     | inbl | ,ds ,bo | ,andlq Nj,Si |     |     |     |     |     |     |     |
| --- | ---- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|     |      | Nj Nj   | Nj           |     |     |     |     |     |     |     |
11 CalculatetheconditionalprobabilityP(N |bl ,ds ,bo ,lq )usingequation(12)
j Nj Nj Nj Nj,Si
12 InvertthecomputedprobabilityandstoretheresultinthearrayProbabilities
| 13  | EndForeach |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
14 EndElse
15 Identifytheneighbor(s)withthemaximumvalueinthearrayProbabilities
| 16  | Ifasingleneighborisidentified(referredtoasN |     |     | )then |     |     |     |     |     |     |
| --- | ------------------------------------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
max
|     | Addthepair<S,N |     | >totheNBSDNoutputset |     |     |     |     |     |     |     |
| --- | -------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
| 17  |                |     | i max                |     |     |     |     |     |     |     |
18 Findthepair<N ,N >intheSelectionhistorysetandincrementN byone
max
19 EndIf
20 Else(multipleneighborshavethesamemaximumvalue)
21 Selecttheone(alsodenotedasN )withtheminimumvalueofN intheSelectionhistoryset
max
|     | Addthepair<S,N |     | >totheNBSDNoutputset |     |     |     |     |     |     |     |
| --- | -------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
| 22  |                |     | i max                |     |     |     |     |     |     |     |
23 Findthepair<N ,N >intheSelectionhistorysetandincrementN byone
max
24 EndElse
25 EndForeach
Subsequently, from the array Probabilities, the neighbor intermediatesensornodes,andterminatesataspecificsensor
with the highest probability value is selected as the best node.Theoutputofthisphaseisasetofcontrolpackets[3],
relaynodeforsensornodeS.Ifmultipleneighborssharethe i each containing a routing path. These packets are sent to
samemaximumvalue,thecontrollerbreaksthetieusingthe the WSN, enabling sensor nodes to identify and learn their
Selection history set. It chooses the neighbor that has been bestrelaynodesassignedbythecontrollerandtransmitboth
assigned as a relay node the fewest times for other nodes, control and data packets to the sink through them. In this
i.e., the neighbor with the smallest N value in the Selection phase,thecontrollerexecutestwosteps:
historyset.Finally,apairconsistingofsensornodeS i andits STEP1:Constructtheroutingpathstowardthesink.
|     |     |     |     |     | Foreachpair<S,Bestrelaynode |     |     |     | >inNBSDNoutput: |     |
| --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --------------- | --- |
designatedrelaynodeisaddedtotheNBSDNoutputset.
|                                     |     |     |     |     |        |            | i      | Si          |             |            |
| ----------------------------------- | --- | --- | --- | --- | ------ | ---------- | ------ | ----------- | ----------- | ---------- |
| STEP4:UpdatetheSelectionhistoryset. |     |     |     |     | •      |            |        |             |             |            |
|                                     |     |     |     |     | If the | relay node | of the | pair is the | sink (i.e., | Best relay |
In the Selection history set, for the pair corresponding to node =S ),createanewroutingpaththatbeginswith
|     |     |     |     |     | Si  | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the nodeelected asthe bestrelay nodefor S , thecontroller the sink S , followed by the sensor node S of the pair.
|                |             |     |     | i   |                                | 1   |     |     | i    |     |
| -------------- | ----------- | --- | --- | --- | ------------------------------ | --- | --- | --- | ---- | --- |
| incrementsitsN | valuebyone. |     |     |     |                                |     |     |     |      |     |
|                |             |     |     |     | Thenewlycreatedroutingpathis[S |     |     |     | ,S]. |     |
|                |             |     |     |     |                                |     |     |     | 1 i  |     |
Algorithm1presentsasummaryoftheprocedureexecuted • Iftherelaynodeofthepairisnotthesink(i.e.,Bestrelay
by the controller in the phase ‘‘best relay node identifica- ̸=
|     |     |     |     |     | node Si | S 1 | ), search in | the previously | created | routing |
| --- | --- | --- | --- | --- | ------- | --- | ------------ | -------------- | ------- | ------- |
tion’’. Once the controller finishes iterating through all the paths for one whose last element is equal to the relay
sensornodestofindtheirbestrelaynodes,itfeedstheNBSDN nodeofthepair(i.e.,apath[S ,...,Bestrelaynode ]).
|             |         |             |           |                    |                                         |     |     | 1   |     | Si      |
| ----------- | ------- | ----------- | --------- | ------------------ | --------------------------------------- | --- | --- | --- | --- | ------- |
| output set, | pairing | each sensor | node with | its selected relay |                                         |     |     |     |     |         |
|             |         |             |           |                    | Ifsuchapathisfound,appendthesensornodeS |     |     |     |     | i ofthe |
node using the Naïve Bayes algorithm, to the next phase, pairtoitsend,resultinginthemodifiedroutingpath[S ,
1
‘‘routingpathsconstructionandtransmission’’.
|     |     |     |     |     | ..., Best | relay   | node Si , S].  | i Otherwise, | from    | the routing |
| --- | --- | --- | --- | --- | --------- | ------- | -------------- | ------------ | ------- | ----------- |
|     |     |     |     |     | paths     | created | so far, search | for and      | extract | a sub-path  |
b: ROUTINGPATHSCONSTRUCTIONANDTRANSMISSION that starts at the sink and ends at the relay node of the
TheinputtothisphaseistheNBSDNoutputset,whichserves pair.Then,createanewroutingpathidenticaltothissub-
as the basis for constructing a set of routing paths to the path,withthesensornodeS ofthepairappendedtothe
i
| sink.Eachpathoriginatesfromthesink,traversesaseriesof |     |     |     |     | end. |     |     |     |     |        |
| ----------------------------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ------ |
| VOLUME13,2025                                         |     |     |     |     |      |     |     |     |     | 207291 |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
Algorithm2Routingpathsconstruction
| Input:NBSDNoutputconsistingofasetofpairs<S,Bestrelaynode |     |     |     |     |     |     |     |     | >   |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                          |     |     |     |     |     | i   |     | Si  |     |     |     |     |     |     |
Output:Routingpaths:arrayofarrays,eachrepresentingaroutingpathoftheform[S 1 ,...,S] i
1 InitializethearrayRoutingpathsasempty
| 2 Foreachpair<S,Bestrelaynode |                 |     |     |                   | >intheNBSDNoutputsetdo |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --------------- | --- | --- | ----------------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                               |                 |     | i   |                   | Si                     |     |     |     |     |     |     |     |     |     |
| 3                             | IfBestrelaynode |     | =S  | then              |                        |     |     |     |     |     |     |     |     |     |
|                               |                 |     | Si  | 1                 |                        |     |     |     |     |     |     |     |     |     |
| 4                             | Addanewpath[S   |     |     | ,S]toRoutingpaths |                        |     |     |     |     |     |     |     |     |     |
|                               |                 |     | 1   | i                 |                        |     |     |     |     |     |     |     |     |     |
5 EndIf
6 Else
7 SearchinRoutingpathsforapathstructuredas[S ,...,Bestrelaynode ]
|     |                        |                    |     |     |     |     | 1   |     |     | Si  |     |     |     |     |
| --- | ---------------------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8   | Ifsuchapathisfoundthen |                    |     |     |     |     |     |     |     |     |     |     |     |     |
| 9   | AddS                   | totheendofthatpath |     |     |     |     |     |     |     |     |     |     |     |     |
i
| 10  | EndIf |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11  | Else  |     |     |     |     |     |     |     |     |     |     |     |     |     |
12 SearchinRoutingpathsforapathstructuredas[S ,...,Bestrelaynode ,...,S ],wherem∈{2,3,...,n}
|     |     |     |     |     |     |     |     | 1   |     | Si  | m   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
13 Oncesuchapathisfound,extractfromitthesub-path[S 1 ,...,Bestrelaynode Si ]
| 14  | Createanewpaththatisidenticaltotheextractedsub-path |                        |     |                    |     |     |                    |     |     |     |     |     |     |     |
| --- | --------------------------------------------------- | ---------------------- | --- | ------------------ | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
| 15  | AddS                                                | i totheendofthenewpath |     |                    |     |     |                    |     |     |     |     |     |     |     |
| 16  | Addthenewpath([S                                    |                        |     | ,...,Bestrelaynode |     |     | ,S])toRoutingpaths |     |     |     |     |     |     |     |
|     |                                                     |                        |     | 1                  |     |     | Si i               |     |     |     |     |     |     |     |
| 17  | EndElse                                             |                        |     |                    |     |     |                    |     |     |     |     |     |     |     |
18 EndElse
19 EndForeach
Theresultingroutingpathstaketheformof,forexample,[S , the controller level, based on control packets received from
1
S ,S ,...,S].Everypathisanarrayorderedinsuchaway theWSN,shortlybeforeaT intervalelapses.
| 2 4 | i   |     |     |     |     |     |     |     |     |     | controller | routing |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --- | --- |
that, for each sensor node in the array, its best relay node, Assoonasthisintervalelapses,thecontrollerexecutesthe
as selected by the controller, is the preceding node. In our firstphaseoftheNBSDNalgorithm,namely‘‘bestrelaynode
example,thebestrelaynodeforS 2 isS 1 ,forS 4 isS 2 ,andso identification’’.
on.Asummaryoftheprocedureforformingroutingpathsis
providedinAlgorithm2.
1) BESTRELAYNODEIDENTIFICATION
STEP2:CommunicatetheroutingpathstotheWSN. ThecontrollerexamineseachsensornodeintheWSN,start-
| Each | constructed | routing | path, | such | as [S | , S , S | , ..., |     |     |     |     |     |     |     |
| ---- | ----------- | ------- | ----- | ---- | ----- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
1 2 4 ing from those closest to the sink, to identify its best relay
S i ], is encapsulated in a control packet and transmitted to node. In the illustrated example, the controller sequentially
the sink. Upon receiving the packet, the sink forwards it examines nodes S , S , and S to determine their respective
|             |      |       |       |           |         |          |      |     |     | 2 3 |     | 4   |     |     |
| ----------- | ---- | ----- | ----- | --------- | ------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| to the node | that | comes | after | it in the | routing | path, in | this |     |     |     |     |     |     |     |
bestrelaynode.
| case, S 2        | . However, | before          | doing | so, it         | removes | itself  | from  |           |     |     |     |     |     |     |
| ---------------- | ---------- | --------------- | ----- | -------------- | ------- | ------- | ----- | --------- | --- | --- | --- | --- | --- | --- |
| the encapsulated |            | path (resulting |       | in a shortened |         | path [S | , S , |           |     |     |     |     |     |     |
|                  |            |                 |       |                |         |         | 2 4   | a: s ANDs |     |     |     |     |     |     |
2 3
..., S]) i to reduce packet length and minimize the energy Both of these nodes have the sink S as a neighbor, so the
1
consumptionofthenodestraversedbythepacket.Whenthe
|             |     |                                          |     |     |     |     |     | routingalgorithm  |     | directlyassigns |           | itas | theirbest      | relaynode |
| ----------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | ----------------- | --- | --------------- | --------- | ---- | -------------- | --------- |
| sensornodeS |     | receivesthecontrolpacket,itrecognizesthe |     |     |     |     |     |                   |     |                 |           |      |                |           |
|             | 2   |                                          |     |     |     |     |     | andaddstwopairs<S |     |                 | ,S >and<S |      | ,S >totheNBSDN |           |
|             |     |                                          |     |     |     |     |     |                   |     | 2               | 1         |      | 3 1            |           |
sinkS 1 asitsbestrelaynodesinceitreceivedthepacketfrom outputset.Moreover,intheSelectionhistoryset,theN
value
it.S thentransmitsthepackettothenextnodeintherouting
| 2      |                                              |     |     |     |     |     |     | ofthepaircorrespondingtothesinkS |     |     |     |     | isincreasedbytwo. |     |
| ------ | -------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | ----------------- | --- |
| path,S | ,onceagainremovingitselffromthepathwithinthe |     |     |     |     |     |     |                                  |     |     |     |     | 1                 |     |
4
| packet(whichnowbecomes[S |            |                                       |        | ,...,S])tofurtherminimize |       |          |      |             |     |      |               |     |                   |     |
| ------------------------ | ---------- | ------------------------------------- | ------ | ------------------------- | ----- | -------- | ---- | ----------- | --- | ---- | ------------- | --- | ----------------- | --- |
|                          |            |                                       |        | 4 i                       |       |          |      | b: s        |     |      |               |     |                   |     |
| packetlength.S           |            | receivesthecontrolpacketandlearnsthat |        |                           |       |          |      | 4           |     |      |               |     |                   |     |
|                          |            | 4                                     |        |                           |       |          |      | S hasnodesS |     | andS | asneighbors(l |     | =2).Thecontroller |     |
|                          |            |                                       |        |                           |       |          |      | 4           |     | 2 3  |               |     |                   |     |
| S 2 is its               | best relay | node,                                 | as the | packet                    | comes | from it. | This |             |     |      |               |     |                   |     |
determineswhichofthetwonodesisthemostsuitablerelay.
| operation | is repeated | at  | each | visited node | until | the packet |     |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ---- | ------------ | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Tothisend,itperformsthefollowingsteps.
reachesitsfinaldestination.
NEIGHBORS2
|     |     |     |     |     |     |     |     | STEP1:NormalizethefeaturesofneighborS |     |     |     |     |     | .   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
2
|     |     |     |     |     |     |     |     | The | values | of the features: |     | battery | level (BL | ), distance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------------- | --- | ------- | --------- | ----------- |
S2
C. EXAMPLE
|               |     |               |     |        |          |       |     | to the sink(DS |                 | S2 ), buffer | occupancy(BO |     | S2 ), | and linkqual- |
| ------------- | --- | ------------- | --- | ------ | -------- | ----- | --- | -------------- | --------------- | ------------ | ------------ | --- | ----- | ------------- |
| To illustrate | the | functionality |     | of our | proposed | NBSDN |     |                |                 |              |              |     |       |               |
|               |     |               |     |        |          |       |     | ity(LQ         | )arenormalized: |              |              |     |       |               |
S2,S4
| algorithm,                                         | let us | apply | it to a | simple | WSN topology |     | con- |     |     |     |     |     |     |       |
| -------------------------------------------------- | ------ | ----- | ------- | ------ | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | ----- |
| sistingoffournodes:onesinknodeandthreesensornodes, |        |       |         |        |              |     |      |     |     | 1   |     | 1   |     | 1     |
|                                                    |        |       |         |        |              |     |      |     | =   |     | =   |     | =   | =0.02 |
bl S2
as depicted in Fig. 4. This WSN topology is constructed at 255−BL 255−205 50
S2
| 207292 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
FIGURE4. AWSNtopologywithfournodesandtheircorrespondingfeaturevalues.
1 1 0.02 × 1 1 × 1
ds S2 = = =1 = 0.02+1+1+0.03 2 × 0.02+1+1+0.03 2
DS S2 1 0.02 1
1 1 0.02+0.1 1+1
bo S2 = = =1 1 × 1 0.03 × 1
BO S2 1 × 0.02+1+1+0.03 2 × 0.02+1+1+0.03 2
1 1 1 0.03
lq S2,S4 = LQ S2,S4 = 36 =0.03 P (cid:0) S 2 |bl S2 1 , + d 1 s S2 ,bo S2 ,lq S2,S4 0 (cid:1) .03+0.03
STEP 2: Compute the conditional probability P ( S
=0.03×0.49×0.49×0.01=7.2×10 −5
2
|bl S2 , ds S2 , bo S2 , lq S2,S4 ) and store the resulting value NEIGHBORS
3
inanarraydenotedasProbabilities.
Both STEP 1 and STEP 2 are subsequently applied to
P (cid:0) S 2 |bl S2 ,ds S2 ,bo S2 ,lq S2,S4 (cid:1) n d e s S ig 3 h , b b o o r S S 3 3 , , l y q i S e 3 ld ,S i 4 n ) g th = e c 6 o . n 6 d 2 iti × ona 1 l 0 p − r 5 o . ba F b o il l i l t o y w P in ( g S 3 | t b h l e S s 3 e ,
=P(S
2
|bl
S2
)×P(S
2
|ds
S2
)
steps, the controller proceeds to execute STEP 3 for both
×P(S 2 |bo S2 )×P (cid:0) S 2 |lq S2,S4 (cid:1) S 2 andS 3 .
= P(bl S2 P | ( S b 2 l ) S × 2 ) P(S 2 ) × P(ds S2 P | ( S d 2 s ) S × 2 ) P(S 2 ) S T T he E c P on 3 d : i S ti e o l n e a c l t p t r h o e b b ab es il t it r i e e l s a P y (S n 2 o | d b e l S f 2 o , r d S s S 4 2 . ,bo S2 ,lq S2,S4 )
× P(bo S2 |S 2 )×P(S 2 ) × P(lq S2,S4 |S 2 )×P(S 2 ) a a n b d ili P ti ( e S s, 3| a b r l e S3 in , v d e s r S t 3 e , d b , o r S e 3 s , u l l q ti S n 3 g ,S i 4 n ), t s h t e or u e p d d i a n te t d he a a rr r a ra y y : [ P S ro : b 1 -
P(bo S2 ) P(lq S2,S4 ) / 7.2 × 10−5, S : 1 / 6.62 × 10−5]. Based on these valu 2 es,
3
blS2 × 1 the controller selects S as the best relay node for S since
= blS2 +dsS2 +boS2 +lq S2,S4 l 3 4
blS2 itcorrespondstothehighestvalueintheProbabilitiesarray.
blS2 +blS3 Thecontrollerthenaddsthepair< S
4
,S
3
>totheNBSDN
dsS2 × 1 outputset.
× blS2 +dsS2 +boS2 +lq S2,S4 l
STEP4:UpdatetheSelectionhistoryset.
dsS2
dsS2 +dsS3 In the Selection history set, for the pair corresponding to
boS2 × 1 nodeS ,thecontrollerincrementsitsN valuebyone.
× blS2 +dsS2 +boS2 +lq S2,S4 l 3
At the end of the phase ‘‘best relay node identification’’,
boS2
boS2 +boS3 the NBSDN output set contains the following pairs: < S
2
,
× blS2 +dsS2 lq + S b 2, o S S 4 2 +lq S2,S4 × 1 l S th 1 is > s , e < tto S 3 th , e S 1 su > bs , e a q n u d e < nt S p 4 h , a S se 3 , > ‘‘r . o T u h ti e n c g o p n a tr t o h l s le c r o t n h s e tr n u f c e t e io d n s
lq S2, l S q 4 S + 2, l S q 4 S3,S4 andtransmission’’.
VOLUME13,2025 207293

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
2) ROUTINGPATHSCONSTRUCTIONANDTRANSMISSION assessedtheirperformancethroughsimulationsconductedin
|     |     |     |     |     |     |     |     | the COOJA | simulator |     | [46] over | a duration | of 720 | seconds. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | --------- | ---------- | ------ | -------- |
STEP1:Constructtheroutingpathstowardthesink.
The relay node in the pair < S , S > is the sink S . WeevaluatedeachroutingalgorithminstaticWSNsofvary-
|     |     |     |     | 2   | 1   |     | 1   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
As aconsequence, the controller createsa new routingpath ing sizes: 11, 21, 31, 41, 51, 61, 71, 81, 91, and 101 nodes.
starting with S 1 , followed by the sensor node to which the Foreachnetworksize,thesimulationwasrun15times,with
controllerassignedS asitsrelaynode(i.e.,S ),resultingin each run using a different pseudo-random seed to generate
|          |          | 1               |     |          |     | 2         |       |                                                      |     |     |     |     |     |     |
| -------- | -------- | --------------- | --- | -------- | --- | --------- | ----- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|          |          |                 |     |          | <   | >,        |       | adistinctnetworktopology.Thisprocedureensuresthatthe |     |     |     |     |     |     |
| the path | [S 1 , S | 2 ]. Similarly, | for | the pair |     | S 3 , S 1 | where |                                                      |     |     |     |     |     |     |
S is also the relay node, the controller applies the same performanceassessmentreflectsabroadrangeofconfigura-
1
operation,yieldingtheroutingpath[S ,S ]. tionsanddoesnotdependonaparticulartopologyinstance.
1 3
|     |     | <   |     | >,  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In the third pair S 4 , S 3 the sink S 1 is not the relay Italsoenabledthecomputationof95%confidenceintervals
node; instead, it is the sensor node S . Thus, the controller for the performance metrics, thereby ensuring the statistical
3
validityofthereportedresults.
| searches | through | the routing |     | paths created |     | so far for | a path |     |     |     |     |     |     |     |
| -------- | ------- | ----------- | --- | ------------- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
endingwithS .Itfindsthepath[S ,S ]andappendsS (the Themainassumptionsandsimulationparametersusedin
|     | 3   |     |     | 1   | 3   |     | 4   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sensornodeforwhichthecontrollerdesignatedS asitsrelay our comparative study are listed below. These assumptions
3
node)toitsend.Theroutingpathbecomes:[S 1 ,S 3 ,S 4 ]. are consistent with those commonly adopted in the related
STEP2:CommunicatetheroutingpathstotheWSN. literature [3], [6], [7], [20]. Moreover, the parameter values
Thecontrollertransmitstheconstructedroutingpaths[S were maintained as originally defined in the SDN-WISE
1 ,
S ]and[S ,S ,S ]tothesinkusingcontrolpackets.Forthe framework[3].
| 2             | 1 3    | 4             |     |     |         |         |        |     |     |     |     |     |     |     |
| ------------- | ------ | ------------- | --- | --- | ------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| first control | packet | encapsulating |     | the | routing | path [S | , S ], |     |     |     |     |     |     |     |
1 2
TheWSNsarecomposedofasinglesinknodeandmul-
| thesinkforwardsittothesensornodethatcomesafteritin |     |     |     |     |     |     |     | •   |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the path, S . Before forwarding, it removes itself from the tiplesensornodes,initiallypositionedrandomlywithin
2
path,leaving[S ]astheupdatedpathwithinthepacket.Upon a100×100m2squarearea.
2
receiving the packet, S identifies S as its best relay node, • Thesinkandallsensornodesremainstationaryattheir
|     |     |     | 2   | 1   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sinceitreceivedthecontrolpacketfromthatnode. initialdeploymentpositionsfortheentiredurationofthe
simulation.
Forthesecondcontrolpacketcontainingtheroutingpath
=10seconds,eachnodegenerates
[S , S , S ], the sink sends it to the sensor node following • EveryT beaconpacket
1 3 4
it in the path, namely S . Before sending the packet, the a beacon packet and sends it to the nodes within its
3
sink removes itself from the path encapsulated within the transmissionrange.
packet,updatingitto[S ,S ].WhenS receivesthepacket, • EveryT =10seconds,eachsensornodegener-
|     |     |     | 3 4 |     | 3   |     |     |     | datapacket |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
atesandforwardsa14-bytedatapackettoitsrelaynode.
| it identifies | S 1 | as its | best relay | node. | It then | forwards | the |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ---------- | ----- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
packettothesensornodesucceedingitinthepathincluded Allthedatapacketsareultimatelydestinedforthesink.
within the packet, notably S . Before doing so, S removes • Every T = 20 seconds, each sensor node
|     |     |     | 4   |     |     | 3   |     |     | report | packet |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --- | --- | --- | --- |
generatesandtransmitsareportpackettoitsrelaynode.
| itselffromthepath,updatingitto[S |     |     |     | 4 ].WhenS |     | 4 receivesthe |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
packet,itdeterminesthatS isitsbestrelaynode. Thereportpacketsareultimatelyaddressedtothecon-
3
trollerthroughthesink.Thesink,incontrast,createsand
Thefollowingsectionpresentstheperformanceevaluation
ofNBSDN,whereitseffectivenessisanalyzedthroughcom- transmitsitsownreportpacketdirectlytothecontroller.
parison with established baseline routing algorithms under • EveryT =60seconds,thecontrollerexe-
controller routing
|     |     |     |     |     |     |     |     | cutes | a specified |     | routing algorithm |     | (EASDN, | RLSDN, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | ----------------- | --- | ------- | ------ |
diversenetworkscalesandtopologies.
SPSDN,NBSDN,orNB-SDWSN).
• Thesensorandsinknodesemploywirelesslinksbased
VI. PERFORMANCEEVALUATION
A. SIMULATIONPARAMETERSANDMETRICS ontheIEEE802.15.4standard[23]totransmitpackets
totheirone-hopneighboringnodes.TheMACsublayer
| Our proposed |     | routing | algorithm, | NBSDN, |     | was evaluated |     |         |     |           |         |     |            |          |
| ------------ | --- | ------- | ---------- | ------ | --- | ------------- | --- | ------- | --- | --------- | ------- | --- | ---------- | -------- |
|              |     |         |            |        |     |               |     | employs | the | unslotted | CSMA/CA |     | algorithm, | which is |
againstfourestablishedroutingapproaches:
|         |     |         |              |     |           |     |         | defined | by  | the IEEE | 802.15.4 | standard | with | its default |
| ------- | --- | ------- | ------------ | --- | --------- | --- | ------- | ------- | --- | -------- | -------- | -------- | ---- | ----------- |
| • EASDN |     | [6], an | energy-aware |     | SDN-based |     | routing |         |     |          |          |          |      |             |
settings[47].Althoughthephysicallayerdoesnotintro-
algorithmdesignedtooptimizenetworklifetimebybal-
|     |     |     |     |     |     |     |     | duce | transmission |     | errors, | packet | collisions | can occur |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------ | --- | ------- | ------ | ---------- | --------- |
ancingenergyconsumptionacrosssensornodes.
whenneighboringnodestransmitsimultaneously,lead-
•
RLSDN [7], a reinforcement learning–based routing ingtopacketloss.
algorithmfortheSDNcontroller.
|         |      |            |     |          |            |     |         | • The | Unit | Disk Graph | Medium   | (UDGM)             | propagation |      |
| ------- | ---- | ---------- | --- | -------- | ---------- | --- | ------- | ----- | ---- | ---------- | -------- | ------------------ | ----------- | ---- |
| • SPSDN | [3], | Dijkstra’s |     | shortest | path–based |     | routing |       |      |            |          |                    |             |      |
|         |      |            |     |          |            |     |         | model | [48] | is used    | to model | distance-dependent |             | sig- |
algorithmfortheSDNcontroller.
nalattenuationinthewirelesscommunicationmedium.
| • NB-SDWSN |     | [20], | an  | earlier | version | of the | Naïve |      |       |         |     |          |            |           |
| ---------- | --- | ----- | --- | ------- | ------- | ------ | ----- | ---- | ----- | ------- | --- | -------- | ---------- | --------- |
|            |     |       |     |         |         |        |       | This | model | defines | two | distinct | zones: the | transmis- |
Bayes–basedroutingalgorithmthatusesdistancetothe sionrangewithinwhichnodescansuccessfullyreceive
sinkandresidualenergyforselectingrelaynodes.
|     |     |     |     |     |     |     |     | transmitted |     | messages | and | the interference | range | where |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | --- | ---------------- | ----- | ----- |
We implemented these routing approaches, including our nodesmayexperiencesignalinterference.Nodeslocated
routing algorithm, within the SDN-WISE framework and beyondtheinterferencerangearenotaffected.
| 207294 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
TABLE6. Summaryoftheparametersandtheircorrespondingvalues TABLE7. Trafficdistributionamongneighboringnodesunderdifferent
usedinthesimulations. routingalgorithms(EASDN,RLSDN,SPSDN,NBSDN,ANDNB-SDWSN).
Valuesrepresenttheamountoftrafficeachneighboringnodereceived
fromthesensornodes.
• The transmission range of the wireless medium is
5meters,whereastheinterferencerangeis0meters(i.e.,
theinterferencerangeisnotconsidered).
• Theprocessingtimeofboththedataandcontrolpackets degradation, as the loss of even a single node can
isnegligible. compromisethesensingcoverageanddisconnectparts
Table6summarizesthekeyparametersandtheirassociated ofthenetworkfromthesink,resultinginpacketloss.
valuesusedinoursimulations. • Packet loss: measures the percentage of data packets
To compare the performance of the routing algorithms, transmittedbysensornodesthatfailtoreachthesink.
weemploythefollowingmetrics: Itiscalculatedbydividingthedifferencebetweenthe
• Load balancing: illustrates how a sensor node dis- total number of data packets sent by the sensor nodes
tributesitstraffic,destinedforthesink,amongneigh- andthenumberofdatapacketssuccessfullydelivered
boringnodeswhenaspecificroutingalgorithmisused tothesinkbythetotalnumberofdatapacketssent.
bythecontroller.Itiscalculatedbytrackingthenumber • Datathroughput:indicatestherateatwhichdatapack-
ofpacketsthateachsensornodeforwardstoeachofits etsweresuccessfullydeliveredfromthesensornodes
neighbors. tothesinkduringthesimulationtime.Itiscomputedby
• Generatedcontroltraffic:measurestheaveragelength dividing the number of data packets that successfully
of the control packets produced by the routing reachedthesinkbythesimulationtime.
algorithm, namely those sent from the controller to • Networklatency:representstheaveragetimetakenby
the sink. This average is computed by dividing the a data packet generated by a sensor node to reach the
totallengthofthepacketsbytheiroverallcount.Addi- sink.Itiscalculatedbysummingthetimetakenbyeach
tionally, this metric quantifies the overall number and generateddatapackettoarriveatthesinkanddividing
length of control packets generated within the WSN thistotalbythenumberofgeneratedpackets.
after a given routing algorithm is applied by the con- B. RESULTSANDDISCUSSIONS
troller. It does so by separately summing the total
numberandlengthofcontrolpacketsthateachnodehas 1) LOADBALANCING
issued upon receiving packets initiated by the routing Table 7 shows the distribution of sensor node traffic (i.e.,
algorithm. data packets) among neighboring nodes across four simu-
• Network lifetime: denotes the time interval between lation runs, with the controller operating EASDN, RLSDN,
the activation of the WSN (i.e., when all the sensor SPSDN,NBSDN,andNB-SDWSN,respectively.
andsinknodesareswitchedon)andthemomentwhen Each simulation was conducted on the same WSN, con-
the first sensor node depletes its battery and becomes sistingof15nodesarrangedasshowninFig.5.InthisWSN,
non-functional. During this period, the WSN remains the sink S has the blue-colored sensor nodes as neighbors.
1
fullyoperational,withallsensornodesactive,ensuring Theyellow-coloredsensornodesareconnectedtothesensor
complete sensing coverage of the monitored area and nodesinthelevelsimmediatelyaboveandbelow,excluding
uninterrupted connectivity between all sensor nodes blue-colorednodesinthelowerlevel.Theblue-colorednodes
and the sink. The network remains fully functional areconnectedtothesinkandtothesensornodesinthelevel
until the first sensor node drains its battery and shuts directly below, excluding those that are also blue-colored.
down.Thiseventmarksthebeginningofperformance Note that in Fig. 5, the value shown close to each node
VOLUME13,2025 207295

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
selectionisrestrictedtothoseclosesttothesink.Forinstance,
|     |     |     |     |     |     |     | fornodesS                            | ,S                        | ,S ,andS     |                  | ,EASDNconsistentlyselects |          |              |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | ------------------------- | ------------ | ---------------- | ------------------------- | -------- | ------------ |
|     |     |     |     |     |     |     |                                      | 9 10                      | 11           | 12               |                           |          |              |
|     |     |     |     |     |     |     | either S                             | or S as                   | their        | relay            | node, alternating         | between  | the          |
|     |     |     |     |     |     |     |                                      | 7 8                       |              |                  |                           |          |              |
|     |     |     |     |     |     |     | two despite                          | the                       | availability | of               | other neighbors,          |          | specifically |
|     |     |     |     |     |     |     | S 4 ,S 5 ,andS                       | 6 .ThispreferenceisduetoS |              |                  |                           | 7 andS 8 | beingonly    |
|     |     |     |     |     |     |     | onehopawayfromthesink,whereasS       |                           |              |                  |                           | ,S ,andS | aretwo       |
|     |     |     |     |     |     |     |                                      |                           |              |                  | 4                         | 5        | 6            |
|     |     |     |     |     |     |     | hopsaway.Supportingthisobservation,S |                           |              |                  |                           | ,S ,andS | receive      |
|     |     |     |     |     |     |     |                                      |                           |              |                  |                           | 4 5      | 6            |
|     |     |     |     |     |     |     | nodatapacketsfromS                   |                           | 9            | toS 12 ,whereasS |                           | 7 andS 8 | exclusively  |
receivetheirpackets,withnearlyequalcountsof124and132,
respectively.
|     |     |     |     |     |     |     | Another  | observation     |      | from    | Table 7 is    | that when | a node      |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | ---- | ------- | ------------- | --------- | ----------- |
|     |     |     |     |     |     |     | has only | one neighboring |      | node    | closest to    | the sink, | EASDN       |
|     |     |     |     |     |     |     | behaves  | identically     | to   | SPSDN,  | repeatedly    | selecting | that        |
|     |     |     |     |     |     |     | neighbor | as the relay.   | This | results | in unbalanced |           | data trans- |
missionasallpacketsaresentthroughthatsingleneighbor.
|     |     |     |     |     |     |     | For example, | S   | and S | have | neighbors | S to S | . Among |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | ---- | --------- | ------ | ------- |
|     |     |     |     |     |     |     |              | 14  |       | 15   |           | 9      | 13      |
FIGURE5. AWSNtopologyorganizedbylevels,containing15nodeswith these,onlyS isonehopawayfromthesink,whiletheothers
13
theirrespectivedistances(inhops)tothesink.
|     |     |     |     |     |     |     | are two              | hops away. | It is              | evident | that EASDN, | like | SPSDN, |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | ---------- | ------------------ | ------- | ----------- | ---- | ------ |
|     |     |     |     |     |     |     | consistentlyselectsS |            | astherelaynodeforS |         |             | andS | ,asit  |
|     |     |     |     |     |     |     |                      |            | 13                 |         |             | 14   | 15     |
receivesall128datapacketstransmittedbybothnodes.
| represents | its distance | to          | the sink, | expressed |      | as the number |             |     |        |     |               |             |     |
| ---------- | ------------ | ----------- | --------- | --------- | ---- | ------------- | ----------- | --- | ------ | --- | ------------- | ----------- | --- |
|            |              |             |           |           |      |               | In contrast | to  | EASDN, | the | other routing | algorithms— |     |
| of hops    | a packet     | transmitted | by        | that node | must | traverse to   |             |     |        |     |               |             |     |
NBSDN,NB-SDWSN,andRLSDN—allowsensornodesto
reachthesink.
|       |                 |     |               |     |     |                | distribute | their data | packets | across     | all        | neighboring | nodes, |
| ----- | --------------- | --- | ------------- | --- | --- | -------------- | ---------- | ---------- | ------- | ---------- | ---------- | ----------- | ------ |
| Given | the illustrated |     | WSN topology, |     | the | controller can |            |            |         |            |            |             |        |
|       |                 |     |               |     |     |                | achieving  | global     | load    | balancing, | as clearly | illustrated | in     |
makethefollowingroutingdecisions:
|                      |     |     |     |       |                    |     | Table7.Forexample,nodesS |     |     |     | andS distributetheirtraffic |     |     |
| -------------------- | --- | --- | --- | ----- | ------------------ | --- | ------------------------ | --- | --- | --- | --------------------------- | --- | --- |
|                      |     |     |     |       |                    |     |                          |     |     | 14  | 15                          |     |     |
| • ForeachofthenodesS |     |     | ,S  | ,andS | ,itmayassigneither |     |                          |     |     |     |                             |     |     |
4 5 6 almost evenly among all their neighboring nodes (S 9 , S 10 ,
S 2 orS 3 astherelaynode. S ,S ,andS )whenthecontrolleremploysNBSDN,NB-
|                             |         |           |     |         |       |            | 11 12                                           | 13  |     |     |      |                 |     |
| --------------------------- | ------- | --------- | --- | ------- | ----- | ---------- | ----------------------------------------------- | --- | --- | --- | ---- | --------------- | --- |
| • For                       | each of | the nodes | S   | , S , S | , and | S , it may |                                                 |     |     |     |      |                 |     |
|                             |         |           | 9   | 10      | 11    | 12         | SDWSN,orRLSDN.Thisissupportedbythefactthatthese |     |     |     |      |                 |     |
| designateeithertheneighborS |         |           |     | ,S      | ,S ,S | ,orS asthe |                                                 |     |     |     |      |                 |     |
|                             |         |           |     | 4       | 5 6   | 7 8        | nodesreceivedatapacketsfromS                    |     |     |     | andS | inapproximately |     |
|                             |         |           |     |         |       |            |                                                 |     |     |     | 14   | 15              |     |
relaynode. equal numbers: 27, 19, 27, 27, and 28 in NBSDN, 21, 20,
| • For | each of | the nodes | S   | and S | , it may | select either |                                             |     |     |     |     |     |     |
| ----- | ------- | --------- | --- | ----- | -------- | ------------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
|       |         |           | 14  | 15    |          |               | 21,34,and32inNB-SDWSN,and6,18,34,35,and35in |     |     |     |     |     |     |
theneighborS 9 ,S 10 ,S 11 ,S 12 ,orS 13 astherelaynode. RLSDN,respectively.ThereasonNBSDN,NB-SDWSN,and
• Fortheblue-coloredsensornodes,sincetheyaredirectly
RLSDNallowsensornodestodistributetheirtrafficalmost
| connected | to  | the sink | S , the | controller | always | assigns |     |     |     |     |     |     |     |
| --------- | --- | -------- | ------- | ---------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
1 evenly across all neighboring nodes is that, for each sensor
S 1 astheirrelaynode. node in the WSN, they periodically rotate the role of relay
FromTable7,weobservethatwhenthecontrolleremploys amongallitsneighbors,notjustthoseclosesttothesink,asin
| SPSDN,          | the sensor | nodes       | fail to  | distribute | their | data pack-     | EASDN. |     |     |     |     |     |     |
| --------------- | ---------- | ----------- | -------- | ---------- | ----- | -------------- | ------ | --- | --- | --- | --- | --- | --- |
| ets across      | multiple   | neighboring |          | nodes      | and   | instead trans- |        |     |     |     |     |     |     |
| mit all packets |            | through     | a single | neighbor.  | The   | lack of a      |        |     |     |     |     |     |     |
load-balancingmechanisminSPSDNstemsfromitsstrategy 2) GENERATEDCONTROLTRAFFIC
ofrepeatedlyassigning,foreachsensornodeintheWSN,the Fig. 6 illustrates the average length (in bytes) of control
same neighbor as its relay node to route its packets toward packetsgeneratedbythefivecompetingroutingalgorithms—
thesink.ThisbehaviorisclearlyillustratedinTable7,where EASDN, RLSDN, SPSDN, NB-SDWSN, and NBSDN—as
SPSDN consistently selects S as the relay node for both thenetworksizeincreasesfrom11to101nodesinincrements
13
nodes S and S , despite the presence of other neighbors of 10. NB-SDWSN and NBSDN consistently produce the
| 14  |     | 15  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(S 9 ,S 10 ,S 11 ,andS 12 ).Thisisdemonstratedbythefactthat shortestcontrolpacketsacrossallnetworksizes,withaverage
S , S , S , and S do not receive any data packets from lengths ranging from 16 to 61 bytes. In contrast, RLSDN
| 9 10 | 11  | 12  |     |     |     |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S or S , whereas S alone receives all 128 data packets generates the longest control packets, exceeding 100 bytes
| 14  | 15  | 13  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
transmittedbythesetwonodes. fornetworksizesof51to101nodes.EASDNfollowsnext,
WealsoobservefromTable7that,incontrasttoSPSDN, producingpacketsslightlyshorterthanthoseofRLSDNbut
EASDN allows sensor nodes to balance their data packets stillsignificantlylongerthanthoseofSPSDN,NB-SDWSN,
amongmultipleneighboringnodes.However,thisbalancing andNBSDN.Thisdisparityinthelengthsofcontrolpackets
isonlypartial(whichwillbereferredtoaspartialloadbalanc- arises from the content of the control packets: RLSDN and
ing),beinglimitedtoneighborslocatedclosetothesink.This EASDN embed a complete routing table in each packet,
isbecause,foreachsensornode,EASDNperiodicallyselects mappingeverysensornodetoitsassignedrelaynode.Incom-
a different neighboring node to serve as its relay, but the parison, SPSDN, NB-SDWSN, and NBSDN include only
| 207296 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
FIGURE7. TotalnumberofcontrolpacketsgeneratedwithintheWSNin
FIGURE6. Lengthofcontrolpacketsgeneratedbythecontrollerin EASDN,NBSDN,NB-SDWSN,RLSDN,andSPSDN.
EASDN,NBSDN,NB-SDWSN,RLSDN,andSPSDN.
| a single | routing path per | packet, | resulting | in  | substantially |     |
| -------- | ---------------- | ------- | --------- | --- | ------------- | --- |
shorterpacketlengths.
| Nonetheless, | NB-SDWSN | and | NBSDN | generate | slightly |     |
| ------------ | -------- | --- | ----- | -------- | -------- | --- |
shorterroutingpacketsthanSPSDN.Thisisbecause,before
| encapsulatingaroutingpath(e.g.,S |                                  |      | ,S         | ,...,S)intoapacket |     |     |
| -------------------------------- | -------------------------------- | ---- | ---------- | ------------------ | --- | --- |
|                                  |                                  |      | 1 2        | i                  |     |     |
| and transmitting                 | it to the                        | sink | S 1 , both | NB-SDWSN           |     | and |
| NBSDNexcludeS                    | fromthepath.Thenextnodeinthepath |      |            |                    |     |     |
1
| (i.e., S 2 )      | can implicitly infer | that   | S 1 is | its relay         | node, | as it |
| ----------------- | -------------------- | ------ | ------ | ----------------- | ----- | ----- |
| directly receives | the routing          | packet | from   | S . Consequently, |       |       |
1
| itisunnecessarytoexplicitlyindicatetoS |     |     |     | itsrelaynodeby |     |     |
| -------------------------------------- | --- | --- | --- | -------------- | --- | --- |
2
includingitintheroutingpath,whichreducesthelengthof
thecontrolpackets.Incontrast,SPSDNdoesnotimplement
thisoptimizationandretainstheentireroutingpathwithinthe
packet.
Figs.7and8presentthetotalnumberandlength(inbytes),
FIGURE8. LengthofcontrolpacketsgeneratedwithintheWSNinEASDN,
respectively,ofcontrolpacketsgeneratedbythenodeswithin NBSDN,NB-SDWSN,RLSDN,andSPSDN.
| the WSNs | when using   | EASDN,          | RLSDN, | SPSDN, |          | NB- |
| -------- | ------------ | --------------- | ------ | ------ | -------- | --- |
| SDWSN,   | and NBSDN at | the controller. |        | RLSDN  | produces |     |
thehighestcontroltrafficoverheadduetoitsrelianceonRL, packetcontainingaroutingpathfromwhichthenodedeter-
which requires frequent control packet exchanges between minesitsrelaynode.Conversely,NB-SDWSNandNBSDN,
byleveragingAlgorithm2,generateandtransmitaminimal
thecontrollerandthenodestodeterminetheoptimalrouting
tables.AnadditionalcontributingfactoristhatRLSDNgen- number of routing control packets with the objective that a
eratesbroadcast-basedroutingcontrolmessages,resultingin single control packet enables multiple nodes in the WSN to
redundant transmissions and a substantial increase in over- identifytheirrespectiverelaynodeswithoutrequiringsepa-
head.EASDNgenerateslesscontroloverheadthanRLSDN ratetransmissionstoeachnode.
butstillexhibitsanotableincreaseasthenetworksizescales.
SimilartoRLSDN,itsroutingcontrolpacketsarebroadcast- 3) NETWORKLIFETIME
based, which significantly contributes to the overall control Fig. 9 depicts the WSN lifetime, expressed in milliseconds,
overhead. asafunctionofnetworksizeforthefiveroutingalgorithms.
Contrastingly, SPSDN, NB-SDWSN, and NBSDN sub- NBSDN consistently attains the longest lifetime across all
stantially reduce control overhead, as they utilize unicast networkscales,followedbyNB-SDWSN,EASDN,RLSDN,
control messages, thereby avoiding redundant retransmis- andSPSDN.ThesuperiorperformancebehaviorofNBSDN
sions,andthusminimizingtotalcontroltraffic.Nevertheless, andNB-SDWSNovertheotheralgorithmsisattributed,first,
NB-SDWSNandNBSDNachievelowercontroltrafficover- totheirabilitytobalancetheloadevenlyamongneighboring
head than SPSDN. This is because SPSDN generates and sensor nodes, resulting in uniform energy consumption and
transmits,foreachsensornodeintheWSN,aroutingcontrol preventing premature energy depletion in individual nodes.
VOLUME13,2025 207297

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
|     |     |     |     |     |     |     |     | FIGURE10. | PacketlossrateinEASDN,NBSDN,NB-SDWSN,RLSDN,and |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------------------------------------------- | --- | --- | --- | --- | --- |
FIGURE9. NetworklifetimeinEASDN,NBSDN,NB-SDWSN,RLSDN,and
SPSDN.
SPSDN.
|            |              |     |         |           |     |              |     | primarily | due to | the generation |     | of longer | routing | control |
| ---------- | ------------ | --- | ------- | --------- | --- | ------------ | --- | --------- | ------ | -------------- | --- | --------- | ------- | ------- |
| This leads | to increased |     | network | longevity |     | and extended |     |           |        |                |     |           |         |         |
packets,asshowninFig.6.Suchcontrolpacketsleadtoearly
| operational | time. | Second, | both | NBSDN | and | NB-SDWSN |     |     |     |     |     |     |     |     |
| ----------- | ----- | ------- | ---- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
energydepletionofnodeslocatedimmediatelynearthesink,
generateminimalcontroltrafficoverheadwithinthenetwork, astheyarethefirsttoreceivethem.Thesubsequentdepletion
therebypreservingnodeenergyandfurthercontributingtoan
|     |     |     |     |     |     |     |     | of these nodes |     | leads to | the isolation | of  | other | nodes from |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ------------- | --- | ----- | ---------- |
extendednetworklifetime.However,thelifetimeoftheWSN the sink, preventing them from delivering their packets and
| is further | prolonged | when | the | controller | employs | NBSDN |     |     |     |     |     |     |     |     |
| ---------- | --------- | ---- | --- | ---------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
therebyincreasingpacketloss.SPSDNexperiencesthehigh-
comparedtoNB-SDWSN.Thisimprovementisattributedto
|     |     |     |     |     |     |     |     | est packet | loss, | especially | in dense | networks. | This | behavior |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ---------- | -------- | --------- | ---- | -------- |
thefactthatNBSDN,unlikeNB-SDWSN,considersthelink is attributed to the absence of a load-balancing mechanism,
qualityparameterwhenselectingarelaynodeforeachsensor
|     |     |     |     |     |     |     |     | which causes | uneven | energy | consumption |     | and | the prema- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ------ | ----------- | --- | --- | ---------- |
node. Consequently, NBSDN, in contrast to NB-SDWSN, ture depletion of specific nodes. Consequently, these nodes
| avoids the | selection | of  | relay | nodes | with poor | link quality, |     |     |     |     |     |     |     |     |
| ---------- | --------- | --- | ----- | ----- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
becomenonfunctionalearlierthantheothers,andthenodes
| enabling | sensor | nodes | to successfully |     | transmit | packets | to  |     |     |     |     |     |     |     |
| -------- | ------ | ----- | --------------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
relyingonthemasrelaysremainisolatedforextendedperi-
their relay nodes on the first attempt without transmission ods. During this time, packets transmitted by the isolated
errors.Thiseliminatestheneedforretransmissions,thereby
|                                                      |     |     |     |     |     |     |     | nodes fail  | to reach | the | sink, contributing |     | significantly | to  |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ------------------ | --- | ------------- | --- |
| conservingnodeenergyandultimatelyextendingthenetwork |     |     |     |     |     |     |     | packetloss. |          |     |                    |     |               |     |
lifetime.Ontheotherhand,EASDNachievesashorternet-
|               |          |     |          |     |               |     |       | In contrast, | NBSDN | demonstrates |     | superior | robustness | to  |
| ------------- | -------- | --- | -------- | --- | ------------- | --- | ----- | ------------ | ----- | ------------ | --- | -------- | ---------- | --- |
| work lifetime | compared |     | to NBSDN |     | and NB-SDWSN, |     | as it |              |       |              |     |          |            |     |
packetlossandsustainshigherdatadeliveryreliability,even
performs only partial load balancing and introduces signif- in large-scale deployments. This performance advantage is
| icant control | overhead. |     | RLSDN, | despite | promoting |     | global |            |            |                |     |            |     |            |
| ------------- | --------- | --- | ------ | ------- | --------- | --- | ------ | ---------- | ---------- | -------------- | --- | ---------- | --- | ---------- |
|               |           |     |        |         |           |     |        | due to its | integrated | load-balancing |     | mechanism, |     | which pro- |
loadbalancing,performsworsethanEASDNduetoitssub- motes uniform energy consumption among sensor nodes.
stantiallyhighercontroltrafficoverhead.SPSDNexhibitsthe As a result, nodes tend to deplete their energy and become
| shortest | network | lifetime | due | to the | absence | of any | load- |     |     |     |     |     |     |     |
| -------- | ------- | -------- | --- | ------ | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
non-functionalnearlysimultaneously.Whentherelaynodes
balancing mechanism. This limitation causes rapid energy fail, the dependent sensor nodes remain active but are iso-
| depletion | in specific | nodes, | particularly |     | those | in proximity |     |            |          |        |       |               |     |              |
| --------- | ----------- | ------ | ------------ | --- | ----- | ------------ | --- | ---------- | -------- | ------ | ----- | ------------- | --- | ------------ |
|           |             |        |              |     |       |              |     | lated only | briefly, | during | which | they continue |     | transmitting |
tothesink,resultinginprematurenetworkshutdown.
packets.Thisshortisolationperiodleadstoalimitednumber
|     |     |     |     |     |     |     |     | of lost packets. |     | Although | NB-SDWSN |     | enables | global load |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | -------- | --- | ------- | ----------- |
4) PACKETLOSS balancing similar to NBSDN, as demonstrated in Table 7,
Fig.10presentsthepacketlossratesacrossvariousnetwork it exhibits a higher packet loss rate. This difference in
sizes for the controller-based routing algorithms: EASDN, performance is due to the fact that NBSDN, unlike NB-
RLSDN, SPSDN, NB-SDWSN, and NBSDN. The results SDWSN, incorporates buffer occupancy as a feature in
indicatethatNBSDNachievesthelowestpacketloss,main- the relay node selection procedure. Consequently, NBSDN
taining stable delivery ratios as the network size increases, avoids choosing relay nodes with loaded buffers, thereby
followed by NB-SDWSN. RLSDN and EASDN exhibit mitigating node overload and congestion and thus reducing
| higher packet | loss | rates | than | NBSDN | and | NB-SDWSN, |     | packetloss. |     |     |     |     |               |     |
| ------------- | ---- | ----- | ---- | ----- | --- | --------- | --- | ----------- | --- | --- | --- | --- | ------------- | --- |
| 207298        |      |       |      |       |     |           |     |             |     |     |     |     | VOLUME13,2025 |     |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
| FIGURE11. | DatathroughputinEASDN,NBSDN,NB-SDWSN,RLSDN,and |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SPSDN.
|                   |          |             |          |     |             | FIGURE12. | NetworklatencyinEASDN,NBSDN,NB-SDWSN,RLSDN,and |     |     |     |     |     |
| ----------------- | -------- | ----------- | -------- | --- | ----------- | --------- | ---------------------------------------------- | --- | --- | --- | --- | --- |
| 5) DATATHROUGHPUT |          |             |          |     |             | SPSDN.    |                                                |     |     |     |     |     |
| Fig. 11 shows     | the data | throughput, | measured |     | in bits per |           |                                                |     |     |     |     |     |
second,obtainedinWSNsofdifferentsizesacrosscontroller
| configurations | based on | EASDN, | RLSDN, | SPSDN, | NB- |                    |     |       |       |      |                    |     |
| -------------- | -------- | ------ | ------ | ------ | --- | ------------------ | --- | ----- | ----- | ---- | ------------------ | --- |
|                |          |        |        |        |     | avoids designating |     | relay | nodes | with | poor communication |     |
SDWSN,andNBSDN.Theresultsrevealthatthethroughput links,therebyminimizingpacketretransmissionsduetocol-
increasesforthefiveroutingalgorithmsasthenetworksize lisions and associated delays, which further contribute to
increases.NBSDNconsistentlyachievesthehighestthrough-
latencyreduction.
put,particularlyindensenetworkscenarios,duetoitsability NB-SDWSNachievesthesecond-lowestnetworklatency,
| to extend | network lifetime | and | reduce packet |     | loss, thereby |               |     |        |        |     |        |          |
| --------- | ---------------- | --- | ------------- | --- | ------------- | ------------- | --- | ------ | ------ | --- | ------ | -------- |
|           |                  |     |               |     |               | outperforming |     | RLSDN, | EASDN, | and | SPSDN. | Its per- |
enablingthetransmissionandsuccessfuldeliveryofagreater
|     |     |     |     |     |     | formance | advantage |     | is attributed | to  | its effective | global |
| --- | --- | --- | --- | --- | --- | -------- | --------- | --- | ------------- | --- | ------------- | ------ |
number of data packets from sensor nodes to the sink. NB- load-balancingmechanism,whichpreventsnodesfromper-
SDWSNexhibitsslightlylowerthroughputthanNBSDNbut
|     |     |     |     |     |     | sistently | forwarding | traffic |     | through the | same | neighbor or |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | ------- | --- | ----------- | ---- | ----------- |
outperforms EASDN, RLSDN, and SPSDN, owing to its a limited subset of neighbors. This mitigates traffic con-
| improved | network longevity |     | and reduced | packet | loss rate. |     |     |     |     |     |     |     |
| -------- | ----------------- | --- | ----------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
centration,reducesexcessivebufferoccupancyatindividual
EASDNisrankednexttoNB-SDWSN,surpassingRLSDN
|     |     |     |     |     |     | relay nodes, | and | shortens | queuing | delays. | RLSDN | exhibits |
| --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------- | ------- | ----- | -------- |
and SPSDN, as it prolongs the network operational time lowerlatencythanEASDNandSPSDNbuthigherthanNB-
| and mitigates | packet loss | more | effectively | than | the other |     |     |     |     |     |     |     |
| ------------- | ----------- | ---- | ----------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
SDWSN.AlthoughRLSDNsupportsgloballoadbalancing,
approaches.Nonetheless,SPSDNhasthelowestthroughput, its substantial control traffic overhead increases buffer uti-
| primarily | due to its shortest | network | operation |     | time and the |     |     |     |     |     |     |     |
| --------- | ------------------- | ------- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
lizationatnodes.Consequently,incomingpacketsexperience
| highest packet | loss rate | among | the evaluated | routing | algo- |            |         |      |     |           |       |             |
| -------------- | --------- | ----- | ------------- | ------- | ----- | ---------- | ------- | ---- | --- | --------- | ----- | ----------- |
|                |           |       |               |         |       | additional | waiting | time | due | to buffer | space | occupied by |
rithms. control messages. EASDN, despite generating less control
trafficthanRLSDN,showshigherlatencybecauseitemploys
6) NETWORKLATENCY onlyapartialload-balancingmechanism.Asaresult,network
Fig. 12 reports the end-to-end latency, in milliseconds, traffic tends to converge on the same subset of neighbors,
for WSNs of different sizes when the controller operates causing rapid buffer buildup and longer queuing delays at
withEASDN,RLSDN,SPSDN,NB-SDWSN,andNBSDN. intermediatenodes.Finally,SPSDNhasthehighestnetwork
Among the five competing algorithms, NBSDN achieves latency among the routing algorithms, primarily due to the
the lowest network latency across all network sizes. This lackofaload-balancingmechanism.Allpacketsgeneratedby
improvement stems from NBSDN’s joint consideration of anodeareforwardedthroughasingleneighbor,causingrapid
node buffer occupancy and link quality parameters when buffer congestion at that node. This congestion increases
selecting relay nodes, unlike NB-SDWSN and the other queuingtimefornewlyarrivingpackets,therebyelevatingthe
algorithms. By accounting for buffer occupancy, NBSDN overallnetworklatency.
prevents the selection of relay nodes with heavily loaded Let us conclude this section by reflecting on the overall
buffers,ensuringthattrafficisforwardedthroughnodeswith findings and implications of the above comparative evalu-
lighterbufferutilization.Thisreducespacketqueuingdelays ation. The results demonstrate that the proposed NBSDN
at the relay nodes and, consequently, the overall network algorithmoffersnotableperformancegainsundertheexam-
latency. Furthermore, by considering link quality, NBSDN inedstaticWSNscenarios.Specifically,NBSDNconsistently
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     | 207299 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
achieves effective global load balancing by evenly dis- trol traffic generation, network lifetime, packet loss, data
tributingtrafficamongneighboringnodes,therebyreducing throughput,andnetworklatency.Notably,loadbalancingand
congestion and extending network lifetime. It also intro- control traffic—metrics often omitted in existing SDWSN
duces minimal control overhead, generating the fewest and routing studies—are included here due to their critical
shortest control packets among all evaluated algorithms, impact on overall network performance, providing a more
and maintaining stable overhead as the network size scales complete and robust evaluation. Simulations across both
up. Although NBSDN relies on periodic routing updates small and large network scenarios have demonstrated that
(every60seconds),whichcanlimitresponsivenesstosudden NBSDN consistently outperforms established algorithms,
topological changes such as node failures or traffic bursts, including Dijkstra’s shortest path (SPSDN), Energy-Aware
it nevertheless demonstrates a favorable trade-off between SDN (EASDN), Naïve Bayes for SDWSN (NB-SDWSN),
routingefficiency,scalability,andcontroloverheadinstatic and Reinforcement Learning–based routing for the SDN
SDN-basedWSNs. controller (RLSDN). The results confirm NBSDN’s effec-
It is important to note that this study has focused exclu- tiveness, achieving longer network lifetime, reduced packet
sively on static topologies, in line with prior research work loss, lower control overhead, decreased latency, and higher
onSPSDN[3],EASDN[6],RLSDN[7],NB-SDWSN[20], data throughput across diverse network configurations. The
and other related routing protocols [4], [9], [12], [30], [32], findings of this study highlight the potential of NBSDN as
duetoconstraintsincomputationalresourcesandtheexces- an efficient and reliable approach to routing in SDWSNs.
sive simulation time required to accurately model mobility. The ability of NBSDN to adapt to dynamic network condi-
WhileNBSDNisexpectedtoretainitsrelativeperformance tions and optimize resource utilization offers a scalable and
advantageunderlow-mobilityconditions,itseffectiveness— practicalsolutionforIoTapplications,particularlyinenergy-
like that of the other competing algorithms—is likely to constrainedenvironments.
degradeasnodemobilityincreases,primarilyduetooutdated Future work will explore several directions for further
routing information and elevated control overhead. In such enhancementandvalidation.Theseincludetheevaluationof
dynamic settings, adaptive or predictive routing strategies NBSDN in mobile network scenarios and the integration of
may be necessary to sustain performance. Nonetheless, the additionalfeatures,suchasmobilitypredictionandlinksta-
findings presented in this study provide strong evidence of bility,toenablethealgorithmtooperateeffectivelyinmobile
NBSDN’ssuitabilityforpracticaldeploymentswheremobil- network environments. Real-world experimental validations
ityislimitedorinfrequent.Suchscenariosaretypicalofmany will also be performed to assess the practical applicability
real-worldWSNapplications,includingenvironmentalmon- androbustnessofNBSDNinlarge-scaleandmobileIoTand
itoring, industrial automation, structural health monitoring, SDWSNdeployments.
pipelinesurveillance,andprecisionagriculture,wheresensor
| nodesaregenerallystationaryorexhibitnegligiblemovement |     |     |     |     |     |     |     | REFERENCES |     |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
overtime[49]. [1] S.R.J.Ramson,S.Vishnu,andM.Shanmugam,‘‘ApplicationsofInternet
ofThings(IoT)—Anoverview,’’inProc.5thInt.Conf.Devices,Circuits
Syst.(ICDCS),Coimbatore,India,Mar.2020,pp.92–95.
VII. CONCLUSIONANDFUTUREWORK [2] F.Bannour,S.Souihi,andA.Mellouk,Software-DefinedNetworking2:
This study has introduced an enhanced Naïve Bayes-based ExtendingSDNControlToLarge-ScaleNetworks.Hoboken,NJ,USA:
routing algorithm (referred to as NBSDN) for the SDN Wiley,2022,doi:10.1002/9781394186181.
|             |          |             |     |                 |     |             |     | [3] L. Galluccio, | S.  | Milardo, | G. Morabito, | and | S. Palazzo, | ‘‘SDN-WISE: |     |
| ----------- | -------- | ----------- | --- | --------------- | --- | ----------- | --- | ----------------- | --- | -------- | ------------ | --- | ----------- | ----------- | --- |
| controller, | designed | to overcome |     | the limitations |     | of existing |     |                   |     |          |              |     |             |             |     |
Design,prototypingandexperimentationofastatefulSDNsolutionfor
| routing | protocols | developed | for | Software-Defined |     | Wireless |     |     |     |     |     |     |     |     |     |
| ------- | --------- | --------- | --- | ---------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
wirelesssensornetworks,’’inProc.IEEEConf.Comput.Commun.(INFO-
SensorNetworks(SDWSNs).NBSDNleveragesprobabilis- COM),Apr.2015,pp.513–521.
|                     |     |     |          |         |              |     |       | [4] M. Baddeley, | R.  | Nejabati, | G. Oikonomou, |     | M. Sooriyabandara, |     | and |
| ------------------- | --- | --- | -------- | ------- | ------------ | --- | ----- | ---------------- | --- | --------- | ------------- | --- | ------------------ | --- | --- |
| tic decision-making |     | to  | optimize | routing | by selecting |     | relay |                  |     |           |               |     |                    |     |     |
D.Simeonidou,‘‘EvolvingSDNforlow-powerIoTnetworks,’’inProc.
| nodes based | on     | key features, |            | including | residual | energy,       |     |          |       |                      |     |           |            |      |       |
| ----------- | ------ | ------------- | ---------- | --------- | -------- | ------------- | --- | -------- | ----- | -------------------- | --- | --------- | ---------- | ---- | ----- |
|             |        |               |            |           |          |               |     | 4th IEEE | Conf. | Netw. Softwarization |     | Workshops | (NetSoft), | Jun. | 2018, |
| distance    | to the | sink, buffer  | occupancy, |           | and      | link quality. |     |          |       |                      |     |           |            |      |       |
pp.71–79.
|              |             |             |                 |             |              |     |         | [5] J. Wang, | Y. Miao, | P. Zhou, | M. S.   | Hossain,      | and S.M.M.Rahman, |            | ‘‘A  |
| ------------ | ----------- | ----------- | --------------- | ----------- | ------------ | --- | ------- | ------------ | -------- | -------- | ------- | ------------- | ----------------- | ---------- | ---- |
| By utilizing | the         | centralized | decision-making |             | capabilities |     | of      |              |          |          |         |               |                   |            |      |
|              |             |             |                 |             |              |     |         | software     | defined  | network  | routing | in wireless   | multihop          | network,’’ |      |
| the SDN      | controller, | NBSDN       |                 | effectively | balances     |     | traffic |              |          |          |         |               |                   |            |      |
|              |             |             |                 |             |              |     |         | J. Netw.     | Comput.  | Appl.,   | vol.    | 85, pp.76–83, | May               | 2017,      | doi: |
loads among neighboring nodes and reduces control traffic 10.1016/j.jnca.2016.12.007.
overhead. These mechanisms collectively contribute to an [6] M. Younus, S. Islam, and S. Kim, ‘‘Proposition and real-time imple-
extended network lifespan and improved network perfor- mentation of an energy-aware routing protocol for a software defined
wirelesssensornetwork,’’Sensors,vol.19,no.12,p.2739,Jun.2019,doi:
| mance. |     |     |     |     |     |     |     | 10.3390/s19122739. |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
This work presented one of the first comprehensive eval- [7] M.U.Younus,M.K.Khan,andA.R.Bhatti,‘‘Improvingthesoftware-
definedwirelesssensornetworksroutingperformanceusingreinforcement
| uations | of routing | algorithms |     | in SDWSNs, |     | addressing | a   |     |     |     |     |     |     |     |     |
| ------- | ---------- | ---------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
learning,’’IEEEInternetThingsJ.,vol.9,no.5,pp.3495–3508,Mar.2022,
notable gap in the existing literature. While prior research doi:10.1109/JIOT.2021.3102130.
has largely focused on small-scale networks and a limited [8] M.U.Younus,M.K.Khan,M.R.Anjum,S.Afridi,Z.A.Arain,and
A.A.Jamali,‘‘Optimizingthelifetimeofsoftwaredefinedwirelesssensor
| set of performance |     | metrics, |     | this study | assessed | network |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | --- | ---------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
networkviareinforcementlearning,’’IEEEAccess,vol.9,pp.259–272,
| performance | across | six | key metrics: | load | balancing, |     | con- |     |     |     |     |     |     |     |     |
| ----------- | ------ | --- | ------------ | ---- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
2021,doi:10.1109/ACCESS.2020.3046693.
| 207300 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
[9] D.Godfrey,B.Suh,B.H.Lim,K.-C.Lee,andK.-I.Kim,‘‘Anenergy- [29] T.Dokeroglu,E.Sevinc,T.Kucukyilmaz,andA.Cosar,‘‘Asurveyon
efficientroutingprotocolwithreinforcementlearninginsoftware-defined newgenerationMetaheuri3sticalgorithms,’’Comput.Ind.Eng.,vol.137,
wirelesssensornetworks,’’Sensors,vol.23,no.20,p.8435,Oct.2023, Nov.2019,Art.no.106040,doi:10.1016/j.cie.2019.106040.
doi:10.3390/s23208435. [30] C.-K. Ke, M.-Y. Wu, W.-H. Hsu, and C.-Y. Chen, ‘‘Discover the opti-
[10] A.Narwaria,V.Kumari,andA.P.Mazumdar,‘‘RL-EAR:Reinforcement malIoTpacketsroutingpathofsoftware-definednetworkviaartificial
learning-based energy-aware routing for software-defined wireless sen- beecolonyalgorithm,’’inProc.12thEAIInt.Conf.WirelessInternets,
sor network,’’ J. Supercomput., vol. 81, no. 3, p. 485, Feb. 2025, doi: Nov.2019,pp.147–162.
10.1007/s11227-025-06998-1. [31] D. Karaboga and B. Basturk, ‘‘A powerful and efficient algorithm for
[11] A. K. Shakya, G. Pillai, and S. Chakrabarty, ‘‘Reinforcement learning numericalfunctionoptimization:Artificialbeecolony(ABC)algorithm,’’
algorithms: A brief survey,’’ Expert Syst. Appl., vol. 231, Nov. 2023, J. Global Optim., vol. 39, no. 3, pp.459–471, Apr. 2007, doi:
10.1007/s10898-007-9149-x.
Art.no.120495,doi:10.1016/j.eswa.2023.120495.
[12] V. Tyagi and S. Singh, ‘‘GM-WOA: A hybrid energy efficient clus- [32] N. Abdolmaleki, M. Ahmadi, H. T. Malazi, and S. Milardo, ‘‘Fuzzy
ter routing technique for SDN-enabled WSNs,’’ J. Supercomput., topologydiscoveryprotocolforSDN-basedwirelesssensornetworks,’’
vol. 79, no. 13, pp.14894–14922, Apr. 2023, doi: 10.1007/s11227- Simul. Model. Pract. Theory, vol. 79, pp.54–68, Dec. 2017, doi:
| 023-05263-7. |     |     |     |     |     |     | 10.1016/j.simpat.2017.09.004. |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |
[13] M.Masood,M.M.Fouad,S.Seyedzadeh,andI.Glesk,‘‘Energyefficient [33] J.CliftonandE.Laber,‘‘Q-learning:Theoryandapplications,’’Annu.Rev.
Statist.Appl.,vol.7,no.1,pp.279–301,Mar.2020,doi:10.1146/annurev-
softwaredefinednetworkingalgorithmforwirelesssensornetworks,’’in
Proc.13thInt.ScientificConf.Sustain.,ModernSafeTransp.,May2019, statistics-031219-041220.
pp.1481–1488. [34] Z. Abbood, M. Shuker, Ç. Aydin, and D. Ç. Atilla, ‘‘Extending wire-
[14] J. Shreyas, D. Chouhan, M. Harshitha, P. K. Udayaprasad, and less sensor Networks’ lifetimes usingdeep reinforcement learning in a
S. M. D. Kumar, ‘‘Network lifetime enhancement routing algorithm software-definednetworkarchitecture,’’AcademicPlatformJ.Eng.Sci.,
vol.9,no.1,pp.39–46,Jan.2021,doi:10.21541/apjes.687496.
| for IoT | enabled | software defined | wireless | sensor | network,’’ | in Proc. |     |     |     |     |     |     |
| ------- | ------- | ---------------- | -------- | ------ | ---------- | -------- | --- | --- | --- | --- | --- | --- |
3rd Int. Conf. Sustain. Adv. Comput., Bangalore, India, Mar. 2022, [35] K. Arulkumaran, M. P. Deisenroth, M. Brundage, and A. A. Bharath,
pp.499–508. ‘‘Deep reinforcement learning: A brief survey,’’ IEEE Signal
[15] R. Samadi, A. Nazari, and J. Seitz, ‘‘Intelligent energy-aware rout- Process. Mag., vol. 34, no. 6, pp.26–38, Nov. 2017, doi:
ing protocol in mobile IoT networks based on SDN,’’ IEEE Trans. 10.1109/MSP.2017.2743240.
[36] A.PrakashandS.Chauhan,‘‘Acomprehensivesurveyoftrendingtools
| Green | Commun. | Netw., vol. | 7, no. | 4, pp.2093–2103, |     | Dec. 2023, doi: |     |     |     |     |     |     |
| ----- | ------- | ----------- | ------ | ---------------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
andtechniquesindeeplearning,’’inProc.Int.Conf.DisruptiveTechnol.
10.1109/TGCN.2023.3296272.
[16] R. J. Kavitha and P. Anandavalli, ‘‘An efficient scyphozoa swarm (ICDT),May2023,pp.289–292.
optimization and fuzzy density-based clustering routing for underwater [37] Z.Li,F.Liu,W.Yang,S.Peng,andJ.Zhou,‘‘Asurveyofconvolutional
wirelesssensornetworks,’’TehničkiVjesnik,vol.31,no.5,pp.1589–1595, neuralnetworks:Analysis,applications,andprospects,’’IEEETrans.Neu-
ralNetw.Learn.Syst.,vol.33,no.12,pp.6999–7019,Dec.2022,doi:
Oct.2024,doi:10.17559/TV-20231121001131.
10.1109/TNNLS.2021.3084827.
| [17] N. Kumar | and D. | P. Vidyarthi, | ‘‘A | green routing | algorithm | for IoT- |     |     |     |     |     |     |
| ------------- | ------ | ------------- | --- | ------------- | --------- | -------- | --- | --- | --- | --- | --- | --- |
[38] T.-V.-T.DuongandL.H.Binh,‘‘IRSML:Anintelligentroutingalgorithm
| enabled | software | defined | wireless | sensor network,’’ |     | IEEE Sensors |     |     |     |     |     |     |
| ------- | -------- | ------- | -------- | ----------------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
J., vol. 18, no. 22, pp.9449–9460, Nov. 2018, doi: 10.1109/JSEN. basedonmachinelearninginsoftwaredefinedwirelessnetworking,’’ETRI
2018.2869629. J.,vol.44,no.5,pp.733–745,Aug.2022,doi:10.4218/etrij.2021-0212.
[18] R.Ramteke,S.Singh,andA.Malik,‘‘Optimizedroutingtechniquefor [39] A.Bahmer,D.Gupta,andF.Effenberger,‘‘Modernartificialneuralnet-
works:Isevolutioncleverer?’’NeuralComput.,vol.35,no.5,pp.763–806,
IoTenabledsoftware-definedheterogeneousWSNsusinggeneticmuta-
Apr.2023,doi:10.1162/neco_a_01575.
| tion based | PSO,’’ | Comput. | Standards | Interfaces, | vol. | 79, Jan. 2022, |     |     |     |     |     |     |
| ---------- | ------ | ------- | --------- | ----------- | ---- | -------------- | --- | --- | --- | --- | --- | --- |
Art.no.103548,doi:10.1016/j.csi.2021.103548. [40] S.Chua,A.Tan,P.N.E.Nohuddin,andM.H.AhmadHijazi,‘‘Com-
[19] M.A.Tawfeek,I.Alrashdi,M.Alruwaili,L.Jamel,G.F.Elhady,and paring the effectiveness and efficiency of machine learning models for
H.Elwahsh,‘‘Improvingenergyefficiencyandroutingreliabilityinwire- spamdetectiononTwitter,’’J.Adv.Res.Appl.Sci.Eng.Technol.,vol.60,
pp.127–138,Oct.2024,doi:10.37934/araset.61.2.127138.
lesssensornetworksusingmodifiedantcolonyoptimization,’’EURASIP
[41] U.Hassan,Z.U.Rehman,I.Ahmad,andS.U.Islam,‘‘Analyzingthe
| J. Wireless | Commun. | Netw., | vol. 2025, | no. 1, | p. 22, | Apr. 2025, doi: |     |     |     |     |     |     |
| ----------- | ------- | ------ | ---------- | ------ | ------ | --------------- | --- | --- | --- | --- | --- | --- |
10.1186/s13638-025-02449-w. energyconsumptionofrandomforestandsupportvectormachinemodels:
[20] A.Tcherak,S.Loucif,andM.O.Khaoua,‘‘OnefficientroutingforSDN- Pavingthewayforgreenandsustainableartificialintelligence,’’Discover
basedwirelesssensornetworks,’’inProc.24thInt.ArabConf.Inf.Technol. InternetThings,vol.5,no.1,p.100,Sep.2025,doi:10.1007/s43926-
025-00188-4.
(ACIT),Ajman,UnitedArabEmirates,Dec.2023,pp.1–6.
[42] D.Kalibatiene˙andJ.Miliauskaite˙,‘‘Ahybridsystematicreviewapproach
[21] I.E.NaqaandM.J.Murphy,‘‘Whatismachinelearning?’’inMachine
|          |              |           |     |            |               |       | on complexity |     | issues in | data-driven | fuzzy inference | systems develop- |
| -------- | ------------ | --------- | --- | ---------- | ------------- | ----- | ------------- | --- | --------- | ----------- | --------------- | ---------------- |
| Learning | in Radiation | Oncology: |     | Theory and | Applications. | Cham, |               |     |           |             |                 |                  |
Switzerland:Springer,Jan.2015,pp.3–11. ment,’’ Informatica, vol. 32, pp.85–118, Jan. 2021, doi: 10.15388/21-
| [22] P.J.B.Pajila,B.G.Sheena,A.Gayathri,J.Aswini,M.Nalini,andR. |     |     |     |     |     |     | infor444. |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
[43] I.WickramasingheandH.Kalutarage,‘‘Naivebayes:Applications,vari-
| S. Subramanian, |     | ‘‘A comprehensive |     | survey on | naive Bayes | algorithm: |     |     |     |     |     |     |
| --------------- | --- | ----------------- | --- | --------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
ationsandvulnerabilities:Areviewofliteraturewithcodesnippetsfor
Advantages,limitationsandapplications,’’inProc.4thInt.Conf.Smart
implementation,’’SoftComput.,vol.25,no.3,pp.2277–2293,Sep.2020,
Electron.Commun.(ICOSEC),Trichy,India,Sep.2023,pp.1228–1234.
doi:10.1007/s00500-020-05297-6.
[23] WirelessMediumAccessControl(MAC)andPhysicalLayer(PHY)Spec-
[44] D.Berrar,Bayes’TheoremandNaiveBayesClassifierinEncyclopediaof
ificationsforLow-RateWirelessPersonalAreaNetworks(LR-WPANs), BioinformaticsandComputationalBiology.Amsterdam,TheNetherlands:
StandardStandard2006;802:4,2006.
Elsevier,2024,pp.483–494.
[24] N.McKeown,‘‘OpenFlow,’’ACMSIGCOMMComput.Commun.Rev.,
|     |     |     |     |     |     |     | [45] Y. Chapre, | P.  | Mohapatra, | S. Jha, | and A. Seneviratne, | ‘‘Received sig- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | ------- | ------------------- | --------------- |
vol.38,no.2,pp.69–74,Mar.2008,doi:10.1145/1355734.1355746.
|     |     |     |     |     |     |     | nal strength | indicator | and | its analysis | in a typical | WLAN system,’’ |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | ------------ | ------------ | -------------- |
[25] S.Chakrabarty,D.W.Engels,andS.Thathapudi,‘‘BlackSDNforthe
|                                                              |     |     |     |     |     |     | in Proc.    | 38th | Annu. IEEE | Conf. | Local Comput. | Netw., Oct. 2013, |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------- | ---- | ---------- | ----- | ------------- | ----------------- |
| InternetofThings,’’inProc.IEEE12thInt.Conf.MobileAdHocSensor |     |     |     |     |     |     | pp.304–307. |      |            |       |               |                   |
Syst.,Oct.2015,pp.190–198. [46] C.Thomson,I.Romdhani,A.Y.AlDubai,M.Qasem,B.Ghaleb,and
[26] A.ElYazidi,M.ElKamili,andM.L.Hasnaoui,‘‘BlackSDNforWSN,’’
|     |     |     |     |     |     |     | I. Wadhaj, | ‘‘Cooja | Simulator | Manual,’’ | Edinburgh | Napier University, |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --------- | --------- | --------- | ------------------ |
inProc.1stInt.Conf.SmartSyst.DataSci.(ICSSD),Rabat,Morocco,
Dubai,U.K.,Jul.2016.
Oct.2019,pp.1–4.
[47] IEEEStandardforLow-rateWirelessNetworks,StandardIEEE802.15.4–
| [27] M. U. | Farooq, | X. Wang, | A. Hawbani, | L.  | Zhao, A. | Al-Dubai, and | 2015,2015. |     |     |     |     |     |
| ---------- | ------- | -------- | ----------- | --- | -------- | ------------- | ---------- | --- | --- | --- | --- | --- |
O.Busaileh,‘‘SDORP:SDNbasedopportunisticroutingforasynchronous [48] F.Osterlind,A.Dunkels,J.Eriksson,N.Finne,andT.Voigt,‘‘Cross-level
wirelesssensornetworks,’’IEEETrans.MobileComput.,vol.22,no.8, sensornetworksimulationwithCOOJA,’’inProc.31stIEEEConf.Local
pp.4912–4929,Aug.2023,doi:10.1109/TMC.2022.3158695.
Comput.Netw.,Tampa,FL,USA,Nov.2006,pp.641–648.
| [28] F. S. | Gharehchopogh | and | H. Gholizadeh, | ‘‘A | comprehensive | survey: |            |          |            |        |                     |                 |
| ---------- | ------------- | --- | -------------- | --- | ------------- | ------- | ---------- | -------- | ---------- | ------ | ------------------- | --------------- |
|            |               |     |                |     |               |         | [49] S. El | Khediri, | ‘‘Wireless | sensor | networks: A survey, | categorization, |
Whaleoptimizationalgorithmanditsapplications,’’SwarmEvol.Comput.,
mainissues,andfutureorientationsforclusteringprotocols,’’Computing,
| vol.48,pp.1–24,Aug.2019. |     |     |     |     |     |     | vol.104,no.8,pp.1775–1837,Mar.2022. |     |     |     |     |        |
| ------------------------ | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | ------ |
| VOLUME13,2025            |     |     |     |     |     |     |                                     |     |     |     |     | 207301 |

A.Tcheraketal.:EfficientRoutingforSoftware-DefinedWSNs:ANaïveBayesApproach
AMINETCHERAKreceivedthebachelor’sdegree MOHAMED OULD KHAOUA was a Pro-
in computer systems from the University of fessor with Sultan Qaboos University, Oman,
Algiers1,Algeria,andthemaster’sdegreeinnet- from2007to2015;aReaderwithGlasgowUni-
worksandcomputersystemsfromtheUniversity versity,U.K.,from2000to2006;aLecturerwith
ofBlida1,Algeria,whereheiscurrentlypursuing StrathclydeUniversity,U.K.,from1997to2000;
thePh.D.degreeinnetworksanddistributedsys- andaPostdoctoralResearchFellowwithTeesside
temswiththeDepartmentofComputerScience. University,U.K.,from 1994to1997.Heis cur-
Hehastaughttheoperatingsystemsmodulewith rentlyaProfessorwiththeDepartmentofCom-
theDepartmentofComputerScience,University puter Science, University of Blida 1, Algeria.
ofBlida1.Inaddition,hewasaDeveloperofweb He is a member of the LRDSI Research Lab-
and mobile applications, as well as the Internet of Things and machine oratory, University of Blida 1. His research interests include computer
learning-basedapplications,foracompanyinAlgeria. networking,wirelessnetworks,performancemodeling,andcomputerarchi-
|     |     |     |     |     |     |     |     | tecture. He | has served as the Editor-in-Chief | for Journal of Engineering |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------------------------- | -------------------------- |
Research.HehasalsoservedontheEditorialBoardofreputablejournals,
includingIEEETRANSACTIONSONPARALLELANDDISTRIBUTEDSYSTEMS,Interna-
tionalJournalofParallel,EmergentandDistributedSystems,International
SAMIALOUCIF(SeniorMember,IEEE)received JournalofComputersandApplications,InternationalJournalofHighPer-
theBachelorofEngineeringdegreeincomputer formanceComputingandNetworking,andJournalofComputerandSystem
|     |     | sciencefromConstantineUniversity,Algeria,the |     |     |     |     |     | Sciences. |     |     |
| --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- |
master’sdegreeincomputersciencefromtheUni-
|     |     | versity | ofConstantine |     | (incollaboration |     | with the |     |     |     |
| --- | --- | ------- | ------------- | --- | ---------------- | --- | -------- | --- | --- | --- |
UniversityofGlasgow),andthePh.D.degreein
computersciencefromtheUniversityofGlasgow,
U.K.SheiscurrentlyanAssociateProfessorwith
|     |     | the | College | of Technological | Innovation, |     | Zayed |     |     |     |
| --- | --- | --- | ------- | ---------------- | ----------- | --- | ----- | --- | --- | --- |
University,UnitedArabEmirates.Beforejoining
ZayedUniversity,shewasanAssociateProfessorandtheChairwiththe
| Software | Engineering | Department, | ALHOSN |     | University; | a Postdoctoral |     |     |     |     |
| -------- | ----------- | ----------- | ------ | --- | ----------- | -------------- | --- | --- | --- | --- |
ResearchFellowwiththeUniversityofMoncton,NewBrunswick,Canada;
andanAssistantProfessorwithUAEUniversity.Shehasactivelycontributed
| to the academic       | community     |              | as a member | of            | organizing     | committees | for     |     |     |     |
| --------------------- | ------------- | ------------ | ----------- | ------------- | -------------- | ---------- | ------- | --- | --- | --- |
| several international |               | conferences. | She         | served        | on the program | committees |         |     |     |     |
| of over 30            | international | conferences  |             | and respected | journals.      | Her        | current |     |     |     |
researchinterestsincludeartificialintelligence(AI),machinelearning,and
| deep learning, | particularly  | their | applications |       | in communication |          | networks |     |     |     |
| -------------- | ------------- | ----- | ------------ | ----- | ---------------- | -------- | -------- | --- | --- | --- |
| and emerging   | technologies, |       | including    | DL in | SDN-based        | wireless | sensor   |     |     |     |
networks,delay-tolerantnetworks,AIinhealthcare,networksecurity,and
| AI ethics. | Her previous | research | interests | include | on-chip | networks | and |     |     |     |
| ---------- | ------------ | -------- | --------- | ------- | ------- | -------- | --- | --- | --- | --- |
mathematicalmodelingforcommunicationnetworks.Sheisamemberof
severalIEEEsocieties.
207302 VOLUME13,2025