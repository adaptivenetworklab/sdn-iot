# DRL-Driven Intelligent SFC Deployment in MEC Workload for Dynamic IoT Networks

> Source file: `DRL-Driven Intelligent SFC Deployment in MEC Workload for Dynamic IoT Networks.pdf`

---

Article
DRL-Driven Intelligent SFC Deployment in MEC Workload
for Dynamic IoT Networks
SeyhaRos1 ,IntaeRyoo2,* andSeokhoonKim1,3,*
1 DepartmentofSoftwareConvergence,SoonchunhyangUniversity,Asan31538,RepublicofKorea;
rosseyha003@gmail.com
2 DepartmentofComputerEngineering,KyungHeeUniversity,Yongin-si17104,RepublicofKorea
3 DepartmentofComputerSoftwareEngineering,SoonchunhyangUniversity,Asan31538,RepublicofKorea
* Correspondence:itryoo@khu.ac.kr(I.R.);seokhoon@sch.ac.kr(S.K.)
Abstract
TherapidincreaseinthedeploymentofInternetofThings(IoT)sensornetworkshasled
toanexponentialgrowthindatagenerationandanunprecedenteddemandforefficient
resourcemanagementinfrastructure. Ensuringend-to-endcommunicationacrossmultiple
heterogeneousnetworkdomainsiscrucialtomaintainingQualityofService(QoS)require-
ments,suchaslowlatencyandhighcomputationalcapacity,forIoTapplications. However,
limitedcomputingresourcesatmulti-accessedgecomputing(MEC),coupledwithincreas-
ingIoTnetworkrequestsduringtaskoffloading,oftenleadtonetworkcongestion,service
latency,andinefficientresourceutilization,degradingoverallsystemperformance. This
paper proposes an intelligent task offloading and resource orchestration framework to
address these challenges, thereby optimizing energy consumption, computational cost,
networkcongestion,andservicelatencyindynamicIoT-MECenvironments. Theframe-
workintroducestaskoffloadingandadynamicresourceorchestrationstrategy,wheretask
offloadingtotheMECserverensuresanefficientdistributionofcomputationworkloads.
Thedynamicresourceorchestrationprocess,ServiceFunctionChaining(SFC)forVirtual
NetworkFunctions(VNFs)placement,androutingpathdeterminationoptimizeservice
executionacrossthenetwork. Toachieveadaptiveandintelligentdecision-making,the
proposedapproachleveragesDeepReinforcementLearning(DRL)todynamicallyallocate
resources and offload task execution, thereby improving overall system efficiency and
AcademicEditors:BartłomiejPłaczek
andMarcinBernas´ addressingtheoptimalpolicyinedgecomputing. DeepQ-network(DQN),whichislever-
agedtolearnanoptimalnetworkresourceadjustmentpolicyandtaskoffloading,ensures
Received:12June2025
Revised:29June2025 flexibleadaptationinSFCdeploymentevaluations. Thesimulationresultdemonstrates
Accepted:7July2025 that the DRL-based scheme significantly outperforms the reference scheme in terms of
Published:8July2025 cumulativereward,reducedservicelatency,loweredenergyconsumption,andimproved
Citation: Ros,S.;Ryoo,I.;Kim,S. deliveryandthroughput.
DRL-DrivenIntelligentSFC
DeploymentinMECWorkloadfor Keywords: deepreinforcementlearning;multi-accessedgecomputing;networkfunctions
DynamicIoTNetworks.Sensors2025,
virtualization;servicefunctionchaining;internetofthings
25,4257. https://doi.org/10.3390/
s25144257
Copyright:©2025bytheauthors.
LicenseeMDPI,Basel,Switzerland. 1. Introduction
Thisarticleisanopenaccessarticle
1.1. BackgroundandMotivation
distributedunderthetermsand
conditionsoftheCreativeCommons The Internet of Things (IoT) has been widely used for digitalization to expose the
Attribution(CCBY)license
potentialofutilizingnetworksensinganddatagatheringfromcitizenenvironments[1,2].
(https://creativecommons.org/
IoTdevicecommunicationwithseveralinterfacetechnologies(i.e.,Wi-Fi,Bluetooth,ZigBee,
licenses/by/4.0/).
Sensors2025,25,4257 https://doi.org/10.3390/s25144257

Sensors2025,25,4257 2of16
LoRaWAN,NFC,and6LoWPAN)throughphysicalmodulation[3–5]isusedtoaccessand
communicatewithnetworkserversviafronthaulphysicalnetworksfordiverseapplication
scenarios. Thus,theincreasingamountofdatageneratedbyIoTsensornetworksleads
toinefficientcomputationandresourceutilization,resultingintheinabilitytoconserve
energyandreduceprocessingtimeondevices. IoTcontinuestogeneratetasksthatrequire
computing, with varying types of processing time, computing resources, and battery
life. However, IoT generates massive traffic requests that often exacerbate bottlenecks
andirregularfluctuationsduetomobilityandspatiotemporalvariationsinserviceusage
patterns[6,7].
Ontheotherhand,multi-accessedgecomputing(MEC)canprovideasolutionfor
managingandorchestratingtheresourceutilizationofcomputationfromIoTsensing[8,9].
MEChasthepotentialtofacilitateresource-intensivecomputation,whichinvolveschaining
virtualizationresourcecapabilitiesandaimstoreducelatencyincommunicationprotocols
andnetworkaspects[10–12]. However,MEChastheresponsibilityofaddressingcomputa-
tionalneeds,leadingtochallengesinbalancingexecutiondelayandenergyconsumption.
Additionally,theintegrationofMECwithsoftware-definednetworks/networkfunction
virtualization(SDN/NFV)controllersenhancestheagilityneededtoreducecomputation
timeandmanageresourcecomplexity,steeringtrafficpatternsfromingresstoegress. Ser-
vicefunctionchaining(SFC)providesinstancesofsequentialvirtualnetworkfunctions
(VNFs)tohostvirtualmachines(VMs),allowingtheorderofVNFstobepropagatedinthe
specifiedorderfortherequiredapplication. Consequently,MEC-enabledSDN/NFVoffers
lowerlatencyandincreasedcomputationalresourcestomanagethehighdemandsofIoT
services. Furthermore,thetimeneededtoprocessresourceallocationandplacementfor
heterogeneousservicefunctionsposesasignificantchallengeforMEC,makingreal-time
determinationandadjustmentsessentialforeffectiveandefficientstatetransitiondecisions
withinthiscomplexsystem.
Toaddresstheselimitations,DeepReinforcementLearning(DRL)hasgainedattention
as a powerful agent for making intelligent, adaptive decisions in highly dynamic net-
working[13,14]. Byconsideringvarioussysteminteractions,DRL-drivenapproachescan
continuouslylearnfromthenetworkenvironmentandSFCplacements[15–19]. Asshown
inFigure1,leveragingtheDRL-integratedMECframeworkcanintelligentlyallocateVNFs
toensureSFCsaredeployedtomaximizeresourceefficiency,minimizelatency,andmain-
tainhighreliability,evenamidunpredictabletrafficfluctuationsastheworkloadchanges.
Furthermore, the timely and efficient advancement of MEC and SFC technologies
remains challenging due to the optimal placement and resource allocation of VNFs in
IoT-drivennetworkenvironments. Ontheotherhand,theyhavedelegatedthecomputing
capacitiesforreal-timeorchestrationandresourcemanagementneededtoinstantiateVNFs
tomeettheworkload. Moreover,thetrade-offsbetweencriticalperformancemetrics,such
aslatency, energyefficiency, cost, andresourceutilization, furthercomplicatetheissue.
Achievinganoptimalbalancebetweenthesefactorsisdifficultduetothelimitedresources
availableatedgenodesandtheunpredictabledemandfromIoTdevices. Intraditional
approaches,SFCdeploymentoftenreliesonpredeterminedrulesorheuristicmethodsthat
cannotadjustefficientlyinreal-time,leadingtoinefficientresourceusageandpoorservice
quality. AsthescaleofIoTnetworkscontinuestogrowandthedemandsofapplications
become more complex, there is a clear need for intelligent, adaptive strategies that can
dynamically optimize SFC placement, resource allocation, and workload distribution
across the edge network. Moreover, DRL is used to determine the policy for charging
SFCdeploymentintheMECserver,enablingadaptiveallocationofoptimaldecisionsfor
instanceresourcesinfluctuatingIoTnetworks.

Sensors2025,25,4257 3of16
Figure1.Multi-agentenabledinNFVforpolicychargingonresourceutilization.
1.2. MotivationandContributions
This paper addresses these challenges by proposing a DRL-driven framework for
intelligentandefficientSFCdeploymentinMECenvironments,capableoflearningoptimal
placement policies that adapt to fluctuating workloads and network conditions. The
followingrecapitalizationisthemaincontributionofthispaper:
• WeformulatedtheVNFplacementandresourceallocationproblemasamulti-objective
optimizationtask,whereconflictingperformancegoalsareconsideredtominimize
latency,conserveenergy,andoptimizeresourceutilization.
• Byintelligentlydistributingworkloadsacrossgeographicallydistributededgenodes
basedonreal-timesystemstates,themodelensuresbalancedresourceutilizationand
reducesservicedegradationinhigh-densityIoTdeployments. Ourschemecanproac-
tivelyreallocateresourcestoavoidandminimizeoverloadrisks,therebyimproving
thelong-termsustainabilityofedgenodes.
• Wedesignajointoptimizationalgorithmfortaskoffloadingandresourceallocation
basedontheDeepQ-Network,withtheoptimizationobjectivesofassistingtheNFVO
ininstantiatingresourcesaccordingtotheworkloadrequirementsofIoTdevices.
• Therewardprovidescomprehensivenetworkperformance. Ourproposedscheme
leverages DRL frameworks and the network environment to highlight significant

Sensors2025,25,4257 4of16
existingsolutionsacrossvariousaspects,includingenergy,latency,packetdelivery
ratio,packetdropratio,andthroughput.
1.3. PaperOrganization
The remaining section of our study is organized as follows: Section 2 provides a
literaturereviewofexistingwork. Section3discussesnetworkmodelingusingDRLto
optimizetheVNFresourceallocationandplacement. Section4outlinestheperformance
metricsandcomparestheproposedmethodswithreferencemethods,concludingwitha
discussioninSection5.
2. RelatedWork
InresponsetothecurrenttrendofutilizingIoTdevicesefficiently,manyresearchers
havefocusedonresourceandenergyconsumptiontohandleresource-intensivecomputing
workloads. However,manystudiesinvestigatingcomputingintheIoTnetworkarestill
challengingduetothevastamountofbigdataandlatencyrequiredtoorchestrateresources
andachievereal-timeefficiency.
ManyresearchscholarsaimtooptimizeresourceallocationandplacementonMEC
to enhance resource utilization concerning communication and computation-intensive
resources[20–22]. Moreover,reducinglatencyfordelay-sensitivetasksonMECservers
posesasignificantchallengeinthiseffort. Traditionally,resourceallocationtechniquesrely
onheuristicoroptimization-basedapproaches,whichstruggletoadapttothereal-time
andunpredictablenatureofIoTtrafficpatterns. Forexample,centralizedmethodssuchas
MixedIntegerLinearProgramming(MILP)andconvexoptimizationhavebeenemployed
tooptimizelatencyandbandwidthutilization[23,24]. Intheirwork,Ref.[25]presented
efficienttaskoffloadingandprofitmaximizationinMEC-enabled5GInternetofVehicles
(IoV).ThisstudyproposedaLyapunov-BasedProfitMaximization(LBPM)algorithmto
optimizethetime-averagedprofitofMECproviderswhileensuringtimelyandeffective
taskexecutionfromvehicles.
Additionally,thepreviousstudyonresourcemanagementinVNFplacementstillfaces
theproblemofduplicatesintheformofchainingandoverwhelmingresourceutilization.
Forinstance,refs.[26–28]studyVNFplacementandtrafficroutingsimultaneously,dividing
themethodsintotwophases: first,VNFplacement,andthenestablishingtheexecuting
links. To achieve optimal resource utilization, ref. [27] consider the tradeoff between
resourceconsumptionandlinks,providingatwo-phaseVNFplacementmethodologythat
usesconstraineddepth-firstsearchalgorithms(CDFSAs)andpath-basedgreedyalgorithms
to assign VNFs with minimum resource consumption [28]. The authors proposed two
methods,hybridSFCandaheuristicalgorithm,tosolvethedynamicSFCembeddingfor
chainingVNFnodes. However,theirutilizationoftheshortestpathorgreedyalgorithms
couldnotachievenetworkloadbalancing.
Inrecentyears,someresearchershavestartedapplyingmachinelearningtotackle
variousoptimizationproblems[29–31],withafocusonresourceallocation,resourceplace-
ment,scheduling,trafficrouting,resourceoffloading,andSFCorchestration. Forinstance,
ref.[32]proposedPPO-ERAtoprovideareal-time, adaptive, anddynamicstrategyfor
VNFs,addressingtaskdelaysandresourceutilization. Meanwhile,SFCdeploymentover
MECserverssharesidlecomputingresourcesthatutilizethesameSFC.In[33],VNFco-
operativeschedulingwithpriority-weighteddelayisexamined. Theirworkincorporated
DRL with a target Q-network to enhance solutions for the optimal problem related to
VNF scheduling, while supporting multidimensional resources in edge nodes. In [34],
a multi-objective SFC mapping technique based on DQN is proposed to achieve delay
andloadbalancingtargets. Intheirwork,Ref.[35]leveragestheDQNandMQDR-based

Sensors2025,25,4257 5of16
methodforthedynamicdeploymentofcustomizedSFCs,includingdynamicadjustments
ofSFCRs. Furthermore,in[36],theVNFformulationproblemisaddressedusinginteger
nonlinearprogrammingtominimizebandwidthcostsandensureserviceexecutionfor
end-to-enddelays.
Throughtheirstrategiesandsignificantefforts,theyenhanceresourceefficiencyand
effectiveresourceutilization. However,computationandresourceallocationtoidleVNFs
present challenges and drawbacks, particularly in terms of reallocating resources and
placement. ThiscanleadtooverwhelmingutilizationinrealtimewithinthesameSFC.
Toclarifythesignificanceofourresearch,wepresenttheutilizationofVNFresource
placementandallocationapproachescomparedtothepreviousstudiesmentionedabove.
We develop a novel dynamic resource allocation and placement based on diverse SFR
in NFVO. VNFs are monitored by NFVI to control resource adjustments that respond
to real-time changes in VNFs within SFCs, coordinating with DQN variance methods.
Furthermore,weconsiderthepriorityofSFCformanagingresourcesbasedonworkload
incomputingtasks.
3. ModelandProblemFormulation
Thissystemmodelsectiondiscussesoursystemsimulationandrepresentsthecom-
pleteVNFandSFCrelatedtoMECserversandtheIoTsensingnetwork. Regardingthe
resource allocation issue in the VNF of the SFC, the optimization goal of this paper is
to address resource placement and facilitate cost-effective application deployments by
consideringtheservicesrequiredformanagingenddevices.
3.1. NetworkModel
Inthenetworksection,weexaminedtheallocationandplacementofNFVresource
utilizationtoalignwiththecomputationandcommunicationdemandsofMECworkloads.
Inthispaper,weillustratethephysicalinfrastructureresourceinstantiationinvolvedin
creatingseveralNetworkFunctionsRequests(NFRs)tosupportmultipleServiceFunctions
(SFs) in terms of requirements and monitoring resource workload. IoT contributes to
resource-intensivenetworkdatatraffic,whichescalatesresource-heavycomputationand
complexworkloadsinedgenetworks,asdepictedinTable1.
Inthesystemmodel,theundirectedgraphisleveragedtorepresentnetworkfunction
resources,whereGisasetofMECserversandV isthesubsetofMECnodesthatconnect
tothelinkdenotedasE. Thetaskprocesscanbedefinedintheprimaryphaseasfollows:
• OffloadingtaskfromIoTtoMECserverforcomputingtask: Ineachtimeslot-t,IoT
devicesoffloadtask−jtoMEC−m. Equation(1)indicatesthecommunicationmodel
thatisassociatedbetweenend-devicesandtheMEC-serverfordatarate,denotedas
EDt forthestateofallocatedbandwidthbwt ,channelgaingt ,transmission
n−m n→m n→m
power pt,andnoise∀ℵ.
n
ptgt
EDt = bwt log (1+ n n→m) (1)
n−m n→m 2 ∀ℵ
In this scenario, we assume that the IoT fully offloads the task−j to MEC −m for
computationineverytimeslot−t,andalltheMECserversaresupposedlyequippedin
everysingledevice.

Sensors2025,25,4257
6of16
Table1.Notationsystemmodelinthenetworkmodel.
| Notation |     |     | Description           |     |     |
| -------- | --- | --- | --------------------- | --- | --- |
| G        |     |     | SetofMECservers       |     |     |
| E        |     |     | Setoflinks            |     |     |
| V        |     |     | SetofVNFs             |     |     |
| J        |     |     | Asetofnumbertasks     |     |     |
| N        |     |     | ThesetofIoTdevices    |     |     |
| T        |     |     | Numberoftimeslots     |     |     |
| R m      |     |     | ResourcesofMECservers |     |     |
| P        |     |     | SetalltheVNFsbyIoT-R  |     |     |
j j
| C up,m | Upper-boundcapacityofMECserverson(CPU,RAM,Disk) |                                     |                     |     |     |
| ------ | ----------------------------------------------- | ----------------------------------- | ------------------- | --- | --- |
| BW     |                                                 |                                     | MaximumofBandwidths |     |     |
| d      |                                                 | Propagationdelaybetweennodesonlinke |                     |     |     |
e
| F   |     |                                         | Numberofservicerequests |     |     |
| --- | --- | --------------------------------------- | ----------------------- | --- | --- |
| BWt |     | Upper-boundbandwidthofMEC-mattimeslot-t |                         |     |     |
up,m
| Ct  |     | RemainingresourcesofMEC-mattimeslot-t |     |     |     |
| --- | --- | ------------------------------------- | --- | --- | --- |
re,m
Decisionvariable
EqualsoneiftheVNFoftheservicerequestthatisdeployedat
xv (t)
| j,f |     |     | node-vattimeslot-t,otherwise |     |     |
| --- | --- | --- | ---------------------------- | --- | --- |
ye(t)
Selectingthevirtuallinkbetweennode-jattimeslot-t,otherwise
j
3.2. SFCRequests
ThesetIoT-RisdenotedbyF.Thej−th IoTdenotesIoT-R ,respondingtoa5-tuple
j
(S ,D , P,R ,R ,R f ). Inthistuple,S andD representthesourceIoTdeviceand
| j j j bw,j, | delay,j cpu,j |     | j   | j   |     |
| ----------- | ------------- | --- | --- | --- | --- |
destinationMECserver,respectively. ThesetP denotesthesequenceofVNFrequirements
j
byIoT-R . R andR denotethebandwidthconsumptionrequiredbyIoT-R and
| j bw,j,                         | delay,j |     |                |     | j   |
| ------------------------------- | ------- | --- | -------------- | --- | --- |
| maximumtoleratedE2EdelayofIoT-R |         |     | ,respectively. |     |     |
j
3.2.1. ResourceConstraints
WeensuresufficientMECservers’resourcetohostVNFsandbandwidthforhandling
| alltheIoT-R : |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- |
j
|     | ∑   | ∑ f   |          |            |     |
| --- | --- | ----- | -------- | ---------- | --- |
|     |     | R ·xm | ≤Ct ∀m   | ∈ G,∀t ∈ T | (2) |
|     |     | cpu,j | j,f re,m |            |     |
|     | i∈J | f∈Fj  |          |            |     |
f
where R indicates CPU demand of VNF-f in request-j, and Ct demonstrates the
cpu,j re,m
remainingresourcecapacityofMEC-mattime-t.
|     |     | ∑ ye(t)·R | ≤Ct |     |     |
| --- | --- | --------- | --- | --- | --- |
(3)
|     |     | j   | bw,j, | re,m |     |
| --- | --- | --- | ----- | ---- | --- |
i∈J
whereye(t) ∈
indicateswhetherlinkeistraversedbyIoT-Rinrequest-j Randequals1if
j
thetrafficofIoT-Rtraversphysicallink;0otherwise.
3.2.2. DelayConstraint
WeusePD
j toindicatethetotalpropagationdelayofIoT-Rnotexceedingthemaxi-
mumtotalofservicerequests:
|     | PD  | = ∑ ye(t)·d | ≤ R       | ∀j ∈ J,∀t ∈ T | (4) |
| --- | --- | ----------- | --------- | ------------- | --- |
|     | j   | j           | e delay,j |               |     |
e∈E
3.3. OptimizationModellingDesigns
ImproveresourceallocationandplacementofVNFovertheMECserver. Thispaper
aimstoimprovethesystemtomaximizesuccessfulplacementresourcesinservicerequests

