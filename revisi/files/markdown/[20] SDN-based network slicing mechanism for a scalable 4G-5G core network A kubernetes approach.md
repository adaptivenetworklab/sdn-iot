# [20] SDN-based network slicing mechanism for a scalable 4G-5G core network A kubernetes approach

> Source file: `[20] SDN-based network slicing mechanism for a scalable 4G-5G core network A kubernetes approach.pdf`

---

sensors
Article
SDN-Based Network Slicing Mechanism for a Scalable 4G/5G
†
Core Network: A Kubernetes Approach
RobertBotez1,*,JoseCosta-Requena2 ,Iustin-AlexandruIvanciu1 ,VladStrautiu1andVirgilDobrota1
1 CommunicationsDepartment,TechnicalUniversityofCluj-Napoca,400114Cluj-Napoca,Romania;
Iustin.Ivanciu@com.utcluj.ro(I.-A.I.);Vlad.STRAUTIU@student.utcluj.ro(V.S.);
Virgil.Dobrota@com.utcluj.ro(V.D.)
2 DepartmentofCommunicationsandNetworking,AaltoUniversity,02150Espoo,Finland;Jose.Costa@aalto.fi
* Correspondence:Robert.Botez@com.utcluj.ro
† ThispaperisanextendedversionofourpaperpublishedinBotez,R.;Strautiu,V.;Ivanciu,I.-A.;Dobrota,V.
ContainerizedApplicationforIoTDevices:ComparisonbetweenbalenaCloudandAmazonWebServices
Approaches.InProceedingsofthe2020InternationalSymposiumonElectronicsandTelecommunications
(ISETC),Timisoara,Romania,5–6November2020;pp.1–4,doi:10.1109/ISETC50328.2020.9301070.
Abstract: ManagingthelargevolumesofIoTandM2Mtrafficrequirestheevaluationofthescal-
abilityandreliabilityforallthecomponentsintheend-to-endsystem.Thisincludesconnectivity,
mobilenetworkfunctions,andapplicationorservicesreceivingandprocessingthedatafromend
devices.Firstly,thispaperdiscussesthedesignofacontainerizedIoTandM2Mapplicationand
themechanismsfordeliveringautomatedscalabilityandhighavailabilitywhendeployingitin:
(cid:1)(cid:2)(cid:3)(cid:1)(cid:4)(cid:5)(cid:6)(cid:7)(cid:8)(cid:1)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:6)(cid:7) (1)theedgeusingbalenaCloud;(2)theAmazonWebServicescloudwithEC2instances;and(3)the
dedicatedAmazonWebServicesIoTservice.Theexperimentsshowedthattherearenosignificant
Citation: Botez,R.;Costa-Requena, differencesbetweenedgeandclouddeploymentsregardingresourceconsumption.Secondly,the
J.;Ivanciu,I.-A.;Strautiu,V.;Dobrota,
solutionsforscalingthe4G/5Gnetworkfunctionsandmobilebackhaulthatprovidetheconnectivity
V.SDN-BasedNetworkSlicing
betweendevicesandIoT/M2Mapplicationsareanalyzed. Inthiscase, thescalabilityandhigh
MechanismforaScalable4G/5G
availabilityofthe4G/5GcomponentsareprovidedbyKubernetes.Theexperimentsshowedthat
CoreNetwork:AKubernetes
ourproposedscalingalgorithmfornetworkslicingmanagedwithSDNguaranteesthenecessary
Approach.Sensors2021,21,3773.
radioandnetworkresourcesforend-to-endhighavailability.
https://doi.org/10.3390/s21113773
AcademicEditors:Daniel-Ioan Keywords:5G;cloudcomputing;EPC;IoT;Kubernetes;networkslicing;NFV;SDN
Curiac,FlorinAlexaandMarius
Otesteanu
Received:29April2021 1. Introduction
Accepted:26May2021 TheInternetofThings(IoT)hasseenamajorgrowthinrecentyearsthankstovari-
Published:29May2021
ousapplicationsemergingasaconsequenceoftheevolutionofsmartsensors,artificial
intelligence,robotics,ornetworkingtechnologies. Accordingto[1],Ciscopredictsthat
Publisher’sNote:MDPIstaysneutral
halfoftheworld’sconnecteddeviceswillberepresentedbymachine-to-machine(M2M)
withregardtojurisdictionalclaimsin
communications, reaching up to 14.7 billion connections or 1.8 M2M connections per
publishedmapsandinstitutionalaffil-
inhabitantoftheglobalpopulation.Althoughinthepreviousreport,M2MandIoTare
iations.
consideredtwosidesofthesamecoin,thereisadifferencebetweenthem.Whiletheformer
ischaracterizedbypoint-to-pointcommunicationswithtelemetryasthemainapplication,
thelatterexpandthiscapabilitybyconvergingpoolsofM2Misolatedsystemsoverthe
Internet. ThedifferencesbetweenthesetwotechnologiesareseeninTable1[2].
Copyright: © 2021 by the authors. Duetothefastgrowthoftheindustry,theamountofdatageneratedbytheentire
Licensee MDPI, Basel, Switzerland. IoT environment will be very high. All these data need to be stored, processed, and
This article is an open access article
analyzedinascalableinfrastructure[3].Withitscapacitytoofferon-demandandscalable
distributed under the terms and
services,cloudcomputingistheperfectcandidatefordeployingIoTapplications.Usually,
conditionsoftheCreativeCommons
applicationsarerunningonavirtualizedinfrastructureinthecloud. Thisapproachhas
Attribution(CCBY)license(https://
severalbenefitscomparedtousingbaremetalserversincludingreducingthecapitaland
creativecommons.org/licenses/by/
operatingexpenses(CAPEXandOPEX),increasingthesecurity,efficiency,andscalability
4.0/).
Sensors2021,21,3773.https://doi.org/10.3390/s21113773 https://www.mdpi.com/journal/sensors

Sensors2021,21,3773 2of26
andsolutionrecoveryincaseofdisasters.Althoughbaremetalserversaremoresuitablefor
mission-criticalapplicationswherelatencyiscrucial,newoptimizationtechniquesmakeit
possibletoadoptvirtualizationtechnologyin5Gindustrialapplicationsthatrequire1ms
round-triptime(RTT)[4].
Table1.ComparisonofM2MandIoT.
M2M IoT
Point-to-pointcommunications ConnectivityviaIPnetworks
Hardware-basedtechnology Suitableforbothhardwareandsoftware
NotdependentontheInternet ReliesonInternetconnectivity
Device-basedcommunications Interfacedeviceswithgatewaysordatasystems
Limitedscalability Scalabilityisakeyrequirement
Containerizationtechnologyhasbecomeareliablesolutionforhostingapplicationsin
thecloud. Acomparisonbetweencontainerizationandvirtualization[5]hasshownthat
containershaveahigherscalabilitythanvirtualmachines(VMs),makingthemabetter
alternativeforIoTscenarioswherescalabilityisimportant.
IoTapplicationscomeinallshapesandsizesand,assuch,theymustfulfillrequire-
mentsintermsoflong-rangetransmissions,costs,energyefficiency,latency,andbandwidth.
Thetechnologiesthatmeettheserequirementsbelongtothelow-powerwide-areanetwork
(LPWAN)domain.LPWANtechnologiescanbedividedintotwocategories: cellular(LTE-
MandNB-IoT)andnon-cellular(Sigfox,LoRaWAN,andSymphonyLink).Thechoiceof
usingaspecificLPWANtechnologydependsontherequirementsthattheIoTapplications
mustmeet;forexample,Sigfoxisthebestoptionifthegoalistohaveabettercoverage,
whileLoRahastheadvantageofaflexibledeployment. However,whenitcomestoappli-
cationswhereQoS,latency,scalability,anddataratesaremoreimportant,NB-IoTisthe
waytogo[6].
Nonetheless,theadventofthe5Gtechnologyshouldbringabouteffectiveinterconnec-
tionsbetweenthevastnumbersofIoTdevices.The5Gtechnologystandard[7]istailored
forthreespecifictypesofservices:
• Enhanced mobile broadband (eMBB) will provide higher bandwidths and lower
latency. Itwillbesuitableforsmarthomeapplications,ultra-high-definition(UHD)
television,orCloudgamingservices(forexample,GoogleStadia).
• Massivemachine-typecommunications(mMTC)willimprovetheexistinglow-power
wide-area networks (LPWANs). The purpose of this type of service is to pave the
wayforsmartcities. ThetwoLPWANtechnologiesusedin4Gnetworks,NB-IoTand
LTE-M,willstillbeusedandwillbeimportantfactorsinmeetingtherequirementsof
the5GstandardforIoT.
• Ultra-reliableandlow-latencycommunications(URLLC)isaspecialtypeofcommu-
nicationsdesignedformission-criticalapplicationswhichrequiremorebandwidth
andlowerlatenciesthanmMTC.Aspecificcaseisillustratedin[8],whereURLLC
slicesprovidelowlatencyforautonomouscarsinanSDN-basedcorenetwork(CN).
Taking into account the requirements for 5G networks and also the fact that this
technologyisdesignedformorethanjustmobilebroadband[9],anewparadigmshouldbe
appliedinbackhaulandcorenetworks. Therequirementsoflatencyandhighavailability
forURLLCtrafficcouldberesolvedbyenablingSDNinthebackhaulnetwork(BN).More-
over,the5Gcorenetworkhasaservice-basedarchitecture(SBA),whichmeansthatthe
componentscouldbeimplementedassoftwareanddeployedusingnetworkfunctionsvir-
tualization(NFV)asnetworkfunctions(NFs). UsingNFVmanagementandorchestration
(MANO)platformsforvirtualnetworkfunctions(VNFs)ornetworksliceswouldleadtoa
5Greliablecorenetwork. Movingthecorecomponentsfromphysicaldedicatedserversto
virtualizedcomponentsrunningonanetworkfunctionvirtualizationinfrastructure(NFVI)

Sensors2021,21,3773 3of26
bringsmanybenefitsnotonlyintermsofcapitalandoperationalexpenditurebutalsoin
termsofefficiencyandscalability[10]. However,therearestillsomedrawbacks,mainly
becausetheVNFsareusuallydeployedinvirtualmachines. Thus,scaling,orchestrating,
andmanagingtheseVMsforlarge-scaledeploymentsbecomesadifficultjobduetothe
large overhead induced by virtualization. To overcome these limitations, migration to
cloud-nativenetworkfunctions(CNFs)mustbeperformed.CNFs[11]aremainlyVNFsop-
timizedtooperateinavirtualcloudenvironment: theyarebasedonmicroservices,hosted
intocontainersandcanbeorchestratedwithKubernetes. Thus,reducingtheoverhead
wouldbeaccomplishedbycontainerization. Moreover,therearemanyadvantagesthat
CNFscanbenefitfromthankstotheintrinsicpropertiesofKubernetessuchasautoscaling,
high-availability,resilience,orbuilt-intelemetryservices.
Thispaperextendsourpreviousworkpresentedin[12].Asafirstcontribution,taken
from [12], we compared the resource consumption of an IoT containerized telemetry
application in different scenarios, with data processing performed either in the cloud
(AmazonWebServicesEC2andAmazonWebServicesIoT)orintheedge(balenaCloud).
Foramoreaccuratecomparison,weusedsimilarresources,theonlydifferencebeingthe
hardwarearchitecturefortheedgedeployment,whichwasARM-based.Theresultswere
similarforresourceconsumptionintermsofCPUandRAMmemory.However,aswehave
seeninthepreviousparagraphs,5GwillbeusedformMTCandothertypesofservices,
someofwhicharesensitivetolatency.Thus,in5GscenariossuchasindustrialIoT,not
onlytheconsumptionofthecomputationalresourcesmustbetakenintoaccount,butalso
theefficiencyofthenetworkintermsoflatency,throughput,andeventuallypacket-loss.
Asasecondcontribution,thispaperproposestheusageofnetworkslicingsupportedin5G
networkstoseparateradio,transport,andcorenetworkfunctionsfordifferentUEswith
differenttrafficrequirements. Anovelsolutionofnetworkslicescalabilityformanaging
NB-IoTtrafficbasedontheleast-loadCNF,managedwithSDN,ispresented.
Thepaperisorganizedasfollows. Section2presentsanoverviewoftherelatedwork,
and Section 3 describes the proposed architecture for two scenarios. The first scenario
involvesresourceconsumptionforanIoTapplicationdeployedinbalenaCloud,Amazon
WebServicesEC2andAmazonWebServicesIoT.Thesecondscenarioreferstothenetwork
slicescalabilityformanagingIoTandMBBbasedontheleast-loadCNFmanagedwith
SDNandKubernetesinaprivatecloudorchestratedbyOpenStack. Section4presentsthe
experimentalresultsandSection5concludesthepaper.
2. RelatedWork
AlthoughtechnologiessuchasSDNandNFVhavebeenpresentforsometime,itis
withtheemergenceof5Gthattheywillprovetheirtruepotential. First,theyprovidea
financialadvantage. In[13],astudywasconductedtoanalyzetheimpactofusingSDN,
NFVandCloudcomputingin5GnetworksfortheCAPEX,theOPEXandthetotalcostof
ownership(TCO).Itwasobservedthatincomparisonwiththetraditionalarchitecture,the
CAPEXwouldbereducedby68%,theOPEXby63%,andtheTCOby69%. Moreover,the
developmentofNFVmanagementandorchestration(MANO)platformsmakesiteasierto
manageandorchestratevirtualnetworkfunction(VNF)instancesornetworkslices. This
way,thesetechnologiescouldhelpinimplementingareliableandscalable5Gcorenetwork.
Forexample,therearesomecommercialsolutionsfor4Gand5Gcorenetworksonthe
marketthatrelyonthepreviouslymentionedtechnologiessuchas[14,15], or[16].The
cloud-nativearchitectureofthesedeploymentscomeswithsomeadvantages,animportant
onebeingtheabilitytoorchestrateandschedulethemobilecorecomponentsondemand
inordertodelivertherequiredserviceswiththeproperqualityofexperience(QoE).
In[17],therequirementsandchallengesregardingtheimplementationofanEPCasa
serviceinacloudenvironment,alongwiththepotentialsolutionstothesechallenges,are
presented.TheauthorsidentifiedfourtypesofmappingsbetweentheinstancesofEPC
functionsandthenumberofVMsforthisapproach,namely1:1,1:N,N:1,andN:2. These
mappingsarethencompared,eachhavingadvantagesanddisadvantageswhenitcomes

Sensors2021,21,3773 4of26
todeployingtheEPCasaservice(EPCaaS).Forexample,althoughthe1:1mappinghas
asimplisticarchitecturewitheachEPCcomponentbeinghostedinaseparateVM,other
aspectssuchasscalingcouldbedifficulttoimplement. Therefore,anappropriatemapping
mustbechosenaccordingtothecharacteristicsofservicesandapplicationsusingtheEPC.
In[18],asolutiontomigratetheMMEcomponentintoacloud-nativeone,inorderto
implementdynamicallyauto-scaling,wasproposed. Themotivationforthepaperwasto
minimizetheoverheadduetocontrolsignalingfromIoTapplicationsimplementedover
5Gnetworks.AcomparisonbetweentheproposedMMEscalablesolutionandthelegacy
oneindicatesthatCPUconsumptiondecreasedby26.64%andthethroughputwashigher
by7.19%forthescalablesolution. AnothersolutionforscalingtheMMEistheSCALE
framework proposed in [19]. This framework also uses an 1:N mapping, which means
that the MME needs to be redesigned by introducing two more components: an MME
LoadBalancer(MLB),whichforwardsthetrafficfromUEtothespecificMME,andthe
MMEprocessingentity(MME),whichstoresinformationrelatedtosessionsandrequests
madebytheUEstotheMME.Althoughtheresultsarepromising,redesigningtheMME
forrealproductscanbecomeproblematic. Also,findingthecorrectMMEwithinapoolfor
aspecificrequestfromaUEcanincreasethelatencyoftheprocedure. Theselimitationsare
overcomeina5GcorenetworkbysplittingtheMMEintothreecomponents: AMF,SMF,
andUDM.Inthisapproach,theAMFwouldbescaled,sinceitisthecomponentwhich
doestheprocessing,whiletheUDMishostingtheUEcontexts. Thismakesitpossiblefor
aUEtobeservedbyanyAMFconnectedtothatUDM.AnalgorithmforscalingtheAMF
basedontheloadoftheinstancesispresentedin[20].
Asolutiontoguaranteetheresourcesfordifferenttrafficrequirementsandensurea
certainqualityofexperienceisgivenbynetworkslicing. Oneoptionforimplementing
networkslicesisbasedontheintegrationofSDNformanagingtheBNresources. In[21],
a solution for providing URLLC using network slices in an SDN backhaul network is
presented. Theauthorsdevelopedanalgorithmthatmonitorsthelatencyofthelinksin
thebackhaultopologyandthencomputestheshortestpathbasedonDijkstra’salgorithm.
Thus,theURLLCtrafficwillalwaysbeforwardedviatheshortestpath,ensuringthelow
latency requirement for this type of communication. In [22], another case for ensuring
URLLC traffic with SDN is illustrated. In this paper, NB-IoT devices are allocated in
the URLLC slice, where the low latency is maintained by policies implemented in the
SDNcontroller. Moreover,withtheincreaseofnetworkcongestion,thepacketlossalso
increasesforthenon-URLLCslice.Aviablesolutionforcreatingthenetworkslicesincloud
environments is the integration of SDN with a network hypervisor. In [23], the Libera
hypervisorwasusedtocreateaproof-of-conceptmodel,calledprogrammablenetwork
infrastructureasaservice(p-NIaaS).Thismodelprovidesanaccessiblewayfortenants
toprogramtheirallocatednetworkinfrastructureinacloudinfrastructure. Byexposing
thevirtualNIs,thenetworkslicingcouldbeenabledwiththeuseofSDNoverthetenant
virtualizednetworkinfrastructure.
Overthelastyears,alternativestotheclassicalOpenFlow-basedswitchOpenvSwitch[24]
weredeveloped. OneofthemistheprogrammablevirtualswitchusedintheMicrosoft
Azurepubliccloud, virtualfilteringplatform(VFP)[25].VFPisbasedonmatch-action
tables(MATs),whichareimplementedaslayerstoenableamulti-controllermodel,with
eachcontrollerbeingabletoapplyitspolicytotheswitchinadifferentlayer. Another
powerful solution used in public clouds is Orion [26], the SDN distributed platform
developedbyGoogle.OneofthekeyaspectsofOrionisthewayithandlesdisconnect
events coming from switches. It was observed that a disconnection event seen by the
controllerdoesnotnecessarilymeanadataplanefailure. Thus,thestrategyistopreserve
thecurrentstateforlargerandcorrelatedfailures,buttoaggressivelyrouteifsmalland
uncorrelatedfailuresoccur.
ThemeasurementoftheUserPlaneFunction(UPF)performancesinarealtestbed
environmentispresentedin[27]. Thispaperdemonstratestheadvantagesofdeployingthe
UPFasastandalonecomponentforensuring5Grequirementsratherthaninamonolithic

Sensors2021,21,3773 5of26
4GapproachandusesOpenBatonasanNFVMANOplatformfororchestratingthecore
componentsasVNFs. TheauthorshighlightedthathavingalargenumberofUPFscould
lead to problems related to orchestration and management. Our proposed method can
mitigatethislimitationbydeployingthecorecomponentsasCNFsandorchestratethem
withKubernetes.Kubernetes,amaturecontainerorchestrationsolutionadoptedinmost
cloudplatforms,willensuretheefficientorchestrationofalargenumberofCNFs,while
the use of containers will significantly reduce the overhead previously introduced by
virtualmachines.
NFV platforms have started to develop rapidly with the advances in the field of
5Gtechnology. SomeoftheexistingMANOframeworksareusedfordeployingthe5G
networkfunctions,suchasOSM[28],ONAP[29],OpenBaton[30],orCloudify[31]. How-
ever,newMANOplatformshavealsobeendevelopedinordertomeet5Grequirements.
Many of these MANO platforms dedicated for 5G were developed within the 5G-PPP
initiative[32].OneofthemisSONATA[33], anNFVmicroservice-basedplatform.The
insightsforimplementingSONATAarepresentedin[34].Theauthorsdescribethemain
stepsduringthedevelopmentphaseoftheplatformandalsohowtheDevOpsapproach
improvestheentiredeploymentprocess.Furthermore,atthattime,theypointedoutthe
gap in integrating the networking capabilities of Kubernetes in SONATA. Meanwhile,
solutionsforenablingTelco-gradenetworkmanagementinKubernetesweredeveloped,
includingMultus[35]andDANM[36].AnotherNFVMANOplatformdevelopedwithin
5G-PPPis5TONIC[37]. 5TONICismorelikeanenvironmentbasedonopentechnologies
anddesignedspecificallyforthedevelopmentof5Gtechnologies. Theenvironmentpro-
posedbytheauthorshasalocalsite,wheretherearetwoNFVIsmanagedbyOpenStack
and orchestrated by the OSM and to which external sites can also be connected. Thus,
multipleexternalsitescanbemanagedbyacentralizedMANOplatform,whichenables
theautomateddeploymentofnetworkservices(NSs)acrossthem. In[38],athorough
comparisonbetweenMANOsolutionsdedicatedfor5Gispresented. Theaimoftheau-
thorswastocomparetheSONATAplatformwithOSMandCloudify. Theresultsshowed
thatSONATAoutperformedOSMintermsofscaling-outtimeandCloudifyintermsof
scaling-in time, but the NS instantiation time was longer than for the other two. All in
all,theplatformsrespondedwellandhadnormalbehaviorduringtheexperiments. The
authorsconcludedthatwhileOSMandCloudifyareveryrobustandcanbeusedinawide
varietyofcases,SONATAisabettertoolfor5Gscenarioswhererun-timeservicelevel
agreementcontractsandnetworkslicingareinvolved.
3. ProposedSystemArchitecture
Thispaperrepresentsanextensionofourpreviousworkin[12]andaimstoextend
thepreviousexperimentsandalsoimplementatestbedforevaluatingtheusageofnetwork
slicingacrossdifferentmobileprivateoperators. Ourworkisdividedintotwoexperiments
coveringtheend-to-endsystemfromservicesandapplicationstoconnectivitythrough
mobilenetworksinordertodeliverthedatafromenddevicestotheapplicationsprocessing
thedatafromthosedevices:
• ThefirstexperimentisrelatedtoacontainerizedtelemetryapplicationforIoTdevices.
Weaimtoanalyzeandcomparetheresourceconsumptionofthisapplicationinthree
different deployment scenarios for both cloud and edge: (1) using a balenaCloud
environment,(2)usingAWSEC2instances,and(3)usingtheAWSIoTcloudservice.
Wechosethesecloudenvironmentsbecausetheycanbeusedinawidevarietyof
deploymentscenariosforIoTandM2Msystems. balenaCloudissuitableforbuilding
and deploying containerized applications on remote devices in the edge. In AWS,
weimplementedthesameapplicationtoperformacomparisonintermsofresource
consumptionbetweencloudandedge. Third,AmazonWebServicesIoTisoneofthe
fivemajorsolutionswiththelargestmarketsharealongsideequivalentIoTplatforms
from Microsoft, Cisco, Google, and IBM [39]. Moreover, AWS IoT can be further
integratedwithAWSWavelengthfor5Gdeployments.

Sensors2021,21,3773 6of26
• Thesecondexperimentfocusesonimplementinganend-to-endtestbedinorderto
deliverdifferenttypesoftraffic,withdifferenttrafficrequirementsthroughspecific
networksliceswhennetworkcongestionisdetected. Moreover,theMobilePrivate
Cloud (MPC) network components are deployed as CNFs and orchestrated with
Kubernetes. The motivation for using Kubernetes was to be able to provide high
availability,scalabilitybasedonlatency,andlifecyclemanagementfortheCNFs. This
scenarioaimstoprovethefeasibilityandefficiencyofourproposedalgorithmfor
scalingtheUPFandload-balancingthenetworktraffictotheleast-loadCNF.
Thedivisionofthepaperintotwoexperimentswasmadeinordertofacilitatethe
betterunderstandingofthetopics. Whilethefirstexperimentisrelatedtotheconsumption
of computational resources for an IoT application in different cloud environments, the
second one extends the focus to the entire end-to-end system, from the sensors to the
cloud,andprovidesanovelandoptimalmechanismformanagingIoTnetworkslicesover
4G/5Gnetworks.
3.1. FirstExperiment: MonitoringtheResourceConsumptionofanIoTTelemetryApplicationin
balenaCloud,AmazonWebServices,andAmazonWebServicesIoT
Inthisfirstexperiment, aDHT11sensorthatmeasurestemperatureandhumidity
wasconnectedtoacontainerizedapplicationrunningonDocker. Threedifferentscenarios
weredevisedtobetteranalyzetheresourceconsumptionofthisapplicationwhenusing
cloud-oredge-basedIoTservices. Assuch,theapplicationwashosted: (1)locally,using
balenaCloud, (2) in the AWS cloud using virtual machines, and (3) in the AWS cloud
using the dedicated AWS IoT cloud service. Not only the hardware used but also the
deploymentmethodsvarybetweenthethreescenarios.Forthefirsttwocases,theDHT11
sensorwasconnectedtoanESP32developmentboard.Thegathereddataweresenttoan
SQLdatabaseinAWS.Forthethirdscenario,thesensorwasconnectedtoaRaspberryPi4,
whichforwardedthedatatoanInfluxDBdatabaseontheedgeserver. Inallthreescenarios,
sensor data were displayed using Grafana. Finally, resource consumption monitoring
wasperformedbymeansofCloudWatchandQuickSightfortheAWSdeployments,and
PrometheusandGrafanafortheedgedeployment.
3.1.1. balenaCloud
ThemainstepsforcreatinganddeployingthecontainerizedIoTapplicationusing
balenaarepresentedinFigure1.
Figure1.CreatinganddeployingacontainerizedIoTapplicationusingbalena.
The first step was to create an account on the platform. As a device, we used a
RaspberryPi4with4GBRAM,whichhastheaarch64hardwarearchitecturesupported
bybalenaCloud. Next,weaddedaspecificbalenaentity,whichcontainsboththefleetof
IoTdevicesandthecoderunningonit,asanapplication.Third,wehadtodownloadthe
balenaOSoperatingsystemandflashittoanSDcardusinganopen-sourcecross-platform
tool,calledbalenaEtcher. Connectingthedevicetotheplatformisinitiallydonebymeans
ofaprovisioningkey,whichisdeletedfromthedeviceafterthefirstboot. Fromthenon,
anotheruniquekey,receivedviaVPN,isused. Managingthefleetcanbedoneeithervia

Sensors2021,21,3773 7of26
thedashboardorthededicatedAPIwithbalenaCLIandSDK.Thecoderunningonthe
fleetissenttothebuildservervalidation. Here,Dockerimagesarebuiltaccordingtothe
specifichardwareofthedevicesthathastobespecifiedinDockerfiles.Theseimagesare
thenforwardedtoaprivatecontainerregistryanddownloadedtothereceivingdevice,as
illustratedinFigure2.
Figure2.ProposedarchitectureinbalenaCloud.
ThedatagatheredfromtheDHT11sensorweresenttoanInfluxDBdatabaserunning
onalocalserver,ratherthantheRaspberryPi. Wechosethisapproachnotonlybecause
wewantedtoensurethescalabilityofthesolution(havingaserverallowsthecollectionof
datainacentralizedmanner),butalsobecausewedidnotwanttheaddedworkloadto
interferewithourresourceconsumptionmeasurements. Themetricsregardingresource
utilizationweregatheredbyaPrometheusagentanddisplayedinGrafana.
3.1.2. AmazonWebServices
ThemainstepsforcreatinganddeployingthecontainerizedIoTapplicationinAWS
arepresentedinFigure3.
Figure3.CreatinganddeployingacontainerizedIoTapplicationusingAWS.
Inthisapproach,thefirststepwastoprogramtheESPboardusingtheopen-source
Arduino IDE with the ESP32 add-on. Moreover, it is important to note that in the first
scenarioadedicatedDockerdaemon,balenaEngine,wasavailablebydefault.Inthissecond
scenario however, the Docker daemon needed to be installed. We used two containers
runningontwodifferentEC2instances: onecontainerwasresponsibleforcollectingthe
dataandsendingittothedatabaseusinganApacheserver,whilethesecondcontainerran
Grafana. TheproposedarchitectureinAWSisillustratedinFigure4.

Sensors2021,21,3773 8of26
Figure4.ProposedarchitectureinAmazonWebServices.
Asforthefirstscenario,Grafanawasconfiguredtodisplayboththedatagathered
fromthesensorsandthemetricsrelatedtoresourcemonitoringgatheredbyCloudWatch.
3.1.3. AmazonWebServicesIoT
For a better comparison with the previous two implementations, we decided to
presentthemainstepsfordeployingtheapplicationusingAWSIoT(Figure5). However,
thearchitectureusedisthedefaultoneprovidedbyAWS,describedindetailin[40],and
wasthereforenotincludedhereinforbrevity.
Figure5.CreatinganddeployingacontainerizedIoTapplicationusingAWSIoT.
DatagatheredbythesensorswerecollectedinAWSIoTAnalytics. Theraw,unpro-
cessedmessagesarearchivedintoachannelwhichstoresalldatafromacertainMQTT
topic. TheMQTTprotocolwascreatedespeciallyforlowlatencyandsmall-sizedpackets
characteristicofIoTdevices.Assuch, comparedtothepreviousimplementationusing
HTTP,MQTTcanensurehighdeliveryguaranteesandhashigherthroughputandlower
energyconsumptionandbandwidthusage. Moreover,itissuitableforintermittentconnec-
tions. MessagesfromachannelcanberedirectedbytheIoTCoretoAWSIoTAnalyticsby
meansofuser-definedrules. ThedatasetisimportedintoAWSQuickSightforgraphical
representation. ThemainadvantageofusingAWSIoTisthattheserverlessinfrastructure
ismanagedentirelybyAWSand,assuch,thissolutionrequirestheleasttimeandeffortto
bedeployed.
3.2. SecondExperiment: NetworkSliceScalabilityManagedwithSDNandKubernetesina
PrivateCloudOrchestratedbyOpenStack
Forthesecondscenario,wedevelopedamechanismwhichnotonlyimprovesthe
scalability of our solution, but also optimizes the end-to-end communication in terms
of latency and throughput in a 4G/5G network. When deploying the mobile network

Sensors2021,21,3773 9of26
functionsweoptedforaprivatecloudorchestratedbyOpenStack,duetothefollowing
reasons:(1)balenausesitsownoperatingsystem,balenaOS,whichisanoptimizedoperat-
ingsystemforIoTdevices,thecorenetworkthatweusedrequiredsomeDebian-specific
dependenciestofunctionproperly;(2)evenif,intheory,aprivatecloudismoreexpensive
thanapublicone,theequipmentwealreadyownaresufficientforrunningtheexperiments,
andthusnoadditionalcostwasinvolved;(3)OpenStackwasourchoicefororchestrating
theprivatecloudbecauseitisanopen-sourcesolutionandareferenceasavirtualized
infrastructuremanager(VIM)[17]forNFVMANO.ItisalreadythefirstchoiceasaVIMin
platformssuchasONAPorOSM.
TheproposedarchitectureisillustratedinFigure6.TheRadioAccessNetwork(RAN)
is composed of two eNBs, which serves two different types of traffic: IoT and mobile
broadband.ThebackhaulnetworkisrepresentedbytwoOpenFlowOpenvSwitchswitches
which connect the RAN to the CN. All the traffic is received by the first switch and
forwardedtotheCN,ifthereisnocongestion. Ifcongestionoccurs,thetrafficoriginating
fromtheeNBdesignatedwiththeIoTtrafficwillbeforwardedtothesecondswitch,and
fromtheretotheCN.Thisway,twonetworkslicesareenabledbytheuseofSDN:onefor
IoTtrafficandtheotheroneformobilebroadband. Finally,inthecloud,wedeployedtwo
CNs,eachonerepresentingadifferentmobileoperator. WedeployedEPCcomponentsas
CNFswiththeuseofKubernetes. Usinga3-nodeK8scluster,notonlythescalabilityand
lifecyclemanagementbutalsothehighavailabilityfortheCNFsisensured.
Figure6.Theproposedsystemarchitectureforthesecondscenario.
3.2.1. TestbedDescription
ThetestbedconsistsofNB-IoTdevicesandmobilephonesasUE.WeusedArduino
boardswiththeu-bloxNB-IoTchipset(Figure7),aBittiumToughMobile,andaMotorola
MotoCPlus.ItisworthmentioningthattheoperationmodeforNB-IoTisin-band,which
means that the sensors are using the same radio access network and share the same
spectrumresourcesasthemobileterminals.

