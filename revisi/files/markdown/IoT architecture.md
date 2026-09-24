# IoT architecture

> Source file: `IoT architecture.pdf`

---

2017 IEEE 5th International Conference on Future Internet of Things and Cloud
| SAVI-IoT: |     |     |     | A   | Self-Managing |     |     |     | Containerized |     |     | IoT |     |
| --------- | --- | --- | --- | --- | ------------- | --- | --- | --- | ------------- | --- | --- | --- | --- |
Platform
|     |     |     | Hamzeh  |                  | Khazaei,   | Hadi             | Bannazadeh  | and                             | Alberto     | Leon-Garcia |     |     |     |
| --- | --- | --- | ------- | ---------------- | ---------- | ---------------- | ----------- | ------------------------------- | ----------- | ----------- | --- | --- | --- |
|     |     |     |         | Department       |            | of Electrical    |             | and Computer                    | Engineering |             |     |     |     |
|     |     |     |         |                  | University |                  | of Toronto, | Ontario,                        | Canada      |             |     |     |     |
|     |     |     | Emails: | {hamzeh.khazaei, |            | hadi.bannazadeh, |             | alberto.leongarcia}@utoronto.ca |             |             |     |     |     |
Abstract—Internet
|                 |                   | of         | Things             | (IoT)         | as a               | service         | is the  |     |     |     |     |     |     |
| --------------- | ----------------- | ---------- | ------------------ | ------------- | ------------------ | --------------- | ------- | --- | --- | --- | --- | --- | --- |
| ultimate        | goal of           | employing  | cloud              | computing     |                    | paradigm        | for     |     |     |     |     |     |     |
| initiating      | IoT application   |            | scenarios.         |               | Due to             | the nature      | of      |     |     |     |     |     |     |
| IoT ecosystems, |                   | an IoT     | application        | should        |                    | be distributed, |         |     |     |     |     |     |     |
| programmable    | and               | autonomic; |                    | also,         | it requires        | to              | support |     |     |     |     |     |     |
| heterogeneity,  | security          | and        | privacy            | by            | following          | design          | pat-    |     |     |     |     |     |     |
| terns involved  | in                | creating   | IoT                | systems.      | A multi-layer      |                 | cloud   |     |     |     |     |     |     |
| architecture    | comprising        |            | of a high-capacity |               | core               | center          | that    |     |     |     |     |     |     |
| is connected,   | through           |            | high speed         | links,        | to                 | geographically  |         |     |     |     |     |     |     |
| distributed     | smart             | edges      | seem               | appropriate   |                    | for highly      | dis-    |     |     |     |     |     |     |
| tributed        | and heterogeneous |            | IoT                | applications. |                    | Building        | upon    |     |     |     |     |     |     |
| our previous    | initiatives       | and        | inspired           | by            | the Infrastructure |                 | as      |     |     |     |     |     |     |
Code(IoC)paradigm,inthispaper,weproposeandevaluate
| a hierarchical, | programmable |     | and | autonomic |     | IoT platform |     |     |     |     |     |     |     |
| --------------- | ------------ | --- | --- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
basedonthemicroservicemodels.Ourplatformsupportsbig
| data, local/edge |         | data processing, |             | high    | level         | of programma- |         |      |      |                      |         |               |     |
| ---------------- | ------- | ---------------- | ----------- | ------- | ------------- | ------------- | ------- | ---- | ---- | -------------------- | ------- | ------------- | --- |
| bility and       | runtime | autonomic        | management. |         |               | The autonomic |         |      |      |                      |         |               |     |
| management       | system  | ensures          | the         | service | availability, |               | quality |      |      |                      |         |               |     |
|                  |         |                  |             |         |               |               |         | Fig. | 1: A | layered architecture | for IoT | applications. |     |
ofserviceandoptimizedresourceutilizationinthewholeIoT
| application | components |        | autonomously. |          | The    | primary     | results |     |     |     |     |     |     |
| ----------- | ---------- | ------ | ------------- | -------- | ------ | ----------- | ------- | --- | --- | --- | --- | --- | --- |
| affirm a    | promising  | future | of our        | platform | toward | realization |         |     |     |     |     |     |     |
of IoT as a service. HVV. It worth noting that, technically, containerization is
notanotherformofvirtualizationwithrespecttoHVV[3].
I. INTRODUCTION
|     |     |     |     |     |     |     |     | In essence, | containers | are group | of isolated | processes | that |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --------- | ----------- | --------- | ---- |
Current Internet of Things (IoT) application and plat- have been configured to have limited access to resources
form design approaches model IoT solutions as layered thanks to namespace and control groups features in Linux
architectures [1] with a bottom layer consisting of de- kernel. However, containerization gives the sense of a
ployed IoT devices, a middleware layer to expose the fullyisolatedenvironmenttoinsideapplicationsorservices
underlying hardware in a unified manner, and a top-level as VMs do. For this reason we use ‘isolation’ term for
including IoT gateways, cloud edges and the core cloud containers instead. Therefore, it is more appropriate to
at top; applications may be deployed at the top three referHVVasstrongisolationandcontainerizationasweak
layers to execute business logic and visualize processed isolation. Linux container isolation (LCI) can bring the
sensordata[2].Suchamethodofapplicationdeploymentis same revolutions to IoT that HVV brought to cloud for re-
feasibleonlybycombinationofamulti-layercloudservices sourcemanagement.LCIallowstoinstantiate,relocate,and
withwell-definedIoTmiddlewarethatconnectsIoTdevices optimize IoT capabilities in order to manage all resources
seamlessly to IoT gateways (aka aggregators). Figure 1 in a more flexible and fine-grained fashion.
shows a high-level architecture of such an architecture. In this paper, we propose and evaluate a self-managing
In order to be able to deliver such multi-layer applica- programmableIoTplatform(hereafterreferredtoas‘SAVI-
tions,resourcevirtualizationdeemednecessaryatalllayers. IoT’)byleveragingbothHVVandcontainerisolationtech-
Hypervisorbasedvirtualization(HVV)isquitematureand niques to manage IoT applications end-to-end. SAVI-IoT
is heavily in use in cloud. However, HVV is not flexible, leverages SAVI Cloud [4] as the underlaying infrastructure
portable, programmable and lightweight enough for edge asaservice.SAVIisatwo-layeracademiccloud,including
and aggregator layers, in particular [1]. As a result, a a core in Toronto and seven smart edges across Canada
lightweight alternative to the hypervisors is required in the whichmakesitaperfecttestbedforourIoTplatform.While
IoT context; the container-based virtualization, also known SAVI-IoT platform is influenced by layered architecture
as Operating System (OS) Level virtualization seems ap- of SAVI cloud, it could be deployed on any public or
propriate for addressing above-mentioned shortcomings of privatecloud.TheSAVI-IoTisequippedwithanautonomic
| 978-1-5386-2074-8/17 $31.00 © 2017 IEEE |     |     |     |     |     |     |     | 227 |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DOI 10.1109/FiCloud.2017.27

Fig. 3: High level architecture of a microservice platform;
Fig. 2: Leveraging both strong and weak isolation tech- adopted from [6].
niques to offer microservices; adopted from [6].
Microserviceplatforms(MSP)suchasNirmata1,Docker
Cloud2 and Giant Swarm3 facilitate the management of
management system which manages all resources at run-
such service paradigm. MSPs are automating deployment,
timeautonomouslytomaintainperformance,reliabilityand
scaling, and operations of application containers across
economics all together for IoT applications. The ultimate
clusters of physical machines in cloud. MSPs enable
goalofSAVI-IoTistoprovideIoTasaserviceforvarious
software-as-service providers to quickly and efficiently re-
use cases and scenarios.
spond to customer demand by scaling the applications on
This paper is organized as follows; in section II, mi-
demand,seamlesslyrollingoutnewfeaturesandoptimizing
croserviceplatformswillbediscussed.SectionIIIdescribes
hardwareusagebyusingonlytheresourcesthatareneeded
the SAVI-IoT platform as a special case of microservice
(aka, continues integration and continues delivery in soft-
platform for IoT scenarios. Then we elaborate on the
ware engineering context). Fig. 2 shows the layered archi-
autonomic management system that is been designed for
tecture in which both isolation techniques, are leveraged
the platform in section IV. In section V, we describe the
to deliver microservices on the cloud. Fig. 3 depicts the
experimentalsetupforevaluationofSAVI-IoTplatform,the
high-level architecture of MSPs and the way they leverage
autonomic management system, in particular. We survey
the backend public or private cloud (ie, infrastructure-as-
related work in section VI and section VII concludes the
a-service clouds). Various microservice platform providers
paper and highlights our future directions of research on
such as Nirmata, Docker Tutum and Giant Swarm im-
IoT applications.
plemented their platform based on this conceptual model.
However such general purpose platforms do not address
II. CLOUDMICROSERVICES thespecificrequirementsandchallengesofIoTapplications
and scenarios, to which we will return in sections III.
Hypervisor-basedvirtualizationprovidesthehighestiso-
lated virtual environment. However, the cost of virtual- III. PLATFORMDESCRIPTION
ization overhead is high as each VM has to run its own
IoT applications, regardless of their use cases, share
kernelastheGuestOS.Moreover,VMresourcesaremainly
common functional and non-functional features; they are
underutilizedaseachVMusuallyhostsoneapplication[5].
highlydistributed,interfacingnumerousandheterogeneous
VM virtualization limitations led to the development of
IoT things and require multiple services for managing the
Linux containers wherein only those resources will be
big data that they are consuming. As Figure 1 shows, IoT
used which are required by applications while avoiding
applications require to have a bidirectional connection to
the overhead of redundant virtualized operating systems
IoT devices for collecting data and executing commands
in HVV. As a result, recently, a pattern has been adopted
from/to sensors. At the aggregator layer (see Figure 1),
by many software-as-a-service providers in which both
IoT applications may need realtime processing for extract,
VMs and containers are leveraged to provide so called
transform or load (ETL) the data along with security and
microservices. Microservices is an approach that allows
privacy measures for the underlaying sensors. The Edge
more complex applications to be configured from basic
layer represents the closest cloud data center to the IoT
buildingblocks,whereeachbuildingblockisdeployedina
plant. An IoT application may manage multiple geograph-
containerandtheconstituentcontainersarelinkedtogether
ically distributed but related regions. At this layer, IoT
to form the cohesive application. The application’s func-
tionality can then be scaled by deploying more containers
1http://www.nirmata.com
of the appropriate building blocks rather than entire new 2https://cloud.docker.com
iterations of the full application. 3https://giantswarm.io
228

this part of the application is deployed on cloud, we lever-
age cloud macroservices (i.e., Infrastructure as a Services
including VMs, networking and storage services). In our
sample application, we deployed Apache Spark5 worker
nodes for stream processing at edge cloud. Autonomic
Manager and IoT Control Services have the same role as
their corresponding in the aggregators.
At Core-Cloud, we have the same orchestration of com-
ponents as Edge-Cloud. However, here Core IoT microser-
vicearedifferent.Inoursampleapplication,wedeploythe
master nodes of our cluster-based services due to higher
reliability of Core-Cloud and the application logic. For
example, we deploy the master node of our Spark cluster
in the Core and Spark worker nodes at Edges. We also
deploy Spark worker nodes at Core-Cloud as well. In our
sample scenario, we wanted to have a global and realtime
view of all sensors at top layer. We also deployed Apache
Fig. 4: SAVI-IoT: architectural view. Cassandra6datastoreasourcentraldatastorageintheCore-
Cloud. The visualization service is also deployed in the
Core-Cloud.
data for each region will be processed or stored in the As can be seen, our IoT application comprises of multi-
closestedgecloud.Thetoplayer,representsthecloudcore ple big data services distributed at three layers to fulfill
data center which theoretically have unlimited resources our requirements. It goes without saying that orchestra-
available. That portion of the IoT applications that needs tion of services at different layers is based on the IoT
toprovideaglobalviewofthewholeIoTplantsforvarious application requirements including both functionals and
stakeholders reside in the core. Also, in case of leveraging non-functionals. For delay sensitive applications, realtime
clustered and distributed services in the IoT application, processing components should be deployed closed to the
such as big data platforms and storages, the master or sensors. Bandwidth limitation or data privacy issues also
manager nodes are better to be deployed at the core cloud. may impose local or edge processing in an IoT applica-
tion. If there is no such requirements, services may be
Aggregators (i.e., IoT gateways) are located outside of deployed on upper layers such as Edge-Cloud or Core-
the cloud and may be deployed on single board computers Cloud. As a result, in addition to functional requirements,
(e.g., Raspberry PIs), mini computers, or smart devices non-functionalpropertiessuchasperformance,securityand
(e.g., smart phones, TVS or refrigerators) to provide man- privacy, reliability, elasticity and scalability have a great
agement, connectivity, and data preprocessing for sensors’ role in service orchestration through layers.
data. The main responsibility of IoT middleware (refer to SAVI-IoT leverages Docker-Machine, Swarm and
Figure4)istofacilitatesuchfunctionalitiesataggregators. Docker-Services for managing macroservices and
A worker node of a cluster based data processing platform microservices. Using Docker-Machine, we provision
may be deployed on aggregators (i.e., Cluster worker). VMs on SAVI cloud (i.e. the backend cloud) at Core
An example for this can be a worker node of a Kafka4 and Edge clouds. Then using Docker-Swarm we create
cluster that is responsible for in-place data cleaning and a Swarm cluster of provisioned VMs. Each VM will be
aggregation. The Aggregator Autonomic Manager com- tagged by its role in the IoT application (e.g., manager,
ponent is a part of the autonomic management system iot-aggregator, iot-edge-worker or iot-core-worker) and its
which is responsible for monitoring performance metrics location (e.g., Core, Edge-1, Edge-2, etc). By leveraging
of aggregators and scale related microservices if needs these tags, we are able to provide location awareness for
be. IoT Control Services are the control services used by services; more specifically, services can be deployed at
the autonomic manager to scale or reconfigure microser- only required layers and locations. For example, following
vices. IoT Gateway Microservices are the part of the IoT command deploys a Spark worker on nodes that have
application that implements application functionalities at iot-edge-worker role and are located at British Colombia
this layer. For example, in our sample implementation of (BC) edge on SAVI cloud.
the IoT application, we deploy Kafka as microservices at $ docker service create --name worker
Aggregators. --network spark --constraint
AtEdge-Cloud,wehavesimilarorchestrationofcompo- node.labels.loc==BC --constraint
nents at aggregators, though, with one difference. Here as
5http://spark.apache.org
6http://cassandra.apache.org
4http://kafka.apache.org
229

node.labels.role==iot-edge-worker
savi-iot/spark:2.1.0-hadoop-2.7
bin/spark-class
org.apache.spark.deploy.worker.Worker
spark://master-ip:7077
| Figure               | 5 shows    | the         | sample        | IoT application         |             | that has   |     |     |     |     |     |     |     |     |
| -------------------- | ---------- | ----------- | ------------- | ----------------------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| been deployed        |            | by the      | SAVI-IoT      | platform                | on SAVI     | cloud.     |     |     |     |     |     |     |     |     |
| In this application, |            | we          | have          | software-defined        | sensors     | that       |     |     |     |     |     |     |     |     |
| collect and          | report     | cpu,        | memory        | and network             | utilization | of         |     |     |     |     |     |     |     |     |
| their hosting        | containers |             | periodically. | We                      | also        | deploy the |     |     |     |     |     |     |     |     |
| aggregators          | on         | Edge-Clouds |               | (i.e., software-defined |             | aggre-     |     |     |     |     |     |     |     |     |
gators)asinthispaper,westrivetoevaluatetheautonomic
managementsystem(AMS)underheavyloadforwhichwe
| don’t have | sufficient | number |     | of real and | physical | sensors. |     |     |     |     |     |     |     |     |
| ---------- | ---------- | ------ | --- | ----------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
IV. AUTONOMICMANAGEMENTSYSTEMFORIOT
APPLICATIONS
Theonlysolutiontoevergrowingcomplexityofsoftware
systemsistoenablethemtoself-managewhileconforming
totheendusersobjective.IoTsoftwareapplicationsareone
|     |     |     |     |     |     |     | Fig. | 5: Sample | IoT | application | for | the experiment. |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | --- | ----------- | --- | --------------- | --- | --- |
ofsuchhighlydistributedandcomplexsystemsthatshould
| leverage     | autonomic | management |       | at runtime        | since | manual    |     |     |     |     |     |     |     |     |
| ------------ | --------- | ---------- | ----- | ----------------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| intervention | at        | runtime    | is no | longer an option. | As    | a result, |     |     |     |     |     |     |     |     |
AMSscalesbothmicroservicesandmacroservicesinacas-
| we design    | and | implement        |     | an Autonomic   | Management |     |               |        |     |         |      |         |             |     |
| ------------ | --- | ---------------- | --- | -------------- | ---------- | --- | ------------- | ------ | --- | ------- | ---- | ------- | ----------- | --- |
|              |     |                  |     |                |            |     | cading manner | across | all | layers. | As a | result, | the managed |     |
| System (AMS) |     | for applications |     | that are being | deployed   | by  |               |        |     |         |      |         |             |     |
IoTapplicationisscaledaccordingtochangesinworkload
SAVI-IoT.AnIoTapplicationmaycompriseofmultiplebig
(i.e.,incomingsensordata)orchangesintheinternalstates
| data services | such | as a | distributed | NoSQL | datastores | (e.g., |            |         |            |                |     |     |     |     |
| ------------- | ---- | ---- | ----------- | ----- | ---------- | ------ | ---------- | ------- | ---------- | -------------- | --- | --- | --- | --- |
|               |      |      |             |       |            |        | (e.g, node | failure | or network | partitioning). |     |     |     |     |
CassandraorHBase),asophisticateanalyticplatform(e.g.,
|              |        |             |       |                   |        |            | We change         | the              | workload    | by          | adding    | software-defined |          |        |
| ------------ | ------ | ----------- | ----- | ----------------- | ------ | ---------- | ----------------- | ---------------- | ----------- | ----------- | --------- | ---------------- | -------- | ------ |
| Apache Spark |        | or Hadoop), | light | weight            | stream | processing |                   |                  |             |             |           |                  |          |        |
|              |        |             |       |                   |        |            | sensors to        | the application; |             | as          | a result, | the              | resource | uti-   |
| components   | (e.g., | Apache      | Kafka | or Flume),        | IoT    | middle-    |                   |                  |             |             |           |                  |          |        |
|              |        |             |       |                   |        |            | lization          | (i.e., cpu,      | memory      | and         | network   | load)            | of       | aggre- |
| ware (e.g.,  | Kaa7   | project)    | and   | other distributed |        | services   |                   |                  |             |             |           |                  |          |        |
|              |        |             |       |                   |        |            | gators increases. |                  | If resource | utilization |           | at aggregators   |          | rich   |
dependingontheusecaseatdifferentlayersandlocations.
|                 |     |         |        |             |     |            | a pre-defined  | threshold, |           | then | the aggregator |     | microservice |     |
| --------------- | --- | ------- | ------ | ----------- | --- | ---------- | -------------- | ---------- | --------- | ---- | -------------- | --- | ------------ | --- |
| The combination |     | of such | highly | distributed |     | systems at |                |            |           |      |                |     |              |     |
|                 |     |         |        |             |     |            | will be scaled | out        | by adding | more | containers.    |     | Aggregator   |     |
largescalemakestheruntimeenvironmentaverycomplex
|                   |             |                   |       |                       |             |           | containers      | run on         | their        | corresponding |        | VMs           | which       | have   |
| ----------------- | ----------- | ----------------- | ----- | --------------------- | ----------- | --------- | --------------- | -------------- | ------------ | ------------- | ------ | ------------- | ----------- | ------ |
| ecosystem         | in          | which maintaining |       | smooth                | and         | optimized |                 |                |              |               |        |               |             |        |
|                   |             |                   |       |                       |             |           | been set        | to accommodate |              | certain       | number | of            | containers. | If     |
| operation         | will        | be a challenging  |       | task. In              | this        | paper, we |                 |                |              |               |        |               |             |        |
|                   |             |                   |       |                       |             |           | more containers |                | are required |               | due to | high load,    | the         | AMS    |
| propose,designand |             | implement         |       | anAMSthatoptimizesthe |             |           |                 |                |              |               |        |               |             |        |
|                   |             |                   |       |                       |             |           | will add        | a new VM       | (i.e.,       | scaling       | the    | macroservice) |             | at the |
| application       | performance |                   | while | prevent under         | utilization | of        |                 |                |              |               |        |               |             |        |
samelocationandsetupitupfordeployingnewcontainers.
resourcesinthewholeapplicationstack.TheAMSisbased
|                                           |     |     |     |     |     |          | Scaling out     | at aggregator |      | layer      | may | trigger | scaling       | at up |
| ----------------------------------------- | --- | --- | --- | --- | --- | -------- | --------------- | ------------- | ---- | ---------- | --- | ------- | ------------- | ----- |
| on Monitor-Analyze-Plan-Execute-Knowledge |     |     |     |     |     | (MAPE-K) |                 |               |      |            |     |         |               |       |
|                                           |     |     |     |     |     |          | stream services | (i.e.,        | edge | services). |     | Again,  | Edge services |       |
loopintroducedbyIBM[7].LeveragingAMSisanattempt
|                  |     |        |     |          |     |            | first scale | out at | microservice |     | and | then at | macroservice |     |
| ---------------- | --- | ------ | --- | -------- | --- | ---------- | ----------- | ------ | ------------ | --- | --- | ------- | ------------ | --- |
| toward realizing |     | DevOps | or  | NoOps in | the | context of |             |        |              |     |     |         |              |     |
level,ifneedsbe.Inacascadingmanner,coremicor/macro
| software         | engineering. |             | The purpose | of            | DevOps | is to fill |                |          |           |             |            |     |               |       |
| ---------------- | ------------ | ----------- | ----------- | ------------- | ------ | ---------- | -------------- | -------- | --------- | ----------- | ---------- | --- | ------------- | ----- |
|                  |              |             |             |               |        |            | services       | may also | be scaled | out         | because    | of  | the expansion |       |
| the gap          | between      | development |             | and operation | tasks  | in soft-   |                |          |           |             |            |     |               |       |
|                  |              |             |             |               |        |            | in underlaying | services |           | (i.e., edge | services). |     | Provided      | that, |
| ware development |              | life        | cycle.      | NoOps extends | the    | concept    |                |          |           |             |            |     |               |       |
thewholeapplicationisscaledoutatalllayerstomaintain
| of DevOps | in     | which operation |           | tasks will | be     | completely |             |          |         |           |        |         |             |     |
| --------- | ------ | --------------- | --------- | ---------- | ------ | ---------- | ----------- | -------- | ------- | --------- | ------ | ------- | ----------- | --- |
|           |        |                 |           |            |        |            | QoS at high | load.    | If load | subsides, |        | the AMS | shrinks     | all |
| removed   | in the | software        | lifetime. | In other   | words, | if the     |             |          |         |           |        |         |             |     |
|           |        |                 |           |            |        |            | application | services | (i.e.,  | again     | bottom | up)     | to maintain |     |
AMScantakecareofallrequiredoperations(includingbut
|     |     |     |     |     |     |     | optimized | resource | utilization. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------------ | --- | --- | --- | --- | --- |
notlimitedtoconfiguration,QoS,reliability,faulttolerance
|                                                     |          |         |                |         |            |         | The AMS        | uses      | different | criteria | to   | scale out/in | services |     |
| --------------------------------------------------- | -------- | ------- | -------------- | ------- | ---------- | ------- | -------------- | --------- | --------- | -------- | ---- | ------------ | -------- | --- |
| and protection                                      |          | against | cyber-attacks) | at      | runtime,   | then we |                |           |           |          |      |              |          |     |
|                                                     |          |         |                |         |            |         | at each layer. | We        | adopt     | function | f as | the generic  | formula  |     |
| have achieved                                       | NoOps.   |         |                |         |            |         |                |           |           |          |      |              |          |     |
|                                                     |          |         |                |         |            |         | to scale the   | services. |           |          |      |              |          |     |
| The AMS                                             | proposed |         | in this        | work is | to deliver | auto-   |                |           |           |          |      |              |          |     |
| scalabilityfortheIoTapplicationwhichbringsaboutQoS, |          |         |                |         |            |         |                |           | +β·mem    |          | +    |              |          |     |
f =α·cpu
reliability and fault tolerance autonomously. The proposed util util
rept
|                             |     |     |     |     |     |     |     |     |     | γ·net |      | +λ· | fac  | (1) |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --- | ---- | --- |
| 7https://www.kaaproject.org |     |     |     |     |     |     |     |     |     |       | util |     | repc |     |
fac
230

inwhichα+β+γ+λ=1.Inadditiontocpu,memory,and Kafka service on that aggregator takes the responsibility
network utilization (percentages %), we also incorporate to forward the aggregated data from virtual sensors to the
replication factor (i.e., rep ) for services which is the upper services. Here we set the Kafka service to aggregate
fac
dependency factor among services. For example, defining sensor data for every 60 seconds and then send them up
| the target | replication | factor | (i.e., | rept ) of | Spark | service |              |           |          |                 |     |         |
| ---------- | ----------- | ------ | ------ | --------- | ----- | ------- | ------------ | --------- | -------- | --------------- | --- | ------- |
|            |             |        |        | fac       |       |         | to the Spark | streaming | service. | Spark Streaming |     | service |
(i.e. Edge service) to Kafka service (i.e., Aggregator ser- at the Edge-Cloud aggregates all the received data streams
vice) as 50% means that for each Spark container there from it’s aggregators and ingest them into the Cassandra
should be at least 2 Kafka containers up and running. The datastore located at the Core-Cloud. Edge Spark service
main idea of using the ratio of target replication factor alsostreamsallthedatafromit’sedgetotheSparkservice
repc
to current replication factor (i.e., ) is to maintain at the Core. Spark streaming service at the Core simply
fac
QoS in times of nodes’ failure or network partitioning. In shows the whole sensor data of the entire IoT application
other words, if due to an internal failure some of services in realtime. Figure 5 shows the experimental setup.
become down or unreachable, the AMS redeploys missing Note that as we discussed in section III, in most of IoT
services autonomically regardless of resource utilizations. projects, aggregators and sensors are physical entities that
The weights of parameters (i.e., α,β,γ,λ) can be tuned resides outside of the cloud. However, as we mentioned
| based on | a bottleneck |     | analysis | that is performed |     | during |            |             |             |                 |     |         |
| -------- | ------------ | --- | -------- | ----------------- | --- | ------ | ---------- | ----------- | ----------- | --------------- | --- | ------- |
|          |              |     |          |                   |     |        | before, in | this paper, | we leverage | software-define |     | sensors |
λ,
application test. By assigning more weight to we can and aggregators to evaluate the efficiency of the AMS at
| guarantee | a higher | level | of reliability | for our | application. |     | scale. |     |     |     |     |     |
| --------- | -------- | ----- | -------------- | ------- | ------------ | --- | ------ | --- | --- | --- | --- | --- |
Thesefourparametersgiveusahighdegreeofflexibility We examine a normal shape workload to evaluate both
to define proper criteria for auto scaling. Note that at out-scaling and in-scaling of the application. A client
f
each layer, we may have different functions as well as program requests for new sensors according to a Poisson
thresholds. Upper and lower thresholds are to trigger out- process. Each request is translated to a virtual-sensor-
scalingandin-scalingrespectively.Resourceutilizationfor
|     |     |     |     |     |     |     | container | which | embodies | 3 virtual sensors | for measuring |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | -------- | ----------------- | ------------- | --- |
eachserviceistheaveragevalueofallresourcesconsumed cpu, memory and network load. The new virtual-sensor-
by containers in that service. container will be attached to an aggregator automatically.
|     |     |     |     |     |     |     | By adding | more | and more | virtual sensors, | the | resource |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | -------- | ---------------- | --- | -------- |
V. EVALUATIONOFTHEAUTONOMICMANAGEMENT
|     |     |     |     |     |     |     | utilization | at aggregators |     | will increase. | If it reaches | the |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | --- | -------------- | ------------- | --- |
SYSTEM
|     |     |     |     |     |     |     | upper threshold, |     | here set | to 70%, according | to  | function |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | ----------------- | --- | -------- |
Inthissection,weelaborateonourexperimentalsetupas f , the AMS scales out the aggregator microservice.
agg
| well as | results. In | the experiment, |     | we use | the latest | stable |           |     |         |     |     |     |
| ------- | ----------- | --------------- | --- | ------ | ---------- | ------ | --------- | --- | ------- | --- | --- | --- |
|         |             |                 |     |        |            |        | f =0.5cpu |     | +0.1mem | +   |     |     |
versions of all software components, as of March 2017, in agg util util
| the IoT | platform | and the | sample | application. |     |     |     |     |     |             | rept |     |
| ------- | -------- | ------- | ------ | ------------ | --- | --- | --- | --- | --- | ----------- | ---- | --- |
|         |          |         |        |              |     |     |     |     |     | 0.1net +0.3 | fac  |     |
(2)
|                 |     |       |     |     |     |     |     |     |     | util | repc |     |
| --------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- |
| A. Experimental |     | Setup |     |     |     |     |     |     |     |      | fac  |     |
We deployed a sample IoT application using SAVI-IoT Eq.2revealsthattheaggregatorservice(i.e.,Kafka)iscpu
platform on SAVI Cloud. Our application leverages the intensiveastheweightofαisequaltoallotherscombined.
Core-Cloud at University of Toronto and three of SAVI We use f and f functions for the Edge and Core
|               |     |         |           |         |     |        |     | edge | core |     |     |     |
| ------------- | --- | ------- | --------- | ------- | --- | ------ | --- | ---- | ---- | --- | --- | --- |
| edges located | at  | British | Colombia, | Ontario | and | Quebec |     |      |      |     |     |     |
services.
| provinces | in Canada. | The      | AMS,    | first, creates |     | required |           |     |         |      |     |     |
| --------- | ---------- | -------- | ------- | -------------- | --- | -------- | --------- | --- | ------- | ---- | --- | --- |
|           |            |          |         |                |     |          | f =0.2cpu |     | +0.5mem | +    |     |     |
| VMs on    | the Core   | and Edge | clouds. | This process   |     | includes |           |     |         |      |     |     |
|           |            |          |         |                |     |          | edge      |     | util    | util |     |     |
provisioning of VMs and installing Docker packages (i.e., rept
|                                                |     |     |     |     |     |     |     |     |     | 0.1net +0.2 | f     | ac (3) |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------ |
| DockerengineandSwarm).Then,aSwarmclusterwillbe |     |     |     |     |     |     |     |     |     | util        | rep c |        |
fac
| created    | out of provisioned |             | VMs; | the Swarm | master  | will    |     |     |     |     |     |     |
| ---------- | ------------------ | ----------- | ---- | --------- | ------- | ------- | --- | --- | --- | --- | --- | --- |
| be located | at the             | Core-Cloud. |      | All VMs   | will be | labeled |     |     |     |     |     |     |
and tagged with their roles and locations. Next, the mi- f =0.2cpu +0.2mem +
|                                                    |     |     |     |     |     |     | core |     | util | util        |      |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | ----------- | ---- | --- |
| croserviceswillbedeployedontopofmacroservicesatall |     |     |     |     |     |     |      |     |      |             | rept |     |
|                                                    |     |     |     |     |     |     |      |     |      | 0.3net +0.3 | f    | ac  |
layers;relatedmicroserviceswillbelinkedtoconstitutethe util rep (4)
c
| application | logic | by the | AMS.          |         |         |      |               |     |        |                 | fac       |      |
| ----------- | ----- | ------ | ------------- | ------- | ------- | ---- | ------------- | --- | ------ | --------------- | --------- | ---- |
| As sensors, | we    | deploy | containerized | virtual | sensors | that |               |     |        |                 |           |      |
|             |       |        |               |         |         |      | Spark service | is  | memory | intensive while | Cassandra | ser- |
collect performance metrics including, CPU utilization, vice is almost intensive to all resources; these sensitivities
network load and memory consumption of their hosting have been reflected in Eqs 3 and 4. After some time, by
containers. We refer to these containers as virtual-sensor- adding more and more sensors, the application reaches it’s
container. In other words, each virtual-sensor-container upper limit capacity; an upper limit capacity for a cloud
embodies three probe sensors that report resource utiliza- application may be set for various reasons [8]. We let the
tions every 15 seconds. Every virtual-sensor-container will application to run at full capacity for some time and then
be attached to a co-located aggregator automatically. The we configure the client program to remove virtual sensors
231

