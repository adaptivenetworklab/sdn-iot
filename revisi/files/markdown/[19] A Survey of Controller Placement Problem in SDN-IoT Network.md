# [19] A Survey of Controller Placement Problem in SDN-IoT Network

> Source file: `[19] A Survey of Controller Placement Problem in SDN-IoT Network.pdf`

---

International Journal of Networked and Distributed Computing (2024) 12:170–184
https://doi.org/10.1007/s44227-024-00035-y
REVIEW ARTICLE
A Survey of Controller Placement Problem in SDN‑IoT Network
Amel Abderrahmane1 · Hamza Drid1 · Amel Behaz1
Received: 12 April 2024 / Accepted: 10 July 2024 / Published online: 25 July 2024
© The Author(s) 2024
Abstract
The Internet of Things (IoT) refers to the billions of intelligent physical devices connected to the Internet for collecting and
sharing data. However, implementing IoT in large-scale industrial applications presents numerous challenges, including
network management and scalability. These challenges encompass: complex network management tasks that are increasingly
difficult to maintain, increased network resource usage, mobility, and high energy consumption. Software-defined networking
(SDN) addresses these limitations by enforcing centralized control of all devices and leveraging a global network view. SDN
is a networking paradigm that separates the control plane from the data plane, allowing managers to centralize the control of
the network infrastructure. For large networks, such as IoT networks, multiple controllers are needed to manage the network
efficiently. The Controller Placement Problem (CPP) involves the challenge of deploying the optimal number of controllers
in a network while satisfying specific performance requirements such as latency, load balancing, and computation time. This
paper provides an overview of recent research efforts addressing CPP issues in the SDN-IoT domain.
Keywords Internet of Things (IoT) · Software-Defined Networking (SDN) · Controller Placement Problem (CPP) ·
SDN-IoT
1 Introduction
revolutionary technology due to the vast number of con-
nected devices and the enormous volumes of data they gen-
According to Kevin Ashton [1], the Internet of Things is at erate. However, managing contemporary networks is chal-
the forefront of the second digital revolution. IoT refers to lenging, and the existing centralized computing and storage
the interconnected network of physical devices embedded models are increasingly insufficient. Future IoT solutions
with sensors, software, and other technologies, enabling will necessitate novel technologies to analyze, filter, and
them to collect and exchange data. This facilitates higher aggregate data at the network level. The diverse nature of
levels of automation, efficiency, and real-time insights across IoT data (in terms of type, semantics, frequency, location,
various industries. However, one of the inherent complexi- and time) and the issues of integration, scalability, secu-
ties of IoT is its extensive scale. The large number of gate- rity, and privacy present significant obstacles to success-
ways and network devices required for high scalability also ful IoT deployments. Therefore, there is an urgent need for
introduces significant management challenges. innovative technologies and approaches to enhance existing
Metcalfe’s Law [2] posits that as the number of inter- networks.
connected devices increases, the value of communication Software-defined networking (SDN) [3] has emerged as
networks grows exponentially. Consequently, IoT offers a promising solution to these challenges. SDN is a network-
substantial benefits, as billions of interconnected items are ing paradigm that separates the control plane from the data
expected to populate future networks. IoT is considered a plane, allowing network administrators to program and man-
age network behavior dynamically and centrally via software
applications. This decoupling facilitates direct network pro-
Authors equally contributed to this work. gramming, offering numerous benefits [4, 5], such as sim-
plified network management, improved network utilization
*
Amel Abderrahmane efficiency, and enhanced support for network innovation.
a.abderrahmane@univ-batna2.dz
SDN supports a centralized control model wherein net-
1 LAMIE Laboratory, Department of Computer Science, work intelligence is logically centralized in software-based
University of Batna 2, 05078 Batna, Algeria
Vol:.(1234567890)

International Journal of Networked and Distributed Computing (2024) 12:170–184 171
controllers that maintain a global view of the network. The and potential advancements, offering a detailed analysis of
combination of IoT and SDN, referred to as SDN-IoT, lever- their effectiveness and limitations. Section 5 concludes the
ages the strengths of both technologies to address network paper by summarizing the key findings, emphasizing the
challenges effectively. IoT benefits from SDN’s central- critical importance of resolving the CPP for the efficient
ized control and programmability, which help manage the deployment of SDN-IoT networks, and proposing future
massive scale, diversity, and complexity of IoT networks. research directions to guide ongoing and upcoming efforts
Conversely, SDN gains from IoT’s extensive data genera- in this evolving field.
tion capabilities, enhancing its ability to optimize network
operations and innovate.
2 Background
Initial SDN implementations, such as OpenFlow [4],
assumed a single controller to manage the network. How-
ever, as SDN networks have evolved, it has become apparent In this section, we introduce the basic architecture of IoT,
that a single controller is insufficient to meet extensive man- the SDN, and the new term SDN-IoT. Following that, we
agement requirements [7]. To address this, logically central- examine the various difficulties encountered within the
ized yet physically distributed multi-controller architectures, SDN-IoT network before presenting the comprehensive for-
such as HyperFlow [8], Kandoo [9], and Onix [10], have mulation and optimized objective of the controller place-
been developed. These architectures aim to enhance net- ment problem.
work scalability and reliability while avoiding single points
2.1 Internet of Things
of failure [11].
One of the critical issues in multi-controller SDN net-
works is the Controller Placement Problem. The CPP 2.1.1 Introduction to IoT
involves determining the optimal number and placement of
controllers in network why significantly impact network per- Kevin Ashton [1] first proposed the idea of the Internet of
formances. This study provides an in-depth analysis of the Things in 1999 as a network of connected items that could
challenges associated to the CPP in SDN-IoT networks. We each have a unique identification using RFID technology.
present a comprehensive review of solutions proposed in the Since then, the concept has evolved significantly, encom-
literature, categorizing them into mono-objective and multi- passing a vast array of interconnected devices that can trans-
objective optimization solutions based on their performance mit, receive, and link to each other using embedded sensors,
improvements. Before discussing representative models and software, and other technologies.
detailing the results of various solutions, we examine the
fundamental factors of each optimization objective and their 2.1.2 Definition of IoT
impact on network performance.
The IoT generally refers to a dynamic global network archi-
1.1 Summary of the Article’s Contributions
tecture characterized by self-configuring capabilities, built
on widely acknowledged standards and communication pro-
• Present the first survey of the Controller Placement Prob- tocols. It includes a wide range of networked devices con-
lem in the SDN-IoT network, considering literature and nected to the internet, allowing them to transmit, receive,
industrial works. and interact seamlessly. These IoT devices, equipped with
• Provide an overview of the emergence of IoT from tradi- tiny computers, can communicate and operate within the
tional networks to SDN-IoT environments. global network, facilitating higher levels of automation,
• Present a classification of CPP approaches in IoT-SDN efficiency, and real-time insights across various industries.
environments. [12, 40, 41]
• Highlight the open research challenges and future
research trends in the SDN-IoT environments. 2.1.3 Architecture of IoT
This paper is structured as follows: Section 2 provides The architecture of the IoT consists of the following layers
a comprehensive overview of the Internet of Things, Soft- Fig. 1.
ware-Defined Networking, SDN-IoT, and the Controller
Placement Problem (CPP). Sections 3 to 4 discuss the cur- • Perception layer: composed of physical objects that can
rent state of research, examining various methodologies, detect physical quantities, [13] (such as heat, humidity,
approaches, and solutions proposed in the literature to vibration, radiation, and others) and convert them into
address the CPP within SDN-IoT environments. These sec- digital magnitudes. This information is processed, stored,
tions also highlight practical implementations, case studies, and transmitted wirelessly to a sink or a network gate-

1 72 International Journal of Networked and Distributed Computing (2024) 12:170–184
necessitates the adoption of new technologies to enhance
IoT network services, such as the innovative paradigm of
SDN. SDN offers centralized control and dynamic network
configuration, enabling the efficient management of exten-
sive IoT deployments. It optimizes resource utilization by
facilitating real-time allocation based on current demand,
enhances security through uniform policy enforcement,
and supports energy management by optimizing com-
munication paths to minimize power consumption. Fur-
thermore, SDN facilitates network function virtualization
(NFV), allowing the deployment of virtualized network
functions on standard hardware, thereby reducing costs
and increasing flexibility. SDN’s programmability enables
adaptive routing and traffic management, ensuring reli-
able data delivery across geographically dispersed IoT
devices. Consequently, SDN is an indispensable technol-
ogy for addressing the scalability, efficiency, and security
requirements of future IoT environment.[43].
2.2 Software‑Defined Netwoking
Fig. 1 IoT Architecture
2.2.1 Introduction to SDN
way. This layer includes technologies such as: Wireless
sensors [14], RFID [15], smartphones [16], wearables, In the fast-changing field of network management, SDN
intelligent homes [17], smart automobiles [18], and many has emerged as a groundbreaking approach, significantly
other technologies. simplifying and optimizing the control and operation of
• Network layer: it sends the digital information gathered network infrastructure. Traditional networking paradigms,
in analog form from the physical world to a sink or a characterized by the tight coupling of the control plane and
network gateway for further processing. [13]. Numer- data plane, often lead to complex and inefficient network
ous technological advancements may be found in this management. SDN addresses these challenges by introduc-
context, including low-energy Bluetooth [14], Lorawan ing a centralized, programmable network architecture that
[16], wifi [19], Zigbee [20], and others. enhances flexibility, scalability, and efficiency. [21].
• Middleware layer: Allows several Internet of Things
devices inside a shared domain to communicate with
one compatible device at a time. In order to do this, it 2.2.2 Definition of SDN
transforms transmitted data into service information by
pulling it out of different hardware components. The SDN is a networking paradigm that decouples the control
requested service’s address and management services plane from the data plane in network devices, allowing
are included in this service information. for centralized management and dynamic configuration
• Application layer: It acts as a user interface for informa- of the network. This separation is facilitated by an appli-
tion gathered from the perception layer, allowing users to cation programming interface (API) that enables com-
modify the data to meet the needs of a particular domain munication between the SDN controller and the network
and process it in a processing system. [42]. devices. The controller, through a programmable inter-
face on the switches, implements rules and manages traffic
2.1.4 Challenges in IoT flows independently of the underlying infrastructure. SDN
transforms traditional network management by providing a
Future IoT applications will face increasing demands centralized control mechanism that oversees multiple net-
and challenges as billions of connected devices become work devices, ensuring efficient traffic flow and optimized
commonplace. These challenges encompass network network performance. This innovative approach not only
management, network function virtualization, ubiquitous simplifies network operations but also enhances the overall
information access, resource utilization, energy manage- agility and responsiveness of the network.
ment, security, and privacy. Addressing these challenges

International Journal of Networked and Distributed Computing (2024) 12:170–184 173
2.2.3 Model of the SDN • The Southbound API enables communication between
the control plane and the data plane, allowing rules to be
The SDN architecture contains the following layers as applied to routers, switches, wireless access points, and
depicted in Fig. 2: other devices directly [23].
• Application layer: Also known as the management plan
[13], this layer enables applications to use northbound 2.2.4 Impact of SDN on IoT Network
APIs to express network management policies that will
be converted into commands by the controller and put The goal of SDN in an IoT is to provide a flexible and scala-
into effect on network equipment directly through south- ble infrastructure that can efficiently manage and control the
bound APIs. large number of devices and data generated by IoT devices.
• Control plan: This segment has been separated from net- Some specific goals of SDN in an IoT network include:
work devices and consolidated onto the SDN controller.
This separation enables the translation of management • Centralized Control: SDN enables administrators to man-
policies from application-defined rules into directives age and control the network centrally, making it easy to
for incoming flows. These rules are then injected into configure, track, and manage IoT devices and their con-
network routing devices using southbound APIs. The nectivity.
controller also facilitates the implementation of specific • Dynamic Resource Allocation: SDN enables the dynamic
constraints on equipment, such as restricting the trans- allocation of network resources according to the shifting
mission of all ICMP packets except those with a destina- needs of IoT devices. This guarantees optimal perfor-
tion IP address of X. Conversely, ICMP packets with a mance and efficient resource use.
destination IP address of X are exclusively transmitted • Security: SDN offers improved security functionalities
through port Y. through the centralized definition and enforcement of
• Data plan: Depending on the connection module used security policies by administrators. The technology facil-
in equipment for message routing from end to end, calls itates the timely identification, prevention, and mitigation
also have a transfer plan [13], which involves connecting of potential risks throughout the entire IoT network.
equipment via wired cables or radio frequencies. • Scalability: SDN facilitates seamless scalability by
• The APIs: The SDN model uses four distinct APIs to accommodating the integration of additional IoT devices
communicate between its components: Northbound API, into the network. The system offers a flexible framework
Southbound API, Eastbound API, and Outbound API. capable of handling the increasing number of devices
• The Northbound API enables communication between while maintaining optimal performance and ease of man-
the application layer and the control layer [22]. Through agement.
this interface, the controllers receive the application's • Traffic Optimization: SDN enables intelligent traffic rout-
quality of service requirements, which adds a layer of ing and load balancing in IoT network, ensuring efficient
network abstraction and presents the network as a system data transfer between devices, gateways, and cloud ser-
[13]. vices.
• Service Orchestration: SDN facilitates service orches-
tration in an IoT network by providing a programmable
infrastructure that dynamically adapts to changing ser-
vice requirements.
2.3 SDN‑IoT
2.3.1 Introduction to SDN‑IoT
Qin et al. [24] developed an innovative framework to inte-
grate SDN with IoT. This early work aimed to address the
complexities of managing diverse IoT environments using
the flexible and programmable features of SDN. By lev-
eraging SDN’s centralized control and dynamic resource
allocation capabilities, the framework seeks to enhance the
Fig. 2 SDN Architecture efficiency and scalability of IoT networks.

1 74 International Journal of Networked and Distributed Computing (2024) 12:170–184
2.3.2 Definition of SDN‑IoT SDN, the SDN controller can determine the optimal path
and establish the necessary rules for the ingress of data
The proposed framework is designed to optimize hetero- flow into the network equipment. This results in a reduc-
geneous architectures within SDN-IoT networks. It sup- tion of network resource utilization and an enhancement
ports various devices, networks, and technologies within of network efficiency.
the IoT ecosystem, utilizing SDN for enhanced network • Energy management optimization: the connection of
management and optimization. Key features of the frame- billions of devices to the IoT network would generate a
work include the ability to dynamically allocate network substantial amount of data, necessitating the establish-
resources, implement centralized security policies, and intel- ment of numerous data centers to handle this processing.
ligently route traffic to ensure optimal performance. Addi- Given the significant electrical energy requirements asso-
tionally, the framework facilitates the seamless integration of ciated with operating data centers, it becomes imperative
new IoT devices and technologies, providing a versatile and to construct data centers prioritizing energy efficiency.
scalable infrastructure for evolving IoT environments. This This can be achieved using intelligent energy manage-
allows for improved interoperability and coordination among ment systems, effectively mitigating energy consump-
a wide range of IoT devices, ensuring that the network can tion. To establish energy-efficient IoT data centers based
adapt to changing conditions and demands while maintain- on SDN, SDN technology will facilitate the efficient rout-
ing high levels of performance and security. ing of network traffic. This will be accomplished through
the SDN controller, directing the network traffic to the
2.3.3 IoT Network Requirements for SDN appropriate server. Additionally, SDN technology will
enable the activation or deactivation of data center equip-
This section investigates several limitations in deploying IoT ment based on their energy consumption levels.
networks to enhance various urban activities. These limita-
tions can be addressed by using SDN, effectively realizing 2.3.4 SDN‑IoT Architecture
the concept that “SDN-IoT.” We identify and differentiate
these limitations as follows: Three layers presented in (Fig. 3) make up the SDN based
IoT architecture:
• Efficient network management: the proliferation of
Internet of Things technologies will soon facilitate the • Infrastructure Layer: it consists of various RFID [18]
connection of many objects to the internet, generating gadgets, wireless sensors [25], detection-capable smart
substantial volumes of data that necessitate effective and phones [17], smart cars [14], and other gadgets. The con-
efficient processing. Managing these devices and their nectivity of these devices to the access layer is estab-
significant data volumes requires a robust approach. By lished through wireless access points, base stations, and
adopting a global network perspective and implementing network gateways, facilitating their connection to the
centralized data control, SDN technology facilitates the broadband backbone. Within the context of the SDN-
management and distribution of traffic flow to reduce IoT architecture, it is crucial to remember that the nodes
latency and achieve load balancing within the network. involved primarily function as conduits for data transmis-
Integrating SDN into IoT networks would enhance load sion, thereby relinquishing the responsibility of higher-
balancing and improve the precision of message trans- level decision-making and control to the SDN controller.
portation, enabling optimal utilization of bandwidth • Control Layer: the intermediate layer facilitates the con-
resources. nection between the application and infrastructure layers,
• Mobility: The IoT will connect billions of devices over allowing developers to construct IoT applications through
the next several years, and users must be able to use all accessible APIs. Additionally, it enables the direct imple-
of their devices' features and easily access the IoT net- mentation of rules onto network hardware to effectively
work at any time and from any location. SDN technology manage the underlying infrastructure at a lower level.
enables efficient management of these devices, ensuring The SDN controller operates at this layer and allocates
smooth handling of users' mobility [13]. diverse hardware resources among the applications
• Remedy the heavy use of network resources: to enhance across different industries. Furthermore, it facilitates the
network efficiency, it is essential to develop a pre-estab- routing of data with the requisite quality of service to end
lished strategy for the desired quality of service and set users situated in the network's core.
up the network infrastructure to facilitate efficient traf- • Application Layer: to optimization of IoT applications,
fic engineering. Excessive network utilization by users the application layer offers a complete separation from
places a heavy burden on network equipment, diminish- the underlying network transport and data connection
ing its operational efficiency. Through the utilization of layers. This is achieved by utilizing northbound APIs,

