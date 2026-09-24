# Enhancing an Intelligent Model for SDN Using Fog Computing and Reinforcement Learning

> Source file: `Enhancing an Intelligent Model for SDN Using Fog Computing and Reinforcement Learning.pdf`

---

Received: March 23, 2025. Revised: April 13, 2025. 347
Enhancing an Intelligent Model for Enhancing Software-Defined Networking
(SDN) Achievement Using Fog Computing and Reinforcement Learning for
Operational Performance and Dynamic Resource Management
Mohanad Sameer Jabbar1*
1Technical College of Engineering, Al-Bayan University, Baghdad, Iraq
* Corresponding author’s Email: mohanad.s@albayan.edu.iq
Abstract: Software-defined networking (SDN) has fundamentally transformed network management through
centralization and programmability. But, high latency, resource waste, and limited adaptability prevent it from
performing well, especially in dynamic applications, such as IoT,5G/6G networks, and smart cities. In order to
overcome these limitations, this research presents an intelligent framework which is a combination of SDN, Fog
Computing and Reinforcement Learning (RL). Fog Computing to process data from source thus removing latency and
bandwidth utilization and RL algorithms can provide an efficient framework for dynamic resource allocation and
intelligent decision making. The proposed work targets at establishing a conceptual model that leverage the best of
both SDN as well as Fog Computing, RL-based algorithms for adapting traffic routing and efficient resource
management, and the design specification of the conceptual framework performance evaluation in terms of latency,
energy and resources consumption. The research applied artificial data that produced simulated environments of IoT
networks and 5G/6G environments and smart city applications. Mininet software handled SDN simulation while
IFogSim operated to model fog computing through custom Python scripts that generated the traffic patterns. The
realness of synthetic data was verified using publicly accessible datasets which included CAIDA and IoT Network
Intrusion Dataset. The research tested various network topologies from 50 nodes to 200 nodes to verify scalability as
well as robustness through different operational situations. Experimental results show that the proposed framework
saturates all resources with an 85% resource utilization and outperforms traditional SDN architectures in terms of
latency (by 40%) and energy efficiency (by 25%). The framework was found to improve overall network performance
while supporting next generation Techs, enabling scalable, flexible, and high performing medium to larger-scale
networks.
Keywords: Computer science, Network, Software-defined networking (SDN), Fog computing, Reinforcement
learning (RL), Latency reduction, Resource allocation, Network optimization, IoT networks.
scalability, flexibility and efficiency such as cloud
1. Introduction computing, 5G/6G networks, and Internet of Things
(IoT) ecosystems [2]. In-spite of having the potential
The evolution of Software-Defined Networking
to transform the network itself, SDN has its own
(SDN) has transformed the world of contemporary
challenges in order to get full advantage &properly
network administration by separating the control
functioning. High latency is one of SDN hot topics,
plane from the data level, allowing for centralized
since there is only one centralized controller in SDN.
control and programmability. This changing of
The far-away physical distance between remote end
architecture enables configuration & management of
devices from the controller limits the decision-
the network properties dynamically, and it is a key
making and forwarding of packets by the controller
pillar for next-gen networks [1]. The global view of
causing significant delays which is not suitable for
the network topology that the SDN provides has
real-time applications e.g. video stream, autonomous
increased its importance in environments that require
systems in large scale networks [3]. Moreover, the
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025 DOI: 10.22266/ijies2025.0630.25
This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received:  March 23, 2025.     Revised: April 13, 2025.                                                                                                   348
misallocation of resources continues to be a major
issue. Conventional SDN architectures are based on
| static  policies  |     | that cannot  |     | adapt  | to  | the  changing  |     |     |     |     |     |     |     |
| ----------------- | --- | ------------ | --- | ------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
behaviour of traffic and availability of resources in
the network which leads to impractical performance
| and  waste  | of  | resources  |     | [4].  | Fog          | Computing  | is       |     |     |     |     |     |     |
| ----------- | --- | ---------- | --- | ----- | ------------ | ---------- | -------- | --- | --- | --- | --- | --- | --- |
| proposed    | to  | overcome   |     | said  | limitations  |            | and  is  |     |     |     |     |     |     |
introduced as a complementary technology to SDN.
| Fog  Computing  |     | broadens  |     | the  | scope  | of  | cloud  |     |     |     |     |     |     |
| --------------- | --- | --------- | --- | ---- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- |
computing by enabling data processing at the edge
| and  close  | to  | data  | sources,  | enhancing  |     | real-time  |     |     |     |     |     |     |     |
| ----------- | --- | ----- | --------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |

| decision-making  |     | while  |     | limiting latency  |     |     | and  |     |     |     |     |     |     |
| ---------------- | --- | ------ | --- | ----------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |

| bandwidth  | usage  | [5].  | However,  |     | integrating  |     | Fog  |     |     |     |     |     |     |
| ---------- | ------ | ----- | --------- | --- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- |
Figure. 1 Hierarchical SDN-based Fog Computing
| Computing with SDN architectures  |     |     |     |     |     | enables us  | to  |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Architecture for IoT Networks
develop a type of distributed framework that takes

| advantage  | of  | the  benefits  |     | presented  |     | by  | the  two  |     |     |     |     |     |     |
| ---------- | --- | -------------- | --- | ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |

technologies. Fog nodes can then take over some
smartphones, sensors, and smart appliances at the
computation from the central SDN controller and
base. The second layer is the fog layer based on SDN
thus, lessen the burden on the controller and achieve
that serves as an intermediate processing point just
| faster  | response  | times  | for  | requests.  |     | Despite  | the  |     |     |     |     |     |     |
| ------- | --------- | ------ | ---- | ---------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- |
below the SDN controller that operates locally. The
| advancement  |     | of  seamless coordination  |     |     |     |     | between  |     |     |     |     |     |     |
| ------------ | --- | -------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
cloud layer includes the global SDN controller that
SDN controllers and fog nodes, it remains a major
|            |     |         |            |     |                |     |     | abstracts  | the  entire  | network.  | For  | example,  | the  |
| ---------- | --- | ------- | ---------- | --- | -------------- | --- | --- | ---------- | ------------ | --------- | ---- | --------- | ---- |
| challenge  | to  | design  | effective  |     | communication  |     |     |            |              |           |      |           |      |
bidirectional arrows symbolize the data flow among
between the two [6]. Reinforcement Learning (RL) is
the layers; the solid lines between layers exhibit a
| a  specific  |          | artificial  | intelligence  |     |               | that  provides  |     |                     |     |                    |     |      |      |
| ------------ | -------- | ----------- | ------------- | --- | ------------- | --------------- | --- | ------------------- | --- | ------------------ | --- | ---- | ---- |
|              |          |             |               |     |               |                 |     | direct  connection  | of  | their components,  |     | and  | the  |
| intelligent  | network  |             | optimization  |     | capabilities  |                 | by  |                     |     |                    |     |      |      |
dashed line in-between fog nodes describing their
| allowing  | systems  |     | to  pursue  |     | optimal  | behaviors  |     |                          |     |       |      |      |        |
| --------- | -------- | --- | ----------- | --- | -------- | ---------- | --- | ------------------------ | --- | ----- | ---- | ---- | ------ |
|           |          |     |             |     |          |            |     | regular  communication.  |     | With  | fog  | and  | cloud  |
through trial-and-error process and is another critical
processing, centralized control is still possible with
| enabler  | of  | intelligent  |     | network  |     | optimization.  |     |          |             |            |          |     |           |
| -------- | --- | ------------ | --- | -------- | --- | -------------- | --- | -------- | ----------- | ---------- | -------- | --- | --------- |
|          |     |              |     |          |     |                |     | minimum  | delay  and  | bandwidth  | between  |     | the  two  |
Reinforcement Learning (RL) has been found to be
points to push and pull information, while the bulk of
| particularly  |     | effective  | for  | complex  |     | optimization  |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | ---- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
the processing occurs between these nodes, allowing
problems in networking, including traffic routing,
|                       |     |     |                               |     |     |     |     | one  to  manage  | the  | entire  | realm  of  | IoT  | devices  |
| --------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | ---------------- | ---- | ------- | ---------- | ---- | -------- |
| load  balancing, and  |     |     | resource allocation [7]. SDN  |     |     |     |     |                  |      |         |            |      |          |
efficiently.
enables the separation of data and control planes,

| providing  | global  |     | network  | view  |     | and  reducing  |     |     |     |     |     |     |     |
| ---------- | ------- | --- | -------- | ----- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Problem Statement
| complexity,  |     | and Fog  | computing  |     |     | covers  | cloud  |     |     |     |     |     |     |
| ------------ | --- | -------- | ---------- | --- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- |
Although there has been lot of improvement in
computing towards the edge of network, bringing
SDN, but there are some challenges that still limits
computation and storing closer to the user, having
|          |           |     |                |     |     |      |          | its  efficiency  | and  adoption  |          | in  modern  |       | network   |
| -------- | --------- | --- | -------------- | --- | --- | ---- | -------- | ---------------- | -------------- | -------- | ----------- | ----- | --------- |
| dynamic  | capacity  |     | of  modifying  |     |     | the  | network  |                  |                |          |             |       |           |
|          |           |     |                |     |     |      |          | environment.     | The  main      | problem  | is          | high  | latency,  |
configuration, and starting to foster the use of RL to
which is due to the centralized mechanism of SDN.
| make  | more  | automated  |     | decisions  |     | in  | these  |     |     |     |     |     |     |
| ----- | ----- | ---------- | --- | ---------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
In wide-area networks, the geographical separation of
| heterogeneous  |     | networks  | [4].  | For  | instance,  |     | it  can  |     |     |     |     |     |     |
| -------------- | --- | --------- | ----- | ---- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- |
end devices and SDN THE controller results in high
predict traffic using R L algorithms and schedule
delay in packet forwarding decision processes. The
resources to maximize the output of the network
presence of latency is a significant challenge in real-
using R L even under different workloads, ensuring
time applications, like IoT-based smart city systems
| that  the  | network  |     | are  performing at  |     |     | their  | full  |     |     |     |     |     |     |
| ---------- | -------- | --- | ------------------- | --- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- |
and autonomous vehicles, wherein even milliseconds
capability [8]. By incorporating RL, it brings this
of delay can lead to disastrous consequences [9]. This
aspect of intelligence to the network management,
SDN incapable of make sure the efficient resource
| providing  | autonomous  |     | decision-making  |     |     | capability  |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ---------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
allocation is one of the main obstacles in the way for
| and  minimizing  |     | the  | manual  |     | intervention.  |     | SDN  |     |     |     |     |     |     |
| ---------------- | --- | ---- | ------- | --- | -------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
SDN. However, traditional SDN architectures are
| architecture  | for  | IoT  | devices  | with  | fog  | computing  |     |     |     |     |     |     |     |
| ------------- | ---- | ---- | -------- | ----- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
based on static policies that ignore the sporadic aspect
| functionalistry(ing)  |     |     | is  illustrated in  |     |     | Fig.  | 1.  The  |     |     |     |     |     |     |
| --------------------- | --- | --- | ------------------- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- |
of either network traffic or resource allocation. This
diagram illustrates a three-tier architecture, with the
leads to sub-optimal utilization of the resources in
| IoT  layer  | including  |     | connected device  |     |     | types  | like   |     |     |     |     |     |     |
| ----------- | ---------- | --- | ----------------- | --- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- |
the networks, resulting in high operational cost and

International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025           DOI: 10.22266/ijies2025.0630.25

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received: March 23, 2025. Revised: April 13, 2025. 349
performance drop [10]. Moreover, conventional SDN new generation networks as per the upcoming
architectures are inflexible and cannot adapt to technologies including Internet of Things (IoT),
dynamic changes of the network condition. For 5G/6G and smart cities. Additionally, RL adds an
example, unexpected traffic bursts or hardware intelligent layer making network management
malfunctions can lead to a loss of network service if autonomous and less manually-intensive process.
the flexibility of the system does not respond fast Additional Contributions This work contributes to
enough to those changes [11]. Fog Computing advancing the theory of SDN and Fog Computing but
combined with SDN alleviates some of these issues also offers practical solutions that can be
by decentralizing data processing and minimizing implemented in real-life applications.
latency. But the integration of SDN controllers with
fog nodes remains a big challenge. Research Objectives
The lack of intelligent decision-making systems This research mainly focuses on the intelligent
worsens the issue, as networks find it difficult to framework design in order to the integration of
allocate resources in a dynamic and efficient manner. Software-Defined Networking (SDN), Fog
These constraints underscore the necessity for a novel Computing and Reinforcement Learning (RL). The
framework that integrates SDN, Fog Computing, and objective of the research is, therefore, specific and is
RL to address these difficulties and improve network to:
functionality. 1. Step 2: Develop a Conceptual Model: A
conceptual model combining the centralised
Significance of the Study features of SDN and decentralised
The current scheme answers the problems stated processing features of fog computing This
above to contribute a unique solution in the form of framework will utilize the benefits of the two
a smart framework consisting of SDN, Fog technologies and develop a distributed
computing, and reinforcement learning. This work architecture that will reduce latency and
makes several key contributions towards a network increase the usage of resources.
management framework. The first is lessening 2. RL Algorithms Implementation: Design and
latency; using Fog Computing, it performs implement of RL algorithms for dynamic
computation at proximity and avoids dependence on resource allocation and smart decision
centralized SDN controllers. This not only facilitates making on these high-level features
faster response times but even lessens the load on the identified in previous subsection. Using
controller, which can serve to perform high-level these Algorithms, Network Traffic Patterns
decision-making tasks. will be analyzed, Future demands will be
Third, the framework entails improved predicted, and Resources will be allocated
operational efficiency through the dynamic allocation accordingly leading to optimal Performance
of resources based on real-time network conditions. under different workloads.
With the introduction of RL algorithms, the 3. Performance Evaluation: Perform extensive
framework can study network traffic behaviours, experiments to assess the performance of the
forecast future requests, and allocate resources. In framework, including latency reduction,
turn, this allows for the best usage of the necessary energy efficiency, and resource utilization.
resources without the need to spend on infrastructure, This evaluation will consider the proposed
thus reducing operational costs and maximizing framework with traditional SDN
network performance. Thirdly, adding RL allows the architectures and other state-of-the-art
framework to make intelligent decisions to adapt solutions.
itself to dynamic network requirements and thereby 4. Show Practical Applicability: Show that the
optimize performance over time. Automation to this framework can actually be used in practice,
degree minimizes human intervention which e.g., in using scenarios like IoT networks,
increases the self-sustainable robustness of the 5G/6G environments, and smart city
network. applications. This would require us to test
Related This study is significant as it has the the framework under realistic environments
potential to move many parts of modern network and study its performance
architecture towards an efficient scalable adaptive The research sections follow this order: Section 2
solution for managing complex networks. Tackling analyzes existing papers about Software-Defined
major challenges including latency, resource Networking (SDN) and Fog Computing and
management and the focus on work style approach, Reinforcement Learning (RL) with their established
the architecture opens up a future for developing shortcomings. The research section details both the
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025 DOI: 10.22266/ijies2025.0630.25
This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received:  March 23, 2025.     Revised: April 13, 2025.                                                                                                   350
study objectives alongside an integrated intelligent  inefficient nature of both static and dynamic platform
framework which connects SDN components with  provisioning leads to poor resource utilization and
Fog  Computing  together  with  Reinforcement  transcription performance, especially on workloads
Learning for solving problems stemming from high  with  unequal  dynamic  characteristics [15].  In
latency and inefficient resources and inflexibility.  addition, SDN architectures have a poor adaptability
The section presents an explanation of methodology  (in all its aspects) that make them non-competitive
where it illustrates mathematical modeling solutions  against real-time variations of network conditions,
with Q-Learning, Deep Q-Networks and Proximal  for example (number of) peak traffic and hardware
Policy  Optimization  algorithms  and  experimental  outage. Despite these limitations, there is still a room
setup  details  for  validating  the  framework.  The  to innovate new solutions to improve the existing
framework  application  analysis  in  Section  5  SDN  frameworks  in  terms  of  efficiency  and
demonstrates how it outperforms conventional SDN  flexibility.  Fog  Computing  has  provided  a  key
structures  and  modern  state-of-the-art  latency  solution  for  a  higher  quality  level  of  network
reduction  and  energy  effectiveness  features  with  performance  (especially  in  IoT  and  Edge-based
resource application metrics. The research decides  systems) throughput or over the Internet in general.
with Section 6 where it displays final remarks about  In contrast to traditional cloud computing, where data
the study's foremost results and proposes additional  processing is centralized in far-away data centers,
research to increase both scalability and practical  Fog Computing decentralizes computation [16] and
presentation of the structure.  moves it toward the edge, that is, closer to where data
is being generated. Fog computing is more suitable
2.  Literature review  for real-time applications like smart city, industrial
|                   |     |     |             |     |        |     |        | IoT,  and       | autonomous  |         | vehicles  | [17],  | due      | to  its  |
| ----------------- | --- | --- | ----------- | --- | ------ | --- | ------ | --------------- | ----------- | ------- | --------- | ------ | -------- | -------- |
| Software-Defined  |     |     | Networking  |     | (SDN)  |     | is  a  |                 |             |         |           |        |          |          |
|                   |     |     |             |     |        |     |        | proximity that  |             | highly  | decrease  | the    | latency  | and      |
paradigm shift in network management that enables a
bandwidth usage in delivery. For instance, in smart
programmable solution for designing and managing
city based IoT systems, fog nodes process the sensor
| networks  | in  a  | simple  | and flexible  |     | manner.  |     | SDN  |     |     |     |     |     |     |     |
| --------- | ------ | ------- | ------------- | --- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
data in proximity of the sensors, which reduces the
makes it possible to separate the communication and
time to make decision and saves the load on central
control functions in networking by separating the
|           |          |       |            |        |                |     |       | cloud      | servers  | [18].  | Abstract:  | It    | signifies  | Fog       |
| --------- | -------- | ----- | ---------- | ------ | -------------- | --- | ----- | ---------- | -------- | ------ | ---------- | ----- | ---------- | --------- |
| control   | plane    | from  | the  data  | plane  | [11].          | As  | this  |            |          |        |            |       |            |           |
|           |          |       |            |        |                |     |       | Computing  | plays    | an     | important  | role  | for        | improved  |
| division  | enables  | the   | dynamic    |        | configuration  |     | of    |            |          |        |            |       |            |           |
network. Aazam et al. presented an extensive survey
network resources, SDN is highly suitable for modern
on Fog Computing, mentioning its key features of
applications like Cloud computing, 5G/6G networks,
|     |     |     |     |     |     |     |     | low latency,  |     | energy-efficiency,  |     | and  | scalability  | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------------- | --- | ---- | ------------ | --- |
and IoT ecosystems. Many studies have examined
overcome the restrictions associated with the cloud-
the evolution of SDN architectures over the last ten
centric designs [19]. Similarly, Dinh et al. showed
years and proposed that they can improve scalability,
|     |     |     |     |     |     |     |     | combined  | support  |     | of  edge  | devices  |     | with  Fog  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | --------- | -------- | --- | ---------- |
lower operational costs, and increase performance
|             |            |     |          |     |          |            |     | Computing,  |        | allowing  | the        | handling  | of dynamic  |          |
| ----------- | ---------- | --- | -------- | --- | -------- | ---------- | --- | ----------- | ------ | --------- | ---------- | --------- | ----------- | -------- |
| [12].  For  | instance,  |     | McKeown  |     | et  al.  | OpenFlow,  |     |             |        |           |            |           |             |          |
|             |            |     |          |     |          |            |     | workloads   | using  | more      | resources  | deployed  |             | in  the  |
however, was one of the first protocols to be defined
distributed environments [20]. Though these have
to become the de facto standard for software-defined
|           |          |     |           |     |           |     |        | covered  | certain  | aspects  |     | but  achieving  |     | seamless  |
| --------- | -------- | --- | --------- | --- | --------- | --- | ------ | -------- | -------- | -------- | --- | --------------- | --- | --------- |
| networks  | (SDNs),  |     | allowing  |     | networks  |     | to be  |          |          |          |     |                 |     |           |
coordination of the above layers with other network
| programmed  | from    | a   | centralized  |        | control  | platform,    |     |            |         |           |     |                |     |           |
| ----------- | ------- | --- | ------------ | ------ | -------- | ------------ | --- | ---------- | ------- | --------- | --- | -------------- | --- | --------- |
|             |         |     |              |        |          |              |     | paradigms  | still   | remain a  |     | challenge      |     | for  Fog  |
| generating  | dozens  |     | of  new      | forms  |          | of  network  |     |            |         |           |     |                |     |           |
|             |         |     |              |        |          |              |     | Computing  | (e.g.,  | SDN).     |     | For  example,  |     | the  SDN  |
automation innovation on top of it [13]. While SDN
|     |     |     |     |     |     |     |     | architectures  |     | involve  | the  | integration of  |     | Fog  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ---- | --------------- | --- | ---- |
has its advantages, it also has its drawbacks. High
|          |             |      |        |             |     |     |      | Computing;  | therefore,  |     | novel  | approaches  |     | must  be  |
| -------- | ----------- | ---- | ------ | ----------- | --- | --- | ---- | ----------- | ----------- | --- | ------ | ----------- | --- | --------- |
| latency  | is  one of  | the  | major  | challenges  |     | as  | SDN  |             |             |     |        |             |     |           |
defined for effective communication and resource
controller is centralized. The physical distance of
|               |        |     |                  |     |     |              |     | management  |     | between  | fog  | nodes  | and  | the  SDN  |
| ------------- | ------ | --- | ---------------- | --- | --- | ------------ | --- | ----------- | --- | -------- | ---- | ------ | ---- | --------- |
| end  devices  | (EDs)  |     | and  controller  |     | in  | large–scale  |     |             |     |          |      |        |      |           |
controller [21]. This highlights the Importance of
networks can degrade the performance of decision–
frameworks which integrate both technologies while
making and packet forwarding due to long–round–
|               |        |     |               |     |     |            |     | maximizing  |     | the  benefits  |     | of  both  | technologies,  |     |
| ------------- | ------ | --- | ------------- | --- | --- | ---------- | --- | ----------- | --- | -------------- | --- | --------- | -------------- | --- |
| trip  times,  | which  | is  | unacceptable  |     | in  | real–time  |     |             |     |                |     |           |                |     |
directing to the overall optimization of the network
applications such as video streaming or autonomous
|     |     |     |     |     |     |     |     | performance.  |     | Reinforcement  |     | Learning  |     | (RL)  has  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | --- | --------- | --- | ---------- |
systems [14]. Also, conventional Software-Defined
attracted a lot of attention in recent years being one
| Networking  | (SDN) architectures  |     |     |     | are  | designed  | to  |     |     |     |     |     |     |     |
| ----------- | -------------------- | --- | --- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
of the most efficient methods of solving complex
configure resource allocation by static policies that
|     |     |     |     |     |     |     |     | optimization  |     | problems  | in  | the  field  | of  | network  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | --- | ----------- | --- | -------- |
do not adapt to the dynamicity of network traffic. The
|     |     |     |     |     |     |     |     | management.  |     | RL  algorithms  |     | allow  | the  | system  to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------------- | --- | ------ | ---- | ----------- |
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025           DOI: 10.22266/ijies2025.0630.25

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received: March 23, 2025. Revised: April 13, 2025. 351
learn the optimal behaviors by trial and error, which [7], or implementation of Fog Computing to provide
leads to them being a great match for environments low latency [6], and have not used the combination of
that are dynamic and hard to predict [22]. Abstract In these technologies. While this modularity boosts the
network optimization, reinforcement learning (RL) overall robustness, it also limits networks from
has been employed in optimization problems such as reaching maximum adaptability and performance as
traffic routing, load balancing, and resource necessary reinforcements remain scattered and
allocation. For example, Li et al. showed through segregated. The second gap is in lack of practical
extensive experiments that using deep reinforcement frameworks combining SDN, Fog Computing, and
learning (DRL) to optimize resource allocation in RL. Although there are proposed theoretical models,
SDN-based IoT networks outperforms existing few studies have shown that these models can be
solutions based on theorem, mathematics, etc [23]. implemented and evaluated [28]. Furthermore, there
Similarly, Boutaba et al. provide an extensive survey is an absence of holistic solutions, as none solve for
on networking machine learning and demonstrate major challenges like latency, resource allocation,
how RL can improve the autonomy and decision and recursiveness concurrently. Some frameworks,
making process in networking [24]. Network for instance, do not account for the dynamic nature
optimization with RL goes beyond resource of network traffic and therefore propose static
allocation. Research has demonstrated the application policies that are unable to adapt to varying conditions.
of RL for traffic forecasting, and how it can be used The shortcomings mentioned spotlight the urgency
to dynamically adjust network configurations based for pioneering research that integrates SDN, Fog
on varying needs [25]. For instance, the study [4] Computing, and RL into a single comprehensive
presented an RL-based framework to traffic framework that can tackle the challenges of
management in 5G networks and achieved contemporary networks. This research aims to fill in
considerable latency and throughput improvements. the aforementioned gaps to help advance intelligent
Although showing great potential, the integration of network architectures moving towards next-
RL into existing network paradigms stays a non- generation technologies such as IoT, 5G/6G and
trivial challenge. Numerous works treat RL in smart city applications. In summary, Table 1 captures
isolation without considering its value with new several new studies related to SDN, FC, Fog
technologies such as SDN and Fog Computing. This Computing, Rl and their challenges, parameters,
research gap points a direction to leverage synergies limitations and range of applications [24]. It
between RL, SDN and Fog Computing for highlights the existing challenges in SDN like the
intelligent and adaptive management of networks [3]. problems of latency and resource utilization and it
Despite the advances in SDN, Fog Computing, and also brings forward the concept of Fog Computing in
RL, there are still some gaps in the existing literature. to minimize latency and enhance real-time decision-
A key deficiency here is the absence of integration making The table also shows RL can solve more
among such technologies to allow near real-time complex optimization issues, for example, in the
decision making in fast changing network areas of resource reduction and advanced adaptive
landscapes. Previous research mostly concentrates on routing such as the traffic routing. However, much
the utilization of each component alone, remains to be done – especially in the integration of
implementation of RL for resource allocation in SDN
Table 1. Comparison of Existing Research on Network Optimization Technologies
Study Problem Addressed Parameters Considered Limitations Application Area
SDN Centralized architecture Latency: 45–50 ms, Static policies fail to Cloud computing,
Challenges [11, leads to high latency Resource Utilization: 65% adapt; limited scalability 5G/6G, IoT
12]
Fog Computing Reducing latency and Latency: Reduced by 30%, Limited coordination Smart cities,
[19, 20] improving real-time Energy Efficiency: Improved with SDN controllers industrial IoT
decision-making by 20%
RL in Complex optimization Latency Reduction: 15%, Isolated applications of Network
Networking [7, problems Resource Utilization: 70% RL; lacks integration automation, 5G
8] with SDN/Fog networks
Proposed High latency, Latency: Reduced by 40%, Requires computational IoT, 5G/6G, smart
Framework inefficient resource Energy Efficiency: Improved resources for RL cities
allocation by 25%, Resource
Utilization: 85%
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025 DOI: 10.22266/ijies2025.0630.25
This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received:  March 23, 2025.     Revised: April 13, 2025.                                                                                                   352
these technologies into adaptive, scalable solutions to
build modern networks such as IoT, 5G/6G and smart
| cities.   | The       | following  |            | synthesis  | of related  | work        |     |     |     |     |     |     |     |
| --------- | --------- | ---------- | ---------- | ---------- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| provides  | insights  |            | into  the  | necessity  | of          | a  unified  |     |     |     |     |     |     |     |
framework integrating SDN, Fog Computing, and RL
to fill in the gaps of existing work and boost the
performance of the networks.
3.  Methodology
This structure stands out from others through its
singular execution of SDN with Fog Computing and
| Reinforcement  |     | Learning  |     | working  | as  one  | unified  |     |     |     |     |     |     |     |
| -------------- | --- | --------- | --- | -------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
design. The current research presents unprecedented
integration of SDN together with Fog Computing and
| Reinforcement  |     | Learning  |     | as  a  | unified  | solution  to  |     |     |     |     |     |     |     |
| -------------- | --- | --------- | --- | ------ | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
overcome three core issues related to latency and
| resource  |     | management  |     | along  | with  | system  |     |     |     |     |     |     |     |
| --------- | --- | ----------- | --- | ------ | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
responsiveness.  The  traditional  SDN  architecture  Figure. 2 Research methodology flow chart

