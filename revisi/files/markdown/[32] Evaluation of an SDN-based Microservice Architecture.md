# [32] Evaluation of an SDN-based Microservice Architecture

> Source file: `[32] Evaluation of an SDN-based Microservice Architecture.pdf`

---

|     | Evaluation |     |     |     | of  | an  | SDN-based |     |     | Microservice |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --------- | --- | --- | ------------ | --- | --- | --- | --- | --- |
Architecture
|     |     |     |     | Anton | Ho¨lscher, |     | Mikael      | Asplund, | and         | Felipe  | Boeira |     |     |     |     |
| --- | --- | --- | --- | ----- | ---------- | --- | ----------- | -------- | ----------- | ------- | ------ | --- | --- | --- | --- |
|     |     |     |     |       | Department |     | of Computer | and      | Information | Science |        |     |     |     |     |
Linko¨ping
|     |     |     |        |                    |     |     | University,            |     | Sweden |                      |     |     |     |     |     |
| --- | --- | --- | ------ | ------------------ | --- | --- | ---------------------- | --- | ------ | -------------------- | --- | --- | --- | --- | --- |
|     |     |     | Email: | anton@holscher.se, |     |     | mikael.asplund@liu.se, |     |        | felipe.boeira@liu.se |     |     |     |     |     |
Abstract—Microservice architectures decompose applications to route the requests then the latency will increase by several
into individual components for enhanced maintainability and orders of magnitude. Such controller intervention is relatively
| horizontal    | scaling, | but           | also comes       | with | an  | increased | cost for |       |         |          |         |         |      |        |              |
| ------------- | -------- | ------------- | ---------------- | ---- | --- | --------- | -------- | ----- | ------- | -------- | ------- | ------- | ---- | ------ | ------------ |
|               |          |               |                  |      |     |           |          | rare, | meaning | that the | average | latency | will | not be | so affected, |
| orchestrating |          | the services. | Software-Defined |      |     | Networks  | (SDNs)   |       |         |          |         |         |      |        |              |
buthasasignificantimpactontheworst-caseor99-percentile
| enables | the dynamic |     | configuration | of  | network | switches | using |     |     |     |     |     |     |     |     |
| ------- | ----------- | --- | ------------- | --- | ------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
latencies.
controllers.Inthispaperweproposeamicroservicearchitecture
that leverages SDN to orchestrate the microservices with the In addition to assessing the latency of the SDN-based
goalofreducingtheorchestrationlatencycost.Weperformaset microservice orchestration, we have performed a set of ex-
| of experiments |     | using Mininet |     | in which | we implement |     | a tailor- |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------- | --- | -------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
perimentstocomparetwodifferentSDNcontrollersandthree
mademicroserviceapplicationthatusesSDNfororchestrationin
|     |     |     |     |     |     |     |     | load-balancing |     | algorithms | when | applied | in  | this context. | The |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | ---- | ------- | --- | ------------- | --- |
combinationwithasetofdifferentcontrollersandloadbalancers.
Ourresultsshowthatourproposedarchitectureperformsinthe taskofthecontrolleristoaltertheflowtableintheswitchand
same order of magnitude as a corresponding monolithic system. the task of the load-balancing algorithm is to determine the
|       |                      |     |     |                  |     |             |     | node | that | will serve | each request. | These | actions | are | necessary |
| ----- | -------------------- | --- | --- | ---------------- | --- | ----------- | --- | ---- | ---- | ---------- | ------------- | ----- | ------- | --- | --------- |
| Index | Terms—microservices, |     |     | software-defined |     | networking, | la- |      |      |            |               |       |         |     |           |
forthemicroserviceorchestrationtowork,andsincethereare
| tency, OpenFlow, |     | load | balancing    |     |     |     |     |           |          |               |                 |         |                |       |             |
| ---------------- | --- | ---- | ------------ | --- | --- | --- | --- | --------- | -------- | ------------- | --------------- | ------- | -------------- | ----- | ----------- |
|                  |     |      |              |     |     |     |     | different |          | designs and   | implementations |         | for            | these | components, |
|                  |     |      |              |     |     |     |     | we        | evaluate | how different |                 | choices | of controllers |       | and load-   |
|                  |     | I.   | INTRODUCTION |     |     |     |     |           |          |               |                 |         |                |       |             |
|                  |     |      |              |     |     |     |     | balancers |          | affect the    | overall         | system  | latency.       |       |             |
Developing and maintaining large-scale software projects Our contributions are threefold, we
| are error-prone |     | and | demanding | tasks. | There | is  | reason | to  |           |          |     |            |             |     |          |
| --------------- | --- | --- | --------- | ------ | ----- | --- | ------ | --- | --------- | -------- | --- | ---------- | ----------- | --- | -------- |
|                 |     |     |           |        |       |     |        |     | summarise | existing | SDN | controller | performance |     | studies, |
•
| believe | that dividing    |     | the system | into | smaller | sub-programs, |     |     |         |         |           |     |              |     |               |
| ------- | ---------------- | --- | ---------- | ---- | ------- | ------------- | --- | --- | ------- | ------- | --------- | --- | ------------ | --- | ------------- |
|         |                  |     |            |      |         |               |     | •   | propose | a novel | SDN-based |     | microservice |     | architecture, |
| where   | each sub-program |     | provides   | a    | single  | functionality |     | of  |         |         |           |     |              |     |               |
and
the system, could potentially result in reduced overall system implementatestenvironmenttoevaluatetheperformance
•
| complexity.       | Such            | a system     | architecture    |                | is typically  |              | referred    | to            |              |                    |                 |              |                 |              |             |
| ----------------- | --------------- | ------------ | --------------- | -------------- | ------------- | ------------ | ----------- | ------------- | ------------ | ------------------ | --------------- | ------------ | --------------- | ------------ | ----------- |
|                   |                 |              |                 |                |               |              |             |               | of the       | proposed           | architecture.   |              |                 |              |             |
| as a Microservice |                 | Architecture |                 | [3].           |               |              |             |               |              |                    |                 |              |                 |              |             |
|                   |                 |              |                 |                |               |              |             | The           | remainder    | of the             | paper           | is organised |                 | as follows:  | Sec-        |
| While             | microservices   |              | are developed   |                | as individual |              | functions   |               |              |                    |                 |              |                 |              |             |
|                   |                 |              |                 |                |               |              |             | tion          | II presents  | the                | background      | and          | related         | work,        | Section III |
| that communicate  |                 | in order     | to              | provide        | the required  |              | functional- |               |              |                    |                 |              |                 |              |             |
|                   |                 |              |                 |                |               |              |             | describes     |              | our implementation |                 | of an        | SDN-based       | microservice |             |
| ity, they         | are usually     | presented    |                 | to the         | users as      | a single     | system.     |               |              |                    |                 |              |                 |              |             |
|                   |                 |              |                 |                |               |              |             | orchestrator, |              | Section            | IV provides     |              | the methodology |              | used in     |
| This can          | be achieved     |              | by adding       | a microservice |               | orchestrator |             |               |              |                    |                 |              |                 |              |             |
|                   |                 |              |                 |                |               |              |             | the           | experiments, | Section            | V               | presents     | the             | results      | from the    |
| which is          | a separate      |              | microservice    | responsible    |               | for          | delegating  |               |              |                    |                 |              |                 |              |             |
|                   |                 |              |                 |                |               |              |             | experiments,  |              | and finally,       | Section         | VI           | concludes       | the          | paper.      |
| all incoming      | requests        |              | to the intended |                | microservice. |              | However,    |               |              |                    |                 |              |                 |              |             |
| adding            | an orchestrator |              | entails         | increased      | latency       | overhead     |             | of            |              |                    |                 |              |                 |              |             |
|                   |                 |              |                 |                |               |              |             |               |              |                    | II. RELATEDWORK |              |                 |              |             |
thesystemsinceallincomingpacketsneedtobereceivedand
forwarded by the orchestrator. Weorganisethissectionintwosubsections,(i)comparisons
In this paper we explore the possibility of lowering the on OpenFlow controllers and (ii) latency measurements of
|             |           |        |              |           |                  |      |            | microservice |          | architectures. |            |     |     |     |     |
| ----------- | --------- | ------ | ------------ | --------- | ---------------- | ---- | ---------- | ------------ | -------- | -------------- | ---------- | --- | --- | --- | --- |
| latency     | impacts   | of the | orchestrator |           | by incorporating |      | the or-    |              |          |                |            |     |     |     |     |
| chestrating | behaviour |        | within       | a switch. | The              | main | motivation |              |          |                |            |     |     |     |     |
|             |           |        |              |           |                  |      |            | A.           | OpenFlow | Controller     | Comparison |     |     |     |     |
forincorporatingthemicroserviceorchestratorintotheswitch
with the help of an SDN-based approach is to reduce the The controller is an external process connected to the
overall latency of service requests from clients. We have OpenFlow switch and is responsible for altering the switches’
performed a set of experiments to assess how well an SDN- flow table and may add/remove flow entries in the switch at
based mircoservice orchestrator performs in terms of latency, any time to adapt to the ever-changing network environment.
which will be affected in two ways. First, there is a certain When the switch receives a packet unmatched by the current
increased latency for every request that goes through the flow table, the packet is automatically sent to the controller,
switch due to time taken by the switching logic. Second, if which then deals with the packet instead. Thus, the controller
the switch needs to ask the controller for information on how gets notified of any flow table misses, and may alter the

