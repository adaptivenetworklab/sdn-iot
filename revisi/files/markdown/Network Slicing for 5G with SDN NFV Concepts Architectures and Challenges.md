# Network Slicing for 5G with SDN NFV Concepts Architectures and Challenges

> Source file: `Network Slicing for 5G with SDN NFV Concepts Architectures and Challenges.pdf`

---

network slIcIng In 5g systems
Network Slicing for 5G with SDN/NFV:
Concepts, Architectures, and Challenges
Jose Ordonez-Lucena, Pablo Ameigeiras, Diego Lopez, Juan J. Ramos-Munoz, Javier Lorca, and Jesús Folgueira
The authors present the AbstrAct Network softwarization, an emerging trend
network slicing concept, that seeks to transform networks using soft-
with a particular focus The fifth generation of mobile communications ware-based solutions, can be a potential enabler
is anticipated to open up innovation opportunities for accomplishing this. Through technologies like
on its application to 5G
for new industries such as vertical markets. How- software-defined networking (SDN) and network
systems. They start by
ever, these verticals originate myriad use cases functions virtualization (NFV), network softwariza-
summarizing the key with diverging requirements that future 5G net- tion can provide the programmability, flexibility,
aspects that enable the works have to efficiently support. Network slic- and modularity that is required to create multi-
realization of so-called ing may be a natural solution to simultaneously ple logical (virtual) networks, each tailored for a
accommodate, over a common network infra- given use case, on top of a common network.
network slices. Then they
structure, the wide range of services that verti- These logical networks are referred to as network
give a brief overview on
cal-specific use cases will demand. In this article, slices. The concept of separated virtual networks
the SDN architecture we present the network slicing concept, with a deployed over a single network is indeed not new
proposed by the ONF and particular focus on its application to 5G systems. (e.g., virtual private networks, VPNs); however,
show that it provides tools We start by summarizing the key aspects that there are specificities that make network slices
enable the realization of so-called network slic- a novel concept. We define network slices as
to support slicing. They
es. Then we give a brief overview on the SDN end-to-end (E2E) logical networks running on a
argue that although such
architecture proposed by the ONF and show common underlying (physical or virtual) network,
architecture paves the that it provides tools to support slicing. We argue mutually isolated, with independent control and
way for network slicing that although such architecture paves the way management, which can be created on demand.
implementation, it lacks for network slicing implementation, it lacks some Such self-contained networks must be flexible
essential capabilities that can be supplied by enough to simultaneously accommodate diverse
some essential capabili-
NFV. Hence, we analyze a proposal from ETSI to business-driven use cases from multiple players on
ties that can be supplied
incorporate the capabilities of SDN into the NFV a common network infrastructure (Fig. 1).
by NFV. architecture. Additionally, we present an example In this article, we provide a comprehensive
scenario that combines SDN and NFV technolo- study of the architectural frameworks of both SDN
gies to address the realization of network slices. and NFV as key enablers to achieve the realization
Finally, we summarize the open research issues of network slices. Although these two approaches
with the purpose of motivating new advances in are not yet commonplace in current networking
this field. practice, especially in public wide area networks
(WANs), their integration offers promising possibil-
IntroductIon
ities to adequately meet the slicing requirements.
Fifth generation (5G) systems are nowadays being Indeed, many 5G research and demonstration
investigated to satisfy the consumer, service, and projects (e.g., 5GNORMA, 5GEx, 5GinFIRE, and
business demands of 2020 and beyond. One 5G!Pagoda) are addressing the realization of 5G
of the key drivers of 5G systems is the need to slicing through the combination of SDN and NFV.
support a variety of vertical industries such as Thus, we present a deployment example that illus-
manufacturing, automotive, healthcare, energy, trates how NFV functional blocks, SDN controllers,
and media and entertainment [1]. Such verticals and their interactions can fully realize the network
originate very different use cases, which impose slicing concept. Furthermore, we identify the main
a much wider range of requirements than exist- challenges arising from implementing network slic-
ing services do nowadays. Today’s networks, with ing for 5G systems.
their “one-size-fits-all” architectural approach, are The remainder of this article is organized as
unable to address the diverging performance follows. We commence by providing a back-
requirements that verticals impose in terms of ground on key concepts for network slicing. Then
latency, scalability, availability, and reliability. To we describe the SDN architecture from the Open
efficiently accommodate vertical-specific use Networking Foundation (ONF) and the NFV archi-
cases along with increased demands for existing tecture from the European Telecommunications
services over the same network infrastructure, Standards Institute (ETSI), respectively. Follow-
it is accepted that 5G systems will require archi- ing that, we show a network slicing use case with
tectural enhancements with respect to current NFV and SDN integration. Finally, we provide the
deployments. main challenges and future research directions.
Digital Object Identifier: Jose Ordonez-Lucena, Pablo Ameigeiras, and Juan J. Ramos-Munoz are with the University of Granada;
10.1109/MCOM.2017.1600935 Diego Lopez, Javier Lorca, and Jesús Folgueira are with Telefónica I+D – Global CTO
80 0163-6804/17/$25.00 © 2017 IEEE IEEE Communications Magazine • May 2017
Authorized licensed use limited to: UNIVERSITAS TELKOM. Downloaded on August 02,2024 at 08:13:23 UTC from IEEE Xplore. Restrictions apply.

| Mobile broadband slice |     |     |     | W e   d e fi      | n e   n e t w o r k       |
| ---------------------- | --- | --- | --- | ----------------- | ------------------------- |
|                        |     |     |     | s li c e s   a s  | e n d - t o -e n d        |
|                        |     |     |     | ( E 2 E )   l o g | i c a l  n e t w o r k s  |
|                        |     |     |     | r u n n i n g   o | n   a   c o m m o n       |
e
l i c
| e  s |     |     |     | u n d e r l y i n | g   ( p h y s i c a l   o r   |
| ---- | --- | --- | --- | ----------------- | ----------------------------- |
a r
h c
| e a l t |     |     |     | v i r t u a l )   n | e t w o r k ,   m u t u - |
| ------- | --- | --- | --- | ------------------- | ------------------------- |
H e
| ic  |     |     |     | a l l y   i s o l a t | e d ,   w i t h   i n d e - |
| --- | --- | --- | --- | --------------------- | --------------------------- |
s   s l
n g
| h i |     |     |     | p e n d e n t |   c o n t r o l   a n d   |
| --- | --- | --- | --- | ------------- | ------------------------- |
f   T
  o
| rn e t |     |     |     | m a n a g e m | e n t ,   w h i c h   c a n   |
| ------ | --- | --- | --- | ------------- | ----------------------------- |
te
I n e
| u r |     |     |     | b e   c r e a t e d |   o n   d e m a n d .   |
| --- | --- | --- | --- | ------------------- | ----------------------- |
ru c t
s t
| r a |     |     |     | S u c h   s e l f - | c o n t a i n e d   n e t - |
| --- | --- | --- | --- | ------------------- | --------------------------- |
i n f
| a l   |     |     |     | w o r k s   m u | s t   b e   fl e x i b l e   |
| ----- | --- | --- | --- | --------------- | ---------------------------- |
ys i c
h
| P   |     |     |     | e n o u g h   | t o   s i m u l t a n e - |
| --- | --- | --- | --- | ------------- | ------------------------- |
Access node
ously accommodate
| WiMAX 2G/3G/4G/5G | Satellite xDSL/cable | Transport/aggregation node | Edge Core   |                          |     |
| ----------------- | -------------------- | -------------------------- | ----------- | ------------------------ | --- |
| access access     | access access        |                            | cloud cloud |                          |     |
|                   |                      | Core node                  |             | diverse business-driven  |     |
Figure 1. 5G network slices running on a common underlying multi-vendor and multi-access network. Each  use cases from multiple
slice is independently managed and addresses a particular use case. players on a common
network infrastructure.
bAckground on key concepts for  vant to such criteria, in an attempt to simplify the
use and management of that resource in some
network slIcIng
useful way. The resources to be virtualized can
In this section, we provide a background on key  be physical or already virtualized, supporting a
aspects that are necessary to realize the network  recursive pattern with different abstraction layers.
slicing concept.  Just as server virtualization [2] makes virtual
machines (VMs) independent of the underlying
resources
physical hardware, network virtualization [3] enables
In its general sense, a resource is a manageable  the creation of multiple isolated virtual networks that
unit, defined by a set of attributes or capabilities that  are completely decoupled from the underlying phys-
can be used to deliver a service. A network slice is  ical network and can safely run on top of it.
composed of a collection of resources that, appro- The introduction of virtualization to the net-
priately combined, meet the service requirements of  working field enables new business models, with
the use case that such a slice supports. In network  novel actors and distinct business roles. We con-
slicing, we consider two types of resources. sider a framework with three kinds of actors:
Network Functions (NFs): Functional blocks  •  Infrastructure provider (InP): owns and man-
that provide specific network capabilities to sup- ages a given physical network and its constit-
port and realize the particular service(s) each  uent resources. Such resources, in the form of
use  case  demands.  Generally  implemented  WANs and/or data centers (DCs), are virtual-
as software instances running on infrastructure  ized and then offered through programming
resources, NFs can be physical (a combination  interfaces to a single or multiple tenants.
of vendor-specific hardware and software, defin- • Tenant: leases virtual resources from one or
ing a traditional purpose-built physical appliance)  more InPs in the form of a virtual network,
and/or virtualized (network function software is  where the tenant can realize, manage, and
decoupled from the hardware it runs on). provide network services to its users. A net-
Infrastructure Resources: Heterogeneous hard- work service is a composition of NFs, and it
ware and necessary software for hosting and con- is defined in terms of the individual NFs and
necting NFs. They include computing hardware,  the mechanism used to connect them.
storage capacity, networking resources (e.g., links  • End user: consumes (part of) the services
and switching/routing devices enabling network  supplied by the tenant, without providing
| connectivity), and physical assets for radio access.  |     | them to other business actors. |     |     |     |
| ----------------------------------------------------- | --- | ------------------------------ | --- | --- | --- |
Suitable for use in network slicing, the aforemen- As discussed above, virtualization is naturally
tioned resources and their attributes have to be  recursive, and the first two actors can happen in
abstracted and logically partitioned leveraging vir- a vertical multi-layered pattern, where a tenant at
tualization mechanisms, defining virtual resources  one layer acts as the InP at the layer immediately
that can be used in the same way as physical ones. above. The recursion mentioned here implies that
a tenant can provide network services to an end
VIrtuAlIzAtIon
user, but also to another tenant (Fig. 2). In such
Virtualization is a key process for network slicing  a case, this second tenant would provide more
as it enables effective resource sharing among  advanced network services to its own users.
slices. Virtualization is the abstraction of resources
orchestrAtIon
using appropriate techniques. Resource abstrac-
tion is the representation of a resource in terms of  Orchestration is also a key process for network
attributes that match predefined selection criteria  slicing. In its general sense, orchestration can be
while hiding or ignoring aspects which are irrele- defined as the art of both bringing together and
| IEEE Communications Magazine • May 2017 |     |     |     |     | 81  |
| --------------------------------------- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: UNIVERSITAS TELKOM. Downloaded on August 02,2024 at 08:13:23 UTC from IEEE Xplore.  Restrictions apply.

In its general sense,
Gray VN consuming
orchestration can be End (part of) the services
user Green VN consuming (part of) the offered by red VN
defined as the art of services offered by blue VN
Red VN running
both bringing together End customized
user Tenant Tenant network and
and coordinating dispa-
business services
rate things into a coher-
Blue virtual network (VN) running network services
ent whole. In a slicing
Tenant InP
environment, where the
players involved are so
diverse, an orchestrator
InP 1 InP 2 InP 3
is needed to coordinate
seemingly disparate
Physical network 1 Physical network 2 Physical network 3
network processes for
creating, managing and
Physical Virtual Physical Virtual
delivering services. node nodes link links
Figure 2. InPs and tenants as virtualization actors. This scenario shows the recursion principle, where these
actors happen in a vertical multi-layered pattern.
coordinating disparate things into a coherent whole. Performance: Each slice is defined to meet par-
In a slicing environment, where the players involved ticular service requirements, usually expressed in the
are so diverse, an orchestrator is needed to coor- form of key performance indicators (KPIs). Perfor-
dinate seemingly disparate network processes for mance isolation is an E2E issue, and has to ensure
creating, managing, and delivering services. that service-specific performance requirements are
A unified vision and scope of orchestration has always met on each slice, regardless of the conges-
not been agreed upon. According to the ONF [4], tion and performance levels of other slices.
orchestration is defined as the continuing process of Security and privacy: Attacks or faults occur-
selecting resources to fulfill client service demands ring in one slice must not have an impact on
in an optimal manner. The idea of optimal refers other slices. Moreover, each slice must have
to the optimization policy that governs orchestra- independent security functions that prevent unau-
tor behavior, which is expected to meet all the spe- thorized entities to have read or write access to
cific policies and service level agreements (SLAs) slice-specific configuration/management/account-
associated with clients (e.g., tenants or end users) ing information, and be able to record any of
that request services. The term continuing means these attempts, whether authorized or not.
that available resources, service demands, and opti- Management: Each slice must be independent-
mization criteria may change in time. Interestingly, ly managed as a separate network.
orchestration is also referred to in [4] as the defining To achieve isolation, a set of appropriate, con-
characteristic of an SDN controller. Note that client sistent policies and mechanisms have to be defined
is a term used in the SDN context. at each virtualization level, following the recursion
The ONF states that the orchestrator functions principle introduced earlier. The policies (what is to
include client-specific service demand validation, be done) contain lists of rules that describe how dif-
resource configuration, and event notification. For ferent manageable entities must be properly isolat-
a more detailed description of these functions, ed, without delving into how this can be achieved.
see [4, Sec. 6.2]. The mechanisms (how it is to be done) are the pro-
However, in network slicing, orchestration can- cesses that are implemented to enforce the defined
not be performed by a single centralized entity, policies. From our point of view, to fully realize the
not only because of the complexity and broad required isolation level, the interplay of both virtual-
scope of orchestration tasks, but also because it ization and orchestration is needed.
is necessary to preserve management indepen-
onf network slIcIng ArchItecture
dence and support the possibility of recursion. In
our view, a framework in which each virtualization The SDN architecture provided by the ONF com-
actor (Fig. 2) has an entity performing orchestra- prises an intermediate control plane that dynam-
tion functions seems more suitable to satisfy the ically configures and abstracts the underlying
above requirements. The entities should exchange forwarding plane resources so as to deliver tai-
information and delegate functionalities between lored services to clients located in the application
them to ensure that the services delivered at a plane (see the SDN basic model in [4]). This is
certain abstraction layer satisfy the required per- well aligned with the requirements of 5G network
formance levels with optimal resource utilization. slicing, which needs to satisfy a wide range of ser-
vice demands in an agile and cost-effective man-
IsolAtIon
ner. Thus, the SDN architecture is an appropriate
Strong isolation is a major requirement that must tool for supporting the key principles of slicing.
be satisfied to operate parallel slices on a com- The purpose of this section is to describe the SDN
mon shared underlying substrate. The isolation architecture and how it can be applied to enable
must be understood in terms of: slicing in 5G systems.
82 IEEE Communications Magazine • May 2017
Authorized licensed use limited to: UNIVERSITAS TELKOM. Downloaded on August 02,2024 at 08:13:23 UTC from IEEE Xplore. Restrictions apply.

