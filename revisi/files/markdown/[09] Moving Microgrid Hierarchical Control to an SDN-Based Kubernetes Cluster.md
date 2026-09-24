# [09] Moving Microgrid Hierarchical Control to an SDN-Based Kubernetes Cluster

> Source file: `[09] Moving Microgrid Hierarchical Control to an SDN-Based Kubernetes Cluster.pdf`

---

sensors
Article
Moving Microgrid Hierarchical Control to an SDN-Based
Kubernetes Cluster: A Framework for Reliable and Flexible
Energy Distribution
RicardoPérez1 ,MarcoRivera2,3,* ,YamisleydiSalgueiro4 ,CarlosR.Baier2 andPatrickWheeler3
1 DepartmentofComputerScience,FacultyofEngineering,UniversidaddeTalca,Curicó3341717,Chile;
riperez@utalca.cl
2 DepartmentofElectricalEngineering,FacultyofEngineering,UniversidaddeTalca,Curicó3341717,Chile
3 DepartmentofElectricalandElectronicEngineering,FacultyofEngineering,UniversityofNottingham,
Nottingham,NG72GT,UK
4 DepartmentofIndustrialEngineering,FacultyofEngineering,UniversidaddeTalca,Curicó3341717,Chile
* Correspondence:marcoriv@utalca.clormarco.rivera@nottingham.ac.uk
Abstract:SoftwareDefinedNetworking(SDN)isacommunicationalternativetoincreasethescala-
bilityandresilienceofmicrogridhierarchicalcontrol.Thecommonarchitecturehasacentralizedand
monolithictopology,wherethecontrollerishighlysusceptibletolatencyproblems,resiliency,and
scalabilityissues.Thispaperproposesanovelandintelligentcontrolnetworktoimprovetheperfor-
manceofmicrogridcommunications,solvingthetypicaldrawbackofmonolithicSDNcontrollers.
TheSDNcontroller’sfunctionalitiesaresegregatedintomicroservicesgroupsanddistributedthrough
abare-metalKubernetescluster.ResultsarepresentedfromPLECShardwareintheloopsimulation
tovalidatetheseamlesstransitionbetweenstandardhierarchicalcontroltotheSDNnetworked
microgrid.ThemicroservicessignificantlyimpacttheperformanceoftheSDNcontroller,decreasing
thelatencyby10.76%comparedwithamonolithicarchitecture.Furthermore,theproposedapproach
demonstratesa42.23%decreaseinpacketlossversusmonolithictopologiesanda53.41%reduction
inrecoverytimeduringfailures. CombiningKuberneteswithSDNmicroservicescaneliminate
thesinglepointoffailureinhierarchicalcontrol,improveapplicationrecoverytime,andenhance
Citation:Pérez,R.;Rivera,M.; containerizationbenefits,includingsecurityandportability. Thisproposalrepresentsareference
Salgueiro,Y.;Baier,C.R.;Wheeler,P. frameworkforfutureedgecomputingandintelligentcontrolapproachesinnetworkedmicrogrids.
MovingMicrogridHierarchical
ControltoanSDN-BasedKubernetes Keywords:kubernetes;hierarchicalcontrol;microgrids;microservices;softwaredefinednetworking
Cluster:AFrameworkforReliable
andFlexibleEnergyDistribution.
Sensors2023,23,3395. https://
doi.org/10.3390/s23073395 1. Introduction
AcademicEditor:ChunSingLai Microgridhierarchicalcontrolaimstoregulatethenetworkfrequencyandvoltage
throughcollaborativeworkbetweendistributedenergysources. Thisstrategyhaschanged
Received:13February2023
theimpactofdistributedgeneration. However,ithasimposedseveralchallengesinpower
Revised:13March2023
control systems, especially those related to integrating power electronics, telecommu-
Accepted:18March2023
nications, fault monitoring, and security issues [1]. The trend of this strategy is to use
Published:23March2023
threelevelsofhierarchicalcontroltostandardizethemicrogrid’soperationandincrease
itsresilience.
Theprimarylevelregulatesthenetwork’sfrequencyandvoltage,ensuringpower-
Copyright: © 2023 by the authors. sharingbetweenthedistributedgenerators(DGs)[2]. Themostimportantapproachisthe
Licensee MDPI, Basel, Switzerland. droopcontrol[3],whichisbasedonthedroopfeaturesofaconventionalgenerator. Droop
This article is an open access article controlensuresstabilitybetweenfrequencyoractivepower(f −P)andvoltageorreactive
distributed under the terms and power(V−Q). Thesecondarylevelstabilizesthevoltageandfrequencydeviationsdueto
conditionsoftheCreativeCommons
theoutputimpedancedecoupling,failuresinpower-sharingorthepresenceofcirculating
Attribution(CCBY)license(https://
currents[4]. Atthislevel,sharinginformationinrealtimebetweentheDGsandsupporting
creativecommons.org/licenses/by/
thestabilityofthemostcriticalcontrolvariableswithintheirnominalvaluesisessential.
4.0/).
Sensors2023,23,3395.https://doi.org/10.3390/s23073395 https://www.mdpi.com/journal/sensors

Sensors2023,23,3395 2of26
Theliteratureprovidesevidencethatintegratesthepowersystemwithcommunica-
tionsarchitecturesinnetworkedmicrogrids(NMG).Forexample,refs. [5–8]proposesa
two-levelhierarchicalcontrolcapableofregulatingtheactiveandreactivepowersharing.
However,despiteusingalow-bandwidthcommunicationsystem,thetopologyneeded
tobemorescalableduetotherecentdevelopmentofcomplexcontrolalgorithms. Previ-
ouslyreportedresearchmodifiedthecommunicationsarchitectureandcontrolapproachto
addnewfacilityunitsandcontrolalgorithms[9]. Furthermore,conventionalcommuni-
cationsandroutingprotocolscannothandlemultipletopologyeventsandlacksufficient
intelligencetomakeappropriatecontroldecisions[10].
SoftwareDefinedNetworking(SDN)isamodernapproachtonetworkingthatallows
forcontrollingandmanagingnetworkresourcesandtrafficflowthroughsoftwareabstrac-
tions[11]. SDNprovidesgreaterflexibilityandscalabilitybydecouplingthecontroland
dataplanesandenablingnetworkadministratorstoconfigureandmanagethetopology
behavior. Thisleadstofasterdeploymenttimes,improvednetworkvisibility,andeasier
troubleshooting[12]. Additionally,itprovidesnewopportunitiesfornetworkautomation,
real-time analytics, and increased security through granular policy enforcement. SDN
alsopromotesanopenandinteroperablenetworkenvironment,enablingorganizationsto
utilizevariousvendorofferingsandtechnologyadvancements.
ThemainlimitationofSDNtechnologyistheuseofacentralizedcontrolplaneandthe
inconveniencesassociatedwithasinglepointoffailureofthiscriticalnode. Thecentralized
controlplanecanpotentiallyleadtonetworkdowntimeifnotproperlymanaged.In[13–15],
theauthorsproposeasetofsystemsthataimtosolvethedrawbacksofconventionalSDN
technology.However,usingareliablecommunicationsstrategyisstillnecessarytoimprove
the heterogeneous communication between different DGs according to the restrictions
defined by the architecture and control algorithms. On the other hand, the complexity
associatedwithmultipleprogrammingAPIswithinamonolithiccontrollerrequiresahigh
leveloftechnicalexpertiseandrepresentsasignificantchallengetonetworkoperations.
Despitetheselimitations,differentresearchersandorganizationsareallocatingresources
towardmodernizingtheirpowersystemsandcommunicationnetworks.
One promising approach is to distribute the functions of the SDN controller into
multiple microservices [16,17]. The goal is to implement these functions as distributed
unitswithareplicationfactorforredundancy. Bydoingso,theworkloadandresources
of the SDN controller are spread among different worker nodes. In the event of a fail-
ure, the data remains accessible through the microservice controller without requiring
manualintervention.
ThereisawidevarietyofSDNcontrollersdevelopedusingdifferentprogramming
languages[18,19],amongwhichRyu[20],Opendaylight[21],andONOS[22]beingthe
most significant due to their capabilities, ease of deployment, and reliability. A study
in[17]exploredthedevelopmentofamicroservices-basedsystemfortheRyucontroller
withintheOpenStackvirtualizednetworkinfrastructure[23]. However,despitedividing
themainfunctionalitiesoftheRyucontrollerintoDockercontainers,thesemicroservices
cannotautomaticallyscaleincaseoffailure. Inthecaseofaworkernodefailure, there
isnoautomaticmethodtorestorethefunctionsassignedtothatelement,impactingthe
communicationsystemandthemicrogrid’sperformance. Althoughthisapproachoffers
a fresh perspective on deploying SDN controllers, it must be noted that Ryu was not
originallydesignedtosupportmicroservices[24]. Thepreviousdrawbackrequirescareful
testingofthearchitecture,services,andcommunicationinterfacesbeforeimplementation
inreal-worldenvironments.
µONOSisanSDNcontrollerthatusesmicroservicesinlarge-scalecommunication
networks[25]. TheONOSProjectpresentsµONOSasasolutionfordisaggregatingthe
functionalitiesoftheSDNcontrollerintomicroservices. Thisprojectaimstoenhancethe
versatilityoftheSDNarchitecturebytargetingcloudcomputingplatforms,datacenters,
andbare-metaldeployments. Abare-metalclusterremovesthehypervisoroverheadand
putstheKubernetesinstallationdirectlyonthehostserver’soperatingsystem.

Sensors2023,23,3395 3of26
Anorchestratorthatautomatesnetworkmanagement,loadbalancing,andnewin-
stancesprovidesanintelligenttopologythatusesmicrogridresourcesefficiently. Com-
bining SDN with Kubernetes provides an intelligent system that analyzes traffic and
applicationrequirementsinreal-timetoadjustnetworkconfigurationandapplicationde-
ployment.Recentliterature[26,27]suggeststhatalthoughtherearedifferencesbetweenthis
proposalandartificialintelligence(AI),thecommunicationalternativecanalsobeclassified
asintelligentbecauseofSDN’sprogrammabilityandthesystem’scapacitytooptimize
networkperformance. Kubernetesmanagescontainerizedapplications’orchestrationand
deployment,whileSDNmanagesthenetworkinfrastructuresupportingthoseapplications.
Together,theycandynamicallyrespondtochangesintraffic,adjustnetworkpolicies,and
optimizenetworkperformance. Forinstance,whentrafficsurges,SDNcanautomatically
increase network resources by adding nodes or expanding bandwidth. Likewise, if an
applicationneedstobemigrated,SDNcanadaptthenetworkroutingtoreducerecovery
time. Comparedtotraditionalnetworking,whichcanbetime-consuminganderror-prone,
our proposal offers automated configuration and management that is not restricted to
specificconditions[28].
Accordingtoliterature[29,30],therestrictionsinthecommunicationssystemsimposed
by the penetration of more distributed generation sources force the use of distributed,
autonomousandefficientcommunicationsstrategiestocontrolthepowersystemefficiently.
Microgridsneedbare-metalKubernetestoensurehighreliability,lowlatency,andoptimal
resourceutilization[31],whicharecriticalrequirementsforamicrogrid’sefficientandsafe
operation.StandbyserversmayprovidelowreliabilityandperformancethanaKubernetes-
basedinfrastructure,especiallyindynamicandchangingloadconditions. Thereareseveral
reasonstoproposebare-metalKubernetesformicrogrids:
• Reliability[32]: Bare-metalKubernetesprovidesahighlyreliableinfrastructurefor
microgridsbydistributingtheworkloadsacrossmultiplenodesandensuringthehigh
availabilityofresources.
• Computational cost [33]: Low costs because virtualization software is no longer
necessary. Cluster automation and microservices deployment are straightforward
becausethereisnohypervisor.
• Low latency [34]: Microgrids require low latency and high-speed communication
betweenthedevicestoensuresafeandefficientoperations. Bare-metalKubernetes
provideslow-latencynetworkconnectivityandefficientdatacommunication.
• Optimalresourceutilization[33,35]: Microgridsrequireoptimalresourceutilization
to ensure energy efficiency and reduce operational costs. Bare-metal Kubernetes
providesefficientresourceallocationandutilization,whichcanhelpoptimizeenergy
consumptionandreducecosts.
• Scalability [36]: Network configuration is more straightforward on the bare-metal
clusterandtroubleshooting. Microgridsrequiretheabilitytoscaleupordownde-
pendingonthedemand. Bare-metalKubernetesprovidesautomaticscalingandload
balancing,whichcanhelpensureoptimalperformanceundervaryingloadconditions.
DespitethepreviouscommentsandthebenefitsofKubernetes,thereisnoevidenceof
SDNmicroservicesbeingusedtosolvethedisadvantagesofmicrogridhierarchicalcontrol.
Decouplingtheapplicationsfromthemonolithiccontrollerintoaseriesofsub-functions
enablesthedeploymentofahighlyflexibleSDNarchitecture. Themostcriticalimpactof
thisresearchistheabilitytocoordinatedifferentapplicationsasmicroservicesandprovide
theguidelinesforprogrammingAPIsinmicrogridhierarchicalcontrol.
Thispaperproposesanovelhierarchicalcontrolarchitecturebasedonmicroservices
toaddressthelimitationsofSDNcontrollersinnetworkedmicrogrids. Implementinga
setofcontrollersasadistributedsystemintheKubernetesbare-metalclusterincreasesthe
redundancyandresilienceofthecommunicationsystem. Theloadisdistributedamong
variousdevicesbasedoncommunicationandpowersystemrestrictions. Ratherthanusing
amonolithiccontroller,thecontrollerfunctionsaredividedintoagroupofmicroservices.
Thekeycontributionsofthisresearcharepresentedasfollows.

Sensors2023,23,3395 4of26
• Anewarchitecture,basedonmicroservices,asasolutiontothecentralizedSDNcon-
trollerproblemregardingloadbalancing,scalability,andlowlatency. Theproposed
methods improve the global resilience of the system and allow the integration of
SDNcontrollersaspodservicesindistributedKubernetesplatforms. Theproposed
approachallowsthedeploymentofbare-metalKubernetesclusterparametersandcan
beappliedtomultipleconfigurationsofAC/DCmicrogrids.
• A new SDN communication architecture has been developed for hardware-in-the-
loopplatformsconnectedtoRaspberrypi,servingasbothaKubernetesworkerand
an OpenFlow communication device. Furthermore, this paper analyzes the most
significantdrawbacksoftheSDNcontrolplaneinnetworkedmicrogrids.
• ProvidesaproofofconcepttoapplyµONOSforsegregatingandorchestratingservices
inbare-metalKubernetescluster. Theproposedmethoddecreasesthedataflowtraffic
throughtheSDNinfrastructure,settingthemostappropriateroutebetweentheDGs.
Thedistributedcommunicationsystemiscapableofmanagingreal-timeenergydata.
Thisimplementationcanbereplicatedandmodifiedthroughourproject’sGitHub
repository. Furthermore,itdesignsamonitoringtoolintegrationthatallowsvisualization
oflogsandmeasuresmetricstocarryoutacompleteanalysisofthenetworkedmicrogrid.
Therestofthispaperisorganizedasfollows. Section2reviewsthemainlimitations
ofSDNcontrollersaccordingtophysicalarchitecture,interfaces,reliability,andscalability.
Section3describesthedevelopmentofhierarchicalcontrolofmicrogridsandthecontrol
methodapplied. Section4providesthemicroservicesbenefitsofSDNcontrollerfunction-
alitiesdisaggregationandourmethodology. TheimplementationoftheSDNcontroller
asagroupofmicroservicesispresentedindetailinSection5. Theresultsanddiscussion
ofthesignificanceofourproposalaregiveninSection6,accordingtodifferentmetrics.
Ontheotherhand,Section7presentsdifferentcommunicationfailuresandcomparesthe
performanceofthecommunicationsystems. Section8concludestheworkandprovidesan
overviewoffutureresearchtopics.
2. MainDisadvantageofanSDNController
ThissectionincludesthefundamentaldisadvantagesofSDNcontrollers,comparing
monolithicand centralizedarchitecturesversus microservices-based architectures. The
contrastedelementsallowdeterminingthemostrelevantmetricsthatmarktheperformance
of the SDN protocol. The scalability of the communications system proposed by SDN
integratedwithKubernetesallowsthedeploymentofanintelligentDGarchitectureata
reducedcostandincreasestheoverallsecuritythroughSDNcontrollerfunctions.
AlthoughSoftwareDefinedNetworkinghasseveralbenefits,ithascertainlimitations
that must be considered. Additionally, the security elements of SDN solutions are still
a concern, as the centralized control plane can be a target for cyberattacks. The most
significantdrawbacksofSDNtechnologyaresummarizedbelow.
2.1. CentralizedController
The most widely used architecture for microgrid control uses a centralized SDN
controllerasanintelligentelementwithinthetopology. However,criticalaspectssuchas
latency,networkconvergence(lessthan100ms),reliability(closeto99%),andpacketlosses
mustbemanagedcarefully[37,38]. Achievingthesepropertiesisdifficultinacentralized
controlscheme,especiallyforalargetopology,duetocommunicationdevices’propagation
latency and processing time. In this way, centralized SDN controllers have significant
challenges, especially regarding scalability and reliability. Consequently, the controller
nodebecomesakeytargetforcyberattacks. Iftheinformationstoredinthecontrolleris
compromised,thereisnowaytorecoverit,resultinginanegativeimpactonthenetwork
andeconomiclosses. ApossiblealternativeistousedistributedSDNcontrollersasstated
in[39,40].

Sensors2023,23,3395 5of26
2.2. MonolithicController
MultipleSDNimplementationsadoptacentralizedcontrollerthatreliesonamono-
lithiccontrolplanearchitecture. Allthepossiblefunctionalitiesareincludedinanextensive
controlprogram,whichneedstobeflexibleforchangingtopologyconditions[17]. Con-
trollers often use a set of services from a pool, which can result in some services being
unusedorrestrictedbythecontroller.Thisfeatureforcesthereplicationoftheentirecontrol
implementationinthedistributedarchitecture,whichlimitscontrollerportability. Asa
result,developersmustcarefullypreparethefunctionalitiesandensureintegrationbetween
themodules. Thisbehaviorposesasignificantchallengeforuserswhoneedtoimplement
newservicesandrequirefastcontrollerdeployment.
MonolithicandmicroservicearchitecturesaretwoapproachestobuildingSoftware-
DefinedNetworking(SDN)solutions.Table1comparesmonolithiccentralizedSDNcon-
trollerwithmicroservicescontroller. AmonolithicSDNissimpletoimplementanddeploy
but has scalability, flexibility, and fault tolerance limitations. In contrast, microservice
SDNisdesignedtodecomposethecontrolplaneintosmaller,independentservicesthat
communicate with each other through APIs. Each service is responsible for a specific
controlfunctionandcanbedeveloped,deployed,andscaledindependently.
Table1.ComparisonofmonolithiccentralizedSDNcontrollervs.microservicescontroller.
Metric Monolithic Microservices
Thewholesystemcanbe
Otherservicesarenotaffected
affectedbyabug,
Resiliency byafailureinaparticular
communicationordevice
microservice.
failure,orsecurityissues.
Orchestratingthedeployment
Simpleandfastdeployment becomescomplexdueto
Deployment
architecture. communicationandhardware.
restrictions.
Redeployingtheentiresystem
Youcanscaleeachelement
tomanagenewchangesmake
Scalability independentlywithout
itdifficulttomanageand
experiencinganydowntime.
maintain.
Adoptingnewtechnology
languagesorframeworksis Multipleintegrationand
Compatibility
impossibleduetothelackof standardization.
flexibility.
TheuseofAPIsto
Communicationwithina
communicatedifferent
Security singleunitsecuredata
servicesproducessome
processing.
securitythreats.
Thehugeindivisibledatabase Eachcomponentcanbe
Development makesdistributingtheteam’s independentlyoperatedbya
effortsimpossible. teamofdevelopers.
2.3. VariabilityinProgrammingInterfaces
SomeofthemostpopularSDNcontrollers(suchasOpendayLight,Ryu,orONOS[18,41])
useRESTAPIinterfacesasacommunicationmechanism. TheRESTfulAPIisadevice
communicationinterfacetosecureinformationexchangeoverthehypertexttransferproto-
col. However,eachcontrollerexposesitsAPIsinadifferentway,forcinguserstomodify
therequestsyntaxortheprogramminglanguageaccordingtothespecificconditions[16].
Thislackofstandardizationturnstheapplicationsintosystemsthatdependonaparticular
SDNcontroller.

Sensors2023,23,3395 6of26
2.4. DependenciesbetweenApplicationsandControllers
Thecloserelationshipbetweencontrolapplicationsandthecontrollertypepresents
achallengethatrestrictstheabilitytoreuseapplicationsandmoduleconfigurations. In
severalsituations,modifyingtheprogramminglanguageandreadjustingcriticalplugins
becomesnecessaryduetotheinterdependencebetweenthemodulesandthecontroller’s
centralcomponent.
2.5. LackofReliabilityandScalabilityofSDNController
Theprincipalreasonforthelackofreliabilityandscalabilityisthehighdependency
betweentheSDNcontrollerandthecommunicationeventshandledbythecontrolplane.
Furthermore,amonolithicarchitectureiscomplextoscaleintoastandalonesystemdue
totherelationshipbetweentheapplicationoftheSDNcontrollerandthecommunication
device. Anyfailureinonecomponentwillresultinacascadefailureoftheentiresystem.
3. HierarchicalControlApproach
HierarchicalcontrolisapracticalapproachtomanagingpowersharinginaMicrogrid.
TheprimarycontrolleveldeterminestheamountofpowertobegeneratedbyeachDG
basedonfactorssuchaspowerdemand, availabilityofenergy, andsystemconstraints,
asFigure1shows. Thesecondarycontrollevelmanagesthepower-sharingbetweenthe
Microgrid and the utility grid, ensuring that the Microgrid operates within acceptable
limits. Systemoptimizationandlong-termplanningarecarriedoutatthetertiarycontrol
leveltoensureoptimalpowersharingamongtheenergysources,energystoragesystems,
andloads.
Bandwidth Latency
• Economicdispatch
Tertiarylevel • Energy/fault/congestionmanagement 20–300[s]
• Energyoptimizationandcontrolconsumption
Low
• Voltage/frequencyrestoration
Secondary
• Activeandreactivepowersharing
level 2–10[s]
Medium • Gridsynchronization
• Voltage/frequencystability
Primarylevel • Innercontrolloop
• Preliminarypower–sharing
High 0.2–1[s]
• Allowplugandplayfeatures
Figure1.Hierarchicalcontrollevelsandcommunicationrestrictionsfornetworkedmicrogrids.
PowersharingbetweenDGsisusuallycarriedoutbyparallelinvertersconnected
to a common AC bus with multiple loads [42]. The proposed controller in this paper
considersthemicrogridasthreeVoltageSourceInverters(VSI)feedinganRLloadatthe
pointofcommoncoupling. AnRLloadwaschosentostudythemicrogrid’sactiveand
reactivepowersharing.EachDGrepresentsapowersourceimplementedinTheSimulation
PlatformforPowerElectronicSystems(PLECS)[43,44].Droopcontrolinparallelinverters
isawidelyusedstrategytoregulateMGpowersharing.Themaingoalofprimarydroop
controlistosetaproportionalloadsharingamongDGs,basedonthewell-known(P-Q)
droopmethod[5].Eachinverterhasanexternaldroopcontrollooptoimproveperformance
andprovideadecentralizedcontrolmethod.Figure2showsthestrategyappliedtoregulate
frequency and voltage for one VSI. The details of hierarchical control can be found in
AppendixesAandB.