Sensors2025,25,4257
7of16
whilemaintainingeffectivenessbyminimizingenergyconsumptionanddelayforeach
applicationundercomputationalandnetworkingresourcesconstraints.
|     |     |     |     |     |    |     |     |     |     |    |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
T
|     |     |     |     | ∑      | ∑ ∑  | ∑ xv |       |     |        |     |     |     |
| --- | --- | --- | --- | ------ | ---- | ---- | ----- | --- | ------ | --- | --- | --- |
|     |     |     |     | Max    |     |      | (t)−λ | .E  | −λ .PD | j  |     | (5) |
|     |     |     |     |        |      |      | j,f   | 1 j | 2      |     |     |     |
|     |     |     |     | t=1j=J | f∈Fj | v∈V  |       |     |        |     |     |     |
s.t. (2)–(4)
|     | 3.3.1. | StateSpace |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
To address the network formulation for resource utilization in orchestration and
management,thestateisgatheredfromnetworkcomponentswithcriticalstates,asshown
inFigure2. Theprocessproceedsbycomputingresourceallocation,gatheringresources
fromthenetwork,andorchestratingforSFR.TheMarkovdecisionprocessisutilizedto
interactwithintheNFVOenvironment.
• R m representsthecoordinationofresourcesintheMECservertopreservetheability
tohandlethecomputationtasksduringIoTandoffloadthetaskstoMEC-m.
• C representstheupper-boundresourceutilizationinMEC-mattimeslot-t.
up,m
• BW iscommunicationfromthelocaldeviceto MEC−m, stateoftotalbandwidth,
observedfromatotalbandwidthallocationandchannelgainbetweenenvironments.
|     | • BWt |     |            |     |                |     |     |           |         |     | MEC−m    |     |
| --- | ----- | --- | ---------- | --- | -------------- | --- | --- | --------- | ------- | --- | -------- | --- |
|     |       |     | represents | how | much bandwidth |     | is  | allocated | between |     | nodes to |     |
up,m
duringthepagingtasksattimeslot−t.
• Asubsetofatuplej comp(t),whichconsistsofprocessingtasks,includingtheconsumed
j−m
resources/energy,andtimespentfromexperience.
|     |     |     |     |     | (cid:110) |         |     |      |         | (cid:111) |     |     |
| --- | --- | --- | --- | --- | --------- | ------- | --- | ---- | ------- | --------- | --- | --- |
|     |     |     |     | S = | R ,C      | ,BW,BWt |     | ,j   | comp(t) |           |     |     |
|     |     |     |     | t   | m         | up,m    |     | up,m | i−m     |           |     | (6) |
Relevant
R
1
| State | T   | State | T   |     | State T |     | ... |     |     | StateT |     |     |
| ----- | --- | ----- | --- | --- | ------- | --- | --- | --- | --- | ------ | --- | --- |
|       | o   |       | 1   |     | 2       |     |     |     |     |        | n   |     |
R
2
Irrelevant

Figure2.Statespaceflowexecutiononaninterval.
|     | 3.3.2. | ActionSpace |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TheoffloadingtaskfromIoTdevicestotheMECserver,whosebackboneSDNcon-
trollerhasaglobalviewoftheflowentity,consistsoftheroutingtablesynchronizedasan
actionfromtheagentspace. Ontheotherhand,themechanismofSDN-MECenablesDRL
toempathizewiththeexperiencedbatchofresourceallocationandresourceplacement
off(t)
for performance patterns in each observation state iteration. a is set to determine
j
theconnectionbetweenIoTdevicesandMECserversforoffloadingtasks. Additionally,
aPlac (t) is the optimal MEC selection for VNF placement to align the ordering of SFC
mec|F
formsincomputingthetaskbasedonSFR.Thecorporationproposedbytheagentand
SDNcontrolleristooptimizetheflowruleofroutingexecutionininstallationandalle-
viationfortheeffectiveexecutionoftasksintermsofcompletiontimewithinmaximum
tolerancedelays.
|     |     |     |     |     |     | (cid:110) |       | (cid:111) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | ----- | --------- | --- | --- | --- | --- |
|     |     |     |     |     | a = | a off(t), | aPlac | (t)       |     |     |     | (7) |
|     |     |     |     |     | t   | j         | mec|F |           |     |     |     |     |

Sensors2025,25,4257
8of16
3.3.3. RewardBasedonPolicyChargingSelection
InthisproposedSDN-NFV,DRLaimstodealwiththeefficiencyofapplyingtheaction
a intotheMEC-IoTenvironmentstates bygainingtherewardr toshowtheimpactof
| t   |     |     |     |     | t   |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theactionthattransitionsthefollowingstates: s t+1 . Inthisstudy,theprimaryrewardby
dentedRt
env istosumthetotaloftwosub-rewards,reducedservicelatencyandlowered
| energyconsumption,denotedasrt |       |     |     | andrt     | ,respectively. |          |         |         |     |
| ----------------------------- | ----- | --- | --- | --------- | -------------- | -------- | ------- | ------- | --- |
|                               |       |     |     | Lat       | Ene            |          |         |         |     |
|                               |       |     | Rt  | =⋋ (t)·rt | +              | ⋋ (t)·rt |         |         |     |
|                               |       |     | env | lat       | Lat            | Ene      | Ene     |         | (8) |
|                               | ⋋ (t) | ⋋   | (t) |           |                |          | ⋋ (t)+⋋ | (t) =1) |     |
where lat and Ene are time-varying weights ( lat lat that adapt
based on current conditions. When the network load is high or delay-sensitive service
requestsareprioritized, ⋋ (t) isincreasedtofocusonreducinglatency.Conversely,under
lat
⋋
lowerloadsorwhenenergyconservationiscritical, (t)isemphasizedtominimize
Ene
energyconsumption.
TheoptimalpolicyissettoNFVOtoorchestratetheresourcesfromtheoverallbatch
thatmaximizesthelong-termrewardexpectationbyfollowingEquation(9). Ontheother
hand, Equation (10) presents an optimal policy selection for the state by following the
Bellmanequation.
|     |     |     |       |         | (cid:34) |      | (cid:35) |     |     |
| --- | --- | --- | ----- | ------- | -------- | ---- | -------- | --- | --- |
|     |     |     | π(t)∗ |         |          | ∑    |          |     |     |
|     |     |     |       | =argmax | E        | γtRt |          |     | (9) |
|     |     |     |       |         | π        |      | env      |     |     |
π
t∈T
|     |     |     |        | (cid:34) |           |     |            | (cid:35) |      |
| --- | --- | --- | ------ | -------- | --------- | --- | ---------- | -------- | ---- |
|     |     |     | ∗(s,a) | =E       | Rt        |     | ∗(cid:0) ′ | ′(cid:1) |      |
|     |     |     | Q      | ∼s′      | +γargmaxQ |     | s          | ,a       | (10) |
env
a′
3.4. PseudoDQNAlgorithmDesigns
Toeffectivelyaddressthedynamicandresource-constrainednatureofIoT-MEC,we
leverageDQN-basedalgorithmstoensureproperVNFplacementandresourceallocation
utilization. In this section, Algorithm 1 presents the DQN algorithms with embedding
ofVNFresourceplacements. TheDQN-basedVNFplacementalgorithmoperatesintwo
phases: the learning phase and the execution phase. From the learning phase, input
|     |     |     |     |     |     | (cid:16) |     |     | (cid:17) |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | -------- |
thestatefromtheIoT-MECenvironment,suchas V, E,R , C ,BW,BWt ,Ct (t) .
|     |     |     |     |     |     |     | m   | u,m up,m re,m |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
Thealgorithmbeginsbyinitializingtheexperiencereplaybufferandtheonlineandtarget
Q-networkparameters. IttheninitializesthesystemstatebasedonincomingSFRs,which
includetheresourcerequirementsandthestructureoftheVNFFG.Abatchofcandidate
MECserversissampledwithoutrepetitionforpotentialVNFplacement.Ateachtimestep−
t,arandomvalueisgeneratedtodeterminetheaction-selectionstrategy. Ifthevalueis
greaterthanathresholdϵ-epsilon,thealgorithmselectsanactionrandomlytoencourage
exploration. Otherwise,itchoosestheactionwiththemaximumQ-value,computedby
theonlinenetwork,toexploitthelearnedpolicy. Theselectedactioninvolvesdeployinga
VNFonachosenMECserverandcomputingtheshortestcommunicationpathwithinthe
VNFFG.Thealgorithmthenobservestheresultingrewardandtransitionstothenextstate,
storingtheexperiencetupleasaresult(s )inmemoryfromwhichmini-batches
|     |     |     |     |     | t ,a t ,r t ,s | t+1 |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
arerandomlysampledduringtraining. Foreachsample,thealgorithmcomputesatarget
Q-valueusingtheBellmanequationandupdatesthenetworkparametersbyminimizing
themeansquarederrorbetweenpredictedandtargetQ-values. Thenetworkparameter
updateprocessincludesboththeonlineQ-networkupdateviagradientdescentandthe
periodic synchronization of the target network to ensure stable learning. Furthermore,
timecomplexity,traininginvolvesthesamplingofabatchofsize N,witheachforward
andbackwardpasscostingΨ, yieldingO(N·Ψ)pertrainingstep; theinference,which
onlyrequiredgoingforwardthroughthenetwork,hasacomplexityO(Ψ)perdecision

Sensors2025,25,4257
9of16
step. The training is looped continuously until VNFs in SFR are successfully placed in
order of requirement. In the execution phase, the trained Q-network is used to make
placement decisions. The action with the maximum Q-value is selected and executed
at each time step, updating the placement strategy and transitioning the environment
stateaccordingly. ThisprocessrepeatsuntilthecompleteVNFchainisplaced,atwhich
j
pointthealgorithmoutputsthefinalplacementstrategyP . Thisapproachenablesthe
MEC
algorithm to make efficient and scalable placement decisions in a resource-constrained
MEC-NFV/SDN, thereby optimizing system-level performance metrics such as delay,
energyconsumption,andloadbalancing.
| Algorithm1: | Pseudo-codeofDQN-basedVNFplacementalgorithms |          |           |      |          |     |
| ----------- | -------------------------------------------- | -------- | --------- | ---- | -------- | --- |
|             |                                              | (cid:16) |           |      | (cid:17) |     |
| Input       | State=                                       | V, E,R   | C ,BW,BWt | ,Ct  | (t)      |     |
|             |                                              |          | m , u,m   | up,m | re,m     |     |
j
| Output | VNFplacementandallocationinMECserversP |     |     |     |     |     |
| ------ | -------------------------------------- | --- | --- | --- | --- | --- |
MEC
Learningprocess:
| 1   | Initializetheexperiencereply. |     |     |     |     |     |
| --- | ----------------------------- | --- | --- | --- | --- | --- |
| 2   | Foreach                       |     |     |     |     |     |
InitializethestatesofVNFfromSFR
3
|     |     |     | Sampleabatchof |     | MECServer−mwithoutrepetition |     |
| --- | --- | --- | -------------- | --- | ---------------------------- | --- |
Foreachtimestep−tdo
4
| 5   |     |                | Generaterandomlyvalue      |     |     |     |
| --- | --- | -------------- | -------------------------- | --- | --- | --- |
| 6   |     | Ifrandomvalue, | ≥ ϵthen                    |     |     |     |
| 7   |     |                | Randomlyselectanactiona(t) |     |     |     |
| 8   |     | Else           |                            |     |     |     |
Q−value
| 9   |     |       | Selectofactionswiththe |      | MAX                     |     |
| --- | --- | ----- | ---------------------- | ---- | ----------------------- | --- |
| 10  |     |       | a = argmax             | Q(s  | ,a ,θ)basedononline_net |     |
|     |     |       | t                      | at t | t                       |     |
| 11  |     | Endif |                        |      |                         |     |
12 EnforcetheactionthatdeploysVNFandcalculatestheshortestpathofVNFFG
| 13  |     |     | Calculatetherewardr             |           | t andnewstates | t+1              |
| --- | --- | --- | ------------------------------- | --------- | -------------- | ---------------- |
|     |     |     | Storethestatetransitionsample(s |           |                | )                |
| 14  |     |     |                                 |           | t              | ,a t ,r t ,s t+1 |
| 15  |     |     | r(s ,a ,s                       | )+γmaxQ(s | ,a ,θ−)        |                  |
|     |     |     | t t t+1                         |           | t t            |                  |
at+1
| 16  |     |                                                | Getupdatingthevalueofθ− |     | = θforeveryCsteps |     |
| --- | --- | ---------------------------------------------- | ----------------------- | --- | ----------------- | --- |
| 17  |     | IftheVNFplacementanddeploymenthasyetcompleted; |                         |     |                   |     |
| 18  |     | Then                                           |                         |     |                   |     |
Endif
20
| 21  | Endfor |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- |
Executionprocess:
| 22  | Readtheonline_netandtarget_net |     |     |     |     |     |
| --- | ------------------------------ | --- | --- | --- | --- | --- |
Foreachstep−t
23
| 24  |     | Do                                           |     |     |     |     |
| --- | --- | -------------------------------------------- | --- | --- | --- | --- |
| 25  |     | SelecttheactionwithMaxQ_value;               |     |     |     |     |
| 26  |     | Executetheactionandupdatetheplacementscheme: |     |     |     |     |
j
| 27  |        | P =                                | s     |       |     |     |
| --- | ------ | ---------------------------------- | ----- | ----- | --- | --- |
|     |        | MEC                                | t     |       |     |     |
| 28  |        | Updatethestate:                    | s t = | s t+1 |     |     |
| 29  |        | IftheVNFplacementiscompleted,then. |       |       |     |     |
| 31  |        | Endif                              |       |       |     |     |
| 32  | Endfor |                                    |       |       |     |     |
| 33  | Return |                                    |       |       |     |     |

Sensors2025,25,4257 10of16
4. PerformanceEvaluation
To conduct the network simulation [11,21], the network environment utilizes the
NetworkXlibrarytocreatenetworktopologiesforallnetworkcomponents. Asdepicted
inTable2,allsimulationsareexecutedonacomputerwithanAMDRyzen(R)75700X
CPU, 3.0 GHz, 32 GB (Advanced Micro Devices, Inc., Santa Clara, CA, USA), NVIDIA
RTX4080GPU(NVIDIA,SantaClara,CA,USA),andPythonprogramming. Anetwork
topologyisinstantiatedtorevealthenetworkforsettingthenetworktopology. Oncethe
network-tolerantdelayisset,thenumberofIoTdevicesissetto100tobeattributedacross
fiveMECservers. WeutilizetheDRLagentfunctionwiththeOpenAIlibrarywithinthe
DRLframework,initializedwithPyTorch.
Table2.ParameterconfigurationinthenetworkandDRLframework.
Parameters Specifications
Hostinginfrastructure Ryzen(R)75700x3dCPU@3.0GHz,32GB,NVIDIARTX4080GPU
NumberofIoT 100
NumberofMECservers 5
NF(types=5)
SFCtypeoflength(2–5)
Servicerequestconfiguration
Flowrate(64Kbps–4Mbps)
Tolerabletime(100–500)
Taskcomplexityandsizes Randomset(Low,normal,high)—(256Kbits,512Kbits,1024Kbits)
Learningrate 0.001
Discountfactor 0.95
Batchsize Randomset(32,64,128,256)
Exploration 0.5
Numberofepisodes 400
Pythonplatform PyTorch
4.1. ComparisonofProposedandReferenceSchemes
Our study conducts network evaluation and sets up three comparison schemes to
illustratehowtheproposedapproachdiffersfromthebaselineapproach. Thiscomparison
illustrates the performance differences in terms of various computation resource work-
loads for IoT-MEC task offloading, leading to enhanced energy efficiency and reduced
overheadlatency.
• DQN-MIoTisourproposedmethod,whichutilizesDRLalgorithmscombinedwith
NFVOinMECtoallocateresourcesforVNFplacement. OurproposedDRL-based
NFV control leverages a DQN architecture to approximate the Q-value function,
enablingcollaborativeconfigurationofSDN/NFVflowrulesforoptimizedplacement
and resource allocation. This method effectively trains the function approximator
tomanagehigh-dimensionalstateobservationsandrepresentations. Asdetailedin
Section3,theapproachincorporatesexperiencereplay,neuralnetworktraining,and
synchronizationwiththeSDN/NFVcontrollertolearnsophisticatedpolicies.
• DQL-MIoTissettoleveragetheDeepQ-learningapproach,whichenableslearning
fromthenetworkenvironmentandapplyingactiontocontrolpolicy;however,DL
achieves low performance in the complex network topology and can only handle
lightweightnetworktopologycases.
• Greedy-MIoTrepresentsthetraditionalSDN/NFVforIoT-MECserversincomput-
ingtaskmanagement. ThisbaselineapproachaddressesacentralizedMANOthat
managesresourcesandcontrolsthecharacteristicsofIoT,adheringtothedefinition
ofstandardNFVrules. Theresourcemanagementcontrollerisbasedontopology,

Sensors2025,25,4257 11of16
trafficconditions,servicerequirements,andoffloadingpolicies. Greedy-MIoTrelies
onnetwork-leveloptimization,efficientresourcemanagement,andresourceallocation
fornon-complexapplications.
• Random-MIoT indicates that the algorithm stochastically chooses an MEC service
toaningresssourcefromtraversingaVNFresourceinstanceandaroutingpathto
commonlychainingtwoadjacentVNFinstancesforeveryincomingIoT-R.
4.2. ResultsandDiscussion
In this section, we present the results for the proposed DQN-MIoT and reference
schemes,namelyDQL-MIoT,Greedy-MIoT,andRandom-MIoT,intermsofcumulative
reward, sub-rewards for latency and energy, packet drop ratio, packet delivery ratio,
throughput,anddelayinservices. Themeasurementofthisperformancemetricsignifi-
cantlyshowcaseshowoursystemsettingintegrateswiththeDQNframework,ensuring
thereliabilityofchainingVNFsandadjustingforresourcedifferencesunderdiverseappli-
cationsandworkloads. Thesametopologyandtasksizeareusedinthissimulation,but
thecontrollerandagentdifferintermsofperformancemetrics. Theresultdemonstratesthe
totalrewardthroughouteachsignificantscheme’sDQNphaseforexplorationandexploita-
tionwithin400episodes. Figure3illustratestheresultsoftheproposedmethod,showing
thetotalrewardover400episodes,asdefinedinEquation(8). Duringtheearlylearning
phase(episodes0–100),allapproachesbeginwithnegativecumulativerewardsduetoran-
dompolicyexplorationandineffectiveactionselection. Astrainingprogresses,DQN-MIoT
showsarapidimprovement,achievingapositivecumulativerewardafterapproximately
150episodes,steadilyincreasingto32.89atepisode400. Meanwhile,DQL-MIoTgradually
improvesandachievesafinalcumulativerewardof19.74,whichisapproximately40%
lowerthanDQN-MIoT.TheGreedy-MIoTmethodshowsminimalimprovement,ending
with a cumulative reward of only 2.53, which is approximately 92% lower than that of
DQN-MIoT. The Random-MIoT baseline performs the worst, consistently maintaining
negativerewardsandendingat−26.48,indicatingnoeffectivelearningoradaptation.
Figure3.Resultofcumulativerewardevaluation.
In Figure 4a, initially, all methods exhibit negative sub-rewards, indicating poor
latencyperformanceduetorandomorsub-optimalpolicyactionsduringearlylearning
phases. However, by episode 200, the DQN-MIoT approach begins to yield positive
sub-rewardvalues,signalingasuccessfuladaptationtotheMECworkloaddynamicsin
IoT scenarios. As learning continues, DQN-MIoT and DQL-MIoT demonstrate robust

Sensors2025,25,4257 12of16
convergencebehavior,withDQN-MIoTconsistentlyachievinghighersub-rewardvalues
than DQL-MIoT. By episode 400, DQN-MIoT achieves a latency sub-reward of 29.57,
comparedto26.51forDQL-MIoT,only5.17forGreedy-MIoT,and−30.31forrandom-MIoT.
Thissubstantialgapunderscoresthebenefitsofemployingavalue-basedQ-valuewith
optimizedexplorationstrategiesforlatency-sensitiveSFCplacement. Figure4billustrates
theefficiencyofenergyscorepointsasDQN-MIoT’strainingprocesstransitionstheagent
intoamorestablepolicyregime,resultinginahigherimmediaterewardscore. DQN-MIoT
demonstratedasteadyimprovement,eventuallypeakingasthetrainingprogresseddue
to its adaptive learning strategy, which optimized energy consumption under network
constraints. Incontrast,DQL-MIoTshowedmoregradualprogress,reflectingitsslower
convergence in handling energy efficiency within the MEC-enabled IoT environment.
TheGreedy-MIoTandRandom-MIoTconsistentlyunderperformedwithnegativeenergy
sub-rewardsthroughoutmostepisodes,astheylackedadaptivemechanismstomanage
resource allocation effectively. From the reward efficiency perspective, the proposed
DQN-MIoT scheme dynamically adjusts resource allocation and offloading decisions,
effectively balancing computational capacity and energy constraints. This adaptability
enablesimprovedhandlingofresource-constrainedandcomputation-intensivetaskswithin
thenetwork,demonstratingstrongsuitabilityforMEC-enabledIoTscenarioswhereenergy
efficiencyandtaskcompletionarecrucial.
Figure4.Performancemetricsonsub-rewardsof(a)latencyand(b)energy.
TheresultsaredemonstratedinFigure5a,bfortaskdeliveryanddropratios,where
networkstatesareconfiguredconsecutivelybysettingdifferentnetworkconditions,con-
gestionlevels,andapplicationtasksevery400simulationintervals. Weevaluatetheagent
basedonthefluctuationofinvestmentresultsinthenetworkparametersettingcompared
tothediversityofstateobservation. Inhightrafficfluctuationsandcomputation-intensive
environments,DQN-MIoTmaintainsitsadvantagewithaPDRof99.9681%,whereasDQL-
MIoTdropsto99.9145%, andGreedy-MIoTdeclinesfurtherto99.7568%. Theseresults
demonstratetherobustnessandreliabilityoftheDQN-MIoTframeworkinmaintaining
high data delivery rates even under increasing network loads. Meanwhile, at shorter
simulationdurations(20s),DQN-MIoTachievesanotablylowpacketdropratioof0.05%,
outperformingDQL-MIoT(0.09%),Greedy-MIoT(0.14%),andRandom-MIoT(0.24%). As
thesimulationtimeincreasesto380s,DQN-MIoTmaintainsitsperformanceadvantage,
recordingadropratioof0.18%,whileDQL-MIoT,Greedy-MIoT,andrandom-MIoTreach
0.245%,0.3401%,and0.3513%,respectively. Thisconsistentperformancetrendunderscores
thesuperiordecision-makingandadaptabilityoftheDQN-MIoTframeworkinmanaging
networktraffic,confirmingitssuitabilityforreal-time,data-sensitiveapplications.

Sensors2025,25,4257 13of16
Figure5.Performancemetricsof(a)packetdeliveryand(b)packetdropratio.
ThethroughputresultspresentedinFigure6,acrossdifferentsimulationtimes,further
reinforcethesuperiorperformanceoftheDQN-MIoTapproachcomparedtoDQL-MIoT
andGreedy-MIoT.At20s,DQN-MIoTachievesthehighestthroughputof805.94units,
slightlysurpassingDQL-MIoT(803.12)andnotablyoutperformingGreedy-MIoT(799.28).
DQN-MIoTmaintainsastablethroughputat801.75,whileDQL-MIoT,Greedy-MIoT,and
random-MIoTdropto798.11,780.82,and772.63,respectively. Thissteadytrendindicates
theDQN-MIoTmodel’sefficiencyinhandlingdatatrafficundervaryingloadconditions.
Figure6.Resultonthroughput.
AthoroughevaluationofperformancemetricsrevealsthatDQN-MIoTsignificantly
outperformsreferenceschemesintermsofconvergencespeed,finalrewardvalue,andover-
alllearningefficiency. Specifically,DQN-MIoTachievesa66.7%higherfinalcumulative
rewardthanDQL-MIoT,over12timeshigherthanGreedy-MIoT,andvastlysuperiorperfor-
mancecomparedtoRandom-MIoT.ThissubstantialimprovementinDQN-MIoT’sstrong
abilitytolearneffectivepoliciesforbalancinglatencyandenergytrade-offsindynamic
MEC-enabledIoTenvironmentsleadstomoreintelligentandrobustSFCdeployment.

Sensors2025,25,4257 14of16
5. Conclusions
Inthispaper,weproposedtheDQN-basedNFVinIoT-MECtohandleresourcecom-
putation for diverse services. We designed an intelligent task offloading and resource
orchestrationframeworkfordynamicIoT-MECenvironments. Theframeworkintegrates
SFCforVNFplacement,dynamicroutepathselection,andworkloaddistributionthrough
MEC-basedtaskoffloading.ByleveragingDRL,specificallyaDQN-basedMarkovDecision
Process,thesystemlearnstomakeadaptivedecisionsfortaskoffloadingandresourceallo-
cation. OursimulationresultsindicatethatDQN-MIoToutperformsbaselineapproaches
intermsofsub-rewardsonlatency,energyconsumptionforMECworkloadswithinheavy
fluctuatingtrafficchanges,packetdeliveryratio,packetdropratio,andthroughputinvari-
ousnetworkconditionsandresourceallocationvalues. Inthefuture,weaimtoincorporate
memory-augmentedandgraph-enhancedlearningmodelstoovercomethelimitationsof
LLMsincapturinglong-term,multi-stageattackpatterns. Moreover,futuresimulations
willconsiderfederatedandedge-awaredeploymentstohandleresourceconstraintsinreal-
timeenvironments. Wewillexplorelightweight,explainableAI(XAI)-drivenframeworks
toimproveinterpretabilityandtransparencyintaskorchestration.
Author Contributions: Conceptualization, S.R., I.R. and S.K.; methodology, S.R.; software, S.R.;
validation,S.R.;formalanalysis,S.R.;investigation,S.K.;resources,S.K.;datacuration,S.R.;writing—
original draft preparation, S.R. and S.K.; writing—review and editing, S.R.; visualization, S.R.;
supervision,I.R.andS.K.;projectadministration,S.K.;fundingacquisition,S.K.Allauthorshave
readandagreedtothepublishedversionofthemanuscript.
Funding:ThisworkwassupportedbytheInstituteofInformationandCommunicationsTechnology
Planning and Evaluation (IITP) grant, funded by the Korean government (MSIT) (No. RS-2022-
00167197,DevelopmentofIntelligent5G/6GInfrastructureTechnologyforTheSmartCity);inpart
byBK21FOUR(FosteringOutstandingUniversitiesforResearch)underGrant5199990914048;andin
partbytheSoonchunhyangUniversityResearchFund.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Deriveddatasupportingthefindingsofthisstudyareavailablefrom
thecorrespondingauthoronrequest.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. Anitha,P.;Vimala,H.S.;Shreyas,J.ComprehensiveReviewonCongestionDetection,Alleviation,andControlforIoTNetworks.
J.Netw.Comput.Appl.2024,221,103749.[CrossRef]
2. Alsharif, M.H.; Kelechi, A.H.; Jahid, A.; Kannadasan, R.; Singla, M.K.; Gupta, J.; Geem, Z.W.AComprehensiveSurveyof
Energy-EfficientComputingtoEnableSustainableMassiveIoTNetworks.Alex.Eng.J.2024,91,12–29.[CrossRef]
3. Ma,H.;Tao,Y.;Fang,Y.;Chen,P.;Li,Y.Multi-CarrierInitial-Condition-Index-AidedDCSKScheme:AnEfficientSolutionfor
MultipathFadingChannel.IEEETrans.Veh.Technol.2025,1–14.[CrossRef]
4. Yu,Q.;Wang,H.;He,D.;Lu,Z.EnhancedGroup-BasedChirpSpreadSpectrumModulation:DesignandPerformanceAnalysis.
IEEEInternetThingsJ.2025,12,5079–5092.[CrossRef]
5. Li,J.;Sun,G.;Wu,Q.;Niyato,D.;Kang,J.;Jamalipour,A.;Leung,V.C.M.CollaborativeGround-SpaceCommunicationsvia
EvolutionaryMulti-ObjectiveDeepReinforcementLearning.IEEEJ.Sel.AreasCommun.2024,42,3395–3411.[CrossRef]
6. Mijumbi,R.;Serrat,J.;Gorricho,J.-L.;Bouten,N.;DeTurck,F.;Boutaba,R.NetworkFunctionVirtualization:State-of-The-Artand
ResearchChallenges.IEEECommun.Surv.Tutor.2016,18,236–262.[CrossRef]
7. Aboubakar,M.;Kellil,M.;Roux,P.AReviewofIoTNetworkManagement:CurrentStatusandPerspectives.J.KingSaudUniv.
Comput.Inf.Sci.2021,34,4163–4176.[CrossRef]
8. Liyanage,M.;Porambage,P.;Ding,A.Y.;Kalla,A.DrivingForcesforMulti-AccessEdgeComputing(MEC)IoTIntegrationin5G.
ICTExpress2021,7,127–137.[CrossRef]

Sensors2025,25,4257 15of16
9. Singh,R.;Sukapuram,R.;Chakraborty,S.ASurveyofMobility-AwareMulti-AccessEdgeComputing:Challenges,UseCases
andFutureDirections.AdHocNetw.2023,140,103044.[CrossRef]
10. Wang,H.;Chen,P.Parallelism-AwareServiceFunctionChainPlacementforDelay-SensitiveIoTApplicationswithVNFReusein
MobileEdgeComputing.InProceedingsofthe2024IEEEInternationalConferenceonWebServices(ICWS),Shenzhen,China,
7–13July2024;pp.968–973.[CrossRef]
11. Ros,S.;Tam,P.;Song,I.;Kang,S.;Kim,S.HandlingEfficientVNFPlacementwithGraph-BasedReinforcementLearningforSFC
FaultTolerance.Electronics2024,13,2552.[CrossRef]
12. Tam,P.;Kim,S.Graph-BasedDeepReinforcementLearninginEdgeCloudVirtualizedO-RANforSharingCollaborativeLearning
Workloads.IEEETrans.Netw.Sci.Eng.2024,12,302–318.[CrossRef]
13. Wang,H.;Guo,R.;Ma,P.;Ruan,C.;Luo,X.;Ding,W.;Zhong,T.;Xu,J.;Liu,Y.;Chen,X.TowardsMobileSensingwithEvent
CamerasonHigh-AgilityResource-ConstrainedDevices:ASurvey.arXiv2025,arXiv:2503.22943.[CrossRef]
14. Ullah,S.A.;Bibi,M.;Hassan,S.A.;Abou-Zeid,H.;Qureshi,H.K.;Jung,H.;Mahmood,A.;Gidlund,M.;Hossain,E.FromNodes
toRoads:SurveyingDRLApplicationsinMEC-EnhancedTerrestrialWirelessNetworks.IEEECommun.Surv.Tutor.2025,1–42.
[CrossRef]
15. Ding,H.;Zhao,Z.;Zhang,H.;Liu,W.;Yuan,D.DRL-BasedComputationEfficiencyMaximizationinMEC-EnabledHeteroge-
neousNetworks.IEEETrans.Veh.Technol.2024,73,15739–15744.[CrossRef]
16. Wu,J.;Yin,J.;Zhao,X.;Liu,Y.DRL-DrivenAdaptiveSFCDeploymentwithGCNinDistributedCloudNetworks.InProceedings
ofthe2025IEEE4thInformationTechnologyandMechatronicsEngineeringConference(ITOEC),Chongqing,China,14–16
March2025;pp.1269–1273.[CrossRef]
17. Onsu,M.A.;Lohan,P.;Kantarci,B.;Janulewicz,E.;Slobodrian,S.ANewRealisticPlatformforBenchmarkingandPerformance
EvaluationofDRL-DrivenandReconfigurableSFCProvisioningSolutions.arXiv2024,arXiv:2406.10356.[CrossRef]
18. Liu, Y.; Lu, Y.; Li, X.; Qiao, W.; Li, Z.; Zhao, D. SFC Embedding Meets Machine Learning: Deep Reinforcement Learning
Approaches.IEEECommun.Lett.2021,25,1926–1930.[CrossRef]
19. Escheikh, M.; Taktak, W. Online QoS/QoE-Driven SFC Orchestration Leveraging a DRL Approach in SDN/NFV Enabled
Networks.Wirel.Pers.Commun.2024,137,1511–1538.[CrossRef]
20. Golec,M.;Khamayseh,Y.;Melhem,S.B.;Alwarafy,A.LLM-DrivenAPTDetectionfor6GWirelessNetworks: ASystematic
ReviewandTaxonomy.arXiv2025,arXiv:2505.18846.[CrossRef]
21. Ros,S.;Kang,S.;Iv,T.;Song,I.;Tam,P.;Kim,S.Priority-AwareResourceAllocationforVNFDeploymentinServiceFunction
ChainsBasedonGraphReinforcementLearning.Comput.Mater.Contin.2025,83,1649–1665.[CrossRef]
22. Xu,Y.;He,Z.;Li,K.ResourceAllocationandPlacementinMulti-AccessEdgeComputing. Stud. BigData2024,151,39–62.
[CrossRef]
23. Tomassilli,A.;Giroire,F.;Huin,N.;Pérennès,S.rovablyEfficientAlgorithmsforPlacementofServiceFunctionChainswith
OrderingConstraints.InProceedingsoftheIEEEINFOCOM2018—IEEEConferenceonComputerCommunications,Honolulu,
HI,USA,16–19April2018.[CrossRef]
24. Guérout,T.;Gaoua,Y.;Artigues,C.;Costa,G.D.;Lopez,P.;Monteil,T.MixedIntegerLinearProgrammingforQualityofService
OptimizationinClouds.FutureGener.Comput.Syst.2017,71,1–17.[CrossRef]
25. Sun,G.;Wang,Z.;Su,H.;Yu,H.;Lei,B.;Guizani,M.ProfitMaximizationofIndependentTaskOffloadinginMEC-Enabled5G
InternetofVehicles.IEEETrans.Intell.Transp.Syst.2024,25,16449–16461.[CrossRef]
26. Pei,J.;Hong,P.;Xue,K.;Li,D.EfficientlyEmbeddingServiceFunctionChainswithDynamicVirtualNetworkFunctionPlacement
inGeo-DistributedCloudSystem.IEEETrans.ParallelDistrib.Syst.2019,30,2179–2192.[CrossRef]
27. Jin,P.;Fei,X.;Zhang,Q.;Liu,F.;Li,B.Latency-awareVNFChainDeploymentwithEfficientResourceReuseatNetworkEdge.
InProceedingsoftheIEEEConferenceonComputerCommunications(IEEEINFOCOM),Toronto,ON,Canada,6–9July2020;
pp.267–276.
28. Zheng,D.;Peng,C.;Liao,X.;Cao,X.TowardOptimalHybridServiceFunctionChainEmbeddinginMultiaccessEdgeComputing.
IEEEInternetThingsJ.2020,7,6035–6045.[CrossRef]
29. Tam,P.;Ros,S.;Song,I.;Kang,S.;Kim,S.ASurveyofIntelligentEnd-To-EndNetworkingSolutions:IntegratingGraphNeural
NetworksandDeepReinforcementLearningApproaches.Electronics2024,13,994.[CrossRef]
30. Mao,M.;Hong,M.YOLOObjectDetectionforReal-TimeFabricDefectInspectionintheTextileIndustry:AReviewofYOLOv1
toYOLOv11.Sensors2025,25,2270.[CrossRef]
31. Sun,R.;Cheng,N.;Li,C.;Chen,F.;Chen,W.Knowledge-DrivenDeepLearningParadigmsforWirelessNetworkOptimizationin
6G.IEEENetwork2024,38,70–78.[CrossRef]
32. Zhai,X.;He,Z.;Xiao,Y.;Wu,J.;Yu,X.DynamicVNFDeploymentandResourceAllocationinMobileEdgeComputing. In
Proceedingsofthe2024IEEEInternationalSymposiumonParallelandDistributedProcessingwithApplications(ISPA),Kaifeng,
China,30October–2November2024;pp.573–581.[CrossRef]

Sensors2025,25,4257 16of16
33. Yao,J.;Wang,J.;Wang,C.;Yan,C.DRL-BasedVNFCooperativeSchedulingFrameworkwithPriority-WeightedDelay.IEEE
Trans.Mob.Comput.2024,23,11375–11388.[CrossRef]
34. Xu,S.;Li,Y.;Guo,S.;Lei,C.;Liu,D.;Qiu,X.Cloud-EdgeCollaborativeSFCMappingforIndustrialIoTUsingDeepReinforcement
Learning.IEEETrans.Ind.Inform.2021,18,4158–4168.[CrossRef]
35. Zhu,R.;Wang,P.;Geng,Z.;Zhao,Y.;Yu,S.Double-AgentReinforcedVNFCDeploymentinEONsforCloud-EdgeComputing.J.
Light.Technol.2023,41,5193–5208.[CrossRef]
36. Gao,X.;Liu,R.;Kaushik,A.;Zhang,H.DynamicResourceAllocationforVirtualNetworkFunctionPlacementinSatelliteEdge
Clouds.IEEETrans.Netw.Sci.Eng.2022,9,2252–2265.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.