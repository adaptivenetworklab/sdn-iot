# QoS-based Routing over Software Defined Networks (Rasppi as OvS)

> Source file: `QoS-based Routing over Software Defined Networks (Rasppi as OvS).pdf`

---

QoS-based Routing over Software Defined Networks
Andrew Kucminski, Ahmed Al-Jawad, Purav Shah, Ramona Trestian
School of Science and Technology,
Middlesex University
London, UK
{MK1629, AA3512}@live.mdx.ac.uk, {p.shah, r.trestian}@mdx.ac.uk
Abstract—Quality of Service (QoS) relies on the shaping of  entity is not aware of the whole network topology. Moreover,
preferential  delivery  services  for  applications  in  favour  of  the traditional networking industry has been dominated by
ensuring sufficient bandwidth, controlling latency and reducing  vendors with their proprietary management and solutions that
packet  loss.  QoS  can  be  achieved  by  prioritizing  important  sometimes fail to satisfy their customers’ needs. In this context,
broadband  data  traffic  over  the  less  important  one.  Thus,  the main goal for Software Defined Networks (SDN) and the
depending on the users’ needs, video, voice or data traffic take
OpenFlow technology is to separate the hardware from the
different priority based on the prevalent importance within a
control software layer enabling the network operators to build
particular context. This prioritization might require changes in
|     |     |     |     |     |     |     |     | cheaper  | and  easier  | to  manage  | networks  |     | by  allowing  | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | ----------- | --------- | --- | ------------- | ---- |
the configuration of each network entity which can be difficult in
|     |     |     |     |     |     |     |     | network  | to  be  open  | and  programmable.  |     |     | This  implies  | that  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | ------------------- | --- | --- | -------------- | ----- |
traditional  network  architecture.  To  this  extent,  this  paper  network  automation  as  data  traffic  can  be  manipulated,
| investigates  | the  | use  of  | a  QoS-based  |     | routing  | scheme  | over  a  |     |     |     |     |     |     |     |
| ------------- | ---- | -------- | ------------- | --- | -------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
diverted and adjusted regardless of routing protocols.
| Software     | Defined  | Network    | (SDN).  |                | A  real  | SDN  test-bed  | is   |     |     |     |     |     |     |     |
| ------------ | -------- | ---------- | ------- | -------------- | -------- | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| constructed  | using    | Raspberry  |         | Pi  computers  |          | as  virtual    | SDN  |     |     |     |     |     |     |     |
switches managed by a centralized controller. It is shown that a
| QoS-based  | routing  | approach  |     | over  SDN  | generates  | enormous  |     |     |     |     |     |     |     |     |
| ---------- | -------- | --------- | --- | ---------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
control possibilities and enables automation.
| Keywords—Quality  |     |     | of  Service,  | Software  |     | Defined  Networks,  |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ------------- | --------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Prioritized Routing, Networking.
|     |     | I.  |  INTRODUCTION  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Nowadays, it is hard to imagine end-user devices without
Internet connection. Similarly, all the big organizations have
their own computer network connected to other organizations
networks. As this network of networks is growing in recent
years with a truly incredible speed, several trends are driving
| users,  organizations  |     | or  | network  | providers  |     | to  develop  | new  |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | -------- | ---------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
network architectures. According to [1], these trends could be
| devised  | into  | three  | main  categories:  |     | increasing  | demand,  |     |     |     |     |     |     |     |     |
| -------- | ----- | ------ | ------------------ | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |

| increasing  | supply  | and  | complex  | traffic  | patterns.  | Increasing  |     |     |     |     |     |     |     |     |
| ----------- | ------- | ---- | -------- | -------- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
demands  refer  to  trends  that  increase  load  on  enterprise  Fig. 1. OpenFlow Network
networks as well as the Internet such as: Internet of Things
(IoT), Big Data, cloud computing and mobile  data traffic.    A traditional Ethernet switch consists of : data path – which
Increasing supply is caused by rising demands which leads to  represents the part dedicated to the hardware, responsible for
capacity expansion of network technologies, such as 4G or 5G
packet forwarding; and the control path – which represents the
over  Wi-Fi.  If  an  organization  requires  specific  network  part dedicated to the software, responsible for taking decisions,
behavior, an application can be developed according to specific  similar to an operating system.
| needs.  | These  | applications  |     | can  be  | specific  | to  common  |     |     |     |     |     |     |     |     |
| ------- | ------ | ------------- | --- | -------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
In order to provide more control over the network, the
| networking  | functions  |     | like  traffic  | engineering  |     | and  security,  |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | -------------- | ------------ | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
OpenFlow enabled switch separates the control plane from the
| Quality  | of  Service  | (QoS),  | routing,  |     | switching,  | monitoring,  |     |     |     |     |     |     |     |     |
| -------- | ------------ | ------- | --------- | --- | ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
virtualization and load balancing. QoS requirements forced on  data plane. The control plane is moved outside the switch
enabling remotely control of the data plane through a secure
| the  network  | are  | extended  | as  | a  result  | of  | the  multitude  | of  |     |     |     |     |     |     |     |
| ------------- | ---- | --------- | --- | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
channel, as seen in Fig. 1. The control functions reside on the
applications, and then network traffic load must be orchestrated
|     |     |     |     |     |     |     |     | OpenFlow  | Controller,  | making  | them  | independent  |     | of  the  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ------- | ----- | ------------ | --- | -------- |
in an increasingly sophisticated and agile way.
hardware they control. OpenFlow provides an abstraction of
In a traditional network, operators configure each node
|     |     |     |     |     |     |     |     | the  data  | plane  through the  |     | use  of  | flow  table  | that  | can be  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------- | --- | -------- | ------------ | ----- | ------- |
individually by using Command-line Interface, but this option  controlled  over  the  secure  channel  by  the  OpenFlow
can be limited to the functionality already installed. Large  Controller.  By  making  use  of  OpenFlow  controllers,  the
networks can contain many nodes to configure or reconfigure  network  administrators  will  be  able  to  define  flows  and
| to implement new routing policies and any single network  |     |     |     |     |     |     |     | policies.   |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
978-1-5090-4937-0 Copyright © by IEEE

TABLE I.  RELATED WORKS SUMMARY
Ref  Objective  Performance Metric  Evaluation Environment  Findings
[8]  Validate OpenFlow and test  Validate OpenFlow function.  SDN testbed with Open vSwitch  Similar performance to net-FGPA.
maximum throughput  Maximum throughput with  on Raspberry Pi  OpenFlow functionality successfully
|     |     |     |     | different segment sizes.  |     |     |     |     |     |     | operated.  |     |     |
| --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
[9]  Open vSwitch design and  High performance and  Hypervisor  Virtualization and flows controlling
implementation.  optimization, flow caches  resulted with gradual optimatization
for datacenters requirements
workload.
[10]  Flow reconfiguration and  Link up latency and link down  SDN testbed called Pi Stack  Network Administrator can recognize
efficient response to service  latency.  Switch  link state and topology changes in less
|     | demands through SDN.  |     |     |     |     |     |     |     |     |     | than one second.  |     |     |
| --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- |
[11]  SDN management and  Various types of policies such  Deployed in a campus network  Procera is feasible for network
configuration tasks across  as: time, data usage,  and a home network.  policies, reduces the complexity of
different network types.  authentication status, and  network management considerably for
|     |     |     |     |     | traffic flow.  |     |     |     |     | a range of network settings and  |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- |
|     |     |     |     |     |                |     |     |     |     | various network policies.        |     |     |     |

[12]  Build and test OpenFlow based  Throughput   Open vSwitch installed on laptop  OpenFlow-based laptop mirroring
mirroring switch.  and on Raspberry Pi as mirroring  switches are more useful then
|     |     |     |     |     |     |     |     | switch.  |     | Raspberry Pi for port mirroring.  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --------------------------------- | --- | --- | --- |

[13]
Analytic Hierarchy Process  Top five SDN controllers  Using Analytic Hierarchy Process  Ryu is the best SDN controller taking
(AHP) to select the best SDN  considering their current  (AHP) to select the best open  into account the specific requirements.
|     |     | controller.  |     | deployment and utilization.   |     |     | source SDN controller.   |     |     |     |     |     |     |
| --- | --- | ------------ | --- | ----------------------------- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |

[14]  SDN Controllers Performance  Round Trip Time (RTT), TCP  Mininet tree topology simulation   POX is not recommended for
|     |     | Testing  |     |     | bandwidth  |     |     |     |     | environments where performance is  |     |     |     |
| --- | --- | -------- | --- | --- | ---------- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- |
crucial.
  In this context, the control of network traffic flows is  even real-time communications. Its main advantage is that it
moved  from  the  infrastructure  (switches  and  routers)  to  simplifies monitoring and troubleshooting problems because it
administrators.  provides  a  high  level  of  visibility  of  the  service  quality
indicators, transmission of multimedia in real time and efficient
  Because evidently there are more and more users, devices
and effective traffic management. Caba et al. [4] investigated
and services on the network, imposing changes in the network
QoS in the context of SDN showing a significant evaluation
infrastructure paves the way for new technologies such as
|     |     |     |     |     |     |     | improvement and increase  |     |     | in traffic  | utilization  | in network  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | ----------- | ------------ | ----------- | --- |
SDN. In the industry, the benefits of SDN technologies can be
|     |     |     |     |     |     |     | throughput  | over  | bandwidth  | allocation  | and  | fairness  | among  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ---------- | ----------- | ---- | --------- | ------ |
seen in several networking sectors including: service providers,
various traffic classes. The evaluation results also proved that
Enterprise Campus Infrastructure, Data Centre and Clouds and
actual QoS Config API is satisfying performance to enable
Wide Area Networks.
dynamic configuration QoS on forwarding devices. SDN as
This paper investigates the use of QoS-based routing over  relatively new technology is attractive to researches for tests
SDN. A real experimental SDN test-bed using Raspberry Pi  under various environments. Araniti et al. [5] investigated the
computers was built. The experiments demonstrate that QoS  performance  of  SDN  over  wireless  environments  and
concluded that the use of OpenFlow introduces benefits in
can be delivered not only by prioritizing some data traffic
|     |     |     |     |     |     |     | terms  of  | end-to-end  | delay,  | throughput,  | and  | jitter.  | Bayes'  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ------- | ------------ | ---- | -------- | ------- |
(e.g., multimedia streams) but also by redirecting particular
theorem and Bayesian network model were used in [6] to find
| traffic  flows  | through      |      | different  links         | aiming  | at        | optimal  |            |           |               |                  |                       |                   |     |
| --------------- | ------------ | ---- | ------------------------ | ------- | --------- | -------- | ---------- | --------- | ------------- | ---------------- | --------------------- | ----------------- | --- |
|                 |              |      |                          |         |           |          | the  most  | feasible  | path          | that  satisfies  | the                   | QoS  constraint.  |     |
| bandwidth       | utilization  | and  | fulfilling requirements  |         | based on  |          |            |           |               |                  |                       |                   |     |
|                 |              |      |                          |         |           |          | Whereas    | in  [7],  | the  authors  | propose          | a  compression-based  |                   |     |
valid policies.
technique for SDN that aims at decreasing the link usage for
QoS applications while increasing the network observability.
II.  RELATED WORKS
SDN has already  produced remarkable  interest  from  both,    However, despite of testing SDN using virtual machines
such as well know network emulator Mininet1, test-beds that
| academia  | and  industry.  |     | SDN  with  | OpenFlow  | was  | first  |     |     |     |     |     |     |     |
| --------- | --------------- | --- | ---------- | --------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
introduced by McKeown et al. in [2] as a promising way to  utilize low cost tiny computer machines with embedded open
enable innovation in production networks. Even though its first  source Linux software can also be explored.
| purpose  was  | for researchers  |     | to run  | experimental protocols  |     |     |                                                             |     |     |     |     |     |     |
| ------------- | ---------------- | --- | ------- | ----------------------- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|               |                  |     |         |                         |     |     |   Kim et al. [8] tested the OpenFlow functionality over an  |     |     |     |     |     |     |
within their campus network, its advantages made it suitable
experimental test-bed created using two Raspberry Pi with
for commercial networks, being adopted by major players in
OpenVSwitch [9] and Floodlight2 as the SDN controller. The
the market. For example, Google is using SDN with OpenFlow
authors highlighted the many benefits of the low complex
technology since 2010 in order to reduce the backbone network
|     |     |     |     |     |     |     | experiment  | including  | effective  | performance  |     | comparable  | to  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ---------- | ------------ | --- | ----------- | --- |
complexity and improve performance [3].

|   The  SDN  | architecture  |     | can  enable  |     | the  dynamic  | QoS  |     |     |     |     |     |     |     |
| ----------- | ------------- | --- | ------------ | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
1 Mininet - http://mininet.org/
provisioning for various applications such as voice, video and
2 Floodlight - http://www.projectfloodlight.org/floodlight/

much more expensive devices, low cost and easy (cid:120) Set of Rules and Path Install block sends the computed
programmable. However, they assessed that Raspberry Pi with paths and rules to the switch.
only one Ethernet interface is not sufficient to process multiple
(cid:120) Network Map block is used to store a map of the
connection individually. Thus, Han et al. [10] developed
network.
another SDN experimental test-bed based on Raspberry Pi,
created on Pi Stack Switch using the Network – Hypervisor
called OpenVirteX. They addressed the issue of one Ethernet B. QoS Path Computation
device by making use of USB to Ethernet adapters. This way The QoS Routing is done based on a weighted routing
the authors managed the network architecture with four algorithm as the one proposed in [15]. When the controller
Raspberry Pi computers, where one Raspberry Pi acted as a receives a packet of a new flow, it computes all the possible
controller and three others as OpenFlow protocol supported paths the flow might take to reach the destination. For each
switches. By use of OpenVirteX hypervisor with virtualization path, a weight is computed based on the current load. The path
functionality they created Pi Stack Switch with 10 ports. The with the highest weight is selected as the target. The switch
tests included topology changes latency, amount of time port counters are used to collect information about the load for
reaction due to a network failure and state changes of links. each link, identify the imbalances in the traffic load and
compute the paths weight.
As there is still a lot of on-going work within the OpenFlow
technology, understanding its performance limitations is Thus, assuming the network topology represented by a
crucial before using it in large-scale deployments. A summary connected graph G = (V, E), with the set of nodes V and the
of related works is listed in Table I. directed set of edges E. Given F(cid:1256)V2 as the set of source-
destination flows, a set N of shortest paths between any
(s,d)
III. QOS-BASED FRAMEWORK FOR SDN source-destination pairs (s, d) ϵ F is computed. Furthermore,
we assume that for any node v ϵ V, any path i ϵ N has a
(s,d)
A. System Architecture number of M subpaths and each subpath j ϵ M has a number of
i i
S segments. We denote with λ and c the traffic link load,
The general QoS-based framework for SDN is illustrated in ij kji kji
which is taken from the SDN switch port counters by polling
Fig. 2. The framework consists of a SDN controller integrating
the switch port using standard OpenFlow mechanisms, and the
custom modules to manage routing, SDN Switch implementing
link capacity on segment k, of subpath j, of path i, respectively.
the flow tables, and the end-host running the applications. The
Thus, the Link Utilisation Ratio (LUR) is defined as in (1) [15].
interaction between the SDN Controller and the SDN Switch is
done using the OpenFlow Protocol.
(1)
Furthermore, at each node v ϵ V, and for any path the flow
could take to reach the destination, a weight is computed. Thus,
for any path i ϵ N the weight w is computed using (2) [15]
(s,d) i
where w ϵ [0,1] and . The highest the path weight,
i
the less loaded the path is. The path is is selected as the target
path and the set of rules and path install instructions are sent to
the SDN switches on the path.
(2)
Fig. 2. System Architecture
The SDN controller consists of the following functional blocks: IV. EXPERIMENTAL SETUP
(cid:120) Topology block is used to store information about all
A. Experimental Test-Bed Setup
devices, ports and the links currently up in the network.
A real experimental test-bed was setup, as illustrated in Fig.
The topology discovery is done by generating link
3, consisting of four Raspberry Pi running the Open vSwitch
events using the Link Layer Discovery Protocol
(OVS), two host PCs, a Server and the Open Network
(LLDP) packets.
Operation System (ONOS)3 Controller. Each Raspberry Pi is
(cid:120) Stats Collector block is used to keep track of the links equipped with several USB to Ethernet adapters to enable
load by periodically collecting load information from multiple Ethernet ports on the OVS SDN switches and create a
the switch ports counter. multi-path environment. The four OVS devices are managed
by one centralized SDN controller ONOS installed on an Apple
(cid:120) Path Weight block is used to compute a weight for
MacBook Pro machine running El Captian operating system.
each path in the topology. The weight is computed
Table II presents a list with the hardware specification used for
based on the available link capacity.
the experimental setup.
(cid:120) QoS Path Compute block is used to compute the paths
the flows could take to reach the destination and enable
QoS provisioning. 3 ONOS - http://onosproject.org/

Fig. 3. Experimental Test-Bed
V. RESULTS AND DISCUSSIONS
TABLE II. LIST OF HARDWARE COMPONENTS FOR EXPERIMENTAL TEST-BED
A. Test-Bed Limitations
Hardware Version Specification
Quad Core CPU 900 The overall test-bed setup was tested in order to determine
Raspberry Pi 2 Model B MHz, 1GB RAM, 16GB the capacity and the maximum available resources. This was
ROM done using iPerf. The Raspberry Pi 2 model B is equipped with
USB 2 Fast Ethernet
VK-QF970 RJ45 10 one RJ45 10/100 network socket and four USB ports. Thus, to
Adapter
enable us to create a mesh topology network four USB to
USB Fast Ethernet
Adapter D Link RJ45 10/100 Ethernet adapters were used for each Raspberry Pi. Although,
Network Cables Cat 5e Up to 100Mbps Raspberry Pi has sufficient processing power to handle the
Sony VAIO connected USB to Ethernet adapters, the tested speed of the
VPCJ 12 LOE
workstation adapters turned out to achieve 4Mbps only, which limited the
HP Laptop ProLiant Gen8 G1610T overall test-bed capacity. Thus, the maximum generated traffic
Apple Laptop MacBook Pro 13
in case of UDP was set at 3 Mbps.
NETGEAR GS305-
Switch 5-Port Gigabit
100UKS
B. System Throughput
B. Experimental Scenarios
The overall test-bed is monitored and managed by the
Several experimental scenarios are considered to test the
ONOS controller which also enables us to view the network
performance of QoS-based routing over the real experimental
topology with all the devices and the active flows through the
test-bed, such as: continuous UDP traffic is generated between
ONOS GUI. We investigated the maximum throughput that
the PC0 host and the Server considering four data rates: 0.5
can be achieved by the system when using the shortest path and
Mbps, 1Mbps, 2Mbps and 3Mbps. Whereas, TCP traffic is
the QoS-based path. In the first case, all the traffic is routed
generated between the PC1 host and the Server. iPerf version 3
over the shortest path following the OVS4-OVS2 link (see Fig.
was used for generating traffic. In this case, we investigate the
3). In the case of QoS-based routing, as UDP starts first, it will
use of QoS-based routing and shortest path routing.
occupy the shortest path. When the TCP traffic starts, the SDN
Additionally, a link failover scenario is considered where the
controller will route it through the next less congested path,
shortest path link is disturbed while PC1 host is transmitting
using the OVS4-OVS3-OVS2 links. In this way, the imbalance
data to the Server.
in the traffic load over the experimental test-bed is avoided.
Fig. 4 illustrates the achieved throughput from the ONOS GUI
for various data rates of the UDP traffic (i.e., 0.5Mbps, 1Mbps,
and 3Mbps) and the TCP traffic between PC1-Server in case of

