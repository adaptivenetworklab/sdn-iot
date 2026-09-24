# A-Novel-DeepLearning-Model-for-Remote-Driver-Monitoring-in-SDNBased-Internet-of-Autonomous-Vehicles-Using-5G-Technolog

> Source file: `A-Novel-DeepLearning-Model-for-Remote-Driver-Monitoring-in-SDNBased-Internet-of-Autonomous-Vehicles-Using-5G-Technolog.pdf`

---

applied
sciences
Article
A Novel Deep-Learning Model for Remote Driver Monitoring
in SDN-Based Internet of Autonomous Vehicles Using
5G Technologies
SherineNagySaleh* andCherineFathy
ComputerEngineeringDepartment,CollegeofEngineeringandTechnology,ArabAcademyforScienceand
Technology(AAST),Alexandria1029,Egypt
* Correspondence:sherine_nagi@aast.edu
Abstract:TherapidadvancementintheInternetofThings(IoT)anditsintegrationwithArtificial
Intelligence(AI)techniquesareexpectedtoplayacrucialroleinfutureIntelligentTransportation
Systems(ITS).Additionally,thecontinuousprogressintheindustryofautonomousvehicleswill
accelerateandincreasetheirshortadoptioninsmartcitiestoallowsafe,sustainableandaccessible
trips for passengers in different public and private means of transportation. In this article, we
investigatetheadoptionof5Gdifferenttechnologies,mainly,theSoftware-DefinedNetworks(SDN)
tosupportthecommunicationrequirementsofdelegationofcontroloflevel-2autonomousvehicles
totheRemote-ControlCenter(RCC)intermsofultra-lowdelayandreliability.Thisdelegationoccurs
uponthedetectionofadrowsydriverusingourproposeddeep-learning-basedtechniquedeployed
attheedgetoreducethelevelofaccidentsandroadcongestion.Thedeeplearning-basedmodelwas
evaluatedandproducedhigheraccuracy,precisionandrecallwhencomparedtoothermethods.The
roleofSDNistoimplementnetworkslicingtoachievetheQualityofService(QoS)levelrequiredin
thisemergencycase.Decreasingtheend-to-enddelayrequiredtoprovidefeedbackcontrolsignals
backtotheautonomousvehicleistheaimofdeployingQoSsupportavailableinanSDN-based
network. Feedbackcontrolsignalsaresenttoremotelyactivatethestoppingsystemortoswitch
thevehicletodirectteleoperationmode. Themininet-WiFiemulatorisdeployedtoevaluatethe
performanceoftheproposedadaptiveSDNframework,whichistailoredtoemulateradioaccess
networks.Oursimulationexperimentsconductedonrealisticvehicularscenariosrevealedsignificant
Citation:Saleh,S.N.;Fathy,C.A
NovelDeep-LearningModelfor improvementintermsofthroughputandaverageRound-TripTime(RTT).
RemoteDriverMonitoringin
SDN-BasedInternetofAutonomous Keywords: deep-learning; internet of things (IoT); software defined networks (SDN); artificial
VehiclesUsing5GTechnologies.Appl. intelligence(AI);autonomousvehicle;qualityofservice(QoS);drowsydetection;5Gslicing;V2X;MEC
Sci.2023,13,875. https://doi.org/
10.3390/app13020875
AcademicEditor:KrzysztofKoszela
Received:6December2022 1. Introduction
Revised:26December2022 There is rapid progress in vehicle automation technologies, which has resulted in
Accepted:5January2023 theavailabilityofautonomouscarsforconsumerpurchase. Accordingto[1],theglobal
Published:8January2023
autonomouscarmarketisexpectedtoreachasizeofnearly62billionU.S.dollarsin2026.
Six levels of driving automation were defined by the Society of Automotive Engineers,
wherelevel0isthecaseofnoautomationandlevel5isthecaseoffullautomationasillus-
tratedinFigure1.Theprimaryadvantagesofautonomousvehicleshavebeennamedby
Copyright: © 2023 by the authors.
theNationalHighwayTrafficSafetyAdministration(NHTSA)asfollows: safety,economic
Licensee MDPI, Basel, Switzerland.
and societal benefits, efficiency and convenience and mobility. Although autonomous
This article is an open access article
vehicleshavehigheraccidentratesthanhuman-drivenvehicles,theinjuriesarelesssevere.
distributed under the terms and
Onaverage,thereare9.1autonomousvehicleaccidentspermillionmilesdriven[2],while
conditionsoftheCreativeCommons
Attribution(CCBY)license(https:// 4.1crashespermillionmilesforregularvehicles. So,thereisanurgentneedtostrengthen
creativecommons.org/licenses/by/ theconceptofaddingaremotecontrolcenterintheautomateddrivingmodelthattakes
4.0/). overcontrolinemergencycases. Article[3]introducesthreeservicecategorieswherethe
Appl.Sci.2023,13,875.https://doi.org/10.3390/app13020875 https://www.mdpi.com/journal/applsci