Sensors2021,21,3773 10of26
Figure7.ExperimentaltestbedforNB-IoTdevices.(a)Withsixu-bloxNB-IoTchipset.(b)Withone
u-bloxNB-IoTchipset.
ThesedeviceswereconnectedtotwodifferentNokiaFZMcommercialeNBs: one
runningon1.8GHzforNB-IoTandtheotheronerunningon2.6GHzisservingthemobile
phones. TheconfigurationoftheeNBsispresentedinTable2.
Table2.ConfigurationmodeforeNBs.
LTE Duplex ULCarrier DLCarrier Channel Carrier
Scope MACAddress
Band Scheme Frequency Frequency Bandwidth Power
IoT 3 FDD 1720MHz 1815MHz 10MHz 24dBm D6:EF:CD:89:53:0B
MBB 38 TDD 2610MHz 2610MHz 20MHz 24dBm D6:EF:CD:88:EF:E4
Next, the eNBs are connected to an L2 switch, which connects the RAN with the
backhaulnetwork. ThebackhaulconsistsoftwoOvSsinstalledonanUbuntu18server
whichisolatetheIoTtrafficfromtheMBBtrafficwhencongestionoccurs. Theswitches
fromthebackhaularedirectlyconnectedwiththeMobileOperatorPrivateCloud.
TheprivatecloudwasdeployedonthreeHPZ240TowerWorkstations. Inthelogical
architectureinOpenStackoneofthenodesisthecontrollerandtheothertwoarecompute
nodes. On top of Kubernetes, we deployed a three-node Kubernetes cluster where we
deployedtheCNs. Then,wedeployedthepacketcoreontheKubernetescluster. Also,
wedeployedtheHSSseparatelyusinganUbuntu18cloudinstance. TheAMFandthe
SMF were implemented as deployment resources with a single pod, using Multus for
assigningstaticIPaddresses. Evenifwedonotusethereplicationfeatureforthesetwo
deploymentsbecauseofthestaticIPconfiguration,usingadeploymentobjectinsteadofa
standalonepodensureshighavailabilitybycreatingthesamepodcomponentincluster
incaseofanodeorapodfailure. Theentireexperimentaltestbed,whichisconceptually
displayedinFigure6,isillustratedinFigure8: oneoftheNokiaFZMeNBsthatweused
isillustratedin(a),theOvSswitchesusedinthebackhaulareillustratedin(b)andthe
physicalinfrastructureoftheprivatecloudorchestratedbyOpenStackisshownin(c).

Sensors2021,21,3773 11of26
Figure8.E2Eexperimentaltestbed.(a)NokiaFZMeNB.(b)OpenvSwitches.(c)OpenStackprivatecloud.
3.2.2. MigrationtoCloud-NativeNetworkFunctions
Inthispaper,weusedthecommercialCumucore4G/5GpacketcorefortheCN.The
architecture of this packet core is illustrated in Figure 9. Although we used a 4G core
network,becauseoftheCumucorepacketcorearchitecturewewillrefertothecomponents
inthecontrolplaneasAMFandSMFandtotheuserplanecomponentasUPF.Moreover,
theproposedsolutioninthispapercanalsobeusedina5Gcore.
Figure9.CumucorevEPCarchitecture.
The Cumucore vEPC [15] is an optimized solution for private mobile networks,
research testbeds, corporate mobile networks, or small/medium operators. Having a
microservice-basedarchitecture,itfitsperfectlyforcloud-nativedeployments.Theofficial
documentationpresentstheinstallationprocessofthissolutiontoasingleVMwithan
Ubuntu18server.However,thisapproachdoesnotfitourpurposes.Hostingtheentirecore
inasingleVMmakesitimpossibletoscaledifferentcomponentsofthecoreon-demand.
Moreover, a single instance of the EPC represents a single point-of-failure of the entire
system. Evenso,takingadvantageofthemicroservice-basedarchitectureofthissolution,
weseparatedeachcomponentintoadifferentvirtualnetworkfunction. Still,inorderto
havecontrolovertheentirecore,weneedacentralorchestratortoimplementfunctions
suchashighavailability,scalability,lifecyclemanagement,monitoringortroubleshooting
forthecomponents. OnesolutionwouldbetoadoptanNFVMANOplatformsuchas
ONAPorOSMfororchestratingthecorecomponentssuchasVNFs. However,usinga

Sensors2021,21,3773 12of26
differentvirtualmachineforeachcomponentwouldleadtoahigherwasteofresourcesand
ahigheroverheadandwouldalsoincreasethesystemdelaywhencreatingnewinstances.
AdifferentapproachwouldbetoimplementthecomponentsasCNFs,whichseemstobe
moreappropriatesincethecorealreadyhasamicroservicearchitecture. Movingthecore
componentstocontainersmeansloweroverhead,lowerstartuptime,andhigherporta-
bility. Moreover,orchestratingthecontainerswithKuberneteswillensureallthefeatures
mentionedinthepreviousparagraph.SincetheorchestrationofCNFsinmostMANO
platformsalreadyrequiresaKubernetesclusteroverwhichtheseshouldrun,wedecided
touseKubernetesasaMANOplatformandtakeadvantageofitsinnateproperties.
Thecontainerizationofthepacketcoreisnotatrivialtask.Thefirststepwastoidentify
allthedependenciesthateachcomponentneedstobuildtheDockerimages. TheDocker
imagesareusedtocreateDockercontainersandarecreatedbasedonaDockerfileforeach
corecomponent. EachDockerfilerepresentsascriptthatisusedtoprovidetheDocker
daemonwithinformationabouthowtheimageshouldbebuiltincludingthebaseimage,
thedependencies,environmentalvariables,executingstartupcommands,andsoon. Note
thateventhoughthecontainersarerunningonthehostOSandthedefaultuserinside
containersistheroot,itisnotthesamerootasonthehost. Thisisagoodsecurityfeature,
becausetherootuserinsidethecontainerismappedonthehostasanon-rootuser,thus
notbeingabletotakecontroloverthehostcapabilitiesincaseofattackssuchasprivilege
escalation. Moreover,thisinformationisimportantbecause,bydefault,Dockerstartsthe
containerswithalimitedsetofcapabilities. However,theUPFcomponentmustusethe
GPRSTunnelingProtocol(GTP)kernelmoduleonthehosttoestablishtheGTPtunnelwith
theeNBforcarryingtheuserdatatraffic. Consideringtheseaspects,theUPFcontainers
needtoruninprivilegedmode. AsecuritycontextneedstobecreatedforUPFpodsto
addkernelcapabilitiestothem.Thisway,theUPFpodsareabletousetheGTPkernel
moduleonthehost. Thesecuritycontextcanbesetsothatthecontainersinsidethepods
runintheprivilegedmode,inwhichcaseallthehostkernelcapabilitieswillbeavailable
for the container. To manipulate only the network stack on the host and implicitly the
GTPmodule,theNET_ADMINandNET_RAWcapabilitiesmustbesetinsidethesecurity
contextofthepods. Althoughthisaspectraisessomesecurityissues,studyingthemisout
ofthescopeofthispaper.
OrchestratingthecontainerizedcorenetworkwithKubernetesisalsochallenging.
First,theEPCarchitecturerequiresthatallthecomponentsarestateful,andthisimpliesa
seriousscalabilityproblem: theIPaddressesofthepodsarenotknownbythedeveloper,
beingassignedtothepodjustafteritwasscheduled. Consideringthis,anL4oranL7load
balancerisusuallyemployedasasingleendpointforasetofpods. Buthavingmultiple
replicasofMMEcouldlead, forexample, tooneUEbeingservedbyanotherMMEfor
differentrequests. Thesameproblemalsoarisesfortheothercomponents;forexample,if
aGTPtunnelisestablishedbetweentheeNBandtheUPF,buttheUEwillbeforwardedby
theKubernetesloadbalancertoanotherUPFpod,thenthePDNconnectivitywillbelost.
AspointedoutintheRelatedWorksection,theEPCcomponentshadtobemodifiedby
introducingsomedatabasesforstoringtheirstatestoachieveon-demandscalability.
Inthispaper,wewanttoachievescalabilitywithoutmodifyingthecomponents,since
weuseacommercialpacketcore. AlthoughscalingtheAMFstillimplieschangesinthe
component by saving the state of every AMF in a database, we can achieve scalability
fortheUPF.Forthis,weneedtopreservethestatefulbehaviorofthecomponents. Also,
the connection between components by well-defined interfaces (e.g., S5, S11) must be
preserved. As a result, attaching different interfaces to pods must be done, besides the
defaultnetworkprovidingclusterinternaladdressesassignedbyKubernetes. Enabling
multiplecontainernetworkinterfaces(CNI)inKubernetescanbeachievedwithMultus.
Thus,thedefaultCNI(inourcase,Calico)providedbyKubernetesforthepodswillbe
used to maintain the connection with the Kubernetes server, while the other interfaces
assignedbyMultuswillbeusedtointerconnectthepacketcorecomponents(Figure10).