International Journal of Networked and Distributed Computing (2024) 12:170–184 175
Fig. 3 SDN-IoT Architecture
allowing seamless interaction with the network infra- According to Heller et al.’s research [26], the CPP is an
structure. NP-hard issue that was first examined to identify an optimal
solution site. Since then, other research teams have worked
Overall, SDN-IoT networks provide a robust, secure, scal- to find a solution. The gap between controllers was consid-
able, and efficient infrastructure that can support the diverse ered a problem in research by Ishigaki et al. [27], who sug-
requirements of IoT applications and services. Since the first gested that bringing the controllers closer together would
SDN-IoT framework proposal, numerous research papers resolve this issue.
have emerged. The increasing number of devices (nodes, St-Hilaire and Sallahi [28] determined the ideal site,
controllers, and switches) in the network, underscores the amount, and type of controllers to use for a CPP. They also
critical importance of placing controllers in relation to rout- decided which connections should be made between each
ing nodes in an SDN-IoT-based design. This challenge is network component. Their model aims to reduce network
widely known in the literature as the Controller Placement costs while considering other constraints. Akbar Neghabi
Problem. et al. [29] proposed a nature-inspired method for load bal-
ancing in SDN. [30] Introduced a heuristic technique for
controller placement based on learning automata (LA). [31]
2.4 Controller Placement Problem (CPP)
Developed a novel routing protocol to reduce power con-
sumption by heterogeneous devices.
It consists of finding the optimal controller placement to
optimize one or more performance metrics, such as, latnecy,
2.4.2 Performance Impacted by CPP
capacity of the controllers, load balancing and energy con-
sumption. The controller placement problem seeks to answer
Heller et al. [26] started by examining the effects of con-
two main questions:
troller placement on network maximum and average delay.
Other goals have been set, such as load balancing, reliabil-
• How many controllers should be used in the SDN-IoT
ity, and energy conservation. Multi-objective optimization
network?
has also proven to be a viable option when conflicts exist
• What is the best location for each controller?
between multiple objectives.
2.4.1 General formulation of CPP • Latency: is the time between sending and receiving a
data message. It measures how long a data packet takes
The SDN-IoT network is modelled as a graph G=(V, E, S) to travel from one place to another. Several factors can
∈
in which each node v V represents an IoT device (router, affect latency, including network congestion, the distance
∈
switch, and any other component), and edge e E is the between devices, and processing times at either end of
physical connection that represents the communication link the connection.
between these nodes. S represents the set of controllers • Load-Balancing: distributes network traffic among
in the network. In particular k=S denotes the number of several servers or other network devices. The goals of
controllers. load-balancing are to optimize resource usage, increase

1 76 International Journal of Networked and Distributed Computing (2024) 12:170–184
throughput, reduce response times, and prevent overload WO component refines these solutions by simulating the
on any device. bubble-net hunting strategy of humpback whales, updat-
• Reliability: is the extent to which a system can be relied ing positions through spiral and shrinking mechanisms.
upon to perform its intended function under given cir- These steps are iteratively repeated, with fitness evalua-
cumstances for a specific period. Reliability is crucial in tions, selection, crossover, mutation, and WO optimiza-
various industries, including engineering, manufacturing, tion, until the maximum number of iterations is reached
transportation, healthcare, and technology. or a satisfactory solution is found.
• Energy-Saving: involves consuming less energy to Results from MATLAB simulations on three different
protect the environment and natural resources. Using network topologies—TataNld, Deutsche, and Forthnet—
energy-efficient equipment, reducing unnecessary energy demonstrate the DEWO algorithm's effectiveness. The
consumption, and utilizing renewable energy sources are algorithm consistently achieved lower average and maxi-
just a few ways to accomplish this. Energy conservation mum latencies compared to other metaheuristic algorithms
has a positive impact on the environment, reduces energy like Genetic Algorithm (GA), Particle Swarm Optimiza-
costs, and promotes sustainability. tion (PSO), and Firefly Algorithm (FFA). For instance, in
the TataNld topology, DEWO reduced average latency by
approximately 7.82% compared to PSO and 2.35% com-
3 Related Works
pared to FFA. Similar improvements were observed in the
Deutsche and Forthnet topologies. The DEWO algorithm
In this section, we comprehensively explore all existing solu- also maintained better scalability and performance stabil-
tions within this domain, systematically classifying them ity as the number of controllers increased, demonstrating
into two distinct subclasses based on the extent of perfor- its robustness in handling large-scale networks. However,
mance enhancements: mono-objective and multi-objective the DEWO algorithm has several limitations. The hybrid
optimization. nature of the algorithm results in increased computational
complexity and longer computation times, especially for
3.1 Mono‑Objective
very large networks. Parameter sensitivity is another issue,
as the effectiveness of the DEWO algorithm depends on
The solutions presented in this section are focused on the appropriate selection of parameters such as crossover
enhancing a specific metric, namely latency (between rate (Cr) and scaling factor (Fr). Additionally, the algorithm
switch-controller and controller-controller): assumes static network topologies, which may not reflect
Keshari et al. [32] introduce an innovative hybrid Dif- the dynamic nature of real-world smart city environments
ferential Evolution and Whale Optimization (DEWO) algo- where network topologies frequently change. The focus on
rithm to solve the CPP in SDN for IoT-enabled smart cities. latency minimization and single-objective optimization also
SDNs separate control logic from the hardware data plane, limits the algorithm's applicability in scenarios requiring a
enabling centralized and programmable management of net- comprehensive approach to network performance, consid-
work devices, which is crucial for efficiently handling the ering factors such as energy efficiency, fault tolerance, and
vast number of IoT devices generating significant data in security. Addressing these limitations in future research will
smart city environments. Traditional IoT networks face chal- be essential to further enhance the DEWO algorithm’s appli-
lenges such as access delays, security issues, and reliabil- cability and performance in real-world SDN-IoT networks
ity concerns, which SDN-enabled networks can overcome. for smart cities.
However, a single controller is insufficient for managing the Ali et al. [33] present a comprehensive approach to
extensive network of IoT devices, necessitating multiple address the CPP in SDN for IoT environments. The SDN
controllers. This solution aims to optimize the placement of paradigm decouples the control plane from the data plane,
these controllers to enhance network performance. enabling centralized management of network devices. This
The DEWO algorithm methodology begins with the ini- separation is particularly advantageous for IoT networks,
tialization of population parameters for Differential Evo- which involve numerous devices generating substantial
lution (DE) and Whale Optimization (WO). The process data. In an SD-IoT setup, sensors frequently exchange data
involves extracting node locations based on longitude and with controllers, and inappropriate placement of these con-
latitude from the network topology and setting initial pop- trollers can significantly increase end-to-end (E2E) latency.
ulations. Fitness functions are defined to minimize both The authors propose a novel clustering strategy leveraging
switch-to-controller and controller-to-controller laten- the Analytical Network Process (ANP), a multi-criteria
cies. The DE component performs mutation and crosso- decision-making (MCDM) method, to optimize controller
ver operations to generate new candidate solutions, ensur- placements, improving network performance by reducing
ing diversity and avoiding premature convergence. The latency and balancing the load across controllers.

International Journal of Networked and Distributed Computing (2024) 12:170–184 177
The methodology begins by modeling the SDN network applications where quick decision-making is necessary.
as a graph and segmenting it into clusters. Each cluster's Although the proposed method shows good scalability,
switches are identified, and criteria such as hop count, handling an increased number of controllers and nodes,
propagation latency, queuing latency, path computation there may still be challenges when applied to extremely
latency, and link utilization are defined for evaluating the large-scale networks. The performance of the method could
placement of controllers. The ANP model is used to rank degrade as network size grows beyond the tested topologies.
switches within each cluster, determining the optimal loca- The effectiveness of the ANP model depends on the appro-
tions for controllers. The process involves creating pairwise priate selection of parameters for criteria such as hop count,
comparison matrices for each criterion, normalizing these propagation latency, and others. Incorrect parameter set-
matrices, and calculating eigenvectors to determine the pri- tings can lead to suboptimal solutions or slow convergence,
ority of each switch. The final placements are refined by requiring extensive experimentation and domain knowledge
ensuring consistency through indices such as the Consist- to fine-tune. The approach assumes static network topolo-
ency Index (CI) and Consistency Ratio (CR), making sure gies, which may not reflect the dynamic nature of real-world
the judgments are coherent. IoT networks where topologies frequently change due to
Results from simulations conducted on four network mobility or varying load conditions. Adapting the model to
topologies (OS3E, US_Net, Abilene, and Interoute) using handle dynamic and adaptive network topologies requires
Mininet and Matlab demonstrate that the proposed ANP- further research and development. The primary focus is
based clustering strategy significantly reduces E2E delay on minimizing latency (both E2E and C2C) and balancing
compared to the standard k-means algorithm. The authors the load. While this is crucial, other important factors like
found that the ANP method not only minimizes delays energy efficiency, fault tolerance, and security are not explic-
between switches and controllers but also reduces control- itly addressed. A more comprehensive approach considering
ler-to-controller (C2C) delays and communication overhead. multiple performance metrics simultaneously would provide
For instance, in the Abilene topology, the total E2E delay a more holistic solution to the CPP. The current implemen-
was significantly reduced using the ANP-based approach tation focuses on single-objective optimization, primarily
compared to the k-means algorithm. The reduction in delay minimizing latency. However, real-world network optimi-
is attributed to the more effective placement of controllers zation often involves multiple conflicting objectives such
as per the defined criteria, which ensures better allocation as cost, reliability, and throughput. Extending the approach
of switches to controllers. The proposed method also dem- to support multi-objective optimization could enhance its
onstrated a decrease in C2C delay. The correct positioning applicability and effectiveness in diverse network scenarios.
of controllers, considering multiple criteria, contributes In conclusion, the ANP-based clustering strategy pro-
to this reduction. The results indicated that the suggested posed by Ali et al. offers a robust and efficient solution to
approach has a shorter C2C delay in all topologies compared the CPP in SDN-IoT networks, significantly reducing E2E
to k-means, especially as the number of clusters increases. and C2C delays and improving overall network performance.
The fairness index, representing the equitable distribu- However, addressing the limitations mentioned above in
tion of switches among clusters, showed that the proposed future research will be essential to further enhance the solu-
method provided a fairer allocation of switches compared tion's applicability and performance in real-world scenarios.
to k-means. A lower value of the fairness index indicates a Future work could explore dynamic network conditions,
smaller number of switches allocated to each cluster relative multi-objective optimization, and considerations for energy
to the number of controllers, which is better achieved by the efficiency, fault tolerance, and security to provide a more
proposed approach. The proposed method exhibited lower comprehensive and adaptive solution for SDN-IoT networks.
communication overhead between switches and controllers
3.2 Multi ‑Objective
(SW-CT) and among controllers (CT-CT) compared to the
k-means algorithm. Lower communication overhead results
in fewer packets exchanged, leading to less frequent inter- The second part of the preposition encompasses all exist-
actions with controllers and reduced computational load on ing solutions that significantly enhance multiple aspects of
controllers. performance:
Despite its advantages, the solution has limitations. The Choumas et al. [35] delves into the integration of SDN
ANP model, with its detailed pairwise comparisons and with low-power IoT, highlighting the optimization of control
consistency checks, increases computational complexity. traffic as crucial for minimizing energy consumption and
This can result in longer computation times, especially for maximizing bandwidth in IoT systems. The study addresses
large networks with numerous nodes and controllers. The the challenge of selecting IoT sensors to host SDN control-
iterative nature of the process requires significant computa- lers and mapping each sensor to a controller, both of which
tional resources, which might not be practical for real-time significantly affect the volume of control traffic.

1 78 International Journal of Networked and Distributed Computing (2024) 12:170–184
The authors model this optimization problem using addressing different controller placement problems, ranging
integer quadratic programming (IQP) and propose a set from basic to complex use cases. The framework includes
of heuristic algorithms to expedite the solution. They ini- heuristic algorithms based on the submodularity concept to
tially present a fast and simple heuristic algorithm, which find near-optimal solutions for different scenarios.
is then extended to two iterative algorithms designed to The submodularity framework simplifies the controller
offer improved performance at the cost of increased time placement problem into five main use cases:
complexity. The algorithms focus on minimizing the total
control traffic, which includes both controller-to-switch • Maximum Covered Submodular Set Problem (P1): This
(Ctr–Sw) and controller-to-controller (Ctr–Ctr) commu- involves placing a set of controllers that can control the
nications. Through simulations using network topologies entire network while maximizing a submodular function.
from the Internet Topology Zoo collection and real-world A greedy incremental algorithm with an approximation
experiments on the NITOS testbed, the results reveal that ratio is used for this problem. The objective is to find a
these heuristics achieve near-optimal performance with subset of nodes that maximizes the network utility while
significantly less computation time than solving the IQP adhering to the constraint of having a limited number of
problem directly. The simple heuristic algorithm performs controllers.
well, providing a good balance of performance and compu- • Maximum Covered Submodular Set Problem with Given
tational efficiency. The iterative algorithms, however, offer Requirement Set of Controllers (P2): This problem
even better performance, particularly for larger networks, extends P1 by including a given set of existing control-
by refining the initial solution through a series of local opti- lers in the network. The solution involves transforming
mizations. The study concludes that balancing the number the original function to account for the pre-existing con-
and placement of controllers is critical for managing control trollers. The goal is to expand the current set of control-
traffic effectively. More distributed controllers reduce con- lers by adding new ones to maximize the network utility
troller-to-switch traffic, whereas fewer, centralized control- while maintaining the existing controllers.
lers minimize controller-to-controller traffic. This balance is • Maximization Control Submodular Problem (P3): This
essential for optimizing energy consumption and bandwidth problem considers a connected graph of all controllers
in low-power IoT networks. The authors note that as the and aims to place controllers such that the sub-graph is
number of controllers increases and the placement becomes connected and maximizes a submodular function. The
more distributed, the controllers get closer to the switches, algorithm ensures that the placement results in a con-
reducing the volume of Ctr–Sw traffic. Conversely, fewer nected network of controllers, which is essential for
and more concentrated controllers reduce the volume of maintaining network integrity and performance.
Ctr–Ctr traffic. The proposed heuristic approaches, while • Maximization Network Quality Factor Submodular Prob-
practical, involve trade-offs between performance and com- lem (P4): This involves selecting a subset of controller
putational complexity. They do not always achieve the abso- locations to maximize the network quality factor, which
lute optimal solution but strike a balance that is practical for includes constraints like hop count or latency measure-
real-world applications. The study acknowledges that the ments. The objective is to ensure that the chosen con-
dynamic nature of IoT environments requires adaptable solu- trollers provide the best possible network performance
tions, and further enhancements are suggested to improve metrics, such as minimizing latency and maximizing
these heuristics, particularly focusing on minimizing con- throughput.
trol delay. The authors provide insights and directions for • Maximization Submodular Problem with Budget Con-
future research, including exploring other centrality metrics, straints (P5): This problem introduces an economic
improving the balance between distributed and centralized aspect by considering deployment costs and budget
controller placement, and enhancing the adaptability of the constraints for placing controllers. The goal is to opti-
solutions to varying network conditions. These improve- mize the placement of controllers within a given budget,
ments aim to further reduce control traffic and enhance the ensuring cost-effective network management.
overall performance of SDN-based IoT networks.
Anh Khoa Tran et al. [36] explores optimizing controller The proposed methodology involves detailed steps for
placement in SDN for IoT networks using a submodularity- each use case, utilizing submodular optimization principles.
based approach. The authors address the challenges of effi- The Nemhauser’s algorithm is used extensively to approxi-
cient controller placement in distributed and dynamic IoT mate solutions to these NP-hard problems, providing a bal-
networks. The methodology involves developing an opti- ance between computational efficiency and solution qual-
mization framework using submodularity theory to handle ity. For example, in P1, the greedy algorithm incrementally
various aspects of controller placement in distributed net- selects nodes that maximize the utility function until the
works. The submodularity theory helps in formulating and desired number of controllers is reached.

International Journal of Networked and Distributed Computing (2024) 12:170–184 179
In P2, the algorithm is extended to include pre-existing solutions, while the POCO tool helps design the controllers
controllers, starting with the given set and then adding new and nodes to solve the controller placement problem effec-
controllers that maximize the network utility. P3 and P4 fur- tively. The fuzzy logic system used includes four stages:
ther refine the placement strategy by ensuring connectiv- fuzzifier, knowledge base, defuzzifier, and fuzzy inference
ity and optimizing network quality factors, respectively. P5 engine. The fuzzifier converts input data into fuzzy sets, the
incorporates budget constraints, transforming the problem knowledge base stores the fuzzy rules, the defuzzifier con-
to handle economic considerations effectively. verts fuzzy sets into a crisp output, and the fuzzy inference
The results from extensive simulations show that the pro- engine processes the fuzzy rules to derive an output. The
posed submodularity-based algorithms outperform baseline adaptive fuzzy controller is designed to reduce the com-
methods regarding execution time, number of controllers, munication burden among controllers by placing multiple
and network latency. The simulations involved creating a controllers at different locations. This reduces the network
physical network using Zipf’s law [37] to generate random delay caused by the limited control capability of a single
nodes and links, evaluating the execution time, and measur- controller. The proposed method optimizes controller place-
ing performance aspects like the number of controlled nodes ment by considering load balancing, delay constraints, and
and average latency. failure tolerance. The objective is to find an optimal solution
For instance, in the simulation environment, a physical for delay constraints, controller selection, and adaptive fuzzy
network with 200 nodes was created, and the algorithms controller placement by balancing the load and reducing
were evaluated based on their ability to control the network propagation latency. The population-based, nature-inspired
efficiently. The results demonstrated that the submodularity- ESFO algorithm imitates the path taken by sunflowers as
based approach achieved near-optimal solutions in signifi- they approach the sun. The algorithm includes the following
cantly less time compared to the optimal solutions obtained steps: initializing the population of flowers, calculating the
using the Gurobi solver [34]. The average latency and num- objective function for all sunflowers, estimating the orien-
ber of controllers were also evaluated, showing that the tation vector for each plant, removing plants farthest from
proposed method effectively reduced network latency and the sun, calculating steps for each plant, pollinating the best
required fewer controllers compared to baseline methods. plants, and evaluating new individuals. The objective func-
The paper discusses the limitations of the current tion maximizes the density and minimizes the distance to
approach, noting that while the submodular approach effec- the controllers. The algorithm ensures that the optimized
tively matches the controller placement problem, it does not number of controllers is identified based on high density
fully consider the relationship between controllers in the and minimum distance.
control channel. Future work aims to combine submodular- The POCO placement tool is used to design controllers
ity theory with other methods to account for control plane and nodes to solve the controller placement problem. It cal-
costs and enhance the framework's applicability to real- culates optimal results and resilience against controller fail-
world scenarios. ures by considering latency and load constraints. The tool
In conclusion, the authors present a promising framework helps in finding the best controller placement in the network
for solving the SDN controller placement problem in IoT by minimizing the maximum latency between nodes and
networks, emphasizing the effectiveness of submodular- controllers, even in failure scenarios.
ity theory in providing flexible and efficient solutions for The results indicate that the proposed method achieves
various network scenarios. The methodology, supported by significant improvements in latency and load balancing com-
extensive simulations, demonstrates significant improve- pared to existing methods. With two controllers, the pro-
ments in execution time, network latency, and the number posed method obtains 400 miles as average latency, which
of controllers required, making it a viable approach for prac- is 22.2% smaller than PSO, 76.9% lesser than hybrid SD,
tical implementation in distributed IoT networks. and 91.89% lesser than PASIN. The study includes detailed
Sikander Hans et al. [40] focuses on optimizing the place- comparison tables and graphical representations of control-
ment of controllers in SDN-IoT networks to reduce latency ler placement, node failure scenarios, and controller imbal-
and improve load balancing. The authors propose using an ance under different conditions.
Enhanced Sunflower Optimization (ESFO) algorithm com- The paper discusses the main limitations related to the
bined with a Pareto Optimal Controller (POCO) placement complexity of controller placement in large-scale networks
tool. This method is compared with existing methods such and the challenges in achieving minimal latency under var-
as PASIN, hybrid SD, and PSO. ying network conditions. The proposed method addresses
The methodology includes the implementation of an these challenges but requires further testing in real-world
adaptive fuzzy controller placement using the ESFO algo- scenarios to validate its effectiveness. In conclusion, the pro-
rithm and POCO tool. The ESFO algorithm mimics the nat- posed ESFO algorithm combined with the POCO tool offers
ural movement of sunflowers towards the sun to find optimal an efficient solution for controller placement in SDN-IoT

1 80 International Journal of Networked and Distributed Computing (2024) 12:170–184
networks. The method provides improved load balancing and and worst-case latencies. The modified worst-case latency
reduced latency compared to existing approaches. Future calculation performs better under different network condi-
work includes testing the proposed strategy in realistic sce- tions compared to traditional methods. The quality of clus-
narios and considering additional performance metrics like tering is assessed using the silhouette method. The results
energy consumption and response time to enhance the qual- indicate that the majority of clusters have positive silhouette
ity of service in IoT networks. values, suggesting a better distribution of clusters within the
The research by Khera et al. [44] investigates enhancing network and improved network performance. The silhouette
the performance of wide-area Cellular IoT (CIoT) networks values range from – 0.5 to 1, with fewer than 10% of clusters
by integrating SDN with IoT networks. The focus is on find- showing negative values, indicating a high-quality cluster-
ing the optimal placement of SDN controllers and evaluat- ing outcome.
ing SDN clustering to boost efficiency. The study proposes Despite the promising results, the study acknowledges
an Un-Supervised Machine-Learning (US-ML) approach several limitations. The use of random distance measures
based on silhouette distance and gap statistics to determine in the methodology leads to probabilistic outcomes, mean-
the optimal number of controllers. The Partition Around ing the results may vary. To address this, future simulations
Medoids (PAM) method is used to allocate these controller should use fixed distance measures for network formation
locations effectively. to achieve more consistent results. Another limitation is
The study begins by identifying the critical need for the challenge of implementing LoRa in WAN architecture,
improving the performance of CIoT-based wide area net- despite its optimal maximum range. This complexity makes
works (WANs). It suggests combining Low-Power Wide it difficult to deploy effectively in real-world scenarios.
Area Networks (LPWAN) and CIoT networks to enhance Additionally, the study recognizes that the method uses ran-
performance. The research introduces a hybrid combination dom distance measures, leading to probabilistic outcomes
of SDN and IoT networks, which has gained popularity in that may vary. To address this, future research should focus
industrial applications such as smart cities, production con- on using fixed distance measures for network formation to
trol, smart homes, and inventory management. The proposed achieve more consistent results.
method involves using US-ML techniques to determine the In conclusion, the study highlights the potential of com-
optimal number of SDN controllers. This is achieved by ana- bining SDN with IoT networks to enhance the effectiveness
lyzing silhouette distance and gap statistics, followed by the of WAN networks by improving data control. The proposed
PAM approach to allocate the controller locations. US-ML based silhouette PAM method for optimal SDN con-
In detail, the study generates topological data from a gml troller placement demonstrates significant improvements in
file using MATLAB, deriving the adjacency matrix, node network performance. Future research should focus on test-
coordinates, and level matrix. The PAM method is applied ing the performance of LoRaWAN and NB-IoT networks
to find the best controller placements by evaluating clus- under reduced power consumption scenarios to further vali-
ter quality and network latencies. This method minimizes date the findings. Overall, the integration of SDN with CIoT
the sum of dissimilarities between points and their nearest networks using advanced machine learning techniques for
medoid, which helps in reducing communication distances controller placement holds considerable promise for improv-
between sensor nodes and controllers. The effectiveness of ing various industrial applications.
the proposed method is validated through simulations, where Table 1 below summarizes all the solutions (methods
average and worst-case latencies are calculated to ensure used, goals, performances improved, etc.)
robust performance under different network conditions.
The study introduces a modified worst-case latency calcu- 3.2.1 Performance Metrics
lation that better reflects real-world scenarios, enhancing the
robustness of the results. The following table (Table 2) summarizes the metrics used
The study presents various results based on simulations by the different proposed solutions to evaluate their CPP
using the proposed US-ML and PAM methods. It evalu- algorithms.
ates the performance of different LPWAN technologies,
including NB-IoT, LoRa, and SigFox, in terms of coverage
4 Future Research Works
and energy efficiency. NB-IoT is found to have the longest
battery life and most effective energy management, mak-
ing it highly suitable for long-term IoT applications. Effec- This section highlights important research issues that
tive placement of SDN controllers significantly reduces should be considered when examining the CPP in the
communication distances between sensor nodes, thereby SDN-IoT. We reviewed the CPP-related solutions put forth
improving network performance. The performance of the by various researchers in light of latency, switch assign-
proposed method is validated by evaluating both average ment, Delay E2E, communication cost inflation, energy

International Journal of Networked and Distributed Computing (2024) 12:170–184  181
 sretemarap eht dna srellortnoc
 rebmun eht fi( srellortnoc fo  eht fo emos gnitcelgeN)dexfi  rehto dna lennahc lortnoc eht -silibaborp ot sdael serusaem  dexfi gniriuqer ,semoctuo cit -tsisnoc rof serusaem ecnatsid  mumixam lamitpo sti etipsed
 rebmun mumixam eht dexiF-  ycnetal gnitcelgeN .noitulos -noc fo rebmun a fo lasoporP  NAW ni aRoL gnitnemelpmI
|     |  eht naht retaerg si dedeen  ekil sretemarap denoitnem | -mun eht nehw( srellortnoc                             |                                                                                     |                           |     |     |  ecnatsid modnar fo esu ehT |     |  gnignellahc si erutcetihcra |
| --- | ------------------------------------------------------ | ------------------------------------------------------ | ----------------------------------------------------------------------------------- | ------------------------- | --- | --- | --------------------------- | --- | ---------------------------- |
|     |                                                        |  fo rebmun eht gnitcelgeN-  ycnetal eht ,sesaercni reb |  gnitcelgen dna )sesaercni -feni era snoitulos citsirueh  tnemecalp eht rof tneicfi |  fo rebmun eht gnitcelgeN |     |     |                             |     | -laer gnitacilpmoc ,egnar    |
denoitnem scirtem rehto
|     |     |     |     | cirtem tnatropmi na sa |     | tneicffie ton si srellort |     |     |     |
| --- | --- | --- | --- | ---------------------- | --- | ------------------------- | --- | --- | --- |
tsrfi eht ni denoitnem
|     |     | secivres fo ytilauq |     |     |     |     |     |     | tnemyolped dlrow |
| --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | ---------------- |
stluser tne
euqitirC
 a dna tnemecalp rellortnoC
|     |  dna tnemecalp rellortnoC |                      |                       |                      |     |  dna tnemecalp rellortnoC |  dna tnemecalp rellortnoC |     |     |
| --- | ------------------------- | -------------------- | --------------------- | -------------------- | --- | ------------------------- | ------------------------- | --- | --- |
|     | srellortnoc fo rebmun     |                      | srellortnoc fo rebmun |                      |     | srellortnoc fo rebmun     | srellortnoc fo rebmun     |     |     |
|     |                           | tnemecalp rellortnoC |                       | tnemecalp rellortnoC |     |                           |                           |     |     |
laoG
|     |                                                            |     |                                                                                           |                            |                          |  htiw metsys eht stnemelpmi |                            |  tnereffid gnitneserper sedon |     |
| --- | ---------------------------------------------------------- | --- | ----------------------------------------------------------------------------------------- | -------------------------- | ------------------------ | --------------------------- | -------------------------- | ----------------------------- | --- |
|     |  s'fpiZ gnisu krowten lacisyP -itpo htiw derapmoc srellort |     |  sehctiws seigolopot ehctsueD -celloc ooZ ygolopoT tenretnI  lauqe ro ssel sehctiwS .noit |                            |                          |                             |                            |                               |     |
|     | -noc 01 dna sedon 002 wal                                  |     | 04 ot 1 neeweteb srellortnoc                                                              |                            |  ,E3SO ,teN_\SU ,enelibA |                             |                            |                               |     |
|     | ecnatsid -tsesolc dna lam                                  |     |                                                                                           |                            | -moC .ygolopot etuoretnI |                             |                            |                               |     |
|     |                                                            |     |                                                                                           |  .seigolopot tenretnI laeR |                          |  knilumiS/BALTAM ehT        |  41 .elfi lmg :ecruoS ataD |                               |     |
snaem-K htiw derap
051 ot 05 neewteb
 ,tenhtroF ,dlNataT
