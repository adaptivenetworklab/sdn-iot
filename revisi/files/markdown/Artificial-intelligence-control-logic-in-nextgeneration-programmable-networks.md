# Artificial-intelligence-control-logic-in-nextgeneration-programmable-networks

> Source file: `Artificial-intelligence-control-logic-in-nextgeneration-programmable-networks.pdf`

---

applied
sciences
Article
Artificial Intelligence Control Logic in Next-Generation
Programmable Networks
MateuszZ˙otkiewicz1 ,WiktorSzałyga1,JaroslawDomaszewicz1 ,AndrzejBa˛k1 ,ZbigniewKopertowski2
andStanisławKozdrowski3,*
1 InstituteofTelecommunications,WarsawUniversityofTechnology,Nowowiejska15/19,
00-665Warsaw,Poland;mzotkiew@tele.pw.edu.pl(M.Z˙.);wiktor.szalyga.stud@pw.edu.pl(W.S.);
domaszew@tele.pw.edu.pl(J.D.);bak@tele.pw.edu.pl(A.B.)
2 OrangeLabsPolska,Obrzezna7,02-691Warszawa,Poland;Zbigniew.Kopertowski@orange.com
3 InstituteofComputerScience,WarsawUniversityofTechnology,Nowowiejska15/19,
00-665Warsaw,Poland
* Correspondence:s.kozdrowski@elka.pw.edu.pl
Abstract:Thenewgenerationofprogrammablenetworksallowmechanismstobedeployedforthe
efficientcontrolofdynamicbandwidthallocationandensureQualityofService(QoS)intermsofKey
PerformanceIndicators(KPIs)fordelayorlosssensitiveInternetofThings(IoT)services.Toachieve
flexible,dynamicandautomatednetworkresourcemanagementinSoftware-DefinedNetworking
(SDN),ArtificialIntelligence(AI)algorithmscanprovideaneffectivesolution. Inthepaper,we
proposethesolutionfornetworkresourcesallocation,wheretheAIalgorithmisresponsiblefor
controllingintent-basedroutinginSDN.Thepaperfocusesontheproblemofoptimalswitchingof
intentsbetweentwodesignatedpathsusingtheDeep-Q-Learningapproachbasedonanartificial
(cid:1)(cid:2)(cid:3)(cid:1)(cid:4)(cid:5)(cid:6)(cid:7)(cid:8)(cid:1)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:6)(cid:7) neuralnetwork.Theproposedalgorithmisthemainnoveltyofthispaper.TheDevelopedNetworked
ApplicationEmulationSystem(NAPES)allowstheAIsolutiontobetestedwithdifferentpatternsto
Citation: Z˙otkiewicz,M.;Szałyga,
evaluatetheperformanceoftheproposedsolution.TheAIalgorithmwastrainedtomaximizethe
W.;Domaszewicz,J.;Ba˛k,A.;
totalthroughputinthenetworkandeffectivenetworkutilization.Theresultspresentedconfirmthe
Kopertowski,Z.;Kozdrowski,S.
validityofappliedAIapproachtotheproblemofimprovingnetworkperformanceinnext-generation
ArtificialIntelligenceControlLogicin
NextGenerationProgrammable networksandtheusefulnessoftheNAPEStrafficgeneratorforefficienteconomicalandtechnical
Networks.Appl.Sci.2021,11,9163. deploymentinIoTnetworkingsystemsevaluation.
https://doi.org/10.3390/app11199163
Keywords:artificialintelligence;deep-Q-learning;internetofthings;softwaredefinednetworking;
AcademicEditor:Eui-NamHuh programmablenetworks;IoTtrafficgeneration
Received:9August2021
Accepted:23September2021
Published:2October2021 1. Introduction
ThispaperpresentsasolutiondevelopedintheFlexNet(www.celticnext.eu/project-
Publisher’sNote:MDPIstaysneutral
flexnet)projectrelatedtothemanagementofnetworkresourcesusingSoftware-Defined
withregardtojurisdictionalclaimsin
Networking (SND) technology. SDN is a new networking solution in which a central
publishedmapsandinstitutionalaffil-
server,calledacontroller,overseesallprocessesandcontrolsnetworkbehaviour,ensuring
iations.
thebestpossiblenetworkquality. Thisnewparadigmofnetworkdesign,asopposedto
thetraditionalmethod,hasbenefits. Itismucheasiertoadapttonewnetworkpolicies
usingsoftware,asitiseasiertoaddormodifycontroller-basednetwork-levelrulesusing
software,ratherthanmanuallyapplyingalimitedsetofcommandstothesedevices. The
Copyright: © 2021 by the authors.
SDNmodelallowscontrolfunctionsfoundinnetworkdevicestobetakenandmoved
Licensee MDPI, Basel, Switzerland.
centrallyattheSDNcontrollerlevel,allowingnetworkdevicestocommunicatewitheach
This article is an open access article
otherinanefficientmanner.
distributed under the terms and
PresentedapproachisinaccordancetoFlexNetprojectobjectiveofbuildingupanew
conditionsoftheCreativeCommons
paradigmofflexiblenetworkcommunicationstofosterIoTvaluecreation. TheFlexible
Attribution(CCBY)license(https://
IoTNetworkprovidestheIoTvaluecreatorswiththeavailabilitytoconsumenetwork
creativecommons.org/licenses/by/
communicationsondemand,inrealtime,andautomaticallytofulfiltheirspecificneeds.
4.0/).
Appl.Sci.2021,11,9163.https://doi.org/10.3390/app11199163 https://www.mdpi.com/journal/applsci

Appl.Sci.2021,11,9163 2of14
This new network paradigm is fully aligned with the efforts currently ongoing in the
implementation of 5G technology, providing high-quality and consistent connectivity
forpeopleandobjects, creatingtheperceptionofinfinitecapacity. TheFlexNetproject
proposesflexibleresourcemanagementusingSDNwiththesupportofanAIsolutionfor
differentIoTusecases.
Usually,thenetworkismanagedmanuallyusingcommands,scriptsorspecialtools,
withoutautomationfortheefficientallocationofnetworkresources. Forseveralyears,
newnetworksolutionswithimprovedmanagementsolutionscanbeseen,wherethemost
advancedoneistheSDNsolution[1–3].In[4],thebasicmechanismsandtechniquesofSDN
fordynamicandscalablenetworkcontrolenvisionedfor5Gtechnologyaredefined[5].One
ofthemainelementsistheSDNcontroller,whichallowsadaptivedynamicprovisioningof
resourcesbyapplyingmanagementrulestothetrafficflowinthenetwork[6]. Ontheother
hand,thetrafficgeneratedinthenetworkisalsobecomingmorecomplex,especiallyinIoT
applications[7–11]wherethemanagementoflargedatavolumesrequiresmoreflexibility
andscalability[12,13].
Thisflexibilityandefficiencyapproachisoftensupportedbyartificialintelligence(AI)
algorithms. Inourproposedapproach,theAIalgorithmsupportstheintentroutingcontrol
inSDNandisresponsiblefortheresourceallocationmechanismandnetworkparameters
suchasthroughputandnetworklosses. ThisapproachisalsousedinourongoingFlexNet
project[14–16]. TheFlexNetprojectcoversdifferentusecasesrelatedtoIoTtechnology,
wheredifferentQualityofService(QoS)requirementshavetobemet.
Inaddition,anIoTtrafficgeneratorcalledNetworkedApplicationEmulationSystem
(NAPES)was developedand usedfor solutionvalidation purposes. Newapplications
andend-userdevicesgeneratedifferentnetworktrafficpatterns;therefore,forvalidating
newnetworksolutionsincomplexapplicationscenarios,theaforementionedIoTtraffic
generatorisaveryuseful,cost-effectiveandfast-to-implementtool.
1.1. Motivation
Theevolutionofthenext-generationtelecommunicationnetworkinprogrammable
flexibleresourcescontrolsolutionsisdrivenbygrowingapplicationrequirementsinservice
qualityandnetworkingresources[17]. Especially, itisthechallengeintheIoTdomain
wheremultiplyverticalusecaseswithdifferenttypesofrequirementsareneededtobe
effectivelyimplement. IntheFlexNetproject, wefocusedondifferenttypesofIoTuse
caseslike:
• Emergencyandpublicsafetywithlowlatencyrequests;
• Videosurveillanceapplications,whereondemandhighbandwidthisrequired.
In these situations, SDN approach allows for flexible, on demand creation of new
servicesusingnetworkcontrollerhandlingvirtualizedresourceacrossthenetwork. Au-
tomatizedmanagementofthenetworkresourcesinrelation,fromonesidetoapplications
demandsandfromothersidetotheiroptimaleffectiveutilizationiscomplextask,where
AImechanismsarepromisingsolutions.
AIhasseenasurgeofinterestinthenetworkingcommunity[18].Recentcontributions
include data-driven flow control for wide-area networks, job scheduling, and network
congestion control [19]. A particularly promising domain is the network management.
ResearchershaveusedMachineLearning(ML)toautomatethemanagementofnetwork
resourcesinrelationtoroutingornetworktrafficoptimization[20–24]. InloTnetworks,
we expect network conditions to vary over time and space. Time varying conditions
maybelongterm(seasonal)orshortterm,resultinginasignificantimpactonnetwork
performance[25]. MLtechniqueswillbedevelopedinordertodetectsuchchangesand
signalthemtotheSDNlayerfortimelyactiontobetakentoimprovetheoverallnetwork
performance. AnothersolutionisaKnowledge-DefinedNetwork(KDN)whichalsoisa
nextsteponthepathtowardsanimplementationofaself-drivingnetwork[26]. KDNisa
complementarysolutionforSDNthatbringsreasoningprocessesandMLtechniquesinto

Appl.Sci.2021,11,9163 3of14
thenetworkcontrolplanetoenableautonomousandfastoperationandminimizationof
operationalcosts.
1.2. ArticleOrganisation
Thearticleisorganizedasfollows: inSection2,webrieflydescribetheproblemand
applicationofAIinthecontribution. Section3presentsdescriptionofIoTtrafficgenerator
called NAPES we developed and use in the contribution. In Section 4, the results are
presented. Contributions of this work are summarized and future work directions are
discussedinSection5.
2. ProblemDescription
TheworkhasbeendoneinthescopeofFlexNetproject,whereOpenNetworkOper-
atingSystem(ONOS)controllerhasbeenusedtocontrolSDN.InONOS,theconceptof
intentsisused. Anintentexpressawillingnesstosendaspecificamountofdatathrougha
network[27].
Intheconsideredarchitecture,foreachregisteredintent,apairofpathsiscomputed.
Thepathsarecomputedimmediatelyafteranintentisregistered,andtheprocesscantake
uptoacoupleofseconds. Then,whenanetworkisinoperationalstate,theAImodule
describedinthispaperselectsonepathfromtheseprecomputedpathsforeachintent. The
selectionitselfhastobefastandpronetotheunexpectedbehaviourofnetworklinksand
intents. Inotherwords,wefacetheproblemofoptimalswitchingofintentsbetweentwo
previouslycomputedpaths. Theswitchingisperformedbasedonanoutputofanartificial
neural network that has been trained to recognize situations and states of the network
requiringswitchingfromonepathtoanother.
Considerthefollowingsets:
E edges
I intents
P pathsforintenti ∈ I
i
E edgesusedonpath p ∈ P
p
Eachintenthasitsvolumedefinedforeachmomentintimeintheconsideredtime
horizon < 0;T >. However, the volume is not known in advance. Intents have to be
assigned to available paths in a way that minimizes the congestion resulting from the
limited capacity of the edges. The volume and the capacities are expressed using the
followingconstants:
v volumeofintenti ∈ I attimet ∈<0;T >
it
c capacityonedgee ∈ E
e
Theassignmentandthecongestionareexpressedusingthefollowingvariables:
x ∈ P equalsthepathintenti ∈ I usesattimet ∈<0;T >
it i
y volumeintenti ∈ I isactuallysendingattimet ∈<0;T >duetocongestion
it
We express congestion using the following function that depends on the network,
loads,andselectedroutes:
(cid:40)
y
it
= v it ∀e ∈ E xit ∑ i(cid:48):e∈E x i(cid:48)t v i(cid:48)t ≤ c e ∀i ∈ I, ∀t ∈<0;T >
C(x ,i) otherwise
t
whereC(x ,i)isanon-trivialfunctionthatdependsonthenetwork,itscurrentstate,andan
t
utilizedcongestionavoidancealgorithm. Theactualoptimizationproblemwearesolving
isasfollows:
(cid:90) T
∑
max y
it
0 i∈I

Appl.Sci.2021,11,9163 4of14
We notice that even a formally defined problem with unrealistically constant and
predictablebehaviourofintentsandstateoflinksisNP-hard,becausewecanreducethe
satisfiabilityproblem(SAT)[28]toit.Therefore,wedecidedfirsttodecomposetheproblem
to alleviate the computational complexity and second to use artificial neural networks
tocopewithunexpectedbehaviourofintentsandlinks. Thedecompositionconsistsof
consideringeachintentindependently. Theconsideredartificialneuralnetworkknows
neitheranexacttopologyofSDNnorvolumesandpathsofallintents. Instead,itisfed
withtheviewofSDNfromapointofviewofasingleintentthatconsistsofthedetailed
informationabouttheconsideredintentandtheaggregatedinformationaboutotherintents
inthevicinity.
WedevelopedasystemwhoseconceptualmodelispresentedinFigure1. First, it
collectsinformationaboutintentsregisteredinONOSusingIntentMonitorandReroute
(IMR) service and standard ONOS API. Then, it collects information about traffic in a
network using ifstat, which is an open-source, interface statistics collecting tool that is
availableinalmostallLinuxmachines.
FlexNet AI
Reroute
IMR
Collect
intents
ONOS
Collect Compute
traffic observations
ifstat
Network
Figure1.Conceptualmodelofthesystem.
Inthenextstep,itcombinesthisknowledgeandcreatesobservationsforarandomly
selectedgroupofregisteredintentindependently. Thecomputedobservationsforeach
selectedintentindependentlyenteraneuralnetworkthatreturnstwovaluesassociated
withexpectedvaluesofq-functionsfortwopossibleactions: doingnothingorswitchingto
anotherpath. Ifthelattervalueisgreaterthantheformervalue,theswitchingisperformed.
Inthisway,ineachstep,onlyapartofregisteredintentsisconsidered,andusuallyonlya
smallfractionofthispartofintentsisissuedwithacommandtochangeacurrentpath.
TheartificialneuralnetworkusedinthisresearchisaDeep-Q-Network(DQN)[29]
consistingoffourinputs(observations),twooutputs,andfourhiddenlayersoften,five,
five,andthreeneurons. WeusedDQNs,becauseitgavethebestresultsinourinternal
studies. ThelearningprocesswasimplementedusingRayframework[30]anditsgoalwas
tomaximizethetotalthroughputinthenetwork. Theneuralnetworktakesastateofa
networkfromaviewpointofasingleintentasaninputandasanoutputitproducesthe
expectedq-functionvaluefortwocases: (a)whennothinghappensand(b)whenthepath
isswitched.

Appl.Sci.2021,11,9163 5of14
Theobservationsprovidedtotheartificialneuralnetworkdependonaconsidered
intent and are computed using data collected from a network and from ONOS. The
observationsareasfollows:
• Ratioofefficiencyonactivepath;
• Ratioofpotentialefficiencyoninactivepath;
• Edgeoccupancypercentageonactivepath;
• Edgeoccupancypercentageoninactivepath.
Thefirstobservationisaratioofanobtainedmomentumthroughputfortheintentto
themaximumthroughputdeclaredforthisintent. Themaximumdeclaredthroughputis
providedbytheowneroftheintentwhencreatingtheintentusingtheONOSinterface.
Thesecondobservationisaratiooftheminimumavailablecapacityonalledgesofthe
inactivepathtothedeclaredintent’smaximumthroughput. Thethirdobservationisthe
minimumratioofanobtainedmomentumthroughputfortheintenttoatotaltrafficonan
edgeforalledgesoftheactivepath. Similarly,thefourthobservationistheminimumratio
oftheobtainedmomentumthroughputfortheintenttoatotalpotentialtraffic(current
trafficincreasesbythecurrentmomentumthroughputoftheintent)onanedgeforall
edgesoftheinactivepath. Alltheseobservationsarecomputedindependentlyforeach
intentusingdatacollectedfromONOSandifstat.
The artificial neural network that is fed with the above observations was trained
usingaheavilymodifiedIrokoframework[31]thatisbasedonOpenAIGym[32]and
wasoriginallyimplementedtooptimizetrafficindatacenters. Episodeswererunwith
themininetframeworkusingamodifiedversionofgoben[33]togeneratevarioustraffic
patterns. Theneuralnetworkwastrainedtomaximizethetotalthroughputinanetwork.
ThemodificationstoIrokoframeworkareasfollows:
• Procedurestocollecttrafficfromanetworkusingifstat;
• Procedurestocomputethepreviouslydescribedobservationsfromthetraffic;
• ObjectivefunctionfedtoRaythatnowexpressesthetotalthroughputinanetwork;
• Dynamically modified network topologies that can change during training
betweenepisodes;
• Dynamicallyselectedcurrentlyconsideredintentsthatalsochangebetweenepisodes;
• Supportfordynamictrafficthatcanvarybetweeniterations.
Thenetworkwastrainedinseriesofepisodes. EachepisodewasdefinedbyanSDN
networktopologyandasetofactivetrafficdemands. Eachdemandwasdescribedbyits
source, destination, andanactivetimeperiod. Notethattheproposedneuralnetwork
wastrainedusingvarioustopologiesandtrafficpatters;thus,itistopologyindependent.
Because of the limitations of mininet and utilized machines, the considered topologies
consistedoftenswitchesatmost.Inthetrainingprocess,weusedthreedifferenttopologies
with eight different traffic patterns for each topology. The episodes were repeated for
36times,totalling864episodesinthetrainingprocess. Eachepisodelastedfor100sin
realtime,resultingin100trainingsteps. Ineachstep,anactivedemandwasselectedat
randomandonlythisdemandwasconsideredinthisparticularstep. Theobservations
werecomputedfortheselecteddemand,anddependingontheoutputofacurrentneural
networktheactionwastaken.
WesetthelearningrateofRLLib’sAdamoptimizer[34]to5×10−4. Areplaybuffer
sizewassetto5000,whichisapproximatelytwiceasmuchasanumberofstepsinoneloop
overallutilizedtopologiesandtrafficpatterns. Theexploration(cid:101)decreasedlinearlyfrom
1.0to0.02inthefirst5000stepsandthenremainedconstant. Finally,thetargetnetwork
wasupdatedeach200steps,andthetrainingbatchsizewassetto8.
3. GeneratingNetworkTraffic
TotestourAIsolution,weuseNetworkedApplicationEmulationSystem(NAPES),
atrafficgeneratorwedevelopedwithintheFlexNetproject. Themotivationbehindthe
developmentofNAPESistoenablerapiddeploymentofsetupsthatexhibitcomplex,time

Appl.Sci.2021,11,9163 6of14
varyingtrafficpatterns,whichcloselyresemblesthoseofactualapplications. Themain
innovativeideabehindNAPESisthatitallowsdistributed,traffic-generating“applications”
tobedefinedwithelementsofapplicationlogic. Specifically,aNAPESapplicationconsists
ofcommunicatingapplicationcomponents,eachofwhichcanhaveseveralstatemachines
representingthecomponent’slogic. Statemachinesaremeanttoapproximatethelogicof
anactualapplication. Interactingstatemachinesofanapplication’scomponentsjointly
giverisetocomplextrafficpatterns. ANAPESdeveloperspecifiesthestatemachines(i.e.,
statesandstatetransitions)foreachofanapplication’scomponents.
Statetransitionsoccurinresponsetoevents,whichmayoriginatelocally(timerevents)
ormayarrivefromothercomponentsoftheapplication.Thus,theeventsservethepurpose
ofintra-andinter-componentcoordination.
Besideslightweightevent-basedcoordination,componentscommunicateviaflows,
whichformthetrafficstress-testingthenetworkunderinvestigation. Acomponentmay
generateaflowaddressedtoanothercomponent. Aflowisasequenceofpacketsdescribed
withsomeparameters,e.g.,onesthatdescribeadistributionofinter-packettimesanda
distributionofpacketsizes. Flowsaresentandreceivedbymeansofcomponents’ports. A
clientportgeneratesthepacketsofaflow,whileaserverportreceivesthepackets.
Thegenerationofflowsisgovernedbythestatesofthestatesmachinesinsidethe
componentscomprisingaNAPESapplication. Specifically,foreachclientport,aNAPES
userspecifiesaflowtobegeneratedineachstateofastatemachineassignedtocontrol
theclientport(insomestatestheremaybenoflowatall). Thus,whenanevent(alocal
oneorreceivedfromanothercomponent)causesastatetransition,flowsgeneratedbythe
component’sclientportscontrolledbythestatemachineinquestionmaychange. Asa
resultofstatechangesofcomponents’statemachines,aNAPESapplicationmaygenerate
trafficofdifferentpatterns. Overall,theabovemechanismsallowaNAPEStoapproximate
someactualIoTapplication,whosecomponentsarealsolikely“tobeindifferentstates”
reflectingthestateoftheenvironment.
In terms of implementation, a component is specified in a data structure to be in-
terpretedbytheso-calledNAPESRuntime. ANAPESRuntimeshouldbeinstalledona
computingdevicetomakeitaNAPESnode. WeintendtoimplementaNAPESRuntime
ondifferentplatforms,fromresource-constrainedIoTnodestocloudservers. Wecurrently
haveaLinuximplementation;runtimesforAndroidandArduinoarebeingdeveloped. As
theacceptedcomponentdatastructureisthesame,nomatterwhattheunderlyingplat-
form,NAPEScomponentsareportableandcanberunondifferentnodes. Inter-component
eventsareexchangedasshortMessageQueuingTelemetryTransport(MQTT)messages.
Ageneralapproachtostress-testanetworkwithNAPESisto(a)developamulti-
componentNAPESapplicationwithanapplicationlogicclosetothatofanactualapplica-
tion,(b)connecttothenetworkundertestanumberofNAPESnodes(computingdevices
withNAPESRuntimes), (c)distributethedatastructurerepresentationsoftheapplica-
tion’scomponentstotheNAPESnodes,(d)runtheapplicationandcollectlogs. Notably,
NAPESapplicationsareagnosticastoanunderlyingstress-testednetwork. Thereisno
application-to-networksignaling,whichcallsforsomenetworkintelligenceandadaptivity.
4. ExperimentsandResults
TheAIalgorithmsweretestedwiththenetworktopologyshowninFigure2. Thetest
networkconsistsofthirteenNAPEShostsonwhichasimpleclientserverapplicationis
deployed. Allnetwork’slinkshavethecapacityof50Mbpsandtheaccesslinks(between
hostsandnetworkswitches)havethecapacityof1Gbps. ThehostsatthetopofFigure2
representsensornodes(e.g.,equippedwithcameras)andthehostatthebottomrepresents
a cloud server. The network topology was setup in such a way that it becomes easily
congestedaroundthecloudservernode,whenshortestpathroutingisused,whilethe
networkhasstillenoughcapacitytohandlethetrafficgeneratedbytheactivesensors.

Appl.Sci.2021,11,9163 7of14
Host-01 Host-02 Host-03 Host-04 Host-05 Host-06 Host-07 Host-08 Host-09 Host-10 Host-11 Host-12
50 50 50 50 50
sw04 sw05 sw06 sw07 sw08 sw09
50 50 50 50 50 50
50 50
sw01 sw02 sw03
50 50 50
sw00
Host-00
Figure2.Analyzednetworktopology.
Theapplicationemulatesthecasewhenaspace(e.g.,thestreetsofasmartcity)is
instrumentedwithmultiplesensornodes. Asensornodemaybeinthestandbyoralert
mode. When in the standby mode, no traffic is generated; when in the alert mode, a
nodegeneratesasimpleUserDatagramProtocol(UDP)flowwiththespecificbitrateof
20Mbps.Notethatthebitrateshavebeenchosentoallowconvenientexperimentation
withtheAIalgorithm;theyneednotberealisticfromtheapplicationdomainpointofview.
Imaginethatsomestimulus(e.g.,noisefromastreetsweepervehicleatnighttime)triggers
achangefromtheusualstandbymodetothealertmode. Asthesweepermovesdownthe
streets,differentsensornodesareexposedtothenoiseandenterthealertmode(starting
generatingtraffic).
We assumed that two sensor nodes enter the alert mode at a time (imagine two
camerasdeployedateachintersection). Moreover,pairsofsensorsarealertedaccording
toaregularpattern. Specifically,NAPEScomponentsrunningonthenodesHost-01and
Host-02 start generating traffic at the time 0 s (one flow per node), components on the
nodesHost-03andHost-04startatthetime20s,componentsonthenodesHost-05and
Host-06startatthetime40s,etc. Eachcomponentremainsinthealertmodefor40sand,
afterwards,returnstothestandbymode(withnotrafficgenerated),whichlastsfor100s.
Afterthat,acomponententersthealertmodeagain.
ToconducttheexperimentswiththeAIalgorithm,weemulatedtheabovetestnetwork
usingtheMiniNettool[35]. ThenetworknodesrepresenttheOpenVirtualSwitch(OVS).
The test flows were generated using the NAPES traffic generator. In all cases the test
instanceswererunonthehardwareplatformwiththefollowingparameters:
• 16GBRAM
• 8VCPU
• 64GBofdiskspace
• Ubuntusystemversion20.04.
Inthefollowingexperiments,wecompared2networkparametersi.e.,totalthrough-
put obtained by the node representing cloud server and temporary network loss rate
(averagedoverallflows)toshowtheadvantageoftheproposedAIalgorithm.
Figure3showstotalthroughputwithoutAIandFigure4showstotalthroughputwith
theAIalgorithm. ItisnoticeablethattheAIalgorithmallowsforbetternetworkresource
utilization by rerouting traffic to alternative paths and as a result increases the overall
networkthroughput. ThehostsHost-01... Host-12arearrangedinpairsthatperiodically
switchbetweenactiveandinactivestates. Whenfourhostsbecomeactiveatthesamethe
networkbecomescongestedifallflowsareroutedoverthesamelink(thismayhappen
with shortest path routing). With the AI algorithm, the flows can be routed over link

Appl.Sci.2021,11,9163 8of14
disjointpaths,thus,networkcongestioncanbeavoided. Thiscanbeobserved,forexample,
inthetimeperiodbetween20and40s. WithoutAI,theserverthroughputisonly50Mbps,
as all active flows are routed over a single link with a capacity of 50 Mbps. When the
AIalgorithmisenabled,twoflowscanbereroutedtoalternativedisjointpathsandthe
throughputincreasesto80Mbps(whichisequaltotheofferedtraffic).
Figure3.TotalthroughputwithoutAI.
Figure4.TotalthroughputwithAI.

Appl.Sci.2021,11,9163 9of14
The advantage of using AI is even clearer for the loss rate parameter. With the
AI algorithm, network losses are significantly lower than without using AI (compare
Figures5and6). However, the traffic losses cannot be completely avoided as the AI
algorithmneedssometimeto“observe”thetrafficpriortothepathswitchoverdecision.
Figure5.LossratewithoutAI.
Figure6.LossratewithAI.
ItcanbeseeninFigure5thatthenetworksuffersfromsixcongestionperiodsdueto
thenaiveshortestpathrouting(thesamecanbeseenalsoininFigure3). Ithappenswhen
fourhostsnearesttothesameaggregationswitch(sw01,sw02,andsw03)arealloperating.
Thesituationhappenstwotimesforeachaggregationswitchduringthe280sexperiment.
Thefirstcongestionperiod(form20to40s)happenswhenhosts:Host-01,Host-02,Host-03,
andHost-04areoperatingandallthetrafficisroutedontheshortestpath. Insuchacase,
link sw00-sw01 becomes the bottleneck, because all the traffic is using it. However, in
the presented AI framework, each intent can chose between two paths that are as link
disjointedaspossible. ItisclearlyseeninFigure2that,foreachhost(Host01-Host-12)in

Appl.Sci.2021,11,9163 10of14
theconsiderednetwork,thereexistsapairofpathstotheserver(Host-00)thatsharesonly
twolinks. Theselinksaredirectlyconnectedeithertothehostortotheserver. Therefore,
thereisalwaysacombinationofpossiblepaths,whichcanbeassignedtointents,thatwill
preventfromthedescribedcongestionsituationsonthelinksconnectingtheserverwith
theaggregationswitches. AsdisplayedinFigure4,thepresentedAIframeworkusually
findsthisperfectassignmentandallowsforconsiderablelossreductions.
Theresultsoftheaboveexperimentsobtainedforfivedifferenttestcasesarepresented
inTables1and2. Table1showstheperflowaveragethroughputobtainedforexperiments
performedwithandwithouttheAIalgorithm. Table2showssimilarresultsfortheaverage
flowlossrateparameter. Wecanseethatthetrafficlosses(andtheresultingthroughput
reductions)arenotevenlydistributedbetweenflows. WithouttheAIalgorithm,theper
flowlossratecanbeashighas40%(meaningthesamelevelofthroughputdecrease). The
AIalgorithmreducestheaverageperflowlossrateover3times,toanaveragelevelof6%
(fromanaverageof18%forthecasewiththeshortestpathrouting).
Table1.Comparisonofflows’throughputfordifferenttestcase.
(a)ThroughputwithoutAI
| FlowNo. |           | TestCase  |      | Average |
| ------- | --------- | --------- | ---- | ------- |
|         | 1 2       | 3 4       | 5    |         |
| 1       | 3.58 5.75 | 3.68 4.83 | 5.23 | 4.61    |
| 2       | 5.75 4.97 | 5.52 4.50 | 3.72 | 4.89    |
| 3       | 5.21 3.61 | 4.11 4.60 | 3.98 | 4.30    |
| 4       | 4.01 4.34 | 5.30 4.71 | 5.64 | 4.80    |
| 5       | 4.26 4.24 | 5.52 5.62 | 3.74 | 4.68    |
| 6       | 4.31 5.69 | 4.25 4.50 | 5.42 | 4.83    |
| 7       | 5.59 4.95 | 4.61 4.79 | 5.39 | 5.07    |
| 8       | 4.52 3.83 | 4.33 3.78 | 4.16 | 4.12    |
| 9       | 5.24 5.50 | 5.55 5.42 | 4.17 | 5.18    |
| 10      | 3.81 4.76 | 4.16 3.79 | 4.46 | 4.20    |
| 11      | 5.69 4.76 | 5.00 4.64 | 4.46 | 4.91    |
| 12      | 3.98 3.68 | 3.99 4.85 | 5.62 | 4.42    |
(b)ThroughputwithAI
| FlowNo. |           | TestCase  |      | Average |
| ------- | --------- | --------- | ---- | ------- |
|         | 1 2       | 3 4       | 5    |         |
| 1       | 5.69 5.43 | 5.54 5.59 | 5.58 | 5.57    |
| 2       | 5.65 5.77 | 5.14 5.77 | 5.66 | 5.60    |
| 3       | 5.75 5.33 | 4.66 5.71 | 5.07 | 5.30    |
| 4       | 5.46 5.71 | 5.76 5.58 | 5.74 | 5.65    |
| 5       | 5.52 4.66 | 5.19 4.98 | 5.57 | 5.19    |
| 6       | 5.19 5.72 | 5.42 4.97 | 4.61 | 5.18    |
| 7       | 5.37 5.59 | 5.69 5.52 | 5.03 | 5.44    |
| 8       | 5.68 5.60 | 5.31 5.74 | 5.55 | 5.58    |
| 9       | 5.56 5.70 | 5.30 5.13 | 5.24 | 5.39    |
| 10      | 5.31 4.97 | 4.96 5.03 | 5.68 | 5.19    |
| 11      | 5.65 5.44 | 5.76 5.65 | 5.72 | 5.64    |
| 12      | 5.61 5.56 | 5.59 5.45 | 5.77 | 5.60    |

Appl.Sci.2021,11,9163 11of14
Table2.Comparisonofflows’losesfordifferenttestcase.
(a)LossratewithoutAI
| FlowNo. |       |       | TestCase |       |       | Average |
| ------- | ----- | ----- | -------- | ----- | ----- | ------- |
|         | 1     | 2     | 3        | 4     | 5     |         |
| 1       | 38.10 | 0.57  | 36.41    | 16.40 | 9.46  | 20.19   |
| 2       | 0.49  | 14.09 | 4.57     | 22.11 | 35.65 | 15.38   |
| 3       | 9.85  | 37.60 | 28.85    | 20.44 | 31.19 | 25.59   |
| 4       | 30.58 | 25.00 | 8.36     | 18.45 | 2.40  | 16.96   |
| 5       | 26.18 | 26.62 | 4.40     | 2.65  | 35.22 | 19.01   |
| 6       | 25.32 | 1.55  | 26.48    | 22.14 | 6.26  | 16.35   |
| 7       | 3.26  | 14.36 | 20.22    | 17.21 | 6.81  | 12.37   |
| 8       | 21.81 | 33.83 | 25.16    | 34.54 | 28.09 | 28.69   |
| 9       | 9.39  | 4.76  | 3.94     | 6.23  | 27.89 | 10.44   |
| 10      | 33.93 | 17.70 | 28.00    | 34.34 | 22.76 | 27.35   |
| 11      | 1.81  | 17.67 | 13.38    | 19.84 | 22.88 | 15.12   |
| 12      | 31.19 | 36.31 | 31.03    | 16.16 | 2.75  | 23.49   |
(b)LossratewithAI
| FlowNo. |       |       | TestCase |       |       | Average |
| ------- | ----- | ----- | -------- | ----- | ----- | ------- |
|         | 1     | 2     | 3        | 4     | 5     |         |
| 1       | 1.49  | 5.98  | 4.08     | 3.33  | 3.57  | 3.69    |
| 2       | 2.29  | 0.24  | 11.14    | 0.15  | 2.07  | 3.18    |
| 3       | 0.58  | 7.79  | 19.35    | 1.23  | 12.34 | 8.26    |
| 4       | 5.63  | 1.18  | 0.38     | 3.40  | 0.65  | 2.25    |
| 5       | 4.47  | 19.34 | 10.17    | 13.74 | 3.52  | 10.25   |
| 6       | 10.13 | 1.07  | 6.17     | 13.91 | 20.23 | 10.30   |
| 7       | 7.12  | 3.26  | 1.55     | 4.56  | 13.07 | 5.91    |
| 8       | 1.73  | 3.22  | 8.11     | 0.66  | 4.04  | 3.55    |
| 9       | 3.71  | 1.35  | 8.34     | 11.21 | 9.27  | 6.77    |
| 10      | 8.03  | 13.95 | 14.24    | 12.91 | 1.72  | 10.17   |
| 11      | 2.24  | 5.86  | 0.48     | 2.37  | 1.15  | 2.42    |
| 12      | 2.98  | 3.80  | 3.33     | 5.67  | 0.20  | 3.20    |
5. Conclusions
Inthispaper, themanagementofSDNnetworkresourceswithAIsupportforIoT
applications was presented. Particularly, the studied problem focuses on an optimal
switchingofintentsbetweentwoavailablepathsinanSDNnetworksusingAIalgorithm.
Inthedevelopedarchitecture,theswitchingisperformedbasedonDeep-Q-NetworkAI
mechanismwhereitsmainpurposeistomaximizethetotalthroughputintheSDNnetwork
with minimal average total data loss rate for served IoT applications. The presented
approachisanintelligentSDNmanagementsystemwithAIsupport,especiallyapplicable
inprogrammablenext-generationnetworks(5Gandbeyond).
Moreover,thenetworkresourceallocationincontextofQoSassuranceisagrowing
problem,especiallyforIoTservices. Thedesignedsolutionissuitableforfastandoptimal
resourceallocation,especiallyincasesofemergencyanddelay-sensitiveIoTservices. To
testtheproposedAIsolution,weusedanIoTtrafficgeneratorcalledNAPES,developed
withintheFlexNetproject.Wecomparedtheperformanceandqualityparameters,i.e.,total
throughputinthenetworkandaveragedatalossrate,toevaluatetheAIusefulnessinthe
designedsolution. ThepresentedresultsconfirmeffectivenessofproposedAIapproach,
whichsignificantlyimprovestheoverallQualityofServiceandnetworkperformance. In
particular,itmaximizesthetotalnetworkthroughputaswellassignificantlyreducesthe
averagetotaldatalossrate. TheobtainedresultsconfirmtherightnessofapplyingAIto
thepresentedproblem.

Appl.Sci.2021,11,9163 12of14
Furtherresearchwillbefocusedonmorecomprehensiveexperimentsthatincludereal
scenariosfromIoTusecaseswithmoreextensivenetworktopologies,withdifferentQoS
parameters(lossesandlatency)andwithrealtrafficscenariosfromIoTverticalservices,
lossanddelaysensitive.
AuthorContributions: Conceptualization,M.Z˙.andS.K.;methodology,M.Z˙.,S.K.,A.B.. J.D.and
Z.K;software,M.Z˙.,J.D.,A.B.andW.S.;validation,S.K.,Z.K.andA.B.;formalanalysis,M.Z˙.and
Z.K.;datacuration,A.B.,S.K.andZ.K.;writing—originaldraftpreparation,S.K.,M.Z˙.,J.D.,Z.K.
andA.B.;writing—reviewandediting,S.K.,M.Z˙.,J.D.andZ.K.;supervision,Z.K.andS.K.;project
administration,Z.K.andS.K.;fundingacquisition,Z.K.Allauthorshavereadandagreedtothe
publishedversionofthemanuscript.
Funding: ThispaperwasfundedbytheFlexNetprojectinEUREKACELTIC-NEXTClusterfor
next-generationcommunicationstogetherwithTheNationalCentreforResearchandDevelopment
inPoland.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
QoS QualityofService
KPI KeyPerformanceIndicator
IoT InternetofThings
SDN Software-DefinedNetworking
AI ArtificialIntelligence
NAPES NetworkedApplicationEmulationSystem
5G Networkof5thGeneration
FlexNet FlexibleNetwork
ML MachineLearning
KDN Knowledge-DefinedNetwork
ONOS OpenNetworkOperatingSystem
SAT SatisfiabilityProblem
IMR IntentMonitorandRerouteservice
MQTT MessageQueuingTelemetryTransport(standardmessagingprotocolforIoT)
Gbps Gigabitperseconds
UDP UserDatagramProtocol
OVS OpenVirtualSwitch
References
1. Liyanage,M.;Ylianttila,M.;Gurtov,A. SecuringtheControlChannelofSoftware-DefinedMobileNetworks. InProceedingsof
theIEEEInternationalSymposiumonaWorldofWireless,MobileandMultimediaNetworks2014,Sydney,NSW,Australia,19
June2014. [CrossRef]
2. Rothenberg,C.E.;Nascimento,M.R.;Salvador,M.R.;Corrêa,C.N.A.;CunhadeLucena,S.;Raszuk,R. RevisitingRoutingControl
PlatformswiththeEyesandMusclesofSoftware-DefinedNetworking. InProceedingsoftheFirstWorkshoponHotTopicsin
SoftwareDefinedNetworks,HotSDN’12,Helsinki,Finland,13August2012;AssociationforComputingMachinery:NewYork,
NY,USA,2012;pp.13–18. [CrossRef]
3. Kreutz, D.; Ramos, F.M.V.; Verissimo, P.E.; Rothenberg, C.E.; Azodolmolky, S.; Uhlig, S. Software-DefinedNetworking: A
ComprehensiveSurvey. Proc.IEEE2015,103,14–76. [CrossRef]
4. IETF. Software-DefinedNetworking:APerspectiveFromWithinaServiceProviderEnvironment;IETF:Fremont,CA,USA,2017.
5. delaOliva,A.;Li,X.;Costa-Perez,X.;Bernardos,C.;Bertin,P.;Iovanna,P.;Deiss,T.;Mangues-Bafalluy,J.;Mourad,A.;Casetti,
C.;etal. 5G-TRANSFORMER:Slicingandorchestratingtransportnetworksforindustryverticals. IEEECommun.Mag.2018,
56,78–84. [CrossRef]
6. Dinh,K.T.;Kuklin´ski,S.;Osin´ski,T.;Wytre˛bowicz,J. HeuristictrafficengineeringforSDN. J.Inf.Telecommun.2020,4,251–266.
[CrossRef]
7. Bera,S.;Misra,S.;Vasilakos,A.V. Software-DefinedNetworkingforInternetofThings:ASurvey. IEEEInternetThingsJ.2017,
4,1994–2008. [CrossRef]
8. Municio,E.;Marquez-Barja,J.;Latre,S.;Vissicchio,S. Whisper:ProgrammableandFlexibleControlonIndustrialIoTNetworks.
Sensors2018,18,4048.[CrossRef][PubMed]

