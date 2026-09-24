# [07] Impact of Network Slicing on Performance in 5G and Beyond

> Source file: `[07] Impact of Network Slicing on Performance in 5G and Beyond.pdf`

---

ISSN: 2583-9888
DOI: : doi.org/10.51219/JAIMLD/Pratik-jangale/368

Journal of Artificial Intelligence, Machine Learning and Data Science

https://urfpublishers.com/journal/artificial-intelligence

Vol: 1 & Iss: 1

Research Article

Impact of Network Slicing on Performance in 5G and Beyond

Pratik Jangale*

Citation: Jangale P. Impact of Network Slicing on Performance in 5G and Beyond. J Artif Intell Mach Learn & Data Sci 2022, 1(1),
1653-1657. DOI: : doi.org/10.51219/JAIMLD/Pratik-jangale/368

Received: 03 January, 2022; Accepted: 28 January, 2022; Published: 30 January, 2022

*Corresponding author: Pratik Jangale, Austin, TX, USA, E-mail: pratikjangale@gmail.com

Copyright: © 2022 Jangale P., Postman for API Testing: A Comprehensive Guide for QA Testers., This is an open-access article
distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and
reproduction in any medium, provided the original author and source are credited.

 A B S T R A C T

Network slicing is a transformative feature of 5G networks, enabling the partitioning of a physical network into multiple
logical networks tailored to specific services. This paper explores the impact of network slicing on network performance, focusing
on Quality of Service (QoS), latency, resource optimization and scalability. Additionally, the paper examines challenges, such as
security, dynamic resource allocation and future advancements in 6G. The results demonstrate that network slicing significantly
enhances network efficiency and flexibility, making it a cornerstone of 5G networks and of critical importance for ultra-reliable,
low-latency communications in future networks.

Keywords: Network slicing, 5G, eMBB, URLLC, mMTC, Performance optimization

1. Introduction

With the advent of 5G networks, the need to support a wide
range of applications, from enhanced mobile broadband (eMBB)
to  ultra-reliable  low-latency  communications  (URLLC)  and
massive  machine-type  communications  (mMTC),  has  become
crucial.  Traditional  network  architectures,  however,  struggle
to  provide  the  tailored  performance  required  by  these  diverse
use  cases.  Network  slicing  addresses  this  gap  by  enabling  the
creation  of  dedicated  virtual  networks  optimized  for  specific
services.

This  paper  discusses  the  concept  of  Software-Defined
Networking (SDN) and Network Function Virtualization (NFV),
Network slicing, analyzes its impact on performance metrics and
explores how it supports emerging applications. Furthermore, it
provides insights into how network slicing will evolve in 6G and
the challenges that must be addressed for seamless deployment1,3.

2. Overview of Network Slicing in 5G

Network slicing allows mobile operators to create multiple
virtual networks on a shared physical infrastructure. Each slice
functions  as  an  independent  network,  optimized  for  a  specific
service category. This technique enables more efficient resource
utilization  and  supports  the  diverse  performance  requirements

1

of modern applications. Key technologies like Software-Defined
Networking (SDN) and Network Function Virtualization (NFV)
play essential roles.

SDN provides centralized control by decoupling the control
and  data  planes,  allowing  network  operators  to  dynamically
configure traffic routes across slices.

NFV replaces traditional hardware-based network appliances
(e.g., routers and firewalls) with virtualized software functions
that run on commodity hardware. This makes it easier to create,
manage and reconfigure network slices4.

Figure 1:5G Usage Features ( eMBB, URLCC, mMTC)6

•

to

power

optimize

•  Energy  Efficiency: Designed
consumption for IoT devices.
Scalability: Easily  scales  to  accommodate  the  growing
number of connected devices.
Smart  homes  and  smart  meters:  Sensors  transmitting
periodic data for energy management.
Smart  agriculture:  Environmental  sensors  measuring  soil
conditions, water levels and weather data.

•

•

•  Logistics  tracking:  Real-time  monitoring  of  goods  and

assets across supply chains.

mMTC  applications  prioritize  scalability  over  speed,
enabling  support  for  millions  of  low-power,  low-data-rate
devices  within  a  small  area.  Resource  efficiency  is  critical  to
extend device battery life while ensuring stable connections for
an ever-growing number of IoT devices6.

Each  slice  is  isolated  from  the  others  to  ensure  reliability,
security and performance. Below are the key types of slices and
how they contribute to specific 5G services:

A. eMBB (Enhanced Mobile Broadband)

This  slice  is  designed  for  applications  that  require  high-speed
data and large bandwidth. eMBB supports:

•  High Data Rates: eMBB supports data rates up to 10 Gbps,

•

•

•

