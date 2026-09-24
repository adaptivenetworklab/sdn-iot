# DLVisor Dynamic Learning Hypervisor for Software Defined Network (2)

> Source file: `DLVisor Dynamic Learning Hypervisor for Software Defined Network (2).pdf`

---

Received5July2023,accepted30July2023,dateofpublication4August2023,dateofcurrentversion14August2023.
DigitalObjectIdentifier10.1109/ACCESS.2023.3302266
DLVisor: Dynamic Learning Hypervisor for
Software Defined Network
MOHAMEDKHALAFALLAHASSAN 1,2,
SHARIFAHHAFIZAHSYEDARIFFIN 2,(SeniorMember,IEEE),SHARIFAHKAMILAHSYED-YUSOF2,
NURZALEFFIYANABINTIGHAZALI 2,MOHAMMEDE.A.KANONA 1,
KHALIDS.MOHAMED 1,(Member,IEEE),MUTAZH.H.KHAIRI1,(SeniorMember,IEEE),
ANDMOSABHAMDAN3,(SeniorMember,IEEE)
1FacultyofTelecommunicationandSpaceTechnology,FutureUniversity,Khartoum10553,Sudan
2FacultyofElectricalEngineering,UniversityTechnologyMalaysia,JohorBahru81310,Malaysia
3InterdisciplinaryResearchCenterforIntelligentSecureSystems,KingFahdUniversityofPetroleumandMinerals,Dhahran31261,SaudiArabia
Correspondingauthor:MohamedKhalafallaHassan(memo1023@hotmail.com)
ABSTRACT SoftwareDefinedNetwork(SDN)isoneofthemodernnetworkingtechnologiesthatprovide
network flexibility and simplifies network management. Virtual SDN (vSDN) enhances the flexibility of
sharingphysicalnetworkingresourcesbymultipleslicesrepresentingmultipletenantsorserviceswhereeach
tenanthascontrolovertheirservicesorapplicationsovertheVirtualNetwork(VN).Networkvirtualization
gives service providers more flexibility to offer new and innovative services with extra efficiency and
reliability. Running multiple virtual networks over a given infrastructure creates challenges for efficient
resourceallocationmechanismstoavoidcongestionandresourcestarvationandtomaintainServiceLevel
Agreement (SLA), where resource management in vSDN is carried out by hypervisors. Few studies have
addresseddynamicresourceallocationinthevSDNdomain.Therefore,toefficientlyutilizetheresourcesof
thevirtualizednetworkinginfrastructure,networkhypervisorsmustbeproactivewithself-reconfiguration
capabilities to assign the physical resources and be highly adaptable and react to changing vSDN future
demands.Thus,dynamiclearning-basedhypervisorsaretoimprovehypervisoroperations.Basedonthat,
thisstudyaimstoenhancethevSDNtechnologytoprovideanenhancedproactivedynamicsliceresource
allocationmechanism,toimprovetrafficdeliveryandresourceutilization.Thiscanbefulfilledbyproposing
anenhancedintelligentforecastingmodelforvSDNsliceresourceutilizationbasedonimprovedstatistical
andMachineLearning(ML)techniques.Theproposedmodelwillreactdynamicallytotheconceptdrifts
and then be utilized to develop a resource allocation mechanism for vSDN slice resource allocation. The
improved dynamic forecasting resource allocation mechanism is verified through available real network
tracesdatasetsfromvarioussources.TheDLVisorwithitsDynamicLearningFramework(DLF)canreduce
overutilizationand,consequently,resourcestarvationby100%comparedtotherelatedbenchmark.
INDEX TERMS Machine learning, resource allocation, resource forecast, software defined network,
virtualization.
I. INTRODUCTION plane.Ontheotherhand,networkvirtualizationenablesshar-
Software-defined networking (SDN) has emerged as a ing of physical networking resources where tenants or slice
promising networking technology that enables flexible data owners have authority over their virtual network resources.
management in computer and communication networks Networks can exploit the benefits of SDN and Network
wherebyitseparatesthedataforwardingplaneandthecontrol Function Virtualization (NFV) through the virtualization of
SDNnetworks.TheSDNhypervisorseparatestheunderlying
The associate editor coordinating the review of this manuscript and physical SDN network into numerous logically separated
approvingitforpublicationwasMahdiZareei . vSDNs, each with its controller. For instance, each Virtual
ThisworkislicensedunderaCreativeCommonsAttribution-NonCommercial-NoDerivatives4.0License.
84144 Formoreinformation,seehttps://creativecommons.org/licenses/by-nc-nd/4.0/ VOLUME11,2023

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
TABLE1. Listofabbreviations. be designed to be adaptable, where it should adopt and
enforceapproachesforself-reconfiguration.Toensurebetter
resourceallocationandoptimization,vSDNrequirescurrent
|     |     |     |     | and future | network states | to be forecasted | and | continuously |
| --- | --- | --- | --- | ---------- | -------------- | ---------------- | --- | ------------ |
runinonlineorsemi-onlinemodetoadapttonetworkdemand
|     |     |     |     | variations. | Such mechanisms | and approaches | must                | work in |
| --- | --- | --- | --- | ----------- | --------------- | -------------- | ------------------- | ------- |
|     |     |     |     | variable    | time scales to  | achieve high   | resource efficiency | for     |
thevirtualizedresources.Therefore,dynamiclearning-based
hypervisorsareneededtoimprovethehypervisoroperations.
Thedesignofhypervisorresourcemanagementalgorithmsin
solvingthesechallengesisanopenresearchfieldandneeds
detailedinvestigation[1],[4].
|     |     |     |     | To efficiently | utilize               | the resources | of the            | virtualized  |
| --- | --- | --- | --- | -------------- | --------------------- | ------------- | ----------------- | ------------ |
|     |     |     |     | networking     | infrastructure,       | sophisticated | forecasting-based |              |
|     |     |     |     | resource       | allocation frameworks | are needed    | for               | the physical |
resources.Theseframeworksmusthavesomeintelligenceto
copewiththedynamicQualityofService(QoS)demandand
beabletoreactautonomouslytodynamicandself-organizing
|     |     |     |     | situations    | without affecting | the SLA.           | Therefore,  | proactive |
| --- | --- | --- | --- | ------------- | ----------------- | ------------------ | ----------- | --------- |
|     |     |     |     | approaches    | for managing      | bandwidth          | and network | resources |
|     |     |     |     | are highly    | needed [7],       | [8]. The proactive | dynamic     | net-      |
|     |     |     |     | work resource | allocation        | relies on the      | forecasting | network   |
demandsandactsaccordinglytoenableatimelyanddynamic
|     |     |     |     | response. | Thus, the accuracy | of predictive | approaches   | was         |
| --- | --- | --- | --- | --------- | ------------------ | ------------- | ------------ | ----------- |
|     |     |     |     | regarded  | as a vital factor  | in various    | applications | of the pre- |
dictiveframeworks.
|     |     |     |     | Accurate     | ML techniques     | are crucial | and          | widely used   |
| --- | --- | --- | --- | ------------ | ----------------- | ----------- | ------------ | ------------- |
|     |     |     |     | in different | applications,     | such as     | network      | traffic fore- |
|     |     |     |     | casts [9],   | [10], [11], [12], | [13], [14], | the Internet | of Things     |
(IoT)[15],andwirelesscommunications[16].Theresource
managementinvSDNisperformedbytheSDNhypervisor.
Noproactivedynamicresourceallocationmechanismswere
|     |     |     |     | provided | in all related  | literature, the | provided | methodolo-   |
| --- | --- | --- | --- | -------- | --------------- | --------------- | -------- | ------------ |
|     |     |     |     | gies and | frameworks were | either static   | (they    | cannot adapt |
Machine (VM) and its guest operating system runs on a to traffic/network changes) or reactive due to working in
specificphysicalcomputingplatform[1],[2],[3].Inaddition current states with no resource forecasting which may lead
to monitoring the virtual machines, the hypervisor assigns toresourcestarvation.Therefore,itisessentialtodevelopa
actualcomputingplatformresourcestoeachvirtualmachine.
|     |     |     |     | dynamic | learning framework | to allocate | and modify | band- |
| --- | --- | --- | --- | ------- | ------------------ | ----------- | ---------- | ----- |
ThehypervisorcreatesseveralvSDNsusingtheOpenFlow width slices for better resource utilization and to avoid
(OF) protocol based on a particular physical network. Each resourcestarvationandSLAviolationsduetocongestionand
vSDN corresponds to a slice of the entire network. Future QoSdegradation.
networkingtechnologiesinFifthGeneration(5G)andbeyond Thisstudy aimsto enhancethe vSDNtechnology topro-
| are to be enabled | by vSDNs | [4], [5], [6]. Running | vSDN |         |                  |                |            |        |
| ----------------- | -------- | ---------------------- | ---- | ------- | ---------------- | -------------- | ---------- | ------ |
|                   |          |                        |      | vide an | improved dynamic | slice resource | allocation | mecha- |
overagiveninfrastructurewithefficientresourceallocation nism to improve resource utilization and minimize resource
mechanisms may improve the utilization of the networking starvation.Thespecificobjectiveofthisworkistoenhance
hardware that meets tenant and service specifications and thesliceallocationmechanisminvSDNbasedontheproac-
Service Level Agreement (SLA). Table 3 shows the list of tive slice management based on resource (bandwidth fore-
symbolswhichwillbeusedinthefollowingsection
|     |     |     |     | cast) in | which will be | reflected as | a result in | eliminating |
| --- | --- | --- | --- | -------- | ------------- | ------------ | ----------- | ----------- |
In addition, vSDN enables network service providers to the count of overutilization and minimize congestion and
deliver new and innovative services with greater flexibil- resourcestarvation.ThisresearchcontributestovSDNtech-
ity, efficiency,and dependability. Operating multiplevirtual nologybyprovidingthehypervisorswiththecapabilitiesto
networksrequiresasignificantamountofphysicalnetwork- manageandimprovetheirperformanceautonomouslysince
ing resources. Therefore, intelligent, and efficient resource bandwidthslicemanagementisoneofthecriticalresources
allocationmethodsareessential.Topersistentlyachieveand that need to work on short time scales to achieve high
sustainthebestperformance,SDNnetworkhypervisorsmust resource efficiency for the virtualized resources. Therefore,
| VOLUME11,2023 |     |     |     |     |     |     |     | 84145 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ----- |

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
| this research | will | proactively | provide |     | ML learning-based |     |     |     |     |
| ------------- | ---- | ----------- | ------- | --- | ----------------- | --- | --- | --- | --- |
hypervisorstoavoidsliceresourcestarvationandSLAviola-
tioninvSDN.Thisincludes:
| 1) integrating |       | an enhanced | static | forecasting |      | model into |     |     |     |
| -------------- | ----- | ----------- | ------ | ----------- | ---- | ---------- | --- | --- | --- |
| vSDN           | slice | management  | to     | improve     | vSDN | slice uti- |     |     |     |
lizationbasedonMLtechniques.
2) adoptingthestaticforecastingmodelusingadynamic
| learning | framework |     | (DLF) | to reduce | the | static model |     |     |     |
| -------- | --------- | --- | ----- | --------- | --- | ------------ | --- | --- | --- |
forecastingerrorduetoconceptchangestoupdateand
improvemodelvalidity.
| 3) proposing |     | proactive | enhanced | resource |     | (bandwidth) |     |     |     |
| ------------ | --- | --------- | -------- | -------- | --- | ----------- | --- | --- | --- |
sliceallocationandsupplyanddemandmanagementin
vSDNusingthedynamiclearningframeworktomini-
mizecongestionandresourcestarvation.Theproposed
| vSDN | slice | management |     | framework | will | be named |     |     |     |
| ---- | ----- | ---------- | --- | --------- | ---- | -------- | --- | --- | --- |
DLVisor.
| The organization |              | of the paper | is         | as follows, | section | II pro-     |     |     |     |
| ---------------- | ------------ | ------------ | ---------- | ----------- | ------- | ----------- | --- | --- | --- |
| vides a brief    | introduction |              | of virtual | network     | and     | virtualiza- |     |     |     |
tion,SDNandvSDN,sectionIIIdiscussthestate-of-the-art FIGURE1. vSDNarchitecture.
| resource | management | in vSDN | technology, |     | section | IV pro- |     |     |     |
| -------- | ---------- | ------- | ----------- | --- | ------- | ------- | --- | --- | --- |
vides the overall methodology, algorithms, architecture and allocation requests can be performed by admission control
implementation of the dynamic bandwidth slice allocation, mechanisms.ThecurrentVNEoptimizationalgorithmsrange
| section VI | discusses | the results |     | and findings |     | while section |                          |                       |             |
| ---------- | --------- | ----------- | --- | ------------ | --- | ------------- | ------------------------ | --------------------- | ----------- |
|            |           |             |     |              |     |               | from exact formulations, | such as mixed-integer | linear pro- |
VIIprovidestheconclusion grams, to heuristic approaches based, it is possible to relate
theresourceassignmentofvSDNstothegenericVNEprob-
II. BACKGROUND lemandoutlinetheuseofthegeneralVNEperformancemet-
ricsintheSDNcontext.Severalpublishedoverviewsurveys
NetworkVirtualization(NV)hasbeenderivedfromthesuc-
cess of virtualization in the computing domain [1], [17]. are already discussing network virtualization’s principles,
It creates separate virtual networks (slices) through spe- benefits, and approaches. For example, a detailed survey of
cific abstraction and isolation functional blocks [1]. In the networkvirtualizedhypervisorsforSDNcanbefoundin[1].
networking domain, slicing concepts are already there. For The capability to program virtual networks using SDN
example, optical fiber-based networking, Wavelength Divi- is another important key aspect of total network virtualiza-
sion Multiplexing (WDM) [18] can create slices at the tion [21]. Looking at legacy network virtualization, such as
physical layer, while at the link layer, Virtual Local Area VLAN-based virtualization with no programming features,
Network (VLAN) and Multiple Protocol Label Switching tenants will not be able to instruct switches to take actions
(MPLS)[7],[19]canbecreated. such as traffic management, i.e., traffic steering. Neverthe-
On the contrary, network virtualization tends to establish less,tofullyrealizeNFV,tenantsmustobtainvirtualnetwork
slices of the entire network, i.e., to form virtual networks resources, such as total views of network topologies and
(slices) across all network protocol layers. At any moment, allocatednetworkingresources,involvinglinkdataratesand
agivensliceshouldhaveitsresources(specificabstractionof network node resources. Moreover, providing isolated and
thenetworktopology,linkbandwidths,switchcomputational programmable virtual networks has a significant advantage.
resources and switch forwarding tables). Virtual network Insuchacase,networkoperatorscandevelopandtestnovel
(slice)enablestestingofnewnetworkingparadigms,regard- networkingtechnologieswithlessimposedconstraints[22].
less of the propriety and restrictions imposed by current In addition, NV is considered a key player in providing
internetstructuresandprotocols[1].Runningmultiplevirtual predictable (guaranteed) network performance [23]. Con-
networks involves consuming specific amounts of physical sequently, Service Providers (SPs) will be able to provide
networkingresources.Therefore,efficient,andsophisticated or provision new services over existing infrastructures in a
resourceallocationmechanismsarehighlyneeded[8],[20]. much faster and more reliable way furthermore, SPs will
For instance, the interconnection between the virtual nodes, allow their networks to dynamically alter and modify their
the virtual paths and VM Placement on the physical infras- virtual network according to the changing user and service
tructure, this is also known as Virtual Network Embedding demands [24], [25], [26]. The network virtualization layer
(VNE)problem[1]. allows hosting multiple controllers [26], [27]. The network
The VNE problem is Non-deterministic Polynomial-time hypervisorcommunicateswiththeunderlyingnetworkhard-
hardness(NP-hard)andisstillbeingextensivelyinvestigated. warethroughthesouthboundinterfaceviaanSDNprotocol,
Generally, accepting and rejecting virtual network resource OFasanexample.InthecaseofNV,thehypervisoroperates
| 84146 |     |     |     |     |     |     |     |     | VOLUME11,2023 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
ontopofthesamesouthboundinterfaceforvirtualnetwork composition configuration to process SDN rules, the study
operatorsandtowardsSDNnetworktenants.Thehypervisor stressedoncompositionpolicyformationtimewhichisadded
is interfaced with multiple southbound with several SDN to the hypervisor OF latency, in addition, the priority list is
controllers [27]. The SDN hypervisor operates as a proxy. staticanddonotallocateormanageresourcesdynamically.
It intercepts and translates the control messages between Authors [21] proposed the Network Virtualization Plat-
tenantsandthephysicalSDNnetwork.Fig1showsthevSDN form (NVP), focusing on data center network resource
architecture. abstraction managed by the cloud tenants for multi-tenant
BycombiningSDNandNFV,tenantswillhavetheadvan- environments, which works as a controller to provide SDN
tageofflexibilityinresourcesharingthroughvirtualnetwork tenants to operate their SDN controllers via Application
sharing in addition to having the programmability feature Programming Interface (API) and control their slices in the
of SDN, while NFV provides the ability to program the data center. This is accomplished by forming a distributed
virtual resources [25] whereby the combination is called controllerclustertoscaletenants’loadasrequiredwithvir-
vSDN[24],[26].ThiscanbeseeninFig1whichshowsthe tualizedswitchestosteertenants’traffictothecorresponding
vSDNarchitecture. virtualmachinesbyfocusingonsoftwarethatresidesinside
the virtual switches on the host servers. NVPs generally
III. RELATEDWORK establishlogicaldatapaths(tunnels)betweenthedestination
Thissectiondiscussestherelatedworkinthecontextofthe andthesourceOpenVirtualSwitch(OVS)wherethelogical
dynamic bandwidth (slice) management in vSDN. As dis- path relates to the corresponding tenant slice using Generic
cussedinprevioussections,thehypervisorsperformresource RoutingEncapsulation(GRE)tunnellingtechniques.
managementtasks,andallvSDNhypervisorsareconsidered OpenVirteX hypervisor in [31] was introduced with two
extensionstotheFlowVisorhypervisor. primary contributions: topology and address virtualization.
FlowVisor(FV)isthefirsthypervisorforSDNnetworks, OpenVirteXextendsFVbytacklingtheflowspaceproblem.
providing the feature of sharing SDN networking resources This is achieved by using of headers to distinguish vSDNs
between multiple controllers. FV can ultimately run as instead of providing the entire of header fields space to the
stand-alone software on commodity hardware (server) [28]. vSDNs.InOpenVirteX,switchesre-writevirtuallyassigned
FVisageneral-purposehypervisorandrepresentsthefoun- Internet Protocol (IP) and Media Access Control (MAC)
dationsforothervSDNhypervisors.Itoffersnodeattributes addressesutilizedbythehostsofeachvSDN(tenant).Open-
isolation such as Central Processing Unit (CPU) and Flow Virtex did not add a valuable contribution to the dynamic
table in addition to bandwidth as a link attribute isolation. resourcemanagement.
FV mainly stressed approaches to isolate network traffic in In [32], a Datapath centric hypervisor was introduced
experimental networks from traffic in production network to address the redundancy issue in FV (Single point of
whereby it provides flexible definitions of network slices. failure) and enhance the virtualization layer performance
However, it added latency in OF messages and exhibits no through the implementation of virtualization function as
admissioncontrolandnomechanismsforslicemanagement switch extensions. It works by implementing Virtualization
andoptimization. Agents(VA)insideswitchesinadditiontotheVirtualization
MobileVisor in [29], applied the FlowVisor approach in AgentOrchestrator(VAO).TheVAO’sultimateresponsibil-
mobile packet core networks; where FlowVisor functional- ityistheslicemonitoringandconfiguration,exampleofthis
ity is integrated into the architectural structure of a virtual isaddingorremovingslices.Ontheotherhand,VAisrespon-
mobilepacketnetworkthatiscomprisedofseveralunderly- sible for communicating with vSDN controllers in addition
ingphysical mobilenetworkssuchas 3Gand4Gnetworks. to resource abstraction for the VAO. If VAO fails, VA can
ItallowedInternetServiceProviders(ISPs)todefinepolicy continuetooperate,avoidingasinglepointoffailureinFlow
and QoS-based service in addition to that mobile operator. visor architecture. Datacentric does not support bandwidth
Moreover, ISPs will be able to manage their charging poli- isolation but still can support QoS based on extensive eval-
cies more efficiently. No latency calculation is mentioned; uations.TheVAcaseaddsanoverheadof18%comparedto
however, since the hypervisor adopts FV, it lacks dynamic the reference case. Failover overhead latency is about 3ms.
resourcemanagement. Although it can support QoS, a lack of bandwidth isolation
In [30] authors introduced compositional hypervisor to willnotallowdynamicbandwidthsliceallocation.
provideaflexibleplatformthatenablesSDNnetworkopera- In [33], CoVisor was introduced as an extension to a
torstochoosevariousnetworkapplicationsdevelopedfordif- compositional hypervisor that facilitates the cooperation of
ferentSDNcontrollers.Thiswillallowdifferentapplications heterogeneous controllers to work on the same type of traf-
written for specific controllers to run on other controllers fic with more focus on improving SDN physical network
written in another language; the compositional hypervisor performance, i.e. flow table space and topology abstraction
establishesacomposedpolicythatrepresentsaprioritizedlist in such a way to provide the necessary resources such as
ofrulesperSDNswitchprovidedbythecorrespondingSDN topologyinformationorabstractionwhenneeded,i.e.aload
controller,andthenthecompositehypervisorformsasuitable balancerdoesnotnecessarilyrequireadetailedtopologyview
VOLUME11,2023 84147

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
to decide to drop or forward a packet. In addition to that, itsupportsdifferentSDNprotocolssuchasNetconfandLISP.
itprovidedaformofsecurityagainstfraudSDNcontrollers. Finally, it was tested and evaluated in minimal scenarios.
CoVisor enhanced Compositional hypervisor latency over- Nodynamicresourceallocationwasdiscussed.
headsbytwotothreefolds.However,thehypervisordidnot In[40],amanagementframeworkwasintroducedtopro-
providedynamicresourceallocation. videbandwidthmanagementthroughthedefinitionofstatic
In [34], DFVisor (Distributed FlowVisor) was introduced thresholds for each slice based on slice prior priority; the
totacklethescalabilityissueofFVasacentralizedSDNvir- framework was presented as an admission control mecha-
tualizationhypervisor.Itaddressedthepossibilityofextend- nism.theproposedframeworkcomprisesaDecisionMaking
ing SDN switches with hypervisor capabilities, producing (DM)Module,whichdecideshowmuchbandwidthtoallo-
enhanced OpenFlow switches which can be accomplished catebasedontherequesthandler’srequestandthedatabase
by extending SDN switches with a local tunnelling module module(DB)information.However,nodetailedassessment
and vSDN slicer. DFVisor utilizes GRE tunnelling for data wasprovidedonlatencyandoverheads.Moreover,theframe-
plan slicing and encapsulating data flows which are benefi- workwasstaticandwasbasedonlyoncurrentstates.
cialinadoptingQoS.DFvisoradoptstwo-levelsynchronized In [41] DART framework can dynamically distribute the
distributed databases, the first database (local) resides on network bandwidth to different to utilize network resources
switches, while the global database maintains slices of sta- efficiently. The framework adopts an admission control
tistical information, network operation and scalability are mechanismtodistributenetworkbandwidthondemand.The
improved.However,theproposedsolutionwasintendedfor scopewaslimitedtotheIndustrialInternetofThings(IIOT)
aclusterenvironment. and only worked on the current state. In this framework,
EnterpriseVisorin[35],isoneofthemostnotablehyper- twomoduleswereproposed,communicationandpublishing
visors regarding resource slice allocation. It introduces an modules. The communication module is used to send and
extended software module to monitor and analyze slice uti- receive information, while the publishing module is used to
lization.Inaddition,linearprogrammingwasusedtoadjust coordinate between the controllers. The centralized compo-
thebandwidthslicesdynamically,theproposedenginedeter- nentisresponsibleforadvisingthebestpossiblebandwidth
mines slice requesters and resource providers to meet ser- foreachSDNcontroller.Theadmissioncontrolcanbetrig-
vicerequirements.Furthermore,theEnterpriseVisorinteracts geredbyload,priority,andpacketlossratiotoredistributethe
withtheFlowVisor,applyingtheslicingpolicytoconfigure networkbandwidth.Thispaperusedprioritiesforthetraffic
thenetwork.Accordingly,sliceconfigurationcanbeadjusted asatriggerbasedontherequestedQoSlevel.
tomeetservicerequirements. In [42], the PrioSDN resource manager (PrioSDN_RM)
In[36],intent-basedvirtualnetworkmanagementplatform waspresentedasaresourcemanagementframeworktopro-
based on SDN is proposed to automate the configuration videadmissioncontrolforvirtualizedSDN-basednetworks.
andmanagementofVNresourcesfromthetenantside.The The proposed mechanism applies limits on the resource
framework was based on OpenVirtex. The proposed frame- utilization for the virtual slices. It adopts an approach to
work simplifies resource definitions and management from taking advantage of a bandwidth distribution mechanism to
the administrative side through high-level business require- react dynamically to load changes. It relies on flow prior-
ment representations since VN resource management is a ity, not device priority. Moreover, the bandwidth threshold
complicatedandtime-consumingprocessinadditiontoalack moves according to a predefined critical flow. the storage
of an available automated provisioning process. The intent keepstrackingcurrentbandwidthutilization,andthecompute
layerhelpsthetenantstospecifyhigh-levelrequirements. module computes the available bandwidth resources. Then,
In [37] and [38], AutoVFlow was introduced as a dis- itallocatesthenecessaryamountofbandwidthresourceswith
tributed hypervisor to be used in wide-area networks where the aid of the flow rules manager and threshold manager,
the underlying infrastructure span across a non-overlapping whichassignstheamountofbandwidthbasedonthepriority
domain. The hypervisor is responsible for each domain and oftheflows,providedthattheprioritythresholdcanbemoved
acts as a proxy that performs slice and abstraction mapping based on flow predefined priority. The proposed method-
AutoVflow delegates administration from heavy load con- ology works are similar to our approach, but it works in
trollerstootherlessloadedcontrollers.Solidupdatespolicy currentbandwidthconsumption,whichcouldleadtoresource
was maintained between the centralized and the distributed starvation.
controllerssinceoneslicecanspanmultipledomains.Several In [43], the Libera hypervisor was introduced to address
identities were used, such as virtual MAC addresses, which scalability and ease of tenants’ capability to provide their
canbedifferentfromonedomaintoanotherwasfoundtobe services. The scalability issue was mainly solved by sup-
considerably high (around 5.85 ms). The control process is porting VM migrations and architectural modifications in
manualanddoesnotconsiderdynamicloaddistribution. whichFlowrulesarereduced;therefore,bandwidthbetween
In[39],ONVisorHypervisorwaspresentedasanSDN-NV controllersandvirtualswitcheswillbeminimized.Liberais
platformtoprovideflexibilitybyadoptingdistributedhyper- considered an extension to OpenVirtx. Resource scalability
visor instances that allowed sharing of VN state. Moreover, is carried out at the current time without considering future
84148 VOLUME11,2023

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
|     |     | FIGURE2. | ScopeofresourcemanagementinvSDN. |     |     |     |     |     |     |     |
| --- | --- | -------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
demands.Moreover,nodetailedinvestigationwasperformed
onthescalabilitybasedonVMmigration.
| In [44],  | TeaVisor | was | presented to        | guarantee | bandwidth     |     |     |     |     |     |
| --------- | -------- | --- | ------------------- | --------- | ------------- | --- | --- | --- | --- | --- |
| isolation | in vSDN. | The | proposed hypervisor |           | addressed the |     |     |     |     |     |
issueofoverloadlinksbyusingagreedyheuristicalgorithm
tosplitthetrafficofoverloadedlinkstomultipleless-loaded
| paths. The | results              | were     | promising and | similar | to what this  |     |     |     |     |     |
| ---------- | -------------------- | -------- | ------------- | ------- | ------------- | --- | --- | --- | --- | --- |
| paper is   | addressing.          | However, | the algorithm |         | is based on   |     |     |     |     |     |
| current    | traffic measurement, |          | which may     | lead    | to a resource |     |     |     |     |     |
(bandwidthstarvation).
In[45],theauthorsproposedaresourcemanagementarchi-
tectureformultidomainSDNcontrollerloadscalabilityusing
anon-SDN-hypervisor.Theframeworkisbasedoncreating
| a new VM | for | the controller | or migrating | the | SDN con- |     |     |     |     |     |
| -------- | --- | -------------- | ------------ | --- | -------- | --- | --- | --- | --- | --- |
trollerbasedonloadelevation;Softwareagentswereusedin
monitoringthecontrollerloads.However,unlikeSDN-based
hypervisors,usingastand-alonehypervisoraddissuesoflack
ofresourceisolationforSDNcontrollers.Moreover,creation
| and VM  | live migrations |              | involve service | downtimes. | In all     |     |     |     |     |     |
| ------- | --------------- | ------------ | --------------- | ---------- | ---------- | --- | --- | --- | --- | --- |
| related | literature,     | the provided | methodologies   |            | and frame- |     |     |     |     |     |
FIGURE3. vSDNresourcemanagementcomponentsinDLVisor.
| works were | either | static | (it cannot adapt | to traffic/network |     |     |     |     |     |     |
| ---------- | ------ | ------ | ---------------- | ------------------ | --- | --- | --- | --- | --- | --- |
changes)orreactiveduetoworkingincurrentstateswithno
IV. DYNAMICBANDWIDTHSLICEALLOCATIONFOR
resourceforecasting,whichcanleadtoresourcestarvations.
| As depicted |     | in Fig 2, | this paper | will concentrate | on  | vSDN |     |     |     |     |
| ----------- | --- | --------- | ---------- | ---------------- | --- | ---- | --- | --- | --- | --- |
bandwidth resource management in self-configurable and ThisworkisbasedonEnterpriseVisor[35]whereitfocuses
|           |      |             |       |               |          | on enhancing | the existing | hypervisors | that should | be able |
| --------- | ---- | ----------- | ----- | ------------- | -------- | ------------ | ------------ | ----------- | ----------- | ------- |
| optimized | vSDN | hypervisors | where | the presented | solution |              |              |             |             |         |
(DLVisor)willbethefirsttocombinelearned-basedhypervi- to perform regardless of the underlying topology and net-
sorsthroughMLandmathematical-basedresourcemanage- work demands. Therefore, hypervisors should exhibit capa-
mentinvSDN. bilities to improve their performance autonomously and
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     | 84149 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
|     |     |     |     |     |     |     | FIGURE5. Testbedcomponents.  |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- |
|     |     |     |     |     |     |     | TABLE2. LSTMhyperparameters. |
FIGURE4. FlowchartfortheDLVisor.
| transparently | with | minimum | overheads. |     | Bandwidth | slice |                             |
| ------------- | ---- | ------- | ---------- | --- | --------- | ----- | --------------------------- |
|               |      |         |            |     |           |       | TABLE3. Datasetdescription. |
managementisoneofthecriticalresourcesthatneedtowork
inshorttimescalestoachievehighresourceefficiencyforthe
virtualizedresources.Thiscanbeachievedviacognitiveand
| learning-based | hypervisors |     | and | under varying | mathematical |     |     |
| -------------- | ----------- | --- | --- | ------------- | ------------ | --- | --- |
modellingobjectivesandconstraints.Theproposedimproved
hypervisorshowninthisworkisnamedDLVisor(Dynamic
| learning | hypervisor), |     | whereby | Fig 3 shows | the | proposed |     |
| -------- | ------------ | --- | ------- | ----------- | --- | -------- | --- |
vSDNresourcemanagementcomponentsinDLVisor.
| For this | purpose   | and | as shown         | in Fig | 3, the        | Dynamic |     |
| -------- | --------- | --- | ---------------- | ------ | ------------- | ------- | --- |
| Learning | Framework |     | (DLF) introduced |        | and discussed | in      |     |
our previous work [46] will be incorporated and integrated ortenant.ThisworkmainlyfocusesonvSDNvirtualization
withtheEnterpriseVisorresourcemanagementmoduleinthe where RAN end to end slicing is out of this paper ‘s scope
EnterpriseVisor hypervisor. The DLF will capture the net- andcanbefoundinotherrelatedworksuchasin[47].Three
workbandwidthslicefromtheCactiserverusingtheSimple utilizationlevelswillbedefinedaslowutilizationintherange
NetworkManagementProtocol(SNMP).Thelivetracescan of0%toβ,middleutilizationisβ toγ,andhighutilization
betweenγ
be accessed directly from network storage in online, semi- and100%.Fig4showstheoverallflowchartfor
| online, or | in batch | mode. | The | dynamic | learning | approach | theDLVisor. |
| ---------- | -------- | ----- | --- | ------- | -------- | -------- | ----------- |
willapplyvarioushybridLongShort-TermMemory(LSTM) The white part indicates the DLF while the dark blue
windows-based smoothing algorithms with minimum data part indicates slice allocation and bandwidth management
lossintroducedearlierin[46].Then,thebestalgorithmwill introduced by the EnterpriseVisor in line with the DLVisor
beusedtoforecastthenetworktrafficforeachserviceslice componentsshowninFig3.
84150 VOLUME11,2023

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
| FIGURE6. | Sequencediagramforthetestbedscenario. |     |     |     |     |
| -------- | ------------------------------------- | --- | --- | --- | --- |
FIGURE7. ATN-OBYslicecreation.
| As depicted     | in Fig 4,          | the flow      | starts with | building     | an  |
| --------------- | ------------------ | ------------- | ----------- | ------------ | --- |
| improved        | ML model by        | incorporating | loss-aware  | window-      |     |
| based smoothing | as a preprocessing |               | technique   | to eliminate |     |
theunnecessaryshort/long-termnoisecomponentsandavoid
FIGURE8. LogmessagesduringATN-OBYslicecreation.
| the erosion | of periodic trends | and | patterns | within the | series |
| ----------- | ------------------ | --- | -------- | ---------- | ------ |
noiseandrapidtrafficfluctuations,theoutputofthisprocess
isanimprovedhybridLSTM-basedMLthatwillbeusedfor
| traffic forecasts. | Then, to | address | ML model | reliability | and |
| ------------------ | -------- | ------- | -------- | ----------- | --- |
validityduetotherapiddatacharacteristicsanddistribution
changes resulting from the dynamic nature of the network FIGURE9. ThescriptusedtomodifytheslicebandwidthlimitbyDLVisor.
properties,theforecastingframeworksmustdetectandadapt
to all changes in the statistical properties of the network Changes in traffic profiles, such as the sudden surge in
traffic. traffic, occur due to changes or variations in the user’s
VOLUME11,2023 84151

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
FIGURE10. SlicesutilizationsinWa=1.
application behavioral demand. Therefore, a change detec- modelisbuiltprovidedtheresultsaresignificant.Thedetails
tor using Anderson Darling (AD) is incorporated due to its of the process are already discussed in our previous work
sensitivity to detect changes in data characteristics, which in[46].Duetoitsreliabilityandsimplicity,hyperparameter
may negatively affect the ML model accuracy. Then if a selectionwasconductedthroughgrid search,asdepictedin
change is detected, a statistical significance test is used to Table 2 [46]. Finally, the forecasted bandwidth is used as
validatetheoutputoftheforecasteddata.Accordingly,ifthe inputtothesliceallocationtoidentifytheresourceproviders
outputofthecurrentlyusedMLalgorithmisinsignificant,the andresourcerequestersusingslicesclassificationsintolow,
current(old)modelisretained,otherwise,anewhybridML medium, and high utilization slices, and then supply and
84152 VOLUME11,2023

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
TABLE4. Listofsymbols.
FIGURE11. CountsofoverutilizationinWa=1.
B. SLICEMANAGEMENTINvSDN
|                     |               |             | Table    | 4 shows the list of | symbols which will | be used in the |
| ------------------- | ------------- | ----------- | -------- | ------------------- | ------------------ | -------------- |
| demand calculations | are performed | to allocate | the vSDN |                     |                    |                |
followingsection
slices proactively to avoid overutilization to minimize and Algorithm 1 shows the Bandwidth Slice requesters and
eliminatecongestionandresourcestarvation. providers’ allocation. The Algorithm 1’s complexity is
O(nmh+m).
| A. DATASET |     |     | ThevSDNnetworkismodelledasasetofentities(nodes |     |     |     |
| ---------- | --- | --- | ---------------------------------------------- | --- | --- | --- |
The dataset was collected from a premier Internet Service and edges) interconnected by a set of links. In this work,
Provider(ISP)inwhichdifferentbandwidthutilizationtime a network is modelled as graph G(ν ,ε ) consisting
|     |     |     |     |     | SDN | SDN |
| --- | --- | --- | --- | --- | --- | --- |
series were examined. The collected data represents the ofν networknodes(i.e.,SDNswitches)connectedwith
SDN
ε
aggregatedbackbonetrafficforLongTermEvolution(LTE), SDN edges.TheSDNhypervisorsaregivenbythesetH SDN ,
MPLSandenodeBs.Datawassampledby50and350-time where H is a subset of ν . The vSDN request, r ,
|     |     |     |     | SDN | SDN | SDN |
| --- | --- | --- | --- | --- | --- | --- |
∈
steps. Each time step represents 28.8 mins, where each 50- wherer SDN R SDN (R SDN issetoftotalrequests),isestab-
time step represents one day, and 350-time steps represent lished between the SDN switches in Vr (Set of a virtual
one week. This was attributed to the limitations of the data nodeofvSDNrequest)andcontrollercr(VirtualController
cr
collection tool, while the values were interpolated and used node of vSDN request r ) at location donated by ∈
fordevelopingatimeseriesmodel.Table3showsthedataset ν . The final objective is to map the controller cr to the
SDN
| names.        |     |     | correspondingphysicalhostswitch,whichisrepresentedby |     |     |       |
| ------------- | --- | --- | ---------------------------------------------------- | --- | --- | ----- |
| VOLUME11,2023 |     |     |                                                      |     |     | 84153 |

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
FIGURE12. SlicesutilizationsinWa=2.
∀r ∈ R ,∀νr ∈ Vr ∪cr → ν .Provisioningslices The Algorithm starts with forecasting bandwidth y as a
SDN SDN SDN bt
throughthevirtualandphysicalnetworkisoutofthescope timeseriesoftimestepst insliceSL belongingtowindow
i i
ofthispaper.Algorithm1showstheresourcerequestersand W . The slices are then allocated based on their calculated
a
providerclassifications.TheAlgorithmsearchesineachtime utilizationsinu (lines5to13ofAlgorithm1)tocandidate
i
stept ∈ yinSL ∈ W ,whereyistheforecastedbandwidth requester. If the utilization is higher than the upper bound
j b i a b
fortheresourcesprovidersandresourcerequestersinslices γ and to the candidate provider else, if the utilization is
SL running on a set of already provisioned ν in lower than the lower bound β, the list of the candidate
i SDN
windowW . providersandrequestersarestoredintheslicesrequesterslist
a
84154 VOLUME11,2023

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
|     |     |     |     |     | Algorithm | 1   | Bandwidth | Slice | Requesters |     | and | Providers |
| --- | --- | --- | --- | --- | --------- | --- | --------- | ----- | ---------- | --- | --- | --------- |
Allocation
|     |     |     |     |     | Input:        | SL     | :slice,y    | :forecastedbandwidthinsliceSL |            |                     |         | ,δ:     |
| --- | --- | --- | --- | --- | ------------- | ------ | ----------- | ----------------------------- | ---------- | ------------------- | ------- | ------- |
|     |     |     |     |     |               | i      | bt          |                               |            |                     |         | i       |
|     |     |     |     |     | statistically |        | significant | smoothed                      |            | LSTM,               | Network | infras- |
|     |     |     |     |     | tructure      | of     | G(ν         | ,ε                            | ), with    | r                   | where   | r ∈     |
|     |     |     |     |     |               |        | SDN         | SDN                           |            | SDN                 |         | SDN     |
|     |     |     |     |     | R             | and    | connected   | to the                        | controller | cr,                 | given   | ∀r ∈    |
|     |     |     |     |     | SDN           |        |             |                               |            |                     |         | SDN     |
|     |     |     |     |     |               | ,∀Vr   | νr          | cr                            | ν          |                     |         |         |
|     |     |     |     |     | R SDN         |        | ∈ ∪         | →                             | SDN        | , i: index,j:       | index   | W tot : |
|     |     |     |     |     | total         | number | of          | slices,t:                     | time,      | a: index            | steps,β | :       |
|     |     |     |     |     |               | Bound, | γ :         |                               |            |                     |         |         |
|     |     |     |     |     | lower         |        |             | Higher                        | bound      | ,h:numberofresource |         |         |
provider,g:numberofresourcerequester
|     |     |     |     |     | i: index, |     | z: Count | number | of  | 100% | overutilization |     |
| --- | --- | --- | --- | --- | --------- | --- | -------- | ------ | --- | ---- | --------------- | --- |
ϵW ϵW
|     |     |     |     |     | fory | t inSL | i tot | a   |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | ------ | ----- | --- | --- | --- | --- | --- |
Output:
|     |     |     |     |     | bR{..}             | :        |           |        |                   |          | , cP{..} | :       |
| --- | --- | --- | --- | --- | ------------------ | -------- | --------- | ------ | ----------------- | -------- | -------- | ------- |
|     |     |     |     |     |                    |          | Candidate |        | Requester         |          | list     |         |
|     |     |     |     |     | Candidte           | provider |           | list , | X: Count          | number   |          | of 100% |
|     |     |     |     |     | overutilizationfor |          | y         | inSL   | ϵp (cid:91) (i)ϵW | ϵ bP{..} |          |         |
|     |     |     |     |     |                    |          | b         | t      | i m               | a        |          |         |
01:begin
02:bR{..}:←∅;
03:bP{..}←∅;
04:foralltimestepsinforecastedbandwidth
|     |     |     |     |     | slicestϵy |      | inSL ϵW | ϵW  | do //usingδ |     |     |     |
| --- | --- | --- | --- | --- | --------- | ---- | ------- | --- | ----------- | --- | --- | --- |
|     |     |     |     |     |           | j bt | i       | tot | a           |     |     |     |
05: u i ←Calculatesliceutilization
06 whileg=!0
≥γ
|     |     |     |     |     | 07  | ifu i      |     |                           |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ------------------------- | --- | --- | --- | --- |
|     |     |     |     |     | 08  | bR{..}←:SL |     | //candidateoftherequester |     |     |     |     |
i
09 Else
whileh=!0
10
|     |     |     |     |     | 11  | Ifu | ≤β  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
|     |     |     |     |     | 12  | {   | cP} ←:SL | //candidateofprovider |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------------- | --- | --- | --- | --- |
i
13 Else
14Calculatesupplyanddemandusingalgorithm2
|     |     |     |     |     |         |                                 | (cid:91) | ϵ bP{..} |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | ------------------------------- | -------- | -------- | --- | --- | --- | --- |
|     |     |     |     |     | 15forSL | i inp                           | m (i)inW | a        |     |     |     |     |
|     |     |     |     |     | 16      | X←Calculatesliceoverutilization |          |          |     |     |     |     |
IfX≥
|     |     |     |     |     | 17  |     | z   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:91)
|     |     |     |     |     | 18- |     | DropSL | ϵp (i)inW |     | frombP{..} |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --- | ---------- | --- | --- |
|     |     |     |     |     |     |     |        | i m       | a   |            |     |     |
19Loop:
CountsofoverutilizationinWa=2. Inline8,thenumberofsuppliedresourcesp (cid:91) (i)fromasetof
| FIGURE13. |     |     |     |     |     |     |     |     |     |     | m   |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
supplyslicesbP..{}iscalculatedandboundedbyconstraintsin
Equation2-5.Inaddition,thesliceutilizationafterresource
listsbR{..
bR {..}and slices providers listbP{..}, and both and donationshouldbebetweenthelowerboundβandtheupper
bP{..}willbepassedtoAlgorithm2toobtaintheamountof
|     |     |     |     |     | bound | γ. The | amount | of supplied | resources |     | requested | from |
| --- | --- | --- | --- | --- | ----- | ------ | ------ | ----------- | --------- | --- | --------- | ---- |
(cid:91)
resourcesthatwillprovidep m (i)andtheamountofrequested arequesterandprovidedbymsliceprovideriscalculatedby
| resources | rd(i). Then for | all providers | slices in the | window |          |           |             |     |                 |     |              |     |
| --------- | --------------- | ------------- | ------------- | ------ | -------- | --------- | ----------- | --- | --------------- | --- | ------------ | --- |
|           |                 |               |               |        | the cost | function, | C, provided |     | all constraints |     | in Equations | 2   |
listbP{..},
W a in the forecasted providers’ overutilization X to5aresatisfied.
| is count | number of 100% | overutilization | for the forecasted |     |     |     |     |     |     |     |     |     |
| -------- | -------------- | --------------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Xn
bandwidth( y ),ifX≥z,wherezisthecountnumberof100% min(C)= w x (1)
|     | b t |     |     |     |     |     |     |     |     | m m |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m=1
| overutilization | for all slices | SL i in window  | W a using      | actual |              |     |     |     |     |     |     |     |
| --------------- | -------------- | --------------- | -------------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
|                 | (cid:91)       |                 |                |        | Constraints: |     |     |     |     |     |     |     |
| bandwidth       | y ,p (i) will  | be dropped from | the providers’ | list   |              |     |     |     |     |     |     |     |
t m
| bP{..}toavoidbandwidthstarvation. |     |     |     |     |     |     | Xn  |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
≤p
|                                                 |     |     |     |     |     |     |     | x m | t   |     |     | (2) |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Algorithm2showssupplyanddemandcalculationswhere |     |     |     |     |     |     | m=1 |     |     |     |     |     |
Algorithm 2’s complexity is O(nmh). In line 4, the demand p (cid:91) (i)≤A (t)−S (3)
|     |     |     |     |     |     |     |     | m   | i   | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
requestersbR{..}
rd(i) is calculated from a set of slice which Xn (cid:16) (cid:91) (cid:17) Xn (cid:16) (cid:91) (cid:17)
|     |     |     |     |     |     | min | p (i)≤ | ≤x  | ≤   |     | Max p | (i) |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ----- | --- |
is limited to the values between the lower bound β and the i=1 m m i=1 m
| upperboundγ,andmostimportantly,boundedbyMax(r |     |     |     |      |     |     |     |     | ,x  | ,.....,x | ≥0  |       |
| --------------------------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | -------- | --- | ----- |
|                                               |     |     |     | t ). |     |     |     |     | x 1 | 1        | n   | (4)   |
| VOLUME11,2023                                 |     |     |     |      |     |     |     |     |     |          |     | 84155 |

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
FIGURE14. SlicesutilizationsinWa=3.
84156 VOLUME11,2023

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
Algorithm2SupplyandDemandResourceCalculation
|     |     |     |            | bR{..}   | :         |           |            |         | list, | P{..} : |
| --- | --- | --- | ---------- | -------- | --------- | --------- | ---------- | ------- | ----- | ------- |
|     |     |     | Input:     |          |           | Candidate | Requesters |         |       |         |
|     |     |     | Candidte   | provider |           | list,     | SL         | : slice |       | ,y :    |
|     |     |     |            |          |           |           |            | i       |       | b       |
|     |     |     | forecasted |          | bandwidth | in        | slice      | SL      | , i:  | index,  |
i
|     |     |     | z: Count   |           | number      | of       | 100%    | overutilization |            | in  |
| --- | --- | --- | ---------- | --------- | ----------- | -------- | ------- | --------------- | ---------- | --- |
|     |     |     | using      | y in      | SL ϵp       | (i),β    | : lower |                 | Bound,     | γ : |
|     |     |     |            | t         | i           | m        |         |                 |            |     |
|     |     |     |            | bound,    |             |          | :       |                 |            |     |
|     |     |     | Higher     |           |             | A i      | Maximum |                 | Bandwidth  |     |
|     |     |     | allocation | for       | ith slice,r |          | : total | requirement,    |            | S : |
|     |     |     |            |           |             | bt       |         |                 |            | i   |
|     |     |     | Minimum    | Bandwidth |             | Gurantee |         | for             | ithSlice,p | :   |
bt
|     |     |     | Total | resourcesfromall |     | resourceprovider |     |     |     |     |
| --- | --- | --- | ----- | ---------------- | --- | ---------------- | --- | --- | --- | --- |
(cid:91)
|     |     |     | Output:C:Costfunction,p |     |     |     | (i) : theamountofProvided |     |     |     |
| --- | --- | --- | ----------------------- | --- | --- | --- | ------------------------- | --- | --- | --- |
m
resources,rd(i):amount
|     |     |     |     |     |     | of  | resourcesRequested |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
01:begin
02:foralltimestepsinforecastedbandwidth
|     |     |     | slicestϵy |       |            | ϵW   |     |     |     |     |
| --- | --- | --- | --------- | ----- | ---------- | ---- | --- | --- | --- | --- |
|     |     |     |           | j bt  | inSL i     | a do |     |     |     |     |
|     |     |     | 03        | forSL | inbR{..}do |      |     |     |     |     |
i
|     |     |     |     |         | inβ   | ≤ byt | ≤γ,Provided |     |       |     |
| --- | --- | --- | --- | ------- | ----- | ----- | ----------- | --- | ----- | --- |
|     |     |     | 04: | s olv e | rd(i) |       |             |     | b r t |     |
|     |     |     |     |         |       | Ai +  | rd(i)       |     |       |     |
|     |     |     |     | = P     | g     |       |             |     |       |     |
i=1bi r
IfbR{..}̸=∅
05:
|     |     |     | 06: |       | Loop       |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ---------- | --- | --- | --- | --- | --- |
|     |     |     | 07: | Else  |            |     |     |     |     |     |
|     |     |     | 08: | forSL | inbP{..}do |     |     |     |     |     |
i
|     |     |     |       |       | (cid:91) |        | (β ≤         |              | byt   | ≤ γ,       |
| --- | --- | --- | ----- | ----- | -------- | ------ | ------------ | ------------ | ----- | ---------- |
|     |     |     | 09:   | Solve | p m      | (i) in |              |              |       |            |
|     |     |     |       |       |          |        |              | Ai −(cid:91) | pm(i) |            |
|     |     |     |       |       | (cid:91) |        |              |              |       | h (cid:91) |
|     |     |     | Where |       | p (i)≤A  | −S     | andprovidedp |              | =     | P p (i)    |
|     |     |     |       |       | m        | i      | i            |              | bt    | m          |
i=1
Ifp{..}̸=∅
|     |     |     | 10: |      | b    |     |     |     |     |     |
| --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- |
|     |     |     | 11: |      | Loop |     |     |     |     |     |
|     |     |     | 12: | Else |      |     |     |     |     |     |
13:SolveminC//Equation1
14:Loop
|     |     |     | The testbed    |          | is comprised | of        | five functional |        | entities  | rep-    |
| --- | --- | --- | -------------- | -------- | ------------ | --------- | --------------- | ------ | --------- | ------- |
|     |     |     | resented       | by three | VMs          | residing  | in a            | single | host, the | details |
|     |     |     | of the virtual | machines |              | are shown | in              | Table  | 5. The    | testbed |
platformwasacomputerwithCorei72.1GHZCPU,32GB
RAM,1GBnetworkinterface,64-bitwindows10operating
systemforhostmachinesandwithubuntuLinuxfortheguest
FIGURE15. CountsofoverutilizationinWa=3.
virtualizedVMs.Table5showsthetestbedVMsIPs
Xn
min(r )≤ ≤Max(r AsdepictedinFig6,theVirtualNetworkManager(VNM)
| t   | x m | t ) (5) |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
m=1 initially creates the physical network using the MININET-
ThecostfunctionandconstraintsareadoptedfromtheEnter- SDN simulator. Then, the physical network is discovered
priseVisor framework [35]. The output from Algorithm 2 is and initiated by the Libera hypervisor. The VN controller
(cid:91)
the amount of provided resources p m (i) and the amount of which is ONOS in our case is to be activated in ONOS
requestedresourcesrd(i)whichisusedbyalgorithm2forslice VM using. As soon as the physical network is activated,
allocation. LiberaestablishesmultiplevSDNsnetworkswhilemaintain-
Thisworkisbasedonextendingtheresourcemanagement ing network isolation. It has been selected as an emulation
module embedded in the EnterpriseVisor framework. Fur- platform due to its flexibility in creating VN and the ease
thermore, this paper adopts the same topology used in [35] ofuseofitsprogrammingfeatures.Eachtenant’sVNMacts
Moreover,atestbedwithLiberahypervisorisusedemulation as the operator of the VN and submits various requests to
platform.Fig5showsthetestbedcomponents. Libera.Itisworthtomentionthat,theproposedframework
Fig6showsthesequencediagramforthetestbedscenario, interacts horizontally with the traffic therefore it does not
including the interaction between the DLVisor, vSDN net- interfereverticallytothetrafficflow/trafficpathbetweenthe
workandLibera. controllersandthevSwitches(Fig5),accordinglyithasthe
VOLUME11,2023 84157

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
FIGURE16. SlicesutilizationsinWa=4.
sameFlowVisorLatencyof17mswhentheOpenFlow’snew Requestsareclassifiedintotwocategories:provisioningof
flowsprocessedanditincreaseportstatusresponselatencyby topologiesandtopologymodifications.First,theVNMstarts
roughly0.71mswhentheOpenFlow’sportstatusisrequested creatingaVNwithaspecifiedtopologyandVNentities.The
similartotheEnterpriseVisorlatency[35]. term‘‘virtualentities’’referstoallentitiesthatcomprisethe
84158 VOLUME11,2023

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
TABLE5. IPaddressoftestbed.
modifyslicesasdepictedinFig6,step6.Figure7showsthe
outputofsliceonecreation.
|     |     |     | Four | VNs were | created | in  | Libera. | Fig 7 | and 8 | show the |
| --- | --- | --- | ---- | -------- | ------- | --- | ------- | ----- | ----- | -------- |
outputofsliceonecreation.Fig7showsthecreationofslice
|     |     |     | one, representing  |               | the       | ATN-OBY           | slice          | referred     | to           | as tenant  |
| --- | --- | --- | ------------------ | ------------- | --------- | ----------------- | -------------- | ------------ | ------------ | ---------- |
|     |     |     | _id 1; the         | slice         | is mapped | to                | physical       | switches     | with         | corre-     |
|     |     |     | sponding           | switch        | IDs,      | ports, and        | links.         | In addition, |              | the slice  |
|     |     |     | is also associated |               | with      | its corresponding |                | ONOS         | Controller   |            |
|     |     |     | at 10.0.0.3        | through       | port      | 1000:             | TCP.           | Figure       | 8 shows      | more       |
|     |     |     | detailed           | log messages, |           | including         | switch         | and          | link         | establish- |
|     |     |     | ment. Figure       | 9             | shows     | the script        | that           | is used      | to modify    | the        |
|     |     |     | slice bandwidth    |               | limit     | in step           | number         | 6 in         | Fig 6        | and as a   |
|     |     |     | result of          | algorithms    | 1         | and 2.            | Fig 8          | shows        | the detailed | log        |
|     |     |     | messages           | during        | ATN-OBY   |                   | slice creation |              | shows        | the script |
usedtocontrolthetrafficqueuingdiscipline(bydefault,First
inFirstOutFIFO).Itisbasedonatrafficcontrolcommandin
Linuxthatallowsconfiguringpacketschedularinsupportof
|     |     |     | qdisc.Ontheotherhand,thetbf |        |           |     | argumentindicatesthatthe |     |         |             |
| --- | --- | --- | --------------------------- | ------ | --------- | --- | ------------------------ | --- | ------- | ----------- |
|     |     |     | token bucket                | filter | mechanism |     | controls                 | the | traffic | flow. It is |
statedherethattherateislimitedto90Mbps.TheIPERFtool
wasusedasaloadgeneratortostresstheVNslicebandwidth
V. RESULTANDDISCUSSIONS
Inthiswork,theproposedresourceallocationalgorithmcan
|     |     |     | onlyserveoneresourcerequesteratatimemax(g) |     |     |     |     |     |     | = 1,and |
| --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ------- |
themaximumnumberofresourceprovidersisfourmax(h)=
|     |     |     | 4. Therefore,  |               | priorities    | were     | assigned | to       | slice requesters. |      |
| --- | --- | --- | -------------- | ------------- | ------------- | -------- | -------- | -------- | ----------------- | ---- |
|     |     |     | The priorities |               | were assigned |          | to LTE,  | ATN-OBY, | ATN-PSD           |      |
|     |     |     | and MPLS       | respectively. |               | In order | to       | create   | a resource        | con- |
straintinnetworkbandwidth,themaximumamountoftotal
FIGURE17. CountsofoverutilizationinWa=4.
|     |     |     | requested | resources | and         | provided | were      | selected   | to  | be equal |
| --- | --- | --- | --------- | --------- | ----------- | -------- | --------- | ---------- | --- | -------- |
|     |     |     | to (r ) = | (p ).     | The maximum |          | bandwidth | limitation |     | for the  |
|     |     |     | t         | t         |             |          |           |            |     |          |
VN, such as vSwitches, ports, and links. For example, the slices is 90 Mbps for ATN-OBY and ATN-PSD, 1.43 Gbps
VNM can specify whether a vSwitch is OpenFlow, white- for MPLS slice and 1.5 Gbps for LTE slice. The maximum
box, or P4. Additionally, the VNM can construct several networkcapacityMis3.2Gbpsandthetargetutilizationrate,
ports on each virtual switch. Similarly, a virtual link can be lower utilization bound, and upper utilization bound were
|     |     |     |     |     |     |     | β   |     |     | γ   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
constructedbyconnectingtwovirtualports. selected to be ideal (u ) = 50%, = 40% and = 60%
x
| In Fig 6 after | the VNM establishes | a VN and associated | respectively. |     |     |     |     |     |     |     |
| -------------- | ------------------- | ------------------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
virtualNetworkInterfaces(NIs),thetenantoperatestheVN These values were determined empirically based on col-
via the VN controller (VNC). The VNC can configure the lected data set slices to create a situation where resource
vSwitch or virtual port by transmitting command messages providerscanexperienceresourcestarvationwhileproviding
toLiberathroughI2(controlchannel).Liberaoffersacontrol theirexcessresourcesatthecurrenttime(t )andupto(t j+n )
j
channelforeveryvirtualswitch.GiventhatthevSwitchonly wherenisthenumberofforecastedtimesteps.
belongs to one VN, each VN’s control messages are routed Fig10showstheutilizationofATN-OBY,ATN-PSD,LTE,
separately to Libera. For Flow rules (FRs), the VNC can and MPLS slices respectively, with and without a resource
installdesiredFRstoanyvSwitchatanytime,therebyallow- allocationusingthedynamiclearningframework(DLF)for
|     |     |     |     |     |     |     |     | tϵy |     | ϵW  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ing packets to be dynamically forwarded or dropped. Addi- all time steps in window 1 provided j bt in SL i a (a =
tionally, the Libera collects statistical data from vSwitches 1andj=1to50,i.e.,thefirst50timesteps);wheretheblue
and virtual ports. Accordingly, DLVisor can reconfigure or lineinthegraphshowstheactual(original)sliceutilization
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     | 84159 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
FIGURE18. SlicesutilizationsinWa=5.
withoutusingtheresourceallocationalgorithmthatwasused otherrequestedsliceslikeLTE,sinceLTEsliceutilizationis
as benchmark in this research. In window one and based morethantheupperboundu ≥γ,whereγ =60%andother
i
on slice utilization, ATN-OBY slice, ATN-PSD slice, and sliceutilizationsarelessthanthelowerboundu ≤β where
i
MPLS slice are considered as resource providers due to its β = 40%attargetutilization(u ) =50%;providedthatall
x
low utilization u ≤ β, whereas LTE slice is considered a boundsandconstraintsaresatisfiedinEquations1to5.The
i
resourcerequesteru ≥γ. orangelinedepictsthenewlyutilizationwithoutDLF.
i
Intimestep1andAccordingtoalgorithms1and2,ATN- Fig 10a shows that slice utilization without DLF exceeds
OBY,ATN-PSD,andMPLSsliceswillprovideresourcesto thefullutilizationof100%,whichcausestheslicetostarve
84160 VOLUME11,2023

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
ourproposedDLF.ThesameanalysisisappliedtotheATN-
PSD slice in Fig 10b. Meanwhile, in the MPLS slice, the
utilization in resource allocation with DLF is increased due
toextraresourcesprovidedtotherequestertocompensatethe
lostresourcesfromdroppedATN-OBYandATN-PSDslices.
Fig 11 shows the count of times that the slice utiliza-
tion exceeds the 100% utilization for ATN-OBY (a) and
ANT-PSDin(b).
In Fig 11a, the ATN-OBY slice is overutilized 27 times
more than when using the original (without resource allo-
cation) and when using our DLF, confirming the proposed
algorithm’s effectiveness. However, in the ATN-PSD slice,
the resource allocation without DLF introduces overutiliza-
tion30timesmorethanDLF.Fig12showsthesliceutiliza-
tion for window 2 for all tϵy in SL ϵW (a = 2 and j =
j bt i a
51to100). Likewise, the graph shows the actual (origi-
nal) slice utilization without using the resource allocation
algorithmandwithoutDLF.
In window 2, ATN-OBY at time steps 51 and 53 was a
resource provider when allocation without DLF was used.
This is due to its low utilization, β < 40% (blue box).
Nevertheless, at step 56, the slice requests a resource as
the utilization is higher than the upper bound, γ > 60%.
In addition, the ATN-OBY slice is a resource requester at
time step 66 using resource allocation with DLF. On the
other hand, the ATN-PSD slice at time steps 53 and 56 is
respectivelyaresourceproviderandresourcerequesterwhen
using allocation without DLF (blue box) and with DLF
(orange box) respectively. In both ATN-OBY and ATN-
PD, the orange line shows that slice utilization exceeds the
full utilization of 100%, which causes the slice to starve
for resources due to the inability to recover the provided
(donated) resources that are in use. This is mainly due to
applyingtheresourceallocationalgorithminthebenchmark
in real-time without considering the future demands. The
yellow line indicates slice utilization using our proposed
DLF. Unlike the resource allocation without using DLF in
yellow, the resource allocation using DLF does not cause
overutilization(Bandwidthutilization).Thisismainlydueto
theslicesbeingdroppedfromresourceproviders’candidate
FIGURE19. CountsofoverutilizationinWa=5. listbP{..} since demand and supply calculation for the next
50-timestepsrevealsresourcestarvationwhenusingresource
for resources due to the inability to recover the provided allocation without DLF (the orange graph). On the other
(donated)resourcesbecauseofotherslicesutilizations.This hand,theLTEsliceisaresourcerequesterandtherequested
is mainly due to applying the resource allocation algorithm resources in allocation without DLF are provided by the
inthebenchmark(EnterpriseVisor)inreal-timewithoutcon- ATN-OBY slice at time step 51 and from all other slices
sidering the future demands. From the other side, in our at time step 53. This is obvious in the sharp drop in the
proposed algorithm’s supply and demand resource alloca- consumed resources at time step 53. Meanwhile, a higher
tion,thecalculationsarebasedonfutureforecastedresource amountofresourceswereprovidedbytheMPLSslice,which
consumption(highlightedinyellowline).Therefore,thereis is reflected in a higher rise in consumed resources when
priorknowledgeofwhethertherewillberesourcestarvation using the allocation with DLF. The sharp increase in result
or not before deciding not to consider (drop) the resource was to compensate for the number of resources that were
provider(doner)frombeingconsideredasacandidatefora initiallyprovidedbythedroppedslice(ATN-OBYsliceand
resourceproviderbP{..}.Theyellowlineshowsthattheslice ATN-PSD slice). Fig 13a and Fig 13b show the count of
utilization is kept the same as the original slice utilization times the slice utilization exceeds the 100% utilization for
since the slice is not considered a slice provider after using theATN-OBYsliceandtheATN-PSDslicerespectively.
VOLUME11,2023 84161

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
| FIGURE20. | SlicesutilizationsinWa=6. |     |     |     |
| --------- | ------------------------- | --- | --- | --- |
No slice overutilization was observed using the pro- algorithms. Fig 14 shows slice utilization for window 3 for
posed DLF compared to the original resource allocation all tϵy in SL ϵW (a = 3 and j = 101 to 150) with and
j bt i a
| without DLF, | confirming | the effectiveness | of the proposed | withoutDLF. |
| ------------ | ---------- | ----------------- | --------------- | ----------- |
84162 VOLUME11,2023

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
|     |     |     |     | consider | (drop) | the resource |     | provider | (doner) |     | from being |
| --- | --- | --- | --- | -------- | ------ | ------------ | --- | -------- | ------- | --- | ---------- |
consideredasacandidateforaresourceproviderbP{..}.The
yellowlineshowsthatthesliceutilizationiskeptthesameas
theoriginalsliceutilizationsincethesliceisnotconsidered
|     |     |     |     | a slice provider |     | after | using | our proposed |     | DLF. | The same |
| --- | --- | --- | --- | ---------------- | --- | ----- | ----- | ------------ | --- | ---- | -------- |
analysisisappliedtotheATN-OBYslicefortimesteps100to
120.Theaboveresourceallocationresultsshowthatresource
|     |     |     |     | allocation | using | DLF | (yellow | line) | reduced | overutilization |     |
| --- | --- | --- | --- | ---------- | ----- | --- | ------- | ----- | ------- | --------------- | --- |
comparedtoothers.Figs15aandFigs15bshowthecountof
timesthesliceutilizationexceedsthe100%utilizationmark
fortheATN-OBYsliceandATN-PSDslicerespectively.
|     |     |     |     | From | Fig 15a | and Fig | 15b, | resource | allocation |     | with DLF |
| --- | --- | --- | --- | ---- | ------- | ------- | ---- | -------- | ---------- | --- | -------- |
reducedthecountof100%overutilizationfortheATN-OBY
sliceandmaintainedtheexactcountcomparedtotheoriginal
|     |     |     |     | ratio for    | the ATN-PSD |             | slice.      | In contrast |            | to the | ATN-OBY     |
| --- | --- | --- | --- | ------------ | ----------- | ----------- | ----------- | ----------- | ---------- | ------ | ----------- |
|     |     |     |     | slice, the   | proposed    | resource    |             | allocation  | with       | DLF    | improved    |
|     |     |     |     | the resource | allocation  |             | by reducing |             | the number |        | of overuti- |
|     |     |     |     | lization     | counts      | as depicted |             | in Fig      | 15b. Fig   | 16     | shows slice |
|     |     |     |     | utilization  | for window  |             | 4 for       | all tϵy     | in SL      | ϵW     | (a = 4 and  |
|     |     |     |     |              |             |             |             | j bt        |            | i a    |             |
j=151to200)withandwithoutDLF.
|     |     |     |     | In Fig            | 16, the      | LTE                              | slice       | is a         | resource     | requester | since      |
| --- | --- | --- | --- | ----------------- | ------------ | -------------------------------- | ----------- | ------------ | ------------ | --------- | ---------- |
|     |     |     |     | γ > 60%,          | whereas      |                                  | the ATN-OBY |              | and          | ATN-PSD   | slices     |
|     |     |     |     | provide           | resources    | to the                           | LTE         | slice        | at step      | 151 (due  | to their   |
|     |     |     |     | lowutilizationofβ |              | <40%inthebluebox).Thiseventually |             |              |              |           |            |
|     |     |     |     | leads to          | resource     | starvation                       |             | for ATN-OBY, |              | and       | ATN-PSD    |
|     |     |     |     | slices as         | depicted     | in                               | the orange  | line         | in           | Figs 16a  | and 16b    |
|     |     |     |     | respectively.     | In           | contrast,                        | when        | using        | DLF,         | since     | the supply |
|     |     |     |     | and demand        | resource     |                                  | allocation  | were         | based        | on        | forecasted |
|     |     |     |     | resource          | consumption, |                                  | both        | slices       | are exempted |           | from the   |
resourceproviders’listbP{..}asillustratedbytheyellowline
|     |     |     |     | in Figs 16a | and | 16b. | Accordingly, |     | there is | prior | knowledge |
| --- | --- | --- | --- | ----------- | --- | ---- | ------------ | --- | -------- | ----- | --------- |
ofwhethertherewillbearesourcestarvationsornot,before
decidingnottoconsider(drop)theresourceprovider(doner)
asacandidateforaresourceprovider.Theyellowlineshows
|     |     |     |     | that the          | slice | utilization | is        | kept the | same           | as  | the original |
| --- | --- | --- | --- | ----------------- | ----- | ----------- | --------- | -------- | -------------- | --- | ------------ |
|     |     |     |     | slice utilization |       | since       | the slice | is       | not considered |     | a slice      |
providerafterusingtheproposedDLF.Conversely,theMPLS
|     |     |     |     | slice provides |     | resource | to the | LTE | slice | at steps | 153 and |
| --- | --- | --- | --- | -------------- | --- | -------- | ------ | --- | ----- | -------- | ------- |
155respectively.Ontheotherhand,regardingresourceallo-
|                                          |     |     |     | cation with | DLF, | ATN-OBY |     | slice | receives | resources | from |
| ---------------------------------------- | --- | --- | --- | ----------- | ---- | ------- | --- | ----- | -------- | --------- | ---- |
| FIGURE21. CountsofoverutilizationinWa=6. |     |     |     |             |      |         |     |       |          |           |      |
LTEsliceatstep162.Itisevidentthattheresourceallocation
|     |     |     |     | with DLF | reduces | the | overall | utilization |     | and the | count of |
| --- | --- | --- | --- | -------- | ------- | --- | ------- | ----------- | --- | ------- | -------- |
In this window, ATN-OBY and ATN-PSD slices pro- overutilization.Fig17aandFig17bshowthenumberoftimes
vide resources from 100–105-time steps to LTE slice thatthesliceutilizationexceedsthe100%utilizationmarkfor
without using DLF due to their low utilization β < ATN-OBYandATN-PSDslicesrespectively.
40%(blue box). Form other side, at time step 120, ATN- FromFig17aandFig17b,resourceallocationusingDLF
OBY requests a resource in which LTE and MPLS slices in ATN-OBY slice reduces the overutilization count com-
providesinceATN-OBY’sutilizationareapproaching100% pared to the original and allocation without DLF. Likewise,
utilization(inblue-original)
and(inyellowwithDLF).Con- in the ATN-PSD slice, the allocation using DLF reduces
versely, due to its low utilization β<40%, the MPLS slice the overutilization to zero, similar to the actual utiliza-
provides resources at time steps 104 and 106 to the LTE tion. Fig 18 shows slice utilization for window 5 for all
slice. In this window, the ATN-PSD slice does not provide tϵy inSL ϵW (a=5andj=201to250)withandwithout
|               |         |            |                       | j bt | i a |     |     |     |     |     |     |
| ------------- | ------- | ---------- | --------------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| any resources | because | the supply | and demand allocation | DLF. |     |     |     |     |     |     |     |
calculationswerebasedonforecastedresourceconsumption. In Fig 18, the ATN-OBY, ATN-PSD, and MPLS slices
Therefore, there will is prior knowledge of whether there (due to their low utilization β < 40% in the blue box)
will be resource starvation or not before deciding not to provide resources to the LTE slice at time step 201 since
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     | 84163 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
FIGURE22. SlicesutilizationsinWa=6.
LTEisaresourcerequesterwithγ > 60%.Thiseventually forecasted resource consumption; both slices are exempted
leads to resource starvation for ATN-OBY, and ATN-PSD fromtheresourceproviderslistbP{..}.Thisexplainsthelow
as depicted in the red line in Figs 18a and 18b. Meanwhile, utilization in ATN-OBY and ATN-PSD (in yellow aligned
forresourceallocationusingDLF,theMPLSsliceonlypro- with the actual utilization). On the other hand, ATN-OBY
vides the requested resources and compensates the dropped also requested resources at time step 210 provided by LTE
resources from ATN-OBY and ATN-PSD since the supply slice. ATN-PSD also requested resources at time step 212,
and demand resource allocation calculations were based on whichLTEalsoprovided.Figs19aand19bshowthecount
84164 VOLUME11,2023

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
showthecountoftimesthatthesliceutilizationexceedsthe
100%utilizationfortheATN-OBYsliceandATN-PSDslice,
respectively.
|     |     |     |     |     |     |     | In Fig | 21, | ATN-PSD | resource |     | allocation | significantly |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------- | -------- | --- | ---------- | ------------- | --- |
improvedoverutilizationcomparedtotheallocationwithout
|     |     |     |     |     |     |     | DLF. Fig | 22 shows | slice                            | utilization |     | for | window | 7 for all |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | -------------------------------- | ----------- | --- | --- | ------ | --------- |
|     |     |     |     |     |     |     | tϵy inSL | ϵW       | (a=7andj=300to350)withandwithout |             |     |     |        |           |
|     |     |     |     |     |     |     | j bt     | i a      |                                  |             |     |     |        |           |
theDLF.
Inwindows7,onlytheMPLSslicewithβ<40%provides
γ >60%.
|     |     |     |     |     |     |     | resources | to LTE | with |     | Meanwhile |     | the ATN-OBY |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ---- | --- | --------- | --- | ----------- | --- |
andATN-PSDslicesdonotprovideorreceiveanyresources.
|     |     |     |     |     |     |     | Fig 23a     | and 23b | show | the  | count       | of times | that            | the slice |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ---- | ---- | ----------- | -------- | --------------- | --------- |
|     |     |     |     |     |     |     | utilization | exceeds | the  | 100% | utilization |          | for the ATN-OBY |           |
andATN-PSDslicesrespectively.
Inoverall,DLVisorcanimproveresourceallocationcom-
paredtoourbenchmark(EnterpriseVisor)by
1- ReducingandeliminatingsliceoverutilizationinEnter-
priseVisor
|     |     |     |     |     |     |     | 2- Reduce |     | resource | starvation |     | resulted | from | resource |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | ---------- | --- | -------- | ---- | -------- |
donationperformedbytheresourcemanagementmod-
uleintheEnterpriseVisor
3- ImprovingtheoverallvSDNsliceutilization
VI. CONCLUSION
|     |     |     |     |     |     |     | In conclusion, |                  | the paper | shows      | the         | development | and          | imple-     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ---------------- | --------- | ---------- | ----------- | ----------- | ------------ | ---------- |
|     |     |     |     |     |     |     | mentation      | of methods       |           | for the    | slice       | (bandwidth) |              | resource   |
|     |     |     |     |     |     |     | management     | in               | vSDN.     | It was     | found       | that        | resource     | man-       |
|     |     |     |     |     |     |     | agement        | and bandwidth    |           | resource   | allocation, |             | particularly | in         |
|     |     |     |     |     |     |     | the current    | actual           | time,     | can        | lead to     | resource    | starvation   | due        |
|     |     |     |     |     |     |     | to resource    | overutilization; |           | especially |             | given       | that         | the calcu- |
|     |     |     |     |     |     |     | lation of      | the resource     |           | supply     | and         | demand      | in the       | related    |
resourcemanagementsolutionsdidnottakefuturedemands
andrapidchangesintrafficprofilesintoaccount.Therefore,
|     |     |     |     |     |     |     | proactive, | intelligent | resource |     | management |     | frameworks | are |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | -------- | --- | ---------- | --- | ---------- | --- |
CountsofoverutilizationinWa=7. needed. Thus, accurate and robust resource (traffic) fore-
FIGURE23.
|     |     |     |     |     |     |     | casting   | algorithms | are       | crucial. | Accordingly, |           | DLVisor | was  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --------- | -------- | ------------ | --------- | ------- | ---- |
|     |     |     |     |     |     |     | developed | with       | a dynamic | learning |              | framework | which   | com- |
oftimesthatthesliceutilizationexceedsthe100%utilization binessmooth-aidedMLalgorithmstolearn(forecast)future
forATN-OBYandATN-PSD,respectively demands. It reacts and adapts to any significant changes in
From Fig 19, the resource management using DLF out- trafficprofileusingconceptchangesdetectorsandsignificant
performresourceallocationwithoutDLFandimprovesslice tests. The window-basedmethods were employed toreduce
utilizationforbothresourceprovidersATN-OBYandATN- or eliminate the fluctuations in the data traffic, which can
PSDslices.Fig20showssliceutilizationforwindow6forall
|     |     |     |     |     |     |     | deteriorate | the | ML performance |     | as  | per | the previous | stud- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | --- | --- | --- | ------------ | ----- |
| ϵ   | ϵW  |     |     |     |     |     |             |     |                |     |     |     |              |       |
t y inSL (a=6andj=251to300)withandwithout ies. Finally, the improved dynamic learning framework are
| j b t | i a |     |     |     |     |     |         |        |          |            |     |           |     |         |
| ----- | --- | --- | --- | --- | --- | --- | ------- | ------ | -------- | ---------- | --- | --------- | --- | ------- |
| DLF.  |     |     |     |     |     |     | applied | to the | resource | management |     | framework | to  | provide |
In Fig 20, in Window 6 at time step 251 and without improvedresourcesutilizationandeliminatetheoverutiliza-
DLF, the ATN-PSD and the MPLS slices (due to their low tionresultingfromformthesupplyanddemandcalculations.
| utilization    | β < | 40% in                          | the blue | box) provide | resources | to  |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------------------------- | -------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTEslicesinceγ |     | >60%.Meanwhile,usingDLFandgiven |          |              |           |     |     |     |     |     |     |     |     |     |
REFERENCES
thatthesupplyanddemandresourceallocationcalculations [1] A.Blenk,A.Basta,M.Reisslein,andW.Kellerer,‘‘Surveyonnetworkvir-
tualizationhypervisorsforsoftwaredefinednetworking,’’IEEECommun.
| are based | on forecasted |      | resource | consumption,       |     | ATN-PSD     |           |                 |              |               |              |             |                   |            |
| --------- | ------------- | ---- | -------- | ------------------ | --- | ----------- | --------- | --------------- | ------------ | ------------- | ------------ | ----------- | ----------------- | ---------- |
|           |               |      |          |                    |     |             | S u rv e  | y s T u t s. ,v | o l .1 8 , n | o. 1 , p p .  | 6 5 5– 6 8 5 | , 1 st Q ua | rt ., 2 0 1 6 .   |            |
| slice was | exempted      | from | the      | resource providers |     | list bP{..} |           |                 |              |               |              |             |                   |            |
|           |               |      |          |                    |     |             | [2] A . K | i v it y , Y .  | K a m a y ,  | D . L a o r , | U . L u b li | n , an d    | A . L i g u o ri, | ‘‘kvm: The |
(Yellowlinealignedwiththeactual)asinFig20b.Thus,the
Linuxvirtualmachinemonitor,’’inProc.LinuxSymp.,Canada,America,
Jun.2007,pp.225–230.
MPLScompensatesforthelostamountwithextraresources.
|     |     |     |     |     |     |     | [3] C. A. | Waldspurger, | ‘‘Memory |     | resource | management | in VMware | ESX |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | -------- | --- | -------- | ---------- | --------- | --- |
ThisjustifiestheelevatedutilizationinMPLSforallocation
|               |         |       |        |          |         |         | server,’’ | ACM | SIGOPS | Operating | Syst. | Rev., | vol. 36, | pp.181–194, |
| ------------- | ------- | ----- | ------ | -------- | ------- | ------- | --------- | --- | ------ | --------- | ----- | ----- | -------- | ----------- |
| using DLF     | (Yellow | line) | in Fig | 20d. Fig | 21a and | Fig 21b | Dec.2002. |     |        |           |       |       |          |             |
| VOLUME11,2023 |         |       |        |          |         |         |           |     |        |           |       |       |          | 84165       |

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
[4] A.A.Blenk,‘‘Towardsvirtualizationofsoftware-definednetworks:Anal- [26] N.Feamster,J.Rexford,andE.Zegura,‘‘TheroadtoSDN:Anintellectual
ysis,modeling,andoptimization,’’Dept.Electron.Inf.Technol.,Technis- historyofprogrammablenetworks,’’ACMSIGCOMMComput.Commun.
cheUniversitätMünchen,Munich,Germany,Tech.Rep.21.11.2017,2018. Rev.,vol.44,no.2,pp.87–98,Apr.2014.
[5] F. Rodríguez-Haro, F. Freitag, L. Navarro, E. Hernánchez-sánchez, [27] R.Sherwood,M.Chan,A.Covington,G.Gibb,M.Flajslik,N.Handigol,
N.Farías-Mendoza, J. A. Guerrero-Ibáñez, and A. González-Potes, T.-Y. Huang, P. Kazemian, M. Kobayashi, J. Naous, S. Seetharaman,
‘‘A summary of virtualization techniques,’’ Proc. Technol., vol. 3, D.Underhill,T.Yabe,K.-K.Yap,Y.Yiakoumis,H.Zeng,G.Appenzeller,
pp.267–272,Jan.2012. R.Johari,N.McKeown,andG.Parulkar,‘‘Carvingresearchslicesout
[6] T. Anderson, L. Peterson, S. Shenker, and J. Turner, ‘‘Overcoming ofyourproductionnetworkswithOpenFlow,’’ACMSIGCOMMComput.
the Internet impasse through virtualization,’’ Computer, vol. 38, no. 4, Commun.Rev.,vol.40,no.1,pp.129–130,Jan.2010.
pp.34–41,Apr.2005. [28] R. Sherwood, G. Gibb, K.-K. Yap, G. Appenzeller, M. Casado,
[7] M.Yu,J.Rexford,X.Sun,S.Rao,andN.Feamster,‘‘Asurveyofvirtual N.McKeown, and G. Parulkar, ‘‘Flowvisor: A network virtualization
LANusageincampusnetworks,’’IEEECommun.Mag.,vol.49,no.7, layer,’’OpenFlowSwitchConsortium,vol.1,p.132,Oct.2009.
pp.98–103,Jul.2011. [29] N. Van Giang and Y. H. Kim, ‘‘Slicing the next mobile packet core
[8] A.Belbekkouche,Md.M.Hasan,andA.Karmouch,‘‘Resourcediscovery network,’’ in Proc. 11th Int. Symp. Wireless Commun. Syst. (ISWCS),
andallocationinnetworkvirtualization,’’IEEECommun.SurveysTuts., Aug.2014,pp.901–904.
vol.14,no.4,pp.1114–1128,4thQuart.,2012. [30] X.Jin,J.Rexford,andD.Walker,‘‘Incrementalupdateforacompositional
[9] R. Boutaba, M. A. Salahuddin, N. Limam, S. Ayoubi, N. Shahriar, SDNhypervisor,’’inProc.3rdWorkshopHotTopicsSoftw.DefinedNetw.,
F.Estrada-Solano, and O. M. Caicedo, ‘‘A comprehensive survey on Aug.2014,pp.187–192.
machine learning for networking: Evolution, applications and research [31] A.Al-Shabibi,M.DeLeenheer,M.Gerola,A.Koshibe,W.Snow,and
opportunities,’’ J. Internet Services Appl., vol. 9, no. 1, pp.1–99, G.Parulkar,‘‘OpenVirteX:Anetworkhypervisor,’’inProc.OpenNetw.
Dec.2018. Summit(ONS),2014,pp.1–9.
[10] M. H. H. Khairi, S. H. S. Ariffin, N. M. A. Latiff, K. M. Yusof, [32] R.Doriguzzi-Corin,E.Salvadori,M.Gerola,M.Suñé,andH.Woesner,
M.K.Hassan, F. T. Al-Dhief, M. Hamdan, S. Khan, and M. Hamzah, ‘‘Adatapath-centricvirtualizationmechanismforOpenFlownetworks,’’
‘‘Detection and classification of conflict flows in SDN using machine inProc.3rdEur.WorkshopSoftw.DefinedNetw.,Sep.2014,pp.19–24.
learningalgorithms,’’IEEEAccess,vol.9,pp.76024–76037,2021. [33] X.Jin,J.Gossels,J.Rexford,andD.Walker,‘‘CoVisor:Acompositional
[11] K. Z. Ghafoor, L. Kong, D. B. Rawat, E. Hosseini, and A. S. Sadiq, hypervisorforsoftware-definednetworks,’’inProc.12thUSENIXSymp.
‘‘Qualityofserviceawareroutingprotocolinsoftware-definedInternetof NetworkedSyst.DesignImplement.(NSDI),2015,pp.87–101.
Vehicles,’’IEEEInternetThingsJ.,vol.6,no.2,pp.2817–2828,Apr.2019. [34] L.Liao,A.Shami,andV.C.M.Leung,‘‘DistributedFlowVisor:Adis-
[12] M. K. Hassan, S. H. Ariffin, S. K. Syed-Yusof, N. E. Ghazali, and tributedFlowVisorplatformforqualityofserviceawarecloudnetwork
M.E.Kanona,‘‘Analysisofhybridnon-linearautoregressiveneuralnet- virtualisation,’’IETNetw.,vol.4,no.5,pp.270–277,Sep.2015.
work and local smoothing technique for bandwidth slice forecast,’’ [35] J.-L.Chen,Y.-W.Ma,H.-Y.Kuo,C.-S.Yang,andW.-C.Hung,‘‘Software-
TELKOMNIKA,Telecommun.Comput.Electron.Control,vol.19,no.4, definednetworkvirtualizationplatformforenterprisenetworkresource
pp.1078–1089,2021. management,’’ IEEE Trans. Emerg. Topics Comput., vol. 4, no. 2,
[13] M. Alauthman, N. Aslam, M. Al-kasassbeh, S. Khan, A. Al-Qerem, pp.179–186,Apr.2016.
and K.-K.R.Choo, ‘‘An efficient reinforcement learning-based Bot- [36] Y.Han,J.Li,D.Hoang,J.-H.Yoo,andJ.W.Hong,‘‘Anintent-based
net detection approach,’’ J. Netw. Comput. Appl., vol. 150, Jan. 2020, networkvirtualizationplatformforSDN,’’inProc.12thInt.Conf.Netw.
Art.no.102479. ServiceManage.(CNSM),Oct.2016,pp.353–358.
[14] X.Li,S.Li,P.Zhou,andG.Chen,‘‘Forecastingnetworkinterfaceflow [37] H.Yamanaka,E.Kawai,andS.Shimojo,‘‘AutoVFlow:Virtualizationof
usingabroadlearningsystembasedonthesparrowsearchalgorithm,’’ large-scalewide-areaOpenFlownetworks,’’Comput.Commun.,vol.102,
Entropy,vol.24,no.4,p.478,Mar.2022. pp.28–46,Apr.2017.
[15] A.R.AbdellahandA.Koucheryavy,‘‘VANETtrafficpredictionusing [38] H. Yamanaka, E. Kawai, S. Ishii, and S. Shimojo, ‘‘AutoVFlow:
LSTMwithdeepneuralnetworklearning,’’inProc.Int.Conf.NextGener. Autonomousvirtualizationforwide-areaOpenFlownetworks,’’inProc.
Wired/WirelessNetw.Cham,Switzerland:Springer,2020,pp.281–294. 3rdEur.WorkshopSoftw.DefinedNetw.,Sep.2014,pp.67–72.
[16] S. K. Singh, M. M. Salim, J. Cha, Y. Pan, and J. H. Park, ‘‘Machine [39] Y. Han, T. Vachuska, A. Al-Shabibi, J. Li, H. Huang, W. Snow, and
learning-basednetworksub-slicingframeworkinasustainable5Genvi- J.W.-K.Hong, ‘‘ONVisor: Towards a scalable and flexible SDN-based
ronment,’’Sustainability,vol.12,no.15,p.6250,Aug.2020. networkvirtualizationplatformonONOS,’’Int.J.Netw.Manage.,vol.28,
[17] M. Berman, J. S. Chase, L. Landweber, A. Nakao, M. Ott, no.2,p.e2012,Mar.2018.
D.Raychaudhuri, R. Ricci, and I. Seskar, ‘‘GENI: A federated testbed [40] S.Agliano,M.Ashjaei,M.Behnam,andL.L.Bello,‘‘Resourceman-
forinnovativenetworkexperiments,’’Comput.Netw.,vol.61,pp.5–23, agementandcontrolinvirtualizedSDNnetworks,’’inProc.Real-Time
Mar.2014. EmbeddedSyst.Technol.(RTEST),2018,pp.47–53.
[18] H.Ishio,J.Minowa,andK.Nosu,‘‘Reviewandstatusofwavelength- [41] V. Struhár, M. Ashjaei, M. Behnam, S. S. Craciunas, and
division-multiplexingtechnologyanditsapplication,’’J.Lightw.Technol., A.V.Papadopoulos,‘‘DART:Dynamicbandwidthdistributionframework
vol.2,no.4,pp.448–463,Aug.1984. for virtualized software defined networks,’’ in Proc. 45th Annu. Conf.
[19] X.Xiao,A.Hannan,B.Bailey,andL.M.Ni,‘‘Trafficengineeringwith IEEEInd.Electron.Soc.(IECON),vol.1,Oct.2019,pp.2934–2939.
MPLSintheInternet,’’IEEENetw.,vol.14,no.2,pp.28–33,Apr.2000. [42] L.Leonardi,L.LoBello,andS.Aglianó,‘‘Priority-basedbandwidthman-
[20] A. Leon-Garcia and L. G. Mason, ‘‘Virtual network resource manage- agement in virtualized software-defined networks,’’ Electronics, vol. 9,
mentfornext-generationnetworks,’’IEEECommun.Mag.,vol.41,no.7, no.6,p.1009,Jun.2020.
pp.102–109,Jul.2003. [43] G.Yang,B.-Y.Yu,H.Jin,andC.Yoo,‘‘Liberaforprogrammablenetwork
[21] T.Koponen,K.Amidon,P.Balland,M.Casado,A.Chanda,B.Fulton, virtualization,’’IEEECommun.Mag.,vol.58,no.4,pp.38–44,Apr.2020.
I.Ganichev,J.Gross,P.Ingram,E.Jackson,andA.Lambeth,‘‘Network [44] G.Yang,Y.Yoo,M.Kang,H.Jin,andC.Yoo,‘‘Bandwidthisolationguar-
virtualizationinmulti-tenantdatacenters,’’inProc.11thUSENIXSymp. anteeforSDNvirtualnetworks,’’inProc.IEEEConf.Comput.Commun.
NetworkedSyst.DesignImplement.(NSDI),2014,pp.203–216. (INFOCOM),May2021,pp.1–10.
[22] S.Shenker,L.Peterson,andJ.Turner,‘‘OvercomingtheInternetimpasse [45] A.AhmadianandM.Ahmadi,‘‘DC-CAMP:Dynamiccontrollercreation,
throughvirtualization,’’inProc.ACMHotNets-III,2004,pp.1–8. allocationandmanagementprotocolinSDN,’’WirelessPers.Commun.,
[23] H. Ballani, P. Costa, T. Karagiannis, and A. Rowstron, ‘‘Towards pre- vol.125,pp.531–558,Feb.2022.
dictabledatacenternetworks,’’inProc.ACMSIGCOMMConf.,Aug.2011, [46] M.K.Hassan,S.H.SyedAriffin,N.E.Ghazali,M.Hamad,M.Hamdan,
pp.242–253. M.Hamdi,H.Hamam,andS.Khan,‘‘Dynamiclearningframeworkfor
[24] D.Drutskoy,E.Keller,andJ.Rexford,‘‘Scalablenetworkvirtualization smooth-aided machine-learning-based backbone traffic forecasts,’’ Sen-
in software-defined networks,’’ IEEE Internet Comput., vol. 17, no. 2, sors,vol.22,no.9,p.3592,May2022.
pp.20–27,Mar.2013. [47] G. Sun, K. Xiong, G. O. Boateng, G. Liu, and W. Jiang, ‘‘Resource
[25] R.JainandS.Paul,‘‘Networkvirtualizationandsoftwaredefinednetwork- slicing and customization in RAN with dueling deep Q-network,’’
ingforcloudcomputing:Asurvey,’’IEEECommun.Mag.,vol.51,no.11, J. Netw. Comput. Appl., vol. 157, May 2020, Art.no.102573, doi:
pp.24–31,Nov.2013. 10.1016/j.jnca.2020.102573.
84166 VOLUME11,2023

M.K.Hassanetal.:DLVisor:DynamicLearningHypervisorforSoftwareDefinedNetwork
MOHAMED KHALAFALLA HASSAN received MOHAMMED E. A. KANONA received the
the B.Sc. degree in computer engineering from B.Sc.,M.Sc.,andPh.D.degreesintelecommuni-
FutureUniversity,Sudan,in2004,andtheM.Sc. cationengineeringfromFutureUniversity,Sudan.
degree in communication network engineering He is currently the Deputy Dean of the Fac-
fromUniversityPutraMalaysia(UPM),in2009. ulty of Telecommunication and Space Technol-
HeiscurrentlypursuingthePh.D.degreeincom- ogy and the Head of the IoT Research Center.
municationengineeringwithUniversityTechnol- He actively involved in research about forward
ogy Malaysia (UTM). He is also an Associate scattering radar. His research interests include
Professor with Future University. He is also a informationtheory,SDN,theIoT,cloudcomput-
researcherandanICTspecialistwith17yearsof ing, machine learning and neural networks, and
wide range of research and ICT experience. He has published 20 papers mobilecommunication.HereceivedtheBestPaperAwardfromICCCEEE20
| ininternationalpeer-reviewedconferencesandjournals.Hisresearchinter- |     |     |     |     | Conference. |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
estsincludeforwardsscatteringradar,machinelearning,NFV,vSDN,and
resourcesmanagementincommunicationnetworks.
|     |     |     |     |     |     | KHALID | S. MOHAMED |     | (Member, IEEE) |
| --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | -------------- |
receivedthebachelor’sdegreeintelecommunica-
|     |     |     |     |     |     | tion engineering |     | from Future | University, Sudan, |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | ------------------ |
in2011,andtheMasterofEngineeringdegreein
|     |     |     |     |     |     | telecommunication |                      | and the Ph.D. | (Engineering)     |
| --- | --- | --- | --- | --- | --- | ----------------- | -------------------- | ------------- | ----------------- |
|     |     |     |     |     |     | degree            | in telecommunication |               | from Multimedia   |
|     |     |     |     |     |     | University,       | Malaysia,            | in 2014       | and 2020, respec- |
SHARIFAH HAFIZAH SYED ARIFFIN (Senior tively.HehasbeenregisteredwiththeSudanese
Member, IEEE) received the B.Eng. degree Engineering Council (SEC) as a Professional
|     | (Hons.) in | London, in 1997, | the M.E.E. | degree |     |           |               |       |                  |
| --- | ---------- | ---------------- | ---------- | ------ | --- | --------- | ------------- | ----- | ---------------- |
|     |            |                  |            |        |     | Engineer, | since January | 2022, | and the Board of |
fromUniversitiTeknologiMalaysia,in2001,and
EngineersMalaysia(BEM)asaGraduateEngineer,sinceApril2019.Heis
thePh.D.degreefromtheQueenMary,University
|     |     |     |     |     | currently an Assistant | Professor | with the | Faculty of | Telecommunication |
| --- | --- | --- | --- | --- | ---------------------- | --------- | -------- | ---------- | ----------------- |
ofLondon,London,in2006.Sheiscurrentlyan andSpaceTechnologyandtheActingDirectoroftheInnovation,Research
Associate Professor with the Faculty of Electri- andDevelopmentCenter(IRDC),FutureUniversity.Hisresearchinterests
cal Engineering, Universiti Teknologi Malaysia. includecellularcommunication,5G,intelligentreflectivesurfaces(IRSs),
Shehadpublished116articles,17copyrights,one beamforming,andinterferencemanagementinwirelessnetworks.
integratedcircuit,andonetrademark.Hercurrent
researchinterestsincludetheInternetofThings,ubiquitouscomputingand
| smart devices, wireless | sensor networks, | ipv6, handoff | management, | net- |     |     |     |     |     |
| ----------------------- | ---------------- | ------------- | ----------- | ---- | --- | --- | --- | --- | --- |
works,andmobilecomputingsystems. MUTAZ H. H. KHAIRI (SeniorMember,IEEE)
receivedtheB.S.degreeincomputerengineering
|     |     |     |     |     |     | from Future | University, | in 2002,    | and the M.S.   |
| --- | --- | --- | --- | --- | --- | ----------- | ----------- | ----------- | -------------- |
|     |     |     |     |     |     | degree in   | electrical  | engineering | from Linkoping |
University,in2007.Heiscurrentlypursuingthe
Ph.D.degreewithUniversitiTechnologiMalaysia
|     |     |     |     |     |     | (UTM). | From 2002 | to 2007, | he was a Lecturer |
| --- | --- | --- | --- | --- | --- | ------ | --------- | -------- | ----------------- |
withtheFacultyofEngineering,FutureUniversity,
|     |          |                    |     |          |     | and the | Director | of the Information | Technology |
| --- | -------- | ------------------ | --- | -------- | --- | ------- | -------- | ------------------ | ---------- |
|     | SHARIFAH | KAMILAH SYED-YUSOF |     | received |     |         |          |                    |            |
Department.HeisalsoaresearcherandanICT
B.Sc.degreeinelectricalengineeringfromGeorge specialistwith16yearsofwiderangeofresearchandICTexperience.His
Washington University, USA, in 1988, and the researchinterestsincludesoftwaredefinenetworks(SDNs),machinelearn-
M.E.E.andPh.D.degreesfromUTM,in1994and ing,telecommunicationnetworks,andantennadesignandimplementation.
|     | 2006, respectively. | She is currently | a   | Full Pro- |     |     |     |     |     |
| --- | ------------------- | ---------------- | --- | --------- | --- | --- | --- | --- | --- |
fessorwiththeFacultyofElectricalEngineering,
UTM.Herresearchinterestincludeswirelesscom-
munication.
|     |     |     |     |     |     | MOSAB    | HAMDAN          | (Senior | Member, IEEE)      |
| --- | --- | --- | --- | --- | --- | -------- | --------------- | ------- | ------------------ |
|     |     |     |     |     |     | received | the B.Sc.degree | in      | computer and elec- |
tronicsystemengineeringfromtheUniversityof
ScienceandTechnology(UST),Sudan,in2010,
theM.Sc.degreeincomputerarchitectureandnet-
workingfromtheUniversityofKhartoum(UofK),
Sudan,in2014,andthePh.D.degreeinelectri-
|     |     |     |     |     |     | cal engineering | (computer | networking) | from the |
| --- | --- | --- | --- | --- | --- | --------------- | --------- | ----------- | -------- |
FacultyofEngineering,SchoolofElectricalEngi-
NURZALEFFIYANABINTIGHAZALIreceived neering, Universiti Teknologi Malaysia (UTM),
theM.S.degreeinelectricalengineeringfromthe Malaysia,in2021.From2010to2015,hewasaTeachingAssistantanda
LecturerwiththeDepartmentofComputerandElectronicsSystemEngineer-
|     | Shibaura Institute | of Technology | and | the Ph.D. |     |     |     |     |     |
| --- | ------------------ | ------------- | --- | --------- | --- | --- | --- | --- | --- |
ing,FacultyofEngineering,UniversityofScienceandTechnology(UST).
degreefromUTM,in2016.Sheiscurrentlydoing
researchinmobilecomputing,mobilitymanage- HeiscurrentlyaResearcherwiththeInterdisciplinaryResearchCenterfor
ment,networkcommunicationprotocol,andsport IntelligentSecureSystems,KingFahdUniversityofPetroleumandMin-
monitoringsystems. erals,SaudiArabia.Hiscurrentresearchinterestsincludesoftware-defined
networking(SDN),loadbalancing,networktrafficclassification,theInternet
ofThings(IoT),cloudcomputing,networksecurity,andfuturenetworks.
| VOLUME11,2023 |     |     |     |     |     |     |     |     | 84167 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |