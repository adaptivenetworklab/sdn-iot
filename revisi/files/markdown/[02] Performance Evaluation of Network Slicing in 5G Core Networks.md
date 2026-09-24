# [02] Performance Evaluation of Network Slicing in 5G Core Networks

> Source file: `[02] Performance Evaluation of Network Slicing in 5G Core Networks.pdf`

---

International Journal of Multidisciplinary Research and Growth Evaluation www.allmultidisciplinaryjournal.com
Performance Evaluation of Network Slicing in 5G Core Networks
Varinder Kumar Sharma
Independent Researcher, USA
* Corresponding Author: Varinder Kumar Sharma
Article Info Abstract
Fifth-generation (5G) mobile networks are introducing revolutionary changes in the design, deployment,
and management of cellular infrastructure. Key technologies such as network slicing, which is
ISSN (online): 2582-7138 unprecedented in the mobile communication domain, serve as one of the key corners of the 5G architecture.
Volume: 03 Each slice is individually customized to accommodate various applications, including Enhanced Mobile
Broadband (eMBB), Ultra-Reliable Low-Latency Communications (URLLC), and massive Machine-Type
Issue: 05 Communications (mMTC). To the best of our knowledge, this paper presents the first detailed investigation
of NS performance in 5 G Core (5GC) networks, along with a comprehensive study of architecture,
September - October 2022
deployment models, and empirical performance metrics in both real and emulated conditions.
Received: 19-08-2022 The primary objective of this work is to quantify the efficiency with which network slicing can achieve
Accepted: 22-09-2022 quality of service guarantees and fulfill SLAs across various service domains. We examine how slicing
performs in terms of core network isolation, latency control, throughput stability, and scalability under
Published: 07-10-2022 multi-tenant, dynamic, and service-differentiated workloads. To achieve this, the study utilizes Software-
Page No: 648-654 Defined Networking (SDN) and Network Function Virtualization (NFV) as building blocks to create a
programmable, elastic network infrastructure that enables slice orchestration and lifecycle management. We
design, instantiate, and monitor individual slices using a service-based architecture (SBA), and analyse their
performance in terms of KPIs such as RTT, PLR, jitter, and CPU/memory usage.
To simulate practical deployment, the evaluation utilizes a virtualized 5 G Core (5GC) environment with
open-source simulators, including Open5GS, Mininet, and ONOS. The core of the research presents
controlled traffic emulations for various use case categories on these platforms. For eMBB, we consider
high-throughput data traffic, like 4K Video Streaming and File download scenarios. For URLLC, we
consider latency-sensitive applications, such as remote surgery and Autonomous vehicle control
applications. For mMTC, we consider the massive amount of IoT sensor data used to model ultra-dense,
low-rate transmissions. These controlled settings enable comparison of slice-level resource isolation,
congestion behavior, and response to orchestration changes under different load profiles in the network.
Preliminary results indicate that network slicing yields significant improvements in resource utilization and
service differentiation, particularly when combined with dynamic slice scaling and policy-based resource
allocation. eMBB slices maintain consistent throughput with little packet drop, even under bursty traffic.
When using dedicated resource pools and preemptive scheduling approaches, URLLC slices exhibit latency
of less than 10 ms. mMTC slices demonstrate resilience in supporting tens of thousands of simultaneous
low-bandwidth devices with low orchestration latency. However, there were also various shortcomings,
including inter-slice interference when resource boundaries are not rigorously isolated, higher control plane
latency resulting from slice instantiation delay, and the need for intelligent orchestration to support CSI
scaling and healing.
This paper makes several interesting contributions. First, it provides a measurable evaluation of 5G network
slicing performance based on open and reproducible testbeds. Second, it performs a trade-off analysis
between slice isolation and resource efficiency. Third, it also furnishes comparative program benchmarks
for the three 5G service categories in support of SLA control policies. Ultimately, it provides a roadmap for
improving slice orchestration, which involves integrating AI-based policy engines and distributed edge
deployments.
The performance analysis presented in this paper confirms the practicality of network slicing in 5G core
networks for delivering fine-grained, QoS-compliant services. However, to make the best use of it, the next
step will focus on optimizing the orchestration layer, enhancing resource isolation, and integrating
predictive analytics to adapt slices proactively. These enhancements are crucial for meeting emerging 5G
use cases and enabling scalable, long-term support for evolving vertical markets.
DOI: https://doi.org/10.54660/.IJMRGE.2022.3.5.648-654
Keywords: G Core Networks, Network Slicing, Software-Defined Networking (SDN), Network Function Virtualization (NFV)
1. Introduction
The fifth generation of mobile networks (5G) represents a pivotal evolution in wireless communications, characterized by its
ambitious vision to support a wide range of services, including high-speed internet access, ultra-low latency applications, and
massive machine connectivity. To fulfill these divergent requirements, the traditional one-size-fits-all approach of cellular
648 | P ag e