Appl.Sci.2023,13,875 2of15
conceptofacontrolcenterisdeployedinautomateddriving. Thesecategoriesarenamely:
emergencyservice,fleetserviceandteleoperationservice(directandindirectteleoperation).
Moreover,tosupportthechallengesofautonomousvehicles(AVs)intermsofQoS,
high mobility, dynamic topologies, a programmable and scalable network paradigm is
requiredtomanageandcontrolthiscommunicationscenario[4]. Thiscanbedonebythe
deploymentofsoftware-definednetworking(SDN).
SDNisanetworkparadigmthatseparatesthecontrolplaneandthedataplane. Asa
resultofthisseparation,thecontrolplaneisimplementedinacentralizedcontroller,and
then,forwardingrulesareinstalledbythiscontrollerintherouters(networkswitches),
whichsimplifiespolicyenforcement,networkreconfiguration,programmabilityandevo-
lution[5,6]. Currently,thecontroller-dataplaneinterface(C-DPI)standardthatpermits
communication between controllers and data plane devices (network switches) is the
OpenFlowprotocol.
Ontheotherhand,artificialintelligence(AI)techniquesbecamecrucialcomponents
ofanautonomousvehicle. AItechniquesareappliedinautonomousvehiclesindifferent
domainsthatcomprise: sensordataprocessing,pathplanning,pathexecution,monitoring
vehicleconditions,andinsurancedatacollection.
Figure1.Vehicleautomationlevels.
In addition, edge computing (EC) overcomes the problems encountered with V2I
(VehicletoInfrastructure)approachesofSDNwithinVANET(VehicularAdhocNetworks)
RSU(RoadSideUnit)communications. So,aperformanceinvestigationoftheusageof
MEC(MobileEdgeComputing)asedgelayerimplementationiscarried-outtoconclude
itsimpactonourproposedmodel. MECintegratesstorageandprocessingintermediate
nodesoverthebasestationofcellularnetworks,whichallowsthedeploymentofcloud
computingservicewithintheradioareanetwork(RAN)[7].
Article[8]presenteda5GV2XecosystembasedonSDNtoprovidetheInternetof
Vehicles(IoV).Simulationsusingns3wereconductedtoevaluatevehicularInternet-based
video service traffic and vehicle-to-vehicle (V2V) communications in urban and rural
scenarios. Article[9]developedaframeworkusing5Gnetworkslicingforapplication-
driven vehicular networks. The authors evaluated their model using simulations and
comparedtheirresultstothestate-of-the-artapproaches.
Therearethreebasicmethodsofsleepinessdetectiontechniques,whicharethemea-
surementofvehiclecharacteristics,physiologicalcharacteristics,orbehavioralcharacteris-

Appl.Sci.2023,13,875 3of15
tics. Vehiclecharacteristicmeasurementfocusesontheassessmentofdriverdrowsiness
andisbasedonvehiclemotionslikethelocationofthevehicleinthelane,steeringwheel
movement,andstopandaccelerationpedalaction. Measurementofphysiologicalchar-
acteristicsincludesdetectingdriverdrowsinessusingbrainsignals,heartrate,andnerve
impulses, among other things. These solutions are not commercially viable since they
areobtrusiveandplaceadditionalstressonthedriver’sbody. Behavioralcharacteristic
measurementisbasedonthedriver’sexpressionandfacialmovementtodeterminetheir
leveloftiredness. Thismethoddoesnotcauseanydisruptionsandisdependentonthe
cameracapturingseveralfacialexpressionstances[10].
Arecentsurvey[11]haspresentedtherecentapplicationsofdrowsinessdetection,and
thevalueofbothtemporalandspatialfeature-basedtechniqueswasdiscussed. Although
thenetworkcanbetrainedrelativelyquicklyusingthetemporalfeature-basedmethod,
itislessaccurate. Thespatialfeature-basedtechnique,ontheotherhand,performswell
in terms of accuracy, but lags in terms of training time, meaning that it takes longer to
trainthenetwork. Sinceprecisionandtimingarebothcrucialcomponentsinsleepiness
detection,theyhaveconcludedthatthehighestresultsindifferentresearchwereachieved
byanalyzingthespatialfeatures.
MotivatedbytheimportantroleIoTandautonomousvehiclestechnologiesplayin
intelligenttransportationsystemsnowadaysandtherequirementsofsafetyandemergency-
relatedserviceintermsoflowlatencyandhighreliability,ouraiminthisresearchisto
developaframeworkthatensuresthesafetyofpassengersbydeployingadeep-learning
modelattheedge(inavehicle)thatdetectsadrowsydriverandpropagatesthisinformation
messagewithQoSrequiredforthistypeofinformationmessagebyleveragingtheSDN
to the remote control center (RCC) to switch the autonomous vehicle to teleoperation
mode. TheSDNcorenetworksatisfiestherequiredend-to-enddelayconstraintforthis
delay-sensitiveapplicationbyexploitingtheSDNglobalviewofthenetworkconditionsto
reallocatetheavailablebandwidthamongtrafficflowsbasedonthepriorityofdifferent
trafficclasses. TheSDNcontrollercommunicateswithforwardingdevicesusingOpenFlow
protocoltobuildthisglobalview. Themaincontributionsofthisresearchareasfollows:
1. ThedeploymentoftheSoftware-DefinedNetwork(SDN)paradigmtoimplement
the5GslicingfeaturetoallowthedynamicallocationofresourcestosupporttheKey
Performance Indicators (KPIs) (e.g., low latency, low packet loss requirements) of
heterogeneousautonomousvehicleapplications.
2. TheapplicationoftheedgecomputingconceptbydeployingAItechniquesattheedge
inanautonomousvehicletoremotelymonitordriverstatusandreportcriticalcases
onlytotheRemoteControlCenter(RCC).IntegrationbetweentheAItechniquesand
edge-computingparadigmresult-inasignificantdecreaseinthebandwidthrequired.
Besides,thedeploymentoftheMECconcepttoimplementthesafetyserversandto
providefurthersupporttothedelayrequirement.
3. Thecompletepipelinestartsfromthevideostreamcapturedbythemobilephone
followingthemachine-learningstepstodeterminewhetherornotadriverisdrowsy.
Finally,employingSDNastheimplementationtechniqueof5Gslicingtoforwardthe
criticalmessageswiththerequiredlevelofQoStothecontrolcenter.
4. AvalidationoftheproposedSDN-VANETQoSframeworkusingarealisticurban
congestion scenario and performing a comparison between the adaptive and the
QoS-freeapproach.
Therestofthearticleisorganizedasfollows: Section2givesathoroughdescription
ofourintelligentandadaptiveQoSproposedframeworkaftergivingabriefreviewofcom-
municationtechnologiesdeployedinITSapplications. Section3presentstheperformance
evaluationresultsofourproposedframework. Wesummarizethefindingsofthisresearch
intheconcludingsection.

Appl.Sci.2023,13,875 4of15
2. MaterialsandMethods
Inthissection,ourproposedframeworkarchitectureisoutlined. First,communication
technologiesdeployedintheInternetofVehicles(IoV)arereviewed. Then,theproposed
frameworkarchitecturethatincludestheIoVlayer,theproposeddeeplearningmodel,the
dataplaneandthecontrolplaneconstitutingtheSDNcorenetwork,andtheQoSalgorithm
isexplained.
2.1. CommunicationTechnologies
ITSapplicationsdependonadvancedwirelesscommunicationschemes,asvehicleon-
boardunits(OBUs)areallowedtointeractwitheachother(v2V),withremotestationsand
entities(V2I)inthesamecommunicationrange,andwithroadusers(V2P)usingavailable
radiointerfaces.Morespecifically,communicationofInternetofVehicleswithinfrastructure
iscarriedoutthroughmultipleaccesstechnologies,likeIEEE802.11(Wi-Fi)customized
forvehicularconnectivityinthe5.9GHzband(theDSRC/WAVE)andmobilebroadband
technologies(e.g., 4G/LTE,5G).5Gisconsideredapromisingtechnology, asitaimsto
bearevolutionintermsofdatarates,ultra-lowlatency,massiveconnectivity,ultra-high
networkreliability,andenergyefficiencytosupportV2X(Vehicle-to-Everything)safetyand
non-safetyapplicationswiththeirdifferentrequirements. MobileEdgeComputing(MEC),
NetworkslicingandSDNaretechnologiesin5Gthataddimportantenhancementstoboth
the radio access networks (RAN) and the core networks of mobile communications [9].
Network slicing is described by [12] as an end-to-end logical network that is equipped
withacollectionofseparatedvirtualresourcesonacommonphysicalinfrastructure. These
logicalnetworksareprovidedasvariousservicestomeetthevariouscommunicationneeds
ofusers. SDNisregardedasanapproachfor5Gnetworkslicingimplementation.
2.2. ProposedModelArchitecture
Article[13]proposedahigh-levelreferencearchitectureofsoftware-definedVANETs.
The proposed architecture consists of three planes including the data plane, a control
plane, andanapplicationplane. Thedataplaneismadeupofswitches, RSUs, cellular
network nodes, and vehicular devices. The control plane includes different types of
controllers:OpenFlowcontrollersandcontrollerstailoredtoenforcethepoliciesrequiredby
theapplications.TheOpenFlowprotocolisusedbythedataplaneelementstocommunicate
withthecontrolplane. Furthermore,thecontrolplanecommunicateswiththeapplication
planeusingtheNorthboundInterface(NBI)suchasRESTAPIs.
OurproposedarchitectureisdepictedinFigure2. Thecomponentsofthisarchitecture
cooperateusing5Gslicingtechnology. Inaddition,MECtechnologyisimplementedby
connectingthesafetyserversdirectlytotheRSUs. Ourproposedframeworkismadeup
of four main modules: IoV layer, edge computing device layer, data plane and control
plane(SDNnetworkcore),andQoSapplication. TheIoVlayerconsistsofautonomous
vehiclesthatgeneratethreetypesoftraffic:trafficbelongingtothesafetyapplication,which
inourresearchisremotemonitoringanddetectionofadrowsydriverusingAImodels,
implemented on the edge computing device, infotainment traffic and best-effort traffic.
Onceadrowsydriverisdetected,amessageissenttothesafetyserver(RCC)toturnthe
vehicleintoteleoperationmode. Weevaluatetheimplementationofsafetyserversusing
theMECconcepttosupporttheultra-lowdelayrequirementofthistypeoftraffic. The
OpenFlow switches use the destination port number to classify the traffic flows. Each
switch’s meter table, which the RYU controller installed, is used to allocate bandwidth
tovarioustrafficclasses. IntheeventthatMECtechnologyisnotactive,themetertable
settingsprioritizesafetytraffictoensureprompttransmissionacrossthedataplanetothe
RCC.ThedeployedQoSmoduleisadaptiveinthatitgathersunusedbandwidthfrom
eachclassandredistributesittotheclassthatismostinneedofit,givingprecedenceto
safetytraffictoensurefewerpacketlossandloweraverageRTT.Thebandwidthneeded
to transfer the entire video of the monitored driver to the RCC and make the decision
thereisreducedwhenasleepydriverisidentifiedattheedge. Ourproposedframework

Appl.Sci.2023,13,875 5of15
architecturecomponentsareexplainedinthefollowingsubsectionsandourdesignchoices
arejustified.
Figure2.Proposedmodelarchitecture.
2.2.1. ApplicationPlane
InSDN,therearetwotypesofapplications.First,theendapplicationthatissupported
bytheinfrastructurewhich,inourproposedmodel,isswitchingtheautonomousvehicle
toteleoperationmodeupondetectionofadrowsydriver. Second,thecontrolapplication
thatspecifiesthenetworkbehavior,whichisinourproposedmodel,isgivingpriorityto
controlcommandstrafficgoingbackandforthbetweentheautonomousvehicleandthe
remotecontrolcenter(RCC)intermsofbandwidth. Inthiswork,wedeployourpreviously
proposedadaptivequalityofservicealgorithm[14]thatwastailoredtotheinvestigated
vehicularapplication.
2.2.2. DataPlane
Inour proposedmodel, thedataplane isthenetworkcorethatconsists ofasetof
interconnected OpenFlow switches (OVS-switches) and RSUs. These switches receive
forwardingrulesthatgiveprioritytovehicularapplicationsdatafromRYUcontroller.
2.2.3. ControlPlane
TheRYUcontrollerusestheOpenFlowprotocoltocommunicatewiththeOpenFlow
switches. TheRYUcontrollerwasselected,asitencompassesaseparatemoduleforQoS
andisimplementedinPythonprogramminglanguage,whichallowsrapidprototypingfor
ourproposedintelligentQoSframework[15]. Inourproposedframework,theRSUsare
SDN-enabledtoextendtheSDNcontroltowardstheOBUs. Thus,RSUsareprogrammable
bythecontroller. TheRYUcontrollerdeterminesthenetworkrulesforeachslicetofulfill
differentvehicularapplicationsKPIsandappliesthemtothedataplane. TheOpenFlow
protocolinstallstheflowentriesbetweenvehiclesandapplicationserverstomeettheITS

Appl.Sci.2023,13,875 6of15
applications’KPIs. Thenetworkpoliciesaredefinedbythecontrolapplicatio,nwhichis
themetertableconfiguredinourproposedadaptiveQoSapplication.
2.2.4. IoVLayer
TheIoV(InternetofVehicles)layerconsistsofautonomousvehiclesequippedwith
drowsinessmonitoringcamerasthatcontinuouslymonitorthedriverandproduceavideo
streamofthemonitoreddriver,whichistheinputoftheedgecomputingdevicelayerthat
implementsthedeeplearningmodel.
2.2.5. EdgeComputingDeviceLayer
TheproposedarchitectureofdriverdrowsinessdetectionandalertisshowninFigure3,
videostreamcapturingfollowedbyframeselection,facedetection,landmarksextraction,
andclassification. Ifadriver’sfaceisdiscovered,itisdetectedandcroppedfromtheimage
usingtheViola–Jones[16,17]facedetectionalgorithmbeforebeingprovidedasinputto
themachinelearningphaseasfaciallandmarks. Themachinelearningalgorithmdetects
whetherornotthedriverisclassifiedasdrowsyattheearliestframe. Theinputtothe
machinelearningmodelwillbe68faciallandmarksofthefaceprovidedbytheOpenCV
library,andeachlandmarkispresentedasanxandycoordinateintheface. Sincethisisa
real-timeapplication,themodelneedstobeverysimpleandfasttoassurethecontinuous
processingoftheframesinminimaltime. Therefore,whenchoosingthemodeltoemploy,
severalfamousarchitectureswerenotincludedbecauseoftheirlargenumberofparameters.
ConsideringtheVGG16[18]architecturewith138Mparameters,thelightestversionofthe
Efficientnet-B0[19]has5.3MparametersandtheSqueezenet[20]has421K.Ourproposed
densemodel,presentedinFigure4,requirestrainingonly5Kparametersmakingitmore
suitedtoreal-timeapplications.
Figure3.Proposedmachinelearningarchitecture.
Theparametersofthepresentedmodelwerechosenbyseveralexperimentsusinga
gridsearchtoassurethebest-chosenmodelfortheproblemaddressedhasadropoutrate
of0.2andabatchnormalizationmomentumof0.8. Themachinelearningmodelneedsto
betrainedwithseveralframeslabeledasbeingdrowsyornon-drowsy. Tobesttrainthe
modelandassureitsgeneralizationability,thedatasetissplitbyactorstomakesurethat
themodelistestedbyactorsthatwerenotpreviouslyseen. Thedatasetcontainsunequal
framesperactortakenfromtheoriginalvideodataset[21]. Theideabehindtheproposed
workistodetectdrowsinessasearlyaspossibleusingasingleframeinsteadofmultiple

Appl.Sci.2023,13,875 7of15
consecutive frames. The available dataset was then split into 10 folds for the different
experimentationeachfoldcontainsafewactorsfortrainingandothersfortesting.
Accuracy,precision,recall,andF-measurewillbeusedtoassesstheproposedidea.
Accuracy is measured by the percentage of points out of all the data points that were
successfullypredicted. Precisionandrecallaretwomeasuresthatareusedinconjunction
toevaluatehowwellsystemsperform. Precisionisdefinedasthefractionofallretrieved
instances that are relevant occurrences. Recall, also referred to as “sensitivity,” is the
proportion of retrieved instances among all relevant examples. A perfect classifier has
precision and recall that are both equal to one. The harmonic average of precision and
recallistheF-measure. Theexperimentationandresultswillbefurtherexplainedinthe
upcomingsection,namelythesplitbyactors.
Figure4.ProposedDeepLearningModel.
Anotherexperimentisalsopresentedthataimstofurtherenhancetheclassification
results,thusachievingthehighestvaluepossible. Thisapproachwillrequirethedriverto
providetwovideos,onemarkedasdrowsyandtheotherasnon-drowsy,asacalibration
step before the initiation of the program. The provided videos will help the model be
fine-tunedtothespecificfeaturesofthedriver,thusdramaticallyenhancingtheclassifica-
tionresults. Theresultswillalsobepresentedintheupcomingsectioninthetrainedwith
calibrationresults.
Inthisresearch,weemploythedatasetgeneratedby[22]fromtheArlingtonReal-Life
DrowsinessDataset(UTA-RLDD)analysisfromtheUniversityofTexasatArlington[21].
Theoriginaldatasetwasdevelopedforthemulti-stagedrowsinessdetectiontask,focusing
onbothextremeandreadilyapparentcasesofdrowsinessaswellassubtlecaseswhere
minormicro-expressionsserveasthediscriminatingcriteria. Itcanbecrucialtoidentify
thesemodestepisodesofdrowsinesstoengagedrowsinesspreventionsystemsatanearly
stage. Sincethemicro-expressionsoftirednesshavephysiologicalandinstinctiveroots,it
canbechallengingforactorstoconvincinglymimicsuchexpressionswhenactingsleepy.
3. Results
3.1. PerformanceEvaluation
MachineLearningEvaluation
Generalizedmodel: Thegeneralizedmodelwastestedusing10-foldcross-validation
andtheaverageaccuracy, precision, recallandf-measurearepresentedinTable1. The
proposed deep learning dense-based model is compared to some benchmarks, namely,