| experience   |     | behavior  |         | limitations     | because  | of    |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ------- | --------------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| centralized  |     | control   | system  | implementation  |          | thus  |     |     |     |     |     |     |     |
facing challenges in large-scale networks [1]. Fog  𝑃 𝑘  : Priority level of application 𝑘.
Computing  operates  independently  without  The  objective  feature  of  resource  allocation
automated  routing  optimization  unless  intelligent  adaptation is defined as reducing the weighted yoga
decision  systems  are  applied.  The  proposed  for delay and resource use:
| framework applies Q-Learning and Proximal Policy  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Optimization (PPO) to complete better performance  ∑𝑁  ∑𝑁 𝑅𝑘    (1)
|     |     |     |     |     |     |     | Minimize𝑍 |     | =   |     |  𝑤 ⋅𝐿 | +𝑤 ⋅    |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ----- | ------- | --- |
|     |     |     |     |     |     |     |           |     | 𝑖=1 | 𝑗=1 | 1     | 𝑖𝑗 2 𝐶𝑖 |     |
by reduction latency by 40% and advancing energy

efficiency by 25% and resource utilization realization
Where:
85%. The joint execution enables the framework to
𝑤  : Weight factor for latency.
| efficiently manage data at its source points while it  |     |     |     |     |     |     | 1   |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑤  : Weight factor for resource utilization.
| concurrently modifies its performance based on real- |     |     |     |     |     |     | 2     |          |             |     |       |              |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | -------- | ----------- | --- | ----- | ------------ | --- |
|                                                      |     |     |     |     |     |     | This  | formula  | guarantees  |     | that  | the  system  |     |
time network replaces
|       |     |        |                 |     |          |           | emphasizes  | low-latency  |     | routes  | while  | effectively  |     |
| ----- | --- | ------ | --------------- | --- | -------- | --------- | ----------- | ------------ | --- | ------- | ------ | ------------ | --- |
| Fig.  | 2   | shows  | the  Flowchart  |     | of  the  | Research  |             |              |     |         |        |              |     |
making use of the resources at hand. The weights w_1
Methodology The framework is structured as a three-
|     |     |     |     |     |     |     | and  w_2  | are  modified  |     | in  | real  time  | according  | to  |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | --- | ----------- | ---------- | --- |
layer architecture:
current network conditions through the use of RL
| 1.  | SDN  | Controller:  |     | It  | is  the  brain  | of  the  |     |     |     |     |     |     |     |
| --- | ---- | ------------ | --- | --- | --------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
algorithms.
network acting as a control center to manage
Step 1: Dataset Description
global policies and coordination with one
|     |     |     |     |     |     |     | Framework  |     | was  | produced  | using  | a  dataset  | -   |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | --------- | ------ | ----------- | --- |
another fog nodes.
synthetic network traffic data used for training and
| 2.  | Fog  | Nodes:  | Distributed  |     | processing  | units  |     |     |     |     |     |     |     |
| --- | ---- | ------- | ------------ | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
testing. The dataset includes:
|     | serving  |     | local  | computations to  |     | the  |     |     |     |     |     |     |     |
| --- | -------- | --- | ------ | ---------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
Network Topology:
customers, which can offload the tasks from
Simulated using Mininet, with varying numbers
the SDN controller, thus reducing latency
of switches, routers, and end devices.
and bandwidth consumption.
Traffic Patterns:
3.  RL Algorithms: Allow for smart decision-
|     |     |     |     |     |     |     | Generated  |     | using  | custom  | Python  | scripts  | to  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | ------- | ------- | -------- | --- |
making systems for traffic routing, resource
simulate IoT, 5G/6G, and smart city scenarios.
allocation, and load balancing.
Resource Demands:
| To  | model  | the  | framework  |     | mathematically,  | we  |     |     |     |     |     |     |     |
| --- | ------ | ---- | ---------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Randomly assigned to applications based on their
define the following variables:
priority levels (Pk).
𝑁 : Total number of nodes in the network.
|     |     |     |     |     |     |     | The  | relevant  | parameters  |     | employed  | in  | the  |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | ----------- | --- | --------- | --- | ---- |
𝐹 : Number of fog nodes.
|     |     |     |     |     |     |     | simulation  | environment  |     | are depicted  |     | in  Table  | 2,  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ------------- | --- | ---------- | --- |
𝐶 : Computational capacity of fog node 𝑖.
𝑖
which includes the total number of nodes, fog nodes,
𝐿  : Latency between node 𝑖 and node 𝑗.
|     | 𝑖𝑗  |     |     |     |     |     | latency, demands of resources, and priority levels.   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
𝑅  : Resource demand of application 𝑘.
|     | 𝑘   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025           DOI: 10.22266/ijies2025.0630.25

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received:  March 23, 2025.     Revised: April 13, 2025.                                                                                                   353
Table 2. Network Parameters and Ranges  Step 2: Tools and Platforms
Parameter  Description  Range  The  following  devices  were  used  for
| Number of Nodes (N)  | Total nodes in the     | 50–    | implementation:                               |     |     |     |     |     |     |
| -------------------- | ---------------------- | ------ | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                      | network                | 200    | 1. Mininet: Imitation of the SDN environment  |     |     |     |     |     |     |
| Number of Fog        | Fog nodes deployed in  | 10–50  |                                               |     |     |     |     |     |     |
including switch, squares and end units.
| Nodes (F)  | the network  |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
2. Tensorflow/Pytorch: The RL algorithm was
| Latency (Lij)  | Latency between  | 1–50  |     |     |     |     |     |     |     |
| -------------- | ---------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
implemented for traffic routing and resource
|     | nodes  | ms  |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
allocation.
| Resource Demand  | Resource demand per  | 1–100  |               |     |            |      |        |      |        |
| ---------------- | -------------------- | ------ | ------------- | --- | ---------- | ---- | ------ | ---- | ------ |
|                  |                      |        | 3.  IFOGSIM:  |     | simulated  | fog  | knots  | and  | their  |
| (Rk)             | application          | units  |               |     |            |      |        |      |        |
interactions with SDN checks.
| Priority Level (Pk)  | Priority weight for  | 1–5  |     |     |     |     |     |     |     |
| -------------------- | -------------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Step 3: Algorithms Used in the Study
each application
|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Algorithm 1: Q-Learning for Traffic Routing

