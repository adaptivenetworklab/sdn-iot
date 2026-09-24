# [40] Offloading Mechanisms Based on Reinforcement Learning and Deep Learning Algorithms in the Fog Computing Environment

> Source file: `[40] Offloading Mechanisms Based on Reinforcement Learning and Deep Learning Algorithms in the Fog Computing Environment.pdf`

---

Received1January2023,accepted25January2023,dateofpublication2February2023,dateofcurrentversion9February2023.
DigitalObjectIdentifier10.1109/ACCESS.2023.3241881
| Offloading          |     | Mechanisms |                  |          | Based       | on Reinforcement |     |     |     |     |     |
| ------------------- | --- | ---------- | ---------------- | -------- | ----------- | ---------------- | --- | --- | --- | --- | --- |
| Learning            |     | and        | Deep             | Learning |             | Algorithms       |     |     |     |     |     |
| in the              | Fog | Computing  |                  |          | Environment |                  |     |     |     |     |     |
|                     |     |            | 1                |          |             | 2                |     |     |     |     |     |
| DEZHEENH.ABDULAZEEZ |     |            | ANDSHAVANK.ASKAR |          |             |                  |     |     |     |     |     |
1DepartmentofComputerScience,UniversityofDuhok,Duhok42001,Iraq
2ErbilTechnicalEngineeringCollege,ErbilPolytechnicUniversity,Erbil44001,Iraq
Correspondingauthor:DezheenH.Abdulazeez(dezheen.abdulazeez@gmail.com)
ABSTRACT Fog computing has emerged as a computing paradigm for resource-restricted Internet of
things (IoT) devices to support time-sensitive and computationally intensive applications. Offloading can
be utilized to transfer resource-intensive tasks from resource-limited end devices to a resource-rich fog
or cloud layer to reduce end-to-end latency and enhance the performance of the system. However, this
advantageisstillchallengingtoachieveinsystemswithahighrequestratebecauseitleadstolongqueues
of tasks in fog nodes and reveals inefficiencies in terms of delays. In this regard, reinforcement learning
(RL)isawell-knownmethodforaddressingsuchdecision-makingissues.However,inlarge-scalewireless
networks,bothactionandstatespacesarecomplexandextremelyextensive.Consequently,reinforcement
learningtechniquesmaynotbeabletoidentifyanefficientstrategywithinanacceptabletimeframe.Hence,
deepreinforcementlearning(DRL)wasdevelopedtointegrateRLanddeeplearning(DL)toaddressthis
problem.ThispaperpresentsasystematicanalysisofusingRLorDRLalgorithmstoaddressoffloading-
related issues in fog computing. First, the taxonomy of fog computing offloading mechanisms based on
RL and DRL algorithms was divided into three major categories: value-based, policy-based, and hybrid-
basedalgorithms.Thesecategorieswerethencomparedbasedonimportantfeatures,includingoffloading
problemformulation,utilizedtechniques,performancemetrics,evaluationtools,casestudies,theirstrengths
anddrawbacks,offloadingdirections,offloadingmode,SDN-basedarchitecture,andoffloadingdecisions.
Finally,thefutureresearchdirectionsandopenissuesarediscussedthoroughly.
INDEX TERMS Fog computing, Internet of Things (IoT), offloading, reinforcement learning, deep
reinforcementlearning.
I. INTRODUCTION therefore, storing and processing data on these devices
The exponential growth in the number of IoT devices, is not an option. Cloud computing technology provides
estimated to reach approximately 75 billion by 2025, will unlimitedstorageandalargeprocessingcapacityviaalarge
resultinthegenerationofhugeamountsofdata(bigdata)[1]. numberofpowerfulvirtualservers,whichcanbeutilizedfor
|          |         |                     |     |              |     | applications | that are not time-sensitive |     | and do | not require | a   |
| -------- | ------- | ------------------- | --- | ------------ | --- | ------------ | --------------------------- | --- | ------ | ----------- | --- |
| Big data | must be | saved, transmitted, |     | and analyzed | to  | be           |                             |     |        |             |     |
converted into meaningful information that the user can higher level of responsiveness. Nevertheless, because of the
understand. However, most IoT end devices are known centralizedfashion,cloudcomputingtechnologiesareunable
tomeettheneedsofreal-timeprocessingapplications,owing
| for their | limited storage | and | computational |     | capabilities; |              |                  |     |              |           |     |
| --------- | --------------- | --- | ------------- | --- | ------------- | ------------ | ---------------- | --- | ------------ | --------- | --- |
|           |                 |     |               |     |               | to the large | end-to-end delay | and | high network | bandwidth |     |
The associate editor coordinating the review of this manuscript and utilization. Moreover, the centralized approach used by
|                                          |     |     |     |     |     | cloud computing | leads to | increasing | delays, | which cannot |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --------------- | -------- | ---------- | ------- | ------------ | --- |
| approvingitforpublicationwasMehdiSookhak |     |     |     | .   |     |                 |          |            |         |              |     |
VOLUME11,2023 ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 12555

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
be tolerated by most IoT applications, including virtual The majority of the currently available conventional
reality (VR) [2], augmented reality (AR) [3], autonomous approaches are considered effective resource management
vehicles [4], industrial IoT, and e-health. To satisfy the solutionsfordistributing,scheduling,andexecutingtasksin
intensive computational demands and stringent latency dedicated computing situations. These approaches are not
requirements of such applications, fog computing has been usefulandefficientinfogenvironmentsbecauseofthelarge
developed as a potential solution for transferring storage, number of resources and tasks that are mainly dynamic in
networking, and processing abilities to the edge of a nature,suchastheGoldmanalgorithm,Banker’salgorithm,
network [5]. The primary objective of fog computing is to Haas-Mohan algorithm, and Isloor-Marsland algorithm [8].
bring cloud-like services to the network edge to optimize In other words, they do not have a common framework
the performance of the system in terms of service latency, for studying resource management problems in the real-
network bandwidth, resource utilization, and workload world computing environment, which involves multiple
balancing[6]. parameters to obtain effective solutions, including mobility,
However,deployingfogcomputingposesadditionalissues heterogeneity,federation,QoSmanagement,interoperability,
concerning decisions regarding whether tasks should be andscalability[9].DifferentMethodsdesignedtohandlethis
performed locally or transferred to the fog or cloud. issue are classified as classical optimization, game theory,
Offloadingisessentiallythemovementofresource-intensive metaheuristics,andmachinelearning.
tasks to different platforms to accomplish tasks more Machine learning, including reinforcement learning (RL)
efficiently. Therefore, offloading must satisfy different and deep reinforcement learning (DRL) has been widely
constraints, including latency, load balancing, privacy, and investigated and studied in the literature to solve offloading
storage. Nevertheless, the distribution of the workload issuesandotherresourcemanagementconcernsindifferent
acrosscomplicatedheterogeneousfogdevices,withvarying uncertain computing contexts. These strategies help make
computationalresourcesandcapacities,isamajorchallenge better decisions regarding when, where, what, and how to
forsuchfogoffloadingsolutions.Thechallengeisincreased offload. For example, task offloading approaches based on
by the growing number of requests, which likely causes RLmethodshavebeenproposedforfogcomputingscenarios
the task queues of the powerful fog nodes to become to determine the optimal decision on where and when to
longer. Owing to the increased waiting time of a long offloadatask[10].Furthermore,anRL-basedloadbalancing
queue,therequirementsfortime-criticalapplicationsmaybe algorithm was proposed and deployed in the dynamic fog
exceeded[5]. contexttolowerthefailedallocationprobabilityandreduce
In addition, many single fogs are incapable of handling the average processing delay [11]. Owing to the large
resource-intensive tasks because of their limited processing and complex action and state spaces of wide-area wireless
capabilities, lack of available resources, or dynamic nature networks,traditionalreinforcementlearning(RL)algorithms
ofresourceneeds.Therefore,whenatask’sprocessingneeds maynotbecapableofdeterminingtheoptimalstrategywithin
exceedthecapabilitiesoffogplatforms,itwillbeoffloaded an acceptable amount of time. Furthermore, in large- space
to the remote cloud server via the vertical offloading situations,suchasvehicularnetworks,thestatespaceislarge,
mechanism. Another option is a horizontal offloading. This and the agent cannot analyze every action in each state to
is primarily achieved by sending computing tasks to the guaranteesuccess.Insuchsituations,theagentsarerequired
bestsurrogatefognodes[6].Makinganintelligentdecision to generalize the state space. Some states are rarely visited.
betweenhorizontalandverticaloffloadingisessentialsothat Reinforcement learning cannot handle continuous or high-
timeisnotwasted,andattemptingtomovealoadhorizontally dimensionalspaces.
whenverticaloffloadingismoreeffective.Forexample,ifa As an alternative solution, deep reinforcement learning
fognodebecomesoverloadedandunabletohandletheload (DRL) was created by combining reinforcement learning
byitself,itcanhorizontallyoffloadcomputationstoseveral (RL) and deep learning (DL) [12]. DRL algorithms can
less loaded fog modes in the same fog layer, rather than achieve exceptional performance in complicated control
verticallyoffloadingtoastrongerFNinahigherfoglayeror domains,provingthattheyarebetterformakingdecisionsin
to the cloud. This will assist in lowering the network traffic complex and uncertain situations. For example, the authors
andlatency. of [13] solved a task allocation problem based on DRL
Fourmajordecisionscommonlyneedtobemadethrough- methodsinadynamicvehicularenvironment.Anotherstudy
out the offloading process: what tasks should be offloaded solved the problem of computation offloading and resource
(what),wheretoexecutethem(locallyorremotely)(where), allocation by using a DRL algorithm to reduce system
which slot should a task be offloaded (when), and how delay[14].
the task should be offloaded or through which channel Tothebestoftheauthors’knowledge,nocomprehensive
(how)[7].Theoffloadingprocesscanbemademoreefficient survey or systematic review paper has been conducted on
by making high-quality, timely decisions based on what, researcharticlesthatusedRLandDRLtechniquestoaddress
where, when, and how. For high quality based on the offloadingconcernsinfogscenarios.Thegoalofthisstudyis
aforementioneddecisions,efficientresourceschedulingand toanalyzeexistingresearchthatusesRLandDRLmethods
allocationarerequiredtosatisfythequalityofservice(QoS) tosolveoffloadingproblemsinfogcomputinginasystematic
requirements. andcomprehensivemanner.
12556 VOLUME11,2023

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
In brief, the following are the major contributions of this methods. This study is also directly related to mobile edge
review: computing, and the concept of fog computing has not been
• Exploring different survey articles on RL or DRL- emphasized. In [19], a comprehensive overview of research
basedoffloadingmechanismsinfoganddiscussingthe areas related to offloading modeling in edge computing
strengthsanddrawbacksofeach. was presented by analyzing various types of offloading
• AsystematicandcomprehensivereviewofthelatestRL modeling based on different patterns, such as game theory,
andDRLapproachesinthefieldoffogoffloading. (non-)convex optimization, and machine learning. Markov
• AnewtaxonomyofcurrentRLandDRLalgorithmswas decision process, or Lyapunov optimization. However, the
developedforoffloadingmechanismsinfogcomputing. selection criteria for the included papers were not well
• Finally, open issues and future research directions are defined,andthestudywasnotasystematicreview.Besides,
discuss as well as weakly covered research challenges itdoesnotincludefuturedirections.
toenhanceoffloadingmechanismsinthecontextoffog Furthermore, the authors of [20] provided a survey
computing. on computational offloading in edge computing, including
The remainder of this paper is organized as follows. different offloading scenarios (IoT devices, between edge
SectionIIreviewstheessentialrelatedworkandmotivation. servers,andthecloud),influencingfactors(device,network,
Section III provides the necessary background on fog com- service, and user factors), and offloading strategies (partial
putingandoffloadingmechanisms,aswellasanoverviewof andfull).Duringtheoffloadingprocess,theyalsodiscussed
theRLandDRLprinciples.Thepaperselectionandresearch key issues, such as whether, what, and where to offload.
methodologyarepresentedinSectionIV.SectionVpresents However,theselectioncriteriafortheincludedpaperswere
asystematicandcomprehensivereviewoftheexistingstudies notwelldefined,andthestudywasnotasystematicreview.
that leverage RL and DRL algorithms in the context of fog Besides, it did not include future directions or open issues,
computing. An analytical discussion is presented in section whichweremeasuredasacorepartofthesurveys.
VI. Section VII discusses corresponding open issues and Another study provides a survey of recent studies on
research challenges for future studies. Finally, conclusions fog environmenst from the perspectives of argument reality
arepresentedinSectionVIII. applications[21],smartcityapplications[22],andhealthcare
applications [23]. However, these studies did not consider
II. RELATEDWORKANDMOTIVATION offloading in fog settings. In addition, a taxonomy of
Thissectionpresentsthecurrentsurveyandreviewpaperson optimization techniques and their applications in fog com-
offloadingissuesinfogcomputing.Themainadvantagesand puting environments was presented in [24]. They classified
drawbacksofeachstudywerethendiscussed. the related research articles into three categories: inte-
Acomprehensivesurveyofedgecomputingenvironments ger programming, heuristics, and metaheuristics. Examples
regarding offloading metrics was presented which included of applications of optimization techniques found in the
quality of service (QoS) and quality of experience (QoE), reviewedliteratureincludeallocation,scheduling,offloading,
energy consumption, resource scheduling approaches, per- placement, loadbalancing, selection, resourceprovisioning,
formance, gaming theory, and overhead, to make the most resourcemanagement,migration,clustering,andacombina-
suitable decision for computation offloading. This article tionoftheseoptimizationproblems.
includes a sufficient number of recently published high- The authors [25] presented a comprehensive study of
quality studies, and is reasonably organized. However, the offloadingmechanisms,focusingoncurrentresearchpapers
article suffers from the following weaknesses: the selection on offloading strategies in a fog environment, including
criteria for the included papers were not well defined, the its architecture, application, and technologies. The selected
study was not a systematic review, and open issues and studies were classified into four main categories: methods
futuredirectionswereincomplete[7].Anotherstudyprovides based on storage, methods based on computation, methods
a comprehensive systematic literature review (SLR) of based on energy, and hybrid methods. Then, it provides a
recent studies focused on resource management approaches comparisonbetweendifferentoffloadingmechanismmetrics,
in fog computing environments [15]. These studies have algorithm types, and evaluation based on the categorization
been categorized into six classes: resource scheduling, oftheselectedpapers.Moreover,theworkin[26]reviewed
resource allocation, task offloading, application placement, the literature on fog computing simulation tools and was
loadbalancing,andresourceprovisioningtechniques. intended to aid researchers in exploring and evaluating fog-
In addition, previous studies have provided a compre- relatedsolutions.
hensive review of offloading methods in mobile edge com- The work in [5] surveyed the existing literature on RL
puting from the perspectives of game-theoretic offloading applications for solving resource allocation problems in
methods [16], machine-learning offloading methods [17], fog computing environment. In future studies, open issues
andstochastic-basedoffloadingmethods[18].Asastrength, and challenges should be addressed. However, the selection
these review articles are well structured and follow the criteria for the included papers were not well defined, and
standardsandformatofasystematicstudy,andtheyinclude the study was not a systematic review. Besides, this study
up-to-date published papers on related studies. However, focuses on resource allocation rather than offloading issues
their surveys did not cover all the reinforcement learning in fog computing. In addition, [27] provided a detailed
VOLUME11,2023 12557

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
overviewofthecurrentapplicationsofRLandDRLtohandle A. FOGCOMPUTING
various problems in vehicular networks. These schemes Fog computing is an extremely virtualized platform that
are divided into two classes: vehicle management and delivers storage, computation, and networking resources
vehicleinfrastructuremanagement.However,thisstudyonly betweenIoTdevicesandconventionalcloudserver[30].Fog
consideredvehicularnetworksasacasestudyintheirreview computing is considered a supplement to cloud computing
paper.Besides,theselectioncriteriafortheincludedpapers andwasintroducedbyCisco[31]toaddresstheshortcomings
were not well defined, and the study was not a systematic ofcloudcomputingsuchasreducingdelays,andminimizing
review. networkusage[32],[33].OpenFogConsortiumdefinedfog
Furthermore, in [28], the most recent findings on ser- computing [34] as; ‘‘a system-level horizontal architecture
vice placement computation and offloading in fog were thatdistributesresourcesandservicesofcomputing,storage,
presented.Specifically,thisstudysuggestsanovelcategory controlandnetworkinganywherealongthecontinuumfrom
of optimization techniques for tackling service placement CloudtoThings’’.
issues in IoT applications running on fog nodes. The Fog computing is also defined by the authors of arti-
methods and optimization objectives play a significant cles[15]as;‘‘Fogcomputingisascenariowhereahugenum-
role in this categorization. However, reinforcement learning berofheterogeneous(wirelessandsometimesautonomous)
methodswerenotinvestigatedasasolutiontotheoffloading ubiquitous and decentralized devices communicate and
issues in fog computing in this study. In addition, the potentially cooperate among them and with the network to
authors of [29] reviewed resource management strategies performstorageandprocessingtaskswithouttheintervention
in fog computing environments considering heterogeneity, of third parties. These tasks can be used to support basic
resource limitations, and unknown future fog computing network functions or new services and applications that
traffic. In addition, they presented significant management operate in a sandboxed environment. Users leasing part of
issues including resource scheduling, resource allocation, their devices to host these services get incentives for doing
task offloading, and resource provisioning. Nevertheless, so’’.
the selection criteria for the included papers were not well Fog computing is composed of a large number of fog
defined, and the study was not a systematic review. Table 1 nodes and is categorized into two main types: resource-
summarizesprevioussurveys.Eachpaperlistsitspublication rich devices that include cloudlets and IOx cables whereas
year, environment, review type, paper selection method, routers, wireless access point (WAP) end devices, set-top-
taxonomy,openissues,andyearcovered. units,switches,andstationsareresource-hungrydevices.
The weaknesses of most previous surveys and review
papersareasfollows.
B. FOGCOMPUTINGARCHITECTURE
• Somerelatedreviewpapersdidnotfocusonoffloading According to previous studies [35], [36], and [37], the
issuesinfogcomputing.
hierarchical architecture of fog computing comprises the
• Some studies have not focused on RL and DRL followingthreemainlayers:
approachesinsolvingoffloadingrelatedissues.
Edgelayer:Thisisthelayerclosesttotheuserdeviceinthe
• Some papers did not present any reasonable physicalenvironment.ItcontainsdifferentIoTsmartdevices
classifications.
such as mobile phones, self-driving vehicles, humidity sen-
• Some studies did not address open issues and future sors, temperature sensors, and CCTV surveillance systems,
directions,whicharecrucialelementsinsurveys.
and so on. These IoT devices create large amounts of data
• Theprocessandselectioncriteriaforthepapersinvolved usingsensingphysicalobjectsorevents.Owingtothelimited
havenotbeenwelldefinedinsomestudies.
resourcesoftheseIoTdevices,thesenseddataaretransferred
• Some papers did not have an adequate number of totheuppertire(for/cloud)forstorageandprocessing.
articles.
Fog layer: This is the middle layer between the cloud
• Some studies did not include newly published articles andedgedevices.Thefoglayerconsistsofmanyfognodes
or state-of-the-art studies, especially those published
with limited computing or storage capabilities, including
between2021and2022.
routers, switchers, gateways, base stations, access points,
Theaforementionedlimitationsmotivatedustoconducta andcloudlets.Thesefogdevicesaredistributedbetweenthe
systematicandcomprehensivereviewofoffloadingstrategies end devices and the cloud, such as shopping centers, cafes,
basedontheRLandDRLmethodsinfogcomputing. parks, bus terminals, and streets. They can be mobile on
a moving carrier or static at a fixed location. End devices
III. BACKGROUNDINFORMATION are usually connected to fog nodes to obtain capabilities
This section presents a brief definition of a fog. First, for computing and storing the received sensed data. The
the layered architecture of fog is described. The offload- fog node stores the data of time-sensitive application for a
ing process is then explained from different perspectives, specific time before transferring it to the cloud. To process
includingoffloadingdecisions,offloadingmodes,offloading the data, the fog computing infrastructure is enabled as a
directions, and offloading metrics. Next, the fog computing supporting middle layer between edge nodes and the cloud
evaluation are further discussed. Finally, the fundamental to collect, process, and analyze the data at the edge. The
conceptsofRLandDRLarealsoexplained. cloud is responsible for storing data in its storage when it
12558 VOLUME11,2023

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
TABLE1. Summaryofrelatedsurveys.
is no longer required by the fog node [32]. The fog layer In this architecture, each end device or IoT object is
played a crucial role in solving long-latency and real-time linked to one of the fog nodes through various available
analysisproblems.Fognodesareconnectedtocloudservers communication technologies (e.g., 3G, 4G, wireless local
toachievepowerfulstorageandcomputingcapabilities.The area network (WLAN), ZigBee, WiFi, and Bluetooth) or
proxyserverenablescommunicationbetweenthefogandthe wiredconnections.Fognodescanbeconnectedtothecloud
cloud. or other fog nodes using wireless or wired communication
Cloud layer: This layer is located at the top layer. The technologies. In addition, all fog nodes were linked to the
cloudcomputinglayeriscomposedofseveralstoragedevices cloudviaanIPcorenetwork.
andhigh-powerservers,whichcanprovidepowerfulstorage
and computing abilities to support permanent extensive
computation analysis and the storage of a large amount of C. EDGECOMPUTING(EC)PARADIGMS
data. It also delivers various application services, including Edge computing paradigms can be divided into three types:
smart homes, factories, and transportation. This layer plays mobileedgecomputing(MEC),fogcomputing,andcloudlet
avitalroleinprocessinglargeamountsofdata,storingdata, computing. Many academic researchers use these concepts
andmanagingtheplatformservicesandmonitoringsystems. interchangeably,buttherearekeydifferencesbetweenthem.
Conversely,thereisalargedistancebetweenthislayerandthe Thissectionintroducestheconceptsofcloudletsandmobile
edgelayer,particularlyintheIoTlayer.Thefogcomputing edge computing. It then describes the main differences
architectureisshowninfigure1. betweentheseterms.
VOLUME11,2023 12559

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
inferenceschemetoreducetheinferencelatencyandsavethe
MECenergyconsumption.Accordingto[24],[35],and[44],
|     |     |     |     | the characteristics | of the | abovementioned |     | edge computing |     |
| --- | --- | --- | --- | ------------------- | ------ | -------------- | --- | -------------- | --- |
paradigmsaresummarizedintable2.
|     |     |     |     | Computation    | offloading        | in             | an edge computing | environ-          |         |
| --- | --- | --- | --- | -------------- | ----------------- | -------------- | ----------------- | ----------------- | ------- |
|     |     |     |     | ment is        | different from    | traditional    | computation       | offloading        |         |
|     |     |     |     | in a mobile    | cloud environment |                | (MCC).            | The MCC           | relied  |
|     |     |     |     | solely on      | mobile devices    | and            | the main          | cloud server      | for     |
|     |     |     |     | offloading     | tasks. Therefore, | the            | main cloud        | servers           | may     |
|     |     |     |     | be physically  | and logically     | distant        | from              | mobile devices,   |         |
|     |     |     |     | resulting      | in large response | latencies      | [46].             | Edge computing    |         |
|     |     |     |     | paradigms      | have been         | developed      | to address        | the               | latency |
|     |     |     |     | issue that     | occurs during     | the offloading |                   | process in        | MCC.    |
|     |     |     |     | Edge computing | is distinguished  |                | by the            | requirement       | for     |
|     |     |     |     | low latency    | and the provision |                | of a high         | workload capacity |         |
|     |     |     |     | while being    | close to          | user devices.  | In addition,      | based             | on      |
|     |     |     |     | the research   | article [44]      | and            | the features      | of new            | edge    |
FIGURE1. Architectureoffogcomputing.
computingparadigms,computationoffloadingdiffersamong
edgecomputingtechnologies.
1) CLOUDLETS Regarding proximity to the edge, in a fog computing
The term ‘‘cloudlet’’ was introduced for the first time environment, the fog node may not be the first hop access
in 2009 [39]. Cloudlets are small data centers that are pointfortheenddeviceduetotheutilizationoflegacydevices
normally one hop away from mobile devices and can be asfogcomputingnodes(FCNs).Forinstance,thefirstrouter
accessed via high-speed connectivity such as Wi-Fi, and linkedtotheenddevicemaynothavetheresourcestorunan
mobilebroadband.Thepotentialbenefitsofcloudletsinclude FCNframework.Therefore,thenearestFCNmaybeseveral
increasedbandwidth,decreasedlatency,offlineaccessibility, hopsaway.However,inthecaseofcloudletsandMEC,the
and lowercosts [40]. Acloudlet isa reliable, and,powerful devicescommunicatedirectlywiththenodeviaWi-Fi,andat
computer or a group of computers with a robust internet thebasestationofthemobilenetwork,respectively.Theyare
connection that is used in the proximity of mobile devices. onlyasinglehopawayfromtheenddevice.
Forexample,inaclassroomorcoffeeshop. In addition, fog devices are diverse and heterogeneous
The architecture of this scheme comprises three layers: in terms of storage, computation, and communication capa-
mobiledevices,cloudlets,andcloud.Thepurposeofadopting bilities, such as hubs and, switches. Cloudlet and MEC,
cloudlets is to enable mobile devices with limited storage on the other hand, do not support heterogeneity devices.
and computational resources to offload heavy computations Furthermore, the offloading process has changed in fog
to cloudlets, which is particularly useful for time-sensitive environments because of the hierarchical and distributed
applications[41].Limitedcoverageisoneofthelimitations structure of fog computing (IoT, fog, and cloud). On the
ofcloudlets[42].However,fogcomputingcanovercomethis other hand, MEC and cloudlets have localized structures.
limitation by providing resources to be located anywhere, Theproximity,diversityandheterogeneityofdevicesandthe
from end devices to the cloud, and allowing large network centralized and distributed architecture of edge computing
| sizes. |     |     |     | makethecomputationoffloadingprocessdifferentandmore |     |     |     |     |     |
| ------ | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- |
challenging.
2) MOBILEEDGECOMPUTING(MEC)
D. FOGCOMPUTINGCHALLENGES
| Mobile Edge | Computing (MEC) | intended to | provide cloud |     |     |     |     |     |     |
| ----------- | --------------- | ----------- | ------------- | --- | --- | --- | --- | --- | --- |
computing services at the base stations of cellular net- ThefogcomputingparadigmintendstoaddressseveralIoT
works [43]. The MEC server is a new device that must be andcloudcomputingapplicationchallenges.However,italso
hasitsownchallengesthatwillbediscussedinthissection.
deployedclosetothebasestationtowerstodelivercomputing
andstorageabilitiesattheedge.
MECwasproposedin2014bytheEuropeanTelecommu- 1) SECURITYANDPRIVACYISSUES
nication Standards Institute (ETSI) for the first time [44]. Because fog computing devices are typically deployed in
In 2017, ETSI officially renamed it MEC for multi-access places that are not under strict surveillance and protection,
theymaybeatriskoftraditionalattacksthatcouldcompro-
| edge computing. | This computing | paradigm | can be used to |     |     |     |     |     |     |
| --------------- | -------------- | -------- | -------------- | --- | --- | --- | --- | --- | --- |
provideawiderangeofservicesincludingaugmentedreality, misethesystemoffogdevicesinordertocarryoutmalicious
locationservices,videoanalytics,localcontentdistribution, taskssuchaseavesdroppinganddatahijacking.Furthermore,
|     |     |     |     | privacy | and security concerns |     | can be triggered | if end | users |
| --- | --- | --- | --- | ------- | --------------------- | --- | ---------------- | ------ | ----- |
andcachingservices.BycachingcontentontheMECserver,
itcanenableaccesstolocalcontentinrealtimeandwithlow offload computations to neighboring fog servers injected
latency.Forexample,theauthorsof[45]proposedreinforce- byattackers[47].Man-in-the-middle,authentication,access
mentlearning(RL)basedenergy-efficientMECcollaborative control, port scanning, and denial-of-service (DoS) threats
| 12560 |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
TABLE2. Thecharacteristicsofedgecomputingparadigms. greater than that of the cloud. This problem can be reduced
byaneffectiveoffloadingmechanismbysendingtheenergy-
intensivepartsfromfognodestootherpowerfulneighboring
|     |     |     |     |     |     |     | fog nodes | or clouds | servers. |     | For instance, |     | the authors | of  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | -------- | --- | ------------- | --- | ----------- | --- |
[49]proposedanenergy-efficientoffloadingdecisionmethod
|     |     |     |     |     |     |     | to simultaneously |     | reduce | energy | consumption |     | and | meet |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------ | ------ | ----------- | --- | --- | ---- |
responsetimeconstraints.Aschedule-delayawareoffloading
|     |     |     |     |     |     |     | technique | was | designed | in their | paper | to  | ensure | service |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | -------- | ----- | --- | ------ | ------- |
qualityinreal-timejobsandreducetheenergyconsumption
|     |     |     |     |     |     |     | of fog-cloud | devices, |     | thereby | maximizing | device | lifetime. |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------- | ---------- | ------ | --------- | --- |
Substantialresearchisrequiredtodevelopsuccessfulenergy
managementtechnologiesinfogenvironment[50].
4) QUALITYOFSERVICE(QoS)
|     |     |     |     |     |     |     | Fog systems      | consider      | various         |              | QoS metrics   | when       | designing     |      |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------- | --------------- | ------------ | ------------- | ---------- | ------------- | ---- |
|     |     |     |     |     |     |     | a successful     | system.       | According       |              | to            | [51], 11   | types of      | QoS  |
|     |     |     |     |     |     |     | metrics          | were          | defined         | (response    | time,         | deadline,  | through-      |      |
|     |     |     |     |     |     |     | put, resource    | utilization,  |                 | execution    |               | time cost, | energy        | con- |
|     |     |     |     |     |     |     | sumption,        | availability, |                 | reliability, | security,     | and        | scalability). |      |
|     |     |     |     |     |     |     | Depending        | on            | the application |              | requirements, |            | these metrics |      |
|     |     |     |     |     |     |     | were considered. |               | Trade-offs      | between      |               | different  | QoS metrics   |      |
|     |     |     |     |     |     |     | are often        | necessary     | when            | implementing |               | QoS        | provisioning, |      |
whichismademorechallengingowingtothedynamicnature
ofdifferentapplicationsandtheirrequirements.
E. OFFLOADING
|     |     |     |     |     |     |     | Offloading       | is       | an efficient | mechanism              |                           | that       | migrates | com- |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | -------- | ------------ | ---------------------- | ------------------------- | ---------- | -------- | ---- |
|     |     |     |     |     |     |     | putation         | or data  | from         | a resource-constrained |                           |            | device   | to   |
|     |     |     |     |     |     |     | another          | powerful | device       | or fog/cloud           |                           | to improve | the      | sys- |
|     |     |     |     |     |     |     | tem performance, |          | particularly |                        | for computation-intensive |            |          | or   |
latency-sensitiveapplications.Thismechanismoffersvarious
|     |     |     |     |     |     |     | benefits | such as | reduced | latency, | decreased |     | device | energy |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------- | -------- | --------- | --- | ------ | ------ |
consumption,andimprovedQoSparameters.Variousaspects
|     |     |     |     |     |     |     | must be   | considered  | when | making        |     | offloading | decisions,    |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ---- | ------------- | --- | ---------- | ------------- | --- |
|     |     |     |     |     |     |     | including | performance |      | maximization, |     | delay      | minimization, |     |
andenergyconsumptionminimization.
F. OFFLOADINGDECISIONS
Beforeoffloadingthecomputation,severaldecisionsmustbe
| have been | addressed | by a number | of  | proposed | solutions | for |     |     |     |     |     |     |     |     |
| --------- | --------- | ----------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
made[52],suchas
fogcomputingsecuritychallenges[48].
1) WHATTOOFFLOAD?
2) RESOURCEMANAGEMENT
|          |            |               |     |     |                  |     | How much | of  | the workload | should |     | be offloaded? | Or  | what |
| -------- | ---------- | ------------- | --- | --- | ---------------- | --- | -------- | --- | ------------ | ------ | --- | ------------- | --- | ---- |
| Resource | management | is considered |     | the | most challenging |     |          |     |              |        |     |               |     |      |
issue in fog landscapes because of resource heterogene- to offload? The task scheduler is responsible for deciding
whetherthetaskcanbeoffloaded,andifso,inwhatcapacity
| ity, resource | limitations, | unpredictability, |     |     | and the dynamic |     |     |     |     |     |     |     |     |     |
| ------------- | ------------ | ----------------- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(i.e.,partialorfulloffload).
| nature of      | the fog | environment | [15].    | These       | issues make | it  |     |     |     |     |     |     |     |     |
| -------------- | ------- | ----------- | -------- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| more difficult | to      | manage      | resource | allocation, | scheduling, |     |     |     |     |     |     |     |     |     |
2) WHENISOFFLOADING?
| placement, | provision, | offloading, |     | and sharing. | Therefore, |     |     |     |     |     |     |     |     |     |
| ---------- | ---------- | ----------- | --- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
effective management solutions are required to satisfy the Thetaskschedulerisresponsibleforselectingtheappropriate
requirementsoftheseapplications. time period for offloading the tasks. The offload interval is
chosenbythetaskschedulerunderdifferentconstraints.
3) ENERGYMANAGEMENT
Fog computing systems are composed of a large number of 3) WHEREISTOOFFLOAD?
geographicallydistributednodesandthesefognoseshasless This question is related to the location of execution (either
capability of storage and computing than cloud. Thus, the locally or remotely). If remote, the optimal fog node for
energy consumption in a fog environment is expected to be offloadingshouldbeselectedamongtheavailablenodes.
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     |     | 12561 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
| 4) HOWTOOFFLOAD? |     |     |     |     |     |     |     | G. OFFLOADINGMODE |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
Throughwhichchannelorthroughwhichpathtooffload. Typically, mobile apps can be split into a series of coarse-
|     |     |     |     |     |     |     |     | grained | or fine-grained |     | tasks, | each | of which | comprises |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | ------ | ---- | -------- | --------- | --- |
sequentialandparallelcomponents.Infine-grainedoffload-
5) WHATKINDOFOFFLOADINGSTRATEGYWILLBEUSED? ing, only a small proportion of the task is sent to a higher-
|            |     |           |             |             |            |       |       | powered     | computational |            | device, | whereas | in     | coarse-grained |     |
| ---------- | --- | --------- | ----------- | ----------- | ---------- | ----- | ----- | ----------- | ------------- | ---------- | ------- | ------- | ------ | -------------- | --- |
| What is    | the | main goal | of          | offloading, | maximizing |       | or    |             |               |            |         |         |        |                |     |
|            |     |           |             |             |            |       |       | offloading, | the           | entire job | is sent | [54].   | It may | not always     | be  |
| minimizing | a   | single    | performance |             | metric,    | joint | opti- |             |               |            |         |         |        |                |     |
mization, and the trade-off among multiple objective advantageous to offload all the computing components to a
remotecloud.Duringtheoffloadingprocess,thedevicemay
metrics?
wastemoreenergyandtimethanlocally.Inaddition,thecost
| Different | techniques |     | have been | suggested | to  | make | better |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --------- | --------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
decisionswithrespecttocomputationaltasksanddata(what) ofthetransfermaynotbeinsignificantifanunsuitablepart
ischosenforoffloading.
| to offload, | place | to execute |     | (either locally |     | or remotely) |     |     |     |     |     |     |     |     |     |
| ----------- | ----- | ---------- | --- | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Therefore,wemustintelligentlyselectwhichpartsofthe
| (where), | what | point in | time to | offload | (when), | and through |     |     |     |     |     |     |     |     |     |
| -------- | ---- | -------- | ------- | ------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
what channel (how) to offload. High-quality and timely application should be executed on a remote cloud server
|            |           |           |       |            |          |            |        | and which | parts    | should | remain     | on  | the mobile   | device   | to  |
| ---------- | --------- | --------- | ----- | ---------- | -------- | ---------- | ------ | --------- | -------- | ------ | ---------- | --- | ------------ | -------- | --- |
| offloading | decisions | are       | based | on what,   | weather, |            | where, |           |          |        |            |     |              |          |     |
|            |           |           |       |            |          |            |        | decrease  | response | time   | and energy |     | consumption. | However, |     |
| when, and  | how       | questions | help  | to enhance | the      | efficiency | of     |           |          |        |            |     |              |          |     |
theoffloadingprocess.Toachievehigh-qualitybasedonthe some applications are relatively basic or strongly integrated
|     |     |     |     |     |     |     |     | and cannot | be  | separated | into | multiple | tasks | for parallel |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | ---- | -------- | ----- | ------------ | --- |
abovementioneddecisions,effectiveresourcesmanagement
|           |     |          |            |     |              |     |        | processing | [20]. | They | must | be completely |     | offloaded | to a |
| --------- | --- | -------- | ---------- | --- | ------------ | --- | ------ | ---------- | ----- | ---- | ---- | ------------- | --- | --------- | ---- |
| solutions | are | required | to satisfy | the | requirements |     | of the |            |       |      |      |               |     |           |      |
applications. server or run on a local device. The fog contains two
computationaloffloadingmodes:full(orbinary)andpartial
| A crucial | aspect | of  | computation | offloading |     | is deciding |     |     |     |     |     |     |     |     |     |
| --------- | ------ | --- | ----------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
offloading.Inbinaryoffloading,thetasksoftheapplication
wheretooffloadthetask(e,g.,fog,cloud,oracombination
of these). Here, task scheduler is required to determine cannotbepartitionedandmustbeexecutedasawhole,either
|             |       |            |             |              |        |            |       | locally or  | offloaded   | to  | the server |        | [20], [55]. | With | partial |
| ----------- | ----- | ---------- | ----------- | ------------ | ------ | ---------- | ----- | ----------- | ----------- | --- | ---------- | ------ | ----------- | ---- | ------- |
| which tasks | will  | be handled |             | by the edge, | fog,   | and        | cloud |             |             |     |            |        |             |      |         |
|             |       |            |             |              |        |            |       | offloading, | application |     | tasks      | can be | subdivided  | into | several |
| layers in   | order | to meet    | the desired | design       | goals. | Generally, |       |             |             |     |            |        |             |      |         |
computationoffloadingmethodshandlecomputingresource components. These components are then executed locally
|     |     |     |     |     |     |     |     | or offloaded | to  | the servers |     | [55]. The | application |     | can be |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | --- | --------- | ----------- | --- | ------ |
restrictionssuchasthestoragespaceofIoTdevices,power,
partitionedstaticallyordynamicallyasfollows:
batterybackup,andsensors.Resourceallocationreferstothe
| algorithm | used  | to allocate | computing | tasks        | among | different |       |                       |     |     |     |     |     |     |     |
| --------- | ----- | ----------- | --------- | ------------ | ----- | --------- | ----- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
|           |       |             |           |              |       |           |       | 1) STATICPARTITIONING |     |     |     |     |     |     |     |
| fog nodes | under | different   | QoS       | requirements |       | and       | other |                       |     |     |     |     |     |     |     |
restrictions. Several strategies have been introduced, which Itisdecidedinadvancewhichapplicationcomponentsshould
canbecategorizedintoauction-basedandoptimization-based be executed locally and which should be offloaded [20].
Forinstance,softwareprogrammersapplystaticannotations
approaches.Theproposedauction-basedsolutionsarebased
onmarketpricingmechanismsthatconsiderthedemandand (e.g., @offloadable or @Remote) to methods that indicate
supply of fog nodes. Resource allocation approaches based that they should be offloaded. However, programs always
|     |     |     |     |     |     |     |     | have non-offloadable |     |     | components | that | must | be processed |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ---------- | ---- | ---- | ------------ | --- |
onoptimization,ontheotherhand,matchcloudserversand
fog nodes for IoT users [29]. For instance, [53] proposed a locally,suchasfacedetection,userinput,andpositioning.
resourceallocationmethodbasedonpricedtimedpetrinets
|     |     |     |     |     |     |     |     | 2) DYNAMICPARTITIONING |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
inafogcomputingsetting.
Task allocation and scheduling are considered the most A task’s resource needs may change based on its input data
challengingandimportantstepinthecomputationoffloading and user-defined objectives (e.g., battery consumption and,
responsetime).Inaddition,resourceavailabilitymaychange
| process | of the | fog computing |     | environment |     | because | of  |     |     |     |     |     |     |     |     |
| ------- | ------ | ------------- | --- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
resourcelimitations,unpredictability,resourceheterogeneity, in wireless network (e.g., network latency and, bandwidth)
and the dynamic nature of the fog environment [15]. andservicenodes(e.g.,memoryand,availableCPUpower).
|         |          |     |        |            |     |            |     | To adapt | to various | network | conditions, |     | latency | limitations, |     |
| ------- | -------- | --- | ------ | ---------- | --- | ---------- | --- | -------- | ---------- | ------- | ----------- | --- | ------- | ------------ | --- |
| Methods | designed | to  | handle | this issue | are | classified | as  |          |            |         |             |     |         |              |     |
classical optimization, game theory, metaheuristics, and andserverstates,appropriatepartitioningdecisionsmustbe
machine learning. Machine learning, including the RL and dynamicallydeterminedduringtheruntime[52].
| DRL algorithms, |     | is widely | considered |     | an efficient | alterna- |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ---------- | --- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tive to traditional optimization strategies. These methods H. OFFLOADINGMETRICS
make more intelligent decisions while offloading tasks In this section, the most important metrics used in the
to cloud or fog servers. In addition, resource allocation computational offloading domain are briefly explained.
concerns such as CPU cycles, channel access, and time Theseoffloadingmetricsareselectedinaccordancewiththe
allocation, can be addressed using these approaches. The requirementsoftheapplication.Trade-offsbetweendifferent
effectiveness of computation offloading is improved by metrics are often necessary when implementing successful
| identifying | suitable | nodes | and | appropriate | resource |     | allo- | applications. |     |     |     |     |     |     |     |
| ----------- | -------- | ----- | --- | ----------- | -------- | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- |
cation strategies that satisfy the QoS requirements of Energy consumption: The offloading mechanism is con-
applications. sumed the total energy. This mechanism sends the task
| 12562 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
from the end device to the server, runs a task on the anotherentityinthesametier,whilealsooffloadingvertically
server,andreturnstheresultstotheenddevice[56].Inthis withanotherentityinanothertier.Forinstance,inafog-fog-
context, various considerations play an essential role in cloud, fog is offloaded with another fog in tier-2 and also
consuming energy in fog computing including the data size offloadedwithacloudintier-3.
| to be offloaded, |     | the wireless | channel’s |     | transmission |     | rate, |     |     |     |     |     |     |     |
| ---------------- | --- | ------------ | --------- | --- | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
power, gain, and bandwidth, as well as the CPU’s power J. EVALUATIONOFFOGCOMPUTINGSOLUTIONS
consumptionpercycleandtherequiredCPUcycleoftheIoT The fog computing testbed has the potential to enhance
devicepertaskbit.
|     |     |     |     |     |     |     |     | the evolution | of fog computing. |     | However, | it  | is challenging |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------------- | --- | -------- | --- | -------------- | --- |
Latency: The total time taken from transferring the task to conduct large-scale real-world experiments in a fog
to the edge servers, running on the server, and receiving computingcontextbecauseofimplementationtimeandhigh
theresponsefromtheserverisreferredtoastaskexecution
cost.Therefore,fewstudieshaveevaluatedtheexperimental
latency [57]. Some parameters have a significant impact on resultsinrealisticandlargescaleareas.Forinstance,in[61],
thetotaldelay,suchasthedatasizeofthetasktobeoffloaded,
|          |         |            |     |         |          |          |     | a multilayer | (IoT-device,  | edge,      | fog, | and cloud) | streaming  |     |
| -------- | ------- | ---------- | --- | ------- | -------- | -------- | --- | ------------ | ------------- | ---------- | ---- | ---------- | ---------- | --- |
| wireless | channel | bandwidth, | CPU | rate of | the edge | servers, |     |              |               |            |      |            |            |     |
|          |         |            |     |         |          |          |     | analytics    | platform with | a two-tier |      | fog layer  | consisting | of  |
andthenumberofCPUcyclesrequiredtoprocesseachbyte analytics and streaming tiers was proposed. This approach,
ofincomingdata. whichhasbeenfunctionallyverifiedonatestbedconsisting
| Cost: | In the | offloading | scope, | the total | execution |     | cost |             |             |               |     |             |             |     |
| ----- | ------ | ---------- | ------ | --------- | --------- | --- | ---- | ----------- | ----------- | ------------- | --- | ----------- | ----------- | --- |
|       |        |            |        |           |           |     |      | of clusters | of low-cost | off-the-shelf |     | components, | illustrates |     |
compriseslocalandremoteexecutioncosts,consideringboth the feasibility of both large-scale data analytics and real-
processingandbufferingdelays.Thiscostmetricdependson time streaming processing. The objective is to manage a
| the task                | demand, | response | time of | the task, | and | location | of  |                                    |          |          |         |              |     |       |
| ----------------------- | ------- | -------- | ------- | --------- | --- | -------- | --- | ---------------------------------- | -------- | -------- | ------- | ------------ | --- | ----- |
|                         |         |          |         |           |     |          |     | large number                       | of cyber | physical | systems | applications |     | based |
| thetaskdeployments[58]. |         |          |         |           |     |          |     | onstreamingandbigdataanalyticsIoT. |          |          |         |              |     |       |
Responsetime:Responsetimeispresentedasthetotaltime
|     |     |     |     |     |     |     |     | Another | study [62] | proposed | a   | time-changing |     | graph |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | -------- | --- | ------------- | --- | ----- |
required to offload a task from the local device to a remote to evaluate the competency of vehicular fog computing
server and to receive a suitable answer on the local device. (VFC) by analyzing Beijing’s vehicular mobility trace and
| The response | time | differs | from | the latency | of  | the system. |     |     |     |     |     |     |     |     |
| ------------ | ---- | ------- | ---- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
constructingamodeunderdiversescenariosinalarge-scale
Latencyistheamountoftimetakenforarequesttobesent urban mobility environment. Furthermore, in [63], a case
andthenreceivedatitsdestination,whereasresponsetimeis study on the creation and deployment of applications in a
theamountoftimebetweensendingarequestandreceiving
large-scale,dynamicfogcomputingsettingutilizinganopen-
asuitableanswer[59]. sourceplatformdistributednode-RED(DNR)waspresented.
Solutionsfordynamicandscalability-natureprototypeswere
I. OFFLOADINGDIRECTION createdusingtheOmnet++networksimulator.Inaddition,
Thissectioninvestigateswherethecomputationaltasksmay thework[64]aself-similarity-basedloadbalancing(SSLB)
be offloaded. Offloading computational tasks can occur in approachforlarge-scalesystemsinafogcomputingsetting
| a variety | of locations, | including |     | IoT devices, |     | fog servers, |     |                |            |      |             |     |                |     |
| --------- | ------------- | --------- | --- | ------------ | --- | ------------ | --- | -------------- | ---------- | ---- | ----------- | --- | -------------- | --- |
|           |               |           |     |              |     |              |     | was presented. | To enhance | SSLB | efficiency, |     | they presented |     |
and clouds. The offloading destination is determined by the anadaptivethresholdstrategyandacorrespondingschedul-
trade-offbetweeninfluencingfactorsandseveralobjectives. ingalgorithm.
| Therefore, | the | offloading | location | is  | crucial | because | it  |         |           |     |              |       |           |     |
| ---------- | --- | ---------- | -------- | --- | ------- | ------- | --- | ------- | --------- | --- | ------------ | ----- | --------- | --- |
|            |     |            |          |     |         |         |     | Because | fog nodes | are | distributed, | it is | difficult | and |
determines the algorithms to be performed [60]. Such expensive for researchers to develop a testbed prototype.
offloadingisrequiredwhenaserviceprovider’sassignedtask Some of them can manage it, but it is expensive to
| exceeds | its processing | capacity, |     | and must | be transferred |     | to  |               |          |           |                 |     |            |     |
| ------- | -------------- | --------- | --- | -------- | -------------- | --- | --- | ------------- | -------- | --------- | --------------- | --- | ---------- | --- |
|         |                |           |     |          |                |     |     | build a large | fog/edge | computing | infrastructure. |     | Therefore, |     |
anotherserviceproviderwithadequatecomputingpower[6]. it is important to create a fog/edge testbed as a service.
Offloadingcanbedoneinthreedifferentways[6]:horizon- An appropriate real network testbed is necessary to assist
tally,vertically,orinahybridtopology.
researchersintestingtheirexperiments,ideas,andalgorithms
|     |     |     |     |     |     |     |     | in realistic | fog computing | environments. |     | It can | also | benefit |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | ------------- | --- | ------ | ---- | ------- |
1) HORIZONTALOFFLOADING researchers by decreasing the deployment time and saving
Horizontaloffloadingoccurswhentwoentitiesbelongtothe costs. The piFogBed was introduced in [65] as the first fog
sametier,suchasacloud-cloudedge-edge,fog-fog,orcloud- computing testbed based on a real network and devices,
cloud. which enables users to execute real fog applications and
|                       |            |        |        |         |     |              |     | receive more                | realistic | results | by utilizing | Docker | container |     |
| --------------------- | ---------- | ------ | ------ | ------- | --- | ------------ | --- | --------------------------- | --------- | ------- | ------------ | ------ | --------- | --- |
| 2) VERTICALOFFLOADING |            |        |        |         |     |              |     | andRaspberryPitechnologies. |           |         |              |        |           |     |
| Vertical              | offloading | always | occurs | between |     | two entities |     |                             |           |         |              |        |           |     |
Furthermore,thestudyin[66]introducedFogbed,anopen
belonging to different tiers, such as edge-fog, edge-cloud, sourcefogsimulationsystembasedonDockerandMininet.
edge-fogorfog-cloud. The existing components were developed for rapid pro-
|     |     |     |     |     |     |     |     | totyping | and testing | of fog | services | in a | real | desktop |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------ | -------- | ---- | ---- | ------- |
3) HYBRIDOFFLOADING environment.Fogbedenablesdeveloperstousetheirverified
Hybrid offloading is a mix of horizontal and vertical applications in real-world settings, with minimal modifica-
offloading in which entities can offload horizontally with tions. FogTestBed was also presented as a framework for
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     |     | 12563 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
| FogTestBed | as    | a service | [67].          | It enables | testbed | owners    | to   |     |     |     |     |     |     |
| ---------- | ----- | --------- | -------------- | ---------- | ------- | --------- | ---- | --- | --- | --- | --- | --- | --- |
| construct  | their | testbed   | infrastructure |            | at the  | network’s | edge |     |     |     |     |     |     |
andtoprovidesecureandprivateaccesstoclientsexecuting
experimentsortests.’’
| However,       | no          | specialized | fog        | computing | testbed   |     | exists to |     |     |     |     |     |     |
| -------------- | ----------- | ----------- | ---------- | --------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- |
| date to assist | researchers |             | in testing | their     | concepts, |     | designs,  |     |     |     |     |     |     |
prototypes,anddistributedalgorithmsinlarge-scalerealistic
| fog computing |            | situations. | Therefore,  |     | researchers    |     | typically |     |     |     |     |     |     |
| ------------- | ---------- | ----------- | ----------- | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
| use existing  | simulators |             | to validate |     | the efficiency |     | of fog    |     |     |     |     |     |     |
computingoffloadingsolutionsunderspecificusecasesand
scenarios.Forexample,iFogSim[68]wasthefirstsimulator
forfogcomputing.Itisanextensionofthemostwell-known FIGURE2. Reinforcementlearningprocess.
cloudcomputingsimulator,CloudSim[69].iFogSimallows
fortheevaluationofresourcemanagementtechniquesbased
onenergyconsumption,latency,networkusage,throughput, their outcomes. Markov Decision Processes (MDPs) are
| and operational |     | costs. | iFogSim | provides | a   | graphical | user |              |        |           |          |     |          |
| --------------- | --- | ------ | ------- | -------- | --- | --------- | ---- | ------------ | ------ | --------- | -------- | --- | -------- |
|                 |     |        |         |          |     |           |      | mathematical | models | [74] that | describe | how | an agent |
interface for describing fog network topologies, including interacts with its environment. When an RL problem meets
sensors, actuators, cloud servers, and connections between theMarkovproperty,thefuturedependsonlyonthecurrent
them.
|     |     |     |     |     |     |     |     | state and action | and not | on what | happened | in history | [75]. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------- | ------- | -------- | ---------- | ----- |
EmuFog [70] is another piece of edge computing sim- According to work [76], an MDP is formally defined as a
ulation software that allows users to emulate large-scale tupleoffivecomponents(S,A,P,R,andY),whereSdenotes
edgecomputingnetworksonindividualcomputers.EmuFog
thecollectionofstates,Adenotesthecollectionofactions,P:
is based on container technology, which means that each S×A×S→[0,1]denotestheprobabilityofmovingfromone
device in the emulation network utilizes its own namespace statetoanothergivenaspecificaction,Rdenotesthereward
| to save | execution | and | network | information |     | and | run the |     |     |     |     |     |     |
| ------- | --------- | --- | ------- | ----------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
function,andYrepresentsadiscountfactorthatdetermines
same program independently. However, some nodes in thesignificanceoffuturerewardsYe[0,1].
realisticedgecomputingsituationsaredynamicandresource- InordertosolvetheMDPproblem,Atthebeginning,the
constrained,andEmuFogisunabletomodelsuchsituations,
agentisinaspecificstate‘s’oftheenvironment,itexecutes
| making | it difficult | to obtain |     | accurate | experimental |     | results. |           |               |       |           |         |           |
| ------ | ------------ | --------- | --- | -------- | ------------ | --- | -------- | --------- | ------------- | ----- | --------- | ------- | --------- |
|        |              |           |     |          |              |     |          | an action | ‘a’. Once the | agent | has taken | action, | the agent |
Furthermore, EdgeCLoudSim [71] is a CloudSim-based movesintothenextstate‘s-’oftheenvironmentandreceives
| edge computing |     | simulator | that | can assess | edge | computing |     |     |     |     |     |     |     |
| -------------- | --- | --------- | ---- | ---------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
somereward‘r’.Asshowninfigure2,theagentperformsthis
performance.Itsedgecomputingsituationsenablerealload
cycleseveraltimesforlearning.
generation and mobility with respect to computing load, Theagenttakesdifferentactionstodiscovernewinforma-
| package | size, and | the ability |     | of users | to combine | their | own |     |     |     |     |     |     |
| ------- | --------- | ----------- | --- | -------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
tionandlearnsbyreceivingarewardforeachcorrectaction
| requirements | into | a tool. | However, |     | the outcomes |     | of the |     |     |     |     |     |     |
| ------------ | ---- | ------- | -------- | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- |
andapenaltyforeachwrongaction.Actionspacereferstothe
experimentdifferdfromthoseoftherealscenario. setofoptionsthatanagentcanexecuteinagivenstate.There
| The MobFogSim |     | simulator |     | was recently | been | developed |     |     |     |     |     |     |     |
| ------------- | --- | --------- | --- | ------------ | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
aretwocategoriesofactionspaces:discreteandcontinuous.
| to simulate | application |     | migration | and | device | mobility | in a |            |              |         |             |         |       |
| ----------- | ----------- | --- | --------- | --- | ------ | -------- | ---- | ---------- | ------------ | ------- | ----------- | ------- | ----- |
|             |             |     |           |     |        |          |      | A discrete | action space | is used | to describe | systems | where |
fogcomputingscenario[72].ThisisanextensionofiFogSim the action space is small, finite, and countable, whereas a
| that incorporates |     | mobility | features |     | into the | fundamental |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | -------- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
continuousactionspaceisusedtodescribeinsystemswhich
| functionality | of  | several | iFogSim | components. |     | However, | the |     |     |     |     |     |     |
| ------------- | --- | ------- | ------- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
anactioncantakeanyvaluewithinagivenrange[77].
MobFogSim mobility support system only interacts with Theagentreceivedarewardimmediatelyafterperforming
| cloud datacenters |     | and IoT | gateways, |     | which limits | its | ability |     |     |     |     |     |     |
| ----------------- | --- | ------- | --------- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- |
theaction.TheimmediaterewardRisdefinedbyanumeric
tocreateclustersinfogcomputingsettings.Inaddition,[73]
|     |     |     |     |     |     |     |     | value (positive | or negative) | to assess | the | desirability | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------ | --------- | --- | ------------ | ------ |
proposed the iFogSim2 simulator, an extension of the action taken by the agent. Thus, the agent’s objective is to
| iFogsim | simulator, | to  | handle | service | migration | for | various |     |     |     |     |     |     |
| ------- | ---------- | --- | ------ | ------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
optimizecumulativerewardsratherthanimmediaterewards.
| IoT device | mobility |     | models, | microservice |     | orchestration, |     |          |                 |      |              |           |     |
| ---------- | -------- | --- | ------- | ------------ | --- | -------------- | --- | -------- | --------------- | ---- | ------------ | --------- | --- |
|            |          |     |         |              |     |                |     | In large | space problems, | such | as vehicular | networks, | the |
and node clustering in edge/fog computing environments. state space is vast, and it is impractical for the agent to
| The benefits |     | of employing |     | simulation-based |     | techniques |     |             |               |           |        |         |          |
| ------------ | --- | ------------ | --- | ---------------- | --- | ---------- | --- | ----------- | ------------- | --------- | ------ | ------- | -------- |
|              |     |              |     |                  |     |            |     | continually | explore every | potential | action | in each | state to |
includethereproducibilityofthestudiesandalessexpensive
achievetheappropriateconfidence.Anagentmustgeneralize
method for evaluating the efficiency of a target platform the state space in such situations. Some states may be
becausephysicalhardwareisnotrequired.
infrequentlyvisitedormayhavecharacteristicsthatallowfor
generalization.Suchcontinuousspacesandhighdimensions
cannotbehandledusingconventionalreinforcementlearning.
K. REINFORCEMENTLEARNING
Reinforcement learning is defined as a feedback-based Deepreinforcementlearningwasusedtosolvethisproblem.
machinelearningtechniqueinwhichanagentlearnstointer- Deepreinforcementlearningintegratesdeeplearning(DL)
actwiththeenvironmentbyexecutingactionsandobserving and reinforcement learning (RL) [78]. DRL is an enhanced
| 12564 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
|     |     |     |     |     |     |     |     | IV. RESEARCHMETHODOLOGY |           |                |     |                |               |               |         |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --------- | -------------- | --- | -------------- | ------------- | ------------- | ------- |
|     |     |     |     |     |     |     |     | This section            | presents  |                | the | methodology    | used          | to            | conduct |
|     |     |     |     |     |     |     |     | the comprehensive       |           | literature     |     | review. First, | it formalizes |               | the     |
|     |     |     |     |     |     |     |     | research                | question. | Next,          | the | electronic     | database      |               | sources |
|     |     |     |     |     |     |     |     | used for                | finding   | and retrieving |     | papers         | related       | to offloading |         |
|     |     |     |     |     |     |     |     | mechanisms              | based     | on             | the | RL and         | DRL methods   |               | in fog  |
computingarediscussed.Furthermore,itoutlinesthegeneral
andexactkeywordsusedtoidentifyrelevantarticlesandtheir
qualityevaluationprocess.
A. QUESTIONFORMALIZATION
|     |     |     |     |     |     |     |     | The research  | objective |            | is to      | search, collect, | and      | identify  | the    |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ---------- | ---------- | ---------------- | -------- | --------- | ------ |
|     |     |     |     |     |     |     |     | best articles | on        | offloading | techniques |                  | based on | RL        | or DRL |
|     |     |     |     |     |     |     |     | approaches    | in        | the fog    | computing  | field.           | The      | following | are    |
someoftheresearchquestionsthatwillbeansweredinthis
study:
|     |     |     |     |     |     |     |     | RQ1: | What | categorization |     | can be applied | to  | RL  | or DRL |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | -------------- | --- | -------------- | --- | --- | ------ |
basedoffloadingmechanismsinfogcomputing?
RQ2:WhichtypesofalgorithmsareutilizedbyRLorDRL
basedoffloadingmechanismsinfogsystems?
RQ3:WhichtypicalperformancemetricsareutilizedinRL
orDRL-basedoffloadingtechniquesinfogcomputing?
|     |     |     |     |     |     |     |     | RQ4: | What | cases are | studies | considered | in  | RL  | or DRL |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --------- | ------- | ---------- | --- | --- | ------ |
basedoffloadingtechniquesinthefogparadigm?
RQ5:WhichtoolsareusedtoevaluateRLorDRLbased
mechanismsforoffloadinginfogsystems?
RQ6:WhichoffloadingmodesareappliedinRLorDRL-
basedoffloadingtechniquesinthefogparadigm?
RQ7:WhatoffloadingdirectionisusuallyappliedinRLor
DRL-basedoffloadingtechniquesinfogareas?
RQ8:Whichoffloadingdecisionsaremadewithrespectto
|     |     |     |     |     |     |     |     | what, where, | when, | and | how | are decisions | in  | their | strategy |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | --- | --- | ------------- | --- | ----- | -------- |
basedonRLorDRL-basedoffloadingtechniquesinthefog
area?
|     |     |     |     |     |     |     |     | RQ9:  | Is SDN       | incorporated |            | into | their strategy |     | based  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | ------------ | ---------- | ---- | -------------- | --- | ------ |
|     |     |     |     |     |     |     |     | on RL | or DRL-based |              | offloading |      | mechanisms     |     | in fog |
computing?
RQ10:Howmanystudieshaveformulatedtheiroffloading
strategyproblemasanMDPorpartiallyobservableMarkov
decisionprocesses(POMDP)problemandsolveditbasedon
FIGURE3. Reviewmethodology.
RLorDRLapproachesinafogenvironment?
|         |           |           |     |          |             |     |       | RQ11: | What | are the | future | research | directions | and | open |
| ------- | --------- | --------- | --- | -------- | ----------- | --- | ----- | ----- | ---- | ------- | ------ | -------- | ---------- | --- | ---- |
| version | of the RL | technique |     | proposed | by DeepMind |     | [79], |       |      |         |        |          |            |     |      |
issuesforRLandDRLbasedoffloadingmechanismsinthe
| in which | DL is | utilized | as a | powerful | tool for | enhancing |     |     |     |     |     |     |     |     |     |
| -------- | ----- | -------- | ---- | -------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fogparadigm?
| the learning | rate      | of RL | techniques | [80].        | In traditional |           | RL, |             |     |        |      |             |     |              |     |
| ------------ | --------- | ----- | ---------- | ------------ | -------------- | --------- | --- | ----------- | --- | ------ | ---- | ----------- | --- | ------------ | --- |
|              |           |       |            |              |                |           |     | In Sections |     | VI and | VII, | the answers | to  | the research |     |
| the values   | of states | and   | actions    | are recorded | using          | a tabular |     |             |     |        |      |             |     |              |     |
questionsarediscussed.
| method. | Therefore, | the | deep | learning | architecture | in  | deep |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ---- | -------- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
reinforcement learning can be considered as a functional B. SOURCEOFINFORMATION
| approximator, | helping | the | system | handle | high-dimensional |     |     |               |     |            |           |      |          |     |       |
| ------------- | ------- | --- | ------ | ------ | ---------------- | --- | --- | ------------- | --- | ---------- | --------- | ---- | -------- | --- | ----- |
|               |         |     |        |        |                  |     |     | The following |     | electronic | databases | were | searched | for | stud- |
data and provide an approximation in the face of massive ies relevant to offloading mechanism-based RL or DRL
actions and state spaces. The mapping from state to action approachesinfogsystems:
inthislearningisdefinedbyneuralnetworksratherthanan • GoogleScholar(<www.scholar.google.co.in>)
|               |     |           |       |          |               |     |       | • IEEEeXplore(<www.ieeexplore.ieee.org>) |     |     |     |     |     |     |     |
| ------------- | --- | --------- | ----- | -------- | ------------- | --- | ----- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| SVM, decision |     | trees, or | other | function | approximators |     | [45]. |                                          |     |     |     |     |     |     |     |
Deep learning convolution and recurrent neural networks • Springer(<link.springer.com>)
|           |      |            |     |          |              |     |       | • ScienceDirect(<www.sciencedirect.com>)          |     |     |     |     |     |     |     |
| --------- | ---- | ---------- | --- | -------- | ------------ | --- | ----- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| have also | been | used [81]. | For | example, | the Q-values |     | for a |                                                   |     |     |     |     |     |     |     |
|           |      |            |     |          |              |     |       | • WileyInterscience(<www.Interscience.wiley.com>) |     |     |     |     |     |     |     |
finitenumberofdiscreteactionsandstatescanberepresented
inatable.However,torepresentQ-valuesincontinuousstate • MDPI(<https://www.mdpi.com>)
|     |     |     |     |     |     |     |     | • ACMDigitalLibrary(<www.acm.org/dl>) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
spaces,functionapproximators,suchasDNNs,arerequired.
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 12565 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
TABLE3. Automaticsearchpaperfilteringusinginclusion/exclusion RL approaches use temporal difference (TD) learning to
criteria. approximatethevaluefunctionratherthanlearningthepolicy
(π),
|     |     |     |     |     |     |     | explicitly       | [78].            | For each       | learned         | policy    | there       | are       | two   |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ---------------- | -------------- | --------------- | --------- | ----------- | --------- | ----- |
|     |     |     |     |     |     |     | related          | value functions: |                | the state-value |           | function    | ’V(s)     | and   |
|     |     |     |     |     |     |     | the state-action |                  | value function |                 | ’Q(s, a). | The         | objective | of    |
|     |     |     |     |     |     |     | the value-based  |                  | method         | is to           | identify  | the optimum |           | value |
function,whichisthemaximumvalueinanygivenstatethat
|     |     |     |     |     |     |     | can be | obtained | under any | policy. | Typical | value-based |     | RL  |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --------- | ------- | ------- | ----------- | --- | --- |
algorithmsincludeQ-learningandSARSA.
1) Q-LEARNING
Q-learningisamodel-freereinforcementlearningtechnique
thatcanbeusedtodeterminetheoptimumpolicyforagiven
state.TheQ-learningalgorithmlearnseachstatetodetermine
theoptimalcourseofactionbasedontheQ-valuefunction.
C. PAPERSELECTIONPROCESS
|                    |     |            |        |     |              |     | Learning | occurs | through | trial | and error | until | a particular |     |
| ------------------ | --- | ---------- | ------ | --- | ------------ | --- | -------- | ------ | ------- | ----- | --------- | ----- | ------------ | --- |
| This comprehensive |     | literature | review |     | has searched | the |          |        |         |       |           |       |              |     |
courseofactionyieldsanidealpolicy[82].
aforementioneddigitallibrariesusingrelevantkeywordssuch Several offloading problems in fog computing have been
| as ‘‘fog,’’ | ‘‘fog | computing,’’ | ‘‘offloading,’’ |     | ‘‘reinforcement |     |     |     |     |     |     |     |     |     |
| ----------- | ----- | ------------ | --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
solvedwiththehelpoftheQlearningmethod.Forexample,
| learning,’’ | ‘‘Deep | learning | learning,’’ | ‘‘DQN,’’ |     | ‘‘DDQN,’’ |     |     |     |     |     |     |     |     |
| ----------- | ------ | -------- | ----------- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
theauthorsofthepaper[10]proposedaninnovativeapproach
‘‘A2C,’’ ‘‘SAC,’’ and ‘‘Q learning’’., Snowball searches to the issue by giving IoT nodes the option to choose to
| were also   | performed | using   | the publications |         | that         | cited each |          |          |               |       |         |       |        |        |
| ----------- | --------- | ------- | ---------------- | ------- | ------------ | ---------- | -------- | -------- | ------------- | ----- | ------- | ----- | ------ | ------ |
|             |           |         |                  |         |              |            | offload  | tasks to | the proximity |       | of fog  | nodes | or the | ideal  |
| found paper | to find   | further | related          | papers. | In addition, | this       |          |          |               |       |         |       |        |        |
|             |           |         |                  |         |              |            | fog node | and      | the remote    | cloud | to meet | the   | needs  | of the |
systematic review included research publications written in applications. A Q-learning-based algorithm is employed to
Englishbetween2019andmid-2022.Atotalof276research
|     |     |     |     |     |     |     | solve the | model | and select | the | optimal | offloading |     | policy. |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ---------- | --- | ------- | ---------- | --- | ------- |
articlesfromvariousconferencesandjournalswereidentified
|     |     |     |     |     |     |     | The fundamental |     | aim of | this | study is | to reduce | the | total |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | ---- | -------- | --------- | --- | ----- |
through the search procedure. As shown in figure 3, the latency and distribute tasks evenly across fog nodes by
| final paper   | selection |             | was filtered | using  | both | inclusion   |          |            |       |             |            |       |           |     |
| ------------- | --------- | ----------- | ------------ | ------ | ---- | ----------- | -------- | ---------- | ----- | ----------- | ---------- | ----- | --------- | --- |
|               |           |             |              |        |      |             | lowering | the number | of    | offloading  | operations |       | required  | to  |
| and exclusion |           | strategies. | The total    | number |      | of research |          |            |       |             |            |       |           |     |
|               |           |             |              |        |      |             | allocate | a task     | to an | appropriate | fog        | node. | Numerical |     |
publications decreased in four stages: first, based on their simulations demonstrate that the recommended technique
| titles, to | 170; and | second, | based | on their | abstracts | and |     |     |     |     |     |     |     |     |
| ---------- | -------- | ------- | ----- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
outperformsotherapproachesintermsofdecreasinglatency,
conclusions,to90.Inthethirdstage,60researchpaperswere
|     |     |     |     |     |     |     | processing | more | tasks, and | distributing |     | the workload |     | more |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---------- | ------------ | --- | ------------ | --- | ---- |
selected based on full-text analysis. Finally, based on the smoothly. Furthermore, the authors of work [11] address
inclusionandexclusionprincipleshownintable3,56papers
|     |     |     |     |     |     |     | the load | balancing | problem |     | while achieving |     | the | lowest |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------- | --- | --------------- | --- | --- | ------ |
wereselectedtoanswerthecurrentstudytechnicalquestions.
|     |     |     |     |     |     |     | possible | latency | in fog | networks. | To  | address | this | issue, |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------ | --------- | --- | ------- | ---- | ------ |
No research articles found in the MDPI or ACM digital a decision-making approach based on Q learning was
librariesmettheinclusionandexclusioncriteria.
|     |     |     |     |     |     |     | developed | to determine |     | the best   | offloading | action | to       | take |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | ---------- | ---------- | ------ | -------- | ---- |
|     |     |     |     |     |     |     | while the | reward       | and | transition | functions  | are    | unknown. |      |
V. OFFLOADINGMECHANISMSINFOGCOMPUTING To reduce the overload probability and processing time, the
BASEDONRLANDDRLTECHNIQUES proposed methods enable fog nodes to choose an available
This section provides a review of current publications neighboring fog node based on their resource capabilities
on RL and DRL algorithms used to address offloading and to offload the maximum number of incoming tasks.
| problems | in fog | computing. | Figure | 4 shows | the | taxonomy |     |     |     |     |     |     |     |     |
| -------- | ------ | ---------- | ------ | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Similarly,in[83],aQ-learning-basedtechniqueforselecting
in which RL and DRL algorithms are organized into three idealoffloadingnodesinopportunisticedgecomputingwas
| major classes: | value-based, |     | policy-based, |     | and hybrid-based |     | proposed. |     |     |     |     |     |     |     |
| -------------- | ------------ | --- | ------------- | --- | ---------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
algorithms.Qlearning,DQN,DoubleDQN,DuelingDQN,
|     |     |     |     |     |     |     | Additionally, |     | a new approach |     | to fog-based |     | IoV network |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | --- | ------------ | --- | ----------- | --- |
DRQN,andSARSAare‘‘value-based’’approaches,whereas communication security, QoS improvement, and end-to-end
PG,DDPG,andPPOare‘‘policy-based’’approaches.Hybrid delay reduction has been proposed by a study [84]. This
| approaches | include | DDPG | and SAC. | This | study | focuses |        |          |                |     |        |     |     |        |
| ---------- | ------- | ---- | -------- | ---- | ----- | ------- | ------ | -------- | -------------- | --- | ------ | --- | --- | ------ |
|            |         |      |          |      |       |         | system | exploits | the advantages |     | of SDN | and | the | block- |
on model-free approaches to address offloading issues in chain technology. The SDN controller uses a Q learning
a fog environment. A summary of the results is presented based RL algorithm to assign tasks to fog nodes so that
intable4.
|     |     |     |     |     |     |     | traffic can | be  | distributed | more | evenly. | As a | result | of the |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | ---- | ------- | ---- | ------ | ------ |
authors’experiments,SaFIoViscapableofavoidingnetwork
|     |     |     |     |     |     |     | congestion, | reducing | latency, |     | and efficiently |     | utilizing | net- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | -------- | --- | --------------- | --- | --------- | ---- |
A. VALUE-BASEDALGORITHMS
The value function, also referred to as the value of the work resources. Similarly, the authors in [85] proposed a
policy, is used to assess the states depending on the secure computation offloading scheme to minimize delay
cumulative reward the agent obtains over time. Value-based andenergyconsumptionintheIoT-Fog-Cloudenvironment.
| 12566 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
| FIGURE4. TaxonomyoffogcomputingoffloadingmechanismsbasedonRLandDRLmethods. |     |     |     |
| -------------------------------------------------------------------------- | --- | --- | --- |
Selection of the best fog node is based on Particle Swarm proposeaQ-learning-baseddynamicoffloadingstrategyfor
Optimization (PSO). When the fog node cannot handle the this purpose. In the next step, the researchers used a neuro-
workload within the latency constraints, it is forwarded to fuzzy model to secure information at the fog node’s smart
| the remote cloud | server for further | processing. | The authors gateway. |
| ---------------- | ------------------ | ----------- | -------------------- |
VOLUME11,2023 12567

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
Oneofthemostchallengingaspectsofresourcemanage- toimprovementsoverthelocalexecution,First-Fit(FF),and
ment for intelligent mobile apps is deciding when and how ASDEOmethods.
tooffloadandprovidesedgeserverstocontroltheirdynamic Furthermore, offloading tasks from heterogeneous nodes
workloads of mobile applications. The authors of [86] used at the edge of an open and dynamic network is challenging
the learning automata technique to make the most optimal becauseofthefluctuatingworkloadgeneratedbyapplications
offloadingselectionforworkloadssubmittedbysmartmobile with different service level agreement (SLA) and quality
applications.Inaddition,theQ-learningtechniqueandLSTM of service (QoS) requirements. The study presented in [93]
predictionmodelwereutilizedtomakeanappropriatescaling provided a new learning-based task offloading approach to
decision for adding or removing the edge server to adapt orchestrate the workload at the network’s edge. In compar-
toworkloadfluctuations.Comparedwithothermethods,the ison with the baseline algorithms, the results indicate that
proposed technique enhances CPU usage and reduces the resources are better utilized and tasks are performed with a
energyconsumptionandexecutiontime.In[87],proposedan highersuccessrate.
| innovative | framework | named | ‘‘DroneCOCoNet |     |     | ‘‘ for | drone |     |     |     |     |     |     |     |     |
| ---------- | --------- | ----- | -------------- | --- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
videoanalyticsthatenablessophisticatedprocessingoflarge 2) DEEPQNETWORK(DQN)
videodatasourcesutilizingfogcomputationoffloadingand In the context of fog computing, it is challenging to fully
accomplishesnetworkprotocolselectionrelatedtoresource
understandthesystemdynamics.Q-learningisamodel-free
awareness. Heuristic and reinforcement learning based Q approach for solving this issue. However, Q-learning is a
learning approaches were used to deal with computation tabular approach, and its size increases exponentially with
| offloading | problems | to  | reduce | overall | computation |     | costs |            |     |        |            |          |     |              |     |
| ---------- | -------- | --- | ------ | ------- | ----------- | --- | ----- | ---------- | --- | ------ | ---------- | -------- | --- | ------------ | --- |
|            |          |     |        |         |             |     |       | the number | of  | nodes. | Therefore, | defining |     | and updating | a   |
andlatencyinedge/fogresourceswhilealsoreducingvideo Q-tableinalargestatespaceenvironmentisacomplexand
processingtimestofulfillapplicationrequirements. challenging task. The deep Q network (DQN) method was
| The study | in  | [88] proposed |     | a reinforcement |     | learning- |     |     |     |     |     |     |     |     |     |
| --------- | --- | ------------- | --- | --------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
usedtoresolvethisproblem.Inthisconfiguration,ratherthan
baseduseraccessandcomputationoffloadingtechniqueinan
|     |     |     |     |     |     |     |     | generating | a Q-table, |     | the neural | network | estimates |     | the Q- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ---------- | ------- | --------- | --- | ------ |
F-RANscenario,whichusedQlearningtomaximizesystem valuesforeachactionandstate.Manyacademicresearchers
| resource | utilization | and | minimize | energy | consumption |     | by  |               |     |            |          |     |               |     |       |
| -------- | ----------- | --- | -------- | ------ | ----------- | --- | --- | ------------- | --- | ---------- | -------- | --- | ------------- | --- | ----- |
|          |             |     |          |        |             |     |     | have proposed |     | offloading | problems | in  | fog computing |     | under |
consideringboththedownlinkanduplinktaskrequirements.
MDP,whichcanbeaddressedbytheDQN,whichdecreases
| Furthermore, | [89] | proposed | an  | intelligent | local | offloading |     |     |     |     |     |     |     |     |     |
| ------------ | ---- | -------- | --- | ----------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thenumberofQ-statesthatmustbetrainedforeachaction.
| to enhance | the      | latency       | and | energy         | efficiency | of          | smart |              |            |          |     |             |     |            |       |
| ---------- | -------- | ------------- | --- | -------------- | ---------- | ----------- | ----- | ------------ | ---------- | -------- | --- | ----------- | --- | ---------- | ----- |
|            |          |               |     |                |            |             |       | For example, |            | in [94], | a   | computation |     | offloading | and   |
| factories. | Besides, | [90] designed |     | cost-efficient |            | computation |       |              |            |          |     |             |     |            |       |
|            |          |               |     |                |            |             |       | resource     | allocation | system   | for | F-RANs      | was | proposed   | using |
offloading (CeCO) for green industrial fog environments. DeepReinforcementLearning(DRL).Thisoffloadingprob-
| In their | research | the fog | controller | concept | was | introduced |     |         |              |     |       |     |            |             |     |
| -------- | -------- | ------- | ---------- | ------- | --- | ---------- | --- | ------- | ------------ | --- | ----- | --- | ---------- | ----------- | --- |
|          |          |         |            |         |     |            |     | lem can | be described |     | as an | MDP | and solved | efficiently |     |
tocontrolcomputationoffloadingbetweenindustrialdevices.
|     |     |     |     |     |     |     |     | using a | DQN. | The main | idea | of the | proposed |     | approach |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | -------- | ---- | ------ | -------- | --- | -------- |
Initially, industrial devices distinguished between remote is that the DRL controller can make intelligent decisions
| and IIoT | executable | tasks.     | They     | also included |             | a frequency- |        |            |            |       |              |           |             |         |          |
| -------- | ---------- | ---------- | -------- | ------------- | ----------- | ------------ | ------ | ---------- | ---------- | ----- | ------------ | --------- | ----------- | ------- | -------- |
|          |            |            |          |               |             |              |        | to process | a produced |       | task locally | or        | to transfer |         | the task |
| enabled  | power      | management | strategy |               | to minimize |              | energy |            |            |       |              |           |             |         |          |
|          |            |            |          |               |             |              |        | to a fog   | access     | point | (FAP)        | or remote | cloud       | server. | The      |
emissionsinanindustrialcontext.Overburdenedtaskswere simulation results indicated that the recommended design
thentransferredtothefogcontroller,wheretheprimaryfog
considerablyminimizeddelaysandmaximizedthroughputin
controllerusedaprobabilistictechniquetoselectthebestfog thesystem.Followingasimilaridea,forlong-termreduction
device. Additionally, the fog controller uses the Q-learning insystemenergyconsumption,theauthorsof[95]proposed
methodtodeterminetheshortestpathtothedestination.
|     |     |     |     |     |     |     |     | a deep reinforcement |     |     | learning | (DRL) | approach | based | on a |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | -------- | ----- | -------- | ----- | ---- |
Moreover, [91] proposed a novel framework called DQN with a scenario of multiple IIoT devices and multiple
(ARTNet) for efficient task offloading in software defined fog access points (F-APs). Subsequently, [96] presented
vehicular (SDV F) based on the Q learning method. The a new incentive system for the IoV scenario based on
major objective of the proposed framework is to improve contractsthatintegratebothresourceutilizationandresource
the offloading action through each system to optimize contribution.Theproposedapproachwasusedtodetermine
the utility while optimally distributing the IoV workloads thebestlocationforexecutingthemodules(mobiledevices,
and reducing the processing time. In addition, the authors fog or cloud). The authors proposed a distributed deep
of[92]presentedatechniquecalledGASDEOforoffloading reinforcementlearning(DRL)basedDQNmethodtoassign
a decision-based MAPE to different mobile devices, fog, resourcesandreducethesystemcomplexity.
orcloudarchitectures.Accordingtotheproposedtechnique, Inaddition,adeeplearningbasedreinforcementnetwork
fog devices (FDs) were analyzed locally using a greedy waspresentedfortheresourceallocationandtaskoffloading
technique, starting with the sibling nodes and continuing to problem in [97]. Specifically, a deep Q learning network
theparentnodes.Inthefollowingstage,theDRLmethodis (DQN)wasusedtoaddressissuesmodeledasanMDP.The
usedtoselectthebestdestinationforrunningmodulesona
|     |     |     |     |     |     |     |     | DQN receives |     | the tasks | in the | queue | as the | input | and the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | ------ | ----- | ------ | ----- | ------- |
mobiledevice,fog,orcloudenvironment,intermsofpower resources available on the fog node. Therefore, instead of
consumption, total execution cost, and network resource using a standard convolutional neural network, this study
usage.Theresultsindicatedthatthesuggestedtechniqueled
|       |     |     |     |     |     |     |     | used a short | term | memory | network |     | (LSTM) | in the        | DQN. |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ------ | ------- | --- | ------ | ------------- | ---- |
| 12568 |     |     |     |     |     |     |     |              |      |        |         |     |        | VOLUME11,2023 |      |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
A DQN environment was constructed with fog nodes using energy consumption in vehicle fog computing. Offloading
the reinforcement learning toolkit in MATLAB and the decisions in IoV are challenging because of the dynamic
SUMOenvironmentforVANETbehavior.TheDQNselects natureoftheenvironmentandlargenumberofexistingstate
thefognodetobeoffloaded,andthevehiclemustbeinside spaces. In addition, [14] proposed a low-complexity deep
the new node’s range of transmission when the simulation reinforcement learning technique based on DQN to address
is run. Next, the vehicle locations were predicted using the theissueofjoboffloadingandresourceallocationinacell-
KalmanfilterpredictionalgorithmintheDQNsetting. freeradioaccessnetwork.Anoptimizationaimofdecreasing
Moreover, the authors of [98], studied a task offloading the system latency is employed, and a DNN is utilized
scheme in optimal query and policy dynamic environ- to speed up the learning of the system, which can make
ments. The authors were able to acquire the ideal query optimalselectionsunderahighnumberofusersandtasksand
policy at the task node using the reinforcement learning generateappropriateoffloadingtechniquesforcomputation.
framework,resultinginlong-termoptimizedtaskoffloading Consequently, computational resource allocation and task
performance. Their research also proposed a simple and, offloading have been jointly enhanced to address and
effective approach for the task node to learn the best query solvethecomputationaloffloadingproblemincollaborative
decision by utilizing deep Q-networks, whereas the task vehicle networks [105]. To reduce the inferior learning per-
node is unaware of the dynamics of the system. According formance resulting from excessive vehicle mobility, an AF-
to the numerical results, the performance of the proposed DQN asynchronous federation mechanism was deployed.
query policy learning method was close to the optimum The simulation results illustrate that the proposed approach
performance. Similarly, in [99] task offloading based deep canhelpreducethetotalqueuinglatencyandenhancesystem
Q learning in the healthcare Internet of Things (IoT) throughput. To address the task offloading issues in delay
was used to distribute the load across the edge, fog, and restriction vehicular edge computing, [106] suggested two
cloud. Besides, thetask offloading problem incollaborative techniques of value-based reinforcement learning: b-FDQO
vehicle networks was modeled as an MDP by the authors andbaselineDQN.
of [100].Then, to enhance user vehicle performance while Accordingtoapreviousstudy[107],asmartmobilityfog
still meeting URLLC constraints, a Deep Reinforcement agent(MFA)isincludedintheSDNcontroller.Theauthors
learning–based URLLC–aware DQN–based task offloading also developed an adaptive policy for resource allocation
algorithm DREAM, was developed. The proposed schema that handles offloading tasks along with the user mobility
outperformed other schemes with existing task offloading information. It also showed an innovative IoT-fog system
methodsintermsofqueuingdelay,throughput,andURLLC. basedonanSDNcontrollerandaDRLstrategy.Thissystem
Finally,[101]proposedanoffloadingstrategybasedondeep provides awareness of mobility services and responds to
Q-learningtomaximizetheQoEoftasksindelay-constrained environmental changes. In their research study, they also
VFC.Consideringboththedeadlineanddelayofataskinthe proposedaninnovativelocalsearch-basedDQNstrategythat
rewardfunctionofDeepQ-Learning improves system costs (energy and execution time) for the
WiththecontinuedgrowthofextensiveIIoTapplications, workloads demanded in different time zones. Furthermore,
effective service delivery and energy reduction face signif- theresearchpaper[108]presentsDRLenergy-efficienttask
icant obstacles. However, a single fog device cannot fully scheduling and offloading in a fog IoT network based on
performlarge-scaleapplicationsowingtoalackofresource SDN. A single SDN controller layer was used to centralize
availability.Apartialserviceprovisioningapproachoffersa network control and orchestration. SDN-fog computing
potentiallysuccessfulsolutiontoactivateservicesonseveral reduces network latency and traffic overhead. In addition,
fog devices or to collaborate with cloud servers. Inspired theyproposedaDRLtechniquetoenhancelatencyreduction
by this scenario, the work [102] presented a cooperative andminimizeenergyconsumptionindynamicanddistributed
partial service provisioning technique for tackling massive IoT networks. There have been a number of problems
industrial applications in fog networks. First, this study with optimizing task offloading in highly dynamic vehicle
aimstojointlyenhanceenergyconsumptionandprocessing networks, including insufficient information, conflicting
latencyacrossallIIoTapplicationsinindustrialfognetworks. queuing latency, and high dimensional curse. In [109],
To accomplish this goal, a task partitioning technique for a queuing delay-aware task offloading algorithm based on
splittinglargeIIoTtasksintoseveralindependenttaskswas DRL methods was proposed to dynamically improve the
presented. Then, to intelligently distribute the partitioned task offloading problem and maximize the throughput of
tasks across the proximate fog devices, a DRL based DQN user vehicles while meeting the requirements for the long-
enabledserviceprovisioningtechniqueisdeployed. term queueing delay in collaborative vehicular networks.
According to [103], task offloading can be solved by The simulation results indicate that the proposed method
consideringbothcommunicationandcomputationresources outperformstheD-QLOAandEMMapproachesintermsof
inamobilevehiclenetwork.Theauthorsformulatedanon- throughputandend-to-endqueuingdelay.
linear issue for energy efficiency. A deep reinforcement
learning (DRL)-based DQN approach is used to solve the 3) DOUBLEDQN
formulatedproblem.Theauthorsof[104]proposedadeepQ- AtraditionalDQNoftenusesasinglemathematicalestimator
learningnetwork(DQN)methodtominimizebothdelayand to select and evaluate an action, which could cause the
VOLUME11,2023 12569

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
value of the action to be overestimated [110]. To address it performs poorly when processing data with long-term
this problem, a double DQN (DDQN) was presented dependency.Toovercomethisproblem,anLSTMalgorithm
in [111]. Specifically, the Double DQN algorithm splits wasintroduced.TheLSTMismoreefficientthantraditional
the evaluation and selection processes into two maximum neural networks in terms of storing and retrieving informa-
function estimators. The double estimator method does not tion. Therefore, it has recently been used in several fields
overestimate the action value, resulting in a more accurate related to sequence processing [116]. The DRQN method
estimation. enhances the DQN by using an LSTM instead of a fully
| A double | DQN-based | computation |     |     | offloading | policy | in  |     |     |     |     |     |     |     |     |
| -------- | --------- | ----------- | --- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
connectedlayer[117].Toefficientlymemorizetheactionthat
a F-RAN considering D2D communication between user maximizestherewardineachstate,theDRQNusesLSTMto
devices was proposed in [110]. This study aims to reduce storeadditionalinformationregardingactionchoiceswithin
| costs by | considering | both | execution |     | delay | and | power |          |              |             |     |      |          |         |     |
| -------- | ----------- | ---- | --------- | --- | ----- | --- | ----- | -------- | ------------ | ----------- | --- | ---- | -------- | ------- | --- |
|          |             |      |           |     |       |     |       | a state. | By combining | information |     | over | a longer | period, | the |
consumption.Simulationfindingsindicatethattheproposed DRQN further improves the network’s ability to deal with
method efficiently minimizes the total cost compared to partiallyobservablemodels[118].
existingmethods.Moreover,in[12],anenergy-efficientcom-
|     |     |     |     |     |     |     |     | As an | alternative | to  | the DQN, | a   | DRQN | approach | can |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | -------- | --- | ---- | -------- | --- |
putationaloffloadingstrategywasproposedforathree-layer be used to estimate optimal value functions and effectively
architecture in IoV, which incorporates layers of cloudlets, deal with inadequate state observations while dealing with
RSUs,andfognodes.Intheirresearch,theyconsideredboth
partialobservabilityandalargestatespace.Therefore,many
stationaryandmovingvehiclesasfogserversanddeveloped fog computing computational task offloading problems are
a DRL method based on queuing theory to coordinate task formed as partially observable Markov decision processes
flowsinordertominimizeoverallenergyusage.
|     |     |     |     |     |     |     |     | (POMDPs) | because | the | agent | can only | view | a portion | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --- | ----- | -------- | ---- | --------- | --- |
For offloading and allocation optimization problems, theentireobservationenvironmentandacademicresearchers
a double DQN was used to address the high-dimensional tackletheseissuesbasedontheDRQNmethod.TheDRQN
statespacewhenthereweremorewirelessdevices.Astudy
|     |     |     |     |     |     |     |     | method | combines | the past | state | with the | current | input | state, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | -------- | ----- | -------- | ------- | ----- | ------ |
in[112]suggestedadecentralizedoptimizationschemebased allowing appropriate decisions, even if the present state of
onadoubleDQNcalled(DOCRRL)forbandwidthallocation theenvironmentisnotobservable.Forinstance,theauthors
and partial offloading. The suggested schema can learn the of[119]formulateddynamiccomputationoffloadinginIoT
best way to make decisions when there are strict limits on fog systems as a POMDP and solved it using a DRQN to
latencyandrisk,therebyavoidingthecurseofdimensionality provide the IoT device’s ideal offloading policy for each
causedbyahighnumberofpossibleactionsandstates. state. Compared to benchmark offloading techniques, the
|     |     |     |     |     |     |     |     | suggested | offloading | strategy | may | efficiently |     | minimize | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | -------- | --- | ----------- | --- | -------- | --- |
4) DUELINGDQN energyconsumptionofIoTdevicesandsatisfytheprocessing
| One significant | limitation |     | of the | DQN | algorithm | is  | that, |     |     |     |     |     |     |     |     |
| --------------- | ---------- | --- | ------ | --- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
delayrequirementsofcomputingtasks.
in some states, the value function does not depend on Similarly,acomputationaloffloadingandtaskscheduling
the selected action. The Dueling Deep Q-network (Dueling method for minimizing energy consumption under delay
DQN)algorithmhasbeenproposedasasolutiontoovercome
constraintswasproposedbytheauthorsof[120].TheDRQN
theaforementioneddilemma[113]. isthenusedtoaddresspartialobservabilitybasedonlimited
| In addition, | depending |        | on the | network   | architecture |     | of   |           |             |              |     |          |          |              |     |
| ------------ | --------- | ------ | ------ | --------- | ------------ | --- | ---- | --------- | ----------- | ------------ | --- | -------- | -------- | ------------ | --- |
|              |           |        |        |           |              |     |      | data. The | results     | demonstrate  |     | that the | proposed | offloading   |     |
| the DDQN,    | the agent | in the | RL     | gradually | acquires     | a   | more |           |             |              |     |          |          |              |     |
|              |           |        |        |           |              |     |      | algorithm | outperforms | conventional |     | methods. |          | Furthermore, |     |
accuratevalue.ThisindicatesthattheduelingDQNalgorithm to ensure a specific quality of service for each task and
| might achieve | a higher          | performance |          | than | the     | DQN method    |     |          |     |             |     |           |     |               |     |
| ------------- | ----------------- | ----------- | -------- | ---- | ------- | ------------- | --- | -------- | --- | ----------- | --- | --------- | --- | ------------- | --- |
|               |                   |             |          |      |         |               |     | maximize | the | utilization | of  | resources | by  | collaborating |     |
| when it       | comes to handling |             | problems |      | related | to offloading |     |          |     |             |     |           |     |               |     |
betweenseveralfogcomputingnodes,ajointtaskoffloading
policies and resources. The work in [114] adopts a dueling strategyandheterogeneousresourceallocationusingDRQN
| DQN algorithm | to  | choose | the | most | suitable | offloading |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------ | --- | ---- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
algorithmwasproposedin[121].Thegoalofthisstudywasto
strategy for each user equipment (UE), which includes increasethenumberofprocessingtaskswithintheirlatency
| offloading    | to fog access | points | (FAP), |        | proximity | idle      | UEs, | timelimits. |      |              |     |     |         |            |     |
| ------------- | ------------- | ------ | ------ | ------ | --------- | --------- | ---- | ----------- | ---- | ------------ | --- | --- | ------- | ---------- | --- |
| or processing | by itself.    | As     | the    | number | of UEs    | requiring |      |             |      |              |     |     |         |            |     |
|               |               |        |        |        |           |           |      | Moreover,   | DRQN | enhancements |     | to  | the DQN | algorithm, |     |
offloadingincreases,thecentralizedduelingDQNalgorithm make it more suitable for handling issues related to the
becomes more complex. Therefore, a preprocessing mecha- offloading of vehicle tasks in IoV. In [122], an offloading
nismisimplementedtoreducethecomplexityofthedueling
approachusingtheDRQNalgorithmwasproposedtoreduce
| DQN algorithm | by  | immediately |     | fulfilling | some | of the | UE’s |             |            |      |             |     |            |     |        |
| ------------- | --- | ----------- | --- | ---------- | ---- | ------ | ---- | ----------- | ---------- | ---- | ----------- | --- | ---------- | --- | ------ |
|               |     |             |     |            |      |        |      | the latency | of vehicle | task | offloading. |     | Initially, | an  | actual |
task demands. Similarly, [115] proposed a new offloading map was modeled, the task queue was initialized, and a
| policy in | an F-RAN | that uses | the | dueling | DQN | method | to  |                 |     |             |      |      |         |       |     |
| --------- | -------- | --------- | --- | ------- | --- | ------ | --- | --------------- | --- | ----------- | ---- | ---- | ------- | ----- | --- |
|           |          |           |     |         |     |        |     | task offloading |     | environment | with | many | service | nodes | was |
optimizetheoverallutilityofUEs. created.Subsequently,theDQNalgorithm,whichintegrates
|     |     |     |     |     |     |     |     | deep learning | with | reinforcement |     | learning, |     | was designed |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | ------------- | --- | --------- | --- | ------------ | --- |
5) DEEPRECURRENTQ-NETWORK(DRQN) to improve the offloading strategy by minimizing offload
In conventional neural network training, training samples delay. Finally, because complete information cannot be
|               |            |     |        |         |        |          |     | adequately | observed | in  | the environment, |     | the | DQN           | applies |
| ------------- | ---------- | --- | ------ | ------- | ------ | -------- | --- | ---------- | -------- | --- | ---------------- | --- | --- | ------------- | ------- |
| are primarily | determined |     | by the | current | state. | However, |     |            |          |     |                  |     |     |               |         |
| 12570         |            |     |        |         |        |          |     |            |          |     |                  |     |     | VOLUME11,2023 |         |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
an LSTM model to train its neural network to increase the B. POLICY-BASEDALGORITHMS
offloadingeffectiveness.Accordingtothesimulationresults,
|     |     |     |     |     |     |     | The policy-based |     | approach | aims | to  | discover | the best | policy |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | ---- | --- | -------- | -------- | ------ |
the proposed schema-based offloading of vehicle tasks can to optimize the reward in the future without relying on the
significantlyminimizevehicleoffloadingdelays. value function [80]. This method explicitly builds a policy
π:s→a)
|     |     |     |     |     |     |     | (mapping |        | representation |     |          | and maintains |           | it in the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------------- | --- | -------- | ------------- | --------- | --------- |
|     |     |     |     |     |     |     | memory   | during | the learning   |     | process. | Policy        | gradients | (PG)      |
6) STATEACTIONREWARDSTATEACTION(SARSA)
|         |          |              |     |       |                      |     | and proximal |     | policy optimization(PPO) |     |     | are | typical | policy- |
| ------- | -------- | ------------ | --- | ----- | -------------------- | --- | ------------ | --- | ------------------------ | --- | --- | --- | ------- | ------- |
| This is | a method | for learning |     | about | temporal differences | in  |              |     |                          |     |     |     |         |         |
basedRLalgorithms.Thepolicy-basedapproachconsistsof
policy.Intheon-policycontrolapproach,eachstate’saction
|     |     |     |     |     |     |     | two primary | types | of  | policies: | deterministic |     | and stochastic. |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --- | --------- | ------------- | --- | --------------- | --- |
isselectedwhilelearninghowtouseaparticularpolicy.The
|         |            |         |       |     |                |          | In deterministic |     | terms, | policy | (π) produces |     | the same | action |
| ------- | ---------- | ------- | ----- | --- | -------------- | -------- | ---------------- | --- | ------ | ------ | ------------ | --- | -------- | ------ |
| primary | difference | between | SARSA |     | and Q-learning | is that, |                  |     |        |        |              |     |          |        |
inallstates,whereasunderastochasticpolicy,theproduced
incontrasttoQ-learning,modifyingtheQ-valueinthetable
actionisdeterminedbyprobability.Theadvantageofpolicy-
doesnotrequireamaximumrewardforthefollowingstate.
|       |         |             |     |         |       |             | based approaches |     | is that | they | have | superior | convergence |     |
| ----- | ------- | ----------- | --- | ------- | ----- | ----------- | ---------------- | --- | ------- | ---- | ---- | -------- | ----------- | --- |
| SARSA | selects | new actions | and | rewards | based | on the same |                  |     |         |      |      |          |             |     |
propertiesandareefficientincontinuousactionspacesorin
policyastheinitialaction[80].Thestudyin[123]proposeda
highdimensionality.
fuzzyreinforcementlearning(FRL)approachforanenergy-
savingtaskoffloadingschemainaVFC.TheFRLcombines
1) POLICYGRADIENT(PG)
fuzzylogicwiththeSARSAmethodtoreduceboththepower
Thepolicygradientapproachoptimizesparameterizedpoli-
consumptionandresponsetime.
ciesinrelationtoexpectedreturnsbyusinggradientdescent
|     |     |     |     |     |     |     | (long-term | cumulative |     | reward). | They | are | not burdened | by  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | -------- | ---- | --- | ------------ | --- |
7) COMBINGRLORDRLMETHODS many of the issues that plague traditional reinforcement
|                  |     |      |      |     |           |         | learning | approaches, |     | such as | the | lack of | assurance | of a |
| ---------------- | --- | ---- | ---- | --- | --------- | ------- | -------- | ----------- | --- | ------- | --- | ------- | --------- | ---- |
| Many researchers |     | have | used | two | RL or DRL | methods |          |             |     |         |     |         |           |      |
to address the offloading problems in fog computing. value function, complexity imposed by continuous states
|              |     |             |        |            |               |         | and actions,      | and | intractability |           | issue | imposed | by        | unknown |
| ------------ | --- | ----------- | ------ | ---------- | ------------- | ------- | ----------------- | --- | -------------- | --------- | ----- | ------- | --------- | ------- |
| For example, |     | in research | [124], | the        | co-offloading | of both |                   |     |                |           |       |         |           |         |
|              |     |             |        |            |               |         | state information |     | [126].         | In [127], | the   | authors | addressed | the     |
| computation  | and | traffic     | for    | industrial | applications  | in fog  |                   |     |                |           |       |         |           |         |
computing was studied. Initially, they created a table that issue of computation offloading in an Internet of Things
|               |            |            |             |      |                 |         | (IoT) fog   | system  | enabled | by        | energy | harvesting    | (EH). | The       |
| ------------- | ---------- | ---------- | ----------- | ---- | --------------- | ------- | ----------- | ------- | ------- | --------- | ------ | ------------- | ----- | --------- |
| stored task   | properties |            | based       | on a | content-centric | design. |             |         |         |           |        |               |       |           |
|               |            |            |             |      |                 |         | researchers | modeled |         | the issue | as     | a distributed |       | partially |
| Subsequently, |            | a strategy | is proposed |      | for offloading  | network |             |         |         |           |        |               |       |           |
tasks that require high volume and expensive computation observable Markov decision process (Dec-POMDP). Dec-
POMDPisdesignedtomaximizethelatency-satisfiedutility
| in fog computing, |     | which | considers |     | both the computational |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ----- | --------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofalltheIoTdevices.Then,Lagrangianandpolicygradient
| workload | and | traffic volume. |     | The author | presented | a novel |     |     |     |     |     |     |     |     |
| -------- | --- | --------------- | --- | ---------- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
formulation that considers both resource constraints and methods were used to find a local optimal solution to the
givenoptimizationproblem.
| vehicle | mobility | with | the goal | of  | meeting traffic | vehicle |     |     |     |     |     |     |     |     |
| ------- | -------- | ---- | -------- | --- | --------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
offloadingrequirements.Subsequently,thetradeoffbetween
service latency and energy usage was addressed in edge 2) ADVANTAGEACTOR-CRITIC(A2C)
|     |     |     |     |     |     |     | The actor–critic |     | deep | reinforcement |     | learning | method | was |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---- | ------------- | --- | -------- | ------ | --- |
offloadingbyconcentratingonexecutionusageandresponse
latency. The author solved the suggested cost reduction first introduced in [128] to incorporate the core concept of
challengebydevisingtwoRL-basedalgorithms:thedynamic value-based and policy-based algorithms and concurrently
RLscheduling (DRLS) method and the deep dynamic predicttwosetsofparameters.A2Crequiresthedeployment
scheduling(DDS)method.TheauthorsproposedDDSbased of actors and critical networks. The actor is responsible for
on DQN and Double DQN. The results demonstrate that mappingstatestoactions,whereasthecriticisresponsiblefor
the proposed offloading method reduces service delay and mappingstate–actionpairstotheexpectedcumulativelong-
| energyconsumptionincomparisontothebaselineoffloading |     |     |     |     |     |     | termreward.                                       |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| schemes.                                             |     |     |     |     |     |     | Usingtheadvantageactor-critic(A2C)algorithmindeep |     |     |     |     |     |     |     |
An effective decision-making system was described in reinforcementlearning(DRL),theauthorof[129]presented
[125], which gives fog nodes the intelligence to choose an a joint optimization method for resource allocation and
appropriate algorithm for processing data. By combining offloadingstrategiestodecreasethedelayforcomputational
|     |     |     |     |     |     |     | tasks in | a fog | environment. |     | Multiple | action | dimensions |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ------------ | --- | -------- | ------ | ---------- | --- |
reinforcementlearningalgorithms(SARSAandQlearning)
into its architecture, Devote can adapt to the dynamic make the network convergence challenging. As a result,
environmentofIoT.Theselectionofanappropriatealgorithm this study employs a multi-agent strategy to obtain the
|          |        |                 |     |        |             |        | solution | by dividing | the | entire | offload | decision | action | into |
| -------- | ------ | --------------- | --- | ------ | ----------- | ------ | -------- | ----------- | --- | ------ | ------- | -------- | ------ | ---- |
| is based | on the | characteristics |     | of the | data, which | can be |          |             |     |        |         |          |        |      |
normal, critical, or too critical. To offload crucial data, multiple sub-actions. Besides, the paper [130] presents a
researchershaveproposedasecretary-basedonlinealgorithm collaborative approach for content caching, radio resource
toselecthemostsuitablefognode.Themobilityoffognodes allocation, and computing offloading in fog-enabled IoT,
and IoT devices is typical in various applications such as with the goal of reducing the overall delay for all service
vehiclenetworks.However,themobilityaspectisignoredin requests.Theythenusedamodel-freereinforcementlearning
thisstudy. framework to interact with the environment and choose the
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     |     | 12571 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
best course of action, which eliminated the requirement proposedstrategysuccessfullyaddressesthechallengesfaced
for a complete system evolution model. As a function by high-dimensional sequential states and action spaces.
approximator,aDNNisusedtoestimatethevaluefunctions Besides, [135] developed IIoT blockchain networks and
owing to the large number of possible system states and highlighted the use of RL approaches in IIoT blockchain
actions.Thestudyproposedanactor-criticdeepRLmethod networkssuchasPPO.
| to learn | the optimal |     | stochastic | policy for | radio resource |     |                     |     |     |     |
| -------- | ----------- | --- | ---------- | ---------- | -------------- | --- | ------------------- | --- | --- | --- |
|          |             |     |            |            |                |     | C. HYBRIDALGORITHMS |     |     |     |
allocation,contentcaching,andcomputingoffloading.With
the help of a critic, the actor represents a stochastically Value-basedandpolicy-basedalgorithmswerecombinedinto
ahybridalgorithm.Theirobjectivewastoimplementpolicy-
| parameterized | policy | with | another | DNN and | improves | the |                  |          |            |                   |
| ------------- | ------ | ---- | ------- | ------- | -------- | --- | ---------------- | -------- | ---------- | ----------------- |
|               |        |      |         |         |          |     | based algorithms | to model | the policy | function, whereas |
policy.
|     |     |     |     |     |     |     | updates to        | these policy functions | were    | based on value-    |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ---------------------- | ------- | ------------------ |
|     |     |     |     |     |     |     | based algorithms. | The DDPG               | and SAC | are typical hybrid |
3) PROXIMALPOLICYOPTIMIZATION(PPO)
algorithms.
| The PPO | is a | deep reinforcement |     | learning | method | based |     |     |     |     |
| ------- | ---- | ------------------ | --- | -------- | ------ | ----- | --- | --- | --- | --- |
on the A2C technique. PPO is an extension of the trust 1) DEEPDETERMINISTICPOLICYGRADIENT(DDPG)
region policy optimization (TRPO) approach, which has DDPG can be viewed as a combination of DQN and DPG
been successful [131], [132]. The TRPO incorporates a algorithms [136]. The primary network, target network,
novel objective function called the surrogate objective and and reply memory are the essential components of DDPG
a KL-divergence constraint known as a trusted region to networks. Both the primary and target networks consist of
enhance the efficiency of other previous policy gradient- twoneuralnetworks:actorandcritic.Theactornetworkwas
based reinforcement learning approaches. Because sudden used to investigate policies, whereas the critic network was
changesinthepolicycanresultininconsistentperformance, usedtoevaluatethepolicies.Thecriticnetworkalsoprovides
the trust region prevents TRPO from altering the decision- critical value for enhancing the policy gradient. The state-
making policy too frequently with each training period action pairs, associated rewards, and subsequent states are
update. However, computing the derivative of the KL- all stored in replay memory. These samples were chosen
divergence is difficult. By introducing a clipped substitute randomlybytheagentduringtrainingtominimizetheimpact
objectivefunction,PPOovercamethisTRPOissue.Because ofthedatacorrelation.
theobjectivefunction’sclippingrestrictsthepolicy’sability Intheliterature,theDDPGapproachhasbeenutilizedto
to alter, the PPO can be trained without a trusted region, tackle several optimization problems related to offloading
which uses fewer computations than TRPO. Compared to computations in fog. For example, a fog-based vehicle
other DRL algorithms, the DQN method as an example, architecture with computational offloading and service
performswellontheproblemofcontinuousaction.Interms caching was developed in [137]. Peer-pool and fog-pool
ofsamplecomplexity,italsoperformsbetterthanA2Candis computationcooperationwereusedinthisdesigntoimprove
similartoACER,althoughitismuchsimpler.ThePPOcan efficiency. To minimize long-term energy utilization and
also be expanded by adding more workers to accelerate the taskprocessingtime,anoptimizationproblemisdefinedfor
training. combiningcomputationoffloadingwithservicecaching.The
|           |       |            |     |               |              |     | DDPG algorithm | was used | to find an optimal | solution to |
| --------- | ----- | ---------- | --- | ------------- | ------------ | --- | -------------- | -------- | ------------------ | ----------- |
| The study | [133] | formulated |     | the challenge | of assigning |     |                |          |                    |             |
limited fog resources to vehicular applications with the the optimization problem. In addition, [138] presented an
goal of minimizing service delays using parked vehicles. intelligent computation offloading technique with resources
Then, a heuristic technique is presented to efficiently find toenhancethecooperativeprocessingefficiencyoffognodes
solutions to the problem. To further improve resource and improve the user service experience. First, the authors
allocation,theproposedmethodiscombinedwiththePPO’s of the papers formulated an energy consumption reduction
utilizeddataonparkingstatusandvehiclemovementinthe issue for all computer workloads that considers offloading
city’s smart environment. Moreover, [134] formulated an decisions, transmission power, and bandwidth resources.
unmannedaerialvehicles(UAV)-assistedoffloadingproblem Moreover, a (D3PG-ICO) algorithm based on DDPG is
proposedtosolvetheformulatedproblem.Therecommended
| for IoT | to jointly | reduce | the | queue length | and | energy |     |     |     |     |
| ------- | ---------- | ------ | --- | ------------ | --- | ------ | --- | --- | --- | --- |
consumption in smart buildings and environments. The technique creates two separate critic networks to better
control decisions include evaluating whether IoT device constructthebestglobalcomputationoffloadingpolicy,and
adiscretizationoperationthatincludescontinuousvariables
| tasks should | be  | offloaded | or processed | locally | as  | well as |     |     |     |     |
| ------------ | --- | --------- | ------------ | ------- | --- | ------- | --- | --- | --- | --- |
allocating time resources and bandwidth to IoT devices is incorporated to improve the randomness of the policy
attached to the UAV. This was reformulated as an MDP- exploration. Finally, the simulation results demonstrate that
|     |     |     |     |     |     |     | the proposed | system is reliable | and that | the policy for |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------ | -------- | -------------- |
basedoffloadingproblem.Toachieveabalancebetweenthe
two conflicting optimization objectives of queue length and reducingpowerconsumptionbyoffloadingcomputationscan
energyusage,theauthorincorporatedbothobjectivesintoa beimplementedquicklyandflexibly.
Inaddition,alearning-basedmobilefogschemetooffload
| single reward | function. |     | The UTO | approach-based | PPO | was |     |     |     |     |
| ------------- | --------- | --- | ------- | -------------- | --- | --- | --- | --- | --- | --- |
designedtoaddresstheissueofUAV-assistedoffloading.The codeblocksinIoTwasproposedinaresearcharticle[142],
proposed method can effectively solve problems faced by that maximizes the use of idle edge computing and storage
high-dimensional consecutive state and action spaces. The resources. Offloading state sets are modeled as Markov
| 12572 |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
decision processes (MDPs) and the DDPG algorithm to first. In terms of offloading delay and task completion rate,
address the problem of state space explosion and identify it outperformed conventional algorithms. Similarly, astudy
an optimal policy for offloading code blocks in different [142]suggestedaSAC-basedDRLalgorithmtoaddressthe
contexts.Besides,[139]investigatedtheproblemofjointtask issue of V2V partial computation offloading in vehicular
partitioning and power control in a fog computing network fogcomputing,inwhichvehicleswithinadequatecomputing
with various mobile devices (MDs) and fog devices (FDs), capabilitiescanoffloadpartoftheiroffloadingtaskstonearby
whereeachMDmustaccomplishaperiodiccomputingtask vehicleswithidlecomputingresources.
under the restrictions of latency and power consumption. In [143] the problem of joint energy and task offloading
To satisfy the latency and power consumption restrictions, in UAV-aided 6G intelligent edge networks was discussed,
the tasks of each MD can be divided into subtasks and where each UAV can offload part of its energy and task to
performedincollaborationwiththeFDs.Tosatisfytheenergy theFCNstodecreasetheamountofpowerusedlocallyand
consumption and delay limitations, the tasks of each MD thetimeittakestocompletetheentiretaskbyimplementing
can be divided into subtasks simultaneously performed by SWIPT.Theauthorsformulatedtheproblemasacooperative
the MD and the FDs. The solution to this issue was a task multi-agent Markov game for UAVs with the objective of
offloadingalgorithmbasedonMADDPG,whichdetermines maximizingthetotalsystemutilitybyoptimizingthepower
the task partitioning and transmission power technique for allocation strategies and task partitioning of each UAV
eachMDtooptimizetheperformanceofthesysteminterms with respect to energy consumption, task size, and average
of power consumption and processing delay. Finally, the latencyduringtheexecutionoftasks,takingintoaccountthe
study [140] offers a resource allocation and task offloading networkdynamics.Amulti-agentsoftactor–critic(MASAC)
approachisproposedtosolvetheproblemformulation.
systembasedonblockchain.Theauthorsbeganbyexamining
both direct and indirect trust using a subjective logical To sum up, the core difference between the value-based
aggregation methodology and distributed trust assessment and the policy-based approaches is that in the value-based
approachesapproachesusetemporaldifference(TD)learning
method.Theresearchersexamineddifferentqualityofservice
features and created a smart contract that uses a DRL to approximate the value function rather than learning
algorithm called DDPG to maximize fog revenue while the policy explicitly [78]. In contrast, the policy-based
approacheslearnthe‘policy’directlywithoutrelyingonthe
meetingthemaximumnumberofuserrequests.Blockchain
facilitatestheentireprocedure,fromtaskgenerationtoresult value function [80]. This method explicitly builds a policy
computation, and all task transactions are recorded in a (mapping π:s→a) representation and maintains it in the
|     |     |     |     |     |     |     |     | memory | during the | learning | process. | Another | distinction |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | -------- | -------- | ------- | ----------- | --- |
secure,unchangeable,tamper-resistantledger
|     |     |     |     |     |     |     |     | between    | the value-based     | approaches |            | and the | policy-based |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------- | ---------- | ---------- | ------- | ------------ | --- |
|     |     |     |     |     |     |     |     | approaches | is that value-based |            | approaches |         | are suitable | for |
2) SOFTACTOR-CRITIC(SAC)
|     |     |     |     |     |     |     |     | scenarios | with small | and | discrete | action-space. | Whereas |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | -------- | ------------- | ------- | --- |
SACisaDRLalgorithmbasedonanoff-policyA2Cmodel
|               |                  |     |          |     |                  |     |     | policy -based | approaches     |     | are more       | suited | for scenarios  |     |
| ------------- | ---------------- | --- | -------- | --- | ---------------- | --- | --- | ------------- | -------------- | --- | -------------- | ------ | -------------- | --- |
| that provides | sample-efficient |     | learning |     | while preserving |     | the |               |                |     |                |        |                |     |
|               |                  |     |          |     |                  |     |     | with large    | and continuous |     | action spaces. |        | The advantages |     |
advantagesofentropyandstabilityoptimization[144],[145].
|                |           |               |              |          |              |               |        | of policy-based | approaches    |             | over value-based |     | approaches |        |
| -------------- | --------- | ------------- | ------------ | -------- | ------------ | ------------- | ------ | --------------- | ------------- | ----------- | ---------------- | --- | ---------- | ------ |
| The primary    | principle | behind        | SAC          | is to    | utilize      | all available |        |                 |               |             |                  |     |            |        |
|                |           |               |              |          |              |               |        | are that        | they have     | superior    | convergence      |     | properties | and    |
| actions to     | optimize  | the actor’s   | entropy      |          | and expected |               | reward |                 |               |             |                  |     |            |        |
|                |           |               |              |          |              |               |        | are efficient   | in continuous |             | action spaces    |     | or high    | dimen- |
| while ensuring |           | task success. |              | This can | be           | accomplished  |        |                 |               |             |                  |     |            |        |
|                |           |               |              |          |              |               |        | sionality       | [146]. The    | value-based | reinforcement    |     | method     | has    |
| by integrating |           | entropy       | maximization |          | with the     | goal          | of a   |                 |               |             |                  |     |            |        |
|                |           |               |              |          |              |               |        | the advantages  | of simplicity |             | and efficiency.  |     | On the     | other  |
stochasticactor.SACismoresuitablethanothervalue-based
hand,policy-basedevaluationhasthedisadvantageofbeing
| DRL algorithms, |     | DQN | and double | DQN | as  | examples, | for |     |     |     |     |     |     |     |
| --------------- | --- | --- | ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
inefficientandhavingahighvariance.Sincebothcategories
| the allocation |         | of vehicular | tasks     | under | fluctuating |          | traffic |            |                |     |                    |     |            |     |
| -------------- | ------- | ------------ | --------- | ----- | ----------- | -------- | ------- | ---------- | -------------- | --- | ------------------ | --- | ---------- | --- |
|                |         |              |           |       |             |          |         | have their | own advantages |     | and disadvantages, |     | Therefore, |     |
| volumes        | because | it is more   | effective | at    | handling    | problems |         |            |                |     |                    |     |            |     |
hybridapproachesworkbasedonthecombinationofvalue-
| with high-dimensional |     | action         | space.    | In  | addition, | the | SAC    |           |              |            |     |           |           |     |
| --------------------- | --- | -------------- | --------- | --- | --------- | --- | ------ | --------- | ------------ | ---------- | --- | --------- | --------- | --- |
|                       |     |                |           |     |           |     |        | based and | policy-based | algorithms |     | that take | advantage | of  |
| can investigate       |     | more effective | solutions |     | by adding | a   | policy |           |              |            |     |           |           |     |
bothcategories.
| entropy | measure        | to the | reward | structure. | If many |      | optimal |     |     |     |     |     |     |     |
| ------- | -------------- | ------ | ------ | ---------- | ------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
| options | are available, | the    | SAC    | strategy   | selects | each | option  |     |     |     |     |     |     |     |
with equal probability. Compared with other policy-based VI. ANALYTICALDISCUSSION
DRL algorithms, such as A3C and DDPG, SAC is more Existing research utilizing RL or DRL techniques for
robustandsample-efficient,makingitsimplertoimplement handling offloading problems in fog computing has been
improvements in a stochastic vehicular environment. For critically analyzed according to the research questions
example, the work in [13] proposed a DRL method based highlighted in section IV-A. The discussion is provided as
| on SAC | to handle | the | task allocation |     | problem | to  | adjust | follows. |     |     |     |     |     |     |
| ------ | --------- | --- | --------------- | --- | ------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- |
the offloading policy to changes in a dynamic vehicular Fig. 5, a two-level pie chart depicts the percentages
environment. The proposed approach becomes more robust of research articles from the various conferences and
and generalized by integrating the policy entropy measure journals of different publishers that were studied in this
intothereward.Basedonthesimulationresults,theproposed comprehensivereviewoftheliterature.Thepiechart’sinner
scheme ensured that high-priority tasks were performed circle demonstrates that 72% of the research publications
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     |     | 12573 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
TABLE4. Side-by-sidecomparisonRLandDRLmethodsforsolvingoffloadingproblemsinfog.
on offloading mechanisms based on RL+DRL algorithms are presented at conferences. The outer circle depicts the
in the Fog paradigm are published in journals, and 28% many publishers considered for publication of the research
12574 VOLUME11,2023

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
TABLE4. (Continued.)Side-by-sidecomparisonRLandDRLmethodsforsolvingoffloadingproblemsinfog.
VOLUME11,2023 12575

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
TABLE4. (Continued.)Side-by-sidecomparisonRLandDRLmethodsforsolvingoffloadingproblemsinfog.
publications. The majority of these research articles were (28%).Ontheotherhand,18%,9%,and9%werepublished
published by IEEE in both journals (36%) and conferences inScienceDirect,Wiley,andSpringerrespectively.
12576 VOLUME11,2023

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
TABLE4. (Continued.)Side-by-sidecomparisonRLandDRLmethodsforsolvingoffloadingproblemsinfog.
VOLUME11,2023 12577

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
FIGURE7. PercentageofRLandDRLmethodsusedinfogsystem
offloadingmechanism.
FIGURE5. Percentageofjournals,conferences,andresearchpaper
publishersreviewed.
FIGURE8. Percentageofperformancemetricsforassessingoffloading
mechanism.
FIGURE6. PercentageofRLandDRLmethodsusedinfogsystem
offloadingbasedonmodefreecategorization. Inaddition,9%and7%ofarticlesusedDDPGandDRQN,
respectively. On the other hand, SARSA (2%), PG (2%),
RQ1: What categorization can be applied to RL or DRL and combining methods (SARSA+Q learning (2%), DQN
basedoffloadingmechanismsinfogcomputing? +Double (2%)) are less-used methods. Additionally, the
According to the proposed taxonomy, Fig. 6 presents a utilized method of offloading mechanisms makes moderate
statistical comparison of the offloading mechanisms based use of the RL and DRL methods: SAC (5%), PPO (5%),
on the RL and DRL approaches for fog. Based on the doubleDQN(5%),A2C(4%),andduelingDQN(4%).
taxonomy,RLandDRLalgorithmsareorganizedintothree RQ3:WhichtypicalperformancemetricsareutilizedinRL
main categories, namely, value-based algorithms, policy orDRL-basedoffloadingtechniquesinfogcomputing?
algorithms, and hybrid algorithms As it is illustrated, 62% Fig. 8 shows the percentage of performance metrics
of the selected articles belong to the value-based approach utilized to assess the offloading mechanisms based on
category. The policy-based approach ranks second with a different RL and DRL algorithms. It can be concluded
29% coverage rate. In addition, only 9% of the reviewed from the figure that latency (46%) and energy (32%),
articleswerededicatedtohybridtechniques. respectively, are two of the most popular metrics used to
RQ2: Which types of algorithms are utilized by RL or evaluate offloading strategies. On the other hand, security
DRL-basedoffloadingmechanismsinfogsystems? (3%),QoE+QoS(3%),responsetime(1%),reliability(1%),
Fig. 7 shows the percentage of RL and DRL algorithms and cost (1%) are less-used parameters. Additionally, the
utilized for solving offloading problems in fog computing. evaluation of offloading mechanisms makes moderate use
Based on proposed taxonomy and the aforementioned of the following parameters: resource utilization (6%),
research articles, DQN is the most popular algorithm with throughput(5%),andscalability(5%).
32% usage. As it is illustrated, 21% of the research papers RQ4: What cases are studies considered in RL or DRL-
have used Q learning for their proposed offloading schema. basedoffloadingtechniquesinthefogparadigm?
12578 VOLUME11,2023

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
FIGURE9. Percentageofcasestudydistributionbasedonoffloading
mechanism.
FIGURE11. Percentageofoffloadingmodesusedinfogsystem
offloadingmechanism.
FIGURE12. Percentageofoffloadingdirectioninthefogsystem
offloadingmechanism.
FIGURE10. Percentageofevaluationtoolsforevaluatingoffloading
mechanism.
methods. The pie chart’s inner circle shows the percentage
Fig.9showsthepercentageofcasestudiesconsideredin of tools used for evaluating offloading strategies, including
the RL and DRL approach-based offloading mechanisms in simulation environments (41%), programming languages
thefogsystem.Thefollowingareexamplesofexistingcase (13%), and hybrid approaches (SE+PL and SE+SE) (7%),
studies that were utilized in the experiment results: general and others (39%). In contrast, the outer circle shows
apps, vehicular networks, industrial applications, fog radio that 20% of articles evaluated their proposed approaches
access (F-RAN), unmanned aerial vehicles (UAV), smart using TensorFlow under the simulation category. Besides,
city applications, smart surveillance applications, health PureEdgeSim, iFogSim, and Pytorch simulations have the
care, smart factories, green industry, and smart mobile samepercentageof4%.Othersimulationtools,suchasEdgex
applications. It concludes from the figure that case studies Mobile, Pycharm,NS-3,Mininet, Mininet-Wifi, and Monte-
onvehicularnetworks,generalapps,andF-RANshavebeen Carloalsohavethesamepercentageof2%.Furthermore,9%
implemented by 34%, 32%, and 11% of the research arti- ofthestudiesusedMATLAB,and4%oftheresearcharticles
cles, respectively. The application areas such as UAV(5%), utilized Python, both of which fall under the programming
green industrial(4%), smart city application(3%), industrial language category. In addition to these, approximately 7%
applications(2%),smartsurveillanceapplication(2%),health of research papers have used a hybrid approach to assess
care(2%), smart factory(2%), and smart mobile applica- the various offloading techniques. In about 39% of the
tion(2%)arerarelyexplored. publications,noevaluationtoolwasspecifiedorreported.
RQ5:WhichtoolsareusedtoevaluateRLorDRLbased RQ6: Which offloading modes are applied in RL or
mechanismsforoffloadinginfogsystems? DRL-basedoffloadingtechniquesinthefogparadigm?
Fig. 10 illustrates several tools utilized for the evaluation Fig. 11 shows the offloading mode used for the imple-
of offloading mechanisms based on different RL and DRL mentation of an offloading mechanism based on different
VOLUME11,2023 12579

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
|     |     |     |     |     |     |     |     | FIGURE15. | Percentageofstudiesbasedonoffloadingproblem |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
formulation.
RQ9:IsSDNincorporatedintotheirstrategybasedonRL
orDRL-basedoffloadingmechanismsinfogcomputing?
Fig.14showsthat86%ofthereviewedpapersdidnotuse
SDNintheiroffloadingschemaarchitecture,wheras14%of
| FIGURE13. | Percentageofdecisionswasmadeinfogsystemoffloading |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theresearcharticlesdiduseSDNintheiroffloadingstrategy
mechanism.
architecture.
RQ10:Howmanystudieshaveformulatedtheiroffloading
strategyproblemasanMDPorPOMDPproblemandsolved
itbasedonRLorDRLapproachesinafogenvironment?
|     |     |     |     |     |     |     |     | Fig. 15          | shows        | that the | RL or  | DRL        | method | was         | used in |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------ | -------- | ------ | ---------- | ------ | ----------- | ------- |
|     |     |     |     |     |     |     |     | 66% of           | the research | papers   | to     | solve the  | MDP    | formulation |         |
|     |     |     |     |     |     |     |     | problem.         | Besides,     | 9%       | of the | research   | papers | developed   |         |
|     |     |     |     |     |     |     |     | their offloading |              | strategy | under  | the POMDP. |        | Also,       | 25% of  |
researchstudiesusedmathematicalornon-linearproblemsto
formulatetheiroffloadingstrategies,ortheyusedRLorDRL
| FIGURE14. | ThepercentageofresearcharticlesusingornotusingSDNin |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
methodsintheiroffloadingstrategiesfordifferentpurposes,
theiroffloadingstrategyarchitecture.
|     |     |     |     |     |     |     |     | such as | finding | the shortest | route | or choosing |     | the | best fog |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------------ | ----- | ----------- | --- | --- | -------- |
candidate.
RLandDRLapproaches.Thepiechart’sinnercircleshows
| the percentage | of        | modes        | used for   | implementing |        | offloading |         |                                |            |      |               |          |        |           |      |
| -------------- | --------- | ------------ | ---------- | ------------ | ------ | ---------- | ------- | ------------------------------ | ---------- | ---- | ------------- | -------- | ------ | --------- | ---- |
|                |           |              |            |              |        |            |         | VII. OPENISSUESANDFUTURETRENDS |            |      |               |          |        |           |      |
| strategies,    | including | binary       | offloading |              | (80%)  | and        | partial |                                |            |      |               |          |        |           |      |
|                |           |              |            |              |        |            |         | This review                    | indicates  | that | some          | critical | issues | regarding |      |
| offloading     | (20%).    | In contrast, |            | the outer    | circle | shows      | that,   |                                |            |      |               |          |        |           |      |
|                |           |              |            |              |        |            |         | offloading                     | techniques | in   | fog computing |          | have   | not yet   | been |
inthepartialoffloadingcategory,authorsof11%ofresearch
|          |           |        |              |     |              |     |       | researched. | To  | address RQ11, | this | section | discusses |     | several |
| -------- | --------- | ------ | ------------ | --- | ------------ | --- | ----- | ----------- | --- | ------------- | ---- | ------- | --------- | --- | ------- |
| articles | have used | static | partitioning |     | to implement |     | their |             |     |               |      |         |           |     |         |
openresearchissues.
proposedoffloadingschema,whileauthorsof9%ofresearch
articleshaveuseddynamicpartitioning.
|     |     |     |     |     |     |     |     | A. SECURITY |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
RQ7:WhatoffloadingdirectionisusuallyappliedinRLor
DRL-basedoffloadingtechniquesinfogareas? One of the significant challenges in modern technology
|            |                  |               |            |             |          |                |        | is finding        | ways    | to make     | the       | system   | more           | robust        | and  |
| ---------- | ---------------- | ------------- | ---------- | ----------- | -------- | -------------- | ------ | ----------------- | ------- | ----------- | --------- | -------- | -------------- | ------------- | ---- |
| Fig. 12    | shows            | a statistical | comparison |             | of       | the offloading |        |                   |         |             |           |          |                |               |      |
|            |                  |               |            |             |          |                |        | secure            | against | phishers.   | When      | it comes | to             | offloading    | in   |
| direction  | applied          | in the        | RL         | and DRL     | approach |                | based  |                   |         |             |           |          |                |               |      |
|            |                  |               |            |             |          |                |        | fog environments, |         | massive     | amounts   | of       | data           | are generated |      |
| offloading | mechanisms       | in            | the fog    | system.     | Three    | offloading     |        |                   |         |             |           |          |                |               |      |
|            |                  |               |            |             |          |                |        | from multiple     |         | interacting | IoT       | smart    | devices.       | This          | data |
| directions | were considered: |               | vertical,  | horizontal, |          | and            | hybrid |                   |         |             |           |          |                |               |      |
|            |                  |               |            |             |          |                |        | must be           | moved   | to the      | fog/cloud | layer    | for processing |               | and  |
flows.Theverticaloffloadingmodehasthehighestpercent-
storage.However,users’devicesmightmistakenlysendtheir
| age of 55% | usage     | in the | literature. | The       | hybrid | offloading |     |               |     |             |             |          |     |            |       |
| ---------- | --------- | ------ | ----------- | --------- | ------ | ---------- | --- | ------------- | --- | ----------- | ----------- | -------- | --- | ---------- | ----- |
|            |           |        |             |           |        |            |     | computations  |     | or data to  | neighboring |          | fog | servers,   | which |
| mode, on   | the other | hand,  | comes       | in second | place, | with       | 43% |               |     |             |             |          |     |            |       |
|            |           |        |             |           |        |            |     | have probably |     | been hacked | by          | a number | of  | attackers, | and   |
usage.Finally,with2%usage,thehorizontaloffloadingmode
|     |     |     |     |     |     |     |     | hence generate |     | serious | security | concerns. |     | Thus, | security |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | -------- | --------- | --- | ----- | -------- |
hadthelowestrankingpercentage.
|     |     |     |     |     |     |     |     | issues regularly |     | impact | network | performance |     | and | energy |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ------- | ----------- | --- | --- | ------ |
RQ8:Whichoffloadingdecisionsaremadewithrespectto
efficiencywhenmultipleoverloadedfogandedgenodesare
| what, where, | when, | and | how are | decisions | in  | their strategy |     |     |     |     |     |     |     |     |     |
| ------------ | ----- | --- | ------- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
considered.Theremaybeaneedforfurtherinvestigationinto
basedonRLorDRL-basedoffloadingtechniquesinthefog
|     |     |     |     |     |     |     |     | smart enterprise |     | security | provisioning. |     | It is | recommended |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | ------------- | --- | ----- | ----------- | --- |
area?
|         |       |          |          |     |              |          |     | that blockchain |     | technology | be integrated |     | into | the proposed |     |
| ------- | ----- | -------- | -------- | --- | ------------ | -------- | --- | --------------- | --- | ---------- | ------------- | --- | ---- | ------------ | --- |
| Fig. 13 | shows | that the | majority | of  | the research | articles |     |                 |     |            |               |     |      |              |     |
strategytoimprovethesystemsecurity.
addressedquestionsregardingwhere/when,where/when/how
| and what/where/when |     | questions |       | by   | 30%, | 29%and | 25%,  |             |     |     |     |     |     |     |     |
| ------------------- | --- | --------- | ----- | ---- | ---- | ------ | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| respectively.       | On  | the other | hand, | 11%, | 3%,  | and    | 2% of | B. MOBILITY |     |     |     |     |     |     |     |
decisionsweremaderegardingwhere,what/where/when/how, The offloading scope of a fog environment faces additional
|     |     |     |     |     |     |     |     | obstacles | because | of its | mobility. | Important |     | obstacles | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------ | --------- | --------- | --- | --------- | --- |
andwhere/howquestions.
| 12580 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
mobility include dynamism and lack of communication. proliferationofrequests.Thisrequiresdynamicandefficient
Because mobile devices with naturally dynamic behaviour resourceauto-scalingtooptimallydistributefogresourcesto
can move quickly between locations, these devices may the requests. A lack of fog resources can lead to a problem
need to relocate their dedicated servers across a large knownas‘‘Over-Provisioning’’,whereasanabundanceoffog
geographic area. To solve this issue, a strong mobility resourcescanleadto‘‘Under-Provisioning’’[147].Notably,
management approach must be implemented such that only a small percentage of the examined studies provided
devices can continue to communicate with the fog server an approach in this regard. Thus, it is essential to study
evenafterleavingthesourcelocation.Additionally,mobility effectiveauto-scalingtohandlefluctuatingworkloadsinfog
poses considerable challenges in several research domains, environments.
| including | vehicular | networks |     | and unmanned |     | aerial | vehicles |     |     |     |     |     |     |     |     |
| --------- | --------- | -------- | --- | ------------ | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
(UAV).Themobilityofthedevicecanimpacttheoffloading
|             |     |        |     |         |        |        |          | F. FINDINGOPTIMALPOLICYFORCANDIDATEFOG |     |     |     |     |     |     |     |
| ----------- | --- | ------ | --- | ------- | ------ | ------ | -------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| performance | and | cannot | be  | ignored | in the | stated | domains. |                                        |     |     |     |     |     |     |     |
SELECTION
| For instance, |           | a device   | needs          | to select    | a          | new fog  | server     |                     |         |              |          |                    |           |          |          |
| ------------- | --------- | ---------- | -------------- | ------------ | ---------- | -------- | ---------- | ------------------- | ------- | ------------ | -------- | ------------------ | --------- | -------- | -------- |
|               |           |            |                |              |            |          |            | Major contributions |         | provide      |          | a wide             | range     | of       | network  |
| to offload    | the       | task again | if             | it leaves    | the        | existing | service    |                     |         |              |          |                    |           |          |          |
|               |           |            |                |              |            |          |            | architectures       | as      | well as      | a number | of                 | different | criteria | for      |
| scope before  | receiving |            | the offloading |              | result.    | This     | results in |                     |         |              |          |                    |           |          |          |
|               |           |            |                |              |            |          |            | action selection.   |         | For example, |          | choosing           | the       | most     | powerful |
| an increased  | latency.  |            | Therefore,     | new          | approaches |          | must be    |                     |         |              |          |                    |           |          |          |
|               |           |            |                |              |            |          |            | computing           | devices | to           | offload  | resource-intensive |           | tasks,   | and      |
| developed     | to solve  | these      | problems       | efficiently. |            | Despite  | their      |                     |         |              |          |                    |           |          |          |
choosingtheshortestpathforoffloading.Therefore,finding
| significance, | mobility |           | difficulties | in     | fog contexts |             | have not |          |          |            |          |          |       |           |       |
| ------------- | -------- | --------- | ------------ | ------ | ------------ | ----------- | -------- | -------- | -------- | ---------- | -------- | -------- | ----- | --------- | ----- |
|               |          |           |              |        |              |             |          | the best | policy   | that meets | multiple | goals    | and   | is robust | is an |
| received      | adequate | attention |              | in fog | environment  | literature. |          |          |          |            |          |          |       |           |       |
|               |          |           |              |        |              |             |          | area of  | research | that has   | not      | yet been | fully | explored  | and   |
| In addition,  | fog      | node      | selection    | during | offloading   |             | depends  |          |          |            |          |          |       |           |       |
remainsopen.
| on the | location | of the | mobile | device, | which | remains | a   |     |     |     |     |     |     |     |     |
| ------ | -------- | ------ | ------ | ------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
challengingproblem.
|     |     |     |     |     |     |     |     | G. OFFLOADINGMODELINGWITHSDNTECHNOLOGY |     |               |     |          |        |         |      |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | ------------- | --- | -------- | ------ | ------- | ---- |
|     |     |     |     |     |     |     |     | SDN integrated                         |     | fog computing |     | is still | in its | infancy | when |
C. MULTI-OBJECTIVEMECHANISMS
|               |     |            |         |       |     |               |     | it comes | to offloading |     | computation, | and | additional |     | research |
| ------------- | --- | ---------- | ------- | ----- | --- | ------------- | --- | -------- | ------------- | --- | ------------ | --- | ---------- | --- | -------- |
| Most existing |     | offloading | studies | based | on  | reinforcement |     |          |               |     |              |     |            |     |          |
learning methodsin thefog paradigm considersingle orbi- is needed to address several open challenges, particularly
inoffloadingmodeling.Forbothdistributedandcentralized
objectivesintheirdesign.Toaddressthepressingproblemsin
|     |     |     |     |     |     |     |     | SDNs, offloading |     | models | can | be created |     | based | on new |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | --- | ---------- | --- | ----- | ------ |
fogcomputing,includingtaskallocation,jobschedulingand
offloading, resource provisioning, clustering, cache place- characteristics such as the timeliness of the collected
information.
ment,andloadbalancing,designingoptimizationmodelsthat
| jointly optimize |           | multiple | objectives |           | (energy    | consumption, |     |                           |     |     |     |     |     |     |     |
| ---------------- | --------- | -------- | ---------- | --------- | ---------- | ------------ | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
| delay, cost,     | capacity, |          | task       | execution | stability, | trust        | and |                           |     |     |     |     |     |     |     |
|                  |           |          |            |           |            |              |     | H. OFFLOADINGPARTITIONING |     |     |     |     |     |     |     |
mobility, and bandwidth reliability) will be an interesting Offloadingpartitioningreferstotheamountofcodethatmust
researchtopicinthefuture.Atthesametime,otherobjectives
beoffloadedandrunremotelytoincreasetheeffectivenessof
| were overlooked, |     | such | as scalability, |     | availability, |     | capacity, |          |         |             |              |     |     |                |     |
| ---------------- | --- | ---- | --------------- | --- | ------------- | --- | --------- | -------- | ------- | ----------- | ------------ | --- | --- | -------------- | --- |
|                  |     |      |                 |     |               |     |           | resource | or time | constrained | applications |     | in  | fog computing. |     |
security,bandwidth,trust,mobility,andcost.Otherrelevant There are two different types of computational offloading:
| obstacles | to this | unresolved |             | problem | include | the         | trade-off |             |          |         |            |     |           |         |        |
| --------- | ------- | ---------- | ----------- | ------- | ------- | ----------- | --------- | ----------- | -------- | ------- | ---------- | --- | --------- | ------- | ------ |
|           |         |            |             |         |         |             |           | binary and  | partial. | Binary  | offloading |     | is widely | used    | in the |
| between   | several | different  | objectives, |         | which   | will become | an        |             |          |         |            |     |           |         |        |
|           |         |            |             |         |         |             |           | literature, | whereas  | partial | offloading |     | is weakly | covered | in     |
interestingtopicforadditionalresearch. the literature. Nevertheless, in practice, task partitioning
|     |     |     |     |     |     |     |     | is essential  | in  | some     | applications, |     | including | 3D      | gaming |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ------------- | --- | --------- | ------- | ------ |
|     |     |     |     |     |     |     |     | audio, video, |     | and face | recognition,  |     | which     | require | more   |
D. IMPLEMENTATIONCHALLENGES
energyandresourcesthanexistingdevices.Binaryoffloading
Itisessentialtoimplementtheproposedoffloadingstrategies
|                   |          |     |        |             |         |              |       | is simpler       | to         | implement    | and     | ideal   | for simple |     | tasks that |
| ----------------- | -------- | --- | ------ | ----------- | ------- | ------------ | ----- | ---------------- | ---------- | ------------ | ------- | ------- | ---------- | --- | ---------- |
| in real           | networks | to  | ensure | that        | the QoS | requirements |       |                  |            |              |         |         |            |     |            |
|                   |          |     |        |             |         |              |       | cannot be        | segmented, |              | whereas | partial | offloading |     | increases  |
| are satisfied.    | However, |     | it is  | challenging |         | to conduct   | real- |                  |            |              |         |         |            |     |            |
|                   |          |     |        |             |         |              |       | the fog server’s |            | capabilities | but     | makes   | offloading |     | modeling   |
| world experiments |          | in  | a fog  | computing   | context | because      | of    |                  |            |              |         |         |            |     |            |
considerablycomplex.
| implementation |     | time and | high | cost. | Therefore, | only | a few |     |     |     |     |     |     |     |     |
| -------------- | --- | -------- | ---- | ----- | ---------- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
selectedpublicationshavevalidatedtheproposedoffloading
mechanismsbasedonareal-testbedtechnique.Todate,there
|     |     |     |     |     |     |     |     | I. OFFLOADINGLARGE-SCALENETWORKS |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
is no dedicated fog computing testbed to assist researchers Fog network offloading techniques for large-scale areas are
intestingtheirconcepts,designs,prototypes,anddistributed
|     |     |     |     |     |     |     |     | difficult | to solve. | The | first problem |     | is that | a wide | network |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ------------- | --- | ------- | ------ | ------- |
algorithmsinrealisticfogcomputingsituations.
|     |     |     |     |     |     |     |     | significantly | increases |          | the complexity |           | of  | all offloading |          |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | -------- | -------------- | --------- | --- | -------------- | -------- |
|     |     |     |     |     |     |     |     | model types,  |           | which in | turn           | increases | the | time           | required |
E. WORKLOADPREDICTIONINFOG(OFFLOADING to make an offloading decision and the overall offloading
PREDICTION) delay.Reinforcementlearningisacentralizedapproachthat
|          |           |     |         |           |     |            |     | makes it | difficult | to collect | information. |     | The | gathering | of  |
| -------- | --------- | --- | ------- | --------- | --- | ---------- | --- | -------- | --------- | ---------- | ------------ | --- | --- | --------- | --- |
| Managing | resources | for | various | workloads |     | is crucial | in  |          |           |            |              |     |     |           |     |
fog environments because of the large volume and rapid information on a large-scale network may lead to network
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 12581 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
overload and contravene the real-time offloading decision hasthepotentialtoenhancetheperformanceofanapplication
requirements. This is due to the fact that the decision and minimize the overall latency by transferring intensive
is made after all the necessary information has been tasks from resource-limited user devices to a resource-rich
gathered, and the amount of time it takes to complete this fog or cloud server. This paper presents a systematic and
procedure is not insignificant. In addition, some of the comprehensive research analysis of offloading mechanisms
mostpromisingoffloadingtechniquesforfognetworksmust based on the RL and DRL methods in a fog computing
| operate | efficiently | on  | small-scale | networks |     | with a | certain | environment. |     |     |     |     |     |     |     |
| ------- | ----------- | --- | ----------- | -------- | --- | ------ | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
number of user devices. However, the reliability of these By applying our search techniques, 56 research articles
mechanisms cannot be guaranteed in a large-scale context. wereselectedforthefinalselection.AccordingtoRQ1,the
Hence, offloading mechanisms on fog networks for large- applied RL or DRL algorithms based on offloading mecha-
scaleareaswillbepursuedinthefuture. nismsinfogcomputingcanbeclassifiedintothreecategories:
|     |     |     |     |     |     |     |     | value-based, | policy-based, |     | and | hybrid-based |     | algorithms. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | --- | ------------ | --- | ----------- | --- |
J. HETEROGENEITYANDINTEROPERABILITY These categories are then compared based on important
|              |     |             |         |     |            |     |        | features, | including | offloading |     | problem | formulation, |     | utilized |
| ------------ | --- | ----------- | ------- | --- | ---------- | --- | ------ | --------- | --------- | ---------- | --- | ------- | ------------ | --- | -------- |
| The majority |     | of existing | studies | on  | offloading |     | models |           |           |            |     |         |              |     |          |
considercomputationtaskstobehomogeneous.Thismakes techniques, performance metrics, evaluation tools, case
the modeling of the offloading procedure easier. However, studies,theirstrengthsanddrawbacks,offloadingdirections,
|                |            |       |                |     |              |          |     | offloading | mode, | SDN | based | architecture, |     | and offloading |     |
| -------------- | ---------- | ----- | -------------- | --- | ------------ | -------- | --- | ---------- | ----- | --- | ----- | ------------- | --- | -------------- | --- |
| many different |            | tasks | are involved   |     | in practice. | Examples |     |            |       |     |       |               |     |                |     |
| include        | preemptive | and   | non-preemptive |     | tasks.       | Modeling | is  | decisions. |       |     |       |               |     |                |     |
extremely challenging owing to the diversity of tasks. It is According to RQ2, DQN and Q learning were the most
commonalgorithmsusedintheirproposedoffloadingschema
| also essential | to  | have | interoperability, |     | which | is the | ability |     |     |     |     |     |     |     |     |
| -------------- | --- | ---- | ----------------- | --- | ----- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
of the destination to execute source code correctly. This by 32% and 21%, respectively. Based on RQ3, the most
is required in such heterogeneous computational models to crucial metrics used to assess the offloading mechanisms
werelatency(46%)andenergy(32%).InthemannerofRQ4,
| share data | and | computations. | Interoperability |     |     | also | arises in |     |     |     |     |     |     |     |     |
| ---------- | --- | ------------- | ---------------- | --- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
a highly heterogeneous networked environment (consisting the majority of case studies were utilized in the experiment
of several types of software and hardware from different results were vehicular networks (34%), and general apps
|           |            |       |                |     |     |                  |     | (32%). Furthermore, |     | regarding |     | RQ5, | the highest | percentage |     |
| --------- | ---------- | ----- | -------------- | --- | --- | ---------------- | --- | ------------------- | --- | --------- | --- | ---- | ----------- | ---------- | --- |
| vendors). | In IoT-fog | cloud | communication, |     |     | interoperability |     |                     |     |           |     |      |             |            |     |
issues have become increasingly challenging. For example, of studies evaluated their proposed approaches using the
variouscloudstorageprovidershaveemployeddiversestor- TensorFlow simulator. According to RQ6, the offloading
|                   |     |             |     |             |                 |     |     | modes used | for | the implementation |     |     | of their | offloading |     |
| ----------------- | --- | ----------- | --- | ----------- | --------------- | --- | --- | ---------- | --- | ------------------ | --- | --- | -------- | ---------- | --- |
| age technologies. |     | Compression |     | techniques, | synchronization |     |     |            |     |                    |     |     |          |            |     |
systems, and data security and privacy measures may differ schemaswerebinaryoffloading(80%)andpartialoffloading
| foreachstorageprovider.Heterogeneoussystemsmakefog |     |     |     |     |     |     |     | (20%). |        |         |     |          |            |      |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------- | --- | -------- | ---------- | ---- | --- |
|                                                    |     |     |     |     |     |     |     | In the | manner | of RQ7, | the | vertical | offloading | mode | had |
serversmoreeffective.However,theyincreasethechallenge
ofoffloadingmodels.Indeed,theaforementionedopenissues thehighestpercentageof55%intheliterature.Regardingto
provideanopportunitytobringtogetherresearchbasedonthe RQ8,themajorityoftheresearcharticlesaddressedquestions
regardingwhere/when,by30%.Furthermore,basedonRQ9,
offloadingmechanismsinfogenvironments.
|     |     |     |     |     |     |     |     | only 14% | of the | research | articles |     | did use | SDN | in their |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | -------- | --- | ------- | --- | -------- |
offloadingstrategyarchitecture.RegardingtoRQ10,66%of
K. FAULTTOLERANCE
theresearchpapershaveformulatedtheiroffloadingstrategy
Inadditiontosecurityandprivacy,faulttoleranceisacrucial
forestablishingtrustintaskoffloadinginfog.Asdiscussed problem into an MDP and solved it based on RL or DRL
approaches.
| in the preceding |     | sections, | mobility | assistance |     | is one | of the |              |     |          |       |          |     |                |     |
| ---------------- | --- | --------- | -------- | ---------- | --- | ------ | ------ | ------------ | --- | -------- | ----- | -------- | --- | -------------- | --- |
|                  |     |           |          |            |     |        |        | In addition, |     | based on | RQ11, | existing |     | fog offloading |     |
mostsignificantrequirementsduringtaskoffloadingbecause
freedom of movement and autonomy of communication are techniques have faced a number of unresolved challenges,
|                 |      |                |          |            |              |       |          | including      | security, | mobility,   |          | multi-objective |            | mechanisms, |         |
| --------------- | ---- | -------------- | -------- | ---------- | ------------ | ----- | -------- | -------------- | --------- | ----------- | -------- | --------------- | ---------- | ----------- | ------- |
| essential       | user | satisfaction   | factors. | However,   |              | there | are sev- |                |           |             |          |                 |            |             |         |
|                 |      |                |          |            |              |       |          | implementation |           | challenges, | workload |                 | prediction |             | in fog, |
| eral challenges |      | to maintaining |          | continuous | connectivity |       | and      |                |           |             |          |                 |            |             |         |
ongoingaccesstofogserversduringrelocation.Forinstance, findingoptimalpolicyforcandidatefogselection,offloading
|     |     |     |     |     |     |     |     | modeling | with | SDN technology, |     | offloading |     | partitioning, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --------------- | --- | ---------- | --- | ------------- | --- |
datatransferratesandnetworkbandwidthcanfluctuateora
|     |     |     |     |     |     |     |     | offloading | large-scale |     | networks, | heterogeneity |     | and | inter- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --------- | ------------- | --- | --- | ------ |
connectioncanbelost.Consequently,taskoffloadingshould
beimprovedwithfaulttolerancemechanismstoensurethat operability, and fault tolerance. Based on an extensive
|          |                 |     |             |     |               |     |         | study, an       | offloading | mechanism |            | based | on    | RL and | DRL      |
| -------- | --------------- | --- | ----------- | --- | ------------- | --- | ------- | --------------- | ---------- | --------- | ---------- | ----- | ----- | ------ | -------- |
| the task | is successfully |     | transmitted |     | and executed, |     | as well |                 |            |           |            |       |       |        |          |
|          |                 |     |             |     |               |     |         | method taxonomy |            | has been  | presented, |       | which | will   | help the |
astodecreasethetimeenergyconsumptionandapplication
responseinend-userdevices. researchcommunitytoachieveabetterunderstandingofthe
offloadingmechanisminfogenvironments.
VIII. CONCLUSION
| Fog computing |         | has emerged |         | as a promising |         | approach | to     | REFERENCES |     |     |     |     |     |     |     |
| ------------- | ------- | ----------- | ------- | -------------- | ------- | -------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
| significantly | improve |             | the QoS | of user        | devices | and      | reduce |            |     |     |     |     |     |     |     |
[1] A.Botta,W.Donato,V.Persico,andA.Pescapé,‘‘Integrationofcloud
networkoperationalcostsbymovingcomputationresources
computingandInternetofThings:Asurvey,’’FutureGenerat.Comput.
tonetworkedges.Computationoffloadingisatechniquethat Syst.,vol.56,pp.684–700,Mar.2016.
| 12582 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
[2] R.Xie,Q.Tang,Q.Wang,X.Liu,F.R.Yu,andT.Huang,‘‘Collaborative [22] S. S. Hajam and S. A. Sofi, ‘‘IoT-fog architectures in smart city
vehicular edge computing networks: Architecture design and research applications:Asurvey,’’ChinaCommun.,vol.18,no.11,pp.117–140,
| challenges,’’IEEEAccess,vol.7,pp.178942–178952,2019. |     |     |     |     |     |     | Nov.2021. |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[3] P. Fraga-Lamas, T. M. Fernández-Caramés, O. Blanco-Novoa, and [23] S.DuggalandP.Kaur,‘‘Fogcomputingbasedhealthcareapplications
M.A.Vilar-Montesinos, ‘‘A review on industrial augmented real- and frameworks: A review,’’ in Proc. 8th Int. Conf. Comput. Sustain.
ity systems for the industry 4.0 shipyard,’’ IEEE Access, vol. 6, GlobalDevelop.(INDIACom),2021,pp.238–243.
pp.13358–13375,2018. [24] S. O. Ogundoyin and I. A. Kamil, ‘‘Optimization techniques and
|           |           |     |             |              |       |               | applications |     | in fog computing: |     | An exhaustive | survey,’’ | Swarm | Evol. |
| --------- | --------- | --- | ----------- | ------------ | ----- | ------------- | ------------ | --- | ----------------- | --- | ------------- | --------- | ----- | ----- |
| [4] A. B. | De Souza, | P.  | A. L. Rego, | T. Carneiro, | J. D. | C. Rodrigues, |              |     |                   |     |               |           |       |       |
P.P.R.Filho,J.N.DeSouza,V.Chamola,V.H.C.DeAlbuquerque, Comput.,vol.66,Oct.2021,Art.no.100937.
and B. Sikdar, ‘‘Computation offloading for vehicular environments: [25] M. Sheikh, S. Mostafa, H. Kashani, and E. Mahdipour, ‘‘Towards
Asurvey,’’IEEEAccess,vol.8,pp.198214–198243,2020. effectiveoffloadingmechanismsinfogcomputing,’’MultimediaTools
[5] H. Tran-Dang, S. Bhardwaj, T. Rahim, A. Musaddiq, and D.-S. Kim, Appl.,vol.81,pp.1997–2042,Oct.2021.
‘‘Reinforcementlearningbasedresourcemanagementforfogcomputing [26] M.GillandD.Singh,‘‘Acomprehensivestudyofsimulationframeworks
andresearchdirectionsinfogcomputing,’’Comput.Sci.Rev.,vol.40,
environment:Literaturereview,challenges,andopenissues,’’J.Commun.
| Netw.,vol.24,no.1,pp.83–98,Feb.2022. |     |              |          |         |            |               | May2021,Art.no.100391. |     |            |            |     |              |        |       |
| ------------------------------------ | --- | ------------ | -------- | ------- | ---------- | ------------- | ---------------------- | --- | ---------- | ---------- | --- | ------------ | ------ | ----- |
|                                      |     |              |          |         |            |               | [27] A. Mekrache,      |     | A. Bradai, | E. Moulay, | and | S. Dawaliby, | ‘‘Deep | rein- |
| [6] B. Kar,                          | W.  | Yahya, Y.-D. | Lin, and | A. Ali, | ‘‘A survey | on offloading |                        |     |            |            |     |              |        |       |
in federated cloud-edge-fog systems with traditional optimization and forcementlearningtechniquesforvehicularnetworks:Recentadvances
machinelearning,’’2022,arXiv:2202.10628. and future trends towards 6G,’’ Veh. Commun., vol. 33, Jan. 2022,
[7] C.Jiang,X.Cheng,H.Gao,X.Zhou,andJ.Wan,‘‘Towardcomputation Art.no.100398.
offloading in edge computing: A survey,’’ IEEE Access, vol. 7, [28] K.Gasmi,S.Dilek,S.Tosun,andS.Ozdemir,‘‘Asurveyoncompu-
tationoffloadingandserviceplacementinfogcomputing-basedIoT,’’
pp.131543–131558,2019.
J.Supercomput.,vol.78,no.2,pp.1983–2014,Feb.2021.
[8] S.Patil-Karpe,S.H.Brahmananda,andS.Karpe,‘‘Reviewofresource
|            |     |                  |     |       |             |               | [29] D.       | Alsadie, | ‘‘Resource    | management |           | strategies      | in fog computing |       |
| ---------- | --- | ---------------- | --- | ----- | ----------- | ------------- | ------------- | -------- | ------------- | ---------- | --------- | --------------- | ---------------- | ----- |
| allocation | in  | fog computing,’’ | in  | Smart | Intelligent | Computing and |               |          |               |            |           |                 |                  |       |
|            |     |                  |     |       |             |               | environment—A |          | comprehensive |            | review,’’ | Int. J. Comput. | Sci.             | Netw. |
Applications.Singapore:Springer,2020,pp.327–334.
Secur.,vol.22,no.4,pp.310–328,2022.
[9] C.Mouradian,D.Naboulsi,S.Yangui,R.H.Glitho,M.J.Morrow,and
|     |     |     |     |     |     |     | [30] H. Sabireen |     | and V. | Neelanarayanan, | ‘‘A | review | on fog computing: |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | --------------- | --- | ------ | ----------------- | --- |
P.A.Polakos,‘‘Acomprehensivesurveyonfogcomputing:State-of-the- Architecture, fog with IoT, algorithms and research challenges,’’ ICT
artandresearchchallenges,’’IEEECommun.SurveysTuts.,vol.20,no.1,
Exp.,vol.7,no.2,pp.162–176,Jun.2021.
pp.416–464,1stQuart.,2018.
[31] F.Bonomi,R.Milito,J.Zhu,andS.Addepalli,‘‘Fogcomputingandits
[10] S.AljanabiandA.Chalechale,‘‘ImprovingIoTservicesusingahybrid
roleintheInternetofThings,’’inProc.MCCWorkshopMobileCloud
fog-cloudoffloading,’’IEEEAccess,vol.9,pp.13775–13788,2021.
Comput.,Aug.2012,pp.13–15.
[11] J.-Y.Baek,G.Kaddoum,S.Garg,K.Kaur,andV.Gravel,‘‘Managingfog
[32] K.S.Awaisi,A.Abbas,M.Zareei,H.A.Khattak,M.U.S.Khan,M.Ali,
networksusingreinforcementlearningbasedloadbalancingalgorithm,’’
|     |     |     |     |     |     |     | I.U.Din, | and | S. Shah, | ‘‘Towards | a fog | enabled efficient | car | parking |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --------- | ----- | ----------------- | --- | ------- |
in Proc. IEEE Wireless Commun. Netw. Conf. (WCNC), Apr. 2019, architecture,’’IEEEAccess,vol.7,pp.159100–159111,2019.
pp.1–7. [33] Z.Á.Mann,‘‘Notionsofarchitectureinfogcomputing,’’Computing,
[12] Z. Ning, P. Dong, X. Wang, L. Guo, J. J. P. C. Rodrigues, X. vol.103,no.1,pp.51–73,Jan.2021.
| Kong,           | J. Huang, | and      | R.Y.K.Kwok,  | ‘‘Deep              | reinforcement | learning      |         |             |          |     |         |              |            |     |
| --------------- | --------- | -------- | ------------ | ------------------- | ------------- | ------------- | ------- | ----------- | -------- | --- | ------- | ------------ | ---------- | --- |
|                 |           |          |              |                     |               |               | [34] A. | Yousefpour, | C. Fung, | T.  | Nguyen, | K. Kadiyala, | F. Jalali, | A.  |
| for intelligent |           | Internet | of Vehicles: | An energy-efficient |               | computational |         |             |          |     |         |              |            |     |
Niakanlahiji,J.Kong,andJ.P.Jue,‘‘Alloneneedstoknowaboutfog
offloadingscheme,’’IEEETrans.Cogn.Commun.Netw.,vol.5,no.4,
computingandrelatededgecomputingparadigms:Acompletesurvey,’’
pp.1060–1072,Jul.2019.
J.Syst.Archit.,vol.98,pp.289–330,2019.
| [13] J. Shi, | J. Du, | J. Wang, | J. Wang, | and J. | Yuan, ‘‘Priority-aware | task |     |     |     |     |     |     |     |     |
| ------------ | ------ | -------- | -------- | ------ | ---------------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
[35] T.-A.-N.Abdali,R.Hassan,A.H.M.Aman,andQ.N.Nguyen,‘‘Fog
offloading in vehicular fog computing based on deep reinforcement computingadvancement:Concept,architecture,applications,advantages,
learning,’’IEEETrans.Veh.Technol.,vol.69,no.12,pp.16067–16081,
andopenissues,’’IEEEAccess,vol.9,pp.75961–75980,2021.
Dec.2020.
|              |     |                      |     |            |              |            | [36] R. K. | Naha, | S. Garg,   | D. Georgakopoulos, |            | P. P. Jayaraman, |            | L. Gao, |
| ------------ | --- | -------------------- | --- | ---------- | ------------ | ---------- | ---------- | ----- | ---------- | ------------------ | ---------- | ---------------- | ---------- | ------- |
| [14] Z. Chen | and | X. Su, ‘‘Computation |     | offloading | and resource | allocation |            |       |            |                    |            |                  |            |         |
|              |     |                      |     |            |              |            | Y. Xiang,  | and   | R. Ranjan, | ‘‘Fog              | computing: | Survey           | of trends, | archi-  |
basedoncell-freeradioaccessnetwork,’’inProc.IEEE6thInf.Technol.
|     |     |     |     |     |     |     | tectures, | requirements, |     | and research | directions,’’ | IEEE | Access, | vol. 6, |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ------------ | ------------- | ---- | ------- | ------- |
MechatronicsEng.Conf.(ITOEC),Mar.2022,pp.1498–1502.
pp.47980–48009,2018.
[15] M.Ghobaei-Arani,A.Souri,andA.A.Rahmanian,‘‘Resourcemanage-
|     |     |     |     |     |     |     | [37] P. Hu, | S. Dhelim, | H.  | Ning, and | T. Qiu, | ‘‘Survey | on fog computing: |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | --------- | ------- | -------- | ----------------- | --- |
mentapproachesinfogcomputing:Acomprehensivereview,’’J.Grid Architecture,keytechnologies,applicationsandopenissues,’’J.Netw.
Comput.,vol.18,no.1,pp.1–42,Mar.2020. Comput.Appl.,vol.98,pp.27–42,Nov.2017.
[16] A. Shakarami, A. Shahidinejad, and M. Ghobaei-Arani, ‘‘A review [38] J. Singh, P. Singh, and S. S. Gill, ‘‘Fog computing: A taxonomy,
onthecomputationoffloadingapproachesinmobileedgecomputing: systematicreview,currenttrendsandresearchchallenges,’’J.Parallel
| A game-theoretic |     | perspective,’’ | Softw., | Pract. | Exper., | vol. 50, no. 9, |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------- | ------- | ------ | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Distrib.Comput.,vol.157,pp.56–85,Nov.2021.
pp.1719–1759,2020.
[39] M.Satyanarayanan,P.Bahl,R.Caceres,andN.Davies,‘‘Thecasefor
[17] A. Shakarami, M. Ghobaei-Arani, and A. Shahidinejad, ‘‘A survey VM-based cloudlets in mobile computing,’’ IEEE Pervasive Comput.,
onthecomputationoffloadingapproachesinmobileedgecomputing: vol.1,no.4,pp.14–23,Oct.2009.
A machine learning-based perspective,’’ Comput. Netw., vol. 182, [40] Y. Jararweh, A. Doulat, O. AlQudah, E. Ahmed, M. Al-Ayyoub, and
Dec.2020,Art.no.107496. E. Benkhelifa, ‘‘The future of mobile cloud computing: Integrating
[18] A. Shakarami and M. Ghobaei-Arani, ‘‘A survey on the computation cloudlets and mobile edge computing,’’ in Proc. 23rd Int. Conf.
| offloading | approaches |     | in mobile | edge/cloud | computing | environment: |     |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | --------- | ---------- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Telecommun.(ICT),May2016,pp.1–5.
Astochastic-basedperspective,’’Comput.Netw.,vol.182,Aug.2020,
|     |     |     |     |     |     |     | [41] M. Babar, | M.  | S. Khan, | F. Ali, | M. Imran, | and M. | Shoaib, ‘‘Cloudlet |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ------- | --------- | ------ | ------------------ | --- |
Art.no.107496. computing:Recentadvances,taxonomy,andchallenges,’’IEEEAccess,
[19] H. Lin, S. Zeadally, Z. Chen, H. Labiod, and L. Wang, ‘‘Journal of vol.9,pp.29609–29622,2021.
networkandcomputerapplicationsasurveyoncomputationoffloading [42] Y. Ai, M. Peng, and K. Zhang, ‘‘Edge cloud computing technologies
modeling for edge computing,’’ J. Netw. Comput. Appl., vol. 169, forInternetofThings:Aprimer,’’Digit.Commun.Netw.,vol.4,no.2,
| May2020,Art.no.102781. |     |     |     |     |     |     | pp.77–86,2018. |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
[20] T. Zheng, J. Wan, J. Zhang, C. Jiang, and G. Jia, ‘‘A survey of [43] K.Bilal,O.Khalid,A.Erbad,andS.U.Khan,‘‘Potentials,trends,and
computationoffloadinginedgecomputing,’’inProc.Int.Conf.Comput.,
prospectsinedgetechnologies:Fog,cloudlet,mobileedge,andmicro
Inf.Telecommun.Syst.(CITS),Oct.2020,pp.1–6. datacenters,’’Comput.Netw.,vol.130,pp.94–120,Jan.2018.
[21] S.M.Salman,T.A.Sitompul,A.V.Papadopoulos,andT.Nolte,‘‘Fog [44] D. Koustabh and S. K. Datta, ‘‘Comparison of edge computing
computingforaugmentedreality:Trends,challengesandopportunities,’’ implementations:Fogcomputing,cloudletandmobileedgecomputing,’’
inProc.IEEEInt.Conf.FogComput.(ICFC),Apr.2020,pp.56–63. inProc.GlobalInternetThingsSummit(GIoTS),2017,pp.1–6.
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     |     | 12583 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
[45] Y.Xiao,L.Xiao,S.Member,K.Wan,andH.Yang,‘‘Reinforcement [66] A.Coutinho,F.Greve,C.Prazeres,andJ.Cardoso,‘‘Fogbed:Arapid-
learningbasedenergy-efficientcollaborativeinferenceformobileedge prototypingemulationenvironmentforfogcomputing,’’inProc.IEEE
computing,’’IEEETrans.Commun.,earlyaccess,Dec.14,2022,doi: Int.Conf.Commun.(ICC),May2018,pp.1–7.
10.1109/TCOMM.2022.3229033. [67] Y.KarimandR.Hasan,‘‘FogTestBed:Agenericarchitecturefortestbed
forfog-basedsystems,’’inProc.SoutheastCon,Mar.2020,pp.1–7.
| [46] M. Maray | and | J. Shuja,   | ‘‘Computation | offloading        | in mobile | cloud    |                |                  |     |           |               |            |     |
| ------------- | --- | ----------- | ------------- | ----------------- | --------- | -------- | -------------- | ---------------- | --- | --------- | ------------- | ---------- | --- |
|               |     |             |               |                   |           |          | [68] H. Gupta, | A. V. Dastjerdi, | S.  | K. Ghosh, | and R. Buyya, | ‘‘iFogSim: |     |
| computing     | and | mobile edge | computing:    | Survey, taxonomy, |           | and open |                |                  |     |           |               |            |     |
issues,’’MobileInf.Syst.,vol.2022,pp.1–17,Jun.2022. A toolkit for modeling and simulation of resource management tech-
[47] W. Tang, X. Zhao, W. Rafique, and W. Dou, ‘‘A blockchain-based niquesintheInternetofThings,edgeandfogcomputingenvironments,’’
Softw.,Pract.Exper.,vol.47,no.9,pp.1–22,2016.
offloadingapproachinfogcomputingenvironment,’’inProc.IEEEInt.
|     |     |     |     |     |     |     | [69] R. N. | Calheiros, R. | Ranjan, | A. Beloglazov, | C. A. | F. De Rose, | and |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | ------- | -------------- | ----- | ----------- | --- |
Conf.ParallelDistrib.Process.Appl.,UbiquitousComput.Commun.,Big
|     |     |     |     |     |     |     | R. Buyya, | ‘‘CloudSim: | A toolkit | for | modeling and | simulation | of  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --------- | --- | ------------ | ---------- | --- |
DataCloudComput.,SocialComput.Netw.,Sustain.Comput.Commun.,
cloudcomputingenvironmentsandevaluationofresourceprovisioning
Dec.2018,pp.308–315. algorithms,’’Softw.,Pract.Exper.,vol.41,no.1,pp.23–50,Jan.2011.
[48] Y. I. Alzoubi, V. H. Osmanaj, A. Jaradat, and A. Al-Ahmad, ‘‘Fog [70] R.Mayer,L.Graser,H.Gupta,E.Saurez,andU.Ramachandran,‘‘Emu-
computingsecurityandprivacyfortheInternetofThingapplications:
|     |     |     |     |     |     |     | Fog: | Extensible and | scalable | emulation | of large-scale | fog computing |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------------- | -------- | --------- | -------------- | ------------- | --- |
State-of-the-art,’’Secur.Privacy,vol.4,no.2,p.e145,Mar.2021. infrastructures,’’ in Proc. IEEE Fog World Congr. (FWC), Oct. 2017,
| [49] Y.-L.Jiang,Y.-S.Chen,S.-W.Yang,andC.-H.Wu,‘‘Energy-efficient |     |     |     |     |     |     | pp.1–6. |     |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
taskoffloadingfortime-sensitiveapplicationsinfogcomputing,’’IEEE [71] C.Sonmez,A.Ozgovde,andC.Ersoy,‘‘EdgeCloudSim:Anenvironment
Syst.J.,vol.13,no.3,pp.2930–2941,Sep.2019. forperformanceevaluationofedgecomputingsystems,’’inProc.2ndInt.
Conf.FogMobileEdgeComput.(FMEC),May2017,pp.1–17.
[50] G.Caiza,M.Saeteros,W.Oñate,andM.V.Garcia,‘‘Fogcomputing
|     |     |     |     |     |     |     | [72] C. Puliafito, | D. M. | Gonçalves, | M. M. | Lopes, Leonardo | L.  | Martins, |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | ----- | ---------- | ----- | --------------- | --- | -------- |
atindustriallevel,architecture,latency,energy,andsecurity:Areview,’’
Heliyon,vol.6,no.4,Apr.2020,Art.no.e03706. E.Madeira,E.Mingozzi,O.Rana,andL.F.Bittencour,‘‘MobFogSim:
[51] M. H. Kashani, A. M. Rahmani, and N. J. Navimipour, ‘‘Quality of Simulationofmobilityandmigrationforfogcomputing,’’Simul.Model.
Pract.Theory,vol.101,May2019,Art.no.102062.
| service-aware |     | approaches | in fog computing,’’ | Int. | J. Commun. | Syst., |                 |                |     |           |               |             |     |
| ------------- | --- | ---------- | ------------------- | ---- | ---------- | ------ | --------------- | -------------- | --- | --------- | ------------- | ----------- | --- |
|               |     |            |                     |      |            |        | [73] R. Mahmud, | S. Pallewatta, | M.  | Goudarzi, | and R. Buyya, | ‘‘iFogSim2: |     |
vol.33,no.8,p.e4340,May2020.
AnextendediFogSimsimulatorformobility,clustering,andmicroservice
[52] H.Wu,‘‘Multi-objectivedecision-makingformobilecloudoffloading:
managementinedgeandfogcomputingenvironments,’’J.Syst.Softw.,
Asurvey,’’IEEEAccess,vol.6,pp.3962–3976,2018. vol.190,Aug.2022,Art.no.111351.
[53] L.Ni,J.Zhang,C.Jiang,C.Yan,andK.Yu,‘‘Resourceallocationstrategy [74] S.ThrunandM.L.Littman,‘‘Reinforcementlearning:Anintroduction,’’
infogcomputingbasedonpricedtimedPetrinets,’’IEEEInternetThings AIMag.,vol.21,no.1,p.103,2018.
J.,vol.4,no.5,pp.1216–1228,Oct.2017. [75] Y. Li, ‘‘Deep reinforcement learning: An overview,’’ 2017,
[54] V.JainandB.Kumar,‘‘Optimaltaskoffloadingandresourceallotment arXiv:1701.07274.
towardsfog-cloudarchitecture,’’inProc.11thInt.Conf.CloudComput., [76] N.AkalinandA.Loutfi,‘‘Reinforcementlearningapproachesinsocial
robotics,’’Sensors,vol.21,no.4,p.1292,Feb.2021.
DataSci.Eng.,Jan.2021,pp.233–238.
|     |     |     |     |     |     |     | [77] S. Gupta, | G. Singal, | and D. | Garg, | ‘‘Deep reinforcement |     | learning |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ---------- | ------ | ----- | -------------------- | --- | -------- |
[55] F.Saeik,M.Avgeris,D.Spatharakis,N.Santi,D.Dechouniotis,J.Violos,
techniquesindiversifieddomains:Asurvey,’’Arch.Comput.Methods
A.Leivadeas,N.Athanasopoulos,N.Mitton,andS.Papavassiliou,‘‘Task
Eng.,vol.28,no.7,pp.4715–4754,Dec.2021.
offloading in edge and cloud computing: A survey on mathematical, [78] V. François-Lavet, P. Henderson, R. Islam, M. G. Bellemare, and
| artificial | intelligence | and | control | theory solutions,’’ | Comput. | Netw., |            |                   |     |                    |     |             |        |
| ---------- | ------------ | --- | ------- | ------------------- | ------- | ------ | ---------- | ----------------- | --- | ------------------ | --- | ----------- | ------ |
|            |              |     |         |                     |         |        | J. Pineau, | ‘‘An introduction | to  | deep reinforcement |     | learning,’’ | Found. |
vol.195,Jan.2021,Art.no.108177. Trends®Mach.Learn.,vol.11,nos.3–4,pp.219–354,Nov.2018.
[56] L.Huang,X.Feng,A.Feng,Y.Huang,andL.P.Qian,‘‘Distributeddeep [79] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness,
learning-basedoffloadingformobileedgecomputingnetworks,’’Mobile M.G.Bellemare, and A. Graves, ‘‘Human-level control through deep
Netw.Appl.,vol.27,no.3,pp.1123–1130,Jun.2022. reinforcementlearning,’’Nature,vol.518,no.7540,pp.529–533,2015.
[57] L.Huang,X.Feng,C.Zhang,L.Qian,andY.Wu,‘‘Deepreinforcement [80] K.Arulkumaran,M.P.Deisenroth,M.Brundage,andA.A.Bharath,
learning-basedjointtaskoffloadingandbandwidthallocationformulti- ‘‘A brief survey of deep reinforcement learning,’’ 2017,
user mobile edge computing,’’ Digit. Commun. Netw., vol. 5, no. 1, arXiv:1708.05866.
pp.10–17,Feb.2019. [81] S. S. Mousavi, M. Schukat, and E. Howley, ‘‘Deep reinforcement
learning:Anoverview,’’2017,arXiv:1806.08894.
[58] N.D.Vahed,M.Ghobaei-Arani,andA.Souri,‘‘Multiobjectivevirtual
|         |           |            |       |                 |               |     | [82] C.J.C.H.Watkins,‘‘Q-learning,’’Mach.learning,vol.292,pp.279–292, |     |     |     |     |     |     |
| ------- | --------- | ---------- | ----- | --------------- | ------------- | --- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| machine | placement | mechanisms | using | nature-inspired | Metaheuristic |     |                                                                       |     |     |     |     |     |     |
May1992.
algorithms in cloud environments: A comprehensive review,’’ Int. [83] G.Yang,L.Hou,H.Cheng,X.He,D.He,andS.Chan,‘‘Computation
J.Commun.Syst.,vol.32,no.14,p.e4068,Sep.2019.
|             |         |         |          |            |          |          | offloading | time optimisation |     | via Q-learning | in opportunistic |     | edge |
| ----------- | ------- | ------- | -------- | ---------- | -------- | -------- | ---------- | ----------------- | --- | -------------- | ---------------- | --- | ---- |
| [59] S. Wu, | W. Xia, | W. Cui, | Q. Chao, | Z. Lan, F. | Yan, and | L. Shen, |            |                   |     |                |                  |     |      |
computing,’’IETCommun.,vol.14,no.21,pp.3898–3906,Dec.2020.
| ‘‘An | efficient offloading |     | algorithm | based on support | vector | machine |                                                                   |     |     |     |     |     |     |
| ---- | -------------------- | --- | --------- | ---------------- | ------ | ------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|      |                      |     |           |                  |        |         | [84] J.AlotaibiandL.Alazzawi,‘‘SaFIoV:Asecureandfastcommunication |     |     |     |     |     |     |
for mobile edge computing in vehicular networks,’’ in Proc. 10th in fog-based Internet-of-Vehicles using SDN and blockchain,’’ in
Int. Conf. Wireless Commun. Signal Process. (WCSP), Oct. 2018, Proc.IEEEInt.MidwestSymp.CircuitsSyst.(MWSCAS),Aug.2021,
| pp.1–6. |     |     |     |     |     |     | pp.334–339. |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
[60] M.Aazam,S.Zeadally,andK.A.Harras,‘‘Offloadinginfogcomputing [85] A.A.AlliandM.M.Alam,‘‘SecOFF-FCIoT:Machinelearningbased
for IoT: Review, enabling technologies, and research opportunities,’’ secure offloading in fog-cloud of things for smart city applications,’’
FutureGener.Comput.Syst.,vol.87,pp.278–289,Oct.2018. InternetThings,vol.7,Sep.2019,Art.no.100070.
[61] S.Nguyen,Z.Salcic,X.Zhang,andA.Bisht,‘‘Alow-costtwo-tierfog [86] A.ShahidinejadandM.Ghobaei-Arani,‘‘Jointcomputationoffloading
|     |     |     |     |     |     |     | and | resource provisioning | for | edge-cloud | computing | environment: |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ---------- | --------- | ------------ | --- |
computingtestbedforstreamingIoT-basedapplications,’’IEEEInternet
|     |     |     |     |     |     |     | A machine | learning-based | approach,’’ |     | Softw., Pract. | Exper., | vol. 50, |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | ----------- | --- | -------------- | ------- | -------- |
ThingsJ.,vol.8,no.8,pp.6928–6939,Apr.2021.
no.12,pp.2212–2230,Dec.2020.
[62] X.Kui,Y.Sun,S.Zhang,andY.Li,‘‘Characterizingthecapabilityof
|     |     |     |     |     |     |     | [87] C. Qu, | P. Calyam, | J. Yu, A. | Vandanapu, | O. Opeoluwa, |     | K. Gao, |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --------- | ---------- | ------------ | --- | ------- |
vehicularfogcomputinginlarge-scaleurbanenvironment,’’MobileNetw. S.Wang,R.Chastain,andK.Palaniappan,‘‘DroneCOCoNet:Learning-
Appl.,vol.23,no.4,pp.1050–1067,Aug.2018.
|     |     |     |     |     |     |     | based | edge computation | offloading | and | control networking |     | for drone |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------------- | ---------- | --- | ------------------ | --- | --------- |
[63] N.K.Giang,R.Lea,andV.C.M.Leung,‘‘Developingapplicationsin
videoanalytics,’’FutureGener.Comput.Syst.,vol.125,pp.247–262,
largescale,dynamicfogcomputing:Acasestudy,’’Softw.,Pract.Exper.,
Dec.2021.
vol.50,no.5,pp.519–532,May2020. [88] T.Wei,Y.Sun,Y.Zhang,Z.Wang,W.Wu,andJ.Gao,‘‘Energyefficient
[64] C.Li,H.Zhuang,Q.Wang,andX.Zhou,‘‘Computerengineeringand user access and computation offloading strategy for fog radio access
computerscienceSSLB:Self-similarity-basedloadbalancingforlarge- networkwithuplink/downlinkdecoupling,’’inProc.IEEE5thInt.Conf.
scalefogcomputing,’’Arab.J.Sci.Eng.,vol.43,no.12,pp.7487–7498, Comput.Commun.(ICCC),Dec.2019,pp.894–900.
2018. [89] A. Rafiq, W. Ping, W. Min, and M. S. A. Muthanna, ‘‘Fog assisted
[65] Q. Xu and J. Zhang, ‘‘PiFogBed: A fog computing testbed based on 6TiSCH tri-layer network architecture for adaptive scheduling and
raspberrypi,’’inProc.IEEE38thInt.Perform.Comput.Commun.Conf. energy-efficientoffloadingusingrank-basedQ-learninginsmartindus-
(IPCCC),Oct.2019,pp.1–8. tries,’’IEEESensorsJ.,vol.21,no.22,pp.25489–25507,Nov.2021.
| 12584 |     |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
[90] A.HazraandT.Amgoth,‘‘CeCO:Cost-efficientcomputationoffloading [111] H.VanHasselt,A.Guez,andD.Silver,‘‘Deepreinforcementlearning
ofIoTapplicationsingreenindustrialfognetworks,’’IEEETrans.Ind. with double Q-learning,’’ in Proc. AAAI Conf. Artif. Intell., 2016,
Informat.,vol.18,no.9,pp.6255–6263,Sep.2022. pp.2094–2100.
[91] M.Ibrar,A.Akbar,S.R.U.Jan,M.A.Jan,L.Wang,H.Song,and [112] H. C. Ke, H. Wang, H. W. Zhao, and W. J. Sun, ‘‘Deep reinforce-
N.Shah,‘‘ARTNet:AI-basedresourceallocationandtaskoffloadingin mentlearning-basedcomputationoffloadingandresourceallocationin
areconfigurableInternetofVehicularnetworks,’’IEEETrans.Netw.Sci. security-awaremobileedgecomputing,’’WirelessNetw.,vol.27,no.5,
Eng.,vol.9,no.1,pp.67–77,Jan.2022. pp.3357–3373,Jul.2021.
[92] F. Jazayeri, A. Shahidinejad, and M. Ghobaei-Arani, ‘‘Autonomous [113] W.Ziyu,T.Schaul,M.Hessel,H.Hasselt,M.Lanctot,andF.Nando,
computationoffloadingandauto-scalingtheinthemobilefogcomputing: ‘‘Dueling network architectures for deep reinforcement learning,’’ in
A deep reinforcement learning-based approach,’’ J. Ambient Intell. Proc.Int.Conf.Mach.Learn.,2016,pp.1995–2003.
HumanizedComput.,vol.12,no.8,pp.8265–8284,Aug.2021. [114] F. Jiang, R. Ma, Y. Gao, and Z. Gu, ‘‘A reinforcement learning-
[93] Z.Safavifar,S.Ghanadbashi,andF.Golpayegani,‘‘Adaptiveworkload basedcomputingoffloadingandresourceallocationschemeinF-RAN,’’
orchestrationinpureedgecomputing:Areinforcement-learningmodel,’’ EURASIPJ.Adv.SignalProcess.,vol.2021,no.1,pp.1–25,Dec.2021.
in Proc. IEEE 33rd Int. Conf. Tools Artif. Intell. (ICTAI), Nov. 2021, [115] F.Jiang,R.Ma,C.Sun,andZ.Gu,‘‘DuelingdeepQ-networklearning
pp.856–860. based computing offloading scheme for F-RAN,’’ in Proc. IEEE 31st
[94] G. M. S. Rahman, T. Dang, and M. Ahmed, ‘‘Deep reinforcement Annu. Int. Symp. Pers., Indoor Mobile Radio Commun., Aug. 2020,
learningbasedcomputationoffloadingandresourceallocationforlow- pp.1–6.
latencyfogradioaccessnetworks,’’Intell.ConvergedNetw.,vol.1,no.3, [116] K. Greff, R. K. Srivastava, J. Koutnìk, B. R. Steunebrink, and
pp.243–257,Dec.2020. J.Schmidhuber,‘‘LSTM:AsearchspaceOdyssey,’’IEEETrans.Neural
[95] Y. Ren, Y. Sun, and M. Peng, ‘‘Deep reinforcement learning based Netw.Learn.Syst.,vol.28,no.10,pp.2222–2232,Oct.2017.
computation offloading in fog enabled industrial Internet of Things,’’ [117] M.HausknechtandP.Stone,‘‘DeeprecurrentQ-learningforpartially
IEEETrans.Ind.Informat.,vol.17,no.7,pp.4978–4987,Jul.2021. observableMDPs,’’inProc.AAAIFallSymp.Ser.,2015,p.23.
[96] J. Zhao, M. Kong, Q. Li, and X. Sun, ‘‘Contract-based computing [118] I.Sorokin,A.Seleznev,M.Pavlov,A.Fedorov,andA.Ignateva,‘‘Deep
resourcemanagementviadeepreinforcementlearninginvehicularfog attentionrecurrentQ-network,’’2015,arXiv:1512.01693.
[119] R.Xie,Q.Tang,C.Liang,F.R.Yu,andT.Huang,‘‘Dynamiccomputation
computing,’’IEEEAccess,vol.8,pp.3319–3329,2020.
offloadinginIoTfogsystemswithimperfectchannel-stateinformation:
[97] U.MaanandY.Chaba,‘‘DeepQ-networkbasedfognodeoffloading
APOMDPapproach,’’IEEEInternetThingsJ.,vol.8,no.1,pp.345–356,
strategy for 5G vehicular adhoc network,’’ Ad Hoc Netw., vol. 120,
Jan.2021.
Sep.2021,Art.no.102565.
[120] J.BaekandG.Kaddoum,‘‘Onlinepartialoffloadingandtaskscheduling
[98] J.Zong,F.Yang,andX.Luo,‘‘Optimalquerypolicyandtaskoffloading
inSDN-fognetworkswithdeeprecurrentreinforcementlearning,’’IEEE
indynamicenvironments,’’inProc.IEEEInt.Conf.Commun.Workshops
InternetThingsJ.,vol.9,no.13,pp.11578–11589,Jul.2022.
(ICCWorkshops),Jun.2020,pp.1–6.
[121] J.BaekandG.Kaddoum,‘‘Heterogeneoustaskoffloadingandresource
[99] F.Firouzi,B.Farahani,E.Panahi,andM.Barzegari,‘‘Taskoffloading
allocationsviadeeprecurrentreinforcementlearninginpartialobserv-
foredge-fog-cloudinterplayinthehealthcareInternetofThings(IoT),’’
able multifog networks,’’ IEEE Internet Things J., vol. 8, no. 2,
inProc.IEEEInt.Conf.Omni-LayerIntell.Syst.(COINS),Aug.2021,
pp.1041–1056,Jan.2021.
pp.1–8.
[122] T.Wang,X.Luo,andW.Zhao,‘‘Improvingtheperformanceoftasks
[100] C. Pan, Z. Wang, Z. Zhou, and X. Ren, ‘‘Deep reinforcement
offloading for Internet of Vehicles via deep reinforcement learning
learning-basedURLLC-awaretaskoffloadingincollaborativevehicular
methods,’’IETCommun.,vol.16,no.10,pp.1230–1240,Jun.2022.
networks,’’ChinaCommun.,vol.18,no.7,pp.134–146,Jul.2021.
[123] S.VemireddyandR.R.Rout,‘‘Fuzzyreinforcementlearningforenergy
[101] D.B.Son,V.T.An,T.T.Hai,B.M.Nguyen,N.P.Le,andH.T.T.Binh,
efficient task offloading in vehicularfog computing,’’Comput. Netw.,
‘‘FuzzydeepQ-learningtaskoffloadingindelayconstrainedvehicular
vol.199,Nov.2021,Art.no.108463.
fog computing,’’ in Proc. Int. Joint Conf. Neural Netw. (IJCNN), [124] Y.Wang,K.Wang,H.Huang,T.Miyazaki,andS.Guo,‘‘Trafficand
Jul.2021,pp.1–8. computationco-offloadingwithreinforcementlearninginfogcomputing
[102] A.Hazra,M.Adhikari,T.Amgoth,andS.N.Srirama,‘‘Collaborative forindustrialapplications,’’IEEETrans.Ind.Informat.,vol.15,no.2,
AI-enabledintelligentpartialserviceprovisioningingreenindustrialfog
pp.976–986,Feb.2019.
networks,’’ IEEE Internet Things J., early access, Sep. 7, 2021, doi: [125] M.Tiwari,S.Misra,P.K.Bishoyi,andL.T.Yang,‘‘Devote:Criticality-
10.1109/JIOT.2021.3110910. awarefederatedserviceprovisioninginfog-basedIoTenvironments,’’
[103] S.M.A.Kazmi,S.Otoum,R.Hussain,andH.T.Mouftah,‘‘Anoveldeep IEEEInternetThingsJ.,vol.8,no.13,pp.10631–10638,Jul.2021.
reinforcementlearning-basedapproachfortask-offloadinginvehicular [126] H.Dong,H.Dong,Z.Ding,andS.Zhang,DeepReinforcementLearning.
networks,’’ in Proc. IEEE Global Commun. Conf. (GLOBECOM), Singapore:Springer,2020.
Dec.2021,pp.12–17. [127] Q. Tang, R. Xie, F. R. Yu, T. Huang, and Y. Liu, ‘‘Decentralized
[104] H.TanandL.Zhu,‘‘Overallcomputingoffloadingstrategybasedondeep computation offloading in IoT fog computing system with energy
reinforcementlearninginvehiclefogcomputing,’’J.Eng.,vol.2020, harvesting:Adec-POMDPapproach,’’IEEEInternetThingsJ.,vol.7,
no.11,pp.1080–1087,Nov.2020. no.6,pp.4898–4911,Jun.2020.
[105] G.Tian,Y.Ren,C.Pan,Z.Zhou,andX.Wang,‘‘Asynchronousfederated [128] V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. Lillicrap, T. Harley,
learningempoweredcomputationoffloadingincollaborativevehicular D.Silver, and K. Kavukcuoglu, ‘‘Asynchronous methods for deep
networks,’’ in Proc. IEEE Wireless Commun. Netw. Conf. (WCNC), reinforcement learning,’’ in Proc. Int. Conf. Mach. Learn., 2016,
Apr.2022,pp.315–320. pp.1928–1937.
[106] D.B.Son,T.H.Binh,H.K.Vo,B.M.Nguyen,H.T.T.Binh,andS.Yu, [129] W.BaiandC.Qian,‘‘Deepreinforcementlearningforjointoffloading
‘‘Value-basedreinforcementlearningapproachesfortaskoffloadingin andresourceallocationinfogcomputing,’’inProc.IEEE12thInt.Conf.
delayconstrainedvehicularedgecomputing,’’Eng.Appl.Artif.Intell., Softw.Eng.ServiceSci.(ICSESS),Aug.2021,pp.131–134.
vol.113,Aug.2022,Art.no.104898. [130] Y.Wei,F.R.Yu,M.Song,andZ.Han,‘‘Jointoptimizationofcaching,
[107] A. Lakhan, M. A. Mohammed, O. I. Obaid, C. Chakraborty, computing, and radio resources for fog-enabled IoT using natural
K.H.Abdulkareem, and S. Kadry, ‘‘Efficient deep-reinforcement actor–criticdeepreinforcementlearning,’’IEEEInternetThingsJ.,vol.6,
learning aware resource allocation in SDN-enabled fog paradigm,’’ no.2,pp.2061–2073,Apr.2019.
AutomatedSoftw.Eng.,vol.29,no.1,pp.1–25,May2022. [131] S. John, S. Levine, P. Abbeel, M. Jordan, and M. Philipp, ‘‘Trust
[108] B. Sellami, A. Hakiri, S. B. Yahia, and P. Berthou, ‘‘Energy-aware region policy optimization,’’ in Proc. Int. Conf. Mach. Learn., 2015,
task scheduling and offloading using deep reinforcement learning in pp.1889–1897.
SDN-enabled IoT network,’’ Comput. Netw., vol. 210, Jun. 2022, [132] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov,
Art.no.108957. ‘‘Proximalpolicyoptimizationalgorithms,’’2017,arXiv:1707.06347.
[109] Z. Jia, Z. Zhou, X. Wang, and S. Mumtaz, ‘‘Learning-based queuing [133] S.-S.LeeandS.Lee,‘‘Resourceallocationforvehicularfogcomputing
delay-awaretaskoffloadingincollaborativevehicularnetworks,’’inProc. using reinforcement learning combined with heuristic information,’’
IEEEInt.Conf.Commun.,Jun.2021,pp.1–6. IEEEInternetThingsJ.,vol.7,no.10,pp.10450–10464,Oct.2020.
[110] F.Jiang,X.Zhu,andC.Sun,‘‘DoubleDQNbasedcomputingoffloading [134] J.Xu,D.Li,W.Gu,andY.Chen,‘‘UAV-assistedtaskoffloadingforIoT
schemeforfogradioaccessnetworks,’’inProc.IEEE/CICInt.Conf. insmartbuildingsandenvironmentviadeepreinforcementlearning,’’
Commun.China(ICCC),Jul.2021,pp.1131–1136. BuildingEnviron.,vol.222,Aug.2022,Art.no.109218.
VOLUME11,2023 12585

