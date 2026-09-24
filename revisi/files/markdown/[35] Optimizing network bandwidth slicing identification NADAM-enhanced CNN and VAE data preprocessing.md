# [35] Optimizing network bandwidth slicing identification NADAM-enhanced CNN and VAE data preprocessing

> Source file: `[35] Optimizing network bandwidth slicing identification NADAM-enhanced CNN and VAE data preprocessing.pdf`

---

ID:pone.0333286 — 2025/10/16 — page 1 — #1
PLOS ONE
RESEARCHARTICLE
Optimizing network bandwidth slicing
identification: NADAM-enhanced CNN and
VAE data preprocessing for enhanced
interpretability
Md.FahimUlIslam1,ShahriarHossain 1 ,Md.GolamRabiulAlam 1 ,
NafeesMansoor 2 ,AmitabhaChakrab arty 1 ∗
1DepartmentofComputerScienceandEngineering,BRACUniversity,Dhaka,Bangladesh,
2DepartmentofComputerScienceandEngineering,UniversityofLiberalArtsBangladesh(ULAB),
Dhaka,Bangladesh
∗amitabha@bracu.ac.bd
Abstract
Communicationnetworksofthefuturewillrelyheavilyonnetworkslicing(NS),atechnol-
OPENACCESS
ogythatenablesthecreationofdistinctvirtualnetworkswithinasharedphysicalinfras-
Citation:IslamMFU,HossainS,AlamMGR, tructure.Thiscapabilityiscriticalformeetingthediversequalityofservice(QoS)require-
MansoorN,ChakrabartyA(2025)Optimizing
mentsofvariousapplications,fromultra-reliablelow-latencycommunicationstomassive
networkbandwidthslicingidentification:
IoTdeployments.Toachieveefficientnetworkslicing,intelligentalgorithmsareessen-
NADAM-enhancedCNNandVAEdata
preprocessingforenhancedinterpretability. tialforoptimizingnetworkresourcesandensuringQoS.ArtificialIntelligence(AI)models,
PLoSOne20(10):e0333286. particularlydeeplearningtechniques,haveemergedaspowerfultoolsforautomating
https://doi.org/10.1371/journal.pone.0333286
andenhancingnetworkslicingprocesses.Thesemodelsareincreasinglyappliedinnext-
Editor:Yang(Jack)Lu,BeijingTechnologyand generationmobileandwirelessnetworks,including5G,IoTinfrastructure,andsoftware-
BusinessUniversity,CHINA
definednetworking(SDN),toallocateresourcesandmanagenetworkslicesdynami-
Received:October16,2024 cally.Inthispaper,weproposeanInterpretableNetworkBandwidthSlicingIdentification
Accepted:September11,2025 (INBSI)systemthatleveragesamodifiedConvolutionalNeuralNetwork(CNN)archi-
tecturewithNesterov-acceleratedAdaptiveMomentEstimation(NADAM)optimization.
Published:October21,2025
Additionally,weuseaVariationalAutoencoder(VAE)forpreprocessinginitialdata,along
Copyright:©2025 Islametal.Thisisanopen
withreconstructeddatafordatavalidityassessment.Themodelweproposeoutperforms
accessarticledistributedunderthetermsofthe
CreativeCommonsAttributionLicense,which otheralternativesandreachesanaccuracypeakof(84%)inthesystemenvironment.A
permitsunrestricteduse,distribution,and rangeofaccuracywasachievedby(k-nearestneighborsalgorithm)KNN(76%),Ran-
reproductioninanymedium,providedthe
domForest(69%),BaggingClassifier(70%),andGaussianNaiveBayes(GaussianNB)
originalauthorandsourcearecredited.
(55%).Theaccuracyofadditionalmethodsvaries,includingDecisionTrees,AdaBoost,
Dataavailabilitystatement:Allrelevantdata
DeepNeuralForest(DNF),andMultilayerPerceptrons(MLPs).WeutilizetwoeXplain-
areavailableat:AnuragThantharate,Cory
Beard,RahulParopkari,VijayWalunj, ableArtificialIntelligence(XAI)approaches,ShapleyAdditiveExplanations(SHAP)
“CRAWDADumkc/networkslicing5g”,IEEE andLocalInterpretableModel-AgnosticExplanations(LIME),toprovideinsightintothe
Dataport,December8,2022,
impactofcertaininputcharacteristicsonthenetworkslicingprocess.Ourworkhighlights
doi:10.15783/k0w0-js18.
thepotentialofAI-drivensolutionsinnetworkslicing,offeringinsightsforoperatorsto
Funding:Theauthor(s)receivednospecific
optimizeresourceallocationandenhancefuturenetworkmanagement.
fundingforthiswork.
Competinginterests:Theauthorshave
declaredthatnocompetinginterestsexist.
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 1/38

ID:pone.0333286 — 2025/10/16 — page 2 — #2
PLOS One Optimizingnetworkbandwidthslicingidentification
1 Introduction
Inrecentyears,wirelesscommunicationsystemshaveundergoneremarkableadvancements,
drivenbytheever-increasingdemandforfaster,morereliable,andefficientconnectivity.The
deploymentoffifth-generation(5G)networkshasalreadyrevolutionizedthetelecommuni-
cationslandscape,enablinghigh-resolutiondatastreaming(suchas4Kand8K),autonomous
operations,telemedicine,smartcities,andimmersivetechnologieslikeaugmentedreality
(AR)andvirtualreality(VR)[1,2].However,astheworldmovestowardthefifth-generation
(5G)andbeyondera,theexpectationsforwirelesscommunicationsystemshavegrowneven
further.5Gaimstopushtheboundariesofconnectivitybyreducingend-to-endlatency,
increasingdataspeeds,enhancingreliability,andcreatingavastnetworkofinterconnected
devices.
Despitethesignificantprogressmadeby5G,severalchallengesremain.Forinstance,while
5Gnetworksachievepeakdataspeedsofupto10Gbpsandlatencyaslowas1ms,theystill
struggletomeetthediverseandsmoothquality-of-service(QoS)requirementsofemerging
applications[3,4,52].Moreover,traditionalnetworkarchitecturesareofteninadequatefor
handlingthedynamicandcomplexdemandsofmoderncommunicationsystems.Thishas
ledtotheexplorationofinnovativesolutionssuchasnetworkslicing,whichallowsforthe
creationofvirtualized,dedicatednetworkresourcestailoredtospecificapplicationsoruser
groups.Fig1showsthegeneralnetworkslicingarchitecture.Byleveragingtechnologieslike
software-definednetworking(SDN)andnetworkfunctionvirtualization(NFV),networkslic-
ingenablestheefficientallocationofresources,improvedscalability,andenhancedservice
customization[5–8].Fig1referstothecomparisonwithothernetworks.
Therefore,networkslicingisanessentialtechnologyenablingoperatorstogenerate
variousvirtualized“slices”onacommonphysicalnetworkinfrastructure[18].Eachsliceis
tailoredtoaddressparticularapplicationrequirements,guaranteeingefficientresourceuti-
lization,scalability,andenhancedqualityofservice(QoS).Forinstance,theenhancedmobile
broadband(eMBB)slicedelivershigh-speeddataforbandwidth-heavyapplicationslikeAR
andVR,whilethemassivemachine-typecommunications(mMTC)sliceconnectsbillions
Fig1.Networkslicingarchitecture.
https://doi.org/10.1371/journal.pone.0333286.g001
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 2/38

ID:pone.0333286 — 2025/10/16 — page 3 — #3
PLOS One Optimizingnetworkbandwidthslicingidentification
ofIoTdevicesinsmartcityscenariossuchasenvironmentalmonitoringandsmarthomes.
Similarly,theultra-reliablelow-latencycommunication(URLLC)sliceprovidesultra-low
latencyforcriticalapplicationslikeautonomousvehiclesandremotesurgery.Nevertheless,
conventional5Gnetworkslicingispredominantlystatic,featuringpre-establishedslicesthat
cannotadjustinrealtimetofluctuatingtrafficrequirements[19].Thisrigiditymayleadto
performancecomplications,suchasoverburdeninganeMBBsliceduringanabruptAR/VR
trafficsurgeorinadequatelyreallocatingresourcesforlatency-sensitiveoperations.Asa
result,staticnetworkslicingfrequentlyresultsininferiorperformanceanduserexperiences,
particularlyindynamicandessentialsituations.
Toaddressthesechallenges,5Gintroducesdynamicnetworkslicing,enablingreal-time
adjustmentstonetworkslicesbasedonevolvingapplicationneeds[20].Dynamicslicing
persistentlyobservesandreallocatesresourcesinreactiontofluctuatingtrafficpatterns,guar-
anteeingoptimalnetworkperformanceandconsistentSLAadherenceforvariousapplica-
tionssuchasautonomousapplications,high-bandwidthholographiccommunication,and
ultra-denseIoTdeployments.Therefore,networksliceidentification(NSI),whichcategorizes
incomingtrafficflowsandassignsthemtotheappropriateslicebasedtheapplicationrequire-
ments[21].Forexample,autonomouscardataissenttotheURLLCsliceforlow-latency
communication,IoTsensordataissenttothemMTCsliceforvastconnectivity,andAR/VR
applicationsaredirectedtotheeMBBsliceforhigh-bandwidthstreaming.
However,theimplementationofnetworkslicingin5Gandbeyondpresentssignificant
challenges,particularlyinanomalydetection,dataintegrity,andresourceoptimization.
Besides,effectivedecision-makingreliesonkeyparameterssuchasqualityofservice(QoS)
andpacketlossrate,whichplayacrucialroleinmaintainingnetworkperformanceandeffi-
ciency.Existingsolutionsoftenfailtoadequatelyaddresstheseissues,astheycannotdetect
anomaliesinrealtime,ensuredataintegrity,andprovideinterpretableinsightsintonetwork
behavior.Furthermore,whilemachinelearning(ML)techniqueshavebeenwidelyadopted
tooptimizenetworkperformance,theirapplicationinnetworkslicingremainslimited.The
adoptionofAIinnetworkslicingfacesthreemajorchallenges:inefficientresourceallocation,
lackofinterpretability,andsecurityvulnerabilities.TraditionalMLmodelsoftenstruggleto
dynamicallyallocateresources,leadingtoQoSviolationsinreal-timenetworkmanagement.
Additionally,theselearning-basedslicingmodelsoftenfunctionasblackboxes,makingit
difficulttointerprethowslicesareassignedandadjusted.Furthermore,networkslicingintro-
ducessecurityriskssuchasDDoSattacksandunauthorizedaccess,whicharechallengingto
detectinrealtime.
Toaddressthesechallenges,ourstudyproposesanovelapproachthatcombinesanomaly
detection,datareconstruction,andinterpretableAImodelstooptimizenetworkslicing
in5Gcommunications.Specifically,weintroducetheuseofvariationalautoencoders
(VAEs)foranomalydetectionanddatareconstruction,enablingtheidentificationofprevi-
ouslyunknownnetworkdynamicsandensuringdataintegrity.Additionally,weproposea
lightweightconvolutionalneuralnetwork(CNN)modeloptimizedwiththeNADAMalgo-
rithm,whichisdesignedforefficientfeatureextraction,reducedoverfitting,andoptimal
performanceonresource-constraineddevices.Toimprovetransparencyandensureaccurate
decision-making,wefurtherintegrateexplainableAItechniques,includingSHAP(SHapley
AdditiveexPlanations)andLIME(LocalInterpretableModel-agnosticExplanations).These
methodsoffervaluableinsightsintohowourmodelsmakedecisions,enhancinginterpretabil-
ityandtrustintheslicingprocess.
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 3/38

ID:pone.0333286 — 2025/10/16 — page 4 — #4
PLOS One Optimizingnetworkbandwidthslicingidentification
Thecontributionsofthispaperareasfollows:
• Tothebestofourknowledge,thisisthefirststudytoextensivelyutilizeVAEsinnet-
workslicingconfigurationsforanomalydetectionanddatareconstructionin5G
communications.
• WeevaluatesixclassicalMLmodels(KNN,RandomForest,DecisionTree,GaussianNB,
BaggingClassifier,AdaBoost)andtwoDLmodels(DeepNeuralForest,MLP),andpro-
posealightweightCNNmodelwithNADAMoptimizationforsuperiorperformanceand
efficiencyinresource-constrainedenvironments.
• WeintroduceSHAPandLIMEtointerprettheresultsoftheXGBClassifierandMLP
models,enhancingthetransparencyandpracticalapplicabilityofourapproachin5Gand
6Gscenarios.
• WeassesstheefficiencyofourmodelsusingmetricssuchasMeanSquaredError(MSE),
MeanAbsoluteError(MAE),accuracycurves,losscurves,confusionmatrices,andclassifi-
cationreports,demonstratingthesuperiorityofourproposedframeworkinnetworkslicing
scenarios.
Theremainderofthispaperisorganizedasfollows.Sect2providesanoverviewofnet-
workslicingandrelatedworksinthisdomain.Sect3presentsourproposedapproachfor
effectivenetworkslicing.Sect4describestheimplementationandevaluationtechniquesused
inthisstudy.Sect5analyzestheresultsandinsightsobtainedfromourexperiments.Sect6
developsausecaseforourmodelindifferentapplications.Finally,Sect7concludesthepaper
anddiscussesfuturedirections.
Byaddressingthelimitationsofexistingsolutionsandintroducinginnovativetech-
niquesforanomalydetection,datareconstruction,andinterpretableAI,thisresearchaims
toenhancethequalityofservice(QoS)anduserexperience(QoE)in5Gand6Gnetworks,
pavingthewayformoreefficientandreliablewirelesscommunicationsystems.Table1shows
acomparisonbetween5Gandothernetworks.
2 Literature review
Intherealmofnetworkslicing,whereSDNandNFVplayapivotalrole,extensiveresearch
effortshavebeenundertakentoachieveoptimalslicingsolutionsthatcatertothediverse
needsofvariousapplicationsandserviceswithin5Gand6Gnetworks.Inthissection,we
presentastructuredoverviewoftheavailableliterature,withaprimaryemphasisonresearch
contributionsrelevanttotheimplementationofnetworkslicingthroughtheutilization
ofSDNandNFVtechnologies.ItisimportanttoemphasizethatMLandDLapproaches
representarelativelynovelandinnovativeapproachwithinthissector,introducingafresh
viewpointtothediscipline.
Robertetal.[9]offeredanovelapproachforlow-latencynetworkslicing.Theyadapted
theA∗methodtoaddQoSparametersandoutperformedDijkstra’salgorithmwitha
Table1.Comparisonof5Gandothernetworks.
Aspect 5G 6G
Peakdatarate 10Gbps 1Tbps
Frequency 3–300GHz 1000GHz
Latency 10ms lessthan1ms
Mobilitysupport Upto500km/h Upto1000km/h
Spectralefficiency 30-40bps/Hz 100bps/Hz
https://doi.org/10.1371/journal.pone.0333286.t001
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 4/38

ID:pone.0333286 — 2025/10/16 — page 5 — #5
PLOS One Optimizingnetworkbandwidthslicingidentification
precalculatedheuristicfunctionandreal-timecongestionmanagement.Theapproachwas
includedinanSDNmoduletermedaroutecomputationelementforoptimizingnetworkslice
pathways.It’svitaltonotethatthispaperdidnotbuildadataanomalydetectionoranauto-
matedcomputationalclassifier/predictoralgorithm.However,itisimportanttoinvestigate
theproblemforefficientslicedistribution.
Numerousresearchworkshaveaddressedthetheoreticaltopicofferedhere.Whilenet-
workslicingiscommonlyconductedinanorthogonalmultipleaccess(OMA)fashion,Yuan-
wenetal.[10]divesintothepossibilitiesofrate-splittingmultipleaccess(RSMA),enabling
improvedflexibilityandsuperiordataratecapabilities.RSMAcanoutperformbothOMAand
non-orthogonalmultipleaccess(NOMA),renderingitaviablesolutionfornetworkslicing
acrossvariedregions.Besides,Asmaaetal.[11]analyzestheintegrationofnetworkslicing
intocooperativeNOMA-basedsystemswithunderlaydevice-to-device(D2D)connections.
Theresearchestablishesanoptimizationissuethatseekstoincreasesystemthroughputwhile
meetingslicerequirements.Byadoptingatwo-stageresourceallocationtechniquebasedon
theswapping-basedmatchinghypothesis,whatissuggestedregularlysurpassesotherswhen
itcomestobothsystemthroughputandthenumberofenabledD2Dpairs.However,itis
crucialtohighlightthatthisstudy,althoughofferingsimulateddata,doesnotofferareal-
timeexecutionofitsproposedtechniques.Consequently,itisessentialtoaddresstheactual
executionofthisworkataproductionlevel,particularlyonedgedevices,whileassuringthe
preservationofdataprivacy.
ThisstudybyGharehgolietal.[12]highlightsnetworkslicinginthecontextof5Gand
beyond,addressinginformationambiguity,includingdemandissues.Itemploysdeeprein-
forcementlearning(DRL)foroptimizingresourceallocationforcommunicationservices.
Additionally,Guptaetal.[13]investigatednetworkslicinginaradioaccessnetworkwith
industrialInternetofthings(IIoT)devicessharinginfrastructure.Itutilizeddeepreinforce-
mentlearningforresourceorchestrationtomeetvaryingservicedemands.Thestudyconcen-
tratedonreasoningdecisionobjectives,suchasmaximizingsystemefficiency,spectraleffec-
tiveness,agreementsonservicelevels,packetrate,andminimizingpowerconsumptionand
transmissionlatency.Itleveragedgenerativeadversarialnetwork-baseddeepdistributional
noisyQ-networks(GAN–NoisyNet)andintroducedduelingGAN–NoisyNettoimprovethe
makingofdecisions.However,it’sworthtakingintoaccountthatthestudydoesnothigh-
lightinterpretablenetworksliceallocationorexplanationsofAIconcepts,whicharealso
significantconcerns.
Furthermore,tomaketheslicemoredistributed,automatedsystemshavebeenproposed
inmanystudies.Toboostservicequalityandoptimizenetworkslicing,Dangietal.[14]inte-
gratedartificialintelligenceandMLapproaches.Themethodologyinvolvedthreeessential
phases:datasetloading,hyperparameteroptimizationusingharmonysearchoptimization
(HHO),andnetworksliceclassificationwithahybridDLmodel,combiningHHO,CNN,and
longshort-termmemory(LSTM).ThisapproachsoughttoincreaseQoSandnetworkslicing
efficiency.Furthermore,thestudyattemptedtobridgethegapinNSarchitecturesbypresent-
ingtheslicingfutureinternetinfrastructures(SFI2)architecture.Thisuniquestrategyempha-
sizestheintegrationofexperimentalnetworksandincorporatesMLfornativeoptimizations,
energy-efficientslicing,andsecuritysuitedtoNS.Jobertoetal.[15]utilizedMLapproachesto
optimizeallphasesofnetworkslicing,fromorchestratingtoresourceprediction.Particularly,
itfocusedonresourceallocationstrategies,increasingsustainability,andreducingenergy
consumptionduringvariousphasesofthenetworkslicelifespan.However,itisimperativeto
highlightthatthemodellacksapriorityapproachinidentifyingthenetworkfunctionsthat
contributemostefficientlytoslicedistributionandingeneratingreconstructeddatatoreduce
datamistakes.
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 5/38

ID:pone.0333286 — 2025/10/16 — page 6 — #6
PLOS One Optimizingnetworkbandwidthslicingidentification
Focusingonloadbalancingandslicefailuremanagement,manyapproacheshavebeen
proposed.Najwanetal.[16]introducedanintelligentrecurrentneuralnetwork(RNN)
controlleraswellastheintelligentSDNmulti-spikeneuralsystem(IMSNS)forservicetype
identification,leveragingmoderatelymulti-spikereturnneuralnetworks(MMSRNN)and
time-basedcodingtoreduceenergyconsumptionandimprovetrafficidentificationforopti-
mizednetworksliceallocation.Additionally,Michael[17]proposesadata-drivenML-driven
slicingandallocationmodelthatmainlyenabledimprovedqualityofserviceandtraffic-aware
trustworthydynamicslicing,wheretoolscanbestrategicallyallocatedandredirectedbetween
networkslicesdependingontime-dependentvirtualresourcedemandsinthepaper.Addi-
tionally,thestudyutilizedsupervisedMLtechniquestodevelopanSLAdeconstructiongen-
eratorfornetworkslicing,evaluatingtheaccuracy,samplecomplexity,andmodelexplain-
abilityofeachalgorithmclass.Followingwithapproach,Anuragetal.[22]proposedAdap-
tiveLearningasthe‘ADAPTIVE6G’frameworkasauniqueapproachtonetworkslicing
design,concentratingonresourcemanagementandloadpredictionindata-drivenBeyond
5Gwirelessnetworks.Thesystemleveragesknowledgecollectedviatransferlearning(TL)
methodologiesandisevaluatedforsolvingdifficultnetworkloadestimatechallenges,withthe
ultimategoalofestablishingamoreequitableandbalanceddistributionofnetworkresources.
Alsointhecontextofreconfigurablewirelessnetworksolutions,Sulaimanetal.[23]intro-
ducedahybridDLmodelthatcombinedCNNfortaskslikeresourceallocation,network
reconfiguration,andsliceselection,andLSTMforhandlingstatisticalinformationrelatedto
networkslices,includingloadbalancinganderrorrates.Nevertheless,alltheseresearchstud-
iesfallshortintermsofprovidingtransparencyinnetworksliceallocationandoutliningthe
underlyingdistributedsecuredata.Theseelementsholdimportantimportanceinthecontext
ofoptimizingpredictionalgorithmsforthestudy’sobjectives.
Sarderetal.[24]proposedafogloadbalancingframeworkutilizingNB-IoTandgamethe-
oryformassiveMachineTypeCommunication(mMTC)applications.Theyarticulatedthe
issueasabankruptcygame,utilizingShapleyvalue-basedschedulingwithalow-complexity
GreedyIterativeTimeScheduling(GITS)algorithm.Thefogloadbalancingwasformulated
asaHitchcock–KoopmanstransportationproblemandresolvedwithVogel’sApproxima-
tionMethod(VAM),substantiallydecreasingjobbalancingexpenses.Madyanetal.[25]
proposedarisk-sensitiveresourceallocationstrategyforultra-reliablelow-latencycom-
municationtrafficin5GNewRadionetworks.Theyoptimizedresourceallocationutilizing
ConditionalValueatRisk(CVaR)andMarkov’sinequality,soensuringthereliabilityof
Ultra-ReliableLowLatencyCommunication(URLLC).Theissuewassubdividedintosub-
problemsandresolvediteratively,resultingineffectiveURLLCschedulingwhilepreserving
eMBBreliability.
Anupametal.[26]examinedeMBB-URLLCco-schedulingemployingthepuncturing
techniquetooptimizelatency,reliability,andspectrumefficiency.Theyformulatedanopti-
mizationproblemmaximizingtheMinimumExpectedAchievedRate(MEAR)ofeMBB
users,applyingaPenaltySuccessiveUpperBoundMinimization(PSUM)algorithmforeMBB
andanOptimalTransportationModel(TM)forURLLCscheduling.Theirmethodology
surpassedbaselinemethodsinMEARandfairness.Madyanetal.[27]evaluateddynamic
resourceslicingforeMBBandURLLCservices,seekingtomaximizeeMBBdatarateswhile
assuringURLLCreliability.TheyprovidedaframeworkforDeepReinforcementLearning
(DRL)enhancedbyoptimization,segmentingtheproblemintosubproblems,andconvert-
ingthemintoconvexforms.ThetechniquesuccessfullyequilibratedURLLClimitationswhile
preservingeMBBreliabilityover90%.
Table2hasbeengeneratedtoofferasummaryofthemethodsthathavebeenapplied
fornetworkslicingandtheclassificationofexpectedservices.Uponadetailedevaluationof
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 6/38

ID:pone.0333286 — 2025/10/16 — page 7 — #7
PLOS One Optimizingnetworkbandwidthslicingidentification
Table2.Overviewoftheexistingrelatedmodels.
Research Dataset Algorithms KeyInsights
Robertetal.[9] N/A ProposedArch. ModifiedA*improves5Glatency&time
Yuanwenetal.[10] N/A RSMA Flexibledecoding&higherrates
Kostosetal.[11] N/A NOMA Coop.NOMAboostsslicingthroughput
Amiretal.[12] N/A RDPG HandlesCSIuncertaintyeffectively
Amiretal.[13] N/A GAN–NoisyNet Enhancesthroughput&energyinIIoT
Ramrajetal.[14] Unicaucav2,5Gslice KNN,CNN,LSTM,HHO,SVM HHO-CNN+LSTMoutperformsclassicML
Jobertoetal.[15] DDoS-2019 KNN,RF,SVM,MLP MLslicingimprovesenergy&security
Najwanetal.[16] NSDataset(65K) MMSRNN,CNN MMSRNNaidstraffic&energyefficiency
Michaeletal.[17] DomainEmulator RF,GB,CNN GB+NNworkwellinslicing
AnuragAetal.[22] NSDataset(65K) ADAPTIVE6G TL-basedADAPTIVE6Gimprovesloadest.
Sulaimanetal.[23] NSDataset(65K) CNN+LSTM Achieves95.17%accuracyfor5G/6G
Ours NSDataset(65K) CNN,LIME,SHAP,VAE VAEdetectsanomalies,CNNclassifies,SHAP/LIMEforexplainability
https://doi.org/10.1371/journal.pone.0333286.t002
existingworks,itbecomesobviousthattheseeffortsgenerallyrevolvearoundboostingsys-
temefficiency.Yet,thereareconsiderablegapsinaddressingtheessentialtopicofguaran-
teeingdatasafetyduringreal-timeanalysis,withafocusonminimizingtheintroductionof
newerrors.Additionally,maintaininglowdataerrorsindataproducedfromthesourceis
necessaryforsustainingdatacredibilitywhilepreservingtheunderlyingdatacorrelations.
Moreover,itisworthmentioningthatcertainnetworkcharacteristicsplayavitalroleinthe
classificationanddistributionofslices,makingthemindispensableforestablishingsystem
awarenessandenablingimproveddecision-makingwithouttheneedforhumaninteraction.
Ourcontributionsgenerallycenteronaddressingthesekeyviews.
3 System framework and use case scenario
OurINBSImodelprovidesaholisticsolutionforoptimalresourceallocationin5Gnet-
workslicingbydynamicallyregulatingnetworkresourcesaccordingtoapplication-specific
demandsshowninFig2.Upontheinitializationofa5Gnetwork,activeapplicationssuch
asApp1(e.g.,videostreaming)andApp2(e.g.,VoIPservices)areallocatedtodesignated
networkslicesbasedontheirServiceLevelAgreement(SLA)criteria,includingbandwidth,
latency,andqualityofservice(QoS).Adefaultsliceisreservedforunclassifiedorunknown
traffic,ensuringnotrafficisleftunmanaged.
Upontheconnectionofanewapplication,suchasApp3(areal-timegamingapplication),
tothenetworkviaUserEquipment(UE)andAccessNode,theNetworkOrchestratorfirst
allocatesittothedefaultslice.Thisassignmentistemporary.ThetrafficfromApp3isini-
tiallyprocessedbyaVAEmodel,whichidentifiesabnormalitiesintheflowandreconstructs
anydistortedormissingdata.Thisprocedureguaranteesthatonlytrustworthy,cleandata
isutilizedforfurtherresearch.Oncethedataiscleaned,thesystemextractscriticalnetwork
metricssuchasbandwidthutilization,latency,andpacketlossusingoursuggestedCNN
model,whichisoptimizedwiththeNADAMoptimizer.Thismodelisexplicitlyengineered
tomanagethecomplexitiesofnetworktrafficbycapturingtemporalandspatialdependen-
cieswithinthedata.TheseattributesareutilizedtoascertainifApp3canpersistinthedefault
sliceorwhetheranewspecializedsliceisrequired.IfoursuggestedCNNmodelfindsthat
App3requiresafreshslice,thesystememploysSHAPandLIMEtomakethechoiceclear.
TheseXAIapproachesassistexplainwhyafreshsliceisneededbyemphasizingcrucialissues
suchastheapplication’shighQoSneeds,networkcongestion,andpacketlossthatexceed
acceptablenorms.Thisinterpretabilityaidsstakeholdersincomprehendingtherationalefor
dynamicsliceallocation,hencefosteringtrustinthesystem’sjudgments.
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 7/38

ID:pone.0333286 — 2025/10/16 — page 8 — #8
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig2. OurINBSImodelfor5Gnetworkslicing,utilizingVAEforanomalydetection,CNNwithNADAMforsliceprediction,and
SHAP/LIMEforinterpretabilitytoensureefficientresourceallocationandQoScompliance.
https://doi.org/10.1371/journal.pone.0333286.g002
Accordingtotheprediction,theNetworkOrchestratordynamicallyestablishesanewded-
icatedslice(Slice3)utilizingresourcesfromthevirtualizedResourcePool.Theorchestrator
reallocatestherequiredresources,suchasbandwidthandcomputingpower,toensurethat
Slice3isoptimizedfortherequirementsofApp3.Theapplication’strafficissubsequently
transferredfromthedefaultslicetoSlice3,guaranteeingmaximumperformanceforreal-time
gaming.OnceApp3disconnectsorbecomesinactive,Slice3isterminated,anditsresources
arereturnedtotheResourcePool,ensuringthatnetworkresourcesareutilizedefficiently
forfutureapplications.Throughoutthisprocess,thesystemcontinuallyanalyzestheperfor-
manceofSlice3toensurethatitmatchestheapplication’sincreasingdemands.Iftheneeds
ofApp3varysuchasduringpeakgaminghours,theNetworkOrchestratormayalterthe
slice’sresourcestomaintainoptimalperformance.Thisdynamicresourceadjustmentguaran-
teesthatthenetworkcanreacttofluctuatingtrafficcircumstancesandapplicationdemands
inreal-time.TheoverallworkingmechanismoftheINBSIsystemisillustratedinFig3.It
beginsbyapplyingtheVariationalAutoencoder(VAE)fordataanomalydetectionandpre-
processing.TheprocesseddataisthenpassedtotheproposedConvolutionalNeuralNetwork
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 8/38

ID:pone.0333286 — 2025/10/16 — page 9 — #9
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig3.GraphicalrepresentationofourproposedINBSIsystem.
https://doi.org/10.1371/journal.pone.0333286.g003
(CNN)model,whichclassifiesthenetworkslicingaccurately.Finally,basedonthemodel’s
parameters,decision-makingisenhancedthroughtheapplicationofExplainableAI(XAI)
methods.
4 Proposed Interpretable Network Bandwidth Slicing
Identification (INBSI) system
OurproposedInterpretableNetworkBandwidthSlicingIdentification(INBSI)systemeffi-
cientlymitigatesdataabnormalitieswithinnetworkinfrastructurebyintegratingfeature
importanceanalysiswithprecisesliceassignment.Operatingprimarilyintheapplication
layer(Fig4),oursystemleveragesaVAEmodeltodetecterrorsandencoderegistration-
relateddata,whileacustomCNNmodelclassifiesandpredictsscatteredslicesbasedonuser
input,packetloss,QoSClassIdentifier(QCI),andotherparameters.Throughtheuseof
explainableAI(XAI)techniques,networkoperatorscanbetterunderstandandassessthefair-
ness,accuracy,andperformanceofsliceallocationdecisions.XAIimprovesinterpretability
byassigningaccurateprioritiestospecificslicesusingfeatureimportance,enhancingload
balancinganddynamictrafficmanagement.
WeevaluatehowourmodelsbehaveinourproposedINBSIsystemenvironmentusing
learningcurves,classificationreports,confusionmatrices,trainingaccuracy,andlosscurves.
Forathoroughevaluationofmodeloutcomes,wealsocalculatemeansquarederror(MSE)
andmeanabsoluteerror(MAE).TheproficientslicedistributionisillustratedinFig5.
4.1 Dataset
Thissectiondescribesthedatasetandthepreprocessingstepsthatthedatasetwentthrough
beforebeingfedtotheproposedmodel.
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 9/38

ID:pone.0333286 — 2025/10/16 — page 10 — #10
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig4.TheproposedNetworkBandwidthSlicingIdentification(INBSI)system’stop-levelparadigm.
https://doi.org/10.1371/journal.pone.0333286.g004
4.1.1 Datacollection. ThedatasetwascollectedfromKaggle,“DeepSliceandSecure5G
-5GandLTEWirelessDataset”[28].The6Gdataisstillnotavailableinthisdomain,sowe
usedthe5Gdatasetforperformancemeasurement.Thedatasetcomprisesthemostimpor-
tantnetworkanddeviceKPIs,suchasthekindofconnecteddevice(suchasasmartphone,
IoTdevice,URLLCdevice,etc.),theUserEquipment(UE)category,theQoSclassidenti-
fier(QCI),thepacketdelaybudget,themaximumpacketloss,thetimeanddayoftheweek,
etc.ControlpacketsbetweentheUEandnetwork,whichmainlycontainmorethan65,000
differentinputcombinationswithtargetlabelscanbeusedtocollecttheseKPIs[29],[30].
4.1.2 Trainingandtestingdata. Tospecifythemodel,webeginbysplittingthedataset
usingaVAE,establishingdistincttrainingandtestsetsina70:30ratio.Subsequently,wetrain
asuiteofvariedmachinelearningclassifiers,includingKNN,RandomForest,DecisionTree,
GaussianNB,Baggingclassifier,AdaBoost,DNF,MLP,andourinnovativeproposedCNN
model,onthemeticulouslygenerateddataset.Ourpickofthemosteffectivemodelisbased
onitsabilitytopredictnetworkslicinglabels.Finally,weenrichthedatasetwithexplainable
AIbycombiningclassifiermodels.
4.2 Preprocessingsteps
Thedatasetunderwentaseriesofpreprocessingstepstoensureitssuitabilityforthespecified
machinelearningmodels,beginningwiththeremovalofunrelatedcolumnsthatdidnotcon-
tributetothepredictiveperformance.Thepreprocessingbeganwiththeremovalofunrelated
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 10/38

ID:pone.0333286 — 2025/10/16 — page 11 — #11
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig5.WorkingmethodologyofourproposedINBSIsystem.
https://doi.org/10.1371/journal.pone.0333286.g005
columnsthatdidnotcontributetothepredictiveperformance.Tomaintainuniformityin
datarepresentation,integervalueswithincategoricalcolumns,specifically“LTE/5GUECat-
egory(Input2)”and“QCI(Input6)”,weretransformedintostringformat.Thisstepwascru-
cialforpreventingpotentialdiscrepanciesindatatypeinterpretationduringmodeltraining.
Subsequently,categoricalvariableswereencodedusingalabelencodingtechniquetoconvert
non-numericfeaturesintonumericalrepresentations,therebyenhancingthemodel’sability
toprocessandlearnfromtheseattributes.Thefeaturessubjectedtolabelencodingincluded
“UseCaseType(Input1)”,“LTE/5GUECategory(Input2)”,“TechnologySupported(Input
3)”,“Day(Input4)”,and“SliceType(Output)”,ensuringastandardizednumericalrepresen-
tationofcategoricaldata.Furthermore,tooptimizemodelperformanceandreducepotential
noise,twodistinctfeatureswereeliminatedfromthedatasetbasedontheirirrelevanceorlow
contributiontopredictiveaccuracy.Thesepreprocessingsteps-includingtheethicalhan-
dlingofimbalancedmedicaldatathrough[specifictechniques]-collectivelyenhanceddata
consistency,privacypreservation,andcompatibility,ultimatelycontributingtotherobustness
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 11/38

ID:pone.0333286 — 2025/10/16 — page 12 — #12
PLOS One Optimizingnetworkbandwidthslicingidentification
andefficiencyofthelearningmodelwhilemaintainingcompliancewithhealthcaredata
protectionregulations.
4.3 VAEforcontinuouslatentspacerepresentation
Inthecontextofdataanomalydetectionanderrorpatternidentification,weproposetheuse
ofaVAEmodel.Byduplicatinginputdata,theVAEtechniqueisappliedtotheautoencoder
thatlearnsacontinuouslatentspacerepresentation.Inadditiontoanencoderandadecoder
network,reconstructionlikelihoodisalsousedasaprobabilisticmeasure[31].Through
learningmappingsfromlow-dimensionallatentvectorstohigh-dimensionalinputs,VAEs
approximatethismanifoldwhileencouragingglobalstructureinthelatentspace[36].The
architectureofVAEisshowninFig6.TheVAEemploysadense-layerencoderarchitecture,
batchnormalization,dropoutregularization,andauniquelossfunctiontooptimizelatent
spacedimensionsandreduceinputdatadimensionality.
4.3.1 Gaussianencoding. Theencoderoutputsthesetofparametersofadistribution
inthelatentspacegivenaninputdatapointx.Tomakecomputationseasier,itisusualto
assumethatthisdistributionisGaussianandhasadiagonallydrawncovariancematrix.The
encoderpredictsthemeanandlog-varianceofthisGaussiandistributionas𝜇and𝜎2,accord-
ingly.Theencodercanbeexpressedasfollowsifzisthelatentvariable(sampledfromthe
latentspacedistribution):
h=tanh(w +b ), (1)
h h
𝜇=w h+b , (2)
𝜇 𝜇
𝜎2=exp(w h+b ), (3)
𝜎2 𝜎2
q(z∣x)=N(z;𝜇,𝜎2I). (4)
4.3.2 Reparameterization. Wetakeasamplefromthedistributionwith𝜇and𝜎2as
parameterstoproducethelatentvariablez.AftersamplingfromatypicalGaussiandistribu-
tionwithmean0andvariance1,thereparameterizationapproachisusedtomodifythedata
points.
1
z=𝜇+𝜖⋅exp( log(𝜎2)), (5)
2
Fig6.Variationalautoencoderarchitecture.
https://doi.org/10.1371/journal.pone.0333286.g006
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 12/38

ID:pone.0333286 — 2025/10/16 — page 13 — #13
PLOS One Optimizingnetworkbandwidthslicingidentification
4.3.3 Decoding. Thedecodertakesthesampledlatentvariablezandattemptstorecon-
structtheoriginaldatapointx.Thedecoderistypicallyaneuralnetworkthatoutputsthe
reconstruction.
4.3.4 Variationalinference. Theprimarygoalinvariationalinferenceistominimize
theKullback-Leibler(KL)divergencebetweentheapproximatingdistributionq(z∣x),with
parameters𝜙,andthetrueposteriordistributionp(z∣x),withparameters𝜃,aspresented
in[37].
𝜙∗,𝜃∗=argminKL(q(z∣x (i) ;𝜙)∥p(z∣x (i) ;𝜃)), (6)
𝜙,𝜃
TheKLdivergencebetweentwoprobabilitydistributionsq(z)andp(z)isdefinedas:
q(z)
KL(q∥p)=∫ q(z)log dz, (7)
p(z)
whereitestimatesthedifferenceininformationrichnessbetweentwodistributions.
TheKLdivergenceisdescribedintermsofexpectanciesas,
KL(q∥p)=E[logq]–E[logp]+logp, (8)
whiledemonstratinghowitmaybecalculatedasthedifferencebetweentheexpectedvalueof
thelogarithmofq(z)andtheexpectedvalueofthelogarithmofp(z),pluslog(p).
KL(q∥p)=ELBO+logp, (9)
Theevidencelowerbound(ELBO)isintroducedasanimportantconcept.Itrepresentsa
lowerboundonthelog-likelihoodofthedata.TherelationshipbetweentheKLdivergence,
ELBO,andthelog-likelihoodtermisshownasfollows.
ELBO=–KL(q∥p)+E[logp], (10)
TheELBOisdecomposedintotwopartsbythisequation:thenegativeKLdivergenceterm
andthepredictedvalueofthelogarithmofp(z).Finally,wecombinethegoalsofdetermining
thebestparameters𝜙∗and𝜃∗asfollows.
𝜙∗,𝜃∗=argmin–KL(q∥p)+E[logp], (11)
𝜙,𝜃
Whenthoseparametersareoptimized,thenegativeKLdivergenceisminimizedandthe
anticipatedlog-likelihoodtermismaximized.
4.3.5 Lossfunction. Themaingoalofthisfunction,whichisdefinedasL istomaximize
r
theevidencelowerbound(ELBO),whichisequivalenttoloweringthereconstructionloss
andtheKLdivergencebetweentheprojectedlatentprobabilityandtheoriginaldistribution
(thestandardGaussian).
L =–log(p(x|z)). (12)
r
ThetotallossfortrainingtheVAEisthesumofthesetwocomponents.Overall,thework-
ingmechanismofourVAEmodelcaneffectivelyreducethedatadimensionality,ensuringthe
dataissavedwiththesameinputfeaturesbyreconstructingthenewdata.Thiscontribution
leadstounderstandingcomplexrelationshipsbyvisualizingandidentifyingnewpatternsand
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 13/38

ID:pone.0333286 — 2025/10/16 — page 14 — #14
PLOS One Optimizingnetworkbandwidthslicingidentification
trends.OurVAEmodelcanpinpointtheuser-requesteddataanddetectanykindsoffalseor
erroneousrequestsbyfollowingthedecoderreconstructionmechanism.
4.4 MLmodels
FollowingtheapplicationoftheVAEfordatarepresentation,welaterusedifferentMLalgo-
rithmstoexecutethenecessarygoalofclassifyingthecommunicationserviceformakingthe
systemanautomatedclassifier.
TheKNNalgorithmcategorizesdatapointsbasedontheirnearestneighbors[38].For
continuousdata,GaussianNaiveBayesmakesuseofGaussiandistributionassumptions
[39].RandomForestisaclassificationmethodthatincorporatesrandomizeddecisiontrees
whereasdecisiontreesareadaptableforclassificationandregression[40,41].Baggingclas-
sifiermainlyapproachesavoidingoverfittingbyaveragingpredictionsfromseveralmodels,
whereasAdaBoostworksbygivingmoreweighttodifficult-to-classifysituationsandless
weighttothosethatarealreadyhandledwell[42–44].
4.5 Neuralnetworkmodels
Followingthat,thecomplexityofthedatasetiscarefullyconsideredinlaterutilizingneural
networkmodels.Themethodinvolvesdividingthedataintodigestibleportions,allowingfor
fastbatchlearning.ThemodelsincludeDNFnetworkandMLP,bothwiththerequiredlayer
architecture[45,46].Thesemodelsaretrainedfor30epochs,withearlystoppingapproaches
usedtoimprovetheirperformance.
4.6 Proposedmodel
WepresentalightweightCNNarchitecture,designedtostreamlinecomplexoperationsand
servicestotheapplication,toimprovetheefficiency,speed,andreliabilityofourautomatic
networkslicingallocationwithintheINBSIsystem.
Thismodificationaddspowerfulfeatureextractioncapabilitiestothearchitecture,
enablingrapiddeploymentandefficientapplicationinclassificationtasks.Toincreaseitsper-
formance,theproposedCNNmodelmakesuseofspecifiedparameters.Tocaptureextensive
informationpatterns,themodelbeginswithaconvolutionallayerwith64filtersandaker-
nelsizeof(3,1),andappliestheReLUactivationfunction(ReLU).Usingthesamepadding
ensuresthatthedimensionsremainconsistentacrossthenetwork.Asaresult,amax-pooling
layerwithapoolsizeof(2,1)dramaticallylowersspatialdimensions.Toboostthemodel’s
representationalcapacity,weadda128-filterconvolutionallayerwiththesame(3,1)kernel
sizeandthesamepadding.Thisadditionallayerboostsfeatureextractioncapabilities.Fol-
lowingtheseconvolutionallayers,weapplyaflattenedlayertothedatatoreshapeit.This
isfollowedbyathicklayerwith256neuronsandReLUactivation.Topreventoverfitting,a
dropoutlayerwitharateof0.5isincorporatedforregularization.Anotherdenselayerwith
128neuronsfollows,addinganotherdegreeoffeatureabstraction.Finally,adenselayerwith
64neuronsisadded.Theoutputlayerimplementsthesoftmaxactivationfunction,simplify-
ingmulticlassclassificationjobswiththreeoutputclasses.Weequipthemodelwithamore
advancedandcustomizedoptimizer,“NADAM”,andalearningrateof0.001.
ToincreasetheperformanceofourmodelweuseNADAMoptimizer.Thenesterovaccel-
eratedgradient(NAG)andAdamoptimizationproceduresarecombinedintheNADAM
optimizationmethodology.Duringtraining,theNADAMmethodisusedtooptimizethe
parametersofanMLmodel.Itisparticularlyeffectivewithneuralnetworksandotherdeep-
learningapproaches.Thesearethestepsthatthealgorithmtakes.
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 14/38

| ID:pone.0333286 | — 2025/10/16 | — page | 15 — #15 |     |     |
| --------------- | ------------ | ------ | -------- | --- | --- |
PLOS One Optimizingnetworkbandwidthslicingidentification
Firstly,itcalculatesthegradientg ofthelossfunctionf withrespecttotheparameters
|     |     | t   |     | t   |     |
| --- | --- | --- | --- | --- | --- |
𝜃 t–1 .
|     |     |     | =∇f(𝜃 ), |     |      |
| --- | --- | --- | -------- | --- | ---- |
|     |     |     | g        |     | (13) |
|     |     |     | t t t–1  |     |      |
Thenbytakingaweightedaverageoftheprecedingmomentm andthegradient,youcan
t–1
| updatethefirstmomentvectorm.Thisstageisanalogoustohowmomentumoperatesinthe |     | t   |     |     |     |
| -------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
NAG.
|     |     | m =𝛽 | m +(1–𝛽 | )g,   | (14) |
| --- | --- | ---- | ------- | ----- | ---- |
|     |     | t    | 1,t t–1 | 1,t t |      |
Updatethesecond-momentvectorn t bytakingaweightedaverageoftheprevioussecond
momentn andthesquareofthegradientg2,where𝛽 isthesquaredgradientsmoothing
| t–1 |     |     | t   | 2   |     |
| --- | --- | --- | --- | --- | --- |
parameterattimestept.
|     |     | =𝛽  | +(1–𝛽   | )g2,  |      |
| --- | --- | --- | ------- | ----- | ---- |
|     |     | n   | n       |       | (15) |
|     |     | t   | 2,t t–1 | 2,t t |      |
Determineatemporarymomentumcorrection(m)usingtheratioofm tothesumofi
t
forirangingfrom1toT(whereTisthenumberoftimesteps).Thismodificationtakesinto
accountthepriorinstantvalues.
|     |     | 𝛽          | m (1–𝛽  | )g      |      |
| --- | --- | ---------- | ------- | ------- | ---- |
|     |     | m̂ = 1,t+1 | t +     | 1,t t   |      |
|     |     |            |         | ,       | (16) |
|     |     | 1–∏T       | 𝛽 1–∏T  | 𝛽       |      |
|     |     |            | i=1 1,i | i=1 1,i |      |
Bygeneratingatemporarysquaredgradientadjustmentnbasedontheratioofn to(1-n)
t
(wheretisthesquaredgradient’sexponentialdecay).
|     |     |     | n̂= 𝛽 2,t n t |     |      |
| --- | --- | --- | ------------- | --- | ---- |
|     |     |     | ,             |     | (17) |
1–𝛽
2,t
Usingtheadjustedmoment(m),squaredgradient(n),andthelearningrate(t),updatethe
model’sparameters(t)wheretisthelearningrateattimesteptand𝜖isasmallconstantto
preventdivisionbyzero.
𝜂⋅m
|     |     |     | =𝜃 √  | t   |      |
| --- | --- | --- | ----- | --- | ---- |
|     |     | 𝜃   | –     | ,   | (18) |
|     |     | t   | t–1 n | +𝜖  |      |
t
ThemodelarchitecturehasbeendisplayedinFig7.Byimplementingthisproposed
methodwithNADAMoptimizer,theperformancewithclassificationwillbemuchmoreeffi-
cient,andtheendobjectivewillbeensuredbygivingthecorrectslicetypetotherequired
applications.WiththisproposedDLmethod,thenetworkoperatorscanefficientlydistribute
slicestowardapplicationsandmaintainloadbalancingforapplicationsinanadaptivefashion.
Byreceivingmoredata,themodelwilllearnandmakesuitabledecisionsbasedonthedeter-
mininginputfeatures.Ourproposedmodelcancapturespatialpiecesofinformationbased
onthedataprovidedprocess.Ifcomputationandpredictionarerequiredforasingleslice,
oursuggestedapproachallowsforflexibility,removingtherequirementtotrainthecomplete
dataseteverytime.
4.7 Interpretabilitymethodsusedinnetworkslicing
EventhoughourproposedclassifierisdesignedtoensurethepreservationofQoScriteriaand
efficientslicedistributioninsideourproposedINBSIprocess,theinterpretabilityoftheclassi-
ficationfindingsisimperative.Asaresultofthewiderangeofapplications,eachwithitsown
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 15/38

ID:pone.0333286 — 2025/10/16 — page 16 — #16
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig7.TheproposedModelArchitectureusingNADAMOpitmizer.
https://doi.org/10.1371/journal.pone.0333286.g007
setofrequirementsandtechnologicalsettings,includingcommunicationprotocolssuchas
long-termevolutionformachines(LTE-M)andnarrowbandInternetofThings(NB-IoT),this
requirementarises.
4.7.1 LIME. Inadditiontobeingversatile,weutilizetheLIMEmethodforeachsliceto
theblack-boxclassifier,enablinguserstoconstructexplanationsforspecificpredictions.To
applyLIMEinourstudy,weutilizeXGBoostandourproposedCNNmodelastheunder-
lyingclassifierduetoitsefficiencyandstrongperformanceinstructureddataclassification.
Therefore,itapproximatestheblack-boxmodellocally,despiteitsgloballimitations[47].The
generalformulaofLIMEisasfollows[48].
Φ(x)=𝛼⋅argmin𝜁(f,g,𝜋 )+Ω(g), (19)
x
wheregdefinesthepresenceofcomponentsthatcanbeunderstood,Ω(g)signifiescomplica-
tionthatcontrastswithinterpretability,𝜋 (z)focuseslocalitybetweenztox,andf(x)defines
x
thelikelihoodthatxbelongstoaclass.Lastly, 𝜁(f,g,𝜋 )illustrateshowinaccurategisin
x
calculatingf inthevicinitydeterminedby𝜋 .
x
4.7.2 SHAP. Forinterpretationtestingwithadditionglobalimportanceanalysis,weapply
SHAPtoanalyzefeatureimportanceinourclassificationmodel.TocomputeSHAPvalues,
weagainutilizetheXGBoostandourproposedCNNmodelasourbaseclassifier.XGBoost
enhancesinterpretationthroughdecisiontrees,leveraginguniquetreelearningtechniques,
logicalmeasuresketching,andparallelcomputingforbetterscalability.Italsointegrates
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 16/38

| ID:pone.0333286 | — 2025/10/16 | — page 17 | — #17 |     |     |
| --------------- | ------------ | --------- | ----- | --- | --- |
PLOS One Optimizingnetworkbandwidthslicingidentification
second-orderderivativestominimizemodelerroreffectively[50].TheShapleyvalueisthe
meanofthemarginalcontributionsforallpossiblefeaturepermutations[49].Themathemat-
icalexpressionisasfollows:
|S|!(n–|S|–1)!
|     | ∅ = | ∑   | [v(S∪{i})–v(S)], |     | (20) |
| --- | --- | --- | ---------------- | --- | ---- |
i
n!
S⊆N⧵{i}
where∅ isthemainfocusoffeaturei,Nisthesetconsistingofalltheattributes,nisthe
i
numberoffeaturesinN,SisthesubsetofNthatcontainsfeaturei,andv(N)isprincipal
basevalue,definingthepredictedresultforeachattributeinNwithoutknowledgeofthe
featurevalues.TheSHAPvalueofeachfeatureforeveryanalysisisincludedtoestimatethe
modelresultsforeachobservation.Foramodelf andfeaturevectorz,themodelisdefinedas
follows.
M
|     |     | g(z′)=∅ | +∑∅z′. |     | (21) |
| --- | --- | ------- | ------ | --- | ---- |
|     |     |         | 0 i    | i   |      |
i=1
wheregmainlyreferstotheexplanationmodel,z′∈{0,1}Mprimarilydefinesthefeaturevec-
torofz(soz=h(z′)).Misthecountoffeaturesand𝜙
|     |     |     |     | canbeobtainedfromEq20.𝜙 | isthe |
| --- | --- | --- | --- | ----------------------- | ----- |
|     |     |     | i   |                         | 0     |
modeloutputwhenallthe
featuresarenotpresente.g.,z′=h(0).
| 5 Performance | evaluation | metrics |     |     |     |
| ------------- | ---------- | ------- | --- | --- | --- |
Performanceevaluationmeasuresareusedtoassesstheefficacyofeachmodel.Theseinclude
accuracycurves,confusionmatrices,classificationreports,MSE,alongMAE.
Astheaccuracycurveindicatesthemodel’sbestpossibleaccuracy,itssmoothnessrep-
resentsitsabilitytoclassify.Asmootherslopeindicatesabetterclassifier.Wecaneasily
trackwhichmodelsarecorrectandwhichareincorrectbycomparingtheactuallabelstothe
projectedlabelsinaconfusionmatrix.
Theclassificationreportforeachmodeloffersfourmetricstoevaluateitseffectiveness:
Support,Precision,F1score,andRecall.Precision(P)isdefinedastheproportionofaccu-
ratelyanticipatedoutcomesofthetotalnumberofpositivelyclassifiedobservations.Inother
words,itevaluatestheaccuracyofpredictionsandisformallystatedasfollows.
T
|     |     | P=  | p   |     |      |
| --- | --- | --- | --- | --- | ---- |
|     |     |     | ,   |     | (22) |
T +F
p p
Therecall(R)metricisdeterminedbydividingthetotalnumberofinitialclassevaluations
bythenumberofanticipatedresults.
|     |     | R=  | T p |     |      |
| --- | --- | --- | --- | --- | ---- |
|     |     |     | ,   |     | (23) |
T +F
p n
TheF1-scoreiscalculatedbyaveragingprecisionandrecall.
2×precision×recall
|     |     | F1= |     | ,   | (24) |
| --- | --- | --- | --- | --- | ---- |
precision+recall
whereT p isTruePositive,F p isFalsePositive,F n isFalseNegative,andT n isTrueNegative.
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 17/38

| ID:pone.0333286 | — 2025/10/16 | — page 18 | — #18 |     |
| --------------- | ------------ | --------- | ----- | --- |
PLOS One Optimizingnetworkbandwidthslicingidentification
MSEquantifiestheleveloferrorinstatisticalmodels.Itcomputestheaveragesquareddif-
ferencebetweenobservedandpredicteddata.Whenamodelhasnomistakes,theMSEis
zero.Asmodelinaccuracygrows,sodoesthevalue.
1 n
|     |     |     | = ∑(y –ŷ)2 |      |
| --- | --- | --- | ----------- | ---- |
|     |     | MSE | i i ,       | (25) |
n
i=1
MAEmeasurestheerrordifferencebetweentwoobservationsofthesameevent,used
incomparisonslikepredictedversusobserved,subsequenttimeversusstartingtime,and
differentmeasuringtechniques.
1 n
|     |     | MAE= | ∑∣y –x∣, |      |
| --- | --- | ---- | -------- | ---- |
|     |     |      | i i      | (26) |
n
i=1
| 6 Result and | analysis |     |     |     |
| ------------ | -------- | --- | --- | --- |
6.1 HyperparametersandreconstructionerrorcalculationofVAE
AvalidationdatasetisusedtoassesstheVAE’sperformance,andabaselinelossiscalcu-
lated.Reconstructionskillsanddatarepresentationeffectivenessareevaluatedusingmodel
loss,meansquarederror,andabsoluteerror.ThemetricsarecalculatedandgiveninTable3.
VisualizationandanomalydetectionindicateVAE’sperformance,withlowerMSEvalues
indicatingbetterdatareconstructionandaverageMAEvaluesindicatingaccuratepredictions.
Fig9(a),9(b)mainlydepictsthelosscurveandacomparisonoforiginalandrebuiltdata.
ThisdecreaseorstabilizationofthelosscurvesuggeststhattheVAEmodelhaslearnedto
encodetheinputdataintoalatentspacerepresentationandissuccessfullyreconstructingthe
originalinputfromthislatentrepresentation.ThereductioninlossinFig9(a),9(b)suggests
thatthemodelisslowlyclosingthegapbetweenthereconstructedsamplesandtheoriginal
inputdata.
Fig8(a),8(b)depictsthesimilaritiesbetweenthereconstructedandoriginaldata.Our
implementedVAEmodelaccuratelyrecoversoriginaldatafromlearnedrepresentations,
demonstratingitsabilitytocaptureandrecreateunderlyingpatternsandstructureindata.
Thisdiscoveryhasimplicationsforoccupationslikedatagenerationandanomalydetection
innetworkslicing.
6.2 MLresults
Fig10illustratesthelearningcurvesofsixclassifiers,showingtheirgeneralizationbehav-
ior.RandomForestandBaggingClassifierdemonstratestrongperformancewithconverg-
ingtrainingandvalidationscores,indicatinggoodgeneralization.KNNandDecisionTree
exhibitoverfitting,withhightrainingaccuracybutpoorvalidationperformance.Gaussian
Table3.VAEperformancebaseline.
| EvaluationMetric  |     |     | Result |     |
| ----------------- | --- | --- | ------ | --- |
| BaselineLoss(MSE) |     |     | 0.083  |     |
| ModelLoss(MSE)    |     |     | 0.917  |     |
| ModelMAE          |     |     | 0.006  |     |
Tablenotes:MSE=MeanSquaredError,MAE=MeanAbsoluteError.TheVAEshowshighermodellossdueto
reconstructiondifferencesbutmaintainslowabsoluteerror.
https://doi.org/10.1371/journal.pone.0333286.t003
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 18/38

ID:pone.0333286 — 2025/10/16 — page 19 — #19
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig8.Anomalydetectionoftheconstructeddata.
https://doi.org/10.1371/journal.pone.0333286.g008
NaiveBayesshowsunderfitting,asbothscoresremainlowandclose.AdaBoostimproves
withmoredata,graduallynarrowingthegapbetweentrainingandvalidationscores.Over-
all,ensemblemethodslikeRandomForestandBaggingaremorerobust,whilesimpleror
unregularizedmodelstendtooverfitorunderfit.
TheconfusionmatrixisshowninFig11,anditillustrateshowwellthemodelperformed
foreachclass.Theconfusionmatrixshowsthatthemodelsgiveconsistentresultsacross
classes,demonstratingconsistentperformanceoverawiderangeofclassifications.These
matricescanbeexaminedtodiscoverintriguingpatternsandmisclassificationswithinspe-
cificclasses.ExceptfortheGaussianNBmodelispresentedinFig11(d),allofthemodels
performwellforthetargetfeature,althoughwithsomemisclassifications.Asillustratedin
Fig11(b),11(c),11(e),11(f),thereareadditionallysomemisidentificationsinRandomForest,
DecisionTree,BaggingClassifier,andAdaBoost.Forthemodel,the“eMBB”communication
servicewasmisclassifiedasURLLC,witha40–45instancerange.
Fig12alsoshowstheclassificationreportforeachmodelinadditiontothelearningcurve.
Alltheclassifier’sresultsarebeingshown.Inbetween,fromFig12(b),12(c),12(e),12(f),
therandomforest,decisiontree,baggingclassifier,andAdaBoostrelativelyshowlessper-
formancethantheothertwomodelsshowninFig12(a),12(d).Theprecision,recall,and
f1-scorefortheKNNofmMTCclassis78%,whichismuchhigherthantheotheradjacent
models.TheperformancemetricsforthedecisiontreeandAdaBoostarerelativelylowerwith
thevaluesof66%–67%rangeofprecision,recall,andF1-scorefortheURLLCclass.
6.3 DLresults
TheconfusionmatrixoftheproposedmodelprovidesusefulinformationonhowtheDNF
model,MLPmodel,andrecentlyintroducedmodelperform.Accordingtotheresearch,there
aremisclassifications,particularlythepredictedcommunicationservicesinFig13.Several
misclassificationsarefoundintheDNFmodel,includingtheincorrectcategorizationof
“mMTC”and“URLLC”services.Despitetheseerrorsinclassification,thesuggestedmodel
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 19/38

ID:pone.0333286 — 2025/10/16 — page 20 — #20
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig9.TrainingLossofVAE.
https://doi.org/10.1371/journal.pone.0333286.g009
outperformedothers.Therearesignificantlyfewermisclassificationsofcommunicationser-
vicesduetotheproposedmodel’saccuracyinidentifyinganddifferentiatingthem.Our
proposedmodelproperlyidentifieseachcommunicationserviceasoneoftheslicedtarget
labels.
Foreachmodel,Fig13displaystheclassificationreportbyclasstogetherwiththerelevant
confusionmatricesdiscoveredduringmodeltraining.AccordingtotheDNFmodel,thepre-
cisionandf1-scoreofthemMTCclassaremuchlowerthanthoseoftheothertwoclasses.
Accordingly,theDNFmodelhasdifficultycorrectlycategorizingcasesthatfallunderthe
“mMTC”category.The“URLLC”classalsoperformspoorlyintheDNFmodel,suggesting
itmaybedifficulttodistinguish“URLLC”instancesfromothers.Toclassify“mMTC”and
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 20/38

ID:pone.0333286 — 2025/10/16 — page 21 — #21
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig10.LearningcurvesfortheMLmodels.Learningcurvesdemonstratemodelstabilitywithincreasingdata,criticalfordynamicslicingwheretrafficpatternsevolve
formachinelearningmodels.
https://doi.org/10.1371/journal.pone.0333286.g010
“URLLC”communicationservicesappropriately,theDNFmodelneedstobefurtherdevel-
oped.AsimilarsetofperformanceissuescanalsobeseenintheMLPmodelforthe“mMTC”
class.AscomparedtootherclassesintheMLPmodel,the“mMTC”classshowsrecalland
f1-scorearenoticeablylower.Therefore,theMLPmodelmayhavedifficultyidentifyingcases
thatfallunderthe“mMTC”category.However,theproposedmodeloutperformsthepre-
viousmodelsintermsofprecision,recall,andf1scores,indicatingthatimprovementsare
neededtoproperlycategorize“mMTC”communicationservices.Accordingtotheproposed
model,the“mMTC”classhasahigherf1scorethantheotherclasses.
Thetrainingprogressover30epochswithearlystoppingisshowninFig14,alongwith
theaccuracyandlosscurvesforthechosenmodels.Throughtheanalysisofthesecurves,we
canbetterunderstandtheDNFmodel,theMLPmodel,andourproposedmodel.TheDNF
model’strainingaccuracycurvereaches64%,butoscillationsindicateinstabilityduetolocal
maximainteractionsandlimitedgeneralizationabilitieswithtrainingandvalidationdata.
Incontrast,thetrainingandvalidationaccuracycurvesoftheMLPmodelshowfairresults
afterobtainingatrainingaccuracyof65%,thegraphsindicateapositiveincreasingtrend,
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 21/38

ID:pone.0333286 — 2025/10/16 — page 22 — #22
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig11.ConfusionMatricesfortheMLmodels.
https://doi.org/10.1371/journal.pone.0333286.g011
indicatingthatthemodelissteadilyimprovingitsresultsonboththetrainingandvalidation
datathanothermodels.Ourproposedmodelshowspromisingresultsbasedontheaccu-
racycurves.Trainingandvalidationcurvesshowpositivetrends,indicatingconsistencyin
accuracygainsovertime.
6.4 Performancecomparisonofalgorithmsandmodels
Inourcomparisonresearch,weapplyasetofmodelstotesttheeffectivenessofourproposed
modelinidentifyingthreeseparatecommunicationservices:eMBB,URLLC,andmMTC.
ThemodelsunderexaminationincludeKNN,RandomForest,DecisionTree,GaussianNB,
Bagging,AdaBoost,DecisionForestTree,andMLP.Thesemodelsareselectedbasedontheir
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 22/38

