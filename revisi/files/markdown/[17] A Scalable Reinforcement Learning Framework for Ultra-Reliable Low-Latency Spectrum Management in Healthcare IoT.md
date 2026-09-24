# [17] A Scalable Reinforcement Learning Framework for Ultra-Reliable Low-Latency Spectrum Management in Healthcare IoT

> Source file: `[17] A Scalable Reinforcement Learning Framework for Ultra-Reliable Low-Latency Spectrum Management in Healthcare IoT.pdf`

---

mathematics
Article
A Scalable Reinforcement Learning Framework for
Ultra-Reliable Low-Latency Spectrum Management in
Healthcare Internet of Things
AdeelIqbal1,† ,AliNauman1,* ,TahirKhurshaid2,† andSang-BongRhee2
1 SchoolofComputerScienceandEngineering,YeungnamUniversity,Gyeongsan-si38541,RepublicofKorea;
adeeliqbal@yu.ac.kr
2 DepartmentofElectricalEngineering,YeungnamUniversity,Gyeongsan-si38541,RepublicofKorea;
tahir@ynu.ac.kr(T.K.);rrsd@yu.ac.kr(S.-B.R.)
* Correspondence:anauman@ynu.ac.kr
† Theseauthorscontributedequallytothiswork.
Abstract
HealthcareInternetofThings(H-IoT)systemsdemandultra-reliableandlow-latencycom-
munication(URLLC)tosupportcriticalfunctionssuchasremotemonitoring,emergency
response,andreal-timediagnostics. However,spectrumscarcityandheterogeneoustraffic
patternsposemajorchallengesforcentralizedschedulingindenseH-IoTdeployments.
Thispaperproposedamulti-agentreinforcementlearning(MARL)frameworkfordynamic,
priority-awarespectrummanagement(PASM),wherecooperativeMARLagentsjointly
optimizethroughput,latency,energyefficiency,fairness,andblockingprobabilityunder
varyingtrafficandchannelconditions. Sixlearningstrategiesaredevelopedandcompared,
includingQ-Learning,DoubleQ-Learning,DeepQ-Network(DQN),Actor–Critic,Dueling
DQN,andProximalPolicyOptimization(PPO),withinasimulatedH-IoTenvironment
thatcapturesheterogeneoustraffic,devicepriorities,andrealisticURLLCconstraints. A
comprehensive simulation study across scalable scenarios ranging from 3to50devices
demonstratedthatPPOconsistentlyoutperformsallbaselines,improvingmeanthroughput
AcademicEditors:YingjieTian,
by6.2%,reducing95th-percentiledelayby11.5%,increasingenergyefficiencyby11.9%,
Cheng-ChiLee,AshutoshMishraand
ShodhanRao loweringblockingprobabilityby33.3%,andacceleratingconvergenceby75.8%compared
tothestrongestnon-PPObaseline. ThesefindingsestablishPPOasarobustandscalable
Received:23July2025
Revised:18August2025 solutionforQoS-compliantspectrummanagementindenseH-IoTenvironments,while
Accepted:9September2025 DuelingDQNemergesasacompetitivedeepRLalternative.
Published:11September2025
Citation: Iqbal,A.;Nauman,A.; Keywords: 5G;internetofthings;priority-awarespectrummanagement;reinforcement
Khurshaid,T.;Rhee,S.-B.AScalable learning;spectrumaccess;resourceallocation
ReinforcementLearningFramework
forUltra-ReliableLow-Latency MSC:68T05;68M10
SpectrumManagementinHealthcare
InternetofThings.Mathematics2025,
13,2941. https://doi.org/10.3390/
math13182941
1. Introduction
Copyright:©2025bytheauthors.
TheInternetofThings(IoT)hasrevolutionizedmodernhealthcarebyenablingcontin-
LicenseeMDPI,Basel,Switzerland.
uousmonitoring,precisediagnostics,andreal-timeinterventionsthroughinterconnected
Thisarticleisanopenaccessarticle
distributedunderthetermsand sensors and devices, as shown in Figure 1. Within this paradigm, Healthcare Internet
conditionsoftheCreativeCommons of Things (H-IoT) systems encompass diverse medical applications, ranging from vital
Attribution(CCBY)license signsmonitoringandglucosetrackingtoemergencyalertsandremoteconsultations,that
(https://creativecommons.org/
demandultra-reliableandlow-latencycommunication(URLLC)[1].
licenses/by/4.0/).
Mathematics2025,13,2941 https://doi.org/10.3390/math13182941

Mathematics2025,13,2941 2of27
Figure1.ApplicationsofHealthcareIoTsystems.
ThemassivedeploymentofH-IoTdevicesinclinicalenvironments,particularlyin
urbanandhospitalsettings,hasintensifiedspectrumscarcity,leadingtocontentionamong
devicesanddegradationinQualityofService(QoS).Thisriskslife-criticaldatadelivery.
Traditionalspectrummanagementschemes,oftencentralizedandstaticallyconfigured,
struggle to meet the dynamic and priority-sensitive demands of medical IoT devices.
Theytypicallyfailtoadaptinrealtimetofluctuatingtrafficloads,heterogeneousservice
priorities,andrapidvariationsinwirelesschannelconditions.Moreover,thecomputational
and signaling overheads of centralized methods make them unsuitable for large-scale,
delay-sensitivehealthcarescenarios[2,3].
To address these limitations, reinforcement learning (RL) has emerged as a robust
paradigm for adaptive spectrum management. RL enables devices to learn efficient re-
sourceallocationpoliciesbyinteractingwiththeenvironmentandautonomouslyadapting
tovaryingnetworkstates. Unlikeconventionalmethods,RLalgorithmsareinherentlysuit-
ableformulti-objectiveoptimization,balancingcompetingobjectivessuchasthroughput
maximization,latencyminimization,energyefficiency,andfairness[4].
Thisworkintroducesascalablemulti-agentreinforcementlearning(MARL)frame-
workforpriority-awarespectrummanagement(PASM)inH-IoTsystemsoperatingunder
URLLCconstraints. BuildingonthePASMmodel, weevaluateacomprehensivesetof
learningstrategies, includingQ-Learning[5], DoubleQ-Learning[6], DeepQ-Network
(DQN)[7],Actor–Critic[4],DuelingDQN[8],andProximalPolicyOptimization(PPO)[9].
Thechoiceofthesesixschemesisdeliberate: tabularmethodsserveaslightweightbase-
lineswithlowcomputationalcost,deepvalue-basedmethodscapturecomplexnon-linear
dynamics,andpolicy-gradientmethodsenhancestabilityandscalability. Bybenchmarking
thesecomplementaryschemeswithinaunifiedframework,MARL-PASMhighlightstheir

Mathematics2025,13,2941 3of27
trade-offsandaddressesakeygapintheliteraturewheremoststudiesfocusonevaluating
asinglealgorithminisolation.
Ourobjectiveistodesignandbenchmarkschedulingpoliciesthatjointlyimprove
throughput,delay,fairness,andenergyefficiencyunderrealistictrafficandchannelcondi-
tionswhileremainingcomputationallypracticalforreal-timeH-IoTdeployments. Thekey
contributionsofthisworkareasfollows:
• WeintroduceMARL-PASM,ascalablemulti-agentreinforcementlearningframework
forpriority-awarespectrummanagementinH-IoTsystems,explicitlydesignedtomeet
URLLCrequirementsbybalancingthroughput,delay,energyefficiency,andfairness.
• Weprovideacomprehensivebenchmarkingstudybyimplementingsixrepresentative
RLstrategies:Q-Learning,DoubleQ-Learning,DQN,Actor–Critic,DuelingDQN,and
PPOwithinaunifiedPASMframework. Thisallowssystematiccomparisonacross
tabular,deepvalue-based,andpolicy-gradientmethods.
• We integrate fairness-aware reward modeling and dynamic class-based prioritiza-
tionintotheframework,enablingadaptiveandpriority-sensitiveschedulingunder
heterogeneoustrafficandrealisticwirelesschannelconditions.
• Weconductextensivesimulationsacrossvaryingnetworksizes(3to50devices)and
heterogeneous traffic distributions, reporting consolidated results on throughput,
delay, energy efficiency, fairness, blocking probability, convergence behavior, and
trainingcost. Theseresultsrevealalgorithmictrade-offsandidentifyPPOasthemost
promisingschemeforlarge-scaleH-IoTdeployments.
Therestofthemanuscriptisorganizedasfollows. Section2reviewsrecentadvances
in H-IoT spectrum management and RL applications in wireless networks. Section 3
presentsthesystemmodel,includingnetworkassumptions,state–actionrepresentation,
andrewarddesign. Section4detailstheproposedMARL-PASMframeworkandlearning
strategies. Section 5 outlines the simulation setup and parameters. Section 6 analyzes
results,interpretskeyfindings,andprovidesfutureresearchdirections. Finally,Section7
concludesthepaper.
2. LiteratureReview
H-IoTnetworksaredesignedtosupportreal-timemonitoring,emergencyresponse,
and intelligent diagnostics through the deployment of connected medical sensors and
wearabledevices. Thesenetworkshandlemission-criticaldatastreams,rangingfromcon-
tinuousvitalsignmonitoringtoemergencyalerts,andarefoundationaltosmarthealthcare
delivery systems. However, achieving the stringent QoS requirements such as URLLC
posesseriouschallengesduetospectrumscarcity,dynamictrafficpatterns,andinterference
indenselydeployedenvironments[10,11].
5G is explicitly designed to address these challenges through support for URLLC,
offeringair-interfacelatenciesaslowas1msandreliabilityguaranteesexceeding99.999%
in3GPPRelease16[12]. However,traditionalstaticorsemi-staticspectrummanagement
schemesfallshortincopingwiththecomplexityanddynamicityofH-IoTtraffic. Therefore,
intelligentandadaptivesolutions,particularlythoseleveragingRL,havegainedincreasing
attentionastheyprovidetheabilitytoautonomouslylearnoptimalaccessandscheduling
policiesinreal-time.
RLisnowanemergingparadigmforDynamicSpectrumAccess(DSA)toallowdevices
andnetworkagentstolearntoselectspectrumchannelsautonomouslyusingadaptive
feedback-basedselection.Q-Learninghasbeenemployedinpreviousworktoequipdevices
withtheabilitytolearnchannelaccesswithincognitiveradioenvironments[13,14]. These
model-freeRLalgorithmsimprovedtheutilizationofthespectrumbyallowingdevicesto
learninterference-awareaccesspatternsovertime. Currentadvanceshavealsoaimedat

Mathematics2025,13,2941 4of27
deepreinforcementlearning(DRL)toleveragedeepneuralnetworkstocontrolthehigh-
dimensionalstateandactionspacestypicalinIoTenvironments. Theauthorsin[15,16]
proposed DRL-based decentralized architectures that significantly improved spectrum
sharingefficacywithoutrelyingoncentralcontrol. SuchadvancesarerelevanttoH-IoT,
whereindistributedhealthcaredevicesoughttobeautonomoustooperateundercongested
andinterference-heavyconditions. MARLtechniqueshavealsoincreasinglybeenapplied
inhealthcare.Theauthorsin[17]introducedabi-levelMARLframeworkusingcooperative
learningandgametheorytoenhancefairnessandsystemthroughput. CooperativeMARL
modelssuchasthesehavebeensuccessfulinlargecognitiveradionetworks[18],validating
the scalability of RL in H-IoT settings. The hierarchical and federated RL is developed
in[19],providingaprivacy-protectingfederatedRLforIoMTsystemswithUAVsupport.
Suchapproachesenablespectrumallocationwithzerointrusionintosensitivehealthcare
data,pavingthewayforsecure,scalableH-IoTsystems.
Besidesreliabilityandthroughput,fairnessandenergyefficiencyarecriticalmetricsin
H-IoTnetworks,especiallyforbattery-poweredmedicalsensors. DRLsolutionslike[20,21]
demonstrate that energy-efficient RL policies can double device lifetimes without com-
promisinglatencyandreliability. Theseschemescontroltaskoffloadingandtransmission
adaptivelyinrealtimetorealizeanoptimalenergy-delaytrade-off. Anotheressentialas-
pectisfairness. Thestudyin[17]incorporatedJain’sFairnessIndexdirectlyintothereward
functionofaMARLsystemtoensureequitablebandwidthallocationamongdevices. But
mostcurrentframeworksareoblivioustofairness,leadingtolow-prioritymedicaldevices
beingdeniedservice. Futureresearchmustincludefairnessasoneofthekeyoptimization
goals, along with latency and throughput. Ensuring URLLC in IoT and particularly in
dynamicH-IoTenvironmentsispossiblythetoughestobjective. Actor–Criticandpolicy-
gradientalgorithmshavebeenexploredtomeetprobabilisticlatencyconstraints[22].The
studyin[23]hasdemonstratedtheuseofRLtoenforcedynamicresourceslicingforhealth-
careapplications,andoncemore,thishighlightsthepracticalityofRLinmeetingstringent
QoSrequirementsinhealthcaresystems.
AdvancedRLmodelssuchasDoubleDQN,DuelingDQN,andActor–Criticmethods
havestartedtogainvisibilityinthewirelesscommunicationdomain. Thesearchitectures
offeradvantagessuchasreducedoverestimationbias,bettervaluefunctionapproximation,
andimprovedstability. Thestudyin[24]demonstratedthatDuelingDQNoutperformed
bothvanillaandDoubleDQNin5Gnetworkslicingscenarios. Sucharchitecturesareun-
derexploredinhealthcare-specificspectrummanagement. ExistingH-IoTworksprimarily
relyonconventionalRLalgorithms,andthereisminimalintegrationofadvancedmethods
tailored to the healthcare context. This presents new opportunities to adopt and adapt
state-of-the-artRLtechniquesinH-IoTsystems.
OtherrelevantworksincludethedistributedRL-basedspectrumallocationframework
in[25],whichappliesadistributedmulti-agentapproachtocognitiveIoTenvironments.
Thismethodimprovesscalabilityandadaptabilityindynamicspectrumsettingsbutdoes
notexplicitlyaddressmedicalQoSrequirementssuchasURLLC.Similarly,Ref. [26]pro-
posed an RL-based routing approach for cognitive radio-enabled IoT communications,
focusing on optimal route selection and interference mitigation. While effective in im-
provingnetworkthroughput,theschemeoverlooksheterogeneousdeviceconstraintsand
priority-basedschedulingneededinH-IoT.
AssummarizedinTable1,mostpriorstudiesoptimizeisolatedperformancemetrics
andrelyonsimplifiedscenarios,limitingtheirapplicabilitytodenseandheterogeneous
H-IoT deployments. To bridge these gaps, this study proposes a unified MARL-based
PASMframeworkthatjointlyevaluatesthroughput,delay,energyefficiency,fairness,and

Mathematics2025,13,2941
5of27
blockingprobabilityunderURLLCdemands,offeringarealisticandscalablebenchmark
acrosssixreinforcementlearningstrategies.
Table 1. Summary of representative RL-based spectrum management works in H-IoT and
relatednetworks.
| Study RLTechnique | ApplicationFocus | Advantages |     | Limitations |     |
| ----------------- | ---------------- | ---------- | --- | ----------- | --- |
Limitedscalability;lacks
Improveschannelutilizationvia
| [13] Q-Learning | IndustrialIoT |     |     | priority-awarenessfor |     |
| --------------- | ------------- | --- | --- | --------------------- | --- |
opportunisticaccess
heterogeneoustraffic
|                      |                    | Ensuresfairness;increases        |     | Highcomputationalcomplexity;    |     |
| -------------------- | ------------------ | -------------------------------- | --- | ------------------------------- | --- |
| [17] Bi-LevelMARL    | IoMT               |                                  |     |                                 |     |
|                      |                    | throughputunderdiverseloads      |     | noreal-timechannelmodeling      |     |
|                      |                    | Distributedspectrumaccess        |     | Ignoresdeviceheterogeneityand   |     |
| [15] DQN             | Multi-userIoT      |                                  |     |                                 |     |
|                      |                    | withoutcentralcontrol            |     | QoSprioritization               |     |
|                      |                    | Adaptstointerference;scalablein  |     | Noevaluationunder               |     |
| [16] DQN             | DynamicIoTSpectrum |                                  |     |                                 |     |
|                      |                    | moderatenetworks                 |     | URLLCconstraints                |     |
| Cooperative          |                    | Enhanceslearningin               |     | Requireshighinter-device        |     |
| [18]                 | CognitiveRadio     |                                  |     |                                 |     |
| MARL                 |                    | densedeployments                 |     | coordinationoverhead            |     |
|                      |                    | Privacy-preservingspectrumand    |     | Increasedlatencyfromfederated   |     |
| [19] FederatedMARL   | UAV-assistedIoMT   |                                  |     |                                 |     |
|                      |                    | computeallocation                |     | updates;ignoresfadingdynamics   |     |
|                      |                    | Achievesoptimaldelay-energy      |     | Notdesignedfordynamicpriority   |     |
| [20] DRLOffloading   | SmartHealthcare    |                                  |     |                                 |     |
|                      |                    | trade-off                        |     | shiftsinH-IoT                   |     |
|                      |                    | Improvesfairness–energytrade-off |     | Single-agentsetup;lacks         |     |
| [21] RLScheduler     | H-IoTURLLC         |                                  |     |                                 |     |
|                      |                    | inscheduling                     |     | multi-agentscalabilityanalysis  |     |
|                      |                    | OutperformsDQNandDouble          |     | Applicationlimitedtoslicing;not |     |
| [24] DuelingDQN      | NetworkSlicing     |                                  |     |                                 |     |
|                      |                    | DQNinutility                     |     | generalizedforH-IoT             |     |
|                      |                    | MeetsURLLCspectrum-power         |     | Nospectrumfairnessor            |     |
| [22] Actor–Critic    | VehicularIoT       |                                  |     |                                 |     |
|                      |                    | constraints                      |     | healthcare-specificmodeling     |     |
|                      |                    | Enhancesrouteselectionand        |     | Lacksheterogeneitymodelingand   |     |
| [26] RL-basedRouting | CognitiveRadioIoT  |                                  |     |                                 |     |
|                      |                    | interferenceavoidance            |     | healthcare-specificQoS          |     |
Distributed CognitiveIoTSpectrum Improvesscalabilityandadaptability NoURLLCconsideration;not
[25]
| MARL | Allocation | indynamicspectrumuse |     | tailoredforH-IoT |     |
| ---- | ---------- | -------------------- | --- | ---------------- | --- |
3. SystemModel
ThissectionoutlinesthesystemmodelfortheproposedRL-basedspectrummanage-
mentframeworkinanH-IoTenvironment,asshowninFigure2. Thearchitectureconsists
ofmultipleparallelchannelssharedamongheterogeneousH-IoTdevicesoperatingindis-
cretetimeslots.Themodelencapsulatesthenetworkdynamics,state–actionrepresentation,
andrewarddesigntoguideRLagentsindecision-making.
We consider a time-slotted wireless communication environment with C orthogo-
nal channels and N H-IoT devices. Each channel c ∈ {1,2,...,C} supports one active
transmissionperslot. Devicesareclassifiedintothreedistinctpriorityclasses,denotedby
theset K = {EmergencyAlert,GlucoseMonitor,FitnessTracker},indexedas k ∈ {1,2,3}
respectively, with EmergencyAlert traffic having the highest priority. At each time slot
∈ {1,2,...},onedevicesendsarequestforspectrumaccess.
t Therequestincludesthe
device class, identity, and current context. The system observes this request and must
decideonanappropriateactiongoverningspectrumallocation. Letthesystemstateattime
|     | tbedenotedass ∈ | S,definedasatuple: |     |     |     |
| --- | --------------- | ------------------ | --- | --- | --- |
t
|     |     |     | s = (c ,k ,a | ),  | (1) |
| --- | --- | --- | ------------ | --- | --- |
|     |     |     | t t t        | t−1 |     |

Mathematics2025,13,2941 6of27
where the c ∈ {1,...,C} is the current channel index selected for access, k ∈ {1,2,3}
t t
denotesthepriorityclassoftherequestingdevice,anda t−1 ∈ Aistheactiontakeninthe
previoustimestep. TheactionspaceAcomprisesfivediscreteactions:
A = {Deny,Grant,Preempt,Coexist,Handoff}, (2)
wheretheaction“Deny”rejectsthespectrumaccessrequest;“Grant”approvestherequest
andallocatesthechannelexclusively. “Preempt”revokestheaccessofalower-priority
devicetograntthecurrentrequest. The“Coexist”actionismodeledasconcurrentchannel
usewithreducedSINR,activatedwhencoexistenceispermittedintheenvironmentconfig-
uration. Finally,“Handoff”migratesthedevicetoadifferentavailablechannel. Thetotal
statespacegrowsas|S| =C×|K|×|A|.
Figure2.Detailedsystemmodel.
RewardFunction
TherewardfunctionisdesignedtopromotekeyobjectivesofH-IoTsystems: high
throughput,energyefficiency,fairnessamongdeviceclasses,andlowlatencyforcritical
devices. Letr denotethescalarrewardattimet,computedas
t
r = λ ·T +λ ·F −λ ·E +λ ·I(k =argminC ), (3)
t 1 t 2 t 3 t 4 t k
k
where T is the normalized throughput achieved in the current time step, E is the nor-
t t
malizedenergycostofspectrumaccess.
I(·)isanindicatorfunctionprovidingareward
bonusifthecurrentlyservedclassistheleastservedsofar,encouragingservicediversity.
λ ,λ ,λ ,andλ areweightparametersthatbalancethecontributionofthroughput,fair-
1 2 3 4

Mathematics2025,13,2941 7of27
ness,energycost,andclassequity,respectively,andF istheinstantaneousfairnessindex,
t
computedusingJain’sindex[27]:
(cid:16) (cid:17)2
∑K x
k=1 k
F = , (4)
t K·∑K x2
k=1 k
Here,F capturesproportionalfairnessacrossdeviceclasses,whiletheindicatorterm
t
providesanadditionalincentivetoservetheleast-attendedclass, ensuringdiversityin
schedulingdecisions. x isthecumulativepayloadvolumesuccessfullydeliveredtoclass
k
kacrosstheepisode,normalizedbythenumberoftimeslots. Accesscountsandper-slot
rewardsareaccumulatedviaenvironmentfeedbackandaggregatedatepisodeend. This
rewardformulationpromotesefficientresourceusewhileensuringfairnessandprioritizing
underserveddevices. Theagentistrainedtomaximizetheexpecteddiscountedcumulative
reward[28]:
(cid:34) ∞ (cid:35)
max E ∑ γtr | π , (5)
t
π
t=0
whereπisthepolicymappingstatestoactionsandγ ∈ [0,1)isthediscountfactor.
4. ProposedMARL-PASMFramework
Inthissection,wedetailthedesignoftheproposedMARL-PASMframeworkforH-
IoTenvironments. TheframeworkintegratessixRLschemes,namelytabularQ-Learning,
Double Q-Learning, Actor–Critic, DQN, Dueling DQN, and PPO. These agents learn
policies to dynamically allocate spectrum across heterogeneous medical devices with
varyingpriorities. TheoverallstructureoftheframeworkisillustratedinFigure3,while
thegenerictrainingprocedurethatunderpinsallschemesisoutlinedinAlgorithm1.
Figure3.MARL-PASM.
Inthefollowingsubsections,eachofthesixreinforcementlearningschemesintegrated
within MARL-PASM is described in detail. These include tabular Q-Learning, Double
Q-Learning,DQN,DuelingDQN,Actor–Critic,andPPO,withemphasisontheirlearning
mechanismsandupdaterules.

Mathematics2025,13,2941 8of27
Algorithm1GenericMARL–PASMtrainingloop
1: InitializeenvironmentE withNdevicesandtrafficclasses
2: Initializelearnerparametersθforthechosenscheme
3: forepisode=1toEdo
4: Resetenvironmentandobtaininitialstates
5: fortimestept =1toTdo
6: Selectactionausingexplorationpolicy
7:
ApplyainE,observerewardr,nextstates′
8:
Store(s,a,r,s′)inbufferortrajectorymemory
9: Learnerupdate:
10: ifSchemeisQ-LearningthenupdateQ(s,a)withTDrule
11:
elseifSchemeisDoubleQthenupdateQA,QBwithdecoupledselect–evaluate
12: elseifSchemeisDQNthensamplemini-batchfrombufferandtakeagradient
steponTDloss
13: elseifSchemeisDuelingDQNthenupdatevalueandadvantageheadsviaTD
loss
14: elseifSchemeisActor–Criticthenupdatepolicywithadvantageestimateand
updatecriticbyvalueloss
15: else if Scheme is PPO then compute advantages and optimize the clipped
surrogateobjectivewithvaluelossandentropybonus
16: s ← s′
17: ifepisodeterminatesthen
18: break
19: endif
20: endfor
21: Logepisodemetrics: throughputinMbps,delayinms,energyefficiencyinGbits/J,
fairness,blockingprobability,utilization,trainingtime
22: endfor
23: returntrainedpolicyandrecordedmetrics
4.1. TabularQ-LearningandDoubleQ-Learning
TabularQ-LearningmaintainsavaluetableQ(s,a)representingtheexpectedlong-
termrewardoftakingactionainstatesandfollowingthecurrentpolicythereafter[29]. It
updatesvaluesusingtherule
(cid:20) (cid:21)
Q(s t ,a t ) ← Q(s t ,a t )+α r t +γmaxQ(s t+1 ,a ′)−Q(s t ,a t ) , (6)
a′
where α is the learning rate and γ is the discount factor. This approach is simple and
interpretable,butscalespoorlywithlargestate–actionspaces.
Tomitigateoverestimationbias,DoubleQ-Learning[30]introducestwoindependent
estimatorsQ andQ :
1 2
(cid:20) (cid:21)
Q 1 (s t ,a t ) ← Q 1 (s t ,a t )+α r t +γQ 2 (s t+1 ,argmaxQ 1 (s t+1 ,a ′))−Q 1 (s t ,a t ) , (7)
a′
(cid:20) (cid:21)
Q 2 (s t ,a t ) ← Q 2 (s t ,a t )+α r t +γQ 1 (s t+1 ,argmaxQ 2 (s t+1 ,a ′))−Q 2 (s t ,a t ) . (8)
a′
BothmethodsusethediscretestaterepresentationdefinedinSection3. Thesealgo-
rithmsserveasbaselinemodelsforcomparisonwithneuralapproaches.
4.2. Actor–CriticQ-Learning
Actor–Criticmethods[29]decomposethepolicylearningintotwocomponents: the
actorπ(a|s)selectsactionsbasedonthecurrentpolicy,andthecriticV(s)estimatesthe