D.H.Abdulazeez,S.K.Askar:OffloadingMechanismsBasedonRLandDLAlgorithmsintheFogComputingEnvironment
[135] T. Alam, A. Ullah, and M. Benaida, ‘‘Deep reinforcement learning DEZHEEN H. ABDULAZEEZ receivedtheB.S.
approachforcomputationoffloadinginblockchain-enabledcommuni- degree in computer science from the University
cations systems,’’ J. Ambient Intell. Humanized Comput., vol. 2022, of Duhok, in 2011, and the M.S. degree in
| pp.1–14,Jan.2022. |     |     |     |     |     |     | webapplicationandservicesfromtheUniversity |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
[136] J.J.Hunt,J.J.Hunt,A.Pritzel,N.Heess,T.Erez,Y.Tassa,D.Silver,
|     |     |     |     |     |     |     | of Leicester, | U.K., | in 2015. | She is | currently |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | -------- | ------ | --------- |
andD.Wierstra,‘‘Continuouscontrolwithdeepreinforcementlearning,’’
pursuingthePh.D.degreeinfogcomputingwith
2015,arXiv:1509.02971.
|               |                |              |     |         |        |               | the College | of Science, | University | of  | Duhok. |
| ------------- | -------------- | ------------ | --- | ------- | ------ | ------------- | ----------- | ----------- | ---------- | --- | ------ |
| [137] D. Lan, | A. Taherkordi, | F. Eliassen, | and | L. Liu, | ‘‘Deep | reinforcement |             |             |            |     |        |
learningforcomputationoffloadingandcachinginfog-basedvehicular Herresearchinterestsincludefogcomputing,the
networks,’’inProc.IEEE17thInt.Conf.MobileAdHocSensorSyst. Internet of Thing (IoT), sematic web, and web
| (MASS),Dec.2020,pp.622–630. |          |        |              |         |      |               | applicationsandservices. |     |     |     |     |
| --------------------------- | -------- | ------ | ------------ | ------- | ---- | ------------- | ------------------------ | --- | --- | --- | --- |
| [138] S. Chen,              | B. Tang, | and K. | Wang, ‘‘Twin | delayed | deep | deterministic |                          |     |     |     |     |
policygradient-basedintelligentcomputationoffloadingforIoT,’’Digit.
Commun.Netw.,vol.2022,pp.1–13,Jun.2022.
| [139] Z. Cheng, | M. Min, | M. Liwang, | L. Huang, | and | Z. Gao, | ‘‘Multiagent |     |     |     |     |     |
| --------------- | ------- | ---------- | --------- | --- | ------- | ------------ | --- | --- | --- | --- | --- |
DDPG-basedjointtaskpartitioningandpowercontrolinfogcomputing
networks,’’IEEEInternetThingsJ.,vol.9,no.1,pp.104–116,Jan.2022.
| [140] V. Jain | and B. Kumar, | ‘‘Blockchain |     | enabled | trusted task | offloading |     |     |     |     |     |
| ------------- | ------------- | ------------ | --- | ------- | ------------ | ---------- | --- | --- | --- | --- | --- |
schemeforfogcomputing:Adeepreinforcementlearningapproach,’’
| Trans. | Emerg. Telecommun. |     | Technol., | vol. 33, | no. 11, | Nov. 2022, |     |     |     |     |     |
| ------ | ------------------ | --- | --------- | -------- | ------- | ---------- | --- | --- | --- | --- | --- |
Art.no.e4587m.
[141] M.Chen,T.Wang,S.Zhang,andA.Liu,‘‘Deepreinforcementlearning
| for | computation offloading |     | in mobile | edge computing |     | environment,’’ |     |     |     |     |     |
| --- | ---------------------- | --- | --------- | -------------- | --- | -------------- | --- | --- | --- | --- | --- |
Comput.Commun.,vol.175,pp.1–12,Jul.2021.
[142] J.Shi,J.Du,J.Wang,andJ.Yuan,‘‘Deepreinforcementlearning-based
V2Vpartialcomputationoffloadinginvehicularfogcomputing,’’inProc.
IEEEWirelessCommun.Netw.Conf.(WCNC),Mar.2021,pp.1–6.
| [143] Z. Cheng, | M. Liwang, | N.  | Chen, L. | Huang, | X. Du, and | M. Guizani, |     |     |     |     |     |
| --------------- | ---------- | --- | -------- | ------ | ---------- | ----------- | --- | --- | --- | --- | --- |
‘‘Deepreinforcementlearning-basedjointtaskandenergyoffloadingin
UAV-aided6Gintelligentedgenetworks,’’Comput.Commun.,vol.192, SHAVAN K. ASKAR receivedtheB.Sc.(Hons.)
andM.Sc.degreesfromtheControlandSystems
pp.234–244,Aug.2022.
|     |     |     |     |     |     |     | Engineering | Department, | Baghdad, | in  | 2001 and |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | -------- | --- | -------- |
[144] T.Haarnoja,A.Zhou,P.Abbeel,andS.Levine,‘‘Softactor-critic:Off-
policymaximumentropydeepreinforcementlearningwithastochastic 2003,respectively,andthePh.D.degreeinelec-
actor,’’inProc.Int.Conf.Mach.Learn.,2018,pp.1861–1870. tronicsystemsengineeringfromtheUniversityof
[145] T.Haarnoja,A.Zhou,K.Hartikainen,G.Tucker,S.Ha,J.Tan,V.Kumar, Essex, U.K., in 2012. He is currently the CEO
H.Zhu,A.Gupta,P.Abbeel,andS.Levine,‘‘Softactor-criticalgorithms with Arcella Telecom. He is also an Associate
andapplications,’’2018,arXiv:1812.05905.
Professorofcomputernetworks.Heworksasan
| [146] M. | Sewak and R. | Learning, | ‘‘Policy-based |     | reinforcement | learning |     |     |     |     |     |
| -------- | ------------ | --------- | -------------- | --- | ------------- | -------- | --- | --- | --- | --- | --- |
AssistantProfessorwiththeCollegeofTechnical
| approaches: | Stochastic | policy | gradient | and | the REINFORCE | algo- |     |     |     |     |     |
| ----------- | ---------- | ------ | -------- | --- | ------------- | ----- | --- | --- | --- | --- | --- |
Engineering,ErbilPolytechnicUniversity.Healso
| rithm,’’ | in Deep Reinforcement |     | Learning. | Singapore: | Springer, | 2019, |     |     |     |     |     |
| -------- | --------------------- | --- | --------- | ---------- | --------- | ----- | --- | --- | --- | --- | --- |
pp.127–140. works in the field of networks that includes the Internet of Things,
[147] M.Etemadi,M.Ghobaei-Arani,andA.Shahidinejad,‘‘Acost-efficient software-definednetworks,opticalnetworks,and5Ginformationsystems
auto-scalingmechanismforIoTapplicationsinfogcomputingenviron- engineering. His research interests include 5G, the IoT SDN, network
virtualization,andfogandcloudcomputing.
ment:Adeeplearning-basedapproach,’’ClusterComput.,vol.24,no.4,
pp.3277–3292,Dec.2021.
| 12586 |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |