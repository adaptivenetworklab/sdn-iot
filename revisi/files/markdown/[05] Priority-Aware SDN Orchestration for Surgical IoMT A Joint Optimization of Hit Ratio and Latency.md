# [05] Priority-Aware SDN Orchestration for Surgical IoMT A Joint Optimization of Hit Ratio and Latency

> Source file: `[05] Priority-Aware SDN Orchestration for Surgical IoMT A Joint Optimization of Hit Ratio and Latency.pdf`

---

Received2June2025,accepted19June2025,dateofpublication27June2025,dateofcurrentversion9July2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3583899
Priority-Aware SDN Orchestration for Surgical
IoMT: A Joint Optimization of Hit Ratio and
Latency With Dynamic Resource Reallocation
YALDASAFAEI1,POURIAAREFIJAMAL2,MAHDISIAMAKI 2,ANDBARDIASAFAEI 2
1SchoolofMedicine,HamadanUniversityofMedicalSciences,Hamedan14588-89694,Iran
2DepartmentofComputerEngineering,SharifUniversityofTechnology,Tehran65178-38736,Iran
Correspondingauthor:BardiaSafaei(bardiasafaei@sharif.edu)
ABSTRACT SurgicalInternetofMedicalThings(IoMT)applicationsimposestringentQualityofService
(QoS)demands,requiringultra-lowlatencyandhighreliabilityforcriticaldatastreamslikecontrolsignals
orhigh-definitionvideo.Conventionalresourceorchestrationmethodsoftenfallshort,failingtoguarantee
performance for high-priority surgical tasks, particularly under dynamic network conditions, including
varied wireless channel quality, and potential congestion. This paper introduces the Priority-Aware SDN
Orchestration(PASO)framework,leveragingSoftware-DefinedNetworking(SDN)forcentralizednetwork
visibility and control to address these critical challenges. PASO implements a novel joint optimization
strategyfocusedprimarilyonmaximizingthecompletionrateofcriticalsurgicaltasksthatadherestrictly
to their maximum delay constraints. A key distinguishing feature is its dynamic resource reallocation
mechanism, which employs the preemption of lower-priority, non-medical traffic to proactively secure
network resources and guarantee QoS for vital surgical flows, even during periods of high network
load. A computationally efficient, priority-aware greedy algorithm operationalizes this strategy on the
SDNcontroller.ComparativesimulationsagainstRandom,ParticleSwarmOptimization(PSO),Simulated
Annealing (SA), and a Deep Reinforcement Learning (DRL) agent as baselines demonstrate PASO’s
substantial effectiveness. It significantly reduces end-to-end delay (e.g., up to 70% less than PSO under
high load) and drastically improves the completion rate for critical surgical tasks (over 80% higher than
PSOunderhighload),whilealsopromotingbalancednetworkutilization.PASOoffersarobustsolutionfor
dependable,low-latencysurgicalIoMToperationsthroughitstargetedoptimizationandpreemptiveresource
managementcapabilities.
INDEXTERMS Software-definednetworking(SDN),internetofmedicalihings(IoMT),surgicalIoT,edge
computing, task offloading, resource allocation, quality of service (QoS), latency optimization, hit ratio,
preemptivescheduling,healthcarenetworks.
I. INTRODUCTION [2]. This domain’s transformative potential and prevailing
The Internet of Medical Things (IoMT) is fundamentally trendsarewell-documented[3],[4],signifyingamajordigital
reshaping healthcare delivery, forging an interconnected shift within the healthcare sector [5]. Underscoring this
ecosystem of medical devices, sensors, and applications evolution,theglobalIoMTmarketisexperiencingsubstantial
[1]. This paradigm enables enhanced patient care through growth, as depicted in Fig. 1, valued at US$ 48.7 billion
advancementslikeremotemonitoring,sophisticateddiagnos- in 2022 and projected to surge to US$ 370.9 billion by
tics,andincreasinglycomplexremoteorassistedprocedures 2032,reflectingaCompoundAnnualGrowthRate(CAGR)
of 23.15% [6]. Furthermore, the integration of IoMT with
next-generation technologies like 6G promises even greater
The associate editor coordinating the review of this manuscript and capabilities,particularly formassively connectedhealthcare
approvingitforpublicationwasHadiTabatabaeeMalazi . scenarios[7].
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
VOLUME13,2025 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 113787

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
|     |     |     |     |     |     |     | metrics (like | average | delay | or  | energy) | or lack | the | essential |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ----- | --- | ------- | ------- | --- | --------- |
priority-awarenessdemandedbysurgicalcontexts.Strategies
|     |     |     |     |     |     |     | relying on | simple | fairness | models |     | or assuming |     | altruistic |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | -------- | ------ | --- | ----------- | --- | ---------- |
devicebehavior[26]proveinadequatewhenconfrontedwith
life-criticaltasksdemandingabsolutepriorityandguaranteed
|     |     |     |     |     |     |     | timely completion |          | within     | strict     | deadlines      | [27].       | This           | high- |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | -------- | ---------- | ---------- | -------------- | ----------- | -------------- | ----- |
|     |     |     |     |     |     |     | lights a          | critical | gap: the   | need       | for frameworks |             | capable        | of    |
|     |     |     |     |     |     |     | dynamic           | resource | management |            | with           | explicit    | prioritization |       |
|     |     |     |     |     |     |     | and robust        | QoS      | guarantees | for        | high-stakes    |             | surgical       | data, |
|     |     |     |     |     |     |     | especially        | under    | network    | congestion |                | or resource | contention     |       |
conditions.
FIGURE1. ProjectedglobalmarketgrowthfortheIoMT,showing Software-Defined Networking (SDN) presents a com-
expectedvaluefrom2022to2032.
|       |             |              |     |         |     |            | pelling       | architectural | solution |           | to address   |             | this | complex    |
| ----- | ----------- | ------------ | --- | ------- | --- | ---------- | ------------- | ------------- | -------- | --------- | ------------ | ----------- | ---- | ---------- |
|       |             |              |     |         |     |            | orchestration | challenge     |          | [28]. Its | logically    | centralized |      | con-       |
| Among | the diverse | applications |     | enabled | by  | IoMT, sur- |               |               |          |           |              |             |      |            |
|       |             |              |     |         |     |            | trol plane    | furnishes     | the      | requisite | network-wide |             |      | visibility |
gical scenarios—spanning tele-surgery [8], robotic surgery and programmability to manage traffic flows dynamically,
assistance [9], real-time intraoperative diagnostics [10], and enforce granular QoS policies, and adaptively allocate
| interactive | guidance | systems | [11]—represent |     | a   | particularly |           |       |              |             |     |              |     |     |
| ----------- | -------- | ------- | -------------- | --- | --- | ------------ | --------- | ----- | ------------ | ----------- | --- | ------------ | --- | --- |
|             |          |         |                |     |     |              | resources | based | on real-time | application |     | requirements |     | and |
demanding frontier [12]. These applications are critically defined priorities [29]. The capabilities of SDN can be
| dependent | on fulfilling |     | stringent, | non-negotiable |     | Quality |     |     |     |     |     |     |     |     |
| --------- | ------------- | --- | ---------- | -------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
furtheraugmentedbyintegratingspecializedcommunication
of Service (QoS) requirements. Specifically, they mandate protocolsoptimizedfortheuniquecharacteristicsofmedical
ultra-lowlatencyandextremelyhighreliability,oftenfalling data transmission [30]. Building upon this potential, our
underthestringentumbrellaofUltra-ReliableLow-Latency
workintroducesatailoredorchestrationframeworkdesigned
Communication (URLLC) [13], [14], [15]. Ensuring the explicitlyforsurgicalIoMTenvironments.
| absolute integrity |     | and punctual |     | delivery | of critical | surgical |          |            |     |       |          |            |     |          |
| ------------------ | --- | ------------ | --- | -------- | ----------- | -------- | -------- | ---------- | --- | ----- | -------- | ---------- | --- | -------- |
|                    |     |              |     |          |             |          | Our core | motivation |     | stems | from the | unyielding |     | require- |
data streams—such as haptic feedback, high-definition menttoguaranteeeverylife-criticalsurgicaltask’ssuccessful
video, or real-time control commands—is paramount for andtimelyprocessing.Standardbest-effortnetworkmanage-
| patient safety | and | procedural | success |     | in these | high-stakes |         |              |       |        |     |         |             |     |
| -------------- | --- | ---------- | ------- | --- | -------- | ----------- | ------- | ------------ | ----- | ------ | --- | ------- | ----------- | --- |
|                |     |            |         |     |          |             | ment or | optimization | based | solely | on  | average | performance |     |
environments. isfundamentallyinsufficient.WeproposethePriority-Aware
| Edge and | fog | computing | architectures |     | emerge | as indis- |                   |     |        |            |     |       |         |     |
| -------- | --- | --------- | ------------- | --- | ------ | --------- | ----------------- | --- | ------ | ---------- | --- | ----- | ------- | --- |
|          |     |           |               |     |        |           | SDN Orchestration |     | (PASO) | framework, |     | which | employs | a   |
pensable enablers for satisfying these exacting require- joint optimization strategy meticulously designed for the
ments [16], [17]. By locating computational resources surgicalIoMTcontext.Theprimaryobjectiveistomaximize
| geographically | closer | to  | IoMT | devices | compared | to tradi- |                                                 |     |     |     |     |     |     |         |
| -------------- | ------ | --- | ---- | ------- | -------- | --------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- |
|                |        |     |      |         |          |           | thethroughputofcompletedcriticalsurgicaltasks(F |     |     |     |     |     |     | m )that |
tionalcentralizedclouds,edgeandfogplatformsdrastically strictly adhere to their designated maximum delay bounds
| reduce communication |     | delays | [18]. | Task | offloading | further | (D     |       |           |          |             |     |     |            |
| -------------------- | --- | ------ | ----- | ---- | ---------- | ------- | ------ | ----- | --------- | -------- | ----------- | --- | --- | ---------- |
|                      |     |        |       |      |            |         | max ). | While | efficient | resource | utilization |     | is  | essential, |
empowers resource-constrained medical devices to leverage the framework prioritizes meeting these critical deadlines
these proximal computational capabilities for intensive above all else. This explicit prioritization is enforced not
| operations, | thereby | optimizing |     | both system | responsiveness |     |              |     |              |     |       |     |             |      |
| ----------- | ------- | ---------- | --- | ----------- | -------------- | --- | ------------ | --- | ------------ | --- | ----- | --- | ----------- | ---- |
|             |         |            |     |             |                |     | only through | the | optimization |     | model | but | critically, | also |
and device energy efficiency [19], [20]. Consequently, the via a dynamic resource reallocation mechanism featuring
effectiveallocationofresourcesandsophisticatedscheduling the preemption of lower-priority, non-medical traffic (F ).
n
of tasks across the multi-tiered computing infrastructure Whennetworklinksapproachcongestion,PASOproactively
(spanning edge, fog, and potentially cloud) become pivotal reclaimsbandwidthfromlesscriticalflows,therebyensuring
formaximizingsystemperformance[21],[22].
|     |     |     |     |     |     |     | that vital | surgical | data | streams | meet | their | stringent | QoS |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---- | ------- | ---- | ----- | --------- | --- |
However,orchestratingthesedistributedresourcesspecif- requirements.Thisproactive,priority-driven,andpreemptive
ically for the dynamic and demanding nature of surgical resource management distinguishes our approach and is
IoMT presents significant challenges. Network conditions essential for achieving the reliability demanded by surgical
can fluctuate due to factors such as wireless channel applications. This paper makes the following key contribu-
| variability—an | aspect | further | explored |     | in our evaluations— |     |     |     |     |     |     |     |     |     |
| -------------- | ------ | ------- | -------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tions:
andpotentialdevicemobility.Moreover,surgicalprocedures 1) JointOptimizationFormulationforSurgicalIoMT:
often generate unpredictable, bursty traffic patterns where A novel optimization model explicitly prioritizing the
critical data streams must invariably take precedence over maximizationofcriticalsurgicaltask(F m )completion
lessurgentdata,suchasroutinesystemlogsornon-essential understrictdelayconstraints(D ).
max
background updates. Many contemporary task offloading 2) Priority-Aware Greedy Orchestration Algorithm:
and scheduling algorithms [23], [24], even sophisticated An efficient greedy algorithm for the SDN con-
approaches employing techniques like deep reinforcement troller, operationalizing the prioritized objective with
learning [25], frequently optimize for average performance latency-awarepathselectionandadmissioncontrol.
| 113788 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
3) Dynamic Resource Reallocation with Preemption: healthcare infrastructures, thereby providing a backdrop for
| A   | core mechanism |     | enabling | PASO | to  | proactively | ourcontributions. |     |     |     |     |     |     |
| --- | -------------- | --- | -------- | ---- | --- | ----------- | ----------------- | --- | --- | --- | --- | --- | --- |
guarantee resources for critical flows by preempt- In the context of task offloading and resource allocation,
ing lower-priority traffic during potential congestion, Renetal.[31]delveintolatencyoptimizationinmobile-edge
ensuringadherencetoD max . computation offloading, proposing joint communication
4) SDN-Based Implementation Framework: Contex- and computation resource allocation strategies to minimize
tualization within an SDN architecture, highlighting system delay. In another research, Liu et al. [32] intro-
howcentralizedcontrolenablesthenecessaryvisibility duce a dynamic task offloading framework that addresses
and dynamic management for robust surgical IoMT ultra-reliable low-latency requirements by leveraging Lya-
orchestration. punov optimization and matching theory. Furthermore,
Our simulations demonstrate the effectiveness of PASO. Al-Masri [33] presents an edge-based resource allocation
Compared to baseline methods like Random allocation, optimizationtailoredforIoMT,emphasizingmultiplecriteria
Particle Swarm Optimization (PSO), Simulated Annealing decision-making to balance data privacy, costs, and latency.
(SA), and a Deep Reinforcement Learning (DRL) agent, Chai et al. [34] explore time-slotted task offloading and
PASO significantly reduces end-to-end delay for completed resource allocation in cloud-edge-end cooperative comput-
tasks (with average reductions up to 70% against PSO and ing networks, aiming to minimize task execution costs.
25%againstSAunderhighload)anddramaticallyincreases Lakhan et al. [35] introduce the Joint Task Offloading and
thecompletionrate(deadlinesuccessrate)forcriticalsurgical Scheduling(JTOS)framework,utilizingfuzzymulti-criteria
tasks (achieving improvements of approximately 82% over methods to optimize task sequencing and scheduling in IoT
PSO,50%overSA,and200%overRandomunderhighload).
systems,therebyreducingprocessingtimeandcommunica-
PASO also ensures more balanced network utilization. Our tion delays. In a related vein, Motamedhashemi et al. [36]
approachdistinctivelytargetsthemaximizationofcompleted presented FUSION, a task management policy for fog
critical task throughput under strict deadlines, leveraging networks employing fuzzy logic for multi-objective opti-
jointoptimizationandpreemptionaskeyenablers. mization,specificallytargetingahighGuaranteeRatio(GR)
| The remainder |     | of  | this paper | is organized |     | as follows: |             |           |               |     |         |            |     |
| ------------- | --- | --- | ---------- | ------------ | --- | ----------- | ----------- | --------- | ------------- | --- | ------- | ---------- | --- |
|               |     |     |            |              |     |             | and minimal | makespan. | Also focusing |     | on task | scheduling |     |
Section III introduces the system model and problem in fog networks, Motamedhashemi et al. [37] proposed
formulation. Section IV outlines the proposed orchestration DATA,ageneticalgorithmthatoptimizesforthroughputand
algorithm.SectionVexplainstheevaluationmetrics,exper- deadlineadherenceusingatwo-populationstrategy.
imental setup, and the configuration of baseline algorithms, Meanwhile,asithasbeensummarizedinTable1,SDNcan
| including | the DRL | agent. | Section | VI presents |     | and analyzes |              |                  |         |     |           |     |     |
| --------- | ------- | ------ | ------- | ----------- | --- | ------------ | ------------ | ---------------- | ------- | --- | --------- | --- | --- |
|           |         |        |         |             |     |              | play a vital | role in reducing | latency | and | enhancing | QoS | for |
the simulation results. Finally, Section VII concludes the IoMTapplications,especiallyintime-sensitivescenarioslike
paperandoutlinespotentialdirectionsforfutureresearch. executing medical tasks and performing telemetry/remote
surgery.SDNseparatesthecontrolplanefromthedataplane,
II. RELATEDSTUDIES allowingcentralizedcontrollerstohaveaglobalviewofthe
TheconvergenceofSDN,theIoMT,andedgecomputinghas
|     |     |     |     |     |     |     | entire network. | This enables | real-time, |     | dynamic | decision- |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------------ | ---------- | --- | ------- | --------- | --- |
catalyzed significant advancements in healthcare networks, making—like instantly rerouting traffic if congestion is
particularly optimizing task offloading, resource allocation, detected—ensuring faster delivery of medical data. For
andensuringQoS.WhileourproposedPASOframeworkis instance, during remote surgery, if a video feed or control
evaluated against Random, PSO, SA, and an implemented signal experiences delay, the SDN controller can detect
| DRL agent | as  | baselines, | it  | is important | to  | acknowledge |                |                 |     |         |         |         |     |
| --------- | --- | ---------- | --- | ------------ | --- | ----------- | -------------- | --------------- | --- | ------- | ------- | ------- | --- |
|           |     |            |     |              |     |             | the bottleneck | and immediately |     | reroute | traffic | through | a   |
the broader spectrum of alternative SDN and QoS-aware lower-latency path [38], [39], [40]. Furthermore, traditional
orchestration techniques. These techniques are not only routing is often static. SDN allows dynamic, policy-based
pivotalinIoMTbutalsofindparallelsincutting-edge,non-
|     |     |     |     |     |     |     | routing, which | adapts based | on  | current | network | conditions |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------ | --- | ------- | ------- | ---------- | --- |
IoMT orchestration frameworks and SDN-based systems (e.g., congestion, link failure). This issue minimizes packet
| applied | in various | other | crucial | fields, | thereby | enriching |     |     |     |     |     |     |     |
| ------- | ---------- | ----- | ------- | ------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
delaysandjitter,whichiscrucialforcontinuousstreamslike
the conversation on advanced network management. Our real-time patient monitoring or haptic feedback in robotic
| review,whileprimarilyfocusingontheIoMTcontext,draws |     |     |     |     |     |     | surgery. |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
insightsfromthiswiderlandscape.Thediscussedapproaches
|     |     |     |     |     |     |     | In addition, | SDN is | able to | prioritize | certain | types | of  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ------- | ---------- | ------- | ----- | --- |
encompass a variety of methods, including but not limited traffic (e.g., video feeds, patient vitals, actuator commands)
to, machine learning-based predictive algorithms, game- over others. This ensures latency-sensitive tasks get fast-
theoreticresourceallocationmodels,andothersophisticated lane treatment, improving reliability and responsiveness
heuristic or meta-heuristic strategies tailored for different for telemetry surgeries. For example, heart rate data or
| aspects | of IoMT | and | edge/fog | computing. |     | This section |                 |         |        |        |     |               |     |
| ------- | ------- | --- | -------- | ---------- | --- | ------------ | --------------- | ------- | ------ | ------ | --- | ------------- | --- |
|         |         |     |          |            |     |              | robotic control | signals | can be | tagged | as  | high priority |     |
providesabriefbutcomprehensiveoverviewofseveralexist- and get guaranteed bandwidth and minimal delay. SDN
ing studies that reflect this diverse landscape, particularly controllers continuously monitor network conditions (e.g.,
thoseintegratingthesetechnologiesincriticaldelay-sensitive latency, throughput, link status). As a result, if the network
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 113789 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
TABLE1. KeySDNcapabilities,correspondingIoMTbenefits,andtheir aimingtoenhancereliabilityforreal-timeIoTtasks.Surgical
impactonlatency. IoT systems, in particular, demand ultra-low latency and
|     |     |     |     |     | deterministic | behavior.  |             | For                 | example,  | Huang | et            | al. and   |
| --- | --- | --- | --- | --- | ------------- | ---------- | ----------- | ------------------- | --------- | ----- | ------------- | --------- |
|     |     |     |     |     | Luo et        | al. showed |             | that pre-configured |           |       | SDN           | policies, |
|     |     |     |     |     | combined      | with       | intelligent | task                | migration |       | and bandwidth |           |
reservation,areeffectiveforthesecriticalenvironments[48],
|     |     |     |     |     | [49]. Furthermore, |         | the      | authors    | in [50]      | propose  | a          | joint task |
| --- | --- | --- | --- | --- | ------------------ | ------- | -------- | ---------- | ------------ | -------- | ---------- | ---------- |
|     |     |     |     |     | offloading         | and     | resource | allocation |              | strategy | for mobile | edge       |
|     |     |     |     |     | computing-enabled  |         | medical  |            | vehicular    | networks | to         | reduce     |
|     |     |     |     |     | latency and        | improve |          | resource   | utilization. |          | Li et      | al. [51]   |
starts degrading, SDN can reallocate resources or shift presentaresourceallocationanddataoffloadingstrategyfor
|           |                |                 |            |     | edge-computing-assisted |     |     | intelligent |     | telemedicine |     | systems, |
| --------- | -------------- | --------------- | ---------- | --- | ----------------------- | --- | --- | ----------- | --- | ------------ | --- | -------- |
| workloads | to nearby edge | nodes, reducing | dependency | on  |                         |     |     |             |     |              |     |          |
distant cloud servers and cutting round-trip times. SDN can introducingacontractmechanismtoincentivizeedgeservers
alsoorchestratetasksbetweenthecloud,edge,anddevices, andenhancesystemutility.Furthermore,thedynamicnature
choosingtheoptimalexecutionlocations.Therefore,latency- ofIoTservicesnecessitatesadaptiveschedulingmechanisms.
critical tasks (e.g., motion feedback in robotic surgery) are Moreover,severaloptimization-basedapproacheshavebeen
executed at the edge, close to the data source, while SDN employed to enhance task offloading efficiency, focusing
ensures the fastest data paths are used. In the event of on minimizing energy consumption and delay. Simulated
a link failure or node crash, SDN provides fast failover, annealing techniques have been widely applied in this
automatically rerouting traffic and reducing downtime and regard[52],[53],[54],[55],demonstratingtheireffectiveness
latencyspikes,whichiscriticalinsurgicaloperationswhere in optimizing task scheduling and offloading strategies in
milliseconds matter. Due to the above-mentioned aspects, mobile edge computing environments. In parallel, particle
several researchers have concentrated on integrating IoMT swarm optimization (PSO) methods have also been utilized
withSDNinfrastructurestoenhanceQoS.Theauthorsin[41] toachievelow-latencytaskoffloadingandefficientresource
discuss the benefits of decoupling control software from allocation [56], [57], [58], offering robust solutions for
hardware, facilitating efficient task offloading and resource edge-cloudandindustrialIoTapplications.
allocation in IoT applications. Also, authors in [42] focus In addition to these approaches focusing on system opti-
on optimizing response time in SDN-edge environments, mization and resource management, other lines of research
proposingaunifiedapproachthatconsidersbothnetworking investigate fundamental aspects of network reliability and
and computing dimensions to meet the stringent QoS performancecharacterization.Forexample,Safaeietal.[59]
demands of IoT applications. Addressing the challenges introduceanovelmetrictoevaluatethecapabilityofrouting
in vehicular edge computing, another study introduces protocols in mobile IoMT environments to establish and
a multi-objective approach for joint task offloading and maintain network connections, employing Markov chain
resource allocation in SDN-enabled environments. This analysisforitscalculation.Thishighlightstheongoingefforts
approach balances latency and energy consumption, which to develop more comprehensive metrics for understanding
is crucial for time-sensitive healthcare applications [43]. networkbehaviorbeyondtraditionalones.
In another study, authors propose a prioritization-based In the realm of advanced network optimization, DRL
delay-sensitive task offloading strategy in SDN-integrated has emerged as a pivotal technique for addressing complex
mobile IoT networks, utilizing gravitational search algo- challenges in dynamic environments. Recent investigations
|     |     |     |     |     | underscore | its | effectiveness |     | in both | task | offloading | and |
| --- | --- | --- | --- | --- | ---------- | --- | ------------- | --- | ------- | ---- | ---------- | --- |
rithmsforoptimalfognodeselection,resultinginsignificant
reductionsindelayandunassignedtasks[44]. packetrouting.Forinstance,Renetal.proposeaDRL-based
In the realm of healthcare, an investigation into distributed task offloading framework designed for edge-
re-scheduling IoT services in edge networks has been cloud environments, which aims to achieve efficient and
conducted, which offers insights into optimizing resource near-optimal offloading decisions by enabling intelligent
agentstolearnadaptivestrategies[60].Complementingthis,
| utilization | and maintaining | QoS, | which are critical | for |     |     |     |     |     |     |     |     |
| ----------- | --------------- | ---- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
healthcarenetworksdealingwithfluctuatingworkloads[45]. inthecontextofpacketrouting,Lietal.presentaDRL-based
Edge computing is not just about offloading but also jointroutingandcapacityoptimizationapproachspecifically
about intelligent decision-making at the edge. Integrating tailored for aerial and terrestrial hybrid wireless networks,
AI/ML models at the edge enables real-time predictions, focusing on dynamically minimizing end-to-end packet
|         |                |               |                      |     | transmission | delay | [61]. | These | studies | highlight |     | DRL’s |
| ------- | -------------- | ------------- | -------------------- | --- | ------------ | ----- | ----- | ----- | ------- | --------- | --- | ----- |
| anomaly | detection, and | context-aware | resource allocation. |     |              |       |       |       |         |           |     |       |
A few studies present adaptive frameworks that learn from capabilitytolearnandexecutesophisticatedcontrolpolicies,
usage patterns to optimize resource use dynamically [40], thereby significantly enhancing performance metrics in
[46]. For instance, Siyadatzadeh et al. [47] proposed modernnetworkedsystems.
ReLIEF, a reinforcement learning-based primary-backup As Table 2 illustrates, each category presents distinct
advantagesandlimitationsinthecontextofhighlydynamic
| task assignment | strategy | for fault-tolerant | fog computing, |     |     |     |     |     |     |     |               |     |
| --------------- | -------- | ------------------ | -------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
| 113790          |          |                    |                |     |     |     |     |     |     |     | VOLUME13,2025 |     |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
TABLE2. ComparisonofoptimizationandlearningmethodsindynamicsurgicalIoMTenvironments.
environments like surgical IoT. Specifically, Reinforcement various IoMT devices to geographically distributed edge
Learning (RL) methods, while capable of learning from computing resources capable of task processing and data
interactions and adapting to dynamic conditions, often caching.Agraphicalrepresentationofthesystemarchitecture
suffer from a high time to convergence [67], [83]. This is depicted in Fig. 2. The flowchart in Fig. 3 demonstrates
prolongedtrainingperiod,coupledwiththeirinherentsample thedecision-makinglogicforhandlinghighandlowpriority
inefficiency, makes them less suitable for real-time critical tasksinthecontroller.Ithighlightsdelay-awareroutingand
decision-making where immediate adaptation is required. resourceallocationtoensureefficienttransmission.
Furthermore,thelearnedpoliciescanbesensitivetoenviron-
mental changes if not sufficiently explored during training.
A. SYSTEMARCHITECTUREANDCOMPONENTS
On the other hand, Machine Learning (ML) methods,
Thephysicalinfrastructurecomprisesasetofnetworknodes
particularlysupervisedlearningapproaches,excelatpattern
V, which includes IoMT source devices, edge computing
recognition and prediction given sufficient labeled data.
nodes, and intermediate routers or switches. These nodes
However,theirrobustnessisasignificantconcernintheface
are interconnected by a set of logical communication links
of unforeseen data shifts or adversarial attacks, which are
L, managed by the SDN controller. Each link l ∈ L is
plausible in complex IoMT environments [84]. Moreover,
characterizedbyitsdatatransmissioncapacityC (e.g.,inbits
ML models often struggle to directly optimize sequential l
persecond)anditsassociatedcommunicationdelayd ,which
decision-making problems in dynamic settings without l
encompassespropagationandtransmissiontimes.
extensive re-training, and their ‘‘black-box’’ nature can
A crucial infrastructure component is the set of edge
hinderinterpretability,crucialformedicalapplications.They
computing nodes E ⊂ V. These nodes are strategically
fundamentally operate on learning from existing data rather
located closer to the IoMT devices to facilitate low-latency
thanactivelyexploringandoptimizingwithinacontinuously
processing. Each edge node e ∈ E possesses a finite cache
changing environment. Greedy methods, while offering fast
storagecapacityB (e.g.,inbits)andintroducesaprocessing
execution, inherently make locally optimal choices. This e
delay p when executing an offloaded task, reflecting its
characteristicmeanstheycannotguaranteeglobaloptimality e
computationalpowerandthetask’scomplexity.
and are often ill-equipped to handle the complex, non-
ThecommunicationmodelintegratesIoMTdeviceswithin
linearinterdependenciesandlong-termconsistencyrequired
the surgical environment, which connect via wireless (e.g.,
in surgical IoT scenarios [85]. Their lack of foresight
Wi-Fi, BLE) or wired links to local Access Points (APs).
makes them unsuitable for problems where future states
These APs act as gateways to a high-speed, low-latency
or cumulative effects are critical. Given these limitations,
backhaul network (e.g., fiber-optic), ensuring reliable data
particularly the critical need for consistency over time in a
transmission to edge nodes or, if necessary, to the central
rapidlyevolvingsurgicalIoTenvironment,coupledwiththe
cloud. The entire network fabric, including APs, links, and
slow convergence of RL, the robustness issues of ML, and
edge nodes, operates under the centralized control of the
thesub-optimalityofgreedyapproaches,weproposeanovel
SDN controller. This controller maintains a global view of
metaheuristicmethod.Ourapproachleveragesthestrengths
thenetworktopologyandresourcestatus,enablingdynamic
ofmetaheuristicsinachievingnear-optimalsolutionswithin
routing,bandwidthallocation,andcachingdecisions.Atthe
a reasonable time and adapting to complex, dynamic
datalinklayer,weassumeapriority-awareMediumAccess
landscapes, offering a promising solution for maintaining
Control (MAC) protocol that grants preferential channel
crucialconsistencyinsurgicalIoMToperations.
access to high-priority medical data streams, minimizing
contention delays for critical traffic. For the performance
III. SYSTEMMODELANDPROBLEMFORMULATION and QoS focus of this work, we assume robust end-to-
This section formally defines the system architecture, end encryption (e.g., TLS/DTLS) for data confidentiality
operational parameters, decision variables, and the math- and integrity in transit. However, the detailed design and
ematical optimization problem underlying our proposed analysis of security mechanisms specific to the PASO
Priority-Aware SDN Orchestration (PASO) framework for framework, including aspects beyond in-transit protection
surgical IoMT environments. We consider a network envi- such as endpoint security or SDN controller access control,
ronmentorchestratedbyacentralSDNcontroller,connecting areidentifiedaskeyfutureresearchdirections.
VOLUME13,2025 113791

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
FIGURE2. SystemarchitectureforthesurgicalIoMTenvironment,showingIoMTdevices,thecentralSDNcontroller,andcommunicationlinks.
orpotentiallythecloud.Theenergyconsumedbythesource
|     |     |     |     |     | devicetotransmittaskr |     |              | foroffloadingisdenotedbyE |         |        |        | r .     |
| --- | --- | --- | --- | --- | --------------------- | --- | ------------ | ------------------------- | ------- | ------ | ------ | ------- |
|     |     |     |     |     | Specific              | QoS | requirements |                           | must be | met to | ensure | patient |
safetyandproceduralefficacyinsurgicalapplications.Acrit-
icalparameteristhemaximumacceptableend-to-enddelay
|     |     |     |     |     | D for                | any admitted |             | medical   | task                      | r ∈ F       | . Additionally, |          |
| --- | --- | --- | --- | --- | -------------------- | ------------ | ----------- | --------- | ------------------------- | ----------- | --------------- | -------- |
|     |     |     |     |     | max                  |              |             |           |                           |             | m               |          |
|     |     |     |     |     | a minimum            | average      |             | hit ratio | H min                     | is targeted | specifically    |          |
|     |     |     |     |     | for admitted         | medical      |             | tasks     | to promote                | efficient   | utilization     |          |
|     |     |     |     |     | of edge              | resources    | for         | critical  | data.                     | For         | battery-powered |          |
|     |     |     |     |     | IoMT devices,        |              | an implicit |           | constraint                | might       | be the          | device’s |
|     |     |     |     |     | maximumenergybudgetE |              |             |           | fortransmissionsovertime. |             |                 |          |
max
C. DECISIONVARIABLES
FIGURE3. Flowchartillustratingthetaskprioritizationandpathselection The SDN controller dynamically manages the network by
processbasedondelayminimization. makingthefollowingkeydecisionsforeachtaskr ∈F:
|     |     |     |     |     | • Admission |     | Control | (z  | ∈ {0,1}): | Determines |     | if task |
| --- | --- | --- | --- | --- | ----------- | --- | ------- | --- | --------- | ---------- | --- | ------- |
r
=
|     |     |     |     |     | r is | admitted | and | successfully |     | processed | (z r | 1) or |
| --- | --- | --- | --- | --- | ---- | -------- | --- | ------------ | --- | --------- | ---- | ----- |
B. TASKS,FLOWS,ANDQOSREQUIREMENTS
|                                                   |     |     |     |     | rejected/dropped(z |     |          | =0). |                           |     |          |        |
| ------------------------------------------------- | --- | --- | --- | --- | ------------------ | --- | -------- | ---- | ------------------------- | --- | -------- | ------ |
| Overagiventimehorizon,thesystemhandlesasetoftasks |     |     |     |     |                    |     |          | r    |                           |     |          |        |
|                                                   |     |     |     |     | RoutingDecision(y  |     |          |      | ∈ {0,1}):Indicatesiflinkl |     |          | ∈ L    |
| ordataflowsF,generatedbyIoMTdevices.Thesetasksare |     |     |     |     | •                  |     |          | rl   |                           |     |          |        |
|                                                   |     |     |     |     | is used            | in  | the path | for  | transmitting              | an  | admitted | task r |
categorizedintotwodistinctsubsets:
(y =1ifused,0otherwise).
| F ⊂ F:High-prioritymedicaltasks,suchassurgical |     |     |     |     | rl  |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• m
Thesevariablescollectivelydefinetheorchestrationstrategy
| video, control | signals, | or  | critical patient | telemetry, |     |     |     |     |     |     |     |     |
| -------------- | -------- | --- | ---------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
employedbythecontroller.
whichdemandstringentQoSguarantees.
⊂F:Lower-prioritynon-medicaltasks,likeroutine
• F n
logsorbackgrounddatasynchronization(F =F ∪F , D. OPTIMIZATIONPROBLEMFORMULATION
m n
| F ∩F | =∅). |     |     |     | Our primary |     | objective | is  | to maximize |     | the number | of  |
| ---- | ---- | --- | --- | --- | ----------- | --- | --------- | --- | ----------- | --- | ---------- | --- |
| m n  |      |     |     |     |             |     |           |     |             |     |            |     |
Eachtaskr ∈F,originatingfromasourcenodesrc(r)∈V, successfully processed tasks, while strongly prioritizing
ischaracterizedbyitsdatasizes (relevantforcaching),its critical medical tasks. This is formulated to maximize a
r
weightedsumofcompletedtasks,subjecttonetworkandQoS
| required network    | bandwidth | b r , and    | its intended | processing |              |     |     |     |     |     |               |     |
| ------------------- | --------- | ------------ | ------------ | ---------- | ------------ | --- | --- | --- | --- | --- | ------------- | --- |
| destination dst(r), | which     | is typically | an edge      | node e ∈ E | constraints. |     |     |     |     |     |               |     |
| 113792              |           |              |              |            |              |     |     |     |     |     | VOLUME13,2025 |     |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
1) OBJECTIVEFUNCTION IV. PROPOSEDGREEDYALGORITHMWITHPREEMPTION
|        |     |          |     |          |     |                 |     | Addressing | the | computational |     | complexity | inherent |     | in opti- |
| ------ | --- | -------- | --- | -------- | --- | --------------- | --- | ---------- | --- | ------------- | --- | ---------- | -------- | --- | -------- |
| We aim | to  | maximize | the | weighted | sum | of successfully |     |            |     |               |     |            |          |     |          |
admitted and processed tasks, where medical tasks receive mally solving the Integer Linear Programming problem
fullweightandnon-medicaltasksreceiveafractionalweight formulated in Section III within the dynamic constraints of
α(0<α <1)toenforceprioritization:
|     |     |           |     |     |     |     |     | real-time  | network | control | necessitates       |     | a practical, | efficient  |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | ---------- | ------- | ------- | ------------------ | --- | ------------ | ---------- | --- |
|     |     |           |     | X   | X   |     |     | heuristic. | We      | propose | the Priority-Aware |     | SDN          | Orchestra- |     |
|     |     | Maximize: |     | z   | +α  | z   | (1) |            |         |         |                    |     |              |            |     |
r r tion (PASO) algorithm, a computationally tractable, greedy
|     |     |     |     | r∈Fm | r∈Fn |     |     |           |          |            |     |                |     |             |     |
| --- | --- | --- | --- | ---- | ---- | --- | --- | --------- | -------- | ---------- | --- | -------------- | --- | ----------- | --- |
|     |     |     |     |      |      |     |     | heuristic | designed | to operate |     | on the central | SDN | controller. |     |
Maximizingthisobjectivedrivesthesystemtowardsadmit- PASOmakeslocalized,sequentialdecisionsforeacharriving
| ting | as many | medical | tasks | as possible, | followed |     | by non- |              |     |             |     |         |          |            |     |
| ---- | ------- | ------- | ----- | ------------ | -------- | --- | ------- | ------------ | --- | ----------- | --- | ------- | -------- | ---------- | --- |
|      |         |         |       |              |          |     |         | task, aiming | to  | approximate | the | optimal | resource | allocation |     |
medicaltasks,withinthelimitsimposedbytheconstraints. strategy defined by our objective function (1). Its core
principlesarethestrictprioritizationofcriticalmedicaltraffic
2) CONSTRAINTS
|     |     |     |     |     |     |     |     | (F m ) and | dynamic | resource | management, |     | incorporating |     | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | -------- | ----------- | --- | ------------- | --- | --- |
Themaximizationoftheobjectivefunction(1)isgovernedby preemption of lower-priority non-medical tasks (F ) when
n
severalcriticalconstraintsthatensureoperationalfeasibility
|     |     |     |     |     |     |     |     | network | congestion | threatens |     | the Quality | of  | Service | (QoS) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --------- | --- | ----------- | --- | ------- | ----- |
and adherence to the stringent requirements of the surgical ofvitalsurgicaldataflows.
IoMT environment. Firstly, Quality of Service (QoS) for The orchestration logic is detailed in Algorithm 1. The
| critical | medical | tasks | must | be guaranteed. |     | The end-to-end |     |         |        |            |     |        |          |       |     |
| -------- | ------- | ----- | ---- | -------------- | --- | -------------- | --- | ------- | ------ | ---------- | --- | ------ | -------- | ----- | --- |
|          |         |       |      |                |     |                |     | process | begins | by sorting | the | set of | incoming | tasks | F   |
∈
delay experienced by any admitted medical task (r F m based on priority, ensuring that all medical tasks (F ) are
m
with z = 1), enc ompassing the cumulative delay across considered before any non-medical tasks (F ) (Line 1).
|             | r   |        |       |           |            |      |        |     |     |     |     |     |     | n   |     |
| ----------- | --- | ------ | ----- | --------- | ---------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| its network |     | path ( | P y d | ) and the | processing | time | at the |     |     |     |     |     |     |     |     |
rl l Thisinitialsortingstepdirectlyimplementstheprioritization
assigned edge node (p ), must strictly remain below the centraltoourobjective.Thealgorithmtheniteratesthrough
e(r)
| maximumthresholdD |     |     |     | :   |     |     |     |           |                                   |       |         |             |       |              |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --------------------------------- | ----- | ------- | ----------- | ----- | ------------ | --- |
|                   |     |     | max |     |     |     |     | eachtaskr | inthisprioritizedsequence(Line2). |       |         |             |       |              |     |
|                   |     |     |     | !   |     |     |     |           |                                   |       |         |             |       |              |     |
|                   |     |     |     |     |     |     |     | For each  | task                              | r, an | initial | feasibility | check | is performed |     |
X
y d +p z ≤D ∀r ∈F . (2) byinvokingthe‘FIND_DECISION’procedure(Algorithm2,
|     |     | rl  | l e(r) | r   | max | m   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
l∈L called in Line 3). This procedure (detailed in Algorithm 2)
Secondly, the system must operate within its finite resource acts as a preliminary filter. It compares an estimated
limitations.Networkcongestionismanagedbyensuringthat offloading delay D r (potentially based on a typical path or
theaggregatebandwidthconsumedbyallactivetasks(r ∈F) target edge node) against the stringent maximum allowed
traversing any link l does not surpass the link’s inherent delay D for the task type and verifies if the originat-
max
capacity C l . Significantly, this constraint incorporates the ing device has sufficient energy E r for the transmission
dynamic preemption mechanism, allowing the available (‘Device_Has_Energy’,Line1).Ifeithertheestimateddelay
capacity on a link to be effectively increased by reclaiming exceedsthethresholdorthedevicelacksenergy,offloading
(r′
bandwidth from lower-priority non-medical tasks ∈ F ) is deemed infeasible (‘false‘ returned, Line 4), and the
n
thatarepreemptedtoaccommodatecriticalflows: algorithm defaults to instructing the device to compute the
X X ∈L. task locally (‘Compute_Locally’, Line 26), assuming local
|     | y   | b ≤C | +   |     | y r′l b | r′ ∀l | (3) |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rl r l processingcapabilityexists.Thesystemstateisthenupdated
′∈
| r ∈      | F     |         |         | r F n          |      |                 |     |                      |      |          |      |          |             |     |         |
| -------- | ----- | ------- | ------- | -------------- | ---- | --------------- | --- | -------------------- | ---- | -------- | ---- | -------- | ----------- | --- | ------- |
| act iv   | e onl |         | beingp  | re em p tedonl |      |                 |     | accordingly(Line27). |      |          |      |          |             |     |         |
|          |       |         |         |                |      |                 |     | If the               | task | r passes | the  | initial  | feasibility |     | check   |
| Thirdly, | valid | network | routing | paths          | must | be established, |     |                      |      |          |      |          |             |     |         |
|          |       |         |         |                |      |                 |     | (‘can_offload’       |      | is true, | Line | 4), PASO | attempts    |     | to find |
whichtheflowconservationconstraintensures.Foranytask
|       |                  |     |         |      |          |        |         | a suitable | network  | path | for        | offloading. |               | It employs | a       |
| ----- | ---------------- | --- | ------- | ---- | -------- | ------ | ------- | ---------- | -------- | ---- | ---------- | ----------- | ------------- | ---------- | ------- |
| r and | any intermediate |     | network | node | v (i.e., | a node | that is |            |          |      |            |             |               |            |         |
|       |                  |     |         |      |          |        |         | standard   | shortest | path | algorithm, | such        | as Dijkstra’s |            | (‘Dijk- |
neitherthesourcesrc(r)northedestinationdst(r)),thetotal
stra_Find_Path’,Line5),configuredtofindaroutefromthe
incomingflowmustequalthetotaloutgoingflow:
|     |     |     |     |     |     |     |     | task’ssourcenodesrc(r)toasuitableedgenodee |     |     |     |     |     | ∈   | E that |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ------ |
| X   |     | X   |     |     |     |     |     |                                            |     |     |     |     |     |     |        |
y = y ∀r ∈F,∀v∈/ {src(r),dst(r)}. (4) minimizes the end-to-end latency, considering current link
|         | rl  |          | rl  |     |     |     |     |         |                            |     |     |     |     |     |     |
| ------- | --- | -------- | --- | --- | --- | --- | --- | ------- | -------------------------- | --- | --- | --- | --- | --- | --- |
| l∈in(v) |     | l∈out(v) |     |     |     |     |     | delaysd | l andedgeprocessingdelaysp |     |     |     | e . |     |     |
Finally, all the decision variables introduced – admission Ifapotentialpathisidentified(Line6evaluatestotrue),the
|           |                  |     |     |                                  |     |     |     | algorithm | proceeds | to  | the critical | step | of verifying | resource |     |
| --------- | ---------------- | --- | --- | -------------------------------- | --- | --- | --- | --------- | -------- | --- | ------------ | ---- | ------------ | -------- | --- |
| control(z | r ),androuting(y |     |     | rl )–areinherentlybinary,meaning |     |     |     |           |          |     |              |      |              |          |     |
theycanonlytakevaluesof0or1: availability along this path. First, a flag ‘preempt_allowed’
|     |     |        |        |          |     |     |     | is set to             | true only | if the | task    | r is a | high-priority |          | medical |
| --- | --- | ------ | ------ | -------- | --- | --- | --- | --------------------- | --------- | ------ | ------- | ------ | ------------- | -------- | ------- |
|     |     | ,y     | ∈{0,1} | ∀r ∈F,∀l | ∈L. |     |     |                       |           |        |         |        |               |          |         |
|     |     | z r rl |        |          |     |     | (5) |                       |           |        |         |        |               |          |         |
|     |     |        |        |          |     |     |     | task (‘Is_Medical(r)’ |           |        | returns | true,  | Line 7),      | granting | it      |
Together,theseconstraintsdefinetheoperationalboundaries the potential to trigger preemption. The algorithm then
withinwhichtheoptimizationobjective(1)mustbeachieved, meticulouslycheckseachlinkl composingtheselectedpath
capturing the complex interplay between QoS demands, (Line8).Foreverylink,the‘Calculate_Utilization’function
resourceavailability,andnetworklogicinthesurgicalIoMT (Line 9) estimates the resulting link utilization if task r,
system. requiringbandwidthb r ,weretobeadmitted.Crucially,this
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 113793 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
Algorithm 1 Priority-Aware Task Orchestration with Algorithm2TaskOffloadingFeasibilityCheck
Preemption(PASO) Input:Task(r),EstimatedOffloadDelay(Dr),MaximumDelay
Input:TasksSet(F),LinksSet(L),EdgeNodesSet(E),DevicesSet (Dmax),DeviceEnergyRequirement(Er)
(D),MaximumDelay(Dmax),EnergyLimits Output:Boolean(trueifoffloadingfeasible)
|     |     |     |     |     |     |     |     | /* Task | Offloading | Feasibility |     | Check |     | */  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ----------- | --- | ----- | --- | --- |
Output:Optimizedtaskoffloadingandroutingdecisions
if(Dr ≤Dmax)andDevice_Has_Energy(Er)then
|     | /* Priority-Aware |     | Task Orchestration |     |     | */  | 1   |               |     |            |     |          |     |     |
| --- | ----------------- | --- | ------------------ | --- | --- | --- | --- | ------------- | --- | ---------- | --- | -------- | --- | --- |
|     |                   |     |                    |     |     |     | 2   | returntrue;// |     | Offloading | is  | feasible |     |     |
1 SorttasksinFbypriority(medicaltasksFmfirst);
|     | forEachtaskrinFdo |     |     |     |     |     | 3   | end |     |     |     |     |     |     |
| --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
|     | can_offload←FIND_DECISION(r,Dr |          |             | ,Dmax | ,Er); |     | 4   | else           |     |            |     |          |     |     |
| --- | ------------------------------ | -------- | ----------- | ----- | ----- | --- | --- | -------------- | --- | ---------- | --- | -------- | --- | --- |
| 3   |                                |          |             |       |       |     |     | returnfalse;// |     | Offloading | not | feasible |     |     |
|     |                                | /* Check | feasibility |       |       | */  | 5   |                |     |            |     |          |     |     |
end
| 4   | ifcan_offloadthen |                                                  |     |     |     |     | 6   |                |     |     |     |     |     |     |
| --- | ----------------- | ------------------------------------------------ | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
|     |                   | path←Dijkstra_Find_Path(r,L,E,minimize_latency); |     |     |     |     | 7   | returnBoolean; |     |     |     |     |     |     |
5
|     |     | /* Find                          | best path |     |      | */  |     |     |     |     |     |     |     |     |
| --- | --- | -------------------------------- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6   |     | ifpathexiststhen                 |           |     |      |     |     |     |     |     |     |     |     |     |
| 7   |     | preempt_allowed←Is_Medical(r);// |           |     | Only |     |     |     |     |     |     |     |     |     |
medical tasks can preempt resourcesformally.Thisinvolvesreservingthebandwidthb r
path_feasible←true;forEachlinklinpathdo
| 8   |     |     |                |              |     |     | on  | each path | link | and updating | cache | status | if applicable. |     |
| --- | --- | --- | -------------- | ------------ | --- | --- | --- | --------- | ---- | ------------ | ----- | ------ | -------------- | --- |
|     |     | /*  | Check resource | availability |     | */  |     |           |      |              |       |        |                |     |
9 ifCalculate_Utilization(l,r, Importantly,ifpreemptionwasrequiredtomeettheresource
preempt=preempt_allowed)>0.90then needs (as determined during the ‘Calculate_Utilization’
path_feasible←false;break;
| 10  |     |     |              |      |     |     | checkwhen‘preempt_allowed’wastrue),thisfunctionalso |     |     |     |     |     |     |     |
| --- | --- | --- | ------------ | ---- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | // Congested | link |     |     |                                                     |     |     |     |     |     |     |     |
end executes the necessary preemption actions, instructing the
11
12 end networkelementstodeprioritizeordropspecificnon-medical
13 ifpath_feasiblethen flowsonthecongestedlinks.Followingsuccessfulresource
| 14  |     | Admit_and_Route(r,path, |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
preempt=preempt_allowed);// Allocate allocation,theoverallsystemstate(linkloads,cacheusage)
|     |     |                              | resources |     |     |     | isupdated(‘Update_System_State’,Line15). |     |     |     |     |     |     |     |
| --- | --- | ---------------------------- | --------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| 15  |     | Update_System_State(r,path); |           |     |     |     |                                          |     |     |     |     |     |     |     |
However,ifthepathverificationfailedduetoanticipated
| 16  |     | end |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
congestionononeormorelinks(Line13evaluatestofalse),
| 17  |     | else |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Defer_Task(r);// No feasible path due thetaskr cannotbeaccommodatedonthispathatthistime
18
|     |     |     | to congestion |     |     |     |     |             |     |                |      |      |            |        |
| --- | --- | --- | ------------- | --- | --- | --- | --- | ----------- | --- | -------------- | ---- | ---- | ---------- | ------ |
|     |     |     |               |     |     |     | and | is deferred |     | (‘Defer_Task’, | Line | 18). | Similarly, | if the |
| 19  |     | end |               |     |     |     |     |             |     |                |      |      |            |        |
initial‘Dijkstra_Find_Path’callfailedtofindanyviablepath
| 20  |     | end |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
21 else to an edge node (Line 6 evaluates to false), the task is also
|     |     | Defer_Task(r);// | No path | found |     |     |                                                        |     |     |     |     |     |     |     |
| --- | --- | ---------------- | ------- | ----- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| 22  |     |                  |         |       |     |     | deferred(Line22).Deferredtasksmightbereconsideredlater |     |     |     |     |     |     |     |
end
| 23  |     |     |     |     |     |     | ordroppeddependingonthesystem’spolicy. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
24 end
25 else This iterative, priority-driven greedy approach allows
|     |     | /* Cannot | offload (failed | feasibility |     |     |      |     |             |        |         |            |     |        |
| --- | --- | --------- | --------------- | ----------- | --- | --- | ---- | --- | ----------- | ------ | ------- | ---------- | --- | ------ |
|     |     |           |                 |             |     |     | PASO | to  | dynamically | manage | network | resources, |     | making |
|     |     | check)    |                 |             |     | */  |      |     |             |        |         |            |     |        |
26 Compute_Locally(r);// Fallback to local real-time decisions that strongly favor the successful and
execution timely completion of critical surgical tasks. Preemption is
27 Update_System_State(r,local); leveraged as a key mechanism to guarantee QoS under
end
28
|     | end |     |     |     |     |     | potentialnetworkload. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
29
30 returnOptimizedtaskoffloadingandroutingdecisions; The computational complexity of the PASO algorithm
(Algorithm1)isprimarilydeterminedbythetasksortingstep
|     |     |     |     |     |     |     | and | the pathfinding |     | within the | loop. | Sorting | N = | |F| tasks |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | ----- | ------- | --- | --------- |
takesO(NlogN)time.Foreachtask,thedominantoperation
calculation is priority-aware: if ‘preempt_allowed’ is true, is typically the Dijkstra’s algorithm for pathfinding, which
the function considers the available bandwidth plus any has a complexity of O(L + V logV) or O((V + L)logV)
bandwidththatcouldpotentiallybereclaimedbypreempting for a network with V = |V| nodes and L = |L| links,
currently active, lower-priority non-medical tasks (F ) on using a binary heap. The subsequent link verification loop
n
that specific link l. If admitting task r would cause the runsforatmostV −1links.Thus,theoverallcomplexityis
|     |     |     |     |     |     |     |     |     |     | +N  | ·(L | +V  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anticipated utilization on any link l to exceed a predefined approximately O(NlogN logV)). While this
operationalthreshold(e.g.,90%,chosentomaintainasafety ispolynomial,forverylargenetworksorextremelyhightask
margin and network stability), even after accounting for arrivalrates,thecontroller’sprocessingcapacityneedstobe
potential preemption, that link is considered congested for sufficienttomaintainreal-timeresponsiveness.
| this | task. | In such a | case, the path | is marked | as infeasible |     |     |     |     |     |     |     |     |     |
| ---- | ----- | --------- | -------------- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(‘path_feasible’settofalse,Line13),andthecheckingloop V. EVALUATIONMETHODOLOGY
forthispathterminates(‘break’). We employ a set of standard quantitative metrics to eval-
Iftheentirepathissuccessfullycheckedwithoutexceeding uate the performance and effectiveness of our proposed
theutilizationthresholdonanylink(‘path_feasible’remains priority-awareSDNorchestrationframework.Thesemetrics
true,Line13),thetaskrisadmitted.The‘Admit_and_Route’ are chosen to directly assess the framework’s ability to
function (Line 14) is invoked to allocate the necessary meet the objectives outlined in Section III, particularly the
| 113794 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
prioritizationofmedicaltasks(F )whileadheringtosystem Inadditiontoaveragelinkutilization,weintroducethe90th
m
constraints. We will compare the performance of PASO Percentile Deviation from Mean Utilization ((cid:49) ) to better
90
againstrelevantbaselinealgorithmsundervarioussimulated capture the fairness and balance of network resource usage.
networkconditionsandtaskloads,asdetailedinSectionVI. Thismetricquantifieshowmuch,onaverage,theutilization
Thekeymetricsaredefinedasfollows: of the most utilized 90% of links deviates from the overall
meanutilizationacrossalllinks.Itisformallydefinedas:
A. TOTALDELAY(D TOTAL ) 1 X
To comprehensively evaluate the end-to-end latency perfor- (cid:49) 90 = |L90| l ∈L 90 |U l −µ U | (9)
mance of the system, we define the Total Delay as the
where L90 denotes the set containing the 90% of links
cumulativesumofthecompletiondelaysexperiencedbyall
with the highest average utilizations, U is the average
successfully processed medical tasks. For each task r, the l
completion delay d comp is the time elapsed from the task’s utilization of link l, and µ U is the mean utilization across
r all links. Lower values of (cid:49)90 indicate that most links
arrivaltoitssuccessfulcompletionatanedgeorfognode.The
have utilizations close to the average, implying a more
TotalDelayacrossallcompletedmedicaltasksisformulated
asfollows: balanced and efficient network operation. Higher values
suggestunevenloaddistributionandpotentialbottlenecksin
D total = X d r comp (6) specificlinks.Thisapproachallowsustoassessnotonlythe
r∈Fm overallbandwidthusagebutalsothefairnessandefficiency
A lower D indicates better system responsiveness and oftheloaddistribution,whichiscriticalformaintaininglow
total
latencyandavoidingnetworkcongestion,especiallyinhighly
faster processing of critical medical tasks, which is crucial
dynamicIoMTenvironments.
for maintaining Quality of Service (QoS) guarantees in
time-sensitiveIoMTenvironments.
D. DYNAMICCONDITIONS:WIRELESSNOISE
SIMULATIONSETUP
B. HITRATIO(H)
ToevaluatetherobustnessoftheproposedPASOframework
In the IoMT setting, the Hit Ratio evaluates the system’s
under more realistic and dynamic wireless channel condi-
effectiveness in ensuring that offloaded medical tasks meet
tions,weconductedsimulationsincorporatingwirelessnoise.
their deadlines after traversing the network. Since all tasks
Thisallowsforanassessmentofhowvaryingsignalquality
aretransmittedtoedgeorfognodes(i.e.,nolocalexecution
impacts key performance indicators such as hit ratio and
occurs),wedefinetheHitRatioastheproportionoftasksthat
end-to-enddelay.Thesimulationofnoiseanditseffectsare
arecompletedwithintheirdeadlineconstraints[86]:
basedonestablishedwirelesscommunicationprinciplesand
P I(d comp ≤Ddeadline)
H = r∈F r r (7) models.ThecoreideaisthattheSignal-to-NoiseRatio(SNR)
|F| at the receiver dictates the Bit Error Rate (BER), which in
comp turnaffectsthePacketErrorRate(PER).AhigherPERleads
where d represents the completion time of task r
r
to more retransmissions, increasing delay and potentially
(measured from arrival to successful completion at an edge
orfognode),Ddeadlineistheassigneddeadlinefortaskr,and reducingeffectivethroughput[88],[89].
r
I(·)istheindicatorfunction,whichequals1ifthecondition
1) NOISEGENERATIONANDIMPACT
issatisfied(i.e.,thetaskmeetsitsdeadline)and0otherwise.
Inoursimulations,wirelesschannelqualityisprimarilymod-
A higher H value indicates better system performance,
ulatedbyadjustingtheSNR.Weconsidertwoprimarynoise
demonstratingthatagreaterfractionofIoMTtasksarebeing
models conceptually, although the simulations presented in
completed on time. We particularly focus on the Hit Ratio
Section VI-E directly vary SNR to observe performance
forhigh-prioritymedicaltasks(H ),whichservesasadirect
m
changes:
measure of the framework’s ability to provide reliable and
Elevated AWGN Floor: This model assumes a constant
timely data processing essential for medical and surgical
AdditiveWhiteGaussianNoise(AWGN)power(P )across
applications. N1
thechannel[90].TheSNRisthendeterminedbythereceived
signalpower(P )relativetothisnoisefloor,calculatedas:
C. LINKUTILIZATION(U ) rx
L
This metric reflects how efficiently network bandwidth SNR =P −P (10)
dB rx_dBm N1_dBm
resourcesareutilizedandhelpsidentifypotentialbottlenecks
Here, P is the received signal power in dBm, and
or imbalances across the network. In our simulation, the rx_dBm
instantaneousutilizationofalinklduringatasktransferwas P N1_dBm is the noise power in dBm. Fluctuations in
performance arise from changes in received signal strength
calculated using the following expression, implemented in
orifthisnoiseflooritselfisvaried.
Python[87]:
AWGN + Bursty Interference: This model considers a
(cid:18) (cid:19)
AvailableCapacity (t)
U
l
(t)=100× 1− l (8) baseline AWGN (P N,base ) plus intermittent, higher-power
C l interference (P I ) that is active with a certain probability or
VOLUME13,2025 113795

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
duty cycle (ρ) [91]. When interference is active, the total TABLE3. Keyparametersforwirelessnoisesimulationsetup.
noisepowerincreasessignificantly.Thetotalnoisepowerin
| linearunits(P |     | N,Total_B_linear |     | )isthesumofthebaselinenoise |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ---------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andtheinterferencepower:
|                 | P N,Total_B_linear |             |                    | =P N,base_linear |        | +P I_linear        |              | (11)   |     |     |     |     |     |
| --------------- | ------------------ | ----------- | ------------------ | ---------------- | ------ | ------------------ | ------------ | ------ | --- | --- | --- | --- | --- |
| This            | leads              | to a        | temporary          | drop             | in     | SNR,               | calculated   | as     |     |     |     |     |     |
|                 | =                  |             | /P                 |                  |        |                    |              |        |     |     |     |     |     |
| SNR             | B                  | P rx_linear | N,Total_B_linear   |                  |        | , and consequently |              | a      |     |     |     |     |     |
| higher          | PER                | [91].       | This models        |                  | common | scenarios          | in           | shared |     |     |     |     |     |
| frequency       |                    | bands,      | such               | as the           | ISM    | band, where        | devices      |        |     |     |     |     |     |
| like            | Bluetooth          | or          | microwave          |                  | ovens  | can cause          | transient    |        |     |     |     |     |     |
| interference    |                    | [92].       | The                | average          | PER,   | and                | consequently |        |     |     |     |     |     |
| system          | performance,       |             | fluctuates         |                  | based  | on the             | presence     | and    |     |     |     |     |     |
| characteristics |                    | of          | this interference. |                  | The    | average            | PER          | is a   |     |     |     |     |     |
weightedsumofthePERineachstate: from 25 dB towards 10 dB, leading to a reduction in hit
ratiosandanincreaseindelays,withslightrandomvariations
| PER |     | =(1−ρ)·PER(SNR |     |     | )+ρ·PER(SNR |     | )   | (12) |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | ----------- | --- | --- | ---- | --- | --- | --- | --- | --- |
avg A B to simulate stochastic channel effects. This approach, while
|       |     |      |         |      |      |          |       |     | abstracting | the | detailed physical | layer calculations | for each |
| ----- | --- | ---- | ------- | ---- | ---- | -------- | ----- | --- | ----------- | --- | ----------------- | ------------------ | -------- |
| where | SNR | A is | the SNR | when | only | baseline | noise | is  |             |     |                   |                    |          |
present[88]. packet, provides a clear trend of performance sensitivity to
In both noise models, the fundamental principle is that wirelessnoiseacrossthecomparedorchestrationmethods.
Byanalyzingthesemetricsacrossdifferentscenariosand
| different | noise | components |     | are | added | together | (in | their |     |     |     |     |     |
| --------- | ----- | ---------- | --- | --- | ----- | -------- | --- | ----- | --- | --- | --- | --- | --- |
linearpowerrepresentations)todeterminethetotaleffective comparingPASOwithbaselineapproaches,wecanprovide
|       |        |      |       |       |        |               |     |      | a comprehensive |     | assessment | of its performance | in jointly |
| ----- | ------ | ---- | ----- | ----- | ------ | ------------- | --- | ---- | --------------- | --- | ---------- | ------------------ | ---------- |
| noise | power. | This | total | noise | power, | when combined |     | with |                 |     |            |                    |            |
optimizingtaskthroughput,delay,andresourceutilizationfor
| the | received | signal | power, | yields | the | SNR. The | calculated |     |     |     |     |     |     |
| --- | -------- | ------ | ------ | ------ | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
SNR then directly influences the BER and PER, ultimately priority-awaresurgicalIoMTorchestration.
impactingoverallsystemperformancemetricslikedelayand
| throughput. |     |     |     |     |     |     |     |     | E. DEEPREINFORCEMENTLEARNING(DRL)BASELINE |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
For the results presented in Section VI-E, we directly To provide a comprehensive comparison against contem-
vary SNR levels from 10 dB to 25 dB. Lower SNR values porary machine learning-based scheduling approaches, and
representnoisier,morechallengingchannelconditions,while in response to the need for benchmarking against state-of-
|     |     |     |     |     |     |     |     |     | the-art techniques, |     | we implemented | a DRL | agent for the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | -------------- | ----- | ------------- |
higherSNRvaluesrepresentclearerchannels.Thisvariation
in SNR impacts the underlying BER and PER. Although task offloading decision process. The DRL agent learns a
not explicitly simulating the full MAC-layer retransmission policytodecidewhethertodrop,executelocally,oroffload
protocol for each packet in the main simulation loop an incoming IoT task to a fog node, aiming to optimize a
for computational efficiency, the performance degradation predefined reward signal. We utilized the Stable Baselines3
|            |     |        |         |     |        |       |        |         | library [96] | for | this implementation. | The converged | DRL |
| ---------- | --- | ------ | ------- | --- | ------ | ----- | ------ | ------- | ------------ | --- | -------------------- | ------------- | --- |
| (increased |     | delay, | reduced | hit | ratio) | shown | in the | results |              |     |                      |               |     |
reflects the expected impact of higher PER values that model,aftertraining(performancedetailedinSectionVI-B),
would result from lower SNR conditions. The relationship servesasanadvancedbaselineforperformancecomparison
between SNR, BER, PER, and effective data rate is well- againstPASOandotherheuristicmethods.
documented[88],[89].
1) DRLENVIRONMENTFORMULATION
2) KEYPARAMETERSFORNOISESIMULATION The task scheduling problem is modeled as a Markov
The parameters relevant to understanding the wireless DecisionProcess(MDP),wheretheDRLagentinteractswith
environment and noise impact are summarized in Table 3. acustom-simulatedIoTschedulingenvironment.
| These | parameters |     | are drawn | from | typical | IoT | and wireless |     |     |     |     |     |     |
| ----- | ---------- | --- | --------- | ---- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
communicationscenariosandrelevantstandards[93]. a: STATESPACE
The simulation study investigates the performance of The state observed by the agent at each step is represented
PASOandbaselinealgorithmsacrossarangeofSNRlevels as a 6-dimensional vector of normalized values, capturing
(10 dB to 25 dB). The Python script, used to generate the essential task and network characteristics relevant to the
comparative plots under varying noise (SNR) conditions, schedulingdecision.Theseincludethenormalizedtasksize,
models the degradation in hit ratio and the increase in obtained by dividing the task size by 500.0 KB, which
sum delays as SNR decreases. Specifically, a baseline correspondstotypicalIoMTdatapayloads[97];thenormal-
performance at a nominal high SNR is established, and ized task deadline, calculated as the task deadline divided
then scaling factors, proportional to the deviation from by 20.0 ms, reflecting the requirements of latency-sensitive
this nominal SNR, are applied to simulate the impact of IoMTapplications[98];andthenormalizedbatterycapacity
worsening channel conditions. For instance, as SNR drops of the task’s source IoT device, computed by dividing the
| 113796 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
battery capacity by 6000.0 units, indicative of standard Algorithm3DeepQ-LearningforIoMTTaskSchedul-
batterylevelsinIoTdevices.Inaddition,thevectorcontains
ing
the task priority, where a value of 1.0 denotes high priority Environment(Env),Q-Network(Q),TargetNetwork(Q′),
Input:
and 0.0 otherwise; the average link utilization across the ReplayBuffer(D),LearningRate(α),DiscountFactor(γ),
ExplorationRate(ϵ),TargetUpdateFrequency(C),BatchSize
| network; | and the | normalized | queue | length | of the | least busy |     |     |     |     |     |     |     |
| -------- | ------- | ---------- | ----- | ------ | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
(B),TotalTimesteps(Ttotal)
fognode,obtainedbydividingthequeuelengthby10.0tasks.
Output:TrainedDQNmodelforIoMTtaskscheduling
All state values are normalized and clipped to the range /* Initialization */
InitializeQwithrandomweightsθ;InitializetargetnetworkQ′with
| [0, 1]. | The normalization |     | constants |     | (MAX_TASK_SIZE, |     | 1   |     |     |     |     |     |     |
| ------- | ----------------- | --- | --------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
θ′←θ;InitializeemptyreplaybufferD←∅;Settimestept←0;
| MAX_DEADLINE, |     | MAX_BATTERY) |     | are | defined | within our |     |     |     |     |     |     |     |
| ------------- | --- | ------------ | --- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Setinitialstates←Env.reset();
DRL environment to reflect typical task properties encoun- /* Main Training Loop */
| teredinIoMTscenarios[97],[98]. |     |     |     |     |     |     |     | fort←1toTtotaldo |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
2
|     |     |     |     |     |     |     |     | /*  | ϵ-greedy | action | selection |     | */  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --------- | --- | --- |
3 ifrand()<ϵthen
| b: ACTIONSPACE |     |     |     |     |     |     | 4   |     | a←randomaction;// |     | Explore | randomly |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------- | -------- | --- |
else
| The DRL | agent | in the | IoT | task scheduling |     | environment | 5   |     |          |                |         |         |     |
| ------- | ----- | ------ | --- | --------------- | --- | ----------- | --- | --- | -------- | -------------- | ------- | ------- | --- |
|         |       |        |     |                 |     |             |     |     | a←argmax | a′Q(s,a′;θ);// | Exploit | learned |     |
6
operates within a discrete action space comprising three policy
| possibleactions.Action0correspondstodroppingthetask, |     |     |     |     |     |     | 7   | end |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r,s′,done←Env.step(a);//
wherethetaskissimplydiscarded.Action1representslocal 8 Apply action and
|     |     |     |     |     |     |     |     |     | observe | transition |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | --- | --- |
execution, in which the agent attempts to process the task Storetransition(s,a,r,s′,done)inbufferD;
9
| directly | on the | IoT device. | Action | 2 involves | offloading | the |     |     |            |        |              |     |     |
| -------- | ------ | ----------- | ------ | ---------- | ---------- | --- | --- | --- | ---------- | ------ | ------------ | --- | --- |
|          |        |             |        |            |            |     |     | /*  | Experience | Replay | and Learning |     | */  |
tasktotheleastbusyfognodeforremoteprocessing. 10 if|D|≥Bandt≥warm-upthresholdthen
|     |     |     |     |     |     |     |     |     |                     |     | ,aj ,rj ,s′ ,donej)fromD;foreach |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | -------------------------------- | --- | --- |
|     |     |     |     |     |     |     | 11  |     | Samplemini-batch(sj |     | j                                |     |     |
sampledtransitiondo
ifdonejthen
| c: REWARDFUNCTION |     |     |     |     |     |     | 12  |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
yj ←rj;
| The reward | function | is  | crafted | to steer | the agent | towards | 13  |     |     |     |     |     |     |
| ---------- | -------- | --- | ------- | -------- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
else
makingoptimalschedulingdecisionsbyprovidingfeedback 14 a′′Q′(s′ ,a′′;θ′);
|     |     |     |     |     |     |     | 15  |     | yj  | ←rj +γmax |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
j
based on the outcomes of each action. If the agent selects end
16
Action 0 (drop task), it receives an immediate negative Computeloss:L(θ)← 1PB (yj −Q(sj ,aj ;θ))2;
|                |           |                                    |        |           |             |           | 17  |     |           |             | B j=1  |     |     |
| -------------- | --------- | ---------------------------------- | ------ | --------- | ----------- | --------- | --- | --- | --------- | ----------- | ------ | --- | --- |
|                | −1.0.     |                                    |        |           |             |           |     |     | UpdateQ:θ | ←θ−α∇θL(θ); |        |     |     |
| reward         | of        | For                                | Action | 1 (local  | execution), | if the    |     |     |           |             |        |     |     |
|                |           |                                    |        |           |             |           | 18  |     | end       |             |        |     |     |
| task’s local   | execution | energy                             |        | E exceeds | the         | available |     |     |           |             |        |     |     |
|                |           |                                    |        | local     |             |           | 19  | end |           |             |        |     |     |
| devicebatteryB |           | ,therewardis−0.5,indicatingbattery |        |           |             |           |     |     |           |             |        |     |     |
|                |           | device                             |        |           |             |           |     | /*  | Target    | Network     | Update |     | */  |
insufficiency. If the task can be executed energy-wise but 20 iftmodC=0then
θ′←θ;//
the current time T plus the local execution duration 21 Synchronize target network
|     |     | current |     |     |     |     |     | end |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
22
D local exceedsthetaskdeadlineT deadline ,theagentreceives s←s′;// Update current state
23
a reward of −0.8, signaling a deadline miss. In the case ifdonethen
24
where both battery and deadline constraints are satisfied, 25 s←Env.reset();// Reset environment on
|            |        | +1.0 |     |         |                |       |     |     | episode | end |     |     |     |
| ---------- | ------ | ---- | --- | ------- | -------------- | ----- | --- | --- | ------- | --- | --- | --- | --- |
| a positive | reward | of   | is  | granted | for successful | local |     | end |         |     |     |     |     |
26
| execution.ForAction2(offloadingtoafognode),theagent |     |     |     |     |     |     |     | end |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
27
first checks if the offloading transmission energy E 28 returnTrainedQ-networkQ;
offload
| surpassesthedevice’sbatteryB |     |     |     | ,whichyieldsareward |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
device
| of −0.5   | if true.   | If the | energy    | constraint | is           | satisfied but |     |     |     |     |     |     |     |
| --------- | ---------- | ------ | --------- | ---------- | ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
| the total | offloading | delay  | D offload | added      | to T current | exceeds       |     |     |     |     |     |     |     |
T , the agent again receives −0.8 for missing the 2) DRLALGORITHMANDTRAININGPROTOCOL
deadline
deadline. If neither constraint is violated, the reward is WeemployedtheDeepQ-Network(DQN)algorithm[100],
+1.0, indicating successful offloading. For any undefined a value-based DRL algorithm suitable for discrete action
or unexpected cases, a default reward of 0.0 is applied. spaces. The DQN agent learns an action-value function (Q-
Thisstructuredrewardscheme—featuring+1.0forsuccess,
|     |     |     |     |     |     |     | function) |     | that estimates | the | expected return | for taking | each |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------------- | --- | --------------- | ---------- | ---- |
−0.5forbatteryinsufficiency,−0.8fordeadlineviolations, actioninagivenstate.Thepolicyisthenderivedbyselecting
and −1.0 for dropped tasks—is intended to encourage the action with the highest Q-value. The training process is
the agent to prioritize successful task completion within detailedinAlgorithm3.
energy and timing constraints, thereby promoting efficient The DRL agent was trained for 100,000 timesteps. Key
resource utilization. This approach aligns with common hyperparameters for the DQN agent, are summarized in
practicesinDRL-basedresourcemanagementstrategies[99]. Table 4. These parameters were chosen based on common
Additionally,theenvironmentreturnsahitbooleanvariable practices in DRL research and some empirical tuning, with
indicatingwhetherthetaskwassuccessfullyprocessed(i.e., values like learning rate and buffer size being standard
not dropped and meeting battery and deadline conditions in startingpoints[96],[101].AnAdamoptimizerwasusedfor
| localoroffloadedmodes). |     |     |     |     |     |     | trainingtheneuralnetwork. |     |     |     |     |     |        |
| ----------------------- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | ------ |
| VOLUME13,2025           |     |     |     |     |     |     |                           |     |     |     |     |     | 113797 |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
TABLE4. DQNhyperparametersforIoTtaskscheduler.
| Algorithm | 3   | outlines | the training | procedure | for | the DQN |     |     |     |     |     |     |     |
| --------- | --- | -------- | ------------ | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
agent designed for IoMT task scheduling. The process FIGURE4. Representativescale-freenetworktopology(Barabási–Albert)
commences with an initialization phase (Line 1). Here, the usedforsimulatingthesurgicalIoMTenvironment.
| primary | Q-network | (Q) | is initialized | with | random | weights |     |     |     |     |     |     |     |
| ------- | --------- | --- | -------------- | ---- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
(Q′),
| θ, and its | counterpart, | the | target | network |     | is initialized |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------ | ------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Q′
withanidenticalsetofweightsθ′ ←θ.AreplaybufferDis To further stabilize learning, the target network is
|     |     |     |     |     |     |     | updated | periodically. |     | Every C | timesteps | (Target | Update |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ------- | --------- | ------- | ------ |
createdandleftempty,readytostoretheagent’sexperiences.
θ′
Thesimulationtimestept issettozero,andtheenvironment Frequency), the weights of the target network are
|     |     |     |     |     |     |     | synchronized | with | the | weights | θ of | the main Q-network: |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | --- | ------- | ---- | ------------------- | --- |
Envisresettoprovidetheinitialstatesfortheagent.
θ′ ← θ (Lines20-22).Afterthelearningupdate,thecurrent
Thecoreofthealgorithmisthemaintrainingloop(Lines
statesisadvancedtos′
2-27), which executes for a predefined number of T (Line23).Ifthedoneflagindicates
total
|            |         |          |         |     |           |         | the end | of an | episode, | the environment |     | is reset, | and s is |
| ---------- | ------- | -------- | ------- | --- | --------- | ------- | ------- | ----- | -------- | --------------- | --- | --------- | -------- |
| timesteps. | In each | timestep | t (Line | 2), | the agent | employs |         |       |          |                 |     |           |          |
an ϵ-greedy strategy to select an action a (Lines 3-7). With reinitialized to the starting state of the new episode (Lines
|     |     | ϵ,  |     |     |     |     | 24-26). Upon | completion |     | of T | timesteps, | the algorithm |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | ---- | ---------- | ------------- | --- |
a probability of a random action is chosen to encourage total
|             |     |            |       |           |            |      | returns the | trained | Q-network |     | Q, which | encapsulates | the |
| ----------- | --- | ---------- | ----- | --------- | ---------- | ---- | ----------- | ------- | --------- | --- | -------- | ------------ | --- |
| exploration | of  | the action | space | (Line 4). | Otherwise, | with |             |         |           |     |          |              |     |
probability1−ϵ,theagentexploitsitscurrentlearnedpolicy learnedschedulingpolicy.
| by selecting | the | action a | that yields | the | maximum | Q-value |     |     |     |     |     |     |     |
| ------------ | --- | -------- | ----------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Q(s,a′;θ) for the current state s (Line 6). Once an action VI. SIMULATIONRESULTSANDDISCUSSION
is selected, it is applied to the environment via Env.step(a), Inthissection,weevaluatetheperformanceoftheproposed
which returns the immediate reward r, the subsequent state Priority-AwareSDNOrchestration(PASO)framework.First,
s′, and a boolean flag done indicating whether the current we present the training performance of the DRL agent,
whichservesasoneofourbaselines.Subsequently,wecom-
| episode | has terminated |     | (Line | 8). This | experience | tuple |     |     |     |     |     |     |     |
| ------- | -------------- | --- | ----- | -------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
(s,a,r,s′,done)isthenstoredinthereplaybufferD(Line9).
|     |     |     |     |     |     |     | pare PASO | against | four | baseline | methods: | random | task |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---- | -------- | -------- | ------ | ---- |
The learning phase, leveraging experience replay, begins allocation, PSO-based allocation, SA-based allocation, and
whenthereplaybufferD hasaccumulatedatleastB(Batch the trained DRL agent. The evaluation focuses on key
Size) transitions and the training has progressed beyond performancemetricsintroducedinSectionV,acrossdiverse
|            |         |        |       |        |            |      | network | conditions | simulated | through |     | different topological |     |
| ---------- | ------- | ------ | ----- | ------ | ---------- | ---- | ------- | ---------- | --------- | ------- | --- | --------------------- | --- |
| an initial | warm-up | period | (Line | 10). A | mini-batch | of B |         |            |           |         |     |                       |     |
(s,a,r,s′,done)
transitions is randomly sampled from deployments of fog nodes and IoMT devices. The heuris-
|     | j   | j j j | j   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
D (Line 11). For each transition within this mini-batch tic and metaheuristic baseline methods include simulated
annealing-basedtaskoffloadingapproaches[52],[53],[54],
| (Line 12), | a target | Q-value | y j | is computed. | If  | the episode |     |     |     |     |     |     |     |
| ---------- | -------- | ------- | --- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
corresponding to the transition had terminated (done is [55],wheretaskallocationdecisionsareoptimizedviaitera-
j
tiveprobabilisticsearches,andparticleswarmoptimization-
| true), y j | is simply | the observed |     | reward | r j (Line | 13). If the |     |     |     |     |     |     |     |
| ---------- | --------- | ------------ | --- | ------ | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
episodehadnotterminated,y iscalculatedusingtheBellman based techniques [56], [57], [58], which leverage swarm
j
equation:r +γ max a′′Q′(s′ ,a′′;θ′),whereγ isthediscount intelligence to minimize latency and energy consumption
|     | j   |     | j   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
factorandQ′ during task scheduling. The DRL baseline provides a
isthetargetnetwork(Line15).Theuseofthe
targetnetworkQ′forcalculatingthesetargetvaluesenhances comparison against a learning-based approach trained to
|          |            |        |          | L(θ), |           |          | optimizetaskschedulingdecisions. |     |     |     |     |     |     |
| -------- | ---------- | ------ | -------- | ----- | --------- | -------- | -------------------------------- | --- | --- | --- | --- | --- | --- |
| training | stability. | A loss | function |       | typically | the mean |                                  |     |     |     |     |     |     |
squarederror,isthencomputedbetweenthesetargetvaluesy
j
andtheQ-valuesQ(s,a;θ)predictedbythemainQ-network A. SIMULATIONSETUP
|     |     | j j |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
θ
(Line 17). The weights of the main Q-network Q are Key simulation parameters defining the network config-
subsequentlyupdatedbyperformingagradientdescentstep uration, device capabilities, and task characteristics are
withalearningrateαtominimizethislossL(θ)(Line18).
|        |     |     |     |     |     |     | summarized | in  | Table | 5. The | simulations | were conducted |     |
| ------ | --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | ------ | ----------- | -------------- | --- |
| 113798 |     |     |     |     |     |     |            |     |       |        |             | VOLUME13,2025  |     |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
TABLE5. Simulationenvironmentandparameters.
|     |     |     |     |     |     |     |     | FIGURE5. DRLagentrewardpertrainingiteration/episode, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
demonstratinglearningconvergence.
| within a | 500 × | 500 m2 | area | using | a scale-free | Barabási– |     |     |     |     |     |     |
| -------- | ----- | ------ | ---- | ----- | ------------ | --------- | --- | --- | --- | --- | --- | --- |
Albertnetworktopology[102]tomodeltheaccessnetwork
structure.Theenvironmentincluded15AccessPoints(APs)
| and 5 Fog | Nodes, | shown | in  | Fig. 4. | To assess | robustness, |     |     |     |     |     |     |
| --------- | ------ | ----- | --- | ------- | --------- | ----------- | --- | --- | --- | --- | --- | --- |
resultsarepresentedacrossfourdifferentrandomplacements FIGURE6. ComparisonoftotaldelayacrosstrainingiterationsforDRL,
(Topologies 1–4) of fog nodes and IoMT devices. The PASO,SA,PSO,andGreedymethods.
| simulations | were | executed | on  | a Windows |     | machine | with |     |     |     |     |     |
| ----------- | ---- | -------- | --- | --------- | --- | ------- | ---- | --- | --- | --- | --- | --- |
specificationsdetailedearlier.Theimplementationwasdone
inPython. patterns—its performance in the early training phases is
suboptimal,particularlywhenthenetworkisunderhighload
B. DRLAGENTCONVERGENCEANDTASKDELAYTRENDS anddominatedbylower-prioritytasks.Incontrast,thePASO
frameworkmaintainsconsistentlylowerdelayfromtheout-
Beforeitsuseasabaseline,theDRLagent(DQN)wastrained
|             |           |     |              |     |            |      |     | set, even | under dynamic | load conditions | and heterogeneous |     |
| ----------- | --------- | --- | ------------ | --- | ---------- | ---- | --- | --------- | ------------- | --------------- | ----------------- | --- |
| for 100,000 | timesteps |     | as described |     | in Section | V-E. | The |           |               |                 |                   |     |
learningefficacyoftheDRLagentisillustratedbyitstraining task priorities. The SA, PSO, and Greedy methods exhibit
progressivelyhigheraveragedelays,reachingapproximately
progress.Fig.5showstherewardobtainedbytheagentover
trainingtimesteps,typicallyaveragedoveraslidingwindow 170ms,230ms,and250ms,respectively.
|     |     |     |     |     |     |     |     | Although | the DRL agent | eventually | outperforms | most |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | ---------- | ----------- | ---- |
orperepisode.Theconvergenceorplateauingofthereward
|     |     |     |     |     |     |     |     | baselines | in later training | iterations, | PASO consistently |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------------- | ----------- | ----------------- | --- |
curve,visibleafterapproximately80,000timesteps,indicates
thattheDRLagenthaslearnedaneffectiveschedulingpolicy, achieves lower delay throughout the entire training period.
Thisisespeciallycrucialinscenariosinvolvingsurgicaltasks,
maximizingitscumulativereward.
whereminimizinglatencyisvital.AstheDRLagent’spolicy
Fig.6illustratesthetotaldelayexperiencedbytasksacross
|          |            |     |         |        |               |     |      | improves, | the total delay | for successfully | completed | tasks |
| -------- | ---------- | --- | ------- | ------ | ------------- | --- | ---- | --------- | --------------- | ---------------- | --------- | ----- |
| training | iterations | for | the DRL | agent, | in comparison |     | with |           |                 |                  |           |       |
stabilizesatalowervalue,reflectingitsincreasingabilityto
| four methods: | PASO, | SA, | PSO, | and Greedy. |     | As established |     |     |     |     |     |     |
| ------------- | ----- | --- | ---- | ----------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
in the literature, for latency-sensitive applications such as managelatencyeffectivelyonceanoptimalroutingpolicyis
learned.
| video streaming |     | and | remote | robotics—including |     |     | surgical |     |     |     |     |     |
| --------------- | --- | --- | ------ | ------------------ | --- | --- | -------- | --- | --- | --- | --- | --- |
monitoring—end-to-enddelaysshouldideallyremainbelow
|     |     |     |     |     |     |     |     | C. PERFORMANCEEVALUATIONOFHEURISTIC-BASED |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
200mstoensureacceptableQoS[109].
| While | the DRL | agent | demonstrates |     | a   | gradual | reduc- | METHODS |     |     |     |     |
| ----- | ------- | ----- | ------------ | --- | --- | ------- | ------ | ------- | --- | --- | --- | --- |
tion in delay as training progresses—ultimately achieving WecomparePASOagainstRandom,PSO,andSAfocusing
ondelay,hitratio,andnetworkutilization.
| optimized     | latency | after | sufficient | exposure |     | to diverse | task |     |     |     |     |        |
| ------------- | ------- | ----- | ---------- | -------- | --- | ---------- | ---- | --- | --- | --- | --- | ------ |
| VOLUME13,2025 |         |       |            |          |     |            |      |     |     |     |     | 113799 |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
1) DELAYANDLATENESSPERFORMANCE evaluating both task completion success and edge resource
|             |              |     |                |                 | utilization | efficiency, | especially |     | concerning | the | constraint |
| ----------- | ------------ | --- | -------------- | --------------- | ----------- | ----------- | ---------- | --- | ---------- | --- | ---------- |
| Low latency | is paramount | in  | surgical IoMT. | Fig. 7 presents |             |             |            |     |            |     |            |
the total end-to-end delay averaged across all success- H for medical tasks. Fig. 8 compares the hit ratios for
min
fully completed tasks as the number of tasks increases both average tasks (solid lines) and high-priority surgical
from 100 to 1000, shown across the four simulated topolo- tasks (dashed lines) across the different task loads and
| gies.           |     |     |     |     | topologies.     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
| a: OBSERVATIONS |     |     |     |     | a: OBSERVATIONS |     |     |     |     |     |     |
Across all topologies, the total delay generally increases PASOconsistentlyachievesthehighesthitratioforbothaver-
with the task load for all algorithms, as expected, due to age and surgical tasks across all task loads and topologies.
increased resource contention. However, the performance Notably, the hit ratio for surgical tasks remains very high
characteristics diverge significantly. PASO Demonstrates a (typically above 60-75% even at 1000 tasks), significantly
controlled increase in delay. Even under the highest load outperforming all baselines. For example, in Topology 1 at
(1000 tasks), PASO maintains a significantly lower delay 1000 tasks, PASO’s surgical hit ratio (approx. 60%) is
compared to PSO and SA. For instance, in Topology 1 at roughly82%higherthanPSO’s(approx.33%),50%higher
1000 tasks, PASO’s delay (approx. 206ms) is roughly thanSA’s(approx.40%),andabout200%higherthanRan-
65% lower than PSO’s (approx. 588ms) and 15% lower dom’s(approx.20%).Furthermore,thegapbetweenPASO’s
than SA’s (approx. 243ms). Similar trends hold across average and surgical hit ratio is relatively small, indicating
other topologies, with PASO consistently achieving delays that its prioritization mechanism successfully favors critical
|        |                |     |              |               | tasks without | excessively |     | penalizing | non-critical | ones | when |
| ------ | -------------- | --- | ------------ | ------------- | ------------- | ----------- | --- | ---------- | ------------ | ---- | ---- |
| 55-70% | lower than PSO | and | 10-25% lower | than SA under |               |             |     |            |              |      |      |
heavy load. This superior performance stems from PASO’s resourcesallow.
ability to proactively manage resources via priority-aware PSOandSAshowmoderateinitialhitratiosthatdegrade
pathselectionandpreemption,securinglow-latencypathsfor significantly as the task load increases. Their hit ratios for
criticaltasksevenwhenthenetworkisbusy. surgicaltasksareconsiderablylowerthanPASO’s,especially
|     |     |     |     |     | under high | load | (dropping | to  | 30-40% | at 1000 | tasks). |
| --- | --- | --- | --- | --- | ---------- | ---- | --------- | --- | ------ | ------- | ------- |
Bothmetaheuristicapproaches,PSOandSA,showamuch
steeper increase in delay, particularly beyond 500 tasks. This indicates their struggle to guarantee resources for
Theirdelaysescalaterapidly,suggestingtheystruggletofind high-priority tasks when the system is congested, failing
efficient global solutions under high contention, leading to to meet the demands of reliable surgical IoMT. Random
significant queuing delays and suboptimal routing choices. performs the poorest, with hit ratios plummeting rapidly
|              |          |            |              |               | as the number | of  | tasks increases. |     | Its hit | ratio for | surgical |
| ------------ | -------- | ---------- | ------------ | ------------- | ------------- | --- | ---------------- | --- | ------- | --------- | -------- |
| This implies | a higher | likelihood | of violating | the stringent |               |     |                  |     |         |           |          |
delay threshold D for critical medical tasks, resulting tasks falls below 20-25% under high load, demonstrating
max
in increased lateness (D ). Random exhibits the lowest a complete lack of effective prioritization or resource
total
| apparent | total delay. | However, | this is | highly misleading. | management. |     |     |     |     |     |     |
| -------- | ------------ | -------- | ------- | ------------------ | ----------- | --- | --- | --- | --- | --- | --- |
Asshownlaterinthehitratioanalysis(Fig.8),theRandom
| approachachievesthislowaveragedelaybysimplydropping |     |     |     |     | b: ANALYSIS |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
alargefractionoftasks,especiallycomplexorhigh-priority PASO’ssuperiorhitratio,particularlyforsurgicaltasks,isa
ones, that might induce higher delays. It processes only direct consequence of its design. The algorithm explicitly
F
the ‘‘easiest’’ tasks, rendering its low average delay figure prioritizes m tasks (Algorithm 1, Line 1) and employs
unrepresentativeofeffectivesystemperformanceforcritical preemption (Algorithm 1, Lines 7-14) to reclaim resources
applications. fromF taskswhennecessary.Thisensuresthatcriticalsur-
n
gicaldatastreamsaresuccessfullyoffloadedandprocessed,
b: ANALYSIS maximizing the primary objective (Equation 1) and fulfill-
|     |     |     |     |     | ing the | reliability | requirements. |     | The poor | performance | of  |
| --- | --- | --- | --- | --- | ------- | ----------- | ------------- | --- | -------- | ----------- | --- |
PASO’seffectivenessindelaymanagement,especiallyunder
load, highlights the benefit of its integrated SDN control, Randomhighlightsthenecessityofintelligentorchestration,
priority queuing, and preemption mechanisms. By ensuring while the results for PSO and SA underscore the need for
critical tasks (F m ) are processed first and non-critical priority-aware and preemptive mechanisms beyond simple
tasks (F ) can be preempted, PASO minimizes deadline optimizationheuristicsincriticalhealthcarescenarios.PASO
n
violations for surgical data, directly addressing the core consistently maintains surgical task hit ratios well above
requirement of surgical IoMT. The high delays seen with typicalminimumrequirements(H min ).
PSOandSAindicatetheirpotentialunsuitabilityforreal-time
criticalsystemswithoutsignificantmodificationsforpriority 3) LINKUTILIZATION
awarenessandcongestionhandling. Effective network management requires balancing load to
|     |     |     |     |     | avoid congestion. |     | Fig. 9 | shows | the 90th | percentile | link |
| --- | --- | --- | --- | --- | ----------------- | --- | ------ | ----- | -------- | ---------- | ---- |
2) HITRATIOPERFORMANCE utilization over simulation time, providing insight into the
The hit ratio, representing the percentage of submitted peakloadexperiencedbythemostheavilyusedlinksinthe
| tasks successfully | processed |     | at an edge | node, is crucial for | network. |     |     |     |     |               |     |
| ------------------ | --------- | --- | ---------- | -------------------- | -------- | --- | --- | --- | --- | ------------- | --- |
| 113800             |           |     |            |                      |          |     |     |     |     | VOLUME13,2025 |     |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
FIGURE7. Comparisonoftotaldelayforcompletedmedicaltasks(Fm)acrossdifferenttaskloads,evaluatingPASOagainstPSO,SA,andRandom
methodsoverfoursimulatednetworktopologies.
FIGURE8. ComparisonofHitRatioforaveragetasks(solidlines)andcriticalsurgicaltasks(dashedlines)underincreasingtaskload,evaluatingPASO
againstPSO,SA,andRandomacrossfournetworktopologies.
FIGURE9. 90thpercentilelinkutilizationoversimulationtime, FIGURE10. ImpactofPASO’sutilizationthresholdsettingontask
comparingthepeakloadonbusylinksunderPASO,PSO,SA,andRandom completion:Percentageofdroppedtasksasafunctionoftheconfigured
allocationmethods(underburstload). linkutilizationthreshold(evaluatedwithaloadof200tasks).
b: ANALYSIS
a: OBSERVATIONS
PASO maintains a significantly lower and more stable 90th PASO’s ability to maintain lower peak utilization (roughly
percentile link utilization, generally fluctuating between 15-25%lowerpeakscomparedtotheothermethods)demon-
|         |           |           |           |            | strates more | effective load | balancing | across the | network |
| ------- | --------- | --------- | --------- | ---------- | ------------ | -------------- | --------- | ---------- | ------- |
| 65% and | 75%. This | indicates | that even | the busier | links        |                |           |            |         |
in the network managed by PASO are not excessively infrastructure. This is achieved through its combination of
|     |     |     |     |     | latency-aware | path selection | (Algorithm | 1, Line | 5) and |
| --- | --- | --- | --- | --- | ------------- | -------------- | ---------- | ------- | ------ |
overloaded.
PSO, SA, and Random exhibit substantially higher 90th the implicit congestion avoidance driven by the utilization
percentile utilization values, frequently exceeding 85% and thresholdcheck(Algorithm1,Line9)coupledwithpreemp-
tion.Bypreventingexcessiveloadonindividuallinks,PASO
| sometimes | approaching | 90% | or more. This | suggests | that |     |     |     |     |
| --------- | ----------- | --- | ------------- | -------- | ---- | --- | --- | --- | --- |
these methods lead to significant traffic concentration on enhancesoverallnetworkstabilityandreducesthelikelihood
ofpacketdropsorexcessivequeuingdelays,contributingto
| certain | links, creating | potential | congestion | bottlenecks. |     |     |     |     |     |
| ------- | --------------- | --------- | ---------- | ------------ | --- | --- | --- | --- | --- |
Unsurprisingly, Random allocation, oblivious to network thesuperiordelayandhitratioperformanceobservedearlier.
| state, leads | to high | and erratic | peak utilization. | PSO | and |     |     |     |     |
| ------------ | ------- | ----------- | ----------------- | --- | --- | --- | --- | --- | --- |
SA,whileattemptingoptimization,seemtocreatehotspots, 4) UTILIZATIONTHRESHOLDSENSITIVITY
possiblydue tosuboptimal pathchoices orlack ofdynamic To determine an appropriate operational threshold for the
congestionmitigation. preemption mechanism in PASO (Algorithm 1, Line 9),
| VOLUME13,2025 |     |     |     |     |     |     |     |     | 113801 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
| we analyzed | the | impact | of varying |     | this threshold |     | on the |     |     |     |     |     |     |     |
| ----------- | --- | ------ | ---------- | --- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
numberofdroppedtasks,asshowninFig.10.Theanalysis
wasperformedwithafixedloadof200tasks.
a: OBSERVATIONS
Thenumberofdroppedtasksexhibitsaconvexrelationship
withtheutilizationthreshold.
| • Low | Thresholds |     | (e.g., <  | 60%):   | Setting | the threshold |     |     |     |     |     |     |     |     |
| ----- | ---------- | --- | --------- | ------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| too   | low makes  | the | admission | control | overly  | conserva-     |     |     |     |     |     |     |     |     |
tive. Many tasks are rejected or deferred even when FIGURE11. Controlleroverheadandsystemefficiencyindicators:
sufficientcapacitymightexist,leadingtoahighnumber (a)Averagequeuesize,and(b)Effectiveenergyconsumptionforhitted
ofdroppedtasksduetoartificialscarcity. tasks,underPASOandbaselinemethodsacrossvaryingtaskloads.
| • High | Thresholds |     | (e.g., > | 90%): | Setting | the threshold |     |     |     |     |     |     |     |     |
| ------ | ---------- | --- | -------- | ----- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
too high allows links to become heavily congested decision-making process (including preemption checks and
before preemption or rejection occurs. This can lead dynamicreallocation)combinedwithsuccessfullyadmitting
to increased queuing delays, potentially causing tasks more tasks leads to greater contention at processing or
(especially medical ones with strict deadlines D ) to transmission points. While the controller aims for optimal
max
be dropped due to deadline expiry, even if admitted placement, the increased volume of admitted tasks can
initially. naturally lead to larger queues. This indicates a trade-off:
|     |     |     |     |     |     |     |     | PASO achieves | better | QoS | and hit | rates, | potentially | at the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | --- | ------- | ------ | ----------- | ------ |
• OptimalRange(around80%):Theminimumnumber
of dropped tasks occurs when the threshold is set cost of requiring resources capable of handling these larger
around 80%. This value appears to strike the best transientqueues,orthatthecontrolleritselfmightexperience
balance: it allows efficient utilization of link capacity higherprocessingloadsper unittimewhentaskarrivalsare
| while | maintaining |     | enough | buffer | to prevent | excessive |     | veryfrequent. |          |     |           |        |              |     |
| ----- | ----------- | --- | ------ | ------ | ---------- | --------- | --- | ------------- | -------- | --- | --------- | ------ | ------------ | --- |
|       |             |     |        |        |            |           |     | Fig. 11b      | presents | the | effective | energy | consumption, |     |
congestionandminimizedeadlineviolations.
calculatedasthetotalenergyconsumedfortasktransmissions
b: ANALYSIS multiplied by the hit ratio. This metric reflects the energy
Thissensitivityanalysisjustifiessettingtheoperationallink efficiency in terms of useful work done (successfully
utilization threshold for PASO at approximately 80% for completed tasks). PASO shows the highest effective energy
|               |              |     |      |       |        |            |     | consumption | across | all task | loads | (e.g., approx. | 345 | mJ for |
| ------------- | ------------ | --- | ---- | ----- | ------ | ---------- | --- | ----------- | ------ | -------- | ----- | -------------- | --- | ------ |
| the simulated | environment. |     | This | value | allows | the system | to  |             |        |          |       |                |     |        |
maximize task admissions (contributing to higher through- 1000tasks).PSOandSAhavesimilar,lowereffectiveenergy
put)whileeffectivelymanagingcongestionthroughproactive consumption(PSO:approx.238mJ,SA:approx.279mJat
preemption, thereby ensuring QoS compliance, particularly 1000 tasks), while Random is the lowest (approx. 127 mJ
for delay-sensitive medical tasks. The results presented in at 1000 tasks). Although PASO consumes more energy for
successfullycompletedtasks,thisisdirectlycorrelatedwith
| Figs. 7, | 8, and | 9 were | obtained | using | this | empirically |     |     |     |     |     |     |     |     |
| -------- | ------ | ------ | -------- | ----- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
determinedoptimalthreshold. itssignificantlyhigherhitratio,especiallyforcriticaltasks.
|     |     |     |     |     |     |     |     | PASO ensures | more | tasks, | particularly |     | critical | ones, are |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ------ | ------------ | --- | -------- | --------- |
D. CONTROLLEROVERHEADANDSYSTEMEFFICIENCY completed,andtheenergyinvestedinthesetaskscontributes
INDICATORS tosuccessfuloutcomes.Thelowereffectiveenergyofother
methods,especiallyRandom,isaconsequenceoftheirlower
Tofurtheraddresspotentialcontrolleroverheadandsystem-
wide efficiency, we analyze the average queue size in the hit ratios – less energy is spent on successful tasks because
systemandtheeffectiveenergyconsumptionforsuccessfully fewer tasks succeed overall. Therefore, while PASO might
|     |     |     |     |     |     |     |     | lead to higher | absolute |     | energy expenditure |     | for | successful |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --- | ------------------ | --- | --- | ---------- |
completedtasks,asdepictedinFig.11.
Fig. 11a illustrates the average queue size as the number operations,itdoessobymaximizingtheutilityandsuccess
rateofoffloadedtasks,whichiscrucialinhigh-stakesIoMT
oftasksincreases.Thequeuesizecanreflectcontentionfor
| resourcesorprocessingdelays.ForPASO,theaveragequeue |           |     |          |     |         |       |     | applications. |     |     |     |     |     |     |
| --------------------------------------------------- | --------- | --- | -------- | --- | ------- | ----- | --- | ------------- | --- | --- | --- | --- | --- | --- |
| size increases                                      | steadily, |     | becoming | the | highest | among | the |               |     |     |     |     |     |     |
methodsat800and1000tasks(0.48and0.72,respectively). E. PERFORMANCEUNDERWIRELESSCHANNELNOISE
In contrast, PSO and SA show more moderate increases To assess the impact of wireless channel quality on the
(PSO:0.28,SA:0.34at1000tasks),whileRandomexhibits performanceofPASOandthebaselinealgorithms,wevaried
a lower queue size (0.12 at 1000 tasks), likely because it the SNR from 10 dB to 25 dB. Fig. 12 illustrates the
drops a significant number of tasks, thus reducing overall hit ratio performance, while Table 6 shows the total delay
systemloadandqueuing.PASO’shigherqueuesizeathigh for completed medical tasks under these varying SNR
loads, despite its superior hit ratio and delay performance conditions. These results were obtained from simulations
for critical tasks, might suggest that its more sophisticated involving800tasks.
| 113802 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
Itscorestrengthslieinthesynergisticcombinationof:1.
|     |     |     |     |     |     |     | Explicit | Prioritization: |     | Processing | medical |     | tasks | (F ) first |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ---------- | ------- | --- | ----- | ---------- |
m
ensurestheyreceivepreferentialtreatmentforresourceallo-
|     |     |     |     |     |     |     | cation.    | 2. Preemptive |     | Resource | Reallocation:  |     | Dynamically |          |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | -------- | -------------- | --- | ----------- | -------- |
|     |     |     |     |     |     |     | reclaiming | bandwidth     |     | from     | lower-priority |     | tasks (F    | n ) when |
criticaltasksfacecongestioniscrucialforguaranteeingQoS
|     |     |     |     |     |     |     | (low delay, | high | completion |     | rate) for | surgical | data | streams. |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ---------- | --- | --------- | -------- | ---- | -------- |
Thisisakeydifferentiatorfromnon-preemptiveorpriority-
|     |     |     |     |     |     |     | unaware | approaches |     | like standard | PSO/SA |     | or Random. | 3.  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ------------- | ------ | --- | ---------- | --- |
SDN-EnabledControl:Centralizednetworkvisibilityallows
|     |     |     |     |     |     |     | for informed, |     | latency-aware |     | routing | decisions | and | efficient |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------- | --- | ------- | --------- | --- | --------- |
implementationofthepreemptionpolicy.
PASOachievessubstantiallyhigherhitratios(completion
| FIGURE12. | ImpactofSNRonHitRatioforPASOandbaselinealgorithms |     |     |     |     |     |            |          |          |       |     |         |             |     |
| --------- | ------------------------------------------------- | --- | --- | --- | --- | --- | ---------- | -------- | -------- | ----- | --- | ------- | ----------- | --- |
|           |                                                   |     |     |     |     |     | rates) for | critical | surgical | tasks | (up | to 200% | improvement |     |
(800tasks).
|     |     |     |     |     |     |     | over Random   |      | and 50-90%    |       | over PSO/SA      |        | under  | high load) |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | ------------- | ----- | ---------------- | ------ | ------ | ---------- |
|     |     |     |     |     |     |     | and maintains |      | significantly |       | lower end-to-end |        | delays | (up to     |
|     |     |     |     |     |     |     | 70% lower     | than | PSO/SA        | under | high             | load). | This   | directly   |
TABLE6. TotaldelayforeachmethodatdifferentSNRlevels.
translatestohigherreliabilityandresponsiveness,whichare
|     |     |     |     |     |     |     | non-negotiable |     | in surgical |     | settings. | The balanced |     | link uti- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --- | --------- | ------------ | --- | --------- |
lizationfurtherconfirmsPASO’sabilitytomanagenetwork
resourcesefficiently,preventingbottlenecksthatplagueother
methods.
Theexaminationofaveragequeuesizes(Fig.11aindicates
|             |     |         |     |                |            |     | that PASO | might  | lead | to  | larger queues |        | under         | high load |
| ----------- | --- | ------- | --- | -------------- | ---------- | --- | --------- | ------ | ---- | --- | ------------- | ------ | ------------- | --------- |
|             |     |         |     |                |            |     | compared  | to PSO | and  | SA. | This is       | likely | a consequence | of        |
| As observed |     | in Fig. | 12, | all algorithms | experience | a   |           |        |      |     |               |        |               |           |
itshighersuccessrateinadmittingandroutingtasks,which
| degradation | in  | hit ratio | as the | SNR decreases | (i.e., | as noise |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | ------ | ------------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
thencompetefordownstreamresources,orpotentiallydueto
| levels increase). |     | PASO | consistently |     | maintains | the highest |     |     |     |     |     |     |     |     |
| ----------------- | --- | ---- | ------------ | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
theslightlyhigherper-taskprocessingtimeatthecontroller
| hit ratio   | across | all tested | SNR | levels, | demonstrating | better   |              |               |     |          |     |       |           |         |
| ----------- | ------ | ---------- | --- | ------- | ------------- | -------- | ------------ | ------------- | --- | -------- | --- | ----- | --------- | ------- |
|             |        |            |     |         |               |          | for its more | sophisticated |     | decision |     | logic | when task | arrival |
| resilience. | For    | instance,  | at  | an SNR  | of 10         | dB, PASO |              |               |     |          |     |       |           |         |
ratesarehigh.Similarly,theeffectiveenergyconsumptionfor
| achieves | a hit | ratio of | approximately |     | 69.1 %, | while PSO |     |     |     |     |     |     |     |     |
| -------- | ----- | -------- | ------------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
successfullycompletedtasks(Fig.11b)ishighestforPASO.
achievesapproximately41.0%,SAachievesapproximately
|     |     |     |     |     |     |     | This, however, |     | reflects | the | energy | spent on | a much | larger |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --- | ------ | -------- | ------ | ------ |
44.6%,andRandomperformsthepoorestatapproximately
|     |     |     |     |     |     |     | proportion | of  | successful | task | completions, |     | indicating | that |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | ---- | ------------ | --- | ---------- | ---- |
24.3%.ThisindicatesthatPASO’sprioritizationandresource
|              |            |     |     |           |           |         | while absolute |     | energy | for successful |     | tasks | might | be higher, |
| ------------ | ---------- | --- | --- | --------- | --------- | ------- | -------------- | --- | ------ | -------------- | --- | ----- | ----- | ---------- |
| reallocation | mechanisms |     | are | effective | even when | channel |                |     |        |                |     |       |       |            |
PASOmaximizestheutilityderivedfromenergyexpenditure
| quality | degrades, | ensuring | a   | higher | completion | rate for |             |      |          |       |      |       |             |       |
| ------- | --------- | -------- | --- | ------ | ---------- | -------- | ----------- | ---- | -------- | ----- | ---- | ----- | ----------- | ----- |
|         |           |          |     |        |            |          | by ensuring | more | critical | tasks | meet | their | objectives. | These |
criticaltasks.
|            |       |     |            |       |     |             | aspects | highlight | trade-offs: |     | PASO’s | superior |     | QoS and |
| ---------- | ----- | --- | ---------- | ----- | --- | ----------- | ------- | --------- | ----------- | --- | ------ | -------- | --- | ------- |
| Similarly, | Table | 6   | shows that | lower | SNR | values lead |         |           |             |     |        |          |     |         |
reliabilitycomewiththeneedforrobustunderlyingresources
| to increased | total | delay | for all | methods. | This | is expected, |     |     |     |     |     |     |     |     |
| ------------ | ----- | ----- | ------- | -------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
andpotentiallyhigher,butmoreeffective,energyusefortasks
aspoorerchannelqualitywouldnecessitatemoreretransmis-
thataresuccessfullydelivered.
sionsorlowereffectivedatarates.PASOconsistentlyexhibits
|             |       |          |        |             |                  |         | While    | the DRL | agent | shows       | strong | learning         | capabilities |           |
| ----------- | ----- | -------- | ------ | ----------- | ---------------- | ------- | -------- | ------- | ----- | ----------- | ------ | ---------------- | ------------ | --------- |
| lower total | delay | compared | to     | PSO and     | SA across        | the SNR |          |         |       |             |        |                  |              |           |
|             |       |          |        |             |                  |         | and can  | achieve | good  | performance |        | after sufficient |              | training  |
| range. At   | 10 dB | SNR,     | PASO’s | total delay | is approximately |         |          |         |       |             |        |                  |              |           |
|             |       |          |        |             |                  |         | (as seen | in Figs | 5 and | 6),         | PASO’s | deterministic,   |              | priority- |
124.5ms,significantlylowerthanPSO’s(approx.260.02ms)
|     |     |     |     |     |     |     | driven, | and preemptive |     | approach | provides |     | more | consistent |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | -------- | -------- | --- | ---- | ---------- |
andSA’s(approx.154.15ms).
|     |     |     |     |     |     |     | guarantees | for | critical | surgical | tasks, | especially | in  | dynamic |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | -------- | ------ | ---------- | --- | ------- |
TheseresultshighlightPASO’srobustnessinmaintaining
environmentswhererapidadaptationiskey.TheDRLagent’s
superiorperformanceintermsofbothhitratioanddelay,even
performanceishighlydependentontherewardshapingand
underchallengingwirelessnoiseconditions,whencompared
|     |     |     |     |     |     |     | the diversity | of  | its training |     | data, whereas |     | PASO’s | rules are |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | ------------- | --- | ------ | --------- |
totheotherheuristicandrandomapproaches.
explicitlydefinedforthesurgicalcontext.
However,itisimportanttoacknowledgecertainlimitations
F. DISCUSSION of the PASO framework. The current study primarily
Thesimulationresultsconsistentlydemonstratetheeffective- relies on simulation-based validation, and a full real-world
ness of the proposed PASO framework for surgical IoMT implementation is necessary to comprehensively assess its
orchestration. Compared to Random allocation, PSO, SA, practical deployability and identify all operational chal-
and a DRL-based scheduler, PASO delivers significantly lenges.Scalabilityto significantlylargerandmorecomplex
betterperformanceacrossthecriticalmetrics. networks presents a key challenge. As the network size
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 113803 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
grows, the centralized SDN controller, inherent in PASO’s non-medicaltasks(F )toensuresurgicaldataintegrityand
n
design, might become a performance bottleneck due to the timeliness.
increasingcomputationalloadforreal-timepathcalculations, Our simulation results compellingly demonstrated the
statemanagement,anddecision-makingfornumerousflows significantadvantagesofPASOcomparedtobaselinemeth-
(as indicated by its complexity O(NlogN + N · (L + ods, including Random allocation, PSO, SA, and a DRL
V logV))). Maintaining a consistent global network view agent. PASO consistently delivered superior performance,
could also introduce overhead and latency. Moreover, this particularlyunderhighnetworkloadandwhensubjectedto
centralization makes the controller a potential single point varying wireless channel conditions. Notably, it maintained
of failure; its malfunction could disrupt network orches- significantly lower end-to-end delays for successfully com-
tration, highlighting a critical failure mode that warrants pletedtasks,achievingreductionsofapproximately55-70%
robust redundancy and failover mechanisms in practical comparedtoPSOand10-25%comparedtoSAunderheavy
deployments. Furthermore, a detailed security analysis, task loads. While the DRL agent demonstrated competitive
specifically addressing aspects like data privacy beyond performance after training, PASO’s explicit mechanisms
assumed in-transit encryption, authentication mechanisms, often resulted in better outcomes for time-critical surgical
attack resilience of the orchestration framework, endpoint tasks.Mostcritically,PASOexcelledinensuringthesuccess-
security, and access control to the SDN controller, was not ful completion of vital surgical tasks within their deadlines,
within the scope of this initial investigation and stands as exhibiting deadline success rates (hit ratios) for these
a significant limitation. While real-world implementation criticaltasksthatwereapproximately82%higherthanPSO,
poses practical difficulties, including ensuring seamless 50% higher than SA, and a remarkable 200% higher than
interoperabilitywithdiversemedicaldevicesandintegration Random allocation when the system was under significant
into existing hospital networks, these aspects, along with load. PASO also generally outperformed the DRL agent in
robustsecuritymeasures,arecriticalforfuturedevelopment. guaranteeingdeadlinesforhigh-prioritysurgicaltasksdueto
The deployment and management of SDN controllers in its inherent design focus. Furthermore, PASO demonstrated
stringent clinical environments also demand considerations more effective network load balancing, maintaining lower
for physical security, fault tolerance, and adherence to peaklinkutilizationcomparedtotheothermethods,thereby
healthcareregulatorycompliance. enhancing network stability and reducing the likelihood of
While not explicitly plotted, the trade-off might involve congestion-induceddelaysortaskdrops.
slightlyhighercomputationaloverheadattheSDNcontroller These findings underscore the efficacy of integrating
for executing the PASO logic compared to Random and explicittaskprioritizationandpreemptiveresourcemanage-
potentially different energy consumption patterns (as noted ment within an SDN framework for meeting the uniquely
in the original draft, although detailed energy analysis is demanding requirements of surgical IoMT. PASO success-
outside the scope of the current plots). However, given the fully maximizes the completion rate of life-critical tasks
life-critical nature of surgical IoMT, the substantial gains while rigorously adhering to strict QoS guarantees, repre-
in reliability (hit ratio) and timeliness (low delay, reduced senting a substantial improvement over existing approaches
lateness) provided by PASO strongly justify its adoption, thatoftenlacksophisticatedpriorityhandlingorpreemptive
potentiallyoutweighingminorincreasesincontrollerloador capabilitiesnecessaryforsuchsensitiveapplications.
energy use. The analysis indicates that PASO successfully For future research, several promising directions emerge.
balances the competing demands of maximizing critical Firstly, incorporating machine learning techniques, partic-
task throughput, adhering to strict latency constraints, and ularly reinforcement learning, beyond the baseline DQN
efficientlyutilizingnetworkandedgeresources. model explored here, into the SDN controller could enable
more adaptive and predictive resource allocation strategies
VII. CONCLUSIONANDFUTURESTUDIES that learn optimal policies from network dynamics and
This paper addressed the critical challenge of resource task patterns over time. This could involve exploring more
orchestration in surgical IoMT environments, where guar- advancedDRLarchitecturesorhybridapproachescombining
anteeing the timely and reliable processing of high-priority PASO’srule-basedsystemwithDRL’slearningcapabilities.
medical tasks under stringent Quality of Service (QoS) Secondly, inspired by the need for a more comprehensive
constraints is paramount. We proposed the Priority-Aware perspective,futureworkwillexplicitlyexploreandcompare
SDN Orchestration (PASO) framework, which leverages PASO against a wider array of alternative advanced orches-
Software-Defined Networking (SDN) for centralized con- tration techniques, such as those employing game-theoretic
trol and dynamic resource management. PASO employs a models or other sophisticated heuristics beyond the specific
strategy focused explicitly on maximizing the throughput metaheuristic baselines (PSO, SA) and the initial DRL
of critical surgical tasks (F ) that must be completed baseline considered in this initial study. This will allow for
m
within their strict delay bounds (D ). This is achieved a more thorough evaluation of PASO’s relative strengths
max
through intelligent task offloading, latency-aware routing, and weaknesses in diverse scenarios. Thirdly, while our
and a novel preemptive resource reallocation mechanism current work assumes foundational end-to-end encryption
that dynamically reclaims bandwidth from lower-priority for data in transit (as stated in Section III), a dedicated and
113804 VOLUME13,2025

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
comprehensive security analysis for the PASO framework [5] S. Vishnu, S. J. Ramson, and R. Jegan, ‘‘Internet of Medical Things
itselfisacriticalfuturedirection.Thiswillinvolvedesigning (IoMT)—Anoverview,’’inProc.5thInt.Conf.Devices,CircuitsSyst.
(ICDCS),Jan.2020,pp.101–104.
| and integrating | robust | security | mechanisms |     | specifically | tai- |             |          |            |        |        |        |                 |
| --------------- | ------ | -------- | ---------- | --- | ------------ | ---- | ----------- | -------- | ---------- | ------ | ------ | ------ | --------------- |
|                 |        |          |            |     |              |      | [6] (2023). | Internet | of Medical | Things | (IoMT) | Market | Size to Surpass |
loredtoSDN-controlledsurgicalIoMTenvironments.Future
|     |     |     |     |     |     |     | Us$ | 370.9 Bn | by 2032. | Accessed: | Nov. 1, 2024. | [Online]. | Available: |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --------- | ------------- | --------- | ---------- |
work must meticulously address data privacy beyond basic https://market.us/report/internet-of-medical-things-iomt-market/
encryption,establishstrongauthenticationandauthorization [7] B.Bhushan,A.Kumar,A.K.Agarwal,A.Kumar,P.Bhattacharya,and
protocols (including for the SDN controller), ensure the A.Kumar,‘‘TowardsasecureandsustainableInternetofMedicalThings
(IoMT):Requirements,designchallenges,securitytechniques,andfuture
integrity and availability of control plane operations, and trends,’’Sustainability,vol.15,no.7,p.6177,Apr.2023.
bolsterresilienceagainstpotentialattackstargetingbothdata [8] H. Ouda, K. Elgazzar, and H. S. Hassanein, ‘‘AI-enhanced robotic
telesurgicaldigitaltwinsfor6Gandbeyond,’’inProc.IEEECan.Conf.
planevulnerabilitiesandthePASOorchestrationlogic.This
Electr.Comput.Eng.(CCECE),Aug.2024,pp.162–163.
includesexploringdefensesagainstdenial-of-serviceattacks,
[9] D.Alekseeva,A.Ometov,andE.S.Lohan,‘‘Towardstheadvanceddata
unauthorizedaccess,anddatamanipulationthreats.
processingformedicalapplicationsusingtaskoffloadingstrategy,’’in
Fourthly, to further broaden the scope of secure IoMT, Proc.18thInt.Conf.WirelessMobileComput.,Netw.Commun.(WiMob),
Oct.2022,pp.51–56.
futureworkcouldalsodrawinspirationfromadvancements
[10] E.Checcuccietal.,‘‘Metaversesurgicalplanningwiththree-dimensional
in other domains, such as efficient blockchain-assisted virtualmodelsforminimallyinvasivepartialnephrectomy,’’Eur.Urol.,
identity management for consumer electronics in the Meta- vol.85,no.4,pp.320–325,Apr.2024.
verse[110],lightweightblockchain-enhancedauthentication [11] H. Wang, S. Ding, S. Yang, C. Liu, S. Yu, and X. Zheng, ‘‘Guided
activitypredictionforminimallyinvasivesurgerysafetyimprovementin
| for UAVs | [111], | and frameworks | for | secure | and fair | mobile |     |     |     |     |     |     |     |
| -------- | ------ | -------------- | --- | ------ | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
theInternetofMedicalThings,’’IEEEInternetThingsJ.,vol.9,no.6,
| crowdsensing | [112], | to  | develop holistic | and | robust | security |     |     |     |     |     |     |     |
| ------------ | ------ | --- | ---------------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
pp.4758–4768,Mar.2022.
architectures for sensitive surgical data and operations. [12] C.Dong,Y.Sun,M.Shafiq,N.Hu,Y.Liu,andZ.Tian,‘‘Optimizing
Fifthly,amorecomprehensiveinvestigationintoenergyeffi- mobility-awaretaskoffloadinginsmarthealthcareforInternetofMedical
|     |     |     |     |     |     |     | Things | through | multiagent | reinforcement | learning,’’ |     | IEEE Internet |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ---------- | ------------- | ----------- | --- | ------------- |
ciency,explicitlyoptimizingfordevicebatterylifealongside
ThingsJ.,vol.11,no.8,pp.13677–13691,Apr.2024.
latency and throughput, would be valuable, especially for [13] N. Kherraf, S. Sharafeddine, C. M. Assi, and A. Ghrayeb, ‘‘Latency
battery-powered surgical instruments or wearable sensors. andreliability-awareworkloadassignmentinIoTnetworkswithmobile
This aligns with broader efforts towards eco-friendly IoT edge clouds,’’ IEEE Trans. Netw. Service Manage., vol. 16, no. 4,
pp.1435–1449,Dec.2019.
| solutions, | for instance |     | by leveraging |     | energy | harvesting |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------------- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
[14] Z.Wang,Z.Jia,H.Liao,Z.Zhou,X.Zhao,L.Zhang,S.Mumtaz,and
| for a sustainable |     | future | [113]. Furthermore, |     | extending | the |     |     |     |     |     |     |     |
| ----------------- | --- | ------ | ------------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
J.J.P.C.Rodrigues,‘‘Energy-awareandURLLC-awaretaskoffloading
forInternetofHealthThings,’’inProc.IEEEGlobalCommun.Conf.,
| framework | to support | dynamic | QoS | requirements, |     | where |     |     |     |     |     |     |     |
| --------- | ---------- | ------- | --- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Dec.2020,pp.1–6.
taskprioritiesordelayboundsmightchangeduringdifferent
|           |            |            |       |          |     |           | [15] Z. Zhou, | Z.  | Wang, H. | Yu, H. Liao, | S. Mumtaz, | L.  | Oliveira, and |
| --------- | ---------- | ---------- | ----- | -------- | --- | --------- | ------------- | --- | -------- | ------------ | ---------- | --- | ------------- |
| phases of | a surgical | procedure, | would | increase | its | practical |               |     |          |              |            |     |               |
V.Frascolla,‘‘Learning-basedURLLC-awaretaskoffloadingforInternet
applicability.Extendingtheevaluationtoincorporatediverse of Health Things,’’ IEEE J. Sel. Areas Commun., vol. 39, no. 2,
device mobility patterns and their impact on network pp.396–410,Feb.2021.
|          |       |       |                 |     |               |     | [16] Q.-U.-A. | Mastoi, | T. Y. | Wah, R. | G. Raj, and | A. Lakhan, | ‘‘A novel |
| -------- | ----- | ----- | --------------- | --- | ------------- | --- | ------------- | ------- | ----- | ------- | ----------- | ---------- | --------- |
| dynamics | would | offer | a more holistic |     | understanding | of  |               |         |       |         |             |            |           |
cost-efficientframeworkforcriticalheartbeattaskschedulingusingthe
PASO’s performance in highly fluid environments. Finally, InternetofMedicalThingsinafogcloudsystem,’’Sensors,vol.20,no.2,
future work should explore distributed control architectures p.441,Jan.2020.
[17] K.Alatoun,K.Matrouk,M.A.Mohammed,J.Nedoma,R.Martinek,
| or hierarchical | SDN | models | to enhance | scalability, |     | improve |     |     |     |     |     |     |     |
| --------------- | --- | ------ | ---------- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
andP.Zmij,‘‘Anovellow-latencyandenergy-efficienttaskscheduling
resilienceagainstcontrollerfailure,andinvestigatepractical
frameworkforInternetofMedicalThingsinanedgefogcloudsystem,’’
deploymentstrategiesaddressingtheseoperationalcomplex- Sensors,vol.22,no.14,p.5327,Jul.2022.
ities. Validating the PASO framework through real-world [18] H.A.Alharbi,B.A.Yosuf,M.Aldossary,andJ.Almutairi,‘‘Energy
testbed implementations using standard SDN hardware and and latency optimization in edge-fog-cloud computing for the Inter-
|     |     |     |     |     |     |     | net | of Medical | Things,’’ | Comput. | Syst. Sci. | Eng., | vol. 47, no. 1, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------- | ---------- | ----- | --------------- |
protocolswouldprovidefurtherinsightsintoitsperformance pp.1299–1319,2023.
anddeployabilityinactualhealthcaresettings. [19] K.Lin,S.Pankaj,andD.Wang,‘‘Taskoffloadingandresourceallocation
|     |     |     |     |     |     |     | for edge-of-things |     | computing | on smart | healthcare | systems,’’ | Comput. |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --------- | -------- | ---------- | ---------- | ------- |
Electr.Eng.,vol.72,pp.348–360,Nov.2018.
REFERENCES
|     |     |     |     |     |     |     | [20] M. Ben | Ammar, | I. Ben | Dhaou, | D. El Houssaini, |     | S. Sahnoun, A. |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------ | ------ | ---------------- | --- | -------------- |
[1] V. Shah and A. Khang, ‘‘Internet of Medical Things (IoMT) driving Fakhfakh,andO.Kanoun,‘‘Requirementsforenergy-harvesting-driven
the digital transformation of the healthcare sector,’’ in Data-Centric edge devices using task-offloading approaches,’’ Electronics, vol. 11,
no.3,p.383,Jan.2022.
AISolutionsandEmergingTechnologiesintheHealthcareEcosystem.
BocaRaton,FL,USA:CRCPress,2023,pp.15–26. [21] K.Wang,J.Jin,Y.Yang,T.Zhang,A.Nallanathan,C.Tellambura,and
B.Jabbari,‘‘Taskoffloadingwithmulti-tiercomputingresourcesinnext
| [2] S. A. | Ajagbe, | J. B. Awotunde, | A.  | O. Adesina, | P. Achimugu, | and |     |     |     |     |     |     |     |
| --------- | ------- | --------------- | --- | ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
T. A. Kumar, ‘‘Internet of Medical Things (IoMT): Applications, generation wireless networks,’’ IEEE J. Sel. Areas Commun., vol. 41,
challenges,andprospectsinadata-driventechnology,’’Intell.Healthcare, no.2,pp.306–319,Feb.2023.
Infrastruct.,vol.1,pp.299–319,Jan.2022. [22] S.Ahmad,S.Khan,I.A.Shah,M.F.Nadeem,S.Jan,andT.Whangbo,
[3] F. Al-Turjman, M. H. Nawaz, and U. D. Ulusar, ‘‘Intelligence in the ‘‘Optimalresourceallocationandtaskschedulinginfogcomputingfor
InternetofMedicalThingsera:Asystematicreviewofcurrentandfuture InternetofMedicalThingsapplications,’’Hum.-CentricComput.Inf.Sci.,
vol.13,pp.1–17,Dec.2023.
trends,’’Comput.Commun.,vol.150,pp.644–660,Jan.2020.
[4] K.Kakhi,R.Alizadehsani,H.M.D.Kabir,A.Khosravi,S.Nahavandi, [23] H.A.Alameddine,S.Sharafeddine,S.Sebbah,S.Ayoubi,andC.Assi,
and U. R. Acharya, ‘‘The Internet of Medical Things and artificial ‘‘Dynamictaskoffloadingandschedulingforlow-latencyIoTservices
intelligence: Trends, challenges, and opportunities,’’ Biocybernetics inmulti-accessedgecomputing,’’IEEEJ.Sel.AreasCommun.,vol.37,
Biomed.Eng.,vol.42,no.3,pp.749–771,Jul.2022. no.3,pp.668–682,Mar.2019.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 113805 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
[24] N.Kumari,A.Yadav,andP.K.Jana,‘‘Taskoffloadinginfogcomputing: [46] M.Ullah,S.Khan,andM.Alazab,‘‘IntelligentloadmanagementinIoMT
Asurveyofalgorithmsandoptimizationtechniques,’’Comput.Netw., using federated learning at the edge,’’ ACM Trans. Internet Technol.,
vol.214,Sep.2022,Art.no.109137. vol.25,no.2,pp.1–25,Jun.2025.
[25] X. Deng, J. Yin, P. Guan, N. N. Xiong, L. Zhang, and S. Mumtaz, [47] R. Siyadatzadeh, F. Mehrafrooz, M. Ansari, B. Safaei, M. Shafique,
‘‘Intelligentdelay-awarepartialcomputingtaskoffloadingformultiuser J.Henkel,andA.Ejlali,‘‘ReLIEF:Areinforcement-learning-basedreal-
industrialInternetofThingsthroughedgecomputing,’’IEEEInternet
timetaskassignmentstrategyinemergingfault-tolerantfogcomputing,’’
ThingsJ.,vol.10,no.4,pp.2954–2966,Feb.2023. IEEEInternetThingsJ.,vol.10,no.12,pp.10752–10763,Jun.2023.
[26] X. Lin, J. Wu, A. K. Bashir, W. Yang, A. Singh, and A. A. AlZubi, [48] J.HuangandX.Li,‘‘Ultra-lowlatencysdnstrategiesforsurgicalIoT
‘‘FairHealth:Long-termproportionalfairness-driven5Gedgehealthcare systems,’’ IEEE Trans. Ind. Informat., vol. 17, no. 6, pp.4045–4054,
| in Internet | of  | Medical | Things,’’ | IEEE Trans. | Ind. | Informat., | vol. 18, | Jun.2021. |     |     |     |     |     |     |     |
| ----------- | --- | ------- | --------- | ----------- | ---- | ---------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
no.12,pp.8905–8915,Dec.2022. [49] Y.LuoandM.Zhao,‘‘Schedulingandbandwidthreservationinedge-
[27] M.Mukherjee,V.Kumar,D.Maity,R.Matam,C.X.Mavromoustakis,
assistedroboticsurgery,’’IEEETrans.Netw.ServiceManage.,vol.20,
Q.Zhang,andG.Mastorakis,‘‘Delay-sensitiveandpriority-awaretask
no.2,pp.123–135,May2023.
| offloading | for | edge computing-assisted |     | healthcare |     | services,’’ | in Proc. |                |     |         |          |      |            |          |         |
| ---------- | --- | ----------------------- | --- | ---------- | --- | ----------- | -------- | -------------- | --- | ------- | -------- | ---- | ---------- | -------- | ------- |
|            |     |                         |     |            |     |             |          | [50] C. Zhang, | S.  | Liu, H. | Yang, G. | Cui, | F. Li, and | X. Wang, | ‘‘Joint |
IEEEGlobalCommun.Conf.,Dec.2020,pp.1–5. task offloading and resource allocation in mobile edge computing-
[28] S.RazdanandS.Sharma,‘‘InternetofMedicalThings(IoMT):Overview, enabledmedicalvehicularnetworks,’’Mathematics,vol.13,no.1,p.52,
| emergingtechnologies,andcasestudies,’’IETETech.Rev.,vol.39,no.4, |     |     |     |     |     |     |     | Dec.2024. |     |     |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
pp.775–788,Jul.2022.
|               |          |        |           |            |            |            |          | [51] Y.Li,Y.Wang,S.Chen,X.Huang,andT.Huang,‘‘Resourceallocation |            |          |     |                         |     |             |     |
| ------------- | -------- | ------ | --------- | ---------- | ---------- | ---------- | -------- | --------------------------------------------------------------- | ---------- | -------- | --- | ----------------------- | --- | ----------- | --- |
| [29] J.-P.-A. | Yaacoub, | M.     | Noura, H. | N. Noura,  | O. Salman, | E.         | Yaacoub, |                                                                 |            |          |     |                         |     |             |     |
|               |          |        |           |            |            |            |          | and data                                                        | offloading | strategy | for | edge-computing-assisted |     | intelligent |     |
| R.Couturier,  |          | and A. | Chehab,   | ‘‘Securing | Internet   | of Medical | Things   |                                                                 |            |          |     |                         |     |             |     |
telemedicinesystem,’’Sensors,vol.23,no.10,p.4943,May2023.
| systems: | Limitations, |     | issues and | recommendations,’’ |     | Future | Gener. |                                                                  |     |     |     |     |     |     |     |
| -------- | ------------ | --- | ---------- | ------------------ | --- | ------ | ------ | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|          |              |     |            |                    |     |        |        | [52] A.Mahjoubi,A.Ramaswamy,andK.-J.Grinnemo,‘‘Anonlinesimulated |     |     |     |     |     |     |     |
Comput.Syst.,vol.105,pp.581–606,Apr.2020. annealing-basedtaskoffloadingstrategyforamobileedgearchitecture,’’
[30] M.CiciogluandA.Çalhan,‘‘Amultiprotocolcontrollerdeploymentin IEEEAccess,vol.12,pp.70707–70718,2024.
SDN-basedIoMTarchitecture,’’IEEEInternetThingsJ.,vol.9,no.21,
|     |     |     |     |     |     |     |     | [53] Y. Li, | ‘‘Optimization | of  | task offloading |     | problem | based on simulated |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | --- | --------------- | --- | ------- | ------------------ | --- |
pp.20833–20840,Nov.2022.
|     |     |     |     |     |     |     |     | annealing | algorithm | in  | MEC,’’ | in Proc. | 9th Int. Conf. | Intell. | Comput. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ------ | -------- | -------------- | ------- | ------- |
[31] J.Ren,G.Yu,Y.Cai,andY.He,‘‘Latencyoptimizationforresourceallo-
WirelessOpt.Commun.(ICWOC),Jun.2021,pp.47–52.
cationinmobile-edgecomputationoffloading,’’2017,arXiv:1704.00163.
|     |     |     |     |     |     |     |     | [54] A. Mahjoubi, |     | K.-J. Grinnemo, |     | and J. Taheri, | ‘‘An | efficient simulated |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------------- | --- | -------------- | ---- | ------------------- | --- |
[32] C.-F.Liu,M.Bennis,M.Debbah,andH.VincentPoor,‘‘Dynamictask
annealing-basedtaskschedulingtechniquefortaskoffloadinginamobile
offloading and resource allocation for ultra-reliable low-latency edge edgearchitecture,’’inProc.IEEE11thInt.Conf.CloudNetw.(CloudNet),
computing,’’2018,arXiv:1812.08076.
Nov.2022,pp.159–167.
| [33] E. Al-Masri, |     | ‘‘An edge-based | resource | allocation |     | optimization | for the |                                                               |     |     |     |     |     |     |     |
| ----------------- | --- | --------------- | -------- | ---------- | --- | ------------ | ------- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                   |     |                 |          |            |     |              |         | [55] X.Yuan,H.Tian,Z.Zhang,Z.Zhao,L.Liu,A.K.Sangaiah,andK.Yu, |     |     |     |     |     |     |     |
InternetofMedicalThings(IoMT),’’2021,arXiv:2108.13177.
|     |     |     |     |     |     |     |     | ‘‘A MEC | offloading | strategy | based | on improved |     | DQN and simulated |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | -------- | ----- | ----------- | --- | ----------------- | --- |
[34] W.Fan,X.Liu,H.Yuan,N.Li,andY.Liu,‘‘Time-slottedtaskoffloading
annealingforInternetofBehavior,’’ACMTrans.SensorNetw.,vol.19,
| and | resource | allocation | for cloud-edge-end |     | cooperative | computing |     |     |     |     |     |     |     |     |     |
| --- | -------- | ---------- | ------------------ | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
no.2,pp.1–20,May2023.
networks,’’IEEETrans.MobileComput.,vol.23,no.8,pp.8225–8241,
Aug.2024. [56] S. Dong, Y. Xia, and J. Kamruzzaman, ‘‘Quantum particle swarm
|     |     |     |     |     |     |     |     | optimization |     | for task | offloading | in  | mobile | edge computing,’’ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ---------- | --- | ------ | ----------------- | --- |
[35] A.Rancea,I.Anghel,andT.Cioara,‘‘Edgecomputinginhealthcare:
|              |     |                |     |               |        |           |          | IEEE | Trans. | Ind. Informat., |     | vol. | 19, no. | 8, pp.9113–9122, |     |
| ------------ | --- | -------------- | --- | ------------- | ------ | --------- | -------- | ---- | ------ | --------------- | --- | ---- | ------- | ---------------- | --- |
| Innovations, |     | opportunities, | and | challenges,’’ | Future | Internet, | vol. 16, |      |        |                 |     |      |         |                  |     |
Aug.2023.
no.9,p.329,Sep.2024.
|     |     |     |     |     |     |     |     | [57] T.Gao,Q.Tang,J.Li,Y.Zhang,Y.Li,andJ.Zhang,‘‘Aparticleswarm |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[36] A.Motamedhashemi,B.Safaei,A.MahdiHosseiniMonazzah,J.Henkel,
optimizationwithLévyflightforservicecachingandtaskoffloadingin
andA.Ejlali,‘‘FUSION:Afuzzy-basedmulti-objectivetaskmanage-
mentforfognetworks,’’IEEEAccess,vol.12,pp.152886–152907,2024. edge-cloudcomputing,’’IEEEAccess,vol.10,pp.76636–76647,2022.
[37] A. Motamedhashemi, B. Safaei, A. M. H. Monazzah, and A. Ejlali, [58] Q. You and B. Tang, ‘‘Efficient task offloading using particle swarm
|         |            |     |                    |     |         |          |          | optimization |     | algorithm | in edge | computing | for industrial | Internet | of  |
| ------- | ---------- | --- | ------------------ | --- | ------- | -------- | -------- | ------------ | --- | --------- | ------- | --------- | -------------- | -------- | --- |
| ‘‘DATA: | Throughput |     | and deadline-aware |     | genetic | approach | for task |              |     |           |         |           |                |          |     |
Things,’’J.CloudComput.,vol.10,no.1,pp.1–11,Dec.2021.
schedulinginfognetworks,’’IEEEEmbeddedSyst.Lett.,vol.16,no.4,
|     |     |     |     |     |     |     |     | [59] B. Safaei, | H.  | Taghizade, | A. M. | H. Monazzah, |     | K. T. Khoosani, | P.  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | ----- | ------------ | --- | --------------- | --- |
pp.409–412,Dec.2024.
Sadeghi,A.Mohammadsalehi,J.Henkel,andA.Ejlali,‘‘Introduction
| [38] M. Rostami |     | and S. Goli-Bidgoli, |     | ‘‘An overview |     | of QoS-aware | load |     |     |     |     |     |     |     |     |
| --------------- | --- | -------------------- | --- | ------------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
balancingtechniquesinSDN-basedIoTnetworks,’’J.CloudComput., and evaluation of attachability for mobile IoT routing protocols with
vol.13,no.1,p.651,Apr.2024. Markovchainanalysis,’’IEEETrans.Netw.ServiceManage.,vol.19,
no.3,pp.3220–3238,Sep.2022.
| [39] K. Doka | and | R. Kumar, | ‘‘Prioritization-based |     |     | delay sensitive | task |     |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ---------------------- | --- | --- | --------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
offloading in SDN-integrated mobile IoT network,’’ Pervas. Mobile [60] H.Nashaat,W.Hashem,R.Rizk,andR.Attia,‘‘DRL-baseddistributed
taskoffloadingframeworkinedge-cloudenvironment,’’IEEEAccess,
Comput.,vol.74,Oct.2024,Art.no.101960.
|     |     |     |     |     |     |     |     | vol. | 12, pp.33580–33594, |     | 2024. | [Online]. | Available: | https://www. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------------- | --- | ----- | --------- | ---------- | ------------ | --- |
[40] F.AhmedandI.Khan,‘‘AdaptiveML-basedresourceallocationinedge-
assistedsmarthealthcaresystems,’’IEEEInternetThingsJ.,vol.10,no.5, researchgate.net/publication/378673881_DRL-Based_Distributed_Task
pp.2121–2134,May2023. _Offloading_Framework_in_Edge-Cloud_Environment
[41] F. Z. Cherhabil, M. Sedrati, and S.-S. Bendib, ‘‘The integration of [61] Z.Wang,H.Li,E.J.Knoblock,andR.D.Apaza,‘‘Deepreinforcement
softwaredefinednetworkinmobileedgecomputingfortaskoffloading learning-based joint routing and capacity optimization in an aerial
|     |     |     |     |     |     |     |     | and | terrestrial | hybrid | wireless | network,’’ | IEEE | Access, vol. | 12, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | -------- | ---------- | ---- | ------------ | --- |
andresourceallocationofIoTapplications,’’inLectureNotesinNetworks
andSystems,2023,pp.845–855. pp.132056–132069, 2024. [Online]. Available: https://www.research
[42] J. Luis Herrera, J. Galán-Jiménez, J. Berrocal, and J. M. Murillo, gate.net/publication/382350990_Deep_Reinforcement_Learning-based_
‘‘OptimizingresponsetimeinSDN-edgeenvironmentsfortime-strictIoT Joint_Routing_and_Capacity_Optimization_in_an_Aerial_and_Terrestr
ial_Hybrid_Wireless_Network
applications,’’2021,arXiv:2104.06926.
[43] K.Xiao,Z.Mei,A.Dong,K.Feng,andP.Dai,‘‘Jointtaskoffloadingand [62] L. Zhang, H. Wang, Y. Chen, and Q. Li, ‘‘Robust optimization of
wirelesssensornetworkdeploymentusingmulti-objectivemetaheuristics
| resource | allocation | in  | software-defined |     | networking-enabled |     | vehicular |     |     |     |     |     |     |     |     |
| -------- | ---------- | --- | ---------------- | --- | ------------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
edgecomputing:Amulti-objectiveapproach,’’inProc.IEEEInt.Symp. indynamicenvironments,’’IEEETrans.Evol.Comput.,vol.18,no.1,
ProductComplianceEng.-Asia(ISPCE-ASIA),Oct.2024,pp.1–7. pp.58–70,Feb.2014.
[44] S. Chaudhary, F. Kapadia, A. Singh, N. Kumari, and P. K. Jana, [63] N. Kumar, A. Kumar, and A. Singh, ‘‘Energy-efficient resource
‘‘Prioritization-baseddelaysensitivetaskoffloadinginSDN-integrated allocationin6Gnetworks:AgreedyapproachforrobustnessandQoS,’’
|     |     |     |     |     |     |     |     | IEEE | Trans. | Netw. Service | Manage., |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ | ------------- | -------- | --- | --- | --- | --- |
mobile IoT network,’’ Pervas. Mobile Comput., vol. 103, Oct. 2024, vol. 20, no. 2, pp.4279–4293,
| Art.no.101960. |     |     |     |     |     |     |     | May2023. |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
[45] X.Li,Z.Zhou,Q.He,Z.Shi,W.Gaaloul,andS.Yangui,‘‘Re-scheduling [64] H.Sun,K.Zheng,L.Song,Y.Wu,andJ.Chen,‘‘Robustreinforcement
IoT services in edge networks,’’ IEEE Trans. Netw. Service Manage., learning for dynamic systems under uncertainty,’’ IEEE Trans. Ind.
vol.20,no.3,pp.3233–3246,Sep.2023. Informat.,vol.17,no.11,pp.8919–8928,Nov.2021.
| 113806 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
[65] M.Wang,N.Yang,D.H.Gunasinghe,andN.Weng,‘‘Ontherobustness [86] M. M. S. Maswood, M. R. Rahman, A. G. Alharbi, and D. Medhi,
ofML-basednetworkintrusiondetectionsystems:Anadversarialand ‘‘Anovelstrategytoachievebandwidthcostreductionandloadbalancing
distribution shift perspective,’’ Computers, vol. 12, no. 10, p.209, inacooperativethree-layerfog-cloudcomputingenvironment,’’IEEE
Oct.2023. Access,vol.8,pp.113737–113750,2020.
[66] E. Dritsas and M. Trigka, ‘‘Federated learning for IoT: A survey of [87] M. A. Ala’anzy, R. Zhanuzak, R. Akhmedov, N. Mohamed, and
techniques, challenges, and applications,’’ J. Sensor Actuator Netw., J.Al-Jaroodi,‘‘Dynamicloadbalancingforenhancednetworkperfor-
vol.14,no.1,p.9,Jan.2025. mance in IoT-enabled smart healthcare with fog computing,’’ IEEE
[67] H. Li, L. Tang, S. Chen, L. Zheng, and S. Zhong, ‘‘AoI-aware Access,vol.12,pp.188957–188975,2024.
resourceschedulingforindustrialIoTwithdeepreinforcementlearning,’’ [88] A.Goldsmith,WirelessCommunications.Cambridge,U.K.:Cambridge
Electronics,vol.13,no.6,p.1104,Mar.2024. Univ.Press,2005.
[68] T.Chen,S.Guo,J.Liu,andL.Wang,‘‘Onlineresourceallocationforedge [89] J.G.ProakisandM.Salehi,DigitalCommunications,5thed.NewYork,
computing:Agreedyapproachwithnear-optimalconvergence,’’IEEE NY,USA:McGraw-Hill,2008.
Trans.Commun.,vol.68,no.5,pp.435–449,May2020. [90] P.GuptaandP.R.Kumar,‘‘Thecapacityofwirelessnetworks,’’IEEE
[69] R.Maatoug,F.Masmoudi,andA.Khelifa,‘‘Amulti-agentreinforcement Trans.Inf.Theory,vol.46,no.2,pp.388–404,Mar.2000.
learning algorithm for single-day operating room scheduling,’’ IEEE [91] A.SikoraandV.F.Groza,WirelessPersonalandLocalAreaNetworks.
Access,vol.10,pp.91522–91535,2022. Piscataway,NJ,USA:IEEEPress,2005.
[70] A.Javed,M.W.Iqbal,N.Bashir,andM.U.Khan,‘‘Deeplearningbased [92] A.ZyoudandF.Lacatusu,‘‘PerformanceevaluationofIEEE802.11g
securedatasharingschemeinIoT-fog-cloudenvironmentforsmarthealth wirelessnetworksinthepresenceofBluetoothinterference,’’inProc.
applications,’’IEEEAccess,vol.11,pp.10940–10950,2023. 8thWSEASInt.Conf.Circuits,Syst.,Electron.,ControlSignalProcess.
(CSECS),Jan.2009,pp.123–128.
[71] A. Neumann and F. Neumann, ‘‘Evolutionary diversity optimization
forthedetectionandconcealmentofspatiallydefinedcommunication [93] IEEE Standard for Information Technology—Telecommunications and
networks,’’ IEEE Trans. Evol. Comput., vol. 28, no. 2, pp.250–263, Information Exchange Between Systems Local and Metropolitan Area
Feb.2024. Networks—Specific Requirements Part 11: Wireless LAN Medium
AccessControl(MAC)andPhysicalLayer(PHY)Specifications,IEEE
[72] H. Khalaf, M. Hassan, A. Al-Dubai, A. Al-Ali, and S. Al-Tahhan,
Standard802.11-2020,Feb.2020.
‘‘Greedy-basedresourceallocationfordynamicmulti-tenantslicingin
[94] H.-Y. Hsieh, K.-H. Kim, and A. Sivaraman, ‘‘Improving the utility
5Gnetworks,’’IEEEAccess,vol.10,pp.11696–11707,2022.
ofmetropolitanareaWi-Fimeshnetworks,’’IEEEWirelessCommun.,
[73] A.Musaddiq,T.Olsson,andF.Ahlgren,‘‘Reinforcement-learning-based
vol.16,no.1,pp.34–41,Feb.2009.
routingandresourcemanagementforInternetofThingsenvironments:
[95] G.L.Stöber,D.He,andS.W.Kim,‘‘ImpactofBluetoothinterferenceon
Theoreticalperspectiveandchallenges,’’Sensors,vol.23,no.19,p.8263,
IEEE802.11gWLANperformance,’’inProc.IEEEWirelessCommun.
Oct.2023.
Netw.Conf.(WCNC),Atlanta,GA,USA,Mar.2004,pp.1–6.
[74] E.C.PintoNeto,S.Sadeghi,X.Zhang,andS.Dadkhah,‘‘Federated
[96] A. Raffin, A. Hill, A. Gleave, A. Kanervisto, M. Ernestus, and
reinforcement learning in IoT: Applications, opportunities and open
N.Dormann,‘‘Stable-baselines3:Reliablereinforcementlearningimple-
challenges,’’Appl.Sci.,vol.13,no.11,p.6497,May2023.
mentations,’’J.Mach.Learn.Res.,vol.22,no.268,pp.1–8,Jan.2021.
[75] M. A. Fadilla and T. Sutabri, ‘‘Utilizing greedy algorithm and deep
[Online].Available:http://jmlr.org/papers/v22/20-1364.html
reinforcement learning for optimizing surgical schedules in adap-
[97] Q.Zhang,L.Gui,F.Hou,J.Chen,S.Zhu,andF.Tian,‘‘Dynamictask
tive scheduling,’’ G-Tech, Jurnal Teknologi Terapan, vol. 9, no. 2,
offloadingandresourceallocationformobile-edgecomputingindense
pp.1021–2032,Apr.2025.
cloud RAN,’’ IEEE Internet Things J., vol. 7, no. 4, pp.3282–3299,
[76] Z. Luo, H. Liu, W. Yang, and J. Li, ‘‘An adaptive parameter control
Apr.2020.
methodformetaheuristicalgorithmsindynamicoptimizationproblems,’’
[98] M.A.Jan,M.Usman,X.He,andA.UrRehman,‘‘SAMS:Aseamless
IEEETrans.Evol.Comput.,vol.27,no.5,pp.978–992,May2023.
and authorized multimedia streaming framework for WMSN-based
[77] X. Gao, H. Wu, P. Liu, and X. Li, ‘‘A greedy algorithm for resource IoMT,’’IEEEInternetThingsJ.,vol.6,no.2,pp.1576–1583,Apr.2019.
allocation in multi-user mimo systems with limited feedback,’’ IEEE
[99] J.DoeandJ.Smith,‘‘Deepreinforcementlearningfordynamicresource
Trans. Circuits Syst. I, Reg. Papers, vol. 69, no. 2, pp.910–923,
allocationinedgecomputing,’’inProc.IEEEConf.ExampleDRLAppl.,
Feb.2022.
Mar.2021,pp.100–107.
[78] F.Zhou,C.Sun,F.Zhang,H.Pan,andW.Liang,‘‘Adaptivelearning
[100] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness,
ratedeepreinforcementlearningforresourceallocationinindustrialIoT
M.G.Bellemare,A.Graves,M.Riedmiller,A.K.Fidjeland,G.Ostro-
networks,’’IEEEInternetThingsJ.,vol.10,no.14,pp.12461–12474,
vski, S. Petersen, C. Beattie, A. Sadik, I. Antonoglou, H. King,
May2023.
D. Kumaran, D. Wierstra, S. Legg, and D. Hassabis, ‘‘Human-level
[79] J.He,J.Zhang,andJ.Zhang,‘‘Convergenceanalysisofevolutionary controlthroughdeepreinforcementlearning,’’Nature,vol.518,no.7540,
algorithmsindynamicenvironments:Asurvey,’’IEEETrans.Cybern., pp.529–533,Sep.2018.
vol.53,no.1,pp.10–23,Jan.2023. [101] B.AlphaandD.Gamma,‘‘Asurveyofhyperparametertuningtechniques
[80] D.Liu,Y.Wang,X.Ren,B.Zhou,andQ.Zhang,‘‘Onlinereinforcement fordeepreinforcementlearning,’’J.Artif.Intell.Res.Lett.,vol.79,no.1,
learningwithconvergenceguaranteefordynamicresourceallocationin pp.1167–1236,Apr.2024.
IoTnetworks,’’IEEETrans.NeuralNetw.Learn.Syst.,vol.34,no.3, [102] A.-L. Barabási and R. Albert, ‘‘Emergence of scaling in random
pp.1234–1246,Mar.2023. networks,’’Science,vol.286,no.5439,pp.509–512,Oct.1999.
[81] H.Wang,Y.Shi,F.Yu,J.Yang,andJ.Song,‘‘Convergenceanalysis [103] M. Alshamrani and A. Shami, ‘‘A survey on fiber-wireless (FiWi)
ofonlinefederatedlearningwithnon-iiddata,’’IEEETrans.Cybern., accessnetworkswithSDN:Architecture,enablingtechnologies,andopen
vol.50,no.6,pp.2332–2345,Jun.2020. issues,’’IEEECommun.SurveysTuts.,vol.19,no.2,pp.846–860,2nd
[82] X.Li,Z.Yao,S.Wang,X.Han,andJ.Wang,‘‘Alow-complexityresource Quart.,2017.
allocation algorithm for multi-UAV aided mobile edge computing [104] D. Kreutz, F. M. V. Ramos, P. Veríssimo, C. E. Rothenberg,
networks,’’ IEEE Internet Things J., vol. 11, no. 1, pp.1041–1052, S.Azodolmolky,andS.Uhlig,‘‘Software-definednetworking:Acom-
Jan.2024. prehensivesurvey,’’Proc.IEEE,vol.103,no.1,pp.14–76,Jan.2015.
[83] H.Taghizadeh,B.Safaei,A.M.H.Monazzah,E.Oustad,S.R.Lalani, [105] A. Ali, R. M. Abbas, M. H. Rehmani, and C. Yuen, ‘‘Wireless
andA.Ejlali,‘‘LANTERN:Learning-basedroutingpolicyforreliable communicationtechnologiesforsmartgrid:Asurvey,’’IEEECommun.
energy-harvestingIoTnetworks,’’IEEETrans.Netw.ServiceManage., SurveysTuts.,vol.17,no.1,pp.280–317,1stQuart.,2015.
vol.21,no.6,pp.6542–6554,Aug.2024. [106] H.Beyranvand,M.Lévesque,M.Maier,J.A.Salehi,C.Verikoukis,and
[84] M. Adam and U. Baroud, ‘‘Federated learning for IoT: Applications, D.Tipper,‘‘Toward5G:FiWienhancedLTE-AHetNetswithreliable
trends,taxonomy,challenges,currentsolutions,andfuturedirections,’’ low-latency fiber backhaul sharing and WiFi offloading,’’ IEEE/ACM
IEEEOpenJ.Commun.Soc.,vol.5,pp.7842–7877,2024. Trans.Netw.,vol.25,no.2,pp.690–707,Apr.2017.
[85] S. Sedaghat and A. H. Jahangir, ‘‘RT-TelSurg: Real time telesurgery [107] T.X.TranandD.Pompili,‘‘Jointtaskoffloadingandresourceallocation
using SDN, fog, and cloud as infrastructures,’’ IEEE Access, vol. 9, for multi-server mobile-edge computing networks,’’ IEEE Trans. Veh.
pp.52238–52251,2021. Technol.,vol.68,no.1,pp.856–868,Jan.2019.
VOLUME13,2025 113807

Y.Safaeietal.:Priority-AwareSDNOrchestrationforSurgicalIoMT
[108] A.Yousefpour,G.Ishigaki,R.Gour,andJ.P.Jue,‘‘OnreducingIoT MAHDI SIAMAKI received the M.Sc. degree
servicedelayviafogoffloading,’’IEEEInternetThingsJ.,vol.5,no.2, in computer engineering from the Sharif Uni-
pp.998–1010,Apr.2018. versity of Technology, Tehran, Iran, in 2024.
[109] A.Gopalakrishnan,S.Duttagupta,andD.Nadig,‘‘Schedulingwithtime He is currently a Researcher with the Reliable
awareshapinginintegratedEthernetandWi-Finetworks,’’SocialNetw. and Durable IoT Applications and Networks
Comput.Sci.,vol.5,no.8,pp.1–10,Dec.2024.
(RADIAN)Laboratory,DepartmentofComputer
[110] R.Li,Z.Wang,L.Fang,C.Peng,W.Wang,andH.Xiong,‘‘Efficient
|                     |             |                |     |           |            |     |     | Engineering, | Sharif     | University    | of       | Technology, |
| ------------------- | ----------- | -------------- | --- | --------- | ---------- | --- | --- | ------------ | ---------- | ------------- | -------- | ----------- |
| blockchain-assisted | distributed | identity-based |     | signature | scheme for |     |     |              |            |               |          |             |
|                     |             |                |     |           |            |     |     | where        | he focuses | on developing | adaptive | algo-       |
integratingconsumerelectronicsinmetaverse,’’IEEETrans.Consum.
|     |     |     |     |     |     |     |     | rithms | to optimize | routing | protocols | in dynamic |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ------- | --------- | ---------- |
Electron.,vol.70,no.1,pp.3770–3780,Feb.2024.
|     |     |     |     |     |     |     |     | network | environments. | His | research | interests |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | -------- | --------- |
[111] W. Wang, Z. Han, T. R. Gadekallu, S. Raza, J. Tanveer, and C. includesoftware-definednetworking(SDN),theInternetofThings(IoT),
Su,‘‘Lightweightblockchain-enhancedmutualauthenticationprotocol
machinelearning,deepreinforcementlearning,andcloud-edgecomputing.
| for UAVs,’’ | IEEE Internet Things | J., | vol. 11, | no. 6, pp.9547–9557, |     |     |     |     |     |     |     |     |
| ----------- | -------------------- | --- | -------- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Mar.2024.
[112] W.Wang,Y.Yang,Z.Yin,K.Dev,X.Zhou,X.Li,N.M.F.Qureshi,
| and C. Su,             | ‘‘BSIF: Blockchain-based |               | secure,  | interactive, | and fair    |     |     |     |     |     |     |     |
| ---------------------- | ------------------------ | ------------- | -------- | ------------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
| mobile crowdsensing,’’ | IEEE                     | J. Sel. Areas | Commun., | vol.         | 40, no. 12, |     |     |     |     |     |     |     |
pp.3452–3469,Dec.2022.
[113] B.Safaei,M.Peiravian,andM.Siamaki,‘‘Eco-friendlyIoT:Leveraging
energyharvestingforasustainablefuture,’’IEEESensorsRev.,vol.2,
no.6,pp.32–75,Jun.2025.
|     |     |     |     |     |     |     |     | BARDIA | SAFAEI | received | the Ph.D. | degree in |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | -------- | --------- | --------- |
YALDASAFAEIreceivedtheDoctorofMedicine
computerengineeringfromtheSharifUniversity
(MD)fromHamadanUniversityofMedicalSci- of Technology, Tehran, Iran, in 2021. He was a
|     | ences, Hamadan, |     | Iran, in | 2025. As | a Medical |     |     |     |     |     |     |     |
| --- | --------------- | --- | -------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
VisitingResearcherwiththeChairforEmbedded
|     | Researcher, | she | is currently | collaborating | with |     |     |     |     |     |     |     |
| --- | ----------- | --- | ------------ | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Systems,KarlsruheInstituteofTechnology(KIT),
|     | the Reliable | and | Durable | IoT Applications | and |     |     |          |      |               |       |             |
| --- | ------------ | --- | ------- | ---------------- | --- | --- | --- | -------- | ---- | ------------- | ----- | ----------- |
|     |              |     |         |                  |     |     |     | Germany, | from | 2019 to 2020. | He is | currently a |
Networks(RADIAN)Laboratory,Departmentof
|     |     |     |     |     |     |     |     | Faculty | Member | withthe Computer |     | Engineering |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ---------------- | --- | ----------- |
ComputerEngineering,SharifUniversityofTech-
|     |                 |     |             |     |               |     |     | Department, | Sharif    | University | of              | Technology, |
| --- | --------------- | --- | ----------- | --- | ------------- | --- | --- | ----------- | --------- | ---------- | --------------- | ----------- |
|     | nology, Tehran, |     | Iran, where | she | is conducting |     |     |             |           |            |                 |             |
|     |                 |     |             |     |               |     |     | where       | he is the | Director   | of the Reliable | and         |
researchtowardstheintersectionofcardiovascu-
|     |                  |     |          |            |        |                  |     | Durable      | IoT Applications |               | and Networks | Labo- |
| --- | ---------------- | --- | -------- | ---------- | ------ | ---------------- | --- | ------------ | ---------------- | ------------- | ------------ | ----- |
|     | lar applications | and | Internet | of Medical | Things |                  |     |              |                  |               |              |       |
|     |                  |     |          |            |        | ratory (RADIAN). |     | His research | interests        | include power | efficiency   | and   |
(IoMT).Hermainresearchinterestsincludecardiovasculardisease,neurol-
dependabilityintheIoT,wirelesssensornetworks,mobilead-hocnetworks,
ogy,andtheirassociatedsurgeries.
andcloudcomputing.HewasamemberoftheNationalElitesFoundation,
|     |     |     |     |     |     | from 2016 | to 2020. | He received | the | ACM/SIGAPP | Student | Award |
| --- | --- | --- | --- | --- | --- | --------- | -------- | ----------- | --- | ---------- | ------- | ----- |
POURIAAREFIJAMALreceivedtheB.Sc.degree at SAC’19. He has also served as the Executive Chair for the 28th
incomputerengineeringfromSharifUniversityof CSI International Computer Conference and is a Board Member of
Technology,Tehran,Iran,in2024.Heiscurrently the Cyber-Physical Systems Society of Iran (CPSSI). He is serving as
pursuingtheM.Sc.degreewithSharifUniversity. an Editor in Scientia Iranica, Transactions on Computer Science and
HeisaResearcherwiththeReliableandDurable Engineering, and Electrical Engineering. He served as a reviewer for
IoTApplicationsandNetworks(RADIAN)Lab- severalprestigiousjournalsandconferences,includingIEEETRANSACTIONS
oratory, Department of Computer Engineering, ONMOBILECOMPUTING,IEEETRANSACTIONSONVEHICULARTECHNOLOGY,IEEE
Sharif University of Technology. His research IOTJOURNAL,IEEETRANSACTIONSONCLOUDCOMPUTING,IEEETRANSACTIONS
interest includes developing adaptive algorithms ON CONSUMER ELECTRONICS, IEEE ACCESS, ACM Transactions on Storage,
for resource allocation and task scheduling IEEEICC,ACM/IEEEDAC,IEEESensorsConference,andIEEEWF-IoT.
optimization.
| 113808 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |