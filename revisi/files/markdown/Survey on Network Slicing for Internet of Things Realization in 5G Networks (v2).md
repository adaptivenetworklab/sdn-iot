# Survey on Network Slicing for Internet of Things Realization in 5G Networks (v2)

> Source file: `Survey on Network Slicing for Internet of Things Realization in 5G Networks (v2).pdf`

---

IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021 957
Survey on Network Slicing for Internet of Things
Realization in 5G Networks
Shalitha Wijethilaka , Student Member, IEEE, and Madhusanka Liyanage , Senior Member, IEEE,
Abstract—Internet of Things (IoT) is an emerging technology
that makes people’s lives smart by conquering a plethora of
diverse application and service areas. In near future, the fifth-
generation (5G) wireless networks provide the connectivity for
this IoT ecosystem. It has been carefully designed to facilitate
theexponentialgrowthintheIoTfield.Networkslicingisoneof
the key technologies in the 5G architecture that has the ability
to divide the physical network into multiple logical networks
(i.e., slices) with different network characteristics. Therefore,
network slicing is also a key enabler of realisation of IoT in
5G.Networkslicingcansatisfythevariousnetworkingdemands
by heterogeneous IoT applications via dedicated slices. In this
survey, we present a comprehensive analysis of the exploita-
Fig.1. EvolutionoftheInternet.
tion of network slicing in IoT realisation. We discuss network
slicing utilisation in different IoT application scenarios, along
with the technical challenges that can be solved via network
application scenarios demand various performance require-
slicing. Furthermore, integration challenges and open research
problems related to the network slicing in the IoT realisation ments such as low latency, ultra-reliability, high security and
are also discussed in this paper. Finally, we discuss the role of high data rates.
other emerging technologies and concepts, such as blockchain Most of these connected devices will use the wireless
andArtificialIntelligence/MachineLearning(AI/ML)innetwork
infrastructure to communicate. However, the existing wireless
slicing and IoT integration.
infrastructure is not able to handle the rapid growth of IoT
Index Terms—Network slicing, IoT, 5G, SDN, NFV, network connectionsalongwithtypicalmobileconnections.Moreover,
architecture, latency, reliability.
suchnetworksareincapableofsatisfyingtheheterogeneous
QoS requirements for different IoT application scenarios. As
a solution, the 5G architecture is designed with the aid of
various new technologies to handle these requirements.
I. INTRODUCTION
Software Defined Networking (SDN), Network Function
INTERNET has evolved over the last four decades, from Virtualization (NFV), Multi-access Edge Computing (MEC)
simple peer-to-peer networks to an advance IoT ecosystem andnetworkslicingaresomeofthepredominanttechnologies
(Figure 1). With the ubiquitous utilisation of IoTs, everything in 5G architecture [4]–[7]. SDN offers the ability to control
around us is becoming smart. It is possible to connect people the network traffic routing centrally and intelligently, using
andthingsatanytimefromanyplacewithnetworkaccess,to software applications [8]. Centralised control, network pro-
receive information of the thing, to operate the thing or even grammability and abstraction are the key benefits of SDN.
both, to make the life of the mankind easier [1]. The number NFV is a concept which is used to package network func-
of connected devices proliferates exponentially. According to tions such routing, load balancing and firewalls as software
Machina research,itisexpected thatthenumber ofconnected applications, so that they can run on commodity and general
devices will be 27 billion by 2024 [2]. Diversity of these hardware devices [9]. Tight coupling between network func-
IoT applications will also expand from simple smart home tions and specific hardware units was a huge bottleneck to
solutions to mission-critical health care systems [3]. These the evolution of such network functions. This can be elimi-
nated by using NFV. Providing cloud computing capabilities
Manuscript received September 25, 2020; revised December 16, 2020 to the edge network is the main purpose of MEC technol-
and January 26, 2021; accepted March 11, 2021. Date of publication
ogy[10].Itwillminimisethenetworkcongestiononbackhaul
March 22, 2021; date of current version May 21, 2021. (Corresponding
author:ShalithaWijethilaka.) andimprovetheresourceoptimisation,userexperienceandthe
Shalitha Wijethilaka is with the School of Computer Science, overall performance of the network [11].
University College Dublin, Dublin 4, D04 V1W8, Ireland (e-mail:
Dividingthephysicalnetworkintoseparatelogicalnetworks
mahadurage.wijethilaka@ucdconnect.ie).
MadhusankaLiyanageiswiththeSchoolofComputerScience,University known as slices is called network slicing. Each slice can be
CollegeDublin,Dublin4,D04V1W8,Ireland,andalsowiththeCentrefor configured to offer specific network capabilities and network
WirelessCommunications,UniversityofOulu,90014Oulu,Finland(e-mail:
characteristics[12].Thus,theEnd-to-End(E2E)networkslic-
madhusanka.liyanage@oulu.fi).
DigitalObjectIdentifier10.1109/COMST.2021.3067807 ing can help to deploy various 5G based services [13]–[18].
ThisworkislicensedunderaCreativeCommonsAttribution4.0License. Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/

958 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
TABLEI
|     |     |     |     | slice for | each service | scenario | is needed, | to allocate | required |
| --- | --- | --- | --- | --------- | ------------ | -------- | ---------- | ----------- | -------- |
SUMMARYOFACRONYMS
|     |     |     |     | resources  | to fulfill | the such requirements. |              |        |           |
| --- | --- | --- | --- | ---------- | ---------- | ---------------------- | ------------ | ------ | --------- |
|     |     |     |     | Similarly, | different  | IoT                    | applications | demand | different |
networkingrequirements.Forinstance,morethan99.99%reli-
|     |     |     |     | ability level    | and less      | than 1 | ms E2E latency | are         | required for |
| --- | --- | --- | --- | ---------------- | ------------- | ------ | -------------- | ----------- | ------------ |
|     |     |     |     | mission-critical | communication |        | IoT use        | cases. 10−9 | packet       |
µs
|     |     |     |     | loss rate    | and E2E            | latency range | of 250       | to         | 10 ms are    |
| --- | --- | --- | --- | ------------ | ------------------ | ------------- | ------------ | ---------- | ------------ |
|     |     |     |     | required     | factory automation |               | applications | [20]. Such | diverse      |
|     |     |     |     | requirements | of different       | IoT           | applications | can be     | fulfilled by |
|     |     |     |     | allocating   | a dedicated        | E2E network   | slice        | for each   | application  |
(Figure 2).
|     |     |     |     | The Network          | Slice             | as a Service      | (NSlaaS)         | concept           | allows        |
| --- | --- | --- | --- | -------------------- | ----------------- | ----------------- | ---------------- | ----------------- | ------------- |
|     |     |     |     | operators            | to create         | customised        | network          | slices for        | their cus-    |
|     |     |     |     | tomers               | as a service.     | This generates    | a new            | business          | model for     |
|     |     |     |     | Mobile               | Network Operators | (MNOs)            | [31],            | [32]. Moreover,   | an            |
|     |     |     |     | E2E network          | slicing           | framework         | that has         | the ability       | to hori-      |
|     |     |     |     | zontally             | slice computation | and               | communication    | resources         | was           |
|     |     |     |     | proposed             | in [33] for       | supporting        | vertical         | industry          | applications. |
|     |     |     |     | Network              | slicing           | improves          | the efficiency   | of resource       | utili-        |
|     |     |     |     | sation by            | dynamically       | adjusting         | network          | resources         | between       |
|     |     |     |     | the slices.          | It is possible    | to                | implement        | autonomous        | systems       |
|     |     |     |     | for such             | resource          | allocations       | and dynamic      | adjustment        | of            |
|     |     |     |     | resources            | [34]. This        | method            | can be           | used to           | improve the   |
|     |     |     |     | scalability          | of future         | IoT applications. |                  |                   |               |
|     |     |     |     | High                 | security and      | privacy           | for sensitive    | IoT               | applications, |
|     |     |     |     | such as              | healthcare,       | can be            | achieved         | through the       | slice iso-    |
|     |     |     |     | lation. For          | instance,         | a secure          | service-oriented | authentication    |               |
|     |     |     |     | framework            | has been          | proposed          | by Ni            | et al. for        | the realisa-  |
|     |     |     |     | tion of              | IoT services      | in 5G networks    | through          | fog               | computing     |
|     |     |     |     | and network          | slicing           | [35]. Since       | IoT              | devices are       | generally     |
|     |     |     |     | resource-constraint, |                   | they are highly   | vulnerable       | to                | attacks. The  |
|     |     |     |     | rapid growth         | in the            | number of         | IoT devices      | and pervasiveness |               |
|     |     |     |     | are also             | attracting many   | attackers         | to the           | IoT ecosystem     | [36].         |
|     |     |     |     | An adversary         | can easily        | dominate          | IoT              | devices and       | can lead      |
themtogenerateDistributedDenial-of-Service(DDoS)attacks
|     |     |     |     | to the network.    | The           | severity     | of these kinds   | of attacks  | can be        |
| --- | --- | --- | --- | ------------------ | ------------- | ------------ | ---------------- | ----------- | ------------- |
|     |     |     |     | minimised          | through       | isolating    | IoT applications | using       | network       |
|     |     |     |     | slicing.           | Also, dynamic | allocation   | of idle          | resources   | to the vic-   |
|     |     |     |     | timised            | network slice | is possible  | to keep          | the service | without       |
|     |     |     |     | any degradation    | during        | an attack.   |                  |             |               |
|     |     |     |     | B. Paper           | Motivation    |              |                  |             |               |
|     |     |     |     | IoT expands        | its roots     | over         | each and         | every field | by permut-    |
|     |     |     |     | ing unintelligible | dumb          | items        | into smart       | things      | over the last |
|     |     |     |     | few years.         | A large       | number of    | vertical         | industries  | are engaged   |
|     |     |     |     | in developing      | smart         | solutions    | at a very        | high speed  | and the       |
|     |     |     |     | community          | rapidly       | adopts these | into their       | lifestyle.  | Multiple      |
SDN and NFV can be identified as key enabling technologies surveysrelatedtoIoThavebeenconductedduringthepastfew
| for network | slicing realisation | in 5G networks | [19]. |            |                 |           |                  |            |          |
| ----------- | ------------------- | -------------- | ----- | ---------- | --------------- | --------- | ---------------- | ---------- | -------- |
|             |                     |                |       | years over | several         | subareas. | Standardisation, | security,  | archi-   |
|             |                     |                |       | tecture,   | privacy, trust, | visions,  | challenges       | and future | research |
A. Role of Network Slicing for IoT directions are some key areas that are exploited in existing
In a nutshell, 5G network architecture is designed to sup- surveys and researches.
portthreemainfundamentalserviceclasses:enhancedMobile Network slicing is a neoteric technology and numerous
BroadBand (eMBB), massive Machine Type Communications network slicing-related areas have to be investigated. The
(mMTC) and Ultra-Reliable Low-Latency Communications standardisation of network slicing is still ongoing by telecom-
(URLLC)[12].Eachserviceclasshasadiversesetofnetwork municationorganisations.Thoughitispossibletofindsurveys
requirements. Therefore, the creation of an E2E network andresearchesassociatedwithnetworkslicingwithinthepast

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 959
Fig.2. E2ENetworkSlicing.
TABLEII
SUMMARYOFIMPORTANTSURVEYSONNETWORKSLICING
few years, most of them tend to be conceptual rather than In[26],Foukasetal.reviewedstate-of-the-artnetworkslicing
technical. Table II consists of a summary of existing surveys and they have presented a framework and evaluated it under
related to network slicing. Slicing architecture, technologies the maturity of current proposals. Resource allocation algo-
thatsupportnetworkslicingrealisation,standards,securityand rithms are analysed in [27]. Issues in allocation, isolation,
use cases are the areas that are covered by most surveys. guaranteeing the inter-operability of the resources between
In [21], they have carried out a comprehensive review slices discussed in [28]. Enabling smart services in future
of network slicing with enabling technologies, standardisa- networks with network slicing and different parameters in
tion efforts, industrial projects that accelerate network-slicing networkslicingarediscussedin[29].Futureresearchareasof
usage and future research directions. The latest status of network slicing with open research problems are highlighted
3GPP standardisation, solutions to reduce the complexity in [19], [21], [22], [25], [26], [28], [29].
introduced by network slicing and future research areas dis- As with the references that we could find, there is
cussed in [22]. Network slicing architecture and some par- no single survey that specifically analyses the contri-
ticular technologies that can be used with network slicing bution of network slicing to the IoT realisation. Since
are discussed in [23]. Reference [24] discussed a signifi- network slicing is the prominent technology that rein-
cant use case in future IoT: smart grid, E2E network slicing forces IoT realisation in 5G networks, it is pertinent
with concepts, technologies, solutions and use cases are con- to analyse the associativity between network slicing and
sidered in [19]. The network slicing concept with aspects IoT, in terms of technical aspects, applications and
that support network slicing realisation is discussed in [25]. challenges.

960 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
Fig.3. PaperOrganization.
C. Our Contribution 4) A concise summary of the network slicing-related
|        |            |                     |             |       | projects | that have a impact | on IoT. |     |
| ------ | ---------- | ------------------- | ----------- | ----- | -------- | ------------------ | ------- | --- |
| In our | survey, we | broadly investigate | how network | slic- |          |                    |         |     |
ing will overcome the challenges of IoT technologies and 5) Adiscussionontheimpactoftheemergingtechnologies
|               |              |                     |             |     | in network | slicing and | IoT. |     |
| ------------- | ------------ | ------------------- | ----------- | --- | ---------- | ----------- | ---- | --- |
| their related | applications | in future networks. | Since there | are |            |             |      |     |
enoughsurveysrelatedtonetworkslicingintegrationtechnolo- 6) Apooloffutureresearchdirectionsinapplyingnetwork
slicingonseveralIoTapplicationsandtechnicalaspects.
| gies, such | as SDN and | NFV, they will | not be covered | in this |     |     |     |     |
| ---------- | ---------- | -------------- | -------------- | ------- | --- | --- | --- | --- |
survey.Acomprehensiveoverviewofthestate-of-the-arttech-
nical aspects that can be used to IoT realisation via network D. Paper Organization
slicingwillbe provided through the survey. The impact of the The paper consists of nine sections and the organisation
emerging technologies and concepts, such as blockchain and is as follows. Section II provides the background knowl-
|        |                    |               |                  | edge | of network | slicing in order | to understand | the concept. |
| ------ | ------------------ | ------------- | ---------------- | ---- | ---------- | ---------------- | ------------- | ------------ |
| AI/ML, | in network slicing | and different | IoT applications | will |            |                  |               |              |
bediscussedinhere.OurcontributiontotheIoTrealisationvia Section III focuses on improving the technical aspects related
network slicing through this paper is enumerated as follows. to IoT via network slicing. Scalability, dynamicity, security,
1) Technical aspects that can be improved via network privacy, QoS, E2E orchestration and resource allocation and
slicing in the IoT realisation. prioritisationarediscussedinhere.Networkslicingutilisation,
|             |            |                    |            | in    | several IoT | application areas, | is described | in Section IV. |
| ----------- | ---------- | ------------------ | ---------- | ----- | ----------- | ------------------ | ------------ | -------------- |
| 2) Detailed | discussion | on the utilisation | of network | slic- |             |                    |              |                |
ing for the realisation of divergent IoT use cases with Section V is allocated to discuss the technical challenges of
different network requirements. network slicing that can rise with the advancement of IoT.
3) Acomprehensive analysisofthetechnicalchallenges of Network slicing-related projects are described in Section VI
network slicing that will rise due to the advancement of and Section VII is dedicated to discuss the lessons learned
|     |     |     |     | in  | each application | and technical | aspect with | future research |
| --- | --- | --- | --- | --- | ---------------- | ------------- | ----------- | --------------- |
the IoT.

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 961
Fig.4. OverallNetworkSlicingArchitecture.
directions respectively. The impact of emerging technolo- • Infrastructure layer is responsible for providing
gies in the IoT realisation via network slicing is described physical or virtual resources such as storage, computing
in Section VIII. Finally, Section IX concludes the paper. resource and connectivity.
Graphicalrepresentationofthepaperorganisationisshownin • Networksliceinstancelayerwhichrunsovertheinfras-
Figure 3. We included the definitions of the frequently used tructure layer, consists of NSIs which form E2E logical
| acronyms | in Table | I.  |     |     |     |     | network    | slices.  |          |              |           |          |                |
| -------- | -------- | --- | --- | --- | --- | --- | ---------- | -------- | -------- | ------------ | --------- | -------- | -------------- |
|          |          |     |     |     |     |     | • Service  | instance | layer    | which        | runs      | over all | other layers,  |
|          |          |     |     |     |     |     | represents |          | end user | and business | services. |          | These services |
II. NETWORKSLICING
|         |            |          |     |     |     |     | will     | be provided | via        | service | instances | by  | the network |
| ------- | ---------- | -------- | --- | --- | --- | --- | -------- | ----------- | ---------- | ------- | --------- | --- | ----------- |
| A. What | Is Network | Slicing? |     |     |     |     | operator | or          | by a third | party.  |           |     |             |
Future mobile networks will have heterogeneous service A functional network slice basically consists of two sub-
requirements due to the wide set of new networking services. slices: the RAN subslice, specific to Next-Generation Radio
Thus, the ‘one size fits all’ networking concept is not Access Network (NG RAN) and the core subslice, specific to
applicable for 5G and beyond. Next Generation Mobile corenetwork.Anoverviewofthenetworkslicingarchitecture
|     |     |     |     |     |     |     | is shown | in Figure | 4   | and it | mainly consists |     | of four seg- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | ------ | --------------- | --- | ------------ |
Network(NGMN)Alliancefirstintroducedthenetworkslicing
concept in 2015 to address the above issue. Third Generation ments: RAN subslice, slice-paring functions, core subslice
Partnership Project (3GPP) considers network slicing as a key and the NSM. Fully data flow of some particular applica-
featurein5Gnetworks[11].Theconceptofdividingthephys- tions throughout the network is shown in the Figure 4. A
ical network into multiple logical networks (network slices) fully functional network slice is able to route and control a
|          |              |              |                     |     |       |          | particular | packet | over the | network | without | influencing | other |
| -------- | ------------ | ------------ | ------------------- | --- | ----- | -------- | ---------- | ------ | -------- | ------- | ------- | ----------- | ----- |
| so that  | each logical | network      | can be specialised  |     | to    | provide  |            |        |          |         |         |             |       |
| specific | network      | capabilities | and characteristics |     | for a | particu- | slices.    |        |          |         |         |             |       |
lar use case can be identified as network slicing [18]. 3GPP Multiple types of User Equipment (UE) can be con-
|         |         |            |               |      |         |     | nected through |     | air interface |     | or fixed-line | interface. | Thus, |
| ------- | ------- | ---------- | ------------- | ---- | ------- | --- | -------------- | --- | ------------- | --- | ------------- | ---------- | ----- |
| defines | network | slicing as | a “technology | that | enables | the |                |     |               |     |               |            |       |
operator to create networks, customised to provide optimised RAN is sliced according to different tenant requirements
|     |     |     |     |     |     |     | of each application. |     | Radio | resource | management, |     | slice spe- |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----- | -------- | ----------- | --- | ---------- |
solutionsfordifferentmarketscenarioswhichdemanddiverse
requirements (e.g., in terms of functionality, performance and cific admission control policies, the configuration rules for
isolation)” [37]. Control Plane (CP) and User Plane (UP) functions and
|     |     |     |     |     |     |     | UE awareness |     | on the RAN | configuration |     | for | the different |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | ------------- | --- | --- | ------------- |
Accordingto[19],networkslicingisbuiltuponsevenmain
principles: isolation, elasticity, automation, programmability, services are the key design aspects for RAN slicing [39].
customisation, E2E and hierarchical abstraction. Separation of RAN resources can be achieved through
frequency,time,code,hardwareequipment,softwareandother
|     |     |     |     |     |     |     | dimensions | [12]. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | --- | --- | --- | --- | --- |
B. Network Slicing Architecture RAN subslice and core subslice will be connected through
As stated by NGMN, network slicing architecture consists slice-paring functions. Paring among RAN/core slices can be
of three layers: infrastructure layer, network slice instance 1:1or1:N,e.g.,aRANslicecouldbeconnectedwithmultiple
| layer and | service | instance | layer [38]. |     |     |     | core slices | [33]. |     |     |     |     |     |
| --------- | ------- | -------- | ----------- | --- | --- | --- | ----------- | ----- | --- | --- | --- | --- | --- |

962 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
Fig.5. NetworkSlicingLifeCycle.
Core network-related functionalities related to a particular edge computing and computation offloading, the gener-
application will be provided via a core slice. Core network ated traffic flow can be made non-uniform. This scenario
resources can be sliced over servers, virtual machines or con- canbeidentifiedashorizontalnetworkslicing.Itremoves
tainers or hardware elements. Logical separation between CP theneedofhigh-resourcerequirementslikecomputation,
and UP functions and the corresponding implemented VNFs communication and storage in a device itself. Complex
shouldbeconsideredwhiledesigningCNslices.Alltheopera- tasksthatrequiredhighcomputationpowercanbehanded
tionalandmanagementtasksrelatedtoNSIswillbefacilitated overtothenexthigherlayer.Asanexample,ARandVR
via the NSM. devices need a very high computation capability, which
NSM plays a key role in network slicing architecture and cannotbeprovidedthroughexistinghardwarethatcanbe
providesampleservices.Compositionanddeploymentofnew realised through edge computing technologies.
Network Slice Templates (NSTs) is a significant service pro- Vertical and horizontal network slicing is possible with
vided by NSM. NST is the blueprint of the NSIs and it is static and dynamic network slicing.
fabricated according to the particular requirements of the ten- • Static network slicing: In here, network slices will be
ants using the network capabilities in each technical domain. pre-instantiatedanddevicesneedtoselecttheslicewhich
NSI-related activities such as status monitoring, scale in/out it is going to have the connection.
and destruction are some other functionalities provided by the • Dynamic network slicing:Operatorsareabletodynam-
NSM. ically design, deploy, customise and optimise the slices
A network slice consists of network functions and those accordingtotheservicerequirementsorconditionsinthe
networkfunctionscanbecategorisedasslice-specificnetwork network [41]. It encourages the emergence of the novel
functionsandslice-independentnetworkfunctions.Sincethere concept known as Network Slice as a Service(NSaaS).
is no consensus on selecting slice-independent network func-
tions,thiscategorisationisconsideredasanunresolveddesign
issue in network slicing realisation in 5G networks [40]. Due
D. Network Slice Life Cycle
to the relative ease of implementing core NFs as software
applications, core slicing is a less complex task than RAN NSIlifecyclecanbedividedintofourphases:preparation,
slicing. commissioning, operation and decommissioning (Figure 5).
• PreparationphaseLifecyclestartsfromthepreparation
C. Different Types of Network Slices
phase and NSI does not exist in this phase. Tasks in this
Network slices can be categorised using several models: phase are as follows.
verticalandhorizontal,staticanddynamicandRANandcore. – NST creation and verification.
RAN and core slicing have been discussed earlier. – Preparationofnecessarynetworkenvironmentwhich
• Vertical network slicing: This can be defined as parti- is used to facilitate the NSI life cycle.
tioning the network according to the use cases, whilst – Capacity planning of the network slice.
simplifying the traditional QoS problem. Here, each – Onboarding NSTs.
network domain will be sliced and then those slices will – Evaluation of the network slice requirements.
be paired using the slice paring functions to create the – Preparationofanyotherrequirementsinthenetwork.
completeslice.Withtheadventof5G,severalnewappli- • Commissioningphase:Inthisphase,NSIwillbecreated
cations, such as smart wearables, Augmented Reality from the NST. Tasks in here:
(AR)/ Virtual Reality (VR) and UHD video, became – Allocating the required network resources.
increasingly popular among the community and for each – Performing the necessary configurations to facilitate
application,averticalnetworkslicecanbeallocated.Few the slice requirements.
verticalnetworkslicescanbeidentifiedin4GLTEeither: Network slice will be ready for the operation phase after
NB-IoT slice and MTC slice [33]. this phase.
• Horizontal network slicing: A large amount of traffic • Operation phase: This phase consists of multiple sub-
is generated at the very edge of the network. Through tasks related to network slice instance:

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 963
– Activation: Activating the NSI is done in here devicesoperateinsleepandwakecycles.Thiscausesnetwork
throughtheprocesses,suchasdivertingtraffictothe resourcestobeidleorover-utilisedfromtimetotime.Network
slice and provisioning databases. slicing facilitates the dynamic allocation of idle network
– Supervision: NSI will be continuously supervised. resources of a particular network slice to another slice that
– Key Performance Indicator (KPI) monitoring : NSI demands high resource requirements. This process improves
will be continuously monitored. the scalability of the IoT network and finally, it leads to
– Modification: Upgrading NSI, reconfiguration, enhance the network performance, increase the efficiency of
changes in NSI topology, association and dis- resource utilisation and reduce the infrastructure cost [38].
association of network functions with NSI, NSI 3) Existing Slicing Based Solutions: According to the
scaling and altering NSI capacity will be handled proposed existing solutions, network slicing is identified as
under here. a solution to improve the scalability of the 5G based IoT
– Deactivation: Taking the NSI out of the active duty networks. In [45], they concluded that the network slic-
is done in here. ing has the potential to address diverse requirements of 5G
• Decommissioning phase: IoT networks that finally lead to improve the scalability of
– Reclamation of dedicated resources. future IoT applications. Their solution is more conceptual
– Reclamation of configurations from the and implementations have not been provided. The presented
shared/dependent resources. dynamic network slicing framework to improve the scala-
After this phase, the NSI does not exist anymore. bility of fog networks in [46] needs to extend to 5G core
network.Furthermore,AI/ML-basedpredictionalgorithmscan
III. THEROLEOFNETWORKSLICINGINIOT be developed to enhance resource allocation that supports
REALIZATION improving scalability of the IoT networks.
This section focuses on the technical aspects that can
be improved for the IoT realisation via network slicing. B. Improving Dynamicity
Improving scalability, dynamicity, security, privacy, QoS, and
Dynamicity describes the continuously changing nature of
E2Eorchestration,throughnetworkslicing,arediscussedhere.
something.IntroductionofIoTandIoTapplicationwillchange
thefixednatureofthetraditionaltelecommunicationnetworks.
A. Improving Scalability Dynamicity should be a key requirement for 5G and beyond
Scalability, often a sign of stability and competitiveness, network to facilitate heterogeneous IoT ecosystem and also to
is an attribute that is used to describe the ability of a pro- optimise resource utilisation.
cess, software, organisation, or network, to grow and manage 1) Description of the Limitation: IoT requires to accom-
increased demand [42]. A proper scalable network should be plish dynamicity of its network facilities in two main
able to handle the influx of traffic while utilising a limited scenarios: dynamic network resource requirements of IoT
number of resources. Network slicing has been identified by applications, and rapid temporary network deployments for
3GPPasatechnologytoimprovetheflexibilityandscalability emergency IoT applications. The quantity of resource is
innetworkingsystemsincludingIoTnetworks[43].Software- approximately remains constant for a long period in most
based network functions in network slices allow deploying telecommunication networks. Such limited and constant
network functions according to the network traffic to achieve resources have to be optimally utilised among heteroge-
scalability. neousnetworkingapplicationsincludingIoTapplications.The
1) Description of the Limitation: The number of con- amountofresourceutilizationdynamicallyvariesaccordingto
nected IoT devices will be exponentially increasing in mod- thetrafficdemandwhichleadstoresourcesbeenunder-utilised
ern telecommunication networks with heterogeneous network or over-utilised time to time. By nature, IoT applications
requirements. According to the statistics, the number of IoT are extremely dynamic and their traffic patters are fluctuat-
devices in 2020 which is 31 billion devices, will increase to ing constantly. Not only allocation of dedicated portions of
75 billion IoT devices by 2025, and 127 new IoT connections the physical network for different IoT applications, but also
will be established at every second [44]. This growth of IoT dynamically change of the resource quantity of those portions
devices will be under myriads of new IoT based applications according to traffic flow, are a vital requirement to operate an
such as smart healthcare, smart grid, autonomous vehicles, efficientIoTservices.Moreover,IoTusesinapplicationssuch
industrialautomationandAR/VRtechnologies.Frequentcon- asemergencysituations(floods,earthquakes)andmilitarysce-
nections and disconnections of nodes of various applications narios. Hence, rapid deployment of temporary IoT networks
with the network are possible. It might pave the way to cause is required to facilitate communication requirements of such
performance degradation, as well as the inability to fulfill the IoT applications. The solution should be fast and effortlessly
network requirements of a diverse set of applications. To han- deployable, and cost-effective.
dletheserecurringchangesintheIoTtrafficflow,thenetwork 2) Benefits of Using Network Slicing: Network slicing can
should be scalable. support to eliminate the static nature of the networks to
2) Benefits of Using Network Slicing: The amount of make them dynamic. Dynamic slice allocation for hetero-
the IoT traffic flow through the network is not always the geneous IoT applications and dynamic resource allocation
same. Due to the energy saving communication links, IoT between slices are two ways of improving dynamicity of the