Appl.Sci.2021,11,9163 13of14
9. Municio, E.; Latre, S.; Marquez-Barja, J.M. ExtendingNetworkProgrammabilitytotheThingsOverlayUsingDistributed
IndustrialIoTProtocols. IEEETrans.Ind.Inform.2021,17,251–259. [CrossRef]
10. Zemrane,H.;Baddi,Y.;Hasbi,A.SDN-BasedSolutionstoImproveIOT:Survey. InProceedingsofthe2018IEEE5thInternational
CongressonInformationScienceandTechnology(CiSt),Marrakech,Morocco,21–27October2018;pp.588–593. [CrossRef]
11. Rego,A.;Canovas,A.;Jiménez,J.M.;Lloret,J. AnIntelligentSystemforVideoSurveillanceinIoTEnvironments. IEEEAccess
2018,6,31580–31598. [CrossRef]
12. Omar,H. IntelligentTrafficInformationSystemBasedonIntegrationofInternetofThingsandAgentTechnology. Int.J.Adv.
Comput.Sci.Appl.2015,6,37–43.[CrossRef]
13. Jin,Y.;Gormus,S.;Kulkarni,P.;Sooriyabandara,M. ContentCentricRoutinginIoTNetworksandItsIntegrationinRPL. Comput.
Commun.2016,89,87–104. [CrossRef]
14. Flexnet. FlexibleIoTNetworksforValueCreators.2020.Availableonline:www.celticnext.eu/project-flexnet(accessedon22
September2021).
15. Choque,J.;Aguero,R.;Kopertowski,Z.;Nguyen,K.K.;Medela,A.;Municio,E.;Marquez-Barja,J.M.;Domaszewicz,J.;Bak,A.;
Lee,J.H.;etal. FLEXNET:FlexibleNetworksforIoTbasedservices. InProceedingsofthe202023rdInternationalSymposiumon
WirelessPersonalMultimediaCommunications(WPMC),Okayama,Japan,19–26October2020;pp.1–6. [CrossRef]
16. Kozdrowski,S.;Banaszek,M.;Jedrzejczak,B.;Z˙otkiewicz,M.;Kopertowski,Z. ApplicationoftheAntColonyAlgorithmfor
RoutinginNextGenerationProgrammableNetworks. InComputationalScience–ICCS2021;Paszynski,M.,Kranzlmüller,D.,
Krzhizhanovskaya,V.V.,Dongarra,J.J.,Sloot,P.M.,Eds.;SpringerInternationalPublishing:Cham,Switzerland,2021;pp.526–539.
17. OpenNetworkingFoundation. Software-DefinedNetworking:TheNewNormforNetworks. WhitePaper2012.
18. Zhao,Y.;Le,Y.;Zhang,X.;Geng,G.;Zhang,W.;Sun,Y. ASurveyofNetworkingApplicationsApplyingtheSoftwareDefined
NetworkingConceptBasedonMachineLearning. IEEEAccess2019,7,95397–95417.[CrossRef]
19. Mao,H.;Alizadeh,M.;Menache,I.;Kandula,S. ResourceManagementwithDeepReinforcementLearning. InProceedings
ofthe15thACMWorkshoponHotTopicsinNetworks,HotNets’16,Atlanta,GA,USA,9–10November2016;Associationfor
ComputingMachinery:NewYork,NY,USA,2016;pp.50–56. [CrossRef]
20. Kozdrowski,S.;Cichosz,P.;Paziewski,P.;Sujecki,S. MachineLearningAlgorithmsforPredictionoftheQualityofTransmission
inOpticalNetworks. Entropy2021,23,7.[CrossRef][PubMed]
21. Chen,B.;Wan,J.;Lan,Y.;Imran,M.;Li,D.;Guizani,N. ImprovingCognitiveAbilityofEdgeIntelligentIIoTthroughMachine
Learning. IEEENetw.2019,33,61–67. [CrossRef]
22. Abar, T.; Letaifa, A.; El Asmi, S. Machine learning based QoE prediction in SDN networks. In Proceedings of the 2017
13thInternationalWirelessCommunicationsandMobileComputingConference(IWCMC),Valencia,Spain,26–30June 2017;
pp.1395–1400.[CrossRef]
23. Dobrijevic,O.;Santl,M.;Matijasevic,M. AntcolonyoptimizationforQoE-centricflowroutinginsoftware-definednetworks.
InProceedingsofthe201511thInternationalConferenceonNetworkandServiceManagement(CNSM),Barcelona,Spain,
9–13November2015;pp.274–278. [CrossRef]
24. Ali,J.;Roh,B.H.ManagementofSoftware-DefinedNetworkingPoweredbyArtificialIntelligence.2021. [CrossRef]
25. Mishra,P.;Puthal,D.;Tiwary,M.;Mohanty,S.P. SoftwareDefinedIoTSystems:Properties,StateoftheArt,andFutureResearch.
IEEEWirel.Commun.2019,26,64–71. [CrossRef]
26. Mestres,A.;Rodriguez-Natal,A.;Carner,J.;Barlet-Ros,P.;Alarcón,E.;Solé,M.;Muntés-Mulero,V.;Meyer,D.;Barkai,S.;Hibbett,
M.J.;etal. Knowledge-DefinedNetworking. SIGCOMMComput.Commun.Rev.2017,47,2–10. [CrossRef]
27. Sanvito,D.;Moro,D.;Gullì,M.;Filippini,I.;Capone,A.;Campanella,A. ONOSIntentMonitorandRerouteservice:Enabling
plugamp;playroutinglogic. InProceedingsofthe20184thIEEEConferenceonNetworkSoftwarizationandWorkshops
(NetSoft),Montreal,QC,Canada,25–29June2018;pp.272–276. [CrossRef]
28. Karp,R. Reducibilityamongcombinatorialproblems. InComplexityofComputerComputations; Miller,R.,Thatcher,J.,Eds.;
PlenumPress:NewYork,NY,USA,1972;pp.85–103.
29. Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu, A.A.; Veness, J.; Bellemare, M.G.; Graves, A.; Riedmiller, M.; Fidjeland, A.K.;
Ostrovski,G.;etal. Human-levelcontrolthroughdeepreinforcementlearning. Nature2015,518,529–533.[CrossRef]
30. Liang,E.;Liaw,R.;Nishihara,R.;Moritz,P.;Fox,R.;Goldberg,K.;Gonzalez,J.;Jordan,M.;Stoica,I. RLlib: Abstractionsfor
DistributedReinforcementLearning. InProceedingsofthe35thInternationalConferenceonMachineLearning,Stockholm,
Sweden,10–15July2018;Dy,J.,Krause,A.,Eds.;PMLR,ProceedingsofMachineLearningResearch:Stockholm,Sweden,2018,
Volume80,pp.3053–3062.
31. Ruffy,F.;Przystupa,M.;Beschastnikh,I. Iroko: AFrameworktoPrototypeReinforcementLearningforDataCenterTraffic
Control.arXiv2018,arXiv:1812.09975.
32. Brockman, G.; Cheung, V.; Pettersson, L.; Schneider, J.; Schulman, J.; Tang, J.; Zaremba, W. OpenAI Gym. arXiv 2016,
arXiv:cs.LG/1606.01540.
33. Marques,E. Goben.2018.Availableonline:https://github.com/udhos/goben(accessedon22September2021).

Appl.Sci.2021,11,9163 14of14
34. Kingma,D.;Ba,J. Adam:AMethodforStochasticOptimization. InProceedingsoftheInternationalConferenceonLearning
Representations,Banff,AB,Canada,14–16April2014.
35. Xiang,Z.;Seeling,P. Chapter11-Mininet:Aninstantvirtualnetworkonyourcomputer.InComputinginCommunicationNetworks;
Fitzek,F.H.,Granelli,F.,Seeling,P.,Eds.;AcademicPress:Cambridge,MA,USA,2020;pp.219–230. [CrossRef]