flow table accordingly. We briefly summarise the most widely TABLEI
known SDN controllers below. SDN-CONTROLLERPERFORMANCEEVALUATIONS
The NOX controller was the first publicly available open
Lowest Highest
Controller IncludedinStudy
source controller software. Tootoonchian et al. [13] presented Latency Throughput
their slightly modified version of NOX, called NOX-MT, to NOX [4],[9],[11],[13] [13] [13]
POX [4],[9],[11],[12],[15]
show that some small alterations to the NOX controller could
Ryu [4],[8],[9],[11],[12],[15] [8],[12],[15]
improve its performance significantly. Beacon [4],[9],[11],[13],[15] [4],[11] [4],[9],[11]
POX is a Python implementation of NOX with some Floodlight [4],[8],[9],[11],[15]
OpenDaylight [8],[9],[12],[15] [9]
design alterations to improve performance [6]. However, the
ONOS [8],[9],[12],[15] [8],[12],[15]
POX controller is outperformed by most other available SDN
controllers in terms of latency and throughput [9].
Ryu is an SDN controller implemented in Python focusing minorincrease ofthe totallatency,they arguethat anincrease
onsimplicityandagiledevelopment.Ryuispubliclyavailable in the microservice granularity might still lead to a significant
andactivelydevelopedbyNTTandaimstobeaframeworkfor increase in the response time of a system.
building SDN applications rather than a complete controller Ueda et al. [14] examine the latency effects of utilising a
with all possible features built into the system. microservice architecture based on how the implementation
Beacon is a Java-based controller developed by Erick- differs from a monolithic server system. They find that the
son [4]. Beacon has shown to be one of the top performing performanceofthemicroserviceapproachisupto79%worse
controllers with respect to network throughput [4], [9], [11]. thanitsmonolithcounterpart,potentitiallycausedbyspending
It also performs well in terms of latency [4], [11]. considerable amount of time processing requests, instead of
Floodlight is an extension of the Beacon controller, and executingthebusinesslogicandalgorithmsoftheapplication.
hasanactivecommunityandcommercialbacking1.Floodlight GanandDelimitrou[5]implementedtwoseparatemoviere-
is widely used and has been used by companies such as viewandstreamingservices,oneusingamonolithicapproach
Canonical, CERN, SRI International, and others. and the other using a microservice architecture. Comparing
OpenDaylight is a decentralised controller, meaning that the performance of both systems, the microservice system
more than one controller node may be utilised to deal with outperformed the monolithic system at high server loads.
unresolved packets and alter the flow tables of the switches Basedontheavailableevidencethereisnoobviousconclu-
inthesystem[7].TheOpenDaylightcontrolleriswidelyused sion to be drawn on the relative performance of microservice
by many large corporations2. architectures compared to their monolithic counterparts. It is
ONOS [1] is a decentralised controller implemented in reasonable to assume that this will be very system-dependent
Java.ItwasfoundedbytheOpenNetworkingFoundationand and that the level of inter-dependence between services is an
serves as a fault-tolerant platform capable of automatic global important factor. Our analysis focuses on the orchestration
network discovery. ONOS supports SDN-Application hot- of services through an SDN controller and is not intended
plugging and automatically adapts to changes in the network to answer whether the microservice architecture approach is
environment.ItisbackedbycompaniessuchasGoogle,Intel, better or worse than monolithic systems.
AT&T and Samsung.
Multiple studies have been performed in order to compare III. SDN-BASEDMICROSERVICEORCHESTRATOR
the different controllers and convey the most fitting controller We propose to use an SDN controller to perform the
in various scenarios. Most studies involve measuring the microservice orchestration. To this end we have designed a
throughput and latency of packets in complex/large network prototype implementation to showcase this approach and to
structures while using different controller implementations use as a test object for performance measurements. When a
with varying number of threads. Table I shows how the client makes a request to the virtual IP address (VIP) of the
different controllers performed in each study. Note that the microservice, the packet is received at the SDN switch. The
table only considers the listed controllers. switch communicates with the currently attached controller,
As shown in the Table I, Beacon and ONOS each have the which utilises its currently attached load balancing algorithm
highest throughput in three of the studies and NOX in one. todecidewhichofthehoststhatwillreceivethepacket.Once
Ryu has the lowest latency in three studies, Beacon in two, a receiver is decided, the controller installs a flow entry into
and NOX and OpenDaylight in one each. In the evaluation by the switch and forwards the packet to the recipient.
Tootoonchianetal.[13],theyusedanolderversionofBeacon The prototype implementation consists of a microservice
compared to the other studies evaluating Beacon. implementation, a load listener and the controller software.
The load listener serves as a communication bridge between
B. Latency of Microservice Architectures
themicroserviceimplementationandthecontrollerinthecases
Shadija et al. [10] study how the chosen granularity of a
where a server-aware load balancer is used.
microservice affects its total latency. While they note only a
Implementing the microservice requires two separate com-
1BigSwitchNetworks:https://www.bigswitch.com/ ponents. The request handler responsible for handling in-
2https://www.opendaylight.org/use-cases-and-users coming requests and the load sender responsible for sending