964 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
TABLEIII
KEYIOTSECURITYATTACKS
networks via network slicing. Learning theory schemes such ransomware [59]–[62]. Network-level security solutions are
asdeeplearningandreinforcementlearning,supporttopredict vitalrequisitestomitigatetheseattacks.Securityrequirements
user demands and change the resource allocation of slices are diverse in various IoT applications. For instance, security
dynamically according to the predictions [29]. requirements in smart healthcare applications are completely
Moreover,networkslicingcanbeusedfortherealizationof different from that of a smart grid scenario. Therefore, dif-
IoT applications in critical situations. Network slicing allows ferent IoT security mechanisms are needed to fulfill these
rapid deployment of dedicated network slices with relatively diverse security requirements [63] of each IoT application in
effortless configurations over the public network. Thus, the a telecommunication network.
slicingbasedapproachiscost-effectiveandfasterthandeploy- 2) Benefits of Using Network Slicing: Network slicing
| ing whole | new | networks | for each | IoT | application. |     | In this |        |         |           |         |          |     |           |         |
| --------- | --- | -------- | -------- | --- | ------------ | --- | ------- | ------ | ------- | --------- | ------- | -------- | --- | --------- | ------- |
|           |     |          |          |     |              |     |         | can be | used to | implement | various | security |     | solutions | for the |
way,networkslicingprovidestherequireddynamicityforIoT plethora of IoT applications. Slice isolation facilitates reduc-
applications. ing the impact of the security attacks, as well as protecting
| 3) Existing | Slicing | Based | Solutions: |     | Improving | dynamic- |     |           |             |     |           |     |              |     |         |
| ----------- | ------- | ----- | ---------- | --- | --------- | -------- | --- | --------- | ----------- | --- | --------- | --- | ------------ | --- | ------- |
|             |         |       |            |     |           |          |     | sensitive | information |     | collected | via | IoT devices. |     | Dynamic |
ity in the 5G network through network slicing is a favoured deployment of security NFs in the slices allows to tackle the
area among researchers. Two areas of enabling dynamicity in attacks in run-time, without affecting other IoT applications.
network slicing, i.e., dynamic resource allocation [47], [48] The ability to create quarantine slices to isolate devices that
and dynamic slice creations for different applications [49], have suspicious behaviours facilitates to operate those devices
| that finally | improve | dynamicity |     | of IoT | networks | have | been |     |     |     |     |     |     |     |     |
| ------------ | ------- | ---------- | --- | ------ | -------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
undertighterrestrictions,untiltakingnecessaryactions.Inthis
addressed in existing solutions. Moreover, efficient resource way, network slicing can be beneficial in improving security
allocation algorithms needs to be formulated to improve of IoT applications. Table III summarises the possible attacks
dynamicity. in the IoT applications, along with the possible solutions that
|              |          |     |     |     |     |     |     | can be provided                   |     | via network |     | slicing | to mitigate          | those. |     |
| ------------ | -------- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | ----------- | --- | ------- | -------------------- | ------ | --- |
| C. Improving | Security |     |     |     |     |     |     |                                   |     |             |     |         |                      |        |     |
|              |          |     |     |     |     |     |     | 3) ExistingSlicingBasedSolutions: |     |             |     |         | Accordingtotheexist- |        |     |
Security is a fundamental requirement in IoT systems. ing research work, network slicing is identified as a way of
| Billions of | resource-constrained |     |     | devices | in heterogeneous |     | IoT |           |          |     |        |               |     |         |           |
| ----------- | -------------------- | --- | --- | ------- | ---------------- | --- | --- | --------- | -------- | --- | ------ | ------------- | --- | ------- | --------- |
|             |                      |     |     |         |                  |     |     | improving | security | of  | 5G IoT | applications. |     | In [50] | and [64], |
applicationsarenowconnectedintopeople’sday-to-daylives.
|     |     |     |     |     |     |     |     | they have | proposed | methods |     | to mitigate |     | IoT based | DDoS |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------- | --- | ----------- | --- | --------- | ---- |
Because they share sensitive information or are involved in attacks through slice isolation and edge computing respec-
| safety-critical | operations |     | [57], attackers | tend | to  | move | towards |               |        |        |     |        |             |         |     |
| --------------- | ---------- | --- | --------------- | ---- | --- | ---- | ------- | ------------- | ------ | ------ | --- | ------ | ----------- | ------- | --- |
|                 |            |     |                 |      |     |      |         | tively. While | secure | keying |     | scheme | for network | slicing | was |
IoT applications.
|                |     |        |             |      |        |     |         | presented     | in [56], | service-oriented |          | authentication |            | framework      |     |
| -------------- | --- | ------ | ----------- | ---- | ------ | --- | ------- | ------------- | -------- | ---------------- | -------- | -------------- | ---------- | -------------- | --- |
| 1) Description |     | of the | Limitation: | Most | of the | IoT | devices |               |          |                  |          |                |            |                |     |
|                |     |        |             |      |        |     |         | was presented |          | in [35].         | However, | new            | scientific | investigations |     |
areresourceconstraintsindesign.Thus,itisdifficulttoimple-
|     |     |     |     |     |     |     |     | have to | be conducted |     | in mitigating |     | other | types of | security |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ------------- | --- | ----- | -------- | -------- |
mentsecuritysolutionsonIoTdevices.Devicevendorstendto attacks by using network slicing.
| use common     | credentials |               | for IoT   | devices | and         | most of      | device  |              |         |     |     |     |     |     |     |
| -------------- | ----------- | ------------- | --------- | ------- | ----------- | ------------ | ------- | ------------ | ------- | --- | --- | --- | --- | --- | --- |
| consumers      | do not      | care          | to change | these   | default     | credentials. |         |              |         |     |     |     |     |     |     |
|                |             |               |           |         |             |              |         | D. Improving | Privacy |     |     |     |     |     |     |
| This increases | the         | vulnerability |           | of the  | IoT devices |              | to dic- |              |         |     |     |     |     |     |     |
tionary attacks, while being used by consumers [58]. This Along with the expansion of IoT systems worldwide, the
will help adversaries gain control of the IoT devices. Such necessity of schemes for protecting the privacy of exchanged
potential reasons may result in a series of different types of IoT data has increased. Preserving data privacy plays an
attacksinIoT,suchasDistributedDenialofServices(DDoS), ever-increasing role in the IoT applications, which collect
Man In The Middle (MITM), Zero-day, IoT botnets and sensitive measurements [65].

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 965
TABLEIV
KEYIOTPRIVACYISSUES
TABLEV
QOSREQUIREMENTSOFDIFFERENTIOTAPPLICATIONS
1) DescriptionoftheLimitation: Theworldwidespreading 3) Existing Slicing Based Solutions: Network slicing can
of IoT devices results in the need for transmitting collected be used to ensure the privacy of IoT applications, but scien-
data to remote data centres that requires to be further pro- tific investigations that are directly addressing this area are
cessed. This has to follow several data privacy standards quite limited. Moreover, some of the existing work can be
and regulations, which may be international or specialised furtherextended.AnIoTusercase-specificprivacy-preserving
for a particular geographical region, such as General Data communication scheme presented in [67] can be extended to
ProtectionRegulation(GDPR)[66].Implementingthisdiverse generalapplications.In[35],Nietal.proposedanefficientand
set of standards and regulations, corresponding to the geo- secure service-oriented authentication framework supporting
graphicalspecificationsisavitalrequirement.Privacyrequire- network slicing 5G-enabled IoT services.
ments are drastically difference in different IoT applications.
For instance, the privacy requirements in a smart healthcare
E. Improving Quality of Service (QoS)
applicationarecrucialthantherequirementsinanenvironmen-
tal monitoring application. Facilitating such diverse privacy QoS can be defined as a form of traffic control mechanism
requirements of IoT applications over traditional telecommu- thatguaranteestheabilitytorunhigh-priorityapplicationsand
nication networks is a burdensome task. traffic under limited network capacity. The measurements of
2) Benefits of Using Network Slicing: Allocation of sepa- concern in QoS are bandwidth (throughput), delay (latency),
ratesliceswithpropersliceisolationmechanismsforeachIoT jitter (variance in latency) and error rate. Different combina-
application, along with required privacy-preserving network tions of these properties are essential in increasing the quality
functions, helps to satisfy the diverse privacy requirements of IoT applications.
of IoT applications. Robust authentication mechanisms and 1) Description of the Limitation: The IoT has prolifer-
strong slice isolation techniques deny the access to a partic- ated within massive application areas that need diverse QoS
ular slice from other slices to protect the confidentiality of requirements for their optimal behavior. As an example, QoS
the IoT application data. The ability to changing the VNF requirements in autonomous vehicle applications, such as
structure of the slices dynamically enhances the difficulty of very low latency and ultra-reliability, are completely different
breakingprivacypreservingmechanisms.Inthisway,network from the requirements in environmental monitoring applica-
slicingcanimprovetheprivacyofIoTapplications.Table[IV] tions. Facilitating all these heterogeneous QoS requirements
describes the privacy issues in different IoT scenarios, along of different IoT applications through the same infrastruc-
with possible solutions that can be provided through network ture entails a revolutionising re-engineering of the network
slicing for ensuring privacy. architecture [68]. Even in congestion situations, QoS control

966 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
allows us to fulfill sufficient service quality requirements of G. Better Resource Allocation and Prioritization
the IoT applications with high priority classification. Table V
IoT networks uses several types of network resources such
illustrates the requirement of different QoS for different IoT
ascomputing,storageandnetworkingresources.Itisrequired
applications [69].
theallocatetheseresourceefficientlytooptimizedtheresource
2) Benefits of Using Network Slicing: Network slicing utilization.
ensures facilitating QoS requirements of different IoT appli- 1) Description of the Limitation: IoT networks are con-
cations, through allocating dedicated slices for each use case. sists billions of connected devices which support different use
Dynamic resource allocation between slices allows us to cases with heterogeneous network requirements. The alloca-
accomplish QoS requirements in congestion situations [70]. tionofphysicalnetworkresourcesforsuchvastamountofIoT
3) Existing Slicing Based Solutions: Based on the existing devicesisacomplextask.Specially,thedynamicnatureofIoT
related works, QoS requirements of different IoT applications services will leads to constant fluctuation in resource utiliza-
canbefacilitatedthroughnetworkslicing.In[68],Yousafetal. tion. Moreover, the amount of available network resources is
presented an architecture to provide QoS requirements of the always limited in SP networks. Thus, it is essential to man-
slices. In [71], Höyhtyä et al. used network slicing as an age these limited resources efficiently. However, most of the
enabling technology inproviding QoS requirements incritical time, SPs struggle to utilise the available resources efficiently.
scenarios over the public networks. Automated slice resource Moreover,someofthemissioncriticalanddelaysensitiveIoT
allocation frameworks can be utilized to maintain the QoS applications such as autonomous vehicles, robotics and AR
level of highly dynamic IoT applications. applications might need prioritization of allocated resources
over other IoT applications [76].
2) BenefitsofUsingNetworkSlicing: Networkslicing,that
F. Providing End-to-End Orchestration implies the allocation of resources [28], can be considered as
theoptimaltechnologytosatisfydiversenetworkrequirements
Whenever a service enabled in a network, the life time
of 5G IoT applications. The primary idea of network slic-
of that service has to be managed for proper operation. The
ing is analogous to the concept of Infrastructure as a Service
service End-to-End orchestrator is responsible for provision,
(IaaS)incloudcomputing,thatsharescomputing,storageand
management and optimization of resources for that particular
networkingresourcesamongtenants[27].Moreover,thechal-
network service.
lenge of varying nature of amount of required resources for a
1) Description of the Limitation: Rapid expansion of IoT
particular IoT use case can be overcome by dynamic adjust-
withinaplethoraofapplications,increasesthenumberoften-
ment of allocated resources for each slice via automated slice
ants and different stakeholders who involve in managing the
manager functions [77]. Moreover, network programmability
ecosystem. As an example, in a smart transportation applica-
is a basic element of network slicing that allows us to alter
tion, road authorities, manufacturing companies, maintenance
thenetworkresourceutilisationdynamicallyamongIoTappli-
teams, need to cooperate for the well-being of the applica-
cations. Network slicing allows us to prioritize traffic in two
tion. Cooperation these multiple parties is a challenging task.
techniques:user/trafficprioritizationviasimultaneousmanage-
With the augmentation of IoT services, the amount of con-
ment of the priority among different slices, and prioritization
trol channel data related to IoT flown through the network
users belong to same slice [47].
increases. Hence, a proper mechanism is required to mitigate
3) Existing Slicing Based Solutions: Network slicing
the challenge of managing the amount of IoT control data.
is recognised as a superlative technology for allocat-
2) BenefitsofUsingNetworkSlicing: Networkslicingpro-
ing required network resources to miscellaneous applica-
vides a solution for this matter through reducing the network
tions in current related works. Radio resource allocation
complexity, by dividing the network into small manageable
frameworks [78], [79] and a hierarchical resource allocation
parts. It supports a wide range of customers’ and operators’
framework [80] for network slicing have been presented for
requirements by allowing them to execute required config-
this. Mathematical models for resource allocation between
uration changes at run time to their slices [72]. Increased
slices were developed in [27]. Since most of the proposed
operational complexity due to a large number of created cus-
resource allocation algorithms are specific to single domain,
tomised networks can be resolved by an end-to-end network
E2E resource allocation algorithms can be identified as a
sliceorchestrator.TheIoTworldcanbeenvisionedasthemost
possible future research direction in this aspect [27].
suitable exploitation for a self-managed and isolated slice of
network resources [73].
3) Existing Slicing Based Solutions: E2E orchestration of
IV. NETWORKSLICINGBASEDIOTAPPLICATIONS
divergent applications is identified as a critical requirement in IoT has been used in many application domains. These IoT
modernnetworksandhavebeenproposedseveralarchitectures applications can be categorised into four key areas accord-
facilitatingthisrequirement.Networkslicingmanagementand ing to their requirements (Figure 6). This section focuses
orchestration architectures [72], [74] and such an architec- on discussing key use cases/applications of IoT and how
ture with federated slicing [75] were proposed to serve this network slicing can be used to overcome the challenges in
requirement. Slice orchestration over multi-domains is dis- these applications. Table VI describes a concise summary of
cussed as a novel scope in E2E orchestration and it can be possible slicing solutions for each IoT application scenarios
further investigated. with required technical aspects.

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 967
Fig.6. IoTapplicationscenarios.
| A. Smart                  | Transportation |           |                    |                       |                    |               |        |
| ------------------------- | -------------- | --------- | ------------------ | --------------------- | ------------------ | ------------- | ------ |
| With                      | the mass       | evolution |                    | of the                | transportation     | system,       |        |
| IoT has                   | tightly        | coupled   |                    | with several          | areas              | in            | trans- |
| portation,                | along          | with      | vehicle-to-vehicle |                       | communication,     |               |        |
| vehicle-to-infrastructure |                |           | communication,     |                       | autonomous         |               | or     |
| semi-autonomous           |                | driving   | and                | in-car                | infotainment       | systems.      |        |
| Ultrareliability          |                | and       | very               | low latency           | are                | critical      | com-   |
| munication                | requirements   |           | in                 | Vehicle-to-Everything |                    |               | (V2X)  |
| applications              | [111].         | Four      | different          | types                 | of                 | communication |        |
| modes of                  | V2X            | are       | identified         | by 3GPP:              | vehicle-to-vehicle |               |        |
Fig.7. NetworkSlicing&SmartTransportation.
| (V2V),    | vehicle-to-infrastructure |     |     | (V2I), | vehicle-to-pedestrian |     |     |
| --------- | ------------------------- | --- | --- | ------ | --------------------- | --- | --- |
| (V2P) and | vehicle-to-network        |     |     | (V2N). |                       |     |     |
1) The Role of Network Slicing in Smart Transportation: the resource requirements of the V2X use cases. Network
V2X covers multiple use cases, such as V2V, V2P, V2I and slicing can provide guaranteed level of network resources
V2N. Each use case has heterogeneous service and connec- for V2X use cases via isolating V2X resources from other
tivity requirements that cannot be facilitated through a single application specific slices. Dynamic deployment of network
networkinfrastructure.Networkslicingistheoptimalsolution functions according to the time of the day (peak and off-
to fulfill these requirements in a cost-effective manner. New peak) or type of area (rural or urban) increases the efficiency
players such as road authorities, vehicle manufacturers and of the network resource utilisation. Moreover, strong security
municipalitiesthatprovidemultipleserviceswillparticipatein mechanisms can be provided to the communication of dif-
theV2Xscenario,ratherthanthetraditionalnetworkprovider. ferent V2X applications through dedicated security network
| It is difficult |     | to support | these | multiple | tenants | via | infras- slicing. |
| --------------- | --- | ---------- | ----- | -------- | ------- | --- | ---------------- |
tructure owned by different operators. A proper set of slice Figure 7 shows a brief overview of the network slicing
templatescanbedevelopedtoconsummatetherequirementsof utilisation in smart transportation use case. Four different
multiple tenants. To manage the high density of moving vehi- slices (autonomous vehicles, teleoperated vehicles, remote
cles, deployment of network functions in the network should diagnostic and management and vehicle infotainment systems
be changed dynamically. Also, variations of resource utilisa- with diverse network requirements) are depicted here. A
tioninnetworkresourcesbyotherusecasesshouldnotviolate slice for autonomous vehicles can be used to facilitate

968 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
TABLEVI
ROLEOFSLICINGFORIOTANDITSPERTINENTDEPLOYMENTCHALLENGES
communication requirements of self-driving cars. Another vehiclesimultaneously:sliceforautonomousdrivingandother
slice for teleoperated vehicles can be utilised to manage vehi- safety-critical services, slice supporting teleoperated driv-
cles remotely in environments that are either dangerous or ing, slice for vehicular infotainment and slice for vehicle
unfavourable for humans. Communication between car manu- remote diagnostic and management. A reference network-
facturers or diagnostic centres and vehicles can be facilitated slicingarchitectureforV2Xservicesisproposedin[82],based
viaaslicededicatedforthisspecificpurpose.Toprovideinfo- onathree-layermodel[112]:infrastructurelayer,servicelayer,
tainment services such as Web browsing, HD video streaming business layer and Management and Orchestration (MANO).
and social media access for passengers, a separate slice can In[83],Khanetal.haveanalysedtheperformanceofnetwork
be allocated. slicinginavehicularnetwork,usingamulti-lanehighwaysce-
2) Related Works: Facilitating communication require- nario with two logical slices (the infotainment slice and the
ments of smart transportation applications through network autonomous driving slice). They showed that their network
slicing have been comprehensively discussed in existing solu- slicingapproachoutperformsthedirectRoadSideUnit(RSU)
tions. method, while attaining high reliability and throughput. Air-
In [81], Campolo et al. stated that heterogeneous require- GroundIntegratedVEhicularNetwork(AGIVEN)architecture
ments of V2X services cannot be mapped into reference is proposed in [113], to provide high capacity with seamless
slices in 5G: eMBB, mMTC, URLCC or into a single coverage. The proposed architecture is divided into multiple
V2X slice. Besides that, they propose a set of slices for slicestosupportaspecificapplicationwhileguaranteeingQoS
identified V2X use cases that may be consumed by a single requirements.

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 969
|     |     |     |     |     |     |     | 2) Related |       | Works:              | Several | slicing-based | implementations |     |         |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ------------------- | ------- | ------------- | --------------- | --- | ------- |
|     |     |     |     |     |     |     | can be     | found | in Industrial       |         | automation    | domain.         |     | In [84] |
|     |     |     |     |     |     |     | and [117], | Wu    | et al. demonstrated |         | a practical   | scenario        |     | in con- |
ditionalmonitoringtoachieveself-organisationandflexibility,
withoptimalutilisationofnetworkresourcesinIIoTnetworks
|     |     |     |     |     |     |     | via network | slicing.  | One        | of    | the challenges      | in  | IIoT | networks |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ---------- | ----- | ------------------- | --- | ---- | -------- |
|     |     |     |     |     |     |     | that they   | addressed | in         | their | demonstration       | was | the  | require- |
|     |     |     |     |     |     |     | ment of     | a quickly | accessible |       | and self-organising |     |      | network. |
Anotherchallengetheyaddressedwasthenecessityforaflexi-
blenetworktoachievediverseQoSrequirementsfromvarious
|     |     |     |     |     |     |     | services, | as well | as on-demand |     | optimisation |     | of the | network |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------------ | --- | ------------ | --- | ------ | ------- |
Fig.8. NetworkSlicing&Industrialautomation.
|     |     |     |     |     |     |     | efficiency. | Results | from    | their   | demonstration | show     | the    | useful- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ------- | ------- | ------------- | -------- | ------ | ------- |
|     |     |     |     |     |     |     | ness of     | network | slicing | in IIoT | systems.      | In [85], | Kalør, | et al.  |
However, improving security and privacy of V2X network discussed how network slicing can be used to overcome the
challengesintraditionaltelecommunicationsystems,byintro-
slicesandefficientresourceallocationalgorithmsforensuring
ducingprogrammabilityandflexibilitytoIIoTnetworks.They
networkrequirementscanbefurtherinvestigatedintransporta-
|     |     |     |     |     |     |     | have used | Industry | 4.0 | use | case to show | the | network | slic- |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | --- | ------------ | --- | ------- | ----- |
tion applications.
|               |             |            |     |            |     |     | ing usage | to achieve |               | a diverse | set of         | requirements. |     | In [86], |
| ------------- | ----------- | ---------- | --- | ---------- | --- | --- | --------- | ---------- | ------------- | --------- | -------------- | ------------- | --- | -------- |
|               |             |            |     |            |     |     | Theodorou | et         | al. presented |           | a cross-domain | network       |     | slicing  |
| B. Industrial | Automation/ | Industrial |     | IoT (IIoT) |     |     |           |            |               |           |                |               |     |          |
solutiondevelopedforEU-fundedresearchprojectVirtuWind,
Fourth industrial revolution (Industry 4.0) [114], the novel for an industrial wind park scenario. A two-level hierarchi-
enhancement in the industrial automation systems, intro- cal structure had been proposed to management and control
duces modern communication and computation technolo- of the network resources. The network slicing process also
gies such as cloud computing and IoT to industrial man- depends on this two-level hierarchical structure. In [118],
ufacturing systems [115]. As a result, a large number of Baddeleyetal.proposedinitialeffortstocreatededicatedSDN
IoT devices, machines and applications with heterogeneous control slices in IIoT networks. They have demonstrated the
network requirements will connect with each other through task using IETF 6TiSCH tracks.
the network for the realisation of industry 4.0 [116]. Utilising Moreover, federated slicing and hierarchical slicing can be
connected IoT based machines rather than human labor with considered as novel research directions related to network
remote monitoring and supervision in a production line will slicing in industrial networks.
| increase        | the efficiency | of the       | system  | while | reducing           | the |          |            |     |     |     |     |     |     |
| --------------- | -------------- | ------------ | ------- | ----- | ------------------ | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
| cost. Different | types          | of IoT based | sensors |       | can be distributed |     |          |            |     |     |     |     |     |     |
|                 |                |              |         |       |                    |     | C. Smart | Healthcare |     |     |     |     |     |     |
throughoutthefactorytomonitortheenvironmentalconditions
and status of the machines for reducing unplanned downtime. Similartotheotherapplicationareas,IoTisheavilyusedin
1) The Role of Network Slicing in Industrial Automation: the healthcare system under various use cases [119]. Recent
Existing traditional networks are not capable of fulfilling the advances in IoT are identified as a potential solution to alle-
|                       |     |               |     |           |              |     | viate the | pressures | on  | the healthcare | systems, | such | as  | medical |
| --------------------- | --- | ------------- | --- | --------- | ------------ | --- | --------- | --------- | --- | -------------- | -------- | ---- | --- | ------- |
| diverse communication |     | requirements, |     | like high | reliability, | low |           |           |     |                |          |      |     |         |
latency and high data rates, of Industrial IoT (IIoT) applica- staff shortage and high healthcare costs, while maintaining
tions. Network slicing is a viable option for supporting the quality care to patients [120]. Remote surgery is one of
diverse set of network requirements using the same physical the mission-critical IoT healthcare applications that enables
network infrastructure cost-effectively. Changing the NFs, in patients to get the service of a set of consultants who are
|          |              |             |     |             |          |       | in different | places | around | the | world. Remote |     | monitoring | of  |
| -------- | ------------ | ----------- | --- | ----------- | -------- | ----- | ------------ | ------ | ------ | --- | ------------- | --- | ---------- | --- |
| terms of | location and | structuring | of  | the slices, | achieves | vari- |              |        |        |     |               |     |            |     |
ous combinations of the properties, such as security, mobility, eldersandpatientswhoneedscontinuousmonitoring,isanIoT
latency and bandwidth. It is possible to allocate a dedicated application that requires communication services with ultra-
slice with guaranteed network resources for a particularly reliabilityandlowlatency[121],[122].Aswiththeprodigious
large-scale factory line to accomplish their communication development in the robotic field, employment of humanoid
requirements. robots near elderly people will support them to live indepen-
Possible use of network slices in a factory environment dently at home. Wearable IoT devices is becoming popular in
are shown in the Figure 8. Factory environment management, multiple remote monitoring scenarios, such as glucose, ECG,
remote operation of the machines and remote diagnostic and blood pressure and heart rate, for the purpose of avoiding
maintenance are the probable scenarios that require separate preventable deaths [123].
slices. Thousands of sensors and actuators in the factory can 1) The Role of Network Slicing in Smart Healthcare:
be connected together via a dedicated slice, for managing the Heterogeneous communication service requirements in the
factory environment effectively. Workers and machines in the diverse set of IoT use cases in the modern healthcare system
factory can be connected together through a separate slice for cannot be accomplished through the traditional telecom-
remote operation. Machine manufacturers or diagnose centres munication network. Higher data capacity and extremely
andthemachinescanbecoupledsecurelythroughadedicated fast response time, received through novel 5G technolo-
slice to optimize the machines maintenance process. gies, support faster and more accurate results needed for

