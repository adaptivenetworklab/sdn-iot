# Multi-tenancy in decentralised IoT

> Source file: `Multi-tenancy in decentralised IoT.pdf`

---

Multi-Tenancy in Decentralised IoT
Sylvain Cherrier∗, Zahra Movahedi∗, Yacine M. Ghamri-Doudane†
∗ Université Paris-Est , Laboratoire d’Informatique Gaspard Monge (CNRS : UMR8049)
† L3i Lab, University of La Rochelle, La Rochelle, France.
Abstract—SincetheInternetofThings(IoT)hasbecomemore In any case (Data approach, or Service approach) a cen-
and more important, new solutions should be proposed in order tralised IoT raises possible issues such as data confidential-
toadaptthespecificitiesintroducedbythisinterconnectionofthe
ity, application security, data ownership, and also network
physical world (Sensors and Actuators) and the public networks
overload (due to the important number of nodes deployed
(The Internet). Some of these solutions use a Cloud approach.
The amount of data collected by Things rises the interest of on WSANs, and the strong constraints of these networks).
the Big-Data community. The main design chosen for the IoT is Choreography reduces in a significant way the transmitted
the centralisation of all data collected and a central treatment volumeofinformationfromandtoeachnode[5].Asdataare
of these data. But another approach is to decentralise the data
processed directly on the node, the only messages exchanged
processing, in order to dramatically lighten the network and
are semantic informations describing the result of the data
limit the exchange to a reduced set of semantic messages. This
decentralised architecture has assets in term of confidentiality, computation.Thelocalprocessingofdatarelievesthenetwork
dataownershipandenergysaving.Butthen,howtosharethings usage (and often objects networks are very constrained in
among users, and keep the control? If computing is done on termsofbandwidth),theenergyconsumption(computingcost
each object, how a user can integrate public objects in its own
is cheaper than transmitting) and does not raise the issue
application, as these objects are used by some other users? How
of data ownership (data are not transmited). Even if Chore-
toorganiseaccesstothesensorsandactuatorsprovidedbythese
objects? This paper proposes an architecture that gives multi- ographedIoTprogramminglanguageshavelimitedprocessing
tenantcapabilitytoIoTdecentralisedapplications,inwhichusers expressivity, they are sufficient to meet the needs of IoT
are using and sharing their objects. A generic architecture is applications.
described, and integrated in our IoT platform as an example.
Index Terms—Multi-Tenancy; Internet of Things; Services This architecture is able to give users the opportunity to
Oriented Computing; Virtual machine build versatile applications, adapted to theirs needs [7]. But
there are an issue when these applications grow, particularly
I. INTRODUCTION when users want to share objects with others, or use public
objects (in a smart city scenario, this could be public display
The Internet of Things is the result of the mix of new
panels, a parking lot reservation system, etc). According to
capabilities added to everyday objects (communication, com-
the Choreography paradigm, each user wants his own control
putation),theincreaseusageofsensorsandactuators(Wireless
flow,hisownsemanticmessagesandhisownobject’reactions,
SensorandActuatorsNetwork,WSAN),andthemassivetake-
and/orintegratepublicobjectwithinhisapplication(forexam-
up and use of the Internet. As soon as they can be connected
ple, to be informed of one available location in a parking lot,
to the Internet, all these things send the data gathered from
andautomaticallyreservedit).Inordertoshareobjectsamong
theircloseenvironmenttoacentralpoint,wherecomputingis
users and still give them the ability to integrate them in their
done and actions can be decided. Then, this central point of
owndecentralisedIoTapplications,amulti-tenantarchitecture
decision can send an order to an actuator in order to react to
must be provided.
the situation.
Some approaches have chosen a "Service" point of view. Amulti-tenantChoreographedarchitectureshouldsolvethe
Insteadofmanipulatingdata,theServiceOrientedComputing following issues:
(SOC) in IoT represents each Thing (or group of Things) as a
service that can be accessible through the Internet [7]. In this • How to handle multiple control flows on objects?
approach,twoorganisationarefeasible[12]:Acentralisedone, • How to define access and rights of each user over the
in which a unique central point interacts with all the services, device?
andadecentralisedone,inwhichservicesinteractwithothers, • How to handle conflicts, particularly concerning the ac-
depending on their own requirements. tuators usages, in case of receiving contradictory orders?
The first approach is called "Services Orchestration". The
central point orchestrates the application, invoking services Thispaperisorganisedasfollow:SectionIIpresentsrelated
following the need of its control flow. The second approach works and some background for our solution. Section III
is called "Services Choreography". In a Choreography, each describes the foundation of a multi-Tenant architecture. The
node reacts to its environment and to its partners. No one has integration of such an architecture on our IoT platform are
a complete view of the running application, each stakeholder giveninSectionIV.Finally,concludingremarksendthispaper
follows its own control flow. in Section V.
978-1-5A0u9th0o-0ri3ze6d6 l-i2ce/1n5se/$d3 u1s.e0 0lim ©it2ed0 1to5: IInEsEtitEut Teknologi Bandung. Downloaded on July 29,2024 at 16:13:08 UTC from IEEE Xplore. Restrictions apply.

II. RELATEDWORKANDBACKGROUND SwissQM [11] is an another example of virtual machine
forresourceconstraineddevicesthatusesSQLquery-likeand
A. Related work
XQuery query to program a sensor networks. SwissQM is
This paper is about the extension of IoT architectures composedoffollowingcomponents:anOperandStackforthe
in order to add a multi-tenancy layer that supports users stack-basedvirtualmachine,aTransmissionBufferthatisused
priority access for shared devices. Our IoT platform is based to store message data and can also serve as temporary storage
on a virtual machine, D-LITe [4], that allows constrained forprograms,aSynopsis(adatastructure)thatisusedfordata
devices to realise Decentralized IoT applications. Several aggregation and for maintaining state over several invocations
virtual machines for resource constrained devices have been oftheprogramandasensorInterface.SwissQM doesnotpro-
implemented in the WSAN literature. In the following part, vide priority mechanism. The sensor nodes running SwissQM
we review these virtual machines and analyse the support of form a tree topology rooted at a gateway node that provides
multi-tenancy in their system. access to the sensor network. SwissQM is able to execute up
The Wukong project [10] proposes a sensor profile frame- to six QM programs concurrently. No priority mechanism is
work based on an object-oriented programming to create performed in this approach.
virtualized sensor abstractions for low-level physical sensor PyMite [1] is a flyweight Python interpreter written from
devices. WuKong Applications are designed as program com- scratch to execute on 8-bit and larger microcontrollers with
position using an abstract form of data flow programming resourcesaslimitedas64KBofprogrammemory(flash)and
and event-driven control flow. In this sense, each device is 4 KB of RAM. PyMite supports a subset of the Python 2.5
virtualizedbyaWuClasswithasetofpropertiesthatdescribe syntax and can execute a subset of the Python 2.5 bytecodes.
and allow access to the resource represented by the WuClass, PyMitecanalsobecompiled,testedandexecutedonadesktop
andanupdate()functiontoimplementtheclass’behaviour.In computer.
this approach, even if there is a control access mechanism for
allowing/denying the access to an object. However the notion B. D-LITe : a virtual machine for decentralized IoT applica-
of priority in control access is absent. tions
Maté [8] is the second VM presented here. Maté is a
our own soution for IoT application is base on a virtual
domain specific bytecode interpreter running on TinyOS [9]
machine called D-LITe [4]. D-LITe is a lightweight RESTful
for programming sensor networks. Programs are small scripts
virtual machine deployed on decentralised IoT devices (see
containing Maté VM instructions (capsules). The basic VM
Figure 1). D-LITe provides a universal access to the function-
template includes the scheduler, concurrency manager, and
alities of heterogeneous devices. In D-LITe, a set of possible
capsule store. The scheduler executes runnable contexts in a
device basic functionalities (called features) such as button,
FIFO round-robin method. The concurrency manager submits
switch, timer, led, etc. are firstly defined. Each feature is
contexts to the scheduler based on whether they are ready to
driven by a set of potential small algorithms that specify the
run and can safely access the shared resources they require.
device functionality and control its usage. These algorithms
The capsule store manages capsule storage and loading; it
are expressed through "Transducers"1 . A Transducer is a
propagates capsules through the network and notifies higher
advanced form of Finite State Machines; i.e. each Thing is
level components when it receives new code. Maté does not
seen as a component with a current state, inputs, outputs,
support priorities.
and transitions. Inputs and outputs are the message events
Squawk [13] is a JVM developped by Sun Microsystems
exchanged by nodes through the network, and states are the
that employs Split VM architecture to minimize resource
node’s reaction to received messages. A transition links two
and memory consumption.In this approach, tasks of the VM
states. A transition can be triggered by an input. States,
that require a large of resource consuming (such as class
transitions, and inputs describes the algorithm to be executed.
file loading and verification) are performed on the desktop.
Transducers add an output to the well-known Finite State
a preloaded and preverified file is generated and transferred
Machines description. The output is generated by the Tran-
then to the motes. Squawk implements a compact garbage
sition when triggered. The transducer representations used in
collection, named Lisp 2, so that tasks are non-preemptible,
D-LITe(andtheirspecificities)aredescribedwithSALT[6],a
whichhasimplicationforhandlinginterruptsinadevicedriver
simpledescriptionlanguagethatlimitsbandwidthandmemory
written in Java. TakaTuka [2] is another example of JVM that
consumption.
issimilartotheSquawk reducingtheusageofRAMandflash
D-LITe uses exchanged messages between devices in order
using some optimization methods. The notion of priority is
tocomposedevicesinteractionsandtocreateIoTapplications.
lacking in Squawk and TakaTuka.
To control the correctness of a composition, typical messages
Darjeeling [3] is a JVM that provides a rich set of (Java)
(called "Interaction Patterns") are exchanged. In this sense,
featuresincludinglight-weightthreads,dynamicmemoryman-
two devices A and B could connect to each other if and only
agement (garbage collection), and exception handling, while
ifthedeviceA’outputmatcheswiththedeviceB’inputusing
atthesametimebeingoptimisedforresource-poortargets.At
themomentDarjeelingdoesnotsupportprioritiesandthreads
1TheseTransducersdescribethecontrolflow,thealgorithmthatdefinesthe
are simply scheduled in a round-robin fashion. objectbehaviour
Authorized licensed use limited to: Institut Teknologi Bandung. Downloaded on July 29,2024 at 16:13:08 UTC from IEEE Xplore. Restrictions apply.

details, and the use of variables).
III. MULTI-TENANTARCHITECTUREOVERVIEW
To be able to handle multiples accesses on a single device,
the following points should be defined and analysed:
A. Impacts of multiple control over an IoT device
Since each IoT device can be a sensor or/and an actuator,
a multi-Tenant architecture has to cope with these two cases.
Sensing in a multi-tenancy architecture is not a very com-
plexissuetosolve.Dependingontheaccessrules,thegathered
data are accessible or not. The flow control will read (or not)
the data.
Actuating is more complex. In the IoT, every (public, or
Figure1. AD-LITeObject,runningaTransducer,interactswiththerealworld personal and shared) device must be kept under its owner’s
andcollaborateswithotherobjects.Thesensingandcollaboratingobjectssend
control. For example, in smart cities, a public display panel,
messagestotheTransducerAnalyserinput.Thesemessagescontainmeasures
or actions to do. These messages trigger reactions from the transducer if a or a parking lot, are accessible to everyone, but security agent
Transition is found for the current state and the input. In that case, the or public services have a priority access (police, hospital,
transducer changes its state, and sends an output message (if defined in
etc). In smart building domain, a fully operational desk (with
the transition). This output message is for actuating functionality or for
collaboratingobjects. computer, phone etc) can be shared among several users, but
should be reserved to a privileged employee.
The multi-tenant architecture needs to set a shared func-
theseInteractionPatterns.D-LITeallowsanend-usertodeploy
tionality under an access control mechanism. In this sense,
a specific behaviour on each device. Each D-LITe enabled
an access rights list for each type user should be provided.
node contains a rules analyzer to execute the behaviour. D-
Because of IoT devices versatility, the handled functionality
LITe devices also have a messaging service to interact with
must be correctly defined, according to the user’s usage. For
each others using XMPP protocol. a standardized protocol
example, the physical access control to a specific room can
for real time communication. This protocol offers instant
be prioritised. In some cases, the usual user of the room is
messaging and presence management. Thus, the discovery of
able to allow other employees to access to his room. But he
new devices is dynamic and their integration in the global
must get a priority access to his own room when he is having
structure is easy. The XMPP-REST (an extension we have
confidential meetings. In some other cases, an actuator of the
createdforD-LITe,allowingtosendRESTcommandsthrough
samekindcanbeusedtogiveanemployeetheabilitytolimit
XMPP) handles behaviours on each device using GET, PUT,
accesses to his room, while the security agents have the total
DELETE, and POST methods. GET RESTful method helps
control over it. If they need it, they can force the opening of
to discover existing features supported by the device, PUT
the door.
method deploys a behaviour on a device, DELETE method
Amulti-tenantsolutionfortheIoTshouldoffertosetwhich
removes an existing behaviour from the device, and POST
object’ functionalities are under control, and exactly which
method exchanges messages between two device’ behaviours.
commands have priority for each functionality. For the last
The implementation of REST approach within XMPP allows
example above, we define that "opening" is the under-control
the use of the presence and chat mechanism offered by the
action for this door. Then, we can describe the access rules:
instant messaging protocol, while this extension mimics the
Securityagentshavepriorityonthisaction,thentheemployee
calls to a web service with the REST commands.
(owneroftheroom)hasalowerpriority,andfinallytheothers.
D-LITe follows an event-centric approach. An object (more
precisely the behaviour that the virtual machine is currently B. Impacts of multi-tenant devices over the control flow
running) reacts on received messages, as events. There are Our approach for Multi-Tenancy in the IoT is closed to
different kinds of events: external events that make an object the access control used in operating systems (such as Linux,
collaborate with other objects, inside an IoT application; Windows, etc). As incoming orders are not predictable, and
hardware events that are used for sensing and actuating the can be contradictory, the multi-tenancy system uses blocking
world; and logical events that define, alter, and test variables. accesses. On one hand, the blocking mechanism controls the
The transducer handles the received events and reacts accesstoaactionoradata.Ontheotherhand,whenaconflict
depending the behaviour deployed. the incoming message isdetected,theuserthathasthelowerpriorityisinformedthat
comes from the hardware (a data has been gathered), or an the order has been refused. We propose to send notifications
external message from another Object (the Choreography). tothedevicehandler,sothataprogrammercouldhandleeach
If a transition is triggered by this event (it match the event conflict, and react to an "access denied".
and the current state), its output is sends it to the hardware IoT devices have two major capabilities: Sensing the phys-
in order to actuate it, or/and to other nodes (in a case of an ical world, and/or actuating it. Multi-Tenancy conflicts have
external message), depending of its type (see [6] for more different impacts for these two categories:
Authorized licensed use limited to: Institut Teknologi Bandung. Downloaded on July 29,2024 at 16:13:08 UTC from IEEE Xplore. Restrictions apply.

For the actuating category, there is 3 cases:
• First case, a user wants to trigger an action. The func-
tionality is not under control, or not shared, or the user
has the best priority. In that case, his control flow takes
controlofthefunctionality,andusesitaslongasitneeds.
• Second case, a user wants to trigger an action, but this
actionisalreadyinusebyanothercontrolflowwithabest
priority. This is a blocking case. In that case, the control
flowisblockedandwaitsforthefunctionalitytobefreed.
It is also possible to execute an alternative in that case,
in order to bypass the blocking case by doing something Figure 2. The control flow running in the object tries to lock a door. The
else. A specific "accessDenied" event is thrown to the main flow receives an eventA, then tries to lock the door. If it succeeds, it
waits for eventB to unlock, and then follow this main control flow. In the
control flow, and the programmer can catch it and then
casetheaccesstothedoorlockisnotgranted,theprogrammerhasdescribed
describe what to do. an alternative action (alt1), that will then follow its own logic. If access to
• The last case appears when a control flow has taken the the door lock is given by the security manager, but that an higher-priority
userrequestthedoorusagebeforeoureventBfreestheaccess,analternative
control of a functionality, and then another control flow
is described ("controlLost" event). The other control flow can have its own
(with better priority) asks for it. In that case, the prior actions,andthengoesbacktothemaincontrolflow.
control flow loses its access, and the access is granted to
the second control flow. A specific "controlLost" event
The security layer executes access controls each time any
is thrown to the control flow that has lost the access
transducer sends or receives an event to/from the hardware.
(because of its lesser priority). It is possible to handle
From outside the object, the access to the security layer
this event, in order to describe an alternative control
is cyphered. An object is owned by a user and must be
flow when losing the access to a functionality while
controlled only by him. The owner defines remotely for each
processing.
functionality the orders’ priority. As seen above, for a given
Forthesensingcategory,thecontrolaccessgrantsordenies
functionality, each user may prefer to control a specific order
access to the control flow, as defined by its rules. According
(for the smart building example, opening the door if the user
to the rules, the data is (or not) accessible, and there is no
aimstoprioritisesecurity,orclosingthedoorifconfidentiality
more impact. For example, if the control flow of a given user
is the main concern).
asks for humidity data but has no access to this sensor, it will
Priority levels are:
be blocked. In our approach, sensing a data is an incoming
event. If a transducer has no right to access the data, it means 1) private: reserved to the owner
that it will never receive the corresponding event. In facts, if 2) priority:from1(thehigher)to4(thelower).Theowner
thisdataisimportantforthecontrolflow,wecanimaginethat can set the priority for each user, each functionality and
the chosen control flow should not be executed on this device each order.
because of the user’s low priority (i.e. in operating system, 3) free: total access to the functionality.
when a not priority user tries a forbidden action, he can be Once the owner has defined his priority access list, all
blocked). users accessing the device can deploy a transducer (a control
TheFigure2representsacontrolflowwithalternativesasit flow) on it, and every access to the hardware will be evaluate
triestolockadoor.Thedifferentevents(AandB)arethemain according to the access list.
flow. Event A leads to a door locking, then event B unlocks it
IV. IMPLEMENTATION
(thesecondpartofeachtransitionistheoutputmessageofthe
transducer. In D-LITe, they are actuating orders for hardware, This section describes the multi-tenant extension to our
or messages for other object). But if a priority conflict results platformfortheIoT.ASecuritylayerisaddedtoeveryobject,
in an access denied, an alternative control flow ("case 2") is placed between the Transducer analyser and the operating
proposed (triggered by "accessDenied" event). This solution system (see Figure 3).
gives the opportunity to avoid the lock by giving alternate
A. Security service
tasks to do. An access lost lately in the process is handled
(see Figure 2) by the "controlLost" event catch in the "case The deployment of transducer is unchanged. An authen-
ticated user (D-LITe use XMPP, but this is not mandatory)
3" branch of the control flow.
accesses to an object through the network. He uses the PUT
C. Security Layer
order (XMPP-REST in our case, but this can be modified if
In order to realise an access control for sensing and actuat- needed) to deploy a new transducer. Then, objects exchange
ingcapabilitiesoftheobjectwhileitrunsseveralcontrolflows, eventsthroughtheXMPPpub-submechanism(SeeFigure3).
a security layer is installed between the hardware drivers and Whenanewuseraccessesanobject(authorizedbecausethe
theprocessmanager.Inthecaseofourproject,wehaveadded owner has shared this object to him, or because it is a public
it between the operating system and the transducers analyser. object such as in the smart city scenario described above),
Authorized licensed use limited to: Institut Teknologi Bandung. Downloaded on July 29,2024 at 16:13:08 UTC from IEEE Xplore. Restrictions apply.

|     |     |     |     |     |     |     |     | invoked    | by all | users     | of priority | 1 and     | 2. Carol | and        | Alice can   |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --------- | ----------- | --------- | -------- | ---------- | ----------- |
|     |     |     |     |     |     |     |     | lock and   | unlock | the door  | while       | Denis     | can      | not. Denis | has the     |
|     |     |     |     |     |     |     |     | right to   | close  | the door, | but         | Alice and | Carol    | overtake   | Denis’      |
|     |     |     |     |     |     |     |     | order. The | door’  | displayer |             | gives an  | example  | of a       | free access |
toafunctionality.Anyusercandisplayamessageonthedoor.
|     |     |     |     |     |     |     |     | Only high   | priority | users   | (priority | 1)      | can       | clear the | displayer, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ------- | --------- | ------- | --------- | --------- | ---------- |
|     |     |     |     |     |     |     |     | while other | users    | can     | only      | add new | messages. | Level     | 3 and      |
|     |     |     |     |     |     |     |     | 4 users     | can also | display | messages, |         | but they  | have      | no higher  |
prioritythanfreeusers:thecellsforthisfunctionalityandthese
|     |     |     |     |     |     |     |     | priority    | levels | (3 and | 4) are | empty, so | they      | can’t overtake | the         |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------ | ------ | --------- | --------- | -------------- | ----------- |
|     |     |     |     |     |     |     |     | access from | the    | free   | users. | On the    | contrary, | free           | users can’t |
usethedoorlock(theircellisempty),soDeniscandoactions
|     |     |     |     |     |     |     |     | (close the | door) | that | free users | can’t | do. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ---- | ---------- | ----- | --- | --- | --- |
B. SALT
|           |        |                |          |           |           |          |                 | SALT        | [6] is | our modified |      | transducer-based |       | language | used    |
| --------- | ------ | -------------- | -------- | --------- | --------- | -------- | --------------- | ----------- | ------ | ------------ | ---- | ---------------- | ----- | -------- | ------- |
| Figure    | 3. The | Security layer | controls | all       | access to | and from | the transducer  |             |        |              |      |                  |       |          |         |
|           |        |                |          |           |           |          |                 | to describe | the    | control      | flow | running          | on an | object.  | SALT is |
| analyser. | The    | object’s owner | has      | a secured | access    | to the   | Security layer, | in          |        |              |      |                  |       |          |         |
ordertosetrulesandusers’priority.Then,eachtimeatransducer(installed now version 2 in order to take into account the new events
byanyuseronthisobject)triestoaccessaactuatingfunctionalityorwaitfor
thatmayoccurbecauseofthemulti-tenancyextension.Legacy
anincomingmessagefromasensor,thesecuritylayercheckshispriority.It
canthengrant/denyaccessandforward/destroythemessage. transducers, written in SALT version 1 (as defined in previous
|     |     |     |     |     |     |     |     | papers), | must    | still be | executable | on     | the new   | version         | of our |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | -------- | ---------- | ------ | --------- | --------------- | ------ |
|     |     |     |     |     |     |     |     | virtual  | machine | D-LITe.  | The        | orders | to access | functionalities |        |
a new REST endpoint is created for him. When this user are still the same. Legacy SALT transducers can access orders
DELETE his transducer, the REST endpoint is removed. under the control of the new access control Security Service.
|     | Accessing | the security | service |     | is done | through | a specific |     |     |     |     |     |     |     |     |
| --- | --------- | ------------ | ------- | --- | ------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Butinthecaseofablockingorder,thelegacytransducerstays
REST endpoint as illustrated in Figure 3, and reserved to stuck until the higher-priority user release the functionality.
the object owner (authenticated by his XMPP credentials). InSALT version2,theblockingstatecanbeavoidedbythe
The owner will DELETE rules and PUT new access rules introduction of two new events. The "accessDenied" event is
describing his settings. generatedwhenatransducerinvokesanorderprotectedbythe
Table I shows an example of a classification defined by accesscontrollistandalreadyinusebyahigher-priorityuser.
the object’s owner. Each user of this Object is categorised The transducer can describe what to do when receiving this
and his priority is set. For example, Alice and Carol have event(seeFigure2),sothecontrolflowwillnotbeblockedin
an higher priority than Denis. These rules are defined by the this state. The "ControlLost" event is automatically generated
object’s owner, can be modified at any time, and are used by bythesecuritylayerwhenanhigher-priorityusertakescontrol
the security layer in order to grant or deny access to each ofafunctionalitythatwaspreviouslyunderthecontrolofthis
functionality. The access rules are defined in Table II for transducer. For example, an employee has closed his door,
object’ functionalities. Each authorised order is indicated for but the fire alarm (with higher priority) starts an evacuation
each priority level. exercise. The "ControlLost" event describes the alternative
According to Table I and Table II, locking the door can be control flow to be executed by the Transducer.
|     |     |     |     |     |     |     |     | These          | two | new events      | give | our virtual | machine  |      | an upward |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------------- | ---- | ----------- | -------- | ---- | --------- |
|     |     |     |     |     |     |     |     | compatibility. |     | New transducers |      | handle      | blocking | case | a-priori  |
TableI (when the access is denied to the control flow). Losing
USERS’LISTANDPRIORITY
|      |           |           |             |           |           |      |                  | the control       | of       | a functionality |     | is proposed |               | as an a-posteriori |           |
| ---- | --------- | --------- | ----------- | --------- | --------- | ---- | ---------------- | ----------------- | -------- | --------------- | --- | ----------- | ------------- | ------------------ | --------- |
|      |           |           |             |           |           |      |                  | handler,          | in order | to inform       |     | the user    | of that       | lost, for          | example.  |
|      | Owner     | Priority1 | Priority2   |           | Priority3 |      | Priority4        |                   |          |                 |     |             |               |                    |           |
|      |           |           |             |           |           |      |                  | The multi-tenancy |          | extension       |     | has a       | limited       | impact             | over the  |
|      | Bob       | —         | Alice,Carol |           | Denis     |      | —                |                   |          |                 |     |             |               |                    |           |
| This | object is | owned by  | Bob. Bob    | has given | priority  | 2 to | Alice and Carol, |                   |          |                 |     |             |               |                    |           |
|      |           |           |             |           |           |      |                  | language,         | as it    | respects        | the | previous    | event-centric |                    | approach. |
andpriority3toDenis.Allotherswillhavenoaccessatall,exceptforfree
Theadditionofalimitednumberofneweventsgivesasimple
functionalities.
solutiontointegratenewandimprovedtransducers,takinginto
|     |     |     |     |     |     |     |     | account | the Security |     | layer responses. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ---------------- | --- | --- | --- | --- |
TableII
ACCESSRULES
|          |          |            |            |        |        |        |      | C. Hardware |     | interactions | with    | the Virtual |     | Machine |           |
| -------- | -------- | ---------- | ---------- | ------ | ------ | ------ | ---- | ----------- | --- | ------------ | ------- | ----------- | --- | ------- | --------- |
|          | Function | Level1     |            | Level2 | Level3 | Level4 | Free |             |     |              |         |             |     |         |           |
|          |          |            |            |        |        |        |      | Extending   |     | our Virtual  | Machine | D-LITe      |     | [4] to  | cope with |
| Doorlock |          | close,lock | close,lock |        | close  |        | — —  |             |     |              |         |             |     |         |           |
Displayer clear,display display — — display Multi-tenant has some impacts over it. First, new users must
| The | door lock | is under | the control | of the | security | layer. | Depending of the |         |           |       |             |     |        |         |            |
| --- | --------- | -------- | ----------- | ------ | -------- | ------ | ---------------- | ------- | --------- | ----- | ----------- | --- | ------ | ------- | ---------- |
|     |           |          |             |        |          |        |                  | be able | to deploy | their | transducers |     | in the | object. | The access |
transducer’sowner,thepriorityissetforthedifferentactions(lockthedoor,
controlisdonethroughXMPP.Infacts,theusergetanaccess
| or  | display a | messagein | the door’displayer) |     | described | foreach | level. Users |     |     |     |     |     |     |     |     |
| --- | --------- | --------- | ------------------- | --- | --------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
priorityisdefinedinTableI. to an object through its pub-sub XMPP account. That access
Authorized licensed use limited to: Institut Teknologi Bandung. Downloaded on July 29,2024 at 16:13:08 UTC from IEEE Xplore.  Restrictions apply.

is given by the XMPP server, following the identification of ofconflict,eventsaresentandhelptoprogramalternativesfor
the requester and the friendship with the object’s owner. Each each user. This paper describes our modified architecture for
time a new user gets an access to the object, a new endpoint this purpose, with an upward compatibility with the previous
is created for him. Then, he can deploy his transducer, and work. In future works, we will concentrate on the different
the transducer can be discovered by any other object of his portsofthevirtualmachineandtheimpactintermofmemory
| application. |          |     |            |          |     |                 |     | and processing | overhead. |     |     |     |     |     |     |
| ------------ | -------- | --- | ---------- | -------- | --- | --------------- | --- | -------------- | --------- | --- | --- | --- | --- | --- | --- |
| Incoming     | messages |     | (the input | alphabet | of  | the transducer) |     |                |           |     |     |     |     |     |     |
REFERENCES
| are hardware | sensing |     | message | or event | sent | by other | objects |     |     |     |     |     |     |     |     |
| ------------ | ------- | --- | ------- | -------- | ---- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
of the whole application. These other objects send event [1] Python-on-a-chip. https://code.google.com/p/python-on-a-chip/.
|            |              |      |          |           |             |          |         | [2] F.Aslam,C.Schindelhauer,G.Ernst,D.Spyra,J.Meyer,andM.Za- |             |           |        |                |     |            |     |
| ---------- | ------------ | ---- | -------- | --------- | ----------- | -------- | ------- | ------------------------------------------------------------ | ----------- | --------- | ------ | -------------- | --- | ---------- | --- |
| trough the | pub-sub      | XMPP | account, | so        | they arrive | on the   | right   |                                                              |             |           |        |                |     |            |     |
|            |              |      |          |           |             |          |         | lloom.                                                       | Introducing | takatuka: | A java | virtualmachine |     | for motes. | In  |
| endpoint.  | For hardware |      | incoming | messages, |             | they are | sent by |                                                              |             |           |        |                |     |            |     |
Proceedingsofthe6thACMConferenceonEmbeddedNetworkSensor
Systems,SenSys’08,pages399–400,NewYork,NY,USA,2008.ACM.
| the security | service | to        | all the | transducers    | that | are authorized |        |                                         |              |          |             |     |                          |                |     |
| ------------ | ------- | --------- | ------- | -------------- | ---- | -------------- | ------ | --------------------------------------- | ------------ | -------- | ----------- | --- | ------------------------ | -------------- | --- |
|              |         |           |         |                |      |                |        | [3] N.Brouwers,K.Langendoen,andP.Corke. |              |          |             |     | Darjeeling,afeature-rich |                |     |
| to access    | them.   | Depending | on      | the transducer |      | running        | at the |                                         |              |          |             |     |                          |                |     |
|              |         |           |         |                |      |                |        | vm for                                  | the resource | poor. In | Proceedings | of  | the 7th                  | ACM Conference |     |
moment, action are executed if a transition for this event has onEmbeddedNetworkedSensorSystems,SenSys’09,pages169–182,
NewYork,NY,USA,2009.ACM.
| been set | for the | current | state | of the transducer. |     |     |     |                  |     |                 |     |         |        |                 |     |
| -------- | ------- | ------- | ----- | ------------------ | --- | --- | --- | ---------------- | --- | --------------- | --- | ------- | ------ | --------------- | --- |
|          |         |         |       |                    |     |     |     | [4] S. Cherrier, | Y.  | Ghamri-Doudane, | S.  | Lohier, | and G. | Roussel. D-lite | :   |
Outputmessagesaregeneratedbythetransducer,andarein
|             |        |          |      |            |     |          |         | Distributedlogicforinternetofthingsservices. |          |           |          |        | InIEEEInternational |        |       |
| ----------- | ------ | -------- | ---- | ---------- | --- | -------- | ------- | -------------------------------------------- | -------- | --------- | -------- | ------ | ------------------- | ------ | ----- |
| destination | of the | hardware | (for | actuation) | or  | to other | objects |                                              |          |           |          |        |                     |        |       |
|             |        |          |      |            |     |          |         | Conferences                                  | Internet | of Things | (iThings | 2011), | pages               | 16–24. | IEEE, |
2011.
(tomakethemreact).Hardwaremessagesarecontrolledbythe
|          |              |       |      |              |     |               |     | [5] S. Cherrier, | Y.  | Ghamri-Doudane, | S.  | Lohier, | and G. Roussel. | Services |     |
| -------- | ------------ | ----- | ---- | ------------ | --- | ------------- | --- | ---------------- | --- | --------------- | --- | ------- | --------------- | -------- | --- |
| security | layer before | their | real | transmission | to  | the hardware. |     |                  |     |                 |     |         |                 |          |     |
CollaborationinWirelessSensorandActuatorNetworks:Orchestration
If they are not authorised (because of the control access rules, versus Choreography. In 17th IEEE Symposium on Computers and
Communications(ISCC’12),page8pp,Cappadocia,Turquie,July2012.
| or because | the | functionality |     | is currently | used | by a | higher- |                  |     |                 |     |         |        |          |       |
| ---------- | --- | ------------- | --- | ------------ | ---- | ---- | ------- | ---------------- | --- | --------------- | --- | ------- | ------ | -------- | ----- |
|            |     |               |     |              |      |      |         | [6] S. Cherrier, | Y.  | Ghamri-Doudane, | S.  | Lohier, | and G. | Roussel. | SALT: |
priorityuser),theorderisblocked.A"accessDenied"eventis
|     |     |     |     |     |     |     |     | a simple | application | logic | description | using | transducers | for internet |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ----- | ----------- | ----- | ----------- | ------------ | --- |
senttotheinputofthetransducer,incaseithasatransitionto of things. In IEEE International Conference on Communications
handleblockingcase.Iftheaccessisgranted,thenthesecurity - Communication Software and Services Symposium (ICC’13 CSS),
Budapest,Hungary,June2013.
service stores the user’s id and the order currently controlling [7] S. Cherrier and Y. M. Ghamri-Doudane. The "object-as-a-service"
the functionality. This is useful when the transducer frees paradigm. In Global Information Infrastructure and Networking Sym-
the resource, or if another access is requested from another posium(GIIS),2014,pages1–7.IEEE,2014.
|     |     |     |     |     |     |     |     | [8] P.LevisandD.Culler.Maté:Atinyvirtualmachineforsensornetworks. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
transducer running in the same object. In that case, the rules InACMSigplanNotices,volume37,pages85–95.ACM,2002.
of the order, the priority of each user are compared, and a [9] P.Levis,S.Madden,J.Polastre,R.Szewczyk,K.Whitehouse,A.Woo,
D.Gay,J.Hill,M.Welsh,E.Brewer,etal.Tinyos:Anoperatingsystem
decisionistakenbythesecuritylayer.Ifourcurrenttransducer
|           |         |                 |     |       |         |               |     | forsensornetworks. |     | InAmbientintelligence,pages115–148.Springer, |     |     |     |     |     |
| --------- | ------- | --------------- | --- | ----- | ------- | ------------- | --- | ------------------ | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
| loses its | access, | a "controlLost" |     | event | is sent | to its input. | The |                    |     |                                              |     |     |     |     |     |
2005.
user’s id and the order of the higher-priority user are stored [10] K.-J.Lin,N.Reijers,Y.-C.Wang,C.-S.Shih,andJ.Y.Hsu. Building
|                 |     |        |     |     |     |     |     | smartm2mapplicationsusingthewukongprofileframework. |     |     |     |     |     | InGreen |     |
| --------------- | --- | ------ | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- |
| in the security |     | layer. |     |     |     |     |     |                                                     |     |     |     |     |     |         |     |
ComputingandCommunications(GreenCom),2013IEEEandInternet
V. of Things (iThings/CPSCom), IEEE International Conference on and
CONCLUSION
IEEECyber,PhysicalandSocialComputing,pages1175–1180.IEEE,
| In our   | decentralised |     | architecture, | users        | or organisations |               | can      | 2013.                                 |                                                |                  |       |                          |      |                |     |
| -------- | ------------- | --- | ------------- | ------------ | ---------------- | ------------- | -------- | ------------------------------------- | ---------------------------------------------- | ---------------- | ----- | ------------------------ | ---- | -------------- | --- |
|          |               |     |               |              |                  |               |          | [11] R.Müller,G.Alonso,andD.Kossmann. |                                                |                  |       | Avirtualmachineforsensor |      |                |     |
| propose  | an access     | to  | their objects |              | and give         | their         | friends, |                                       |                                                |                  |       |                          |      |                |     |
|          |               |     |               |              |                  |               |          | networks.                             | InProceedingsofthe2NdACMSIGOPS/EuroSysEuropean |                  |       |                          |      |                |     |
| citizens | or employees  |     | the ability   | to integrate |                  | shared things |          | in                                    |                                                |                  |       |                          |      |                |     |
|          |               |     |               |              |                  |               |          | Conference                            | on                                             | Computer Systems | 2007, | EuroSys                  | ’07, | pages 145–158, |     |
their own applications. Sharing Things in such an architecture NewYork,NY,USA,2007.ACM.
|          |           |         |     |           |               |     |          | [12] C.Peltz.Webservicesorchestrationandchoreography.Computer,pages |     |     |     |     |     |     |     |
| -------- | --------- | ------- | --- | --------- | ------------- | --- | -------- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| leads to | conflicts | between | all | the users | that interact |     | with the |                                                                     |     |     |     |     |     |     |     |
46–52,2003.
hardware.Inthispaper,weproposeanarchitecturethatisable
|     |     |     |     |     |     |     |     | [13] D.Simon,C.Cifuentes,D.Cleal,J.Daniels,andD.White.Java&#8482; |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
to solve these issues. Using the user credentials, a priority on the bare metal of wireless sensor devices: The squawk java virtual
machine.InProceedingsofthe2NdInternationalConferenceonVirtual
| definition, | and | an access | list, each | object | grant | or deny | access |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | ---------- | ------ | ----- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ExecutionEnvironments,VEE’06,pages78–88,NewYork,NY,USA,
| tothedifferentusersinregardoftheownerdefinition.Incase |     |     |     |     |     |     |     | 2006.ACM. |     |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Institut Teknologi Bandung. Downloaded on July 29,2024 at 16:13:08 UTC from IEEE Xplore.  Restrictions apply.