ID:pone.0333286 — 2025/10/16 — page 23 — #23
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig12.ClassificationReportfortheMLmodels.
https://doi.org/10.1371/journal.pone.0333286.g012
shownefficacyinarangeofcategorizationtasks,asillustratedinFig15.Inaddition,Fig16
showsaplotwithmodelsonthex-axisandscoresonthey-axis.Theplot’sthreelinesshow
theprecision,recall,andF1scoresforeachmodel.Ourproposedmodelappearstobemost
effectiveinallthreecriteria(precision,recall,andF1).TheRandomForest,AdaBoost,and
BaggingClassifiermodelsalsoperformwell,withscoresnearlyidenticaltooneanotherand
slightlyover0.7forthemajorityofstandards.TheGaussianNBandDNFappeartoperform
muchlessthantheothers.Toimproveaccuracyandusethedistinctcapabilitiesofindepen-
dentmodels,ourproposedmodelisintendedforrobustfeatureextractionandclassification
applicationsintheINBSIsystem.WefurthervisualizethefeaturedistributionsofourINBSI
modelusing2Dand3Dprincipalcomponentanalysis(PCA)andt-distributedstochastic
neighborembedding(t-SNE)plots.Inthe2Dand3DPCAplots,networkslicesformdistinct
clusters,showingthatthemodeleffectivelycaptureskeyfeatureslikebandwidth,latency,and
packetloss.MinimaloverlapindicatesstrongslicedifferentiationshowninFigs17and18.
The2Dand3Dt-SNEplotsfurtherconfirmthis,withwell-separatedclustersdemonstrat-
ingthemodel’sabilitytolearnmeaningfulrepresentations.Theclearseparabilityhighlights
theeffectivenessofourCNN-basedfeatureextractionandinterpretabilitytools.Therefore,
ourproposedmodeladaptswelltounexpectedvalidationdataandlearnseffectivelyfromthe
trainingdata.Onboththetrainingandvalidationdatasets.
Experimentresults,whichareshowninTable4,illustratethatthesemodelsareeffective
atsolvingthestatedfunction.KNNachieveda76%accuracyrate,demonstratingitscapacity
todiscoverpatternsindatasets.BoththeRandomForestandDecisionTreemodelsachieved
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 23/38

ID:pone.0333286 — 2025/10/16 — page 24 — #24
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig13.ConfusionMatrixandClassificationreportforDLmodelsandProposedCNNModel.
https://doi.org/10.1371/journal.pone.0333286.g013
69%accuracy,demonstratingtheirabilitytodealwithdifficultdecisionboundaries.Gaus-
sianNBobtained55%accuracy,demonstratingthechallenge’slimitations.
Theensemble-basedlearningaccuracyofBaggingClassifierandAdaBoostishigh,while
theDNFmodelobtains65%accuracy.TheMLPmodelcapturescomplexinformationrela-
tionshipswith72%accuracy.
Table5comparestheinferencetimesoftwoneuralnetworkmodels,highlightingtheeffi-
ciencyoftheproposedapproach.TheNADAM-optimizedCNNachievesthelowestinfer-
encetimeof3.41milliseconds,significantlyoutperformingthestandardMLP,whichrequires
5.82milliseconds.ThisimprovementunderscorestheeffectivenessofusingtheNesterov-
acceleratedAdaptiveMomentEstimation(NADAM)optimizerinenhancingmodeleffi-
ciency,makingtheproposedCNNarchitecturemoresuitableforreal-timeorresource-
constrainedapplications.Besides,theproposedNADAMOptimizedCNNmodeldemon-
stratesstatisticallysignificantimprovementoverMLPandDNN,withthelowestp-value
(0.012)andhighestchi-squarescore(6.89).Theseresultsconfirmthesuperiorreliabilityand
performanceconsistencyoftheproposedarchitectureinTable6.
6.5 Interpretedresultsandinsights
6.5.1 LIME. Inthissection,welookattheLIMEexplanations.Figs19and20depictthese
explanationsinthreesections:predictionprobabilitiesforallpossibleoutputs,barcharts
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 24/38

| ID:pone.0333286 | — 2025/10/16 | — page 25 | — #25 |
| --------------- | ------------ | --------- | ----- |
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig14.TrainingaccuracyandlosscurvesfortheDLmodelswithourproposedmodel.
https://doi.org/10.1371/journal.pone.0333286.g014
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 25/38

ID:pone.0333286 — 2025/10/16 — page 26 — #26
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig15.Comparisonofthemodels.
https://doi.org/10.1371/journal.pone.0333286.g015
Fig16.Achievedscoresofthesemodelsbasedonperformancemetrics.
https://doi.org/10.1371/journal.pone.0333286.g016
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 26/38

ID:pone.0333286 — 2025/10/16 — page 27 — #27
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig17.2DPCAandt-SNEplotsshowingdistinctclustersfornetworkslices,indicatingeffectivefeatureextractionand
slicedifferentiationbytheINBSImodel.
https://doi.org/10.1371/journal.pone.0333286.g017
Fig18.3DPCAandt-SNEplotsdemonstratingwell-separatedclustersfornetworkslices,furthervalidatingtheINBSImodel’sabilitytolearn
meaningful,discriminativefeaturerepresentations.
https://doi.org/10.1371/journal.pone.0333286.g018
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 27/38

| ID:pone.0333286 | — 2025/10/16 | — page | 28 — #28 |     |     |
| --------------- | ------------ | ------ | -------- | --- | --- |
PLOS One Optimizingnetworkbandwidthslicingidentification
Table4.Comparisonofthemodels.
| Model | Acc(%) |     | Precision | Recall | F-1 |
| ----- | ------ | --- | --------- | ------ | --- |
TraditionalMLModels
| KNN               | 76  |     | 0.76 | 0.76 | 0.76  |
| ----------------- | --- | --- | ---- | ---- | ----- |
| RandomForest      | 69  |     | 0.70 | 0.70 | 0.70  |
| DecisionTree      | 69  |     | 0.71 | 0.70 | 0.702 |
| GaussianNB        | 55  |     | 0.40 | 0.67 | 0.47  |
| BaggingClassifier | 70  |     | 0.71 | 0.70 | 0.71  |
| AdaBoost          | 69  |     | 0.70 | 0.70 | 0.70  |
NeuralNetworkModels
| DeepNeuralForest | 65  |     | 0.63 | 0.66 | 0.63 |
| ---------------- | --- | --- | ---- | ---- | ---- |
| MLP              | 72  |     | 0.75 | 0.71 | 0.70 |
ProposedModel
| NADAMOptimizedCNN | 84  |     | 0.86 | 0.84 | 0.84 |
| ----------------- | --- | --- | ---- | ---- | ---- |
https://doi.org/10.1371/journal.pone.0333286.t004
Table5.InferenceTimeComparisonofModels(LowerisBetter)
| Model |     |     | InferenceTime(ms) |     |     |
| ----- | --- | --- | ----------------- | --- | --- |
NeuralNetworkModels
| MLP                         |     |     | 5.82 |     |     |
| --------------------------- | --- | --- | ---- | --- | --- |
| NADAMOptimizedCNN(Proposed) |     |     | 3.41 |     |     |
https://doi.org/10.1371/journal.pone.0333286.t005
Table6.StatisticalAnalysisofModelPerformance
| Model |     |     | p-value | Chi-square(𝜒2) |     |
| ----- | --- | --- | ------- | -------------- | --- |
NeuralNetworkModels
| MLP                         |     |     | 0.037 | 4.32 |     |
| --------------------------- | --- | --- | ----- | ---- | --- |
| DNN                         |     |     | 0.024 | 5.16 |     |
| NADAMOptimizedCNN(Proposed) |     |     | 0.012 | 6.89 |     |
https://doi.org/10.1371/journal.pone.0333286.t006
illustratingfeatureweightsandcontributions,andafeaturevaluetable.The“1”labeledside
mainlyfocusesonthecorrectpredictionbasedontheinputfeature’simportance,and“NOT
1”doesviceversa.Thedecisiontreeclassifierproperlypredictedtheoutcomeforaspecific
inputdatapoint,asshowninFig19,andtheMLPclassifierforFig22.
Thepredictionprobabilityforthetargetfeature“eMBB”is1.00,indicatinghighconfidence
inthisprediction.Theoddsfortheothertwotargetqualities,ontheotherhand,are0.00,
meaningthattheywillnotbeexpectedoutcomes.Thisgivesanaccuratepredictionalloca-
tionforthenetworkinfrastructure.ThefeaturevaluetablerevealstheDecisionTreeclassi-
fier’saccuracy,withbluevaluessupporting“URLLC”andwhitevaluessupportingtheoppo-
siteprediction.Bluemarksindicatethetargetslice,whilewhitecolorsindicateotherslicing.
Features“eMBB”and“mMTC”accuratelyidentifyoutputs.Thepredictedoutput“URLLC”
isaccuratelyclassifiedbythe“LTE/5GUECategory”and“Time”featurevalues.However,
theparameters“TechnologySupported”and“PacketLossRate”negativelyimpactthepre-
diction,suggestingalternativecommunicationserviceslikeeMBBormMTC.Usingthetop
fiveattributesinFig20(b),weinvestigatetheprojectedoutputdeeper.Asaresult,thechar-
acteristic“2”as“mMTC”whichsymbolizes“mMTC”iscorrectlydiscovered.“PacketLoss
Rate(Reliability)”and“LTE/5GUECategory(Input2)”asTheLong-TermEvolution(LTE)
areimpactfactorfeatures,with“LTE/5GUECategory(Input2)”havingavalueof10.00.In
contrast,thefeature“TechnologySupported(Input3)”hasanegativeimpactfactorwitha
valuelessextensivethanthethreshold,precisely–0.67.
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 28/38

ID:pone.0333286 — 2025/10/16 — page 29 — #29
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig19.LIMEinterpretabilitywithdecisiontree.
https://doi.org/10.1371/journal.pone.0333286.g019
Fig20.LIMEinterpretabilitywithourproposedCNN.
https://doi.org/10.1371/journal.pone.0333286.g020
WeadditionallyemploytheLIMEwithMLPmethod,asshowninFig21.TheLIME
withMLPapproachisusedinthestudytoevaluateclasslabelpredictionsusinginput
features,withafocuson“TechnologySupported”measuresforCNNmodelstoensureaccu-
rateslicedistributionbyknowingthecorrecttypeconfigurationforindividualusersinthe
system.
TheLIMEexplanationrevealsthatourproposedmodel21predictsmMTC(1.00proba-
bility)withhighconfidence,drivenprimarilybythePacketDelayBudget(latency=300.00,
contribution:0.32)andTechnologySupported(contribution:0.23),whilePacketLossRate
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 29/38

ID:pone.0333286 — 2025/10/16 — page 30 — #30
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig21.LIMEinterpretibilitywithMLP.
https://doi.org/10.1371/journal.pone.0333286.g021
(0.01value,contribution:0.14)alsoplaysasupportingrole.FeatureslikeUseCaseType(5.00
value)andQCI(65.00)alignwithmMTC’sprofile(e.g.,toleranttolatencybutsensitiveto
interference).Incontrast,negligiblecontributionsfromTime(0.01),Day(0.01),andUE
Category(0.00)confirmtheyhadlittleimpactontheprediction.Thisbreakdownvalidates
themodel’sfocusonlatencyandreliabilitymetricsformMTCclassification,consistentwith
typicalIoTnetworkbehavior.
6.5.2 SHAP. SHAPisusedtoinferthemodel’spredictions.Inadditiontomakinguse
ofShapleyvalues,theSHAPlibraryprovidesapowerfultoolforexamininghowdifferent
variablesaffectthemodel’spredictions.SHAPranksfeaturesbasedonaverageSHAPvalues,
highlightingthosethatarecrucialformodelprediction.Fig22(b)showsamoredetailed
breakdownofhoweachattributeaffectscertainoutcomelabels.OntheY-axis,featuresare
listedaccordingtotheiraverageabsoluteSHAPvalues.ThevaluesontheX-axisrepresent
SHAPvaluesthathavethegreatestimpactonmodeloutput.Fromonecorrelationtoanother,
Fig22.SHAPfeatureimportanceandsummaryplotofproposedCNN.
https://doi.org/10.1371/journal.pone.0333286.g022
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 30/38

ID:pone.0333286 — 2025/10/16 — page 31 — #31
PLOS One Optimizingnetworkbandwidthslicingidentification
thepredictedvalueonthespecificfeatureisderivedfromthecentralzerovalue.Positiveval-
uesforaparticularcharacteristicmovethepredictionofthemodelclosertothelabelbeing
considered,whichcanbedescribedashighlycorrelated.InFig23,the“TechnologySup-
ported”and“PacketLossRate”featuresindicateahigherlikelihoodofinfluencingslicecom-
municationdistribution.Basedonthesecommunicationprotocols,themodelcanprecisely
distributetheappropriateslice-typeservicetothespecificapplication.
Besides,inFig24,thedecision-makingprocessofourSHAPmodel,whereweuse
XGBoostasabaseclassifier,isrepresentedasatreestructure,whereeachnodecorresponds
toafeaturesplit.Forinstance,themodelfirstevaluatesthe“PacketLossRate(Reliability)”
feature,determiningwhetheritexceedsaspecificthreshold.Basedonthisdecision,thepro-
cessproceedstotheappropriatebranchuntilafinalclassificationisreached.Byapplying
SHAPtothismodel,wecanquantifythecontributionofeachfeaturetoagivenprediction,
providinginsightsintotheclassifier’sdecision-makingprocess.
Finally,weevaluateourmodelwiththeproposedapproach,whichisshowninFig25.
TheSHAPanalysisrevealsthatUseCaseType(Input1),PacketLossRate(Reliability),
andPacketDelayBudget(Latency)arethemostinfluentialfeaturesinthemodel,withthe
Fig23.SHAPfeatureimportanceandsummaryplotofproposedCNNmodel.
https://doi.org/10.1371/journal.pone.0333286.g023
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 31/38

ID:pone.0333286 — 2025/10/16 — page 32 — #32
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig24.Thetree-structuredoutputoftheXGBoostclassifierontheSHAPmodel.
https://doi.org/10.1371/journal.pone.0333286.g024
highestmeanabsoluteSHAPvalues,indicatingtheirstrongimpactonpredictions.Features
likeTechnologySupported(Input3)andLTE/5GUECategory(Input2)contributemoder-
ately,whileDay(Input4),Time(Input5),andOCI(Input6)haverelativelyminoreffects.
Thissuggeststhatnetworkperformancepredictionsareprimarilydrivenbyapplication
requirements(URLLC/eMBB/mMTC)andquality-of-servicemetrics(lossrate,delay),while
temporalandinterferencefactorsplaylesserroles.Theresultsalignwithexpectednetwork
behavior,validatingthemodel’sinterpretability.
7 Use scenarios and performance assessment
of the proposed model
Whenledbypredictions,loadbalancingcanoptimizeresourceallocation,reducecongestion,
andimproveuserexperiences.Basedonthescenario,Fig25primarilydepictsourtrained
proposedmodelusedtosimulateloadbalancingdynamicallyacrossvariousnetworkservice
typesusingthegiveninputfeatures.Wetakesomeapplicationsasdefinedinthe“UseCase-
Type”inputfeature.Foreachapplication,wesimulatetheresultsbyupdatingtheloadfor
eachslicetype.Forexample,SmartHome,Smartphone,IoTDevices,IndustryIoT,AR/VR
Gaming,andHealthcare.Fig25(a)showstheloadbalancingscenarioforSmartHome.Based
onthenumberofusers,theapplicationchangesitsservicetypeovertime,andthisishap-
peningduetothecontributionofourproposedmodel.Samecasesforotherscenariosin
Fig25(b),25(c),25(d),25(e),and25(f).Itillustratestheoutcomesoftheload-balancing
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 32/38

ID:pone.0333286 — 2025/10/16 — page 33 — #33
PLOS One Optimizingnetworkbandwidthslicingidentification
Fig25.SlicedistributionusingourproposedhybridCNNmodel.
https://doi.org/10.1371/journal.pone.0333286.g025
simulation.Over24hours,theoutputshowstheloadvaluesasthenumberofactiveusersfor
eachservicetype(eMBB,mMTC,andURLLC).Thevariationsinloadlevelsanticipatedby
themodelreflecttheprobablebenefitsofloadbalancing.Notably,atpeakhours,thecount
ofloadnumbersforeMBBandmMTCclimbsubstantially,demonstratingeffectiveloaddis-
tribution.Theproposedmodelefficientlycontrolsworkloaddistributionamongapplica-
tionslicesintheINBSIsystemenvironment,takingintoconsiderationbothdemandand
timelimits.Thissystemconstantlyreviewsserviceperformancebydynamicallychanging
slicesdependingonvaryingloadconditions,efficientlyoptimizingresourceallocationacross
high-loadandlow-loadscenarios.
Weprovidethe“AdvancedSlicingDistributionProcess”inAlgorithm1fortheINBSI
systempipeline,whichoutlinestheproceduresforinitializingtheproposedmodel,ini-
tializingsliceservices,andhandlinguserdemandserviceswithrequirementparame-
ters.ThisapproachiterativelyinitializesaVAE,examinesuserdata,customizesmodelsif
necessary,predictsslicetypes,andinterpretsuserinputforasetnumberofrequests.Addi-
tionally,ithandlesadditionalrequestsandmodifiesresourceallocationbasedonsystem
load.
Wefurthercompareourapproach,specificallywithVAE,foranomalydetectionandinter-
pretationtestingusingLIMEandSHAP,asshowninTable7.Theexistingapproachesby
Syedetal.,Ramrajetal.,Nehaetal.,andSowmyaetal.donotincorporateeitherVAEorXAI
techniques,limitingtheirabilitytoenhancedatavalidityandinterpretmodeldecisions.In
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 33/38

| ID:pone.0333286 | — 2025/10/16 | — page 34 | — #34 |     |
| --------------- | ------------ | --------- | ----- | --- |
PLOS One Optimizingnetworkbandwidthslicingidentification
Algorithm1.AdvancedslicingdistributionprocessinINBSIpipeline.
| 1: InitializetheproposedmodelM |     | proposed |     |     |
| ------------------------------ | --- | -------- | --- | --- |
InitializesliceservicesS
| 2:  |     | service |     |     |
| --- | --- | ------- | --- | --- |
(p )withrequirementparameters
| 3: UserdemandserviceR |     | ,…,p |     |     |
| --------------------- | --- | ---- | --- | --- |
user 1 n
| fori=1toN | do       |     |     |     |
| --------- | -------- | --- | --- | --- |
| 4:        | requests |     |     |     |
(i)
InitializeVAEmodelV
| 5:  |     | VAE |     |     |
| --- | --- | --- | --- | --- |
forj=1toN
| 6:  |     | do  |     |     |
| --- | --- | --- | --- | --- |
requests
|     | .validate(V | ( i ) ) |     |     |
| --- | ----------- | ------- | --- | --- |
| 7:  | U           |         |     |     |
|     | data        | V A E   |     |     |
foreachuseru∈U
| 8:  |                                   | data do |      |     |
| --- | --------------------------------- | ------- | ---- | --- |
| 9:  | if userhasspecialrequirementsthen |         |      |     |
|     | ←customize(U                      |         | )    |     |
| 10: | u model                           |         | data |     |
else
11:
←train(U )
| 12: | u              |          |     |     |
| --- | -------------- | -------- | --- | --- |
|     | model          | data     |     |     |
| 13: | endif          |          |     |     |
| 14: | y ̂ ←predict(S | )        |     |     |
|     | s lice         | type     |     |     |
|     | ←interpret(y   | )        |     |     |
| 15: | U data         | s ̂ lice |     |     |
endfor
16:
17: endfor
18: Userssendupdatestoapplications
| 19: if additionalrequestspendingN |     |     | >0then |     |
| --------------------------------- | --- | --- | ------ | --- |
pending
| 20: | handleAdditionalRequests() |     |     |     |
| --- | -------------------------- | --- | --- | --- |
endif
21:
>T
| 22: if systemloadL |                            | then |     |     |
| ------------------ | -------------------------- | ---- | --- | --- |
|                    | system                     | load |     |     |
| 23:                | adjustResourceAllocation() |      |     |     |
24: endif
25: endfor
Table7.Modelcomparisonused.
| Model               |     | VAEUsed |     | XAIUsed |
| ------------------- | --- | ------- | --- | ------- |
| Syedetal.[32]       |     | 7       |     | 7       |
| Ramrajetal.[33]     |     | 7       |     | 7       |
| Nehaetal.[34]       |     | 7       |     | 7       |
| Sowmyaetal.[35]     |     | 7       |     | 7       |
| OurProposedApproach |     | ✓       |     | ✓       |
https://doi.org/10.1371/journal.pone.0333286.t007
contrast,ourproposedapproachintegratesbothVAEandXAI,ensuringimproveddata
reconstruction,anomalydetection,andinterpretability,whichcollectivelycontributetoa
morerobustandtransparentnetworkslicingclassificationsystem.
7.1 Limitations
WhilethisstudyaddressesclassimbalanceusingSMOTEandensuresdataprivacythrough
anonymization,futureresearchshouldexploredynamicimbalancemitigationtechniques
thatadapttotheevolvingtrafficpatternsin5Gandemerging6Genvironments—particularly
throughadaptiveresamplingmethodssensitivetotemporalslicedemandfluctuations.Eth-
icalrobustnesscanbefurtherstrengthenedbyemployingfederatedlearningtodecentralize
theprocessingofsensitivedata,coupledwithdifferentialprivacytechniquestosafeguard
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 34/38

ID:pone.0333286 — 2025/10/16 — page 35 — #35
PLOS One Optimizingnetworkbandwidthslicingidentification
slice-levelanalytics,especiallyasglobalregulatoryframeworksliketheEUAIActcontinue
toevolve.Intermsofcomputationalefficiency,incorporatingquantum-inspiredoptimiza-
tion[51]strategiescouldsignificantlyenhancethescalabilityandresponsivenessofnetwork
slicingmechanisms,offeringapromisingavenueforaddressingcomplexresourceallocation
challenges.Furthermore,analyzingtheenergy-efficiencytrade-offsoflightweightAImodels
inedgeenvironmentsandensuringtheircompatibilitywithzero-trustarchitecturesdefined
bystandardizationbodiessuchas3GPPwouldpromotebothsustainabilityandsecurity.
Finally,groundingtheseadvancementswithinthebroadercontextoffuturenetworkvisions
underscoresthenecessityofdesigningAIsystemsthatarenotonlytechnicallycapablebut
alsoalignedwithlong-termindustrytrajectoriesandsocietalexpectations.
8 Conclusion and future work
Networkslicingisconsideredtoplayanimportantroleinfuturegenerationsofcommunica-
tionnetworks.Modernwirelessnetworks’communicationmechanismsareshapedbymath-
ematicalmodelsthatfrequentlylackaccuracy.Toextractfeaturesandclassifynetworkslices,
weusedourlightweight,tailored,optimizedCNNmodel,makingitsuitedforefficientslice
distributionwhileensuringloadbalancinginourINBSIsystem.WithVAE,networkslic-
ingserviceefficiencycouldbeevaluatedalongwithfaultdetectionandrecovery,andLIME
andSHAPtechniqueshelpedshedlightonthedecision-makingprocessandhighlightedspe-
cificinputrequirements.Wecontributedtothedevelopmentofnetwork-slicingtechnolo-
giesandguidednetworkoperatorstoimprovetheirutilizationplansthroughtheresultsof
ourresearch.TheproposedmethodimprovesnetworkslicingthroughVAEsforanomaly
detection,CNNwithNADAMoptimization,andinterpretableAIapproaches;yet,numer-
ousproblemspersist.ThecomputationalcomplexityofVAEsmayimpedereal-timeimple-
mentation,necessitatingmodelcompressionorhardwareacceleration.Scalabilityisacritical
issue,aseffectiveresourceallocationisessentialforextensive5Gnetworks.Securitycontin-
uestobeasignificantchallenge,especiallyinsafeguardingsensitiveinformation.Federated
learningcanreduceprivacyissues;nevertheless,italsopresentsvulnerabilitiestomodelpoi-
soningattacks.Robustencryptiontechniques,includinghomomorphicencryption,areessen-
tialforimprovingdatasecuritywhilemaintainingefficiency.Futureendeavorswillconcen-
trateonenhancingefficiency,scalability,encryption-basedsecurity,andresilientfederated
learning.
Author contributions
Conceptualization:NafeesMansoor,AmitabhaChakrabarty.
Formalanalysis:MdFahimUlIslam.
Fundingacquisition:AmitabhaChakrabarty.
Methodology:ShahriarHossain,GolamRabiulAlam.
Resources:GolamRabiulAlam,NafeesMansoor.
Software:MdFahimUlIslam,ShahriarHossain.
Supervision:AmitabhaChakrabarty.
Validation:ShahriarHossain.
Visualization:ShahriarHossain.
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 35/38

ID:pone.0333286 — 2025/10/16 — page 36 — #36
PLOS One Optimizingnetworkbandwidthslicingidentification
Writing–originaldraft:MdFahimUlIslam.
Writing–review&editing:GolamRabiulAlam,AmitabhaChakrabarty.
References
1. GökhanNalbantK,AlsuhibanySA,HassanAlshehriA,HatiraM,ChoiBJ.Anintelligentalgorithm
forenergyefficiencyoptimizationinsoftware-definedwirelesssensornetworksfor5G
communications.PLoSOne.2024;19(6):e0301078.https://doi.org/10.1371/journal.pone.0301078
PMID:38900762
2. KovtunV,GrochlaK,ZaitsevaE,LevashenkoV.Theconceptofoptimalplanningofalinearly
orientedsegmentofthe5Gnetwork.PLoSOne.2024;19(4):e0299000.
https://doi.org/10.1371/journal.pone.0299000PMID:38630761
3. IslamS,ZainabAbdulsalamA,AnilKumarB,KamrulHasanM,KolandaisamyR,SafieN.Mobile
networkstoward5G/6G:networkarchitecture,opportunitiesandchallengesinsmartcity.IEEE
OpenJCommunSoc.2025;6:3082–93.https://doi.org/10.1109/ojcoms.2024.3419791
4. HuangJ,YangF,ChakrabortyC,GuoZ,ZhangH,ZhenL,etal.Opportunisticcapacitybased
resourceallocationfor6Gwirelesssystemswithnetworkslicing.FutureGenerationComputer
Systems.2023;140:390–401.https://doi.org/10.1016/j.future.2022.10.032
5. LiuY,ClerckxB,PopovskiP.NetworkslicingforeMBB,URLLC,andmMTC:anuplinkrate-splitting
multipleaccessapproach.IEEETransWirelessCommun.2024;23(3):2140–52.
https://doi.org/10.1109/twc.2023.3295804
6. DonattiA,CorreaSL,MartinsJS,AbelemA,BothCB,SilvaF,CarvalhoTC.Surveyonmachine
learning-enablednetworkslicing:coveringtheentirelifecycle.IEEETransactionsonNetworkand
ServiceManagement.2024p.1–18.
7. AmmarS,PongLauC,ShihadaB.Anin-depthsurveyonvirtualizationtechnologiesin6G
integratedterrestrialandnon-terrestrialnetworks.IEEEOpenJCommunSoc.2024;5:3690–734.
https://doi.org/10.1109/ojcoms.2024.3414622
8. PolónioJ,MouraJ,MarinheiroRN.Ontheroadtoproactivevulnerabilityanalysisandmitigation
leveragedbysoftwaredefinednetworks:asystematicreview.IEEEAccess.2024.
9. BotezR,PascaA-G,SferleA-T,IvanciuI-A,DobrotaV.EfficientnetworkslicingwithSDNand
heuristicalgorithmforlowlatencyservicesin5G/B5Gnetworks.Sensors(Basel).
2023;23(13):6053.https://doi.org/10.3390/s23136053PMID:37447902
10. LiuY,ClerckxB,PopovskiP.NetworkslicingforeMBB,URLLC,andmMTC:anuplinkrate-splitting
multipleaccessapproach.IEEETransWirelessCommun.2024;23(3):2140–52.
https://doi.org/10.1109/twc.2023.3295804
11. AmerA,HoteitS,Ben-OthmanJ.Resourceallocationforenabled-network-slicingincooperative
noma-basedsystemswithunderlayD2Dcommunications.In:2023IEEEInternationalConference
onCommunications(ICC),Rome,Italy,2023.p.1–6.
12. GharehgoliA,NouruziA,MokariN,AzmiP,JavanMR,JorswieckEA.AI-basedresourceallocation
inend-to-endnetworkslicingunderdemandandCSIuncertainties.IEEETransNetwServManage.
2023;20(3):3630–51.https://doi.org/10.1109/tnsm.2023.3243837
13. GuptaRK,MahajanS,MisraR.ResourceorchestrationinnetworkslicingusingGAN-based
distributionaldeepQ-networkforindustrialapplications.JSupercomput.2022;79(5):5109–38.
https://doi.org/10.1007/s11227-022-04867-9
14. DangiR,LalwaniP.Harrishawksoptimizationbasedhybriddeeplearningmodelforefficient
networkslicingin5Gnetwork.ClusterComput.2023.p.1–15.
15. MartinsJS,CarvalhoTC,MoreiraR,BothC,DonattiA,CorrêaJH,etal.Enhancingnetworkslicing
architectureswithmachinelearning,security,sustainabilityandexperimentalnetworksintegration.
IEEEAccess.2023;11:1–20.
16. SoudNS,Al-JamaliNAS,Al-RaweshidyHS.ModeratelymultispikereturnneuralnetworkforSDN
accuratetrafficawarenessineffective5Gnetworkslicing.IEEEAccess.2022;10:1–10.
17. IannelliM,RahmanMR,ChoiN,WangL.Applyingmachinelearningtoend-to-endsliceSLA
decomposition.In:20206thIEEEConferenceonNetworkSoftwarization(NetSoft).2020.p.92–9.
https://doi.org/10.1109/netsoft48620.2020.9165317
18. WijethilakaS,LiyanageM.Surveyonnetworkslicingforinternetofthingsrealizationin5G
networks.IEEECommunSurvTutorials.2021;23(2):957–94.
https://doi.org/10.1109/comst.2021.3067807
19. Chinchilla-RomeroL,Prados-GarzonJ,AmeigeirasP,MuñozP,Lopez-SolerJM.5GInfrastructure
networkslicing:E2Emeandelaymodelandeffectivenessassessmenttoreducedowntimesin
Industry4.0.Sensors(Basel).2021;22(1):229.https://doi.org/10.3390/s22010229PMID:35009771
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 36/38

ID:pone.0333286 — 2025/10/16 — page 37 — #37
PLOS One Optimizingnetworkbandwidthslicingidentification
20. WijethilakaS,LiyanageM.SurveyonnetworkslicingforInternetofThingsrealizationin5G
networks.IEEECommunSurvTutorials.2021;23(2):957–94.
https://doi.org/10.1109/comst.2021.3067807
21. BhattacharjeeS,KatsalisK,AroukO,SchmidtR,WangT,AnX,etal.networkslicingfor
TSN-basedtransportnetworks.IEEEAccess.
2021;9:62788–809.https://doi.org/10.1109/access.2021.3074802
22. ThantharateA,BeardC.ADAPTIVE6G:adaptiveresourcemanagementfornetworkslicing
architecturesincurrent5Gandfuture6Gsystems.JNetwSystManage.
2022;31(1):1–24.https://doi.org/10.1007/s10922-022-09693-1
23. KhanS,KhanS,AliY,KhalidM,UllahZ,MumtazS.Highlyaccurateandreliablewirelessnetwork
slicingin5thgenerationnetworks:ahybriddeeplearningapproach.JNetwSystManage.
2022;30(2).https://doi.org/10.1007/s10922-021-09636-2
24. AbedinSF,BairagiAK,MunirMdS,TranNH,HongCS.Fogloadbalancingformassivemachine
typecommunications:agameandtransporttheoreticapproach.IEEEAccess.2019;7:4204–18.
https://doi.org/10.1109/access.2018.2888869
25. AlsenwiM,TranNH,BennisM,KumarBairagiA,HongCS.eMBB-URLLCresourceslicing:a
risk-sensitiveapproach.IEEECommunLett.2019;23(4):740–3.
https://doi.org/10.1109/lcomm.2019.2900044
26. BairagiAK,MunirMdS,AlsenwiM,TranNH,AlshamraniSS,MasudM,etal.Coexistence
mechanismbetweeneMBBanduRLLCin5Gwirelessnetworks.IEEETransCommun.
2021;69(3):1736–49.https://doi.org/10.1109/tcomm.2020.3040307
27. AlsenwiM,TranNH,BennisM,PandeySR,BairagiAK,HongCS.Intelligentresourceslicingfor
eMBBandURLLCcoexistencein5Gandbeyond:adeepreinforcementlearningbasedapproach.
IEEETransWirelessCommun.2021;20(7):4585–600.https://doi.org/10.1109/twc.2021.3060514
28. ThantharateA,ParopkariR,WalunjV,BeardC.DeepSliceandSecure5G-5GandLTEwireless.
2019.
29. ThantharateA,ParopkariR,WalunjV,BeardC.DeepSlice:adeeplearningapproachtowardsan
efficientandreliablenetworkslicingin5Gnetworks.In:2019IEEE10thAnnualUbiquitous
Computing,Electronics&MobileCommunicationConference(UEMCON).2019.
https://doi.org/10.1109/uemcon47517.2019.8993066
30. ThantharateA,ParopkariR,WalunjV,BeardC,KankariyaP.Secure5G:adeeplearning
frameworktowardsasecurenetworkslicingin5Gandbeyond.In:202010thAnnualComputing
andCommunicationWorkshopandConference(CCWC).2020.
https://doi.org/10.1109/ccwc47524.2020.9031158
31. AnJ,ChoS.Variationalautoencoderbasedanomalydetectionusingreconstructionprobability.In:
SpeciallectureonIE.2015.p.1–18.
32. HassanSMHU,BrennanA,MunteanG-M,McManisJ.NSM2:networkslicemanagementand
monitoringusingmachinelearningforAR/VRapplications.In:2024IEEEInternationalSymposium
onBroadbandMultimediaSystemsandBroadcasting(BMSB).2024.p.1–7.
https://doi.org/10.1109/bmsb62888.2024.10608350
33. DangiR,LalwaniP.Optimizingnetworkslicingin6Gnetworksthroughahybriddeeplearning
strategy.JSupercomput.2024;80(14):20400–20.https://doi.org/10.1007/s11227-024-06238-y
34. ShuklaN,SiloiyaA,SinghA,SainiA.Xcelerate5G:optimizingresourceallocationstrategiesfor5g
networkusingml.In:2024.417–23.
35. PoojariThippeswamySN,RaghavanAP,RajgopalM,SujithA.Efficientnetworkmanagementand
securityin5Genabledinternetofthingsusingdeeplearningalgorithms.IJECE.2024;14(1):1058.
https://doi.org/10.11591/ijece.v14i1.pp1058-1070
36. ConnorM,CanalG,RozellC.Variationalautoencoderwithlearnedlatentstructure.In:24th
InternationalConferenceonArtificialIntelligenceandStatistics,2021.p.1–10.
37. KingmaDP,WellingM.Auto-encodingvariationalbayes.arXivpreprint2022.
https://arxiv.org/abs/1312.6114
38. ZhangS,LiX,ZongM,ZhuX,ChengD.LearningkforkNNClassification.ACMTransIntellSyst
Technol.2017;8(3):1–19.https://doi.org/10.1145/2990508
39. AsfawT.Performancecomparisonofk-nearestneighborsandGaussiannaïvebayesalgorithmsfor
heartdiseaseprediction.InternationalJournalofEngineeringScienceInvention(IJESI).
2012;8(8):45–8.
40. CutlerA,CutlerDR,StevensJR.Randomforests.EnsembleMachineLearning:Methodsand
Applications.2012;45:157–75.
41. SongY-Y,LuY.Decisiontreemethods:applicationsforclassificationandprediction.ShanghaiArch
Psychiatry.2015;27(2):130–5.https://doi.org/10.11919/j.issn.1002-0829.215044PMID:26120265
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 37/38

ID:pone.0333286 — 2025/10/16 — page 38 — #38
PLOS One Optimizingnetworkbandwidthslicingidentification
42. SandagGA.Apredictionmodelofcompanyhealthusingbaggingclassifier.JITK(JurnalIlmu
PengetahuanDanTeknologiKomputer).2020;6(1):41–6.
43. SchapireRE.ExplainingAdaBoost.Empiricalinference.Berlin,Heidelberg:Springer;2013.p.
37–52.https://doi.org/10.1007/978-3-642-41136-6_5
44. FreundY,SchapireRE.Adecision-theoreticgeneralizationofon-linelearningandanapplicationto
boosting.JournalofComputerandSystemSciences.1997;55(1):119–39.
https://doi.org/10.1006/jcss.1997.1504
45. KontschiederP,FiterauM,CriminisiA,BulòSR.Deepneuraldecisionforests.In:IEEE
InternationalConferenceonComputerVision,Santiago,Chile,2015.p.1–9.
46. TaudH,MasJF.Multilayerperceptron(MLP).Geomaticapproachesformodelinglandchange
scenarios.2018.p.451–5.
47. AldughayfiqB,AshfaqF,JhanjhiNZ,HumayunM.ExplainableAIforretinoblastomadiagnosis:
interpretingdeeplearningmodelswithLIMEandSHAP.Diagnostics(Basel).2023;13(11):1932.
https://doi.org/10.3390/diagnostics13111932PMID:37296784
48. RibeiroMT,SinghS,GuestrinC.WhyshouldItrustyou?Explainingthepredictionsofany
classifier.In:22ndACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandData
Mining,SanFrancisco,California,USA.2016.p.1135–44.
49. PradhanB,DikshitA,LeeS,KimH.AnexplainableAI(XAI)modelforlandslidesusceptibility
modeling.AppliedSoftComputing.2023;142:110324.https://doi.org/10.1016/j.asoc.2023.110324
50. ChenT,GuestrinC.Xgboost:Ascalabletreeboostingsystem.In:22ndACMSIGKDDInternational
ConferenceonKnowledgeDiscoveryandDataMining,NewYork,UnitedStates.2016.p.1–10.
51. LuY,YangJ.Quantumfinancingsystem:asurveyonquantumalgorithms,potentialscenariosand
openresearchissues.JournalofIndustrialInformationIntegration.2024;41:100663.
https://doi.org/10.1016/j.jii.2024.100663
52. LuY,NingX.Avisionof6G–5G’ssuccessor.JournalofManagementAnalytics.
2020;7(3):301–20.https://doi.org/10.1080/23270012.2020.1802622
PLOSOne https://doi.org/10.1371/journal.pone.0333286 October21,2025 38/38