970 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
|     |     |     |     |     | use case       | for highlighting | the necessity | of            | managing | network     |
| --- | --- | --- | --- | --- | -------------- | ---------------- | ------------- | ------------- | -------- | ----------- |
|     |     |     |     |     | slices through | defining         | the remote    | healthcare    | slice    | for various |
|     |     |     |     |     | requirements   | of dynamic       | healthcare    | environments. |          | In [124],   |
Priesetal.demonstratedallocatinganetworksliceforasmart
|     |     |     |     |     | health use | case, that      | connects a | smart wearable     |     | device with |
| --- | --- | --- | --- | --- | ---------- | --------------- | ---------- | ------------------ | --- | ----------- |
|     |     |     |     |     | a specific | traffic pattern | to the     | cloud efficiently. |     | Innovative  |
eHealthsystem,poweredby5Gnetworkslicing,wasproposed
|     |     |     |     |     | in [89]. | In there, they | have studied | the | health | data collec- |
| --- | --- | --- | --- | --- | -------- | -------------- | ------------ | --- | ------ | ------------ |
Fig.9. NetworkSlicing&SmartHealthcare. tion and analysis from various IoT medical devices via 5G
networks.Dynamicprovisioningof5Gslicesaccordingtothe
|     |     |     |     |     | medical | devices with | diverse requirements |     | was considered | in  |
| --- | --- | --- | --- | --- | ------- | ------------ | -------------------- | --- | -------------- | --- |
patients’ remote monitoring and examination in the health- their proposed architecture.
| care domain     | [87]. Since   | the lion’s share   | of the       | healthcare |          |          |      |     |     |     |
| --------------- | ------------- | ------------------ | ------------ | ---------- | -------- | -------- | ---- | --- | --- | --- |
| applications    | directly deal | with the patients’ | lives,       | communi-   |          |          |      |     |     |     |
|                 |               |                    |              |            | D. Smart | Home and | City |     |     |     |
| cation services | used          | in the healthcare  | applications | such as    |          |          |      |     |     |     |
remotesurgeriesshouldhavesupremereliability.Whilemain- The smart home concept is extended up to smart offices,
taining the promising network resource allocation for these smart buildings and finally, to smart cities. Making people’s
critical healthcare applications, disturbances that will gener- lives smarter through automating day-to-day activities, cost
ate through the variation of resource utilisation from other reductionandenergypreservationaremajoradvantagesofIoT
applications should be minimised. Network slicing is the pro- utilisation in smart home and city applications. Smart home
pitious technology that allows achieving this requirement via applications are ranging from a simple temperature sensing
slice isolation. The ability to allocate resources dynamically system that automates the functionality of the air conditioner,
tohealthcareslicesalleviatestheresourceconsumptionsurges toanadvancedimageprocessingsystemthatidentifiesintrud-
generated through the Internet of Medical Things (IoMT) ers, to increase the protection. Despite the advantages of IoT
devices. Security and privacy are primary concerns in the from a smart home perspective, the rate of adoption of IoT
healthcare industry, since it deals with sensitive data of the devices to their homes by users depends on their desire to
people. Additional security and privacy can be provided by buy those devices. Security and convenience have been iden-
deployingmoresecurityandprivacyrelatednetworkfunctions tified as the key factors that influence their decision [125].
in healthcare slices. Slice isolation removes the visibility of Rapidpopulationgrowthandurbanisationaroundcitiestendto
healthcare traffic flow to other application slices. utilisemostoftheresourcesaroundtheearthinaverylimited
Figure 9 explains how different network slices can be used space. This dramatic expansion of cities should be addressed
|     |     |     |     |     | sustainability | while increasing | the | quality | of life. | The IoT has |
| --- | --- | --- | --- | --- | -------------- | ---------------- | --- | ------- | -------- | ----------- |
inthesmarthealthapplications.Forthissector,separateslices
forremotesurgeries,remotehealthmonitoringandsmarthos- been made use of to tackle these issues with the smart city
| pitalsareidentifiedasrequired.Applicationsinvolvingremote |     |     |     |     | concept | [91]. |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | ------- | ----- | --- | --- | --- | --- |
surgeries that demand network requirements, such as very 1) The Role of Network Slicing in Smart HomeandCity:
high throughput, ultra-reliability and very low latency, can be Heterogeneity of IoT devices in homes is varied from very
includedintoaseparateslice.Remotehealthmonitoringappli-
|     |     |     |     |     | primitive | devices with | very limited | energy, | to  | very power- |
| --- | --- | --- | --- | --- | --------- | ------------ | ------------ | ------- | --- | ----------- |
cations and wearable devices can be connected to a dedicated ful devices that need a continuous power supply and from
slice to provide a secure communication. Medical appliances insecure devices, to devices with very high-security mecha-
in a hospital can be networked to a centralised location via a nisms[92].Sincesecuritydeviceslikedoorlocks,surveillance
dedicated slice. cameras, lights, sirens, smoke detectors and garage door
2) Related Works: In terms of providing required secu- openers deal directly with the security of homes, intruders
rity, latency and reliability requirements of healthcare-related who take control of those devices are able to create neg-
IoT applications, network slicing is recognised as a dominant ative effects to the homeowners. Network slicing is a way
solution in existing related works. to eliminate such negative effects to some extent through
In[87],Mavrogiorgouetal.proposedaplatformtomanage slice isolation and implementing various security functions
healthcare data efficiently with the use of the latest tech- in the smart home slice. Smart city applications such as
niquesinnetworkslicing,dataacquisitionanddataoperability. waste-management systems, automated-road-lamp systems,
Through the developed platform, they were able to identify connected-traffic-control systems and smart-parking systems
unknown devices and collect their data to assign that into a will be connected together to facilitate centralised manage-
particular slice to inter-operate with other IoMT devices. ment. Since a majority of these IoT devices are very simple
In [88], Celdrán et al. proposed an architecture to manage and use batteries, energy-efficient communication services is
the life cycle of network slicing, while addressing resource avitalrequirementwithveryhighsecurity,asitdealsdirectly
orchestration problems, in terms of what, when and how. A with the daily living styles of the people who live in the city.
policy-basedsystemwithtwotypesofpolicies,intra-slicepoli- Networkslicingistheprominenttechnologytofulfillthecom-
cies and inter-slice policies, is defined to control the network municationrequirementsofsuchdevices.Thiscanbedonevia
slices,aswellastochangetheresourceallocationtotheslices allocating a separate slice with lightweight network functions
dynamically. They have thoroughly examined the remote care and isolating this traffic stream from other traffic.

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 971
Fig.11. NetworkSlicing&AR/VR/Gaming.
contribution to facilitate indispensable services like remote
Fig.10. NetworkSlicing&SmartCity&Home.
surgeries, tourism industry, remote meetings, retail, market-
ing and smart education, as well as entertainment activities.
Some of the possible network slices with their network In [96], Alam et al. proposed a monitoring and safety system
capabilities in a smart home and city environment is depicted using AR/VR technologies and various IoT devices. Remote
in Figure 10. Though a large number of slices is realisable monitoring and supervision are possible with the proposed
in a smart home and city environment, five key scenarios solution. The traditional gaming industry has faced a mas-
among them are shown in the figure: eMBB services, home sive transformation along with AR/VR technologies with IoT
management, waste-management system, traffic-management devices. It is viable to connect multiple players around the
system and energy-management system. Since eMBB devices world to the gaming environment and enhance the gaming
are distributed over smart homes and smart cities, they can experience, rather than playing in a isolated environment. A
be connected to a single dedicated slice. Smart devices in a rapid growth of the VR-based gaming market was achieved
home can be connected to a distinct slice to assure secure over the past few years, due to the development of innova-
communication. tive accessories and wearables. The majority of startups who
enter the electronic games industry tend to engage with VR
2) Related Works: In [92], Dzogovic et al. proposed a
technology to develop their games [127].
network slicing-based smart home system, using three differ-
ent end-to-end slices. Slice dedicated to the home security 1) The Role of Network Slicing in AR, VR, and Gaming:
system, eMBB slice to devices that demand high data rates Morelatencycausesexperiencing disorientationanddizziness
and massive IoT network slice to provide low-data rates (cyber-sickness) to users while consuming AR/VR devices.
for low-power devices are proposed in the paper. In [93], Hence, the Motion-To-Photon (MTP) latency is required to
Chaabnia and Meddeb presented a model for smart home, keep less than 20ms. Accordingly, considerable range for
using network slicing. In their scheme, smart home appli- network-side latency must be 5 to 9ms [128]–[130]. Existing
cations are sliced into four different classes according to traditional networks are not capable to facilitate this require-
theirusage,bandwidthrequirementsandtraffictype.In[126], ment. In the cases of remote surgeries and virtual meetings,
Boussard et al. presented an end-to-end research solution, security and privacy are critical requirements, since they are
called Future Spaces, based on SDN and NFV, to dynami- directlydealingwiththesensitiveinformationofmankind.AR
cally control people’s digital assets. They have used network and VR-related applications need very high data rates. For a
slices to provide secure access to devices. low resolution, 360 degree AR/VR video requires bandwidth
around 25Mbits/s, and according to the quality of the video,
the required bandwidth ramps up significantly [128], [129].
E. AR, VR and Gaming
These heterogeneous network requirements can be facilitated
Augmented Reality (AR), which brings digital elements to through network slicing. The standard eMBB service scenario
liveview,andVirtualReality(VR),whichcompletelyreplaces in the novel 5G architecture is designed to facilitate these
the live view with a digital view, are the novel technologies kinds of applications. Customised network slices can be used
that have the ability to join the physical world and digi- toprovidespecificnetworkcharacteristicsoftheAR/VRappli-
tal world. AR, one of the disruptive technologies developed cations that cannot be facilitated through the standard eMBB
under the expansion of IoT, is used to improve the interaction slice.
between human and computer in a more entertaining manner Figure 11 shows the allocation of different network slices
within smart environments [94]. Mobile phones can be used in the AR/VR/gaming applications. Since AR/VR entered a
as AR visors at the early stage, to evaluate the effectiveness plethora of application scenarios, it is feasible to categorise
ofARinIoT.Afterthis,thetransitioncanbedonetomultiple those scenarios within three slices, according to the network
alternativeoptions,suchashead-mounteddisplayslikeGoogle requirements as depicted in the figure: slice for AR/VR in
Glass, Magic Leap Lightwear and Microsoft Hololons, and entertainment that includes real-time games, slice for AR/VR
other wearables that allow users hands-free interaction with inhealthcareandsliceforAR/VRingeneralapplicationssuch
IoT services and objects [95]. VR with IoT provides a huge as education, business, and tourism.

972 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
2) RelatedWorks: In[131],Estevesetal.proposedaProof-
of-Concept (PoC) to use the user’s location to the placement
of a network slice. They considered an interactive-gaming
event that has multiple players who access the gaming appli-
cationsimultaneously,inimplementingtheirPoC.Adedicated
network slice is used to facilitate the QoS/QoE requirements
ofthegamingserviceprovidertousers.In[132],SKTelecom
Fig.12. NetworkSlicing&Militaryapplications.
and Ericsson reported that their ability to create different
virtual network slices optimised for AR services.
SinceAR/VRisrelativelyarecentapplicationarea,network
howtoimplementcriticalcommunicationservicesoveracom-
slicing utilisation is not much covered in existing scien-
mercial 5G mobile network. They also talked about creating
tific investigations. However, AR/VR realisation via network
rapidly deployable networks for emergency and tactical oper-
slicing has been proved only by some companies through
ations, using techniques such as network slicing and licensed
demonstrations [132].
shared access.
Figure 12 explains how network slicing facilitates network
requirementsinthemilitaryIoT.Twoimportantcasesforallo-
F. Military Applications cating slices have been identified and they are shown in the
figure:sliceforabattlefieldandsliceforgeneraldefensecom-
IoT integration with technologies, such as wireless sensor
munication. Fast temporary deployments of slices dedicated
networks, embedded systems, M2M communications, cloud
to a battlefield can facilitate communication requirements of
computing and mobile applications, has the potential to
drones, smart weapons and soldiers. A portion of the public
serve mission-critical military applications. IoT deployment
network with high security mechanisms can be permanently
in military applications has primarily focused on battlefield
allocated to general-defense communications.
applications. Millions of sensors deployed on multiple appli-
2) Related Works: In [133], Grønsund et al. discussed the
cations are used to serve the systems of Command, Control,
implementation of military communication services over the
Communications, Computers, Intelligence, Surveillance and
5G network via network slicing. They proposed two network
Reconnaissance (C4ISR). The situational awareness gained
slices for military mobile users: military slice for military
through those sensors helps senior commanders to steer the
services which requires more restricted access and security
battalion and helps warfighters to combat strategically [97].
and commercial slice for traditional services. The methodol-
In [98], Wrona discuss some important use cases for IoT
ogy of providing the basic service requirements of military
deployment inmilitaryapplications, suchassmartequipment,
communications such as isolation, security, high availability,
situational awareness, logistics and medical care. Military IoT
QoS,andperformance,vianetworkslicinghasbeendiscussed.
(MIoT) supports to realise the concept of “anytime, anyplace
Moreover, they described the basic implementation of the
connectivity for anything, ubiquitous network with ubiquitous
military slice based on the 5G URLCC slice.
computing” in the military domain. It increases the efficiency
of the utilisation of military resources via implementing and
managing military diversification affairs more accurately and G. Smart Energy
dynamically [99]. Use of IoT-aided robotics in military appli- The smart grid can be identified as an electrical system
cations are discussed in [100] within the following activities: that consists of operations such as electricity generation,
detection of hazardous chemicals and biological weapons, transmission, distribution, control and consumption. It uses
autonomous vehicles in battlefields, support on civil opera- two-way flows of electricity and information, along with
tionsinwarfields,deactivationofnuclearweaponsandaccess computational and communication technologies to achieve an
control of people in restricted areas. automatedanddistributedenergy-deliverynetwork,withprop-
1) The Role of Network Slicing in Military Applications: ertiessuchasclean,safe,secure,efficient,sustainable,reliable
End-to-end secured communication is a crucial requirement and resilient [101]. The overall efficiency of the integrated
in the battlefields for scenarios like communication between power grid can be improved by using the IoT to form an
soldiers and the control centre and transmission of the interactive real-time network connection between the users
information gathered by the IoT devices. Using an exist- and power equipment [102]. All kinds of components such
ing public network infrastructure with large coverage is a as transformers, breakers, meters and capacitors in the grid
cost-effective solution. Without specifying a separate slice in can be made intelligible through IoT. It facilitates the advan-
the physical network with appropriate security functions and tagessuchasenhancingcustomerengagement,optimisationof
strong slice isolation mechanisms, security requirements can’t renewable energy and reducing maintenance costs. In [103],
beaccomplished.IntheapplicationssuchasIoT-aidedrobotics Sarwatetal.dividethesmartgridintothreemainlogicalenti-
and Unmanned Aerial Vehicles (UAVs), very low latency, ties: Functional Entity (FE), Operational Entity (OE) and IoT
ultra-reliability, and high bandwidth are critical network Entity (IE). The IE entity is responsible for making the smart
requirements.Traditionaltelecommunication networks arenot grid intelligent by constantly sensing accurate measurements
capabletofacilitatetheserequirementsalongwiththerequired from FE and reporting them to OE. A shift into more renew-
security in military use cases. In [71], Höyhtyä et al. discuss able and distributed energy generation to reduce greenhouse

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 973
|     |     |     |     |     |     |     | Return On | Investment       |      | (ROI) of     | network    | slicing      | in smart | grids     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------------- | ---- | ------------ | ---------- | ------------ | -------- | --------- |
|     |     |     |     |     |     |     | have been | analysed         | from | the          | operator’s | perspective. |          | In [137], |
|     |     |     |     |     |     |     | Dorsch    | et al. discussed |      | the economic |            | advantages   | that     | can be    |
|     |     |     |     |     |     |     | achieved  | through          | SDN  | and          | network    | slicing      | when     | transmit- |
tingcriticalmeasurementsandcontrolcommandsthatrequired
|     |     |     |     |     |     |     | ultra-reliability |                    | and low | latency         | in         | smart    | grids. They   | have      |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------------ | ------- | --------------- | ---------- | -------- | ------------- | --------- |
|     |     |     |     |     |     |     | proposed          | a techno-economic  |         |                 | evaluation | approach |               | that con- |
|     |     |     |     |     |     |     | sists of          | smart-grid-traffic |         | modelling,      |            | network  | dimensioning, |           |
|     |     |     |     |     |     |     | operator          | modelling          | and     | cost modelling. |            | In       | [136], Kurtz  | et al.    |
|     |     |     |     |     |     |     | proposed          | an SDN             | and     | NFV             | based      | network  | slicing       | solution  |
Fig.13. NetworkSlicing&SmartEnergy. for critical communications in 5G shared infrastructure. They
|                |     |           |             |        |       |           | have evaluated  |       | the solution | using    | a   | testing     | setup for      | two real- |
| -------------- | --- | --------- | ----------- | ------ | ----- | --------- | --------------- | ----- | ------------ | -------- | --- | ----------- | -------------- | --------- |
|                |     |           |             |        |       |           | world scenarios |       | - smart      | grid     | and | Intelligent | Transportation |           |
| gas emissions, |     | generates | instability | in the | power | grid. IoT |                 |       |              |          |     |             |                |           |
|                |     |           |             |        |       |           | System          | (ITS) | - allocating | separate |     | slices      | for each       | scenario  |
helps to remove the instability in the grid through continuous under three cases: performance study, scalability analysis
real-time monitoring. andcritical-infrastructurecommunication.Theyhaveachieved
1) TheRoleofNetworkSlicinginSmartEnergy: Typically, higher scalabilityandlowend-to-end delayviatheirproposed
| a smart     | grid consists |       | of a       | massive number | of      | connected    | solution. |     |     |     |     |     |     |     |
| ----------- | ------------- | ----- | ---------- | -------------- | ------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| components, | distributed   |       | across     | a very         | large   | geographical |           |     |     |     |     |     |     |     |
| area [103]. | These         | smart | components | have           | diverse | network      |           |     |     |     |     |     |     |     |
requirements [45] across multiple application areas, such as H. UAVs and Drones
| online monitoring |     | for | the power | transmission |     | line, smart |                |     |             |     |        |          |         |      |
| ----------------- | --- | --- | --------- | ------------ | --- | ----------- | -------------- | --- | ----------- | --- | ------ | -------- | ------- | ---- |
|                   |     |     |           |              |     |             | The popularity |     | of Unmanned |     | Aerial | Vehicles | (UAVs), | also |
homesandsmartvehicles[134].Someofthecomplicationsin known as drones, increased over the past few years in a wide
the existing network infrastructure include providing a good range of areas related to civilian, military, commercial and
network connectivity, handling the massive amount of data governmental sectors. Drones have the ability to facilitate
generated through those components, and facilitating diverse multipleIoTservicesfromgreatheights,formingtheairborne
| network | requirements. |     | Allocation | of separate | slices | for smart |             |          |     |         |     |             |     |            |
| ------- | ------------- | --- | ---------- | ----------- | ------ | --------- | ----------- | -------- | --- | ------- | --- | ----------- | --- | ---------- |
|         |               |     |            |             |        |           | IoT through | sensors, |     | cameras | and | GPS modules |     | fixed into |
grid-based applications in the 5G network can mitigate these drones and emerging telecommunication technologies such
complications cost-effectively. The smartgridapplications are as 5G [104]. Surveillance scenarios (e.g., traffic, power line,
moreattractivetocyber-attacks[135],sinceasuccessfulattack agriculture and environment) are one of the key aspects in
onagridcancauseabadimpacttothewholecountry,through IoT. UAVs can be used to facilitate the requirements of these
creatingdisturbancesinthedailyroutineofthepeople,aswell applications [138], [139]. In [140], Motlagh et al. presented
as damaging the electric assets. Communication through pub- an integrative IoT platform operational in the sky, using
lic networks increases the vulnerability for attacks and proper UAVs equipped with diverse IoT devices. They have imple-
security mechanisms should be implemented to mitigate these mented UAV-based crowd surveillance applications through
vulnerabilities. Network slicing is a prominent way to imple- the proposed platform. Using drones as aerial base stations
ment security functions for grid systems. Slice isolation is a isanovelapproachinwirelessnetworkstoenhancecoverage,
potential solution for segregating the grid-based traffic over capacity, energy efficiency and reliability. Attributes of UAVs
the public network. suchasmobility,adaptivealtitudeandflexibilitysupportsome
Different application areas in the smart energy service sec- potential applications in wireless systems [105]. This helps to
tor, along with allocating separate slices for each application, improve the network coverage in remote areas to facilitate
are shown in Figure 13. Four different feasible slices have remote IoT applications, such as wildlife monitoring and IoT
been identified in the smart-grid use case: firstly, for UAV- devices that have small transmit power. In addition to sup-
based-grid inspection, secondly, for distribution automation, portingIoTapplications,UAVsareconsideredpartoftheIoT,
| thirdly, | for smart | metering | and | lastly, for load | control. | Slices |             |               |     |         |     |               |     |          |
| -------- | --------- | -------- | --- | ---------------- | -------- | ------ | ----------- | ------------- | --- | ------- | --- | ------------- | --- | -------- |
|          |           |          |     |                  |          |        | since their | functionality |     | depends | on  | a combination | of  | sensors, |
have been allocated according to the network requirements in antennas and embedded software [106].
each use case. 1) The Role of Network Slicing and UAVs: There are two
2) Related Works: Allocation of separate slices for iden- main kinds of data that need to be communicated with UAVs,
tified smart grid applications [24], [136] and increasing the one being control data that needs to handle the UAV. The
revenue of MNOs through network slicing [137] have been other is payload data collected from cameras and sensors
covered in current related works. that needs to be sent to another location for further process-
In [24], Zhang et al. thoroughly examined network slic- ing. These data types have diverse network requirements. It
ing in smart grid applications. They have identified four use needs to facilitate these requirements cost-effectively. High
cases in smart grids, along with different network require- reliability and low latency are key QoS requirements in con-
ments: Advanced Metering Infrastructure (AMI), Distribution trol data. In payload data, a massive amount of data may
Automation,UAV-basedgridInspectionandMillisecond-level need to be transmitted. Along with existing technologies, it
precise load control and they proposed separate slices for is not possible to separate UAV-related traffic from other traf-
each use case. The Total Cost of Ownership (TCO) and fic, as well as control traffic from payload traffic. Network

