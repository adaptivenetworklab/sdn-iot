# VPLS on Software Defined Network Using ONOS Controller Based on Raspberry-Pi 3 (2)

> Source file: `VPLS on Software Defined Network Using ONOS Controller Based on Raspberry-Pi 3 (2).pdf`

---

The 2021 IEEE Asia Pacific Conference on Wireless and Mobile (APWiMob)
VPLS on Software Defined Network Using ONOS
Controller Based on Raspberry-Pi 3
1st Rizal Cerdas Kurniawan 2nd Rohmat Tulloh 3rd Indrarini Dyah Irawati
School of Applied Science School of Applied Science School of Applied Science
Telkom University Telkom University Telkom University
Bandung, Indonesia Bandung, Indonesia Bandung, Indonesia
rizalcerdaskurniawan@gmail.com rohmatth@telkomuniversity.ac.id indrarini@telkomuniversity.ac.id
Abstract—In this paper, Software Defined Network (SDN) Another concept is also used to gain effectiveness on the
technology is applied using the Open Network Operating existing network, the VPLS. The advantage concept of VPLS
System (ONOS), which can separate the control plane and the is providing Ethernet-based multipoint to multipoint
data plane on a network device. ONOS is installed on communication via an IP network. It can overcome the spread
Raspberry-Pi 3 to minimize the use of Personal Computer (PC) geographic constraints of sharing Ethernet broadcast domains
devices on SDN networks. ONOS is also implemented to support by connecting virtually.
Virtual Private LAN Service (VPLS) features that create the
Layer-2 network by using the OpenFlow protocol. Software is Several previous studies referenced, among others in [6],
connected to the host network by connecting to network the authors analyzed several SDN controllers such as NOX,
overlays that are connected to the OpenFlow data plane POX, RYU, Beacon, OpenDaylight, Onix, and ONOS. POX
protocol. VPLS can maximize the existing bandwidth when and Maestro controllers still work very well, even though the
communication occurs between remote network devices on a network has many switch devices. Simultaneously, the ONOS
local network. We tested voice over Internet Protocol (VoIP) controller has better performance when it also works as an
with a variety of background traffic. The test results show that SDN control plane for local area networks (LAN) and data
the network performance meets the good level according to the center networks. In research [7], the SDN firewall has been
THIPON standard.
implemented and performed using a POX controller, but this
study was only carried out with measurements of Wireshark,
Keywords— Software Defined Network, ONOS, Raspberry-Pi
ICMP, and iperf with mininet simulation. In research [8],
3, VPLS
control of open and disaggregated transport networks with
I. INTRODUCTION ONOS has been conducted, implementation and simulation
carried out with the NETCONF protocol to consider
The VoIP market's growth has increased significantly
establishing connectivity services and connectivity recovery
since 2016, so it is necessary to increase effective and cost-
in the event of a failure during data transmission. In other
efficient VoIP services [1]. The existing network-based
research [9], the authors propose the concepts of SDN
infrastructure must meet the increase in service needs. A
combined with Network Function Virtualization (NFV) to
network infrastructure that vendors almost entirely manage
improve VPLS network performance. System performance is
causes increasingly complex networks to be built, so we need measured by running the TCP service. Regardless of the
a system to manage and implement networks to support
expected benefits, some limitations arise include
diverse needs. Software-Defined Network (SDN) is a new
interoperability, security, performance, and scalability.
concept in controlling, implementing, and managing a
network that supports the needs and innovations in the This study carried out the SDN network's design and
telecommunications sector that are increasingly growing and implementation using an ONOS controller installed on
complex [2]. Sdn concept is to separate control plane and data Raspberry-Pi 3 with the Virtual Private LAN Service (VPLS)
plane. SDN can make networks both small scale and large application. We build our network consists of 3 OpenFlow
scale capable of being controlled using one centralized switches, 4 Laptops, and 1 Raspberry-Pi 3 as a controller. To
controller [3]. Some of the controllers in SDN include POX, find out the performance of the proposed system, we provide
RYU, OpenDaylight, and ONOS. Network Operating VoIP services on the network. System performance is
Systems must meet requirements that demand Scalability, measured based on parameters throughput, delay, jitter, packet
Performance, and Availability to support large-scale loss. The performance must meet the requirements based on
networks. To overcome these challenges, ONF introduced the the Telecommunications and Internet Protocol Harmonization
Open Network Operating System (ONOS) [4]. Over Network (TIPHON) standard [10].
ONOS is a Java-based controller that utilizes the
framework's Open Service Gateway (OSGi) initiative to more
easily install and update applications [5].
978-1-7281-9475-2/21/$31.00 ©2021 IEEE 19
5325349.1202.11115BOMIWPA/9011.01
:IOD
|
EEEI
1202©
00.13$/12/2-5749-1827-1-879
|
)boMiWPA(
eliboM
dna
sseleriW
no
ecnerefnoC
cificaP
aisA
EEEI
1202
Authorized licensed use limited to: Institut Teknologi Bandung. Downloaded on July 22,2024 at 14:17:26 UTC from IEEE Xplore. Restrictions apply.

The 2021 IEEE Asia Pacific Conference on Wireless and Mobile (APWiMob)
II. OVERVIEW Ethernet services and Quality of Service (QoS) guarantees
[17].
A. Software-Defined Network
Software-Defined Network (SDN) is a new concept in
controlling, implementing, and managing a network that
supports the needs and innovations in telecommunications
that are increasingly growing and complex. SDN concept is to
separate the control plane and data plane [11]. SDN can make
networks both small scale and large scale capable of being
controlled using one centralized controller [12-14]. Some
controllers in SDN include POX, RYU, OpenDaylight, and
ONOS.
Fig. 2. VPLS Concept
Fig. 2 shows some of the advantages of being a VPLS are
better than the previous tunneling technology, namely that
VPLS has pseudowires as virtual circuits. VPLS also has
auto-discovery and auto-configuration, allowing several
devices on the VPLS network to recognize each other and
build pseudowires for newly recognized devices. VPLS
consists of Virtual Switched Instance (VSI) or Virtual
Fig. 1. SDN architecture Forwarding Instance, which can define members of the VPLS
domain and resemble virtual switches on a PE router. VPLS
Fig. 1 shows SDN Architecture consists of 3 layers.
allows ethernet interfaces that have the same virtual LAN to
• Data Plane: consists of network elements that can be connected with many PE devices. For example, user A in
manage Datapath SDN following instructions given the VPLS domain consists of an ethernet interface connected
via the Control-Data-Plane Interface (CDPI). to user A on the CE router in a different place. VSI can
remotely MAC addresses and ensures the VPLS domain is
• Control Plane: Part of a network service as an SDN
free from looping. VSI has the functions of MAC address
controller that functions to translate the application
management, flooding, and data forwarding [18].
layer requirements to the infrastructure layer. This
process is carried out by providing appropriate SDN D. Raspberry-Pi 3
Datapath and providing relevant information
This study using a mini-computer as a controller. A third-
required by the Application layer.
generation Raspberry-Pi type mini-computer that uses an
• Application: located at the top layer, communicating ARM System-on-chip (SoC). Raspberry 3 was chosen
with the system via the Northbound Interface (NBI). because it is equipped with 4 USB 2 ports and a 100 Base
Ethernet port to connect with an open flow switch. The
B. Open Network Operating System
network configuration in this study requires a minimum of 3
ONOS is one of the controllers besides NOX, POX, Ryu, ethernet ports for three switches. Consequently, two USB
Floodlight, Opendaylight (ODL), Beacon, and many others, ports are converted to ethernet ports using a USB to ethernet
which continue to grow. Each controller from these various converter. This mini-computer also provides 1GB of RAM
vendors has a different approach to implementing the and a 1.2GHx 64-bit ARMv8 quad-core CPU. This processor
controller's communication process. ONOS is an open-source and RAM are handy when performing control plane and
controller and functions as the central control plane on SDN. network management functions. Several other functions are
ONOS is an open-source project distributed Java-based available such as Bluetooth 4.1 support, 80.11n wireless
programming language [15]. With ONOS, we can manage LAN, and support Bluetooth Low Energy (BLE)
network elements, such as switches and routing, and run and
develop software programs in modularity, providing reliable III. SYSTEM IMPLEMENTATION
communication services, high scalability, and expected to
A. Network Topology
have better performance.
Three applications are active on the ONOS controller, that
C. Virtual Private LAN Service is, OpenFlow, Forwarding, and VPLS. Configuring VPLS on
VPLS is a multipoint VPN layer 2 that allows many the ONOS terminal creates two VPLS IDs, namely VPLS1
regions to be connected in the same single bridge domain and VPLS2. Hosts with different VPLS IDs cannot
over the Internet Protocol (IP) network. All client regions in communicate with each other. On the other hand, hosts that
the VPLS instance can be as if they are on the same LAN have the same VPLS ID can communicate with each other.
network even though it is geographically separated [16]. This type of service uses VoIP using Asterisk, Zoiper, and
VPLS uses an Ethernet interface to the client. VPLS services iperf software as background traffic generators. PC 1 as a
are provided for operators, service providers, and large VoIP server and three other PCs as a client. QoS
companies that require the availability of high-performance measurement parameters consist of throughput, delay, packet
loss, and jitter using Wireshark software.
978-1-7281-9475-2/21/$31.00 ©2021 IEEE 20
Authorized licensed use limited to: Institut Teknologi Bandung. Downloaded on July 22,2024 at 14:17:26 UTC from IEEE Xplore. Restrictions apply.

The 2021 IEEE Asia Pacific Conference on Wireless and Mobile (APWiMob)
Fig. 5. New OpenFlow Interface
Fig. 5 shows the configuration by adding the controller IP
Address so that the controller can recognize the switch.
Fig. 3. Network topology design
Fig. 3 shows some devices used on this network, namely
1 Raspberry-Pi 3 as an ONOS controller, 2 USB-To-Ethernet
converters, 3 OpenFlow switches, 10 UTP cables, and 4 PCs.
B. Bridge Configuration
Raspberry-Pi 3, which is used as a controller device, only Fig. 6. Port Forwarding Configuration
has one ethernet interface [19], for that it is done by adding
devices, namely 2 USB-to-Ethernet converters on Raspberry- Fig. 6 shows the OpenFlow data plane configuration port
Pi 3 so that it can connect directly to the Raspberry-Pi 3 with the specifications:
controller device with a switch OpenFlow on SDN networks.
• Ether2: connected to switch2
auto br0
• Ether3: connected to switch3
iface br0 inet static
address 100.100.100.254 • Ether4: connected with PC1
netmask 255.255.255.0
network 100.100.100.0 • Ether5: connected with PC2
bridge_ports eth0 eth1 eth2
D. VPLS Configuration
Fig. 4. Bridge Configuration In this paper, a VPLS configuration is performed by
creating 2 VPLS IDs with the ID names, namely VPLS1 and
In the implementation process so that every OpenFlow VPLS2. Each VPLS ID consists of 2 PCs. VPLS1 consisting
switch connected to the controller can communicate on the of PC1 and PC3, and VPLS2 is consisting of PC2 and PC4.
same network, a bridge configuration is required on the
controller interface [20]. Fig. 4 shows the addition of a new
bridge interface, br0, with a static IP Address configuration
with three port interfaces being bridged, namely eth0, eth1,
eth2.
C. OpenFlow Switch Configuration Fig. 7. VPLS ID Addition
On an SDN network, not all network devices can be Fig. 7 shows VPLS ID is added with the names VPLS1 and
directly recognized by the controller, only devices that support VPLS2.
the OpenFlow protocol can be recognized [21]. Therefore in
this paper, using the OpenFlow switch with a Mikrotik device.
At this stage, the OpenFlow switch configuration is
performed, several configurations are performed, namely IP
Address, bridge, OpenFlow as the control plane, and the data
plane.
Fig. 8. Provide ID On The Host Interface
Fig. 8 shows ID is added to each host's interface so that VPLS
can recognize it.
978-1-7281-9475-2/21/$31.00 ©2021 IEEE 21
Authorized licensed use limited to: Institut Teknologi Bandung. Downloaded on July 22,2024 at 14:17:26 UTC from IEEE Xplore. Restrictions apply.

The 2021 IEEE Asia Pacific Conference on Wireless and Mobile (APWiMob)
  controller  can  control  the  SDN  network  through  these
switches. The next step is to connect each switch to the PC
according to the topology, then configure the IP address on
each PC as if it were in a local network with the same network
prefix.
IV.  RESULT AND ANALYSIS
A. Controller Test

| Fig. 9. VPLS Group   |     |     |     |     | Controller  |     | Host 2  |     |
| -------------------- | --- | --- | --- | --- | ----------- | --- | ------- | --- |
Fig. 9 shows the grouping of Hosts on VPLS ID. PC 1 and PC
Host 3
3 into VPLS1 while PC 2 and PC 4 into VPLS2.
E. System Specification
Switch 2
•
Controller Specification
Switch 3
For the controller using Raspberry-pi 3 with specifications
Switch 1
as shown in table 1
TABLE 1. Raspberry-Pi 3 Specification
Host 4
Host 1
|     | Type  | Specification  |     |     |     |     |     |     |
| --- | ----- | -------------- | --- | --- | --- | --- | --- | --- |
Fig. 11. Network topology implementation
| Central Processing Unit  | 4x ARM Cortex-A53, 1.2 GHz  |     |     |       |                 |             |                       |      |
| ------------------------ | --------------------------- | --- | --- | ----- | --------------- | ----------- | --------------------- | ---- |
|                          |                             |     |     | Fig.  | 11  shows  the  | controller  | side's  test,  where  | the  |
| RAM                      | 1 GB                        |     |     |       |                 |             |                       |      |
controller already recognizes all devices on the SDN network.
Network  10/100 Ethernet, 2.4 GHz 802.11n  In this test, the controller can recognize all available devices
according to the implementation topology, where there are
WLAN
three switches and 4 PCs according to topology planning.
| Operating System  | Raspbian 4.19  |     |     |     |     |     |     |     |
| ----------------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
B. Connectivity Test

Fig. 10 shows a schematic circuit of the Raspberry-Pi 3 used.
| In  this  | study,  2  USB-to-Ethernet  | converters  | are  used  to  |     |     |     |     |     |
| --------- | --------------------------- | ----------- | -------------- | --- | --- | --- | --- | --- |
connect the Raspberry-Pi 3 with OpenFlow switches, namely
Switch 2 and Switch 3 and 1 Ethernet port Switch 1. All ports
will be connected to the switch using a UTP cable. To connect
| all  OpenFlow  | switches  with  | this  controller,  | a  bridge  |     |     |     |     |     |
| -------------- | --------------- | ------------------ | ---------- | --- | --- | --- | --- | --- |
configuration is done on the controller side. Raspberry-pi
configuration as a controller

Fig. 12. Connectivity Test Via Controller
Fig. 12 shows network connectivity testing to find out all
switch devices connected to the controller can communicate
|     |     |     |     | adequately.  | Fig.  12.  also  | shows  that  | it  has  successfully  |     |
| --- | --- | --- | --- | ------------ | ---------------- | ------------ | ---------------------- | --- |

performed PING with a packet value of 64 Bytes to 3 switches
Fig. 10. Raspberry-pi 3 configuration as a controller  connected directly to the controller from the controller side.
•
|     | Switch Specification  |     |     | C. Virtual Private LAN Service Test  |     |     |     |     |
| --- | --------------------- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
For the forwarding plane function using a Mikrotik Router
with Openflow installed with the specifications as in table 2.  This VPLS test is done by doing PING between hosts with
the same VPLS ID or hosts with different VPLS IDs. If the
TABLE 2. Mikrotik Specification  VPLS configuration has not been done automatically, all
|     | Type  | Specification  |     |     |     |     |     |     |
| --- | ----- | -------------- | --- | --- | --- | --- | --- | --- |
hosts can communicate.
|     | Operating System    | RouterOS       |     |     |     |     |     |     |
| --- | ------------------- | -------------- | --- | --- | --- | --- | --- | --- |
|     | Number of LAN Port  | 5              |     |     |     |     |     |     |
|     | RAM                 | 128 MB         |     |     |     |     |     |     |
|     | Routernoard         | RB-951Ui-2HnD  |     |     |     |     |     |     |

The next step is to configure OpenFlow on the switch so

that each switch connected to the Raspberry-Pi 3 controller
Fig. 13. Host Connectivity with Different VPLS ID
can detect the ONOS topology, which means that ONOS as a
| 978-1-7281-9475-2/21/$31.00 ©2021 IEEE |     |     |     | 22  |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Institut Teknologi Bandung. Downloaded on July 22,2024 at 14:17:26 UTC from IEEE Xplore.  Restrictions apply.

The 2021 IEEE Asia Pacific Conference on Wireless and Mobile (APWiMob)
Fig. 13 shows that PING between h2 and h1 generates a Fig. 16 shows the delay from measurements without
Request Time Out because h2 and h1 have different VPLS ID. background traffic valued at 2.75 ms and measurements with
the highest background traffic worth 3.58 ms. These results
indicate that the delay shown on this measurement is still
following the TIPHON standardization. The average of these
overall delay measurements is 3.11 ms.
• Jitter
In this part, jitter is measured by reducing the first or
previous packet delay time with the second or subsequent
packet delay time.
Fig. 14. Host Connectivity with The Same VPLS ID
Fig. 14 shows the PING between h2 and h4 resulting in a
TTL Reply, which means that h2 and h4 can communicate
because h2 and h4 are included in the same VPLS ID.
D. Performance Test (Voice Over Internet Protocol)
• Throughput
This part will show the measurement of throughput to
determine the network's actual speed when sending data.
Measurements are made by making calls between h1 and h3
that are already connected and can communicate through Fig. 17. Jitter Performance
VPLS services on SDN.
Fig. 17 shows that the value of jitter in this measurement
is still following TIPHON standardization. In this
measurement, the higher the value of background traffic, the
jitter's value will also increase. The jitter's value without
background traffic shows a value of 0.0352 ms, while jitter's
value on the highest background traffic is worth 0.0414 ms.
The average of these jitter measurements is 0.0381 ms.
• Packet Loss
In this part, the packet loss is measured by counting the
number of packets sent minus the number of packets received
Fig. 15. Throughput Performance then multiplied by 100%.
Fig. 15 shows that the throughput generated on this
measurement is still following the TIPHON standard, where
the value of throughput without background traffic reaches
3.62 Mbps and the highest throughput value on background
traffic reaches 3.473 Mbps. The average overall throughput
is 3,528 Mbps.
• Delay
In this part, we take measurements of the delay by
calculating the average arrival time of the first or previous
packet reduced by the second or after packet's arrival time
during the VoIP communication process using Zoiper.
Fig. 18. Packet Loss Performance
Fig. 18 shows that the value of packet loss from this
measurement is still following TIPHON standardization,
wherein this measurement, the packet loss value in the
measurement without background traffic is 2.1%, and the
packet loss value in the highest background traffic
measurement is 7.2%.
Fig. 16. Delay Performance
978-1-7281-9475-2/21/$31.00 ©2021 IEEE 23
Authorized licensed use limited to: Institut Teknologi Bandung. Downloaded on July 22,2024 at 14:17:26 UTC from IEEE Xplore. Restrictions apply.

The 2021 IEEE Asia Pacific Conference on Wireless and Mobile (APWiMob)
  [6]  A. A. Semenovykh, O. R. Laponina, “Comparative analysis of SDN
  controllers,” International Journal of Open Information Technologies,
vol. 6, no. 7. 2018.
TABLE 3. Performance Conclusion
[7]  W. M. Othman, H. Chen, A. Al-moalmi, A. N. Hadi, “Implementation
| N Quality of  | Without  | Backgrou | Indeks  | Indeks  |     |     |     |     |
| ------------- | -------- | -------- | ------- | ------- | --- | --- | --- | --- |
and performance analysis of SDN firewall on POX controller,” in 2017
o  Service  Backgro nd  without  Backgrou IEEE 9th International Conference on Communication Software and
|     | und      | Traffic  | Backgrou | nd       | Networks (ICCSN), China, 2017.  |     |     |     |
| --- | -------- | -------- | -------- | -------- | ------------------------------- | --- | --- | --- |
|     | Traffic  | Max      | nd       | Traffic  | [8]                             |     |     |     |
A. Giorgetti, A. Sgambelluri, R. Casellas,” Control of open and
Traffic  max  disaggregated transport networks using the Open Network Operating
1  Throughput  3,62  3,47Mbps  Excellent  Excellent  System (ONOS),” IEEE/OSA Journal of Optical Communications and
|           | Mbps     |          |          |          | Networking, vol. 12, no. 2, pp. A171-A181, 2019.  |     |     |     |
| --------- | -------- | -------- | -------- | -------- | ------------------------------------------------- | --- | --- | --- |
| 2  Delay  | 2,75 ms  | 3,58 ms  | Perfect  | Perfect  |                                                   |     |     |     |
[9]  M. Liyanage, M. Ylianttila, A. Gurtov,  "Software Defined VPLS
| 3  Jitter  | 0,0352  | 0,0414  | Good  | Good  |     |     |     |     |
| ---------- | ------- | ------- | ----- | ----- | --- | --- | --- | --- |
Architectures: Opportunities and Challenges," 2017 IEEE 28th Annual
|     | ms  | ms  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
International Symposium on Personal, Indoor, and Mobile Radio
| 4  Packet Loss  | 2,1%  | 7,2%  | Perfect  | Good  |                             |                   |                     |       |
| --------------- | ----- | ----- | -------- | ----- | --------------------------- | ----------------- | ------------------- | ----- |
|                 |       |       |          |       | Communications              | (PIMRC  2017)At:  | Montreal,  Canada,  | DOI:  |
|                 |       |       |          |       | 10.1109/PIMRC.2017.8292519  |                   |                     |       |
Based on Table 3. the results of QoS measurements that  [10] Telecommunications
|     |     |     |     |     |     | and  Internet  | Protocol  Harmonization  | Over  |
| --- | --- | --- | --- | --- | --- | -------------- | ------------------------ | ----- |
have been carried out using VoIP services on this network  Networks (TIPHON), “Tr 101 329,” Etsi, vol. 1, no. General aspects of
Quality of Service (QoS), pp. 1–37, 1999.
| implementation  | have  good  | QoS  performance  |     | following  |     |     |     |     |
| --------------- | ----------- | ----------------- | --- | ---------- | --- | --- | --- | --- |
[11] A.
TIPHON standardization.  Zahmatkesh,  T.  Kunz,  “Software  defined  multihop  wireless
networks: Promises and Challenges,” Journal of Communications and
Networks, vol. 19, no. 6, 2017.
|     | V.  | CONCLUSION  |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
[12] Y. Zhou, B. Ramamurthy, B. Guo, “Supporting dynamic bandwidth
We build VPLS on the SDN network that separates the  adjustment based on virtual transport link in software-defined IP over
optical networks,” IEEE/OSA Journal of Optical Communications and
| control  plane  | from  the  | data  plane.  | We  use  ONOS  | as  a  |     |     |     |     |
| --------------- | ---------- | ------------- | -------------- | ------ | --- | --- | --- | --- |
Networking, vol. 10, no. 3, pp. 125-137, 2018.
controller that is applied to Raspberry-Pi 3. The performance
[13] R. Tulloh, H. Tussyadiah, R. W. Hutabri and R. M. Negara, “Load
results of VPLS implementation on SDN networks using the
distribution analysis on bipartite topology using floodlight controller,”
ONOS controller applied to the Raspberry-Pi 3 show that the
Journal of Theoretical and Applied Information Technology, vol. 96,
four QoS parameters' values still follow a good TIPHON
no. 5, pp. 1238-1252, 2018.
standard. In this research, a comparison of the results of QoS
[14] R. Tulloh, J. G. Amri Ginting, A. Mulyana, and M. Lutfi, “Performance
measurements  with  200Mb,  400Mb,  600Mb,  800Mb  Comparison of File Transfer Protocol Service between Link State and
background  traffic  is  used  to  determine  the  network  Distance Vector Routing Protocol in Software Defined Network,” IOP
Conference Series: Materials Science and Engineering, vol. 982, no.
| performance  | limits  on  | traffic  loads.  | The  result  | is  the  |     |     |     |     |
| ------------ | ----------- | ---------------- | ------------ | -------- | --- | --- | --- | --- |
1, 2020.
measurement with the highest traffic load, and the QoS value
[15]  A. S. Muqaddas, P. Giaccone, A. Bianco, “Inter-Controller Traffic to
still shows a good value according to TIPHON standards.
Support Consistency in ONOS Clusters,” IEEE Transactions on
VPLS implementation can be run on SDN networks using the  Network and Service Management, vol. 14, no. 4, pp. 1018-1031, 2017.
ONOS controller to share private networks between hosts.  [16] C. Fancy, L. M. M. Thanveer, “An evaluation of alternative protocols-
based Virtual Private LAN Service (VPLS),” in 2017 International
REFERENCES  Conference on IoT and Application (ICIOT), India, 2017.
[17] M. Liyanage, M. Ylianttila, A. Gurtov, “Secure Hierarchical VPLS

Architecture for Provider Provisioned Networks,” IEEE Access, vol. 3,
[1]  A. Bhutani, P. Wadhwani, "Voice over Internet Protocol (VoIP)
pp. 967-984, 2015.
Market Size By Type," April 2019. [Online]. [Acessed 26 January
[18] M. Barreiros, P. Lundqvist, “The VPLS Case Study,” QOS-Enabled
| 2021].  | https://www.gminsights.com/industry-analysis/voice-over- |     |     |     |     |     |     |     |
| ------- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
internet-protocol-voip-market.  Networks: Tools and Foundations, Wiley Telecom, 2015, 163-191.
[2]  [19] R.  Heradio,  J.  Chacon,  H.  Vargas,  “Open-Source  Hardware  in
M. Liyanage, A. Gurtov, M. Ylianttila, "Software-Defined Networking
Concepts,"  Software-Defined  Mobile  Network  (SDMN),  Wiley  Education: A Systematic Mapping Study,” IEEE Access, vol. 6, pp.
| Telecom, 2015, 21-44.  |     |     |     |     | 72094-72103, 2018.  |     |     |     |
| ---------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- |
[3]  [20] K. Lee, B. Kwon, J. Kang, “Optimal Flow Rate Control for SDN-Based
V. Monita, I. D. Irawati, R. Tulloh, “Comparison of routing protocol
performance on multimedia services on software defined network,”  Naval Systems,” IEEE Transactions on Aerospace and Electronic
Bulletin of Electrical Engineering and Informatics, vol. 9, no. 4, pp.  Systems, vol. 53, no. 6, pp. 2690-2705, 2017.
1612-1619, 2020.  [21] M. Yang, H. Rastegarfar, I. B. Djordjevic, “Physical-layer adaptive
[4]  T. Alharbi, M. Portmann, “The (In)Security of Virtualization in  resource  allocation  in  software-defined  data  center  networks,”
Software Defined Networks,” IEEE Access, vol. 7, pp. 66584-66594,  IEEE/OSA Journal of Optical Communications and Networking vol.
10, no. 12, pp. 1015-1026, 2018.
2019.
| [5]  A. H. Eljack, A. Hassan, H. H. Elamin. “Performance Analysis of  |     |     |     |     |     |     |     |     |
| --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ONOS and Floodlight SDN Controllers based on TCP and UDP              |     |     |     |     |     |     |     |     |
| Traffic,” in 2019 International Conference on Computer, Control,      |     |     |     |     |     |     |     |     |
Electrical, and Electronics Engineering (ICCCEEE), Sudan, 2019.

| 978-1-7281-9475-2/21/$31.00 ©2021 IEEE |     |     |     |     | 24  |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Institut Teknologi Bandung. Downloaded on July 22,2024 at 14:17:26 UTC from IEEE Xplore.  Restrictions apply.