the current server load to the load listener. We implemented evaluate the effectiveness of the utilised load balancer. Once
the microservice using C++ and the communication was the entire NFS is started, another client, referred to as the
implemented using the Linux socket interface. Main Client, begins issuing ping-requests to the microservice
The Request Handler. In order to keep the study focused IPandrecordtheirround-triptime(RTT).Anoverviewofthe
on the performance of the controllers and load balancers, as experiment is depicted in Figure 1.
opposedtotheperformanceoftheservers,theactualworkload For each controller and load balancer combination, the
in the experiments is synthethically generated. Each server experiment was performed ten times. Five times where each
node listens to a UDP socket. All packets received consist NFS client made a request with a static workload, referred
| of a single | positive | integer | denoting | the | amount | of simulated |     |           |        |              |              |     |            |       |
| ----------- | -------- | ------- | -------- | --- | ------ | ------------ | --- | --------- | ------ | ------------ | ------------ | --- | ---------- | ----- |
|             |          |         |          |     |        |              |     | to as the | Static | Microservice | Architecture |     | Experiment | (MAE- |
load this packet would require, which is a constant in the Static). The other five times, each NFS client got assigned
static request experiment and chosen randomly in the random a random request workload, and each request made by that
request experiment. The load is parsed by the server which client increased the server workload by the assigned amount.
increases its simulated load accordingly. This experiment is referred to as the Random Microservice
The Load Sender. The load sender is a component re- Architecture Experiment (MAE-Random).
sponsible for continuously updating the load listener with the Metrics. We perform measurements for five different
| load of                         | the server | node.    | In a set      | time interval, | the                  | load     | sender |             |              |        |           |         |         |                 |
| ------------------------------- | ---------- | -------- | ------------- | -------------- | -------------------- | -------- | ------ | ----------- | ------------ | ------ | --------- | ------- | ------- | --------------- |
|                                 |            |          |               |                |                      |          |        | latency     | percentiles, | 50%    | (median), |         | 90%,    | 99%, 99.99%,    |
| sends the                       | current    | load     | of the system | along          | with                 | a server | node   |             |              |        |           |         |         |                 |
|                                 |            |          |               |                |                      |          |        | 99.999%,    | as well      | as min | and max   | values. |         |                 |
| identifier                      | to a       | specific | UDP-port      | of the         | load listener.       |          |        |             |              |        |           |         |         |                 |
|                                 |            |          |               |                |                      |          |        | The         | other metric | that   | we focus  | on      | in this | work is the     |
| TheLoadListener.Theloadlistener |            |          |               |                | isresponsibleforlis- |          |        |             |              |        |           |         |         |                 |
|                                 |            |          |               |                |                      |          |        | server load | imbalance    |        | which can | be      | seen as | an inefficiency |
teningforthecurrentloadofeachserver-nodeandforwarding in the orchestration. DeRose et al. [2] designed the Load
ittotheSDNcontroller.Itforwardedtheloadtothecontroller
ImbalancePercentagemetricthatquantifieshowunevenlythe
| using POSIX |     | shared memory. |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
workloadwasbetweenseveralprocesses.Themetricisdefined
asfollows,whereI
|                                                        |     | IV. EXPERIMENTMETHOD |          |     |     |        |       |          |         | istheresultingloadimbalancepercentage, |     |             |         |              |
| ------------------------------------------------------ | --- | -------------------- | -------- | --- | --- | ------ | ----- | -------- | ------- | -------------------------------------- | --- | ----------- | ------- | ------------ |
|                                                        |     |                      |          |     |     |        |       | m is the | maximum | workload,                              | a   | is the      | average | workload and |
| A. Experiment                                          |     | Design               |          |     |     |        |       |          |         |                                        |     |             |         |              |
|                                                        |     |                      |          |     |     |        |       | n is the | number  | of processes                           | in  | the system: |         |              |
| Since                                                  | the | performance          | of using | an  | SDN | switch | as an |          |         |                                        |     |             |         |              |
| orchestratormightbetiedtotheperformanceofthecontroller |     |                      |          |     |     |        |       |          |         | m−a                                    |     | n           |         |              |
|                                                        |     |                      |          |     |     |        |       |          |         | I =                                    | ×   |             | ×100    |              |
itself, we performed a set of latency measurements using m n−1
| different   | SDN | controllers. |      |     |        |             |     |              |       |          |          |     |           |                |
| ----------- | --- | ------------ | ---- | --- | ------ | ----------- | --- | ------------ | ----- | -------- | -------- | --- | --------- | -------------- |
|             |     |              |      |     |        |             |     | In the cases | where | m        | = 0 or n | = 1 | we assign | I = 0, since   |
| Performance |     | Experiments. | Both | the | Switch | Performance |     |              |       |          |          |     |           |                |
|             |     |              |      |     |        |             |     | either there | is no | workload | or there | is  | only one  | process in the |
Experiment(SPE)andtheControllerPerformanceExperiment
(CPE) consist of an emulated network containing two clients system. Both cases imply that there is no server imbalance.
LatencyComparison.ToassessthelatencyeffectsofSDN-
andanSDNswitchconnectedtoanSDNcontroller.Oncethe
environment was set up and the controller initialised, one of based microservice orchestration it is important to find an
approachoffairlycomparingthedifferentsystems.Therefore,
| the clients | issued | 100    | 000 ping      | requests  | to the | other | client, |           |      |               |         |     |       |                |
| ----------- | ------ | ------ | ------------- | --------- | ------ | ----- | ------- | --------- | ---- | ------------- | ------- | --- | ----- | -------------- |
|             |        |        |               |           |        |       |         | we assume | that | the different | systems |     | could | be implemented |
| measuring   | the    | RTT of | each of those | requests. |        |       |         |           |      |               |         |     |       |                |
IntheSPEtheflowentriesfortherequestispre-installedin with similar latency w.r.t. code performance.
|             |           |     |               |              |     |        |      | We measure |     | latency | by issuing | ping | requests | to the mi- |
| ----------- | --------- | --- | ------------- | ------------ | --- | ------ | ---- | ---------- | --- | ------- | ---------- | ---- | -------- | ---------- |
| the switch, | resulting | in  | no controller | interaction. |     | In the | CPE, |            |     |         |            |      |          |            |
flow entry installation is disabled, resulting in all requests croservicehostforallexperiments.IntheanalysisoftheSPE,
having to travel through the controller. The purpose of these we establish that the controller had no impact on the latency.
experiments is to gauge the latency impact of the controller Additionally, the network layout of the SPE and would be
communication overhead. identical to a monolithic architecture if the monolith replaced
|              |     |              |              |     |     |               |     | the switch, | and | the two | clients in | the experiments |     | instead was |
| ------------ | --- | ------------ | ------------ | --- | --- | ------------- | --- | ----------- | --- | ------- | ---------- | --------------- | --- | ----------- |
| Microservice |     | Architecture | Experiments. |     | In  | the Microser- |     |             |     |         |            |                 |     |             |
vice Architecture Experiments (MAE), several hosts resides in one single client sending requests to itself through the switch.
anemulatednetwork.Somehostsinthenetwork,referredtoas However, one of the ping requests in the SPE experiment
microservice-hosts,start hostingtheserverprogram. Oncethe wouldthenrepresenttwopingrequeststothemonolith.Thus,
microservice-hostsareconfigured,aNetworkFloodingSwarm wecanestimatethepingpercentilesofthemonolithbysimply
|          |          |            |      |           |            |     |          | halvingtheresponsetimesfromtheSPE |     |     |     |     | results.Weconclude |     |
| -------- | -------- | ---------- | ---- | --------- | ---------- | --- | -------- | --------------------------------- | --- | --- | --- | --- | ------------------ | --- |
| (NFS) is | started, | consisting | of a | multitude | of clients |     | that all |                                   |     |     |     |     |                    |     |
start to flood the network with requests. Each request sent in the analyis of the SPE that the controller doesn’t matter in
towards the microservice IP is caught by the SDN switch thatexperiment.Therefore,wecanusethemeanofboththose
and forwarded to one of the microservice-hosts. The SDN experiments to get a more reliable result.
switch chooses the microservice-host using its flow-table or In order to quantify the MAE latencies in relation to the
theconnectedSDNcontroller.Thecontrollerdecidestherecip- monolith latencies we can calculate the ratio using the the
ient using its associated load balancer. Each of these requests following formula, where R is the relative latency, E is
increasesthetotalworkloadoftherecipientmicroservice-host, the estimated latency of the monolith and M is the latency
M
and the workload of each microservice-host is observed to measured in the microservice experiment: R=
E

