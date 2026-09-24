# AIEnabled-Traffic-Control-Prioritization-in-SoftwareDefined-IoT-Networks-for-Smart-Agriculture

> Source file: `AIEnabled-Traffic-Control-Prioritization-in-SoftwareDefined-IoT-Networks-for-Smart-Agriculture.pdf`

---

sensors
Article
AI-Enabled Traffic Control Prioritization in Software-Defined
IoT Networks for Smart Agriculture
FahadMasood1,2,∗,WajidUllahKhan2,SanaUllahJan3 andJawadAhmad3
1 DepartmentofElectronics,QuaidiAzamUniversity,Islamabad45320,Pakistan
2 DepartmentofComputing,AbasynUniversity,Peshawar25000,Pakistan;arbabwajid.ullah@abasyn.edu.pk
3 SchoolofComputing,EngineeringandtheBuiltEnvironment,EdinburghNapierUniversity,
EdinburghEH105DT,UK;s.jan@napier.ac.uk(S.U.J.);j.ahmad@napier.ac.uk(J.A.)
* Correspondence:fahad.masood@abasyn.edu.pk
Abstract: Smartagriculturalsystemshavereceivedagreatdealofinterestinrecentyearsbecause
oftheirpotentialforimprovingtheefficiencyandproductivityoffarmingpractices.Thesesystems
gatherandanalyzeenvironmentaldatasuchastemperature,soilmoisture,humidity,etc.,using
sensor networks and Internet of Things (IoT) devices. This information can then be utilized to
improvecropgrowth,identifyplantillnesses,andminimizewaterusage.However,dealingwithdata
complexityanddynamismcanbedifficultwhenusingtraditionalprocessingmethods.Asasolution
tothis,weofferanovelframeworkthatcombinesMachineLearning(ML)withaReinforcement
Learning(RL)algorithmtooptimizetrafficroutinginsideSoftware-DefinedNetworks(SDN)through
trafficclassifications.MLmodelssuchasLogisticRegression(LR),RandomForest(RF),k-nearest
Neighbours(KNN),SupportVectorMachines(SVM),NaiveBayes(NB),andDecisionTrees(DT)
areusedtocategorizedatatrafficintoemergency,normal,andon-demand. Thebasicversionof
RL,i.e.,theQ-learning(QL)algorithm,isutilizedalongsidetheSDNparadigmtooptimizerouting
basedontrafficclasses.ItisworthmentioningthatRFandDToutperformtheotherMLmodelsin
termsofaccuracy. Ourresultsillustratetheimportanceofthesuggestedtechniqueinoptimizing
trafficroutinginSDNenvironments.IntegratingML-baseddataclassificationwiththeQLmethod
improvesresourceallocation,reduceslatency,andimprovesthedeliveryofemergencytraffic.The
Citation:Masood,F.;Khan,W.U.; versatilityofSDNfacilitatestheadaptionofroutingalgorithmsdependingonreal-timechangesin
Jan,S.U.;Ahmad,J. AI-Enabled networkcircumstancesandtrafficcharacteristics.
TrafficControlPrioritizationin
Software-DefinedIoTNetworksfor Keywords:SDN;IoT;emergency/criticaldata;smartagriculturesystem;machinelearning;reinforcement
SmartAgriculture.Sensors2023,23, learning
8218. https://doi.org/10.3390/
s23198218
AcademicEditor:Wonsuk
1. Introduction
(Daniel)Lee
Software-defined networks (SDNs) have evolved as potential tools for managing
Received:14August2023
andcontrollingmodernnetworkinfrastructures[1]. TheabilityofSDNstoseparatethe
Revised:29September2023
controlanddatalayersallowsforflexiblenetworksetups,effectiveresourcemanagement,
Accepted:30September2023
and granular traffic control, as shown in Figure 1. SDNs have found use in a number
Published:2October2023
ofindustries,includingtransportation,healthcare,smartcities,andagriculture. Modern
communicationnetworkshaveundergonesubstantialchangesduetotheriseofSoftware-
DefinedNetworking(SDN).Theadministrationofnetworkresourcesisprogrammable,
Copyright: © 2023 by the authors. dynamic,andextensiblethankstoSDNs’isolatingofthecontrolplanefromthedataplane.
Licensee MDPI, Basel, Switzerland. Thismakesitpossibletocreateintelligentandflexiblenetworksystemsforvarioususes,
This article is an open access article includingintheagriculturalsector[2,3].
distributed under the terms and Agricultureisoneofthemostimportantareasoftheglobaleconomy;witharising
conditionsoftheCreativeCommons populationcomesaninevitableincreaseinfoodconsumption. Smartagriculture,which
Attribution(CCBY)license(https://
combinescutting-edgetechnologieswithtraditionalfarmingmethods,hastheabilityto
creativecommons.org/licenses/by/
transformhowwecreatefoodandhandleagriculturalresources[4–9].SDN-basedsolutions
4.0/).
Sensors2023,23,8218.https://doi.org/10.3390/s23198218 https://www.mdpi.com/journal/sensors

Sensors2023,23,8218 2of17
canpromotesmartagriculturebyofferingadynamicandclevernetworkarchitecturein
supportofabroadvarietyofapplications,suchasprecisionagriculture,weathertracking,
and livestock management [10]. In modern agriculture, sensors play a critical role in
collectinginformationaboutvariousfactorssuchaswater,soil,climate,etc.,asshownin
Figure2. Analysiscanbecarriedoutwiththehelpofdataobtainedfromdifferentsensors
to identify and improve the current situation of crop production [11]. The progressive
variabilityofacquiredmeasurementsisanessentialaspectoftheagriculturaldomainthat
requiressignificantattention. Thescaleofagriculturalproductionandindustrialweakness
canbesignificantlychangedthroughmodernagriculture. Moreover,ithasanimperative
roleinagriculturedevelopment,aswellasintherealizationofahealthysociety[12].
Figure1.SDNarchitecture.
Traditionaldataprocessingtechniquesinsmartagriculturalsystemsfacenumerous
severe hurdles when dealing with the complexities of data management. The massive
amounts of data created by sensors and devices can overwhelm traditional workflows,
resultinginslowanalysisanddecision-makingprocesses. Thisisworsenedbythewide
rangeofdatatypes,whichnecessitatespecializedprocessingcapabilities. Theimportance
ofreal-timemonitoringheightenstherequirementofquickdatahandling,whichtraditional
systemsfailtosatisfy[13–16]. Inthiscontext,datacanbemanagedandanalyzedwiththe
helpofevent-baseddataanalysismethods. Event-baseddataanalysiscanassistinlocating
patterns,trends,andanomaliesinthedatathatcanthenbeusedtoenhanceagricultural
decision-makingbyidentifyingandanalyzingeventsinrealtime. Thankstoitsabilityto
autonomouslyidentifytrendsandcorrelationsinmassivedatasets,machinelearning(ML)
isapotentinstrumentforevent-baseddataanalysis. Real-timetrackingofagricultural
circumstancesismadepossiblebytheuseofsoftware-definednetworksandML,offering
usefulinformationforimproveddecision-making.
Inthisarticle,wesuggestanevent-basedtrafficcontrolprioritizationframeworkfor
smartagriculturethatmakesuseofMLtechniques. Theoptimizedtrafficroutingbegins
withthecategorizationofincomingdatausingvariousMLtechniques,suchasLogisticRe-
gression(LR),RandomForest(RF),k-nearestNeighbours(KNN),SupportVectorMachine
(SVM),NaiveBayes(NB),andDecisionTree(DT).Thesealgorithmsanalyzecharacteristics
suchasashumidity,temperature,windspeed,leafmoisture,soiltemperature,andsoil

Sensors2023,23,8218 3of17
moisturetoclassifydatatrafficintoemergency,normal,andon-demandcategories. Fol-
lowingclassification,Q-learning,afundamentalreinforcementlearning(RL)algorithm,
managesdynamicroutingintheSDNconfiguration. SDNallowsthesystemtodynami-
callyhandlenetworktrafficandresourcesbasedontherequirementsoftheapplication.
TheSDNdesignenablesacentralizedcontrollayerthatmakesnetworkmanagementand
configurationsimpler. ItkeepsaQ-tablewiththeprojectedcumulativerewardforcertain
actionsinspecificdataclassconditions.QLconvergestooptimalQ-valuesthroughresearch
andapplication,suggestingtheappropriateactionsforeachdataclass. TheSDNcontroller
examinestheQ-tableduringtrafficroutingtomakedecisionsaccordingtotheprevious
routingperformanceoftherelevantdataclass. Thisintegratedsystemmodifiesrouting
pathwaysbasedondatatraffictype,ensuringeffectiveandfastdecisionsregardingrouting
in the SDN environment. The combination of ML’s categorization expertise with QL’s
flexibledecision-makingresultsinaversatilesystemthatoptimizesdataroutingwhile
allowingforreal-timeadaptation.
Theuseofevent-basedtrafficanalysisservestoreducedataduplicationandimprove
dataprocessingefficiency,whileMLalgorithmshelptocategorizethedataintovarious
groups,suchasnormaloremergencyconditions. TheproposedtechniqueemploysQL
todynamicallyalterroutingdecisionsinaccordancewithreal-timedataclassesandpast
performance. Thisadvancementenablesoptimalresourceutilizationandreducedlatency.
Furthermore,theuseofML-baseddatacategorizationenablesclass-basedrouting,which
improves network intelligence and customizes routing decisions. The innovative com-
ponentistheinteractionofMLclassificationwithQLadaptiverouting. Thistechnique
providesreal-timeoptimization,comprehensivetrafficmanagement,andempiricalconfir-
mationinasimulatedenvironmentbyovercomingthegapbetweenefficientcategorization
anddynamicrouting. Theimplementationofthisresearchinsmartagriculturehasthe
potentialtoincreaseagriculturalyields,cutwateruse,andimproveresourcemanagement.
Moreover,theexecutionofthesystemismadeflexibleandscalablethroughtheuseofa
software-definedIoTnetwork.
The rest of this paper is organized as follows: Section 2 offers a comprehensive
overviewofrelatedworkinthefieldsofSDN-basedsmartagricultureandevent-based
trafficanalysis;Section3coversthesuggestedmethodologyindepth,includingthedataset
usedforexperimentation;Section4containsthetestingresults,alongwithacomparison
ofthevariousMLmethodsused; finally,Section5concludesthepaperbyhighlighting
upcomingresearchpaths.
Figure2.TraditionalIoTschemeforsmartagriculture.
2. LiteratureReview
ML methods are increasingly being used nowadays. These methods are thought
tobesuperiortoconventionalalgorithms,especiallywhenhandlingandanalyzingbig
data. Researchersarefocusingontheapplicationofsuchtechniquesinthefieldofnet-
works. MLhasfoundvariedusesintheareaofSDN,includingtrafficengineering[17,18],
resourcemanagement[19,20],intrusiondetectionsystems[21,22],andothersecurityob-
jectives[23,24]. Inthisregard,Akyildizetal.[25]presentedthestateoftheartfortraffic

Sensors2023,23,8218 4of17
engineeringinSDN/OpenFlownetworks. Mijumbietal.[26]usedMLtoadjustvirtual
networksandcontrolresourcesinvirtualizednetworksusingacontrolplane. Asaresult,
the significance of ML in SDN has increased of late due to its numerous applications.
SDN’sarchitecturalreasoningworksbetterwithMLalgorithmsthanwithconventional
algorithms. Inparticular,numerousresearchfindingshaveusedSDNandMLmethods
incombinationtooptimizerouting. Furthermore,MLisconsideredacrucialtechnology
developmentfor6Gandbeyond[27].
Etenguetal. thoroughlyevaluatedAI-assistednetworksforloadbalancingandgreen
routing. Theiranalysiscenteredonapragmaticstrategy,hybridSDN,whichistypically
utilized for smooth migration from legacy systems [28]. A collection of challenges and
prospectiveresearchpathswerediscussedandaparticularframeworkforhandlingthem
was proposed. Qian et al. provided a succinct overview of a variety of use cases in
communicationnetworksthatrelyonreinforcementlearning,suchasnetworkcachingand
tasksharing[29],althoughtheirreviewbarelymentionedtheconnectionbetweenrouting
appsandSDN.Mammerietal. thoroughlyexaminedreinforcementlearningapproaches
forroutingforSDN-basednetworksaswellasforotherkindsofnetworks,providingavery
excellentoverviewoftheevolutionofthisparticularMLtechniqueanditsimplementation
incommunicationnetworks[30].
Jamshidietal. classifiedML-basedappsintosixnetworkingcategories: networksecu-
rity,trafficprediction,cloudservices,domainnamesystem,applicationidentity,andQoS.
TheythenselectedthebestMLalgorithmsandrawdatasetsforeachofthesegroups[31].
ThisapproachhighlightsthekeyproblemsandoutcomesoftheserawdataandMLtech-
niques. Zhang et al. showed various uses of ML in resource allocation and routing in
optical networks, though with no particular emphasis on SDN-enabled networks [32].
Boutabaetal. surveyedMLresearchpossibilitiesandevolutionintheareaofnetwork-
ing[33],providingashortsummaryofMLtechniquesinrouting,anomalydetection,traffic
categorization, fault management, QoS/QoE, and intruder detection. The engineering
techniques,approaches,andmethodsfordatacollectioninnetworktrafficwerediscussed
aswell,andtheyemphasizedthevalueofonlinelearning,safelearningassistance,andsys-
temarchitecturesthatmakeitsimpletouseML.Xieetal. providedathoroughdescription
of ML techniques and of the design and operation of SDNs [34] in terms of QoE/QoS,
optimization,resourcemanagement,security,andtrafficcategorization,variousMLalgo-
rithmtypes. Zhaoetal. reviewedthevariousnetworkingapplicationsthatprofitfromthe
integrationofSDNandML,includingabriefdiscussionofroutingoptimization[35].
Tamizhselvan and Vijayalakshmi discussed an SDN-based solution named “SDN-
MCHO”designedtoimprovereliabledeviceroutinginIoTcontexts,especiallyforsmart
surveillanceapplications[36]. TheirkeyfocuswasonleveragingSoftware-DefinedNet-
working (SDN) to optimize routing decisions in IoT networks. Sharma et al. provided
amethodcalled“FCS-fuzzynet”thathandlesCHselectionaswellasroutingforweed
categorizationinIoTcontexts[37]. Theirstudyemphasizedtheuseoffuzzylogic, and
reliedonaframeworkknownasMapReduceforeffectivedataprocessingandroutingin
IoTnetworks. Fuzzylogicwasusedtoimprovethedecision-makingprocessforpicking
clusterheads,whichplayanimportantroleinorganizingdataroutinginIoTsystems,with
aspecificapplicationfocusonweedcategorization. Naeemetal. usedSDNtoprovide
a unique solution to energy-efficient routing optimization in the Industrial Internet of
Things(IIoT)[38]. TheirmajorgoalwastoimproveenergyefficiencyinIIoTnetworksby
optimizingroutingdecisionsusingSDNcapabilities. Inlightofthevitalroleofenergy
managementinIIoT,theirstudyisparticularlypertinentwithrespecttoindustrialappli-
cations,whereeffectiveroutingcanresultinconsiderableenergysavingsandenhanced
networkefficiency.
3. MaterialsandMethods
We consider the band communication model with the SDN controller having re-
activeflowinstallationmodeandopenflowenablingtheswitch, asshowninFigure3.

Sensors2023,23,8218 5of17
Theemploymentofacontrollerinthisstudy,particularlyinthecontextofSoftware-Defined
Networking(SDN),providesnumerousmajoradvantages.Firstofall,itcentralizesnetwork
administration,effectivedecision-making,andallocationofresources. Second,thecon-
trollerallowsfordynamicroutingadaptionbasedondataclassification,guaranteeingthat
datapacketsareroutedappropriatelydependingontheirpriorityandfeatures. Thenet-
work’sflexibilityimprovesitsefficiencyandresponsiveness. Furthermore,thecontroller
optimizesresourceallocation,resultinginbetterresourceutilizationandlowercongestion,
andplaysanimportantroleinreducinglatencyforvitaldatatypesandimprovingdata
deliverydependability. Theproposedapproachcontainsprocesseswithanultimategoal
of assisting the agricultural sector through a merged SDN paradigm and AI modeling
for normal, emergency, and data on demand operation. The first step is to collect data
fromfieldsensorsforvariousfeatures. Dataacquiredfromthesensorsarepreprocessed
beforebeingsenttotheMLClassificationLayer. Aftercollection,thedatamustbecleaned
andtransformedintoaformatappropriateformachinelearningmodels. Afterprepro-
cessing,thedataaredividedintotrainingandtestingsets. Thetrainingsetisthenused
totrainanMLmodel. Themodelisfinallytestedonthetestingdatasettoevaluatethe
accuracy. Aftertrainingandtesting,themodelmaybeusedtocategorizetrafficasnormal,
emergency, or data on demand. The categorized data traffic is then passed to the SDN
control layer, where the controller uses the Q-learning algorithm to dynamically route
trafficflowdependingonthedataclassifications. TheQ-learningalgorithmadaptstothe
present state of the network and performs actions to optimize a reward signal, such as
prioritization,efficientrouting,andbandwidthallocation. TheQ-valuesaremodifiedde-
pendingonlearnedrewards,andtheSDNcontrolleralterstrafficflowcontrolmechanisms
appropriately. Thedetailedworkflowprocessisdiscussedbelow.
Figure3.Systemarchitecture.
3.1. DataCollection
AnetworkofsensorsstrategicallypositionedinthecityofPeshawar,Pakistanwas
usedtocollectdata. Thesesensorsweremeticulouslyplacedtoaccountforavarietyofde-
terminingfactors,suchasparticularcroprequirements,varyingenvironmentalconditions,
andtheoptimumrangeofeachsensortype. Toavoidinterference,thesensorswereequally

Sensors2023,23,8218 6of17
spaced,andwereplacedinaccordancewiththespecificdatarequirements. Locationsfor
sensorswerechosenbasedontheiraccessibilitytoinstallationsitesandtheircosteffective-
ness. Dataforsixdifferentcroptypes(wheat,mint,coriander,radish,turnip,andcarrot)
werecollectedoverafour-monthperiodfrommid-October2022tomid-February2023.
Thechosencropsexhibitavarietyofpreferenceswithrespecttoclimaticconditions,soil
properties,andothervariations. Wheatgrowsbestinloamysoilsthatarewell-drained
andmoderate. Ontheotherhand,mintandcorianderprefersomewhatwarmerandmore
humidsettings,necessitatingwell-drainedsoilsrichincompost. Rootvegetables,including
turnip,carrot,andradish,aretoleranttoawiderangeofclimateconditionsandsoiltypes,
generallypreferringlooseandwell-drainedsoils.
Forfulldatacoverage,atotaloftwenty-fivesensorsweredeployedwithinarangeof
1000–3000movertheagriculturalregiontomeasurehumidity,temperature,windspeed,
leafmoisture,soiltemperature,andsoilmoisture. Thesensorswereplacedforcompre-
hensiveenvironmentaldatagatheringwhileconsideringthefield’ssizeandtheresearch
objectives. Threesensorswerepositionedfortemperatureandhumiditymonitoring: one
dedicatedtowheat,anothertomintandcoriandercollectively,andathirdtocarrot,radish,
andturnipcollectively. Similarcombinationswereemployedfortheleafmoistureand
windspeedsensors. Eachofthesesensorgroupswastailoredtothespecificrequirements
ofthecropswithintheircollectivecategory. Forcriticalfactorssuchassoilmoistureand
soiltemperature,additionalsensorswerededicated: sixtosoiltemperatureandsevenfor
soilmoistureforeachcrop,withtwosensorsoutoftheselattersevendedicatedtowheat
duetothelargercroparea.
The specialized sensors were carefully selected to guarantee precise and complete
monitoring of critical environmental parameters: capacitive humidity sensors (DHT22,
TZT,China)forhumiditylevelsintheair,resistancetemperaturedetectors(RTDPT100,
MKYD, China) for temperature measurement, anemometers (UT363BT, UNI T, China)
for measuring wind speed and providing information about weather conditions, leaf
wetness sensors (LWS-31, LIYUAN, China) for monitoring the leaf moisture, thermo-
couples (MAX6675, Thermocouple Module + K type Sensor, TZT, China) to measure
soil temperature, and volumetric soil moisture sensors (Smart Electronics Soil Mois-
ture Hygrometer Detection Humidity Sensor, STLXY, China) for the soil moisture con-
tent. ThesensorswereconnectedtoanArduinomicrocontroller(UNO-R3,TZT,China)
for data collection, and the data collected by the sensors was transmitted via Wi-Fi
to a central hub for further processing. The data were then preprocessed to remove
any unusual or unnecessary data before being translated into a suitable format for the
machine-learning models. The preprocessed data were divided into training and test-
ingsetsinordertotrainandassesstheperformanceofseveraldifferentmachinelearn-
ing models. The data used in this research can be accessed at the following repository:
https://github.com/researchcsaup/IoTs.git(accessedon5August2023).
3.2. MLModels
MLisaprominentapplicationforartificialintelligence,asitautomatesthesystem
andenablesittolearnanddevelop. TheMLlearningprocessbeginswiththeobservation
ofdatathroughcasesorobservations. Thesedatacontainpatternsthat,whenfound,can
supportmoreaccuratepredictions. Usingthetestdataset,thesixalternativeMLmodels
discussedbelowwereemployedtotraintheclassifiers,thentheirclassificationperformance
wasassessed.
3.2.1. LogisticRegression
Logisticregressionisabinaryclassificationmethodthatemploysalogisticfunctionto
describethelikelihoodofabinaryresponsevariable[39]. Thelogisticfunctiononwhich
thealgorithmisbuiltconvertsanyinputtoanumberbetween0and1. Thisapproachis
employedtoestimatethelikelihoodofaspecificoccurrence.

Sensors2023,23,8218 7of17
3.2.2. DecisionTrees
Decisiontreesareaformofsupervisedlearningalgorithmcommonlyusedforclassifi-
cationissues[40]. Theyutilizeamodelofchoicesandpotentialoutcomesthatresemblesa
tree. Decisiontreesoperatebyrecursivelydividingthedataintosmallergroups,which
theydobyselectingthefeaturethatbestdividesthedataaccordingtocertainparameters,
suchastheinformationgainortheGiniindex.
3.2.3. RandomForest
Randomforestsareanexpansionofdecisiontreesfoundedontheconceptofgener-
atingnumerousdecisiontrees,eachwitharandomportionofthedata,thencombining
theirfindingstoenhanceoverallperformance[41]. Randomforestsarefrequentlyused
forcategorizationissues,especiallywhenworkingwithhigher-dimensionaldata.
3.2.4. NaiveBayes
NaiveBayesisaclassofprobabilisticalgorithmthatusesBayes’theoremtoforecast
thelikelihoodofanoccurrencehappening[42]. Inordertodeterminethelikelihoodofa
classgivenacollectionofcharacteristics,theGaussianNaiveBayesalgorithmreliesonthe
presumptionofthefeaturesbeingnormallydistributed.
3.2.5. SupportVectorMachine
Supportvectormachinesareaformofsupervisedlearningalgorithmusedtosolve
classification and regression issues [43]. The SVM algorithm divides data into groups
bylocatingahyperplaneinahigh-dimensionalregion. TheSVMapproachisespecially
helpfulwhenworkingwithdatathatarenotlinearlyseparable,asitusesakernelfunctions
toconvertthedatatoahigher-dimensionalspacewheretheycanbedivided.
3.2.6. K-NearestNeighbros
K-nearest neighbors is a simple classification method that works by locating the k
nearest data points in the training set with respect to a particular test point and then
predictingthetestpoint’sclassbasedonthemajorityclassofitsk-nearestneighbors[44].
KNNisanon-parametricmethod,whichmeansthatitdoesnotmakeanyassumptions
aboutthedistributionofthedata.
3.3. Bootstrapping
Inthebootstrappingtechnique,Hello,Feature-Request,andFeature-Replymessages
areexchangedviatheOpenFlowprotocolwhenthenetworkisswitchedon. Thistakes
place between the controller and the switch to obtain the network’s global view of the
controller. TheFeature-Requestmessageisperiodicallygeneratedbythecontrollerthrough
Hellomessagestoobtaintheswitchfeatures.
TheswitchsendsaFeature-ReplymessagetothecontrollerafterreceivingtheFeature-
Requestmessage; thecontrollerobtainstheswitch’scapabilitiesinthisprocess. Asdis-
cussedearlier,reactiveflowinstallationmodeisassumed. Unliketraditionalforwarding
devices,theswitcheshavenoawarenessinthismodewhenthenetworkisconfiguredfor
routingandfirststartsrunning. Whenthedatapacket(PackectIn)ofaflowarrivesatthe
switch,theswitchimmediatelylooksforthematchingentryinitsforwardingtable;ifthe
matchingflowentryisfound,itforwardsthesaiddatapacketusingthecorresponding
actionintheflowtableentry. Otherwise, theswitchasksthecontrollertocomputethe
actionfortheflow.
Thecontrollerchecksthenetworkreachabilityrulefortheflowamongsourceand
destinationIPs;whetheritisallowedordeniedisspecifiedatthecentralcontrollernext
tothereceivingrequestfromtheswitch. Iftheflowisdenied,thecontrollerinstallsthe
dropactionattheswitches;otherwise,itcomputestheprimarypath,forwhichvarious
approachescanbeused. Whenaswitchisconnectedtoacontroller,thecontrollerperi-
odicallysendscommandstothedevicesthroughthelinklayerprotocolofthediscovery

Sensors2023,23,8218 8of17
broadcastdomain’sdiscoveryprotocolviaallinterfacesoftheswitches. Adiscoverypacket
containsthedatapathidentificationofthesendinghostalongwiththeinterfaceinforma-
tionthatgeneratesthepacketforthedestinationend. Occupiedsetsofdestinationdevice
MACaddressesandtheEthernettypearedifferentiatedfromotherkindsofpacketsinthe
networkbythecontrollerbasedonthelinklayerdiscoveryprotocol(LLDP).TheLLDPis
widelyusedfordiscoveryofdirectlinkstothenexthopinanetwork(forinstance,among
twoswitches),whilethebroadcastdomaindiscoveryprotocoliswidelyusedfordevice
discoveryinthesamedomain.
3.4. ControllerEventCompositioninGraphTheory
Event-drivenapplicationbehaviorhasthecompositionofallSDNbindings(controller,
server,forwardingdevices);inthispaper,weusegraphtheorytosupportourproposed
approach. Applications use a hash object (dictionary) to store nodes, attributes, link
properties,communicationchannelattributesoverSSL,andstate-of-the-artalgorithmic
pathcomputationoptimization. Graphcompositioncanbeinductedthroughthefollowing
procedureinthePOXcontroller:
G = (V,E), (1)
where“V”representstheendnodesandforwardingdevicesinthenetworkand“E”isthe
setoftheedgesofdevicesandendnodesinthenetwork.
Morespecifically,anetworktranslatedorcomposedintheformatofthegraphencom-
passesthefollowingattributes:
V =(MAC,IP,sensorconnected,localsensorcontrollerconnected,timeinnetwork,
eventonadditionanddeletion).
E =(edgesamongthenodes(sensors),edgesamongthecontrollerinthenetwork,
edgesfromswitchestothesensorconveyerorcontroller,timestampofjoiningtheSDN
network,timeofleavingthenetwork).
3.5. AlternativePathComputationinCaseofCriticalSensorTraffic
Inthisprocess,ourcontrolapplicationisintendedtofindapathwithintermediate
forwardingdevicesthatarenotincludedinthecontrollerdictionaryrecordoftheinstalled
flowrule. Criticaltrafficrequiresalternatepathstoenablespeedycontroloftrafficbythe
controllerspecificationandreceivingattheserver.
OFPFC_ADDisanOpenFlowcommandusedfortheflowruleinstallationintheflow
tableoftheswitch. Thematchfieldsencapsulatedintheflow-addingcommandarefirst
comparedforacorrespondingflowruleentryintheswitch. Matchingobjectsarematched:
nw_proto(applicationlayerprotocol),match.dl_type(opcodeofIPV4,ARP),match.nw_src
(sourceIPaddress)andmatch.nw_dst(destinationIPaddress). Thetimeoutandthepriority
valuesarespecifiedbythecontroller,alongwiththeflowruleinstallationcommand.
3.6. RoutingAlgorithm
ReinforcementLearningandSoftware-DefinedNetworkingforIntelligentRouting
(RSIR)introducesaknowledgeplaneandidentifiesaroutingalgorithmusingReinforce-
mentLearning(RL)thattakeslinkstateinformationintoconsiderationwhenexploring,
learning,andexploitingpotentialpathsduringintelligentroutingregardlessofanydy-
namictraffictransitions. Thisalgorithmmakesuseoftheenvironment’sinteraction,thein-
telligenceofferedbyRL,andtheglobalperspectiveformanagingthenetworkprovidedby
SDN.Itdeterminesandimplementsoptimumroutesintheroutingtableofthedataplane
switchesinadvance.
TheRLagentdefinestheflowpathwaysusingtheQ-learningapproach. Q-learningis
amethodwithoutmodelsthatdoesnotrequirepriorknowledgeoftherewardearnedby
performingagivenactioninaspecifiedsituation[30]. TheflowoftheQL-basedroutingis
showninFigure4.

Sensors2023,23,8218 9of17
Figure4.Q-Learningalgorithm.
3.7. MLPerformanceMetrics
The performance metrics used for evaluation were the accuracy, precision, recall,
andF1-score,usingthefollowingequations.
TP+TN
Accuracy = (2)
TP+TN+FP+FN
TP
Precision = (3)
TP+FP
TP
Recall = (4)
TP+FN
2∗Precision∗Recall
F1-Score = (5)
Precision+Recall

Sensors2023,23,8218 10of17
3.8. BoxPlot
Aboxplotisastatisticalgraphicthatshowsthedistributionofadatasetintheform
ofthemedian,interquartilerange(IQR),andrangeofthedata[45]. Boxplotsarehelpful
forassessingadataset’sdistribution,skewness,andprobableoutliers. Themiddle50%of
thedataisindicatedbytheboxitself,thelowestorfirstquartile(Q1)representsthe25th
percentile, and the highest or third quartile (Q3) indicates the 75th percentile. The line
inside the box shows the median value of the data. The IQR is the difference between
Q3 and Q1. There are two whisker lines that extend from the outside of the box; one
extendsfromtheminimumtothelowerquartileandthesecondfromtheupperquartile
tothemaximum. Theoutliervaluesareindicatedbythesmallcirclesontopofthetop
whiskerandatthebottomofthebottomwhisker. Anoutlierinthedataisaveryhigh
orextremelylowvalue. Theboxplot’stopwhiskerreflectsthegreatestvalueinthedata
thatisnotanoutlier. Theoutliervaluescanbeobtainedasoutlier>Q3+(3×IQR)and
outlier<Q1−(3×IQR).
3.9. PerformanceEvaluation
Mininet 2.2 EEL was used as a network simulator, as it provides good ease of use
fortheuserandoffersformationandeasysettingofSDNelementsalongwithsharing,
customization, and testing of the SDN network’s performance. It includes forwarding
deviceswitches,endhosts,links,andinterfacesforcontrollerinteroperability. Further,it
providesaseparatevirtualenvironmentforexecutingvariousapplicationsforeachhost.
Forcontrolfunctions,thePoxcontrollerevent-drivenapproachwasused. Ournetwork
simulator-basedvirtualscenarioencompassestheresourcesofanHP450G5,Corei7-8250U,
16GBofphysicalmemory,andLinuxdistribution(Ubuntu)operatingsystem.
Thetopologyofournetworkconsistsof25sensorswiththesamegeolocationformea-
suringhumiditylevel,temperature,windspeed,leafmoisture,soiltemperature,andsoil
moisture. Moreprecisely,eachsensorcontributorhasanIPaddress. Thetopologyconsists
oftenOpenFlow-EnabledswitcheswhicharecommandedbythePoxcontrollerforreach-
abilityspecificationandinstallationofflowrules. Theseforwardingdevicesactuponthe
receivedcommandsinstantaneously.
4. ResultsandDiscussion
The results of the proposed number of sensor communications are discussed for
variousparametersi.e.,sensornodes,protocol,controller,simulationtime,packettime,
traffic,andtotalcalculationtime. Theparametersusedforthesimulationsareshownin
Table1.
Table1.Simulationparameters.
Sr.No Parameter Value
1 NumberofSensors 25
2 Protocol OpenFlow
3 Controller Pox
4 SimulationTimePerIteration 1min
5 Packetsperiteration 10,000
6 PacketSize 512bytes
7 Bandwidth 10Mbps
8 Traffic UDP
9 ShortestRouteCalculation RSIR[46]
Variousevaluationmetrics,suchasaccuracy,precision,recall,andF1score,provided
in Equations (2)–(5), were used to evaluation the models’ performance, as mentioned in
Table2.Notably,theRFandDTmodelsoutperformtheotherMLmodelsintermsofaccuracy.
AgraphicalpresentationoftheresultsforalltheMLmodelsisshowninFigure5. Overall,
theRFandDTmodelsperformwellacrossallmeasures,indicatingtheirabilitytoaccurately
categorizedataintotherequiredcategories.TheperformanceoftheKNNandSVMmodelsis

Sensors2023,23,8218 11of17
lowcomparedtothatoftheLRandNBmodels,whichinturnperformlesseffectivelythan
theRFandDTmodels.
Table2.Performanceevaluationoftheproposedtechniqueandindividualclassifiers.
Methods Accuracy Precision Recall F1Score
LR 0.81 0.52 0.47 0.48
NB 0.84 0.68 0.73 0.65
KNN 0.93 0.82 0.85 0.83
SVM 0.94 0.82 0.85 0.83
RF 0.99 0.99 0.97 0.98
DT 0.99 0.99 0.97 0.98
Figure5.ComparativeanalysisofvariousMLmodels.
The box plot results for all the features are presented in Table 3 and Figures6and7.
Adetailedanalysisoftheresultsforeachfeatureisprovidedbelow.
HumidityLevel:
The mean humidity level is 28, with 75% of the data being less than 31 and 25%
beinglessthan26. Themaximumhumiditylevelis52,theminimumhumiditylevelis24,
andthereare106outliers. TheIQRis5,with38.5beingthehighestoutlierand18.5being
thelowestoutlier.
Temperature:
Themeantemperatureis20,with75%ofthedatabeinglessthan23and25%being
lessthan18. Themaximumtemperatureis32,theminimumtemperatureis8,andthere
aretwelveoutliers. TheIQRis5,with30.5beingthehighestoutlierand18.5beingthe
lowestoutlier.
WindSpeed:
Themeanwindspeedis9, with75%ofthedatabeinglessthan10and25%being
lessthan8. Themaximumwindspeedis20,theminimumwindspeedis7,andthereare
98outliers. TheIQRis2,with13beingthehighestoutlierand5beingthelowestoutlier.
LeafMoisture:
Themeanleafmoistureis86,with75%ofthedatabeinglessthan92and25%beingless
than84. Themaximumleafmoistureis97,theminimumleafmoistureis66,andthereare
nooutliers. TheIQRis8,with104beingthehighestoutlierand72beingthelowestoutlier.
SoilTemperature:
The mean soil temperature is 17, with 75% of the data being less than 19 and 25%
beinglessthan15. Themaximumsoiltemperatureis24,theminimumsoiltemperatureis
12,andtherearenooutliers. TheIQRis4,with25beingthehighestoutlierand9beingthe
lowestoutlier.

| Sensors2023,23,8218 |     |     |     |     |     |     |     | 12of17 |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | ------ |
SoilMoisture:
Themeansoilmoistureis13,with75%ofthedatabeinglessthan14and25%being
lessthan12. Themaximumsoilmoistureis15,theminimumsoilmoistureis6,andthere
arenooutliers. TheIQRis2,with17beingthehighestoutlierand9beingthelowestoutlier.
Figure6.Comparativeanalysisofthedatadistributionforvariousparameters.
Table3.Comparativeanalysisofthedatadistributionforvariousparameters.
|                 | Min 25th         |        | 75th       | Max   | Noof     |     | Lower   | Higher  |
| --------------- | ---------------- | ------ | ---------- | ----- | -------- | --- | ------- | ------- |
| Features        |                  | Median |            |       |          | IQR |         |         |
|                 | Value Percentile |        | Percentile | Value | Outliers |     | Outlier | Outlier |
| HumidityLevel   | 24 26            | 28     | 31         | 52    | 106      | 5   | 18.5    | 38.5    |
| Temperature     | 8 18             | 20     | 23         | 32    | 12       | 5   | 18.5    | 30.5    |
| WindSpeed       | 7 8              | 9      | 10         | 20    | 98       | 2   | 5       | 13      |
| LeafMoisture    | 66 84            | 86     | 92         | 97    | 0        | 8   | 72      | 104     |
| SoilTemperature | 12 15            | 17     | 19         | 24    | 0        | 4   | 9       | 25      |
| SoilMoisture    | 6 12             | 13     | 14         | 15    | 0        | 2   | 9       | 17      |

Sensors2023,23,8218 13of17
Figure7.Datadistributionanalysisfortheindividualparameters.
Figure8presentsacomparisonoftraffictypesbasedontheiraveragedelaycharac-
teristics. Becauseofthehighfrequencyofdatatransfersinthiscategory,“normaltraffic”
has a significantly larger average latency in this context. The increased frequency of
regulardatapackettransmissioncausesnetworkcongestion,whichcontributestoan
increaseintheaveragedelaytime. When“criticalpackettransmission”isconsidered,
thescenariochanges,resultinginapathwithlesstraffic. Asthispathencountersless
congestion,thereareshorterwaittimesinthisscenariocomparedtotheusualtraffic
category. This difference in latency can be related to differences in traffic flow and
packetreceptionfrequencies,wherenormaltrafficconsistsofacontinuousflowofdata

Sensors2023,23,8218 14of17
packets;criticalpackettransmissioncompriseslesstraffic,andasaresult,lesscongestion
andshorterdelayperiods.
Figure9showstheaveragepacketlossencounteredbythethreedatacategoriesof
emergency,normal,andon-demand. Notably,themeandelaysforemergencytrafficare
consistently shorter than those for regular and on-demand traffic. The reason for this
disparityisthattheRSIRalgorithmisusedforemergencydata. RSIRprioritizestheuseof
shorterandlesscongestedpathsforcriticaldatapackets. Asaresult,criticaldatapackets
experiencefewerdelaysandlesspacketloss. Ontheotherhand,normalandon-demand
traffic, which may use alternative routing algorithms, tend to face significantly longer
delays,andasaresultexperiencehigheraveragepacketloss.
Figure8.Averagedelaythroughouttheweek.
Figure9.Averagepacketlossthroughouttheweek.
Figure10representstheaveragethroughputoverthecourseofaweekforthethree
data traffic types of emergency, on-demand, and routine. It can be noticed that critical
andon-demanddatatrafficfollowauniquepatterndefinedbyabroaderdispersionof

Sensors2023,23,8218 15of17
flowsoverthenetwork. Whencomparedwithnormaldataflow,thisphenomenonresults
intheuseofahighernumberofcomparativelyless-usedchannels. Surprisingly,despite
thedecreasedpacketlossandmeandelayencounteredbycriticalandon-demanddata,
themeanthroughputforeachcategoryappearstobelowerthanfornormaltraffic. Itis
worthmentioningthatcriticalandon-demanddatareceiveadvantagessuchasdecreased
datalossandshorterdelaysasaresultoftheirmoreeffectiverouting. Thediversificationof
theirflowsacrossmultiplenetworkchannelsmayresultinlessoptimizeduseofavailable
bandwidth,resultinginreducedbandwidth. Thishighlightsthecomplexitiesofrouting
schemesandtheirinfluenceonnetworkefficiency.
Figure10.Averagethroughputthroughouttheweek.
5. Conclusions
In this research, we have presented an event-based data analysis technique for
smartagriculturesystemsusingtheInternetofThings(IoT)basedonmachinelearning
(ML)modelssuchasLogisticRegression(LR),RandomForest(RF),k-NearestNeigh-
bours (KNN), Support Vector Machine (SVM), Naive Bayes (NB), and Decision Tree
(DT).Themodels’accuracywasusedtoevaluatetheirperformanceforfeaturessuchas
humiditylevel,temperature,soilmoisture,windspeed,etc.,findingacceptablelevels
ofaccuracy. Theproposedapproachmakesuseofsoftware-definednetworking(SDN)
capabilitiestoidentifyandmanageessentialnetworkevents. Asoftware-definednet-
working(SDN)controllerandtheQ-learningalgorithmarethenusedtoroutethedata
traffic. Ourresultsindicatethattheproposedtechniquecanefficientlymanagethedata
flow. TheusefulnessofmergingMLandSDNforintelligentroutingandnetworkperfor-
manceoptimizationisdemonstratedbythisresearch. Havingexploredthebenefitsof
utilizingadvancedalgorithmsfordataclassificationandroutinginasoftware-defined
IoTnetwork,thescalabilityandapplicationofthisapproachinlargerorheterogeneous
networksmaybeaninterestingareaforfutureresearch.
AuthorContributions:Conceptualization,F.M.andW.U.K.;methodology,F.M.andW.U.K.;software,
F.M.andW.U.K.;validation,F.M.andW.U.K.;formalanalysis,F.M.,S.U.J.andW.U.K;investigation,
F.M.andJ.A.; resources, S.U.J.andJ.A.; datacuration, F.M.andW.U.K.; writing—originaldraft
preparation,F.M.andW.U.K;writing—reviewandediting,S.U.J.andJ.A.;visualization,F.M.and
S.U.J.;supervision,F.M.andJ.A.;projectadministration,F.M.andW.U.K.;fundingacquisition,S.U.J.
andJ.A.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement: Notapplicable.

Sensors2023,23,8218 16of17
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Thecollectionofdatausedintheresearchisaccessibleatthefollowing
repository(accessedon5August2023):https://github.com/researchcsaup/IoTs.git.
ConflictsofInterest:Theauthorsdeclarethattheyhavenoconflictofinteresttoreportregarding
thepresentstudy.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
IoT InternetofThings
SDN Software-DefinedNetwork
WRAN WirelessRegionalAreaNetwork
CPE ConsumerPremiseEquipment
WSN WirelessSensorNetwork
TDMA Time-DivisionMultipleAccess
References
1. Feamster,N.;Rexford,J.;Zegura,E.TheroadtoSDN:Anintellectualhistoryofprogrammablenetworks.ACMSIGCOMMComp.
Comm.Rev.2014,44,87–98.[CrossRef]
2. Ouallane,A.A.;Bakali,A.;Bahnasse,A.;Broumi,S.;Talea,M.Fusionofengineeringinsightsandemergingtrends:Intelligent
urbantrafficmanagementsystem.Inf.Fusion2022,88,218–248.[CrossRef]
3. Priyadarsini,M.;Bera,P.Softwaredefinednetworkingarchitecture,trafficmanagement,security,andplacement: Asurvey.
Comput.Netw.2021,192,108047.[CrossRef]
4. Zervopoulos,A.; Tsipis,A.; Alvanou,G.; Bezas,K.; Papamichail,A.Wirelesssensornetworksynchronizationforprecision
agricultureapplications.Agriculture2020,10,89.[CrossRef]
5. Vincent,D.R.;Deepa,N.;Elavarasan,D.;Srinivasan,K.;Chauhdary,S.H.;Iwendi,C.Sensorsdrivenartificialintelligencebased
agriculturerecommendationmodelforassessinglandsuitability.Sensors2019,19,3667.[CrossRef][PubMed]
6. Kim,W.S.;Lee,W.S.;Kim,Y.J.Areviewoftheapplicationsoftheinternetofthings(IoT)foragriculturalautomation.J.Biosys.
Eng.2020,45,385–400.[CrossRef]
7. Friha,O.;Ferrag,M.A.;Shu,L.;Maglaras,L.;Wang,X.Internetofthingsforthefutureofsmartagriculture:Acomprehensive
surveyofemergingtechnologies.IEEE/CAAJ.Autom.Sin.2021,8,718–752.[CrossRef]
8. Adli,H.K.;Remli,M.A.;WanSalihinWong,K.N.S.;Ismail,N.A.;González-Briones,A.;Corchado,J.M.;Mohamad,M.S.Recent
AdvancementsandChallengesofAIoTApplicationinSmartAgriculture:AReview.Sensors2023,23,3752.[CrossRef]
9. Saban,M.;Bekkour,M.;Amdaouch,I.;ElGueri,J.;AitAhmed,B.;Chaari,M.Z.;Ruiz-Alzola,J.;Rosado-Muñoz,A.;Aghzout,O.
ASmartAgriculturalSystemBasedonPLCandaCloudComputingWebApplicationUsingLoRaandLoRaWan.Sensors2023,
23,2725.[CrossRef]
10. Asaithambi,S.;Ravi,L.;Kotb,H.;Milyani,A.H.;Azhari,A.A.;Nallusamy,S.;Vairavasundaram,S.AnEnergy-Efficientand
Blockchain-IntegratedSoftwareDefinedNetworkfortheIndustrialInternetofThings.Sensors2022,22,7917.[CrossRef]
11. Baggio,A.Wirelesssensornetworksinprecisionagriculture. InProceedingsoftheACMWorkshoponReal-WorldWireless
SensorNetworks(REALWSN2005),Stockholm,Sweden,21June2005;p.1567.
12. Khanna,A.;Kaur,S.Evolutionofinternetofthingsanditssignificantimpactinthefieldofprecisionagriculture.Comput.Electron.
Agric.2019,157,218–231.[CrossRef]
13. Capello,F.;Toja,M.;Trapani,N.Arealtimemonitoringservicebasedonindustrialinternetofthingstomanageagrifoodlogistics.
InProceedingsofthe6thInternationalConferenceonInformationSystems,LogisticsandSupplyChain,Bordeaux,France,1–4
June2016;pp.1–8.
14. Pang,Z.;Chen,Q.;Han,W.;Zheng,L.Value-centricdesignoftheinternetofthingssolutionforfoodsupplychain:Valuecreation,
sensorportfolioandinformationfusion.Inf.Syst.Front.2015,17,289–319.[CrossRef]
15. Zhang,X.;Zhang,J.;Li,L.;Zhang,Y.;Yang,G.Monitoringcitrussoilmoistureandnutrientsusinganinternetofthingsbased
system.Sensors2017,17,447.[CrossRef][PubMed]
16. Verdouw,C.;Wolfert,S.;Tekinerdogan,B.Internetofthingsinagriculture.CABRev.Persp.Agr.Vet.Sci.Nutr.Nat.Res.2016,11,
1–12.[CrossRef]
17. Amaral,P.;Dinis,J.;Pinto,P.;Bernardo,L.;Tavares,J.;Mamede,H.S.Machinelearninginsoftwaredefinednetworks: Data
collectionandtrafficclassification.InProceedingsofthe2016IEEE24thInternationalConferenceonNetworkProtocols(ICNP),
Singapore,8–11November2016;pp.1–5.
18. Phan,T.V.;Islam,S.T.;Nguyen,T.G.;Bauschert,T.Q-DATA:Enhancedtrafficflowmonitoringinsoftware-definednetworks
applyingQ-learning.InProceedingsofthe201915thInternationalConferenceonNetworkandServiceManagement(CNSM),
Halifax,NS,Canada, 21–25October2019;pp.1–9.

