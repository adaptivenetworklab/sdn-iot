# Adaptive Network Slicing in Multi-Tenant 5G IoT Networks (1)

> Source file: `Adaptive Network Slicing in Multi-Tenant 5G IoT Networks (1).pdf`

---

ReceivedDecember29,2020,acceptedJanuary4,2021,dateofpublicationJanuary18,2021,dateofcurrentversionJanuary26,2021.
DigitalObjectIdentifier10.1109/ACCESS.2021.3051940
Adaptive Network Slicing in Multi-Tenant
5G IoT Networks
ANTONIOMATENCIOESCOLAR 1,JOSEM.ALCARAZ-CALERO1,(SeniorMember,IEEE),
PABLOSALVA-GARCIA 1,JORGEBERNALBERNABE 2,ANDQIWANG 3
1SchoolofComputing,EngineeringandPhysicalSciences,UniversityoftheWestofScotland,PaisleyPA11LU,U.K.
2DepartmentofInformationandCommunicationEngineering,UniversityofMurcia,30100Murcia,Spain
3SchoolofComputing,EngineeringandPhysicalSciences,UniversityoftheWestofScotland,PaisleyPA11LU,U.K.
Correspondingauthor:JoseM.Alcaraz-Calero(jose.alcaraz-calero@uws.ac.uk)
ThisworkwassupportedinpartbytheEuropeanCommissionthroughtheproject6GBringingReinforcementlearningInto
RadioLightNetworkforMassiveConnections(BRAINS)underGrantH2020-ICT-2020-2/101017226,andinpartbytheUniversityofthe
WestofScotland5G(UWS5G)VideoLaboratoryproject.
ABSTRACT The Fifth Generation (5G) mobile networking coupled with Internet of Things (IoT) can
provideinnovativesolutionsforawiderangeofusescases.Theflexibilityofvirtualized,softwarizedand
multi-tenantinfrastructuresandthehighperformancepromisedby5Gtechnologyarekeytocopewiththe
deployment of the IoT use cases demanded by various vertical businesses. Such 5G IoT use cases incur
challenging Quality of Service (QoS) requirements especially connectivity for millions of IoT devices to
achieve massive Machine-Type Communication (mMTC). In addition, network slicing is a key enabling
technology in 5G multi-tenant networks to create logical virtualized networks for delivering customised
solutionstomeetdiverseQoSrequirements.Thisworkpresentsa5GIoTframeworkwithnetworkslicing
capabilities able to manage a vast number of heterogeneous IoT network slices dynamically on demand.
The proposed solution has been empirically tested and validated in five realistic vertical-oriented IoT use
cases. The achieved results demonstrate a excellent stability, isolation and scalability while being able to
meetextremeQoSrequirementseveninthemostcongestedandstressfulscenarios.
INDEX TERMS 5G, Internet of Things (IoT), network management, network slicing, quality of service
(QoS),softwaredefinednetworks(SDN).
I. INTRODUCTION Massive Machine-Type Communication (mMTC), and
TheFifthGeneration(5G)mobilenetworksallowinstantiat- demand efficient communications with millions of con-
ingmultipleconcurrentlogicalsystemstomeetdiverseverti- strainedIoTdevices.SomeusecasesinSmartcitiese.g.,traf-
calindustryservicerequirements,overacommonunderlying ficmonitoringthroughvideocameraswouldneedEnhanced
softwarized,virtualizedandmulti-tenantinfrastructure.The Mobile Broadband(eMBB) communicationto achievehigh
InternetofThings(IoT)isbeingembracedbythe5Garchi- dataratesandlowlatency.
tecture,wherevariousverticalIoTservicessuchasIndustrial To meet the diverging network performance demands
IoT(IIoT),SmartAgricultureorSmartCitiesamongothers, by heterogeneous vertical use cases, network slicing has
canbeinstantiatedoverthesamesharedphysicalnetworkand emerged as a key approach in 5G. A network slice can be
cloudified5Ginfrastructure. defined as a set of network functions and the associated
Each vertical imposes different requirements in terms network resources that are logically isolated and allocated
of network Quality of Service (QoS) parameters such as accordingtotheService-LevelAgreement(SLA),andcanbe
bandwidth, reliability and latency/delay. For instance, IIoT sharedperkindoftraffic,perservice,protocolorapplication,
typically requires high reliability to cope with critical ser- or dedicated per user or per device, if allowed by a flexible
vices based on Ultra-Reliable and Low-Latency Commu- 5Gmanagementsystem.Differenttypesofcommunications
nications (uRLLC). Smart agriculture scenarios may need canbesupportedbydifferentkindsofnetworkslices[1].
Therefore, different IoT services can be virtualized and
The associate editor coordinating the review of this manuscript and instantiated in dedicated slices based on different service
approvingitforpublicationwasMarcoMartalo . requirements,whereIoTserviceproviderscanallocatethose
14048 ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME9,2021

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
slicesinacost-effectivewayandattendtouserspreferences. for virtualized, multi-tenant, and mMTC communica-
Industrial IoT services, e.g. mission critical services, can tions,managingthousandsofheterogeneousslices.
be moved to the Edge of the network in a specific slice to • A new enforceable protocol is defined to apply net-
minimize transition delay while massive IoT services e.g. work slices in the 5G IoT network and cope with in
forsmartcitieswillrequirevastnumberofdedicatedslices, ahomogeneousandtechnology-agnosticapproachwith
each one with different QoS needs. As recently highlighted thedifferenttechnologiesandhardwarecomposingthe
asmajorchallengesin[2],5Gnetworkslicingshouldenable dataplane.
new business models for delivering heterogeneous 5G ser- • Thenetworkslicingapproachhasbeenimplementedin
vices exploited by different industry verticals, combining thedataplanebysignificantlyextendingOpenvSwitch
different 5G services types including mMTC, uRLLC and (OVS),usingakernelspacemechanisminordertohave
eMBBwhileensuringnecessaryperformanceandscalability fullcontroloftheslicinginvirtualized5GIoTnetworks.
throughpropersliceisolationanddynamism. • Agile and flexible management of slices which allows
Torealizeatrulyscalable5GIoTslicemanagement,there dynamicadaptationondemandtotheverticals’needs.
could be multiple concurrent shared slices plus a potential • The proposed solution has been empirically validated,
vastnumberofdedicatedslicesallocatedperIoTdevice,with withperformanceevaluationoverareal5GIoTnetwork
differentnetworkparametersneeds,andwithdifferentpacket deploymentusingvertical-orientedusecases.
sizesandprotocols.Intheworstcase,thiscouldmeanthatthe Therestofthepaperisorganizedasfollows.InSectionII
virtualswitchesinthedatapathneedtocopewithmillionsof we analyze the current state of the art regarding network
heterogeneousconcurrentadaptiveslices. slicing in 5G IoT networks. Section III lays out the spe-
5Gmanagementframeworksandnetworkelements,such cific requisites that 5G IoT networks must satisfy to pro-
as virtual network switches and routers deployed over the vide adaptive network slicing capabilities and provides an
5Ginfrastructureneedtobeevolvedtocontroldynamically overview of the proposed 5G IoT multi-tenant architecture.
the network traffic of multiple, heterogeneous and concur- SectionIVpresentstheproposedSliceControlarchitecture.
rent tenants, from diverse verticals, ensuring QoS parame- Then, Section V introduces the vertical-oriented IoT use
ters over the shared network’s available resources. The new cases used to empirically evaluate and validate the solution
imposed requirements are manifold, as the new 5G slicing proposed in this work. Section VI provides implementation
implementations need to deal with nested-encapsulation in details and a description of the testbed deployed to conduct
thedatapathtosupportbothmobilityandmulti-tenancytypi- the experiments. Section VII presents the achieved experi-
callythroughtunnellingprotocolssuchasVXLANandGTP, mental results in terms of scalability, QoS performance and
support scalability to handle a vast number of concurrent adaptive management of the life cycle of network slices.
heterogeneousslices,enableflexibilityandelasticitytoman- Finally,conclusionsaredrawnwithfutureresearchactivities
age and orchestrate dynamically on demand slicing rules outlinedinSectionVIII.
overmultiplevirtualnetworkappliancesandthusensurethe
slices end-to-end, and assure interoperability with enriched II. BACKGROUNDANDRELATEDWORK
slicing models enforceable and understandable in the data Network slicing for 5G IoT deployments plays a key role
plane. to provide the capability to enable the new business models
Tothebestoftheauthor’sknowledge,thesolutionsiden- expectedintheIoTera.Thisfactisevidencedbyasignificant
tifiedinthecurrentliteratureprovideeitherpartialsolutions amountofresearchactivityandcontributionsonthissubject.
forspecificusecasesorpresentpreliminaryoutcomes.They Inarecentsurvey,Khanetal.[3]reviewthelatestadvances
havenotbeenvalidatedinarealistic5GIoTscenariowhere ofnetworkslicingforIoTverticalsandusecases,including
differentserviceswithvaryingQoSrequirementsandtraffic smart transport systems, smart industry, smart homes and
profilearedemanded,challengingthe5Ginfrastructureand smartcare.Theyidentifyscalability,interoperabilityandeffi-
imposing the imperative of addressing 5G network traffic cientresourceallocationamongthemajoropenresearchchal-
withmultiplelevelsofnestedencapsulation. lengesrelevantto networkslicing.Furthermore,theauthors
Tocontributetoaddressingtheabovechallenges,thispaper highlightasoneoftheirmainconclusionsthatnetworkslicing
introducesanew5GIoTslicecontrolframeworkthatallows isanindispensabletechnologytoenableawiderangeof5G
theadaptiveinstantiationandmanagementofheterogeneous use cases and beyond. They also underline that it is neces-
andevolvingslicesovermultipletechnologicalIoTdomains, sarytoproposenoveladaptivenetworkslicingmanagement
which demand different slicing according to the vertical schemes to cope on demand with services of varying users’
needs. demands.
Thecontributionsofthispaperaremanifold: Severalauthorshaveproposed5G-basedsolutionsforspe-
• A practical cognitive network management framework cific IoT use cases. For instance, Cheng et al. [4] propose
ispresentedforautonomicenforcementofscalablenet- a 5G IoT architecture for smart manufacturing although no
workslicingin5GIoTnetworks. implementationisprovided.In[5],theauthorsanalyzehow
• Anew,highlyscalablenetworkslicingapproachispro- network slicing technology in 5G networks can meet the
posed for multi-tenant 5G networks especially devised specific needs of different smart grid services to support
VOLUME9,2021 14049

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
multiple power business scenarios in Power Internet of IoTscenarios.DespitethesetwoworkaddressthemMTCser-
Things (PIoT). In [6], the authors focus on IoT solutions vicesrequirements,theyarenotfocusedonQoSmanagement
forSmartHomeapplicationsandproposea5Garchitecture neededfordealingwith5Gnetworkslicing.
wherethreeslicesaredeployed(SmartHomesecurity,eMBB A novel network slicing framework for 5G networks is
trafficandMassiveIoTtraffic).Unlikeourproposalthatpro- presented and evaluated in [16]. The authors address spe-
vides a 5G IoT framework able to cope with heterogeneous cific challenges of media use cases, through an End-to-End
5GIoTtraffic,alltheseworkaddressthedeploymentofIoT QoS-awareslicingintendedtosupportmigrationofmission
usecasesin5Ginfrastructuresfromtheperspectiveofagiven critical services (eHealth tele-medicine services) to 5G net-
single use case and the authors do not provide an empirical works.TheproposedsystemimplementsLowLatencyMEC
validationandevaluationoftheofferedsolution. Platform,withQoScontrolbasedondataplaneprogramma-
Kapassa et al. [7] describe an IoT-oriented architecture bility that allows establishing priorities of the 5G network
for5GnetworkslicingthatenablestheallocationofQuality traffic.Unlikeourworkwhichsupportscombinationofeither
ofService(QoS)ofdiverseconcurrentIoTapplicationsand mMTC,eMBB,andURLLCservices,theyfocusmainlyon
serviceswithdifferentrequirements.Nonetheless,theydonot mediausecases,withhighdemandsintermsoflowlatency
implementorvalidatetheirproposal. (URLLservices)andhighbandwidth(eMBB).
In [8], the authors propose an authentication framework Regarding network slicing solutions complying with the
supporting network slicing and fog computing for 5G IoT, specifications and standards developed by the Standardiza-
allowing users to establish secure connections with IoT tionDevelopmentOrganizations(SDOs)andthe5GIndustry,
devicesthroughdedicatedslices.Unliketheirwork,wefocus Diaz-Rivera et al. [17] propose a Network Slice Selection
onthemechanismforslicemanagementinthe5Gdatapath, Function(NSSF)toenabletheselectionofslicesinthedata
ratherthansecurityaspectsofslicing. planemeetingthe3GPPfunctionalityspecifications[18].The
Kurtz et al. [9] propose and implement a slicing mech- authorsprovideafunctionalvalidationalthoughtheydonot
anism for 5G networks based on SDN/NFV, evaluated in reportresultsonscalabilityorbehaviourinIoTenvironments
demanding critical infrastructure use cases. They use OVS or5Gmulti-tenantnetworks.Thispaperhighlightstheimpor-
andSDNcontrollerstoenforcetheslices.However,theydo tance of providing an abstraction mechanism for network
not use real 5G traffic that demands specific modifications configurationduetothegrowingcomplexityofthedataplane
(e.g.duetoencapsulationtoprovidetenantisolationanduser which is one of the strengths of our contribution (see Data
mobility in 5G networks) in the datapath management (e.g. PlaneAbstractionServicedescriptioninsectionIV).
adaptationinswitcheslikeOVS)tohandletheslices. Network Slicing in industrial environments with extreme
In [10], the authors propose an end-to-end mIoT slicing QoSrequirementsisamajorchallengefacedbythe5Gindus-
mechanism with enhanced control and user planes (CP/UP) try and several contributions have been made in the recent
for the 5G network. Unlike in our work that focuses on past.Inthisregard,in[19]authorsproposeamethodtoper-
ensuringtheQoSinthedatapath,theyfocusonreducingthe form network slicing for deterministic and packet-switched
signaling overhead and an efficient UP resource utilization. industrial communication protocols such as OPC-UA.
Moreover,theirsolutionisstillpreliminaryasitissimulated Rost et al. [20] describe a testbed in a real industrial envi-
notimplementedinarealistic5Gnetwork. ronment, the Hamburg port area, where they deploy a 5G
Bektasetal.[11]proposeaRANnetworkslicingscheduler infrastructurewithnetworkslicingcapabilitiessuchasslice
for5G,aimedtodealwithmissioncriticalservicesdemanded isolation, flexible slice customization and multi-tenancy.
byIoTverticals(e.g.SmartGrid). In [21], authors propose a framework aimed at providing
In[12],theauthorsproposeandvalidatedynamicnetwork networkslicingcapabilitiestomeetthespecificrequirements
slicingfor5GIoTandeMBBservices.Althoughtheymanage of Industry 4.0. The framework provides slicing through
properly and dynamically the slices, their proposal assumes public and private federated infrastructures across Radio,
just two slices for the traffic profile, i.e. one for IoT traffic Edge and Core segments. The framework is validated with
andtheotherforeMBBservices.Similarly,theslicingarchi- 3 use cases: remote production monitoring, remote equip-
tectureproposedby[13]evaluatesonesliceper5Gservices ment maintenance and dynamic industrial manufacturing.
types:mMTC,eMBB,oruRLLC. Although promising, none of these works give results on
Asoftware-baseddataplaneprogrammabilityapproachis scalabilityandperformanceandthereforedonotdemonstrate
followedbySalva-Garciaetal.[14]toperformnetworktraf- their suitability in the foreseen large-scale industrial IoT
ficfilteringformulti-tenant5GIoTnetworksinkernelspace. scenarios.Theyalsodonotcovermultipleusecaserunning
Likeinourwork,theyfollowanintent-basedandSDNmodel simultaneouslytodemonstratethesuitabilityofslicing.
foradaptive,flexibleandnetworkfilteringinmassiveMTC Efficient QoS-aware data plane network slicing in 5G
scenarios demanded by IoT. Similarly, Matencio-Escolar networks has been recently implemented in hardware by
et al. [15] implement a software-defined firewall for 5G Ricart-Sanchezetal.[22].Itprovideshardware-basedtraffic
NB-IoT networks to increase considerably the number of classification, priority configuration, and traffic scheduling
supported rules (up to one million), which makes it fully usingNetFPGAs.Moreover,theframeworkdealswithtraffic
suitableforhighlydemandedmMTCservicesdemandedby withtwolevelsofencapsulation(VXLAN,GTP)tosupport
14050 VOLUME9,2021

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
multi-tenant5Gnetworksandallowsperformingisolationfor • Heterogeneous slicing support: the slicing system
5G MEC network traffic. Although the general goal of that should concurrently and efficiently support the control
paper is similar to ours, they do not address the particulari- and management of heterogeneous network traffic and
ties of IoT scenarios, with thousands of devices and slices, protocolsdemandedbydifferentverticals,whomayuse
asevaluatedinourproposal. anyofthe5GservicestypesincludingmMTC,URLLC
Despite the considerable number of related work in the and eMBB or a combination of these types in more
areaof5GIoTnetworkslicing,practical,scalableandflexi- demandingusecases.
blesoftware-definednetworkingsolutionsarestillnotsuffi- • Flexibleandadaptivemanagement:theslicingsystem
cientlyresearchedfromthe5Gdatapathperspectivetosatisfy should be able to manage on demand and efficiently
various use cases of diverging requirements including not adaptingtheslicingoftheevolving5GIoTnetworktraf-
only massive IoT scenarios but also hybrid scenarios with fic,andaddingordecommissioningtheslicingpolicies.
heterogeneousIoTtrafficprofiles. This will allow upper cognitive layers in the 5G man-
agementframeworktoautomaticallyupdatethenetwork
III. NETWORKSLICINGINVIRTUALIZEDAND slicingbehaviouraccordingtothecontext.
MULTI-TENANT5GIOTDEPLOYMENTS • Interoperability: the system should be managed by a
A. SLICINGREQUIREMENTSIN5G-ENABLEDIoT common,interoperableandhigh-levelabstractinterface,
NETWORKS following a common data model intended to handling
There are a number of specific requirements for adaptive dynamicallydifferentkindsofslicesforheterogeneous
networkslicingin5GIoTnetworks,listedasfollows: traffic.
• Multi-tenant support: 5G IoT networks comprise
virtualized network functions running over a shared B. 5GIoTMULTI-TENANTINFRASTRUCTUREFOR
physical infrastructure, which is exploited simultane- VERTICALBUSINESSES
ously by different verticals and operators. Therefore, This section overviews an infrastructure that perfectly
the network slicing system should be able to handle matches the case of study in this paper and gives a realistic
encapsulatednetworktrafficintendedtodifferentiatethe scenariotoresearchandevaluatetheproposedsolution.From
networkslicesandtheassociatedSLAspereachtenant. abottom-upperspective,Fig.1showsfourdifferentnetwork
• Mobility support: as identified as a major challenge segments:(i)TheRadioAccessNetworktoconnectindivid-
in 5G IoT slicing [2], the slicing system should be ualdevicestothe5Gnetwork.(ii)TheMobile/Multi-access
able to handle, differentiate, manage and control effi- EdgeComputing(MEC)segmenttoenhancetheexperience
cientlytheGTPencapsulatednetworktrafficneededto ofenduserswhenaccessingcommonservicesthroughcom-
dealwithUserEquipment(UE)i.e.,IoTdevicemobil- putingresourcelocalization.(iii)The5GCoreNetworkseg-
ity.ThisincludeshandlingtheUplink/Downlinktraffic ment with expanded service capabilities, scalability, agility
differentiating tunnels by the management framework and network functions. (iv) The Inter-domain Segment to
andtheslicingagent.Indeed,theslicingsystemshould reach the Internet and other domains managed by different
support nested encapsulation to deal with mobility and organisations.
multi-tenancysimultaneously. Itisnotedthatthe5GarchitecturefollowsaServiceBased
• ScalableslicingformMTC:inordertosupportmMTC Architecture (SBA) and builds upon virtualization and soft-
services,theslicingsystemshouldbeabletohandleand warisation paradigms. These technologies are expected to
differentiate traffic coming from a vast number (mil- have a significant impact on 5G deployment as they aim to
lions) of different devices. It could imply managing offersignificantagilityandflexibilitytomeetverticalindus-
andcontrolefficientlythousandsofconcurrentnetwork tries’ service requirements while providing multi-tenancy
slices (in the most demanding case one slice per IoT and user mobility capabilities in a common underlying
device). infrastructure. That allows scenarios like the one presented
• IoT service differentiation with high bandwidth in Fig. 1 where different verticals, each one imposing dif-
requirements (eMBB services): certain IoT verticals ferentnetworkrequirements(e.g.,eMBB,mMTC,uRLLC),
(e.g. video surveillance in Smart cities) might require are co-existing in the same infrastructure. To deal with
broadband communications with high transmissions such heterogeneity of the network, this paper proposes a
rates. The slicing management system should support Software-DefinedNetwork(SDN)approachthatisbasedon
subscriptionassociatedtohighbandwidthrequirements, extendingtheindustry-leading,production-qualityOVSplat-
andtheslicingcontrolsystemshouldbeefficientlyhan- formandallowscontrolling,managingandactingoncomplex
dlethatkindoftraffic. network traffic (see Fig. 4) traversing these architectures.
• IoT device differentiation with reliable and low Theobjectiveistoguaranteetheeffectivefunctioningofthe
latency requirements (URLLC services): the slicing vertical slices associated to each tenant/service through the
system should support the subscription, management whole 5G network. Specifically, we leverage the proposed
and control of dedicated slices with ultra reliable low 5G IoT Slice Management Framework to interact with this
latencyrequirements. enhancedOpenvSwitchtoensurethatSLAsarerespected.
VOLUME9,2021 14051

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
FIGURE1. Overviewoftheproposed5GIoTMulti-TenantInfrastructure.
C. 5GIoTSLICEMANAGEMENTFRAMEWORK • Virtual Area. It contains all the virtualised equipment
To be able to provide dynamic adaptation of the network (createdbythehypervisor)runningontopofthephysi-
slicingcapabilitiespresentedinthisresearch,aSliceManage- calcomputersthatrepresentlogicalhardwareresources
mentFrameworkhasbeenadoptedasillustratedinFig.2.The assignedtospecifictenants.
frameworkiscomposedmainlyoffivearchitecturaldomains.
ThearrowsinFig.2indicatethecommunicationmanagement 2) CONTROLANDMANAGEMENTDOMAIN
among the different planes and their underlying modules. • Sensing. It provides a common point to manage all
Roles and responsibilities of each component are described the different sensors that report metrics about the cur-
below,fromabottom-upperspective. rentstateoftheinfrastructure.Here,time-basedmetric
reports are collected for monitoring purposes such as
1) INFRASTRUCTUREDOMAIN portspeed,bandwidthconsumedorbandwidthavailable
• PhysicalArea.Itcontainsallthe5Ghardwareresources atdifferentpointsofthenetwork.
such as computes, storage and networking devices, • SDN Controller. It is the module that maintains a
amongothers,placedthroughoutthephysicalinfrastruc- strategic control point in an SDN as the one presented
tureabletobesharedamongthedifferenttenants. here. From its northbound API (NBI) it receives the
14052 VOLUME9,2021

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
|     |     |     |     |     |     |     | • Virtual | Infrastructure |           |         | Manager | (VIM).          | It      | controls |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --------- | ------- | ------- | --------------- | ------- | -------- |
|     |     |     |     |     |     |     | virtual   | resources      |           | and the | life    | cycle of        | all the | virtual  |
|     |     |     |     |     |     |     | hardware  |                | resources | in the  | virtual | infrastructure. |         | It also  |
keepsthecatalogandtheinventoryoftheexistingVMs.
|     |     |     |     |     |     |     | 3) ADAPTIVESLICEANDORCHESTRATIONDOMAIN           |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | • Monitoring.ItmonitorsmetricsprovidedbytheSens- |     |     |     |     |     |     |     |
ingmoduletoperformhighlyscalabledatastorage.
|     |     |     |     |     |     |     | • Analyzer.Itallowsthedefinitionofrulesthatareused |     |             |     |        |        |                |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | ----------- | --- | ------ | ------ | -------------- | --- |
|     |     |     |     |     |     |     | to monitor                                         |     | the current |     | status | of the | infrastructure | by  |
usingspatialandtemporalcorrelationintheinformation
|     |     |     |     |     |     |     | gathered | from | both | the | monitoring | component |     | and the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ---- | --- | ---------- | --------- | --- | ------- |
resourceinventory.Therulesproducealertsaboutspe-
cificeventsintheinfrastructurethatrequireattention.
|     |     |     |     |     |     |     | • PolicyPlanner.Itmakesitpossibletodefinetemplates |          |              |     |              |     |           |        |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | -------- | ------------ | --- | ------------ | --- | --------- | ------ |
|     |     |     |     |     |     |     | that                                               | are used | to transform |     | the strategy |     | indicated | by the |
SlicePolicyEditorintoanorderedsetofimplementable
stepsrequiredtoimplementthestrategyreceived.
|     |     |     |     |     |     |     | Orchestrator. |     | It  | receives | an implementable |     |     | plan and |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | -------- | ---------------- | --- | --- | -------- |
•
|     |     |     |     |     |     |     | then | orchestrates |     | the execution |     | of each | of  | the steps |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------ | --- | ------------- | --- | ------- | --- | --------- |
involvedintheplaninordertoenforceitintotheinfras-
tructurewiththepurposeofresolvingthealert.
|     |     |     |     |     |     |     | 4) ADMINPLANE                                      |       |             |     |           |        |           |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | ----- | ----------- | --- | --------- | ------ | --------- | --- |
|     |     |     |     |     |     |     | • SlicePolicyEditor.Anyauthorizedexternalagentthat |       |             |     |           |        |           |     |
|     |     |     |     |     |     |     | can                                                | reach | the exposed |     | functions | by the | framework | to  |
create,modifyorremovenetworkslices.Usually,verti-
calservicesadministratorswilldefineheretheirtailored
configurations.
|     |     |     |     |     |     |     | IV. SLICECONTROLARCHITECTURE |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
Fig.3depictsamodulararchitecturedividedinthreediffer-
|     |     |     |     |     |     |     | ent planes. | First | (on top), | the | Infrastructure |     | Management |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --------- | --- | -------------- | --- | ---------- | --- |
FIGURE2. Architectureofthecognitive5GIoTSliceManagement Plane provides the slice policies to be enforced throughout
Framework.
|              |             |     |            |         |                |     | the infrastructure. |              | Next,       | the        | Infrastructure |         | Control   | Plane       |
| ------------ | ----------- | --- | ---------- | ------- | -------------- | --- | ------------------- | ------------ | ----------- | ---------- | -------------- | ------- | --------- | ----------- |
|              |             |     |            |         |                |     | is used             | as an        | entry point | to         | apply          | traffic | control   | rules to    |
|              |             |     |            |         |                |     | any of the          | programmable |             | networking |                | devices | available | on          |
| instructions | to apply    | the | business   | logic   | by controlling |     |                     |              |             |            |                |         |           |             |
|              |             |     |            |         |                |     | the network         | equipment    |             | by         | following      | the     | SDN       | principles. |
| flows and    | programming |     | networking | devices | placed         | on  |                     |              |             |            |                |         |           |             |
Itisnotedthatusuallythisplanedirectlyprogramsrequested
thedataplane.Inparticular,thisresearchproposesanew
|           |        |      |            |       |         |       | network  | control | actions  | into    | a concrete | networking |          | device.   |
| --------- | ------ | ---- | ---------- | ----- | ------- | ----- | -------- | ------- | -------- | ------- | ---------- | ---------- | -------- | --------- |
| component | in the | data | plane, the | Slice | Control | Agent |          |         |          |         |            |            |          |           |
|           |        |      |            |       |         |       | However, | as it   | is shown | in this | figure,    | we         | delegate | this task |
(SCA),whichwillfinallybeinchargeofsuchprogram-
ming of the network device. This is further explained to a proposed Slice Control Agent (SCA) (at the Resource
|     |     |     |     |     |     |     | Control | Plane), | to abstract |     | particular | slicing | tasks | and to |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ----------- | --- | ---------- | ------- | ----- | ------ |
withmoredetailinSectionIV-A.
|                     |     |     |              |     |                |     | homogenize | technology-dependant |     |     |     | syntax | among | different |
| ------------------- | --- | --- | ------------ | --- | -------------- | --- | ---------- | -------------------- | --- | --- | --- | ------ | ----- | --------- |
| • VNF Orchestrator. |     | It  | is in charge | of  | the deployment |     |            |                      |     |     |     |        |       |           |
FlowAgentsthatco-existinthenetwork.Tothisend,atthe
| of the different | Virtual |     | Network | Functions | (VNFs) | by  |           |        |               |     |       |        |        |          |
| ---------------- | ------- | --- | ------- | --------- | ------ | --- | --------- | ------ | ------------- | --- | ----- | ------ | ------ | -------- |
|                  |         |     |         |           |        |     | lower end | of the | architecture, |     | it is | placed | in the | Resource |
consideringcurrentphysicalandlogicalresourcesofthe
|     |     |     |     |     |     |     | Control | Plane, | where | the | SCA processes |     | every | received |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ----- | --- | ------------- | --- | ----- | -------- |
infrastructure.
messageandprogramsagivennetworkequipment.
| • VNF Manager. |     | It is a | key component |     | of the Manage- |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ------- | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mentandOrchestrationparadigmthatworksinconcert
|                |                  |     |        |        |              |         | A. SLICECONTROLAGENTARCHITECTURE |          |          |      |          |     |          |      |
| -------------- | ---------------- | --- | ------ | ------ | ------------ | ------- | -------------------------------- | -------- | -------- | ---- | -------- | --- | -------- | ---- |
| with the       | VNF Orchestrator |     | (VNFO) | and/or | the          | Virtual |                                  |          |          |      |          |     |          |      |
|                |                  |     |        |        |              |         | The SCA                          | consists | of three | main | modules, |     | SCA-API, | SCA- |
| Infrastructure | Manager          |     | (VIM)  | and it | is in charge | of      |                                  |          |          |      |          |     |          |      |
controlling, managing and monitoring the VNFs’ life Core,andtheDataPlaneAbstractionService(DPAS).
| cycle.Inaddition,italsocontrolsElementManagement |     |     |     |     |     |     | • SCA-API: |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
System (EMS) and/or Network Management System This module is the access point from/to the Infrastruc-
| (NMS).       |     |     |     |     |     |     | ture | Control | Plane. | It consumes |     | intent-based |     | messages |
| ------------ | --- | --- | --- | --- | --- | --- | ---- | ------- | ------ | ----------- | --- | ------------ | --- | -------- |
| VOLUME9,2021 |     |     |     |     |     |     |      |         |        |             |     |              |     | 14053    |

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
|     |     |     |     |     | Listing.1. Intent-basedMessage.      |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- |
|     |     |     |     |     | • DataPlaneAbstractionService(DPAS): |     |     |     |
TheDPASisamodulethatprovidesanabstractionlayer
|     |     |     |     |     | to deal with | the different | network traffic | control tech- |
| --- | --- | --- | --- | --- | ------------ | ------------- | --------------- | ------------- |
nologies(FlowAgents)registeredasplug-ins.Through
FIGURE3. NetworkSliceControlframeworkarchitecture. this approach, the SCA-Core does not need to know
howeachoftheseFlowAgentsworks,therebyachieving
|          |                      |       |                  |     | a modular | approach | where the DPAS | communicates |
| -------- | -------------------- | ----- | ---------------- | --- | --------- | -------- | -------------- | ------------ |
| (further | explained in Section | IV-B) | to apply actions | at  |           |          |                |              |
any location of the data path by exposing the NBI of within a common language with upper layers of the
architectureandthusinatechnology-dependentmanner
| the proposed | service. | When the SCA | is instantiated, |     |     |     |     |     |
| ------------ | -------- | ------------ | ---------------- | --- | --- | --- | --- | --- |
as a first step, it publishes its location and capabili- withanyplug-ableunderlyingFlowAgent.Theaimof
thismoduleistoselectaproperFlowAgentabletoapply
| ties by using | the discovery | and catalogue | sub-modules |     |     |     |     |     |
| ------------- | ------------- | ------------- | ----------- | --- | --- | --- | --- | --- |
slicingpolicyrulesinaspecifichookingpoint(datapath
| respectively. | After that, | it waits for | new intent-based |     |     |     |     |     |
| ------------- | ----------- | ------------ | ---------------- | --- | --- | --- | --- | --- |
messagescomingfromitsNBI.Additionally,theACK point)ofthehostcomputer.
| sub-module | publishes | the result of | any applied | action |     |     |     |     |
| ---------- | --------- | ------------- | ----------- | ------ | --- | --- | --- | --- |
overthedataplaneandthemetricssub-moduleprovides B. INTENTDEFINITIONFOR5GIoTNETWORKSLICES
behavioralinformationontheperformanceofasuccess- The Intent-based Consumer sub-module, depicted in the
fullyappliedslice. upper left corner of the resources control plane of Fig. 3,
• SCA-Core: conceptualizes the lower level details used to interface with
TheSCA-Coremoduleprocessesincomingintent-based higher level infrastructure control components and decom-
messagesandmanagesthelifecycleoftheslices.Ithas poses concepts in the technical details to enable following
the logic to dissect the packet representation struc- sub-modules to program a target networking device on the
tureintodifferentsub-flowsassociatedtoeachoverlay dataplane.Messagesreachingthisnorthboundinterfaceare
network. The slice builder sub-module creates generic composedofoneormoreresourcesdescribingtheflowsto
instructions to satisfy the slice requirements but dele- take action to, one intent that defines which kind of action
gatestheirimplementationtootherunderlyingmodules hastobeappliedoversuchflows(e.g.createaslice),anda
thatcontainthelogicforaspecifictechnology.Inaddi- listofparametersforfine-grainedspecifications(e.g,target
tion, it also contains a metric sub-module in charge of networkinterface,mode,time,duration,etc.).
calculating and sharing slice metrics by using its local Listing 1 gives an example of a message that could be
database. received at the NBI of the SCA to be processed. This
| 14054 |     |     |     |     |     |     |     | VOLUME9,2021 |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------------ |

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
particularexampleshowsanintent-basedmessagewiththree overlay network for each tenant over IoT traffic previously
resources, the original network traffic flow plus two encap- encapsulatedwithGTP.TheGTPencapsulationanddecapsu-
sulations.Eachresourcecontainsvaluableinformationabout lationareperformedbythegNBintheRANsegmentandthe
itsown/previousencapsulationdetailsandsomenetworking UPFinthecoresegment.Regardingtenantisolation,thevir-
parameterswithspecificprotocolfields/valuesthatrepresent tual switches that interconnect the virtual machines in both
the network traffic belonging to what has been defined as a edgeandcoresegmentsareresponsiblefortheencapsulation
slice.Tokeepthisexamplesimpleforbrevity,Listing1just anddecapsulationoftheoverlaytraffic.
includes srcIP and dstPort but any other field of any other Thisworkadoptsthedefinitionofnetworksliceproposed
protocol (if present in the packet structure) would also be in[25].Thescopeofthisnetworkslicedefinitionisflexible
allowedhere.Moreover,theIntentsectionindicatestocreate enoughtodealwithalltypesoftrafficthatcanbeidentifiedin
a new slice where all network traffic matching this specifi- a5Gnetwork(suchasthoseshowninFig.4)inordertomeet
cationwillbeforwardedbyusingaOVS-basedFlowAgent. thediverseQoSrequirementsthatverticalusecasesdemand.
ThreefieldsoftheIntentdefinetheQoSrequirementsofthe Inaccordancewiththisdefinition,differentslicescaninvolve
slice:Priority,MinimumGuaranteedBandwidth(MGB)and traffic with different levels of granularity depending on the
Maximum Allowed Bandwidth (MAB) and they are further usecaseaddressed.Forinstance,aslicecouldbeallthetraffic
explained in subsection V-C. Finally, the section Params ofaparticulartenant,thetrafficofaverticalor,withamore
givesinstructiontoprogramthisjustovertheinterfaceeth0. fine-graineddetail,thetrafficofasingleIoTdeviceoreven
ItshouldbenotedthatListing1justshowsanexamplewith thetrafficofasingleserviceofaspecificIoTdevice.Inthe
the aim of simplifying the understanding of the structure of experiments conducted to validate the proposed framework,
anIntent-basedmessage,meaningthatmuchmorecomplex a slice corresponds to the network traffic of a vertical, that
resources,typeofactions,andfine-grainparametersarealso is,theaggregatetraffictransmittedbyalltheIoTdevicesof
allowedhere. such specific vertical. Nevertheless, It is worth highlighting
thatourproposalisabletocoverthewidescopeoftheslice
C. SLICECONTROLAGENTSOUTHBOUND:FLOWAGENT definitionproposedin[25].
CAPABILITIESTOENABLENETWORKSLICINGIN5GIoT Therefore, to provide fine-grained network slicing capa-
NETWORKSANDOPENvSwitchEXTENSIONS bilities, the first stage is that the Flow Agents that handle
5G architectures are based on softwarization and virtualiza- network traffic in the data plane must be able to access
tion, using SDN and NFV paradigms as enabling technolo- the inner headers of the packets and extract information
gies[1],[23].Thisallowsdifferenttenantstosharethesame about the IoT devices including Source and Destination
physical infrastructure and, as a result, Telecommunication IP addresses, Source and Destination Ports, etc. and their
ServiceProviders(TSP)canreducebothOperationalExpen- associated metadata including GTP Tunnel Endpoint Iden-
diture(OPEX)andCapitalExpenditure(CAPEX)[24].Fur- tifier (TEID) and VXLAN network identifier (VNI). This
thermore, each mobile IoT device has a dedicated logical scenarioisexacerbatedsince5Gnetworksarecomplexhet-
connectiontothe5GUserPlaneFunction(UPF)tomaintain erogeneousecosystemswheredifferenttechnologiesco-exist
connectivityacrossdifferentnetworks.Therefore,controlling andnetworktrafficistreatedbymanydifferentFlowAgents
tenantisolationanddevicemobilityaretwocrucialaspectsof alongthedatapath,bothhardwareandsoftware,suchasvir-
5GIoTnetworks.Intypicalimplementation,devicemobility tualswitches,NICs,FPGAsorphysicalroutersandswitches.
is supported by encapsulating the original IoT traffic with AsmentionedinsubsectionIV-A,theDPASmoduleofthe
GTP,andtenantisolationisprovidedbyusingothertunneling proposedSCAmitigatesthisproblembyprovidingtheupper
protocolssuchasVXLAN,GRE,STTorGENEVE. managementlayerswithacommontechnology-agnosticAPI
Fig. 4 gives an example of double encapsulated 5G IoT in a transparent manner regardless of the network device
traffic where VXLAN has been chosen to create a virtual playingtheroleofFlowAgentandtheunderlyingnetworking
technology used. In addition, Flow Agents are required to
have capabilities to enforce in the 5G data plane the QoS
policiesimposedbytheuppermanagementandcontrollayer
throughtheDPASAPI.
Theresultspresentedinthispaperarefocusedonaspecific
segmentofthe5Gdataplane,thesoftwaredatapath,whichis
thesegmentthatprovidesconnectivitybetweenthedifferent
VMs of the tenants allocated in the physical hosts of the
5Ginfrastructure.TheFlowAgentdeployedinthesoftware
data path of the proposed architecture is named Open Slice
Virtual Switch (OpenSliceVS) and it has been implemented
bymakingsignificantextensionstothebaseversion2.9.2of
OVS [26], [27]. OVS is an open source multi-layer vir-
FIGURE4. Doubleencapsulationin5Gnetworksfortenantisolationand
5GIoTtrafficmobility. tual switch widely used in virtualized environments where
VOLUME9,2021 14055

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
this, the prototyped Flow Agent has been enhanced
withanewclassifierthatperformsadeepinspectionof
the network packets, providing support for encapsula-
tion/tunneling and other protocols not supported in the
baseversionofOVSsuchasGTP,VXLAN,GENEVE,
GTP and GRE. This new classifier allows re-entrance
betweenheadersthatenableanefficientdeepinspection
oftheinnerheadersoftheoverlaynetworks,gathering
dataaboutthetenants,theIoTdevicesandtheverticals
sothatafine-grainedidentificationofalltypesoftraffic
presentin5GIoTnetworksispossible.
• Open Flow tables: The OpenFlow tables have been
augmented with new fields that increase their expres-
siveness, providing a flexible, fine-grained slice defi-
nition that fits the intend-based message received by
theSCAfromthemanagementplane.Thesenewfields
enrich the semantics of the left part of an OpenFlow
rule,includingmetadataaboutverticals,IoTdevicesand
FIGURE5. OverviewofthearchitectureoftheOpenSliceVSsoftwaredata
encapsulation/tunnelingprotocols.
pathFlowAgent.
• Netlink protocol: The inter-process communication
between the OVS kernel module (openvswitch.ko)
and the OVS user space daemon (ovs-vswitchd) is
SDN/NFVtechnologiesplayakeyrole[1],[23].Itprovides
implemented using netlink sockets provided by the
OpenFlow capabilities to the SDN controller through the
netlink Linux kernel interface. The netlink handler
northbound interface. Since Linux kernel version 3.3, OVS
sub-modules (DPIF) and the user-defined netlinkmes-
kernelmodulesareavailablewithintheupstreamLinuxker-
sageshavebeenextendedtoprovidesupportfor5GIoT
nel distributions. OVS has become essential in SDN/NFV
slicingcapabilities.
deploymentsanditisusedinleadingopensourceSDN/NFV
• North Bound Interface: OVS exposes an OpenFlow-
oriented projects such as OpenDayLight [28] and Open-
based NBI, named OFPROTO, to establish communi-
Stack [29], among others. The following subsection pro-
cation with the upper management and control layers
vides an overview of the OpenSliceVS architecture and
on the basis of SDN principles. The OpenFlow mes-
the extensions implemented to provide support for flexible,
sagesandtheNBIfunctionalitytosendandreceivesuch
fine-grained control of 5G IoT traffic and network slicing
OpenFlowmessageshavebeenextendedtoaddressthe
capabilitiesinthesoftwaredatapathofthe5GIoTnetwork.
newfieldsaddedtotheOpenFlowtables.
• Command line applications: Finally, the command
D. OpenSliceVSFLOWAGENT:ARCHITECTUREAND line application suite included in the OVS distribution
IMPLEMENTATIONDETAILS has also been upgraded with new capabilities to allow
The proposed prototype has been implemented by extend- theupperlayerstomanageslicesinthe5GIoTsoftware
ingsignificantlyseveralOVSfeaturesandfunctionalitiesin datapatheitherbythecommandlineorviaaRESTAPI.
different modules throughout the OVS architecture, both in
To conclude this subsection, the integration between
user and kernel spaces: traffic parser and classifier, flow
OpenSliceVS and the DPAS module (Southbound interface
and actions table, netlink communications between kernel
of the SCA) is achieved via a REST API that enforces the
module and user space daemon (DPIF), OpenFlow proto-
slicepolices(slicedefinitionsandQoSrequirements)inthe
col,OpenFlow northboundAPI (OFPROTO)andcommand
5Gdataplaneusingthecommandlineapplicationsprovided
lineapplicationsinterfaces.Fig.5showsanoverviewofthe
byOpenSliceVS.
OpenSliceVS architecture, depicting the main modules in
both user and kernel spaces. These are the main extensions
implementedtothebaseversionofOVStoprovidenetwork E. DYNAMICMANAGEMENTOFTHELIFECYCLEOFA
slicingsupportwithinthesoftwaredatapath: SLICEINTHEDATAPLANE
• 5GIoTawareTrafficclassifier:OVSdelegatestothe A network slice is a dynamic entity, hence it is required a
Linux kernel flow dissector module the extraction of managementofitslifecycleasithasbeenoutlinedbyStan-
theflowkeythatidentifiesaflowunequivocally.How- dardDevelopmentOrganizations(SDOs)suchas3GPP[30],
ever,theLinuxkerneldoesnotsupportfunctionalityto IETF [31] or 5G Americas [32]. The proposed framework
inspectprotocolheaderssuchasencapsulationheaders offers to the upper control and management layers, a novel
ortheinnerheadersofoverlaytrafficwithseveralencap- mechanismtocontrolthecompletelifecycleofaslicewithin
sulationsthatareexpectedin5GIoTnetworks.Tosolve the data plane aligned with the specifications developed by
14056 VOLUME9,2021

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
andtechnology-specificinstructionissenttothisFlow
|     |     |     |     |     |     | Agent | to create | and enforce |     | the requirements |     | of the |
| --- | --- | --- | --- | --- | --- | ----- | --------- | ----------- | --- | ---------------- | --- | ------ |
newsliceinthedataplane.IntheOpenSliceVSexam-
ple,thecreationofaslicecomprisestwophases.First,
theslicedefinitionisinsertedasanOpenFlowruleinto
|     |     |     |     |     |     | the slice | definition | and | action | table. | Second, | a hierar- |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------ | ------ | ------- | --------- |
chicaltokenbucket(htb)queuingdisciplineconfigured
FIGURE6. Lifecycleofasliceinthedataplane.Aslicecanbeinthree with the QoS requisites of the new slice is created and
differentstates:Creation,inServiceandTermination. attached to he network interface where the slice traffic
willberedirected.Steps12-15arethewaybackuptothe
externalSDNapplicationsothatitcanbeawarewhether
the SDOs. In this regard, a network slice instance can be in thenetworkpolicy(theslice)hasbeenapplied.
threedifferentstatesasdepictedinFig.6:
• VerticalUseCase(Steps16-22):
Creation:Provisionofthenecessarynetworkresources
| •         |                 |           |     |         |          | This last | stage | begins      | when    | the service | starts | to be     |
| --------- | --------------- | --------- | --- | ------- | -------- | --------- | ----- | ----------- | ------- | ----------- | ------ | --------- |
| to ensure | the performance | isolation |     | and QoS | require- |           |       |             |         |             |        |           |
|           |                 |           |     |         |          | used (16) | and   | its network | traffic | reaches     | a      | data-path |
mentsoftheslice.
|     |     |     |     |     |     | point that | has | been programmed |     | to  | satisfy | the slice |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --------------- | --- | --- | ------- | --------- |
• InService:Theslicehasbeensuccessfullyinstantiated specific requirements. When a packet arrives at the
withinthedataplaneanditisprocessingnetworktraffic.
|                |               |     |        |           |        | Flow Agent,      | it  | is deeply | inspected | to      | extract | data from  |
| -------------- | ------------- | --- | ------ | --------- | ------ | ---------------- | --- | --------- | --------- | ------- | ------- | ---------- |
| In this state, | the framework |     | offers | a dynamic | change |                  |     |           |           |         |         |            |
|                |               |     |        |           |        | the encapsulated |     | inner     | headers   | (17 and | 18).    | This data, |
of the QoS parameters of the slice on request. This namedflowkey,includes,amongotherdetails,informa-
allowsthenetworktoadapttothecontinuouslyevolving
tionabouttheverticalID,thesourceIoTdeviceandthe
scenariosexpectedin5GIoTusecases. destination IoT service, which is essential to provide a
| • Termination: | Decommissioning |     | of  | the network | slice |     |     |     |     |     |     |     |
| -------------- | --------------- | --- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
fine-grainedslicecontrol.Theflowkeyisthencompared
| and releasing | of the | network | resources | attached | to the |          |                  |     |            |       |     |          |
| ------------- | ------ | ------- | --------- | -------- | ------ | -------- | ---------------- | --- | ---------- | ----- | --- | -------- |
|               |        |         |           |          |        | with the | slice definition |     | and action | table | (19 | and 20). |
networkslice. If the search is successful, the packet is forwarded to
ThesequencediagramprovidedinFig.7detailsthelogical
|     |     |     |     |     |     | the assigned | slice, | i.e., | to the | htb queuing |     | discipline |
| --- | --- | --- | --- | --- | --- | ------------ | ------ | ----- | ------ | ----------- | --- | ---------- |
steps involved in the process of creating a network slice, responsible for enforcing the QoS requirements of the
| and how different | components | of  | the architecture |     | cooperate |     |     |     |     |     |     |     |
| ----------------- | ---------- | --- | ---------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
slice(21and22).Ontheotherhand,iftheflowkeydoes
| to finally ensure | the overall | QoS | of the | data | plane for a |     |     |     |     |     |     |     |
| ----------------- | ----------- | --- | ------ | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
notmatchanydefinedslice,adefaultpolicy(drop,sent
vertical service. As seen in Fig. 7, the sequence diagram is tomanagementplane,etc.)isapplied.
divided(horizontalgraylines)inthreedifferentstages:SCA
Theinteractionbetweenthedifferentarchitecturalcompo-
Instantiation,SliceCreation,andVerticalUseCase.Eachof
|     |     |     |     |     |     | nents to update | or delete | a   | slice instance |     | is very | similar to |
| --- | --- | --- | --- | --- | --- | --------------- | --------- | --- | -------------- | --- | ------- | ---------- |
thesestagescommenceswithanevent,producedeitherbythe
management layer or the involved vertical, which triggers a the one described in steps 6 to 15 of the sequence diagram
inFig.7andtherefore,forsimplicity,nosequencediagramis
sequenceofautomatedsteps.
included.Themajordifferenceliesinthefactthat,toupdate
• SCAInstantiation(Steps1-5):
ordeleteasliceinstance,theSCAdoesnothavetoprocessa
First,aftertheinfrastructuremanagementhastriggered
|                   |             |        |            |          |          | large and complex |     | intend-based | message   |          | (steps     | 8 and 9 in |
| ----------------- | ----------- | ------ | ---------- | -------- | -------- | ----------------- | --- | ------------ | --------- | -------- | ---------- | ---------- |
| a new SCA         | deployment, | the    | SCA-Core   | requests | for a    |                   |     |              |           |          |            |            |
|                   |             |        |            |          |          | Fig. 7). Instead, | the | SCA          | delegates | the      | task to    | the Flow   |
| list of available | Flow        | Agents | (1). After | that,    | the DPAS |                   |     |              |           |          |            |            |
|                   |             |        |            |          |          | Agent by passing  | the | slice        | ID that   | uniquely | identifies | the        |
moduleprovidessuchalistofFlowAgents,theircapa-
slicethroughoutthedataplane.SubsectionVII-Cprovidesan
bilities,andtheirlocationsthroughouttheinfrastructure
|                  |              |     |       |                   |     | empirical analysis | of  | the response | time | to  | handle | a network |
| ---------------- | ------------ | --- | ----- | ----------------- | --- | ------------------ | --- | ------------ | ---- | --- | ------ | --------- |
| (2, 3). Finally, | the SCA-Core |     | sends | this information, |     |                    |     |              |      |     |        |           |
sliceinstanceinanyofitsstates.
| through                     | its North Bound | API        | (4), | to the      | external |                                          |     |     |     |     |     |     |
| --------------------------- | --------------- | ---------- | ---- | ----------- | -------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| agent (5)                   | so that the     | next stage | can  | take place, | which    |                                          |     |     |     |     |     |     |
| istheslicecreation.         |                 |            |      |             |          | F. ALIGNMENTANDINTEGRATIONWITH5GINDUSTRY |     |     |     |     |     |     |
| • SliceCreation(Steps6-15): |                 |            |      |             |          | STANDARDSANDSPECIFICATIONS               |     |     |     |     |     |     |
This stage starts when an external policy enforcer Toconcludethissection,itworthtohighlightthatthesolution
defines a new slice and sends an intent-based mes- proposedinthisworkisfullycompliantandalignedwithdif-
sage for it to be enforced (6, 7). Next, the SCA-Core ferentstandardsandspecificationsdevelopedby5Gindustry
processes the message (8) and delegates to the andSDOs.Mostoftheeffortsmadeby3GPPareaimedatthe
Data Plane Abstraction Service (9) the task of build- designofaglobalstandardforthe5GNewRadio(5GNR),
ing a technology-dependant message (10). At this the air interface of 5G networks [33]. In this regard, our
point, the DPAS module selects a specific technol- solutionisdeployedintheedgeandcoresegmentsofthe5G
ogy depending on the Flow Agent that is specified network providing slicing capabilities across such network
in the intent-based message, which in this example segments. Thus, it is complementary to 3GPP achieving an
is OpenSliceVS (see Listing 1). In (11), a tailored UEs end-to-end network slicing service. In relation to the
| VOLUME9,2021 |     |     |     |     |     |     |     |     |     |     |     | 14057 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
FIGURE7. Sequencediagramdescribingtheslicecreationprocessandshowinginteractionbetweentheactorsinvolved:verticals,
managementplane,theSCAandtheFlowAgentinthesoftwaredatapath(OpenSliceVS).
5GarchitectureproposedbyETSIwhichisorientedtowards
orchestrationandvirtualizationaspects[34],ourSCAmodule
describedabovematchesthefunctionaldescriptionrequired
forthecomponentnamedNetworkSliceSelectionFunction
(NSSF)intheETSIspecification.Themainfunctionalityof
theNSSFistheselectionofDataPlanenetworkslices,which
arecreatedandconfiguredwithtailoredQoSthatfulfilsthe
requirementsofnetworkusers[35].
V. VERTICAL-ORIENTEDIoTUSECASESFOR
BENCHMARKING
| To validate | and demonstrate      | the suitability | of the proposed |     |     |     |     |
| ----------- | -------------------- | --------------- | --------------- | --- | --- | --- | --- |
| framework,  | this paper considers | five realistic  | IoT use cases   |     |     |     |     |
FIGURE8. ITUcategoryforeveryverticalorientedIoTusecasesfor
thatallowtoevaluatethesystem’sperformanceinscenarios evaluationtestbed.
wheredifferentverticalsposediverserequirementsinterms
| of latency, | data rate, reliability | and scalability | (number of |     |     |     |     |
| ----------- | ---------------------- | --------------- | ---------- | --- | --- | --- | --- |
IoT devices and number of slices). The characteristics and • mMTC:ItsupportsalargenumberofIoTdevicescon-
nectedtothesamecell,intermittentlyactiveandsending
requirementsoftheseusecasesarelistedinTable1.AsFig.8
illustrates, these use cases have been carefully chosen to traffic with small payload at a low uplink transmission
| coverthethreegeneralcategoriesofservicesdefinedbyITU: |     |     |     | rate.  |                     |              |           |
| ----------------------------------------------------- | --- | --- | --- | ------ | ------------------- | ------------ | --------- |
|                                                       |     |     |     | URLLC: | It supports traffic | that demands | very high |
| eMBB,mMTCandURLLC[36],[37].                           |     |     |     | •      |                     |              |           |
A brief overview of these three categories of services for reliability and low latency as main requirements, with
5GIoTusecasescanbegivenasfollows: arelativelylowtransmissionrateofsmallpayloads.
• eMBB:Itsupportsenhanced4Gbroadbandtrafficchar-
acterized by large payloads, moderate reliability and A. OVERVIEWOFTHEVERTICAL-ORIENTEDIoTUSE
| highdatatransmissionrates.AmoderatenumberofIoT |     |     |     | CASES |     |     |     |
| ---------------------------------------------- | --- | --- | --- | ----- | --- | --- | --- |
devices are connected to the same base station (BS) Below we provide a description of every use case from a
demandingstablecommunicationovertime. vertical point of view, underlining the QoS requirements
| 14058 |     |     |     |     |     |     | VOLUME9,2021 |
| ----- | --- | --- | --- | --- | --- | --- | ------------ |

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
TABLE1. Verticalorientedusecases:characteristics,KPIsandtrafficprofile.
demandedbyverticalsinreal-worldoperationsandthetraffic automation of complex operations such as control and
profiles generated by the IoT devices, which are then emu- monitoring of the manufacturing process, resource and
latedinourtestbed: assetmanagementorpredictivemaintenance.Asystem
• Use case 1 (Ambient Monitoring in Smart malfunction can have a negative impact on the overall
Agriculture): Smart agriculture aims to provide crop network and therefore low latency and high reliability
development optimization by means of environmental arecrucialQoSrequirementsinthisscenario.SuchQoS
monitoring services. It provides farmers with timely requisitesarecharacteristicofuRLLCusecases.Inthis
information for better management and exploitation of use case, 100 smart factories are simultaneously con-
their agricultural facilities, leading to maximized pro- nected to the 5G IoT network. An infrastructure made
ductivity. Each vertical deploys a large number of IoT up of 2000 IoT devices (sensors and robots) has been
sensors in their farms to perform real-time monitoring deployed in every manufacturing plant whereby each
and gather a range of climatic metrics such as relative IoTdevicesendstrafficatamoderateconstantthrough-
humidity, air temperature, soil temperature, light, soil putof11.5Kbps.
moisture,windorraindetection,tomentionofew[38]. • Usecase3(SoundAnalysisinSmartcity):Theadop-
The traffic profile is typically packets with small pay- tionofIoTinurbanenvironmentalacousticshelpspro-
load sent every few seconds where requirements in vide solutions for use cases such as noise control at
termsofreliability,latencyandthroughputarenotabig publicevents(concerts,festivals,...),detectionofsound
concern.SinceitisamMTCusecase,oneofthemajor patternsforcrimeprevention(shots,screams,breaking
challengesistoprovideconnectivityforahugenumber glasses),trafficstatusmonitoringoraudiosurveillance
of low-power wide-area (LPWA) IoT devices sending by using keyword spotting. The information extracted
traffic intermittently. The proposed 5G IoT framework fromsounddatagatheredbythecity-wideacousticIoT
hasbeentestedinprovidingservicetoupto1000farms network is further analyzed by speech recognition and
(verticals) where each farm deploys up to 1000 IoT sound analysis algorithms [40]. Local authorities can
sensors.Therefore,the5GIoTnetworkprocessestraffic benefitfromthisinformationandimprovethequalityof
from up to 1 million IoT sensors simultaneously con- life of citizens in a efficient and cost-effective fashion.
nected. The scenario for testing the proposed framework con-
• Usecase2(RobotControlinIndustrialAutomation): sistsof24cities,i.e.verticals.Foreveryvertical,anIoT
In Industrial Internet of Things (IIoT), often referred infrastructurecomprising3000soundsensorshasbeen
toasindustry4.0,robotautomationprocessesareused deployedthroughoutthecity,sendingreal-timeambient
to automate highly repetitive routine tasks tradition- sound to the application servers located on the edge of
allyperformedbyhumans.Suchtasksarenowaccom- the 5G network. The sound is encoded in MP3 quality
plished with high accuracy by robots in a faster and at a bitrate of 192 kbps and sent in 1500 byte pack-
more efficient manner, eliminating errors introduced ets. The traffic profile of this use case fits in a hybrid
by human factors. This leads to a productivity boost mMTC/eMBBservice.
and cost savings in time and money [39]. To test the • Use case 4 (Video Surveillance in Smart Building):
proposed framework, we consider a smart manufactur- Video surveillance in smart building combined with
ing scenario where every vertical is defined as a smart videoanalyticssolutionsisabletoserveawiderangeof
factory using sensors and robots for material handling applicationssuchascrowdcontrol,visitormanagement,
(picking and packing) and assembly tasks. NFV-based lighting and HVAC control for efficient energy con-
serviceslocatedattheedgeofthe5Gnetworkenablethe sumptionorsafetyandfireprevention.Traditionalvideo
VOLUME9,2021 14059

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
cameras are replaced by IP devices that send data-rich encapsulationresultsinthenetworkdealingwithlargerpack-
video to application servers that analyze the data and ets than the ones originally sent by the IoT devices. As a
triggertheappropriateactions.Inthisusecase,IPvideo consequence, there is an overhead in the overall bandwidth
camerassendfullHD1080pH.264encodedvideowith that the 5G infrastructure has to process. The encapsulation
astandardframerate(30fps),whichmeansaconstant processmodifiesthenetworkpacketsbyaddingnewheaders
video bitrate of 5 Mbps per IoT device (recommended at the beginning of the packets. The structure and size of
configurations for video bitrate and resolution settings these new headers are constant regardless of the size of the
in[41]).Thebuildingsplaytheroleofverticalsandthe packetsinitiallysentbytheIoTdevices.Hence,thesmaller
proposed5GIoTarchitectureprovidesconnectivityfor the packet size, the higher the proportional impact of the
up to 40 buildings with up to 100 cameras deployed doubleencapsulationontheoverallbandwidthandnetwork
in each building. The traffic pattern corresponds to a resourcesneededtocopewiththeverticals’demands.Inthe
moderate amount of devices forwarding large payload experimentscarriedoutinourtestbed,VXLANandGTPare
packetsatamoderaterate,whichiseMBBtraffic. theprotocolsemployedtoperformthedoubleencapsulation
• Use case 5 (AR-VR Tactile Application in Manu- and104extrabytesareaddedtoeverypacket(asaresultof
| facturing | Industry): |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
In a smart manufacturing con- inserting the sequence of headers MAC-IPv4-UDP-VXLAN-
text, augmented reality (AR) focuses on improving the MAC-IPv4-UDP-GTPatthebeginningofthepacket).
interaction between humans and machines by allowing It is noted that in Table 2 for use cases 1 and 2, which
humans to access digital information through a virtual send packets with small payloads, the impact of the double
layerontopofthephysicalworlddisplayedonvisual- encapsulationinthebandwidthissignificant:81%and40%
izationdevicessuchasmartglassesortablets[42].The respectively.Regardingtheremainingusecases(3,4and5),
applicationsarediverse:liveguidanceformaintenance, theincreaseintherequiredbandwidthislower,7.44%.Itis
training for assembly or warehouse operations among worthhighlightingthatallresultsgiveninthispaperreferto
manyothers.TheuseofARinindustrialenvironments doubleencapsulatedtrafficwithinthe5Ginfrastructure.
| involves  | real-time video | processing   | that        | demands  | high |     |     |     |
| --------- | --------------- | ------------ | ----------- | -------- | ---- | --- | --- | --- |
| bandwidth | as well as      | transmission | of critical | informa- |      |     |     |     |
TABLE2. Bandwidthoverheadduetodoubleencapsulationprocessin
tion about real-time industrial processes that imposes relationtotheoriginalpacketsizesentbytheIoTdevices.
extremerequirementsintermsofreliabilityandlatency.
| In our testbed,  | the 5G       | network   | provides      | coverage        | up                                      |     |     |     |
| ---------------- | ------------ | --------- | ------------- | --------------- | --------------------------------------- | --- | --- | --- |
| to 24 verticals, | i.e. 24      | smart     | manufacturing | factories.      |                                         |     |     |     |
| Each vertical    | is equipped  | with      | 20 AR         | units operating |                                         |     |     |     |
| simultaneously   | in its       | premises  | requiring     | a bandwidth     |                                         |     |     |     |
| of 40 Mbps       | per AR unit. | This      | is the most   | demanding       |                                         |     |     |     |
| of the five      | use cases,   | combining | URLLC         | and             | eMBB                                    |     |     |     |
| features.        |              |           |               |                 | C. PARAMETERSFORQoSREQUIREMENTSOFASLICE |     |     |     |
Inafirstsetofexperiments,insubsectionVII-A,everyuse INTHETESTBED
casehasbeenempiricallyevaluatedseparatelytoprovidean In terms of performance, the needed parameters to set up a
individualizedanalysisofthescalabilityandperformanceof slice are three: Maximum allowed bandwidth (MAB), mini-
theproposedsolutionwhenprocessinghomogeneoustraffic mumguaranteedbandwidth(MGB)andpriority.TheMAB
matchingthetrafficprofileandQoSrequirementsdemanded and the MGB values determine respectively the upper and
bytheverticalsforaspecificusecase. lower boundaries within a vertical is allowed to send traffic
Nevertheless, IoT ecosystems are fragmented by nature according to its SLA. A traffic rate above the upper limit
in multiple verticals with diverse requirements and, as a would be a SLA violation by the vertical and it should not
consequence,heterogeneousservicesareexpectedtocoexist bepermittedbythecontrolandmanagementlayerunderany
simultaneouslyin5GIoTnetworkswithinthesamephysical circumstances. A traffic rate lower than the minimum limit
infrastructure. Therefore, once the performance boundaries mayindicateanunder-utilizationoftheprovisionedresources
of each specific use case are known, in a second set of and a revision of the network slices configuration would be
experiments,theproposed5GIoTframeworkhasbeeneval- usefultooptimizetheavailablenetworkresources.
uated under heterogeneous traffic in a more complex and For the experiments conducted in our testbed (see results
challengingscenario(seeresultsinsubsectionVII-B). in sections VII), the slices have been configured using the
|     |     |     |     |     | expected bandwidth | as a reference | value to determine | the |
| --- | --- | --- | --- | --- | ------------------ | -------------- | ------------------ | --- |
B. BANDWIDTHOVERHEADDUETODOUBLE MAB and the MGB parameters, assigning an interval of
ENCAPSULATIONIN5GIoTMULTI-TENANTNETWORKS ±25%oftheexpectedbandwidthtoeveryslice.Fig.9illus-
As mentioned in subsection IV-C, the double encapsulation tratesthiswithanexampleforusecase5.Forthisusecase,
of 5G- IoT network traffic is necessary to support tenant every single IoT device transmits at a constant data rate
isolation and IoT devices mobility in multi-tenant 5G IoT of39.6Mbps.Inthemorecomplexscenariowith24verticals
virtualized infrastructures. On the other hand, the double and 20 IoT devices per vertical, the expected bandwidth of
| 14060 |     |     |     |     |     |     | VOLUME9,2021 |     |
| ----- | --- | --- | --- | --- | --- | --- | ------------ | --- |

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
|     |     |     |     |     |     |     | A. HARDWAREANDSOFTWARESPECIFICATIONSFOR |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
TESTBED
Theexperimentshavebeencarriedoutonacomputerwiththe
|     |     |     |     |     |     |     | following | specifications: | 2-node | NUMA | architecture |     | where    |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | ------ | ---- | ------------ | --- | -------- |
|     |     |     |     |     |     |     | each node | was an Intel    | Xeon   | CPU  | E5-2660      | v4  | based on |
Broadwellarchitecturewith14coresoperatingat2GHzand
hyper-threadingfeatures.Thesystemhada128GByteRAM
anda2TerabyteSCSIHDD.TheoperatingsystemwasCen-
tOSrelease7.8.2003runningaLinuxkernelversion3.10.0.
|     |     |     |     |     |     |     | Regarding    | the virtualisation |       | software,       | the | hypervisor | was     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------ | ----- | --------------- | --- | ---------- | ------- |
|     |     |     |     |     |     |     | qemu version | 1.5.3              | using | libvirt version |     | 4.5.0.     | The CPU |
providesaconstantTimeStampCounter(TSC)thatallows,
|     |     |     |     |     |     |     | using the      | virtual Precision |       | Time Protocol |        | (PTP)           | hardware |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----------------- | ----- | ------------- | ------ | --------------- | -------- |
|     |     |     |     |     |     |     | clock provided | by the            | Linux | kernel,       | a time | synchronization |          |
betweenthehostandtheguestswithasub-microsecondaccu-
racy.1Thisisneededtogetaccuratetimestampingofnetwork
trafficinvirtualizedenvironmentslikeourtestbedinfrastruc-
|     |     |     |     |     |     |     | ture where | events such | as  | interruptions, | process |     | migrations |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | -------------- | ------- | --- | ---------- |
ordeepCstatescouldleadtoissuesoftimekeepinginguest
VMs.Therefore,theempiricalresultsachievedinthispaper
FIGURE9. Maximumallowedbandwidth(MAB)andminimum are accurate and trustworthy with an error of the order of
guaranteedbandwidth(MGB)forusecase5inascenariowith24smart
nanoseconds.
manufacturingfactories(slices)with20ARunitsperfactory.
|     |     |     |     |     |     |     | B. METHODOLOGYTOEXECUTEEXPERIMENTSAND |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
everyverticalis792Mbps.Theaccumulatedexpectedband-
ANALYZERESULTS
width,i.e.,thesumofthebandwidthofallslicesthatthe5G Concerning the procedure followed to gather results, all the
| IoT infrastructure |     | must handle, | is 19 Gbps. | Thus, | the | MAB |     |     |     |     |     |     |     |
| ------------------ | --- | ------------ | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
experimentshavebeenreproducedfortentimes.Theresults
and MGB for every single slice are 990 and 594 Mbps in the best one and the worst one have been discarded to
respectively (792 Mbps ±25%). Similarly, the accumulated preventoutliersand,therefore,theresults(delay,packetloss,
| values of | MAB and | MGB | are 23.75 Gbps | and | 14.75 | Gbps |     |     |     |     |     |     |     |
| --------- | ------- | --- | -------------- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
bandwidth,etc.)showninthisworkarethearithmeticmean
respectively(19Gbps±25%). oftheeightremainingintermediatevalues.Foreverysingle
Regardingpriority,thisparameteristightlylinkedtoreli-
experiment,networktraffichesbeensentforatleast30sec-
ability and latency. On every interface, the traffic scheduler onds, mapping the use case traffic profile, the amount of
prioritizes higher priority traffic over lower priority traffic. IoT devices connected and the number of verticals. Based
| Consequently, | packets | with | higher priority | are | queued | for |     |     |     |     |     |     |     |
| ------------- | ------- | ---- | --------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
onprevioustestcarriedout,30secondsisareasonabletime
a shorter time and are forwarded before packets with lower intervaltoproducetrustworthyandaccurateresults.
priority.Thedirectimplicationsonhighprioritytrafficwhen
compared with lower priority traffic are higher reliability C. TESTBEDINFRASTRUCTUREANDIMPLEMENTATION
| (a packet | is less likely | to  | be dropped | due to | a full | queue) | DETAILS |     |     |     |     |     |     |
| --------- | -------------- | --- | ---------- | ------ | ------ | ------ | ------- | --- | --- | --- | --- | --- | --- |
andlowerdelay(duetolowerqueuingdelay).Itisnotedthat
Fig.10illustratesthetestbeddeployedtocarryouttheempir-
prioritiesaresetdifferentlydependingonwhetherthetraffic icalvalidationandevaluationofthe5GIoTnetworkslicing
| is homogeneous | or  | heterogeneous. | In  | the experiments |     | con- |     |     |     |     |     |     |     |
| -------------- | --- | -------------- | --- | --------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
capabilitiesofthenovelproposedframework.Thisfigurealso
ductedwithhomogeneoustrafficinsubsectionVII-A,since
showsthesoftwareartefactsinthetestbedandtheworkflow
allnetworktrafficcorrespondstothesameITUcategory,all toconducteachsingleexperiment,startingwhenthevertical
sliceshavebeensetwiththesamepriorityand,hence,equally
requestssubscriptiontoanetworkserviceuntilthedatagath-
treated.Regardingtheexperimentswithheterogeneoustraf- eredduringtheexperimentareanalyzedtoobtainempirical
| fic, the priority | of              | every slice | has been | set according |         | to the |           |             |                |          |             |          |            |
| ----------------- | --------------- | ----------- | -------- | ------------- | ------- | ------ | --------- | ----------- | -------------- | -------- | ----------- | -------- | ---------- |
|                   |                 |             |          |               |         |        | results.  | The testbed | infrastructure | consists |             | of three | virtual    |
| latency           | and reliability | requisites  | demanded | by            | the use | case   |           |             |                |          |             |          |            |
|                   |                 |             |          |               |         |        | machines. | The first   | VM (VM1)       | is       | responsible |          | for a cen- |
(seesubsectionVII-B). tralized management of the infrastructure, and thus accom-
|     |     |     |     |     |     |     | modates | the control | and | management | modules |     | described |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | ---------- | ------- | --- | --------- |
VI. IMPLEMENTATIONDETAILSANDTESTBEDFOR in subsection III-C3 and the SDN controller. VM2 and
EXPERIMENTATION
|     |     |     |     |     |     |     | VM3 virtual | machines | host | NF-based | virtualized |     | services |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ---- | -------- | ----------- | --- | -------- |
Thissectionprovidesdetailsaboutthetestbedinfrastructure
1KVMguesttimingmanagement:https://access.redhat.com/
deployedtoempiricallyvalidateandevaluatetheframework
documentation/en-us/red_hat_enterprise_linux/7/
proposed,andthemethodologyadoptedtoexecutetheexper-
html/virtualization_deployment_and_administration_
imentsandanalyzethegatheredresults. guide/chap-kvm_guest_timing_management
| VOLUME9,2021 |     |     |     |     |     |     |     |     |     |     |     |     | 14061 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
FIGURE10. Architecture,artifactsandworkflowofthetestbeddeployedfortheempiricalevaluationofourproposed5GIoTSliceManagement
Framework.
that send and receive 5G IoT traffic respectively. Connec- number of IoT devices, transmission bandwidth per device,
tivitybetweenVM2andVM3isprovidedbyaninstanceof payloadsize,etc.)(see5inFig.10).TheNFserviceallocated
OpenSliceVS, the Flow Agent tasked with provisioning and inVM2generatesnetworktrafficmatchingthispattern.This
enforcing slicing policies in the software data path segment trafficissenttotheOpenSliceVSinstancewheretheslicing
ofthedataplane.Therefore,theresultsachievedinthiswork is performed and the packets are forwarded to the IoT NF
correspond to an Edge-to-cloud network slicing preformed service allocated in VM3 (steps 6 and 7 in Fig. 10). Every
between VM2 and VM3. The communication between the single packet is uniquely tagged along the experiment by a
SliceManagementsuitelocatedinVM1andtheOpenSliceVS unique8-byteIDanditsassociatedsliceID,bothincludedin
instance is ensured in a technology-independent way by an thepayload.Oncethetransmissionhasbeenconducted,both
SCAinstanceasdescribedinsubsectionIV-A. IoTservices,senderandreceiver,generateaPCAPfilethatis
TheexperimentsareconductedbytheAutomatedScenario reportedtotheASDS(8and9inFig.10).Finally,theASDS
Deployment Script (ASDS). This tool has been developed agent compares the data of both PCAP files (timestamp,
to evaluate in an automated manner the performance of the packet ID and associated slice ID) to obtain the empirical
proposed 5G IoT Network Slicing framework in different resultsoftheexperiment.
scenarios. It is able to execute large batches of experiments
whose parameters have been previously defined in a JSON VII. EMPIRICALVALIDATION,EVALUATIONAND
file. The workflow to conduct an experiment is as follows: ACHIEVEDRESULTS
Afterreadingtheexperimentconfiguration(see1inFig.10), In this section, we first provide an empirical evaluation
the ASDS agent assumes the role of the verticals and sends and analysis of the scalability of the achieved performance
a request to the Slice Management Framework about the in terms of delivered QoS (latency, packet loss and band-
SLAscorrespondingtoeveryverticalinvolvedintheongoing width)whendealingwithhomogeneous5GIoTtraffic.Next,
experiment (see 2 in Fig. 10). Then, the Slice Management the proposed framework is evaluated in a more demanding
Framework enforces the slicing policies derived from the scenario with heterogeneous 5G IoT traffic where we focus
SLAs subscribed by the vertical and provisions the needed onresultsaboutpriorityQoSrequirementsandperformance
resources to ensure the demanded network slicing service. isolationbetweenslices.Finally,weprovideresultsaboutthe
UsingtheDataPlaneAbstractionService(DPAS)provided flexibility and agility of the system when managing the life
by the SCA, the slices are created in the data plane by the cycle of a slice (provisioning, modification and decommis-
softwaredatapathFlowAgent(OpenSliceVS)(see3and4in sioningofaslice).
Fig. 10). At this point, the 5G infrastructure is aware of the
verticals’requirements,andthenecessaryhardwareandsoft- A. HOMOGENEOUSSCALABILITYOF5GIoTNETWORK
wareresourcestomeetthemhavebeenprovisioned.Hence, SLICING
the verticals’ IoT devices can start to send network traffic This subsection provides an empirical analysis of the pro-
tothevirtualizedIoTservicesallocatedintheserversofthe posed framework suitability when processing homogeneous
5Gnetwork.Next,theASDSagentsendstotheIoTservice 5GIoTtraffic,i.e.,networktrafficfromonlyoneoftheuse
in VM2 the traffic profile of the experiment (including the casesintroducedinSectionV.Sinceallnetworktrafficisof
14062 VOLUME9,2021

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
FIGURE11. Scalabilityresultswhenprocessinghomogeneous5GIoTtraffic(averageend-to-enddelayperpacketinµs).Foreachusecase,
theframeworkhasbeenevaluatedrangingthenumberofslices(verticals)andthenumberofIoTdevicesperslice.Itisgiventhemaximumnumberof
IoTdevicesperslice,packetspersecond(PPS)transmittedandaccumulatedTxbandwidthconfiguredforeachusecase.
TABLE3. Averagedelayperpacketforthemoststressfulconfiguration theaveragedelayisintheorderofµswhileforsomeofthe
foreveryusecase.
mostdemandingscenariositisslightlyover1ms.Packetloss
ratiois0%foralltheexecutedscenariosinalltheusecases,
andthusnographisprovidedregardingpacketloss.
|     |     |     |     | In use     | case 1 (mMTC   | traffic), the maximum | measured         |
| --- | --- | --- | --- | ---------- | -------------- | --------------------- | ---------------- |
|     |     |     |     | delay is   | 143 µs when    | handling the emulated | traffic from     |
|     |     |     |     | 1000 smart | farms equipped | with 1000 IoT         | climate sensors. |
Therefore,theproposedframeworkisabletocopewithone
|     |     |     |     | million mMTC | IoT devices    | with 0% packet           | loss and yield |
| --- | --- | --- | --- | ------------ | -------------- | ------------------------ | -------------- |
|     |     |     |     | very low     | latency. These | values are significantly | lower than     |
therequirementsspecifiedforthistypeoftrafficinTable1.
Concerningusecase2,sinceitinvolvesuRLLCtraffic,high
thesametype,allslicesareconfiguredwiththesamepriority
and thus, equally treated with a round robin policy by the reliabilityandlowlatencyarestrictrequirementsthatmustbe
queuingscheduler. fulfilled.Theoutcomeoftheexperimentscarriedoutonour
Fig.11showsthesystemperformanceintermsoflatency testbedprovesthattheproposedsolutionisabletocopewith
(averagedelayperpacket)whenrangingthenumberofver- bothsuccessfully:lowlatency(133µsfortheworstcase)and
highreliability(0%packetloss).Unlikeusecases1and2,
| ticals and | the number of | IoT devices | per vertical for each |     |     |     |     |
| ---------- | ------------- | ----------- | --------------------- | --- | --- | --- | --- |
use case. As it can be observed in Table 3, the latency latency and reliability are not challenging requirements for
requirements listed in Table 1 are fulfilled for all the use usecases3and4.Notwithstanding,thegatheredresultsare
caseseveninthemoststressfulscenarios(configurationswith beyondtherequirementsimposedbytheverticals:maximum
the highest number of verticals and 5G IoT devices). It is average delay of around 1 ms (significantly less than the
100msspecifiedforbothusecases)and0%packetlosseven
| worth highlighting | that, for | the majority | of the scenarios, |     |     |     |       |
| ------------------ | --------- | ------------ | ----------------- | --- | --- | --- | ----- |
| VOLUME9,2021       |           |              |                   |     |     |     | 14063 |

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
FIGURE12. AccumulatedRxBandwidth(inGbps)whenprocessinghomogeneous5GIoTtrafficandsafesliceboundariesforeachusecase.Itisgiventhe
maximumnumberofIoTdevicesperslice,packetspersecond(PPS)transmittedandaccumulatedTxbandwidthconfiguredforeachusecase.
though both use cases are tolerant to packet loss. Finally, bluedottedlinesthatdelimitthisareadeterminethevaluesof
usecase5istheonethatdemandsmoresevererequirements theMABandtheMGBasdescribedinsubsectionV-C.The
sinceitstrafficprofilecorrespondstoahybriduRLLC/eMBB orangedottedlineinthecentreistheaccumulatedexpected
category.Aswiththeprevioususecasesdiscussed,thepro- bandwidth used as a reference to calculate the bandwidth
posed 5G IoT framework is able to guarantee the require- limitsoftheslices.Consequently,notrafficshouldbeallowed
mentsimposedbytheverticalsoftheusecase5:lowlatency in the upper green area as it is a violation of the SLAs by
(delay lower than 1 ms in the most stressful configuration theverticals.Finally,theverticalscansendtrafficbellowthe
with 24 verticals and 20 AR units per verticals) and high MGB(thelowerblueareineverygraph),although,asmen-
reliability(0%packetloss)whilstbeingabletoprocessahigh tionedinsubsectionV-C,itindicatesanunder-utilizationof
bandwidthinherenttoeMBBtraffic. theprovisionedresourcesfortheslice.
Sofar,theperformanceachievedinrelationtolatencyand The results shown in Fig. 12 demonstrate that the infras-
reliabilityhasbeenanalyzed.Regardingbandwidthrequire- tructure is able to fulfill the bandwidth requirements for
ments, Fig. 12 shows the accumulated bandwidth achieved all the executed scenarios. In fact, for most configurations,
for every use case. For clarity and simplicity, the results theaccumulatedbandwidthmeasuredmatchesprettyclosely
showedforeveryusecasecorrespondstothescenarioswith the expected one. Only for the scenarios with the higher
the highest number of verticals (slices) when ranging the numberofIoTdevicesdeployedinusescases4an5,theaccu-
number of IoT devices connected to the 5G IoT network. mulatedbandwidthachievedisbellowtheexpectedone,but
Theresultsgatheredwithfewerverticalsaresimilaroreven stillwithintheguaranteedlimits.Sincetheframeworkisdeal-
better due to the fact that these are configurations where ingwithhomogeneoustrafficwherealltheverticals(slices)
the network is less congested. Three different areas can be demand the same requisites in terms of bandwidth, it is
observedineverygraph.Thecentralyellowareaindicatesthe expectedthatthe5GIoTnetworkwilltreatalltheverticalsin
bandwidthintervalforeveryslice.Theuppergreenandlower thesamemanner.Inafirstapproachtoillustratethissystem
14064 VOLUME9,2021

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
TABLE4. Testbedsetupforempiricalevaluationwithheterogeneous5GIoTtraffic.Usecasesorderedbypriority.
behaviour,weintendedtoplotthestandarddeviationofthe
| achieved | bandwidth | per | slice | with a | whisker | plot | on top of |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | ----- | ------ | ------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
eachbarinthebargraphsinFig.12.However,thestandard
deviationvaluescalculatedaresoclosetothearithmeticmean
| that, once  | plotted, | they | are imperceptible |     | in       | the bar   | graphs. |     |     |     |     |     |     |     |     |
| ----------- | -------- | ---- | ----------------- | --- | -------- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| In a second | approach |      | to assess         | the | system’s | behaviour | in      |     |     |     |     |     |     |     |     |
relationtothis,weprovidetheratio(inpercentage)between
thestandarddeviation(σ)oftheachievedbandwidthperslice
anditsarithmeticmean(µ)fortheworstexecutionofevery
| use case | (see annotations |       | in   | green boxes    | for | every  | use case |     |     |     |     |     |     |     |     |
| -------- | ---------------- | ----- | ---- | -------------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| in Fig.  | 12). This        | ratio | is a | good indicator |     | of how | equally  |     |     |     |     |     |     |     |     |
slicesaretreatedbythenetworkintermsonbandwidth.From
| a statistical | viewpoint, |     | 95% | of the values |     | for the | achieved |     |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | --- | ------------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
µ−2σ,µ+2σ
| bandwidth  | per         | slice are | in the        | interval | [        |         | ].  |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --------- | ------------- | -------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Therefore, | the smaller |           | this interval | is,      | the more | equally | the |     |     |     |     |     |     |     |     |
slicesaretreatedintermsofachievedbandwidth.Thehighest
valueofthisindicatoris0.13%(usecase3),whichindicates FIGURE13. Averagedelaypersliceandusecase(inµs)whenprocessing
a good stability and robustness of the system. Even in the heterogeneous5GIoTfrom280,920IoTdevicesand432slicesenforced
morecongestedscenarioswheretheaccumulatedbandwidth inthesoftwaredataplanebytheOpenSliceVSFlowAgent.
measuredisbelowtheexpectedone,theavailablebandwidth TABLE5. Exampleofproposedprioritiesmappingdifferent5GIoTtraffic
profiles.
| is distributed | almost | equally |     | among | all the | slices | with the |     |     |     |     |     |     |     |     |
| -------------- | ------ | ------- | --- | ----- | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
samepriorityandthroughoutrequisites(seeexecutionswith
highernumberofIoTdevicesinusecase4and5).
| To conclude         |              | this subsection, |           | the gathered |             | results | demon-   |     |     |     |     |     |     |     |     |
| ------------------- | ------------ | ---------------- | --------- | ------------ | ----------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| strate that         | the proposed |                  | framework | is           | able        | to meet | the ver- |     |     |     |     |     |     |     |     |
| ticals requirements |              | in               | terms     | of latency,  | reliability |         | (packet  |     |     |     |     |     |     |     |     |
| loss) and           | throughput   | when             | dealing   | with         | homogeneous |         | traf-    |     |     |     |     |     |     |     |     |
| fic where           | all slices   | match            | traffic   | with         | the same    | profile | and      |     |     |     |     |     |     |     |     |
| requirements.       | The          | proposed         |           | solution     | provides    | good    | scala-   |     |     |     |     |     |     |     |     |
| bility while        | being        | flexible         | enough    | to           | adapt       | to the  | diverse  |     |     |     |     |     |     |     |     |
requirementsoftheusecasesanalyzedinthiswork:itisable
|     |     |     |     |     |     |     |     | this scenario | is  | a realistic | example | of  | 5G IoT | traffic | which |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ------- | --- | ------ | ------- | ----- |
to provide connectivity for up to 1 million IoT devices in is expected in a real-world 5G IoT infrastructure. As it
mMTCtraffic,achieveover15Gbpsbandwidthincongested
|                   |     |                |     |           |     |           |        | can been | noticed, | the     | proposed   | framework |            | has been   | tested  |
| ----------------- | --- | -------------- | --- | --------- | --- | --------- | ------ | -------- | -------- | ------- | ---------- | --------- | ---------- | ---------- | ------- |
| eMBB scenarios    |     | or ensure      |     | delays in | the | order of  | µs for |          |          |         |            |           |            |            |         |
|                   |     |                |     |           |     |           |        | with 432 | slices   | sending | traffic    | from      | a total    | of 280,920 | IoT     |
| critical-missions |     | communications |     | (uRLLC),  |     | providing | high   |          |          |         |            |           |            |            |         |
|                   |     |                |     |           |     |           |        | devices. | In terms | of      | bandwidth, | the       | 5G network |            | handles |
reliabilityinallofthetestedscenarios(0%packetlossratio).
|     |     |     |     |     |     |     |     | 1,404,000 | packets | per        | second  | (PPS), | reaching | a combined |          |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---------- | ------- | ------ | -------- | ---------- | -------- |
|     |     |     |     |     |     |     |     | bandwidth | of      | 13.83 Gbps | whereas | it     | has to   | ensure     | the ver- |
B. HETEROGENEOUSSCALABILITYOF5GIoTNETWORK ticals’QoSrequirementscommittedintheSLAs.
SLICING Unlike the previous experiments with homogeneous traf-
The prototyped 5G IoT framework has also been evalu- fic, priority is a key QoS parameter when dealing with het-
ated in a more challenging scenario where traffic from the erogeneous5GIoTtrafficinamorecomplexscenariowhere
5 use cases demanding diverse QoS requirements is com- it is required to guarantee delay-sensitive and high-reliable
peting simultaneously for the available network resources. services.Incongestednetworkswithhightrafficload,pack-
Table 4 provides a breakdown of the heterogeneous traffic ets are buffered before being forwarded, causing an addi-
profile of the experiments conducted. The configuration of tional delay. Moreover, if the buffer becomes full, packets
| VOLUME9,2021 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 14065 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
FIGURE14. Averagebandwidthpersliceforeachusecaseinascenariowithheterogeneous5GIoTtraffic.Themeasuredresultscorrespondtoa
10-secondintervalwhere5Gnetworktrafficissimultaneouslysentfor5vertical-orientedusecases.Thecombinedtotalbandwidthachievedis
12.36Gbps.
are dropped. This fact might compromise the fulfillment of Fig. 13 displays the average delay per slice for every use
theQoSparametersspecifiedintheSLAintermsoflatency case when the 5G infrastructure processes traffic from all
and reliability. Prioritization mechanisms address this issue 5usecasessimultaneously.Thedatacorrespondtonetwork
by forwarding high priority traffic (demanding low latency traffic captured for 10 seconds in the testbed. There are
and/orhighreliability)beforeothertrafficwithlessstrictQoS severalconclusionsthatcanbedrawnfromthisgraph.Firstly,
needs.Table5providesaproposalonassigningprioritiesto an average delay below 1 ms is achieved for all slices. Sec-
differenttypesof5Gnetworktraffic.Thesevalueshavebeen ondly,asexpected,thetraffictransmittedbytheIoTdevices
usedtosetthepriorityforthetrafficofeachverticalbusiness of the use case with the highest priority (URLLC category)
in the experiments carried out in the testbed (see the fifth getstheshortestdelay(around200µs).Furthermore,itcan
columninTable4). beenobservedthattheslicesofusecaseswithhigherpriority
14066 VOLUME9,2021

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
(2and5)obtainaratherstabledelayincomparisonwiththe
remainingusecases(thewhiskerbox’sheightislower).This
fact suggests that the 5G network is honoring the priority
parameterspecifiedwhentheseslices,withmoresevereQoS
requirements, were enforced in the data plane. As a con-
sequence, their traffic is treated with higher priority by the
the Flow Agent, leading in a better delay performance and
stability.Toconcludetheanalysisoffig.13,itcanbenoticed
thatthedelayintervalofthesliceswithlesspriority(usecase
1 with mMTC traffic profile) is larger than the rest of the
use cases. This interval measures the stability of the delay
along the time (jitter). Results indicate that lowest priority
trafficisbufferedlongerandforwardedwithamoreirregular
patterndependingonthenetworkcongestion.Itdependson
howothersliceswithhigherpriorityareconsumingnetwork
FIGURE15. Empiricalanalysisofthescalabilityofthetimerequiredby
resources.Intheworstcasescenario,thejittervariesroughly theResourceControlplanetocreateanetworkslice(processthe
250 µs (between 650 and 900 µs) for use case 1 which intend-basedmessageandprovisionthenecessarynetworkresources).
is a more than acceptable value for this kind of use cases.
Concerning reliability, as with the experiments conducted the Resource Control plane (see Fig. 3), i.e., since the NBI
withhomogeneoustraffic,thepacketlossratioisalso0%for oftheSCAreceivesanintend-basedmessagefromtheSDN
allusecasessonographisprovidedinthisregard. controlleruntiltheslicehasbeensuccessfullyenforcedinthe
Fig.14depictsthesystembehaviourintermsofbandwidth dataplaneandanACKmessageissentbacktothemanage-
whendealingwith5GIoTnetworktraffictransmittedsimul- mentplane.Thisprocesscorrespondstosteps6to13ofthe
taneouslyfromIoTdevicesofthe5differentusecases.The sequencediagraminFig.7asdiscussedinsubsectionIV-E.
results correspond to a 10-second interval where the aver- Three architectural components are involved in this task:
age bandwidth per slice has been computed at 0.25 second the SCA core, the DPAS module and the Flow Agent
intervals. It can be observed that, for all use cases, the pro- (OpenSliceVS). It can be observed that the major workload
posed framework is able to deliver a guaranteed bandwidth reliesupontheFlowAgent.TheFlowAgentisresponsiblefor
service within the boundaries agreed in the SLAs between theinsertionoftheOpenFlowrulematchingtheslicetrafficin
the verticals and the service provider. Regarding the num- the slice definition and action table (the orange stacked bar
ber of packets, the 5G infrastructure has managed around in Fig. 15) and setting up the htb queuing discipline where
1,2500,000 packets for this experiment while the average theslicetrafficwillbeforwardedandtheQoSrequirements
overallbandwidthobtainedis12.36Gbps. will be enforced (the green stacked bar in Fig. 15). Mean-
Therefore, it can be concluded that the proposed 5G while, the time required by the SCA module to process the
IoT framework has been empirically validated against a intend-based message has less impact on the overall time
large-scaleinfrastructure.Itissuitabletodelivernetworking spenttocreateaslice(thebluestackedbarinFig.15).
slicingforIoTserviceswithguaranteedQoSrequirementsin Thegatheredresultsindicatethattheproposedframework
5G networks dealing with simultaneous and heterogeneous needs 1463 ms to create 256 slices, resulting in an average
traffic. The framework has shown very promising results in timeofonly5.7msperslice.Similarexperimentshavebeen
termsofthenumberofslicessupported,andintermsofthe carriedouttoevaluatethetimetodeleteandmodifynetwork
bandwidth,delay,jitterandpacketlossabletobewarrantied slices,obtainingbetterresultsthanthosewhencreatingnew
inthe5Ginfrastructure. network slices (an average overall time of 21% lower). For
the sake of brevity, these results are not shown. To delete
C. PERFORMANCEEVALUATIONOFADAPTIVESLICE or modify a network slice, the SCA core does not have to
MANAGEMENT processafullintend-basedmessage,insteaditjustdelegates
Since 5G IoT networks are dynamic ecosystems subject to to the Flow Agent the required action based on the slice ID
continuous changes, one of the most challenging features reported by the external policy enforcer of the management
that a 5G IoT slice control framework must address is the plane, which is faster. Similarly, regarding the Flow Agent
flexibilitytoadapttosuchcomplexscenarios.Thisimpliesa side, releasing network resources or modifying previously
quickresponseinmanagingnetworkslicesandprovisioning provisioned network resources is quicker than provisioning
theappropriatenetworkresourcesneededtoenforcetheslices themfromscratch.
inthedataplaneandmeetthediverserequirementsdemanded Hence,theseresultsprovethattheproposed5GIoTframe-
byverticals.Fig.15providesabreakdownofthetimespent work is able to adapt on demand to evolving IoT traffic,
by the proposed framework in creating different number of adding, modifying or decommissioning in an efficient way
sliceswhenrangingexponentiallythenumberofslicesfrom (justafewmilliseconds)theslicingpoliciesimposedbythe
2 to 256. The given results refer to the time consumed in uppercognitivemanagementlayers.
VOLUME9,2021 14067

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
VIII. CONCLUSION [7] E.Kapassa,M.Touloupou,P.Stavrianos,andD.Kyriazis,‘‘Dynamic5G
This paper has presented a highly scalable and effective slicesforIoTapplicationswithdiverserequirements,’’inProc.5thInt.
Conf.InternetThings:Syst.,Manage.Secur.,Oct.2018,pp.195–199.
| network              | slicing | framework  | for | 5G IoT    | networks, |         | following |                |                |                      |             |                         |             |
| -------------------- | ------- | ---------- | --- | --------- | --------- | ------- | --------- | -------------- | -------------- | -------------------- | ----------- | ----------------------- | ----------- |
|                      |         |            |     |           |           |         |           | [8] J. Ni,     | X. Lin, and X. | S. Shen, ‘‘Efficient | and         | secure service-oriented |             |
| the software-defined |         | networking |     | approach. |           | All the | specific  |                |                |                      |             |                         |             |
|                      |         |            |     |           |           |         |           | authentication | supporting     | network              | slicing for | 5G-enabled              | IoT,’’ IEEE |
J.Sel.AreasCommun.,vol.36,no.3,pp.644–657,Mar.2018.
| requirements | to  | provide | network | slicing | capabilities |     | in 5G |     |     |     |     |     |     |
| ------------ | --- | ------- | ------- | ------- | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- |
[9] F.Kurtz,C.Bektas,N.Dorsch,andC.Wietfeld,‘‘Networkslicingforcrit-
| IoT infrastructures |     | identified |     | in subsection |     | III-A | are fully |     |     |     |     |     |     |
| ------------------- | --- | ---------- | --- | ------------- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- |
icalcommunicationsinshared5GInfrastructures—Anempiricalevalua-
| addressed | by our | solution. | It  | is capable | of  | supporting | key |     |     |     |     |     |     |
| --------- | ------ | --------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
tion,’’inProc.4thIEEEConf.Netw.Softw.Workshops(NetSoft),Jun.2018,
5Gfeaturesincludingnetworkfunctionvirtualization,multi- pp.262–266.
[10] R.Trivisonno,M.Condoluci,X.An,andT.Mahmoodi,‘‘MIoTslicefor
| tenancy, | and device | mobility. |     | It is particularly |     | designed | for |     |     |     |     |     |     |
| -------- | ---------- | --------- | --- | ------------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
5Gsystems:Designandperformanceevaluation,’’Sensors,vol.18,no.2,
massivemachine-typecommunicationsandisabletomanage p.635,Feb.2018.
thousandsofheterogeneousslicesconcurrently.Furthermore, [11] C.Bektas,S.Bocker,F.Kurtz,andC.Wietfeld,‘‘Reliablesoftware-defined
itsupportsother5Gusecasesthatrequireenhancedmobile RANnetworkslicingformission-critical5Gcommunicationnetworks,’’
inProc.IEEEGlobecomWorkshops(GCWkshps),Dec.2019,pp.1–6.
broadband,orultrareliableandlow-latencycommunications, [12] S.Costanzo,I.Fajjari,N.Aitsaadi,andR.Langar,‘‘Dynamicnetwork
oracombination.Five5GIoTusecasescoveringthesethree slicing for 5G IoT and eMBB services: A new design with prototype
andimplementationresults,’’inProc.3rdCloudificationInternetThings
| ITU use | case categories |     | individually |     | and | collectively | have |     |     |     |     |     |     |
| ------- | --------------- | --- | ------------ | --- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- |
(CIoT),Jul.2018,pp.1–7.
beenconsideredandtheirQoSrequirementswereabstracted [13] Y.Tsukamoto,R.K.Saha,S.Nanba,andK.Nishimura,‘‘Experimental
to inform a realistic emulation in a testbed, where the evaluation of RAN slicing architecture with flexibly located functional
|          |         |         |           |     |          |              |     | components | of base | station according | to diverse | 5G services,’’ | IEEE |
| -------- | ------- | ------- | --------- | --- | -------- | ------------ | --- | ---------- | ------- | ----------------- | ---------- | -------------- | ---- |
| proposed | network | slicing | framework |     | has been | successfully |     |            |         |                   |            |                |      |
Access,vol.7,pp.76470–76479,2019.
| tested and | evaluated. | Empirical |     | results | have | highlighted | the |                       |     |                    |          |                |     |
| ---------- | ---------- | --------- | --- | ------- | ---- | ----------- | --- | --------------------- | --- | ------------------ | -------- | -------------- | --- |
|            |            |           |     |         |      |             |     | [14] P. Salva-Garcia, | J.  | M. Alcaraz-Calero, | Q. Wang, | J. B. Bernabe, | and |
high scalability and performance achieved by this proposed A.Skarmeta,‘‘5GNB-IoT:Efficientnetworktrafficfilteringformulti-
tenantIoTcellularnetworks,’’Secur.Commun.Netw.,vol.2018,pp.1–21,
| system. | In the | tests, the | implemented |     | framework |     | has been |     |     |     |     |     |     |
| ------- | ------ | ---------- | ----------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- |
Dec.2018.
validatedtobeabletosupportmMTCtrafficofupto1million
[15] A.M.Escolar,J.M.A.Calero,andQ.Wang,‘‘Highly-scalablesoftware
IoTdevices,achieveover15GbpseMBBbandwidth,ensure firewallsupportingonemillionrulesfor5GNB-IoTnetworks,’’inProc.
IEEEInt.Conf.Commun.(ICC),Jun.2020,pp.1–6.
| delays in   | the order | of µs  | for    | uRLLC,    | whilst | providing | high        |               |                    |     |                 |       |            |
| ----------- | --------- | ------ | ------ | --------- | ------ | --------- | ----------- | ------------- | ------------------ | --- | --------------- | ----- | ---------- |
|             |           |        |        |           |        |           |             | [16] Q. Wang, | J. Alcaraz-Calero, | R.  | Ricart-Sanchez, | M. B. | Weiss, and |
| reliability | in all    | of the | tested | scenarios | with   | 0%        | packet loss |               |                    |     |                 |       |            |
A.Gavra,‘‘EnableadvancedQoS-awarenetworkslicingin5Gnetworks
ratio. Moreover, it takes only 5.7 ms on average to create a forslice-basedmediausecases,’’IEEETrans.Broadcast.,vol.65,no.2,
networksliceinthedataplaneforchallengingheterogeneous pp.444–453,Jun.2019.
[17] J.J.DiazRivera,T.A.Khan,A.Mehmood,andW.-C.Song,‘‘Network
trafficsituations. sliceselectionfunctionfordataplaneslicinginamobilenetwork,’’inProc.
Futureworkwillinvestigatetheapplicationoftheproposed 20th Asia–Pacific Netw. Oper. Manage. Symp. (APNOMS), Sep. 2019,
| solution | in real-world |     | 5G and | beyond | trials | and | evaluate | pp.1–4. |     |     |     |     |     |
| -------- | ------------- | --- | ------ | ------ | ------ | --- | -------- | ------- | --- | --- | --- | --- | --- |
[18] SystemArchitectureforthe5GSystem(Release15),documentTR23.501
the perceived quality of its performance for various verti- V15.0.03,GenerationPartnershipProject(3GPP),Dec.2017.
cal business applications. In addition, the integration of the [19] A.E.Kalor,R.Guillaume,J.J.Nielsen,A.Mueller,andP.Popovski,‘‘Net-
workslicinginindustry4.0applications:Abstractionmethodsandend-to-
| OpenSliceVS | Flow | Agent | with | kernel | bypass | applications |     |     |     |     |     |     |     |
| ----------- | ---- | ----- | ---- | ------ | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
endanalysis,’’IEEETrans.Ind.Informat.,vol.14,no.12,pp.5419–5427,
suchasDPDKoreXpresswillbeassessedinordertomiti-
Dec.2018.
gatetheperformancelimitationsoftheLinuxkernelnetwork
[20] P.Rost,M.Breitbach,H.Roreger,B.Erman,C.Mannweiler,R.Miller,
andI.Viering,‘‘Customizedindustrialnetworks:Networkslicingtrialat
| stack and, | thus | provide | improved | key | performance |     | indica- |         |                 |          |               |            |           |
| ---------- | ---- | ------- | -------- | --- | ----------- | --- | ------- | ------- | --------------- | -------- | ------------- | ---------- | --------- |
|            |      |         |          |     |             |     |         | hamburg | seaport,’’ IEEE | Wireless | Commun., vol. | 25, no. 5, | pp.48–55, |
tors(KPIs)andboostscalability.
Oct.2018.
[21] T.Taleb,I.Afolabi,andM.Bagaa,‘‘Orchestrating5Gnetworkslicesto
REFERENCES supportindustrialInternetandtoshapenext-generationsmartfactories,’’
IEEENetw.,vol.33,no.4,pp.146–154,Jul.2019.
[1] I. Afolabi, T. Taleb, K. Samdanis, A. Ksentini, and H. Flinck, ‘‘Net- [22] R.Ricart-Sanchez,P.Malagon,A.Matencio-Escolar,J.M.AlcarazCalero,
workslicingandsoftwarization:Asurveyonprinciples,enablingtech- and Q. Wang, ‘‘Toward hardware-accelerated QoS-aware 5G network
| nologies, | and | solutions,’’ | IEEE | Commun. | Surveys | Tuts., | vol. 20, no. 3, |     |     |     |     |     |     |
| --------- | --- | ------------ | ---- | ------- | ------- | ------ | --------------- | --- | --- | --- | --- | --- | --- |
slicingbasedondataplaneprogrammability,’’Trans.Emerg.Telecommun.
pp.2429–2453,3rdQuart.,2018. Technol.,vol.31,no.1,Jan.2020.Art.no.ett3726.[Online].Available:
[2] A. A. Barakabitze, A. Ahmad, R. Mijumbi, and A. Hines, ‘‘5G https://onlinelibrary.wiley.com/doi/abs/10.1002/ett.3726
network slicing using SDN and NFV: A survey of taxonomy, [23] F.Z.Yousaf,M.Bredel,S.Schaller,andF.Schneider,‘‘NFVandSDN—
architecturesandfuturechallenges,’’Comput.Netw.,vol.167,Feb.2020, Keytechnologyenablersfor5Gnetworks,’’IEEEJ.Sel.AreasCommun.,
Art.no.106984. [Online]. Available: http://www.sciencedirect.com/ vol.35,no.11,pp.2468–2478,Nov.2017.
science/article/pii/S1389128619304773
[24] C.Bouras,P.Ntarzanos,andA.Papazois,‘‘CostmodelingforSDN/NFV
[3] L.U.Khan,I.Yaqoob,N.H.Tran,Z.Han,andC.S.Hong,‘‘Network based mobile 5G networks,’’ in Proc. 8th Int. Congr. Ultra Modern
slicing:Recentadvances,taxonomy,requirements,andopenresearchchal- Telecommun.ControlSyst.Workshops(ICUMT),Oct.2016,pp.56–61.
lenges,’’IEEEAccess,vol.8,pp.36009–36028,2020. [25] A. Matencio-Escolar, Q. Wang, and J. M. Alcaraz Calero,
[4] J.Cheng,W.Chen,F.Tao,andC.-L.Lin,‘‘IndustrialIoTin5Genvi- ‘‘SliceNetVSwitch: Definition, design and implementation of 5G
| ronment | towards | smart | manufacturing,’’ |     | J. Ind. | Inf. Integr., | vol. 10, |     |     |     |     |     |     |
| ------- | ------- | ----- | ---------------- | --- | ------- | ------------- | -------- | --- | --- | --- | --- | --- | --- |
multi-tenantnetworkslicinginsoftwaredatapaths,’’IEEETrans.Netw.
pp.10–19, Jun. 2018. [Online]. Available: http://www.sciencedirect. ServiceManage.,vol.17,no.4,pp.2212–2225,Dec.2020.
com/science/article/pii/S2452414X18300049 [26] B. Pfaff, J. Pettit, T. Koponen, E. Jackson, and A. Zhou, ‘‘The
[5] W.Li,R.Liu,Y.Dai,D.Wang,H.Cai,J.Fan,andY.Li,‘‘Researchon design and implementation of Open vSwitch,’’ in Proc. USENIX
networkslicingforsmartgrid,’’inProc.IEEE10thInt.Conf.Electron.Inf. Symp. Netw. Syst. Design Implement., Oakland, CA, USA,
EmergencyCommun.(ICEIEC),Jul.2020,pp.107–110.
|     |     |     |     |     |     |     |     | May | 2015, pp.117–130. | [Online]. | Available: | https://www.usenix. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --------- | ---------- | ------------------- | --- |
[6] B.Dzogovic,B.Santos,J.Noll,V.T.Do,B.Feng,andT.V.Do,‘‘Enabling org/conference/nsdi15/technical-sessions/presentatio%n/pfaff
smarthomewith5Gnetworkslicing,’’inProc.IEEE4thInt.Conf.Comput. [27] TheLinuxFoundationProject.(2019).OpenvSwitchwebsite.[Online].
Commun.Syst.(ICCCS),Feb.2019,pp.543–548. Available:https://www.openvswitch.org/
| 14068 |     |     |     |     |     |     |     |     |     |     |     | VOLUME9,2021 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

A.MatencioEscolaretal.:AdaptiveNetworkSlicinginMulti-Tenant5GIoTNetworks
[28] October (2020). Open Daylight Official Website. [Online]. Available: JOSE M. ALCARAZ-CALERO (SeniorMember,
https://www.opendaylight.org/ IEEE)receivedthePh.D.degreeincomputerSci-
[29] The Open Infrastructure Foundation (OIF). (2020). OpenStack Official ence from the University of Murcia. He is cur-
Website.[Online].Available:https://www.openstack.org/ rentlyaFullProfessorinnext-generationnetworks
[30] Study on Management and Orchestration of Network Slicing for Next and security with the University of the West of
GenerationNetwork(Release15),documentTR28.801V15.01.0,3GPP,
Scotland.HeistheTechnicalCo-Coordinatorof
Mar.2017.
|     |     |     |     |     |     |     | the EU H2020 | 5G-PPP SELFNET | and SliceNet |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | ------------ |
[31] L.Cheng,‘‘Networkslicingarchitecture,’’InternetEngineeringTaskForce
projectsandaCo-PrincipalInvestigatoroftheEU
(IETF),Fremont,CA,USA,Tech.Rep.draft-geng-netslices-architecture-
|     |     |     |     |     |     |     | H2020 5G | INDUCE and 6G | BRAINS projects. |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | ---------------- |
02,Jul.2017.
[32] NetworkSlicingfor5GNetworksandServices(WhitePaper),5GAmeri- Hisprofessionalinterestsincludenetworkcogni-
tion,management,securityandcontrol,servicedeployment,automationand
cas,Bellevue,WA,USA,2016.
orchestration,and5Gmobilenetworks.
| [33] Summary | of Rel-15 | Work | Items | (Release | 15), document | TR 21.915 |     |     |     |
| ------------ | --------- | ---- | ----- | -------- | ------------- | --------- | --- | --- | --- |
V15.0.0,3GPP,Sep.2019.
[34] NetworkFunctionsVirtualisation(NFV)Release3;EvolutionandEcosys-
| tem; | Report on | Network | Slicing | Support | with ETSI | NFV Architecture |     |     |     |
| ---- | --------- | ------- | ------- | ------- | --------- | ---------------- | --- | --- | --- |
Framework,documentGRNFV-EVE012V3.1.1,ETSI,Dec.2017. PABLO SALVA-GARCIA received the Ph.D.
degreefromtheUniversityoftheWestofScotland,
[35] Systemarchitectureforthe5GSystem(5GS),EuropeanTelecommunica-
U.K.HeiscurrentlyaPost-DoctoralResearcher
tionsStandardsInstitute,SophiaAntipolis,France,Apr.2019.
[36] ITU-R(RadioCommunicationSectorofITU),MinimumRequirements with the University of the West of Scotland.
Related to Technical Performance for IMT-2020 Radio Interface(s), HehasbeentechnicallyinvolvedintheEUHori-
document ITU-R M.2410-0, ITU, Geneva, Switzerland, Nov. 2017. zonH2020SELFNETandSliceNetprojects.Heis
[Online]. Available: https://www.itu.int/dms_pub/itu-r/opb/rep/R-REP- amemberoftheB5G-Hubresearchinggroup.His
M.2410-2017-PDF-E.pdf maininterestsincludenetworkmanagement,cog-
| [37] G. Architecture |     | and W. | Group. | (2017). | View of | 5G Architecture. |     |     |     |
| -------------------- | --- | ------ | ------ | ------- | ------- | ---------------- | --- | --- | --- |
nitivecontrolplane,dataplaneprogrammability,
https://5g-ppp.eu/wp-content/uploads/2018/01/5G-PPP-5G-Architecture-
software-definednetworks,andvideodeliveryin
Whi%te-Paper-Jan-2018-v2.0.pdf
5Gnetworks.
[38] M.Ayaz,M.Ammad-Uddin,Z.Sharif,A.Mansour,andE.M.Aggoune,
| ‘‘Internet-of-Things |     | (IoT)-based | smart | agriculture: | Toward | making the |     |     |     |
| -------------------- | --- | ----------- | ----- | ------------ | ------ | ---------- | --- | --- | --- |
fieldstalk,’’IEEEAccess,vol.7,pp.129551–129583,2019.
| [39] K. Tange, | M.            | De Donno, | X. Fafoutis, | and       | N. Dragoni,  | ‘‘A systematic |              |         |                    |
| -------------- | ------------- | --------- | ------------ | --------- | ------------ | -------------- | ------------ | ------- | ------------------ |
|                |               |           |              |           |              |                | JORGE BERNAL | BERNABE | received the B.S., |
| survey         | of industrial | Internet  | of Things    | security: | Requirements | and fog        |              |         |                    |
M.S.,andPh.D.degreesincomputerscienceand
computingopportunities,’’IEEECommun.SurveysTuts.,vol.22,no.4,
|     |     |     |     |     |     |     | the M.B.A. | degree from the | University of Mur- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | ------------------ |
pp.2489–2520,2ndQuart.,2020.
[40] T.Spadini,D.L.deOliveiraSilva,andR.Suyama,‘‘SoundEventRecog- cia, Spain. He is currently an Assistant Profes-
nitioninaSmartCitySurveillanceContext,’’2019. sor with the University of Murcia. He has been
|          |              |         |          |           |                 |            | a Visiting   | Researcher with    | the Hewlett-Packard |
| -------- | ------------ | ------- | -------- | --------- | --------------- | ---------- | ------------ | ------------------ | ------------------- |
| [41] IBM | Watson Media | Support | Center.  | (Oct.     | 2020). Internet | Connection |              |                    |                     |
|          |              |         |          |           |                 |            | Laboratories | and the University | of the West of      |
| and      | Recommended  |         | Encoding | Settings. | [Online].       | Available: |              |                    |                     |
Scotland.Duringthelastyears,hehasbeenwork-
https://support.video.ibm.com/hc/en-us/articles/207852117-Internet-
conn%ection-and-recommended-encoding-settings/ ing in several European research projects, such
[42] J. Egger and T. Masood, ‘‘Augmented reality in support of intelligent asSocIoTal,ARIES,OLYMPUS,ANASTACIA,
manufacturing – a systematic literature review,’’ Comput. Ind. Eng., INSPIRE-5G,andCyberSec4EU.Hehasauthoredseveralbookchaptersand
vol. 140, Feb. 2020, Art.no.106195. [Online]. Available: http://www. morethan60articlesininternationaltop-levelconferencesandjournals.
sciencedirect.com/science/article/pii/S0360835219306643
|     |     |     |     |     |     |     | QI WANG | received the Ph.D. | degree in mobile |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------------ | ---------------- |
networkingfromtheUniversityofPlymouth,U.K.
ANTONIO MATENCIO ESCOLAR is currently HeiscurrentlyaFullProfessorwiththeUniver-
pursuing the Ph.D. degree with the University sityoftheWestofScotland.HeistheTechnical
of the West of Scotland, U.K. He is currently a Co-CoordinatoroftheEUH20205G-PPPSELF-
member of the B5G-Hub Research Group, Uni- NET and SliceNet projects and a Co-Principal
versity of the West of Scotland. He has been Investigator of the EU H2020 5G INDUCE and
6GBRAINSprojects.HeisaBoardMemberof
activelyinvolvedintheH20205G-PPPSlicenet
project. His main research interests include net- theTechnologyBoardofEU5G-PPP.Hisresearch
work slicing, software datapath, IoT, SDN, data primarilyfocuseson5Gmobilenetworks,video
planeprogrammability,and5Gmobilenetworks networking,andartificialintelligence.
andnetworkcontrolandmanagement.
| VOLUME9,2021 |     |     |     |     |     |     |     |     | 14069 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | ----- |