974 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
Fig.15. NetworkSlicing&MassiveIoT.
Fig.14. NetworkSlicing&Drones.
slicing in 5G networks is a noteworthy technology to facil- devices. Agriculture and environment-monitoring applications
itate this requirement via slice isolation, while facilitating areanexampleforsuchcontext,wherescalebecomesthecrit-
icalfactor,ratherthanspeed[142].Traditionalfarmsthatused
| heterogeneous | network |     | requirements | in UAV-related |     | traffic. |     |     |     |     |     |     |     |
| ------------- | ------- | --- | ------------ | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Figure 14 shows how network slicing can be used in UAV to be small units distributed over small land areas have now
service areas with diverse network requirements. Three possi- evolved into massive farms that have thousands of animals
|     |     |     |     |     |     |     | over large | geographic | areas, | armed | with | heterogeneous | sen- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ------ | ----- | ---- | ------------- | ---- |
bleusecasesofdronesthatrequiredseparateslicesareshown
in the figure: UAVs in emergency situations, UAVs as floating sors and actuators. These highly accurate embedded sensors
|               |     |      |               |            |     |               | enable precision |     | agriculture | by  | measuring | the environmental |     |
| ------------- | --- | ---- | ------------- | ---------- | --- | ------------- | ---------------- | --- | ----------- | --- | --------- | ----------------- | --- |
| base stations | and | UAVs | in commercial | activities |     | like delivery |                  |     |             |     |           |                   |     |
services and photography. Each drone use case can be fur- context inside farms [143], [144]. Improving productivity and
ther sliced to communicate control signals and payload data maximising yields and profitability, and reducing the envi-
|     |     |     |     |     |     |     | ronmental | footprint, | are | resulted | by the | optimal | usage of |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | -------- | ------ | ------- | -------- |
respectively.
2) Related Works: Accomplishing communication require- fertilizers,pesticidesandefficientirrigationmechanisms[108].
Thesmartfarmingconceptthatincludesreal-timedatagather-
| ments of | UAVs and | drones, | in terms | of controlling |     | and other |     |     |     |     |     |     |     |
| -------- | -------- | ------- | -------- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
operationssuchasvideostreaming,throughdedicatednetwork ing and processing, along with automating necessary actions
slices, is discussed in current related works. Further investi- over farming procedures, is realised by precision agriculture.
In[109],Ruanetal.dividedIoTtechniquesinagricultureinto
| gations should | be  | conducted | in  | the realisation | of  | other UAV |     |     |     |     |     |     |     |
| -------------- | --- | --------- | --- | --------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
use cases, such as aerial base stations and military operations, fourcategories:controlledequipmentfarming,livestockbreed-
ing,aquacultureandaquaponicsandopen-fieldplanting.They
| through | network | slicing. |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In [107], Garcia et al. discussed the performance impact of discussed challenges in exploitation of IoT into agriculture.
using network slicing in aerial vehicle communications. They IoT enables environmental monitoring with an assemblage
|     |     |     |     |     |     |     | of connected | sensors | to  | monitor | environmental |     | parameters |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | ------- | ------------- | --- | ---------- |
haveallocatedseparatenetworkslicestocontroldataandpay-
load data, referred to as control slice and payload slice. The such as temperature, humidity, wind speed, gases and pres-
|            |          |      |       |               |        |              | sure. It | provides | advantages | such | as maintaining |     | healthy |
| ---------- | -------- | ---- | ----- | ------------- | ------ | ------------ | -------- | -------- | ---------- | ---- | -------------- | --- | ------- |
| experiment | has been | done | under | three trials. | In the | first trial, |          |          |            |      |                |     |         |
they have measured Ipref values in control slice and payload growth of crops and ensuring safe working environments in
| slice in Down | Link | (DL). | The second | trial | had the | same prin- | industries | [110]. |     |     |     |     |     |
| ------------- | ---- | ----- | ---------- | ----- | ------- | ---------- | ---------- | ------ | --- | --- | --- | --- | --- |
ciple with Up Link (UP) and DL. In the final trial, they have 1) The Role of Network Slicing and Massive IoT:
checked whether the delay of the control slice is affected by InternationalstandardorganisationsidentifiedthemassiveIoT
thepayloaduseofthenetwork.Theyhaveshownthatrequired as one of the main service areas in the novel 5G architecture,
throughput of the control slice can be maintained while allo- which is referred as mMTTC. Network slicing is a promis-
cating remaining capacity to payload slice during the flight, ing technology to facilitate network requirements in massive
via first and second trials. Using the results in the third trial, IoT applications that have billions of low power devices with
they have shown that the Round Trip Time (RTT) of control a small amount of data. Narrow Band (NB) IoT is a kind
slice is not influenced by the varied payload throughput. They of network slicing technology in Long Term Evolution (LTE)
have concluded that slicing performs effectively in facilitating networks, which runs over the same physical network infras-
network resources for control communication in aerial vehi- tructure. It is designed to facilitate low-cost devices, high
|                     |     |           |       |              |     |         | coverage, | long device | battery | life | and massive | capacity | [145]. |
| ------------------- | --- | --------- | ----- | ------------ | --- | ------- | --------- | ----------- | ------- | ---- | ----------- | -------- | ------ |
| cle communications. |     | Reference | [141] | demonstrated |     | how 5G, |           |             |         |      |             |          |        |
along with network slicing, can be used in disaster and emer- Power consumption of the IoT devices can be optimised via
gencysituationsusingdrones.Thedemoisexecutedundertwo allocating a separate E2E network slice with optimised NFs.
scenarios (delivering supplies and video streaming) in given Normally, in smart farming and environmental monitoring
situations and a dedicated slice is used to provide network applications, IoT devices will be distributed in rural areas that
donothaveapropernetworkcoverage.Thesedevicesconnect
| connectivity | to the | drone | with | required | QoS requirements. |     |     |     |     |     |     |     |     |
| ------------ | ------ | ----- | ---- | -------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
They have shown how networks can be deployed in disaster tothenetworkintermittentlytotransmitcollectedinformation,
situations using network slicing. in order to optimise the battery life. Just like NB-IoT, allocat-
|            |               |     |             |     |              |     | ing a separate | slice  | facilitates    | network | requirements |                    | of these |
| ---------- | ------------- | --- | ----------- | --- | ------------ | --- | -------------- | ------ | -------------- | ------- | ------------ | ------------------ | -------- |
| I. Massive | IoT (Farming, |     | Agriculture | and | Environment) |     |                |        |                |         |              |                    |          |
|            |               |     |             |     |              |     | devices over   | common | infrastructure |         | with         | cost optimisation. |          |
The concept of Massive IoT lies on transmitting and con- Two application areas, farming and environmental monitor-
sumingasmallamountofdatafromamassivenumberofIoT ing, in massive IoT are shown in Figure 15 and it describes

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 975
how network slicingcan be used tofacilitatenetwork require- correspondinglytomitigatemanagementandorchestrationdif-
mentsofthoseapplications.Furthermore,dedicatedsliceswith ficulties evolved through the massive number of slices due to
differentNFscanbecreatedtoothermassiveIoTapplications. the rapid expansion of IoT.
2) Related Works: In [146], Popovski et al. discussed 2) Existing Solutions: In [170], Kuklin´ski and
heterogeneous non-orthogonal sharing (H-NOMA) of RAN Tomaszewski proposed a scalable approach to mitigate
resourcesinuplinkcommunicationsofasetofeMBB,mMTC difficulties (i.e., massive increment in the number of network
and URLLC devices, which connects to a common base sta- slices and involvement of third parties to have slices for their
tion in RAN slicing. They have analysed slicing of resources needs) in network slicing management and orchestration.
betweeneMBBandURLCCandbetweeneMBBandmMTC, They have introduced a concept called DASMO (Distributed
withillustrationsoftradeoffsbetweenH-OMAandH-NOMA. and Autonomic Slice Management and Orchestration), which
In both cases, they have shown that non-orthogonal solu- reduces the management delays and management related
tions must be guided by reliability diversity to achieve more traffic, along with enabling the formation of distributed and
efficiency. automated network slicing management solutions. However,
theproposedsolutionisonlyconceptualandnotimplemented.
J. Other Applications In[169],Afolabietal.proposedanovelE2ENetworkSlicing
|             |                    |               |      |                 |          |            |           | Orchestration |        | System   | (NSOS)    | and a Dynamic |     | Auto-Scaling  |        |
| ----------- | ------------------ | ------------- | ---- | --------------- | -------- | ---------- | --------- | ------------- | ------ | -------- | --------- | ------------- | --- | ------------- | ------ |
| In addition | to                 | the discussed |      | IoT application |          | areas,     | there are |               |        |          |           |               |     |               |        |
|             |                    |               |      |                 |          |            |           | Algorithm     | (DASA) | for      | it. Their | auto-scaling  |     | algorithm     | scales |
| several     | other applications |               | that | can             | lay hold | of network | slic-     |               |        |          |           |               |     |               |        |
|             |                    |               |      |                 |          |            |           | the resources |        | of their | proposed  | multi-domain  |     | orchestration |        |
ingfortheirrealisation.Typically,theseapplicationshaveless
impactfromnetworkslicingratherthandiscussedapplications, systembyhandlingthelargenumberofslicecreationrequests
|          |          |             |             |      |     |               |     | to maintain  | system-wide |           | stability. |     |          |         |     |
| -------- | -------- | ----------- | ----------- | ---- | --- | ------------- | --- | ------------ | ----------- | --------- | ---------- | --- | -------- | ------- | --- |
| but have | specific | advantages. |             |      |     |               |     |              |             |           |            |     |          |         |     |
|          |          |             |             |      |     |               |     | Furthermore, |             | efficient | algorithms | for | resource | sharing | can |
| Smart    | retail   | is an       | application | that | IoT | has dominated |     | in           |             |           |            |     |          |         |     |
many segments, including supply-chain management, smart be investigated to improve the scalability of network slices.
| vending                                               | machines | and | digital | signage. | Smart | retail | is iden- |              |     |     |     |     |     |     |     |
| ----------------------------------------------------- | -------- | --- | ------- | -------- | ----- | ------ | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| tifiedasthesecond-largestMECusecase[147].Technologies |          |     |         |          |       |        |          | B. Recursion |     |     |     |     |     |     |     |
such as AR/VR that require network slicing for its realisa- Theabilitytocreatelargerfunctionalblocksbyaggregating
tion have the ability to influence the customer’s decision, multiple numbers of smaller functional blocks can be defined
| finally impacting |     | smart | retail | [148]. | The | smart | wearable | is           |        |          |     |           |          |            |     |
| ----------------- | --- | ----- | ------ | ------ | --- | ----- | -------- | ------------ | ------ | -------- | --- | --------- | -------- | ---------- | --- |
|                   |     |       |        |        |     |       |          | as recursion | [171]. | Applying |     | recursion | property | in network |     |
anotherapplicationdomainthatiscomprisedwithseveraldis- slicingmeansthecreationofnewnetworkslicesusingexisting
| cussed applications, |     | such | as smart | healthcare, |     | smart | city and |               |     |       |                |         |           |     |        |
| -------------------- | --- | ---- | -------- | ----------- | --- | ----- | -------- | ------------- | --- | ----- | -------------- | ------- | --------- | --- | ------ |
|                      |     |      |          |             |     |       |          | slices [172]. | In  | other | terms, network | slicing | recursion |     | can be |
AR/VR/gaming. Networking slicing with MEC is recognised defined as methods for network slice segmentation, allowing
as a solution to overcome the critical concerns in wearable a slicing hierarchy with parent-child relationships [173].
| communications, |     | such | as short | battery | life | and limited | com- |                  |     |                                      |     |     |     |     |     |
| --------------- | --- | ---- | -------- | ------- | ---- | ----------- | ---- | ---------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
|                 |     |      |          |         |      |             |      | 1) Requirements: |     | IoTapplicationscanspanacrossmultiple |     |     |     |     |     |
puting capability [149], [150]. Smart supply chain is listed in tenets and network domains. Therefore, creation a completely
| the top | ten IoT | applications |     | in [151]. | Tracking | goods | while |     |     |     |     |     |     |     |     |
| ------- | ------- | ------------ | --- | --------- | -------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
newsliceisacomplextaskwhencomparingwithusingexist-
they are on the roads and exchanging inventory information, ingslices.DuethedynamicityofIoTusecases,thecreationof
aresomepossibleusecasesinthesmartsupplychainthatcan new slices is a frequent operation which has to accommodate
| be facilitated | through |     | mMTC | slice over | 5G  | networks. |     |         |           |      |        |             |       |                |     |
| -------------- | ------- | --- | ---- | ---------- | --- | --------- | --- | ------- | --------- | ---- | ------ | ----------- | ----- | -------------- | --- |
|                |         |     |      |            |     |           |     | in many | networks. | Most | of the | time, there | is no | be significant |     |
Table VII summarises the potential network slices and differencesbetweentheusecasesandhencethecharacteristics
| the technical |     | requirements | of  | each | proposed | slice | in each |                  |     |         |            |       |            |          |     |
| ------------- | --- | ------------ | --- | ---- | -------- | ----- | ------- | ---------------- | --- | ------- | ---------- | ----- | ---------- | -------- | --- |
|               |     |              |     |      |          |       |         | of the requested |     | slices. | Therefore, | it is | beneficial | for most | of  |
discussed IoT application. the IoT applications to create new slices by inheriting prop-
|     |     |     |     |     |     |     |     | erties from | parent | slices. | This | will optimise | the | slice creation |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------- | ---- | ------------- | --- | -------------- | --- |
V. TECHNICALCHALLENGESRELATEDTONETWORK
|     |     |     |     |     |     |     |     | operation | in IoT | context. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | -------- | --- | --- | --- | --- | --- |
SLICINGINIOTREALIZATION 2) Existing Solutions: In [174], Héno et al. presented
Thissectionisallocatedtodescribethetechnicalchallenges a recursive network slicing model. The proposed model is
related to the network slicing, due to the IoT realisation. The based on a parallel analysis between IT virtualisation and
|          |         |         |           |     |         |         |         | network | virtualisation, |     | using | virtualisation | theory | introduced |     |
| -------- | ------- | ------- | --------- | --- | ------- | ------- | ------- | ------- | --------------- | --- | ----- | -------------- | ------ | ---------- | --- |
| state of | the art | of each | challenge | in  | network | slicing | will be |         |                 |     |       |                |        |            |     |
discussed in detail here. by Popek and Goldberg. Isolation, recursiveness and indepen-
|     |     |     |     |     |     |     |     | dence are | considered |     | in their | model. | They | showed how | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | -------- | ------ | ---- | ---------- | --- |
enablenewBusiness-to-Business-to-Consumer(B2B2C)busi-
A. Scalability
|                  |           |                                     |     |              |        |           |         | ness models |            | through | network   | slicing  | by re-renting |         | rented |
| ---------------- | --------- | ----------------------------------- | --- | ------------ | ------ | --------- | ------- | ----------- | ---------- | ------- | --------- | -------- | ------------- | ------- | ------ |
| 1) Requirements: |           | Alongwiththeexponentiallyrisingnum- |     |              |        |           |         |             |            |         |           |          |               |         |        |
|                  |           |                                     |     |              |        |           |         | resources   | achieved   | by      | recursive | building | of            | network | slices |
| ber of different |           | IoT applications,                   |     | the          | number | of slices | in the  |             |            |         |           |          |               |         |        |
|                  |           |                                     |     |              |        |           |         | layered     | and nested | within  | each      | other.   |               |         |        |
| network          | will also | increase.                           |     | Furthermore, |        | service   | area of | a           |            |         |           |          |               |         |        |
networkslicethatoffercriticalserviceswithultra-lowlatency
|              |      |      |        |     |         |        |        | C. Adaptive | Service | Function |     | Chaining |     |     |     |
| ------------ | ---- | ---- | ------ | --- | ------- | ------ | ------ | ----------- | ------- | -------- | --- | -------- | --- | --- | --- |
| requirements | will | also | shrink | due | to high | number | of IoT |             |         |          |     |          |     |     |     |
devices. This might finally increase the required number of The network softwarization concepts, especially NFV
slices, thus increasing the slice orchestration requests [169]. proposedtousedvirtualizednetworkfunctionsorservicesthan
Thus, the network slice management function should scale hardware based network services such as firewalls, Network

976 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
TABLEVII
SUMMARYOFEXPECTEDPERFORMANCEINTHEIOTAPPLICATIONSWITHPOSSIBLESLICES
Address Translation (NAT) and intrusion protection. These policyandoperationalrequirements.Linkageofthesenetwork
vitalized networks services have to execute in certain order functions to form service can be defined as Service Function
to satisfy a particular business need and facilitate the service Chaining (SFC) [175]. Improved operational efficiency and

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 977
automatedhandlingoftrafficflowswithadvancefeatures(i.e., In [180], Khettab et al. proposed and evaluated a novel
moresecurity,lowerlatencyoroverallhighQoSforconnected Security as a Service (SECaaS) architecture that leveraged
services)canbeachievedthroughSFC[176].Anetworkslice SDN and NFV to secure a network slice. This ensured
can be also identified as a collection of connected VNFs. an optimal resource allocation that efficiently manages the
According the nature of supported applications, it is neces- slice-security strategy. Their proposed architecture consists of
sary to dynamically change the structure of the slices. This four main parts: cloud network, each managed by a Virtual
can be realized via by implementing adaptive service function InfrastructureManager(VIM),VNFmanagerstomonitoraset
chaining. of VNFs in a slice, an NFV orchestrator responsible for life
1) Requirements: IoT applications are highly dynamic cycle managing of VNFs and an SDN controller to monitor
and the network requirements, such as security, latency and and control traffic flows. Along with deploying and manag-
QoS are always changing. Using dynamic service chain- ing security VNFs (including Intrusion Detection/Prevention
ing, network operators will be able to create, scale, modify System [IDS/IPS] and Deep Packet Inspection [DPI]), the
and remove network functions of a network slice according capabilities in their proposed architecture include monitor-
to the such changing demand, networks and cloud context ing their performance and predictive auto-scaling based on
information[177].Recurringchangesofnetworkrequirements pre-defined policies, to ensure the elasticity.
of IoT applications entails continuous updates of SFCs of In [65], Cunha et al. presented a detailed discussion on
network slices to reduce the network cost. Hence, adaptive security challenges of network slicing at the packet core.
SFC in network slicing is a challenge that has to address due ApplyingAItechniquesinachievingsecurityinnetworkslices
to the evolution of IoT applications. is discussed in [181]. They have discussed various security
2) Existing Solutions: In [178], Li et al. introduced a challenges with possible AI mechanisms, in order to mitigate
novel concept of an elastic service function chain. They those attacks in network slicing. Reference [182] discusses
addressed network slicing with such chaining constraints as implementation of a quarantine slice to isolate devices that
a Software Defined Topology (SDT) (performs slice framing) were subjected to a security attack to perform security-related
problem. They formulated the SDT problem (when VF shar- operations for those devices and to minimise the effect of the
ing across services, node overlapping may appear between attack on the other systems.
logicaltopologies)withelasticSFCasacombinatorialoptimi-
sation problem. Then they devised a fast multi-stage heuristic
E. Privacy
algorithm to tackle it.
1) Requirements: Network slicing has its own set of pri-
D. Security
vacy issues and integration of IoT will further increase the
1) Requirements: Several security vulnerabilities can be impact of it. Information leakages between slices expose the
identified within the network slicing ecosystem. The prolif- sensitive data to third parties, endangering the privacy. Strong
eration of IoT and network slicing exploitation of different slice isolation techniques with secure inter-slice communica-
IoT applications, intensify the effect of these vulnerabilities. tion via secure channels are a critical requirement in using
Suchissuescanbecategorizedintothreedifferentareas[179]. network slicing for communications in order to preserve the
• Lifecyclesecurityaspectsforsecurity-relatedindifferent privacy of the users. Also, slice isolation mechanisms should
phases of the network slice life cycle be implemented in customer-end devices to assure the privacy
• Intra-slice security for security aspects in slice itself and of the data from the customer end intruders. Some of the end
• Inter-slice security for security aspects between slices IoT devices can access more than one slice simultaneously
Proper slice isolation is a critical security requirement in may also be a cause for information leakages between slices.
network slicing. Since end-device can access more than one In [65], Cunha et al. discussed the probable security and
slice at once, if there are no strong isolation mechanisms, privacy breaches in network slicing descriptively. Network
attackers can launch attacks to other slices relatively easily. functions that may be shared between slices are allowing
Duetotheuseoflightweightandlesscomplexsecuritymech- unauthorisedinter-slicecommunication,challengingtheconfi-
anisms, IoT devices become attractive for many attackers to dentiality and the integrity of the data communicated through
perform such attacks. slices. IoT tenet might ask to use such third party network
InvolvementofthirdpartiesincreasesduetotheIoTexpan- functions in their slices which might jeopardize the whole
sion. Specially, new set of attackers such as cyber criminals slicing system. Successful impersonation of the NSM allows
andterroristwillalsotargetIoTapplicationwhentheyareused subverting slice isolation, resulting in unauthorised access to
in Critical National Infrastructures (CNIs). In such scenar- all the slices that could be resulted in a breach of system
ios,slice-relatedconfigurationandmanagementoperationsare confidentialityandintegrity.Theabilitytochangethemanage-
given to third parties via Application Programming Interfaces mentandconfigurationviaAPIsforthirdpartytenantsallows
(APIs). These APIs are an entry point for intruders to enter them to impersonate the host platform and run as an autho-
and perform unauthorised activities. rised platform. By exposing the network and private services
2) Existing Solutions: Exploitation of IoT in a plethora to an attacker, confidentiality and the integrity of the system
of applications increases the security challenges of network can be endangered. The mentioned privacy issues can become
slicingandseveralmechanismshavebeenproposedtomitigate morechallengingalongwiththerapidexploitationofIoTwith
these challenges. network slicing.

978 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
2) ExistingSolutions: Basedontheexistingsolutions,slice In[186],Menesesetal.proposedtheSliMANOframework
isolation [183] and securing inter-slice communication [184], for slice management and orchestration with an implemented
[185]havebeenidentifiedassolutionstoaddressprivacychal- and experimentally evaluated prototype. The proposed frame-
lenges related to network slicing. Furthermore, investigations work consists of three parts: SliMANO core for coordinating
can be conducted in preserving privacy in communications SliMANO functionalities, SliMANO-plugin framework for
when sharing network resources between slices. facilitating the continuous deployment of new plugins and
In [184], Liu et al. proposed two heterogeneous signcryp- respectiveagentsandSliMANO-agentframeworkforperform-
tion schemes to accomplish mutual communications between ingtheactionsrequestedbypluginstoexternalnetworkentities.
the Public Key Infrastructure (PKI) and the CertificateLess In[188],Yousafetal.shedthelightontheconceptofMANO-as-
public key Cryptography (CLC) environment, in order a-service (MANOaaS) to customise and distribute the MANO
to ensure secure communication between network slices. instances between different network tenants for improving the
PKI-CLC Heterogeneous Signcryption (PCHS) and CLC- control of network slices. In [187], Abbas et al. presented
PKI Heterogeneous Signcryption (CPHS) are the proposed different aspects of slice management for 5G networks. They
schemes in there. They presented how to secure communica- proposed a framework that exploited Mobile-Central Office
tionbetweenamobileInternetsliceandavehicleInternetslice Re-Architected as Datacentre (M-CORD) for introducing a
using proposed schemes. In [183], Kotulski et al. presented a slicing mechanism for transport network. It enables slices to
detailed discussion on slice isolation, along with types of iso- be available every time a UE requests them.
lation,isolationparametersanddynamicsliceisolation.These
address inter-slice communication to accomplish security per- G. Other Technical Challenges
spectives. In [185], Suárez et al. presented a mathematical
Apart from the technical challenges above discussed, a few
modelbasedontheconceptofnetworkslicechains,tomanage
other technical challenges can be found due to the rise of the
the inter-slice communication securely when there are differ-
IoT realisation. The impact of these challenges is far away
ent security requirements and attributes between slices. Their
fromtheabove-discussedchallenges,byreasonoflackoflarge
proposed model is extensible for application in any service
scale network slicing implementations.
and it complies with any access control model.
Limited nature of the RAN resources such as frequency
and time than network resources in the core network such as
F. E2E Management and Orchestration
servers and databases, causes difficulties in RAN slicing. It
1) Requirements: The proliferation of the IoT applications
affects negatively for the E2E implementation and the rapid
increasestheneedfordedicatedslicesinthenetworkfortheir
deploymentoftheapplicationspecificslices.Inmobilityman-
optimal behavior, finally causing the rise of the number of
agement and handling roaming scenarios, the same serving
slices that have to be managed. Resource allocation between
slice needs to exist in different operators [189]. IoT devices
slices, changing configurations, facilitating QoS requirements
should be able to cross these boundaries without experienc-
andmanagingthesecurityandprivacyaspectsforthismassive
ing any disturbances in communications. Secure and efficient
number of slices, are complex tasks that need to be han-
slice information (slice configuration information and user-
dled efficiently. An abundance of third-party tenants due to
specific information) transmission between MNOs is required
IoT collaboration within diverse fields will involve manag-
in accomplishing this challenge.
ing and configuring the slices. Managing the involvement of
third parties is a challenging task. Temporary usage of slices
VI. PROJECTS
in emergency situations such as earthquakes, floods and fires
This section is allocated to discuss some important projects
make the need for rapid deployment of slices. In addition to
that explicitly work with IoT and network slicing technolo-
theconventionalIoTsecurityattacksthatarepotentialtoharm
gies. Most of the projects are based on the Europe region
telecommunication networks, IoT intensifies the severity of
and the recent Horizon 2020 (H2020) funding scheme has
the security threats in the network slicing ecosystem. More
fueled for most ongoing projects. Discussed projects along
robust network slicing management facilities are required to
with their technical aspects and the focused research areas,
overcomethesesecuritychallenges.Utilizationofacentralised
are summarized in the Table IX.
approachforsliceorchestrationandmanagementwillincrease
the scalability and reliability issues, along with the escalated
A. SliceNet
network slices. According to these facts, IoT systems origi-
nate several challenges to the network slice management and SliceNet[191](1stJune2017-31stMay2020)isaproject
orchestration. funded by the EU commission under the H2020 program. It
2) Existing Solutions: According to the existing solutions, aims to develop a management/control framework to support
slice management and orchestration can become a complex 5Gverticalservicesbuiltas‘slices’ofnetworkresources.This
activity, along with the rapid increment of the number of project drives in achieving three main objectives based on
slices. A couple of MANO frameworks [186], [187] and the the softwarization of network elements, one being removing
MANOaaSconcept[188]havebeenidentifiedassolutionsthat the limitations of current network infrastructure. Another is
address this challenge. Future researches can be directed on addressing the associated challenges in managing, controlling
developing more efficient slice management and orchestration andorchestratingthenewservicesrunningin5Ginfrastructures
frameworks. andthirdly,maximisingthepotentialof5Ginfrastructuresand

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 979
IIIVELBAT
SKROWDETALERFOYRAMMUS

980 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
IIIVELBAT
SKROWDETALERFOYRAMMUS).deunitnoC(

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 981
TABLEIX
CONTRIBUTIONOFGLOBALLEVELPROJECTSONNETWORKSLICINGANDIOT
their services. The SliceNet managed domain consists of five Centre Technologic de Telecomunicacions de Catalunya. In
layers,frombottomtotoprespectively:physicalinfrastructure, thisproject,theywillcreateanadvancedresearchandtraining
virtual infrastructure, service, control and sliced service. The structure for multi-GHz spectrum communications, MEC-
project is running across three main use cases: 5G smart grid empowered service provisioning and end-to-end network slic-
self-healing use case, 5G e-Health-connected ambulance use ing.ThegoalofthisprojectistrainingEarlyStageResearchers
case and smart-city use case. (ESRs)toformhighly-trainedacademicresearchersandindus-
|     |     |     |     |     |     |     | try professionals | in the | mentioned | areas. | This | aims | to over- |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------ | --------- | ------ | ---- | ---- | -------- |
B. AutoAir come the technical gaps towards the journey to 5G with the
AutoAir [192] project,led by Airspan, is a unique, acceler- guidance from industry professionals.
| ated program | for | 5G technology. |       | This  | is based on       | small cells |            |     |     |     |     |     |     |
| ------------ | --- | -------------- | ----- | ----- | ----------------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
| that operate | on  | a ‘Neutral     | Host’ | basis | that uses network | slic-       | E. MATILDA |     |     |     |     |     |     |
ing for allowing multiple public and private mobile operators Matilda [195] (1st June 2017 – 30th November 2019) was
| to use the | same | infrastructure. |     | This project | uses | the mobile |           |                 |     |           |         |     |           |
| ---------- | ---- | --------------- | --- | ------------ | ---- | ---------- | --------- | --------------- | --- | --------- | ------- | --- | --------- |
|            |      |                 |     |              |      |            | funded by | H2020-EU.2.1.1, |     | aiming to | develop | a   | holistic, |
infrastructure installed at Millibrook. The launch event was innovative 5G framework over sliced programmable infras-
heldon12thFebruary2019withademonstrationofproviding
|                |     |           |     |     |     |     | tructure.  | This is for design, |              | development     | and             | orchestration |      |
| -------------- | --- | --------- | --- | --- | --- | --- | ---------- | ------------------- | ------------ | --------------- | --------------- | ------------- | ---- |
| gigabit access | to  | vehicles. |     |     |     |     |            |                     |              |                 |                 |               |      |
|                |     |           |     |     |     |     | phases of  | the 5G-ready        | applications | and             | the network     | services.     |      |
|                |     |           |     |     |     |     | One of the | main objectives     |              | of this project | is facilitating |               | ver- |
C. 5G!Pagoda
|     |     |     |     |     |     |     | tical industries | by enabling | the | development, | deployment |     | and |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ----------- | --- | ------------ | ---------- | --- | --- |
5G!Pagoda [193] (July 2016 - December 2019) is funded orchestration of network-aware applications via dynamically
| by European | Commission’s |     |     | H2020 program. | The | principal |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
createdapplication-awarenetworkslicesinthe5Gecosystem.
goal of the project is to explore relevant standards and align It incorporated technological and business requirements that
views on 5G network infrastructure. It uses dynamic creation rose from various parties, such as industry, service providers,
andmanagementofnetworkslicesforvariousmobileservices
|     |     |     |     |     |     |     | application | users and | the research | community. |     | The | project |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ------------ | ---------- | --- | --- | ------- |
using federated Japanese and European 5G testbeds. They consisted of four IoT use cases: 5G emergency infrastructure
| have presented |     | a demo | on IoT | services | via 5G network | slic- |              |               |      |                  |     |            |     |
| -------------- | --- | ------ | ------ | -------- | -------------- | ----- | ------------ | ------------- | ---- | ---------------- | --- | ---------- | --- |
|                |     |        |        |          |                |       | and services | orchestration | with | SLA enforcement, |     | smart-city |     |
ing technology at the IoT week in Aarhus in 2019. The top intelligent-lighting system, remote control and monitoring of
network-slicing-related objective in this project is the devel- automobileelectricalsystemsandanIndustry4.0smartfactory.
| opment | of scalable | 5G  | architecture | with | a scalable | network |     |     |     |     |     |     |     |
| ------ | ----------- | --- | ------------ | ---- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
F. 5G!Drones
slicemanagementandorchestrationframework.TheIoT-based
objective of this project is to develop emerging 5G applica- H2020 research and innovation program funded for
| tions based | on IoT | use | cases | and human | communication, | that |           |             |      |       |       |         |        |
| ----------- | ------ | --- | ----- | --------- | -------------- | ---- | --------- | ----------- | ---- | ----- | ----- | ------- | ------ |
|             |        |     |       |           |                |      | 5G!Drones | [196] (June | 2019 | - May | 2022) | project | and it |
require high scalability and customisation of diverse end-user is aiming to trial several UAV use cases distributed over
requirements. eMBB, URLCC and mMTC service areas in 5G architec-
|     |     |     |     |     |     |     | ture. It | is also validating |     | 5G KPIs | for such | challenging |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------------ | --- | ------- | -------- | ----------- | --- |
D. SEMANTIC use cases. The objectives of this project are validating 5G
end-to-end Slicing and data-drivEn autoMAtion of Next- KPIs and evaluating and validating the performance of dif-
generation cellular neTworks with mobIle edge Clouds (1st ferent UAV applications. This project covers four use cases:
January 2020 – 31st December 2023) SEMANTIC [194] UAV traffic management, public safety/ saving lives, sit-
is a project funded by H2020-EU.1.3.1 and coordinated by uation awareness and connectivity during crowded events.

982 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
Network slicing is featured as the key component in this J. 5G-MONARCH
project, to run UAV services across the network using the
5G MObile Network ARCHitecture (5G-
same 5G infrastructure. It demonstrates that each UAV appli-
MONARCH) [200] (1st July 2017 - 30th June 2019) is
cation runs independently without affecting the performance
a project that was aiming to build a flexible, adaptable
of other applications. The results obtained through this
and programmable architecture for 5G. Network slicing
project will be used by the UAV association to make further
utilization is the specific technical goal of this project. The
recommendations.
project consists of two phases. In phase 1, they designed
such an architecture at a conceptual level with three enabling
G. MonB5G innovations. In phase 2, the addressed architecture was
MonB5G [197] (November 2019 - November 2022) was brought into practice. The three enabling innovations in this
funded by the European Union’s Horizon 2020 research project are inter-slice control and cross-domain management,
and innovation program. It is aiming a novel zero-touch- experiment-driven optimisation and cloud-enabled protocol
managementandorchestrationframeworkfornetworkslicing, stack. The developed architecture deployed in two testbeds:
to increase the scalability massively for 5G LTE and beyond. the smart sea port related to vertical industry use case and
This will leverage distribution of operations, together with the tourist city related to media and entertainment use case.
AI-based mechanisms. Security and energy efficiency are Resilience, security and resource elasticity are the functional
consideredkeyfeaturesintheirconceptual,hierarchical,fault- innovations of the instantiated slices in use cases respectively.
tolerant, data-driven network management system, in order
to orchestrate a plethora of parallel network slices specific K. 5GCity
for diverse services. This project consists of two PoCs: zero-
5GCity [201] (June 2017 – June 2019) is funded by the
touchnetworkandservicemanagementwithend-to-endSLAs
H2020researchandinnovationprogram.Thevisionisdesign-
andAI-assistedpolicy-drivensecuritymonitoringandenforce-
ing, developing, deploying and demonstrating a distributed
ment. The architecture of this project is about splitting the
cloud and radio platform for 5G neutral hosts. This project
centralised management system into multiple management
was focused on bringing benefits of smart city infrastruc-
subsystems that contain one or more distributed management
ture based on resource sharing and end-to-end virtualisation
elements. It has the purpose of distributing intelligence and
to 5G neutral hosts. The project targeted three different cities
design making across various components.
(Barcelona, Bristol and Lucca) under three use cases: media,
neutralhostandunauthorised-waste-dumpingprevention.This
H. 5GMOBIX
was to enable the creation of dynamic E2E slices with vir-
5GMobix[198](November2018-October2021)isfunded tualised edge and network resources to lease to third-party
via H2020 program and this project is examining the impli- operators. Under the media use case, they will consider three
cations of 5G and its role in future autonomous driving. They differentscenarios:mobilereal-timetransmission,UHDvideo
will develop and test the functionalities of automated vehicles distribution and real-time video acquisition and production
using5Gtechnologyinvariousenvironments,suchascityand in edge. For dumping use case, they would use surveillance
urban. This will be under several conditions like vehicular cameras to monitor and detect unauthorised dumping.
traffic and network coverage and service demand, consider-
ing social and business aspects. Network slicing will be used
L. Inspire-5Gplus
to facilitate Corporative, Connected and Automated Mobility
(CCAM) trial activities in this project. INtelligentSecurityandPervasIvetRustfor5GandBeyond
(INSPIRE-5Gplus) [202] (November 2019 - November 2022)
which is a Horizon 2020 project, aims to address the cyber-
I. PRIMO-5G
security risks of 5G and beyond networks, and vertical appli-
The goal of the Primo-5G [199] (July 2018 - June 2021)
cations, ranging from connected cars to industry 4.0, through
project , funded by H2020 program, is to demonstrate an
an innovative security management concept. The project will
end-to-end 5G system providing immersive video services for
improve security in several dimensions including, vision,
moving objects. The project consists of three objectives, one
use cases, integration and management, architecture, models,
being demonstrating a 5G system to provide video services to
and assets. Ensuring the expected Security SLAs (SSLAs)
movingobjects.Thesecondisdevelopingtechnologiesrelated
and the regulation requirements via a fully automated E2E
to mmWave access and 5G core networks. Finally, the third
smartnetworkandsecuritymanagementframework,isanother
objective is AI-assisted communications to support objective
objective of this project.
1, 5G standardisation and spectrum regulation activities. The
main envisaged scenario of this project is the firefighting sce-
M. Hexa-X
nariothatisapartofthePublicProtectionandDisasterRelief
(PPDR). Drones with cameras will be used by the crew to Hexa-X [203] (January 2021 - June 2023) is the European
get real-time situation awareness of the fire scene prior to Commission’s 6G flagship initiative project which aims to
whentheyreachtothelocation,throughAR/VRtechnologies. develop and define the architecture, technologies and vision
Network slicing will be used to provide network services for for next generation 6G wireless networks. The research areas
drones and other moving objects in this project. ofHexa-Xprojectisfocusingonsixkeytopics,i.e.,connected

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 983
Fig.16. Futureresearchdirections.
intelligence, networks of networks, sustainability, global ser- of them are conceptual. Researches with actual slicing imple-
vice coverage, extreme experience, and trustworthiness. mentations can be considered as a valuable movement in the
|     |     |     |     |     |     |     |     | realisation | of smart transportation. |     | Since | security | and privacy |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------------ | --- | ----- | -------- | ----------- |
VII. LESSONSLEARNEDANDFUTUREDIRECTIONS are extremely important aspects of autonomous vehicles, the
|              |            |         |         |         |         |         |         | implementation | of those    | aspects  | using      | network            | slicing can |
| ------------ | ---------- | ------- | ------- | ------- | ------- | ------- | ------- | -------------- | ----------- | -------- | ---------- | ------------------ | ----------- |
| This section |            | focuses | on the  | lessons | learned | and the | future  |                |             |          |            |                    |             |
|              |            |         |         |         |         |         |         | be identified  | as a future | research | direction. | Traffic-prediction |             |
| research     | directions | with    | respect | to      | network | slicing | and IoT |                |             |          |            |                    |             |
algorithmsusingAI/MLandreinforcementtechniquesneedto
| integration.       | Network        | slicing        | in                           | different | IoT   | applications,   | and   |                 |                   |                |           |             |               |
| ------------------ | -------------- | -------------- | ---------------------------- | --------- | ----- | --------------- | ----- | --------------- | ----------------- | -------------- | --------- | ----------- | ------------- |
|                    |                |                |                              |           |       |                 |       | be formulated   | to increase       | the efficiency |           | of resource | allocation    |
| technical          | aspects        | and challenges |                              | related   | to    | IoT realisation | via   |                 |                   |                |           |             |               |
|                    |                |                |                              |           |       |                 |       | between         | slices, to tackle | the traffic    | surges.   |             |               |
| network            | slicing        | will be        | discussed                    | in        | here. | Figure 16       | shows | a               |                   |                |           |             |               |
| summary            | of the         | discussed      | future                       | research  |       | directions.     |       |                 |                   |                |           |             |               |
|                    |                |                |                              |           |       |                 |       | B. Industrial   | Automation        |                |           |             |               |
|                    |                |                |                              |           |       |                 |       | 1) Lessons      | Learned:          | Network        | slicing   | tackles     | the gener-    |
| A. Smart           | Transportation |                |                              |           |       |                 |       |                 |                   |                |           |             |               |
|                    |                |                |                              |           |       |                 |       | ated complexity | to the            | industrial     | networks. |             | This includes |
| 1) LessonsLearned: |                |                | WeexploredhowIoTcanbeengaged |           |       |                 |       |                 |                   |                |           |             |               |
|                    |                |                |                              |           |       |                 |       | managing        | and controlling   | the network,   |           | according   | to the intro- |
in different smart transportation applications with diverse duced new range of requirements by Industry 4.0. Facilitating
network requirements. Autonomous vehicles play a key role the network requirements through allocating resources effi-
in smart transportation. Several pieces of research have been ciently via network slicing has been examined in the existing
conducted to discuss the realisation of autonomous vehicles, researches. Hierarchical slicing can be used in large scale fac-
| including | fulfilling | network |     | requirements. |     | We identified | that |           |                       |     |       |         |            |
| --------- | ---------- | ------- | --- | ------------- | --- | ------------- | ---- | --------- | --------------------- | --- | ----- | ------- | ---------- |
|           |            |         |     |               |     |               |      | tories to | reduce the complexity | in  | MNO’s | network | and taking |
network slicing can be used to facilitate diverse network the management of the factory network to the factory author-
requirements of different applications in smart transporta- ity. Utilising network slicing to implement secure industry
tion. Moreover, MEC helps to fulfill latency requirements in networks has to be investigated further.
smart transportation applications. Slice isolation is lucrative 2) FutureDirections: UsingAR/VRtechnologiesinindus-
in implementing security and privacy requirements of trans- trial automation [204], [205] for operating machines remotely
portation communications. Dynamic allocation of network is a significant requirement to enhance the performance of a
resourceswithenhancedscalabilitymightberequiredinslices factorylineandreducethecost.Anotherrequirementisremote
allocatedtotransportationduetosuddentrafficsurgesinduced diagnosingfaultsandperformingnecessarymaintenanceactiv-
from irregular patterns of using vehicles. ities in machines. Network slicing is a salient technology
2) Future Directions: Though some researches can be that enables this feature and more researches can be con-
foundregardingnetworkslicingandsmarttransportation,most ducted in the future in this area. In [206], Backman et al.

984 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
proposedanovelconceptofblockchainsliceleasingledgerto Network slicing is recognised as the way of providing the
autonomously and dynamically acquire the slices needed for network requirements, such as very low latency and high
increasing the efficiency in future factories. Future researches security required to AR/VR applications over the common
canbedirectedinusingblockchaintechnologytothemanage- infrastructure. Modern games enforced with smart wearables
ment of 5G network slices that enable several new business and AR/VR tools that connect people around the world need
models for smart factories, as well as IT infrastructure. networkslicingtoattainitsnetworkrequirements,suchaslow
|     |     |     |     |     |     |     |     | latency | and high | throughput |     | over | the public | network | cost- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ---------- | --- | ---- | ---------- | ------- | ----- |
C. Smart Healthcare efficiently. Edge computing [210] is a supported technology
1) Lessons Learned: A myriad of use cases of the for the realisation of the AR/VR.
|     |     |     |     |     |     |     |     | 2) Future | Directions: |     | To  | the best | of our | knowledge | at the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | --- | -------- | ------ | --------- | ------ |
IoMT[207]intensifiestheneedofnetworkslicingtofacilitate
|               |         |     |              |             |      |           |       | time that  | we are  | doing | the survey, | no            | researches | can    | be found   |
| ------------- | ------- | --- | ------------ | ----------- | ---- | --------- | ----- | ---------- | ------- | ----- | ----------- | ------------- | ---------- | ------ | ---------- |
| heterogeneous | network |     | requirements | of          | each | use case. | Since |            |         |       |             |               |            |        |            |
|               |         |     |              |             |      |           |       | in network | slicing | and   | AR/VR       | applications. |            | Future | researches |
| IoMT deals    | with    | the | sensitive    | information | of   | people,   | secu- |            |         |       |             |               |            |        |            |
canbedirectedintherealisationofAR/VRapplicationsusing
| rity and | privacy | of the | exchanged | healthcare |     | data should | be  |     |     |     |     |     |     |     |     |
| -------- | ------- | ------ | --------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
preserved during the communication [208]. Technical aspects network slicing including satisfying AR/VR network require-
ments,suchassecurityandhighthroughput.Implementingthe
innetworkslicing,suchassliceisolationandadaptiveSFCto
sameservingslicewithinmultipleMNOsspreadoverdifferent
| change the | security-related |               | VNFs        | dynamically,  |        | are spotted | as      |              |         |     |             |     |        |        |     |
| ---------- | ---------------- | ------------- | ----------- | ------------- | ------ | ----------- | ------- | ------------ | ------- | --- | ----------- | --- | ------ | ------ | --- |
|            |                  |               |             |               |        |             |         | geographical | regions |     | is required | in  | modern | games. |     |
| preserving | ways             | to healthcare |             | data. Network |        | slicing     | and the |              |         |     |             |     |        |        |     |
| 5G network | support          | the           | realisation | of            | remote | surgeries   | [209]   |              |         |     |             |     |        |        |     |
that need ultra-reliable network requirements with very low F. Military Applications
latency and guaranteed bandwidth. 1) Lessons Learned: Military applications need extremely
2) Future Directions: Remote patients’ monitoring frame- securecommunicationwithveryhighprivacy.Networkslicing
| work collects |     | valuable | information |     | from wearables, |     | heart |               |     |        |        |          |        |     |          |
| ------------- | --- | -------- | ----------- | --- | --------------- | --- | ----- | ------------- | --- | ------ | ------ | -------- | ------ | --- | -------- |
|               |     |          |             |     |                 |     |       | is recognised |     | as the | way of | enabling | secure | and | privacy- |
monitors and infusion pumps to provide better treatment to preserved communication in military applications over the
| patients | in remote. | This | is highlighted |     | as a | future | direction |                 |     |              |     |             |            |     |         |
| -------- | ---------- | ---- | -------------- | --- | ---- | ------ | --------- | --------------- | --- | ------------ | --- | ----------- | ---------- | --- | ------- |
|          |            |      |                |     |      |        |           | public network. |     | Scalability, |     | dynamicity, | end-to-end |     | orches- |
of remote healthcare [88]. Healthcare-data transmission and tration, recursion, security, adaptive SFC and privacy are
data-management operations can be identified as very chal- all critical requirements in military networks, that can be
| lenging | research | topics | in healthcare |     | [89]. So, | the | attention |             |         |         |          |     |     |     |     |
| ------- | -------- | ------ | ------------- | --- | --------- | --- | --------- | ----------- | ------- | ------- | -------- | --- | --- | --- | --- |
|         |          |        |               |     |           |     |           | facilitated | through | network | slicing. |     |     |     |     |
of future researches can be paved the way to healthcare-data 2) Future Directions: As far as we are aware, there are no
| transmission | via | network | slicing. | AI/ML | techniques |     | can be |            |                |     |         |         |       |      |           |
| ------------ | --- | ------- | -------- | ----- | ---------- | --- | ------ | ---------- | -------------- | --- | ------- | ------- | ----- | ---- | --------- |
|              |     |         |          |       |            |     |        | scientific | investigations |     | in this | domain. | Thus, | this | area is a |
used to clean the collected massive healthcare data in MEC novel domain that researchers can direct their researches on
serverspriortransmittingtothecloudforanalysis.Facilitating the network slicing utilisation in military applications. Since
| network | requirements |     | in applying | AR/VR |     | technologies |     | in  |     |     |     |     |     |     |     |
| ------- | ------------ | --- | ----------- | ----- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
securityandprivacyaresupremeaspectsinthedefensesector,
remote surgeries and telemedicine via network slicing is an modernmethodsforenhancingtheseaspectsareneeded.Rapid
| enthralling                                               | research | direction. |            |           |            |              |           |                    |          |            |                                   |              |              |            |            |
| --------------------------------------------------------- | -------- | ---------- | ---------- | --------- | ---------- | ------------ | --------- | ------------------ | -------- | ---------- | --------------------------------- | ------------ | ------------ | ---------- | ---------- |
|                                                           |          |            |            |           |            |              |           | deployment         | of       | new slices | for                               | covering     | battlefields |            | and multi- |
|                                                           |          |            |            |           |            |              |           | domain             | slicing, | need       | to be                             | investigated | to           | facilitate | military   |
| D. Smart                                                  | City and | Home       |            |           |            |              |           | applications.      |          |            |                                   |              |              |            |            |
| 1) Lessons                                                | Learned: |            | Network    | slicing   | enhances   |              | the effi- |                    |          |            |                                   |              |              |            |            |
| ciencyofnetworkresourceutilisation,toenabletherealisation |          |            |            |           |            |              |           | G. Smart           | Grid     |            |                                   |              |              |            |            |
| of a smart                                                | city     | concept    | that has   | billions  | of devices | connected    |           |                    |          |            |                                   |              |              |            |            |
|                                                           |          |            |            |           |            |              |           | 1) LessonsLearned: |          |            | Networkslicingisthesolutionforthe |              |              |            |            |
| together                                                  | under    | various    | use cases. | Recursion |            | is discerned | as        |                    |          |            |                                   |              |              |            |            |
|                                                           |          |            |            |           |            |              |           | realisation        | of       | the smart  | grid                              | that needs   | several      | isolated   | slices     |
a salient aspect that supports the fast deploying of network for services such as smart metering and UAV-based power-
slicesforhomogeneoussmartcityusecases.Amongthesmart
|     |     |     |     |     |     |     |     | line inspection |     | to facilitate |     | diverse | network | requirements. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------- | --- | ------- | ------- | ------------- | --- |
homediversified-networkrequirements,security,performance,
|     |     |     |     |     |     |     |     | Slices need | to  | be distributed |     | over | a very | large | geographical |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | --- | ---- | ------ | ----- | ------------ |
costandmanagementshortcomingsareaddressedvianetwork
|     |     |     |     |     |     |     |     | area [211]. | MEC | can | be considered |     | as a | viable | solution for |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ------------- | --- | ---- | ------ | ------------ |
slicing elaborately.
|     |     |     |     |     |     |     |     | delay-sensitive |     | applications |     | in smart | grids. | Higher | scalability |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------ | --- | -------- | ------ | ------ | ----------- |
2) Future Directions: More elaborate pilots with more in the network requested by the massive number of connected
| devices      | in multiple     | home      | applications |            | are required, |            | despite |                      |          |          |                                    |              |       |            |             |
| ------------ | --------------- | --------- | ------------ | ---------- | ------------- | ---------- | ------- | -------------------- | -------- | -------- | ---------------------------------- | ------------ | ----- | ---------- | ----------- |
|              |                 |           |              |            |               |            |         | devices,             | such     | as smart | meters                             | to the       | grid, | can be     | facilitated |
| primitive    | implementations |           | of           | smart-home | solutions.    |            | This    | is                   |          |          |                                    |              |       |            |             |
|              |                 |           |              |            |               |            |         | via network          | slicing. |          |                                    |              |       |            |             |
| to recognise | the             | viability | of network   | slicing    | in            | smart      | homes.  |                      |          |          |                                    |              |       |            |             |
|              |                 |           |              |            |               |            |         | 2) FutureDirections: |          |          | Itispossibletofindhigh-levelinves- |              |       |            |             |
| Recursive    | composition     |           | of network   | slices     | can be        | researched |         | in                   |          |          |                                    |              |       |            |             |
|              |                 |           |              |            |               |            |         | tigations            | related  | to smart | grid                               | applications |       | in network | slicing.    |
order to support smart city use cases. However, scientific investigations specified for a particular
|     |     |     |     |     |     |     |     | application | related | to  | the grid | are | difficult | to find | and it will |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | -------- | --- | --------- | ------- | ----------- |
E. AR/VR/Gaming open a new research direction. Diverse energy sources and
1) Lessons Learned: AR/VR is becoming a realisation consumerscanbeconnectedtogethertobuildamoreeffective
through the 5G architecture. It extends its roots into multiple smart grid. More researches can be conducted in combining
service areas including mission-critical scenarios, like health- diverse sectors into the grid. Methods to improve the slice
care, and entertaining applications, like gaming and movies. coverage are required in smart grid applications.

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 985
H. UAVs and Drones is recognised as two main areas in achieving dynamicity via
1) Lessons Learned: In addition to the very fast communi- network slicing. We have identified that the number of active
|                     |     |     |             |     |      |                |     | connections | and | the amount | of  | traffic | flowed | vary | rapidly |
| ------------------- | --- | --- | ----------- | --- | ---- | -------------- | --- | ----------- | --- | ---------- | --- | ------- | ------ | ---- | ------- |
| cation requirements |     | for | controlling | the | UAV, | high-bandwidth |     |             |     |            |     |         |        |      |         |
requirements exist for applications like transferring the video in the IoT applications. Dynamic resource allocation using
|               |           |              |        |              |        |         |          | network           | slicing | is a possible |            | solution | to    | increase    | the effi- |
| ------------- | --------- | ------------ | ------ | ------------ | ------ | ------- | -------- | ----------------- | ------- | ------------- | ---------- | -------- | ----- | ----------- | --------- |
| recordings    | collected |              | by the | UAV. Network |        | slicing | provides |                   |         |               |            |          |       |             |           |
|               |           |              |        |              |        |         |          | cient utilisation |         | of network    | resources. |          | Rapid | deployments | of        |
| these diverse |           | requirements |        | on top       | of the | same    | physical |                   |         |               |            |          |       |             |           |
infrastructure. Slice isolation for providing required resources new slices for situations such as disaster management and
|     |     |     |     |     |     |     |     | battlefields, | intensify | the | need of | dynamicity |     | of the | network. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | ------- | ---------- | --- | ------ | -------- |
uninterruptedlyisacriticalrequirementinUAVs,toassurethe
best functionality. 2) Future Directions: AI/ML-based resource-requirement
|           |             |        |         |              |        |                |       | prediction | algorithms  | are        | a vital | requirement |            |     | in enhanc- |
| --------- | ----------- | ------ | ------- | ------------ | ------ | -------------- | ----- | ---------- | ----------- | ---------- | ------- | ----------- | ---------- | --- | ---------- |
| 2) Future | Directions: |        |         | Contribution | of     | Multiple       | Input |            |             |            |         |             |            |     |            |
|           |             |        |         |              |        |                |       | ing the    | flexibility | of dynamic |         | resource    | allocation |     | between    |
| Multiple  | Output      | (MIMO) | systems |              | in UAV | communications |       |            |             |            |         |             |            |     |            |
canbeconsideredasfutureresearchdirections.Improvingthe slices and it will be a sophisticated research direction. For
efficientdynamicresourceallocation,resource-allocationalgo-
| network | performance |     | in order | to increase | the | flying | time can |     |     |     |     |     |     |     |     |
| ------- | ----------- | --- | -------- | ----------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
alsobeconsidered.Application-specificoptimisationofdeploy- rithms should be designed with a very low computational
|     |     |     |     |     |     |     |     | complexity | [27]. | Due to | the heterogeneity |     |     | of Radio | Access |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ------ | ----------------- | --- | --- | -------- | ------ |
ment,mobilityandoperationsofdrones[212]areanimportant
|            |            |     |            |       |         |          |     | Technologies  | (RATs), | slicing | the      | RAN | is a        | complex | task and |
| ---------- | ---------- | --- | ---------- | ----- | ------- | -------- | --- | ------------- | ------- | ------- | -------- | --- | ----------- | ------- | -------- |
| research   | topic that | can | be tackled | using | network | slicing. |     |               |         |         |          |     |             |         |          |
|            |            |     |            |       |         |          |     | it aggravates | dynamic | RAN     | resource |     | allocation. |         |          |
| I. Massive | IoT        |     |            |       |         |          |     |               |         |         |          |     |             |         |          |
L. Recursion
| 1) Lessons |     | Learned: | A   | massive | number | of  | connected |     |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --- | ------- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
devices with low power and low data rates increases the 1) Lessons Learned: Slice creation is a frequent activity
|             |     |           |         |        |      |        |         | due to various  |     | slice requirements |          | with   | slight | changes | among    |
| ----------- | --- | --------- | ------- | ------ | ---- | ------ | ------- | --------------- | --- | ------------------ | -------- | ------ | ------ | ------- | -------- |
| requirement | of  | dedicated | network | slices | with | simple | network |                 |     |                    |          |        |        |         |          |
|             |     |           |         |        |      |        |         | them. Recursion |     | supports           | creating | slices | using  | the     | existing |
functionsoverthecommonnetworkinfrastructure,duetosim-
ple power-preserving communication requirements. Massive slices and it reduces the complexity of creating new slices
|         |         |           |         |     |         |         |          | while fastening |     | the deployment |     | of new | ones. | We  | recognised |
| ------- | ------- | --------- | ------- | --- | ------- | ------- | -------- | --------------- | --- | -------------- | --- | ------ | ----- | --- | ---------- |
| amounts | of data | collected | through | the | sensors | in this | applica- |                 |     |                |     |        |       |     |            |
tion can be processed in the edge to reduce the burden in the that the recursion supports the rapid expansion of the IoT in
| core network. |             |     |        |                |     |            |     | novel application |             | areas. |       |           |     |         |          |
| ------------- | ----------- | --- | ------ | -------------- | --- | ---------- | --- | ----------------- | ----------- | ------ | ----- | --------- | --- | ------- | -------- |
|               |             |     |        |                |     |            |     | 2) Future         | Directions: |        | Since | recursion | is  | a novel | concept, |
| 2) Future     | Directions: |     | Simple | authentication |     | mechanisms |     |                   |             |        |       |           |     |         |          |
for these kinds of devices can be implemented as VNFs there is a lot to investigate under this aspect. To the best of
|         |          |     |          |            |     |         |          | our knowledge |     | at the time | we  | are conducting |     | the | research, |
| ------- | -------- | --- | -------- | ---------- | --- | ------- | -------- | ------------- | --- | ----------- | --- | -------------- | --- | --- | --------- |
| so that | they can | be  | deployed | in network |     | slices. | They are |               |     |             |     |                |     |     |           |
a vital requirement and further investigations can be done we couldn’t find a dedicated scientific investigation regarding
in this area. Scientific investigations related to RAN-slicing implementing recursion in network slicing. Required algo-
rithms,entities,protocolsandinterfacesneedstoberesearched
| techniques | for | massive | IoT | scenarios | are also | an  | interesting |     |     |     |     |     |     |     |     |
| ---------- | --- | ------- | --- | --------- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
research direction. Methods to improve the coverage of the in implementing recursion.
slicesarerequiredwhenfacilitatingenvironmentalmonitoring.
|     |     |     |     |     |     |     |     | M. Adaptive | SFC |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
J. Scalability
|     |     |     |     |     |     |     |     | 1) Lessons | Learned: |     | Network | slice | that | is allocated | for a |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ------- | ----- | ---- | ------------ | ----- |
1) Lessons Learned: With the exploitation of the IoT for particular use case can be identified as an SFC itself. It runs
a myriad of applications, an enormous quantity of devices on the principles of SFC [213]. The chain of the NFs will be
with diverse network requirements exist for connecting. The neededtochangeaccordingtothedifferentsituations,suchas
|        |             |           |     |         |            |      |      | deploying | a security | function | when | there | is  | a security | attack |
| ------ | ----------- | --------- | --- | ------- | ---------- | ---- | ---- | --------- | ---------- | -------- | ---- | ----- | --- | ---------- | ------ |
| number | of actively | connected |     | devices | is varying | from | time | to        |            |          |      |       |     |            |        |
time. This escalates the need for a scalable network. Through andremovingthesecurityfunctionaftertheattack.Theadapt-
slicing the network and changing the network-resource allo- ability of the SFC in the network slice supports minimising
|                    |     |       |         |     |                  |     |          | the cost | related | to the network |     | in terms | of  | the resources | and |
| ------------------ | --- | ----- | ------- | --- | ---------------- | --- | -------- | -------- | ------- | -------------- | --- | -------- | --- | ------------- | --- |
| cation dynamically |     | (with | respect | to  | the requirements |     | like the |          |         |                |     |          |     |               |     |
amount of traffic through the slice), network slicing increases time, as well as increasing the productivity of the use case.
the scalability of the network. 2) FutureDirections: Asstatedin[29],therearetwomain
2) Future Directions: Extending the proposed dynamic challenges in SFC: selecting the optimal node and the routing
network-slicing framework for fog computing systems into schemefortheselectednodes.AI/ML-basedalgorithmscanbe
developedinselectingoptimalnodesandtheoptimumrouting
| the 5G | core network |     | is stated | as a | future | research | direction |     |     |     |     |     |     |     |     |
| ------ | ------------ | --- | --------- | ---- | ------ | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
in[46].Dynamicresourceallocationisanimportantaspectof scheme for the SFC.
| the operation                                          | of             | improving |           | scalability. | The    | use of | prediction |             |          |     |                  |     |     |          |          |
| ------------------------------------------------------ | -------------- | --------- | --------- | ------------ | ------ | ------ | ---------- | ----------- | -------- | --- | ---------------- | --- | --- | -------- | -------- |
| algorithmsbasedontheAI/MLtechniquestopredictthetraffic |                |           |           |              |        |        |            | N. Security |          |     |                  |     |     |          |          |
| pattern is                                             | an enthralling |           | direction | that         | can be | used   | to enhance |             |          |     |                  |     |     |          |          |
|                                                        |                |           |           |              |        |        |            | 1) Lessons  | Learned: |     | IoT exploitation |     | in  | critical | applica- |
the scalability of the network. tions like smart grids and military applications and sensitive
|     |     |     |     |     |     |     |     | applications | like | smart | health, | increases | the | security | require- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ----- | ------- | --------- | --- | -------- | -------- |
K. Dynamicity
|     |     |     |     |     |     |     |     | ments. To | accomplish | the | different | security |     | levels | in the IoT |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | --------- | -------- | --- | ------ | ---------- |
1) Lessons Learned: Dynamic resource allocation between applications, network slicing can be considered as one of the
slices and the ability to deploy network slices dynamically optimum technologies. Slice isolation in network slicing is

986 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
identified as the basic way of providing security between dif- Q. Resource Management
ferentapplications.Deploymentofdifferentsecurityfunctions
1) Lessons Learned: IoT increases the resource require-
intheslicesisanotherwaytoachievesecurityrequirements.In
ments in the telecommunication networks that can’t be
addition to the traditional security challenges, a series of new
satisfied cost-efficiently using traditional methods. We iden-
security challenges have been introduced due to network slic-
tified that the network slicing is the modern solution for
ing.Securityinnetworkslicingcanbedividedintothreemain
addressing this problem. Assigning a dedicated amount of
parts: life cycle security, inter-slice security and intra-slice
resources for each slice, along with the ability to dynami-
security [179].
cally reassign or overbook the allocated resources, increases
2) Future Directions: Due to the lack of large-scale imple-
the resource utilisation efficiency and cost-efficiency of the
mentations of network slicing and the ongoing 5G security
system [214]. Assuring the SLAs of the connected third-party
specifications being prone to change, the analysis of network
tenants due to heterogeneous applications, including the IoT,
slicing security is still in an incipient phase [179]. Slice iso-
becomes a reality due to network slicing [215].
lation is a critical requirement in achieving security. Several
2) Future Directions: Radio resource management with
possible research directions can be identified, such as level of
guaranteeing the diverse QoS requirements is a challenging
isolationandinter-slicecommunicationwithsliceisolation.As
task [28]. Investigating efficient methods for RAN resource
discussed in [179], solutions for life cycle security, inter-slice
management for RAN slicing is a possible future research
securityandintra-slicesecuritycanbeinvestigated.Duetothe
direction.In[215],Khodapanah etal.highlighted therequire-
third-party involvement in management scenarios of network
ment of an intelligent slice management function for fulfilling
slicing,aseriesofunknown securityattacks willbe generated
the SLAs of different network slices in the network. AI/ML-
and those can be examined in future researches.
related algorithms for predicting resource requirements is a
novel approach that can be used in resource management in
O. Privacy
network slicing.
1) Lessons Learned: Since IoT has entered to the appli-
cations that deal with sensitive information like healthcare
VIII. EMERGINGANDFUTURERESEARCHDIRECTIONS
applications and military applications, privacy became a
FORNETWORKSLICINGANDIOTINTEGRATION
momentous requirement. Allocating separate slices for differ-
In this section, we present some of the novel technolo-
entapplicationswithstrongsliceisolationmechanismsallows
gies and their impact on network slicing and IoT realisation.
privacy-preservation of the data communicated in different
Blockchain, AI/ML, multi-domain slicing and hierarchical
slices. The ability to change the privacy-related network func-
slicing will be covered in here.
tions of the network slice dynamically facilitates to corporate
more privacy-preserving facilities into the IoT data streams.
A. Network Slicing and Blockchain
2) Future Directions: As slice isolation is a critical
requirement in preserving privacy, implementing an E2E Blockchain is a novel technology that began to attract the
isolatednetworksliceneedstobeinvestigated.Novelprivacy- attention as the basis of cryptocurrencies such as Bitcoin. It
protecting algorithms that can be implemented as VNFs and hastheabilitytovastlyimprovetheexistingtechnologyappli-
deployed in a slice can be addressed. Effectuating concepts cations,aswellastoenabletherealisationofthenewapplica-
like Privacy by design and Sensitive Data Protection (SDP) in tionsthatwereneverpreviouslypracticaltobedeployed[216].
network slicing to preserve privacy can be studied. Blockchain can be identified as a time-stamped series of
data that are immutable. This means once data is added to
P. End-to-End Orchestration
the blockchain, they cannot be deleted or modified. Data is
1) Lessons Learned: Network slicing is an end-to-end stored in the blocks that are connected to each other and
technologythatenablesthedeploymentofslices,fromthecus- secured, using cryptographic principles. Different kinds of
tomer end to the application backend, through the network. It existing blockchain-based activities can be categorised into
hastheabilitytochangetheconfigurationsinslicesaccording three areas: Blockchain 1.0 for currency-related operations,
to the SLAs between the tenants and the network providers. Blockchain 2.0 for contracts such as stocks, bonds and loans
Thissmoothsthejoiningofnewapplicationsintothe5Gmar- andBlockchain3.0forapplicationssuchashealth,scienceand
ket,includingdiverseIoTapplications.Werecognisedthatthe literacy [217], [218]. Blockchain has been rapidly utilised to
diverse management requirements during the end-to-end traf- register,authenticateandvalidateassetsandtransactions.Ithas
ficflowofvariousIoTapplicationscanbeaccomplishedusing alsobeenutilisedtorecorddata,managetheidentificationand
the end-to-end orchestration property of network slicing. govern interactions among multiple parties [219]. As well as
2) Future Directions: Though there are proposed E2E in the other application areas, blockchains can be utilised in
network slicing management and orchestration frameworks, the telecommunication applications such as fraud detection,
a sophisticated E2E orchestration and management plane Identity-as-a-Service and data management, 5G enablement
is required. It must have adaptive solutions for man- and the IoT connectivity [220]–[222]. In [219], Chaer et al.
aging resources holistically and efficiently, through mak- identified the main five areas that can be used blockchain
ing the decisions according to the current state of in 5G networks: 5G infrastructure and crowdsourcing, 5G-
the slice, as well as the predictions of future user infrastructure sharing, international roaming, network slicing
demands [21]. and management and authentication of mMTC and uRLLC.

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 987
Fig.17. RoleofBlockchainforNetworkslicinginIoT.
Figure 17 explains how blockchain can be used to achieve serve a plethora of vertical services including the IoT [227].
benefits in network slicing and in different IoT applications. Networkslicingneedsintegrationandmoreintelligentcapabil-
Network slice broker is a popular research area of using itiesbasedonMLandbigdataapplications,inordertoachieve
blockchain in network slicing and several researches can be functionalitiessuchasself-configuration,self-optimisationand
found in this domain [206], [223]–[225]. In [223], Nour et al. faultmanagement[228].MLtechniques(i.e.,supervisedlearn-
proposed a network slice broker design based on blockchain ing, unsupervised learning and reinforcement learning) have
technology. It supports the slice provider that is a new role been extensively used in improving network security, includ-
included in 5G, to select resources from different resource ing authentication, access control, malware detection and
providers and create E2E slices. They envisioned a subslice- anti-jamming offloading [229]. A comprehensive survey on
deployment-brokering mechanism as a series of small con- resource management in cellular and IoT networks using ML
tracts.In[224],Zanzietal.proposedanovelnetwork-slicing- techniques, was presented in [230]. Figure 18 shows how
brokeringsolutionthatleveragesblockchaintechnologycalled AI/ML can be used in network slicing and in different IoT
NSBchain. It allows the allocation of network resources from application scenarios.
Infrastructure Providers (InPs) to the Intermediate broker (IB) In [231], Thantharate et al. implemented a deep learning
viasmartcontracts.ItalsoallowsIBtoassignandredistribute neural network, to develop a DeepSlice model to manage
their resources to tenants in a secure, automated and scal- network-load efficiency and network availability. It covers
able manner. In [225], Valtanen et al. presented a blockchain three main goals: appropriate slice selection for a device, cor-
network-slice-brokeringusecasevalueanalysis.Theyusedan rectslicepredictionandallocatingrequiredresourcesbasedon
industrialautomationscenarioasausecaseintheirpaperthat thetrafficpredictionandadaptionofsliceassignments,incase
acquired the slices needed autonomously and dynamically. ofnetworkfailures.In[232],Meietal.proposedanintelligent
network-slicing architecture for V2X services that leverages
B. Network Slicing and Machine Learning/Artificial the recent advancements of ML technologies. A novel deep
Intelligence reinforcement algorithm is proposed to automate the deploy-
Artificial Intelligence (AI) and Machine Learning (ML) ment of network slices based on the collected historical data
are revolutionary technologies that have become ubiqui- of vehicular networks. A deep reinforcement algorithm was
tous in every field, making machines intelligent in order proposed in [233] for resource mapping in 5G network slic-
to make decisions themselves without any human interven- ing. The proposed RLCO algorithm was able to solve the
tion. Telecommunication operators tend to use ML techniques problems of poor efficiency of existing algorithms in virtual
in multifarious areas such as network automation, customer network mapping, low resource utilisation and poor coordi-
experience, business process automation, infrastructure main- nation between node mapping and link mapping. In [234],
tenance and new digitalservices [226].MLcan be recognised De Bast et al. proposed a fast-learning Deep Reinforcement
as a necessary part of any 5G network, due to its higher com- Learning (DRL) model that has the ability to optimise the
plexity than previous generation networks and the ability to slice configuration of unplanned Wi-Fi networks dynamically

988 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
Fig.18. RoleofAI/MLfornetworkslicinginIoT.
Fig.19. Multi-domainnetworkslicing.
without expert knowledge. The proposed approach was able high-quality connectivity infrastructure in specific locations
to optimise various Wi-Fi parameters per slice dynamically. such as schools and transport hubs, the context-driven and
|                 |                    |         | location-specific     | needs for wireless    | connectivity | in different  |
| --------------- | ------------------ | ------- | --------------------- | --------------------- | ------------ | ------------- |
| C. Multi-Domain | and Multi-Operator | Slicing |                       |                       |              |               |
|                 |                    |         | facilities, different | business requirements | for          | deployment of |
Network slices that are allocated to different vertical appli- 5G networks, and the growing interest for local 5G networks
cations, may be spread over large geographical areas or to serve restricted set of customers such as in a factory envi-
encompassing areas where coverage can’t be provided by a ronment, are some facts that burgeon the concept of local
single operator, may need to combine resources from differ- 5G operators concept [235]. Therefore, the involvement of
ent operators to provide the coverage [75]. Provisioning of multiple administrative domains in creating and operating the

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 989
a hierarchical resource allocation architecture for network
slicing. In there, they use Global Radio Resource Manager
(GRRM) to allocate resources for a slice and Local Radio
Resource Manager (LRRM) that is specific for the slice, to
further divide the allocated amount of resources for the slice
among the UEs. To the best of our knowledge, there are no
significantscientificinvestigationsthatwereconductedinhier-
archical slicing and hence, this is a rich area for conducting
future researches.
IX. CONCLUSION
Network slicing is becoming a reality in future telecommu-
Fig.20. HierarchicalslicingArchitecture.
nication networks, due to the support of several technologies,
such as SDN, NFV and cloud computing. It has been iden-
tified as an inevitable technology in the realisation of the
network slices for providing a better service is a significant
IoT solutions that are proliferating in several applications
requirement in novel 5G networks.
with heterogeneous network requirements. We comprehen-
Figure 19 shows the concept of multi-domain network
sively discussed how network slicing can be used in different
slicing that depicted a network slice spanned over three
IoTapplications,alongwiththeexistingresearchesandfuture
administrative domains. As shown in the figure, a minimum
researchdirectionsforeachapplication.Technicalaspectsthat
of three orchestrators are needed to facilitate multi-domain
can be improved in the IoT through network slicing were
network slicing. One is domain-specific-slice orchestrator for
explored. Although network slicing imparts a lot of advan-
themanagementandorchestrationoftheNetworkSliceSubnet
tages in the IoT realisation, several technical challenges in
Instances(NSSIs)ineachdomain.Anotherisdomain-specific-
network slicing will mature, due to the evolution of the IoT.
NFVI orchestrator for managing network resources. Thirdly,
We identified those challenges during the survey. Since the
multi-domain E2E-slice orchestrator for E2E management
lack of large-scale implementations of slicing and the spec-
of the NS. The significant challenges in multi-domain slic-
ifications related to network slicing that are still prone to
ing includes identifying the necessary administrative domains
changes, network slicing is a rich area that has several possi-
with required resources to deploy the NSSIs, stitching them
ble future research directions. In all essence, network slicing
to create the federated NSI, and the run-time coordination
andIoTaretwocomplementarytechnologiesthat,ifwellhar-
of the management operations across different administra-
nessed, have the potential of enabling the smart world since
tive domains [75]. The open-research challenges in the area
5G networks and beyond.
of multi-domain network slicing are service-management
interfaces and service profiling, resource sharing and isolation
and service-based network management [75].
REFERENCES
[1] P.F.P.Guillemin.(2009).TheIndustrialInternetofThingsVolumeG1:
Reference Architecture. [Online]. Available: http://www.internet-of-
D. Hierarchical Slicing
things-research.eu/pdf/IoTClusterStrategicResearchAgenda2009.pdf
Hierarchicalslicingisanexoticareainnetworkslicingthat [2] M.Hatton,“TheglobalM2Mmarketin2013,”London,U.K.,Machina
Research,WhitePaper,Jan.2013.
will generate new business models. Ordinarily, MNO creates
[3] Y.Zhou,F.R.Yu,J.Chen,andY.Kuo,“Cyber-physical-socialsystems:
networkslicesaccordingtotherequirementsreceivedfromthe Astate-of-the-artsurvey,challengesandopportunities,”IEEECommun.
thirdpartytenants.Thoughitsatisfiesthebasiccommunication SurveysTuts.,vol.22,no.1,pp.389–425,1stQuart.,2020.
[4] B. Blanco et al., “Technologypillars in the architecture offuture 5G
requirements of the tenant, he may need to further slice the
mobile networks: NFV, MEC and SDN,” Comput. Stand. Interfaces,
received network slice into more subslices that are specified vol.54,pp.216–228,Nov.2017.
forseparateserviceareasoftheparticulartenant.Asanexam- [5] V. W. Wong, Key Technologies for 5G Wireless Systems. Cambridge,
U.K.:CambridgeUniv.Press,2017.
ple,agiant-sizedsmartfactorycangetadedicatedslicefroma
[6] W. H. Chin, Z. Fan, and R. Haines, “Emerging technologies
largeMNO.Butthefactoryneedstofurtherslicethereceived and research challenges for 5G wireless networks,” IEEE Wireless
network slice into more slices that are specialised to different Commun.,vol.21,no.2,pp.106–112,Apr.2014.
[7] M. Liyanage, A. Gurtov, and M. Ylianttila, Software Defined Mobile
applications in the factory, such as operating machines, mon-
Networks (SDMN): Beyond LTE Network Architecture. Chichester,
itoring the factory environment and communication between U.K.:Wiley,2015.
employees. This can be recognised as the concept of hierar- [8] M. Jarschel, T. Zinner, T. Hoßfeld, P. Tran-Gia, and W. Kellerer,
“Interfaces, attributes, and use cases: A compass for SDN,” IEEE
chical slicing.Reference [236]highlights asetof key features
Commun.Mag.,vol.52,no.6,pp.210–217,Jun.2014.
in hierarchical network slicing concepts, such as multi-tenant [9] Y.LiandM.Chen,“Software-definednetworkfunctionvirtualization:
Virtual Service Networks (VSNs) with embedded slices, hier- Asurvey,”IEEEAccess,vol.3,pp.2542–2553,2015.
[10] P.Ranaweera,A.D.Jurcut,andM.Liyanage,“Realizingmulti-access
archicalSDNcontrolandNFVintegrationanddistributedslice
edgecomputingfeasibility:Securityperspective,”inProc.IEEEConf.
selection. Stand.Commun.Netw.(CSCN),2019,pp.1–7.
Figure 20 shows the concept of hierarchical slicing. [11] P.Porambage,J. Okwuibe,M.Liyanage, M.Ylianttila, andT.Taleb,
“Survey on multi-access edge computing for Internet of Things real-
Allocated slice is sliced again into three slices that are speci-
ization,”IEEECommun.SurveysTuts.,vol.20,no.4,pp.2961–2991,
fied for the services of the tenant. In [80], Sun et al. proposed 4thQuart.,2018.