Sensors2021,21,3773 13of26
Figure10.Kubernetesnetworking.
Fortheadditionalcontainernetworkinterface(CNI)enabledbyMultus,weusedthe
Macvlandriver.Thisway,thenodenetworkinterfaceissplitintomultipleIPaddresses
andMACaddressestothepods. AssigningotherinterfacestoEPCpodsisimportantso
thattheyarevisibletotheeNB.
3.2.3. ScalingAlgorithmforUPF
Next,weproposedamethodtoscaletheUPFusingnativeKubernetesmechanisms,
withoutmodifyingthecomponent.TheUPFcomponentwasalsoimplementedasaKuber-
netesdeploymentresourcebut,inordertoenablethereplicationfeature,theIPaddressesof
thesecondinterfacesofthepodswillbeassignedautomaticallyfromapoolofIPaddresses.
This is due to the fact that it is not possible to provide static IP allocation to a Replica
Setresource.
ToscaletheUPFpods,weusedtheHorizontalPodAutoscaler(HPA)resource. The
HPAusesMetricsAPItoprovidethemeasurementsbasedonwhichthescalingwillbedone.
Bydefault,theHPAusesforscalingjustmetricsrelatedtoCPUandMemoryutilization.
However,wewereinterestedinsteadinscalingtheUPFbasedontheincomingbitrateon
theUPFnetworkinterface.Thiscoulddecreasethelatencyduetothequeueingdelaywhen
theincomingbitrateishigherthanthecapacityoftheinterface,byforwardingthetraffic
fromthenewincominguserstoanewUPF.TosendmoremetricstotheHPA,anotherAPI
mustbecreatedinKubernetes. Forthis,wedeployedthev1beta1.external.metrics.k8s.io
APItosendthenumberofbitspersecondreceivedontheUPFpodinterfacetoKubernetes.
WeusedKubeMetricsAdapter[41],anopen-sourceproject,forimplementingthecustom
andexternalmetricAPIs. Then,Prometheuswasdeployedintheexistingcluster,sothat
theHPAcouldcollectthemeasurementsfromthev1beta1.external.metrics.k8s.ioAPIand
dothescalingbasedonPrometheusmetrics.
ToscaletheUPFpods,theHPAwilldetectwhenaspecifiedthresholdsetforthebits
persecondmeasurementisexceeded. TheruleusedbytheKubernetesHPAforthescaling
decisionis
(cid:24) (cid:25)
cM
dR = cR× (1)
dM
wheredRrepresentsthedesirednumberofpods,cRisthecurrentnumberofpods,cMis
themeasuredmetric,anddMisthethresholdspecifiedforthemetric.Theceilfunction
alsoensurestheexistenceofatleastoneUPFpodinthesystem.

Sensors2021,21,3773 14of26
Letusconsider(1)forthescalingupoperation. IfweconsiderNtobethenumberof
currentUPFpodsandthecurrentmeasurementasthemeanmeasuredloadvalueforthe
Ncomponents,then(1)becomes(2)and,aftersimplification,weobtain(3):
|     |     |     | (cid:38) |       | (cid:39) |     |     |     |
| --- | --- | --- | -------- | ----- | -------- | --- | --- | --- |
|     |     |     |          | 1 ×∑N | cM       |     |     |     |
|     |     |     |          |       | i=1 i    |     |     |     |
|     |     | dR  | = N×     | N     |          |     |     | (2) |
dM
|     |     |     |     | (cid:38) | (cid:39) |     |     |     |
| --- | --- | --- | --- | -------- | -------- | --- | --- | --- |
|     |     |     |     | ∑N cM    |          |     |     |     |
|     |     |     | =   | i=1      | i        |     |     |     |
|     |     |     | dR  |          |          |     |     | (3) |
dM
andforeveryrealxandy,thefollowingpropertyforceilfunctionholds:
|     |     |     | (cid:100)x+y(cid:101) | ≤ (cid:100)x(cid:101)+(cid:100)y(cid:101) |     |     |     | (4) |
| --- | --- | --- | --------------------- | ----------------------------------------- | --- | --- | --- | --- |
Thus,(3)becomes
|     | (cid:38) |          | (cid:39) |                   |          |          |          |     |
| --- | -------- | -------- | -------- | ----------------- | -------- | -------- | -------- | --- |
|     | ∑N       |          | (cid:24) | (cid:25) (cid:24) | (cid:25) | (cid:24) | (cid:25) |     |
|     |          | i=1 cM i |          | cM 1              | cM 2     | cM       | N        |     |
| dR  | =        |          | ≤        | +                 | +...+    |          |          | (5) |
|     |          | dM       |          | dM                | dM       |          | dM       |     |
Now,weassumethatthethresholdsetforthedesiredmetricvalueisatleasthalfof
thetotalcapacityofthenetworkinterface,eachUPFhasopenconnectionswithUEs,and
thenewincomingtrafficisonlysenttooneUPFreplicaatatime. Thus,theceilfunction
foreachcomponentisdefinedby(6):

|     |             |          | 0,cM | =0  |     |     |     |     |
| --- | ----------- | -------- | ---- | --- | --- | --- | --- | --- |
|     | (cid:24) cM | (cid:25) |     | k   |     |     |     |     |
k
|     |     | =   | 1,cM | k ∈ (0,dM] |     |     |     | (6) |
| --- | --- | --- | ---- | ---------- | --- | --- | --- | --- |
dM
|     |     |     |  2,cM | ∈ (dM,TotalCapacity) |     |     |     |     |
| --- | --- | --- | ------ | -------------------- | --- | --- | --- | --- |
k
Consequently,basedonthetrafficloadforeachcomponent,thefollowinginequality
isvalidforthedesirednumberofUPFcomponents:

|     |      | N−1,cM |     | =0       |     |     |     |     |
| --- | ---- | ------ | --- | -------- | --- | --- | --- | --- |
|     |      |       |     | k        |     |     |     |     |
|     | dR ≤ | N,cM   |     | ∈ (0,dM] |     |     |     |     |
k
|     |     |  N+1,cM   |       | ∈ (dM,TotalCapacity) |     |     |     |     |
| --- | --- | ---------- | ----- | -------------------- | --- | --- | --- | --- |
|     |     |            |       | k                    |     |     |     | (7) |
|     |     | (cid:40) ∈ | [1,N] |                      |     |     |     |     |
k
|     | where |     | (cid:16) |     |     | (cid:17) |     |     |
| --- | ----- | --- | -------- | --- | --- | -------- | --- | --- |
∈ TotalCapacity
|     |     | dM  |     |     | ,TotalCapacity |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- |
2
GiventhefactthatthenewincomingtrafficissenttothemostrecentlycreatedUPF,
weconsideredtheinequality(7)asanequalityinthefollowingcases:
|     |    | N−1,wherecM |                           | =0  | (cid:54)= |      |     |     |
| --- | --- | ----------- | ------------------------- | --- | --------- | ---- | --- | --- |
|     |    |             |                           | k   | fork      | N    |     |     |
| dR  | =   | N,∀cM       | (cid:54)=0andatleastonecM |     |           | < dM |     | (8) |
|     |     |             | k                         |     |           | k    |     |     |
|     |    | N+1,∀cM     |                           | ≥   |           |      |     |     |
k dM
Thepreviousequationillustrateshowthescalingdecisionmustbemadeinorderto
havetheoptimalnumberofUPFsinthesystem.Thus,thescalingmustbedoneonlywhen
themeasuredmetricisabovethethresholdforallthereplicas. Basedon(8),weproposed
thefollowingscalingalgorithm,illustratedinFigure11.
Weimplementedanentity,namedUPFManager(UPFM),asanorchestratorforUPF
components. UPFMcontinuouslyqueriesmetricsprovidedbyPrometheustomeasurethe
networkload. TheideawastoextendtheexistingHPAscalingcapabilitiesandcustomize
themforourspecificneeds.AthresholdforthenetworkloadoftheUPFwassetandwhen
thisthresholdisexceeded,anotherUPFtowhichnewconnectedUEswillbeforwardedis
created. IfmorethanoneUPFiscreated,usingonlytheHPAcapabilitiescould,insome
cases,leadtohighload. Thisaspectwillbediscussedinmoredetailinthenextsection.

Sensors2021,21,3773 15of26
Figure11.TheproposedscalingalgorithmforUPF.
ForeveryUEandUPF,theirinformationisstoredintheHSSwithaspecificAccess
PointName(APN).Thisway,theUEwillconnecttotheUPFwiththesameAPN.Toensure
uninterruptedcommunicationandavoidareattachmentprocedureoftheUE,whenthe
newUPFiscreated,thisisstoredwiththeAPNofthepreviousUPFwhichisoverloaded.
Consequently,theUEsthatareusingthepreviousUPFwillstillbeusingitforexisting
sessions. AlistwiththeavailableUPFsisalsostoredintheUPFMforthefollowingreason:
whenthecurrentUPFisoverloadedbuttheloadofapreviousUPFisbelowthethreshold,
the UPFM should forward the new incoming traffic to it, thus preserving the current
numberofUPFs. Thenumberofpodsshouldonlybescaledupwhenalloftheexisting
podsfromthelistareoverloaded. Also,ifapodfromthelisthasnomoreconnections,it
mustbedeletedsincenoothertrafficwillbeforwardedtoit.
SincewedonotknowthepreciseIPaddressassignedbyMultustothenewlycreated
UPF,ascriptistriggeredafterthepod’screationwiththeuseofcontainerlifecyclehooks.
ThiswillsenditsIPaddressandthehostnametoUPFMtogetherwithaflag. Aflagisalso
sentwhenaUPFisdeletedtoknowwhichUPFmustberemovedfromthelist. Forthis,
weexposedanAPIontheUPFMtolistenforpodrequeststriggeredbythecreationor
deletionofacontainer.
3.2.4. NetworkSlicingforDifferentTypesofNetworkTraffic
Another aspect that must be considered is separating customer and IoT network
traffic in the backhaul network. The idea of separation is to prevent one type of traffic
frominterferingwiththeother,inthecaseofheavytrafficsituations.Toaccomplishthis,
wecreatenetworkslicesfordifferenttypesoftrafficbasedoncongestionmeasurements,
withtheuseofSDN.Inourscenario(Figure12),thetrafficfrombotheNBsismultiplexed
throughoneL2switchandisthensenttothebackhaulnetwork. WeusedtwoOpenFlow
switchesforthebackhaulnetwork,implementedwiththeuseofOpenvSwitch: ifthere
isnocongestionbetweenbackhaulandMPC,thenthefirstOvSwillbeusedforallthe
networktraffic. However,ifnetworkcongestionisdetected,thentheIoTtrafficissentto
thecloudviathesecondOvS.Inthisway,weareabletocreatedifferentnetworkslices
forseparatingcustomerandIoTtrafficincaseofnetworkcongestion. Formeasuringthe
latency,weusedanactivemeasurementtechniquebetweenOvS1andtheMPC:wesent
ICMPpacketsonceasecondandmeasuredtheRound-TripTime(RTT).Then,weseta
thresholdfortheRTTandwhenthethresholdisexceeded,arulebasedonthesourceMAC

