# [04] A P4-Based Approach to Traffic Isolation and Bandwidth Management for 5G Network Slicing

> Source file: `[04] A P4-Based Approach to Traffic Isolation and Bandwidth Management for 5G Network Slicing.pdf`

---

TSINGHUA SCIENCE AND TECHNOLOGY
ISSN 1007-0214 13/31 pp171−185
DOI: 10.26599/TST.2024.9010020
Volume 30, Number 1, February 2025
A P4-Based Approach to Traffic Isolation and Bandwidth
Management for 5G Network Slicing
Wenji He, Haipeng Yao*, Huan Chang, and Yunjie Liu
Abstract: With various service types including massive machine-type communication (mMTC) and ultra-reliable
low-latency communication (URLLC), fifth generation (5G) networks require advanced resources management
strategies. As a method to segment network resources logically, network slicing (NS) addresses the challenges
of heterogeneity and scalability prevalent in these networks. Traditional software-defined networking (SDN)
technologies, lack the flexibility needed for precise control over network resources and fine-grained packet
management. This has led to significant developments in programmable switches, with programming protocol-
independent packet processors (P4) emerging as a transformative programming language. P4 endows network
devices with flexibility and programmability, overcoming traditional SDN limitations and enabling more dynamic,
precise network slicing implementations. In our work, we leverage the capabilities of P4 to forge a
groundbreaking closed-loop architecture that synergizes the programmable data plane with an intelligent
control plane. We set up a token bucket-based bandwidth management and traffic isolation mechanism in the
data plane, and use the generative diffusion model to generate the key configuration of the strategy in the
control plane. Through comprehensive experimentation, we validate the effectiveness of our architecture,
underscoring its potential as a significant advancement in 5G network traffic management.
Key words: network slicing; P4; traffic isolation; bandwidth management; diffusion model
1 Introduction management[1]. To address these complexities,
particularly when diverse applications coexist on a
With the advancement of fifth generation (5G) and
shared network infrastructure, leading to issues like
Beyond 5G (B5G) technologies, a new paradigm in
bandwidth congestion and variable connectivity
mobile communications is unfolding. These
quality, network slicing (NS) emerges as a strategic
technologies are marked by a substantial surge in data
solution[2]. By segmenting the network into distinct
traffic and an extensive variety of service offerings,
slices each tailored for specific services or applications,
posing new challenges in network resources
NS not only enhances resource efficiency but also
improves user experiences by reducing latency and
Wenji He, Haipeng Yao, and Yunjie Liu are with School of
Information and Communication Engineering, Beijing offering customized quality of service (QoS)[3].
University of Posts and Telecommunications, Beijing 100876, Building upon the network management challenges
China. E-mail: hewenji@bupt.edu.cn; yaohaipeng@bupt. brought forth by the surge in data traffic and service
edu.cn; liuyj@pmlabs.com.cn. variety in 5G and B5G technologies, the integration of
Huan Chang is with School of Information and Electronics,
software-defined networking (SDN) with network
Beijing Institute of Technology, Beijing 100081, China. E-mail:
slicing emerges as a crucial innovation[4].
changhuan@bit.edu.cn.
Characterized by its distinctive separation of the
* To whom correspondence should be addressed.
Manuscript received: 2023-11-02; revised: 2023-12-25; control plane from the data plane, SDN facilitates
accepted: 2024-01-18 dynamic resource management, optimizing application
© The author(s) 2025. The articles published in this open access journal are distributed under the terms of the
Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/).

172 Tsinghua Science and Technology, February 2025, 30(1): 171−185
performance for a diverse range of requirements. networks.
However, when combined with network slicing, To address the limitations of static meter
traditional SDN encounters unresolved challenges, configurations in P4, we advocate the integration of
particularly in terms of adaptability and flexibility due generative artificial intelligence (GAI) algorithms
to the constraints imposed by vendor-specific within the control plane. This approach is designed to
hardware, which becomes especially pronounced when dynamically predict and optimize the parameters for
addressing the dynamic and varied requirements of 5G bandwidth management in P4 meters, significantly
network services[5]. The advent of programmable data enhancing the adaptability and efficiency of network
planes, exemplified by programming protocol- slicing. In the ever-evolving networking sphere, GAI is
independent packet processors (P4), introduces a new poised to revolutionize various aspects of network
level of programmability across diverse network operations[11]. It offers a breadth of capabilities, from
devices[6]. As a domain-specific language tailored for facilitating dynamic responses to real-time network
orchestrating packet-forwarding mechanisms in various conditions to providing predictive insights for informed
networking hardware, P4’s unique strength lies in its decision-making. Furthermore, GAI introduces
ability to support NS with high precision, thereby innovative strategies for resource allocation, ensuring
overcoming the adaptability constraints of traditional optimal network performance. Amongst the generative
data planes. models, diffusion models stand out for their unique
The integration of P4 programming with network data generation process[12]. These models are trained
slicing marks a significant shift, enabling precise by gradually adding Gaussian noise to the training data
control over various network segments within a single and then learning to reverse this process, effectively
physical infrastructure, addressing the diverse needs of denoising the data. In application, this involves taking
modern network services[7]. NS effectively partitions a random noise samples and processing them through the
physical network into several virtual segments, each trained denoising mechanism to generate new data
optimized for specific requirements. P4’s role as a instances. This technique capitalizes on the model’s
specialized programming language extends this ability to reconstruct original data from noise-altered
states, offering a powerful tool for data generation and
capability, allowing intricate control over packet
analysis in network environments.
processing from header modifications to priority-based
forwarding. The effectiveness of P4 in supporting Within the networking optimization, GAI exerts
network slicing is evident in several key areas. It substantial influence across all network facets. Its
allows for dynamic resource distribution, tailored impact extends from fundamental aspects like content
processing routines for each slice, and efficient use of delivery to the intricate architectural configurations of
hardware resources[8]. Techniques like dynamic table networks. For instance, GAI enhances network
updates and flexible packet modifications facilitated by adaptability by enabling dynamic adjustments that
P4 lead to reduced latency and enhanced service respond to real-time conditions. It offers predictive
customization[9]. Some researches focus on the meters insights that support informed decision-making, and it
in P4 for managing network resources effectively, as devises strategic resource allocation methods that are
they enable rate-limiting and bandwidth control within crucial for achieving optimal network performance.
each slice, isolating traffic to prevent resource Diffusion models are categorized as generative models,
contention between slices[10]. By incorporating designed to generate data akin to the data used for their
metering, P4 facilitates advanced techniques like training. Essentially, these models operate by
dynamic table updates, flexible packet modifications, systematically perturbing the training data with
and priority queuing, all while ensuring each slice successive increments of Gaussian noise and
operates within its allocated resources, thereby subsequently learning to restore the original data by
reducing latency and enhancing service customization. reversing this noise application. Following the training
However, the static nature of meter settings in P4 can phase, employing the diffusion models for data
lead to suboptimal resource allocation, as they cannot generation becomes a straightforward process−by
dynamically adjust to the fluctuating network directing randomly sampled noise through the acquired
conditions and traffic patterns, especially in the context denoising process, the model generates new data
of the ever-changing demands of 5G and B5G instances. This method leverages the model’s learned

Wenji He et al.: A P4-Based Approach to Traffic Isolation and Bandwidth Management for 5G Network Slicing 173
capacity to reconstruct the original data from the noise- establish the problem. In Section 4, we propose a P4-
induced representations[13]. based approach to traffic isolation and bandwidth
In this article, we introduce an innovative network management for the network slicing, In Section 5, we
slicing framework driven by P4 programming, which design a generative diffusion algorithm for the
continuously monitors network traffic and performance bandwidth management strategy. In Section 6,
metrics to establish dedicated, independent channels simulation results and performance analysis are
within the network. The key focus is on utilizing P4’s presented, followed by a summary of our findings and
dynamic capabilities to partition network resources, a discussion on potential future work in Section 7.
ensuring isolated traffic within each slice and
2 Related Work
preventing any interference from adjacent slices.
Enhancing this framework, we integrate GAI In this section, we will discuss related work from the
algorithms, particularly diffusion models, into the view of resource management of the network slicing,
control plane. This integration enables the system to the usage of the programmable data plane, and the
predict future traffic patterns and service demands, generative AI algorithms for network optimization.
allowing for proactive and real-time adjustments in
2.1 Resource management of the network slicing
slice scaling and resource allocation. Such predictive
capabilities are transformative, ensuring uninterrupted Network slicing necessitates sophisticated resource
service during peak traffic periods and avoiding the management strategies for effectively distributing
need for excessive resource provisioning. The major computational, storage, and bandwidth resources across
contributions of this paper are summarized as follows. its virtual segments. This ensures that each slice is
(1) We introduce P4’s programmability to resource adequately resourced while maintaining overall
management at the data plane level. This encompasses network efficiency and reliability. In Ref. [14], Bega
detailed information management and the et al. proposed a deep learning architecture for
implementation of innovative meter designs along with predicting the capacity needed to meet future traffic
token bucket mechanisms. By exploiting the demands within a single network slice, taking into
programmable nature of P4, we achieve precise traffic account the operators’ desire to strike a balance
isolation and cater to diverse service requirements with between resource over-provisioning and service request
enhanced accuracy. violations. In Ref. [1], Zhang et al. presented a logical
(2) We present a novel methodology that integrates architecture for a 5G system built on network slicing
generative diffusion model within the control plane. and proposed a scheme for managing mobility between
This approach leverages the predictive power of AI to different access networks. In Ref. [15], Jošilo et al. put
anticipate traffic patterns and service demands, forward a game theory-based architecture aimed at
enabling dynamic adjustments in network slicing. This jointly optimizing the dynamic assignment of
predictive approach allows for more efficient and computational tasks to slices and resource
responsive resource allocation, ensuring the network management. They considered a slicing-enabled edge
adapts to changing demands while maintaining service system where the slice resource orchestrator assigns
quality. devices to slices and shares radio resources among
(3) To evaluate the effectiveness of our proposed them, with the objective of maximizing overall system
closed-loop architecture, we develop a comprehensive performance. In Ref. [16], Thantharate et al. proposed
architecture using P4 meters. This architecture provides the utilization of a transfer learning approach to
a practical experimental pathway to assess the address the complex network load estimation problem
performance and viability of our approach, showcasing in network slicing. Their goal was to promote a fairer
the enhanced adaptability and efficiency brought by the and more equitable distribution of network resources.
integration of GAI. In Ref. [17], Mai et al. proposed to improve the
The rest of this work is organized as follows. In performance of slicing in terms of quality of service,
Section 2, we review the pertinent literature, energy efficiency, and reliability by combining the
delineating the existing challenges and current capabilities of deep reinforcement learning based on a
methodologies. In Section 3, we formulate the migration learning framework. However, much
mathematic model of our proposed system and existing research tends to treat network elements as

174 Tsinghua Science and Technology, February 2025, 30(1): 171−185
black-boxed entities with a relatively coarse granularity optimization represents a significant leap in the field of
of control. This indicates the potential for further network slicing. In Ref. [19], Xu et al. proposed the
advancements in more granular and detailed resource deployment of mobile AIGC networks via
management within network slicing. collaborative cloud-edge-mobile infrastructure is
proposed to support wider AIGC services. In Ref. [20],
2.2 Programmable data plane assisted the
Huang et al. proposed a novel diffusion model-based
network slicing
learning approach to dynamically and adaptively
The role of P4 programmable data planes in network generate the network design to cope with the time-
slicing has been a focal point in recent research. In varying environments and various service
Ref. [7], Chen et al. proposed a design of bandwidth requirements. In Ref. [21], Huang et al. proposed
management for QoS with SDN and P4-programmable distributed learning paradigms to enable the AIGC in
switch based the function of the meter in P4 switch. In the wireless network supported by harmonious cloud-
Ref. [9], Wang et al. further designed and implemented edge-mobile infrastructures to enhance a broader range
a TCP friendly meter in the packet processing pipeline of AIGC services. In Ref. [22], Du et al. proposed a
of the P4 switch to realize resource control and quality novel collaborative distributed diffusion based AIGC
of service assurance for specific flow services. In Ref. framework, which uses the collaboration among
[10], Chen et al. designed the programmable switch’s devices in wireless networks and optimizes edge
meter to flexibly bandwidth-guarantee and manage computation resource utilization. These advanced AI
network slices by isolating different types of traffic in algorithms, including diffusion models, bring
multiple priority queues while setting appropriate transformative potential in predictive analytics, leading
storage bucket sizes. While these studies concentrated to more efficient and intelligent network management.
on the resource management capabilities of P4-based
3 System Model and Problem Formulation
programmable switches, they mainly emphasized
bandwidth resources rather than exploiting the full This section clarifies the mathematical framework of
potential of fine-grained resources provided by these our P4-based network slicing strategies.
switches. In Ref. [8], Hauser et al. proposed P4-
3.1 Network architecture
programmable targets are capable of network slicing in
all proposed variants. They explored the different As depicted in Fig. 1, the network architecture is
aspects of inter-tenant interference due to differences in stratified into three distinct layers: Application plane
targeting and slicing methods, and proposed hardware- interfaces with user applications, cataloging specific
based slicing methods to eliminate these interferences. service demands such as bandwidth, latency, and
In Ref. [18], Pinto et al. proposed a hierarchical SDN resilience against packet loss. This layer is pivotal in
optical packet survivability solution based on network translating user-centric requirements into precise
slicing is proposed to provide different levels of network configurations, forming the nexus between
reliability. Slicing is implemented in a P4 demand and delivery. Control plane orchestrates the
programmable ASIC for traffic prioritization and network’s operational dynamics, leveraging advanced
protection switching. Despite these advancements, the generative AI algorithms to facilitate informed
majority of existing approaches primarily focused on decision-making processes. It is the linchpin that
managing and optimizing bandwidth resources, translates high-level service policies into granular,
utilizing programmable data planes, open switches, and actionable configurations for the data plane, guiding
fine-grained storage, compute, and transport resources. the network’s adaptive behavior to align with service-
However, many of these management schemes level agreements and optimization objectives. At the
predominantly targeted the data plane, often neglecting foundation lies programmable data plane, the execution
the powerful control and decision-making capacities layer where data packets are actively processed,
available in the control plane. managed, and routed. This is facilitated by the intrinsic
programmability of P4 switches, which execute the
2.3 Generative AI methods for network
policies formulated by the control plane, embodying
optimization
the operational instructions in real-time traffic
The incorporation of GAI methods in network management.

  Wenji He et al.:  A P4-Based Approach to Traffic Isolation and Bandwidth Management for 5G Network Slicing 175

Fig. 1    System model of the P4-based network slicing strategies.
3.2　User model slice.  As  delineated  in  Fig. 2,  the  P4  processing
|           |        |           |     |               | pipeline, |               |  fundamental |  to  INT,         |  progresses |  through     |
| --------- | ------ | --------- | --- | ------------- | --------- | ------------- | ------------ | ----------------- | ----------- | ------------ |
| The  user |  model |  provides |  a  |  mathematical |           |               |              |                   |             |              |
|           |        |           |     |               | parsing,  |  match-action |              |  decision-making, |             |  and  packet |
characterization of service demands that informs the
|     |     |     |     |     | reassembly, |     |  enabling |  the  extraction, |  processing, |  and |
| --- | --- | --- | --- | --- | ----------- | --- | --------- | ----------------- | ------------ | ---- |
configuration of network slices to meet the specific
|     |     |     |     |     | modification |     |  of  packet |  data  in |  real-time[6]. |  This |
| --- | --- | --- | --- | --- | ------------ | --- | ----------- | --------- | -------------- | ----- |
QoE objectives for varied 5G applications. We use
pipeline not only mirrors the network’s current state to
| D(u)=fB                   | ;L ;P g denote the demand of user u as a set |              |     |                    |     |          |        |                       |      |             |
| ------------------------- | -------------------------------------------- | ------------ | --- | ------------------ | --- | -------- | ------ | --------------------- | ---- | ----------- |
|                           | u u u                                        |              |     |                    |     |          |        |                       |      |             |
|                           |                                              |              |     |                    | the |  control |  plane |  but  also  furnishes |  the |  predictive |
| that includes bandwidth B |                                              | u, latency L |     | u, and packet loss |     |          |        |                       |      |             |
analytics crucial for resource management and network
| rate  P u. |  In  the  user |  model, |  each |  application’s |               |     |     |              |      |               |
| ---------- | -------------- | ------- | ----- | -------------- | ------------- | --- | --- | ------------ | ---- | ------------- |
|            |                |         |       |                | optimization. |     |  We |  denote  the |  INT |  metadata  as |
requirements inform the network slice’s characteristics. F =fB ′ ;L ′;P ′ g, where INT provides real-time data on
i
|     |     |     |     |     |     | i   | i ′ i | ′   |     | ′   |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
For  instance,  critical  applications  such  as  remote bandwidth B , latency L , and packet loss P  for each
|                                            |     |     |                     |             |            |                                                | i   | i   |     | i   |
| ------------------------------------------ | --- | --- | ------------------- | ----------- | ---------- | ---------------------------------------------- | --- | --- | --- | --- |
| surgery demand a D(u) with high B          |     |     | u for uninterrupted |             |            |                                                |     |     |     |     |
|                                            |     |     |                     |             | slice i. F | i not only informs the control plane about the |     |     |     |     |
| high-definition video streaming, minimal L |     |     |                     | u to ensure |            |                                                |     |     |     |     |
current state of the network but also enables predictive
| real-time responsiveness, and a near-zero P |     |     |     | u for data |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
analytics for anticipating future network states. These
integrity. In contrast, less critical services like smart indicators not only reflect the current network state to
home monitoring may present a more lenient set of the control plane but also underpin predictive analytics,
| demands, allowing for higher L |     |     | u and a tolerable P |     | u,        |     |                   |          |             |      |
| ------------------------------ | --- | --- | ------------------- | --- | --------- | --- | ----------------- | -------- | ----------- | ---- |
|                                |     |     |                     |     | essential |     |  for  forecasting |  network |  conditions |  and |
reflecting a scalable and flexible approach to resource preemptively  managing  resources.  Such  foresight  is
allocation.  These  models  are  essential  for  tailoring integral  to  proactive  resource  allocation  and  traffic
network slices to the demands of 5G services. shaping.  Utilizing  INT  data,  the  control  plane
dynamically orchestrates network slices to meet their
3.3　Programmable switch model
|             |               |          |         |                     | respective    |     |  performance |  objectives,  |     |  leveraging    |
| ----------- | ------------- | -------- | ------- | ------------------- | ------------- | --- | ------------ | ------------- | --- | -------------- |
| Our  model  |  for  network |  slicing |  within |  a  P4  switch      |               |     |              |               |     |                |
|             |               |          |         |                     | sophisticated |     |  algorithms  |  for  dynamic |     |  slicing  that |
| environment |  emphasizes   |  the     |  vital  |  roles  of  in-band |               |     |              |               |     |                |
ensures each slice upholds its service level without
| network telemetry (INT) and metering. |     |     |     |     | impacting others. |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
3.3.1　INT information
3.3.2　Meter configuration
INT is pivotal for providing granular, real-time insights The meter in P4 is a fundamental construct, functioning
into  network  performance,  tailored  to  each  network to  monitor  the  rate  of  packet  or  byte  flow  over

    176 Tsinghua Science and Technology, February 2025, 30(1): 171−185

Fig. 2    Architecture of the P4[6].
designated  time  intervals  and  to  execute  specific utilization factor of the allocated table entries.
actions contingent on the measured rates. For slice s,
3.4　Problem formulation
|            |                  | =CIR               | ;CBS           | ;PIR g, |              |            |     |               |                 |
| ---------- | ---------------- | ------------------ | -------------- | ------- | ------------ | ---------- | --- | ------------- | --------------- |
| the  meter |  configuration,  | Meter              |                |         |              |            |     |               |                 |
|            |                  | s                  | s              | s s     |              |            |     |               |                 |
|            |                  |                    |                |         | Our  primary |  objective |  is |  to  optimize |  the  alignment |
| functions  |  as  a  traffic  |  regulator  within |  P4  switches, |         |              |            |     |               |                 |
aligning traffic flow with control plane policies. CIR between  user  demands  and  actual  network
s
is the committed information rate, ensuring a consistent performance, a goal grounded in the need to maximize
bandwidth rate for slice  s, which is vital for stable user satisfaction within the constraints of finite network
performance  and  adherence  to  service  requirements. resources. By effectively balancing these aspects, we
CBS s  represents  the  committed  burst  size,  allowing aim to create a network slicing environment that is not
slices  to  maintain  performance  under  typical  traffic only  responsive  to  user  needs  but  also  maintains
loads.  PIR s  signifies  the  peak  information  rate, optimal operational efficiency. The utility function for
accommodating  maximum  bandwidth  usage  during meeting the requirements of user u is defined as a sum
surge conditions. Effective metering enables the data of  logarithmic  terms,  capturing  the  principle  of
plane to uphold each slice’s service level objectives,
|     |     |     |     |     | diminishing |  returns, |  which |  reflects |  the  reality  that |
| --- | --- | --- | --- | --- | ----------- | --------- | ------ | --------- | ------------------- |
including  bandwidth  limitations  and  latency  targets, incremental  improvements  in  network  performance
while  promoting  equitable  resource  sharing  among yield  progressively  smaller  increases  in  user
| slices.                                               |  P4  switches’  | meter  configurations |     |  are | satisfaction, |                        |     |                    |        |
| ----------------------------------------------------- | --------------- | --------------------- | --- | ---- | ------------- | ---------------------- | --- | ------------------ | ------ |
| instrumental in realizing these operational controls. |                 |                       |     |      |               |                        |     | ′                  |        |
|                                                       |                 |                       |     |      |               |                        |     | B                  |        |
|                                                       |                 |                       |     |      |               | Utility(D(u))=(cid:11) |     | log(1+ u)+(cid:12) | log(1+ |
| 3.3.3　Table entries of P4 switches                    |                 |                       |     |      |               |                        | u   |                    | u      |
B
u (1)
P4  employs  tables  as  key  constructs  for  matching L max;u P max;u
|                                                        |     |     |     |     |     | )+(cid:13) | log(1+ | )   |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | ---------- | ------ | --- | --- |
| packet headers and executing corresponding actions, as |     |     |     |     |     | ′          | u      | ′   |     |
|                                                        |     |     |     |     |     | L          |        | P   |     |
|                                                        |     |     |     |     |     | u          |        | u   |     |
depicted in Fig. 2. Each entry in a table specifies a
Subject to
| match |  criterion  and |  an  associated |  action |  with |     |     | ∑   |     |     |
| ----- | --------------- | --------------- | ------- | ----- | --- | --- | --- | --- | --- |

| parameters, allowing for dynamic adaptability to meet |     |                          |     |     |     |                   | B0       | ⩽B      |     |
| ----------------------------------------------------- | --- | ------------------------ | --- | --- | --- | ----------------- | -------- | ------- | --- |
|                                                       |     |                          |     |     |     |                   |          | s total |     |
| slicing demands. We denote E                          |     | i;j as the allocation of |     |     |     |                   | s2S      |         |     |
|                                                       |     |                          |     |     |     | (cid:11) (cid:12) | (cid:13) |         |     |
table entries for slice i in switch  j, where the total where  u,  u,  and  u  are  weighting  factors  for
|          |                     |                 |      | C.    | bandwidth, latency, and packet loss, respectively, each |     |     |     |     |
| -------- | ------------------- | --------------- | ---- | ----- | ------------------------------------------------------- | --- | --- | --- | --- |
| capacity |  of  each  switch’s |  table  entries |  is  |  This |                                                         |     |     |     |     |
dynamic  configuration  facilitates  efficient  routing, reflecting the relative importance of these aspects in
|     |     |     |     |     |     |     |     | ′   | ′ ′ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bandwidth  management,  and  QoS  maintenance  for determining user satisfaction. B , L , and P  represent
|     |     |     |     |     |     |     |     | u   | u u |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
each slice, ensuring optimal alignment with specific the  actual  bandwidth,  latency,  and  packet  loss
traffic  profiles.  We  use  g(E )  to  represent  the experienced by the user collected from INT, while B u,
i;j

  Wenji He et al.:  A P4-Based Approach to Traffic Isolation and Bandwidth Management for 5G Network Slicing 177
L max;u, and P max;u denote their respective demanded or constraints  and  service  level  agreements.
acceptable levels. Our goal is to maximize user utility, Complementing the DiffServ framework, we utilize the
balancing this with the cost of P4 configurations to two-rate, three-color marker (trTCM) mechanism. This
enhance resource utilization efficiency as mechanism segregates packets into green, yellow, or
|     |     | ∑   |     | ∑   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  Utility(D(u))(cid:0) ((cid:20) (cid:2)CIR + red categories, based on their ingress rates relative to
max
|     |     |     |     |      | 1 s |     | the established CIR and PIR, using a dual token bucket |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     |     | u2U |     | s2S∑ |     |     |                                                        |     |     |     |     |     |     |     |
(2)
(cid:20) (cid:2)CBS +(cid:20) (cid:2)PIR )(cid:0)(cid:21) g(E ) algorithm to control the rate of transmission.
|     | 2   | s 3 | s   |     | i;j |     |                                                     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | j2J |     |     | Figure 3 provides a detailed representation of a P4 |     |     |     |     |     |     |     |
Subject to switch,  highlighting  the  interconnection  between  its
∑

E i;j ⩽C;8j2J; software programming, table resources, and hardware
i2I
|     |     |      |              |     |     |     | infrastructure. |     |  The |  meter |  pipeline |     |  showcases |  the |
| --- | --- | ---- | ------------ | --- | --- | --- | --------------- | --- | ---- | ------ | --------- | --- | ---------- | ---- |
|     |     | 0⩽Ut | ⩽1;8i2I;j2J: |     |     |     |                 |     |      |        |           |     |            |      |
i;j
We denote (cid:20) ;(cid:20) ;(cid:20) 3, and (cid:21) as cost coefficients for trTCM  methodology  in  bandwidth  management,
1 2
allocating traffic to high or low priority queues based
| CIR, |  CBS, |  PIR,  and |  table |  entry |  utilization, |     |     |     |     |     |     |     |     |     |
| ---- | ----- | ---------- | ------ | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
on specific criteria. Green packets, compliant with the
| respectively. |     |  The  cost |  functions |     |  for |  meter |     |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | ---------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
agreed traffic profile by not exceeding the CIR, are
| configurations |     |  and  table |  entries |     |  in  the  objective |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | -------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
typically given priority, supporting the network’s goals
function can indeed be linear. This choice simplifies
|                  |     |              |     |       |                  |     | of  minimizing |           |  latency |     |  and  maximizing |           |  throughput. |         |
| ---------------- | --- | ------------ | --- | ----- | ---------------- | --- | -------------- | --------- | -------- | --- | ---------------- | --------- | ------------ | ------- |
| the  formulation |     |  and  aligns |     |  with |  the  principles |  of |                |           |          |     |                  |           |              |         |
|                  |     |              |     |       |                  |     | Yellow         |  packets, |  which   |     |  exceed          |  the  CIR |  but         |  remain |
mixed-integer linear programming (MILP).
below the PIR, indicate a tolerable deviation from the
4　P4-Based  Fine-Grained  Resources committed  rate  and  are  usually  queued  with
Management Method intermediate priority. Red packets, exceeding the PIR,
|     |     |     |     |     |     |     | represent |  a  |  significant |  deviation |     |  and |  are  frequently |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------ | ---------- | --- | ---- | ---------------- | --- |
This section presents a comprehensive examination of
subjected to lower priority handling or dropping, as a
| the  programmable |     |  switch |  components, |     |  focusing |  on |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
measure to control excessive bandwidth usage.
| both  the |  architecture |  and |  resource |     |  modeling |  of  the |     |     |     |     |     |     |     |     |
| --------- | ------------- | ---- | --------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Algorithm 1 shows the integration of trTCM in the
programmable data plane. Our objective is to not only
|     |     |     |     |     |     |     | P4  environment |     |  enables |     |  network |  administrators |     |  to |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | --- | -------- | --------------- | --- | --- |
ensure effective bandwidth guarantees but also to allow
|     |     |     |     |     |     |     | dynamically |     |  shape |  traffic |  and |  enforce |     |  policies |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | -------- | ---- | -------- | --- | --------- |
for the interference-free sharing of residual bandwidth
effectively, a crucial aspect in managing the diverse
when design the meter in P4, as illustrated in Fig. 3.
demands of modern network traffic and maintaining
4.1　Meter in P4 service  integrity  across  various  network  segments.
Adjusting the CIR and PIR thresholds in response to
Fundamental to our strategy for P4-based bandwidth
management is the implementation of the differentiated real-time  network  conditions  allows  for  fine-tuned
service delivery, aligning with changing traffic patterns
| services |  (DiffServ) |  model. |  This |  approach |  classifies |     |              |     |                |     |     |        |              |     |
| -------- | ----------- | ------- | ----- | --------- | ----------- | --- | ------------ | --- | -------------- | --- | --- | ------ | ------------ | --- |
|          |             |         |       |           |             |     | and  service |     |  requirements. |     |  In |  order |  to  provide |  a  |
packets based on distinct code-points indicating their
service  level,  which  then  governs  their  forwarding practical understanding of the metering design within
behavior and aligns traffic flow with predefined policy our P4-based approach, we present a key segment of
the P4 ingress control code. This code exemplifies how

the trTCM mechanism is applied to network packets
for effective bandwidth management:
4.2　A
|     |     |     |     |     |     |     |     |  differentiated |     |     |  resource |     |  management |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --------- | --- | ----------- | --- |
approach based onmeter in P4
We aim to devise a novel network slicing solution that
|     |     |     |     |     |     |     | guarantees                                            |  and |  manages  |     |  bandwidth |       |  for  each |  slice,   |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | ---- | --------- | --- | ---------- | ----- | ---------- | --------- |
|     |     |     |     |     |     |     | leveraging                                            |  the |  scalable |     |  resources |  and  |  the       |  flexible |
|     |     |     |     |     |     |     | programmability                                       |      |  of       |  P4 |  switches. |  From |  our       |  earlier  |
|     |     |     |     |     |     |     | discussions, we have established that the meter-based |      |           |     |            |       |            |           |
Fig. 3    Integrated  view  of  P4  switch  resources  and component,  empowered  by  the  trTCM  scheme,
|     |     |     |     |     |     |     | facilitates |     |  effective |  bandwidth |     |  management |     |  for |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | ---------- | --- | ----------- | --- | ---- |
bandwidth management.

178 Tsinghua Science and Technology, February 2025, 30(1): 171−185
Algorithm 1 P4 Ingress Control Code with trTCM settings network slice, we configure a trTCM meter instance in
control Ingress { P4, enforcing the committed and peak information
apply { rates (CIR and PIR).
if (ingress_port_acl.apply().hit) { Figure 4 illustrates the integrated resource
meter_result_t result = trTCM.execute_meter( management approach within a P4 switch,
packet_size, flow_index); incorporating our novel design of metering combined
switch (result.color) { with token buckets. This design is pivotal for fine-
case GREEN: grained bandwidth management across network slices,
// GREEN: For slice ID 1 with CIR of 100 Mbit/s as depicted by Meter s1 through Meter sN , and for traffic
if (flow_index = = 1) { that does not belong to a specific slice, labeled as non-
mark_packet_dscp(EXPEDITE_FORWARDING sliced. Each meter is associated with a corresponding
); token bucket that regulates the passage of packets
transmit_packet(); based on their priority level. High-priority traffic is
} ensured guaranteed bandwidth by its meter, ensuring
break; compliance with predefined service-level agreements.
case YELLOW: Low-priority traffic, which does not exhaust its meter’s
// YELLOW: For slice ID 2 with CIR of 50 Mbit/s, allocated rate, is allowed to tap into unused high-
enqueued to mid-priority
priority bandwidth, thus utilizing the excess capacity in
if (flow_index = = 2) {
an interference-free manner. This mechanism is
mark_packet_dscp(ASSURED_FORWARDING)
illustrated through two distinct pathways originating
;
from each meter: one directs packets that meet the
enqueue_packet(mid_priority_queue);
committed rate, encapsulated within the token bucket,
}
to a high-priority queue for expedited processing
break;
(indicated by a green arrow representing guaranteed
case RED:
traffic), while the other diverts to a low-priority queue.
// RED: For slice ID 3 exceeding PIR, packets are
dropped
The token buckets serve a critical function in this
if (flow_index = = 3) {
architecture by dynamically adjusting to traffic
mark_packet_dscp(DEFAULT_FORWARDING)
conditions. They replenish their token count over time,
;
up to the maximum burst size, allowing for short-term
drop_packet(); // Assuming RED packets are surges in traffic to be accommodated without
dropped penalizing the overall network performance. The token
} bucket associated with each meter ensures that green-
break; coded packets are transmitted with priority, while
} yellow-coded packets, which exceed the committed
} burst size but not the peak rate, are queued for later
} transmission. Red-coded packets, exceeding the peak
} rate, are subject to possible dropping, as indicated by
different flows and efficient slice resource allocation.
However, the advent of new resources necessitates
more stringent traffic isolation to optimize the use of
remaining bandwidth.
We have instituted a metering mechanism that
employs P4’s register arrays to continuously monitor
the utilization of various network resources, including
bandwidth, storage, and computational capacity. This
dynamic surveillance permits us to modulate resource
Fig. 4 Token bucket assists shared bandwidth allocation
allocations based on real-time measurements. For each and traffic isolation.

Wenji He et al.: A P4-Based Approach to Traffic Isolation and Bandwidth Management for 5G Network Slicing 179
the red “Drop” line, to prevent network congestion. Algorithm 2 P4 ingress control code with trTCM utilizing
This dynamic bandwidth sharing is especially metering and token bucket
significant in scenarios where high-priority traffic does control Ingress {
not fully utilize its reserved bandwidth. In such cases, action set_dscp_and_transmit(bit<6> dscp_value, bit<9>
egress_port) {
the unused bandwidth can be temporarily allocated to
standard_metadata.egress_spec = egress_port;
low-priority traffic, enhancing overall network
// Set the egress port for the packet
throughput without compromising the QoS of high-
hdr.ipv4.dscp = dscp_value;
priority slices. The proposed method thus ensures that
each network slice can utilize its fair share of }
resources, enhancing the fairness and ensuring optimal action enqueue_yellow(bit<3> queue_id) {
resource utilization across the network. We different // The meter has a committed bucket (CB) and a peak
bucket (PB)
slices can be managed with varying priorities within a
if (meter_cb.tokens > 0) {
P4 programmable switch, utilizing metering and token
// Consume a token from the committed bucket
bucket algorithms for effective bandwidth management
meter_cb.consume_token();
in Algorithm 2.
set_dscp_and_transmit(ASSURED_FORWARDING,
As we state the key code of P4, the
MID_PRIORITY_EGRESS_PORT);
set_dscp_and_transmit action within the code sets the
} else if (meter_pb.tokens > 0) {
differentiated services code point (DSCP) for the
// Consume a token from the peak bucket for burst
packet and designates its egress port, a crucial step in
allowance
applying the QoS policies. The subsequent
meter_pb.consume_token();
enqueue_yellow action showcases the token bucket
set_dscp_and_transmit(ASSURED_FORWARDING,
mechanism in action: tokens from the committed
MID_PRIORITY_EGRESS_PORT);
bucket are consumed first, allowing packets that
} else {
conform to the agreed-upon rate to be transmitted at a
drop_or_enqueue_packet(queue_id);
medium priority level. If the committed bucket is
}
exhausted, tokens from the peak bucket are used,
}
reflecting the allowance for traffic bursts. Should both
apply {
buckets be depleted, packets may be dropped or
if (ingress_port_acl.apply().hit) {
enqueued at a lower priority, ensuring fair access to the
// Execute metering with token buckets to determine the
network while avoiding congestion.
packet’s color
5 Design of the Generative Diffusion
meter_result_t result = meter.execute(packet_size,
flow_index);
Algorithm
// Actions are determined based on the color assigned by
the meter
5.1 Closed-loop of control plane and programmable
switch (result.color) {
data plane
}
As illustrated in Fig. 5, we propose an end-to-end }
resource management architecture for network slicing, }
comprising P4 switches and open-source controllers, }
such as ONOS. P4 switches in the architecture are
configured for rapid wire-speed forwarding, crucial for proficiency. Upon entering the system, data is initially
maintaining the low-latency, high-throughput processed by the controller and subsequently routed
performance expected in 5G networks. through the internal processing card. Here, it is directed
To complement their forwarding capabilities, the to the application-specific integrated circuit (ASIC)
switches are outfitted with processing cards that based on predefined specific service (SP) conditions,
combine computing and storage functionalities. These which cater to specialized services or protocols.
cards adeptly manage complex, non-time-critical Compliant data streams follow the SP path, while
processing tasks, striking an equilibrium between others proceed along the normal service route. This
expeditious data handling and computational bifurcation ensures that resources are judiciously

    180 Tsinghua Science and Technology, February 2025, 30(1): 171−185

Fig. 5    An end-to-end sliced resource management architecture.
allocated and services meticulously tailored, bolstering obscured by noise in a forward process. These models
network slicing management. then employ a reverse operation, iteratively refining
Within this framework, the control plane employs a and restoring the data’s structure. This approach casts
generative diffusion model (GDM) to analyze network
the model in the role of a latent variable system, where
performance feedback from the data plane. This AI- the data’s original form is gradually uncovered through
| centric  method |     |  dynamically |  refines |     |  network |  slicing | denoising steps. |     |     |     |     |     |     |
| --------------- | --- | ------------ | -------- | --- | -------- | -------- | ---------------- | --- | --- | --- | --- | --- | --- |
w
| parameters, |  optimizing |     |  bandwidth |  management |     |  and |     |     |                 |             |     |     |     |
| ----------- | ----------- | --- | ---------- | ----------- | --- | ---- | --- | --- | --------------- | ----------- | --- | --- | --- |
|             |             |     |            |             |     |      |     |     | p(cid:18)(x ):= | p(cid:18)(x | )dx |     | (3) |
traffic  isolation  based  on  real-time  network  traffic 0 0:T 1:T
analysis and demand patterns. We denote the latents of the same dimensionality as
|                  |     |            |            |     |           |     | fx ;x | ;:::;x | g. The reverse diffusion joint distribution, |     |     |     |     |
| ---------------- | --- | ---------- | ---------- | --- | --------- | --- | ----- | ------ | -------------------------------------------- | --- | --- | --- | --- |
| 5.2　  Generative |     |  diffusion |  algorithm |     |  designed |  to | 1     | 2      | T                                            |     |     |     |     |
p(cid:18)(x 0:T ), is defined as a Markov chain with learned
solve bandwidth management
Gaussian transitions, starting from a standard Gaussian
| In  our  network |     |  architecture, |  the |  GDM |  is  deployed |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------- | ---- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
distribution, which can be expressed as
| within  the |  control |  plane, |  applying |     |  a  conditioned |     |     |     |     |     |     |     |     |
| ----------- | -------- | ------- | --------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|             |          |         |           |     |                 |     |     |     |     |     | ∏T  |     |     |
diffusion  process  to  inform  decision-making.  This ):=p(x jx
|     |     |     |     |     |     |     |     |     | p(cid:18)(x | )   | p(cid:18)(x | t(cid:0)1 ) | (4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | ----------- | --- |
|     |     |     |     |     |     |     |     |     | 0:T         | T   |             | t           |     |
approach  employs  a  sophisticated  machine  learning t(cid:0)1
model, designed to generate optimal decisions based on
|               |          |               |     |     |        |           | where |  each |  transition |  is  modeled |     |  by  a  Gaussian |     |
| ------------- | -------- | ------------- | --- | --- | ------ | --------- | ----- | ----- | ----------- | ------------ | --- | ---------------- | --- |
| the  existing |  network |  environment, |     |     |  which |  includes |       |       |             |              |     |                  |     |
distribution:
| incoming |  user |  tasks  and |  the |  status |  of |  network |     |     |     |     |     | ∑   |     |
| -------- | ----- | ----------- | ---- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     | p(cid:18)(x | jx ):=N(x | ;(cid:22) | (cid:18)(x ;t); | (x ;t)) | (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --------- | --------------- | ------- | --- |
resources. The primary aim of the GDM algorithm is to t(cid:0)1 t t(cid:0)1 t t
maximize overall utility, optimizing the allocation of (cid:18)
key  network  resources,  particularly  bandwidth.  This Conversely,  the  forward  diffusion  chain
ensures effective traffic management and meets service incrementally adds noise over time through a Markov
requirements efficiently. process  according  to  a  variance  schedule
| We denote the original strategy for meter as x |                                            |     |     |     |     | s for | f(cid:27) ;(cid:27) | ;:::;(cid:27) | g as |     |     |     |     |
| ---------------------------------------------- | ------------------------------------------ | --- | --- | --- | --- | ----- | ------------------- | ------------- | ---- | --- | --- | --- | --- |
|                                                |                                            |     |     |     |     |       | 1                   | 2             | T    |     |     |     |     |
| the slice                                      | s. Diffusion-based generative models frame |     |     |     |     |       |                     |               |      | ∏T  |     |     |     |
|                                                |                                            |     |     |     |     |       |                     |               | jx   | ):= | jx  |     |     |
the process of creating data as a methodical reversal of q(x 1:T 0 q(x t t(cid:0)1 ) (6)
noise  addition.  Initially,  the  data  is  progressively t=1

  Wenji He et al.:  A P4-Based Approach to Traffic Isolation and Bandwidth Management for 5G Network Slicing 181
where each step is described by This  stepwise  increase  in  noise  level  gradually
√
  jx ):=N(x 1(cid:0)(cid:27) ;(cid:27) obscures the original data, simulating the uncertainty
|     | q(x | t(cid:0)1 | ;   | x t(cid:0)1 | I) (7) |     |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t t t t and variability inherent in network traffic patterns.
Following the training, the model generates data by
|                 |     |                                      |     |     |     | (2) |  Reverse |  Diffusion: |     |  After |  the |  data |  reaches |  a  |
| --------------- | --- | ------------------------------------ | --- | --- | --- | --- | -------- | ----------- | --- | ------ | ---- | ----- | -------- | --- |
| sampling from x |     | T and applying the reverse diffusion |     |     |     |     |          |             |     |        |      |       |          |     |
certain noise saturation, the reverse diffusion process
chain. The model can be adapted to specific conditions commences.  In  this  phase,  noise  is  methodically
| by  incorporating |     |  additional |  contextual |     |  information. |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ----------- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
removed, or the data is denoised. This reverse process
Diffusion models exhibit a versatile architecture that
|     |     |     |     |     |     | is  critical: |     |  as  the |  noise |  diminishes, |     |  our |  AI-driven |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ------ | ------------ | --- | ---- | ---------- | --- |
allows for their extension to conditional models. This is
|     |     |     |     |     |     | algorithm, |     |  encompassing |     |     |  the  | “Strategy |  Quality |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ------------- | --- | --- | ----- | --------- | -------- | --- |
achieved  by  incorporating  conditions  into  the Network”  and  the  “Strategy  Generation  Network”
| probability |     |  distribution, |  denoted |  as  | p(cid:18)(x jx ;c), |                                                           |     |     |     |     |     |     |     |     |
| ----------- | --- | -------------- | -------- | ---- | ------------------- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|             |     |                |          |      | t(cid:0)1 t         | learns to reconstruct and refine the resource allocation. |     |     |     |     |     |     |     |     |
thereby guiding the model to generate data based on
|     |     |     |     |     |     | This |  iterative |  learning |     |  approach |  guides |     |  the  system |     |
| --- | --- | --- | --- | --- | --- | ---- | ---------- | --------- | --- | --------- | ------- | --- | ------------ | --- |
given conditions or parameters.
towards generating strategies that progressively align
As shown in Fig. 6, decisions derived from the GDM closer  to  the  ideal  solution  for  efficient  bandwidth
in the control plane are transformed into implementable
|     |     |     |     |     |     | management |     |  and |  resource |     |  allocation |  in |  network |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | --------- | --- | ----------- | --- | -------- | --- |
configurations and rules within the P4 programmable
slicing.
data plane. These decisions, formulated through the
The environment essentially encapsulates the static
conditioned diffusion process, aim to optimize resource and  dynamic  aspects  of  the  network  that  are  not
utilization and traffic management within the network
|     |     |     |     |     |     | directly |  controlled |     |  by |  the |  bandwidth |  management |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | --- | ---- | ---------- | ----------- | --- | --- |
slices. P4 switches are then programmed to enforce
strategies but instead influence or constrain them. This
these  strategies,  encompassing  traffic  isolation, includes  the  physical  network  infrastructure,  current
prioritization,  and  rate  limiting  for  each  slice.  We network conditions (like congestion or failure states),
depict two key step in the GDM algorithm:
|     |          |             |          |          |          | and |  user |  requirements. |     |  We |  use  | e  to  represent |     |  the |
| --- | -------- | ----------- | -------- | -------- | -------- | --- | ----- | -------------- | --- | --- | ----- | ---------------- | --- | ---- |
| (1) |  Forward |  Diffusion: |  In  our |  system, |  network |     |       |                |     |     |       |                  |     |      |
environment, including both static and dynamic aspects
strategies for each slice begin as initial configurations, that  influence  or  constrain  bandwidth  management
which  are  then  subjected  to  a  controlled  forward strategies. This set of variables includes:
| diffusion |  process. |  This |  involves |  the |  systematic |     |      |     |       |         |            |                          |     |     |
| --------- | --------- | ----- | --------- | ---- | ----------- | --- | ---- | --- | ----- | ------- | ---------- | ------------------------ | --- | --- |
|           |           |       |           |      |             |     |      |     |       | ′;L ′;P | ′;(cid:11) |                          |     |     |
|           |           |       |           |      |             |     | e=fB | ;L  | ;P ;B |         | ;(cid:12)  | ;(cid:13) ;J;C;(cid:27)g |     | (8) |
introduction  of  Gaussian  noise  to  the  contractual u u u i i i u u u t
parameters, akin to incrementally blurring an image. The  AI-driven  network  slicing  design  process

Fig. 6    Adaptive resource management in network slicing using generative diffusion models.

    182 Tsinghua Science and Technology, February 2025, 30(1): 171−185
analyzes  this  environment,  leveraging  data  from  P4 the  meter  configurations  for  each  network  slice,
meters  to  create  and  optimize  network  slices.  We adapting  to  varying  network  conditions  and
| represent  |  the  bandwidth |  management                      |     |  strategies |  as | requirements.                                      |     |     |     |     |     |
| ---------- | --------------- | -------------------------------- | --- | ----------- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
| =fCIR ;PIR | ;CBS            | ;E g, which are adapted based on |     |             |     |                                                    |     |     |     |     |     |
| f          |                 | i;j                              |     |             |     | We introduce the slicing strategy quality network, |     |     |     |     |     |
| s          | s               | s                                |     |             |     |                                                    |     |     |     |     |     |
the environmental conditions. The diffusion model’s Q v, drawing inspiration from the Q-function used in
policy,  (cid:25) (cid:18)(fje),  which  maps  the  states  of  the deep  reinforcement  learning  (DRL).  This  network
environment  to  specific  meter  designs.  This  policy maps each environment-meter pair, fe;fg, to a value
aims  to  output  a  deterministic  meter  design  that that quantifies the expected cumulative reward. This
maximizes expected cumulative rewards over a series process of quantification is pivotal as it captures the
of  time  steps,  effectively  translating  complex anticipated utility from implementing a specific meter
environmental  data  into  actionable  network design policy. It takes into account the prevailing state
configurations.  The  intricate  process  of  reverse of the network and projects the benefits of adhering to
diffusion in the conditional diffusion model is outlined the chosen policy in future operations. Therefore, the
| as                                                 |     |     |     |                           |     | ideal  meter                                             |  design    |  policy,   |  which      |  is  crucial |  for |
| -------------------------------------------------- | --- | --- | --- | ------------------------- | --- | -------------------------------------------------------- | ---------- | ---------- | ----------- | ------------ | ---- |
|                                                    |     |     | ∏N  |                           |     | achieving                                                |  efficient |  bandwidth |  management |              |  and |
| (cid:25) (cid:18)(fje)=p(cid:18)(f0:Nje)=N(fN;0;I) |     |     |     | p(cid:18)(fi(cid:0)1jf;e) |     |                                                          |            |            |             |              |      |
|                                                    |     |     |     |                           | (9) | effective network slicing, is determined as the one that |            |            |             |              |      |
i=1
|     |     |     |     |     |     | optimizes |  this  expected |     |  cumulative |  utility. |  This |
| --- | --- | --- | --- | --- | --- | --------- | --------------- | --- | ----------- | --------- | ----- |
This formulation clarifies the policy as a probability optimization  ensures  that  network  resources  are
distribution, evolving over multiple iterations to refine allocated and managed in the most effective manner,
the  meter  design  towards  an  optimal  state.  As aligning with the dynamic demands of modern network
illustrated  in  Fig. 6,  the  concluding  iteration  of  the environments. Mathematically, this optimal policy can
reverse  diffusion  chain  yields  the  selected  meter be  obtained  by  solving  the  following  optimization
| configuration, |  representing |  the |  optimized |     |  design  for | problem: |     |     |     |     |     |
| -------------- | ------------- | ---- | ---------- | --- | ------------ | -------- | --- | --- | --- | --- | --- |
network resource management. Here, p(cid:18)(fi(cid:0)1jf;e) can
|     |     |     |     |     |     |     | (cid:25)=argminL((cid:18))=(cid:0)E |     |     | (e;f0)] |      |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | ------- | ---- |
|     |     |     |     |     |     |     |                                     |     | [Q  |         | (13) |
b e modeled as a Gaussian distribution N(fi(cid:0)1;(cid:22) (cid:18)(fi;e;i); f0s(cid:25)(cid:18) v
| ∑   |     |     |     |     |     |     | (cid:25)(cid:18) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
p(cid:18)(fi(cid:0)1jf;e)
| (cid:18)(fi;e;i)).  |     | can |  be  modeled |  as |  a  noise |     |     |     |     |     |     |
| ------------------- | --- | --- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- |
As shown in Fig. 6, the strategy quality network,
prediction model wi th the covariance matrix fixed as (e;f), and the strategy generation network operate to
|     |     | ∑   |     |     |     | Q v |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  (fi;e;i)=(cid:27) evaluate and generate resource strategies. They work to
|     |     |     | I   |     | (10) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
i
(cid:18) map  the  environment-resource  pairs  to  an  expected
and mean the mean is constructed to guide the reverse cumulative reward value, fostering an objective-driven
diffusion towards the desired meter design: approach  to  network  resource  management.  As  the
|                            |     | (           |          |                    | )   | process unfolds, the algorithm converges on an optimal |     |     |     |     |     |
| -------------------------- | --- | ----------- | -------- | ------------------ | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- |
|                            |     |             | (cid:27) |                    |     |                                                        |     |     |     |     |     |
| (cid:22) (cid:18)(fi;e;i)= |     | 1 fi(cid:0) | i        | " (cid:18)(fi;e;i) |     |                                                        |     |     |     |     |     |
p p (11) decision for resource allocation strategies, denoted as
|                 | 1(cid:0)(cid:27) |     | 1(cid:0)(cid:28) |     |     |                                                         |     |     |     |     |     |
| --------------- | ---------------- | --- | ---------------- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
|                 |                  | i   |                  |     |     | (cid:25)(cid:3)                                         |     |     |     |     |     |
|                 | ∏                |     |                  |     |     | . This strategy represents the culmination of iterative |     |     |     |     |     |
| where (cid:28)= | i                |     |                  |     |     |                                                         |     |     |     |     |     |
s=1 a s signifies the cumulative product of a
learning and refinement, aimed at achieving the best
sequence  of  parameters  up  to  the  i-th  step,  which possible  alignment  between  network  conditions  and
influences the reverse diffusion process. To initiate the
resource management objectives.
| reverse diffusion, we begin by sampling  |     |     |     |     | fN from a |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
6　Experiment and Analysis
normal distribution with a mean vector of zero and a
covariance matrix of the identity matrix, denoted as For  our  experimental  evaluation,  we  constructed  a
N(0;I). Subsequently, this sampled point is iteratively
network within a Mininet environment, operating on a
refined through the reverse diffusion chain, which is
Linux 18.04 platform, that consists of two P4 switches,
(cid:18),
| parameterized |  by  |  effectively |  tracing |  back |  to  the |     |     |     |     |     |     |
| ------------- | ---- | ------------ | -------- | ----- | -------- | --- | --- | --- | --- | --- | --- |
each establishing connections to four servers. These
optimal meter configuration. switches conform to the P4-16 architecture and are

f i (cid:27) p i n tr ic a te l y   c o n f i g u re d  t o  s u p p o rt   a  s p e c t ru m   o f   u p   to
| fi(cid:0)1jfi= | p   | (cid:0)           | i "              | (cid:18)(fi;e;i)+ | (cid:27) " |     |     |     |     |     |     |
| -------------- | --- | ----------------- | ---------------- | ----------------- | ---------- | --- | --- | --- | --- | --- | --- |
|                |     | (1(cid:0)(cid:27) | 1(cid:0)(cid:28) |                   | i          |     |     |     |     |     |     |
1 (cid:0) (cid:27) i )( i ) e ig h t  p r i or i t y   q u e u e s.  T h i s  c o n fi g u r at i o n   mi r r o r s  t h e
i
(12)
|     |     |     |     |     |     | practical |  bandwidth |  constraints |  of |  contemporary |     |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | ------------ | --- | ------------- | --- |
This network is pivotal in interpreting and optimizing networks,  with  a  1  Gbit/s  bandwidth  per  link,  as

  Wenji He et al.:  A P4-Based Approach to Traffic Isolation and Bandwidth Management for 5G Network Slicing 183

| dictated |  by  the  capacity |     |  of  local |  network |  interface |     |     |     |     |     |     |     |
| -------- | ------------------ | --- | ---------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
cards.
| We  simulate |  traffic  |  flows   |  using |  iPerf, |  generating |     |     |     |     |     |     |     |
| ------------ | --------- | -------- | ------ | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| both  UDP    |  and  TCP |  streams |  to    |  mimic  |  a  variety |  of |     |     |     |     |     |     |
network traffic scenarios. The flows are initiated from
| servers  attached |     |  to  one |  P4  switch |  and |  are |  directed |     |     |     |     |     |     |
| ----------------- | --- | -------- | ----------- | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- |
towards servers on the corresponding switch. To glean
precise measurements of TCP flow round-trip times
(RTT), we employ the Flowgrind tool. This tool is
| indispensable |  for |  our  analysis, |     |  providing |  granular |     |     |     |     |     |     |     |
| ------------- | ---- | --------------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
performance metrics that reveal the impact of different
traffic conditions and switch configurations on network
efficiency.

Adhering to the experimental parameters set forth in
Fig. 7    Dynamic throughput allocation for sliced and non-
| Ref. [10], each of our tests spans a duration of  |     |     |     |     |     | 80  |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sliced traffic in P4 meter.
seconds. The initial 19 seconds are characterized by a
baseline state where no slicing is implemented, serving
Then, we evaluate the performance of the bucket for
as a control for subsequent comparisons. Commencing different  flows.  Figure  8  showcases  a  comparative
from the 20th second and extending to the 39th second,
|     |     |     |     |     |     |     | analysis |  of  throughput |  over |  time |  for  various |  traffic |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | ----- | ----- | ------------- | -------- |
we activate a network slice designed for sliced traffic
flows under our P4-based network slicing strategies.
flows, applying a configuration denoted as S(0:7;0:8)—
|     |     |     |     |     |     |     | This  experimental |     |  insight |  underscores |  the |  nuanced |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | ------------ | ---- | -------- |
indicative of a 0:7 Gbit/s CIR and an 0.8 Gbps PIR.
traffic management capabilities of our P4-based slicing
Subsequently, we introduce a variation in the slicing
system, particularly the efficacy of its bucket strategy
configuration to S(0:2;1) during the interval marked as
in dynamically adjusting to varying load conditions. It
I[40;59], simulating a dynamic adjustment of network
further validates the system’s capability to maintain
policies. This change serves to evaluate the adaptability
|     |     |     |     |     |     |     | fidelity |  to  slice |  specifications, |  guaranteeing |     |  service |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ---------------- | ------------- | --- | -------- |
and responsiveness of the P4 switch under modified
|     |     |     |     |     |     |     | levels  while |  ensuring |  fair |  bandwidth |     |  distribution |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ----- | ---------- | --- | ------------- |
traffic management conditions. Finally, the system is
among concurrent flows.
| reverted |  to  a |  non-sliced |  state, |  allowing |     |  for  a |     |     |     |     |     |     |
| -------- | ------ | ----------- | ------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
Then, we evaluate the performance of the generated
| comparative |  analysis |  against |  the |  predefined |     |  slicing |     |     |     |     |     |     |
| ----------- | --------- | -------- | ---- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
intervals. We set diffusion step N=10, batch size as algorithm  for  bandwidth  allocation  strategy.  As
512, discount factor 0:9, soft target update parameter depicted  in  Fig. 9,  GDM  maintains  a  consistently
(cid:28)=0:003, exploration noise "=0:01, the learning rate higher  reward  trajectory  throughout  the  iterations,
| of the strategy generation network as "         |                |                      |            |             | =10      | (cid:0)5, and |     |     |     |     |     |     |
| ----------------------------------------------- | -------------- | -------------------- | ---------- | ----------- | -------- | ------------- | --- | --- | --- | --- | --- | --- |
|                                                 |                |                      |            |             | (cid:18) |               |     |     |     |     |     |     |
| learning rate of the strategy quality network Q |                |                      |            |             | v as 10  | (cid:0)5.     |     |     |     |     |     |     |
| Figure                                          |  7  presents   |  the                 |  empirical |  results    |  from    |  our          |     |     |     |     |     |     |
| examination                                     |  of            |  traffic  management |            |  via        |  P4      |  switch       |     |     |     |     |     |     |
| metering                                        |  capabilities, |  particularly        |            |  focusing   |          |  on  the      |     |     |     |     |     |     |
| enforcement                                     |  of            |  CIR  and            |  PIR       |  parameters |          |  across       |     |     |     |     |     |     |
network slices. The graph delineates the throughput
over time for both sliced and non-sliced UDP traffic
flows, capturing the nuanced behavior enforced by the
P4 switch’s metering logic. Figure 7 illustrates that the
sliced UDP stream consistently attains a throughput
| that  surpasses                                     |  the              |  CIR |  yet  remains |  below      |  the |  PIR     |     |     |     |     |     |     |
| --------------------------------------------------- | ----------------- | ---- | ------------- | ----------- | ---- | -------- | --- | --- | --- | --- | --- | --- |
| threshold.                                          |  This  phenomenon |      |  is           |  attributed |  to  |  the  P4 |     |     |     |     |     |     |
| switch’s priority queueing mechanism, where the CIR |                   |      |               |             |      |          |     |     |     |     |     |     |
bandwidth is safeguarded within high-priority queues, Fig. 8    Throughput evaluation of token bucket performance
ensuring that the minimum service level is always met.
across different flows.

    184 Tsinghua Science and Technology, February 2025, 30(1): 171−185

|     |     |     |     |     |     | National  Natural |             |  Science |  Foundation |  of       |  China |  (Nos.   |
| --- | --- | --- | --- | --- | --- | ----------------- | ----------- | -------- | ----------- | --------- | ------ | -------- |
|     |     |     |     |     |     | 62325203  and     |  U22B2033), |          |  in         |  part  by |  the   |  General |
Artificial Intelligence computing Chip project for training
in 2022 (No. CEIEC-2022-ZM02-0244) from Kunlunxin
(Beijing) Technology Co., LTDt, and in part by the BUPT
Excellent Ph.D. Students Foundation (No. CX2023147).
References

[1]
H. Zhang, N. Liu, X. Chu, K. Long, A. H. Aghvami, and

V. C. M. Leung, Network slicing based 5G and future
|     |     |     |     |     |     | mobile       |  networks:  | Mobility, |  resource |  management, |           |  and    |
| --- | --- | --- | --- | --- | --- | ------------ | ----------- | --------- | --------- | ------------ | --------- | ------- |
|     |     |     |     |     |     | challenges,  | IEEE        |  Commun.  |  Mag.,    |  vol.        | 55,  no.  | 8,  pp. |
138–145, 2017.
[2] Y. Wu, H. N. Dai, H. Wang, Z. Xiong, and S. Guo, A
|     |     |     |     |     |     |        |                  |     |          |                      |     |      |
| --- | --- | --- | --- | --- | --- | ------ | ---------------- | --- | -------- | -------------------- | --- | ---- |
|     |     |     |     |     |     | survey |  of  intelligent |     |  network |  slicing  management |     |  for |
Fig. 9    Performance of GDM vs. RL algorithms.
|     |     |     |     |     |     | industrial      |  IoT:  | Integrated |               |  approaches |  for       |  smart |
| --- | --- | --- | --- | --- | --- | --------------- | ------ | ---------- | ------------- | ----------- | ---------- | ------ |
|     |     |     |     |     |     | transportation, |        |  smart     |  energy,  and |  smart      |  factory,  | IEEE   |
reflecting its superior capability to converge on optimal Commun. Surv. Tutorials, vol. 24, no. 2, pp. 1175–1211,
| network slicing strategies. In contrast, PPO and DDPG |     |     |     |     |     | 2022. |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
[3] S. Zhang, An overview of network slicing for 5G, IEEE
| exhibit  fluctuations |     |  in |  reward  optimization, |     |  with |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ---------------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |

Wirel. Commun., vol. 26, no. 3, pp. 111–117, 2019.
DDPG demonstrating more significant variance. This
[4] Z. Shu and T. Taleb, A novel QoS framework for network

variability  might  indicate  a  sensitivity  to  initial slicing in 5G and beyond networks based on SDN and
conditions  and  a  longer  path  to  convergence  for NFV, IEEE Netw., vol. 34, no. 3, pp. 256–263, 2020.
[5] C. Bektas, S. Monhof, F. Kurtz, and C. Wietfeld, Towards
traditional reinforcement learning approaches.

5G: An empirical evaluation of software-defined end-to-
7　Conclusion and Future Work end network slicing, in Proc. IEEE Globecom Workshops
(GC Wkshps), Abu Dhabi, United Arab Emirates, 2018,
| In  this  research, |     |  we  have |  developed |  an |  integrated | pp. 1–6. |     |     |     |     |     |     |
| ------------------- | --- | --------- | ---------- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
framework for network slicing resource management [6] P. Bosshart, D. Daly, G. Gibb, M. Izzard, N. McKeown, J.

|                |      |          |               |     |         | Rexford, |  C.  Schlesinger, |     |  D. |  Talayco, |  A.  Vahdat, |  G. |
| -------------- | ---- | -------- | ------------- | --- | ------- | -------- | ----------------- | --- | --- | --------- | ------------ | --- |
| that  exploits |  the |  dynamic |  capabilities |     |  of  P4 |          |                   |     |     |           |              |     |
Varghese, et al., SIGCOMM Comput. Commun. Rev., vol.
| programmable |  switches |  and |  open-source |     |  controllers. |     |     |     |     |     |     |     |
| ------------ | --------- | ---- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
44, no. 3, pp. 87–95, 2014.
The inclusion of a generative diffusion model within
[7] Y. W. Chen, L. H. Yen, W. C. Wang, C. A. Chuang, Y. S.

the  control  plane  has  significantly  enhanced  our Liu, and C. C. Tseng, P4-enabled bandwidth management,
in Proc. 2019 20th Asia-Pacific Network Operations and
system’s responsiveness to the diverse requirements of
|     |     |     |     |     |     | Management |     |  Symposium  | (APNOMS), |     |  Matsue, |  Japan, |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | --------- | --- | -------- | ------- |
5G services. This novel GAI-centric approach allows
2019, pp. 1–5.
for dynamic resource allocation that is adaptable to
[8] E. Hauser, M. Simon, H. Stubbe, S. Gallenmüller, and G.

changing network conditions, ensuring optimal traffic Carle, Slicing networks with P4 hardware and software
differentiation and service quality. Looking forward, targets, in Proc. ACM SIGCOMM Workshop on 5G and
the  framework  will  need  to  be  expanded  to Beyond  Network  Measurements,  Modeling,  and  Use
Cases, Amsterdam, the Netherlands, 2022, pp. 36–42.
accommodate the complexities of shared infrastructure
[9] S. Y. Wang, H. W. Hu, and Y. B. Lin, Design and
| scenarios, |  particularly |  in |  multi-operator |     |  hardware |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | --------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
implementation of TCP-friendly meters in P4 switches,
environments. Additionally, future developments will IEEE/ACM Trans. Netw., vol. 28, no. 4, pp. 1885–1898,
| focus on the imperative of energy efficiency, with the |     |     |     |     |     | 2020. |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
[10] Y. W. Chen, C. Y. Li, C. C. Tseng, and M. Z. Hu, P4-
| aim of designing P4-based mechanisms that optimize |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TINS: P4-driven traffic isolation for network slicing with
| network  operations |     |  for  reduced |  power |  consumption |     |     |     |     |     |     |     |     |
| ------------------- | --- | ------------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
bandwidth guarantee and management, IEEE Trans. Netw.
through smarter traffic shaping and resource allocation
Serv. Manag., vol. 19, no. 3, pp. 3290–3303, 2022.
strategies,  aligning  network  advancements  with [11] Z. Chen, Z. Zhang, and Z. Yang, Big AI models for 6g

sustainable energy practices. wireless networks: Opportunities, challenges, and research
directions, arXiv preprint arXiv: 2308.06250, 2023.
Acknowledgment [12] J.  Ho,  A.  Jain,  and  P.  Abbeel,  Denoising  diffusion

|     |     |     |     |     |     | probabilistic |  models,  |     | Advances |  in  neural |  information |     |
| --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | -------- | ----------- | ------------ | --- |
This work was in part supported by the funding from the
processing systems, vol. 33, pp. 6840–6851, 2020.

Wenji He et al.: A P4-Based Approach to Traffic Isolation and Bandwidth Management for 5G Network Slicing 185
[13] H. Du, R. Zhang, Y. Liu, J. Wang, Y. Lin, Z. Li, D. and C. E. Rothenberg, Packet-optical differentiated
Niyato, J. Kang, Z. Xiong, S. Cui, et al., Beyond deep survivability implemented by P4 slices and gNMI
reinforcement learning: A tutorial on generative diffusion telemetry, in Proc. Optical Fiber Communication Conf.
models in network optimization, arXiv preprint arXiv: (OFC) 2023, San Diego, CA, USA: Optica Publishing
2308.05384, 2023. Group, 2023, pp. M1G–3.
[14] D. Bega, M. Gramaglia, M. Fiore, A. Banchs, and X. [19] M. Xu, H. Du, D. Niyato, J. Kang, Z. Xiong, S. Mao, Z.
Costa-Perez, DeepCog: Cognitive network management in Han, A. Jamalipour, D. I. Kim, V. Leung, et al.,
sliced 5G networks with deep learning, in Proc. IEEE Unleashing the power of edge-cloud generative AI in
INFOCOM 2019 - IEEE Conf. Computer mobile networks: A survey of aigc services, arXiv preprint
Communications, Paris, France, 2019, pp. 280–288. arXiv: 2303.16129, 2023.
[15] S. Jošilo and G. Dán, Joint wireless and edge computing [20] Y. Huang, M. Xu, X. Zhang, D. Niyato, Z. Xiong, S.
resource management with dynamic network slice Wang, and T. Huang, Ai-generated 6g internet design: A
selection, IEEE/ACM Trans. Netw., vol. 30, no. 4, pp. diffusion model-based learning approach, arXiv preprint
1865–1878. arXiv: 2303.13869, 2023.
[16] A. Thantharate and C. Beard, ADAPTIVE6G: Adaptive [21] X. Huang, P. Li, H. Du, J. Kang, D. Niyato, D. I. Kim, and
resource management for network slicing architectures in Y. Wu, Federated learning-empowered AI-generated
current 5G and future 6G systems, J. Netw. Syst. Manag., content in wireless networks, arXiv preprint arXiv:
vol. 31, no. 1, pp. 9, 2022. 2307.07146, 2023.
[17] T. Mai, H. Yao, N. Zhang, W. He, D. Guo, and M. [22] H. Du, R. Zhang, D. Niyato, J. Kang, Z. Xiong, D. I. Kim,
Guizani, Transfer reinforcement learning aided distributed X. S. Shen, and H. V. Poor, Exploring collaborative
network slicing optimization in industrial IoT, IEEE distributed diffusion-based AI-generated content (AIGC)
Trans. Ind. Inf., vol. 18, no. 6, pp. 4308–4316, 2022. in wireless networks, IEEE Netw., pp. 1–8, 2024.
[18] R. P. Pinto, K. S. Mayer, D. S. Arantes, D. A. A. Mello,
Haipeng Yao is a professor in Beijing Wenji He received the bachelor degree
University of Posts and from Beijing University of Posts and
Telecommunications. He received the PhD Telecommunications in 2021. She is
from Beijing University of Posts and pursuing the PhD degree at School of
Telecommunications in 2011. His research Information and Communication
interests include future network Engineering, Beijing University of Posts
architecture, network artificial intelligence, and Telecommunications. Her research
networking, space-terrestrial integrated interests are in the areas of intelligent
network, network resource allocation, and dedicated networks. network and the programmable network.
He has published more than 150 papers in prestigious peer-
reviewed journals and conferences. Dr. Yao has served as an Yunjie Liu received the BS degree in
associate editor of IEEE Transactions on Mobile Computing, technical physics from Peking University,
and IEEE Transactions on Sustainable Computing. He has also Beijing, China, in 1968. He is currently the
served as a member of Technical Program Committee as well as academician of China Academy of
Symposium Chair for a number of international conferences, Engineering, the chief of the Science and
including IWCMC 2019 Symposium Chair, and ACM TUR-C Technology Committee of China Unicom,
SIGSAC2020 Publication Chair. and the dean of School of Information and
Communication Engineering, BUPT. His
Huan Chang is an assistant professor with research interests include next generation networks and network
School of Information and Electronics, architecture and management.
Beijing Institute of Technology (BIT). She
received the PhD degree from Beijing
University of Posts and
Telecommunications (BUPT), China, in
2020. Her main research interests include
large-capacity optical communication and
adaptive optics.