with the same Poisson process to see if the AMS shrinks core.Eachrequestspecifiesthelocationofnewsensors.For
the whole application accordingly. any request, the application provisions a virtual-container-
Tables I and II show the settings for microservices and sensor,thatincludes3virtualprobesensors.ThentheAMS
macroservices. attaches the new virtual sensor to the Kafka service at the
same Edge. As can bee seen in the top plot of Figure 7,
TABLE I: Macroservices’ Settings (VM)
the AMS first scales the Kafka microservice by adding
more containers as the 70% threshold has been reached
Layer Services VM(OpenStack) Container
according to Eq 2. Consequently, after some time, around
Aggregator Kafka m1.small Type a iteration 13, the AMS scales the Spark service as well.
Spark Type b The scaling out process of microservices is going on until
Edge-Cloud m1.medium
Cassandra Type c around iteration 30 in which the AMS, this time, scales
Spark Type b the macroservice, i.e., adding one VM, for the aggregator
Core-Cloud Cassandra m1.large Type c service as the existing VM is filled with containers. We
Visualization Type d
canseethatthemacroservicesscalingisalsohappenedfor
the Spark service at iteration 50. This cascading scaling
continuesuntilapplicationreachesitscapacitylimitaround
TABLE II: Microservices’ Settings (Containers)
iteration 60. Afterwards, requests for new sensors will be
rejected by the application.
Type Network RAM CPUQuotaofVM
Around iteration 100, we set the client program to
Type a dedicateoverlay 512MB 25.0% remove the virtual sensors with the same process. As
Type b dedicateoverlay 1250MB 33.0% can be seen, the AMS shrinks both microservices and
Type c dedicateoverlay 3GB 50.0% macroservices to maintain optimized resource utilization.
Type d dedicateoverlay 1GB 25.5% Arounditeration 130,theAMSscales-in theapplicationto
theinitialstateasalltheaddedsensorshavebeenremoved
by the client program. The lower threshold for in-scaling
Figure 6 shows the resource utilization of the Swarm
has been set to 40%. The same story is going on in other
cluster that hosts the IoT application. This figure is part of
Edges as can be seen from bottom plot in Figure 7.
the output of the Visualization microservice.
Figure8showstheAMSoperationsontheCoreservices.
B. Results and Discussion Here,inadditiontoSparkandKafkaserviceswehavedata-
We set the upper capacity limit for our application as store service (i.e., Cassandra) deployed as microservices.
TableIII.TheapplicationhasbeendeployedatthreeEdges The top plot shows the auto-scaling at macroservices and
including the Alberta, Quebec and Ontario edges and the themiddleplotdepictsthereconfigurationofmicroservices
Core cloud that is located at the University of Toronto in with respect to workload. As Figure 8 (top plot) shows,
Canada. Due to space limitation, we only show the results the AMS scales Cassandra at microservice level up to 3
for the Alberta (top) and the Quebec (bottom) edges in instancesandthereisnoscalinghereatmacroservicelevel.
Figure 7. The solid lines represent the number of VMs Based on our experiments, it would be beneficial to scale
and dashed lines show the number of containers in the Cassandra datastore at microservice level for the sake of
application during the experiment that took around 150 performance;however,scalingforthesakeofincreasingthe
minutes; we refer to each minute of the experiment as an storage capacity is better to be done at macroservice level
iteration. For the first 10 minutes, application is working during low load and in a scheduled manner. Adding more
with initial sensors so no scaling has been initiated. It nodes or storage capacity to Cassandra datastore at high
can be seen that initial configuration for each edge is load,willhavenegativeeffectsonapplicationperformance
one virtual-container-sensor, one Kafka container, and one for a long time (even hours) due to data replication and
Spark container (see the first 10 minute in Figure 7). synchronization processes in the background.
ThebottomplotinFigure8showstheprovisioningtime
TABLE III: Upper Capacity limit for the Application for both macroservices and microservices. In macroservice
level, provisioning means a) creating the VM at backend
Service VM(#) ContainerperVM Container(#) cloud b) installation of Docker services c) labeling node
basedontheirrolesintheapplicationandd)joiningtothe
Kafka 12 4 48
application swarm cluster. As can be seen in the bottom
Spark 8 3 24 plot(i.e.,bluebars),provisioningmacroservicestakes50to
Cassandra 1 3 3 150 seconds depending on the VM specifications. In terms
Visualization 1 1 1 of microservice, the provisioning time is in order of mil-
liseconds. Provisioning at microservice includes, loading
At iteration 9, we turn the client program on to request the Docker image (images will be available locally after
newsensorsinaroundrobinfashionamongedgesandthe first instantiations) and configure it to be part of the target
232

|     | (a)CPUutilization. |     |     |     |     | (b)Memoryconsumption. |     |     |     |     | (c)Networkload. |     |     |
| --- | ------------------ | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --------------- | --- | --- |
Fig. 6: Initial resource utilization of the Swarm cluster that hosts the IoT application. This figure is the the result of
| visualization |     | microservice | in  | the application. |     |     |                 |                |              |                    |               |                |            |
| ------------- | --- | ------------ | --- | ---------------- | --- | --- | --------------- | -------------- | ------------ | ------------------ | ------------- | -------------- | ---------- |
|               |     |              |     |                  |     |     | think of        | different      | ways         | of how             | to design,    | develop,       | deploy     |
|               |     |              |     |                  |     |     | and manage      | such           | applications |                    | not only      | in the         | cloud, but |
|               |     |              |     |                  |     |     | also in         | the underlying |              | IoT infrastructure |               | [9]. To        | this end,  |
|               |     |              |     |                  |     |     | author in       | [10] explored  |              | the container      |               | virtualization | tech-      |
|               |     |              |     |                  |     |     | nology in       | IoT devices    | to           | analyze            | microservices |                | advantages |
|               |     |              |     |                  |     |     | and performance |                | in IoT       | applications.      |               | In particular, | they       |
discussbenefitsinadoptingvirtualizationtechniquesinIoT
|     |     |     |     |     |     |     | scenarios | both in | terms | of cloud | service | management | and |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ----- | -------- | ------- | ---------- | --- |
business opportunities.
Pizollietal.[11]designedanddevelopedCloud4IoTthat
|     |     |     |     |     |     |     | is platform    | offering      | automatic      |            | deployment,    | orchestration |          |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------- | -------------- | ---------- | -------------- | ------------- | -------- |
|     |     |     |     |     |     |     | and dynamic    | configuration |                | of IoT     | support        | software      | com-     |
|     |     |     |     |     |     |     | ponents        | through       | microservices. |            | This work      | is similar    | to our   |
|     |     |     |     |     |     |     | approach       | in this       | paper          | as we also | leverage       | microservices |          |
|     |     |     |     |     |     |     | with automatic |               | deployment     | and        | configuration. |               | However, |
|     |     |     |     |     |     |     | their platform | lacks         | the            | AMS        | which          | takes care    | of the   |
Fig.7:Auto-scalingatbothmicroandmacroservicesinthe
|            |        |             |          |             |                       |     | whole platform |            | at runtime | autonomically.  |           | To            | the best of |
| ---------- | ------ | ----------- | -------- | ----------- | --------------------- | --- | -------------- | ---------- | ---------- | --------------- | --------- | ------------- | ----------- |
| all Edges; | we     | didn’t show | the      | number      | of virtual-container- |     |                |            |            |                 |           |               |             |
|            |        |             |          |             |                       |     | our knowledge, |            | there is   | no published    |           | work in       | which an    |
| sensors    | in the | plots for   | the sake | of clarity. |                       |     |                |            |            |                 |           |               |             |
|            |        |             |          |             |                       |     | autonomic      | management |            | system          | had       | been designed | and         |
|            |        |             |          |             |                       |     | evaluated      | for IoT    | platforms  | or application. |           |               |             |
|            |        |             |          |             |                       |     | Barna          | et al. [8] | designed   | an              | evaluated | a model-based |             |
service.
It worth noting that provisioning time is different than AMS for management big data applications comprising of
|              |     |          |       |                 |     |             | both micro/macro |     | services. | Big | data services | are | part of a |
| ------------ | --- | -------- | ----- | --------------- | --- | ----------- | ---------------- | --- | --------- | --- | ------------- | --- | --------- |
| contribution |     | time. We | refer | to contribution |     | time as the |                  |     |           |     |               |     |           |
typicalIoTapplication.Ourworkinthispaperincorporated
| amount | of time | that        | is needed | for       | the new    | resources |              |     |          |           |     |                |     |
| ------ | ------- | ----------- | --------- | --------- | ---------- | --------- | ------------ | --- | -------- | --------- | --- | -------------- | --- |
|        |         |             |           |           |            |           | all required | IoT | services | including | big | data services. | We  |
| (i.e., | VMs or  | containers) | to        | virtually | contribute | into the  |              |     |          |           |     |                |     |
application. Contribution time is based on the application leveraged some of design patterns presented in [12] in
|       |                |                 |             |          |              |               | developing | our AMS | in          | this paper. |           |           |     |
| ----- | -------------- | --------------- | ----------- | -------- | ------------ | ------------- | ---------- | ------- | ----------- | ----------- | --------- | --------- | --- |
| logic | and the        | nature of       | the service |          | that is      | being scaled. |            |         |             |             |           |           |     |
| As a  | general        | rule, stateless | services    |          | (e.g., load  | balancers)    |            |         |             |             |           |           |     |
|       |                |                 |             |          |              |               |            |         | VII.        | CONCLUSIONS |           |           |     |
| have  | a contribution | time            | close       | to their | provisioning | time,         |            |         |             |             |           |           |     |
|       |                |                 |             |          |              |               | In this    | paper,  | we proposed | and         | evaluated | SAVI-IoT, | a   |
| while | statefull      | services        | have        | a much   | longer       | contribution  |            |         |             |             |           |           |     |
time compared to the provisioning time (i.e., distributed programmable self-managing IoT platform based on mi-
datastores). As a result, elasticity can be quantified based croservices. The platform is generic enough to be tailored
on provisioning time while scalability is more related to andcustomizedforvariousIoTusecases.Bigdatacompati-
bility,in-placedataprocessing,highlevelprogrammability,
| contribution | time. |     |             |     |     |     |             |                 |     |                      |     |     |           |
| ------------ | ----- | --- | ----------- | --- | --- | --- | ----------- | --------------- | --- | -------------------- | --- | --- | --------- |
|              |       |     |             |     |     |     | elasticity, | fault tolerance |     | and auto-scalability |     |     | are among |
|              |       | VI. | RELATEDWORK |     |     |     |             |                 |     |                      |     |     |           |
primefeaturesofthepresentedIoTplatform.Wedeployed
IoT applications may include lightweight embedded ser- a sample IoT application and examined the autonomic
vices and enterprise services. Therefore it is necessary to management system under high loads of sensor data. The
233

Fig. 8: Auto-scaling at both micro and macro services in the Core-Cloud; the bottom plot shows the provisioning time
| for VMs | and containers. |     |     |     |     |     |     |     |     |     |     |     |
| ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
primary results show a promising future for SAVI-IoT to [4] SAVI. (2015, June) Smart Applications on Virtual Infrastructure,
http://www.savinetwork.ca.Cloudplatform.
| be a cornerstone |     | in providing |     | IoT as a | service | paradigm. |                |              |              |     |           |             |
| ---------------- | --- | ------------ | --- | -------- | ------- | --------- | -------------- | ------------ | ------------ | --- | --------- | ----------- |
|                  |     |              |     |          |         |           | [5] W. Felter, | A. Ferreira, | R. Rajamony, | and | J. Rubio, | “An updated |
As the future work, we plan to facilitate the connection performancecomparisonofvirtualmachinesandlinuxcontainers,”
and management of physical sensors to IoT applications technology,vol.28,p.32,2014.
in a software defined manner. This way sensors can be [6] H.Khazaei,C.Barna,N.Beigi-Mohammadi,andM.Litoiu,“Effi-
ciencyanalysisofprovisioningmicroservices,”inIEEEInternational
added/removed to/from the application in a plug-and-play Conference on Cloud Computing Technology and Science (Cloud-
fashion.Anotherdirectionwouldbeimplementingamech- Com). IEEE,2016,pp.261–268.
|     |     |     |     |     |     |     | [7] “An architectural | blueprint | for | autonomic | computing,” | IBM, Tech. |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --------- | --- | --------- | ----------- | ---------- |
anismtoauthenticatesensorsandproviderequiredsecurity
Rep.,2005.
| measures | for IoT | devices | at  | aggregators’ | level. | To this |               |             |     |              |            |           |
| -------- | ------- | ------- | --- | ------------ | ------ | ------- | ------------- | ----------- | --- | ------------ | ---------- | --------- |
|          |         |         |     |              |        |         | [8] C. Barna, | H. Khazaei, | M.  | Fokaefs, and | M. Litoiu, | “A devops |
end, we plan to extend the autonomic management system architectureforcontinuousdeliveryofcontainerizedbigdataappli-
|              |         |          |            |              |         |            | cations,”                               | in International | Symposium  | on     | Software     | Engineering for |
| ------------ | ------- | -------- | ---------- | ------------ | ------- | ---------- | --------------------------------------- | ---------------- | ---------- | ------ | ------------ | --------------- |
| to leverage  | machine | learning |            | models,      | queuing | systems    |                                         |                  |            |        |              |                 |
|              |         |          |            |              |         |            | AdaptiveandSelf-ManagingSystems(SEAMS). |                  |            |        |              | IEEE,2017.      |
| and software | defined |          | networking | capabilities |         | to provide |                                         |                  |            |        |              |                 |
|              |         |          |            |              |         |            | [9] H. Bannazadeh,                      | A.               | Tizghadam, | and A. | Leon-Garcia, | “Smart city     |
self-protection for the SAVI-IoT platform which will be platformsonmultitiersoftware-definedinfrastructurecloudcomput-
ing,”inSmartCitiesConference(ISC2),2016IEEEInternational.
| inherited | by all | the resulted | applications. |     |     |     |     |     |     |     |     |     |
| --------- | ------ | ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IEEE,2016,pp.1–6.
[10] A.Celesti,D.Mulfari,M.Fazio,M.Villari,andA.Puliafito,“Ex-
ACKNOWLEDGMENTS
ploringcontainervirtualizationinIoTclouds,”inIEEEInternational
This research was supported the Natural Sciences and ConferenceonSmartComputing(SMARTCOMP). IEEE,2016,pp.
| Engineering | Council | of           | Canada | (NSERC),   | and   | the Ontario | 1–6.              |           |             |           |     |                  |
| ----------- | ------- | ------------ | ------ | ---------- | ----- | ----------- | ----------------- | --------- | ----------- | --------- | --- | ---------------- |
|             |         |              |        |            |       |             | [11] D. Pizzolli, | G. Cossu, | D. Santoro, | L. Capra, | C.  | Dupont, D. Char- |
| Research    | Fund    | for Research |        | Excellence | under | the Con-    |                   |           |             |           |     |                  |
alampos,F.DePellegrini,F.Antonelli,andS.Cretti,“Cloud4IoT:
nected Vehicles and Smart Transportation (CVST) project. a heterogeneous, distributed and autonomic cloud platform for
|     |     |     |     |     |     |     | the IoT,” | in IEEE International |     | Conference | on  | Cloud Computing |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------------------- | --- | ---------- | --- | --------------- |
REFERENCES TechnologyandScience(CloudCom). IEEE,2016,pp.476–479.
[12] S.Qanbari,S.Pezeshki,R.Raisi,S.Mahdizadeh,R.Rahimzadeh,
| [1] T. Renner, | M.  | Meldau, | and A. | Kliem, “Towards |     | container-based |     |     |     |     |     |     |
| -------------- | --- | ------- | ------ | --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
N.Behinaein,F.Mahmoudi,S.Ayoubzadeh,P.Fazlali,K.Roshani
resource management for the internet of things,” in International etal.,“IoTdesignpatterns:Computationalconstructstodesign,build
| ConferenceonSoftwareNetworking(ICSN).                    |             |                      |       |                     | IEEE,2016,pp.1–5. |              |                  |                       |     |            |                     |       |
| -------------------------------------------------------- | ----------- | -------------------- | ----- | ------------------- | ----------------- | ------------ | ---------------- | --------------------- | --- | ---------- | ------------------- | ----- |
|                                                          |             |                      |       |                     |                   |              | and engineer     | edge applications,”   |     | in IEEE    | First International | Con-  |
| [2] S. Li,                                               | L. Da Xu,   | and S.               | Zhao, | “The internet       | of things:        | a survey,”   |                  |                       |     |            |                     |       |
|                                                          |             |                      |       |                     |                   |              | ference          | on Internet-of-Things |     | Design and | Implementation.     | IEEE, |
| InformationSystemsFrontiers,vol.17,no.2,pp.243–259,2015. |             |                      |       |                     |                   |              | 2016,pp.277–282. |                       |     |            |                     |       |
| [3] M.                                                   | Vo¨gler, J. | Schleicher,          | C.    | Inzinger,           | S. Nastic,        | S. Sehic,    |                  |                       |     |            |                     |       |
| and                                                      | S. Dustdar, | “Leonore–large-scale |       | provisioning        |                   | of resource- |                  |                       |     |            |                     |       |
| constrained                                              | IoT         | deployments,”        |       | in IEEE             | Symposium         | on Service-  |                  |                       |     |            |                     |       |
| OrientedSystemEngineering(SOSE).                         |             |                      |       | IEEE,2015,pp.78–87. |                   |              |                  |                       |     |            |                     |       |
234