srellortnoc owt
b9102baltaM
| noitalumiS |     |     |     |       |                                 |                              | BALTAM |        |     |
| ---------- | --- | --- | --- | ----- | ------------------------------- | ---------------------------- | ------ | ------ | --- |
|            |     |     |     | 03 ot |                                 |                              |        | seitic |     |
|            |     |     |     |       |  riaf )rellortnoc-ot-rellortnoc |  rebmun decuder ecnalab daoL |        |        |     |
krowten ToI-NDS ni srellortnoc tnemecalp melborp eht ot snoitulos gnitsixe eht llA  1 elbaT
|                      |     | sdaol hctiws eht ecnalaB |                   |                         | daehrevo noitacinummoc                        | yaled dna ycnetal egareva |     |                    |     |
| -------------------- | --- | ------------------------ | ----------------- | ----------------------- | --------------------------------------------- | ------------------------- | --- | ------------------ | --- |
| devorpmi ecnamrofreP |     |                          |                   |  deriuqer eht seziminiM |  dna dne-ot-dne( yeleD sehctiws fo noitacolla |                           |     |                    |     |
|                      |     |                          | tnemngissa hctiwS |                         |                                               |                           |     | ytilauQ gniretsulC |     |
lennahc lortnoc
|     | emit noitucexE |     |     | cffiart lortnoC |     | srellortnoc fo |     |     |     |
| --- | -------------- | --- | --- | --------------- | --- | -------------- | --- | --- | --- |
tdiwdnab
|     | ycnetaL | ycnetaL |     |     |     |     | ycnetaL |     |     |
| --- | ------- | ------- | --- | --- | --- | --- | ------- | --- | --- |
ygrenE
|     |                                                     |  noitulovE laitnereffiD dirbyH |                            |                            |                                                       |                                                       |     |                              |  ycnetaL esaC-tsroW defiidoM                     |
| --- | --------------------------------------------------- | ------------------------------ | -------------------------- | -------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | --- | ---------------------------- | ------------------------------------------------ |
|     |                                                     |                                |                            |  citsirueH dnA .)PQI( gnim |  )MDCM( gnikam-noisiced                               |  lamitpO oteraP dnA .mhtir  looT tnemecalP rellortnoC |     | sisylanA ecnatsiD etteuohliS |                                                  |
|     |  s’resuahme’N( smhtirogla  hcraes eht dna mhtiroglA |                                |                            |                            |  ssecorP krowteN lacitylanA  airetirc-itlum dna )PNA( | -ogla )OFSE( noitazimitpo                             |     |                              |                                                  |
|     |                                                     |  noitazimitpO elahW dna        | -margorp citardauq regetnI |                            |                                                       |  .rellortnoc yzzuf evitpadA  rewoflnus decnahne dnA   |     |                              | sdiodeM dnuorA noititraP dohteM gniretsulC )MAP( |
 enihcaM desivrepuS nU
 owt htiw noitazimitpO
|     |     |     | mhtiroglA )OWED( |     |     |     |     |  )LM-SU( gninraeL |     |
| --- | --- | --- | ---------------- | --- | --- | --- | --- | ----------------- | --- |
)mhtirogla eert
|     |     |     |     |           |     |     |     |          | scitsitatS paG noitaluclaC |
| --- | --- | --- | --- | --------- | --- | --- | --- | -------- | -------------------------- |
|     |     |     |     | mhtirogla |     |     |     | hcaorppA |                            |
)OCOP(
| sdohteM |                              |                                 |                                                                                  |                            | emehcs                                                                      |                               |                           |                                                  |     |
| ------- | ---------------------------- | ------------------------------- | -------------------------------------------------------------------------------- | -------------------------- | --------------------------------------------------------------------------- | ----------------------------- | ------------------------- | ------------------------------------------------ | --- |
|         |  desaB-ytiraludombuS dezim   |  lamitpo rof yaw tnegilletnI nA |                                                                                  |                            |                                                                             |  fo tenretnI denfieD erawtfoS |                           |                                                  |     |
|         |  ni tnemecalP rellortnoC NDS |                                 |                                                                                  |  rof tnemngissA hctiwS dna |                                                                             |  noitazimitpO gnisU sgnihT    |                           |                                                  |     |
|         |                              |                                 | -ten ToI–denfied-erawtfos ]23[ .seitic trams rof skrow  tnemecalP rellortnoC NDS |                            | -tenretnI denfieD-erawtfoS                                                  |                               |  fo ecnamrofreP gnicnahnE |  yb NDS ToIC aerA ediW ]44[ tnemecalP rellortnoC |     |
|         |                              |  ni stnemecalp rellortnoc       |                                                                                  |                            |  rof hcaorppA evitceffE nA  ni tnemecalP rellortnoC ]33[ )ToI-DS( sgnihT-fo |                               |                           |  mumitpO desaB LM-SU                             |     |
|         | -itpO nA :skrowteN ToI       |                                 |                                                                                  |                            |                                                                             |  ni tnemecalP rellortnoC      |                           |                                                  |     |
]53[ ToI rewoP woL
]04[ .mhtiroglA
]63[ hcaorppA
eltiT

1 82 International Journal of Networked and Distributed Computing (2024) 12:170–184
Table 2 number of the metrics improved with each solution
Latency Load-Balanc- Control Traffic Others
ing
Keshari et al. [32] X
Ali et al. [33] X
Choumas et al. [35] X switch assignment- increase bandwidth
Tran et al. [36] X -Number of controllers -time execution -Control channel
Hans et al. [40] X X Reduced number of controllers and average latency and delay
Khera et al. [44] X Energy
Clustering Quality
costs, and different goal-related functions. There are still 5 Conclusions
several obstacles to be explored. By addressing various
issues and proposing potential research directions, we aim As SDN-IoT networks rapidly evolve, using a single con-
to stimulate researchers delving into this topic. troller to manage multiple IoT-enabled switches can be
inefficient. Therefore, multiple controllers are needed
• Network performance: performance is an essential to manage all switches in the SDN IoT network. We are
parameter for evaluating an SDN-IoT network. It can be therefore faced with the problem of determining their loca-
measured in terms of throughput, latency, and response tion and quantity. Use different methods to solve controller
time. A high-performance network must efficiently placement issues. However, as the number of controllers
manage the data generated by connected objects. increases, the effectiveness of these methods decreases due
• Security: is another critical parameter to evaluate in an to previous changes. CPP is a current research hotspot on
SDN-IoT network. The data generated by connected SDN architecture behavior. Various types of research have
objects can be sensitive and must be protected against been conducted to address CPP issues and try to improve
malicious attacks. The network must have security performance metrics (latency, reliability, cost, etc.). Due
mechanisms such as authentication, confidentiality, to the inherent complexity of the CPP and its NP-Hard
and data integrity. nature, existing solutions cannot fully satisfy all funda-
• Scalability: is another important parameter for eval- mental requirements for various network types with abso-
uating an SDN-IoT network. The number of con- lute precision.
nected objects can increase rapidly, which requires This article mainly studies the concepts and archi-
the ability to scale the network rapidly. tecture of IoT and SDN as well as the concept of SDN-
• Traffic Management: is essential for evaluating an IoT. We then explore the idea of the CPP and highlight
SDN-IoT network. Connected objects can generate the importance of considering it in the context of SDN
large amounts of data, leading to network congestion for the IoT. The CPP can be categorized into two main
if traffic is improperly handled. groups: mono-objective solutions and multi-objective
• Flexibility: is also necessary when evaluating an SDN- solutions. Moreover, we have discussed each module and
IoT network. The network must adapt to changes in the its mathematical formulation and provided a thorough
IoT environment and user needs. analysis of CPP solutions, noting any drawbacks. Table 1
• Interoperability: is also essential for evaluating an lists the disadvantages of each CPP solution and can be
SDN-IoT network. Connected objects can come from used to determine the most effective approach to solving
different suppliers and use other communication pro- CPP problems. Finally, we list some research topics that
tocols. The network must be able to support these researchers can pursue further. The main purpose of this
different protocols to ensure efficient communication survey is to provide a comprehensive overview of the CPP,
between related entities. identify gaps in the existing literature, and stimulate dis-
• Reliability: is a key consideration for evaluating an cussion on possible future research directions. The survey
SDN-IoT network. The network must ensure consist- highlights the challenges posed by SDN-IoT architecture
ent and dependable performance, even in the face of and positions CPP as one of the most essential topics
hardware failures, network congestion, or other issues. in this network. It is observed that multiple controllers
High reliability is essential to maintain trust and func- are required to achieve the scalability and reliability of
tionality in critical applications.

International Journal of Networked and Distributed Computing (2024) 12:170–184 183
SDN-IoT. Determining the optimal number and location of 2. Metcalfe’s Law. https://e n.w ikipe dia.o rg/w iki/M etcal fe.
controllers is critical to improving network performance. 3. Kreutz D, Ramos FM, Verissimo PE, Rothenberg CE, Azodol-
molky S, Uhlig S (2014) Software-defined networking: a com-
A review of all CPP solutions reveals the existence of mul-
prehensive survey. Proc IEEE 103(1):14–76
tiple approaches based on specific objective functions and 4. McKeown N, Anderson T, Balakrishnan H, Parulkar G, Peterson
constraints. L, Rexford J, Turner J (2008) OpenFlow: enabling innovation
Future research directions should focus on developing in campus networks. ACM SIGCOMM Comput Commun Rev
38(2):69–74
more sophisticated algorithms for controller placement that
5. Lin YD, Lin PC, Yeh CH, Wang YC, Lai YC (2015) An extended
leverage artificial intelligence and machine learning to pre- SDN architecture for network function virtualization with a case
dict network conditions and optimize controller locations study on intrusion prevention. IEEE Network 29(3):48–53
dynamically. Additionally, exploring the integration of edge 6. Liu J, Jiang Z, Kato N, Akashi O, Takahara A (2016) Reliability
evaluation for NFV deployment of future mobile broadband net-
computing with SDN-IoT frameworks can significantly
works. IEEE Wirel Commun 23(3):90–96
enhance data processing efficiency and reduce latency, 7. Guo Z, Su M, Xu Y, Duan Z, Wang L, Hui S, Chao HJ (2014)
making the network more responsive and resilient. Practi- Improving the performance of load balancing in software-defined
cal applications of these advancements include smart cities, networks through load variance-based synchronization. Comput
Netw 68:95–109
where optimized controller placement can ensure seamless
8. Tootoonchian A, Ganjali Y (2010) Hyperflow: a distributed con-
connectivity and efficient management of IoT devices in trol plane for openflow. In Proceedings of the 2010 internet net-
urban environments. Moreover, the advent of 5G technol- work management conference on research on enterprise network-
ogy and beyond will provide new opportunities to enhance ing (Vol. 3, pp. 10–5555)
9. Hassas Yeganeh S, Ganjali Y (2012) Kandoo: a framework for
SDN-IoT infrastructures by offering higher bandwidth and
efficient and scalable offloading of control applications. In Pro-
lower latency, further supporting real-time applications ceedings of the first workshop on hot topics in software defined
such as autonomous vehicles and industrial automation. By networks (pp. 19–24).
addressing the CPP with emerging technologies, we can 10. Koponen T, Casado M, Gude N, Stribling J, Poutievski L, Zhu M,
Shenker S (2010) Onix: a distributed control platform for large-
create more robust, scalable, and efficient networks capa-
scale production networks. In 9th USENIX symposium on operat-
ble of meeting the demands of future IoT applications. This ing systems design and implementation (OSDI 10)
ongoing research will pave the way for innovative solutions 11. Guo Z, Liu R, Xu Y, Gushchin A, Walid A, Chao HJ (2017)
that can transform various industries and improve overall STAR: Preventing flow-table overflow in software-defined net-
works. Comput Netw 125:15–25
network performance and reliability.
12. Chen J, Liu Y, Zhang Y (2024) Advances in IoT-enabled smart
environments. Sensors 24(5):1234–1250
13. Zemrane H, Baddi Y, Hasbi A (2018) SDN-based solutions to
Funding Not applicable. improve IoT: survey. In 2018 IEEE 5th international congress on
information science and technology (CiSt) (pp. 588–593). IEEE.
Data availability Not applicable. 14. Satam P, Pacheco J, Hariri S, Horani M (2017) Autoinfotainment
security development framework (ASDF) for smart cars. In 2017
Declarations International conference on cloud and autonomic computing
(ICCAC) (pp 153–159). IEEE.
Conflict of Interest The authors declare that they have no competing 15. Pal D, Funilkul S, Charoenkitkarn N, Kanthamanon P (2018)
interests. Internet-of-things and smart homes for elderly healthcare: an end
user perspective. IEEE Access 6:10483–10496
Ethical Approval Not applicable. 16. Rolik J, Lens JE, Dewoolkar MM, Weller TM (2018) Effects of
soil characteristics on passive wireless sensor interrogation. IEEE
Open Access This article is licensed under a Creative Commons Attri- Sensors J 18(8):3454–3460
bution 4.0 International License, which permits use, sharing, adapta- 17. Jadhav KB, Chaskar UM (2017) Design and development of smart
tion, distribution and reproduction in any medium or format, as long phone based ECG monitoring system. In 2017 2nd IEEE interna-
as you give appropriate credit to the original author(s) and the source, tional conference on recent trends in electronics, Information &
provide a link to the Creative Commons licence, and indicate if changes Communication Technology (RTEICT) (pp. 1568–1572). IEEE.
were made. The images or other third party material in this article are 18. Zhang JF, Wen CJ (2017) The university library management sys-
included in the article's Creative Commons licence, unless indicated tem based on radio frequency identification. In 2017 10th inter-
otherwise in a credit line to the material. If material is not included in national congress on image and signal processing, BioMedical
the article's Creative Commons licence and your intended use is not Engineering and Informatics (CISP-BMEI) (pp. 1–6). IEEE.
permitted by statutory regulation or exceeds the permitted use, you will 19. Kim J, Song J (2018) A secure device-to-device link establishment
need to obtain permission directly from the copyright holder. To view a scheme for LoRaWAN. IEEE Sens J 18(5):2153–2160
copy of this licence, visit http://c reati vecom mons.o rg/l icens es/b y/4.0 /. 20. Nishikori S, Kinoshita K, Tanigawa Y, Tode H, Watanabe T
(2017) A cooperative channel control method of ZigBee and WiFi
for IoT services. In 2017 14th IEEE annual consumer communica-
tions & networking conference (CCNC) (pp. 1–6). IEEE.
References
21. Priscilla O (2010). Top-down network design.
22. Bonfim MS, Dias KL, Fernandes SF (2019) Integrated NFV/SDN
1. Ashton K (2009) That ‘internet of things’ thing. RFID J architectures: a systematic literature review. ACM Comput Surv
22(7):97–114 (CSUR) 51(6):1–39

1 84 International Journal of Networked and Distributed Computing (2024) 12:170–184
23. Kunz T, Muthukumar K (2017) Comparing openflow and NET- 3 4. https://w ww.g urobi.c om/
CONF when interconnecting data centers. In 2017 IEEE 25th 35. Choumas K, Giatsios D, Flegkas P, Korakis T (2020) SDN con-
international conference on network protocols (ICNP) (pp. 1–6). troller placement and switch assignment for low power IoT. Elec-
IEEE. tronics 9(2):325
24. Qin Z, Denker G, Giannelli C, Bellavista P, Venkatasubramanian 36. Tran AK, Piran MJ, Pham C (2019) SDN controller placement in
N (2014) A software defined networking architecture for the inter- IoT networks: an optimized submodularity-based approach. Sen-
net-of-things. In 2014 IEEE network operations and management sors 19(24):5474
symposium (NOMS) (pp. 1–9). IEEE. 37. Newman ME (2005) Power laws, Pareto distributions and Zipf’s
25. Frolik J, Lens JE, Dewoolkar MM, Weller TM (2018) Effects of law. Contemp Phys 46(5):323–351
soil characteristics on passive wireless sensor interrogation. IEEE 38. Wang A, Wu J (2018). Policy and resource orchestration in soft-
Sens J 18(8):3454–3460 ware-defined networks. In 2018 IEEE 4th international conference
26. Heller B, Sherwood R, McKeown N (2012) The controller on collaboration and internet computing (CIC) (pp. 203–206).
placement problem. ACM SIGCOMM Comput Commun Rev IEEE.
42(4):473–478 39. Hans S, Ghosh S, Kataria A, Karar V, Sharma S (2022) Controller
27. Ishigaki G, Gour R, Yousefpour A et al (2017) Cluster leader placement in software defined internet of things using optimiza-
election problem for distributed controller placement in sdn. In: tion algorithm. CMC-Comput Mater Continua 70(3):5073–5089
GLOBECOM 2017–2017 IEEE Global Communications Confer- 40. Gupta P, Kumar R, Singh S (2024) Integration of AI and IoT: a
ence. IEEE, p. 1–6 comprehensive review. IEEE Internet Things J 11(1):56–72
28. Sallahi A, St-Hilaire M (2014) Optimal model for the controller 41. Khan M, Ali Z, Rahman A (2024) Blockchain-enhanced IoT
placement problem in software defined networks. IEEE Commun architecture for secure data management. Internet Things J
Lett 19(1):30 25(3):345–360
29. Milan ST, Rajabion L, Ranjbar H, Navimipour NJ (2019) Nature 42. Herencsar N, Soltan A et al (2023) Internet of things: a com-
inspired meta-heuristic algorithms for solving the load-balancing prehensive overview on protocols, architectures, technologies,
problem in cloud environments. Comput Oper Res 110:159–187 simulation tools, and future directions. Energies 16(8):3465
30. Polat H, Polat O, Cetin A (2020) Detecting DDoS attacks in 43. Zhu Q, Wang L, Li Y (2023) Software-defined networking for
software-defined networks through feature selection methods and internet of things: a comprehensive review. J Netw Comput Appl
machine learning models. Sustainability 12(3):1035 123:45–67
31. Kharkongor C, Chithralekha T, Varghese R (2016) A SDN con- 44. Khera A, Kurmi US (2023) Enhancing performance of wide area
troller with energy efficient routing in the internet of things (IoT). CIoT SDN by US-ML based optimum controller placement. Res
Procedia Comput Sci 89:218–227 Rep Comput Sci
32. Keshari SK, Kansal V, Kumar S (2021) An intelligent way for
optimal controller placements in software-defined–IoT networks Publisher's Note Springer Nature remains neutral with regard to
for smart cities. Comput Ind Eng 162:107667 jurisdictional claims in published maps and institutional affiliations.
33. Ali J, Roh BH (2022) An effective approach for controller place-
ment in software-defined internet-of-things (SD-IoT). Sensors
22(8):2992