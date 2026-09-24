# Developing Small Size Low-Cost

> Source file: `Developing Small Size Low-Cost.pdf`

---

Developing Small Size Low-Cost
fi
Software-De ned Networking Switch
Using Raspberry Pi
Vipin Gupta, Karamjeet Kaur and Sukhveer Kaur
Abstract Software-defined networking (SDN) is a new emerging technology for
networking that separates the forwarding and control plane. With SDN static,
inflexible and complex network are replaced by dynamic, scalable, and innovative
networks.Themotivationofdevelopinglow-costportableSDNswitcharosewhen
we were developing load balancing and stateful firewall SDN applications during
our research work. To test and measure the performance of our applications, we
needed low-cost SDN testbed. Existing solutions were utilizing special hardware
suchasNetFPGAorrealswitches.Butthesewerenotsuitableduetohighcostsand
complexity involved. We could have tested these applications using Mininet
emulator but there are performance issues. In this paper, we created a small size,
lowcost,portableSDNswitchfortestingourSDNapplicationsusingRaspberryPi.
Our low-cost switch supports OpenFlow Specification 1.0–1.4. Raspberry Pi is
Linux-based small size low-cost device which can be used as a personal computer
as well as for making low-cost portable SDN switch.
(cid:1) (cid:1) (cid:1) (cid:1)
Keywords Open vSwitch OpenFlow Raspberry Pi SDN Controller
1 Introduction
Computer network consists of a large number of network devices such as routers,
switches, and various middleboxes such as firewalls, load balancers, network
address translators having complex protocols on them. Network operators are
V.Gupta
U-NetSolutions,Moga,Punjab,India
e-mail:vipin2411@gmail.com
K.Kaur(&)(cid:1)S.Kaur
ADCollege,Dharamkot,Punjab,India
e-mail:bhullar1991@gmail.com
S.Kaur
e-mail:bhullarsukh96@gmail.com
©SpringerNatureSingaporePteLtd.2018 147
D.K.Lobiyaletal.(eds.),Next-GenerationNetworks,AdvancesinIntelligent
SystemsandComputing638,https://doi.org/10.1007/978-981-10-6005-2_16

148 V.Guptaetal.
responsible for configuring individual network devices using configuration
interface.
Software-definednetworkingisanewnetworkingconceptinwhichthedataplane
isdecoupledfromcontroldecisionplane[1].Dataplanesareactuallydumbmerchant
silicon boxes. We can turn them into a simple hub, learning switch, or a router by
creating flow entries in flow tables. SDN in part represents logically centralized
network intelligence in control plane and data plane become simple packet for-
wardingdevicethatcanbeprogrammedviaopeninterface.OpenFlowisaprominent
example of such an interface [2, 3]. OpenFlow switch has flow tables that contain
packet handling rules. When a rule matches with the incoming traffic, then corre-
spondingactionsuchasdropping,forwarding,andfloodingistaken.Accordingtothe
flowtablerules,OpenFlowswitchbehaveslikeaswitch,router,hub,orfirewall[4].
SDN is getting a lot of attention from research community as well as industry
[5]. Open network foundation (ONF) has been created for promoting SDN and
standardizes the OpenFlow (Fig. 1).
Fig.1 SDNarchitecture

DevelopingSmallSizeLow-CostSoftware… 149
| 2 Related | Work |     |     |
| --------- | ---- | --- | --- |
Mininet[6,7]isaemulatorsoftwarethatenablesyouincreatinglargenetworkson
a simple laptop or virtual machine (VM). It allows you to create simple as well
complexnetworkingconsistingofswitches,controllers,hosts,andlinks.Itprovides
a simple, robust mechanism for testing OpenFlow applications. But there are
scalabilityissuesandresourceconstraintswhenwerunMininetonasinglesystem.
ManyotherresearchersusespecialdevicessuchasNetFPGAforcreatingtestbeds.
But these SDN testbeds are not suitable due to higher cost and complexity [8].
EarlierworksupportedOpenFlowspecification1.0[9],whileincaseofourwork,it
|     | Specification | 1.0–1.4. |     |
| --- | ------------- | -------- | --- |
supports OpenFlow
Raspberry Pi is small size low-cost device which can be used as personal
computer as well as for making low-cost SDN switch. Raspberry Pi is basically a
| device using | embedded Linux. |            |     |
| ------------ | --------------- | ---------- | --- |
| 3 Steps      | for Developing  | SDN Switch |     |
Our switch was made using Raspberry Pi which comes preloaded with Raspbian
operatingsystem.Forourswitch,weusedlatestRaspberryPimodelB+whichalso
comeswith1 GBRaminstead of512 MBRaminearlier versions. TheRaspberry
Pi is a small, powerful, and lightweight ARM-based computer [9]. We loaded the
latestUbuntuMATE15.04onRaspberryPi.RaspberryPicontains onlyoneLAN
card. Since we wanted four ports SDN switch, so we ordered three USB-based
low-cost LAN cards online. The following are the steps for converting our
| Raspberry | Pi system to a SDN | switch. |     |
| --------- | ------------------ | ------- | --- |
1. Attached three USB LAN cards to our Raspberry Pi system thus making total
| number | of LAN cards available | to four. |     |
| ------ | ---------------------- | -------- | --- |
2. We downloaded a pre-built image of Ubuntu MATE which is available on the
file
Internet[10]. We unzipped that image and wrote the Ubuntu MATE image
fileonMicroSDcardthatcomesalongwithRaspberryPisystem.Itremovedthe
default Raspbian image on MicroSD. We removed the Raspbian OS because it
does not support the latest version of OpenFlow switch (Fig. 2).
3. We used the ‘apt-get install’ for installing the Open vSwitch packages on
| Raspberry | Pi. |     |     |
| --------- | --- | --- | --- |
4. Weusedthe‘óvs-vsctl’formakingourRaspberryPiasSDNswitchandadded
| four LAN | cards as four | ports of our SDN | switch. |
| -------- | ------------- | ---------------- | ------- |
5. We attached four laptops to four ports of our Raspberry Pi SDN switch. One
laptop was used as client system, one laptop as POX/RYU controller and two
| other | laptops as servers. |     |     |
| ----- | ------------------- | --- | --- |
6. First, we tested our load balancing application using POX controller [11, 12].
Our Raspberry Pi switch was properly working as a load balancer.

| 150 |     |     |     |     |     |     | V.Guptaetal. |
| --- | --- | --- | --- | --- | --- | --- | ------------ |
Fig.2 RaspberryPi-basedSDNlaboratory
7. Secondly,wetestedourfirewallapplicationusingRYUcontroller[13,14].Our
| Raspberry    | Pi  | switch was | now | properly working | as firewall. |     |     |
| ------------ | --- | ---------- | --- | ---------------- | ------------ | --- | --- |
| 4 Laboratory |     | Setup      |     |                  |              |     |     |
Fortestingourswitch,wecreatedthelaboratoryasshownfigure.Ourswitchports
were named eth0, eth1, eth2, eth3. We attached our POX controller on eth0 and
hostsoneth1,eth2, andeth3 ports.Wetested ourRaspberryPi-basedSDNswitch
using load balancing application and firewall application (Fig. 3).
The load balancing architecture consists of OpenFlow switch network with a
POXcontrollerandmultipleserversconnectedtotheportsoftheOpenFlowswitch.
EachserverisassignedstaticIPaddress,andthePOXcontrollermaintainsalistof
liveserversthatareconnectedtotheOpenFlowswitch.Webservice isrunningon
| each server | on a   | well-known | port      | 80.      |          |          |             |
| ----------- | ------ | ---------- | --------- | -------- | -------- | -------- | ----------- |
| firewall    |        |            |           | specific |          | firewall |             |
| A           | allows | or         | rejects a | type     | of data. | Our      | application |
traffic
allows or restricts the based on MAC addresses (Layer 2), source and des-
tination IP addresses (Layer 3), ports (Layer 4). When a packet enters into the
firewall
| switch, the | packet | header | is matched | against the | rules. |     |     |
| ----------- | ------ | ------ | ---------- | ----------- | ------ | --- | --- |

DevelopingSmallSizeLow-CostSoftware… 151
Fig.3 Laboratorysetup
Fig.4 Switchportsfor
connectinghosts
We tested our load balancing application using POX controller installed on
‘172.24.0.81’host.FirewallapplicationwastestedusingRyucontrollerinstalledon
‘172.24.0.81’.RaspberryPiSDNswitchwasconfiguredtouseremotecontrolleras
shown in figure. Both of these applications are working properly on Raspberry
Pi-based SDN switch (Fig. 4).

152 V.Guptaetal.
5 Conclusion
Here we have successfully developed a SDN switch using Raspberry Pi by
installing Ubuntu MATE Linux and other open source softwares. We were able to
successfully test our load balancing and firewall applications. This switch is very
low cost and portable as compared to other available alternatives in the market.
Future work can involve creating a SDN testbed consisting of Raspberry-based
switches and hosts.
References
1. Mendonca, M., Nunes, B.A.A., Nguyen, X.N., Obraczka, K., Turletti, T.: A Survey of
Software-DefinedNetworking:Past,Present,andFutureofProgrammableNetworks(2013)
2. McKeown, N., Anderson, T., Balakrishnan, H., Parulkar, G., Peterson, L., Rexford, J.,
Shenker, S., Turner, J.: OpenFlow: enabling innovation in campus networks.
ACMSIGCOMMComput.Commun.Rev.38(2),69–74(2008)
3. Hegr, T., Bohac,L., Uhlir, V., Chlumsky,P.:OpenFlow deployment and conceptanalysis.
Adv.Electr.Electron.Eng.11(5),327–335(2013)
4. Lara, A., Kolasani, A., Ramamurthy, B.: Network Innovation Using Openflow: A Survey,
pp.1–20(2013)
5. Feamster, N., Rexford, J., Zegura, E.: The road to SDN: an intellectual history of
programmablenetworks.ACMSIGCOMMComput.Commun.Rev.44(2),87–98(2014)
6. Handigol, N., Heller, B., Jeyakumar, V., Lantz, B., McKeown, N.: Reproducible network
experiments using container-based emulation. In: Proceedings of the 8th International
Conference on Emerging Networking Experiments and Technologies, pp. 253–264. ACM
(2012)
7. Lantz, B., Heller, B., McKeown, N.: A network in a laptop: rapid prototyping for
software-definednetworks. In:Proceedings ofthe9thACM SIGCOMM Workshop onHot
TopicsinNetworks,p.19.ACM(2010)
8. Naous,J.,Erickson,D.,AdamCovington,G.,Appenzeller,G.,McKeown,N.:Implementing
an OpenFlow switch on the NetFPGA platform. In: Proceedings of the 4th ACM/IEEE
SymposiumonArchitecturesforNetworkingandCommunicationsSystems,pp.1–9.ACM
(2008)
9. Kim, H., Kim, J., Ko,Y.-B.: Developing acost-effective OpenFlow testbed for small-scale
software defined networking. In: 2014 16th International Conference on Advanced
CommunicationTechnology(ICACT),pp.758–761.IEEE(2014)
10. https://ubuntu-mate.org/raspberry-pi/
11. Kaur,S.,Singh,J.,Ghumman,N.S.:NetworkProgrammabilityUsingPOXController
12. POXathttps://openflow.stanford.edu/display/ONL/POX+Wiki
13. Shalimov, A., Zuikov, D., Zimarina, D., Pashkov, V., Smeliansky, R.: Advanced study of
SDN/OpenFlowcontrollers.In:Proceedingsofthe9thCentral&EasternEuropeanSoftware
EngineeringConferenceinRussia,p.1.ACM(2013)
14. Lin, T., Kang, J.-M., Bannazadeh, H., Leon-Garcia, A.: Enabling SDN applications on
software-defined infrastructure. In: Network Operations and Management Symposium
(NOMS),2014IEEE,pp.1–7.IEEE(2014)