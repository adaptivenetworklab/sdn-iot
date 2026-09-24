# [23] Network Slicing Automation Challenges and Benefits

> Source file: `[23] Network Slicing Automation Challenges and Benefits.pdf`

---

| Network | Slicing | Automation: |     | Challenges |     | and Benefits |
| ------- | ------- | ----------- | --- | ---------- | --- | ------------ |
Downloaded from: https://research.chalmers.se, 2026-01-25 06:51 UTC
| Citation | for the | original | published | paper | (version | of record): |
| -------- | ------- | -------- | --------- | ----- | -------- | ----------- |
Tonini, F., Natalino Da Silva, C., Furdek Prekratic, M. et al (2020). Network Slicing Automation:
Challenges and Benefits. 202024th International Conference onOptical Network Design and
Modeling, ONDM 2020.http://dx.doi.org/10.23919/ONDM48393.2020.9133004
| N.B. When | citing this | work, | cite the | original | published | paper. |
| --------- | ----------- | ----- | -------- | -------- | --------- | ------ |
research.chalmers.seoffersthepossibilityofretrievingresearchpublicationsproducedatChalmersUniversityofTechnology.It
coversallkindofresearchoutput:articles,dissertations,conferencepapers,reportsetc.since2004.research.chalmers.seis
administratedandmaintainedbyChalmersLibrary
|     |     |     | (article |     | starts on | next page) |
| --- | --- | --- | -------- | --- | --------- | ---------- |

|     | Network |     |     | Slicing |     |     | Automation: |     |     | Challenges |     |     | and |     |
| --- | ------- | --- | --- | ------- | --- | --- | ----------- | --- | --- | ---------- | --- | --- | --- | --- |
Benefits
Federico Tonini†, Carlos Natalino†, Marija Furdek†, Carla Raffaelli∗, Paolo Monti†
†Department
of Electrical Engineering, Chalmers University of Technology, SE-412 96 Gothenburg, Sweden
|     |     |     |     | E-mail: | {tonini,carlos.natalino,furdek,mpaolo}@chalmers.se |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∗DEI,
|                  |     |         |     |             |     | University | of Bologna,              | 40136 | Bologna, | Italy |     |     |     |     |
| ---------------- | --- | ------- | --- | ----------- | --- | ---------- | ------------------------ | ----- | -------- | ----- | --- | --- | --- | --- |
|                  |     |         |     |             |     | E-mail:    | carla.raffaelli@unibo.it |       |          |       |     |     |     |     |
| Abstract—Network |     | slicing | is  | a technique |     | widely     | used in 5G               |       |          |       |     |     |     |     |
networkswheremultiplelogicalnetworks(i.e.,slices)runovera
| single      | shared    | physical infrastructure. |          |              | Each    | slice may        | realize one |     |     |     |     |     |     |     |
| ----------- | --------- | ------------------------ | -------- | ------------ | ------- | ---------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| or multiple | services, | whose                    | specific | requirements |         | are              | negotiated  |     |     |     |     |     |     |     |
| beforehand  |           | and regulated            | through  |              | Service | Level            | Agreements  |     |     |     |     |     |     |     |
| (SLAs).     | In Beyond | 5G                       | (B5G)    | networks     |         | it is envisioned | that        |     |     |     |     |     |     |     |
slicesshouldbecreated,deployed,andmanagedinanautomated
| fashion       | (i.e.,          | without human      |                 | intervention) |              | irrespective         | of the     |     |     |     |     |     |     |     |
| ------------- | --------------- | ------------------ | --------------- | ------------- | ------------ | -------------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| technological |                 | and administrative |                 | domains       |              | over which           | a slice    |     |     |     |     |     |     |     |
| may           | span. Achieving | this               | vision          | requires      | a            | combination          | of novel   |     |     |     |     |     |     |     |
| physical      | layer           | technologies,      | artificial      |               | intelligence | tools,               | standard   |     |     |     |     |     |     |     |
| interfaces,   | network         | function           | virtualization, |               |              | and software-defined |            |     |     |     |     |     |     |     |
| networking    | principles.     |                    | This paper      | provides      |              | an overview          | of the     |     |     |     |     |     |     |     |
| challenges    | facing          | network            | slicing         | automation    |              | with                 | a focus on |     |     |     |     |     |     |     |
transport networks. Results from a selected group of use cases Fig. 1: Example of a hierarchical architecture for 5G network
showthebenefitsofapplyingconventionaloptimizationtoolsand
slicing.
machine-learning-basedtechniqueswhileaddressingsomeslicing
| design | and provisioning |     | problems. |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ---------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IndexTerms—Networkslicing,Automation,Machinelearning,
Beyond 5G exchanged between the data and the control plane to monitor
|     |     |     |     |     |     |     |     | the state | of  | resources | and services | currently | running | in the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | ------------ | --------- | ------- | ------ |
I. INTRODUCTION
|     |     |     |     |     |     |     |     | network. | In  | this process, | domain-specific |     | information | must |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- | --------------- | --- | ----------- | ---- |
5G is entering the early deployment phase. It will support be abstracted and exchanged through standard or proprietary
an unprecedented number of services (e.g., enhanced Mobile communication protocols. Thanks to this data, the control
Broadband (eMBB), massive Machine Type Communication and orchestration layers (equipped with the right tools) are
(mMTC), and Ultra Reliable and Low Latency Communica- then able to adapt to traffic changes (e.g., scale up or down
|      |           |         |         |        |     |                  |     | slices), | to detect | potential | faults/security |     | breaches, | and to |
| ---- | --------- | ------- | ------- | ------ | --- | ---------------- | --- | -------- | --------- | --------- | --------------- | --- | --------- | ------ |
| tion | (URLLC)). | Network | slicing | allows |     | the provisioning | of  |          |           |           |                 |     |           |        |
these different services over a common physical infrastruc- take proper countermeasures. The entire process needs to be
ture. It creates end-to-end logical networks (i.e., the slices) reliable,secureandautonomous,toreduceasmuchaspossible
|     |           |         |        |          |           |     |              | human | intervention. | This, | in turn, | is one | of the cornerstones |     |
| --- | --------- | ------- | ------ | -------- | --------- | --- | ------------ | ----- | ------------- | ----- | -------- | ------ | ------------------- | --- |
| by  | assigning | virtual | and/or | physical | resources |     | to different |       |               |       |          |        |                     |     |
slices with the guarantee that the performance requirements of Beyond 5G (B5G) networks that aim at creating automated
of specific service are met [1]. and trustworthy network environments [3].
An example of a typical architecture leveraging on the Inthispaper,wehighlighttheprogressandmainchallenges
slicing concept is presented in Fig. 1. It comprises several in achieving a fully automated slice deployment. While the
technological and/or administrative domains in a hierarchical network slicing concept can be applied to all technological
manner[2].Dataplaneresourcesarecontrolledandmonitored domains, we primarily focus on the transport network re-
by domain-specific controllers (i.e., one for each domain). sources. Selected results show how different algorithms based
On top of them, one or more orchestration layers act to onmachinelearningcanbeusedinsliceadmissioncontroland
provide multi-domain, end-to-end services. Once a service attack detection, and how different levels of reliability impact
provider requests a slice, the orchestration layer decides if the backup resources to be provisioned in a URLLC scenario.
| the       | request          | can be satisfied |              | by the      | network. | If          | a slice  | is  |     |                            |     |     |     |     |
| --------- | ---------------- | ---------------- | ------------ | ----------- | -------- | ----------- | -------- | --- | --- | -------------------------- | --- | --- | --- | --- |
| admitted, | a                | proper set       | of resources |             | has      | to be       | assigned | to  |     |                            |     |     |     |     |
|           |                  |                  |              |             |          |             |          |     | II. | STATEOFTHEARTANDCHALLENGES |     |     |     |     |
| meet      | the Service      | Level            | Agreements   |             | (SLAs).  | While       | the net- |     |     |                            |     |     |     |     |
| work      | is in operation, |                  | telemetry    | information |          | is gathered | and      |     |     |                            |     |     |     |     |
Thesectionsummarizesthestateoftheartonnetworkslic-
|     |     |     |     |     |     |     |     | ing. Each | subsection | focuses | on  | a specific | topic highlighting |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ------- | --- | ---------- | ------------------ | --- |
This study was financed in part by the project ”Smart city concepts in what it has been accomplished and what are still the open
Curitibalow-carbontransportandmobilityinadigitalsociety”sponsoredby
| VINNOVA.          |     |     |        |      |     |     |     | questions | that | need to | be addressed. |     |     |     |
| ----------------- | --- | --- | ------ | ---- | --- | --- | --- | --------- | ---- | ------- | ------------- | --- | --- | --- |
| 978-3-903176-21-8 |     |     | © 2020 | IFIP |     |     |     |           |      |         |               |     |     |     |

A. Transport Network Slicing and Technologies Slice isolation techniques prevent different services to po-
tentially depleting slice resources, or to exhaust common
When looking at transport networks, slicing techniques
resourceswithmultipleslices,causingDenialofService(DoS)
should support services with different requirements (e.g., in
to other subscribers. Distributed DoS attacks may also be
terms of data rates and delay) while differentiating the traffic
caused by malware on user’s devices, and since they may
flowing in and the resources used by each slice (i.e., isola-
be connected to different slices simultaneously, this could
tion). For example, Virtual Local Area Networks (VLANs)
lead to unwanted inter-slice communication [11]. Isolation
or Multiprotocol Label Switching (MPLS) can be used to
is also required to avoid resources assigned to a slice to
tag traffic from different users through labels or IDs or
be accessed by other slices, especially for privacy reasons
using other forms of encapsulation [4]. Depending on the
(e.g., personal data stored in a data center). For example,
technology used by a specific data plane, other technologies,
if a network function (NF) is shared, a violation of the NF
such as Flexible Ethernet (FlexE), Optical Transport Network
may allow attackers to steal information from different slices
(OTN),andtime/wavelengthdivisionmultiplexingcanbeused
[10].IsolationofNFscanbedone,e.g.,atthehardwarelevel,
to provide stronger isolation while guaranteeing a specific
the virtual machine, or kernel level [12]. Complete isolation
amount of physical resources for each service [5].
NF is preferable from a security point of view. However,
Transportnetworkresourcescanbeslicedindifferentways
this usually leads to different dedicated networks with very
depending on the use case. For example, a mobile network
low multiplexing gains. Since slices with different security
provider may need different connectivity services depending
requirements must be provided on the same infrastructure,
on which radio splits are used [6]. Physical layer splits may
additional studies are required to investigate how to provide
need hundreds of Gbps of capacity, depending on the antenna
theproperlevelofisolation,dependingonthespecificservice.
configuration. This, in turn, requires a very high capacity
Network virtualization and softwarization introduce also
transport system. Space Division Multiplexing (SDM) tech-
several vulnerabilities to attacks [13] [14]. The separation of
niquescanhelpinthisrespectallowingtocarryhighcapacity
thecontrolandthedataplaneexposesthenetworktopotential
fronthaul traffic. Spatial different SDM resources (e.g., cores
attacks.Managementinterfacesbetweennetworkentitiesmust
and modes) can be assigned to different services, enabling
be secured to avoid impersonation of slice managers, which
isolation [7].
mayleadtotheftofsensitiveinformation,creation/termination
Splits can be also changed at run-time, depending on the
of slice instances and other unauthorized activities. A breach
network conditions (e.g., interference) and resource availabil-
of data plane functions could also result in a control plane
ity[8].Theadoptionofdifferentsplitsbringsstrictlatencyre-
violation [11]. Even though sensitive data can be encrypted,
quirements. Some are delay-tolerant, while other split options
side channels attacks, where an attacker collects information
are time-critical, calling for time-sensitive and deterministic
that is usually exchanged in the clear (e.g., metadata), can
transportsolutionsthatcanadapttoevolvingtrafficconditions.
be conducted. These data could be used, for example, to
As a result, IEEE recently formed the Time-Sensitive Net-
induce faults or tamper with the system cache [11]. All
working(TSN)workinggroupintendingtodevisesolutionfor
these aspects must be studied in the context of 5G and B5G
carrying high and low priority traffic together. They propose
frameworks. The delay and computational effort introduced
to introduce deterministic delay via time synchronization in
by different levels of encryption may impact the slice design
Ethernet networks [5]. Conversely, fusion is a different option
and require additional studies. The most appropriate level of
effective in inserting best-effort traffic in real-time streams by
security countermeasures must be investigated, depending on
addingfixedandboundeddelay(andnojitter)tohighpriority
the service type.
streams,withnoneedfortimesynchronization[9].Slicingcan
Transport network slices may also be affected by physical
be provided with these architectural solutions but studies on
layer attacks, e.g., via signal jamming or external polarization
efficient traffic scheduling are still missing.
modulation. In- or out-of-band jamming can significantly
degrade signals, both wireless or wired, or may target control
B. Attacks, Security and Vulnerabilities
channels, resulting in a denial of access for selected users
A network infrastructure can be attacked to steal sensitive [15], [16]. Polarization modulation attacks in fibers induce
information and/or to disrupt traffic. This, in turn, requires demultiplexing errors [16]. Techniques to detect and mitigate
encryption, authentication, and integrity check mechanisms to theerrorsinducedbytheseattacksmustbeprovided.Different
beputinplace.Threatstophysicalresource,virtualfunctions, ML-based techniques can be employed to detect and classify
andsoftwareplatformsmustbequicklydiscoveredandactions attacksorfindanomaliesinopticalnetworks,requiringaccess
must be taken promptly to avoid service outages [10]. ML- to data at different control and orchestration levels [17].
based techniques can help in finding relationships among Approaches based on hierarchical learning can be applied in
heterogeneous data, where explicit models or complete infor- multi-domain scenarios to hide domain-specific information
mationarenotavailable.However,thisrequires(i)integration [18]. However, this requires to study accurate abstraction
of ML modules with existing platforms, also offering support policiestoavoidtheeffectsoferrorpropagationwhilekeeping
to legacy and current-generation devices, and (ii) proper ML reasonable scalability performance. In addition, ML models
models that match the specific use case and address the also present inherent inaccuracy, especially when new data
inaccuracies due to false positives/negatives. areintroduced.Tocompensate,errormitigationtechniquescan

be considered, e.g., by combining multiple ML models. This that SLAs are met. Also, an appropriate set of data must be
requiresfindingatrade-offamongmodelcomplexity,accuracy, selectedandsenttotheorchestrationlayerto(i)solvetheslice
and time needed to compute the solution (including training). admission and mapping problems in an optimal way and (ii)
to be able to continuously monitor the SLAs during the slice
C. Optimal Resource Allocation Strategies
lifecycle.
Upon acceptance, a slice needs to be mapped into the Establishingamulti-domainsliceleveragesontheprinciple
network infrastructure. In turn, this becomes an optimization ofrecursivevirtualizationandhierarchicalnetworkabstraction
problem where only the right amount of network resources [26]. The network resources allocated to a particular tenant
should be provided while guaranteeing the performance level can be abstracted and exposed to a third party that can
required by a specific service. Otherwise, overprovisioning of constructanewserviceontopofthepriorone.Thisapproach
resources might lead to an increased slice rejection rate or to simplifies the composition of slices allowing a combination
servicedegradation,withanobviousimpactontherevenueof of different resources in a flexible way. Upon the arrival of a
the service/infrastructure provider. slicerequest,theserviceorchestrationlayerdecideswhetherto
Slice resource mapping can be seen as an extension to the admit the slice or not. This process involves the identification
wellstudiedVirtualNetworkEmbedding(VNE)problem[19]. of the domains to be involved. Then, the slice request must
More specifically, VNE finds (i) the optimal placement of be converted into directives for the different domains, that
NF and (2) the best allocation of the virtual link capacity must select the most appropriate set of resources. This can be
required to interconnect the NFs. The solution to a slice doneusinganintent-basednetworkingparadigm,whichallows
resource mapping problem might also have to identify the expressing slice requirements and constraints in the form of
most appropriate data plane technology to be used as well policies [27]. Each domain is also responsible for providing
as a proper set of backup resources (local vs. end-to-end, monitoring data throughout the slice life-cycle. Data from
dedicatedvs.shared)tosupporttherequiredlevelofresiliency different domains are collected and elaborated by the service
in the presence of failures [20]–[22]. In some cases, only orchestration layer to monitor SLAs and take the necessary
specific functions or paths within a single slice need to be actions.Theinteractionsamongtheseentitiescanbebasedon
protected, requiring additional resources to be provided as a a peer to peer approach or a federated infrastructure domain
backup. In other cases, with extreme reliability requirements, [2]. In the former, orchestrators of different domains interact
backupresourcesmustbeprovisionedina1+1or1:1manner. to find a solution that satisfies specific SLA. In the latter,
When the problem becomes very complex, game-theoretic a common cross-domain slice coordinator leverages trusted
approaches can be used to consider the relationship among connectivity across administrative domains and carries out
users, network operators, and service providers, to formulate domain-specific resource allocation.
optimization problems. Examples are the fairness of network In terms of challenges, end-to-end management and or-
resource allocation, profit maximization, and cost minimiza- chestration frameworks require the implementation of specific
tion of network slice’s users [23]. functionalitiestoreachcompleteautomation.Slicedeployment
It should be noted that the slice resources requirement pro- should be autonomous, requiring automatic acceptance or
filemaychangeovertime(e.g.,usersmightbehavedifferently denial of slice requests, based on the network resources and
at a different time of day) and a mere peak-based resource servicerequirements.Thenetworkcontrolshouldalsobeable
assignment could result in low service acceptance. This calls to continuously monitor the state of the resources to adapt the
for strategies aimed at reconfiguring slices over time. As a slice mapping to the evolving network conditions, i.e., to be
result, there are approaches in the literature that support the able to re-configure itself. This is required, for example in the
scaling up/down of slices at run-time based on the level of case of traffic variarion and/failures. All this must work when
utilization of the network resources [24]. Another example of slices traverse different technological and/or administrative
sliceadaptionisthepossibilitytovarythechoiceofbaseband domains,requiringtoelaborateandexposeinformationamong
splits over time, while the slice is in operation. This approach the different entities in a common, standard way.
helps to achieve better resource utilization and to reduce the Artificial intelligence (AI) allows the creation of systems
transport network load. However, this may require frequent that autonomously take decisions based on their perceived
reconfigurations to pursue cost minimization and therefore environment. To do so, information must be collected from
trade-offsmustbederived[25].Predictionmodelscanbealso the network, where equipment of different suppliers co-exists,
be adopted to forecast network changes and take actions on requiring the definition of common standard interfaces to
the network resources in advance. These aspects are analyzed create vendor-agnostic monitoring systems [28]. Moreover,
in the next section. telemetryinformationcanbeexploitedforproactiveorreactive
network re-configurations. Different models can be used to
D. Slice Management and Orchestration
obtaininformationaboutthephysicallayerandtriggerchanges
In the most general case slices might span across multiple atthenetworklevel,e.g.,inrouting,spectrumandmodulation
administrative domains while combining resources belonging assignments [29]. These data can also be used to estimate
to different technological domains. This calls for the de- the traffic and take appropriate actions [30], i.e., triggering
velopment of a standard way to exchange information and reconfiguration strategies to change the current slice resource
interactions among different providers and domains, to ensure assignment and avoid SLA violation or slice request rejection

[28] [31]. Even though these approaches are effective, further
analysis of the computational effort and performance of these 40
strategies, as well as the amount of data to be collected and
elaborated in real-size scenarios require further studies. 35
Finally, from the standardization point of view efforts are
30
needed to enhance current information models to account for
multi-domain connectivity and control, resiliency and perfor- 25
mance measurements, as well as multi-domain intent-based
networking interfaces. From a resource abstraction point of 20
view, the functions and connectivity resources to be exposed 0 250 500 750
impact the end-to-end network performance and cost. Finally, Training iterations
security aspects are yet to be considered in multi-domain
scenarios, e.g., how to guarantee authorization, integrity, and
encryption among different players.
III. BENEFITSOFAUTOMATION:AFEWRESULTS
This section reports a number of selected results while
addressing some of the challenges described above. The use
cases under exam include: slice admission control, optimal
URLLC slice deployment strategies, and application of ML-
based method to address security problems.
A. Intelligent Slice Admission Control
Different strategies based on ML can be employed in the
slice admission process. For example, reinforcement learning
(RL) strategies can be used to make scheduling decisions
based on the feedback derived from past actions. Another
possibility is to use supervised learning methods to derive
traffic predictions (TP) to be used to get insight into future
resource needs.
The work in [31] reports a comparison of the two ap-
proaches.InRL,theinputsfortheneuralnetworkarethevalue
of the service holding time, the number of required resources
and the current status of the infrastructure. The output of the
neural network indicates the best service in the queue to be
provisioned. The reward function is proportional to the sum
of the penalties associated with the services currently waiting
in the buffer and to the ones currently being provisioned
in the infrastructure. At each training iteration, to minimize
the value of the reward function, the discounted reward is
computedandapolicynetworkisoptimizedusingthegradient
descent method. The TP-based heuristic provisions a service
with the help of a regression-based TP function that estimates
the resources required by each one of the services included
within the prediction window τ. A TP-based heuristic checks
each service in the queue and selects the service for which
(i) enough resources are available, and (ii) its provisioning
generates the lowest penalty as compared to selecting other
services in the buffer. Each service expected to be requested
within τ is provisioned if the penalty incurred by the services
within τ when the service is provisioned is greater than the
same penalty when the service is not provisioned. Otherwise,
the service is held in the queue.
Two different kinds of services are considered. A mobile
service provider (MSP) requires the activation of up to 3
small cells, each requiring a dedicated wavelength, and a
total service capacity of up to 4 CPUs in a data center, for
ytlaneP
.gvA
40
Random
Best Fit 30
MaxRev
RL 20
10
0
-10
0 10 20 30
Prediction error (%)
(a)
)%(
LR
.t.r.w
ytlaneP
RL
TP = 1
TP = 3
TP = 5
(b)
Fig. 2: Comparison of average penalty for RL, Random, Best
Fit, and MaxRev (a), and RL vs. TP for different prediction
windows τ and prediction errors (cid:15) (b).
a duration of up to 3 time steps. A cloud service provider
(CSP) requires services with up to 2 wavelengths and 4 CPUs
each, for a duration of [10,15] time steps. All these variables
arerandomlyselectedusingindependentuniformdistributions.
80% of all the services are MSP, while 20% are CSP. The
infrastructureproviderpaysapenaltyproportionaltothedelay
(i.e., measured in time steps) in provisioning a service. The
penalty coefficient of the MSP services is five times bigger
than the one of the CSP services. More details are available
in [31].
Fig. 2a shows how the RL is able to reduce the penalty
factor with respect to three benchmarks: (i) Random, that
selects which service to provision with a uniform probability,
(ii) Best Fit, that selects the service that fits best the available
resources, and (iii) Maximum Revenue (MaxRev), that pri-
oritizes MSP services over the CSP ones. In the beginning,
the RL performs similarly to the Random strategy. When
the number of iterations increases, RL learns that it is more
beneficialtoserveMSPoverCSPservicestokeepthepenalty
factor low. Fig. 2b compares the performance of RL with the
TP-based heuristic for different prediction windows. It shows
that when τ = 1, the performance of RL is always better
regardlessofthevalueofthepredictionerror(cid:15).Forlowvalues
of (cid:15), larger prediction windows allow TP to outperform RL
by up to 6% and 10% in case of τ = 3 and 5, respectively.
However, if (cid:15) is large (i.e., >20%), there is no gain in using
a TP-based heuristic.
B. Optimal URLLC Service Slice Deployment
Networkfailuresimpacttheoperationwithconsequenceson
theserviceprovisioning.Amongalltheservicesenvisionedfor
5G, URLLC are the most critical ones. The deployment of a
URLLC service slice requires provisioning of radio, transport
and cloud resources. In addition, provisioning of additional
backup resources must be considered, to be used in case
of failures. Backup resources can be dedicated or shared,
depending on the specific requirement, whereas in the latter
case some time is needed to switch to the backup resources
when a failure is detected.

TABLE I: Active nodes and capacity savings for 6 node
parameters. Supervised, semi-supervised, and unsupervised
network in the balanced and unbalanced cases under 2 and
learning techniques can be used to identify security breaches
3 hop constraints. The unconstrained case relaxes limitations
by jointly analyzing multiple monitoring parameters. Super-
on the network resources and delay.
vised learning models can be trained to learn the trends
in optical performance indicators that characterize different
Activenodes Saved
attacks and normal working conditions, potentially providing
Network DPP SPP Capacity
fine-granular classification of the attack type and intensity,
2hops-bal 6 4 66.6%
3hops-bal 6 4 66.6% depending on the training set. However, it is not easy to
2hops-unbal 4 4 23.6% provide a representative and precise set of correctly labeled
3hops-unbal 4 4 27.8%
dataforacontinuouslyevolvingattacklandscape.Undersuch
Unconstrained 2 2 0%
circumstances, semi-supervised learning models can be used
for detecting the presence of an attack even if it is previously
unseen,butwithouttheabilitytocategorizeit.Thisisobtained
Two different ILP models are presented in [22] comparing
through training using only the data from normal operating
the outcome of dedicated and shared backup path protection
conditions. Unsupervised learning models can be used to
(DPP and SPP, respectively). Both strategies allow to select
detect attack presence in the network in circumstances when
the best baseband split depending on the available network
no training data is available. These three techniques exhibit
resources while providing resiliency against a single node or
differentrequirementsintermsofdataacquisitionbeforetheir
link failure. The objective of these strategies is to minimize
use, in addition to different levels of performance obtained
the number of nodes where to install cloud resources and the
during their use. Depending on the considered scenario, the
amount of resources to be provisioned. Numerical results are
most appropriate technique to be used needs to be carefully
obtained considering the deployment of a URLLC slice in
evaluated.
a 6 node network, under different conditions. Two different
resource distributions are considered. In the balanced case, In the following, we consider a real test-bed subject to
all the nodes have the same capacity (25 processing units - physical-layer attacks described in [16]. Three different at-
PUs). In the unbalanced case, two nodes are assumed to have tacks have been considered: in- and out-of-band jamming,
unlimited resources, while other nodes have limited capacity and external polarization modulation. The first two attacks
(10PUs).Allthelinkshavethesameandlimitedcapacity(40 consist in inserting harmful signals generated by a continuous
Gbps). More details are available in [22]. wave laser into a breached fiber, propagating in the same
Table I shows the number of nodes selected to host either or in an adjacent optical channel as the channel under test.
baseband,coreorcloudfunctions(referredtoasactivenodes) Polarization modulation, instead, is performed by squeezing
and the saved backup computational capacity when SPP is the fiber with a modulator driven by a sine-wave generator,
used, with respect to the DPP, in the sample network. The inducing changes in the state of polarization that are too fast
unconstrained case, reported as a benchmark, provides a for the coherent receiver to compensate for, which results
lower bound for the number of active nodes, that is the case in erroneous detection. Twelve different Optical Performance
when no constraints on capacity, bandwidth, and latency are Monitoring(OPM)parametersarecollectedfromthenetwork.
applied. Since this case requires only 2 nodes, it also exhibits Threedifferentmodelshavebeenusedforattackdetection:(i)
no backup resource sharing. In real case scenarios, when a supervised learning model using Artificial Neural Network
resources are limited, the number of nodes increases due to (ANN),(ii)asemi-supervisedlearningmodelusingOne-Class
finite node and link capacity. This situation is evaluated under Support Vector Machine (OCSVM), and (iii) an unsupervised
twodifferentdelayconstraints(2and3hops).Inthebalanced learning model using Density-Based Spatial Clustering of
case, sharing backup resources leads to a reduction in the Applications(DBSCAN).TheresultsaresummarizedinTable
number of nodes to be activated, regardless of the number II, where the false positive and negative rates, and the f1
of hops. This is due to the sharing of backup resources in scorearereportedforeachmodel.TheANNisalwayscapable
bothlinksandnodes,thatallowsreducingthebackupcapacity of detecting the attacks although sometimes it might classify
by 66.6%. In the unbalanced case instead, where some nodes theminthewrongattackcategory.Inthesemi-supervisedand
provideextensivecapacity,theSPPisstilleffectiveinsharing unsupervised models, instead, there is a probability that an
backup capacity with a reduction of up to 27.8%. attackwillremainundetected(falsenegative)andaprobability
thatanormaloperatingconditionisflaggedasanattack(false
C. Machine Learning in Optical Network Security
positive). The f1 score is a measure that considers both false
Attacks targeting the physical layer of optical networks can positiveandnegativeratesprovidingaunifiedaccuracymetric.
causeserviceoutagesinvolvingoneormoreslices,depending In the case of OCSVM and DBSCAN, the false positive rate
onthelevelofresourcesharingandisolation.Differentattacks is 0.029 and 0.062, respectively, while the false negative rate
cancauseopticalparameterstodeviatefromregularoperating is 0.003 and 0, respectively. In case of ANN, the f1 score
conditions. Existing models of physical layer impairments are is 1, as it is able to detect all attacks, while in case of
too simplistic to capture the complex effects of a range of OCSVM and DBSCAN it is lower. In particular, the OCSVM
attacks [17]. Instead, ML techniques have found a useful provides very good performance with a score of 0.985, while
application in identifying intricate patterns among different for the DBSCAN the score is 0.970. These results indicate

| TABLE | II: Comparison |     | of the | performance |     | for different | ML  |     |     |     |     |     |     |     |     |
| ----- | -------------- | --- | ------ | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[7] S.G.Leon-Saval,N.K.Fontaine,andR.Amezcua-Correa”,“Photonic
modelsshowingfalsepositiveandnegativerate,andf1score. lantern as mode multiplexer for multimode optical communications,”
OpticalFiberTechnology,vol.35,pp.46–55,2017,nextGeneration
MLmodel Falsepositiverate Falsenegativerate f1score MultiplexingSchemesinFiber-basedSystems.
[8] Y.Lietal.,“Flexibleran:Combiningdynamicbasebandsplitselection
ANN 0 0 1 andreconfigurableopticaltransporttooptimizeranperformance,”IEEE
| OCSVM  |     | 0.029 |     |     | 0.003 |     | 0.985 | NetworkMagazine,2020. |     |                     |            |          |     |              |            |
| ------ | --- | ----- | --- | --- | ----- | --- | ----- | --------------------- | --- | ------------------- | ---------- | -------- | --- | ------------ | ---------- |
| DBSCAN |     | 0.062 |     |     | 0     |     | 0.970 |                       |     |                     |            |          |     |              |            |
|        |     |       |     |     |       |     |       | [9] S. Bjornstad      |     | et al., “Minimizing |            | delay    | and | packet delay | variation  |
|        |     |       |     |     |       |     |       | in switched           |     | 5G transport        | networks,” | IEEE/OSA |     | Journal      | of Optical |
CommunicationsandNetworking,vol.11,no.4,pp.B49–B59,2019.
|          |                |     |           |     |       |          |             | [10] “Theevolutionofsecurityin5G,”5GAmericas,Jul.2019. |       |                  |     |                   |     |            |            |
| -------- | -------------- | --- | --------- | --- | ----- | -------- | ----------- | ------------------------------------------------------ | ----- | ---------------- | --- | ----------------- | --- | ---------- | ---------- |
| that, in | the considered |     | scenario, | the | lower | the data | acquisition |                                                        |       |                  |     |                   |     |            |            |
|          |                |     |           |     |       |          |             | [11] V. A.                                             | Cunha | et al., “Network |     | slicing security: |     | Challenges | and direc- |
overhead, the larger is the error provided by the solution. tions,”InternetTechnologyLetters,vol.2,no.5,p.e125,2019.[Online].
Available:https://onlinelibrary.wiley.com/doi/abs/10.1002/itl2.125
Dependingonthespecificcase,techniquesaimedatimproving
|     |     |     |     |     |     |     |     | [12] Z. Kotulski | et  | al., “On | end-to-end | approach | for | slice isolation | in 5G |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | ---------- | -------- | --- | --------------- | ----- |
theperformanceofunsupervisedandsemi-supervisedlearning
|     |     |     |     |     |     |     |     | networks. | fundamental |     | challenges,” | in 2017 | Federated | Conference | on  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ------------ | ------- | --------- | ---------- | --- |
can be adopted. For example, a time window based approach Computer Science and Information Systems (FedCSIS), Sep. 2017, pp.
783–792.
| allows to | trigger        | countermeasures |          |       | if the  | attack is | detected    | in                                                               |         |            |      |                |     |         |            |
| --------- | -------------- | --------------- | -------- | ----- | ------- | --------- | ----------- | ---------------------------------------------------------------- | ------- | ---------- | ---- | -------------- | --- | ------- | ---------- |
|           |                |                 |          |       |         |           |             | [13] S.Scott-Hayward,S.Natarajan,andS.Sezer,“Asurveyofsecurityin |         |            |      |                |     |         |            |
| several   | of consecutive |                 | samples, | which | reduces | the       | probability |                                                                  |         |            |      |                |     |         |            |
|           |                |                 |          |       |         |           |             | software                                                         | defined | networks,” | IEEE | Communications |     | Surveys | Tutorials, |
of false alarms or attack misdetection over the window at vol.18,no.1,pp.623–654,Firstquarter2016.
|             |     |             |      |       |     |            |           | [14] M.Pattaranantakuletal.,“NFVsecuritysurvey:Fromusecasedriven |          |                     |     |                   |     |      |            |
| ----------- | --- | ----------- | ---- | ----- | --- | ---------- | --------- | ---------------------------------------------------------------- | -------- | ------------------- | --- | ----------------- | --- | ---- | ---------- |
| the expense | of  | introducing | some | delay | in  | the attack | detection |                                                                  |          |                     |     |                   |     |      |            |
|             |     |             |      |       |     |            |           | threat                                                           | analysis | to state-of-the-art |     | countermeasures,” |     | IEEE | Communica- |
process.
tionsSurveysTutorials,vol.20,no.4,pp.3330–3368,Q42018.
|     |     |     |     |     |     |     |     | [15] M. Lichtman |     | et al., “5G | NR jamming, |     | spoofing, | and sniffing: | Threat |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | ----------- | --- | --------- | ------------- | ------ |
IV. CONCLUSIONS assessmentandmitigation,”in2018IEEEInternationalConferenceon
CommunicationsWorkshops(ICCWorkshops),May2018,pp.1–6.
| This | paper | presents | an  | overview | of  | the work | currently |                  |     |                    |     |       |                           |     |     |
| ---- | ----- | -------- | --- | -------- | --- | -------- | --------- | ---------------- | --- | ------------------ | --- | ----- | ------------------------- | --- | --- |
|      |       |          |     |          |     |          |           | [16] C. Natalino | et  | al., “Experimental |     | study | of machine-learning-based |     | de- |
underway to address a number of challenges in the area of tectionandidentificationofphysical-layerattacksinopticalnetworks,”
JournalofLightwaveTechnology,vol.37,no.16,pp.4173–4182,2019.
| transport       | network | slicing. | The   | paper | also         | elaborate | on the   |                                                                   |     |         |         |       |                |     |            |
| --------------- | ------- | -------- | ----- | ----- | ------------ | --------- | -------- | ----------------------------------------------------------------- | --- | ------- | ------- | ----- | -------------- | --- | ---------- |
|                 |         |          |       |       |              |           |          | [17] M.FurdekandC.Natalino,“Machinelearningforopticalnetworksecu- |     |         |         |       |                |     |            |
| main challenges |         | to that  | needs | to    | be addressed |           | to reach | a                                                                 |     |         |         |       |                |     |            |
|                 |         |          |       |       |              |           |          | rity management,”                                                 |     | in 2020 | Optical | Fiber | Communications |     | Conference |
fully automated slice deployment scenario, one of the key andExhibition(OFC),2020,pp.1–3.
et al.,
features for beyond 5G networks. Results on a number of [18] G. Liu “Hierarchical learning for cognitive end-to-end service
provisioninginmulti-domainautonomousopticalnetworks,”Journalof
| selected | use cases | show | how | different | algorithms |     | based on |     |     |     |     |     |     |     |     |
| -------- | --------- | ---- | --- | --------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
LightwaveTechnology,vol.37,no.1,pp.218–225,2019.
machine learning can be used in slice admission control [19] S.Vassilarasetal.,“Thealgorithmicaspectsofnetworkslicing,”IEEE
and attack detection, and how different levels of reliability CommunicationsMagazine,vol.55,no.8,pp.112–119,Aug2017.
|        |            |           |     |       |             |     |         | [20] N. Shahriar |              | et al., “Reliable | slicing | of                   | 5G transport | networks | with      |
| ------ | ---------- | --------- | --- | ----- | ----------- | --- | ------- | ---------------- | ------------ | ----------------- | ------- | -------------------- | ------------ | -------- | --------- |
| impact | the backup | resources |     | to be | provisioned | in  | a URLLC |                  |              |                   |         |                      |              |          |           |
|        |            |           |     |       |             |     |         | dedicated        | protection,” |                   | CoRR,   | vol. abs/1906.10265, |              | 2019.    | [Online]. |
scenario. The discussion of the main challenges suggests Available:http://arxiv.org/abs/1906.10265
that several aspects remain unexplored. Resource assignment [21] M.Lashgarietal.,“Costbenefitsofcentralizingserviceprocessingin
|     |     |     |     |     |     |     |     | 5G network |     | infrastructures,” | in  | Asia Communications |     | and | Photonics |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------------- | --- | ------------------- | --- | --- | --------- |
and re-allocation techniques in dynamic scenarios must be Conference(ACPC)2019. OpticalSocietyofAmerica,2019,p.M3C.2.
studied, especially with novel equipment supporting time- [22] F. Tonini, E. Amato, and C. Raffaelli, “Optimization of optical ag-
sensitive networking. In addition, multi-domain orchestration gregation network for 5G URLLC service,” in 2019 IEEE Global
CommunicationsConference(GLOBECOM),Dec2019,pp.1–6.
frameworksstilllackastandardizedwaytocommunicatewith [23] R.Suetal.,“Resourceallocationfornetworkslicingin5Gtelecommu-
otherdomainorchestrators.Properdatasetstobeexchangedin nicationnetworks:Asurveyofprinciplesandmodels,”IEEENetwork,
thisview(e.g.,monitoringparametersorabstractedresources) vol.33,no.6,pp.172–179,Nov2019.
|     |     |     |     |     |     |     |     | [24] M.R.Razaetal.,“Dynamicslicingapproachformulti-tenant5Gtrans- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
as well as the impact on the network performance require portnetworks[invited],”IEEE/OSAJournalofOpticalCommunications
additional investigation. Also, artificial intelligence is indeed andNetworking,vol.10,no.1,pp.A77–A90,2018.
a powerful tool towards secure and autonomous networks, but [25] G. Wang et al., “Reconfiguration in network slicing—optimizing the
|     |     |     |     |     |     |     |     | profit | and performance,” |     | IEEE | Transactions | on  | Network | and Service |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------------- | --- | ---- | ------------ | --- | ------- | ----------- |
still lacks a deeper scalability analysis. Management,vol.16,no.2,pp.591–605,June2019.
|     |     |     |     |     |     |     |     | [26] I. Afolabi | et  | al., “Network | slicing | and | softwarization: |     | A survey on |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------- | ------- | --- | --------------- | --- | ----------- |
REFERENCES
principles,enablingtechnologies,andsolutions,”IEEECommunications
SurveysTutorials,vol.20,no.3,pp.2429–2453,thirdquarter2018.
[1] “Description of network slice concept, v1.0,” NGMN Alliance, Jan. [27] T.Subramanya,R.Riggio,andT.Rasheed,“Intent-basedmobileback-
2016. hauling for 5G networks,” in 2016 12th International Conference on
| [2] T. Taleb | et al., | “On | multi-domain | network | slicing | orchestration | archi- |     |     |     |     |     |     |     |     |
| ------------ | ------- | --- | ------------ | ------- | ------- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
NetworkandServiceManagement(CNSM),Oct2016,pp.348–352.
tecture and federated resource control,” IEEE Network, vol. 33, no. 5, [28] D. M. Gutierrez-Estevez et al., “Artificial intelligence for elastic man-
pp.242–252,Sep.2019. agement and orchestration of 5G networks,” IEEE Wireless Communi-
[3] “Newservicesandcapabilitiesfornetwork2030:Description,technical cations,vol.26,no.5,pp.134–141,October2019.
| gap | and performance |     | target | analysis,” | ITU-T | FG NET-2030 | Sub-G2, |                  |     |             |          |                |     |            |          |
| --- | --------------- | --- | ------ | ---------- | ----- | ----------- | ------- | ---------------- | --- | ----------- | -------- | -------------- | --- | ---------- | -------- |
|     |                 |     |        |            |       |             |         | [29] F. Musumeci |     | et al., “An | overview | on application |     | of machine | learning |
Oct.2019. techniquesinopticalnetworks,”IEEECommunicationsSurveysTutori-
[4] X. Costa-Pe´rez et al., Network Slicing for 5G Networks. John als,vol.21,no.2,pp.1383–1408,Secondquarter2019.
Wiley and Sons, Ltd, 2018, ch. 9, pp. 327–370. [Online]. Available: [30] D.RafiqueandL.Velasco,“Machinelearningfornetworkautomation:
https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119333142.ch9
|     |     |     |     |     |     |     |     | overview, | architecture, |     | and applications |     | [invited | tutorial],” | IEEE/OSA |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ---------------- | --- | -------- | ----------- | -------- |
[5] P.Sehieretal.,“TransportevolutionfortheRANofthefuture[invited],”
|     |     |     |     |     |     |     |     | Journal | of Optical | Communications |     | and | Networking, | vol. | 10, no. 10, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | -------------- | --- | --- | ----------- | ---- | ----------- |
IEEE/OSAJournalofOpticalCommunicationsandNetworking,vol.11, pp.D126–D143,Oct2018.
no.4,pp.B97–B108,April2019. [31] C.Natalinoetal.,“Machinelearningaidedorchestrationinmulti-tenant
et al.,
[6] R. Ferrus “On 5G radio access network slicing: Radio interface networks,” in 2018 IEEE Photonics Society Summer Topical Meeting
protocolfeaturesandconfiguration,”IEEECommunicationsMagazine,
Series(SUM),July2018,pp.125–126.
vol.56,no.5,pp.184–192,May2018.