Sensors2023,23,3395 7of26
|     |     |     |     | L R |     | υ   |     | i   |     |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     | f f |     | abc |     | abc |     |      |
| υa  |     |     |     |     |     |     |     |     |     | Load |
+
− υb
υc
υ
| dc  |     |     |     | C   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | f   |     | V V | V   |     |     |     |
Power
|     |     | υd  |     | id  |     | id,iq | abc→dq |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- | --- |
SC
| PWM     |     |              |     |           |           | υd,υq |         | calculation |                 |               |
| ------- | --- | ------------ | --- | --------- | --------- | ----- | ------- | ----------- | --------------- | ------------- |
|         |     |              |     | +         |           |       | υdref   |             |                 |               |
|         |     | + kp+ki      | +   | idref +   | kp+ki     |       | +       |             |                 |               |
|         |     | +            |     |           |           | s     |         |             |                 |               |
|         | −   | s            | −   | i −       |           | −     | υ       |             |                 |               |
|         |     | ω L          |     | d ω       | C         |       | d       | u =         | u − n (Q        | − Q )         |
|         |     |              |     |           |           |       |         | dre f       | re f q          | r e f         |
| dq →abc |     |              |     | i q       |           |       | υ q     |             |                 |               |
|         |     | + ω L        |     | ω         | C         |       |         | ω =         | ωr ef − m p ( P | − P r e f )   |
|         |     | + kp+        | − + | + +       | kp+       | ki −  | +       |             |                 |               |
| θ       |     | ki           |     |           |           |       |         |             |                 |               |
|         |     | + s          |     | iq r ef + |           | s     | υ q ref | θ           | D r o o p       | c o n t r o l |
|         |     | υq Innerloop |     | iq        | Outerloop |       |         |             |                 |               |
Figure2.GeneralstructureandhierarchicalcontrolofoneVSI.TheacronymSCrepresentssecondary
control.
Thecontrolstrategyisevaluatedaccordingtodifferenteventswithinthemicrogrid.
The droop control is activated during the first second until it reaches the steady state
condition. AsshowninFigures3and4,thereisadeviationinvoltageandfrequencythat
needstobesolvedbythesecondarycontrol. Forthatreason,itisnecessarytoperform
secondarycontroltoreachthestabilityoftheMG.Thesecondarycontrolisactivatedafter
10secondsandremainsuntiltheendofthesimulation.
3400
3396
)zH( ycneuqerF
60
)up( egatloV 3380
|     | 3394 |     |     |     |     | 60  |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
59.98
| 3360 | 3392 |     |     | Inv1 |     |     |     |     |     | Inv1 |
| ---- | ---- | --- | --- | ---- | --- | --- | --- | --- | --- | ---- |
59.96
|      | 10  | 10.5 |     | Inv2 |       | 59.995 |     |     |     | Inv2 |
| ---- | --- | ---- | --- | ---- | ----- | ------ | --- | --- | --- | ---- |
| 3340 |     |      |     | Inv3 |       |        |     |     |     | Inv3 |
|      |     |      |     |      | 59.94 |        | 1 2 | 3   |     |      |
| 0 1  | 5   | 10   | 15  | 20   |       | 1      | 5   | 10  | 15  | 20   |
Figure3.VoltageendfrequencyregulationwithSDNmicroservicecontrollerofthisproposal.
Figure4.LinetotheneutralvoltageandphasecurrentforSDNmicroserviceproposal.
ResearchstudieshaveusedahierarchicalcontrolapproachwithanSDN-basedcom-
municationarchitecturetoenhanceoverallsystemintelligence[13,37,45]. However,while
this approach addresses some aspects of power sharing in networked microgrids, the
communicationsystemremainsacriticalfactorthatimpactsthepowersystemandhin-
dersoverallrecovery. ThemonolithicarchitectureoftheSDNcontroller,theintegration
of new control functionalities, and the excessive workload can be improved through a
microservices-basedarchitectureandautomaticorchestration.
4. DisaggregatingFunctionalitiesandMigratingSDNasMicroservices
SDNcontrollersimplementdifferentmodulestohandlethemostrelevantaspectof
thecommunicationdevices. Thesemodulesaffordkeyfunctionalities,suchasselecting
the best route for message forwarding, monitoring topology changes, and enhancing
security[46,47],asoutlinedinFigure5. Theprocessstartswithdiscoveringandmanaging
thenodes,findingtheactivecommunicationlinks,andupdatingfunctionsaccordingly.
Next,optimalpacketflowandroutingmanagementareestablishedbycreatingnewflows

Sensors2023,23,3395 8of26
andforwardingpackets. Thecontrollermustactivatethefunctionstomonitorthetraffic
andguaranteethequalityofservice(QoS)accordingtopredefinedmetrics. Finally,several
optionsareappliedtoensurenetworkmanagementandsecurity,avoidlatencyissues,and
improverestrictionsimposedbythepowersystem.
Routing
| Node Link |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- |
Applyre-
| identi- |     | manage- |     |     | QoS |
| ------- | --- | ------- | --- | --- | --- |
discovery strictions
| fication |     | ment |     |     |     |
| -------- | --- | ---- | --- | --- | --- |
Figure5.MainfunctionalitiesoftheSDNcontroller.
Previousfunctionalitiesarethecomponentsthatsupportsegmentationinmicroser-
vices.
ComponentsandInterfacesasMicroservices
Inthisproposal,theSDNcontrollerdeploysasetofmicroservicesinseveralDocker
containers,asshowninFigure6. TheupperlayercorrespondstotheSDNcontroller,the
middlelayerrepresentsthecommunicationtopology,andthebottomlayeristheelectrical
system. Thecontainer’sfunctionalityincludestrafficrouting,topologymanagement,and
eventhandling. Theabilitytosegregatethecontrollerfunctionsasmicroservicesallows
adistributedsystemtoscaleaccordingtotopologydemand. Ifthenumberofcontainers
increases,aplatformfororchestratingmultiplepodsisrequired.
SDN
µONOS Controller
Controlplanelayer
|     | MICROSERVICES     |     | MICROSERVICES       |     | MICROSERVICES  |
| --- | ----------------- | --- | ------------------- | --- | -------------- |
|     | onos-cli          |     | onos-config         |     | onos-consensus |
|     | onos-gui          |     | onos-operator       |     | onos topo      |
|     | atomix-controller |     | atomix-raft-storage |     |                |
Dataplanelayer
SPI
SECONDARY CONTROL
|     | PI PI | ∑   | N ωDGi | ∑ N  | υDGi |
| --- | ----- | --- | ------ | ---- | ---- |
|     |       |     | i =1   | i =1 |      |
|     |       |     | N      |      | N    |
LOW PASS
|     | Ecos(ωt) |     |     |     | FILTER |
| --- | -------- | --- | --- | --- | ------ |
|     |          | i   | i   |     |        |
DROOP
| Powersystemlayer |     |     |     | CONTROL |     |
| ---------------- | --- | --- | --- | ------- | --- |
POWER
INNER CONTROL
CALCULATION
|     | & MODULATION |     |     |     |      |
| --- | ------------ | --- | --- | --- | ---- |
|     |              |     | i   | υ   | i Z  |
|     |              |     | f   | c   | o Li |
υ dc
|     |     | L   | C   |     | L   |
| --- | --- | --- | --- | --- | --- |
|     |     |     | f   | f   | o   |
Figure6.Communicationframeworkformicroservicesimplementation.

Sensors2023,23,3395 9of26
Figure6presentstheproposedtopologyandconsiderstheaggregationofmicroser-
vices deployed in three Raspberry pi 4 (with ARM architecture). Given the increased
computationalcapacityofthelatestversionsofRaspberryanditslowercostcomparedto
othercomputingdevices,thisplatformisselectedtooperateasaworkerintheKubernetes
clusterandanOpenFlowcommunicationdevice. OpenFlowisacommunicationprotocol
SDN uses to standardize the interfaces between the control and data planes [48]. This
researchusesOpenFlowbecauseitisastandardsupportedbymultiplecommunication
devices, addinggreatflexibilityandprogrammabilitytothenetwork. Theflexibilityof
OpenFlow minimizes the effort and resources necessary to manage complex networks,
includingthoseinmicrogridhierarchicalcontrol.
TheKubernetesclusterisdeployedinK3s[49]toobtaintheSDNcontroller’sglobal
functionality. K3sisalightweightKubernetesdistributionbuiltforIoTandEdgecomput-
ing. ThethreeRaspberrysarephysicallyindependentandconfiguredasahigh-availability
clustertoimprovethecontrolleroperationandprovidegoodresiliencethroughmicroser-
vices. ThesynchronizationofeachcontainerandtheglobaladministrationoftheSDN
controllerisorchestratedbyRancher[50]. RancherisaKubernetes-basedorchestration
softwareintegratingcontainermonitoringandmanagementtoolsthroughasimplegraphi-
calinterface.
Thenorthboundinterface(NB)allowstheinteractionbetweentheSDNcontrollerand
externalapplications. Ontheotherhand,thesouthboundinterface(SB)standardizesthe
operationofthecommunicationprotocols,asinthecaseofOpenFlow[51]. RESTAPIsare
communicationchannelsthatusetheHTTPprotocoltocarryoutoperationssuchasGET,
POST,orDELETEondata. Ithashighscalability, goodperformance, andtheabilityto
decoupleitsfunctions,makingitanidealcandidatefordevelopingmicroservices.
5. ImplementationofµONOSSDNController
Microgridsarechangingintomorecomplexandextensivenetworksinwhichappli-
cations, service virtualization, and edge computing are highly related to control strate-
gies[29,52]. MicroONOS(µONOS)isanewversionoftheSDNcontroller,developedby
theOpenNetworkFoundation(ONF[53]),whichusesmicroservicestodeployascalable
infrastructurewithexcellentthroughputandlowlatency. ItisbasedonDockercontainers
deployedinacloud-basedinfrastructureorlocaldatacenters.Unlikemonolithiccontrollers
thatintegratemultipleAPIs,itcomprisesafewinterfacessuchasGoogleRemoteProcedure
Call(gRPC),gRPCNetworkManagementInterface(gNMI)andP4Runtime[25].
TheµONOSinfrastructure,networkfunctionsandmonitoringservicesonlysupport
KubernetesapplicationsthroughHelmchartsimplementation[54]. Toinstall,manageand
deletethedeviceconfigurationsandtheirperformance,µONOSconfiguresthegNMIasan
open-sourcedatamanagementprotocolfornetworkdevices. Thefunctionalitiesprovided
by gNMI can be modeled using YANG (Yet Another Next Generation data modeling
language)[25]. ThenetworkmanagerinteractswiththeSDNcontrollerthroughthegRPC
interface,accessingboththeonos-cliandonos-guiservicesfornetworkmanagement,
networkmodificationsandrevertingchanges. AccordingtoONF[53],theonos-config
serviceoffersagNMIendpointforvariousfunctions,includingreadingstates,configuring
settings,andsubscribingtospecificfeatures. Thisinterfacecanalsopreventinvalidvalues
andenabletheoperationalstate.
TheµONOSidentificationcomponentfacilitatesthecontroller’smanagementfrom
externalapplications, asdepictedinthetoplayerofFigure7. Aproposedmiddleware
enablesinformationexchangebetweenexternalapplications(power-sharinginformation
fromnetworkedMG)andtheSDNcontrolplane. AsshowninFigure7,thecoreofthe
SDN controller is separated from the event handler within the middleware, allowing
communication between the REST API and the controller microservices. This service,
namedonos-config,isresponsibleforlinkingthemodule’sfunctionalitytothespecific
microservicesthatareexecutedinadistributedmanner.

Sensors2023,23,3395 10of26
app
Admin gNMI
ad ad m m in in -c - m cm d d onos-config e
µONOS mananger or
onos (Client)
St k/v
gNMI client
gNMI
Openflow Switches
(Raspberry pi)
Figure7.High-leveldesignoftheproposedµONOScontroller(modifiedfrom[25]).
The essential microservice of Figure 7 is the block onos-config, as it manages the
configurationofdevicesthroughgNMIinterfacesandregistersalleventstosendthemto
theAtomixdriver. TheAtomixdriverimplementsanAPItoscaletheµONOSKubernetes
resources. Thispropertyofscalingresourcesaddsgreaterredundancytothecontroller. It
providesasystemwithdistributedadditionalresourcesandisresponsibleformaintaining
andmanagingtheONOSservice. AtomixcontrollerdetailscanbefoundintheGitHub
repooftheOpenNetworkingFoundation[55].
5.1. Functionalitiesofonos-configModule
Theonos-configmodulestrivestohandlenetworkanddevicealterationsbyinvoking
theNetworkChangeandDeviceChangeservices,respectively. Theseserviceskeeprecords
ofallchangelogsandpassthemtotheAtomixdriversviathegRPCinterface.
Forconnectingdevicesthroughthesouthboundinterface,onos-configonlysupports
itthroughgNMI.Furthermore,theYANGmodelssettheconfigurationandtopologyarchi-
tectureintoonos-configservice. ThedeploymentofthismodulerequiresaKubernetes
clustercapableofrunningHelmchartsasdetailedinitsdeploymentpage[56]. Theinter-
actionbetweenonos-configandonos-cliallowstheusertodefinerulesorroutepaths
throughthegNMIinterface. Toexecuteit,accesstheonos-clipodandruntheplugins
fromthere(youcanviewthelistofpluginsbyrunningonos-config get plugins).
Figure8showsthedeploymentofthepodsduringtheexecutionoftheµONOSin
thetopology. Fivepodsoftheonos-configservicearedeployed,andsixpodsofAtomix
increasetheavailabilityanddistributetheservicesacrossthenodes. Allstepstodeploy
thisproposalareavailableintheGitHubrepository[57].
5.2. NetworkInterfaceClusterImplementation
This paper implements two network interfaces for each Raspberry, as shown in
Figure9. The eth0 is the default ethernet interface of the Raspberry pi 4. It serves as
theLinuxbridgeandisusedforconfiguringKubernetesclusters,exchangingpodscontrol
information,accessingRancherandtheloadbalancer,andconnectingtotheInternetgate-
way. Itmeansthateth0actsasanoverlayinterfaceforexternalcommunications. Onthe
otherhand,eth1isusedbytheOpenFlowprotocoltocommunicatebetweenSDNservice
pods. Conversely,theeth1interface,connectedviaaUSBtoEthernetadapter,enablesthe
substitutionofthevethinterfacesofthepodswithkbr-int-ex. Eachpodinthecluster
willusethekbrinterfaceinsteadofitsvethtoavoidroutingandforwardingissues.

Sensors2023,23,3395 11of26
Figure8.NumberofpodsoftheSDNcontrollerdistributedintheworker’snodes.
|     |         | Calico        |     |     | K3S Master |      |
| --- | ------- | ------------- | --- | --- | ---------- | ---- |
|     | K3sNode | K3sNetworking |     | API | ETCD       |      |
|     |         |               |     | api |            | etcd |
NI NI
C
o- C
o-
ali c c
ali
| br0        | br0              | br0 C   | C   | br0              | br0   | br0        |
| ---------- | ---------------- | ------- | --- | ---------------- | ----- | ---------- |
| veth1      | veth2            | veth3   |     | veth1            | veth2 | veth3      |
|            |                  | kbr-int |     | kbr-int          |       |            |
| kbr-int-ex | VXLAN/GRE/GENEVE |         |     | VXLAN/GRE/GENEVE |       | kbr-int-ex |
OVSDB
REST API
gRPC
| phy-kbr-ex |     |     |     |     | phy-kbr-ex |        |
| ---------- | --- | --- | --- | --- | ---------- | ------ |
| kbr-ex     |     |     |     |     |            | kbr-ex |
eth0
|     | eth1 eth0 |     |     |     | eth1 |     |
| --- | --------- | --- | --- | --- | ---- | --- |
Figure9.KubernetesmanagementandoverlaytunnelingnetworkingwithCalico-CNI.
CalicoCNI(KubernetesContainerNetworkInterface(CNI))deploysaDaemonseton
eachnode,ensuringcommunicationbetweengRPCandtheµONOScontroller.
Inother
words,thispluginprovidesnetworkingforthecontainersandpodswithintheKubernetes
cluster. TheclusterformedbytheRaspberrynodescanoperateasconventionalEthernet
devices(viaTCPandUnixdomainsocket)orasanOpenFlowswitchtohandleSDNtraffic.
5.3. CreatetheKubernetesClusteronRaspberry
K3sdistribution[49]allowsdeployingofthebare-metalclusterandisanexcellent
choice for IoT devices, particularly Raspberry pi. From Rancher’s official documenta-
tion[58],ahigh-availabilityclusterwithanembeddeddatabaseisimplemented. However,
usingasingleloadbalancerasimplementedinthedefaultconfigurationbringsbackthe
drawbacks of the centralized system. Integrating the K3s cluster with Keepalived and
HAproxyasdescribedin[59],solvesthepreviousdisadvantagesinadistributedway. To
setupanHAKubernetesclusterusingKeepalivedandHAproxy,youneedtoinstalland

Sensors2023,23,3395 12of26
configure Keepalived and HAproxy on each node in the cluster. Keepalived is used to
managethevirtualIPaddressthatclientsusetoaccesstheKubernetesAPI.Incontrast,
HAproxyisusedtoloadbalanceincomingtrafficacrosstheKubernetesAPIservernodes.
Thisalternativeissuperiortotheexternaldatabaseimplementationbecausethestorage
is distributed in each etcd node’s services [58], increasing the system’s availability and
removingthesinglepointoffailurethroughdistributedstorage.
Ansibleautomatesnodecreation,storageconfiguration,networkinterfaces,services,
anddeploymentprocesses. Thistoolallows(inasimpleway)theclustertobedeployed
through the execution of a series of scripts developed in Ansible. All the manifest and
AnsibleinventoryfilesareinthesharedGitHubrepo.
5.4. ConnectiontoPLECSRTBox
PossiblecommunicationalternativesbetweenRaspberryandPLECSareSPI,I2C,and
CANprotocols. However,thePLECSRTBoxonlyhastwoSPIcommunicationmodules
(SPI1andSPI2),leavingoneofourworkernodesunconnected. In[60],theaveragedata
ratesofthethreetechnologiesarecompared. AccordingtothePLECSmanual,SPIhasthe
bestdatarate,followedbytheCANbusandI2C.Wedecidedtoconnectthethirdnode
oftheclustertothesameSPIportofnode2’sPLECSserverforthesereasons. Although
this is not the best communication alternative, as the frequency and voltage values on
eachRaspberryareaveraged,thiswillnotaffecttheoverallperformanceoftheMG.For
morecomplexmicrogridimplementations,itisrecommendedtousetheSFPtransceiver
modules,availablefromPLECS,toachievespeedsofupto10Gbps.
EachRaspberrywillserveasanOpenFlowcommunicationdevicethatensuresthe
exchange of secondary control information. Figure 10 shows the practical implementa-
tionofthisproposal. TherearethreeRaspberrysconnectedthroughEthernetandUSB.
The first connection allows external access, and the second provides SDN functionali-
ties. Additionally,thePLECSplatformiswiredtotheclusterthroughtheSPIbusofthe
LaunchpadF28069M.
b
i
c
a
d
g
e f
h
Figure10.ExperimentalsetupforKubernetesclusterwithRaspberrypi:(a)PLECSoutput,(b)ONOS
commandlineinterface,(c)SDNflowsduringcommunication,(d)RaspberrypiKubernetescluster,
(e)USBnetworkadapter,(f)overlayinterface,(g)Ciscorouterand52switch,(h)SPIconnection,
(i)MGoutputcurrent.
Accordingtothepriceofthisproposal,Table2showsthatitispossibletocreatea
bare-metal cluster with less than 1300 USD. The Cisco router can be replaced by other
cheaperalternatives,suchastheZodiacFX[61].

Sensors2023,23,3395 13of26
Table2.Totalcostofbare-metalcluster.
|                               | Item      |     | Quantity |     |     | UnitPriceinUSD |      |
| ----------------------------- | --------- | --- | -------- | --- | --- | -------------- | ---- |
| Raspberrypi4B8GB              |           |     |          | 3   |     |                | 170  |
| SanDiskMicroSDcard32GB        |           |     |          | 3   |     |                | 5    |
| AdapterUSBtoEthernet          |           |     |          | 4   |     |                | 10   |
| 0.5mCAT6Ethernetcables        |           |     |          | 4   |     |                | 4.5  |
| RouterCisco891F(notnecessary) |           |     |          | 1   |     |                | 670  |
|                               | Totalcost |     |          |     |     |                | 1248 |
5.5. MonitoringPlatform
Differentfactors,suchashardwareresources,load,orcommunicationarchitecture,
limitthenumberofpodsexecutedoneachdevice. However,withRancher,thesepodscan
bescaledautomaticallywithoutcompromisingthecluster’soverallstructure. Toconfigure
automaticscalinginRancherisnecessarytoselectthedeployment.Fromthere,the“Scaling”
tabspecifiestheminimum,maximum,anddesirednumberofreplicasforthedeployment
andalsosetsthescalingpolicybasedonCPUormemoryusage. Thisproposalshowsthe
numberofreplicasforeachserviceinFigure8,withtheboundaryforscalingnewpodsset
at80%ofCPUusage. It’simportanttonotethatautomaticscalingrequiresamonitoring
andmetricssystemtotrackyourdeployment’sresourceutilization. Rancherintegrates
withPrometheusandGrafanatotriggeralertsaccordingtothethresholdvaluesconfigured.
Finally,theGrafanagraphicaluserinterfaceallowsmonitoringthedeployment’sstatus
andthenumberofreplicasscaled.
Thesolutiontomonitoringthecommunicationdevices’statusandthetools’interac-
tionispresentedinFigure11. OurproposalusesaRancherHelmcharttodevelopaJava
application(PrometheusExporter)toobtaininformationaboutnetworkmetrics. Further-
more,itexportsthedatatoPrometheus,whichisresponsibleformonitoringeventsand
triggeringalertsaccordingtostandardconditions.
KUBERNETES
API
ELECTRICAL
STORAGE PVC
|     | SYSTEM  |     |     | Service Discovery |     |     |     |
| --- | ------- | --- | --- | ----------------- | --- | --- | --- |
PROMETHEUS

Hierarchical Control
Networked Microgrid
PROMETHEUS
|     | MICRO - ONOS  | RETRIEVAL |     | TSDB |     | CONFIG |     |
| --- | ------------- | --------- | --- | ---- | --- | ------ | --- |
HTTP SERVER
|                          |     |              |     |     | Monitoring |     | Push alerts |
| ------------------------ | --- | ------------ | --- | --- | ---------- | --- | ----------- |
| Multiple SDN Controllers |     | Pull metrics |     |     |            |     |             |
as Microservices
|     |     |     | PROMETHEUS  |     | GRAFANA  |     | ALERTMANAGER  |
| --- | --- | --- | ----------- | --- | -------- | --- | ------------- |
EXPORTER
|     | µONOS   µONOS LOGS |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- |
|     | API REST FILE      |     |     |     |     |     |     |
Logs and information
about Microservices
Figure11.Proposedarchitectureformonitoringandintegrationoftheelectricalsystem,SDNtopology,
andCloudComputingenvironment.
Prometheus sends the information to the local storage to collect operating system
metrics. WeusetheµONOSinterfacetoobtaininformationandnetworkmetrics. Different
notificationscanbetriggeredthroughthePrometheusconfigurationfiletoperformfast
reactionswithoutdowntime.

Sensors2023,23,3395 14of26
Finally,GrafanaallowsimportingaseriesofdashboardswithinformationontheDG
flows. This tool obtains the knowledge of the packet flows that pass through the USB
ethernetadaptertotheSDNcontroller. Figure12demonstratethecorrectintegrationof
PrometheusandGrafanawithintheKubernetescluster. UsingRancherinthisproposal
simplifiesthedeploymentandconfigurationoftheservices.
Figure12.TypesofeventsinGrafanatool.PacketsouttoPLECSwithdestinationmicroservicesin
K3Scluster.Grafanaregistersdata.
Anessentialelementtoconsiderwhenimplementingahigh-availabilityKubernetes
clusteronRaspberryistheperformanceofthecomputationalresources. Asthecluster
scales,thecomputationalresourcesbecomemorelimited. Increasingthenumberofpods
inKubernetescanbedonetominimizetheimpactonserviceperformanceasfollows.
• Ensurethatthenodesinyourclusterhaveenoughresources(CPU,memory,storage)
to support the increased number of pods. The notification system and the alerts
configuredinGrafanaallowthemonitoringofresourceusageandglobalcapacity.
• Usinghorizontalpodautoscaling(HPA)automaticallyadjuststhenumberofpods
basedonresourceusageanddemand. HPAcanbeconfiguredbasedonCPUusage,
memoryusage,orcustommetrics.
• Topreventresourcecontentionandperformanceissues,podanti-affinityrulesensure
thatpodsarenotplacedonthesamenode. Thismethodavoidstheschedulingof
podsonthesamenode.
• Optimizepodresourcerequestsandlimitstofunctioncorrectly.
• Use pod disruption budgets (PDB) to ensure that a minimum number of pods are
availableduringnodemaintenanceorfailures. BysettingaPDB,youcanguarantee
thattheserviceisunaffectedbyremovingpodsfromthecluster.
Monitoringtheservice’sperformancefollowingthepreviouspointsandadjustingthe
settingsasnecessarytooptimizeresourceutilizationandperformanceiscrucial.
6. ExperimentalScenariosandResults
Toanalyzetheresultsofthisproposal,aseriesofcriticalelementsweretested,which
imposedrestrictionsonthecommunicationsandpowersystems. Figure13presentthe
topologyusedtotestthemicroservice(leftside)andmonolithic/OSPF(totherightside).
OSPFandmonolithiconlydifferinthesetupofRaspberryconfiguration. EachRaspberry

Sensors2023,23,3395 15of26
wasconfiguredasarouterforOSPF,whilethemonolithicwasconfiguredasanOpenFlow
switch. Table3showsthemainparametersettingsoftheexperiments. Thefirstscenario
testedislatency,introducedbydecouplingthecontrollerfunctionalitiesintodistributed
microservices.
Microservices topology OSPF and Monolithic topology
|     | for testing |                   |     | for testing |                   |
| --- | ----------- | ----------------- | --- | ----------- | ----------------- |
|     | Management  | Secondary control |     |             | Secondary control |
Management
| and monitoring |     | communication |     |     | communication |
| -------------- | --- | ------------- | --- | --- | ------------- |
and monitoring
|     |     |     | Network service |     | Network service |
| --- | --- | --- | --------------- | --- | --------------- |
Load
balancer
Openflow
& OSPF
| Rasp. 2 |     |         | Rasp. 3 |          |          |
| ------- | --- | ------- | ------- | -------- | -------- |
|         |     |         |         | Openflow | Openflow |
| µonos   |     | Rasp. 1 | µonos   |          |          |
|         |     |         |         | & OSPF   | & OSPF   |
|         |     | µonos   |         |          | or OSPF  |
Figure13.Proposedarchitecturefortestingthemetricperformance.
Table3.ElectricalandcontrolparametersoftheMG.
|     |     | Item |     |     | Value |
| --- | --- | ---- | --- | --- | ----- |
Microgridparameter
|     | Ratedfrequency      |              |     |     | 60√[Hz]     |
| --- | ------------------- | ------------ | --- | --- | ----------- |
|     |                     | Ratedvoltage |     |     | 4160 2/3[V] |
|     | LoadpowerratingRES1 |              |     |     | 1[MVA]      |
|     | LoadpowerratingRES2 |              |     |     | 500[kVA]    |
|     | LoadpowerratingRES3 |              |     |     | 200[kVA]    |
|     |                     | H Line1      |     |     | 0.4[mH]     |
|     |                     | H            |     |     | 0.65[mH]    |
Line2
|     |     | H   |     |     | 0.9[mH] |
| --- | --- | --- | --- | --- | ------- |
Line3
|     |                | Filter(L,C) |     |                      | 1.8[mH],[25µF] |
| --- | -------------- | ----------- | --- | -------------------- | -------------- |
|     |                | Ro,Lo,Co    |     | 80[Ω],12.5[mH],5[mF] |                |
|     | Sampletime(Ts) |             |     |                      | 10[kHz]        |
Primarycontrolparameters
|     | P-ωDroopCoeff.(mp |     |     | )   | 1[ ra d ] |
| --- | ----------------- | --- | --- | --- | --------- |
W · s
|     | Q-VDroopCoeff.(nq |     |     | )   | V   |
| --- | ----------------- | --- | --- | --- | --- |
25[ V ar ]
|     | Frequencyproportionaltermkpf |     |     |     | 0.01 |
| --- | ---------------------------- | --- | --- | --- | ---- |
3s−1
|     | Frequencyintegraltermk |     |     | f   |     |
| --- | ---------------------- | --- | --- | --- | --- |
i
|     | Voltageproportionaltermkpυ |     |     |     | 0.01 |
| --- | -------------------------- | --- | --- | --- | ---- |
|     | Voltageintegraltermkυ      |     |     |     | 2s−1 |
i
Secondarycontrolparameters
|     | Frequencyproportionaltermkpf |     |     |     | 0.001 |
| --- | ---------------------------- | --- | --- | --- | ----- |
|     | Frequencyintegraltermk       |     |     | f   | 4s−1  |
i
|     | Voltageproportionaltermkpυ |     |     |     | 0.001 |
| --- | -------------------------- | --- | --- | --- | ----- |
6s−1
|     | Voltageintegraltermkυ |     |     | i   |     |
| --- | --------------------- | --- | --- | --- | --- |
6.1. Latency
The evaluation tests of this proposal consider the measurement of two types of la-
tency. ThefirstcolumninFigure14considerstheresponsetimewhensendingthefirst
messagefromtheMGarchitecture. Thislatencygivesusameasureoftheinitialcostofthe
distributedcontrollerasmicroservicesandthetimeittakestoobtainavalidroute. Once
theentryintheflowtableisupdated,therestofthepacketsdonotneedtogothroughthe

Sensors2023,23,3395 16of26
SDNcontroller,sotherestoftheflowsareexpectedtohavelowerlatency. Thecolumns
update1andupdate2inFigure14representthistypeoftest.
250 244.7
235
200 192.1 189
173.4
162.4
150 141.3
132.3
112.1
105.4
100 94.1 95.3
first1 update1 first2 update2
]sm[ycnetaL
OSPF Monolithic Microservices
Figure14.ComparisonoflatencybetweenOSPF,SDNwithamonolithiccontrollerandSDNwith
themicroservicecontroller.“First”columnsrepresentthelatencyforthefirstmessageand“update”
columnsrepresentthelatencywhentherouteisestablished.
Thesecondexperimentconsiderstheaveragelatencyfortherestofthepacketsusing
OSPFroutingandSDNtechnology. AsshowninFigure14,theperformanceoftheOSPF-
basedstrategyisslightlybetter. Thisisduetotheadditionalprocessingoverheadaddedby
thedistributionofmicroservicesinthreedifferentRaspberrynodestotheprocessingtime
oftheapplications. Thecomplexityofthenetworktopology,asdeterminedbythenumber
of OpenFlow switches, notably impacts the number of controller connections and the
processingcapacityofDockercontainers. TheconnectionsbetweentwoDGsaredenoted
byfirst1andupdate1,whiletheconnectionsbetweenDG1andtheSDNcontrollerare
representedbyfirst2andupdate2. InOSPF,theconnectionisestablishedbetweenthe
twonearestDGs. Ascanbeseen,thehighestlatencyisoriginatedwhenthefirstflowis
sentbetweentwonodes. Powerdata(frequencyandvoltage)sharedbyhierarchicalcontrol
inPLECSareshippedusingtheSPIandCANprotocol,andtheresultsaresummarizedas
averageroundtriptime.
However,eventhoughOSPFandSDNwithcentralizedcontrolhaveslightlyhigher
performance,theneedtousealoadbalancerisevident,especiallyinthetopologywitha
monolithicSDNcontrollerandmultipleDGs. Furthermore,whenthetrafficincreases,its
performancestartstodegrade.FortheOSPFroutingstrategy,itcanbeseenthatthesending
ofthefirstpacketofthetopologyisslightlyhigherthanitscompetitors. Thisismainly
duetotheneighbordiscoveryalgorithmandtheSPFalgorithmneedingtoknowtheentire
topologyforproperperformance. Toavoidasinglepointoffailure,theproposalofthis
paperincorporatesadistributedloadbalancer,followingtherecommendationin[59].
The researchers performed three communication tests to evaluate the response of
the proposed alternatives as a solution to the hierarchical control problem in electrical
microgrids.Figure15illustratesthepercentagesofpacketssuccessfullydeliveredonthe
firsttransmission,thoserequiringsingleretransmission,thoserequiringmultipleretrans-
missions,andthoseexperiencingpacketlossforeachscenario. Furthermore,Figure15
presentsatrade-offbetweenmonolithicandmicroservicesarchitecturesregardinglatency
andthroughput. Tensimulationswereconductedforeachofthethreetests,andtheresult-
ingaverageswereanalyzedtoinvestigatetheaforementionedrelationshipacrossdifferent
datarates. Specifically,lowdatarates(0< Throughput ≤299Mbps),mediumdatarates
(300 < Throughput ≤ 599 Mbps), and high data rates (Throughput ≤ 600 Mbps) were

Sensors2023,23,3395 17of26
coveredintheanalysis. ThemessagethroughputismodifiedfromthePlecssimulation,
increasingthesampleperiodofsecondarycontrol. Thisgraphshowstheaveragelossrate
for the centralized communication strategies is similar (with a difference of about 5%).
Incomparison, thedistributedsystemsimprovetheseresultsby25to60%forthetests
performed. Theaveragelatencywas287msfortheglobaltest. Thelatencyincreasesasthe
throughputincreaseduetotheclosenesstothespeedlimitsupportedbytheRaspberries.
]sm[tuphguorhTegarevA
100 700
80 600
60 450
40 300
20 150
0 0
µS Ml O µS Ml O µS Ml O
Low Medium Highdatarate
)%(snoissimsnartfonoitcarF
100
Latency
Throughput
80
60
40
20
0
µS Ml O µS Ml O µS Ml O
Noretransmits Singleretransmits Multipleretransmits Losses
Figure 15. The trade-off between latency and throughput varies across different test scenarios.
ColumnsµSreferstothisproposal,MlmeansMonilithicsarchitectureandOSPFisO.
The findings reveal that monolithic architectures can offer lower latency since all
the system components are closely integrated and communicate directly, reducing net-
workcommunicationoverhead. However,thisclosecouplingcanalsolimitthesystem’s
horizontalscalabilityandabilitytohandlehighthroughputrequirements. Ontheother
hand, microservices architectures can provide higher throughput as the system can be
scaledhorizontallybyaddingmoreinstancesofindividualservicesasneeded. However,
theaddednetworkcommunicationbetweenservicescanincreaselatencyandreducethe
system’s response time. Typically, the Raspberry Pi 4 (ARM64) can achieve consistent
transferratesof600–700Mbpswithappropriatenetworkconfigurationandoptimization.
Therefore,thechoicebetweenmonolithicandmicroservicesarchitecturesdependsonthe
system’srequirements. Amonolithicarchitecturemaybethebetterchoiceiflowlatencyis
criticalandhighthroughputrequirementsaremanageablewithatightly-coupledsystem.
Amicroservicesarchitecturemaybemoreappropriateifhighthroughputiscriticaland
latencycanbetoleratedwithloosely-coupledservices. Ourproposalhandlesthesurgein
demandbyincreasingthetransmittedpackets. Incontrast,themonolithicarchitectureand
OSPFdemonstratereducedresilience,scalability,andmultipleretransmissions.
Inthisway,itisevidentthatthethreestrategieshaveanacceptablebehavioraccording
toTable4. However,OSPFandSDNmicroservicesaretwodifferentapproachestonetwork
management,andtheyhavedistinctcharacteristicsandfeatures. TheresultsofTable4can
besummarizedasfollows.

Sensors2023,23,3395 18of26
Table4.Summaryofcommunicationresultsfortestscenarios.
PairedDifferences
| Microservicesvs.OSPF         |        |               |           | Improvements |
| ---------------------------- | ------ | ------------- | --------- | ------------ |
|                              | Mean   | Std.Deviation | Std.Error |              |
|                              | −17.41 |               |           | −29.74%      |
| Latencyoffirstpackage        |        | 13.12         | 2.39      |              |
| OverallLatency               | −20.66 | 32.41         | 6.01      | −4.75%       |
| Throughput                   | 14.28  | 5.24          | 0.95      | −4.15%       |
| Recoverytime                 | 214.82 | 39.95         | 7.29      | 53.41%       |
| Packetloss-linkfailure       | 19.75  | 2.06          | 0.37      | 55.98%       |
| Packetloss-devicefailure     | 11.83  | 2.30          | 0.42      | 38.66%       |
| Packetloss-controllerfailure | 86.00  | 1.38          | 0.25      | 100%         |
PairedDifferences
| Microservicesvs.Monolithic   |        |               |           | Improvements |
| ---------------------------- | ------ | ------------- | --------- | ------------ |
|                              | Mean   | Std.Deviation | Std.Error |              |
| Latencyoffirstpackage        | 8.46   | 14.02         | 2.56      | −5.09%       |
| OverallLatency               | 32.91  | 38.79         | 7.20      | 10.76%       |
| Throughput                   | −50.47 | 5.96          | 1.08      | 7.05%        |
| Recoverytime                 | 257.50 | 36.23         | 6.61      | 36.58%       |
| Packetloss-linkfailure       | 13.01  | 2.21          | 0.40      | 42.23%       |
| Packetloss-devicefailure     | −1.13  | 2.41          | 0.44      | −1.42%       |
| Packetloss-controllerfailure | 85.83  | 1.38          | 0.25      | 100%         |
• Latency: Regardinglatency,OSPFisadistributedprotocolthatreliesonexchanging
routinginformationbetweendevices. It’sdesignedtofindtheshortestpathbetween
twopoints,whichcanhelptominimizelatency. Ingeneral,monolithicarchitectures
canofferlowerlatencysinceallthesystemcomponentsarecloselyintegratedand
communicatedirectly,reducingnetworkcommunicationoverhead. However,this
closecouplingcanalsolimitthesystem’shorizontalscalabilityandabilitytohandle
high throughput requirements. On the other hand, SDN microservices rely on a
centralcontrollerthatmanagesthenetwork,andthelatencycanbeaffectedbythe
communicationbetweenthecontrollerandthedevices.
• Throughput: OSPF is a protocol that supports link-state routing and can quickly
adapttonetworktopologychanges. Asaresult,itcanprovidehighthroughputin
astablenetworkenvironment. Incontrast, SDNmicroservicescanprovidehigher
throughput as the system can be scaled horizontally by adding more instances of
individualservicesasneeded.
• Recoverytime: OSPFisdesignedtosupportfastconvergenceandcanquicklyrecover
fromalinkordevicefailure. However,theconvergencetimecandependonthesize
andcomplexityofthenetwork. SDNmicroservicescanalsoprovidefastrecovery
times,butitdependsonthespecificimplementationandconfiguration.
• Linkfailure: OSPFcandetectalinkfailureandreroutetrafficalonganalternatepath,
whichhelpstomaintainconnectivity. SDNmicroservicescanalsodetectlinkfailures
andpotentiallyprovidemoregranularcontroloverhowtrafficisrerouted.
• Devicefailure: InOSPF,ifadevicefails,theroutingtablesarerecalculated,andthe
network can continue to operate. In SDN microservices, the central controller can
detectadevicefailureandreconfigurethenetworkaccordingly.
• Controllerfailure: InSDNmicroservices,thecentralcontrollerisasinglepointoffail-
ure. Ifthecontrollerfails,thenetworkmaynotbeabletooperatecorrectly. However,
manySDNsolutionsprovideredundancyandfailovermechanismstominimizethe
impactofcontrollerfailure.
Overall,OSPFandSDNmicroserviceshavedifferentstrengthsandweaknesses,and
thechoiceofwhichonetousedependsonthespecificnetworkrequirementsandgoals.
All of these values are within the ranges defined by the IEEE 61850 standard [37] for
safe microgrid operation. Nevertheless, this microservice implementation has the best

Sensors2023,23,3395 19of26
portability(byusingaDockercontainer),resiliency(providedbyRancherorchestrator),
andscalabilityresults(demonstratedbytherecoverytimepresentedinTable5).
Table5.Recoverytimeofdifferentprotocolswhenafailureoccurs.
CommunicationProtocols RecoveryTime
OSPF 637.8ms
Monolithiccontroller 468.5ms
Microservicescontroller 297.1ms
6.2. Throughput
Throughput is generally used to determine how well SDN routers and controllers
canhandletrafficandhowefficienttheyareatthistask. Thistestmeasuresthenumber
ofpacketssentpersecondinthecaseofOSPF,whileSDNmeasuresthenumberofflows
installedonthedevices. Equation(1)presentsasimplewaytocalculatethethroughput.
Throughput = maximum_receiver_bandwidth/round−trip_time (1)
Theiperf3toolobtainsthemaximumreceiverbandwidth,whileasimplepingreturns
theround-triptime. Figure15showstheresultsofthistest. Asisevident,theresultsshow
abetterperformanceinthecaseofconventionalstrategies. However,thisadvantagemay
becompromisedinmoreextensivenetworkswheretheOSPFprotocolneedstodescribeall
routerneighbors.
7. CommunicationFailureandRecoveryTest
CombiningKuberneteswithasetofSDNmicroservicescanimproveapplicationre-
coverytimebyeliminatingthesinglepointoffailureinhierarchicalcontrol. Inatraditional
network architecture, the control plane and the data plane are tightly coupled, which
meansthatafailureinthecontrolplanecanleadtosignificantdisruptionsinthenetwork’s
operation. This hierarchical control model has a single point of failure, which can be a
bottleneckforrecoverytime.
However,withKubernetesandSDNmicroservices,thecontrolplaneisdecoupled
from the data plane, and the control functions are distributed across the network. If a
failure occurs in one part of the network, the rest can continue normally, and recovery
time can be significantly reduced. Moreover, the combination of Kubernetes and SDN
microservicesoffersasignificantlyautomatedandcustomizablenetworksettingthaten-
ablesquickandflexiblenetworktopologyadjustmentsinresponsetoanymodificationsin
theinfrastructureorapplication. Thisattributefurtherreducesthenetworkreconfigura-
tiontime,henceenhancingtherecoveryperiod,whichwouldotherwiserequiremanual
intervention. CombiningKuberneteswithSDNmicroservicescanimproveapplication
recoverytimebyeliminatingthehierarchicalcontrol’ssinglepointoffailureandproviding
ahighlyautomatedandprogrammablenetworkenvironment. Thiscanhelpensurethat
applications and services are always available and performing optimally, even during
networkfailures.
A communication system failure (closer to the distributed generation sources) is
simulatedinthisscenario. Theobjectiveistoverifywhichstrategyhasbetterperformance
fromthepointofviewofcommunicationswithoutdegradingthepower-sharingbetween
thelocalcontrollersoftheMG.
Thefailureisgenerated,forinstance,containingtheSDNmonolithic,andtheyare
comparedwiththelossesproducedinoneoftheinstancesthatincludethemicroservices.
Theorchestratorisexpectedtobeabletoinstantiateanewsubsysteminstancewithout
degradingtheperformanceoftheMG.Kuberneteshasbeenconfiguredtobescaledauto-
maticallyaccordingtotheresearchshownin[62]. Furthermore,inFigure16,thepacket
losspercentageshowsthatmicroservicesperformwellduetodistributedservicesabove
thenodes.

Sensors2023,23,3395 20of26
100100
100
80
]%[ssoltekcaP
60
4036.24
32.41
27.61
191.69.88
15.95
| 20  |     | 12.55 |     |     |     |
| --- | --- | ----- | --- | --- | --- |
0
| Link-failure | Device-failure | Controller-failure |     |     |     |
| ------------ | -------------- | ------------------ | --- | --- | --- |
| OSPF         | Monolithic     | Microservices      |     |     |     |
Figure16.Numberofpacketlossduringconvergencetime.
Figures17and18showtheresultsobtainedduringpower-sharingwithandwithout
hierarchicalcontrol,respectively. Atonesecond,thedroopcontrolisstartedtodistribute
theactiveandreactivepower-sharing.At10s,thehierarchicalcontrolisenabledtoregulate
voltageandfrequencydeviations.Sincethereisnomessagelossbetweencontrollers(minor
glitchesonlyintheaveragemessagedelay),itprovesthesystem’srobustness. However,
thesecondarycontrolwithamonolithiccontrollerishighlysusceptibletosmalllatencies,
CPUburden,andpropagationdelay. Inthisscenario,oneoftheOpenFlowswitcheswas
removedtodeterminetheeffectsofthemonolithiccontrolstrategy. Thisexperimentshould
be understood as a way to highlight the robustness achieved by the SDN system in its
deploymentbasedonmicroservices.
Figure17.ActiveandreactivepowersharingwithSDNdistributedcontrollerinthisproposal.
| 1 0.6 |     |     | -0.07 |     |     |
| ----- | --- | --- | ----- | --- | --- |
]up[ rewoP evitcaeR
| ]up[ rewoP evitcA |     | -0.05 |     |     |     |
| ----------------- | --- | ----- | --- | --- | --- |
0.8 0.5
-0.1
| 0.6 0.4 |       |            | -0.08 |       |      |
| ------- | ----- | ---------- | ----- | ----- | ---- |
| 10      | 10.05 | Inv1       | 10    | 10.05 | Inv1 |
|         |       | Inv2 -0.15 |       |       | Inv2 |
| 0.4     |       | Inv3       |       |       | Inv3 |
| 0 1 5   | 10    | 15 20      | 0 1 5 | 10 15 | 20   |
Figure18.ActiveandreactivepowersharingwithSDNmonolithiccontroller.
Ourproposalusesaproactiveapproachtolatencytestingandareactiveapproachto
managetopologychanges. Thearchitecturewillreactimmediatelyifanewdistributed
generationsourceisadded,allowingproperpowersharing,asFigure3shows. Onthe
otherhand,theorchestratorcanaddintelligencetothetopologyaccordingtoitsappro-
priateprogramming. Forexample,ourmonitoringsystemarchitecturecandetectlatency
increasing or node congestion and take the necessary actions to reduce the impact and

Sensors2023,23,3395 21of26
the consequences. For example, it can scale a more significant number of instances as
microservicesandthussimultaneouslyservemorecommunicationrequests.
8. Conclusions
Monolithiccontrollershaveseveraldrawbacksconcerningscalabilityandreliability.
In most cases, these architectures do not meet the requirements of fault tolerance and
rapid adaptability, which are imposed by networked microgrids. This proposal’s most
significantcontributionwasthepropertytodynamicallyreconfigurecontrolflowsbased
onamicroservicesarchitectureandtheautomaticdeploymentofmicroservicesinstances.
Usingabare-metalKubernetesclusteronaRaspberrypianddeployingdistributed
microservices allowed us to improve the reality of a distributed energy control system.
MicroservicestestbedsdemonstratedtheSDNcontrollers’rapiddeployment,portability,
highavailabilityandresiliencytoapplicationfailures.
TheKubernetesorchestratorprovidedgoodscalabilityofthecommunicationsystem,
aswellasimprovedthefaulttoleranceandreplicationcapacity. Thisisduetothehighfault
tolerance,capableofmanaginganddistributingtheloadbetweenmicroservices. Froma
comparativeperspective,thisproposalsignificantlyimprovesfailurerecoverytimeand
resilienceconcerningcommunicationsdevices.
TheAPIRESTmicroservicetopologyallowedthesplittingoftheSDNcontroller’s
corefunctionalitiesintosmall,well-definedfunctions. Inalltestcasescenarios,reliability
showedexcellentbehavior. Furthermore,theportabilityofallthenodesinthetopologyis
possibleduetotheDockercontainers. Theabilitytoexchangecontrolinformationbetween
DGs over an SDN network allows them to regulate the system’s response and reach a
steadystatemorequickly. Theresultsshowthattoincreasetheresilienceofthenetwork,
moresophisticatedcontrolstrategiesandhighlyavailableprogrammablecommunications
networksarerequired. Finally, themonitoringarchitectureallowstheexportoflogsin
real-timeanddetectsfailuresthroughnotificationsoftware.
Author Contributions: Conceptualization, R.P.; Investigation, R.P., M.R. and Y.S.; Methodology,
C.R.B.andP.W.;Projectadministration,M.R.;Software,R.P.,M.R.andY.S.;Supervision,C.R.B.and
P.W.;Validation,R.P.,M.R.,C.R.B.andP.W.;visualization,R.P.andY.S.;Writing—originaldraft,R.P.,
M.R.andC.R.B.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:ThisresearchwasfundedbytheNationalDoctorateScholarshipCONICYT2019;ANID/
ATE220023Project; FONDECYTRegularResearchProject1220556; CLIMATAMSUD21001and
FONDAPSERCChile15110019.
DataAvailabilityStatement:Notapplicable.
Acknowledgments:TheauthorsexpresstheirgratitudetotheUniversityofTalcaandtheUniversity
ofNottinghamfortheirsupportduringthisresearchperiod.Furthermore,wewouldliketothank
theµOnosTeamfortheguidelinesprovidedtocompletethismanuscript.
ConflictsofInterest:Theauthorsdeclarethattheyhavenoknowncompetingfinancialinterestsor
personalrelationshipsthatcouldhaveappearedtoinfluencetheworkreportedinthispaper.
Nomenclature
Thefollowingabbreviationsareusedinthismanuscript:
API ApplicationProgrammingInterface
SDN Software-definednetworking
DGs Distributedgenerators
NMG Networkedmicrogrids
PLECS TheSimulationPlatformforPowerElectronicSystems
µONOS MicroservicesOpenNetworkOperatingSystem

Sensors2023,23,3395 22of26
Bare-metal Physicaldevicedesignedtorundedicatedservices
AC/DC Alternatingcurrent/directcurrent
RESTAPI Representationalstatetransferforapplicationprogramminginterface
VSI Voltagesourceinverter
RL Resistive-inductiveload
P,Q Activeandreactivepower
MG Microgrid
ω Frequency
ω ,υ Nominalfrequencyandvoltage
ref ref
∆P,∆Q Powerinputerrorfordroopcontrol
m ,n Constanttohandlemaximumdeviationofthemicrogrid
p q
P ,Q Nominalfrequencyandvoltage
ref ref
υ Droopcontrolvoltage
dref
υ Voltageacrossthefilter
abc
α,β α,βconstantframe
i ,i Filterandoutputcurrents
f o
δω Frequencyobtainedbysecondarycontrol
DGk
δυ Voltageobtainedbysecondarycontrol
DGk
k ,k ControllerparametersofPI
pω iω
ω ,υ AveragefrequencyandvoltagebroadcastedbyeachDG
DGk DGk
QoS Qualityofservice
K3s LightweightKubernetes
ONF OpenNetworkFoundation
gRPC RemoteProcedureCalls
gNMI gRPCNetworkManagementInterface
gNOI gRPCNetworkOperationsInterface
NB,SB Northboundandsouthboundinterfaces
P4Runtime Controlplanespecificationforcontrollingthedataplaneelements
YANGmodel Yetanothernext-generationdatamodelinglanguage
CNI Kubernetescontainernetworkinterface
CAN Controllerareanetworkprotocol
SPI Serialperipheralinterface
I2C Inter-IntegratedCircuitcommunicationprotocol
OSPF Openshortestpathfirstcommunicationprotocol
AppendixA
PrimaryControl
Theprimarycontrolincludesoutercontrolloops(forvoltageregulation),innercontrol
loops(forcurrentregulation),anddroopcontrolloopstosharethepowerbetweeninverters.
Grid-forming(comprisedoftheinnerandouterloops)includesaproportional-integral
PIcontrollertoregulatetheoutputvoltageandfrequencyoftheMG.Furthermore,the
frequency and voltage amplitude can be addressed by droop control as shown in the
Equations(A1)and(A2),[1]:
ω = ω −m (P−P ) = ω −m ∆P (A1)
ref p ref ref p
υ = υ −n (Q−Q ) = υ −n ∆Q (A2)
dref ref q ref ref q
whereω andυ arethenominalfrequencyandvoltage,PandQarethemeasuredactive
ref ref
andreactivepowerinjection,and∆Pand∆Qarethecorrespondingpowerinputerrorsfor
thedroopcontroller. Coefficientsm andn regulatemaximumdeviationsallowedinthe
p q
MG[42,63].
Different lengths of transmission lines make the VSI output impedance different,
causingunequalpowersharingindroopcontrol. Virtualimpedanceisanessentialcon-

Sensors2023,23,3395 23of26
cept[64]tofixtheoutputimpedancevalueanddecouplethecontrolofactiveandreactive
powers. The virtual impedance can help to keep the voltage within certain limits and
isusedforapplicationssuchasharmonicvoltagecompensationandimprovedstability.
Refs.[37,65]showtheimplementationofvirtualimpedance. However,itisoutofthescope
ofthisresearch.
Thevoltageacrossthecapacitorυ canbecalculatedusingEquation(A3):
abc
|     |       | (t) =     | sin(ω              | t)+jυ |                     | cos(ω              | t)        |      |
| --- | ----- | --------- | ------------------ | ----- | ------------------- | ------------------ | --------- | ---- |
|     | υ abc | υ         | ref                | ref   |                     | ref                | ref       | (A3) |
|     |       | (cid:124) | (cid:123)(cid:122) |       | (cid:125) (cid:124) | (cid:123)(cid:122) | (cid:125) |      |
|     |       |           | ∗(t)               |       |                     | υ∗                 |           |      |
|     |       |           | υα                 |       |                     | (t)                |           |      |
β
whereυ andω arethevoltageamplitudeandangularfrequencyω =2πf ofthe
| ref ref |     |     |     |     |     |     | ref | ref |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- |
referencesignalintimet. ThevoltagederivativereferenceisobtainedfromEquation(A4):
dυ (t)
|     | abc | =     | cos(ω |     | t)+jω |           | sin(ω t) |      |
| --- | --- | ----- | ----- | --- | ----- | --------- | -------- | ---- |
|     |     | ω ref | υ ref | ref |       | ref υ ref | ref      | (A4) |
dt
|     |     | (cid:124) | (cid:123)(cid:122) |     | (cid:125) (cid:124) |        | (cid:123)(cid:122) (cid:125) |     |
| --- | --- | --------- | ------------------ | --- | ------------------- | ------ | ---------------------------- | --- |
|     |     |           | ωrefυ∗             |     |                     |        | ∗(t)                         |     |
|     |     |           |                    | (t) |                     | ωrefυα |                              |     |
β
To track υ it is necessary to expand the last results to α,β frame. The predicted
ref
currentsi f andmeasuredcurrentsi o arecalculatedas[64],topredictthecapacitorderivative
voltageasfollows:
|     |     |     | (t)−i     | (t)                |           | (t)−i     | (t)                          |      |
| --- | --- | --- | --------- | ------------------ | --------- | --------- | ---------------------------- | ---- |
|     | dυ  | (t) | i fα      | oα                 |           | i fβ      | oβ                           |      |
|     | abc | =   |           |                    | +j        |           |                              | (A5) |
|     | dt  |     | C         | f                  |           |           | C f                          |      |
|     |     |     | (cid:124) | (cid:123)(cid:122) | (cid:125) | (cid:124) | (cid:123)(cid:122) (cid:125) |      |
|     |     |     | dυabcα(t) |                    |           | dυabcβ(t) |                              |      |
|     |     |     |           | dt                 |           |           | dt                           |      |
From Equation (A5), it can be seen that the derivative path of the voltage can be
trackediftheerrorbetweenthefirsttermandthesecond(A4)and(A5)isminimized.
AppendixB
SecondaryControl
Secondary control allows the regulation of voltage and frequency, which are not
adjustedbytheprimarycontrolloop. Implementingalocalsecondarycontrollerateach
distributed generator (DG) results in improved output quality and offers a significant
advantagecomparedtocentralizedcontrollerapproaches[10].
EachDGmeasuresitsfrequencyateachsamplingtime,averagingthereceivedinfor-
mationfromotherunitsandthenbroadcastingitsaverageversion(ω DG )totheotherDGs.
Then,theconsensusdataiscomparedwiththenominalfrequencyoftheMG(ω )and
ref
senttothesecondarycontrollerofDG torestorethefrequencyusing:
i
(cid:90)
| δω  | =   | k (ω | −ω  | )+k |     | (ω  | −ω )dt | (A6) |
| --- | --- | ---- | --- | --- | --- | --- | ------ | ---- |
|     | DGk | pω   | ref | DGk | iω  | ref | DGk    |      |
∑N
ω
|     |     |     | ω¯  | = i=1 | DGi |     |     | (A7) |
| --- | --- | --- | --- | ----- | --- | --- | --- | ---- |
DGk
N
wherek pω andk iω arethecontrollerparametersofPIandδω DGk isthecompensatorsignal
forprimarycontrol(refertoSecondaryControlblockshowninFigure6). ω andω
DGk ref
aretheaveragesoffrequencyforallDGsandreferencefrequencyoftheMG,respectively.
Aftercalculatingtheaveragevoltagereceivedfromthecommunicationnetwork(υ ),
MG
thelocalcontrollerdeterminestheerrorbetweenthisvalueandthevoltagereferenceυ ref
asshowninEquation(A8). Finally,δυ issenttotheprimarycontroltocompensatefor
DGk
thevoltagedeviation. ThestrategyisshowninthePowerSystemlayerofFigure6.
(cid:90)
| δυ  | =   | k (υ | −υ  | )+k |     | (υ  | −υ )dt | (A8) |
| --- | --- | ---- | --- | --- | --- | --- | ------ | ---- |
|     | DGk | pv   | abc | DGk | iv  | abc | DGk    |      |

Sensors2023,23,3395 24of26
∑N υ
υ = i=1 DGi (A9)
DGk
N
where v refers to average voltages broadcasted from each DG at the sampling time.
DGk
Smallsignalrepresentationsofthefrequencyandvoltageforsecondarycontrolaredetailed
in[63].
References
1. Tinajero,G.D.A.;Nasir,M.;Vasquez,J.C.;Guerrero,J.M.Comprehensivepowerflowmodellingofhierarchicallycontrolled
AC/DChybridislandedmicrogrids.Int.J.Electr.PowerEnergySyst.2021,127,106629.[CrossRef]
2. Han,Y.;Li,H.;Shen,P.;Coelho,E.A.A.;Guerrero,J.M.Reviewofactiveandreactivepowersharingstrategiesinhierarchical
controlledmicrogrids.IEEETrans.PowerElectron.2016,32,2427–2451.[CrossRef]
3. Kulkarni,S.V.;Gaonkar,D.N.Improveddroopcontrolstrategyforparallelconnectedpowerelectronicconverterbaseddistributed
generationsourcesinanIslandedMicrogrid.Electr.PowerSyst.Res.2021,201,107531.[CrossRef]
4. Pérez-Guzmán,R.E.;Salgueiro-Sicilia,Y.;Rivera,M.Communicationsinsmartgrids. InProceedingsofthe2017CHILEAN
ConferenceonElectrical,ElectronicsEngineering,InformationandCommunicationTechnologies(CHILECON),Pucon,Chile,
18–20October2017;pp.1–7.
5. Simpson-Porco,J.W.;Shafiee,Q.;Dörfler,F.;Vasquez,J.C.;Guerrero,J.M.;Bullo,F.Secondaryfrequencyandvoltagecontrolof
islandedmicrogridsviadistributedaveraging.IEEETrans.Ind.Electron.2015,62,7025–7038.[CrossRef]
6. Khayat,Y.;Shafiee,Q.;Heydari,R.;Naderi,M.;Dragicˇevic´,T.;Simpson-Porco,J.W.;Dörfler,F.;Fathi,M.;Blaabjerg,F.;Guerrero,
J.M.;etal.OnthesecondarycontrolarchitecturesofACmicrogrids:Anoverview.IEEETrans.PowerElectron.2019,35,6482–6500.
[CrossRef]
7. Ferreira,D.;Silva,S.;Silva,W.;Brandao,D.;Bergna,G.;Tedeschi,E.OverviewofConsensusProtocolandItsApplicationto
MicrogridControl.Energies2022,15,8536.[CrossRef]
8. Shan,Y.;Pan,A.;Liu,H.Aswitchingevent-triggeredresilientcontrolschemeforprimaryandsecondarylevelsinACmicrogrids.
ISATrans.2022,127,216–228.[CrossRef]
9. Shafiee,Q.;Dragicˇevic´,T.;Vasquez,J.C.;Guerrero,J.M.HierarchicalcontrolformultipleDC-microgridsclusters. IEEETrans.
EnergyConvers.2014,29,922–933.[CrossRef]
10. Zhou,Q.;Shahidehpour,M.;Paaso,A.;Bahramirad,S.;Alabdulwahab,A.;Abusorrah,A.Distributedcontrolandcommunication
strategiesinnetworkedmicrogrids.IEEECommun.Surv.Tutor.2020,22,2586–2633.[CrossRef]
11. Yang,L.;Ng,B.;Seah,W.K.;Groves,L.;Singh,D.AsurveyonnetworkforwardinginSoftware-DefinedNetworking.J.Netw.
Comput.Appl.2021,176,102947.[CrossRef]
12. Ndiaye, M.; Hancke, G.P.; Abu-Mahfouz, A.M.; Zhang, H. Software-defined power grids: A survey on opportunities and
taxonomyformicrogrids.IEEEAccess2021,9,98973–98991.[CrossRef]
13. Ren,L.;Qin,Y.;Li,Y.;Zhang,P.;Wang,B.;Luh,P.B.;Han,S.;Orekan,T.;Gong,T.Enablingresilientdistributedpowersharingin
networkedmicrogridsthroughsoftwaredefinednetworking.Appl.Energy2018,210,1251–1265.[CrossRef]
14. Ren,L.;Qin,Y.;Wang,B.;Zhang,P.;Luh,P.B.;Jin,R.EnablingResilientMicrogridThroughProgrammableNetwork.IEEETrans.
SmartGrid2017,8,2826–2836.[CrossRef]
15. Danzi,P.;Angjelichinoski,M.;Stefanovic,C.;Dragicevic,T.;Popovski,P.Software-DefinedMicrogridControlforResilience
AgainstDenial-of-ServiceAttacks.IEEETrans.SmartGrid2019,10,5258–5268.[CrossRef]
16. Comer,D.;Rastegarnia,A.TowarddisaggregatingtheSDNcontrolplane.IEEECommun.Mag.2019,57,70–75.[CrossRef]
17. Arzo,S.T.;Scotece,D.;Bassoli,R.;Barattini,D.;Granelli,F.;Foschini,L.;Fitzek,F.H.MSN:APlaygroundFrameworkforDesign
andEvaluationofMicroServices-BasedsdNController.J.Netw.Syst.Manag.2022,30,1–31.[CrossRef]
18. Siddiqui,S.;Hameed,S.;Shah,S.A.;Ahmad,I.;Aneiba,A.;Draheim,D.;Dustdar,S.TowardsSoftware-DefinedNetworking-
basedIoTFrameworks: ASystematicLiteratureReview, Taxonomy, OpenChallengesandProspects. IEEEAccess2022, 10,
70850–70901.[CrossRef]
19. Isong,B.;Molose,R.R.S.;Abu-Mahfouz,A.M.;Dladlu,N.ComprehensivereviewofSDNcontrollerplacementstrategies.IEEE
Access2020,8,170070–170092.[CrossRef]
20. NipponTelegraphandTelephoneCorporation(NTT).RyuSDNController.Availableonline:https://ryu-sdn.org/(accessedon
22December2022).
21. OpenDaylight(ODL)Controller.Availableonline:https://www.opendaylight.org/(accessedon3June2022).
22. ONOSProjectCommunity.OpenNetworkOperatingSystem(ONOS).Availableonline:https://opennetworking.org/onos/
(accessedon18January2023).
23. Markelov,A.OpenStackNetworking.InCertifiedOpenStackAdministratorStudyGuide;Springer:Berlin/Heidelberg,Germany,
2022;pp.77–121.
24. Hölscher,A.;Asplund,M.;Boeira,F.EvaluationofanSDN-basedMicroserviceArchitecture.InProceedingsofthe2022IEEE8th
InternationalConferenceonNetworkSoftwarization(NetSoft),Milan,Italy,27June–1July2022;pp.151–156.

Sensors2023,23,3395 25of26
25. OpenNetworkFoundation.OpenNetworkOperatingSystem(ONOS).Availableonline:https://docs.onosproject.org/(accessed
on22October2022).
26. Ray,P.P.;Kumar,N.SDN/NFVarchitecturesforedge-cloudorientedIoT:Asystematicreview. Comput. Commun. 2021,169,
129–153.[CrossRef]
27. Okwuibe,J.; Haavisto,J.; Harjula,E.; Ahmad,I.; Ylianttila,M.SDNenhancedresourceorchestrationofcontainerizededge
applicationsforindustrialIoT.IEEEAccess2020,8,229117–229131.[CrossRef]
28. Nsafoa-Yeboah, K.; Tchao, E.T.; Yeboah-Akowuah, B.; Kommey, B.; Agbemenu, A.S.; Keelson, E.; Monirujjaman Khan, M.
Software-DefinedNetworksforOpticalNetworksUsingFlexibleOrchestration:Advances,Challenges,andOpportunities.J.
Comput.Netw.Commun.2022,2022,5037702.[CrossRef]
29. Marzal, S.; Salas, R.; González-Medina, R.; Garcerá, G.; Figueres, E. Current challenges and future trends in the field of
communicationarchitecturesformicrogrids.Renew.Sustain.EnergyRev.2018,82,3610–3622.[CrossRef]
30. Abbasi, M.; Abbasi, E.; Li, L.; Aguilera, R.P.; Lu, D.; Wang, F. Review on the Microgrid Concept, Structures, Components,
CommunicationSystems,andControlMethods.Energies2023,16,484.[CrossRef]
31. Lévy,L.N.;Bosom,J.;Guerard,G.;Amor,S.B.;Bui,M.;Tran,H.DevOpsModelAppproachforMonitoringSmartEnergySystems.
Energies2022,15,5516.[CrossRef]
32. Johansson,B.;Rågberger,M.;Nolte,T.;Papadopoulos,A.V.Kubernetesorchestrationofhighavailabilitydistributedcontrol
systems. InProceedingsofthe2022IEEEInternationalConferenceonIndustrialTechnology(ICIT),Shanghai,China,22–25
August2022;pp.1–8.
33. Zhu,C.;Han,B.;Zhao,Y.AComparativeStudyofSparkonthebaremetalandKubernetes. InProceedingsofthe20206th
InternationalConferenceonBigDataandInformationAnalytics(BigDIA),Shenzhen,China,4–6December2020;pp.117–124.
34. Huedo,E.;Montero,R.S.;Moreno-Vozmediano,R.;Vázquez,C.;Holer,V.;Llorente,I.M.Opportunisticdeploymentofdistributed
edgecloudsforlatency-criticalapplications.J.GridComput.2021,19,1–16.[CrossRef]
35. Tonini,F.;Natalino,C.;Temesgene,D.A.;Ghebretensaé,Z.;Wosinska,L.;Monti,P.BenefitsofPoddimensioningwithbest-effort
resourcesinbaremetalcloudnativedeployments.IEEENetw.Lett.2023,5,41–45.[CrossRef]
36. Klos,A.;Rosenbaum,M.;Schiffmann,W.Scalableandhighlyavailablemulti-objectiveneuralarchitecturesearchinbaremetal
kubernetescluster.InProceedingsofthe2021IEEEInternationalParallelandDistributedProcessingSymposiumWorkshops
(IPDPSW),Portland,OR,USA,17–21June2021;pp.605–610.
37. Guzmán,R.E.P.;Rivera,M.;Wheeler,P.W.;Mirzaeva,G.;Espinosa,E.E.;Rohten,J.A.MicrogridPowerSharingFrameworkfor
SoftwareDefinedNetworkingandCybersecurityAnalysis.IEEEAccess2022,10,111389–111405.[CrossRef]
38. Yadav, G.; Joshi, D.; Gopinath, L.; Soni, M.K. Reliability and Availability Optimization of Smart Microgrid Using Specific
ConfigurationofRenewableResourcesandConsideringSubcomponentFaults.Energies2022,15,5994.[CrossRef]
39. Ahmad,S.;Mir,A.H.Scalability,Consistency,ReliabilityandSecurityinSDNControllers:ASurveyofDiverseSDNControllers.
J.Netw.Syst.Manag.2021,29,9.[CrossRef]
40. Mokhtar,H.;Di,X.;Zhou,Y.;Hassan,A.;Ma,Z.;Musa,S.Multiple-levelthresholdloadbalancingindistributedSDNcontrollers.
Comput.Netw.2021,198,108369.[CrossRef]
41. Gupta,N.;Maashi,M.S.;Tanwar,S.;Badotra,S.;Aljebreen,M.;Bharany,S.AComparativeStudyofSoftwareDefinedNetworking
ControllersUsingMininet.Electronics2022,11,2715.[CrossRef]
42. Guerrero, J.M.; Vasquez, J.C.; Matas, J.; DeVicuna, L.G.; Castilla, M.Hierarchicalcontrolofdroop-controlledACandDC
microgrids—Ageneralapproachtowardstandardization.IEEETrans.Ind.Electron.2010,58,158–172.[CrossRef]
43. Garces,L.MicrogridinIslandOperation.2022.Availableonline:https://www.plexim.com/support/application-examples/1259
(accessedon3December2022).
44. Garces,L.J.;Liu,Y.;Bose,S.SystemandMethodforIntegratingWindandHydroelectricGenerationandPumpedHydroEnergy
StorageSystems.U.S.Patent7,239,035,3July2007.
45. Zargar,R.H.M.;Yaghmaee,M.H.EnergyexchangecooperativemodelinSDN-basedinterconnectedmulti-microgrids.Sustain.
EnergyGridsNetw.2021,27,100491.[CrossRef]
46. Khorsandroo,S.;GallegoSanchez,A.;Tosun,A.S.;Arco,J.;Doriguzzi-Corin,R.HybridSDNevolution:Acomprehensivesurvey
ofthestate-of-the-art.Comput.Netw.2021,192,107981.[CrossRef]
47. Biswas,R.;Wu,J.TrafficEngineeringtoMinimizetheNumberofRulesinSDNDatacenters.IEEETrans.Netw.Sci.Eng.2021,8,
1467–1477.[CrossRef]
48. Miguel-Alonso,J.AResearchReviewofOpenFlowforDatacenterNetworking.IEEEAccess2022,11,770–786.[CrossRef]
49. CNCFoundations.Availableonline:https://k3s.io/(accessedon25November2022).
50. Labs,R.Rancher:EnterpriseKubernetesManagement.Availableonline:https://www.rancher.com/(accessedon25November
2022).
51. Wazirali,R.;Ahmad,R.;Alhiyari,S.SDN-OpenFlowTopologyDiscovery:AnOverviewofPerformanceIssues.Appl.Sci.-Basel
2021,11,6999.[CrossRef]
52. Yan, L.; Sheikholeslami, M.; Gong, W.; Shahidehpour, M.; Li, Z. Architecture, Control, and Implementationof Networked
MicrogridsforFutureDistributionSystems.J.Mod.PowerSyst.CleanEnergy2022,10,286–299.[CrossRef]
53. SivaAnanmalay,J.A.;Barton,D.OpenNetworkingFoundation.2022.Availableonline:https://opennetworking.org/(accessed
on16July2022).