enabling faster downloads and streaming.
Increased  Capacity: Enhanced  capacity  allows  more
users  to  connect  simultaneously  without  compromising
performance.
Improved Coverage: eMBB extends coverage to previously
underserved areas, ensuring reliable connectivity.
4K/8K video streaming, virtual reality (VR) and augmented
reality (AR) experiences, cloud gaming, immersive media
and smart cities.

Since  eMBB  applications  demand  fast  and  uninterrupted
data transfer, this slice focuses on maximizing throughput and
ensuring consistent coverage even in high-traffic scenarios, such
as  concerts  or  sports  events.  The  goal  is  to  enhance  the  user
experience by delivering high-quality experience6.

B. URLLC (Ultra-Reliable Low-Latency Communications)

This slice prioritizes extremely low latency and high reliability
for mission-critical applications. Key use cases include:

•  Low Latency: URLLC aims to achieve latencies as low as

Figure 3: mMMTC Use cases8

1 millisecond, crucial for real-time applications.

•  High  Reliability: Ensures  consistent  and  dependable

connections, even in challenging environments.

•  Critical

Applications: Supports

mission-critical

applications.

•  Autonomous  vehicles:  Vehicles  require  split-second
communication for navigation and collision avoidance.
•  Remote surgery: Healthcare applications depend on ultra-
reliable, low-latency networks to support robotic surgeries.
Industrial automation: Factory robots and control systems
must communicate in real-time to ensure smooth operations.

•

URLLC slices provide end-to-end latency as low as 1 ms and
99.999% reliability to meet the stringent requirements of these
services. Dedicated resources ensure that delays are minimized
even during peak network loads7,8.

Figure 2: URLLC Use Cases8

C. mMTC (Massive Machine-Type Communications)

This  slice  is  optimized  for  Internet  of  Things  (IoT)  devices,
which require connectivity for large-scale deployments, such as:

•  High Device Density: mMTC can support up to 1 million

devices per square kilometer.

2

3. Enhancing Network Slicing using SDN and NFV

Software-Defined  Networking

and  Network
Functions Virtualization (NFV) play crucial roles in enhancing
the  performance  of  5G  networks,  especially  in  the  context  of
network slicing:

(SDN)

A. Software-Defined Networking

•  Centralized Control: SDN provides a centralized control
plane  that  decouples  the  network’s  control  logic  from  the
data  plane,  enabling  dynamic  and  real-time  management
of network resources. This is essential for provisioning and
managing network slices based on varying demands.

•  Dynamic  Resource  Allocation:  SDN  enables  dynamic
allocation  and  management  of  network  resources  across
different slices, optimizing bandwidth usage and reducing
latency by adjusting to real-time traffic conditions.
Simplified Management: With SDN, operators can manage
network  configurations  and  policies  centrally,  making
it  easier  to  deploy  and  modify  network  slices  quickly,
ensuring  efficient  use  of  resources  and  improved  network
performance1.

•

B. Network Function Virtualization

•  Virtualized  Network  Functions  (VNFs):  NFV  allows
network  functions  (e.g.  load  balancers)  to  be  virtualized
and  run  on  generic  hardware  instead  of  specific  OEMs.
This  flexibility  enables  the  rapid  deployment  of  VNFs
in  different  slices  based  on  specific  application  needs,
enhancing performance and reducing costs.
Scalability: NFV facilitates scaling up or down of network
functions  dynamically,  responding  to  traffic  fluctuations
within  specific  slices.  This  adaptability  ensures  that

•

J Artif Intell Mach Learn & Data Sci | Vol: 1 & Iss: 1Jangale P.,performance metrics like latency and throughput meet the
required  service-level  agreements  (SLAs)  for  different
applications.

•  Cost  Efficiency:  By  leveraging  generic  hardware,  NFV
reduces  capital  expenditures  (CapEx)  and  operational
expenditures (OpEx). This allows operators to invest more
in  performance  enhancements  rather  than  on  expensive
proprietary hardware3.

4.  Impact  of  Network  Slicing  on  Key  Performance
Metrics

Network  slicing  not  only  helps  address  the  specific  needs
of  each  service  type  but  also  ensures  isolation  between  slices
to  maintain  their  quality.  For  example,  if  an  eMBB  slice
experiences heavy data usage, it will not affect the performance
of a URLLC slice supporting critical applications. This ability to
create tailored and independent network environments improves
key performance indicators like:

Figure 4: Frequency bands and Latency Correlation7.

Packet  Loss  Rate  (Ploss  ):  The  fraction  of  packets  lost  in
transmission.

•  Latency: Faster response times due to traffic prioritization.
•  Throughput:  Improved  bandwidth  management  for  data-

Jitter (J): The variation in packet arrival time, critical for real-
time applications (e.g., VoIP).

intensive services.

•  Packet Loss: Reduced data loss by isolating traffic flows.
•  Resource  Utilization:  Dynamic  resource  allocation  to

optimize network efficiency.

This  flexibility  makes  network  slicing  a  crucial  part  of  5G
networks and with enablement of SDN and NFV can make next-
generation services, including 6G faster to deploy and scale.

A. Latency Reduction

Latency refers to the time taken for a data packet to travel from
the source to the destination. Network slicing optimizes latency-
sensitive traffic through dedicated resources, minimizing delays
caused by congestion, queuing and processing overhead2,8.

End-to-End (E2E) Latency calculation can be denoted by below
formula:

L total = L propagation + L transmission + L processing + L queueing

Where:

L propagation   = Time for the signal to travel over a link (depends on
distance and medium).
L transmission = Time to push all packet bits onto the medium.
L  processing     =  Time  spent  in  processing  headers,  routing  and
encryption.
L queueing = Time spent waiting for packets in buffers.

In URLLC slices, Lqueueing  is minimized by assigning dedicated
spectrum  and  prioritizing  m ission-critical  traffic. Additionally,
MEC  (Multi-Access  Edge  Comp uting)  reduces  Lpropagation  by
processing data closer to the user, ensuring E2E latency <1 ms.

In  autonomous  vehicles,  rea l-time  decisions  like  braking
require  latency  <1  ms.  Netw ork  slicing  assigns  a  dedicated
URLLC slice to avoid delays from public traffic, ensuring the
car reacts instantly to obstacles.

B. Quality of Service (QoS) Enhancement

QoS is crucial for guaranteeing specific performance metrics
like bandwidth, latency, jitter and packet loss. Network slicing
enforces distinct QoS profiles for each slice to meet the varying
requirements of eMBB, URLLC and mMTC applications4.

3

Bandwidth  (B):  Amount  of  data  that  can  be  transmitted  per
second (bps).

Using QoS classes, an eMBB slice ensures high bandwidth,
while  URLLC  minimizes  packet  loss  and  jitter.  SDN  allows
dynamic path selection, ensuring QoS adherence under varying
network loads.

For  cloud  gaming  (eMBB  slice),  low  jitter  and  high
bandwidth  are  crucial.  If  this  slice  gets  congested,  SDN
dynamically shifts traffic to a lower-latency path to avoid game
lag, keeping the user experience seamless.

C. Resource Optimization

Network  slicing  enables  optimal  use  of  resources  by
dynamically assigning them based on real-time demands. SDN
allows centralized control and NFV virtualizes network functions,
providing flexibility in resource distribution3,1.

The  bandwidth  requirement  for  a  specific  slice  (Bs )  can  be

expressed as:

Where:

R = Total available network bandwidth.

Nactive   = Active devices in the slice.
Ntotal   = Total devices in the network.
The goal is to maximize throughput (T) for the slice:

where  SNR  is  the  signal-to-noise  ratio.  Higher  SNR  ensures
better data rates.

Using  adaptive  resource  management  algorithms,
the
network  reallocates  resources  to  underutilized  slices  and
prevents resource contention.

Jangale P.,J Artif Intell Mach Learn & Data Sci | Vol: 1 & Iss: 1For  ex:  In  a  sports  stadium,  an  eMBB  slice  delivers  high-
speed streaming to spectators, while the mMTC slice supports
thousands of IoT sensors. Dynamic resource allocation prevents
video streaming from affecting the sensors’ telemetry, ensuring
reliable performance for both.

D. Scalability

Scalability  is  the  network’s  ability  to  handle  increasing
demand  without  degrading  performance.  Network  slicing
ensures  scalability  by  isolating  resources  for  each  slice.  If
demand for a slice increases (e.g., due to more IoT devices in
mMTC), horizontal and vertical scaling can be performed4.

•  Horizontal and Vertical Scaling in Network Slicing
•  Horizontal  Scaling:  Adding  more  virtual  instances  (e.g.,
more VNFs or virtual machines) to handle additional traffic.
•  Vertical Scaling: Adding more CPU, memory or bandwidth

to existing network instances.

The capacity C of a network slice is calculated as:

Where:

U = Average utilization per device (in bps).
N = Number of connected devices.

In  mMTC,  the  slice  must  support  millions  of  devices
with  minimal  data  rates.  Network  slicing  avoids  congestion
by  distributing  devices  across  isolated  slices,  ensuring  that
performance does not degrade even under heavy IoT loads.

During a large music festival, the network experiences a surge
in  traffic  from  wearable  devices  and  mobile  applications  used
for  attendee  tracking  and  event  scheduling.  To  accommodate
this increase, the network efficiently expands the mMTC slice
by deploying additional virtual instances, ensuring uninterrupted
service for attendees while preserving the quality of the URLLC
slice  utilized  for  critical  safety  communications  and  artist’s
performance live-streaming.

5. Challenges in Network Slicing

Despite

its  numerous  positive

impacts  on  network
performance, Network Slicing presents several challenges to its
implementation

A. Security Risks

The virtualization of network functions increases the attack
surface,  necessitating  robust  protections  for  isolated  slices  to
prevent unauthorized access, data leakage and denial-of-service
attacks.  Implementing  slice-aware  firewalls  and  encryption
is  essential  for  mitigating  these  risks.  Public  access  Wi-Fi
exemplifies these security challenges, as it often lacks adequate
protections,  making  it  vulnerable  to  various  threats  that  could
potentially compromise network slices2.

B. Dynamic Resource Management

While  network  slicing  enhances  resource  utilization,  it
simultaneously  introduces  complexities  in  real-time  resource
allocation.  Software-Defined  Networking  (SDN)  controllers
and orchestration platforms must possess advanced algorithms
capable  of  dynamic  resource  allocation  across  multiple  slices,
ensuring Quality of Service (QoS) parameters are met for diverse

4

applications. This requires the implementation of sophisticated
monitoring  tools  and  predictive  analytics  to  assess  resource
demands and traffic patterns continuously.

Furthermore,  the  orchestration  of  resources  must  account
for  both  physical  and  virtual  network  functions,  leveraging
techniques such as load balancing and service function chaining1.

C. Inter-Slice Interference

Despite

isolation,

interference  between  slices  sharing
physical resources can affect performance. Advanced scheduling
algorithms are needed to minimize conflicts and ensure smooth
operation across all slices.

E. Trade-offs Between Flexibility and Efficiency

Balancing  flexibility  and  efficiency  in  network  slicing
presents  challenges:  dynamic,  flexible  slices  can  lead  to
increased resource overhead and operational costs.

Managing  these  slices  complicates  orchestration,  requiring
strategic  service  classification  to  optimize  resource  allocation.
Additionally,  maintaining  compliance  with  SLAs  while
addressing  competing  demands  adds  complexity  to  load
management.

6. Future of Network Slicing in 6G Networks

As 6G networks evolve, network slicing will become more
dynamic  and  intelligent. AI-powered  orchestration  will  enable
predictive slicing, where network resources are allocated based
on  anticipated  traffic  patterns.  Moreover,  terrestrial-satellite
hybrid slicing will provide seamless connectivity across different
environments, including remote and underserved areas.

Network slicing will also play a vital role in supporting new

use cases, requiring ultra-low latency and high data rates3.

7. Conclusion

Network  slicing  is  a  fundamental  enabler  of  5G  networks,
significantly enhancing performance through improved latency,
QoS, resource optimization and scalability. However, challenges
such  as  security  risks,  resource  management  complexities  and
others  must  be  addressed  to  realize  its  full  potential.  As  we
transition  towards  6G,  network  slicing  will  evolve  to  support
more  advanced  applications  and  dynamic  environments,
ensuring  the  adaptability  and  efficiency  required  for  next-
generation networks.

8. References

1.  Ordonez-Lucena  J, Ameigeiras  P,  Lopez  D,  Ramos-Munoz  JJ,
Lorca J and Folgueira J. “Network Slicing for 5G with SDN/NFV:
Concepts, Architectures and Challenges,” IEEE Communications
Magazine, 2017;55:80-87.

2.  Ksentini  A  and  Nikaein  N.  “Toward  Enforcing  Network  Slicing
IEEE

on  RAN:  Flexibility  and  Resources  Abstraction,”
Communications Magazine, 2017;55:102-108.

3.  Bega D, Gramaglia M, Banchs A, Costa-Pérez X, Bertin P and
Nikaein N. “Toward the Network of the Future: From Enabling
Technologies  to  5G  and  Beyond,”  IEEE  Network,  2019;33:50-
57.

4.  Rost P, Mannweiler C, Michalopoulos DS, Sartori C, Bega D and
Zhang DT. “Network Slicing to Enable Scalability and Flexibility
in  5G  Mobile  Networks,”  IEEE  Communications  Magazine,
2017;55:72-79.

J Artif Intell Mach Learn & Data Sci | Vol: 1 & Iss: 1Jangale P.,5.  https://futurenetworks.ieee.org/tech-focus/march-2017/towards-

5g-network-slicing

6.  https://www.researchgate.net/figure/G-Usage-Scenarios-eMBB-

MMTC-uRLLC_fig5_338149616

7.  https://broadbandlibrary.com/5g-low-latency-requirements/ .

8.  https://www.researchgate.net/figure/Ultra-Reliable-Low-
Latency-URLLC-provides-ultra-reliable-and-low-latency-
communication_fig3_335937022

5

Jangale P.,J Artif Intell Mach Learn & Data Sci | Vol: 1 & Iss: 1