Load Balancer Load Balancer Load Balancer
1 2 N
...
...
Controller 1 Controller 2 Controller K
Network Flooding Swarm
Microservice
Microservice A
ClieCntlCielnietCntlieCntlient Mi M cHr i o c o Hr ss o e o t s r se v t i r c v e ic e A A
Cli C e l n C ie t l n ie t ntClientCl C ie l n ie t nt SDN Mi M cHr i M o c o Hr s i M s o c e o H t r s i r s o c e o v H t r s i r s o c e o v t s e i r s c e v t e A i r c v e A ic e A A
Switch MiHcroosste rvice
Host
Main
Client
Fig. 1. Experiment Network Layout - The SDN switch forwards all packets from the client to the microservice, consulting the attached
controller which uses the current load balancer to decide recipients for requests with no flow entries yet installed.
B. Experimental Setup the remaining requests, the latency increases to around 8 mi-
crosecondsatthe99thpercentileandaround20microseconds
Simulation Environment. We use Mininet to emulate a
for the 99.9th percentile. For the slowest requests, the latency
network environment. In the setup, the Mininet network con-
tains an emulated Open vSwitch3 which is connected to an increases to 422 microseconds when the Beacon controller
was measured and 161 microseconds when measuring the
OpenFlow controller running outside of the Mininet network.
Ruy controller. When not installing flow entries, the latency
ChoiceofControllers.AsshowninTableI,OpenDaylight,
increasessignificantly,reachingashighas20millisecondsfor
Ryu, Beacon and NOX have been regarded as the controllers
theslowestrequests.Comparingthecontrollers,forthefastest
with lowest latency in at least one of the surveyed controller
90%ofallrequestswitheachcontroller,Beaconyieldsatleast
evaluation studies. Of these NOX and OpenDaylight were
5 times faster responses. For the remaining 10%, the latency
omitted due to configuration issues.
of the requests measured when using Beacon approaches the
Load Balancers. Due to their simplicity and wide-spread
latency measured when using Ruy with both measurements
use, we include the Round Robin and Random Assign al-
beingapproximately20millisecondsfortheirslowestrequest.
gorithms in our comparison. In order to examine the effects
of a server-aware load balancing algorithm, the Least Loaded
TABLEII
algorithm has also been implemented.
LATENCYPERCENTILESINSPEANDCPE(MILLISECONDS).
Gathering Data. The current load and timestamp of each
microservice-hostiscapturedonceevery100ms.Aftertheex- Controller Experiment Min P50.0 P90.0 P99.0 P99.9 P99.99 Max
Beacon SPE 0.003 0.004 0.004 0.008 0.026 0.078 0.422
periment has finished, these loads and timestamps are written Ryu SPE 0.003 0.004 0.004 0.007 0.021 0.058 0.161
Beacon CPE 0.162 0.268 0.381 0.957 3.870 9.620 20.000
to a file and analyzed. Similarly, the latency of each ping-
Ryu CPE 1.010 1.430 1.650 2.070 5.030 7.850 18.700
request made by the main client is recorded to a file.
When comparing the controllers in the SPE, the latency
V. RESULTS is almost identical. This was expected, since when the flow
This section presents the results of our experiments. First, entries are pre-installed, the controller will never be involved
the results of SPE and CPE are presented and explained, in the experiment, which effectively turns the tests identical
followed by the MAE-Static and MAE-Random, respectively. to each other.
Comparing the latencies from CPE shows that Ryu is
A. Latency Experiments around five times slower for the 50th percentile, with Ruy
The results for the SPE and the CPE, shown in Table II, never resulting in latencies lower than a millisecond and
consistofthelatencyoftheRTTbetweenthetwohostsinthe Beaconbeingabletoproducelatencieslessthan200microsec-
system. A higher value in the table indicates a higher latency onds. For the slowest requests, however, the results show that
for that controller. the controller has little effect on the resulting latency. This
Thetableshowsthatwheninstallingflowentries,thelatency is likely due to the communication between the switch and
of a request is constantly below a millisecond. Regardless controller being the slower factor rather than the performance
of controller, the lowest latency is 3 microseconds and for of the controller itself in some cases.
90% of all requests, the latency is below 5 microseconds. For Based on these results we can conclude that the latency
caused by the controller communication plays a major part
3OpenvSwitchhttps://www.openvswitch.org/ in the total latency of the slowest requests. When striving for