|     |     |     |     |     | Governs its slice via |     | Through orchestration,  |
| --- | --- | --- | --- | --- | --------------------- | --- | ----------------------- |
server context
the SDN controller
Governs the SDN
| controller | Administrator  |     |                | Application/SDN controller |                |        |                           |
| ---------- | -------------- | --- | -------------- | -------------------------- | -------------- | ------ | ------------------------- |
|            |                |     |                |                            |                | Client | optimally dispatches the  |
|            | Server context |     | Server context | Server context             | Server context |        |                           |
selected resources to
such separate Resource
| Administrative |     | SDN controller |     |     |     |     | Groups. The interplay of  |
| -------------- | --- | -------------- | --- | --- | --- | --- | ------------------------- |
Server
| client | Resource |     | Resource |     |     |     |                            |
| ------ | -------- | --- | -------- | --- | --- | --- | -------------------------- |
|        | Group    |     | Group    |     |     |     | both controller functions  |
context
|               | Client context |                | Client context     |     |     |        | enables the fulfillment   |
| ------------- | -------------- | -------------- | ------------------ | --- | --- | ------ | ------------------------- |
| Resource      |                | Orchestration  |                    |     |     | Client |                           |
| orchestration |                | virtualization |                    |     |     |        | of the diverging service  |
| and           |                |                |                    |     |     |        | demands from all cli-     |
|               | Server context | Server context | ••• Server context |     |     |        |                           |
virtualization
ents while preserving
|     | Resource | Resource | Resource | Resource    | Resource |        |                      |
| --- | -------- | -------- | -------- | ----------- | -------- | ------ | -------------------- |
|     |          |          |          |             |          | Server | the isolation among  |
|     | Group    | Group    | •••      | Group Group | Group    |        |                      |
them.
Virtual Support
Client
resources resources
|     |     | support |     | Client context = slice |     |     |     |
| --- | --- | ------- | --- | ---------------------- | --- | --- | --- |
Resource Group
Client context
Figure 3. ONF SDN network slicing architecture [5].
According to [4], the major SDN architectur- by the client associated with that context to realize
al components are resources and controllers. For  its service(s). Through orchestration, the SDN con-
SDN, a resource is anything that can be utilized to  troller optimally dispatches the selected resources
provide services in response to client requests. This  to such separate Resource Groups. The interplay
includes infrastructure resources and NFs, but also  of both controller functions enables the fulfillment
network services, in application of the recursion  of the diverging service demands from all clients
principle described earlier. A controller is a logi- while preserving the isolation among them.
cally centralized entity instantiated in the control  The SDN architecture also includes an adminis-
plane which operates SDN resources at runtime  trator. Its tasks consist of instantiating and config-
to deliver services in an optimal way. Therefore,  uring the entire controller, including the creation
it mediates between clients and resources, act- of both server and client contexts and the installa-
| ing simultaneously as server and client via client  |     |     | tion of their associated policies.  |     |     |     |     |
| --------------------------------------------------- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
and server contexts, respectively. Both contexts  According to the ONF vision, the SDN architec-
are conceptual components of an SDN controller  ture naturally supports slicing [5], as the client con-
enabling the server-client relationships (Fig. 3): text provides the complete abstract set of resources
Client context: Represents all the information the  (as a Resource Group) and the supporting control
controller needs to support and communicate with  logic that constitute a slice, including the complete
a given client. It comprises a Resource Group and  collection of related client service attributes.
a Client support function. The Resource Group con- Another key functional aspect that makes SDN
tains an abstract, customized view of all the resourc- architecture ideal to embrace 5G slicing is recur-
es that the controller, through one of its northbound  sion. Because of the different abstraction layers
interfaces, offers to the client, in order to deliver  that the recursion principle enables, the SDN
on its service demands and facilitate its interaction  control plane can involve multiple hierarchically
with the controller. Client support contains all that  arranged controllers that extend the client-server
is necessary to support client operations, including  relationships at several levels (Fig. 4). According to
policies on what the client is allowed to see and do  these premises, it is evident that SDN can support a
[4], and service-related information to map actions  recursive composition of slices [5]. This implies that
between the client and the controller.  the resources (i.e., Resource Group) a given con-
Server context: Represents all the informa- troller delivers to one of its clients in the form of a
tion the controller needs to interact with a set of  dedicated slice (i.e., client context) can, in turn, be
underlying resources, assembled in a Resource  virtualized and orchestrated by such a client in the
Group, through one of its southbound interfaces.  case of being an SDN controller. This way, the new
The  process  of  transforming  the  set  of  controller can utilize the resource(s) it accesses via
Resource Groups accessed through server con- its server context(s) to define, scale, and deliver
texts to those defined in separate client contexts  new resources (and hence new slices) to its own
is not straightforward, and it requires the SDN  clients, which might also be SDN controllers.
controller to perform virtualization and orchestra-
| tion functions.  |     |     |     | nfV reference  |     |     |     |
| ---------------- | --- | --- | --- | -------------- | --- | --- | --- |
When performing the virtualization function, the
ArchItecturAl frAmework
SDN controller carries out the abstraction and the
aggregation/partitioning of the underlying resourc- Although the SDN architecture described above
es. Thanks to virtualization, each client context pro- gives a comprehensive view of the control plane
vides a specific Resource Group that can be used  functionalities enabling slicing, it lacks capabilities
IEEE Communications Magazine • May 2017 83
Authorized licensed use limited to: UNIVERSITAS TELKOM. Downloaded on August 02,2024 at 08:13:23 UTC from IEEE Xplore.  Restrictions apply.

• Orchestrator: According to ETSI, it has two
••••• set of functions performed by the Resource
Orchestrator (RO) and Network Service
Client SDN controller (level n + 1) Client Orchestrator (NSO), respectively. The RO
orchestrates the NFVI resources across
(potentially different) VIMs. The NSO per-
Southbound interfaces forms the life cycle management of network
VNF Network Network belonging to SDN services using the capabilities provided by the
Server controller (level n+1)
service service RO and the (potentially different) VNFMs.
Network Management System (NMS): Frame-
Client SDN controller (level n) Northbound interfaces work performing the general network manage-
belonging to SDN
ment tasks. Although its functions are orthogonal
controller (level n-1)
to those defined in MANO, NMS is expected to
interact with MANO entities by means of a clear
VNF PNF Infrast.
End separation of roles [9]. NMS comprises:
resources
client • Element management (EM): anchor point
SDN controller (level n – 1)
responsible for the fault, configuration,
accounting, performance, and security
Infrast. Infrast. PNF Infrast. Infrast. PNF (FCAPS) of a VNF.
resources resources resourcesresources Server • Operation/business support system (OSS/
Server
BSS): a collection of systems and manage-
SDN controller (level n – 2)
ment applications that network service provid-
••••• ers use to provision and operate their network
services. In terms of the roles we considered
PNF: Physical network function VNF: Virtualized network function
earlier, tenants would run these applications.
Figure 4. Complex client-server relationships enabled by the recursion in the The ETSI proposal includes two SDN controllers
SDN control plane, adapted from [7]. in the architecture. Each controller centralizes
the control plane functionalities and provides an
abstract view of all the connectivity-related com-
that are vital to efficiently manage the life cycle of ponents it manages. These controllers are:
network slices and its constituent resources. In this Infrastructure SDN controller (IC): Sets up
respect, the NFV architecture [6] is ideal to play and manages the underlying networking resourc-
this role, as it manages the infrastructure resources es to provide the required connectivity for com-
and orchestrates the allocation of such resources municating the VNFs (and its components [10]).
needed to realize VNFs and network services. Managed by the VIM, this controller may change
To benefit from the management and orches- infrastructure behavior on demand according to
tration functionalities of NFV, appropriate coop- VIM specifications adapted from tenant requests.
eration between SDN and NFV is required. Tenant SDN controller (TC): Instantiated in
However, embracing SDN and NFV architectures the tenant domain [11] as one of the VNFs or as
into a common reference framework is not an part of the NMS, this second controller dynami-
easy task [7, 8]. In this section, we briefly describe cally manages the pertinent VNFs used to realize
the tentative framework that ETSI presents in [8] the tenant’s network service(s). These VNFs are
to integrate SDN within the reference NFV archi- the underlying forwarding plane resources of the
tecture. This framework incorporates two SDN TC. The operation and management tasks that the
controllers, one logically placed at the tenant and TC carries out are triggered by the applications
another at the InP level. We commence providing running on top of it (e.g., the OSS).
a brief overview of the NFV architectural frame- Both controllers manage and control their
work, and later describe the integration of the underlying resources via programmable south-
two SDN controllers (Fig. 5). bound interfaces, implementing protocols like
The NFV architecture comprises the following OpenFlow, NETCONF, and I2RS. However, each
entities: controller provides a different level of abstrac-
Network Functions Virtualization Infrastruc- tion. While the IC provides an underlay to support
ture (NFVI): A collection of resources used to the deployment and connectivity of VNFs, the
host and connect the VNFs. While the broad TC provides an overlay comprising tenant VNFs
scope of SDN makes resource a generic concept, that, properly composed, define the network ser-
the current resource definition in the NFV frame- vice(s) such a tenant independently manages on
work comprises only the infrastructure resources. its slice(s). These different resource views each
VNFs: Software-based implementations of NFs controller offers through its interfaces have reper-
that run over the NFVI. cussions on the way they operate. On one side,
Management and Orchestration (MANO): the IC is not aware of the number of slices that uti-
Performs all the virtualization-specific manage- lize the VNFs it connects, nor the tenant(s) which
ment, coordination, and automation tasks in the operate(s) such slices. On the other side, for the
NFV architecture. The MANO framework [9] TC the network is abstracted in terms of VNFs,
comprises three functional blocks: without notions of how those VNFs are physically
• Virtualized infrastructure manager (VIM): deployed. Despite their different abstraction levels,
responsible for controlling and managing the both controllers have to coordinate and synchro-
NFVI resources. nize their actions [8]. Note that the service and
• VNF manager (VNFM): performs configu- tenant concept mentioned here can be extended
ration and life cycle management of the to higher abstraction layers by simply applying the
VNF(s) on its domain. recursion principle, as shown in Fig. 2.
84 IEEE Communications Magazine • May 2017
Authorized licensed use limited to: UNIVERSITAS TELKOM. Downloaded on August 02,2024 at 08:13:23 UTC from IEEE Xplore. Restrictions apply.

NFV management and orchestration (MANO) Both VIMs and WIMs
act as SDN applications,
OSS/BSS
Orchestrator
Tenant SDN controller delegating the tasks
Service, VNF and
infrastructure related to the manage-
description
EM B EM C
ment of networking
VNF resources to their
VNF A VNF B VNF C
manager(s)
underlying ICs. Although
in this example the ICs
NFVI
are deployed on the
Virtual Virtual Virtual
computing storage network NFVI, it would be possi-
Infrastructure SDN controller ble to integrate
Virtualization layer Virtualized
infrastructure them into their corre-
Hardware resources manager(s)
sponding VIMs
Computing Storage Network
hardware hardware hardware
Figure 5. Integrating SDN controllers into the reference NFV architectural framework at the two levels
required to achieve slicing [8].
network slIcIng use cAse prises an OSS, a TC, and an NSO. The OSS,
an SDN application from the TC’s perspective,
wIth sdn-nfV IntegrAtIon
instructs the controller to manage slice’s constitu-
In this section, we describe an SDN-enabled NFV ent VNFs and logically compose them to efficient-
deployment example that illustrates the network ly realize the network service(s) the slice offers.
slicing concept, with several slices running on a The life cycle of such network service(s) is man-
common NFVI (Fig. 6). This deployment includes aged by the NSO, which interacts with the TC via
two tenants, each managing a particular set of the OSS. The TC, deployed as a VNF, relies on the
slices. In the example, we only consider a single capabilities provided by virtual switches/routers
level of recursion, and thus the tenants directly (in the form of VNFs as well) to enable the VNF
serve the end users. Each slice consists of VNFs composition, forwarding pertinent instructions to
that are appropriately composed to support and such virtual switches/routers via its southbound
build up the network service(s) the slice (and interfaces. Through its northbound interfaces, the
thus the tenant) delivers to its users. Note that TC provides a means to securely expose select-
the deployment includes two distinct phases: ed network service capabilities to end users.
first, a slice creation phase, in which an end user Such interfaces allow end users to retrieve con-
requests a slice from a network slice catalog, and text information (real-time performance and fault
then the tenant instantiates the slice; and next, information, user policies, etc.), operate, manage,
a runtime phase, where the different functional and make use of the slice’s network service(s),
blocks within each slice have already been creat- always within the limits set by the tenant.
ed and are now operative. For simplicity, in Fig. 6 The fact that each slice is provided with its
we only depict the runtime phase. own NSO, OSS, and TC instances enables the
The example considers that the tenants required management isolation.
access NFVI resources from three InPs. InP1 pro- Each tenant must efficiently orchestrate its
vides compute and networking resources, both assigned resources to simultaneously satisfy the
deployed on two NFVI points of presence (NFVI- diverging requirements of the slices that are under
PoPs) [12] in the form of DCs. InP2 and InP3 its management. The RO is the functional block
provide SDN-based WAN transport networks, that performs such task on behalf of the tenant,
used to communicate such NFVI-PoPs. The VMs providing each slice with the required resourc-
and their underlying hardware, instantiated in the es via interfaces with each slice’s NSO. The RO
NFVI-PoPs and in charge of hosting VNFs (and must perform the resource sharing among slices
their components), are directly managed by the while fulfilling their required performance, follow-
VIMs. The networking resources, supporting VM ing an adequate, effective resource management
(and hence VNF) connectivity at the infrastructure framework that must comply with both tenant
level, are programmatically managed by the ICs and slice-specific policies. Such a framework is
following the VIM and the WAN infrastructure required so that the RO enables performance iso-
manager (WIM) premises. Both VIMs and WIMs lation among slices.
act as SDN applications, delegating the tasks relat- All the NFVI resources available for use by a
ed to the management of networking resources tenant (i.e., those that RO orchestrates) are sup-
to their underlying ICs. Although in this example plied by the different InPs. Each InP rents part
the ICs are deployed on the NFVI, it would be of the virtual resources according to a business
possible to integrate them into their correspond- lease agreement that both InP and tenant have
ing VIMs, as [8] suggests. previously signed. To access, reserve, and request
On top of the InPs, the tenants independently such resources, the tenant’s RO interacts with the
manage a set of network slices. Each slice com- VIM(s)/WIM(s) by means of interfaces those func-
IEEE Communications Magazine • May 2017 85
Authorized licensed use limited to: UNIVERSITAS TELKOM. Downloaded on August 02,2024 at 08:13:23 UTC from IEEE Xplore. Restrictions apply.