990 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
[12] P. C. Chih and I. Lin, End to End Network Slicing, Wireless World [37] S.Antipolis,“Studyonarchitecturefornextgenerationsystem,release
Res.Forum,Zurich,Switzerland,2017. 14,”3GPP,SophiaAntipolis,France,Rep.23.799,Dec.2016.
[13] Nokia,Huawei,andEricsson,“5Gnetworkslicingforverticalindus- [38] M. A. Habibi, B. Han, and H. D. Schotten, “Network slicing in 5G
tries,” Global Mobile Suppliers Assoc., London, U.K., Rep., 2017. mobilecommunicationarchitecture, profitmodeling,andchallenges,”
[Online]. Available: https://www.huawei.com/minisite/5g/img/5g- 2017.[Online].Available:arXiv:1707.00852.
network-slicing-for-vertical-industries-en.pdf [39] P.PorambageandM.Liyanage,“Securityinnetworkslicing,”Wiley5G
[14] “Service requirements for the 5G system: Stage I,” 3GPP, Sophia Ref: The Essential 5G Reference Online. Hoboken, NJ, USA: Wiley,
Antipolis,France,Rep.22.261,Aug.2016. 2019,pp.1–12.
[15] “Feasibility study on new services and markets technology enablers [40] T. Yoo, “Network slicing architecture for 5G network,” in Proc.
network operation,” 3GPP, Sophia Antipolis, France, Rep. 22.864, Int. Conf. Inf. Commun. Technol. Convergence (ICTC), 2016,
Jan.2016. pp.1010–1014.
[16] “Systemarchitectureforthe5G,”3GPP,SophiaAntipolis,France,Rep. [41] S. Staff. (Dec. 2017). What is Dynamic Network Slicing? What is
23.501,Dec.2016. DynamicNetworkSlicing?[Online].Available:https://www.sdxcentral.
[17] “Study on architecture for next generation syste,” 3GPP, Sophia com/5g/definitions/dynamic-network-slicing/
Antipolis,France,Rep.23.799,Dec.2015. [42] Techopedia.(Jan.2017).Scalability.[Online].Available:https://www.
[18] “Description of network slicing concept,” NGMN Alliance, techopedia.com/definition/9269/scalability
Frankfurt, Germany, Rep., Jan. 2016. [Online]. Available: [43] 3GPP. (2016). Network Sharing; Architecture and Functional
https://www.ngmn.org/wp-content/uploads/Publications/2016/161010_ Descriptio. [Online]. Available: https://portal.3gpp.org/
NGMN_Network_Slicing_framework_v1.0.8.pdf desktopmodules/Specifications/SpecificationDetails.aspx?
[19] I.Afolabi,T.Taleb,K.Samdanis,A.Ksentini,andH.Flinck,“Network specificationId=830
slicingandsoftwarization:Asurveyonprinciples,enablingtechnolo- [44] (Jan. 2020). The IoT Rundown for 2020: Stats, Risks, and Solutions.
gies, and solutions,” IEEE Commun. Surveys Tuts., vol. 20, no. 3, [Online].Available:https://securitytoday.com/Articles/2020/01/13/The-
pp.2429–2453,3rdQuart.,2018. IoT-Rundown-for-2020.aspx?Page=2
[20] P.Schulzetal.,“LatencycriticalIoTapplicationsin5G:Perspectiveon [45] P.Rostetal.,“Networkslicingtoenablescalabilityandflexibilityin
thedesignofradiointerfaceandnetworkarchitecture,”IEEECommun. 5Gmobilenetworks,”IEEECommun.Mag.,vol.55,no.5,pp.72–79,
Mag.,vol.55,no.2,pp.70–78,Feb.2017. 2017.
[21] A. A. Barakabitze, A. Ahmad, R. Mijumbi, and A. Hines, “5G [46] Y.XiaoandM.Krunz,“Dynamicnetworkslicingforscalablefogcom-
network slicing using SDN and NFV: A survey of taxonomy, archi- putingsystemswithenergyharvesting,”IEEEJ.Sel.AreasCommun.,
tectures and future challenges,” Comput. Netw., vol.167, Feb. 2020, vol.36,no.12,pp.2640–2654,Dec.2018.
Art.no.106984. [47] M. Jiang, M. Condoluci, and T. Mahmoodi, “Network slicing man-
[22] A. Kaloxylos, “A survey and an analysis of network slicing in 5G agement & prioritization in 5G mobile systems,” in Proc. Eur. 22nd
networks,” IEEE Commun. Stand. Mag., vol. 2, no. 1, pp.60–65, WirelessConf.,2016,pp.1–6.
Mar.2018. [48] Y. L. Lee, J. Loo, T. C. Chuah, and L.-C. Wang, “Dynamic network
[23] Q.ChenandC.Liu,“Asurveyofnetworkslicingin5G,”inProc.Int. slicing for multitenant heterogeneous cloud radio access networks,”
Conf.Comput.Sci.Mech.Autom.(CSMA),2017,pp.27–35. IEEE Trans. Wireless Commun., vol. 17, no. 4, pp.2146–2161,
[24] L.Zhangetal.,“Asurveyon5Gnetworkslicingenablingthesmart Apr.2018.
grid,”inProc.IEEE25thInt.Conf.ParallelDistrib.Syst.(ICPADS), [49] A.Mayoral,R.Vilalta,R.Casellas,R.Martinez,andR.Munoz,“Multi-
2019,pp.911–916. tenant 5G network slicing architecture with dynamic deployment of
[25] J. Ordonez-Lucena, P. Ameigeiras, D. Lopez, J. J. Ramos-Munoz, virtualizedtenantmanagementandorchestration(MANO)instances,”
J. Lorca, and J. Folgueira, “Network slicing for 5G with SDN/NFV: inProc.42ndEur.Conf.Opt.Commun.,2016,pp.1–3.
Concepts,architectures,andchallenges,”IEEECommun.Mag.,vol.55, [50] D. Sattar and A. Matrawy, “Towards secure slicing: Using slice iso-
no.5,pp.80–87,May2017. lationtomitigateDDoSattackson5Gcorenetworkslices,” inProc.
[26] X.Foukas,G.Patounas,A.Elmokashfi,andM.K.Marina,“Network IEEEConf.Commun.Netw.Security(CNS),2019,pp.82–90.
slicingin5G:Surveyandchallenges,”IEEECommun.Mag.,vol.55, [51] P. Schneider, C. Mannweiler, and S. Kerboeuf, “Providing strong 5G
no.5,pp.94–100,May2017. mobilenetworksliceisolationforhighlysensitivethird-partyservices,”
[27] R.Suetal.,“Resourceallocationfornetworkslicingin5Gtelecom- inProc.IEEEWirelessCommun.Netw.Conf.(WCNC),2018,pp.1–6.
municationnetworks:Asurveyofprinciplesandmodels,”IEEENetw., [52] D. Sattar and A. Matrawy, “Optimal slice allocation in 5G core
vol.33,no.6,pp.172–179,Nov./Dec.2019. networks,”IEEENetw.Lett.,vol.1,no.2,pp.48–51,Jun.2019.
[28] M.Richart,J.Baliosian,J.Serrat,andJ.-L.Gorricho,“Resourceslicing [53] A.Mathew,“Networkslicingin5Gandthesecurityconcerns,”inProc.
in virtual wireless networks: A survey,” IEEE Trans. Netw. Service 4thInt.Conf.Comput.Methodol.Commun.(ICCMC),2020,pp.75–78.
Manag.,vol.13,no.3,pp.462–476,Sep.2016. [54] T.Haugen,A.A.Hassan,andP.F.Menezes,“Devicequarantineina
[29] L.U.Khan,I.Yaqoob,N.H.Tran,Z.Han,andC.S.Hong,“Network wirelessnetwork,”U.S.Patent9717006,Jul.25,2017.
slicing:RecentAdvances,taxonomy,requirements,andopenresearch [55] V.K.Choyi,A.Abdel-Hamid,Y.Shah,S.Ferdi,andA.Brusilovsky,
challenges,”IEEEAccess,vol.8,pp.36009–36028,2020. “Networksliceselection,assignmentandroutingwithin5Gnetworks,”
[30] W. Rafique, L. Qi, I. Yaqoob, M. Imran, R. U. Rasool, and W. Dou, inProc.IEEEConf.Stand.Commun.Netw.(CSCN),2016,pp.1–7.
“ComplementingIoTservicesthroughsoftwaredefinednetworkingand [56] P.Porambage,Y.Miche,A.Kalliola,M.Liyanage,andM.Ylianttila,
edge computing: A comprehensive survey,” IEEE Commun. Surveys “Securekeyingschemefornetworkslicingin5Garchitecture,”inProc.
Tuts.,vol.22,no.3,pp.1761–1804,3rdQuart.,2020. IEEEConf.Stand.Commun.Netw.(CSCN),2019,pp.1–6.
[31] X.Zhou,R.Li,T.Chen,andH.Zhang,“Networkslicingasaservice: [57] M. Nawir, A. Amir, N. Yaakob, and O. B. Lynn, “Internet of Things
Enabling enterprises’ own software-defined cellular networks,” IEEE (IoT):Taxonomyofsecurityattacks,”inProc.3rdInt.Conf.Electron.
Commun.Mag.,vol.54,no.7,pp.146–153,Jul.2016. Design(ICED),2016,pp.321–326.
[32] V. Sciancalepore, F. Cirillo, and X. Costa-Perez, “Slice as a ser- [58] D. Stiawan, M. Idris, R. F. Malik, S. Nurmaini,
vice(SlaaS)optimalIoTsliceresourcesorchestration,”inProc.IEEE N. Alsharif, and R. Budiarto, “Investigating brute force
GlobalCommun.Conf.,2017,pp.1–7. attack patterns in IoT network,” J. Electr. Comput. Eng.,
[33] Q.Li,G.Wu,A.Papathanassiou,andU.Mukherjee,“Anend-to-end vol.2019, Jan. 2019, Art. no. 4568368. [Online]. Available:
network slicing framework for 5G wireless communication systems,” https://www.hindawi.com/journals/jece/2019/4568368/
2016.[Online].Available:arXiv:1608.00572. [59] N.JOSHI. (May2019).8Types ofSecurityThreats toIoT.[Online].
[34] V. P. Kafle, Y. Fukushima, P. Martinez-Julia, T. Miyazawa, and Available: https://www.allerin.com/blog/8-types-of-security-threats-to-
H. Harai, “Adaptive virtual network slices for diverse IoT services,” iot
IEEECommun.Stand.Mag.,vol.2,no.4,pp.33–41,Dec.2018. [60] R.Khan,P.Kumar,D.N.K.Jayakody,andM.Liyanage,“Asurvey
[35] J. Ni, X. Lin, and X. S. Shen, “Efficient and secure service-oriented onsecurityandprivacyof5Gtechnologies:Potentialsolutions,recent
authentication supporting network slicing for 5G-enabled IoT,” IEEE advancements and future directions,” IEEE Commun. Surveys Tuts.,
J.Sel.AreasCommun.,vol.36,no.3,pp.644–657,Mar.2018. vol.22,no.1,pp.196–248,1stQuart.,2020.
[36] C. Kolias, G. Kambourakis, A. Stavrou, and J. Voas, “DDoS in the [61] I.Butun,P.Österberg,andH.Song,“SecurityoftheInternetofThings:
IoT: Mirai and other botnets,” Computer, vol. 50, no. 7, pp.80–84, Vulnerabilities,attacks,andcountermeasures,”IEEECommun.Surveys
Jul.2017. Tuts.,vol.22,no.1,pp.616–644,1stQuart.,2020.

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 991
[62] S.A.Hamad,Q.Z.Sheng,W.E.Zhang,andS.Nepal,“Realizingan [85] A.E.Kalør,R.Guillaume,J.J.Nielsen,A.Mueller,andP.Popovski,
InternetofSecureThings:Asurveyonissuesandenablingtechnolo- “Network slicing in industry 4.0 applications: Abstraction methods
gies,” IEEE Commun. Surveys Tuts., vol. 22, no. 2, pp.1372–1391, andend-to-endanalysis,”IEEETrans.Ind.Informat.,vol.14,no.12,
| 2ndQuart.,2020. |     |     |     |     |     |     |     | pp.5419–5427,Dec.2018. |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
[63] 5G Security Recommendations Package# 2: Network Slicing, NGMN [86] V. Theodorou, K. V. Katsaros, A. Roos, E. Sakic, and V. Kulkarni,
Alliance,Frankfurt,Germany,2016. “Cross-domain network slicing for industrial applications,” in Proc.
[64] K.Bhardwaj,J.C.Miranda,andA.Gavrilovska,“TowardsIoT-DDOS Eur.Conf.Netw.Commun.(EuCNC),2018,pp.209–213.
prevention using edge computing,” in Proc. {USENIX} Workshop [87] A. Mavrogiorgou, A. Kiourtis, M. Touloupou, E. Kapassa, and
Hot Topics Edge Comput. (HotEdge), 2018. [Online]. Available: D.Kyriazis,“InternetofMedicalThings(IoMT):Acquiringandtrans-
https://www.usenix.org/system/files/conference/hotedge18/hotedge18- formingdataintoHL7FHIRthrough5Gnetworkslicing,”Emerg.Sci.
| papers-bhardwaj.pdf |     |     |     |     |     |     |     | J.,vol.3,no.2,pp.64–77,2019. |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
[65] V. A. Cunha et al., “Network slicing security: Challenges and direc- [88] A. H. Celdrán, M. G. Pérez, F. J. G. Clemente, F. Ippoliti, and
tions,”InternetTechnol.Lett.,vol.2,no.5,p.e125,2019.
|     |     |     |     |     |     |     |     | G. M. | Pérez, “Dynamic |     | network slicing | management |     | of multimedia |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------------- | --- | --------------- | ---------- | --- | ------------- |
[66] GeneralDataProtectionRegulation.Accessed:Aug.4,2020.[Online]. scenarios for future remote healthcare,” Multimedia Tools Appl.,
Available:https://gdpr-info.eu/ vol.78,no.17,pp.24707–24737,2019.
[67] Y.Zhang,J.Li,D.Zheng,P.Li,andY.Tian,“Privacy-preservingcom- [89] E. Kapassa et al., “An innovative eHealth system powered by 5G
| munication | and | power | injection | over vehicle | networks | and | 5G smart |     |     |     |     |     |     |     |
| ---------- | --- | ----- | --------- | ------------ | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
networkslicing,”inProc.6thInt.Conf.InternetThingsSyst.Manag.
gridslice,”J.Netw.Comput.Appl.,vol.122,pp.50–60,Nov.2018.
Security(IOTSMS),2019,pp.7–12.
[68] F. Z. Yousaf et al. “Network slicing with flexible mobility and [90] F.K.SantosoandN.C.Vun,“SecuringIoTforsmarthomesystem,”
QoS/QoEsupportfor5GNetworks,”inProc.IEEEInt.Conf.Commun. inProc.Int.Symp.Consum.Electron.(ISCE),2015,pp.1–2.
Workshops(ICCWorkshops),2017,pp.1195–1201. [91] E. Theodoridis, G. Mylonas, and I. Chatzigiannakis, “Developing an
| [69] (Jul. 2020). | QoS | Class | Identifier. | [Online]. | Available: |     | https://en. |     |     |     |     |     |     |     |
| ----------------- | --- | ----- | ----------- | --------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
IoTsmartcityframework,”inProc.IISA,2013,pp.1–6.
wikipedia.org/wiki/QoS_Class_Identifier
|            |          |     |          |                |     |             |     | [92] B. Dzogovic, | B.    | Santos,   | J. Noll, V. | T. Do, B. | Feng, | and T. van Do, |
| ---------- | -------- | --- | -------- | -------------- | --- | ----------- | --- | ----------------- | ----- | --------- | ----------- | --------- | ----- | -------------- |
| [70] D. N. | Skoutas, | N.  | Nomikos, | D. Vouyioukas, |     | C. Skianis, | and |                   |       |           |             |           |       |                |
|            |          |     |          |                |     |             |     | “Enabling         | smart | home with | 5G network  | slicing,” | in    | Proc. IEEE 4th |
A. Antonopoulos, “Hybrid resource sharing for QoS preservation in Int.Conf.Comput.Commun.Syst.(ICCCS),2019,pp.543–548.
virtual wireless networks,” Cloud and Fog Computing in 5G Mobile [93] S. Chaabnia and A. Meddeb, “Slicing aware QoS/QoE in software
| Networks: | Emerging | Advances | and | Applications, |     | vol. 70. | Stevenage, |     |     |     |     |     |     |     |
| --------- | -------- | -------- | --- | ------------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
definedsmarthomenetwork,”inProc.IEEE/IFIPNetw.Oper.Manag.
U.K.:IET,2017,p.303.
Symp.,2018,pp.1–5.
| [71] M. Höyhtyä | et  | al., “Critical | communications |     | over | mobile | operators’ |                                                                   |     |     |     |     |     |     |
| --------------- | --- | -------------- | -------------- | --- | ---- | ------ | ---------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                 |     |                |                |     |      |        |            | [94] B.Pokricetal.,“AugmentedrealityenabledIoTservicesforenviron- |     |     |     |     |     |     |
networks:5Gusecasesenabledbylicensedspectrumsharing,network mentalmonitoringutilisingseriousgamingconcept”J.WirelessMobile
slicingandQoScontrol,”IEEEAccess,vol.6,pp.73572–73582,2018. Netw.UbiquitousComput.DependableAppl.,vol.6,no.1,pp.37–55,
| [72] A. Devlic, | A.  | Hamidian, | D. Liang, | M.  | Eriksson, | A. Consoli, | and |     |     |     |     |     |     |     |
| --------------- | --- | --------- | --------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
2015.
| J. Lundstedt, | “NESMO: |     | Network | slicing | management | and | orchestra- |                                                                 |     |     |     |     |     |     |
| ------------- | ------- | --- | ------- | ------- | ---------- | --- | ---------- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|               |         |     |         |         |            |     |            | [95] G.White,C.Cabrera,A.Palade,andS.Clarke,“Augmentedrealityin |     |     |     |     |     |     |
tionframework,”inProc.IEEEInt.Conf.Commun.Workshops(ICC
IoT,”inProc.Int.Conf.Service-OrientedComput.,2018,pp.149–160.
Workshops),2017,pp.1202–1208.
|     |     |     |     |     |     |     |     | [96] M. F. | Alam, S. | Katsikas, | O. Beltramello, | and | S. Hadjiefthymiades, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --------- | --------------- | --- | -------------------- | --- |
[73] C.Pereira,A.Pinto,D.Ferreira,andA.Aguiar,“Experimentalchar- “Augmentedandvirtualrealitybasedmonitoringandsafetysystem:A
acterizationofmobileIoTapplicationlatency,”IEEEInternetThings
prototypeIoTplatform,”J.Netw.Comput.Appl.,vol.89,pp.109–119,
J.,vol.4,no.4,pp.1082–1094,Aug.2017.
Jul.2017.
| [74] S. Redana, | A.    | Kaloxylos,     | A.       | Galis, | P. Rost, | and V.       | Jungnickel, |            |             |            |            |     |          |              |
| --------------- | ----- | -------------- | -------- | ------ | -------- | ------------ | ----------- | ---------- | ----------- | ---------- | ---------- | --- | -------- | ------------ |
|                 |       |                |          |        |          |              |             | [97] D. E. | Zheng andW. | A. Carter, | Leveraging | the | Internet | ofThings for |
| “View           | on 5G | architecture,” | Germany, |        | 5G-PPP,  | White Paper, | 2016.       |            |             |            |            |     |          |              |
aMoreEfficientandEffectiveMilitary.Lanham,MD,USA:Rowman
| [Online].Available:https://5g-ppp.eu/wp-content/uploads/2014/02/5G- |     |     |     |     |     |     |     | &Littlefield,2015. |     |     |     |     |     |     |
| ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
PPP-View-on-5G-Architecture-For-public-consultation.pdf
|     |     |     |     |     |     |     |     | [98] K. Wrona, | “Securing | the | Internet | of Things | a military | perspective,” |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | --- | -------- | --------- | ---------- | ------------- |
[75] T.Taleb,I.Afolabi,K.Samdanis,andF.Z.Yousaf,“Onmulti-domain
|     |     |     |     |     |     |     |     | in Proc. | IEEE | 2nd World | Forum | Internet | Things (WF-IoT), | 2015, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --------- | ----- | -------- | ---------------- | ----- |
networkslicingorchestrationarchitectureandfederatedresourcecon-
pp.502–507.
trol,”IEEENetw.,vol.33,no.5,pp.242–252,Sep./Oct.2019.
[76] Y. Siriwardhana, P. Porambage, M. Liyanage, and M. Ylinattila, [99] L.Yushi,J.Fei,andY.Hui,“Studyonapplicationmodesofmilitary
“A survey on mobile augmented reality with 5G mobile edge Internet of Things (MIOT),” in Proc. IEEE Int. Conf. Comput. Sci.
Autom.Eng.(CSAE),vol.3,2012,pp.630–634.
| computing: | Architectures, |         | applications |       | and     | technical | aspects,” |               |           |                 |          |               |         |               |
| ---------- | -------------- | ------- | ------------ | ----- | ------- | --------- | --------- | ------------- | --------- | --------------- | -------- | ------------- | ------- | ------------- |
|            |                |         |              |       |         |           |           | [100] L. A.   | Grieco et | al., “IoT-aided | robotics | applications: |         | Technological |
| IEEE       | Commun.        | Surveys | Tuts.,       | early | access, | Feb.      | 25, 2021, |               |           |                 |          |               |         |               |
|            |                |         |              |       |         |           |           | implications, | target    | domains         | and      | open issues,” | Comput. | Commun.,      |
doi:10.1109/COMST.2021.3061981.
[77] H. Wang, Y. Wu, G. Min, J. Xu, and P. Tang, “Data-driven dynamic vol.54,pp.32–47,Dec.2014.
resourceschedulingfornetworkslicing:Adeepreinforcementlearning [101] X.Fang,S.Misra,G.Xue,andD.Yang,“Smartgrid—Thenewand
improvedpowergrid:Asurvey,”IEEECommun.SurveysTuts.,vol.14,
approach,”Inf.Sci.,vol.498,pp.106–116,Sep.2019.
no.4,pp.944–980,4thQuart.,2012.
| [78] M. Leconte, | G.         | S. Paschos, | P.  | Mertikopoulos, | and       | U. C.    | Kozat, “A |                                                                  |     |     |     |     |     |     |
| ---------------- | ---------- | ----------- | --- | -------------- | --------- | -------- | --------- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                  |            |             |     |                |           |          |           | [102] M.YunandB.Yuxin,“Researchonthearchitectureandkeytechnology |     |     |     |     |     |     |
| resource         | allocation | framework   |     | for network    | slicing,” | in Proc. | IEEE      |                                                                  |     |     |     |     |     |     |
IEEEConf.Comput.Commun.,2018,pp.2177–2185. ofInternetofThings(IoT)appliedonsmartgrid,”inProc.Int.Conf.
[79] H. Zhang, N. Liu, X. Chu, K. Long, A.-H. Aghvami, and Adv.EnergyEng.,2010,pp.69–72.
V. C. M. Leung, “Network slicing based 5G and future mobile [103] A.I.Sarwat,A.Sundararajan,andI.Parvez,“Trendsandfuturedirec-
|           |           |          |             |     |     |              |      | tions | of research | for smart | grid IoT | sensor | networks,” | in Proc. Int. |
| --------- | --------- | -------- | ----------- | --- | --- | ------------ | ---- | ----- | ----------- | --------- | -------- | ------ | ---------- | ------------- |
| networks: | Mobility, | resource | management, |     | and | challenges,” | IEEE |       |             |           |          |        |            |               |
Symp.Sens.Netw.Syst.Security,2017,pp.45–61.
Commun.Mag.,vol.55,no.8,pp.138–145,Aug.2017.
[80] Y. Sun, M. Peng, S. Mao, and S. Yan, “Hierarchical radio resource [104] T.Lagkas,V.Argyriou,S.Bibi,andP.Sarigiannidis,“UAVIoTframe-
allocation for network slicing in fog radio access networks,” IEEE work views and challenges: Towards protecting drones as “Things”,”
Trans.Veh.Technol.,vol.68,no.4,pp.3866–3881,Apr.2019. Sensors,vol.18,no.11,p.4015,2018.
[81] C. Campolo, A. Molinaro, A. Iera, and F. Menichella, “5G network [105] M. Mozaffari, W. Saad, M. Bennis, Y.-H. Nam, and M. Debbah,
|         |                           |     |     |            |      |          |          | “A tutorial | on  | UAVs for | wireless networks: | Applications, |     | challenges, |
| ------- | ------------------------- | --- | --- | ---------- | ---- | -------- | -------- | ----------- | --- | -------- | ------------------ | ------------- | --- | ----------- |
| slicing | for vehicle-to-everything |     |     | services,” | IEEE | Wireless | Commun., |             |     |          |                    |               |     |             |
vol.24,no.6,pp.38–45,Dec.2017. and open problems,” IEEE Commun. Surveys Tuts., vol. 21, no. 3,
[82] C.Campolo,A.Molinaro,A.Iera,R.R.Fontes,andC.E.Rothenberg, pp.2334–2360,3rdQurt.,2019.
“Towards 5G network slicing for the V2X ecosystem,” in Proc. [106] C. Luo, J. Nightingale, E. Asemota, and C. Grecos, “A UAV-cloud
4th IEEE Conf. Netw. Softwarization Workshops (NetSoft), 2018, system for disaster sensing applications,” in Proc. IEEE 81st Veh.
Technol.Conf.(VTCSpring),2015,pp.1–5.
pp.400–405.
[83] H.Khan,P.Luoto,M.Bennis,andM.Latva-aho,“Ontheapplication [107] A. E. Garcia et al., “Performance evaluation of network slicing for
of network slicing for 5G-V2X,” in Proc. 24th Eur. Wireless Conf., aerial vehicle communications,” in Proc. IEEE Int. Conf. Commun.
| 2018,pp.1–6. |     |     |     |     |     |     |     | Workshops(ICCWorkshops),2019,pp.1–6. |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
[84] H.Wu,I.A.Tsokalo,D.Kuss,H.Salah,L.Pingel,andF.H.Fitzek, [108] A.Kamilaris,F.Gao,F.X.Prenafeta-Boldu,andM.I.Ali,“Agri-IoT:
“Demonstration of network slicing for flexible conditional monitor- A semantic framework for Internet of Things-enabled smart farming
ing in industrial IoT networks,” in Proc. 16th IEEE Annu. Consum. applications,” in Proc. IEEE 3rd World Forum Internet Things (WF-
| Commun.Netw.Conf.(CCNC),2019,pp.1–2. |     |     |     |     |     |     |     | IoT),2016,pp.442–447. |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |

992 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
[109] J.Ruanetal.,“AlifecycleframeworkofgreenIoT-basedagriculture [131] J.J.A.Esteves,A.Boubendir,F.Guillemin,andP.Sens,“Optimized
and its finance, operation, and management issues,” IEEE Commun. networkslicingproof-of-conceptwithinteractivegamingusecase,”in
Mag.,vol.57,no.3,pp.90–96,Mar.2019. Proc. 23rd Conf. Innovat. Clouds Internet Netw. Workshops (ICIN),
[110] S. R. Shinde, A. Karode, and D. S. Suralkar, “Review on-IoT based 2020,pp.150–152.
environment monitoring system,” Int. J. Electron. Commun. Eng. [132] Augmented Reality for Enterprise Alliance. (Oct. 2015). SK Telecom
Technol.,vol.8,no.2,pp.103–108,2017. and Ericsson Demonstrate 5G Network Slices for Augmented
[111] O. Zakaria, J. Britt, and H. Forood, “Internet of Things (IoT) auto- Reality. [Online]. Available: https://thearea.org/ar-news/sk-telecom-
and-ericsson-demonstrate-5g-network-slices-for-augmented-reality/
| motive | device, | system, | and method,” |     | U.S. Patent | 9717012, | Jul. 25, |     |     |     |     |     |     |     |
| ------ | ------- | ------- | ------------ | --- | ----------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
2017. [133] P. Grønsund et al., “5G service and slice implementation for a mil-
[112] T. Soenen, R. Banerjee, W. Tavernier, D. Colle, and M. Pickavet, itary use case,” in Proc. IEEE Int. Conf. Commun. Workshops (ICC
“Demystifying network slicing: From theory to practice,” in Workshops),2020,pp.1–6.
Proc. IFIP/IEEE Symp. Integr. Netw. Service Manag. (IM), 2017, [134] J.Liu,X.Li,X.Chen,Y.Zhen,andL.Zeng,“ApplicationsofInternet
|     |     |     |     |     |     |     |     | of Things | on  | smart grid | in China,” in | Proc. 13th | Int. Conf. | Adv. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | ------------- | ---------- | ---------- | ---- |
pp.1115–1120.
[113] S.Zhang,W.Quan,J.Li,W.Shi,P.Yang,andX.Shen,“Air-ground Commun.Technol.(ICACT),2011,pp.13–17.
integratedvehicularnetworkslicingwithcontentpushingandcaching,” [135] C. Bekara, “Security issues and challenges for the IoT-based smart
IEEEJ.Sel.AreasCommun.,vol.36,no.9,pp.2114–2127,Sep.2018. grid,”inProc.FNC/MobiSPC,2014,pp.532–537.
|                |      |            |            |     |                  |     |              | [136] F.Kurtz,C.Bektas,N.Dorsch,andC.Wietfeld,“Networkslicingfor |                |     |                              |     |     |           |
| -------------- | ---- | ---------- | ---------- | --- | ---------------- | --- | ------------ | ---------------------------------------------------------------- | -------------- | --- | ---------------------------- | --- | --- | --------- |
| [114] Industry | 4.0: | The Fourth | Industrial |     | Revolution—Guide |     | to Industrie |                                                                  |                |     |                              |     |     |           |
|                |      |            |            |     |                  |     |              | critical                                                         | communications | in  | shared 5G infrastructures—An |     |     | empirical |
4.0.Accessed:Jul.14,2020.[Online].Available:https://www:i-scoop:
eu/industry-4–0/#:∼:text=Industry%204:0%20is%20the%20digital; evaluation,”inProc.4thIEEEConf.Netw.SoftwarizationWorkshops
of%20the%20industrial%20value%20chain (NetSoft),2018,pp.393–399.
[115] T. Qiu, J. Chi, X. Zhou, Z. Ning, M. Atiquzzaman, and D. O. Wu, [137] N. Dorsch, F. Kurtz, and C. Wietfeld, “On the economic benefits
|       |           |     |            |          |     |         |               | of software-defined |     | networking | and network | slicing   | for    | smart grid |
| ----- | --------- | --- | ---------- | -------- | --- | ------- | ------------- | ------------------- | --- | ---------- | ----------- | --------- | ------ | ---------- |
| “Edge | computing | in  | industrial | Internet | of  | Things: | Architecture, |                     |     |            |             |           |        |            |
|       |           |     |            |          |     |         |               | communications,”    |     | NETNOMICS  | Econ. Res.  | Electron. | Netw., | vol. 19,   |
advancesandchallenges,”IEEECommun.SurveysTuts.,vol.22,no.4,
nos.1–2,pp.1–30,2018.
pp.2462–2488,4thQuart.,2020.
[116] A.Gurtov,M.Liyanage,andD.Korzun,“Securecommunicationand [138] S. Petkovic, D. Petkovic, and A. Petkovic, “IoT devices vs. drones
dataprocessingchallengesintheindustrialInternet,”Balt.J.Modern for data collection in agriculture,” in DAAAM International Scientific
Book,vol.16.Vienna,Austria:DAAAMInt.,2017,pp.63–80.
Comput.,vol.4,no.4,pp.1058–1073,2016.
|          |        |            |       |            |     |            |          | [139] A.Rajakaruna,A.Manzoor,P.Porambage,M.Liyanage,M.Ylianttila, |     |     |     |     |     |     |
| -------- | ------ | ---------- | ----- | ---------- | --- | ---------- | -------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| [117] H. | Wu, G. | T. Nguyen, | A. K. | Chorppath, | and | F. Fitzek, | “Network |                                                                   |     |     |     |     |     |     |
andA.Gurtov,“Enablingend-to-endsecureconnectivityforlow-power
| slicing | for | conditional | monitoring |     | in the industrial |     | Internet | of  |     |     |     |     |     |     |
| ------- | --- | ----------- | ---------- | --- | ----------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Things,” Proc. IEEE Softw., Jan. 2018, pp.1–2. [Online]. Available: IoTdeviceswithUAVs,”inProc.IEEEWirelessCommun.Netw.Conf.
https://sdn.ieee.org/newsletter/january-2018/network-slicing-for- Workshop(WCNCW),2019,pp.1–6.
|     |     |     |     |     |     |     |     | [140] N. H. | Motlagh, | M. Bagaa, | and T. Taleb, | “UAV-based | IoT | platform: |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --------- | ------------- | ---------- | --- | --------- |
conditional-monitoring-in-the-industrial-internet-of-things
Acrowdsurveillanceusecase,”IEEECommun.Mag.,vol.55,no.2,
| [118] M. | Baddeley, | R.  | Nejabati, | G.  | Oikonomou, |     | S. Gormus, |     |     |     |     |     |     |     |
| -------- | --------- | --- | --------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
pp.128–134,Feb.2017.
| M.      | Sooriyabandara, |                 | and D. | Simeonidou, | “Isolating |     | SDN control |                |      |                   |       |          |        |      |
| ------- | --------------- | --------------- | ------ | ----------- | ---------- | --- | ----------- | -------------- | ---- | ----------------- | ----- | -------- | ------ | ---- |
|         |                 |                 |        |             |            |     |             | [141] S. Wray. | (May | 2018). Autonomous | Drone | Services | Tested | Over |
| traffic | with            | layer-2 slicing | in     | 6TiSCH      | industrial | IoT | networks,”  | in             |      |                   |       |          |        |      |
Proc. IEEE Conf. Netw. Funct. Virtualization Softw. Defined Netw. Intercontinental 5G. [Online]. Available: https://5g.co.uk/news/drone-
services-over-intercontinental-5g/4374/
(NFV-SDN),2017,pp.247–251.
|          |           |            |            |            |            |            |           | [142] M. Contento. |          | (Mar. 2020). | Massive IoT          | and 5G:                | What’s | Next for |
| -------- | --------- | ---------- | ---------- | ---------- | ---------- | ---------- | --------- | ------------------ | -------- | ------------ | -------------------- | ---------------------- | ------ | -------- |
| [119] Y. | A. Qadri, | A. Nauman, | Y.         | B. Zikria, | A. V.      | Vasilakos, | and S. W. |                    |          |              |                      |                        |        |          |
|          |           |            |            |            |            |            |           | Large-Scale        | Cellular | IoT.         | [Online]. Available: | https://www.telit.com/ |        |          |
| Kim,     | “The      | future of  | healthcare | Internet   | of Things: |            | A survey  | of                 |          |              |                      |                        |        |          |
blog/massive-iot-5g-whats-next/
emergingtechnologies,”IEEECommun.SurveysTuts.,vol.22,no.2,
pp.1121–1167,2ndQuart.,2020. [143] P.ChivengeandS.Sharma,“Precisionagricultureinfoodproduction:
|          |             |         |               |     |              |     |               | Nutrient | management,” | in  | Proc. Int. Workshop | ICTS | Precision | Agr., |
| -------- | ----------- | ------- | ------------- | --- | ------------ | --- | ------------- | -------- | ------------ | --- | ------------------- | ---- | --------- | ----- |
| [120] L. | Catarinucci | et al., | “An IoT-aware |     | architecture | for | smart health- |          |              |     |                     |      |           |       |
2019,p.12.
| care | systems,” | IEEE | Internet | Things | J., vol. 2, | no. 6, | pp.515–526, |                                                               |     |     |     |     |     |     |
| ---- | --------- | ---- | -------- | ------ | ----------- | ------ | ----------- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|      |           |      |          |        |             |        |             | [144] J.P.S.Sundaram,W.Du,andZ.Zhao,“AsurveyonLoRAnetworking: |     |     |     |     |     |     |
Dec.2015.
Researchproblems,currentsolutions,andopenissues,”IEEECommun.
[121] P.S.Ranaweera,M.Liyanage,andA.D.Jurcut,“NovelMECbased SurveysTuts.,vol.22,no.1,pp.371–388,1stQuart.,2020.
approachesforsmarthospitalstocombatCOVID-19pandemic,”IEEE [145] N. Mangalvedhe, R. Ratasuk, and A. Ghosh, “NB-IoT deployment
Consum.Electron.Mag.,vol.10,no.2,pp.80–91,Mar.2021.
|     |     |     |     |     |     |     |     | study | for low | power wide | area cellular | IoT,” in | Proc. IEEE | 27th |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ---------- | ------------- | -------- | ---------- | ---- |
[122] Y.Siriwardhana,G.Gür,M.Ylianttila,andM.Liyanage,“Theroleof
Annu.Int.Symp.Pers.IndoorMobileRadioCommun.(PIMRC),2016,
| 5G  | for digital | healthcare | against | COVID-19 | pandemic: |     | Opportunities |     |     |     |     |     |     |     |
| --- | ----------- | ---------- | ------- | -------- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
pp.1–6.
andchallenges,”ICTExp.,tobepublished. [146] P. Popovski, K. F. Trillingsgaard, O. Simeone, and G. Durisi,
[123] M.S.HossainandG.Muhammad,“Cloud-assistedIndustrialInternet “5G wireless network slicing for eMBB, URLLC, and mMTC:
ofThings(IIoT)—Enabledframeworkforhealthmonitoring,”Comput.
|     |     |     |     |     |     |     |     | A communication-theoretic |     |     | view,” | IEEE | Access, | vol. 6, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | ------ | ---- | ------- | ------- |
Netw.,vol.101,pp.192–202,Jun.2016.
pp.55765–55779,2018.
[124] R.Pries,H.-J.Morper,N.Galambosi,andM.Jarschel,“Networkasa
|     |     |     |     |     |     |     |     | [147] The | Business | Case for | MEC in Retail: | A TCO | Analysis | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | -------- | -------------- | ----- | -------- | --- |
service—Ademoon5Gnetworkslicing,”inProc.28thInt.Teletraffic Its Implications in the 5G Era. Accessed: Jul. 21, 2020. [Online].
Congr.(ITC),vol.1,2016,pp.209–211. Available:https://builders.intel.com/docs/networkbuilders/the-business-
[125] Y. Chang, X. Dong, and W. Sun, “Influence of characteristics of the case-for-mec-in-retail-a-tco-analysis-and-its-implications-in-the-5g-
InternetofThingsonconsumerpurchaseintention,”SocialBehav.Pers.
era.pdf
Int.J.,vol.42,no.2,pp.321–330,2014.
|     |     |     |     |     |     |     |     | [148] S.G.Dacko,“Enablingsmartretailsettingsviamobileaugmentedreal- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
[126] M.Boussardetal.,“Futurespaces:Reinventingthehomenetworkfor ity shopping apps,” in Technol. Forecasting Social Change, vol.124,
bettersecurityandautomationintheIoTera,”Sensors,vol.18,no.9, pp.243–256,Nov.2017.
p.2986,2018. [149] H. Sun, Z. Zhang, R. Q. Hu, and Y. Qian, “Challenges and enabling
[127] Srikanth. (Jan. 2020). How IoT is Empowering Virtual Reality. technologies in 5G wearable communications,” 2017. [Online].
| [Online]. |     | Available: |     | https://www.techiexpert.com/how-iot-is- |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | ---------- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Available:arXiv:1708.05410v1.
empowering-virtual-reality/ [150] P.Ranaweera,A.D.Jurcut,andM.Liyanage,“Surveyonmulti-access
[128] “Empowering consumer-focused immersive VR and AR expe- edge computing security and privacy,” IEEE Commun. Surveys Tuts.,
riences with mobile broadband,” Huawei, Shenzhen, China, earlyaccess,Feb.26,2021,doi:10.1109/COMST.2021.3062546.
Rep., 2016. [Online]. Available: https://www-file.huawei.com/-/media [151] (2018). The Top 10 IoT Segments in 2018–Based on 1,600 Real
/corporate/pdf/mbb/huawei_whitepaper_vr_ar_final.pdf?la=sw-ke
|     |     |     |     |     |     |     |     | IoT Projects. | [Online]. | Available: | https://iot-analytics.com/top-10-iot- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ---------- | ------------------------------------- | --- | --- | --- |
[129] “VR and AR pushing connectivity limits,” Qualcomm, segments-2018-real-iot-projects/
San Diego, CA, USA, Rep., 2018. [Online]. Available: [152] How Network Latency Affects the Future of Autonomous Vehicles.
https://www.qualcomm.com/media/documents/files/vr-and-ar-pushing- Accessed: Jul. 13, 2020. [Online]. Available: https://www.orcad.com/
| connectivity-limits.pdf |     |     |     |     |     |     |     | jp/node/6591 |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
[130] G. F. Networks. (Apr. 2019). Cloud AR/VR Whitepaper. [Online]. [153] AutonomousCarsWillGenerateMoreThan300TBofDataPerYear.
Available: https://www.gsma.com/futurenetworks/wiki/cloud-ar-vr- Accessed:Jul.18,2020.[Online].Available:https://www.tuxera.com/
| whitepaper/ |     |     |     |     |     |     |     | blog/autonomous-cars-300-tb-of-data-per-year/ |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |

WIJETHILAKAANDLIYANAGE:SURVEYONNETWORKSLICINGFORIoTREALIZATIONIN5GNETWORKS 993
[154] (May2017).PuttingSensorstoWorkintheFactoryEnvironment:Data [174] M. L. Héno, A. Boubendir, and N. Simoni, “Telco network slicing
to Information to Wisdom. [Online]. Available: https://itpeernetwork. modelsenablingrecursivemulti-tenancy,”inProc.10thInt.Conf.Netw.
intel.com/putting-sensors-to-work-in-the-factory-environment/#gs. Future(NoF),2019,pp.40–47.
9lkvhx [175] P. Q. Carlos Pignataro. (Apr. 2017). Service Function Chaining.
[155] (2018). New Ethernet Applications—Industrial Networking [Online]. Available: https://www.cisco.com/c/dam/m/en_us/network-
Requirements. [Online]. Available: http://www.ieee802.org/3/ad_ intelligence/service-provider/digital-transformation/knowledge-
hoc/ngrates/public/18_03/woods_nea_01_0318.pdf network-webinars/pdfs/0426-techad-ckn.pdf
|          |                |             |           |              |            |                      | [176] | S.          | Raynovich. | (Jan. 2016). | What       | Is Network |                             | Service | Chaining? |
| -------- | -------------- | ----------- | --------- | ------------ | ---------- | -------------------- | ----- | ----------- | ---------- | ------------ | ---------- | ---------- | --------------------------- | ------- | --------- |
| [156] 5G | in Healthcare: | Boosting    |           | Remote Brain | Surgeries, | Connected            |       |             |            |              |            |            |                             |         |           |
|          |                |             |           |              |            |                      |       | Definition. |            | [Online].    | Available: |            | https://www.sdxcentral.com/ |         |           |
| Health,  | or             | Medical VR. | Accessed: | Jul. 25,     | 2020.      | [Online]. Available: |       |             |            |              |            |            |                             |         |           |
https://medicalfuturist.com/5g-in-healthcare-boosting-telehealth-vr- networking/virtualization/definitions/what-is-network-service-chaining/
connected-health/ [177] S. Zhang, “An overview of network slicing for 5G,” IEEE Wireless
[157] Q. Zhang, J. Liu, and G. Zhao, “Towards 5G enabled tactile robotic Commun.,vol.26,no.3,pp.111–117,Jun.2019.
telesurgery,”2018.[Online].Available:arXiv:1803.03586. [178] X.Li,J.Rao,H.Zhang,andA.Callard,“Networkslicingwithelas-
|            |        |             |           |     |           |          |        | tic | SFC,” in | Proc. IEEE | 86th | Veh. Technol. | Conf. | (VTC-Fall), | 2017, |
| ---------- | ------ | ----------- | --------- | --- | --------- | -------- | ------ | --- | -------- | ---------- | ---- | ------------- | ----- | ----------- | ----- |
| [158] What | Is the | Recommended | Bandwidth | for | Different | Types of | Health |     |          |            |      |               |       |             |       |
pp.1–5.
| Care | Providers? | Accessed: |     | Jul. 26, | 2020. [Online]. | Available: |     |     |     |     |     |     |     |     |     |
| ---- | ---------- | --------- | --- | -------- | --------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
https://www.healthit.gov/faq/what-recommended-bandwidth-different- [179] R. F. Olimid and G. Nencioni, “5G network slicing: A security
types-health-care-providers overview,”IEEEAccess,vol.8,pp.99999–100009,2020.
[159] Why a Smart Hospital Needs to Look After the Security of [180] Y.Khettab,M.Bagaa,D.L.C.Dutra,T.Taleb,andN.Toumi,“Virtual
securityasaservicefor5Gverticals,”inProc.IEEEWirelessCommun.
| Its | Network. | Accessed: | Jul. | 26, 2020. | [Online]. | Available: |     |     |     |     |     |     |     |     |     |
| --- | -------- | --------- | ---- | --------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Netw.Conf.(WCNC),2018,pp.1–6.
https://internationalsecurityjournal.com/why-a-smart-hospital-needs-to-
|     |     |     |     |     |     |     | [181] | L.  | Suárez, | D. Espes, | P.  | Le Parc, | F. Cuppens, | P.  | Bertin, |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------- | --------- | --- | -------- | ----------- | --- | ------- |
look-after-the-security-of-its-network/
|           |      |          |       |           |       |      |       | and | C.-T.Phan, | “Enhancing |     | network slice | security | via | Artificial |
| --------- | ---- | -------- | ----- | --------- | ----- | ---- | ----- | --- | ---------- | ---------- | --- | ------------- | -------- | --- | ---------- |
| [160] How | Much | Internet | Speed | Does Your | Smart | Home | Need? |     |            |            |     |               |          |     |            |
Accessed: Jun. 8, 2020. [Online]. Available: Available: https://www: Intelligence: Challenges and solutions,” in Proc. Conf. C&ESAR,
smarthomeblog:net/bandwidthsmart-home/#:∼:text=Speed%3A% Rennes, France, Nov. 2018. [Online]. Available: https://hal.archives-
ouvertes.fr/hal-01959251
20As%20a%20general%20recommendation;you%20can%20adjust%
|     |     |     |     |     |     |     | [182] | (Jul. | 2019). | The Evolution | of  | Security | in 5G. [Online]. |     | Available: |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ------ | ------------- | --- | -------- | ---------------- | --- | ---------- |
20from%20there
https://www.5gamericas.org/wp-content/uploads/2019/08/5G-Security-
| [161] P. | Fedchenkov, | A. Zaslavsky, |     | A. Medvedev, | T.  | Anagnostopoulos, |     |     |     |     |     |     |     |     |     |
| -------- | ----------- | ------------- | --- | ------------ | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
White-Paper_8.15.pdf
I.Sosunova,andO.Sadov,“SupportingdatacommunicationsinIoT-
enabledwastemanagement,”inInternetofThings,SmartSpaces,and [183] Z.Kotulskietal.,“Towardsconstructiveapproachtoend-to-endslice
isolationin5Gnetworks,”EURASIPJ.Inf.Security,vol.2018,no.1,
NextGenerationNetworksandSystems.Cham,Switzerland:Springer,
p.2,2018.
2017,pp.163–174.
|          |            |                     |           |             |          |              | [184]     | J.Liu,L.Zhang,R.Sun,X.Du,andM.Guizani,“Mutualheteroge- |              |         |     |            |            |      |         |
| -------- | ---------- | ------------------- | --------- | ----------- | -------- | ------------ | --------- | ------------------------------------------------------ | ------------ | ------- | --- | ---------- | ---------- | ---- | ------- |
| [162] E. | Mohyeldin. | Minimum             | Technical | Performance |          | Requirements | for       |                                                        |              |         |     |            |            |      |         |
|          |            |                     |           |             |          |              |           | neous                                                  | signcryption | schemes | for | 5G network | slicings,” | IEEE | Access, |
| IMT-2020 |            | Radio Interface(s). |           | Accessed:   | Jun. 20, | 2020.        | [Online]. |                                                        |              |         |     |            |            |      |         |
Available: https://www:itu:int/en/ITU-R/study-groups/rsg5/rwp5d/imt- vol.6,pp.7854–7863,2018.
2020/Documents/S01–1Requirements%20for%20IMT-2020Rev:pdf [185] L.Suárez,D.Espes,F.Cuppens,C.-T.Phan,P.Bertin,andP.LeParc,
|                 |     |              |     |                 |      |               |     | “Managing |     | secure inter-slice |     | communication | in  | 5G network | slice |
| --------------- | --- | ------------ | --- | --------------- | ---- | ------------- | --- | --------- | --- | ------------------ | --- | ------------- | --- | ---------- | ----- |
| [163] Bandwidth |     | Requirements | for | Virtual Reality | (VR) | and Augmented |     |           |     |                    |     |               |     |            |       |
chains,”inProc.IFIPAnnu.Conf.DataAppl.SecurityPrivacy,2020,
Reality(AR).Accessed:Aug.8,2020.[Online].Available:https://www.
pp.24–41.
mushroomnetworks.com/infographics/bandwidth-requirements-for-
|     |     |     |     |     |     |     | [186] | F.Meneses,M.Fernandes,D.Corujo,andR.L.Aguiar,“SliMANO: |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
virtual-reality-vr-and-augmented-reality-ar-infographic/
|     |     |     |     |     |     |     |     | An  | expandable | framework | for | the management | and | orchestration | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | -------------- | --- | ------------- | --- |
[164] H. Mendis, P. E. Heegaard, and K. Kralevska, “5G network slicing end-to-endnetworkslices,”inProc.IEEE8thInt.Conf.CloudNetw.
asanenablerforsmartdistributiongridoperations,”inProc.CIRED,
(CloudNet),2019,pp.1–6.
2019,pp.1–5.
|     |     |     |     |     |     |     | [187] | M.  | T. Abbas, | T. A. | Khan, | A. Mahmood, | J.  | J. D. Rivera, | and |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --------- | ----- | ----- | ----------- | --- | ------------- | --- |
[165] 5GNetworkSlicingEnablingtheSmartGrid.Accessed:May25,2020.
W.-C.Song,“IntroducingnetworkslicemanagementinsideM-CORD-
| [Online]. |     | Available: |     | http://www-file.huawei.com/-/media/ |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | ---------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
based-5Gframework,”inProc.IEEE/IFIPNetw.Oper.Manag.Symp.,
| CORPORATE/PDF/News/5g-network-slicing-enabling-the-smart- |     |     |     |     |     |     |     | 2018,pp.1–2. |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
grid.pdf [188] F. Z. Yousaf, V. Sciancalepore, M. Liebsch, and X. Costa-Perez,
[166] Growing Use of UAVs Strains Bandwidth. Accessed: May 28, 2020. “MANOaaS:Amulti-tenantNFVMANOfor5Gnetworkslices,”IEEE
| [Online]. | Available: | https://spacenews.com/growing-use-uavs-strains- |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Commun.Mag.,vol.57,no.5,pp.103–109,May2019.
bandwidth/
|     |     |     |     |     |     |     | [189] | R. Wen, | G.  | Feng, J. Zhou, | and | S. Qin, | “Mobility | management | for |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | --- | -------------- | --- | ------- | --------- | ---------- | --- |
[167] Enterprise Application of Autonomous UAVs: QoS & QoE From network slicing based 5G networks,” in Proc. IEEE 18th Int. Conf.
Modern Telecom Networks. Accessed: Jun. 1, 2020. [Online]. Commun.Technol.(ICCT),2018,pp.291–296.
Available: https://www.itu.int/en/ITU-T/Workshops-and-Seminars/qos/ [190] M. Richart, J. Baliosian, J. Serrati, J.-L. Gorricho, R. Agüero, and
201809/Documents/R_Roy_Presentation.pdf
N.Agoulmine,“ResourceallocationfornetworkslicinginWiFiaccess
| [168] What | Value | Can High-Speed |     | Broadband | Create | for | Farming |     |     |     |     |     |     |     |     |
| ---------- | ----- | -------------- | --- | --------- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
points,”inProc.13thInt.Conf.Netw.ServiceManag.(CNSM),2017,
Communities.Accessed:Jun.2,2020.[Online].Available:https://www.
pp.1–4.
smartfarmnet.com/farming-with-high-speed-broadband.html [191] SliceNet.Accessed:Aug.15,2020.[Online].Available:https://slicenet.
| [169] I.Afolabi,J.Prados,M.Bagaa,T.Taleb,andP.Ameigeiras,“Dynamic |     |     |     |     |     |     |     | eu/ |     |     |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
resourceprovisioningofascalableE2Enetworkslicingorchestration [192] AutoAir. Accessed: Aug. 15, 2020. [Online]. Available: https://www.
| system,”IEEETrans.MobileComput.,vol.19,no.11,pp.2594–2608, |     |     |     |     |     |     |     | airspan.com/autoair/ |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
Nov.2019.
|                                                               |     |     |     |     |     |     | [193] | 5G!Pagoda.Accessed:Aug.17,2020.[Online].Available:https://5g- |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| [170] S.Kuklin´skiandL.Tomaszewski,“DASMO:Ascalableapproachto |     |     |     |     |     |     |       | pagoda.aalto.fi/                                              |     |     |     |     |     |     |     |
network slices management and orchestration,” in Proc. IEEE/IFIP [194] SEMANTIC. Accessed: Aug. 16, 2020. [Online]. Available:
Netw.Oper.Manag.Symp.,2018,pp.1–6. https://cordis.europa.eu/project/id/861165
[171] L.Geng,S.Bryant,K.Makhijani,A.Galis,X.deFoy,andS.Kuklinsk. [195] MATILDA.Accessed:Aug.20,2020.[Online].Available:https://www.
(2017).NetworkSlicingArchitectur.[Online].Available:https://tools. matilda-5g.eu/index.php
ietf.org/id/draft-geng-netslices-architecture-01.html#rfc.section.3.3.1 [196] 5G!Drones. Accessed: Aug. 19, 2020. [Online]. Available:
https://5gdrones.eu/
| [172] C. | E. Curtis | Collicutt. | (2018). | 5G Network | Slicing | and OpenStac. |     |     |     |     |     |     |     |     |     |
| -------- | --------- | ---------- | ------- | ---------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[Online]. Available: https://object-storage-ca-ymq-1.vexxhost.net/ [197] MonB5G.Accessed:Aug.19,2020.[Online].Available:https://www.
| swift/v1/6e4619c416ff4bd19e1c087f27a43eea/www-assets-prod/ |     |     |     |     |     |     |     | monb5g.eu/ |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
presentation-media/5G-Network-Slicing-and-OpenStack-Presentation- [198] 5GMOBIX.Accessed:Aug.21,2020.[Online].Available:https://www.
| Copy-C03.pdf |     |     |     |     |     |     |     | 5g-mobix.com/ |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
[173] A. Galis. (Nov. 2018). Network Slicing—A Holistic Architectural [199] PRIMO-5.Accessed:Aug.21,2020.[Online].Available:https://primo-
| Approach,OrchestrationandManagementwithApplicabilityinMobile |     |     |     |     |     |     |     | 5g.eu/ |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
andFixedNetworksandCloud.[Online].Available:http://cnsm-conf. [200] 5G-MONARCH. Accessed: Aug. 22, 2020. [Online]. Available:
| org/2018/files/CNSM18_SlicingTutorial_AlexGalis_5–10-2018.pdf |     |     |     |     |     |     |     | https://5g-monarch.eu/ |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |

994 IEEECOMMUNICATIONSSURVEYS&TUTORIALS,VOL.23,NO.2,SECONDQUARTER2021
[201] 5GCity. Accessed: Aug. 23, 2020. [Online]. Available: https://www. [226] B.Ciszewski.(Oct.2018).MachineLearninginTelecommunications:
5gcity.eu/ The Sector Bound to Lead the AI Revolution. [Online]. Available:
[202] INSPIRE-5Gplus. Accessed: Aug. 23, 2020. [Online]. Available: https://www.netguru.com/blog/ai-in-telecommunications
https://www.inspire-5gplus.eu/ [227] E. Schmit. (Dec. 2019). The Powerful Combination of Machine
[203] Hexa-X.Accessed:Jan.25,2021.[Online].Available:https://hexa-x.eu/ Learningand5GNetworks.[Online].Available:https://shape.att.com/
[204] J. Martin and J. Bohuslava, “Augmented reality as an instrument for blog/combination-of-machine-learning-and-5g
teaching industrial automation,” in Proc. Cybern. Informat. (K&I). [228] L.-V.Le,B.-S.P.Lin,L.-P.Tung,andD.Sinh,“SDN/NFV,machine
2018,pp.1–5. learning, and big data driven network slicing for 5G,” in Proc. IEEE
[205] I. Maly`, D. Sedlácˇek, and P. Leitao, “Augmented reality experiments 5GWorldForum(5GWF),2018,pp.20–25.
withindustrialrobotinindustry4.0environment,”inProc.IEEE14th [229] L.Xiao,X.Wan,X.Lu,Y.Zhang,andD.Wu,“IoTsecuritytechniques
Int.Conf.Ind.Informat.(INDIN),2016,pp.176–181. based on machine learning: How do IoT devices use AI to enhance
[206] J. Backman, S. Yrjölä, K. Valtanen, and O. Mämmelä, “Blockchain security?” IEEE Signal Process. Mag., vol. 35, no. 5, pp.41–49,
networkslice broker in5G: Slice leasing infactory of thefuture use Sep.2018.
case,”inProc.InternetThingsBus.ModelsUsersNetw.,2017,pp.1–8. [230] F.Hussain,S.A.Hassan,R.Hussain,andE.Hossain,“Machinelearn-
[207] Why the IoMT Will Start to Transform Healthcare. ingforresourcemanagementincellularandIoTnetworks:Potentials,
Accessed: Aug. 27, 2020. [Online]. Available: https://www.forbes. currentsolutions,andopenchallenges,”IEEECommun.SurveysTuts.,
com/sites/bernardmarr/2018/01/25/why-the-internet-of-medical-things- vol.22,no.2,pp.1251–1275,2ndQuart.,2020.
iomt-will-start-to-transform-healthcare-in-2018 [231] A. Thantharate, R. Paropkari, V. Walunj, and C. Beard, “DeepSlice:
[208] Using Network Slicing to Enhance Security in e-Health Use Cases. A deep learning approach towards an efficient and reliable network
Accessed: Aug. 28, 2020. [Online]. Available: https://protego-project. slicingin5Gnetworks,”inProc.IEEE10thAnnu.UbiquitousComput.
eu/2019/05/using-network-slicing-to-enhance-security-in-e-health-use- Electron.MobileCommun.Conf.(UEMCON),2019,pp.762–767.
cases/ [232] J. Mei, X. Wang, and K. Zheng, “Intelligent network slicing for
[209] How 5G Mobile Networks are Opening the Door to Remote V2X services toward 5G,” IEEE Netw., vol. 33, no. 6, pp.196–204,
Surgery. Accessed: Aug. 28, 2020. [Online]. Available: https://www. Nov./Dec.2019.
medicaldevice-network.com/features/5g-remote-surgery/ [233] L. Zhao and L. Li, “Reinforcement learning for resource mapping in
[210] How 5G and Edge Computing Can Enhance Virtual Reality. 5G network slicing,” in Proc. 5th Int. Conf. Comput. Commun. Syst.
Accessed: Aug. 30, 2020. [Online]. Available: https://www.ericsson. (ICCCS),2020,pp.869–873.
com/en/blog/2020/4/how-5g-and-edge-computing-can-enhance-virtual- [234] S.DeBast,R.Torrea-Duran,A.Chiumento,S.Pollin,andH.Gacanin,
reality “Deep reinforcement learning for dynamic network slicing in IEEE
[211] 5GNetworkSlicingEnablingtheSmartGrid.Accessed:Aug.30,2020. 802.11networks,”inProc.IEEEConf.Comput.Commun.Workshops
[Online]. Available: http://www-file.huawei.com/-/media/ (INFOCOMWKSHPS),2019,pp.264–269.
CORPORATE/PDF/News/5g-network-slicing-enabling-the-smart- [235] P. Ahokangas et al., “Business models for local 5G micro opera-
grid.pdf tors,”IEEETrans.Cogn.Commun.Netw.,vol.5,no.3,pp.730–740,
[212] S.Sekander,H.Tabassum,andE.Hossain,“Multi-tierdronearchitec- Sep.2019.
turefor5G/B5Gcellularnetworks:Challenges,trends,andprospects,” [236] (Jul. 2018). 5G and Network Slicing: A New Era in Networking.
IEEECommun.Mag.,vol.56,no.3,pp.96–103,Mar.2018. [Online]. Available: https://ieee-wf-5g.org/wp-content/uploads/sites/
[213] SFC/Network slicing. Accessed: Sep. 1, 2020. [Online]. Available: 102/2018/11/POLYCHRONOPOLISSlides.pdf
https://newslab.iith.ac.in/research/sfc.html
[214] C.Marquez,M.Gramaglia,M.Fiore,A.Banchs,andX.Costa-Pérez,
“Resource sharing efficiency in network slicing,” IEEE Trans. Netw. Shalitha Wijethilaka (Student Member, IEEE)
ServiceManag.,vol.16,no.3,pp.909–923,Sep.2019. received the bachelor’s degree (First Class Hons.)
[215] B. Khodapanah, A. Awada, I. Viering, J. Francis, M. Simsek, and in electronics and telecommunication engineering
G.P.Fettweis,“Radioresourcemanagementincontextofnetworkslic- from the University of Moratuwa, Sri Lanka, in
ing:Whatismissinginexistingmechanisms?”inProc.IEEEWireless 2017.HeiscurrentlypursuingthePh.D.degreewith
Commun.Netw.Conf.(WCNC),2019,pp.1–7. theSchoolofComputerScience,UniversityCollege
[216] S.Underwood,“Blockchainbeyondbitcoin,”Commun.ACM,vol.59, Dublin,Ireland.Hismainresearchinterestsinclude
no.11,pp.15–17,2016. networkslicing,networksecurity,andIoT.
[217] M.Swan,Blockchain:BlueprintforaNewEconomy,Sebastopol,CA,
USA:O’ReillyMedia,Inc.,2015.
[218] T.Hewa,M.Ylianttila,andM.Liyanage,“Surveyonblockchainbased
smart contracts: Applications, opportunities and challenges,” J. Netw.
Comput.Appl.,vol.117,Mar.2021,Art.no.102857.
[219] A.Chaer,K.Salah,C.Lima,P.P.Ray,andT.Sheltami,“Blockchainfor Madhusanka Liyanage (Senior Member, IEEE)
5G:Opportunitiesandchallenges,”inProc.IEEEGlobecomWorkshops receivedtheB.Sc.degree(FirstClassHons.)inelec-
(GCWkshps),2019,pp.1–6. tronicsandtelecommunicationengineeringfromthe
[220] HowBlockchainCanImpacttheTelecommunicationsIndustryandIts University of Moratuwa, Moratuwa, Sri Lanka, in
RelevancetotheC-Suite.Accessed:Sep.5,2020.[Online].Available: 2009, the M.Eng. degree from the Asian Institute
https://www2.deloitte.com/content/dam/Deloitte/za/Documents/ of Technology, Bangkok, Thailand, in 2011, the
technology-media-telecommunications/za_TMT_Blockchain_TelCo. M.Sc. degree from the University of Nice Sophia
pdf Antipolis, Nice, France, in 2011, and the Doctor
[221] A. Braeken, M. Liyanage, S. S. Kanhere, and S. Dixit, “Blockchain of Technology degree in communication engineer-
and cyberphysical systems,” Computer, vol. 53, no. 09, pp.31–35, ing from the University of Oulu, Oulu, Finland, in
Sep.2020. 2016. From 2011 to 2012, he worked a Research
[222] N. Weerasinghe, T. Hewa, M. Dissanayake, M. Ylianttila, and ScientistwiththeI3SLaboratoryandInria,ShopiaAntipolis,France.Heis
M.Liyanage,“Blockchain-basedroamingandoffloadserviceplatform currentlyanAssistantProfessor/AdAstraFellowwiththeSchoolofComputer
forlocal5Goperators,”inProc.IEEEConsum.Commun.Netw.Conf. Science,UniversityCollegeDublin,Ireland.HeisalsoactingasanAdjunct
(CCNC),2020,pp.1–6. ProcessorwiththeCenterforWirelessCommunications,UniversityofOulu.
[223] B.Nour,A.Ksentini,N.Herbaut,P.A.Frangoudis,andH.Moungla, From2015to2018,hehasbeenaVisitingResearchFellowwiththeCSIRO,
“Ablockchain-basednetworkslicebrokerfor5Gservices,”IEEENetw. Australia,theInfolabs21,LancasterUniversity,U.K.,ComputerScienceand
Lett.,vol.1,no.3,pp.99–102,Sep.2019. Engineering, The University of New South Wales, Australia, School of IT,
[224] L. Zanzi, A. Albanese, V. Sciancalepore, and X. Costa-Pérez, University of Sydney, Australia, LIP6, Sorbonne University, France, and
“NSBchain: A secure blockchain framework for network slicing bro- Computer Science and Engineering, The University of Oxford, U.K. His
kerage,”2020.[Online].Available:arXiv:2003.07748. researchinterestsare5G/6G,SDN,IoT,Blockchain,MEC,mobileandvirtual
[225] K. Valtanen, J. Backman, and S. Yrjölä, “Creating value through networksecurity.HewasarecipientofprestigiousMarieSkłodowska-Curie
blockchain powered resource configurations: Analysis of 5G network ActionsIndividualFellowshipfrom2018to2020.In2020,hehasreceivedthe
slice brokering case,” in Proc. IEEE Wireless Commun. Netw. Conf. 2020IEEEComSocOutstandingYoungResearcherAwardbyIEEEComSoc
Workshops(WCNCW),2018,pp.185–190. EMEA.Moreinfo:www.madhusanka.com.