Mathematics2025,13,2941
9of27
valuefunctiontoguidepolicyupdates. WeuseatabularActor–Criticvariantwherethe
criticupdatesthestate-valueestimateusing
|     |     | V(s | ) ←V(s | )+α | [r +γV(s | )−V(s | )], | (9) |
| --- | --- | --- | ------ | --- | -------- | ----- | --- | --- |
|     |     |     | t      | t   | c t      | t+1   | t   |     |
The actor updates the policy via preference values P(s,a), typically using a soft-
maxpolicy:
exp(P(s,a))
|     |     |     | π(a|s) | =   |     | .   |     | (10) |
| --- | --- | --- | ------ | --- | --- | --- | --- | ---- |
∑ a′exp(P(s,a′))
Thepreferenceisupdatedas
|           |       |       | P(s | ,a ) ←                          | P(s ,a )+α | ·δ, |     | (11) |
| --------- | ----- | ----- | --- | ------------------------------- | ---------- | --- | --- | ---- |
|           |       |       |     | t t                             | t t        | a t |     |      |
| whereδ =r | +γV(s | )−V(s |     | )isthetemporal-differenceerror. |            |     |     |      |
| t         | t     | t+1   | t   |                                 |            |     |     |      |
Actor–Critic methods tend to converge faster in dynamic environments by de-
coupling policy and value updates, which is beneficial for H-IoT systems with mixed
devicedemands.
4.3. DeepQ-Network(DQN)
To address the scalability limitations of tabular methods, we adopt DQN, which
|     | Q(s,a) |     |     |     | (s,a) |     |     |     |
| --- | ------ | --- | --- | --- | ----- | --- | --- | --- |
approximates using a neural network Q θ [28]. The network is trained to
minimizethetemporaldifferenceloss:
|     |     |     |     | (cid:34)(cid:18) |     |     | (cid:35) |     |
| --- | --- | --- | --- | ---------------- | --- | --- | -------- | --- |
(cid:19)2
|     |      | =E  |            |         |       | ′ ′)−Q |         |      |
| --- | ---- | --- | ---------- | ------- | ----- | ------ | ------- | ---- |
|     | L(θ) |     | (s,a,r,s′) | r+γmaxQ | θ− (s | ,a     | (s,a) , | (12) |
|     |      |     |            |         | a′    |        | θ       |      |
whereθ−
denotesthetargetnetworkparametersupdatedperiodicallyfortrainingstability.
DQNemploysexperiencereplay,storingtransitions(s,a,r,s′)inabufferandsampling
mini-batches for training. Input states are encoded using one-hot encoding for device
class,currentchannel,andlastaction. Thisenablestheagenttogeneralizeacrossdiverse
trafficscenarios.
4.4. DuelingDeepQ-Network(DuelingDQN)
DuelingDQN[28]enhanceslearningbydecomposingQ(s,a)intotwoseparateesti-
mators:
|     |     |        |               |     |     | 1 ∑ |           |      |
| --- | --- | ------ | ------------- | --- | --- | --- | --------- | ---- |
|     |     | Q(s,a) | =V(s)+A(s,a)− |     |     |     | A(s,a ′), | (13) |
|A|
a′
where V(s) represents the state value and A(s,a) the advantage of action a in state s.
This architecture helps the agent identify important states independently of the action,
improvinglearningefficiencyandpolicyrobustness.
Theduelingarchitectureemploystwoneuralnetworkbranchessharinginitiallayers,
withoneestimatingV(s)andtheother A(s,a). Theaggregatedoutputprovidesthefinal
Q(s,a)valuesforactionselection.
4.5. ProximalPolicyOptimization(PPO)
PPOisapolicy-gradientreinforcementlearningalgorithmdesignedtoachievestable
andreliablepolicyupdates,particularlyincomplexorhigh-dimensionalenvironments[9].
PPOoptimizesaclippedsurrogateobjectivethatconstrainsthepolicyupdatewithina
predefinedtrustregion,preventingdestructivelarge-stepupdatesandimprovingconver-
gencestability. Thepolicyandvaluefunctionsarebothparameterizedusingdeepneural

Mathematics2025,13,2941 10of27
networks,withtheactornetworkproducingaprobabilitydistributionoveractionsandthe
criticnetworkestimatingthestate-valuefunction.
TheclippedobjectivefunctionusedinPPOisgivenby
LCLIP(θ) =E (cid:2) min (cid:0) r (θ)Aˆ , clip(r (θ),1−ϵ,1+ϵ)Aˆ (cid:1)(cid:3) , (14)
t t t t t
where r (θ) = πθ (at |st ) is the probability ratio between the new and old policies, Aˆ
t πθold (at |st ) t
is the advantage estimate at time t, and ϵ is the clipping parameter. This formulation
limitsthepolicyupdatesizewhileencouragingimprovementonlywhenitalignswiththe
advantageestimate.
Inthiswork,PPOisimplementedinanon-policysettingwithmini-batchstochastic
gradientdescentupdates. WeadoptanadaptiveKullback–Leibler(KL)divergencepenalty
and entropy regularization to balance exploration and exploitation. Hyperparameters
such as learning rate, clipping range, discount factor, and update frequency are tuned
toensureafaircomparisonwiththeotherMARLschemes. ByincorporatingPPOinto
theMARL-PASMframework,weaimtoevaluateitspotentialforimprovingadaptability,
convergencespeed,andpolicyrobustnessinheterogeneousH-IoTscenarios.
5. ExperimentalSetup
TheproposedMARL-PASMframeworkisevaluatedinadiscrete-time,event-driven
simulatorthatemulatesrealisticH-IoToperatingconditionswithheterogeneousdevice
classes, latency-sensitive traffic, and energy-constrained spectrum access. Each device
belongstooneofthreeclinicallyinspiredclasseswithdistincttransmissionpowerlimits,
samplingrates,payloadsizes,andbatterycapacities. Class-dependentenergy-per-bitcosts
andmobility-inducedthroughputpenaltiesdirectlyinfluencepacketarrivals,achievable
rates, andenergydepletion, allowingMARLagentstolearnpriority-awarescheduling
underrealisticconstraints. Allagentsshareaspectrumdividedintofiveorthogonalchan-
nels,witheachepisodemodelingsequentialaccess,contentionresolution,anddynamic
decision-making. SimulationswereimplementedinPython3.13andexecutedona64-bit
workstation. Hyperparameters such as learning rate, discount factor, and exploration
decayweretunedforeachschemewithinconsistentrangestoensurestabilityandfairness
incomparison.
ThestatespaceprovidedtoeachRLagentincludesnotonlythedeviceclass,channel
index,andpreviousaction,butalsotheinstantaneousqueueoccupancyandrecentSINR
statistics,whichcaptureshort-termbacklogconditionsandinterferencevariability. This
augmentationprovidestheagentswithamorecontext-awareviewoftheenvironment
withoutsubstantiallyincreasingthestatedimensionality. Table2summarizesthephysical-
layerandnetwork-levelparameters. Whereapplicable,valuesareadaptedfromtheIEEE
TMLCN [31]studytoensurerealismintheassumedchannelandtransmissionmodels.
TheBaselineScenariousesN =3devicestostudyrewarddynamicsandconvergence
behaviorinacontrolledsetting. TheScalabilitySweepincreasesthenetworksizeupto
N =50devices,randomlyassignedtoclasseswiththestatedproportions,toemulatedense
hospitalorsmartclinicdeploymentswithsignificantspectrumcontention. Devicehetero-
geneityinenergybudgets,samplingrates,transmissionpowerconstraints,andpayload
sizesfollowstheclassprofilesdescribedinTable2,ensuringthatclass-specificoperational
lifetimes and performance trade-offs are faithfully reflected. The 30–40–30distribution
was selected to mirror realistic H-IoT traffic patterns. Medium-priority transmissions,
whichare40%dominantduetocontinuousmonitoringanddiagnosticdata,whilehigh-
priorityemergencyalerts,whichare30%,andlow-prioritybackgroundupdates30%,occur
lessfrequently. Thisbalanceprovidesarepresentativeworkloadforevaluatingspectrum

Mathematics2025,13,2941
11of27
management policies under heterogeneous demand. All results are averaged over five
independentrunswithdifferentrandomseedstoensurestatisticalreliability.
Table2.Simulationenvironmentandtransmissionparameters.
| Parameter |     | Value | Description |     |
| --------- | --- | ----- | ----------- | --- |
Episodes(N
|                        | ep ) | 500    | Totaltrainingepisodesperscheme |     |
| ---------------------- | ---- | ------ | ------------------------------ | --- |
| Timeslotsperepisode(T) |      | 1000   | Discretestepsperepisode        |     |
| Slotduration(∆t)       |      | 1ms    | URLLC-alignedtimegranularity   |     |
| Numberofchannels(C)    |      | 5      | Orthogonalparallelchannels     |     |
| Bandwidthperchannel(B) |      | 180kHz | Per-channelbandwidth(5GNRRB)   |     |
| Channelrate(R)         |      | 1Mbps  | IdealPHYrateperchannel         |     |
Transmitpowerperclass(P ) 18/6/0dBm HP/MP/LPclasstransmitceilings
tx
Samplingrateperclass 5.0/0.2/1.0Hz Packetgenerationrate: HP/MP/LP
Bitspersample 4000/2000/1500 Payloadsizepergeneratedpacket(bits)
| Batterycapacity |     | 50/20/15J  | Initialenergy:    | HP/MP/LPclasses |
| --------------- | --- | ---------- | ----------------- | --------------- |
| NoisePSD(N      | )   | −174dBm/Hz | Thermalnoisefloor |                 |
0
| Receivernoisefigure(F) |      | 5dB                 | Receiverfront-endNF    |     |
| ---------------------- | ---- | ------------------- | ---------------------- | --- |
| Pathlossmodel          |      | Urbanmicrocell(UMi) | 3GPPTR38.901-compliant |     |
| SINRthreshold(γ        | th ) | 3dB                 | MinimumrequiredSINR    |     |
Devicetypes 3classes Emergency(HP),GlucoseMonitor(MP),FitnessTracker(LP)
| Priorityratios |     | 30%/40%/30% | High/Medium/Lowclassproportions |     |
| -------------- | --- | ----------- | ------------------------------- | --- |
Trafficmodelsincorporatebothperiodicandburstypacketarrivals,withemergency
devicescapableofgeneratingirregularhigh-prioritybursts,glucosemonitorsproducing
low-ratecontinuousreadings,andfitnesstrackersgeneratingmoderate-rateperiodicdata.
These patterns, coupled with class-specific transmit powers, payload sizes, and energy
budgets,emulaterealisticmedicaltrafficcharacteristicsobservedinhospitalandhome-care
environments. Channel conditions include additive white Gaussian noise, log-normal
shadowing,anddistance-dependentpathloss;nointer-channelinterferenceisassumedfor
orthogonalallocation. Performanceisevaluatedusingaveragethroughput,delay,energy
efficiency,Jain’sfairnessindex,blockingprobability,interruptionprobability,convergence
time,andtrainingtime,enablingacomprehensivecomparisonofalgorithmictrade-offs
underrealisticH-IoTconditions. ForPPO,weadoptaclippedsurrogateobjectivewith
=0.2,learningrate=3×10−4,discountfactorγ =0.99,updatefrequencyof4epochs
ϵ
perbatch,andentropycoefficient0.01,ensuringabalancebetweenconvergencespeedand
policystabilityforfaircomparisonwithotherRLschemes.
6. ResultsandDiscussion
This section presents a comprehensive evaluation of MARL-PASM against six re-
inforcementlearningschemes,focusingonbaselinebehavior,scalabilityundervarying
networksizes,distributionalperformance,andconvergence/complexitytrade-offs. The
analysis connects observed trends directly to URLLC requirements, highlighting how
MARL-PASMaddressesthroughput,delay,fairness,energyefficiency,andblockingproba-
bilityinH-IoTnetworks.
6.1. LearningDynamicsandBaselinePerformance
Thissectionanalyzedthelearningbehaviorofthesixreinforcementlearningalgo-
rithms, usingthreefundamentalmeasures: themovingaverageofrewardperepisode,
theconvergenceofmaximumQ-values,anddetailedPPOtrainingdiagnostics. Figure4
presentsthemovingaverageofrewardsacross1000trainingepisodes. PPOconsistently
demonstratessuperiorrewardlearning,reachingvaluescloseto95–100andconverging
quicklywithinthefirst200episodes.Actor–Criticalsoperformsstrongly,stabilizingaround

Mathematics2025,13,2941 12of27
85–90. DuelingDQNachievesstablereturnsofapproximately80–85,whileQ-Learning,
Double Q-Learning, and DQN remain in the range of 70–80, reflecting their relatively
slowerconvergenceundercomplexH-IoTtrafficconditions.
Figure4.Movingaverageofrewardacrosstrainingepisodes.
TheQ-valueconvergencetrendsaredepictedinFigure5. DQNachievesthehighest
stability,plateauingaround25–27,followedbyActor–Critic,whichstabilizesnear22–24.
Q-LearningandDoubleQ-Learningconvergetomoremodestvaluesof15–16and5–6,
respectively, showing their conservative policy updates. Interestingly, Dueling DQN,
despiteperformingwellintermsofrewards,showsconsistentlylowQ-valueestimates
(near0–1),whichsuggeststhatitsadvantagedecompositionemphasizesrelativeaction
evaluation rather than absolute Q-value scaling. It is important to note that Q-value
convergence is not directly applicable to PPO, as it does not rely on explicit Q-value
estimation. Instead,PPOstabilityisassessedviaitsdiagnostics(policyloss, valueloss,
entropy,andKLdivergence),showninFigure6. Thisexplainstheadditionofadedicated
PPOdiagnosticfigurealongsiderewardandQ-valueplots.
TofurtheranalyzePPO,Figure6providesdetaileddiagnostics.Thepolicylossremains
tightlyboundedaroundzero,confirmingstableclippedsurrogateupdates. Thevalueloss
fluctuatesbetween2000and3000, reflectingthecritic’sefforttoadapttodiversetraffic
andchannelconditions. Policyentropyremainsbetween0.5and1.5,indicatingsustained
explorationduringtraining. Finally,theKLdivergencebetweenoldandnewpoliciesstays
mostly below 0.015, ensuring that PPO maintains stability without catastrophic policy
shifts. The combination of high reward and stable convergence trends highlights the
strong learning potential of PPO and Actor–Critic in spectrum management for H-IoT.
DQN also shows promising convergence but with slightly lower returns. Meanwhile,
Q-LearningandDoubleQ-Learningremainsuitableforlightweightdeploymentswhere
simplicityandstabilityareprioritized,thoughtheyunderperformincomplexdynamic
environments. DuelingDQNdemonstratedgoodrewardperformancebutlimitedQ-value
growth, suggesting that its structural advantage is more beneficial for relative action
selectionthanabsolutevaluescaling.

Mathematics2025,13,2941 13of27
Figure5.ConvergenceofmaximumQ-valuesacrossepisodes.
Figure6.PPOtrainingdiagnostics:(top-left)policyloss,(top-right)valueloss,(bottom-left)policy
entropy,and(bottom-right)KLdivergence.

Mathematics2025,13,2941 14of27
6.2. ScalabilityandRobustness
Toevaluatetheframework’srobustnessindenseH-IoTscenarios,wesimulatescaling
behaviorfrom5to50devices. Figures7–11illustratethetrendsinthroughput,delay,fair-
ness,blockingprobability,andtrainingtimeacrossallsixreinforcementlearningmethods.
Figure7highlightsthatDuelingDQNsustainsthehighestthroughput, stabilizing
around36–37unitsregardlessofscale,followedcloselybyDQNat34–35units. Incontrast,
Q-Learning,DoubleQ-Learning,andActor–Criticallexperiencesharpthroughputdeclines
belowfiveunitsasdevicecountincreases. PPOperformswellunderlightload(≈28units
atfivedevices)butquicklydegradesundercongestion,convergingnearonetotwounitsat
highdensity. Delaytrends,showninFigure8,reinforcethesefindings. PPOdemonstrates
thelowestandmostconsistentdelay(~2ms),whileDuelingDQNachieveslowandstable
latency(14–15ms). Q-Learning,DoubleQ-Learning,andDQNstabilizeintherangeof
~16–19ms. Actor–Critic, however, suffers from the worst delay, saturating near 99 ms,
reflectinginstabilityinitsvalueestimationunderscale.
Figure7.Throughputvs.numberofdevices.
Figure8.Delayvs.numberofdevices.

Mathematics2025,13,2941 15of27
FairnessoutcomesinFigure9showthatDuelingDQNconsistentlyachievesthehigh-
estfairnessindex(~0.65),followedbyDQN(~0.62). PPOlagsbehindsignificantly,rarely
exceeding0.2,indicatingatrade-offbetweenitslowblockingprobabilityandequitablere-
sourceallocation. Q-LearningandDoubleQ-Learningexhibitfairnessdipsatintermediate
scalesbutrecoverto~0.25–0.3. Actor–Critic,thoughinitiallypoor,improvesbeyond0.35at
50devices,suggestinglateadaptivity. Blockingprobabilityresults(Figure10)demonstrate
thatPPOachievesthelowestblocking(~0.01),outperformingallothermethods. Dueling
DQNfollowsat 0.07–0.08,andDQNat 0.09–0.10,whileQ-Learning,DoubleQ-Learning,
andActor–Criticremainsignificantlyhigheraround0.17–0.18.
Figure9.Fairnessindexvs.numberofdevices.
Figure10.Blockingprobabilityvs.numberofdevices.
Training time comparisons (Figure 11) add another layer of insight. Tabular Q-
Learning,DoubleQ-Learning,andActor–Criticremainlightweight,withruntimesnear
1s. PPOshowsmoderatecomputationaloverhead(~30–35s),whileDQNrequires~55s,

Mathematics2025,13,2941 16of27
andDuelingDQNincursthehighestcost(~80–90s). Thishighlightsthetrade-off: PPO
isefficientinlatencyandblockingbutlessfair,whileDuelingDQNdemandsmorecom-
putationyetprovidesthemostbalancedoverallscalability. Takentogether,theseresults
suggestthatDuelingDQNandPPOoffercomplementarystrengths.DuelingDQNachieves
robustfairness,highthroughput,andlowdelay,whilePPOminimizesblockinganddelay
but struggles with fairness under scale. For fairness-critical and high-utilization H-IoT
deployments,DuelingDQNispreferable,whereasPPOmaybesuitableforultra-reliable,
latency-sensitiveapplicationswherefairnessislesscritical.
Figure11.Trainingtimevs.numberofdevices.
6.3. DistributionalPerformanceInsights
Thissectionprovidesadetaileddistributionalanalysisofkeyperformanceindicators
usingcumulativedistributionfunctions(CDFs)andcorrespondingmeanbarplots. The
performanceofeachMARLvariantisevaluatedwithrespecttothroughput,delay,energy
efficiency,fairness,channelutilization,andinterruptionprobability.
6.3.1. ThroughputDistribution
Figures12and13presentthethroughputdistribution(CDF)andmeanthroughput
across all schemes. The results reveal a more balanced landscape compared to earlier
findings. FromtheCDFinFigure12,allreinforcementlearningschemesexhibitrelatively
closedistributions,withslightshiftsintailbehavior. PPOdemonstratedaslightlydelayed
riseinitsCDFcurve,indicatingthatwhileitachieveshigherpeakthroughputincertain
instances, its distribution is less consistent at lower percentiles compared to DQN and
DuelingDQN.
ThemeanthroughputcomparisoninFigure13highlightsPPOasthebestperformer,
achievinganaveragethroughputofapproximately0.57Mbps. DuelingDQNandActor–
Criticfollowcloselyataround0.55–0.56Mbps,confirmingtheirrobustnessundervarying
traffic loads. In contrast, Q-Learning, Double Q-Learning, and DQN yield lower mean
throughputvalues(around0.53–0.54Mbps),reflectingthelimitationsoftabularandstan-
dardvalue-basedapproachesindynamicenvironments. Thesefindingsdemonstratethat
PPOandDuelingDQNsustainhigherthroughputunderrealisticloadconditions,directly
supportinglife-criticaldatatransmissioninH-IoT.

Mathematics2025,13,2941 17of27
Figure12.CDFofthroughput.
Figure13.Meanbarplotsofthroughput.
6.3.2. DelayDistribution
Figures14and15illustratethecomparativedelaydistributionsacrossallsixlearning
schemes. TheresultsclearlyindicatethatPPOachievesthelowestdelays,withamean
delayofapproximately7msanditsCDFrisingsteeply,demonstratingthatthemajorityof
transmissionscompletewithinverylowlatencybounds. ThishighlightsPPO’sefficiency
inmaintainingstabilityundervaryingnetworkconditions.

Mathematics2025,13,2941 18of27
Figure14.CDFofdelay.
Figure15.Meanbarplotsofdelay.
Q-LearningandDoubleQ-Learningexhibitmoderateperformance,averagingaround
10–12ms,whileDuelingDQNmaintainsaslightlyhighermeanof12ms. DQNlagsfurther
behindwithanaveragedelaycloseto14ms,showinglessrobustnessinlatency-sensitive
scenarios. Actor–Critic,althoughcomputationallylightweight,continuestounderperform
withdelaysfrequentlyexceeding80msintailcases,reflectinginstabilityinvalueestimation
andgradientupdates.
Importantly,tailperformanceanalysisshowsthatPPOreducesthe95th-percentile
delaybyapproximately11.5%comparedtothenextbestscheme. ThisconfirmsthatPPO
notonlyminimizesaveragelatencybutalsoeffectivelysuppressesextremedelayoutliers,
whichiscrucialforURLLCscenarioswheremillisecond-levelguaranteesaredecisive.

Mathematics2025,13,2941 19of27
6.3.3. EnergyEfficiencyAnalysis
Figures 16 and 17 illustrate the distribution and mean values of energy efficiency
acrossallsixschemes. PPOachievesthehighestmeanenergyefficiency,reachingnearly
1.5×1010bits/Joule,outperformingallotheralgorithms. ThishighlightsPPO’sabilityto
optimizebothspectralutilizationandpowerconsumptionsimultaneously. DuelingDQN
andDQNfollowclosely,withmeanefficienciesof1.34×1010and1.33×1010bits/Joule,re-
spectively,demonstratingthestrengthofdeepneuralapproximatorsinsustainingefficient
policiesunderhigh-loadH-IoTconditions.
Figure16.CDFofenergyefficiencyacrossschemes.
Figure17.Meanbarplotsofenergyefficiency.
TabularQ-LearningandDoubleQ-Learningexhibitcomparativelylowerefficiency,
around1.29×1010 and1.19×1010 bits/Joule,reflectingtheirlimitedadaptabilityindy-
namicspectrumenvironments. Actor–Criticrecordsthelowestperformanceamongfunc-
tionapproximators, atapproximately1.13×1010 bits/Joule, consistentwithitsweaker
convergencebehaviorobservedinearliersubsections.

Mathematics2025,13,2941 20of27
6.3.4. FairnessEvaluation
Figures18and19demonstratethatallsixschemesachieveconsistentlyhighfairness,
withmeanvaluesclusteredinthenarrowrangeof0.82–0.83. Unlikeearlierobservations
whereDuelingDQNappeareddominant, theupdatedresultsrevealonlymarginaldif-
ferencesamongthealgorithms. PPOachievesthehighestfairnessatapproximately0.83,
closelyfollowedbyDuelingDQNandQ-Learning. DoubleQ-LearningandDQNexhibit
nearlyidenticalfairnesslevels, whileActor–Criticalsomaintainscomparableequityin
resourceallocation. Theconvergenceoffairnessindicesacrossschemeshighlightsthat
modernRL-basedpoliciesarecapableofensuringsociallyfairspectrumaccessevenunder
densevehicularIoTconditions. Thissuggeststhatthroughputanddelayoptimizationdo
notcomeattheexpenseoffairness,reinforcingtherobustnessoftheproposedPASMframe-
work. TheconvergenceoffairnessacrossschemesindicatesthatMARL-basedpoliciescan
improveefficiencywithoutcompromisingtheequityofspectrumaccess.
Figure18.CDFoffairnessindex.
Figure19.Meanbarplotsoffairnessindex.

Mathematics2025,13,2941 21of27
6.3.5. ChannelUtilizationandInterruptionRisk
Figures20and21presentthetrade-offbetweenchannelutilizationandinterruption
probabilityacrossallsixschemes. TheresultsshowthatPPOachievesthehighestmean
channelutilization,approaching0.19(normalized),withconsistentlywiderdistribution
bounds. Dueling DQN and Actor–Critic follow closely, maintaining utilization above
0.18,whereasQ-Learning,DoubleQ-Learning,andDQNshowslightlyloweraverages
(0.17–0.18). Thisindicatesthatdeeppolicy-basedmethodsallocateresourcesmoreaggres-
sivelyandeffectivelyincongestedconditions.
Figure20.Channelutilizationunderdifferentpolicies.
Figure21.CDFofinterruptionprobability.
However, higher utilization must be balanced against interruption risk. The CDF
ofinterruptionprobabilityhighlightsthatActor–Criticexhibitsthesteepestdistribution,

Mathematics2025,13,2941 22of27
reachingnearly90%probabilityofinterruptioninextremecases,reflectingunstablepolicy
convergence. Q-LearningandDoubleQ-Learningperformmoderately,buttheirinterrup-
tionprobabilityspreadsacrosswiderranges,indicatinglesspredictability. Incontrast,PPO
demonstratedamoregradualCDFslope,sustaininglowerinterruptionrisksrelativetoits
higherutilization. DuelingDQNalsoperformsrobustly,offeringabalancedcompromise
betweenthroughput-drivenutilizationandstability.
6.4. Convergencevs. ComputationalCost
Figure22showedthatPPOconvergesinthefewestepisodes(around75)andwiththe
lowesttrainingtimebelow80s,highlightingitsefficiencyinbothlearningandcomputation.
Incontrast,Actor–Criticconvergesinnearly440episodesandincursthelargesttraining
costofapproximately250s,revealinginstabilityinitspolicygradientupdates.Amongdeep
Q-learningvariants,DuelingDQNandDQNconvergeinapproximately340–390episodes,
slightlyslowerthantabularmethodsbutmorestableonceconverged. TabularQ-Learning
and Double Q-Learning require around 310–325 episodes, but with negligible training
overheadbelow25s,whichmakesthemlightweightbutlessrobustatscale.
Figure22. Convergencespeedandtrainingtimeacrossschemes. Coloredbarsshowepisodesto
convergence(lefty-axis),whiletheblackdashedlinewithcirclemarkersshowstrainingtimein
seconds(righty-axis).
Beyondtrainingconvergence,wealsoassessedinferencecomplexityacrossschemes.
Tabular methods required negligible memory, under 1 kB, and delivered near-instant
decisionlatency,yettheystruggledtoscaleinaccuracyandstability. DQNandDueling
DQNusedmodelsizesinthetensofkilobytesandachievedinferencetimesaround0.02to
0.03msperdecision,yieldingthousandsofdecisionspersecondoncommodityhardware.
PPOusedthelargestmodelbutremainedhighlyefficient,withinferencelatencycloseto
0.01msandthehighestdecisionthroughput. Actor–Criticfellbetweentheseextremes,
withafootprintof60kparametersandinferencetimeof0.04msperdecision, whichis
largerthantabularmethodsbutslightlyhigherinlatencythanPPO.
Figure23furtherevaluatestheblockingprobability.PPOdeliveredthelowestblocking
probabilityofaround0.02withlimitedvariance,demonstratingitsabilitytoensurereliable
servicecontinuity.Actor–Criticalsoachievesalowaverageblockingnear0.03,butitshigher

Mathematics2025,13,2941
23of27
variancesuggestsinconsistencyacrosstrafficscenarios. DuelingDQNandQ-Learning
maintainmoderateblockingratesaround0.045,whileDoubleQ-LearningandDQNrecord
thehighestblockingratesbetween0.055and0.06,whichmayhinderperformanceunder
heavierloads.
Figure23.Meanblockingprobabilitywithstandarddeviation.
6.5. HolisticPerformanceComparison
Table 3 consolidates the performance of all six schemes across throughput, delay,
energyefficiency,fairness,blockingprobability,convergencebehavior,andtrainingtime.
TheresultsrevealthatPPOconsistentlyoutperformsitscounterpartsbydeliveringthe
highestthroughputof 680Mbps, thelowest averagedelay of9.2 ms, and the strongest
energyefficiencyof15gigabitsperjoule. Italsoachievesthelowestblockingprobability
of0.02andthefastestconvergenceat75episodes,balancingstabilitywithcomputational
efficiency. Among the deep Q-learning methods, Dueling DQN emerges as the most
competitivealternative. Itoffersbalancedthroughputof640Mbps,lowdelayof10.4ms,
highenergyefficiencyof13.4gigabitsperjoule,andfairnessof0.823. Althoughitstraining
timeof190sishigherthanPPO,itsrobustnessmakesitasuitablecandidateforapplications
wherepolicystabilityiscritical. StandardDQNshowedslightlyweakerdelayandblocking
performance,thoughitmaintainsstrongthroughputandenergymetrics.
Table3.Performancecomparisonacrossallschemes.
Energy
|        | Throughput |           |            | Blocking | Convergence | Training |
| ------ | ---------- | --------- | ---------- | -------- | ----------- | -------- |
| Scheme |            | Delay(ms) | Efficiency | Fairness |             |          |
|        | (Mbps)     |           |            | Prob.    | (Episodes)  | Time(s)  |
(Gbits/J)
| Q-Learning | 540 | 11.2 | 12.9 | 0.823 0.045±0.045 | 325 | 20  |
| ---------- | --- | ---- | ---- | ----------------- | --- | --- |
0.057±0.06
| DoubleQ     | 510 | 12.8 | 11.9 | 0.824            | 310 | 25  |
| ----------- | --- | ---- | ---- | ---------------- | --- | --- |
| DQN         | 620 | 10.7 | 13.2 | 0.820 0.058±0.06 | 390 | 150 |
| DuelingDQN  | 640 | 10.4 | 13.4 | 0.823 0.048±0.06 | 340 | 190 |
| ActorCritic | 470 | 13.5 | 11.3 | 0.822 0.030±0.05 | 440 | 250 |
| PPO         | 680 | 9.2  | 15.0 | 0.829 0.020±0.03 | 75  | 75  |
Thetabularmethods,Q-LearningandDoubleQ,demonstratelowercomputational
overheadbutlaginthroughput,energyefficiency,andblockingprobability,whichhigh-

Mathematics2025,13,2941 24of27
lights their limited scalability in complex H-IoT environments. Actor–Critic performs
moderately,withreasonablefairnessandblockingvalues,butitsslowerconvergenceof
440episodesandhighertrainingtimeof250smakeitlesspracticalforreal-timedeploy-
ments. ThesefindingsunderscorePPOasthemostpromisingschemeforlarge-scaleH-IoT
spectrummanagement,withDuelingDQNasastrongdeepreinforcementlearningalter-
native. Thecomparativeanalysisvalidatesthetrade-offbetweenalgorithmiccomplexity
andoperationalperformance,providinginsightsintotheselectionofappropriatestrategies
fordifferentdeploymentscenarios. TheseresultsshowthatevaluatingdiverseRLschemes
inaunifiedPASMframeworkrevealscomplementarystrengthsthatwerepreviouslyover-
lookedinsingle-schemestudies. Thisintegratedperspectiveconstitutesthekeynovelty
ofourworkandprovidesactionableinsightsforselectingspectrumpoliciesinpractical
H-IoTdeployments.
Table3presentstheaveragednumericalresultsforallevaluatedschemes,comple-
mentingthegraphicalanalysisandenablingdirectquantitativecomparison.
6.6. PracticalConsiderationsforDeployingMARLinH-IoTNetworks
AlthoughtheproposedMARL-PASMframeworkperformssatisfactorilyunderthe
simulatedscenario, itsimplementationasareal-worldH-IoTdeploymentbringsalong
several practical problems that require careful scrutiny. In practice, it is not simple to
estimatetheglobalorshapedrewardsignalswithinarealnetwork. Centralizedorches-
trationthroughanedgeservercanbeusedtogatherobservationsandperformfeedback
computation on the basis of statistics such as latency violations, interference levels, or
successfuldatadelivery. However,centralizedrewardcomputationintroducesadditional
delay and scalability issues. Furthermore, coordination between MARL agents, which
isveryimportantforlearningstabilityandconvergence,createsnon-trivialcommunica-
tionoverhead,particularlywhenbandwidthandlatencyarelimited. Tocounteractthis,
real-worldsystemshavetheoptiontoutilizedecentralizedtraining,federatedMARL,or
low-communicationarchitecturesinordertosacrificecoordinationinfavorofefficiency.
Partial observability is another significant problem. H-IoT nodes usually operate with
partialenvironmentalawareness,whichcanreduceconvergenceandpolicyrobustness.
Techniquessuchasbelief-statemodelingorrecurrentpolicylearningcanofferrobustness
undersuchlimitations. Trainingcomplexityisalsoaconcern;real-worldagentsareeither
trainedofflineindigitaltwinplatformsorfinetunedinalightweightwaytoremaincom-
putationallymanageable. Finally,thenetworkstackimposesaconstraintondesign. As
mentionedinrecentresearchsuchas[31],MAC-layerlearningplatformsmustincorporate
realistic access delays, collision dynamics, and signaling limitations in order to remain
deployable. Thesefactorsguidetheresearchroadmapinthefuture,inwhichscalability,
feasibility,andprotocol-awarenessmustbeco-optimizedtorenderMARL-basedspectrum
accessnearlypossibleforclinicalandmission-criticalH-IoTapplications.
6.7. FutureWork
Infutureextensionsofthiswork, wewillmovebeyondthefixedthree-tierdevice
classificationusedhereandadoptcontext-awaredynamicprioritization. Thiswillallow
devicestoadjusttheirpriorityinrealtimebasedonphysiologicalreadings,patientlocation,
ortemporalurgency,therebymoreaccuratelyreflectingreal-worldmedicalrequirements.
Wewilldesignlightweightclassifierstoenablethisdynamicpriorityassignmentwhile
ensuringlowcomputationaloverhead,whichisessentialforresource-constrainedH-IoT
deployments.Anotherdirectionwewillpursueisthedevelopmentofhybridreinforcement
learningarchitecturesthatmergecomplementaryschemes. Forexample,wewillcombine
thestablepolicyupdatesofPPOwiththerapidvalue-basedlearningofDQNvariants,

Mathematics2025,13,2941 25of27
or integrate Actor–Critic frameworks with double estimators to mitigate bias. These
hybridapproacheswillbedesignedtoimproveadaptability,accelerateconvergence,and
enhancepolicyrobustnessincomplexandrapidlychangingH-IoTenvironments. Wewill
also extend the state space to include long-term temporal patterns such as time-of-day
usagecyclesandpatient-specificactivitytrends,enablingagentstoanticipateandadapt
topredictablefluctuationsinhealthcaretraffic. FutureworkwillalsoextendPASMwith
classicalschedulingbaselinessuchaspriorityschedulers,TDMA,andproportionalfair
allocation,enablingdirecthead-to-headbenchmarkingwithRL-basedmethods.
Inaddition,wewillexpandMARL-PASMtohandleextreme-eventtrafficpatterns,
suchasscenarioswheremanydevicessimultaneouslytransmitemergencydataorwhere
trafficdynamicsshiftabruptly. Thiswillallowustostress-testtheframeworkandassess
itsscalabilityunderhighlydynamicandchallengingconditions. Wewillalsoincorporate
explicitfaulttoleranceevaluation,coveringsuddendevicedisconnections,overlapping
transmissions,highpacketlossrates,andrapidenergydepletion. Theseexperimentswill
provideadeeperunderstandingofthesystem’sresilienceandreliabilityunderadverse
operatingenvironments. Furthermore,wewillintegrateprivacy-preservingmechanisms,
withafocusonFederatedMulti-AgentReinforcementLearning,whereagentslearnlocally
andshareonlymodelupdates. Bycouplingthiswithdifferentialprivacy,wewillensure
sensitivepatientdataremainsprotectedwhilemaintainingeffectivecollaborativelearning,
therebymeetingstrictmedicaldataprotectionrequirements. Finally,wewillre-implement
andbenchmarkMARL-PASMdirectlyagainstadvanceddistributedspectrumallocation
andRL-basedroutingmodelstoenableconsistent,head-to-headcomparisons. Thiswill
ensurethatourframeworkisrigorouslyevaluatedagainststate-of-the-artsolutionsand
highlightsitscontributionstothebroaderlandscapeofspectrummanagementinhealthcare
IoTsystems.
7. Conclusions
ThisstudypresentedtheMARL-PASMframeworkfordynamicspectrumallocation
in H-IoT environments, addressing the challenges of heterogeneous traffic classes and
stringentQoSdemandsthroughcentralized,intelligentdecision-making. Bybenchmarking
six RL strategies, including PPO, we demonstrated that advanced DRL models deliver
clearperformanceadvantages. PPOconsistentlyachievedthehighestthroughput,lowest
latency,strongestenergyefficiency,andlowestblockingprobability,whileDuelingDQN
emergedasthemostbalanceddeepQ-learningalternative,sustainingrobustperformance
underdensenetworkconditions. Actor–Criticofferedfastconvergenceunderlightertraffic
loads, and the tabular methods, though computationally efficient, lacked scalability in
complexdeployments. ScalabilityandrobustnessevaluationsconfirmedtheabilityofDRL
methodstomaintainstabilityandfairnessasdevicedensityincreases,highlightingtheir
potentialforreal-worldH-IoTapplications.
Despitethesepromisingoutcomes,severallimitationsremain. Thecurrentframework
employsfixeddeviceclassesandstaticprioritydistributions,doesnotfullyaccountfor
extremeemergencysurges,andhasnotbeenrigorouslystress-testedforfaulttolerance
underconditionssuchasdevicedisconnections,interferencespikes,orenergydepletion.
Privacy-preserving mechanisms such as federated MARL are also yet to be explored,
andvalidationusingreal-world,trace-drivendatasetsisstillrequired. Addressingthese
gapswillinvolveincorporatingdynamicprioritization,hybridRLarchitectures,explicit
resilience testing, and privacy-preserving learning techniques. Future work will also
benchmarkMARL-PASMdirectlyagainststate-of-the-artdistributedspectrumallocation
andRL-basedroutingmodelstoensurearigorouscomparativeevaluation. Byadvancing
alongthesedirections,MARL-PASMcanevolveintoarobust,scalable,andsecurespectrum

Mathematics2025,13,2941 26of27
management framework capable of supporting the safety-critical requirements of next-
generationH-IoTcommunicationsystems.
AuthorContributions:Conceptualization,A.I.;simulations,A.I.,A.N.andT.K.;writing—original
draftpreparation,A.I.andT.K.;writing—reviewandediting,A.I.,A.N.andS.-B.R.;supervision,
S.-B.R.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement: Thedatapresentedinthisstudyareavailableonrequestfromthe
correspondingauthorduetoourongoingproject.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. Bhuiyan,M.N.;Rahman,M.M.;Billah,M.M.;Saha,D. Internetofthings(IoT):Areviewofitsenablingtechnologiesinhealthcare
applications,standardsprotocols,security,andmarketopportunities. IEEEInternetThingsJ.2021,8,10474–10498.[CrossRef]
2. Kumar,A.;Kaur,R.;Gaur,N.;Nanthaamornphong,A. Exploringandanalyzingtheroleofhybridspectrumsensingmethodsin
6G-basedsmarthealthcareapplications. F1000Research2024,13,110.[CrossRef]
3. Iqbal,A.;Nauman,A.;Qadri,Y.A.;Kim,S.W. OptimizingSpectralUtilizationinHealthcareInternetofThings. Sensors2025,
25,615.[CrossRef]
4. Abdellatif,A.A.;Mhaisen,N.;Mohamed,A.;Erbad,A.;Guizani,M. Reinforcementlearningforintelligenthealthcaresystems:A
reviewofchallenges,applications,andopenresearchissues. IEEEInternetThingsJ.2023,10,21982–22007.[CrossRef]
5. Almagrabi, A.O.; Ali, R.; Alghazzawi, D.; AlBarakati, A.; Khurshaid, T. A reinforcement learning-based framework for
crowdsourcinginmassivehealthcareinternetofthings. BigData2022,10,161–170.[CrossRef][PubMed]
6. Jiang,H.;Li,G.;Xie,J.;Yang,J. ActioncandidatedrivenclippeddoubleQ-learningfordiscreteandcontinuousactiontasks. IEEE
Trans.NeuralNetw.Learn.Syst.2022,35,5269–5279.[CrossRef]
7. Swapno,S.M.R.;Nobel,S.N.;Meena,P.;Meena,V.;Azar,A.T.;Haider,Z.;Tounsi,M. Areinforcementlearningapproachfor
reducingtrafficcongestionusingdeepQlearning. Sci.Rep.2024,14,30452.[CrossRef]
8. MohiUdDin, N.; Assad, A.; UlSabha, S.; Rasool, M. Optimizingdeepreinforcementlearningindata-scarcedomains: A
cross-domainevaluationofdoubleDQNandduelingDQN. Int.J.Syst.Assur.Eng.Manag.2024,1–12.[CrossRef]
9. Schulman, J.; Wolski, F.; Dhariwal, P.; Radford, A.; Klimov, O. Proximal policy optimization algorithms. arXiv 2017,
arXiv:1707.06347.[CrossRef]
10. Qadri,Y.A.;Nauman,A.;Zikria,Y.B.;Vasilakos,A.V.;Kim,S.W. Thefutureofhealthcareinternetofthings:Asurveyofemerging
technologies. IEEECommun.Surv.Tutor.2020,22,1121–1167.[CrossRef]
11. Selvaraj,S.;Sundaravaradhan,S. ChallengesandopportunitiesinIoThealthcaresystems:Asystematicreview. SNAppl.Sci.
2020,2,139.[CrossRef]
12. Huang,Q.;Xie,X.;Cheriet,M. Reinforcementlearning-basedhybridspectrumresourceallocationschemeforthehighloadof
URLLCservices. EURASIPJ.Wirel.Commun.Netw.2020,2020,1–21.[CrossRef]
13. Li,F.;Lam,K.Y.;Sheng,Z.;Zhang,X.;Zhao,K.;Wang,L. Q-learning-baseddynamicspectrumaccessincognitiveindustrial
InternetofThings. Mob.Netw.Appl.2018,23,1636–1644.[CrossRef]
14. Raza,A.;Ali,M.;Ehsan,M.K.;Sodhro,A.H. SpectrumevaluationinCR-basedsmarthealthcaresystemsusingoptimizabletree
machinelearningapproach. Sensors2023,23,7456.[CrossRef]
15. Naparstek,O.;Cohen,K. Deepmulti-userreinforcementlearningfordistributeddynamicspectrumaccess. IEEETrans.Wirel.
Commun.2018,18,310–323.[CrossRef]
16. Song,H.;Liu,L.;Ashdown,J.;Yi,Y. Adeepreinforcementlearningframeworkforspectrummanagementindynamicspectrum
access. IEEEInternetThingsJ.2021,8,11208–11218.[CrossRef]
17. Kim,S. Learningandgamebasedspectrumallocationmodelforinternetofmedicalthings(IoMT)platform. IEEEAccess2023,
11,48059–48068.[CrossRef]
18. Tan,X.;Zhou,L.;Wang,H.;Sun,Y.;Zhao,H.;Seet,B.C.;Wei,J.;Leung,V.C.Cooperativemulti-agentreinforcement-learning-based
distributeddynamicspectrumaccessincognitiveradionetworks. IEEEInternetThingsJ.2022,9,19477–19488.[CrossRef]
19. Seid,A.M.;Erbad,A.;Abishu,H.N.;Albaseer,A.;Abdallah,M.;Guizani,M. Multiagentfederatedreinforcementlearningfor
resourceallocationinUAV-enabledInternetofMedicalThingsnetworks. IEEEInternetThingsJ.2023,10,19695–19711.[CrossRef]
20. Su,X.;Fang,X.;Cheng,Z.;Gong,Z.;Choi,C.Deepreinforcementlearningbasedlatency-energyminimizationinsmarthealthcare
network. Digit.Commun.Netw.2024,11,795–805.[CrossRef]

Mathematics2025,13,2941 27of27
21. Iqbal,A.;Khurshaid,T.;Nauman,A.;Rhee,S.B. Energy-AwareUltra-ReliableLow-LatencyCommunicationforHealthcareIoTin
Beyond5Gand6GNetworks. Sensors2025,25,3474.[CrossRef]
22. Khan,N.;Coleri,S. Event-TriggeredReinforcementLearningBasedJointResourceAllocationforUltra-ReliableLow-Latency
V2XCommunications. IEEETrans.Veh.Technol.2024,73,16991–17006.[CrossRef]
23. Khadem, M.; Zeinali, F.; Mokari, N.; Saeedi, H. AI-enabled priority and auction-based spectrum management for 6G. In
Proceedingsofthe2024IEEEWirelessCommunicationsandNetworkingConference(WCNC),Dubai,UnitedArabEmirates,
21–24April2024;pp.1–6.
24. Chen,G.;Shao,R.;Shen,F.;Zeng,Q. SlicingresourceallocationbasedonduelingDQNforeMBBandURLLChybridservicesin
heterogeneousintegratednetworks. Sensors2023,23,2518.[CrossRef]
25. Elhachmi,J. Distributedreinforcementlearningfordynamicspectrumallocationincognitiveradio-basedinternetofthings. IET
Netw.2022,11,207–220.[CrossRef]
26. Rahman,M.H.;Bayrak,A.E.;Sha,Z. Areinforcementlearningapproachtopredictinghumandesignactionsusingadata-driven
rewardformulation. Proc.Des.Soc.2022,2,1709–1718.[CrossRef]
27. Jain,R.K.;Chiu,D.M.W.;Hawe,W.R. Aquantitativemeasureoffairnessanddiscrimination. East.Res.Lab.Digit.Equip.Corp.
1984,21,2022–2023.
28. Wang,Z.;Schaul,T.;Hessel,M.;Hasselt,H.;Lanctot,M.;Freitas,N.Duelingnetworkarchitecturesfordeepreinforcementlearning.
InProceedingsoftheInternationalConferenceonMachineLearning,NewYork,NY,USA,19–24June2016;pp.1995–2003.
29. Sutton,R.S.;Barto,A.G. ReinforcementLearning:AnIntroduction;MITPress:Cambridge,UK,1998;Volume1.
30. Hasselt,H. DoubleQ-learning. Adv.NeuralInf.Process.Syst.2010,23,2613–2621.
31. Miuccio,L.;Riolo,S.;Samarakoon,S.;Bennis,M.;Panno,D. OnlearninggeneralizedwirelessMACcommunicationprotocolsvia
afeasiblemulti-agentreinforcementlearningframework. IEEETrans.Mach.Learn.Commun.Netw.2024,2,298–317.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.