Appl.Sci.2023,13,875 8of15
Adaboost,randomforestandsupportvectorclassification. Theresultsproducedshowthat
theproposedmodelhasatleastan8%improvementintheaccuracyresultsovertheother
measureandanimprovementintheF-measureofabout3.5%.
Table1.Generalizedmodelresults.
Training Testing
Accuracy Precision Recall F-Measure Accuracy Precision Recall F-Measure
Adaboost 63.74% 81.47% 41.65% 55.12% 53.59% 67.19% 25.54% 37.01%
RandomForest 99.59% 99.58% 99.65% 99.61% 51.82% 56.28% 44.37% 49.62%
SVC 81.97% 86.55% 78.50% 82.33% 66.69% 61.21% 95.55% 74.62%
ProposedDense 97.72% 97.82% 97.93% 97.87% 74.85% 72.92% 84.26% 78.18%
Calibratedmodel:Thecalibratedmodelwastrainedontheactorsandprovidedfurther
samplesfromthetestactorstoallowthemodeltofurtherlearnthefeaturesofthedesignated
driver. Table2showstheresultsoftheproposedscenarioanditcanbeconcludedthat
thereisarounda10%improvementinaccuracyresultsbetweenthegeneralizedandthe
calibratedmodelsanda9%improvementinF1scoreresults. Furthermore,thecomparison
betweenthedensenetworkandtheotherbenchmarksshowedatleasta7%improvement
intheaccuracyresultsandanalmost8%improvementintheF1measure. Sincedrowsy
driverdetectionisacriticaldetectionproblemwithasevereriskresultinginaccidents,itis
recommendedtocalibratethemodelbeforeusetoensurebetterperformance.
Finally, a sample of the 200 epochs of training the model is presented in Figure 5.
Thechartshowsthatthemodelisnotoverfittingtothegivendatasetandthechoiceof
200epochswasenoughfortrainingthepresentedmodel.
Table2.Calibratedmodelresults.
Training Testing
Accuracy Precision Recall F-Measure Accuracy Precision Recall F-Measure
Adaboost 64.12% 80.07% 43.84% 56.66% 62.34% 68.77% 54.16% 60.60%
RandomForest 99.70% 99.71% 99.72% 99.72% 78.01% 81.93% 75.46% 78.56%
SVC 78.53% 83.26% 74.94% 78.88% 78.29% 80.26% 78.68% 79.46%
ProposedDense 98.13% 98.25% 98.25% 98.25% 85.69% 82.23% 93.37% 87.45%
Figure5.Areaunderthecurveandaccuracyresultsoftheproposeddeeplearningmodel.
3.2. Sdn-VanetQoSFrameworkEvaluation
TheperformanceevaluationoftheSDN-VANETQoSFrameworkiscarriedoutusing
Mininet-WiFiwirelessnetworkemulator[23],anOpenFlow-enablednetworkemulator
forkedfromMininettoaddwirelesschannelemulationandmobilitysupport.TheSDNcon-
trollerdeployedistheopen-sourceRYUforthejustificationgivenpreviously. Inaddition,
theSUMO(SimulationofUrbanMObility)[24]toolisused,whichisanopen-source,highly
portable,microscopicandcontinuousmulti-modaltrafficsimulationpackage—including
roadvehicles,publictransportandpedestriansdesignedtohandlelargenetworks.

Appl.Sci.2023,13,875 9of15
Theperformanceevaluationisconductedusinganurbancongestionscenariohaving
vehicularapplicationswithheterogeneousbandwidthrequirements. Ourimplementations
consider three classes of application priority: 1, 2 and 3. Class 1 is devoted to safety
applicationswithultra-lowdelayrequirements. Forthisclass,weevaluatetheimpactof
theusageofMEConperformance;oneofthe5Gfeatures.Class2isdevotedtoinfotainment
applicationwhichismoredelaytolerant. Class3isreservedforbest-effortapplications
thatdon’thaveanypriorityorspecificrequirements. Inourimplementationenvironment,
thecontrollerhastodelaytherunoftheadaptivecomponentofthecontrolapplication
beforerecalculatingthebandwidthassignedforeachmeteraccordingtotheassociation
timeoutoccurringwhenthevehiclechangestheRSUs.
PerformanceMetrics
ToassesstheperformanceofthesuggestedSDN-VANETQoSFramework,thefollow-
ingperformancemetricswillbedeployed: averagethroughputofdatabetweenvehicles
andapplicationsserversandaverageroundtriptime(RTT).TheRTTcanbedefinedasthe
timetakenbythemessagesentbythesourcevehicleuntilreceivingaresponsefromthe
receivingapplicationserver.
3.3. EvaluationScenario1
In this scenario, the configuration deployed in [9] is used. This configuration was
generatedbytheSUMOurbanmobilitysimulator,tosimulatevariouslevelsofcongestion
overtime. Inthisconfiguration,onehundredandfifty-eightvehiclesmoveinthe650mof
anurbanroadinManhattan(NYC).TheMininet-WiFiemulatorandtheSUMOsimulator
wereintegratedtoimplementmobility. Toevaluateourproposedframework,inthissce-
nario42vehiclesoutofthe158vehiclesgeneratetrafficbelongingtodifferentapplications
simultaneously,whereas26vehiclesgeneratetrafficforsafetyapplications. Thisscenario
representsahigh-trafficscenariotostudytheimpactofahighlevelofinterferenceonour
proposedframework. Theparametersusedintheperformanceevaluationaresummarized
inTable3. Figure6depictsthenetworksetupusedinsimulationincaseofapplyingthe
MECconcepttosupportsafetyapplicationsprerequisitesintermsofultra-lowdelayand
withoutapplyingtheMECconcept. ThevaluesofRTTarecalculatedusingthe“PING”
ICMP messages. Table 4 illustrates the average RTT results in the case of applying our
proposed Adaptive Quality of Service (AQoS) algorithm and in the case of a QoS-free
modelinthishigh-levelinterferencescenario. Ouralgorithmachievesanimprovementof
upto74.63%intermsofaverageRTTinthecaseofsafetyapplicationsandupto90.88%
in the case of infotainment applications. The high improvement in average RTT in the
caseofinfotainmentastheinfotainmentapplicationshaveapriorityclass2andareas-
signedabandwidthgreaterthanthebesteffortclassandincaseofthisclassishungry
forbandwidth,itcollectsthefreebandwidthfromotherclasses. Ontheotherhand,the
improvementinsafetyapplicationsislessasinbothcasesthesafetyserversareconnected
directlytoRSUsapplyingtheMECconceptof5Gtosupportultra-lowdelayapplication.
Moreover,resultsrevealedthattheusageofMECtechnologyimprovestheaverageRTTby
upto98.09%. Finally,withoutapplyingtheMECtechnologyandmovingsafetyserversto
theSDNnetworkcore,ourproposedAQoSstillimprovestheperformancebyupto64%
comparedtotheQoS-freemodel.

Appl.Sci.2023,13,875 10of15
(a)WithoutMEC (b)UsingMEC
Figure6.Simulationnetworksetupsusedinevaluationscenarios.
Table3.Parametersusedintheperformanceevaluationscenarios.
|                               | Parameter     |     |     | Value       |     |     |
| ----------------------------- | ------------- | --- | --- | ----------- | --- | --- |
| NumberofVehicles              |               |     |     | 158         |     |     |
| NumberofRSUs                  |               |     |     | 3           |     |     |
|                               | RSUsRange     |     |     | 250m        |     |     |
| NumberofSwitches(CoreNetwork) |               |     |     | 6           |     |     |
| PropagationModel              |               |     |     | LogDistance |     |     |
| RANMACLayer                   |               |     |     | IEEE802.11g |     |     |
| NumberofApplicationsTypes     |               |     |     | 3           |     |     |
|                               | EmulationTime |     |     | 300s        |     |     |
Table4.Averageroundtriptimeresultsforallmodelsincaseofhightrafficscenario.
| Model     |     | Application        | MinimumRTT |     | AverageRTT |     |
| --------- | --- | ------------------ | ---------- | --- | ---------- | --- |
| MEC(AQoS) |     | SafetyApplications | 1.146ms    |     | 73.46ms    |     |
Infotainment
| MEC(AQoS) |     |     | 6.93ms |     | 3061.63ms |     |
| --------- | --- | --- | ------ | --- | --------- | --- |
Applications
| MEC(QoS-Free) |     | SafetyApplications | 6.945ms |     | 289.56ms |     |
| ------------- | --- | ------------------ | ------- | --- | -------- | --- |
Infotainment
| MEC(QoS-Free) |     |     | 16,133.43ms |     | 33,570.39ms |     |
| ------------- | --- | --- | ----------- | --- | ----------- | --- |
Applications
| NoMEC(AQoS)     |     | SafetyApplications | 4.82ms    |     | 3849.49ms |     |
| --------------- | --- | ------------------ | --------- | --- | --------- | --- |
| NoMEC(QoS-Free) |     | SafetyApplications | 2475.84ms |     | 6878.73ms |     |
3.3.1. EvaluationScenario2
Inthisscenario,45vehiclesoutofthe158vehiclesgeneratetraffic,where15vehicles
generatesafetyapplicationstraffic,15vehiclesgenerateinfotainmentapplicationstraffic
and15vehiclesgeneratebest-efforttraffic. Table5summarizesthecharacteristicsofdiffer-
entapplications. Figures7–10illustratethethroughputresultsforallapplicationservers.
Theresultsrevealedanaverageaggregatethroughputof2.05Mbpsforallinfotainment
trafficincaseofapplyingourproposedAQoSalgorithmagainst1.45MincaseofQoS-
free model showing an improvement of 29.27%, once again due to reassigning the free
bandwidthtoinfotainmenttraffic. Theaveragethroughputofsafetyapplicationsisnot
improvedassafetyserversareconnecteddirectlytoRSUsindependentoftheimplemented
algorithmsincethetrafficdoesnotgothroughthenetworkcore.
Table5.Applicationcharacteristics.
|              |              | DataRate |          |      |     | Priority |
| ------------ | ------------ | -------- | -------- | ---- | --- | -------- |
| Applications | Use          |          | Protocol | Port |     |          |
|              |              | KPI      |          |      |     | Class    |
| S            | Safety       | 0.5Mbps  | UDP      | 5002 |     | 1        |
| IF           | Infotainment | 1.5Mbps  | UDP      | 5003 |     | 2        |
| BE           | Best-Effort  | 0.5Mbps  | UDP      | 5004 |     | 3        |

Appl.Sci.2023,13,875 11of15
(a)AQoS (b)QoS-Free
Figure7. Averagethroughputresultsforbothapproaches: AQoSandQoS-freeofScenario2for
SafetyServer1.
(a)AQoS (b)QoS-Free
Figure8. Averagethroughputresultsforbothapproaches: AQoSandQoS-freeofScenario2for
SafetyServer2.
(a)AQoS (b)QoS-Free
Figure9. Averagethroughputresultsforbothapproaches: AQoSandQoS-freeofscenario2for
InfotainmentServere.
(a)AQoS (b)QoS-Free
Figure10. Averagethroughputresultsforbothapproaches: AQoSandQoS-freeofScenario2for
InfotainmentServere2.

Appl.Sci.2023,13,875 12of15
3.3.2. EvaluationScenario3
Figures11–15showsthethroughputincaseofmovingthesafetyserverstobecon-
nected to the network core (SW5). The results show an average aggregate throughput
of1.251MbpsforallsafetytrafficinthecaseofapplyingourproposedAQoSalgorithm
against1.01MbpsinthecaseofaQoS-freemodelwithanimprovementofupto19.26%.
Moreover,theresultsrevealedanaverageaggregatethroughputof2.18Mbpsforallinfo-
tainmenttrafficinthecaseofapplyingourproposedAQoSalgorithmversus1.13Mbpsin
thecaseofQoS-freemodelwithanimprovementofupto48.17%.
(a)AQoS (b)QoS-Free
Figure11. Averagethroughputresultsforbothapproaches: AQoSandQoS-freeofScenario3for
SafetyServer1.
(a)AQoS (b)QoS-Free
Figure12. Averagethroughputresultsforbothapproaches: AQoSandQoS-freeofScenario3for
SafetyServer2.
(a)AQoS (b)QoS-Free
Figure13. Averagethroughputresultsforbothapproaches: AQoSandQoS-freeofScenario3for
SafetyServer3.

Appl.Sci.2023,13,875 13of15
(a)AQoS (b)QoS-Free
Figure14. Averagethroughputresultsforbothapproaches: AQoSandQoS-freeofScenario3for
InfotainmentServere.
(a)AQoS (b)QoS-Free
Figure15. Averagethroughputresultsforbothapproaches: AQoSandQoS-freeofScenario3for
InfotainmentServere2.
4. Conclusions
In this work, we proposed a framework that integrates 5G technologies (network
slicing, MEC, SDN) with deep learning models to support safety applications in IoV.
RemotedrivermonitoringtodetectdrowsydriversusingAImodelsandswitchingthe
vehicleintoteleoperationmodewasourdeployedcasestudy. Evaluationoftheproposed
SDN-VANET QoS-based model showed significant improvements in terms of average
RTTandaveragethroughputinallscenariosinvestigated. Thisisduetovariousreasons.
First,theapplicationof5Gtechnologies,namely;MECandnetworkslicing. Secondly,the
integrationofthedeep-learningmodelwithSDNreducesthebandwidthrequiredsince
onlycriticalcasesarereportedtotheRCC.Finally,deployingtheSDNparadigmallowed
thesuccessoftheadaptationphaseofthealgorithmasaresultoftheglobalviewofnetwork
conditionstheSDNparadigmoffers. Furthermore,theproposedworkhaspresenteda
machinelearningarchitecturethatwouldextractfaciallandmarkspervideoframeand
theninputittoadensedeeplearningmodeltodetectwhetherornotthedriverisdrowsy
andaccordinglyreporttothecontrolroom. Theproposeddensemodelwascompared
tobenchmarksandprovidedanimprovementintermsofaccuracy,precision,recalland
F-measure. Inthefuture,inthecontextofSDN,wewillexploreiftheusageofhierarchical
controllerswillimproveperformanceandwillgivemoresupporttotherequirementsof
safetyapplicationsbymakingeachcontrollerresponsibleforapartoftheRAN.
AuthorContributions:Conceptualization,S.N.S.andC.F.;methodology,S.N.S.andC.F.;software,
S.N.S.andC.F.;validation,S.N.S.andC.F.;formalanalysis,S.N.S.andC.F.;investigation,S.N.S.and
C.F.;resources,S.N.S.andC.F.;writing—originaldraftpreparation,S.N.S.andC.F.;writing—review
andediting,S.N.S.andC.F.;visualization,S.N.S.andC.F.;projectadministration,C.F.Allauthors
havereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement: Notapplicable.