Sensors2023,23,8218 17of17
19. Kim,S.I.;Kim,H.S.DynamicservicefunctionchainingbyresourceusagelearninginSDN/NFVenvironment.InProceedingsof
the2019InternationalConferenceonInformationNetworking(ICOIN),KualaLumpur,Malaysia,9–11January2019;pp.485–488.
20. Xu,J.;Wang,J.;Qi,Q.;Sun,H.;He,B.IARA:Anintelligentapplication-awareVNFfornetworkresourceallocationwithdeep
learning.InProceedingsofthe201815thAnnualIEEEInternationalConferenceonSensing,Communication,andNetworking
(SECON),HongKong,China,11–13June2018;pp.1–3.
21. Hossain,M.;Rahman,M.;Hosen,A.S.M.;Seo,C.;Cho,G.H.Intellectualpropertytheftprotectionininternetofthingsbased
precisionagricultureusingsoftwaredefinednetwork.Electronics2021,10,1987.[CrossRef]
22. Abbassi,Y.;Benlahmer,H.BCSDN-IoT:Towardsaninternetofthingssecurityarchitecturebasedonsoftwaredefinednetwork
andblockchain.Int.J.Electr.Comput.Eng.Syst.2022,13,155–163.
23. Kaur,G.;Gupta,P.HybridapproachfordetectingDDOSattacksinsoftwaredefinednetworks.InProceedingsofthe2019Twelfth
InternationalConferenceonContemporaryComputing(IC3),Noida,India,8–10August2019;pp.1–6.
24. Prakash,A.;Priyadarshini,R.Anintelligentsoftwaredefinednetworkcontrollerforpreventingdistributeddenialofservice
attack.InProceedingsofthe2018SecondInternationalConferenceonInventiveCommunicationandComputationalTechnologies
(ICICCT),Coimbatore,India,20–21April2018;pp.585–589.
25. Akyildiz,I.F.;Lee,A.;Wang,P.;Luo,M.;Chou,W.AroadmapfortrafficengineeringinSDN-OpenFlownetworks.Comput.Netw.
2014,71,1–30.[CrossRef]
26. Mijumbi, R.; Serrat, J.; Rubio-Loyola, J.; Bouten, N.; De Turck, F.; Latre, S. Dynamic resource management in SDN-based
virtualizednetworks.InProceedingsofthe10thInternationalConferenceonNetworkandServiceManagement(CNSM)and
Workshop,RiodeJaneiro,Brazil,17–21November2014;pp.412–417.
27. Mourad, A.; Yang, R.; Lehne, P.H.; Oliva, A.Towards6G:Evolutionofkeyperformanceindicatorsandtechnologytrends.
InProceedingsofthe20202nd6GWirelessSummit(6GSUMMIT),Levi,Finland,17–20March2020;pp.1–5.
28. Etengu,R.;Tan,S.C.;Kwang,L.C.;Abbou,F.M.;Chuah,T.C.AI-assistedframeworkforgreen-routingandloadbalancingin
hybridsoftware-definednetworking:Proposal,challengesandfutureperspective.IEEEAccess2020,8,166384–166441.[CrossRef]
29. Qian, Y.; Wu, J.; Wang, R.; Zhu, F.; Zhang, W. Survey on reinforcement learning applications in communication networks.
J.Commun.Inf.Netw.2019,4,30–39.[CrossRef]
30. Mammeri,Z.Reinforcementlearningbasedroutinginnetworks:Reviewandclassificationofapproaches.IEEEAccess2019,7,
55916–55950.[CrossRef]
31. Jamshidi,S.TheApplicationsofMachineLearningTechniquesinNetworking.Ph.D.Dissertation,UniversityofOregon,Eugene,
OR,USA,2019.
32. Zhang,Y.;Xin,J.;Li,X.;Huang,S.Overviewonroutingandresourceallocationbasedmachinelearninginopticalnetworks.Opt.
FiberTechnol.2020,60,102355.[CrossRef]
33. Boutaba,R.;Salahuddin,A.N.;Limam,M.;Ayoubi,S.;Shahriar,N.;Estrada-Solano,F.;Caicedo,O.M.Acomprehensivesurveyon
machinelearningfornetworking:Evolution,applicationsandresearchopportunities.J.InternetServ.Appl.2018,9,16.[CrossRef]
34. Xie,J.;Yu,F.R.;Huang,T.;Xie,R.;Liu,J.;Liu,Y.Asurveyofmachinelearningtechniquesappliedtosoftwaredefinednetworking
(SDN):Researchissuesandchallenges.IEEECommun.Surv.Tutor.2019,21,393–430.[CrossRef]
35. Zhao,Y.;Li,Y.;Zhang,X.;Geng,G.;Zhang,W.;Sun,Y.Asurveyofnetworkingapplicationsapplyingthesoftwaredefined
networkingconceptbasedonmachinelearning.IEEEAccess2019,7,95397–95417.[CrossRef]
36. Tamizhselvan,C.;Vijayalakshmi,V.SDN-MCHO:SoftwareDefinenetworkbasedMulti-criterionHysteresisOptimizationbased
forreliabledeviceroutinginInternetofThingsforthesmartsurveillanceapplication.Comput.Commun.2020,153,632–640.
37. Sharma,S.;Nitin,C.;Kaushal,K.B.;Abhay,K.S.;Prashan,M.;Swati,S.;Sundeep,R.;Sandesh,T.FCS-fuzzynet:Clusterhead
selectionandrouting-basedweedclassificationinIoTwithmapreduceframework.WirelessNet.2021,27,4929–4947.[CrossRef]
38. Naeem,F.;Muhammad,T.;Vincent,P.SDN-enabledenergy-efficientroutingoptimizationframeworkforindustrialInternetof
Things.IEEETrans.Ind.Inform.2020,17,5660–5667.[CrossRef]
39. Hosmer, D.W., Jr.; Lemeshow, S.; Sturdivant, R.X.AppliedLogisticRegression; JohnWiley&Sons: Hoboken, NJ,USA,2013;
Volume398.
40. Quinlan,J.R.Inductionofdecisiontrees.Mach.Learn.1986,1,81–106.[CrossRef]
41. Breiman,L.Randomforests.Mach.Learn.2001,45,5–32[CrossRef]
42. Domingos,P.;Pazzani,M.OntheoptimalityofthesimpleBayesianclassifierunderzero-oneloss.Mach.Learn.1997,29,103–130.
[CrossRef]
43. Cortes,C.;Vapnik,V.Support-vectornetworks.Mach.Learn.1995,20,273–297.[CrossRef]
44. Cover,T.;Hart,P.Nearestneighborpatternclassification.IEEETrans.Inf.Theory1967,13,21–27.[CrossRef]
45. McGill,R.;Tukey,J.W.;Larsen,W.A.Variationsofboxplots.Am.Stat.1978,32,12–16.
46. Casas-Velasco,D.M.;Rendon,O.M.C.;daFonseca,N.L.Intelligentroutingbasedonreinforcementlearningforsoftware-defined
networking.IEEETrans.Netw.Serv.Manag.2020,18,870–881.[CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.