International Journal of Multidisciplinary Research and Growth Evaluation www.allmultidisciplinaryjournal.com
network architecture has been replaced by a flexible, Underpinning the implementation of network slicing are two
scalable, and programmable model enabled by network critical technologies: Software-Defined Networking (SDN)
slicing. Network slicing in 5G Core (5GC) networks allows and Network Function Virtualization (NFV). SDN separates
mobile network operators to deploy multiple logical the control plane from the data plane, enabling centralized
networks—each optimized for specific use cases—over a and programmable control over network flows. NFV, on the
shared physical infrastructure. This paradigm shift offers an other hand, decouples network functions from dedicated
unprecedented level of service differentiation and resource hardware, allowing them to run as software instances on
utilization efficiency. general-purpose servers. Together, these technologies
The motivation for adopting network slicing stems from the facilitate the dynamic creation, management, and
emergence of new service categories, including Enhanced orchestration of network slices. Additionally, the 5GC adopts
Mobile Broadband (eMBB), Ultra-Reliable Low-Latency a Service-Based Architecture (SBA), which enables network
Communications (URLLC), and Massive Machine-Type functions to communicate over RESTful APIs, supporting
Communications (mMTC), each with distinct Quality of modularity, scalability, and service reusability.
Service (quality of service) and Service Level Agreement Despite its theoretical promises, the actual performance of
(SLA) requirements. eMBB services, including high- network slicing in real-world 5 G Core (5GC) deployments
definition video streaming and virtual reality, demand high requires rigorous evaluation. Questions surrounding inter-
bandwidth. URLLC services, such as remote surgery and slice resource contention, orchestration latency, slice
autonomous driving, necessitate extremely low latency and elasticity, and fault isolation remain open. Furthermore, the
high reliability. In contrast, mMTC applications, such as dynamic and distributed nature of 5G services introduces
environmental monitoring and smart metering, require complexities in maintaining SLA guarantees, particularly
massive scalability with minimal data transmission overhead. when slices are scaled in or out, migrated, or healed during
The 5GC network is designed to support these diverse runtime. Understanding these challenges and quantifying the
services through logical partitioning, enabling resource performance characteristics of different slice types are
isolation, independent lifecycle management, and essential for optimizing slicing strategies and informing
differentiated policy enforcement for each network slice. architectural decisions.
Fig 1: Comparison of 5G Use Case Requirements
This bar chart compares throughput, latency, and device enhancing the overall efficiency and reliability of 5G
density requirements across eMBB, URLLC, and mMTC, networks.
emphasizing the rationale for network slicing differentiation. By synthesizing architectural insights, experimental
This research paper aims to address these gaps by conducting evaluations, and comparative analyses, this study offers a
a detailed performance evaluation of network slicing in 5 G comprehensive understanding of the practical implications of
Core (5GC) networks. The evaluation is conducted using network slicing in 5G Core (5GC) networks. It aims to guide
virtualized testbeds based on open-source platforms, both researchers and industry practitioners in designing
allowing for repeatable and extensible experiments. Key robust, SLA-compliant network slices and developing
performance indicators (KPIs) such as latency, jitter, orchestration policies that strike a balance between
throughput, and CPU/memory utilization are measured under performance, flexibility, and cost-effectiveness. Ultimately,
various traffic conditions and service categories. The paper this work contributes to the growing body of knowledge that
also examines the orchestration and isolation mechanisms will shape the future of adaptive, intelligent, and service-
that impact slice performance and discusses strategies for oriented 5G core networks.
649 | P ag e

International Journal of Multidisciplinary Research and Growth Evaluation www.allmultidisciplinaryjournal.com
2. Literature Review compliant policy enforcers were developed to enforce service
While the concept of network slicing has its roots in prior differentiation over network functions and interfaces.
research on network virtualization and software-defined Nonetheless, there are still some blind spots regarding the
networking, it has evolved into a key feature in the design of orchestration overhead, particularly when slices are being
5G networks. In 2015, the nascent work had already scaled continuously or shared between edge and cloud.
investigated the architectural migration required to support Furthermore, some practical measurements are necessary in
virtualized, multi-tenant wireless infrastructures, and hybrid deployments, which involve both physical and virtual
research was increasingly shifting towards the dynamic devices. Accordingly, in this work, we leverage the above
instantiation and lifecycle management of network slices. understanding to offer an emulated 5 G Core (5GC) with
This paper then evaluates the significant advances in the field Open5GS and further assess slicing performance across all
up to December 2020, discussing the architectural designs, core service categories.
orchestration approaches, and performance models for
slicing in 5 G networks. 3. Methodology
One of the first definitions of slicing for 5G was proposed by In this work, we adopt a systematic approach to assessing
the NGMN Alliance, which described network slicing as the working network slicing through experimentation in a
ability to provide independent logical networks on top of simulated 5 G Core (5GC) scenario. The approach comprises
shared infrastructure to support services [1]. This vision was creating a virtualized 5 G testbed, deploying different types
realized in the 3GPP Release 15 document, which introduced of slices for real 5G service categories, and monitoring the
the Service-Based Architecture (SBA) for the 5G Core KPIs using different traffic and orchestration scenarios. The
Network (5GC) and enabled modular interworking between analysis utilizes open-source software and emulation to
network functions through standardized APIs. The simulate realistic deployment scenarios, ensuring
introduction of SBA in slicing is scalable and flexible for reproducible results. The virtual testbed is built with service-
heterogeneous services, such as eMBB, URLLC, and mMTC based architecture (SBA) elements, which include
[2]. configurations with Open5GS for core network functions,
Architecturally, for 5GC slicing, it utilizes SDN and NFV to Mininet for simulated traffic generation and host
virtualize and allocate physical and virtual resources flexibly. management, and the ONOS SDN controller to offer
The Open Network Foundation (ONF) and the ETSI NFV programmable network control. These components run on
group defined enabling programmable control and virtualized virtual machines (VMs) hosted on a Linux-based KVM
network functions (VNFs), which are essential for creating hypervisor, providing scalable orchestration and isolation
and maintaining slices. According to [5], the benefits of across network slices.
SDN/NFV integration towards orchestrating virtualized Three GPP Release 15 provides the slicing model; officially,
slices across edge/flung cloud-native environments have a slice is considered a set of logically related network
been extensively demonstrated. functions that provide a specific service type. Three slices are
Whether it is about orchestration, the biggest challenge has defined: one for eMBB, one for URLLC, and one for mMTC.
been to maintain isolation between slices, and resource Each slice has its dedicated instances of the AMF, SMF, and
optimizations are made effectively. Research by Foukas et al. UPF for control and data plane separation on the RAN. These
proposed "Orion", a slicing framework with on-demand network functions run as Docker containers, which are used
resource allocation based on SLA involving both RAN and to emulate lightweight VNFs. Each slice is separated by
core networks [6]. Similarly, Zhang et al. proposed a multi- VLAN tagging and CPU pinning, allowing for the
tier orchestration model for 5G slicing, underpinned by concealment of resource contention at runtime.
predictive scaling and healing using machine learning [7]. iperf and custom scripts are used to generate synthetic loads
These orchestration policies tend to reduce overhead and that mimic the traffic from a servicing application. High-
maintain quality of service guarantees for each slice. throughput TCP/UDP flows mimic streaming services and
Studies assessing performance as of 2020 use simulated large file downloads for the eMBB slice. The URLLC slice
environments and simulation tools. Sabella et al. measured generates latency-critical packets with high-accuracy
end-to-end latency for eMBB and URLLC slices using timestamping to compute one-way latency and jitter, and the
OpenAirInterface and FlexRAN, demonstrating the mMTC slice forwards a massive number of low-bandwidth
possibility of achieving sub-10 ms latency with dedicated MQTT messages, mirroring MQTT-based IoT device
resource allocation [8]. Alsafasfeh et al.\ used mininet and telemetry. Traffic is generated via simulated user equipment
ONOS controllers to study inter-slice traffic disturbance and interfaces connected to gNodeBs, which are realized on
the balance between strict isolation and resource sharing [9]. srsRAN and connected to the Open5GS core. This setup
On the service side, several studies have examined how provides full traffic patterns end-to-end for the realistic
different slice types behave under load. For instance, Bega et evaluation of slice performance.
al. employed empirical models to define the resource Both active and passive measurement tools generate
elasticity for mMTC slices and demonstrated how light performance measurements. Ping and D-ITG are used to
orchestration can greatly alleviate signaling overhead while collect RTT, packet loss, and jitter, while Iperf and sFlow-RT
achieving adequate scalability [10]. On the other hand, the are set up for throughput monitoring. Values of the control
performance of eMBB in slice contention was explored in [11], plane metrics, such as the slice instantiation time and the CPU
where the authors noticed a decrease in throughput when utilization of core functions, are monitored by Prometheus
slices were not granted resources at the kernel level. and Grafana. The orchestration manager logs the `slice
Security and enforcing SLA also became issues that need elasticity' and partitions scaling time, reconfiguration success
urgent attention. Li et al. studied isolation violations in multi- rate, and recovery from failures for degradation. They further
slice scenarios and suggested container-level improvements experiment under different conditions, such as slice load
for isolation for 5GC [12]. QoS-aware schedulers and SLA- stress, multi-slice enqueuing, and dynamic slice scaling, to
650 | P ag e

International Journal of Multidisciplinary Research and Growth Evaluation www.allmultidisciplinaryjournal.com
see how it functions under normal and stressed conditions. differentiated services under a shared infrastructure model.
Experiments on controlled interference scenarios are The eMBB slice demonstrated consistent high-throughput
provided to verify the slice isolation and resource efficiency performance, maintaining average downstream throughput of
of the testbed. Activity loads are applied on one slice to 950 Mbps with negligible jitter (<5 ms) and packet loss
monitor overflow to the neighboring slices. Metrics such as (<0.01%) during peak load conditions. This was attributed to
inter-slice latency drift and CPU contention are continuously the dedicated bandwidth assignment via the UPF and
tracked to measure the fidelity of isolation. The effect of efficient traffic steering through SDN policies. Even when
orchestration delay is also investigated by initiating dynamic neighboring slices experienced bursty traffic, the throughput
slice instantiations and measuring how long it takes for the in the eMBB slice showed only a marginal 2% degradation
operation to reach a steady state. These comments give a due to effective VLAN isolation and CPU affinity
complete characterization of the isolating/resource trade-offs configuration. This confirmed the slice’s robustness in
in shared network settings. supporting bandwidth-intensive applications such as video
This approach offers a multidimensional insight into the streaming and large data transfers.
performance of network slicing by examining the technical In contrast, the URLLC slice exhibited excellent latency
behavior of the slice components, as well as the orchestration behavior, consistently achieving one-way latency of less than
system's response time. The simulated environment ensures 7 ms, even during concurrent load events in the testbed. The
the hardware neutrality of the results and the realistic deployment of preemptive scheduling and real-time kernel
behavior of the traffic by utilizing open-source tools. The prioritization enabled the URLLC slice to meet stringent
approach is particularly convenient, as it focuses on delay budgets. However, jitter values exhibited variability
reproducibility, system completeness, and metric variety, when dynamic slice reconfiguration was triggered during live
allowing for an in-depth assessment of network slicing in a 5 URLLC sessions, with brief spikes reaching up to 12 ms. This
G Core (5GC) scenario. highlights the need for optimization of the orchestration layer
to ensure ultra-reliability under dynamic conditions.
4. Results The mMTC slice demonstrated high scalability in a dense
The performance evaluation of network slicing in the 5G device scenario, successfully supporting up to 50,000
Core (5GC) network yielded a comprehensive set of simulated IoT devices that sent telemetry at 10-second
observations derived from over 60 experimental runs. Each intervals. The control plane remained stable with minimal
slice, eMBB, URLLC, and mMTC, was subjected to CPU overhead (<30%) across AMF and SMF functions.
controlled conditions and service-specific workloads to Packet loss remained below 0.05%, and slice elasticity
assess behavior across different performance dimensions. mechanisms responded efficiently to increased device
The core performance metrics analyzed include latency, registration load, scaling out UPF instances in under 2
jitter, throughput, packet loss, control plane overhead, slice seconds. The key observation in the mMTC context was the
instantiation time, CPU/memory utilization, and inter-slice negligible impact on adjacent slices, despite the massive
interference. These results provide a concrete understanding signaling load, which validated the effectiveness of control
of how well 5 G Core (5GC) slicing supports the delivery of plane decoupling.
Fig 1: Performance Comparison of Slices
The bar chart compares latency and throughput across the in) for eMBB slices took approximately 6 seconds on
three slice types, based on experimental results from average, reflecting the overhead associated with high-
synthetic traffic workloads. bandwidth VNF instantiation and inter-VNF state
Slice instantiation and reconfiguration times were also synchronization. Slice teardown time was fastest for mMTC
benchmarked. Initial slice deployment times averaged 4.3 due to the lightweight nature of the traffic and minimal
seconds, with URLLC slices benefiting from faster session context.
instantiation (3.1 seconds) due to pre-defined policies and Resource isolation was tested by injecting artificial CPU
container images. Dynamic scaling (both scale-out and scale- contention in the eMBB slice. The mMTC and URLLC slices
651 | P ag e

International Journal of Multidisciplinary Research and Growth Evaluation www.allmultidisciplinaryjournal.com
maintained stable operation, indicating strong CPU pinning services. ULRLLC slices realized ultra-low latency through
and scheduler enforcement. However, when memory the prioritization, kernel tuning, and preemption provisions
contention was introduced, performance degradation was that are mandatory for time-sensitive applications, like AVs
more noticeable across slices, with latency increasing by 15– and telehealth. mMTC slices proved to be scalable and
20% in URLLC and CPU load surging to 85% in SMF lightweight container-based VNFs, and stateless signaling
containers across all slices. These findings suggest that while mechanisms coped even with such a high number of devices.
CPU isolation mechanisms are effective, memory resource Such a multi-dimensional performance demonstrates that
enforcement requires further refinement to prevent inter-slice 5GC, combined with the adoption of Lean slice-specific
resource starvation. policies, can deliver the guaranteed services required by
Finally, orchestration overhead was quantified by observing heterogeneous verticals.
the response time of slice adaptation actions. The orchestrator Although good results have been achieved, some operational
responded to SLA violations within an average of 5.8 issues have been encountered, including orchestration
seconds, initiating scaling or re-routing actions. This latency and resource conflicts. Despite successfully isolating
response time was acceptable for eMBB and mMTC CPU utilization via pinning and affinity rules, concurrent
scenarios but posed a potential risk for latency-sensitive slice reconfiguration led to temporary quality of service
URLLC traffic. Monitoring overhead was also found to degradation due to memory contention, particularly in
contribute 8–10% CPU usage across orchestration VNFs, URLLC slices. These results indicate that CPU and I/O
suggesting a trade-off between real-time insight and isolation are well-developed in NFV-based slicing
infrastructure efficiency. environments. At the same time, multi-player memory
management (especially shared buffer allocation) needs to be
5. Discussion improved to prevent interference from other slices. This is
The results obtained in the virtualized 5GC testbed especially important in scenarios of edge or multi-access
demonstrate strong evidence for the potential ways in which edge deployments, as the hardware constraints are more
Network Slicing can indeed deliver on the promise of stringent, and the response time is low.
providing differentiated and SLA-compliant service across The orchestration layer itself is also functional, but its
different communication domains. However, these findings response time was experienced to take between 3 and 8
also reveal several practical concerns and compromises that seconds during SLA violations and slice adjustments. This
need to be reconciled to deploy network slicing at scale in delay may be acceptable in eMBB and mMTC slices, but in
real-life production. In this talk, I examine what slicing URLLC scenarios, a 2–3 second delay in reallocating or
performance metrics reveal about the impact of isolation rescheduling resources may jeopardise safety or wreck
mechanisms, the trade-offs in orchestration with dynamic operational reliability. These results emphasize the
slice management, and architectural bottlenecks under stress. importance of cloud-native, predictive, or proactive
The most exciting result of our performance experiments is orchestration systems that can leverage live telemetry and AI-
the capability of slicing to impose separate behavior on informed policy engines. These processes could enable
service classes, especially in high-concurrency scenarios. preemptive scaling in advance of SLA violations or failover
The eMBB slice provided stable high throughput and low mitigations, thereby preventing them from occurring.
packet loss, demonstrating its capability to host data-driven
Fig 3: Orchestration Latency and Slice Response Time
Another interesting finding is the effect of slice elasticity on severe bottleneck, particularly in mobile devices, where users
service continuity. Creating a slice typically took less than 5 are mobile across slice domains and require ultra-fast and
seconds, but re-scaling a slice was significantly longer, seamless handovers. The inclusion of stateless VNFs, or even
especially for high-bandwidth slices, such as eMBB. the use of function state migration, may minimize re-scaling
However, the overhead due to VNFs for state synchronization and recovery time, enhancing the overall flexibility of the
and session continuity was non-negligible. This becomes a network.
652 | P ag e

International Journal of Multidisciplinary Research and Growth Evaluation www.allmultidisciplinaryjournal.com
From the perspective of management and orchestration highlighted significant limitations and areas requiring further
(MANO), even the resource consumption of monitoring and optimization.
control became an issue. The orchestration agents used 10% Orchestration overhead and memory resource contention
of the CPU in peak reconfiguration times. While such a cost emerged as critical bottlenecks. While the slicing control
is bearable in small-scale networks, it can be expensive in plane was generally effective in enforcing slice boundaries
large-scale scenarios where thousands of concurrently online and monitoring performance, the dynamic response time
slices are present. In the future, it will be necessary to during scaling and SLA violations averaged over 5 seconds.
consider the efficiency of the telemetry pipeline and the This is acceptable for eMBB and mMTC traffic but
frequency of the control loop to maintain the tradeoff inadequate for URLLC, where delay budgets are much
between visibility and infrastructure load. tighter. Additionally, even with strong CPU isolation, shared
The isolation experiments also indicated that a complex memory utilization introduced variability in slice behavior,
balance exists between rigid resource segregation and the particularly under stress, indicating the need for more fine-
network's ex ante utilisation efficiency. Strong isolation grained isolation mechanisms beyond current container-
ensures service fidelity, but over-provisioning leads to based virtualization strategies. These challenges must be
suboptimal resource utilization. On the contrary, the sharing addressed to ensure consistent performance, especially as
resource model can lead to higher load while risking breaches deployment scenarios become more dynamic and edge-
of SLAs. A slicing model hybridized with an isolation intensive.
strength dynamically adapted to the real-time network state Another important takeaway from this study is the trade-off
and forecasted traffic trend might present a valid compromise between slice isolation and infrastructure efficiency. While
with a better balance. This also indicates a general need for strict isolation ensures SLA adherence, it also leads to
slice admission control by global resource context. underutilization of shared resources. Conversely, overly
The debate highlights that while network slicing is shared infrastructures risk inter-slice interference and
technically feasible and operationally effective in restricted degradation of service quality. A promising approach lies in
environments, deploying it at an industrial and national scale adaptive, hybrid resource allocation models that can
will necessitate a dedicated set of enhancements. These intelligently balance isolation strength and utilization based
techniques include sophisticated memory isolation, on traffic predictions and slice priority. Such models will
predictive and autonomous orchestration, efficient and rapid require the integration of AI/ML capabilities into slice
scale-out methods, and hybrid resource management orchestrators to provide real-time, predictive slice
mechanisms. Overcoming these challenges will be essential management and proactive enforcement of SLAs.
to achieve the full potential of 5G network slicing and This paper contributes to the ongoing discourse on 5G
develop programmable, flexible, and service-centric network network slicing by providing empirical evidence,
infrastructures. reproducible methods, and performance benchmarks for real-
world deployment considerations. The methodology and
6. Conclusion results provide a foundation for future research and practical
This study has conducted a detailed performance evaluation implementations aimed at optimizing the service granularity
of network slicing within 5G Core (5GC) networks, with a and reliability of 5 G Core (5GC). The testbed architecture,
particular focus on the three key service categories defined traffic emulation scenarios, and orchestration policies used in
by 3GPP: Enhanced Mobile Broadband (eMBB), Ultra- this work can be extended to evaluate other dimensions of
Reliable Low-Latency Communications (URLLC), and slicing, such as mobility management, security, and multi-
massive Machine-Type Communications (mMTC). Using a domain orchestration across core and edge networks.
virtualized, open-source emulation environment based on Looking ahead, future research should explore advanced slice
Open5GS, Mininet, and SDN/NFV orchestration, the lifecycle management frameworks incorporating
research has shown that network slicing is a viable and reinforcement learning, container-native observability
effective method for delivering differentiated service solutions, and edge-aware orchestration for latency-sensitive
experiences over a common infrastructure. The experiment’s services. Additionally, slice-level security enforcement,
findings demonstrate that when implemented with proper inter-operator slicing across federated infrastructures, and
slice orchestration, resource partitioning, and monitoring SLA monetization models offer promising avenues for
strategies, network slicing can provide the required investigation. As 5G matures and converges with 6G visions
performance isolation, SLA compliance, and elasticity for of ultra-dense networks and AI-native infrastructure, robust
modern service delivery across varied 5G verticals. and intelligent slicing mechanisms will be indispensable to
The quantitative results validated the ability of the 5GC delivering programmable, dynamic, and secure next-
architecture to support high-throughput eMBB services with generation mobile services.
minimal packet loss, ultra-low-latency URLLC traffic with While network slicing in 5G Core networks has matured to a
sub-10ms round-trip times, and high-scale mMTC scenarios point of practical feasibility, achieving consistent, low-
involving tens of thousands of concurrent IoT devices. The latency, high-isolation, and dynamically elastic service
performance characteristics for each slice were generally delivery across all verticals requires a continued focus on
preserved even during concurrent operation and dynamic orchestration intelligence, isolation robustness, and scalable
slice scaling events. Furthermore, the application of monitoring. The lessons and findings from this research will
container-based VNFs, combined with traffic engineering via serve as a crucial reference point for academic, industrial, and
SDN and efficient CPU pinning, proved essential in regulatory stakeholders advancing the next phase of 5G
achieving reliable performance and resource isolation in evolution.
multi-slice environments. However, the study also
653 | P ag e

  International Journal of Multidisciplinary Research and Growth Evaluation  www.allmultidisciplinaryjournal.com
7. References
| 1.  NGMN  |     | Alliance.  | Description  |     | of  Network  |     | Slicing  |     |     |
| --------- | --- | ---------- | ------------ | --- | ------------ | --- | -------- | --- | --- |
Concept. NGMN 5G P1. 2016.
2.  3rd Generation Partnership Project. System Architecture
for the 5G System (Release 15). 3GPP TS 23.501. 2019.
| 3.  European  |     | Telecommunications  |     |     | Standards  | Institute.  |     |     |     |
| ------------- | --- | ------------------- | --- | --- | ---------- | ----------- | --- | --- | --- |
Network Functions Virtualisation (NFV); Architectural
Framework. ETSI GS NFV 002 V1.2.1. 2014.
| 4.  Open  |     | Networking  |     | Foundation.  | Software-Defined  |     |     |     |     |
| --------- | --- | ----------- | --- | ------------ | ----------------- | --- | --- | --- | --- |
Networking: The New Norm for Networks. ONF White
Paper. 2012.
5.  Mijumbi R, Serrat J, Gorricho JL, Bouten N, De Turck
F, Boutaba R. Network Function Virtualization: State-
| of-the-Art  |     | and  | Research  | Challenges.  | IEEE  | Commun  |     |     |     |
| ----------- | --- | ---- | --------- | ------------ | ----- | ------- | --- | --- | --- |
Surv Tutor. 2016;18(1):236-262.
| 6.  Foukas X, Patounas G, Elmokashfi  |     |     |     |     | A, Marina MK.  |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
Network Slicing in 5G: Survey and Challenges. IEEE
Commun Mag. 2017;55(5):94-100.
7.  Zhang H, Liu N, Chu X, Long K, Aghvami A, Leung
VCM. Network Slicing Based 5G and Future Mobile
| Networks:  |     | Mobility,  |     | Resource  | Management,  |     | and  |     |     |
| ---------- | --- | ---------- | --- | --------- | ------------ | --- | ---- | --- | --- |
Challenges. IEEE Commun Mag. 2017;55(8):138-145.
8.  Sabella D, Serrano P, De Marinis E, Sanguineti A, Virdis
A, Stea G. End-to-End Latency Evaluation for 5G eMBB
and URLLC Use Cases with OpenAirInterface. In: IEEE
| International  |     | Conference  |     | on  | Communications  |     | (ICC).  |     |     |
| -------------- | --- | ----------- | --- | --- | --------------- | --- | ------- | --- | --- |
2018.
| 9.  Rostami  |     | P,  Zanzi  | L,  | Widmer  | J.  Dynamic  | Resource  |     |     |     |
| ------------ | --- | ---------- | --- | ------- | ------------ | --------- | --- | --- | --- |
Isolation for Network Slices in 5G Networks. IEEE
Trans Netw Serv Manag. 2019;16(3):1023-1036.
10. Bega D, Gramaglia M, Banchs A, Sciancalepore V,
Costa-Perez X. Optimising 5G Infrastructure Markets:
The Business of Network Slicing. In: IEEE INFOCOM.
2017.
11. Zanzi L, Widmer J, Pentikousis K. On the Performance
of End-to-End Network Slicing in 5G. In: IEEE/IFIP
Integrated Management Symposium (IM). 2019.
| 12. Li     | X,  Cao  | J,  He   | Y.               | Enhancing  | 5G         | Network  | Slice  |     |     |
| ---------- | -------- | -------- | ---------------- | ---------- | ---------- | -------- | ------ | --- | --- |
| Isolation  |          | Through  | Container-Based  |            | Security.  |          | IEEE   |     |     |
Netw. 2019;33(3):183-189.
| 13. Sciancalepore  |     | V,  | Samdanis  |      | K,  Costa-Pérez  |     | X.  A   |     |     |
| ------------------ | --- | --- | --------- | ---- | ---------------- | --- | ------- | --- | --- |
| Double-Sided       |     |     | Platform  | for  | Dynamic          | 5G  | Tenant  |     |     |
Allocation. IEEE Netw. 2018;32(6):14-21.
14. Bernabeu-Auban G, Mangues-Bafalluy J, Gramaglia M.
| Orchestrating  |     | End-to-End  |     | Network  | Slices  | in  | 5G:  A  |     |     |
| -------------- | --- | ----------- | --- | -------- | ------- | --- | ------- | --- | --- |
Survey. Comput Netw. 2020;178:107343.
| 15. Xiang  | H,  | Wang       | Y,  Zhang  |       | L.  QoS-Aware           | Network        |     |     |     |
| ---------- | --- | ---------- | ---------- | ----- | ----------------------- | -------------- | --- | --- | --- |
| Slicing    |     | for  5G    | Networks:  |       | A  Deep                 | Reinforcement  |     |     |     |
| Learning   |     | Approach.  |            | IEEE  | Access.  2020;8:179774- |                |     |     |     |
179783.

|     |     |     |     |     |     |     |     |           |       |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- |
|     |     |     |     |     |     |     |     |   654 | P | ag e  |