Appl.Sci.2023,13,875 14of15
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:https:\sites.google.com/view/utarldd/home(accessedon1Decem-
ber2022)andhttps:\www.kaggle.com/datasets/ismailnasri20/driver/-drowsiness/-dataset-ddd
(accessedon1December2022).
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
AI ArtificialIntelligence
API ApplicationProgrammingInterface
AVs AutonomousVehicles
ICMP InternetControlMessageProtocol
IoT InternetofThings
IoV InternetofVehicles
ITS IntelligentTransportationSystems
KPI KeyPerformanceIndicator
MEC MobileEdgeComputing
NBI NorthBoundInterface
NHTSA NationalHighwayTrafficSafetyAdministration
QoS QualityofService
RAN RadioAccessNetwork
RCC RemoteControlCenter
RSU RoadSideUnit
SDN SoftwareDefinedNetworks
SUMO SimulationofUrbanMObility
V2I VehicletoInfrastructure
V2P VehicletoPerson
V2X VehicletoEverything
V2V VehicletoVehicle
VANET VehicularAdhocNetworks
References
1. Placek, M. Autonomous Car Market Size Worldwide 2021–2026. Report, March 2021. Available online: https://www.
researchandmarkets.com/reports/5359435/global-autonomous-cars-market-2021-2026-by(accessedon1December2022).
2. Law,C. TheDangersofDriverlessCars. Natl.LawRev.2022,XII.Availableonline:https://www.natlawreview.com/article/
dangers-driverless-cars(accessedon30November2022).
3. Feiler,J.;Hoffmann,S.;Diermeyer,F. ConceptofaControlCenterforanAutomatedVehicleFleet. InProceedingsofthe2020
IEEE23rdInternationalConferenceonIntelligentTransportationSystems,ITSC2020,Rhodes,Greece,20–23September2020.
[CrossRef]
4. Kaur,K.;Garg,S.;Kaddoum,G.;Kumar,N.;Gagnon,F. SDN-BasedInternetofAutonomousVehicles: AnEnergy-Efficient
ApproachforControllerPlacement. IEEEWirel.Commun.2019,26,72–79.[CrossRef]
5. Kreutz, D.; Ramos, F.M.V.; Veríssimo, P.E.; Rothenberg, C.E.; Azodolmolky, S.; Uhlig, S. Software-Defined Networking:
AComprehensiveSurvey. Proc.IEEE2015,103,14–76.[CrossRef]
6. Karakus,M.;Durresi,A. QualityofService(QoS)inSoftwareDefinedNetworking(SDN):Asurvey. J.Netw.Comput.Appl.2017,
80,200–218.[CrossRef]
7. Mahi,M.J.N.;Chaki,S.;Ahmed,S.;Biswas,M.;Kaiser,M.S.;Islam,M.S.;Sookhak,M.;Barros,A.;Whaiduzzaman,M. AReview
onVANETResearch:PerspectiveofRecentEmergingTechnologies. IEEEAccess2022,10,65760–65783.[CrossRef]
8. Storck, C.R.; Duarte-Figueiredo, F. A5GV2Xecosystemprovidinginternetofvehicles. Sensors(Switzerland)2019, 19,550.
[CrossRef]
9. DoValeSaraiva,T.;Campos,C.A.V.;Fontes,R.D.R.;Rothenberg,C.E.;Sorour,S.;Valaee,S. AnApplication-DrivenFramework
forIntelligentTransportationSystemsUsing5GNetworkSlicing. IEEETrans.Intell.Transp.Syst.2021,22,5247–5260.[CrossRef]
10. Pandey,N.N.;Muppalaneni,N.B. Temporalandspatialfeaturebasedapproachesindrowsinessdetectionusingdeeplearning
technique. J.-Real-TimeImageProcess.2021,18,2287–2299.[CrossRef]
11. Pandey,N.N.;Muppalaneni,N.B. Asurveyonvisualandnon-visualfeaturesinDriver’sdrowsinessdetection. Multimed.Tools
Appl.2022,2022,1–41.[CrossRef]

Appl.Sci.2023,13,875 15of15
12. Li,X.;Samaka,M.;Chan,H.A.;Bhamare,D.;Gupta,L.;Guo,C.;Jain,R. NetworkSlicingfor5G:ChallengesandOpportunities.
IEEEInternetComput.2018,21,20–27.[CrossRef]
13. DosReisFontes, R.; Campolo, C.; EsteveRothenberg, C.; Molinaro, A. Fromtheorytoexperimentalevaluation: Resource
managementinsoftware-definedvehicularnetworks. IEEEAccess2017,5,3069–3076.[CrossRef]
14. Fathy,C.;Saleh,S.N. IntegratingDeepLearning-BasedIoTandFogComputingwithSoftware-DefinedNetworkingforDetecting
WeaponsinVideoSurveillanceSystems. Sensors2022,22,5075.[CrossRef][PubMed]
15. Ryu. RyuDocumentation.2016. p.490.Availableonline:https://media.readthedocs.org/pdf/ryu/latest/ryu.pdf(accessedon
30November2022).
16. Viola,P.;Jones,M. Rapidobjectdetectionusingaboostedcascadeofsimplefeatures. InProceedingsofthe2001IEEEComputer
SocietyConferenceonComputerVisionandPatternRecognition,CVPR2001,Kauai,HI,USA,8–14December2001;Volume1,
p.I.
17. Viola,P.;Jones,M. Robustreal-timeobjectdetection. Int.J.Comput.Vis.2001,4,4.
18. Simonyan,K.;Zisserman,A. Verydeepconvolutionalnetworksforlarge-scaleimagerecognition. arXiv 2014,arXiv:1409.1556.
19. Tan,M.;Le,Q. Efficientnet:Rethinkingmodelscalingforconvolutionalneuralnetworks. InProceedingsoftheInternational
ConferenceonMachineLearning,PMLR,LongBeach,CA,USA,9–15June2019;pp.6105–6114.
20. Iandola,F.N.;Han,S.;Moskewicz,M.W.;Ashraf,K.;Dally,W.J.;Keutzer,K. SqueezeNet:AlexNet-levelaccuracywith50xfewer
parametersand<0.5MBmodelsize. arXiv 2016,arXiv:1602.07360.
21. Ghoddoosian,R.;Galib,M.;Athitsos,V. Arealisticdatasetandbaselinetemporalmodelforearlydrowsinessdetection. In
ProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognitionWorkshops,LongBeach,CA,USA,16–17
June2019.
22. Nasri,I.;Karrouchi,M.;Snoussi,H.;Kassmi,K.;Messaoudi,A. DetectionandPredictionofDriverDrowsinessforthePrevention
ofRoadAccidentsUsingDeepNeuralNetworksTechniques.InWITS2020;Springer:Singapore,2022;pp.57–64.
23. Fontes, R.R.; Afzal, S.; Brito, S.H.B.; Santos, M.A.S.; Rothenberg, C.E. Mininet-WiFi: EmulatingSoftware-DefinedWireless
Networks.InProceedingsofthe 201511thInternationalConferenceonNetworkandServiceManagement(CNSM),Barcelona,
Spain,9–13November 2015;pp.384–389.
24. Lopez,P.A.;Behrisch,M.;Bieker-Walz,L.;Erdmann,J.;Flötteröd,Y.P.;Hilbrich,R.;Lücken,L.;Rummel,J.;Wagner,P.;Wießner,E.
MicroscopicTrafficSimulationusingSUMO.InProceedingsofthe21stIEEEInternationalConferenceonIntelligentTransportation
Systems,Maui,HI,USA,4–7November2018.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.