Sensors2023,23,3395 26of26
54. Vachuska,T.ONOSHelmCharts.2023.Availableonline:https://github.com/onosproject/onos-helm-charts(accessedon3
December2022).
55. Vachuska,T.;Halterman,J.Atomix-Controller: KubernetesControllerforAtomix4. Availableonline: https://github.com/
atomix/atomix-controller(accessedon16July2022).
56. Open Network Foundation. Deploying Onos-Config. Available online: https://docs.onosproject.org/onos-config/docs/
deployment/(accessedon7December2022).
57. Pérez,R.DeployHAKubernetesClusterforSDNMicrogridHierarchicalControl.2023.Availableonline:https://github.com/
ricardopg1987/kubernetes-rpi(accessedon3December2022).
58. CNCFoundations.Availableonline:https://docs.k3s.io/installation/ha-embedded(accessedon25September2022).
59. KubeSphere.SetupanHAKubernetesClusterUsingKeepalivedandHAproxy.2023.Availableonline:https://kubesphere.io/
docs/v3.3/installing-on-linux/high-availability-configurations/set-up-ha-cluster-using-keepalived-haproxy/(accessedon25
September2022).
60. Zhang,Z.Acomparisonoflow-speedcommunicationmodes. InProceedingsoftheInternationalConferenceonNetwork
CommunicationandInformationSecurity(ICNCIS2021),Qingdao,China,19–21August2022;Volume12175,pp.38–43.
61. ZodiacFXCommunicationDevice.Availableonline:https://www.cryptomuseum.com/radio/zodiac/(accessedon17March
2023).
62. Muhammad,A.;Saqib,M.;Song,W.C.SensorVirtualizationandDataOrchestrationinInternetofVehicles(IoV).InProceedings
ofthe2021IFIP/IEEEInternationalSymposiumonIntegratedNetworkManagement(IM),Bordeaux,France,18–20May2021;
pp.998–1003.
63. Heydari,R.;Dragicevic,T.;Blaabjerg,F.High-bandwidthsecondaryvoltageandfrequencycontrolofvsc-basedacmicrogrid.
IEEETrans.PowerElectron.2019,34,11320–11331.[CrossRef]
64. Dragicˇevic´,T.ModelpredictivecontrolofpowerconvertersforrobustandfastoperationofACmicrogrids.IEEETrans.Power
Electron.2017,33,6304–6317.[CrossRef]
65. Villalón,A.;Rivera,M.;Salgueiro,Y.;Munoz,J.;Dragicˇevic´,T.;Blaabjerg,F.Predictivecontrolformicrogridapplications: A
reviewstudy.Energies2020,13,2454.[CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.