| Web portals  |                       |     |     |                       |     | Web portals  |
| ------------ | --------------------- | --- | --- | --------------------- | --- | ------------ |
| and APIs for |                       |     |     |                       |     | and APIs for |
| end users    |                       |     |     |                       |     | end users    |
| O&M          | End users for slice 1 |     |     | End users for slice 1 |     | O&M          |
|              |                       | OSS | OSS |                       |     |              |
VNFs instantiated
VNFs instantiated
| in orange VMs | TC(VNF) |     |         | TC(VNF) | in blue VMs |     |
| ------------- | ------- | --- | ------- | ------- | ----------- | --- |
|               | Slice 1 |     | Slice 1 |         |             |     |
Forwarding Forwarding
instructions instructions
| VNF | VNF vRouter/ | NSO | NSO | vRouter/ | VNF | VNF |
| --- | ------------ | --- | --- | -------- | --- | --- |
vSwitch vSwitch
|       | Tenant 1                    |                         |        |                            | Tenant 2 |       |
| ----- | --------------------------- | ----------------------- | ------ | -------------------------- | -------- | ----- |
|       |                             | RO                      | RO     |                            |          |       |
|       |                             | WIM                     | WIM    |                            |          |       |
|       | VIM                         |                         |        |                            | VIM      |       |
|       |                             | WAN IC                  | WAN IC |                            |          |       |
|       | IC                          |                         |        |                            | IC       |       |
|       | VMVM VMVM                   | Forwarding instructions |        | VMVM VMVM                  |          |       |
|       | VMVM VMVM                   |                         |        | VMVM VMVM                  |          |       |
| NFVI- | Virtualization layer        |                         |        | Virtualization layer       |          | NFVI- |
| PoP 1 |                             |                         |        |                            |          | PoP 2 |
|       | Networking ComputingStorage |                         |        | StorageComputingNetworking |          |       |
|       | InP1                        | InP2                    | InP3   |                            | InP1     |       |
IC: Infrastructure SDN controller        TC: Tenant SDN controller
Figure 6. Network slicing deployment in a common framework, integrating both SDN and NFV.
tional blocks expose and that tenant’s RO con- guarantee that faults or attacks occurring in one
sumes. Indeed, we assume that VIMs and WIMs  slice are confined to that slice, preventing their
|     | support multi-tenancy. We also assume that WIMs  |     | propagation across slice boundaries. |     |     |     |
| --- | ------------------------------------------------ | --- | ------------------------------------ | --- | --- | --- |
can communicate with each other according to  Additionally, although recursion has not been
predefined business agreements. In this respect,  addressed in this example, it is readily applica-
the interaction between a WIM and an RO might  ble to this scenario by simply assuming that some
be achieved indirectly through another WIM.  of the slice’s users are tenants that in turn can
As Fig. 6 suggests, the resource management  deploy and operate their own slices.
must be performed at two levels: at the infra-
chAllenges And reseArch dIrectIons
structure level, where a slice-agnostic VIM/WIM
provides the subscribed tenants with (virtualized)  In this section, we identify the main challenges
infrastructure resources, and at the tenant level,  and future research arising from implementing
|     | where the RO delivers its assigned resources to  |     | slicing in 5G systems. |     |     |     |
| --- | ------------------------------------------------ | --- | ---------------------- | --- | --- | --- |
the corresponding slices. Both the VIM(s)/WIM(s)
performAnce Issues In A shAred InfrAstructure
and the RO have to collect accurate resource
usage information (each at its domain) and in turn  When network slices are deployed over a com-
to forecast resource availability in relatively short  mon underlying substrate, the fulfillment of the
timescales to satisfy tenant and slice demands,  performance isolation requirement is not an easy
|     | respectively. |     | task. If a tenant’s RO only assigns dedicated  |     |     |     |
| --- | ------------- | --- | ---------------------------------------------- | --- | --- | --- |
Please note that, with the exception of hard- resources to network slices, their required per-
ware resources, the functional blocks (e.g., VIM,  formance levels are always met at the cost of
RO, NSO, SDN controllers) are modeled as inde- preventing slices sharing resources. This leads to
pendent software components. The need for  overprovisioning, an undesired situation bearing
separate access, configuration, and management  in mind that the tenant has a finite set of assigned
suggests this modeling, wherein the software rela- resources. One way to resolve this issue is to per-
tionships are enabled with the help of the appli- mit resource sharing (see, e.g., [13]), although this
cation programming interfaces (APIs) that each  means slices are not yet completely decoupled
component provides. in terms of performance. Thus, it is required to
To preserve security and privacy isolation  design adequate resource management mecha-
among slices, it is required to apply the compart- nisms that enable resource sharing among slices
mentalization principle at each virtualization level.  when necessary without violating their required
In addition, each functional block and manage- performance levels. To accomplish the sharing
able resource (e.g. VNF) within a given slice must  issue, the RO could use policies and strategies
have its own security mechanisms, ensuring oper- similar to those used in VIMs (e.g., the OpenStack
ation within expected parameters and preventing  Congress module or Enhanced Platform Aware-
|     | access to unauthorized entities. This is intended to  |     | ness attributes). |                                         |     |     |
| --- | ----------------------------------------------------- | --- | ----------------- | --------------------------------------- | --- | --- |
| 86  |                                                       |     |                   | IEEE Communications Magazine • May 2017 |     |     |
Authorized licensed use limited to: UNIVERSITAS TELKOM. Downloaded on August 02,2024 at 08:13:23 UTC from IEEE Xplore.  Restrictions apply.

mAnAgement And orchestrAtIon Issues [3] N. M. M. K. Chowdhury and R. Boutaba, “A Survey of Net-
Given the dynamism and scalability that slicing work Virtualization,” Computer Networks, vol. 54, no. 5, Given this business-ori-
Apr. 2010, pp. 862–76
brings, management and orchestration in multi- [4] ONF TR-521, “SDN Architecture,” Feb. 2016. ented approach, new
tenant scenarios are not straightforward. To [5] ONF TR-526, “Applying SDN Architecture to 5G Slicing,”
flexibly assign resources on the fly to slices, the Apr. 2016. transition strategies
[6] ETSI GS NFV 002, “Network Functions Virtualization (NFV);
optimization policy that governs the RO must must be broadly ana-
Architectural Framework,” v. 1.1.1, Dec. 2014.
deal with situations where resource demands [7] ONF TR-518, “Relationship of SDN and NFV,” Oct. 2015 lyzed, allowing for a
vary considerably in relatively short timescales. To [8] ETSI GS NFV-EVE 005, “Network Functions Virtualisation
accomplish this: (NFV); Ecosystem; Report on SDN Usage in NFV Architec- gradual evolution to
tural Framework,” v. 1.1.1, Dec. 2015.
• An appropriate cooperation between [9] ETSI GS NFV-MAN 001, “Network Functions Virtualisation future 5G networks and
slice-specific management functional blocks (NFV); Management and Orchestration,” v. 1.1.1, Dec. 2014.
ensuring compatibility
and RO is required. [10] ETSI GS NFV-INF 001, “Network Functions Virtualisation
• Policies need to be captured in such a way that (NFV); Infrastructure Overview,” v. 1.1.1, Jan. 2015. with past infrastructure
[11] ETSI GS NFV-SEC 003, “Network Functions Virtualisation
they can be automatically validated. This auto-
(NFV); NFV Security; Security and Trust Guidance,” v. 1.1.1, investments. To accom-
mation enables both the RO and slice-specific Dec. 2014.
functional blocks to be authorized to perform [12] ETSI GS NFV 003, “Network Functions Virtualisation (NFV); plish this, a deep review
the corresponding management and configu- Terminology for Main Concepts in NFV,” v. 1.2.1, Dec. 2014. of the telecom regula-
[13] P. Andres-Maldonado et al., “Virtualized MME Design for
ration actions in a timely manner.
IoT Support in 5G Systems,” Sensors, vol. 16, no. 8, Aug. tory framework has to
• It is necessary to design computational- 2016, pp. 1338–62.
ly efficient resource allocation algorithms [14] R. Harel and S. Babbage, “5G Security Recommendations be made.
and conflict resolution mechanisms at each Package #2: Network Slicing,” NGMN Alliance, Apr. 2016.
abstraction layer.
bIogrAphIes
securIty And prIVAcy Jose ordonez-Lucena (jordonez93@gmail.com) received his
B.Sc. in telecommunications engineering from the University of
The open interfaces that support the programma-
Granada, Spain, in 2015. Currently he is a Master’s student and
bility of the network bring new potential attacks is working in research projects with the Department of Signal
to softwarized networks. This calls for a consistent Theory, Telematics and Communication of the University of
multi-level security framework composed of poli- Granada. His research interests are focused on network virtual-
ization and network slicing in 5G systems.
cies and mechanisms for software integrity, remote
attestation, dynamic threat detection and mitiga- PabLo ameigeiras (pameigeiras@ugr.es) received his M.Sc.E.E.
tion, user authentication, and accounting manage- degree in 1999 from the University of Malaga, Spain. He per-
ment. The security and privacy concerns arising formed his Master’s thesis at the Chair of Communication
Networks, Aachen University, Germany. In 2000 he joined the
from 5G slicing (see [14]) are today a major barrier
Cellular System group at Aalborg University, Denmark, where
to adopting multi-tenancy approaches. he carried out his Ph.D. thesis. After finishing his Ph.D. he
worked at Optimi/Ericsson. In 2006 he joined the University
new busIness models of Granada, where he has been leading several projects in the
field of LTE and LTE-Advanced systems. Currently his research
The innovative partnerships between several
interests include the application of the SDN and NFV paradigms
players, each providing services at different posi- for 5G systems.
tions of the value chain, and the integration of
new tenants such as verticals, over-the-top service diego LoPez (diego.r.lopez@telefonica.com) joined Telefonica
I+D in 2011 as a senior technology expert and is currently in
providers, and high-value enterprises, empow-
charge of the Technology Exploration activities within the GCTO
ers promising business models. Given this busi- Unit. He is focused on network virtualization, infrastructural
ness-oriented approach, new transition strategies services, network management, new network architectures, and
must be broadly analyzed, allowing for a gradu- network security. He chairs the ETSI ISG on Network Functions
Virtualization and the NFVRG within the IRTF, and he is a mem-
al evolution to future 5G networks and ensuring
ber of the Board of 5TONIC, the Telefonica 5G Testbed.
compatibility with past infrastructure investments.
To accomplish this, a deep review of the telecom Juan J. ramos-munoz (jjramos@ugr.es) received his M.Sc. in
regulatory framework has to be made. Innova- computer sciences in 2001 from the University of Granada.
Since 2009, he has held a Doctorate degree from the same
tive ways of pricing, new grounds for cost shar-
university. He is a lecturer at the Department of Signals Theory,
ing and standardized solutions, which provide the Telematics and Communications of the University of Granada.
required support for interoperability in multi-ven- He is also a member of the Wireless and Multimedia Network-
dor and multi-technology environments, must be ing Lab. His research interests are focused on real-time multi-
media streaming, quality of experience assessment, network
studied as well.
virtualization, and network slicing for 5G.
Acknowledgments Javier Lorca (franciscojavier.lorcahernando@telefonica.com)
This work is partially supported by the Spanish received an M.Sc. degree in telecommunication engineering
from Universidad Politécnica de Madrid in 1998, and is current-
Ministry of Economy and Competitiveness, the
ly pursuing his Ph.D. degree at the University of Granada. He is
European Regional Development Fund (Project in charge of Radio Access Networks Innovation within Telefóni-
TIN2013-46223-P), the Ministry of Education, ca Global CTO. His research is focused on 5G, including virtual-
Culture, and Sport of the Government of Spain, ization, massive MIMO, mmWave, new waveforms, interference
control, and advanced channel coding techniques. He has multi-
under grant Beca de Colaboración (2015-2016),
ple patents and publications and a book chapter on 5G.
and the University of Granada, under grant Beca
de Iniciación a la Investigación (2016-2017). Jesús FoLgueira (jesus.folgueira@telefonica.com) received his
M.Sc. degree in telecommunications engineering from Univer-
sidad Politécnica de Madrid (1994) and M.Sc. in telecommuni-
references
cation economics in 2015 (UNED). He joined Telefónica I+D
[1] 5G-PPP, ERTICO, EFFRA, EUTC, NEM, CONTINUA and Net- in 1997. He is currently the head of Transport and IP Networks
world2020 ETP, “5G Empowering Vertical Industries,” white within Telefonica Global CTO unit, in charge of network planning
paper, Feb. 2016. and technology. He is focused on optical, metro, and IP net-
[2] M. Pearce, S. Zeadally, and R. Hunt, “Virtualization: Issues, work architecture and technology, network virtualization (SDN/
Security Threats, and Solutions,” ACM Computer Surveys, NFV), and advanced switching. His expertise includes broadband
vol. 45, no. 2, Feb. 2013, pp. 1–38. access, R&D management, and network deployment.
IEEE Communications Magazine • May 2017 87
Authorized licensed use limited to: UNIVERSITAS TELKOM. Downloaded on August 02,2024 at 08:13:23 UTC from IEEE Xplore. Restrictions apply.