a) Shortest path – UDP 0.5Mbps b) QoS-based path – UDP 0.5Mbps c) Shortest path – UDP 1Mbps
d) QoS-based path – UDP 1Mbps e) Shortest path – UDP 3Mbps f) QoS-based path – UDP 3Mbps
Fig.4. Throughput for Shortest path and QoS-based path for UDP 0.5Mbps, 1Mbps, and 3Mbp
. the case of QoS-based path, as the UDP traffic increases it has
a negligible impact on the TCP throughput. For example, when
the UDP stream data rate is 0.5Mbps the TCP throughput goes
as up as 3.11Mbps, whereas when the UDP stream data rate is
3Mbps the TCP traffic throughput goes as low as 2.6Mbps.
C. System Packet Loss
In order to investigate the overall system performance in terms
of packet loss in case of shortest path and QoS-based path,
UDP traffic was generated between PC1-Server at the
maximum link capacity. The UDP traffic between PC0-Server
was set at 1Mbps, 2Mbps and 3Mbps. In this way, the two
paths containing the OVS4-OVS2 link and the OVS4-OVS3-
Fig. 5. Achieved Throughput PC1-Server under the four UDP data rates OVS2 links are over utilized. Thus, in the case of shortest path
all the traffic is going through the OVS4-OVS2 link, whereas
shortest path and QoS-based path. The achieved throughput for
in the case of QoS-based path, the PC0-Server UDP traffic is
all the UDP data rates is illustrated in Fig. 5. It can be noticed
passing through the OVS4-OVS2 link and the PC1-Server
that in case of the shortest path, where the traffic flows are
UDP traffic is going through the OVS4-OVS3-OVS2 links.
sharing common links, for the first scenario with UDP data rate
The results are illustrated in Fig. 6. As the test-bed is also
of 0.5Mbps, the TCP traffic reaches as high as 2.79Mbps.
limited by the capacity and processing of the USB to Ethernet
However, as the UDP data rate increases the throughput for the
adapters, this causes increased packet loss especially when the
TCP traffic decreases significantly, reaching as low as
setup is used at its maximum capacity. Additionally, the packet
0.88Mbps when the UDP data rate of 3Mbps is streamed. In