minimal latency, it would be beneficial to pre-install as many
100
flow entries as possible into the switch in order to minimise
the number of requests communicated to the controller.
80
B. Microservice Architecture Experiment
60
For the MAE-Static and MAE-Random, the results consist
40
of the the ping requests latencies in the Main Client as well
as the load imbalance chart of the system. The balance chart
20
depicts,foreachcontroller/loadbalancercombination,howthe
load imbalance percentage of the system changes throughout
0
the session. A higher value in the y-axis indicates a more 0 10 20 30 40 50 60
Time(s)
unfair balance of the workload between the server-nodes.
The ping table consists of the percentiles in the RTT
achieved for each controller and load balancer. Thus, a higher
value in the table indicates a higher latency for that con-
troller/load balancer combination.
StaticWorkload.TheupperchartinFigure2showsthatthe
loadimbalancepercentageisalmostidenticalwhencomparing
the controllers for each load balancing algorithm. The chart
shows that the imbalance is rather high and volatile in the
beginning, especially for the random load balancers, then
turning stable around halfway through the experiment. The
chart shows a rapid decline in load imbalance for both the
Server- and Round Robin load balancers, settling at less than
10%. For the Random load balancer, the imbalance declines
to about 70% shortly after its volatile start, only to increase
to 80% and then starting its slow decline towards 50% after
20 seconds.
Observing Table III, the latency increases in an almost
equal pace for all load balancer and controller combinations,
starting at 3 microseconds and slowly increasing to about
50 microseconds at 99.9th percentile. In the remaining 0.1
percent of the requests, the latency of all requests increases
drastically, having around 1 millisecond of latency for the
99.99th percentile almost 10 milliseconds for the 99.999th
percentileandatleast25millisecondsfortheslowestrequest.
FortheBeaconcontrollertheslowestrequeststookaround30
milliseconds, whereas for Ruy the slowest requests averaged
around 40 milliseconds.
Random Workload. Similarly to the static workload ex-
periment, Figure 2 also shows that the controller have no
noticeable effect on the load imbalance. In this experiment,
all three load balancers yield different results. Random load
balancing results in an initial decline to 70%, followed by an
incline to 80% and then a slow decline towards 50% load
imbalance. Using the Round Robin approach resulted in 60-
70% load imbalance initially, and then slowly declining to
30% after a slight increase to 70-80%. For the server aware
load balancer, the first 25 seconds show a steady decrease to
70% in load balance, followed by a steep decrease from 70%
to 20% in around 5 seconds. Thereafter, the load imbalance
stabilises at around 10%.
Table III shows that the latencies are quite similar for the
lowest99.9percentoftherequests.Thelast0.1percentgreatly
varies as well showing a major increase in latency.
)%(egatnecrePecnalabmIdaoL
Beacon-Random
Ryu-Random
Beacon-RoundRobin
Ryu-RoundRobin
Beacon-Server
Ryu-Server
100
80
60
40
20
0
0 10 20 30 40 50 60
Time(s)
)%(egatnecrePecnalabmIdaoL
Beacon-Random Ryu-Random
Beacon-RoundRobin
Ryu-RoundRobin
Beacon-Server
Ryu-Server
Fig. 2. Server Load Imbalance in the Microservice Archtecture
Experiments - These charts show how the load imbalance of the
server-node workloads changes throughout the experiments. The
upper chart depicts the results from MAE-Static, while the bottom
chart shows the results of the MAE-Random.
Analysing the Microservice Architecture Experiments.
The results of both MAE experiments show that, in terms
of load balancing, the chosen controller had no significant
impact. This is expected, since the controller does not alter
the logic of the load balancing implementation. The charts
also show that the the Random load balancer results in a 50%
load imbalance, regardless if the requests have a randomised
imposed load or all requests have the same load. This high
imbalance is probably due to the balancer being client-aware,
due to installing flow entries for each host, which, in turn,
causes the amount of requests being randomly chosen to
drastically decrease. This results in the randomness of the
systembeingtoolowfortherandomloadbalancertodistribute
requests evenly enough.
The results also show that the Round Robin is really
well suited for servers where each request results in similar
workload for the server, but is somewhat lacking when the
request workload is randomised. The adaptiveness of the
server-awareloadbalancermakesitabletohandlebothrequest
types without an issue, and for the experiments in this study,
the extra network load imposed by constantly communicating
the current workload to the switch, did not seem to affect the
network to any noticeable effect.
Thelatencymeasurementsmadeintheseexperimentsshow
that for the vast majority of all requests, the response time

TABLEIII
LATENCYPERCENTILESINALLTHEREQUESTEXPERIMENTS.THEEXPERIMENTCOLUMNINDICATESTHETYPEOFMAEBEINGMEASURED.
Experiment Controller Balancer min P50.0 P90.0 P99.0 P99.9 P99.99 P99.999 max
Static Beacon Random 0.003 0.004 0.006 0.016 0.045 0.940 9.504 39.420
Static Beacon RoundRobin 0.003 0.004 0.006 0.020 0.089 1.798 8.920 27.360
Static Beacon Server 0.003 0.004 0.006 0.018 0.054 1.304 7.906 25.940
Static Ryu Random 0.003 0.004 0.006 0.016 0.045 1.039 9.344 53.860
Static Ryu RoundRobin 0.003 0.004 0.006 0.015 0.042 0.903 8.206 47.620
Static Ryu Server 0.003 0.004 0.006 0.016 0.044 0.944 8.408 27.740
Random Beacon Random 0.003 0.004 0.006 0.020 0.065 1.392 10.800 39.280
Random Beacon RoundRobin 0.003 0.004 0.006 0.017 0.047 1.072 11.008 49.120
Random Beacon Server 0.003 0.004 0.006 0.017 0.054 1.442 9.956 28.020
Random Ryu Random 0.003 0.004 0.006 0.015 0.043 0.990 11.628 54.200
Random Ryu RoundRobin 0.003 0.004 0.006 0.018 0.050 1.058 10.482 51.700
Random Ryu Server 0.003 0.004 0.006 0.016 0.045 0.985 9.098 44.300
will be less than a millisecond in this architecture, even when the round robin load balancer is encouraged, due to its
the network is flooded with other requests. However, looking simplicity and slightly better performance.
at the requests past the 99.999th percentile, we see that the OurresultsshowthatusingSDNtoimplementthemicroser-
slowest requests measured are even slower than those made vice orchestration directly into the switch is feasible. It does
in the CPE experiment. This would indicate that when the increase the latency compared to a corresponding monolithic
network is flooding with requests, the communication with version,butifamicroserviceapproachisdesired,oursolution
the switch is also affected to some extent, with the response is a good option to consider.
| time being | more than | doubled | in some | scenarios | compared | to  |     |     |     |     |     |     |     |
| ---------- | --------- | ------- | ------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
REFERENCES
| the worst | case of | the CPE | results. |     |     |     |     |     |     |     |     |     |     |
| --------- | ------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
When comparing the latency of using each controller in the [1] P. Berde, M. Gerola, J. Hart, Y. Higuchi, M. Kobayashi, T. Koide, B. Lantz,
B.O’Connor,P.Radoslavov,W.Snow,etal.ONOS:towardsanopen,distributed
MAE experiments, the difference is not nearly as significant SDNOS.InProceedingsofthethirdworkshoponHottopicsinsoftwaredefined
as the differences shown in the CPE experiment. This could networking.ACM,2014. doi:10.1145/2620728.2620744.
|     |     |     |     |     |     |     | [2] L. DeRose, | B. Homer, | and D. | Johnson. | Detecting application | load | imbalance |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | ------ | -------- | --------------------- | ---- | --------- |
beexplainedbytherebeingsuchfewrequestsbeingmeasured on high end massively parallel systems. In European Conference on Parallel
where the request is handled by the controller, since the first Processing.Springer,2007. doi:10.1007/978-3-540-74466-5 17.
|     |     |     |     |     |     |     | [3] N.Dragoni,S.Giallorenzo,A.L.Lafuente,M.Mazzara,F.Montesi,R.Mustafin, |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
requestbetweenaclientandthemicroserviceresultsinaflow
|     |     |     |     |     |     |     | and L. Safina. | Microservices: |     | yesterday, | today, and tomorrow. | In  | Present and |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------------- | --- | ---------- | -------------------- | --- | ----------- |
entry installation. Ulterior Software Engineering. Springer, 2017. doi: 10.1007/978-3-319-67425-
4 12.
|     |     |     |     |     |     |     | [4] D.Erickson.Thebeaconopenflowcontroller.InProceedingsofthesecondACM |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
VI. CONCLUSION SIGCOMMworkshoponHottopicsinsoftwaredefinednetworking.ACM,2013.
doi:10.1145/2491185.2491189.
| In this | paper | we have | investigated | the | effects | of trans- |                           |     |                                                   |     |     |     |     |
| ------- | ----- | ------- | ------------ | --- | ------- | --------- | ------------------------- | --- | ------------------------------------------------- | --- | --- | --- | --- |
|         |       |         |              |     |         |           | [5] Y.GanandC.Delimitrou. |     | Thearchitecturalimplicationsofcloudmicroservices. |     |     |     |     |
forming a monolithic server architecture to a microservice IEEEComputerArchitectureLetters,17(2):155–158,2018.
architecture orchestrated by an SDN switch. To conduct ex- [6] Y. Jarraya, T. Madi, and M. Debbabi. A survey and a layered taxonomy of
|     |     |     |     |     |     |     | software-defined | networking. |     | IEEE communications | surveys | & tutorials, | 2014. |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ----------- | --- | ------------------- | ------- | ------------ | ----- |
periments a microservice architecture has been created using doi:10.1109/COMST.2014.2320094.
|     |     |     |     |     |     |     | [7] D.Kreutz,F.M.Ramos,P.Verissimo,C.E.Rothenberg,S.Azodolmolky,and |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
anSDNswitchasthemicroserviceorchestrator.Theeffectsof
|     |     |     |     |     |     |     | S.Uhlig. | Software-definednetworking:Acomprehensivesurvey. |     |     |     | Proceedingsof |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------------------------------------------ | --- | --- | --- | ------------- | --- |
employing said system have been evaluated both with regular theIEEE,2015. doi:10.1109/JPROC.2014.2371999.
|             |         |          |       |           |      |           | [8] L. Mamushiane, | A.         | Lysko, and | S. Dlamini.  | A comparative    | evaluation | of the |
| ----------- | ------- | -------- | ----- | --------- | ---- | --------- | ------------------ | ---------- | ---------- | ------------ | ---------------- | ---------- | ------ |
| and varying | request | workload | using | different | load | balancing |                    |            |            |              |                  |            |        |
|             |         |          |       |           |      |           | performance        | of popular | sdn        | controllers. | In 2018 Wireless | Days (WD). | IEEE,  |
algorithms. From this work, we draw three main conclusions. 2018. doi:10.1109/WD.2018.8361694.
|        |           |            |         |               |     |           | [9] M.Paliwal,D.Shrimankar,andO.Tembhurne. |     |                                  |     | ControllersinSDN:Areview |     |     |
| ------ | --------- | ---------- | ------- | ------------- | --- | --------- | ------------------------------------------ | --- | -------------------------------- | --- | ------------------------ | --- | --- |
| First, | the study | shows that | for the | vast majority | of  | requests, |                                            |     |                                  |     |                          |     |     |
|        |           |            |         |               |     |           | report. IEEEAccess,2018.                   |     | doi:10.1109/ACCESS.2018.2846236. |     |                          |     |     |
the latency for a SDN-supported microservice orchestrator [10] D.Shadija,M.Rezai,andR.Hill.Microservices:granularityvs.performance.In
CompanionProceedingsofthe10thInternationalConferenceonUtilityandCloud
is about three times slower than an optimistic estimate of Computing,2017. doi:10.1145/3147234.3148093.
a monolithic solution, which led to approximately 40 extra [11] A.Shalimov,D.Zuikov,D.Zimarina,V.Pashkov,andR.Smeliansky. Advanced
microsecondsinresponsetime.However,forasmallportionof studyofSDN/OpenFlowcontrollers.In9thCentral&EasternEuropeanSoftware
|     |     |     |     |     |     |     | EngineeringConferenceinRussia.ACM,2013. |     |     |     | doi:10.1145/2556610.2556621. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | ---------------------------- | --- | --- |
requests, the latency increases significantly, resulting in more [12] A. L. Stancu, S. Halunga, A. Vulpe, G. Suciu, O. Fratu, and E. C. Popovici.
|     |     |     |     |     |     |     | Acomparisonbetweenseveralsoftwaredefinednetworkingcontrollers. |     |     |     |     |     | In12th |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | ------ |
than20xslowerrequestsinsomecasesandhundredsoftimes
InternationalConferenceonTelecommunicationinModernSatellite,Cableand
slower for the slowest requests. BroadcastingServices.IEEE,2015. doi:10.1109/TELSKS.2015.7357774.
|         |           |        |          |     |        |            | [13] A. Tootoonchian,                            |     | S. Gorbunov, | Y. Ganjali, | M. Casado,          | and R. Sherwood. | On  |
| ------- | --------- | ------ | -------- | --- | ------ | ---------- | ------------------------------------------------ | --- | ------------ | ----------- | ------------------- | ---------------- | --- |
| Second, | comparing | Beacon | and Ryu, | the | Beacon | controller |                                                  |     |              |             |                     |                  |     |
|         |           |        |          |     |        |            | controllerperformanceinsoftware-definednetworks. |     |              |             | In2ndUSENIXWorkshop |                  |     |
resulted in the lowest latency when considering the fastest onHotTopicsinManagementofInternet,Cloud,andEnterpriseNetworksand
Services(Hot-ICE12),2012.
| 99.9% of | all requests. |     |     |     |     |     |                                                                            |     |     |     |     |     |     |
| -------- | ------------- | --- | --- | --- | --- | --- | -------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|          |               |     |     |     |     |     | [14] T.Ueda,T.Nakaike,andM.Ohara.Workloadcharacterizationformicroservices. |     |     |     |     |     |     |
Third, comparing different load balancing algorithms, since In 2016 IEEE international symposium on workload characterization (IISWC).
|     |     |     |     |     |     |     | IEEE,2016. | doi:10.1109/IISWC.2016.7581269. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------------------- | --- | --- | --- | --- | --- |
the OpenFlow architecture enforces a client-aware load- [15] L. Zhu, M. M. Karim, K. Sharif, C. Xu, F. Li, X. Du, and M. Guizani. Sdn
balancing model, we conclude that for requests of varying controllers: A comprehensive analysis and performance evaluation study. ACM
imposedworkload,aserver-awareload-balancingalgorithmis Comput.Surv.,53(6),2020. doi:10.1145/3421764.
needed.However,whenallrequestsresultinsimilarworkload,