Sensors2021,21,3773 16of26
addressfortheincomingpacketsissetontheOvS1inordertoforwardtheIoTtrafficto
theOvS2andfromtheretothecloud.
Figure12.NetworkSlicingenabledbySDNforIoTandMBBtraffic.
TherearemultiplesolutionsformonitoringnetworkmetricsinanSDNtopology,a
popularonebeing[42], whichenablesaccuratemeasurementsfordelay, packet-lossor
availabletransferrateforlinksandswitches.However,inourscenario,onlytheOvS1
needstobemanagedtoassigndifferentpathsforeverytypeofnetworktraffic. Moreover,
since there is only one path by default between eNBs and MPC, we assumed that the
forwardandbackwardpathswerethesameintermsofcongestionwhenitoccurred. Thus,
theend-to-enddelay(i.e.,latency)wasapproximatedashalfoftheRTT.TheICMPpackets
sent for the delay measurement were captured in OvS 1 with tcpdump, which added
timestampstothem. WhenthesequencenumberofanECHOREQUESTmatchedtheone
ofanECHOREPLY,thedelaywascomputedeverysecondbysubtractingthetimestamps
from these packets. Then we verified whether two consecutive computed delays were
abovethefirstsetthresholdofahysteresis. IfonlythefirstRTTwasabovethethreshold
(andnotthenextone)noactionwasrequired. IfbothRTTsexceededthethreshold,the
OvS1startedtoforwardtheIoTtrafficthroughanotherpathuntiltwoconsecutiveRTTs
fellbelowthesecondthreshold. Thishysteresisisusefultoavoidrouteoscillations. The
forwardingisdonewhenoneoftheabovetwoactionsoccurredbydeletingandaddinga
newpathforthepacketsincominganddestinedfortheMACaddressoftheeNBIoT.All
theoperationsdescribedabovewereperformedbyaPythonscriptwhichinteractedwith
Linuxprocessesforrunningtcpdumpbyopeningapipewiththepopen()method. Next,
theICMPpacketprocessingwasdoneinrealtime,andthecomputedRTTsweresavedina
PythonList. Whenthescriptdetectedcongestion,itinteractedwiththeovs-ofctlprogram
toaddtheflowsintotheOvS1flowtable.
4. ExperimentalResults
In this section, we present the results for the two scenarios discussed in the prev-
iousparagraphs.
4.1. ExperimentalResultsfortheFirstScenario
TwoGrafanadashboardswerecreatedforthebalenaCloudandAWSimplementations:
onewasusedtomonitorthevaluesgatheredbytheIoTsensors,whilethesecondwas

Sensors2021,21,3773 17of26
usedtomonitortheresourceconsumptionofthecontainerizedapplication. Temperature
andhumidityaredisplayedonthefirstdashboard,asillustratedinFigure13.
Figure13.Dashboardcorrespondingtotemperatureandhumidity.
Dependingontheimplementation,resourceconsumptionmonitoringwasperformed
inthecloudorontheRaspberryPi. UsingbalenaCloud,allthecomputationisdoneonthe
edgedevice(RaspberryPi),whileforthetwoAWS-basedimplementationstheESP32is
justagateway,andthecomputationisdoneontheEC2instances. Datarelatedtoresource
consumptioninthefirstscenarioweregatheredviaPrometheusanddisplayedinGrafana,
asillustratedinFigures14and15.
Figure14.ResourceconsumptionofRaspberryPiinbalenaCloud.
Figure15.NetworktrafficfortheRaspberryPiinthebalenaimplementation.
TheapplicationrunningontheRaspberryPiuses1.1%ofthefourCPUcoresand9.7%
ofthe4GBRAMmemory. Bycomparison,theAWSclustercomposedofEC2instances
uses4.45%of1vCPUand2.4%of3GBclusterRAMmemory(1GBperinstance).The
highermemoryconsumptionfortheRaspberryPiisduetothefactthattheAWSinstances
run only strictly necessary services and are highly optimized in this sense. Note that
the Raspberry Pi transmits more data than it receives. This is not unexpected since we
configuredthedeviceasagatewayforcollectingdatafromthesensorsandforwardingit
tobalenaCloud. Theonlytrafficreceivedisthesignalingsentfromthecloudwhichalso
includescommandsfortheremotecontrolofthedevice.
InAWSIoT,dataarerepresentedgraphicallyusingQuickSight. Acountofrecords
bytemperatureisillustratedinFigure16. Asexplainedintheprevioussection,AWSIoT

Sensors2021,21,3773 18of26
CoreusesmessagestocommunicatewiththeIoTdevices.AWSIoTisbasedonserverless
functions;therefore,acomparisonintermsofresourceconsumptioncannotbeperformed
withthefirsttwoscenarios. Instead, thecostisdeterminedbythenumberofrequests.
Severalstatisticsarereadilyavailable,asillustratedinFigure17.
Figure16.NumberofcountsfortemperatureinQuickSight.
Figure17.AWSIoTCoremessagestatistics.
MostofthemessageswereMQTTandoutbound,correspondingtodatapublishing.
However, there were also some HTTP messages used for connecting. Other types of
messageswereusedtoperiodicallychecktheconnectivitywithpingortosubscribetoa
certainchannel.
4.2. ExperimentalResultsfortheSecondScenario
AscanbeseeninFigure12,OvS1isresponsibleforisolatingtrafficincaseofcon-
gestion. Thus, an application was developed in order to program this switch for for-
warding traffic in case of congestion based on eNB MAC addresses. Figures 18 and 19
illustrate the flows before and after the congestion occurs. Note that for the MBB eNB
(D6:EF:CD:88:EF:E6)theflowpathhighlightedinorangeremainsthesame,whileforthe
IoT eNB (D6:EF:CD:89:53:0B) both the input and output ports are modified to assign a
differentsliceandconsequentlyadifferentflowpath,highlightedinblue.
Thus,thetrafficforIoTdevicesservedbytheeNBwithMACaddressD6:EF:CD:89:53:0B
wasisolated. Thecongestionwasdetectedusinganactivemeasurementtechnique,inspect-
ingtheRTTonthelinkbetweenOvS1andthecloud.Thefirstcongestionthresholdwasset
to10msandthesecondoneto5ms. ThedifferenceinRTTbetweentheIoT(blue)andthe
MBB(orange)slicesisillustratedinFigures20and21. Wefirstsentallthetrafficthrough
the same link to highlight the motivation for traffic isolation. The variation of RTT for
bothIoTandMBB,whenusingthesamelink,isillustratedinFigure20a,whileFigure20b
presentsthevariationofRTTwhentheOvSisusingthecongestiondetectionfeature. Itis
importanttomentionthatthevaluesarebasedonmeasurementsbetweenOvS1andthe
UPFsanddonotreflecttheend-to-endlatency. Thisisbecausewewantedtoevaluatethe

Sensors2021,21,3773 19of26
effectofisolatingthetrafficindifferentslicesinthebackhaulnetworkwithSDN.Sincethe
slicesarecreatedinthebackhaul,addingthelatencyfromtheradionetworkwouldnot
leadtoacorrectassessment. Figure21alsoillustratesthetwothresholds,T1setto10ms
andT2setto5ms,whichdefinethehysteresisforthecongestiondetection.
Figure18.FlowtableforOvS1beforenetworkcongestion.
Figure19.FlowtableforOvS1afternetworkcongestion.
Figure20.ComparisoninRTTvariationbetweenIoTandMBBtraffic:(a)whenusingthesamelink;
(b)afterthenetworkcongestiondetectionfeatureisenabled.
ItcanbeobservedthatthereisasignificantdifferencebetweentheRTTvaluesfor
theIoTandMBBtrafficincaseofcongestionwhennetworksliceswerecreated. While
themeanvalueofRTTfortheIoTsliceis3.0456ms,thesamevaluefortheMBBsliceis
18.4673ms. Moreover,asitcanbeseeninFigure12,thenetworktrafficfrombotheNBsis
multiplexedintoaL2switch,whichcouldbeabottleneck. However,whendifferentports
wereusedtoconnectbotheNBstoOvS,theRTTfortheIoTtrafficwasbelow1ms.
Next, we evaluated our proposed scaling algorithm for UPF. For this, we started
congestingtheexistingUPFwithUDPtrafficusingiperfandmeasuredtheend-to-end
throughputdirectlyfromtheUEs,usingtheSpeedtestapplicationforAndroid[43]. We
evaluatedthethroughputofUEsbycongestingtheUPFatdifferentnetworkloadthresh-
olds(0%,10%,30%,40%,50%,70%,and90%). Weobservedinsomecasesthatthedropof

Sensors2021,21,3773 20of26
downlinkthroughputislinearwithnetworkloadincrease,andinothercasesthedecreas-
ingslopebecomessteepafterthe40%threshold. Thesevariationscouldbeintroducedby
radiointerferenceorbytheSpeedtestapplicationweusedforestimatingtheend-to-end
throughput. WeranmultipletestsbetweentheMotorolasmartphoneandtheSpeedtest
application using a UPF with a network load within 10%, and the range for variations
within5Mbps. For10consecutivemeasurements,theresultsvariedbetween30.86and
34.72Mbpswithameanvalueof31.94Mbps. TherangefortheBittiumsmartphonewas
different,i.e.,37.67and41.33Mbps. Thevariationsdonotseemunusual,especiallyforan
end-to-endsystemthatinvolvesradioconnectivity. Nonetheless,uptothethresholdof
40%weobservedathroughputgreaterthan20MbpsonDLand12MbpsonUL,anda
reductionto10MbpsonDLandunder10MbpsonULwhenthethresholdexceeded70%.
Figure22illustratesthescalingdecisionofouralgorithm,usingathresholdof90%. Once
thenetworkloadexceededthisthreshold,anotherUPFwascreatedandusedbythenewly
attachedUE.
Figure21.ComparisoninRTTbetweenIoTandMBBslices.
Figure22.ThroughputvariationforUEwithUPFnetworkloadaffectedbythescalingdecision.

Sensors2021,21,3773 21of26
ThedifferenceinthroughputwhentheMotorolasmartphone(left)isconnectedtothe
previousoverloadedUPFandtheBittiumsmartphone(right)isconnectedtothenewly
createdUPFisillustratedinFigure23a,b. InFigure23a,thepreviousUPFhasalmosta
loadof100%,whileinFigure23bthenetworkloadis70%.
Figure23.ThethroughputdifferencefortheUEsconnectedtodifferentUPFs.(a)TheloadofthepreviousUPFisalmost
100%(leftimage).(b)TheloadofthepreviousUPFisapproximate70%(rightimage).
Intheseexperiments,themobilephoneswereconnectedtotheNB-IoTeNBtoallow
for a visual comparison (Figure 23) in terms of UE throughput achieved by using our
proposedalgorithm.ThereasonwhywedidnotusetheothereNBwasbecausetheBittium
smartphonecannotusethe38LTEbandusedbythateNB.However,thebehaviorandthe
resultsforourscalingalgorithmwouldbethesame;onlythenumericalvaluesatdifferent
thresholdsforthroughputwouldbedifferent. Thedifferenceinthroughputwhenusing
theothereNBcanbeseeninFigure24. Here,theMotorolasmartphonewasusedtoshow
themaximumachievablethroughput(77.3MbpsforDLand12.68MbpsforUL)forour
deploymentinthe38LTEband.
Figure24.ThemaximumthroughputforMotorolaMotoCPlusconnectedtotheMBBeNB.
WealsomeasuredtheUEthroughputforveryhighUPFloadstoevaluateitsbehavior.
TheresultsaredepictedinFigure25:
WeobservedthatthereductionoftheUEthroughputafterthe95%thresholdcanbe
approximatedbyanexponentialdecaylaw,halvedwithincreasingtheloadwith1%,as
describedin(9):
θ(95+x) = θ ×2 −x (9)
0
whereθ(95+x)representstheUEthroughputasafunctionofnetworkloadfornetwork
loadsover95%,θ representstheUEthroughputat95%UPFload,andxrepresents1%of
0
theUPFnetworkload. Aninterestingfactisthatwecanmakeananalogywiththehalf-life

Sensors2021,21,3773 22of26
periodinradioactivedecay,ifweconsider1%ofUPFloadasthehalf-lifeperiod[44]. The
differencebetweenthemeasuredvaluesandtheoreticalvaluesapproximatedby(9)forthe
UEthroughputisillustratedinFigure26aforDLandFigure26bforUL.Althoughthereis
aslightdifferenceinthecaseofafewvalues,itisimportanttonotethatthemeasurements
performedattheseloadsareunstablesinceitisverydifficulttomaintainaconstantvalue
oftheload.
Figure25.TheUEthroughputvariationincaseofhighnetworkloadonUPF.
Figure26.ComparisonofUEthroughputbetweenthemeasuredvalueandthevaluepredictedby(9)incaseofnetwork
loadhigherthan95%.(a)Downlink.(b)Uplink.
Toprovideabetterunderstandingofourmechanism,weillustratethelogmessages
for two different scenarios (see Figures 27 and 28): (1) the UPF load is higher than the
thresholdandbecausethereisjustonepod(orange),anotheroneneedstobecreated(blue);
and(2)eventhoughthecurrentUPFloadishigherthanthethreshold,anewsessioncan
beaccommodatedinanotheractiveUPF.Hence,thereisnoneedtoscaleupthepods.
Figure27.ScalingdecisionincaseofhighloadonUPF.

Sensors2021,21,3773 23of26
Figure28.Load-balancingdecisionincaseofhighloadonUPF.
ThebehaviorofourmechanismwascomparedwiththeusageofthedefaultKuber-
netesHPA.WhileforthefirstscenariopresentedinFigure27thebehaviorwasthesame,a
bigdifferencewasobservedforthesecondscenario. AfterthesecondUPFwascreated,
wecongestedittocomparethedefaultHPAmechanismwiththeonewedeveloped. For
this,wesetupthethresholdto60%oftheUPFcapacity. Themaindisadvantageofthe
defaultHPAisusingthemeanvalueforallthepods,andthiswasillustratedinthenext
threeexperiments.
Forthefirstexperiment,weconsideredthefirstUPFcongestedwith20%network
load above the threshold. In this case, both mechanisms scaled to three replicas when
theHPAdetectedthemeanvalueofthenetworkloadbeingabovethethreshold. Forthe
secondexperiment,wedecreasedthecongestionforthefirstUPFto30%belowtheHPA
thresholdandthenwestartedtocongestthesecondUPF.Inthiscase,ouralgorithmstarted
toforwardthetraffictothefirstUPF(asinFigure28),whilethedefaultHPAwaiteduntil
themeanvalueofthenetworkloadwasexceeded. Forthedefaultmechanismtoscale
up, we needed to congest the second UPF with 30% above the set threshold. Also, the
defaultHPAcreatedanotherpodinthiscase,whileourapproachstartstoload-balancethe
traffictotheoldoneifitscapacitycanserveotherUEs. Finally,inthethirdexperiment,we
decreasedthecongestionforthefirstUPFto50%ofitscapacity. ThedefaultHPAbecomes
unusablesinceourtheoreticalmodelrequiresthatthedesiredmetricafterwhichtheHPA
hastoscalemusthaveavaluebetweenhalfandfulloftheUPFcapacity. Inthiscaseeven
ifwecongestthesecondUPFuptoitsfullcapacity,themeanvaluewillremainat55%and
theHPAwillneverscaleup. TheeffectwasthatthesamecongestedUPFwasusedforthe
incomingUEs,whileforourapproachthesamebehaviorwasobservedasinFigure28.
5. DiscussionsandConclusions
Thispaperextendsourpreviousworkin[12]relatedtotheresourceconsumptionof
containerizedapplicationsforIoTinvariousdeployments. Weproposeanovelmechanism
forscalingnetworkslicesinordertoforwardNB-IoTandMBBtrafficusingtheleast-load
CNFmanagedwithSDNandKubernetes. SinceinourpreviouspaperwefocusedonCPU
andRAMmemoryutilization, inthisworkthenetworkloadanddelaywereanalyzed
inordertooptimizetheconnectivityforboththeIoTandMBBtraffic. Weconsiderthis
a logical follow-up given the enormous amount of information that is estimated to be
providedbyIoTdevicesin5Gnetworksandbeyond.
First,anapplicationwasimplementedfordynamicallyassigningnetworkslicesfor
IoTandMBBtrafficincaseofcongestion. Itwasobservedthatbyusingdifferentslices,we
significantlyreducedtheRTTfortheIoTtrafficincaseoflinkcongestion,from18.4673ms
toalmost3ms.Adisadvantageofourimplementationisthatweusedaswitchtomultiplex
thetrafficfromthetwobasestationsinasinglelink,whichcouldaffecttheend-to-end
delayincasethislinkgetscongested. Totacklethisdrawback,trafficfromeNBsshould
notbemultiplexed,butsentondifferentphysicallinksinstead.
Next,weconsideredimplementinga4G/5GcorenetworkusinganNFVapproach.
Since the majority of NFV MANO platforms are VNF-based, we chose Kubernetes for
a containerized approach. Thus, a commercial 4G/5G packet core was deployed on a
Kubernetesclusterinordertoorchestrateitscomponentsandensurefeaturessuchashigh-
availability,scalability,monitoring,orlifecyclemanagement. WiththisCNFapproach,we
wantedtoscaletheUPFcapacitybyload-balancingtheincomingtrafficthroughmultiple
UPFsusingaleast-loadpolicy. Forthis,weproposedascalingalgorithmandimplemented
anewcomponent,namelyUPFM,whichovercomestheKubernetesHPAlimitationswhen
itcomestoexternalmetrics. OnelimitationthatthedefaultHPAhaswithexternalmetrics

Sensors2021,21,3773 24of26
isthatscalingcanbedonebyevaluatingeitherthecurrentortheaveragevalue. Usingthe
currentvalueleadstoevaluatingonlytheloadofthefirstcreatedpod. Theaveragevalue
couldbeused,buttherearesomesituationsthatcanleadtooverloadingtheUPFwithout
makingthescalingdecision. Theexperimentalresultsforsuchscenarioswerepresentedin
theprevioussectionandprovedtheadvantagesthatouralgorithmbrings.
Ourproposedscalingalgorithmperformsoptimalscaling,thescalingdecisionbeing
madeonlywhenalltheavailableUPFsarealmostoverloaded. Whennoscalingisneeded,
theUPFwiththeleastloadisselectedfromtheavailableonesandtheincomingtraffic
isforwardedtoit.Consideringthepreviouscase, ouralgorithmevaluateswhetherthe
currentUPFexceedsthethreshold,andifso,itwillchecktheloadoftheotherUPFsto
evaluateiftheycanservemoreUEs. Next,theincomingtrafficwilleitherbebalancedto
theleast-loadone,orforwardedtoanewlycreatedUPF.Forwardingisdonebyupdating
theHSSwiththeIPaddressofthechosenUPF.Alimitationofouralgorithmisthatwe
cannotscaledownthecomponentsgiventhecurrentbehavioroftheHPA.Toreducethe
numberofUPFswehavetocheckwhetheranunusedavailableUPFhasactivesessionsor
notandassuchcanbedeleted. TheHPAcannotscaledownastheUPFthatservesactive
sessions,becauseitdoesnotknowhowtoeliminateacertainpod.Asolutionwouldbe
tocreateacustomKubernetesHPAthatmakesthescalingdowndecisionbasedonthe
numberofGTPtunnelswhichcanhelpusdetermineiftherearemoreusersattached. We
havethisideainmindforfurtherimplementation.Theresultsshowedthatouralgorithm
isefficient,makingthescalingdecisionbasedonasetthreshold. Wedemonstratedthat
aftertheloadofthecurrentUPFisexceeded,anotherload-lessUPFiscreatedinorderto
servefurtherconnectionswithamaximumthroughput. Moreover,wedemonstratedthat
ifthescalingisnotnecessary,theloadbalancingisdonetotheleast-loadavailableUPF.
FutureworkwillconsidertheimplementationofacustomHPAKubernetes,which
willaddthescaling-downcapabilitytoouralgorithm. Anotherconsiderationistodesigna
systemfortrafficanomalydetectionbasedonasupervisedlearningmethod,inorderto
identifywhetheraCNFisloadedandneedsscalingup. Basedonitsperformances,this
couldbeavaluableextensionofourcurrentalgorithmandmightevenreplaceitentirely.
AuthorContributions:Conceptualization,R.B.;Software,R.B.andV.S.;Writing—originaldraft,R.B.;
Writing—reviewandediting,R.B.,I.-A.I.,J.C.-R.andV.D.; Supervision,J.C.-R.andV.D.; Project
administration,J.C.-R.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding: ThisworkwassupportedinpartbytheBusinessFinlandundertheproject5GFinnish
OpenRe-searchCollaborationEcosystem(5G-FORCE)andAcademyofFinlandunderProjectNo.
319003.ThisworkhasbeenperformedintheframeworkoftheH2020project5G-SMART,co-funded
bytheEU.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Thedatathatsupportthefindingsofthisstudyareavailablefromthe
correspondingauthor,R.B.,uponreasonablerequest.
Acknowledgments: ThisworkwassupportedinpartbytheBusinessFinlandundertheproject
5GFinnishOpenResearchCollaborationEcosystem(5G-FORCE)andAcademyofFinlandunder
ProjectNo.319003.ThisworkhasbeenperformedintheframeworkoftheH2020project5G-SMART,
co-fundedbytheEU.Theauthorswouldliketoacknowledgethecontributionsoftheircolleagues.
Thisinformationreflectstheconsortium’sview,buttheconsortiumisnotliableforanyusethatmay
bemadeofanyoftheinformationcontainedtherein.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

Sensors2021,21,3773 25of26
References
1. CiscoAnnualInternetReport(2018–2023)WhitePaper.Availableonline:https://www.cisco.com/c/en/us/solutions/collateral/
executive-perspectives/annual-internet-report/white-paper-c11-741490.html(accessedon25March2021).
2. Presad,R.;Rohokale,V.InternetofThings(IoT)andMachinetoMachine(M2M)Communication.InCyberSecurity:TheLifeline
ofInformationandCommunicationTechnology; Prasad,R.,Jackson,O.,Eds.; Springer: Cham,Switzerland,2020; pp. 125–141.
[CrossRef]
3. Marjani,M.;Nasaruddin,F.;Gani,A.;Karim,A.;Hashem,I.A.T.;Siddiqa,A.;Yaqoob,I.BigIoTDataAnalytics:Architecture,
Opportunities,andOpenResearchChallenges.IEEEAccess2017,5,5247–5261.[CrossRef]
4. Xiang,Z.;Gabriel,F.;Urbano,E.;Nguyen,G.T.;Reisslein,M.;Fitzek,F.H.P.ReducingLatencyinVirtualMachines:Enabling
TactileInternetforHuman-MachineCo-Working.IEEEJ.Sel.AreasCommun.2019,37,1098–1116.[CrossRef]
5. Zhang,Q.;Liu,L.;Pu,C.;Dou,Q.;Wu,L.;Zhou,W.AComparativeStudyofContainersandVirtualMachinesinBigData
Environment.InProceedingsoftheIEEE11thInternationalConferenceonCloudComput.(CLOUD),SanFrancisco,CA,USA,
2–7July2018;pp.178–185.[CrossRef]
6. Mekki,K.;Bajic,E.;Chaxel,F.;Meyer,F.AcomparativestudyofLPWANtechnologiesforlarge-scaleIoTdeployment. ICT
Express2019,5,1–7.[CrossRef]
7. ThePathto5G:AsMuchEvolutionasRevolution.Availableonline:https://www.3gpp.org/news-events/1774-5g_wiseharbour
(accessedon26March2021).
8. Chekired,D.A.;Togou,M.A.;Khoukhi,L.;Ksentini,A.5G-Slicing-EnabledScalableSDNCoreNetwork:TowardanUltra-Low
LatencyofAutonomousDrivingService.IEEEJ.Sel.AreasCommun.2019,37,1769–1782.[CrossRef]
9. Yu,H.;Lee,H.;Jeon,H.Whatis5G?Emerging5GMobileServicesandNetworkRequirements. Sustainability2017,9,1848.
[CrossRef]
10. Basta,A.;Blenk,A.;Hoffmann,K.;Morper,H.J.;Hoffmann,M.;Kellerer,W.TowardsaCostOptimalDesignfora5GMobileCore
NetworkBasedonSDNandNFV.IEEETrans.Netw.Serv.Manag.2017,14,1061–1075.[CrossRef]
11. Cloud-NativeNetworkFunctions.Availableonline:https://www.cisco.com/c/en/us/solutions/service-provider/industry/
cable/cloud-native-network-functions.html#~introduction(accessedon26March2021).
12. Botez,R.;Strautiu,V.;Ivanciu,I.-A.;Dobrota,V.ContainerizedApplicationforIoTDevices:ComparisonbetweenbalenaCloud
andAmazonWebServicesApproaches.InProceedingsofthe2020InternationalSymposiumonElectronicsandTelecommunica-
tions(ISETC),Timisoara,Romania,5–6November2020;pp.1–4.[CrossRef]
13. Bouras,C.;Ntarzanos,P.;Papazois,A.CostmodelingforSDN/NFVbasedmobile5Gnetworks. InProceedingsofthe8th
InternationalCongressonUltra-ModernTelecommunicationsandControlSystemsandWorkshops(ICUMT),Lisbon,Portugal,
18–20October2016;pp.56–61.[CrossRef]
14. EnablingNextGenerationMobileNetworks.Availableonline:https://cumucore.com/#products(accessedon27March2021).
15. Evolve Your Core Network for 5G. Available online: https://www.ericsson.com/en/core-network/5g-core (accessed on
27March2021).
16. 5G Core (5GC). Available online: https://www.nokia.com/networks/portfolio/5g-core/#5g-core-solution (accessed on
27March2021).
17. Taleb,T.;Corici,M.;Parada,C.;Jamakovic,A.;Ruffino,S.;Karagiannis,G.;Magedanz,T.EASE:EPCasaservicetoeasemobile
corenetworkdeploymentovercloud.IEEENetw.2015,78–88.[CrossRef]
18. Amogh,P.C.; Veeramachaneni,G.; Rangisetti,A.K.; Tamma,B.R.; Franklin,A.A.Acloudnativesolutionfordynamicauto
scalingofMMEinLTE.InProceedingsoftheIEEE28thAnnualInternationalSymposiumonPersonalIndoor,andMobileRadio
Communications(PIMRC),Montreal,QC,Canada,8–13October2017;pp.1–7.[CrossRef]
19. Banerjee,A.;Mahindra,R.;Sundaresan,K.;Kasera,S.;VanderMerwe,K.;Rangarajan,S.ScalingtheLTEcontrol-planeforfuture
mobileaccess.InProceedingsofthe11thACMConferenceonEmergingNetworkingExperimentsandTechnologies,Heidelberg,
Germany,1–4December2015;pp.1–13.[CrossRef]
20. Alawe,I.;Hadjadj-Aoul,Y.;Ksentini,A.;Bertin,P.;Darche,D.Onthescalabilityof5Gcorenetwork:TheAMFcase.InProceedings
ofthe15thIEEEAnnualConsumerCommunications&NetworkingConference(CCNC),LasVegas,NV,USA,12–15January
2018;pp.1–6.[CrossRef]
21. Hefele,A.;Costa-Requena,J.SDNmanagedNetworkSlicinginMobileBackhaul.InProceedingsoftheInternationalConference
onElectronicsInformation,andCommunication(ICEIC),Barcelona,Spain,19–22January2020;pp.1–8.[CrossRef]
22. Adem,A.;Costa-Requena,J.;Kantola,R.SDNNetworkSlicingforURLLCNB-IOT.InProceedingsoftheInternationalConference
onElectronicsInformation,andCommunication(ICEIC),Barcelona,Spain,19–22January2020;pp.1–7.[CrossRef]
23. Yang, G.; Yu, B.-y.; Jin, H.; Yoo, C.LiberaforProgrammableNetworkVirtualization. IEEECommun. Mag. 2020, 58, 38–44.
[CrossRef]
24. OpenvSwitch.Availableonline:https://docs.openvswitch.org/en/latest(accessedon20April2021).
25. Firestone,D.VFP:AVirtualSwitchPlatformforHostSDNinthePublicCloud.InProceedingsofthe14thUSENIXSymposium
onNetworkedSystemsDesignandImplementation,Boston,MA,USA,27–29March2017;pp.315–328.
26. Ferguson,A.D.;Gribble,S.;Hong,C.Y.;Killian,C.;Mohsin,W.;Muehe,H.;Ong,J.;Poutievski,L.;Singh,A.;Vicisano,L.;etal.
Orion:Google’sSoftware-DefinedNetworkingControlPlane.InProceedingsofthe18thUSENIXSymposiumonNetworked
SystemsDesignandImplementationVirtualConference,Boston,MA,USA,12–14April2021;pp.83–98.

Sensors2021,21,3773 26of26
27. Costa-Requena,J.;Poutanen,A.;Vural,S.;Kamel,G.;Clark,C.;Roy,S.K.SDN-BasedUPFforMobileBackhaulNetworkSlicing.
InProceedingsofthe2018EuropeanConferenceonNetworksandCommunications(EuCNC),Ljubljana,Slovenia,18–21June
2018;pp.48–53.[CrossRef]
28. OpenSourceMANO.Availableonline:https://osm.etsi.org(accessedon20April2021).
29. OpenNetworkAutomationPlatform.Availableonline:https://www.onap.org(accessedon20April2021).
30. OPENBATON.Availableonline:https://openbaton.github.io(accessedon20April2021).
31. Cloudify.Availableonline:https://cloudify.co/technologies/(accessedon20April2021).
32. The5GInfrastructurePublicPrivatePartnership.Availableonline:https://5g-ppp.eu(accessedon20May2021).
33. SONATA.Availableonline:https://5g-ppp.eu/sonata/(accessedon20May2021).
34. Soenen,T.;VanRossem,S.;Tavernier,W.;Vicens,F.;Valocchi,D.;Trakadas,P.;Karkazis,P.;Xilouris,G.;Eardley,P.;Kolometsos,S.;etal.
InsightsfromSONATA:ImplementingandIntegratingaMicroservice-basedNFVServicePlatformwithaDevOpsMethodology.
InProceedingsoftheNOMS2018-2018IEEE/IFIPNetworkOperationsandManagementSymposium,Taipei,Taiwan,23–27
April2018;pp.1–6.[CrossRef]
35. Multus-CNI.Availableonline:https://github.com/k8snetworkplumbingwg/multus-cni(accessedon21May2021).
36. DANM.Availableonline:https://github.com/nokia/danm(accessedon21May2021).
37. Nogales,B.;Vidal,I.;Lopez,D.R.;Rodriguez,J.;Garcia-Reinoso,J.;Azcorra,A.DesignandDeploymentofanOpenManagement
andOrchestrationPlatformforMulti-SiteNFVExperimentation.IEEECommun.Mag.2019,57,20–27.[CrossRef]
38. Trakadas,P.;Karkazis,P.;Leligou,H.C.;Zahariadis,T.;Vicens,F.;Zurita,A.;Alemany,P.;Soenen,T.;Parada,C.;Bonnet,J.;etal.
ComparisonofManagementandOrchestrationSolutionsforthe5GEra.J.Sens.ActuatorNetw.2020,9,4.[CrossRef]
39. MakingSenseofIoTPlatforms:AWSvs.Azurevs.Googlevs.IBMvs.Cisco.Availableonline:https://www.altexsoft.com/
blog/iot-platforms/(accessedon22May2021).
40. AWSDocumentation.Availableonline:https://docs.aws.amazon.com(accessedon19April2021).
41. KubeMetricsAdapter.Availableonline:https://github.com/zalando-incubator/kube-metrics-adapter(accessedon22May2021).
42. VanAdrichem,N.L.M.;Doerr,C.;Kuipers,F.A.OpenNetMon:NetworkmonitoringinOpenFlowSoftware-DefinedNetworks.
InProceedingsofthe2014IEEENetworkOperationsandManagementSymposium(NOMS),Krakow,Poland,5–9May2014;
pp.1–8.[CrossRef]
43. Speedtest.Availableonline:https://www.speedtest.net(accessedon20April2021).
44. Rutherford,E.Aradio-activesubstanceemittedfromthoriumcompounds.Lond.Edinb.DublinPhilos.Mag.J.Sci.1900,49,1–14.
[CrossRef]