loss when the shortest path is used is much higher than when approach enables optimal bandwidth utilization by redirecting
the QoS-based path is used. some data traffic through less congested links and avoiding the
network traffic imbalances. However, the small scale test-bed
is limited in performance by the USB to Ethernet adapters
used which reduces in turn the overall system capacity.
Future works will consider creating a more stable test-bed
setup and faster USB to Ethernet adapters will be used to
improve the overall performance of the test-bed. A scalability
scenario will also be considered.
REFERENCES
[1] W. Stallings, Foundations of Modern Networking: SDN, NFV, QoE,
IoT, and Cloud. Addison-Wesley Professional, 2015.
[2] N. McKeown et al., ‘OpenFlow: enabling innovation in campus
Fig. 6. Packet Loss Rate PC1-Server under three UDP data rates networks’, ACM SIGCOMM Computer Communication Review, vol. 38,
no. 2, p. 69, Mar. 2008.
D. Link Failover [3] L. Faughnan, ‘Software Defined Networking’, TechCentral.ie, 01-May-
In this scenario we test the reaction of the system to the link 2013. [Online]. Available: http://www.techcentral.ie/pro/22. [Accessed:
07-Jan-2017].
failover. To emulate the link failure, the cable connecting two
[4] CM. Caba, J. Soler, ‘SDN-based QoS Aware Network Service
switches that connect the hosts was removed, during data
Provisioning’ in S Boumerdassi, S Bouzefrane & É Renault (eds),
transmission as illustrated in Fig. 7. Initially the traffic is Mobile, Secure, and Programmable Networking. Springer, pp. 119-133.
following the shortest path (see Fig. 7a) when the link drops. Lecture Notes in Computer Science, vol. 9395, DOI: 10.1007/978-3-
The ONOS controller detects the link failure and reroutes the 319-25744-0_11
traffic over a different path (see Fig. 7b). The latency [5] G. Araniti, J. Cosmas, A. Iera, A. Molinaro, R. Morabito, and A. Orsino,
introduced by the controller for link down is 3ms and for link ‘OpenFlow over wireless networks: Performance analysis’, in 2014
IEEE International Symposium on Broadband Multimedia Systems and
up is 8ms. This latency is due to the time it takes for the switch
Broadcasting, 2014, pp. 1–5.
to respond to OpenFlow request and replay messages.
[6] A. Al-Jawad, R. Trestian, P. Shah, and O. Gemikonakli, ‘BaProbSDN:
A probabilistic-based QoS routing mechanism for Software Defined
Networks’, in Proceedings of the 2015 1st IEEE Conference on Network
Softwarization (NetSoft), 2015, pp. 1–5.
[7] A. Al-Jawad, P. Shah, O. Gemikonakli, and R. Trestian, ‘Compression-
based technique for SDN using sparse-representation dictionary’, in
NOMS 2016 - 2016 IEEE/IFIP Network Operations and Management
Symposium, 2016, pp. 754–758.
[8] H. Kim, J. Kim, and Y.-B. Ko, ‘Developing a cost-effective OpenFlow
testbed for small-scale Software Defined Networking’, Advanced
Communication Technology (ICACT), 2014 16th International
Conference on, 2014, pp. 758–761.
[9] B. Pfaff, J. Pettit, T. Koponen, E. J. Jackson, A. Zhou, J. Rajahalme, J.
a) Shortest Path Routing
Gross, A. Wang, J. Stringer, P. Shelar, K. Amidon, M. Casado, “The
Design and Implementation of Open vSwitch.” USENIX NSDI 2015.
[10] S. Han and S. Lee, ‘Implementing SDN and network-hypervisor based
programmable network using Pi stack switch’, 2015, pp. 579–581.
[11] H. Kim and N. Feamster, ‘Improving network management with
software defined networking’, IEEE Communications Magazine, vol. 51,
no. 2, pp. 114–119, Feb. 2013.
[12] K. Ohira, ‘Performance Evaluation of an OpenFlow-based Mirroring
Switch on a Laptop/Raspberry Pi’, in Proceedings of The Ninth
International Conference on Future Internet Technologies, New York,
NY, USA, 2014, p. 20:1–20:2.
[13] R. Khondoker, A. Zaalouk, R. Marx, and K. Bayarou, ‘Feature-based
b) Re-routing in case of Link Failover comparison and selection of Software Defined Networking (SDN)
Fig. 7. Link Failover Example controllers’, in 2014 World Congress on Computer Applications and
Information Systems (WCCAIS), 2014, pp. 1–7.
VI. CONCLUSIONS
[14] A. L. Stancu, S. Halunga, A. Vulpe, G. Suciu, O. Fratu, and E. C.
Popovici, ‘A comparison between several Software Defined Networking
This paper investigates the use of QoS-based routing over
controllers’, in 2015 12th International Conference on
a controlled SDN environment. A real experimental test-bed
Telecommunication in Modern Satellite, Cable and Broadcasting
was setup using Raspberry Pi computers running virtual SDN Services (SIKS), 2015, pp. 223–226.
switches and enabling a multi-path SDN environment [15] R. Trestian, G.-M. Muntean, and K. Katrinis, ‘MiceTrap: Scalable traffic
managed by the ONOS controller. The results show that engineering of datacenter mice flows using OpenFlow’, in 2013
IFIP/IEEE International Symposium on Integrated Network
compared to the shortest path routing, a QoS-based routing
Management (IM 2013), 2013, pp. 904–907.