These parameters outline the type and size of the  Q-Learning  is  a  strengthening  learning  algorithm
experiments  performed  with  the  framework.  This  used to optimize traffic routing decisions. Below is
table defines ranges for each parameter used in the  the complete algorithm:
underlying experiment to guarantee reproducibility  Input: Network topology, traffic patterns, resource
| and clarity of the experimental setup. Traffic Routing  |     |     | demands.  |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
using Q-Learning: Flowchart, see Fig. 3.  Output: Optimal routing policy.
|     |     |     | 1.  Initialize Q-Table: Generate a Q-table where  |            |     |         |      |               |     |
| --- | --- | --- | ------------------------------------------------- | ---------- | --- | ------- | ---- | ------------- | --- |
|     |     |     | noises                                            | represent  |     | states  | (s)  | and  columns  |     |
represent actions (a). Initialize all Q-values to
zero.
|     |     |     | 2.  Define  | State  | Space:  |     | Each  | state  | st  is  |
| --- | --- | --- | ----------- | ------ | ------- | --- | ----- | ------ | ------- |
represented by the current network conditions,
including:
- Current traffic load.
- Available resources at fog nodes.
- Latency between nodes.
|     |     |     | 3.  Define  | Action  | Space:     |              | Actions      | at        | include  |
| --- | --- | --- | ----------- | ------- | ---------- | ------------ | ------------ | --------- | -------- |
|     |     |     | selecting   |         | paths      | for  packet  |              | routing.  | For      |
|     |     |     | example,    |         | if  there  | are          | M  possible  |           | paths    |
between two nodes, the action space has M
elements.
|     |     |     | 4.  Reward  |     | Function:  | Define  |     | the  | reward  |
| --- | --- | --- | ----------- | --- | ---------- | ------- | --- | ---- | ------- |
function rt as:

|     |     |     | 𝑟 = 𝑤 | ⋅Δ𝐿+𝑤 | ⋅Δ𝑈   |     |     |     |  (2)  |
| --- | --- | --- | ----- | ----- | ----- | --- | --- | --- | ----- |
|     |     |     | 𝑡 1   |       | 2     |     |     |     |       |

Where:
Δ𝐿 : Reduction in latency achieved by the
selected action.
|     |     |     | Δ𝑈  :  | Improvement  |     | in  | resource  | utilization  |     |
| --- | --- | --- | ------ | ------------ | --- | --- | --------- | ------------ | --- |
achieved by the selected action.

|     |     |     | 5  Q-Learning  |      | Update             | Rule:  | Update  |        | the  Q- |
| --- | --- | --- | -------------- | ---- | ------------------ | ------ | ------- | ------ | ------- |
|     |     |     | value          | for  | each state-action  |        | pair    | using  | the     |
following rule:

|     |     |     | 𝑄(𝑠 ,𝑎 )= | 𝑄(𝑠        | ,𝑎 )+   |         |     |                  |     |
| --- | --- | --- | --------- | ---------- | ------- | ------- | --- | ---------------- | --- |
|     |     |     | 𝑡 𝑡       |            | 𝑡 𝑡     |         |     |                  |     |
|     |     |     | 𝛼⋅[𝑟      | +𝛾⋅max 𝑄(𝑠 |         | ,𝑎)−𝑄(𝑠 |     | ,𝑎 )]       (3)  |     |
|     |     |     | 𝑡+1       |            |         | 𝑡+1     |     | 𝑡 𝑡              |     |
𝑎

|     |     |     | Where:  |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
Figure. 3 Q-Learning for Traffic Routing flowchart  𝛼 : Learning rate (set to 0.1 in this study).
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025           DOI: 10.22266/ijies2025.0630.25

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received: March 23, 2025. Revised: April 13, 2025. 354
𝛾 : Discount factor (set to 0.9 in this study). Algorithm 2: Deep Q-Network (DQN) for
6 Policy Selection: Use an 𝜖-greedy policy to Resource Allocation
balance exploration and exploitation: Deep Q-Networks (DQNs) extend Q-Learning by
With probability 𝜖, select a random action using neural networks to approximate the Q-function.
(exploration). Below is the complete algorithm:
With probability 1−𝜖, select the action with Input: Network topology, traffic patterns, resource
the highest Q -value (exploitation). demands.
7 Iterate Until Convergence: Repeat steps 2–6 Output: Optimal resource allocation policy.
until the Q-values converge or a predefined 1. Initialize Neural Networks: Create two
number of iterations is reached. neural networks:
8 Extract Optimal Policy: Once the Q-table • Main Network: Approximates the Q-
converges, extract the optimal policy by function 𝑄(𝑠,𝑎;𝜃).
choosing the act with the highest Q-value for
• Target Network: Provides stable targets for
each state. training, parameterized by 𝜃−.
Fig. 4 presents the Deep Q-Network (DQN)
architecture.
2. Define Replay Buffer: Store experiences
( 𝑠 ,𝑎 ,𝑟 ,𝑠 ) in a replay buffer to break
𝑡 𝑡 𝑡+1 𝑡+1
temporal correlations.
3. Define Loss Function: Use the Mean Squared
Error (MSE) loss function:
𝐿(𝜃)= 𝔼[(𝑟 +𝛾⋅max 𝑄(𝑠 ,𝑎;𝜃−)−
𝑡+1 𝑡+1
𝑎
2
𝑄(𝑠 ,𝑎 ;𝜃)) ] (4)
𝑡 𝑡
4. Training Loop:
• Taster a batch of involvements from the
replay buffer.
• Compute the target Q-value:
𝑦 = 𝑟 +𝛾⋅max 𝑄(𝑠 ,𝑎;𝜃−) (5)
𝑡 𝑡+1 𝑡+1
𝑎
• Update the main network parameters 𝜃
using gradient descent to minimize the loss
𝐿(𝜃).
5. Update Target Network: Periodically update
the target network parameters 𝜃−by copying
them from the main network:
𝜃− = 𝜏⋅𝜃+(1−𝜏)⋅𝜃− (6)
Where τ is the soft update rate (set to 0.01 in this
study).
6. Iterate Until Convergence: Repeat steps 3–5
until the network's performance stabilizes or
a predefined number of episodes is reached.
The RL algorithms received precise adjustments
to their hyperparameters to reach their best possible
Figure. 4 Deep Q-Network (DQN)
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025 DOI: 10.22266/ijies2025.0630.25
This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received:  March 23, 2025.     Revised: April 13, 2025.                                                                                                   355
Input: Network topology, traffic patterns, resource
demands.
Output: Optimal dynamic adaptation policy.
1.  Initialize Policy Network: Create a neural
|     |     |     |     |     |     |     | network  | 𝜋 (𝑎 ∣ 𝑠) |  that  |     | outputs  the  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------ | --- | ------------- |
𝜃
probability distribution over actions given a
state.
|     |     |     |     |     |     | 2.  | Gather  | Trajectories:  | Interrelate  |     | with  the  |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | ------------ | --- | ---------- |
setting using the current policy to collect
|     |     |     |     |     |     |     | trajectories ( 𝑠 | ,𝑎 ,𝑟 | ,𝑠  |  ).  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ----- | --- | ---- | --- |
|     |     |     |     |     |     |     |                  | 𝑡 𝑡   | 𝑡+1 | 𝑡+1  |     |
3.  Compute Advantage Function: Calculate the
𝐴ˆ
|     |     |     |     |     |     |     | advantage  | function  |     |  using  | Generalized  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | ------- | ------------ |
𝑡
Advantage Estimation (GAE):

|     |     |     |     |     |     | 𝐴ˆ  | ∑∞  (𝛾𝜆)𝑙𝛿 |                                 |     |     |       |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------------------- | --- | --- | ----- |
|     |     |     |     |     |     | =   |            |                                 |     |     |  (7)  |
|     |     |     |     |     |     | 𝑡   | 𝑙=0        | 𝑡+𝑙                             |     |     |       |

Where:
|     |     |     |     |     |     | 𝛿 = | 𝑟 +𝛾⋅𝑉(𝑠 | )−𝑉(𝑠 |     | ) : Temporal  |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --- | ------------- | --- |
|     |     |     |     |     |     | 𝑡   | 𝑡        | 𝑡+1   | 𝑡   |               |     |
difference error.
𝑉(𝑠 𝑡 ) : Value function approximated by a
separate neural network.
4.  Define Objective Function: Use the clipped
surrogate objective function:

|     |     |     |     |     |     | 𝐿𝐶𝐿𝐼𝑃(𝜃) | = 𝔼                                                                         | [min(𝑟(𝜃)𝐴ˆ | ,clip (𝑟(𝜃),1− |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --------------------------------------------------------------------------- | ----------- | -------------- | --- | --- |
|     |     |     |     |     |     |          |                                                                             | 𝑡 𝑡         | 𝑡              |     | 𝑡   |
|     |     |     |     |     |     | 𝜖,1+𝜖)𝐴ˆ | )]                                                                     (8)  |             |                |     |     |
𝑡

Where:
|     |     |     |     |     |     |        | 𝜋𝜃  | (𝑎𝑡∣𝑠𝑡 )                         |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | -------------------------------- | --- | --- | --- |
|     |     |     |     |     |     | 𝑟 (𝜃)= |     | : Probability ratio between the  |     |     |     |
𝑡
|     |     |     |     |     |     |     | 𝜋𝜃old  | (𝑎𝑡∣𝑠𝑡 ) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | --- | --- |
new and old policies.
𝜖 : Clipping parameter (set to 0.2 in this study).
|     |     |     |     |     | 5.  | Update                                         | Policy  | Network:  |     | Update  | the  policy  |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------- | ------- | --------- | --- | ------- | ------------ |
|     |     |     |     |     |     | network parameters θ using gradient ascent to  |         |           |     |         |              |
Figure. 5 Proximal Policy Optimization (PPO)  maximize L CLIP (θ).

|     |     |     |     |     | 6.  | Iterate                                         | Until  | Convergence:  |     | Repeat  | steps  2–5  |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------- | ------ | ------------- | --- | ------- | ----------- |
|     |     |     |     |     |     | until the policy's performance stabilizes or a  |        |               |     |         |             |
results. Initial testing determined 0.1 as the value for
predefined number of iterations is reached.
the Q-Learning learning rate (α) while the discount

factor  (γ)  was  set  to  0.9.  The  Proximal  Policy  The  test scenarios  designed  to  validate  the
Optimization model implemented 0.2 for its clipping
framework are described in detail in Table 3. The
parameter along with τ set to 0.01 as the soft update  document describes  the  network  topology,  traffic
| rate.  The  system  | used  grid  | search  | and  | Bayesian  |     |     |     |     |     |     |     |
| ------------------- | ----------- | ------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
patterns and evaluated metrics for each scenario (IoT
optimization approaches to systematically evaluate  networks,  5G/6G  networks  and  smart  city
| many  values  | in  hyperparameter  |     | tuning.  | The  |     |     |     |     |     |     |     |
| ------------- | ------------------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
applications). As illustrated by the table, the settings
framework  obtained  its  optimal  exploratory  and  in which the framework was applied are diverse,
| exploitative  | characteristics  |     | through  | these  |     |     |     |     |     |     |     |
| ------------- | ---------------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
making its testing robust and impeding identification
optimizations as Fig. 5 shows.  of challenges associated with environmental factors.

We have empirically validated the framework in a
Algorithm 3: Proximal Policy Optimization  simulated environment that mimics realistic network
(PPO) for Dynamic Adaptation  conditions.  Network  topologies,  including  IoT
|     |     |     |     |     | networks,  |     | 5G/6G  | networks,  |     | and  | smart  city  |
| --- | --- | --- | --- | --- | ---------- | --- | ------ | ---------- | --- | ---- | ------------ |
Proximal Policy Optimization (PPO) is a strategy
gradient technique used for continuous control tasks.  applications were set up in the testing environment.
| Below is the complete algorithm:  |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025           DOI: 10.22266/ijies2025.0630.25

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received:  March 23, 2025.     Revised: April 13, 2025.                                                                                                   356
Table 3. Experimental Scenarios and Evaluation Metrics
Scenario  Network Topology  Traffic Pattern Type  Evaluation Metrics
IoT Networks  100 nodes, 20 fog  Periodic sensor data updates  Latency, Energy Efficiency,
|     |     |     |     | nodes  |     |     |     |     |     | Packet Delivery Ratio  |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- |
5G/6G Networks  150 nodes, 30 fog  High-bandwidth video streaming  Latency, Energy Efficiency,
|     |     |     |     | nodes  |     | & AR traffic  |     |     |     | Packet Delivery Ratio  |     |     |     |
| --- | --- | --- | --- | ------ | --- | ------------- | --- | --- | --- | ---------------------- | --- | --- | --- |
Smart City Applications  200 nodes, 50 fog  Mixed traffic: video surveillance,  Latency, Energy Efficiency,
|     |     |     |     | nodes  |     | sensor alerts, traffic data  |     |     |     | Packet Delivery Ratio  |     |     |     |
| --- | --- | --- | --- | ------ | --- | ---------------------------- | --- | --- | --- | ---------------------- | --- | --- | --- |

The  following  metrics  were  used  to  validate the  traffic  is  still  as  realistic  as  possible  but
framework:  computationally efficient. The experiments were all
1 Latency (𝐿 ) : Measured as the time booked  run on a high performance computing (HPC) cluster
𝑖𝑗
with an NVIDIA Tesla V100 GPU, 128 GB of RAM
|     | for  | data  packets  |     | to  travel  | from  | source  to  |     |     |     |     |     |     |     |
| --- | ---- | -------------- | --- | ----------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
destination.  and a 32-core Intel Xeon CPU. We heavily relied on
GPU acceleration to speed up the deep reinforcement
|     | 2 Energy  | Efficiency:  |     | Calculated  | as  | the  total  |     |     |     |     |     |     |     |
| --- | --------- | ------------ | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
power consumed by fog nodes and end devices.  learning models training, allowing us to explore a
|     |           |           |     |         |          |          | wide  range  |     | of  experiments  |     | in a  | timely  | manner.  |
| --- | --------- | --------- | --- | ------- | -------- | -------- | ------------ | --- | ---------------- | --- | ----- | ------- | -------- |
|     | 3 Packet  | Delivery  |     | Ratio:  | Defined  | as  the  |              |     |                  |     |       |         |          |
percentage of successfully delivered packets.  Mininet was used to simulate the SDN environment
|     |     |     |     |     |     |     | as  it  provides a  |     | flexible  |     | platform to  |     | test  various  |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --------- | --- | ------------ | --- | -------------- |
The Eq. 9 ensures reliable network performance
by measuring the success rate for data transfer. The  network topologies like switches, routers, and end
package distribution ratio is calculated:  devices. IFogSim, known tool for fog computing
environment emulation were used to emulate fog

 Packet Delivery Ratio =   nodes.  TensorFlow  and  PyTorch  —  For
|     |                               |     |     |                                      |     |     | implementing  |     | reinforcement  |     | learning  |     | algorithms,  |
| --- | ----------------------------- | --- | --- | ------------------------------------ | --- | --- | ------------- | --- | -------------- | --- | --------- | --- | ------------ |
|     |  Number of Packets Delivered  |     |     | ×100                            (9)  |     |     |               |     |                |     |           |     |              |
 Total Number of Packets Sent  with  both  providing  powerful  frameworks  for
|     |     |     |     |     |     |     | building and training neural networks. These tools  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
In order to validate the synthetic dataset used in
selected according to the compatibility, scalability,
this study, a comprehensive validation process was  and handling the complex computation to train RL
carried out. To create the dataset, custom python
models. The simulation environment had to be tested
scripts were used to simulate realistic network traffic  for  its  stability  and  reproducibility  before  the
patterns for devices, such as IoT sensors, 5G/6G
experiments are run. Over many iterations of the
video streaming, and smart city surveillance systems.  same  scenario,  these  were run  to  check  for
The patterns were fine-tuned χ using popular publicly
repeatability, for example. In the case of simulation
accessible  data  set  i.e.  CAIDA  Internet  Traffic  parameters, they were tuned dynamically to imitate
Dataset and The IoT Network Intrusion Data set
|     |     |     |     |     |     |     | actual  | variation  | of  | network  | conditions  |     | for  these  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | -------- | ----------- | --- | ----------- |
which are well-established datasets in the area of  factors for example bandwidth, latency and resource
representation of actual network conditions [13-15].
|     |     |     |     |     |     |     | demands.  | Besides,  |     | Since  | the  performance  |     | of  the  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ------ | ----------------- | --- | -------- |
To ensure representation of the collected data, the
|                 |     |                  |           |                     |            |          | reinforcement  |          | learning  |             | algorithms (Q-Learning,  |            |            |
| --------------- | --- | ---------------- | --------- | ------------------- | ---------- | -------- | -------------- | -------- | --------- | ----------- | ------------------------ | ---------- | ---------- |
| statistical     |     | characteristics  |           | of  the             | synthetic  | data,    |                |          |           |             |                          |            |            |
|                 |     |                  |           |                     |            |          | DQN,           | and      | PPO)      | are  quite  | sensitive                |            | to  hyper  |
| including       |     | packet           | size      | and  inter-arrival  |            | time     |                |          |           |             |                          |            |            |
|                 |     |                  |           |                     |            |          | parameter      | tuning.  | We        | trained     | each                     | algorithm  | for        |
| distributions,  |     | were             | compared  | with                | those      | of  the  |                |          |           |             |                          |            |            |
10,000 episodes and compared its convergence using
| reference  |     | datasets.  | This  | validation  | process  | both  |                  |     |      |          |          |     |            |
| ---------- | --- | ---------- | ----- | ----------- | -------- | ----- | ---------------- | --- | ---- | -------- | -------- | --- | ---------- |
|            |     |            |       |             |          |       | loss  functions  |     | and  | rewards  | curves.  |     | To  avoid  |
bolstered  the  realism  of  the  synthetic  data  and  overfitting  and  also  ensure  that  the  models
| allowed  |     | the  performance  |     | of  the  | framework  | to  |                   |     |     |                |     |             |     |
| -------- | --- | ----------------- | --- | -------- | ---------- | --- | ----------------- | --- | --- | -------------- | --- | ----------- | --- |
|          |     |                   |     |          |            |     | generalized well  |     | to  | out-of-sample  |     | scenarios,  | we  |
generalise  to  different  types  of  network  implemented early stopping mechanisms. Then for
| environments.  |     | Other  | factors  | considered  |     | were  the  |             |     |                |     |          |      |                |
| -------------- | --- | ------ | -------- | ----------- | --- | ---------- | ----------- | --- | -------------- | --- | -------- | ---- | -------------- |
|                |     |        |          |             |     |            | Q-Learning  |     | the  learning  |     | rate  α  | was  | 0.1  and  the  |
scalability of  the  dataset.  It  was  tested  for  the  discount factor γ 0.9. These values were selected
framework through small scale networks, consisting
based on initial experiments to achieve an optimal
of 50 nodes to large scale networks, consisting of  trade-off between exploration and exploitation. First,
200 nodes This strategy enabled us to assess the
|     |     |     |     |     |     |     | an  ε-greedy  |     | policy  | was  | utilized,  | using  | an  initial  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ---- | ---------- | ------ | ------------ |
scalability of the framework and verify that it can  exploration ratio of 0.2 that decayed exponentially
| robustly  |     | accommodate  |     | highly  | dynamic  | and  |                    |     |     |             |               |     |            |
| --------- | --- | ------------ | --- | ------- | -------- | ---- | ------------------ | --- | --- | ----------- | ------------- | --- | ---------- |
|           |     |              |     |         |          |      | over  episodes to  |     |     | facilitate  | exploitation  |     | in  later  |
heterogeneous  scenarios.  We  configure our  episodes. Likewise, we added a replay buffer with a
| simulation  |     | environment  |     | where  | the  implemented  |     |           |         |              |     |     |           |            |
| ----------- | --- | ------------ | --- | ------ | ----------------- | --- | --------- | ------- | ------------ | --- | --- | --------- | ---------- |
|             |     |              |     |        |                   |     | size  of  | 10,000  | experiences  |     | in  | order to  | stabilize  |
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025           DOI: 10.22266/ijies2025.0630.25

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received: March 23, 2025. Revised: April 13, 2025. 357
training by breaking correlations with past showcased by deploying it in simulated settings
experiences for DQN. For the soft update τ of target modeling realistic scenarios such as IoT networks,
network, we used 0.01, meaning the main networks 5G/6G venues and smart city applications. As an
will synchronize with the target network over a long example, in the IoT scenario, the framework was
time. Lastly, we used a clipping parameter ε of 0.2 evaluated for a network consisting of 100 nodes and
and a discount factor γ of 0.99 in PPO to encourage 20 fog nodes in which sensors periodically send
long-term rewards. A mini-batch size of 64 was updates. Using a network of 150 nodes and 30 fog
leveraged for compute efficiency and policy updates nodes, simulating high-bandwidth applications like
were done every 4,096 timesteps. A thorough video stream and augmented reality in the 5G/6G
statistical analysis was performed in order to verify scenario, the framework was subsequently tested.
the results. For each of the scenarios (IoT, 5G/6G, These experiments validated the ability of the
smart cities), the key performance metrics, such as framework to decrease latency and improve energy
reduction of latency, energy efficiency, and packet efficiency and resource utilization in realistic
delivery ratio were computed. To ensure that conditions. In addition, the adaptability of the
observed improvements were not random, paired t- framework was evaluated via real-life scenarios by
tests and ANOVA were conducted to assess making unexpected changes in network situations
statistical significance. For example, the proposed (e.g., traffic spikes and hardware failures). The
framework achieved a 30–40% decrease in latency framework proved to successfully adapt its policies
compared to traditional SDN architectures, and this in real time so that its performance remained stable,
was statistically significant (p < 0.01). In a similar indicating potential for implementation in ever-
manner, confidence intervals and variance analysis changing environments.
confirmed the 25% drop in energy consumption, and
the 10% increase in packet delivery ratio. 4. Results and analysis
Performance trends over the various scenarios were
The proposed framework succeeds its
illustrated via line charts or bar graphs. The
effectiveness through tentative evidence presented in
visualisation were cover such information visually
this section which demonstrates outperformance
where it became more intuitive to see the effect of
versus standard SDN designs and existing solutions.
the framework that I proposed. As an example, two
The examination of different frameworks using Table
plots were plotted: a line chart was drawn to
4 reveals that the proposed framework brings about
demonstrate the reduction in latency with the
latency reductions which reach 40% for IoT networks
increasing number of fog nodes and a bar graph was
and 5G/6G environments as well as smart city
utilized to compare the packet delivery ratios of the
applications. The proposed framework demonstrates
proposed framework along with the baseline methods.
enhanced energy efficiency according to Table 5
Although the findings are promising, a few aspects of
because it decreases power usage by 25%. Results in
the study should be noted. One: The use of synthetic
Table 6 indicate that the proposed system achieves
data has been validated against real-word traces, but
resource utilization rates of 85% compared to
synthetic data may not accurately capture all aspects
traditional SDN architecture rates at 65%. Statistical
of real-world networks. Testing the framework in on-
tests of paired t-tests and ANOVA verify that the
ground systems or live setups would be the possible
measured improvements achieve statistical
next work or implementation using real-time data
significance at the p<0.01 level. Figs. 6 to 8 visually
from IoT deployments. Second, the framework was
demonstrate how the framework manages dynamic
tested for scalability up to 200 nodes additionally, for
workloads while adapting to real-time
even larger-scale networks with higher
computational needs additional optimizations will be
needed. A second restriction is that fog nodes are
Table 4. Comparative Analysis of Latency Across
homogeneous, meaning that each node possesses a
Frameworks
computational capacity that is mostly similar to
Framework IoT 5G/6G Smart City
others of its type. In reality, fog nodes may give
Networks Networks Applications
different hardware capabilities and energy limitations. (ms) (ms) (ms)
This heterogeneity might be an interesting avenue for Traditional 45 38 50
future research to tackle. Finally, though the SDN
framework outperformed on-grid-based synthesis Ryu Controller 40 32 45
domains, using it with the real human-robot Proposed 27 23 30
interaction will bring unexpected issues that should Framework
be solved. The utility of the proposed framework was Note: Lower values indicate better performance.
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025 DOI: 10.22266/ijies2025.0630.25
This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received:  March 23, 2025.     Revised: April 13, 2025.                                                                                                   358
Table 5. Energy Efficiency Comparison Across
Frameworks
| Framework  |           | IoT  | 5G/6G     |     | Smart City    |     |     |     |     |     |     |     |     |
| ---------- | --------- | ---- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|            | Networks  |      | Networks  |     | Applications  |     |     |     |     |     |     |     |     |
|            | (Watts)   |      | (Watts)   |     | (Watts)       |     |     |     |     |     |     |     |     |
Traditional
|     |     | 250  |     | 300  |     | 350  |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
SDN
Ryu
|     |     | 220  |     | 280  |     | 320  |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
Controller
Proposed
|     |     | 188  |     | 225  |     | 263  |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
Framework
Note: Lower power consumption indicates higher energy
efficiency.
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Table 6. Resource Utilization Rates Across Frameworks  Figure. 8 Resource Utilization Performance Comparison

| Framework  |     | IoT       |     | 5G/6G     |               | Smart City  |     |     |     |     |     |     |     |
| ---------- | --- | --------- | --- | --------- | ------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|            |     | Networks  |     | Networks  | Applications  |             |     |     |     |     |     |     |     |
(%)  (%)  (%)  adjustments by proving its performance in latency
Traditional SDN  65  70  60  and resource utilization and energy efficiency metrics.
| Ryu Controller  |     | 70  |     | 75  |     | 68  |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
An analytic approach based on data enables readers
Proposed  85  88  82  to understand completely the scientific value of this
Framework
research.
| Note:  Higher  | percentages  |     | indicate  |     | better  | resource  |                              |     |     |     |     |     |     |
| -------------- | ------------ | --- | --------- | --- | ------- | --------- | ---------------------------- | --- | --- | --- | --- | --- | --- |
| utilization.   |              |     |           |     |         |           | 4.1 Presentation of results  |     |     |     |     |     |     |

The proposed structure was evaluated in three
|     |     |     |     |     |     |     | separate  | network  | environments:  |     | IoT  | networks,  |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | -------------- | --- | ---- | ---------- | --- |
5G/6G Network and Smart City Application. The
|     |     |     |     |     |     |     | results  | were  | compared  | to  | traditional  |     | SDN  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --------- | --- | ------------ | --- | ---- |
architecture and condition -Art -art solutions to verify
the efficiency.
4.1.1. Latency reduction
Latency is a key benchmark for the performance
|     |     |     |     |     |     |     | of  real-time                                      | applications.  |                   | We  | plot          | the  evaluation  |          |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | -------------- | ----------------- | --- | ------------- | ---------------- | -------- |
|     |     |     |     |     |     |     | latency                                            | in  Fig.       | 1  for different  |     | frameworks.   |                  | Our      |
|     |     |     |     |     |     |     | proposed                                           | framework      | lowered           |     | the  average  |                  | latency  |
|     |     |     |     |     |     |     | every message takes to send and deliver getting a  |                |                   |     |               |                  |          |
Figure. 6 Comparative Analysis of Latency Across
40% comparison gain, taking it over traditional SDN
Frameworks
architectures. The integration of Fog Computing– so

|     |     |     |     |     |     |     | that data will be processed closer to the data source– |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
with RL algorithms to enhance the optimization of
|     |     |     |     |     |     |     | routing  | decisions  |     | dynamically  |     | reached  | an  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ------------ | --- | -------- | --- |
improvement on this Metric.
4.1.2. Energy efficiency
|     |     |     |     |     |     |     | Energy       | efficiency  |     | was      | measured  | as   | total  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | -------- | --------- | ---- | ------ |
|     |     |     |     |     |     |     | electricity  | consumed    |     | by  fog  | knots     | and  | final  |
equipment. The proposed structure demonstrated an
|     |     |     |     |     |     |     | improvement  | in               | the  | energy       | efficiency  | of    | 25%  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------------- | ---- | ------------ | ----------- | ----- | ---- |
|     |     |     |     |     |     |     | compared     | to  traditional  |      | approaches.  |             | This  | was  |
achieved by reducing fruitless components through
|     |     |     |     |     |     |     | adaptation  | of  resource  |     | allocation  | and  | RL-based  |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | ----------- | ---- | --------- | --- |

| Figure. 7 Energy Efficiency Across Different Network  |     |     |     |     |     |     | decisions.  |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Frameworks
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025           DOI: 10.22266/ijies2025.0630.25

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received:  March 23, 2025.     Revised: April 13, 2025.                                                                                                   359
4.1.3. Resource utilization  minimizes the compute load on centralized servers
and reduces total energy consumption.
| Resource  |     | use  was  | evaluated  | based  | on  the  |     |     |     |     |     |     |     |
| --------- | --- | --------- | ---------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
percentage of available resources effectively used  4.2.3. Enhanced resource utilization
during surgery. The proposed structure achieved an
Due to the implementation of novel strategies for
average use of resources of 85%, much higher than
65% achieved by traditional SDN architecture. This  node  coordination,  resource  utilization  of  a
framework which utilises such node coordination is
| improvement  |     | was  made  | possible  | by  | dynamic  |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
allocation of resources using RL –Sgorithms.   superior compared to the conventional techniques.
|     |     |     |     |     |     | • Real-Time  | Adaptability:  |     | RL-based  |     | algorithms  |     |
| --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | --------- | --- | ----------- | --- |
4.1.4. Energy consumption analysis  continuously monitor  the  network  traffic  and
dynamically allocate resources.
Model performance and power usage received
• This type of allocation is based on the priority
analysis through an energy consumption evaluation.
|     |     |     |     |     |     | level  | of  the  | application  | and  | serve  | to  | assign  |
| --- | --- | --- | --- | --- | --- | ------ | -------- | ------------ | ---- | ------ | --- | ------- |
The framework of the proposed method reflects 25%
resources in a more efficient manner.
better power efficiency compared to standard SDN
| configurations  |     | as  presented  |     | in  Fig.  | 7.  Local  |     |     |     |     |     |     |     |
| --------------- | --- | -------------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
4.3 Implications for real-world applications
| processing  | at  | Fog  points  | together  | with  | resource  |     |     |     |     |     |     |     |
| ----------- | --- | ------------ | --------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
allocation using Reinforcement Learning leads to this  •  Experimental  results  highlight  the  real-world
improvement  through  reducing  undesired  data  implementation  aspects  of  the  framework  in
movements while optimizing energy utilization. RL  today network settings. Key implications include:
algorithms  in  large-scale  networks  introduce  a  •  IoT  Networks:  Thanks  to  its  low-latency  and
moderate increase in power consumption throughout  energy-efficient characteristics, the framework is
their  computational  process.  The  forthcoming  well-suited  for  IoT  ecosystems  that  usually
research effort concentrates on designing minimal RL  involve devices with high power limitations.
models  with  enhanced  energy  protection  •  5G/6G  Networks:  Supporting  high-throughput,
performance capabilities.  ultra-low-latency  applications  such  as  video-
|     |     |     |     |     |     | streaming  | and  | autonomous  |     |     | systems,  | the  |
| --- | --- | --- | --- | --- | --- | ---------- | ---- | ----------- | --- | --- | --------- | ---- |
4.2 Analysis of results
|     |     |     |     |     |     | framework  | is  | the ideal  |     | solution  | for  | next- |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | --- | --------- | ---- | ----- |
generation networks.
4.2.1. Reduced latency
|     |     |     |     |     |     | •  Smart  | City  Applications:  |     |     | The  | framework  | can   |
| --- | --- | --- | --- | --- | --- | --------- | -------------------- | --- | --- | ---- | ---------- | ----- |

The significant reduction in latency achieved by
the  proposed  framework can  be  attributed  to  the  •  efficiently handle large-scale sensor networks for
traffic monitoring and surveillance systems due
following factors:
to its scalability and adaptability.
| • Fog  | Computing    | Integration:  |            | By  decentralizing  |               |     |     |     |     |     |     |     |
| ------ | ------------ | ------------- | ---------- | ------------------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| data   | processing,  | the           | framework  |                     | reduces  the  |     |     |     |     |     |     |     |
4.4 Comparative analysis with previous studies
reliance on centralized SDN controllers, thereby
| minimizing  |     | delays  | caused  | by  long-distance  |     |      |           |            |     |             |     |      |
| ----------- | --- | ------- | ------- | ------------------ | --- | ---- | --------- | ---------- | --- | ----------- | --- | ---- |
|             |     |         |         |                    |     | Our  | proposed  | framework  |     | expands on  |     | the  |
communication.  findings  from  studies  conducted  by  [1]  and  [7].
• RL-Based Routing Decisions: Algorithms like Q-
|     |     |     |     |     |     | Previous works  |     | were  | based  | on  | one  | or  two  |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ----- | ------ | --- | ---- | -------- |
Learning and Deep Q-Networks (DQN) enable the  components (i.e. use of RL for resource allocation
| framework  |     | to  select  | optimal  | paths  | for  packet  |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | -------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
and or use of Fog Computing for reducing latency);
routing, further reducing latency.  in contrast, this work combines SDN, Fog Computing
and RL into a holistic framework. The comparison is
4.2.2. Improved energy efficiency
|       |       |         |             |                   |     | summarized  | in       | Table 7.     |     | The      | performance  |           |
| ----- | ----- | ------- | ----------- | ----------------- | --- | ----------- | -------- | ------------ | --- | -------- | ------------ | --------- |
|       |       |         |             |                   |     | comparison  | of  the  | traditional  |     | SDN and  |              | the  Ryu  |
| This  | high  | energy  | efficiency  | of  the proposed  |     |             |          |              |     |          |              |           |
framework derives from:  Controller with the proposed framework is mentioned
in Figs. 6 to 8. In addition, the latency reduction
| • Efficient Resource  |     | Scheduling:  |     | RL  | algorithms  |     |     |     |     |     |     |     |
| --------------------- | --- | ------------ | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
analysis demonstrates that the proposed framework
forecast demand and schedule resources based on
|         |             |     |            |            |        | can  reduce  | average  | latency  |     | in  different  |     | network  |
| ------- | ----------- | --- | ---------- | ---------- | ------ | ------------ | -------- | -------- | --- | -------------- | --- | -------- |
| future  | workloads,  |     | resulting  | in  lower  | power  |              |          |          |     |                |     |          |
scenarios by an appreciable amount and thus is well-
wastage.
suited for time-sensitive applications such as IoT and
| • Computation  |     | Offloading:  |     | Fog           | nodes  are  |                 |            |         |             |              |             |             |
| -------------- | --- | ------------ | --- | ------------- | ----------- | --------------- | ---------- | ------- | ----------- | ------------ | ----------- | ----------- |
|                |     |              |     |               |             | smart  cities.  | The        | energy  | efficiency  |              | comparison  |             |
| responsible    |     | for  local   |     | computation,  | which       |                 |            |         |             |              |             |             |
|                |     |              |     |               |             | demonstrates    | lower      | energy  |             | consumption  |             | of  the     |
|                |     |              |     |               |             | proposed        | framework  | with    |             | respect      | to          | classical   |
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025           DOI: 10.22266/ijies2025.0630.25

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received:  March 23, 2025.     Revised: April 13, 2025.                                                                                                   360
Table 7. Comparative Analysis with Previous Studies
Study  Focus Area  Key Contribution  Limitation  Performance  Metrics
|     |     |     |     |     |     |     |     |     | (Proposed  |     | Framework  |     | vs.  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | --- | ---- |
Baseline)
 [1]  SDN  Introduced  OpenFlow  for  High  latency  in  Latency:  40%  reduction  vs.
Architecture  programmable  network  large-scale networks  traditional SDN
behavior
 [7]  RL  for  Demonstrated  DRL's  Limited  to  isolated  Energy  Efficiency:  25%
Resource  effectiveness  in  optimizing  RL applications  improvement vs. baseline
|     | Allocation  |     | resources  |     |     |     |     |     |     |     |     |     |     |
| --- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Propose Integrated  Unified  framework  Requires  Resource Utilization: 85% vs.
d  SDN,  Fog,  addressing  latency,  energy,  computational  65% (traditional SDN)
| Framew | and RL  |     | and resources  |     |     |     | resources for RL  |     |     |     |     |     |     |
| ------ | ------- | --- | -------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
ork

approaches, which can improve sustainability and  design  [9].  The  network  building  revolution  is
operational efficiency. As we can see in this figure  attainable recognizes to the framework's performing
the performance chart of resource utilization, and in  although it faces challenges with computational costs.
this chart, we can say that the resource utilization fair
5.  Conclusion
| rate  of  | our  proposed  |     | framework  |     | is  higher  | as  |     |     |     |     |     |     |     |
| --------- | -------------- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
compared to others, because the proposed framework
|     |     |     |     |     |     |     | In  | summary,  | this  | research  |     | introduced  | an  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | --------- | --- | ----------- | --- |
which uptake the resources in an efficient way by
|     |     |     |     |     |     |     | intelligent  | framework  |     | which  | combines  |     | Software- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | ------ | --------- | --- | --------- |
utilizing the intelligent decision making. The packet
|     |     |     |     |     |     |     | Defined  | Networking  |     | (SDN),  | Fog  Computing  |     | and  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ------- | --------------- | --- | ---- |
delivery ratio pie chart provides further confirmation
Reinforcement Learning (RL) that addresses certain
| that  the  | proposed  | framework  |     | achieves  | maximum  |     |         |            |          |     |             |     |             |
| ---------- | --------- | ---------- | --- | --------- | -------- | --- | ------- | ---------- | -------- | --- | ----------- | --- | ----------- |
|            |           |            |     |           |          |     | issues  | in modern  | network  |     | management  |     | like  high  |
packet success rate (95%) to make sure that the data
latency, non-optimal resource allocation and poor
transmission is stable and reliable. All these sorted
flexibility. By using Fog Computing closer to the data
results highlight the benefit of the integration of the
|     |     |     |     |     |     |     | source  | for  processing,  |     | the  | proposed  | framework  |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------------- | --- | ---- | --------- | ---------- | --- |
SDN, Fog Computing, and Reinforcement Learning
|     |     |     |     |     |     |     | mitigates  | latency  | issues,  | as  | well  as  | relieves  | the  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | -------- | --- | --------- | --------- | ---- |
for the optimization of the contemporary network
pressure of overloading the SDN controller in the
fields.
|      |           |            |     |     |               |      | cloud.               | By  leveraging  |     | RL   | algorithms,  |     | dynamic   |
| ---- | --------- | ---------- | --- | --- | ------------- | ---- | -------------------- | --------------- | --- | ---- | ------------ | --- | --------- |
| The  | proposed  | framework  |     |     | demonstrates  | its  |                      |                 |     |      |              |     |           |
|      |           |            |     |     |               |      | resource allocation  |                 |     | and  | intelligent  |     | resource  |
effectiveness by conducting an evaluation against
|     |     |     |     |     |     |     | provisioning  | and  | decision-making  |     |     | allow  | optimal  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | ---------------- | --- | --- | ------ | -------- |
existing technologies in the field. SDN relates to Fog
|     |     |     |     |     |     |     | performance  |     | under  | different  | workloads.  |     | Its  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | ---------- | ----------- | --- | ---- |
Computing through Reinforcement Learning (RL) to
|            |               |          |       |               |                |           | performance  |              | evaluation  | shows that  |                 | the  | novel  |
| ---------- | ------------- | -------- | ----- | ------------- | -------------- | --------- | ------------ | ------------ | ----------- | ----------- | --------------- | ---- | ------ |
| build      | a  framework  |          | that  | solves        | key  problems  |           |              |              |             |             |                 |      |        |
|            |               |          |       |               |                |           | framework    | outperforms  |             |             | the  classical  |      | SDN    |
| involving  | high          | latency  | and   | insufficient  |                | resource  |              |              |             |             |                 |      |        |
architecture by over 40% in latency, 25% in energy
| utilization  | and  | limited  | adaptability.  |     | Experimental  |     |     |     |     |     |     |     |     |
| ------------ | ---- | -------- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
efficiency, and achieves a resource utilization rate of
| experiments  | show  | a   | 40%  | shorter  | latency  | than  |            |          |            |     |                 |     |          |
| ------------ | ----- | --- | ---- | -------- | -------- | ----- | ---------- | -------- | ---------- | --- | --------------- | --- | -------- |
|              |       |     |      |          |          |       | 85%.  The  | results  | highlight  |     | the  potential  |     | of  the  |
conventional SDN systems because Fog Computing
framework for revolutionizing network architectures,
| performs  | local  | data  | managing  | together  | with  | RL- |     |     |     |     |     |     |     |
| --------- | ------ | ----- | --------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
offering solutions that are scalable, adaptable, and
based dynamic routing outcomes [3]. The overall
efficient to support emerging technologies such as
energy efficiency reaches 25% higher levels through
|     |     |     |     |     |     |     | IoT,  5G/6G  | networks, and  |     |     | smart  cities.  |     | Still,  the  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | --- | --------------- | --- | ------------ |
enhancement of resource scheduling and fog node
study has a few shortfalls. Second, the use of RL
| computation  | offloading  |     | [10].  | The  | 85%  | resource  |     |     |     |     |     |     |     |
| ------------ | ----------- | --- | ------ | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
algorithms introduces computational overhead in the
utilization of resource allocation stands higher than
|     |     |     |     |     |     |     | framework,  | which  | limits  | the  | applicability  |     | of  this  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------- | ---- | -------------- | --- | --------- |
SDN's standard 65% because of RL-based adaptive
|           |                               |     |     |     |           |     | framework  | to  | large-scale  | networks  |     | that  | may  not  |
| --------- | ----------------------------- | --- | --- | --- | --------- | --- | ---------- | --- | ------------ | --------- | --- | ----- | --------- |
| resource  | allocation [7]. SDN combined  |     |     |     | with Fog  |     |            |     |              |           |     |       |           |
possess the necessary resources. Finally, the current
| Computing  | and  | Reinforcement  |     | Learning  |     | achieves  |     |     |     |     |     |     |     |
| ---------- | ---- | -------------- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
implementation focuses on simulated environments
| network       | optimization  |              | through  | new   | technological  |     |           |       |             |     |            |             |     |
| ------------- | ------------- | ------------ | -------- | ----- | -------------- | --- | --------- | ----- | ----------- | --- | ---------- | ----------- | --- |
|               |               |              |          |       |                |     | and  the  | true  | deployment  |     | may  face  | unexpected  |     |
| developments  | that          | researchers  |          | have  | confirmed      | in  |           |       |             |     |            |             |     |
problems (hardware compatibility, etc., scalability,
| their  | recent  | findings  | [14].  |     | The  framework  |     |     |     |     |     |     |     |     |
| ------ | ------- | --------- | ------ | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
etc.). A potential future direction is lightweight RL
demonstrates superior capabilities when compared to
models to lower computational costs and improve
existing IoT, 5G/6G network applications as well as
|     |     |     |     |     |     |     | scalability.  | In  | addition  | to  | that,  | testing  | in  the  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | --- | ------ | -------- | -------- |
smart city systems due to its adaptable framework
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025           DOI: 10.22266/ijies2025.0630.25

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received:  March 23, 2025.     Revised: April 13, 2025.                                                                                                   361
industrial IoT and autonomous systems will help test  [7]  L. Li, J. Liu, and H. Ji, “Reinforcement Learning
the dependability of the configuration and frame.  for  Network  Slicing  in  6G  Networks:
Delving into the blending of edge computing with  Challenges  and  Opportunities”,  IEEE
Fog  Computing  can  also  help  in  gaining  more  Transactions  on  Network  and  Service
information  about  the solution  of  latency  and  Management, Vol. 21, No. 2, pp. 1234-1256,
| resource  utilization.  | Future  |     | work  | can  take  these  | 2024.  |     |     |     |     |     |     |
| ----------------------- | ------- | --- | ----- | ----------------- | ------ | --- | --- | --- | --- | --- | --- |
efforts  even  farther  by  sourcing  additional  [8]  J. Ren, H. Zhang, and K. Zhang, “Hybrid SDN-
experiments  (broader  things  explored  in  a  given  Fog  Architectures  for  Real-Time  Decision
intellectual space) and jobs (defined futures exposed  Making  in  AutoNomous  Systems”,  IEEE
to the variety of inks explored), overcoming various  Communications Magazine, Vol. 63, No. 3, pp.
limitations  here  antiphon  the  aforementioned  45-56, 2025.
intelligent  network  architectures  and  other  next- [9]  S. K. Sharma, X. Wang, and M. Chen, “Latency
generation technologies.  Optimization  in  SDN-Based  IoT  Networks
|     |     |     |     |     | Using  | Deep  | Reinforcement  |     | Learning”,  |     | IEEE  |
| --- | --- | --- | --- | --- | ------ | ----- | -------------- | --- | ----------- | --- | ----- |
Conflicts of Interest  Internet of Things Journal, Vol. 10, No. 3, pp.
4567-4582, 2023.
The authors declare no conflict of interest.
|     |     |     |     |     | [10] J.  Xu,  | L.  | Chen,       | and  | P.  Zhou,  | “Dynamic  |          |
| --- | --- | --- | --- | --- | ------------- | --- | ----------- | ---- | ---------- | --------- | -------- |
|     |     |     |     |     | Resource      |     | Management  |      | in         |           | Fog-SDN  |
Acknowledgments
|     |     |     |     |     | Environments:  |     |     | A  Reinforcement  |     |     | Learning  |
| --- | --- | --- | --- | --- | -------------- | --- | --- | ----------------- | --- | --- | --------- |
The authors  would like  to rapid their sincere  Approach”,  IEEE  Transactions  on  Industrial
appreciation  to  Al-Bayan  University  for  their  Informatics,  Vol.  20,  No.  6,  pp.  4021-4031,
| generous support and cooperation in this research.  |     |     |     |     | 2024.  |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
[11] N. McKeown, T. Anderson, H. Balakrishnan, G.
| References  |     |     |     |     | Parulkar, L. Peterson, J. Rexford, S. Shenker,  |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
and J. Turner, “OpenFlow: Enabling InNovation
| [1]  A.  Al-Fuqaha,  | M.  | Guizani,  | and  | H.  ElSawy,  |             |     |             |     |      |          |     |
| -------------------- | --- | --------- | ---- | ------------ | ----------- | --- | ----------- | --- | ---- | -------- | --- |
|                      |     |           |      |              | in  Campus  |     | Networks”,  |     | ACM  | SIGCOMM  |     |
“Advancements in SDN and Fog Computing
Computer Communication Review, Vol. 38, No.
| Integration  | for  Next-Generation  |     |     | Networks”,  |     |     |     |     |     |     |     |
| ------------ | --------------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
2, pp. 69-74, 2023.
| IEEE  Communications  |     |     | Surveys  | &  Tutorials,  |     |     |     |     |     |     |     |
| --------------------- | --- | --- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
[12] M. Jammal, A. Singh, T. Shami, R. Asal, and Y.
Vol. 25, No. 2, pp. 1234-1267, 2023.
Li, “SDN and Virtualization Solutions for 5G
| [2]  Y.  Zhang,  | X.  | Li,  and  | Z.  | Wang,  “Deep  |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Networks: A Survey”, IEEE Communications
Reinforcement Learning for Dynamic Resource
Surveys & Tutorials, Vol. 25, No. 4, pp. 3033-
Allocation in SDN-Based IoT Networks”, IEEE
3055, 2023.
| Transactions  | on  | Network  |     | Science  and  |     |     |     |     |     |     |     |
| ------------- | --- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
[13] M. Aazam, I. Khan, and A. Anpalagan, “Fog
Engineering, Vol. 21, No. 3, pp. 890-905, 2024.
Computing: A TaxoNomy, Systematic Review,
[3]  R. Kumar, S. Singh, and J. Chen, “Fog-Enabled
and Future Directions”, IEEE Internet of Things
| SDN  Architectures  |     | for  | Ultra-Low  | Latency  |     |     |     |     |     |     |     |
| ------------------- | --- | ---- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Journal, Vol. 10, No. 5, pp. 3132-3150, 2024.
Applications in 5G/6G Networks”, Journal of
[14] L. Li, J. Liu, and H. Ji, “Deep Reinforcement
Network and Systems Management, Vol. 32, No.
Learning for Network Resource Allocation: A
4, pp. 456-478, 2023.
Comprehensive Survey”, IEEE Transactions on
[4]  M. Chen, H. Liu, and L. Zhang, “Intelligent
Network Science and Engineering, Vol. 18, No.
| Edge  | Computing  | Using  |     | Reinforcement  |     |     |     |     |     |     |     |
| ----- | ---------- | ------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
4, pp. 2345-2367, 2023.
Learning for Adaptive Traffic Routing”, IEEE
[15] R. Boutaba, M. A. Salahuddin, N. Limam, and
Internet of Things Journal, Vol. 11, No. 5, pp.
|     |     |     |     |     | S.  Ayoubi,  |     | “A  | Comprehensive  |     | Survey  | on  |
| --- | --- | --- | --- | --- | ------------ | --- | --- | -------------- | --- | ------- | --- |
7890-7905, 2024.
Machine Learning for Networking: EVolution,
[5]  S. Wang, Y. Li, and T. Nguyen, “AI-Driven
|     |     |     |     |     | Applications  |     | and  | Research  |     | Opportunities”,  |     |
| --- | --- | --- | --- | --- | ------------- | --- | ---- | --------- | --- | ---------------- | --- |
SDN Frameworks for Smart City Applications:
Journal of Network and Systems Management,
A Comprehensive Review”, IEEE Transactions
Vol. 30, No. 3, pp. 561-604, 2024.
on Industrial Informatics, Vol. 21, No. 1, pp.
[16] H. T. Dinh, C. Lee, D. Niyato, and P. Wang, “A
123-145, 2025.
Survey on Resource Management in Fog/Edge
[6]  T. Q. Dinh, C. Lee, and P. Wang, “Federated
Computing: Architectures, Key TechNologies,
Learning and Fog Computing for Scalable IoT
|     |     |     |     |     | and  | Open  | Issues”,  | IEEE  | Communications  |     |     |
| --- | --- | --- | --- | --- | ---- | ----- | --------- | ----- | --------------- | --- | --- |
Networks”, IEEE Internet of Things Journal,
Surveys & Tutorials, Vol. 25, No. 1, pp. 368-403,
Vol. 10, No. 7, pp. 5684-5699, 2023.
2023.
International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025           DOI: 10.22266/ijies2025.0630.25

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/

Received:  March 23, 2025.     Revised: April 13, 2025.                                                                                                   362
| [17] M.  Chen,  | Y.   | Hao,  | and   | K.  Hwang,       | “Fog  |
| --------------- | ---- | ----- | ----- | ---------------- | ----- |
| Computing       | and  | Its   | Role  | in  Intelligent  | Edge  |
Networks”, IEEE Internet of Things Journal,
Vol. 8, No. 4, pp. 2900-2912, 2023.
| [18] P.  Mach  | and  | Z.      | Becvar,       | “Mobile       | Edge  |
| -------------- | ---- | ------- | ------------- | ------------- | ----- |
| Computing:     | A    | Survey  | on            | Architecture  | and   |
| Computation    |      |         | Offloading”,  |               | IEEE  |
Communications Surveys & Tutorials, Vol. 21,
No. 3, pp. 1628-1656, 2023.
| [19] X.  Liu,  | Z.  | Qin,         | and      | Y.  Gao,   | “Deep     |
| -------------- | --- | ------------ | -------- | ---------- | --------- |
| Reinforcement  |     | Learning     |          | for        | Resource  |
| Management     |     | in  Network  |          | Slicing”,  | IEEE      |
| Transactions   |     | on           | Network  | Science    | and       |
Engineering, Vol. 19, No. 1, pp. 348-362, 2024.
[20] S. Wang, X. Zhang, and L. Zhao, “Machine
Learning for Networking: Workflow, Advances
and Opportunities”, IEEE Network, Vol. 36, No.
2, pp. 92-99, 2023.
[21] T. Q. Dinh, N. Nguyen, and E. Dutkiewicz,
| “Federated  | Learning   |     | for        | Internet  | of  Things:  |
| ----------- | ---------- | --- | ---------- | --------- | ------------ |
| Recent      | Advances,  |     | TaxoNomy,  |           | and  Open    |
Challenges”, IEEE Internet of Things Journal,
Vol. 10, No. 7, pp. 5684-5699, 2024.
[22] W. Shi, J. Cao, Q. Zhang, Y. Li, and L. Xu,
| “Edge  | Computing:  |     | Vision  | and  Challenges”,  |     |
| ------ | ----------- | --- | ------- | ------------------ | --- |
IEEE Internet of Things Journal, Vol. 7, No. 5,
pp. 637-646, 2023.
[23] J. Ren, H. Zhang, and K. Zhang, “Integrating
SDN and Fog Computing: A Survey”, IEEE
Communications Surveys & Tutorials, Vol. 24,
No. 2, pp. 1107-1130, 2024.
[24] Y. Mao, C. You, J. Zhang, K. Huang, and K. B.
Letaief, “A Survey on Mobile Edge Computing:
| The  Communication  |     |     | Perspective”,  |     | IEEE  |
| ------------------- | --- | --- | -------------- | --- | ----- |
Communications Surveys & Tutorials, Vol. 22,
No. 4, pp. 2322-2358, 2024.
[25] Z. Ning, P. Dong, X. Wang, and L. Guo, “A
Comprehensive Survey on AI-Driven Digital
Twins in Industry 4.0: Smart Manufacturing and
| Advanced  | Robotics”,  |     | IEEE  | Transactions  | on  |
| --------- | ----------- | --- | ----- | ------------- | --- |
Industrial Informatics, Vol. 21, No. 9, pp. 6433-
6444, 2025.

International Journal of Intelligent Engineering and Systems, Vol.18, No.5, 2025           DOI: 10.22266/ijies2025.0630.25

This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
License details: https://creativecommons.org/licenses/by-sa/4.0/