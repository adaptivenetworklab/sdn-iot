# An Intelligent fuzzy based system for handover decision in 5G-Iot network

> Source file: `An Intelligent fuzzy based system for handover decision in 5G-Iot network.pdf`

---

InternetofThings23(2023)100870
ContentslistsavailableatScienceDirect
InternetofThings
journalhomepage:www.elsevier.com/locate/iot
Anintelligentfuzzy-basedsystemforhandoverdecisionin5G-IoT
networksconsideringnetworkslicingandSDNtechnologies
PhuditAmpririta,∗,ShunyaHigashia,ErmioniQafzezib,MakotoIkedab,
KeitaMatsuob,LeonardBarollib
aGraduateSchoolofEngineering,FukuokaInstituteofTechnology(FIT),3-30-1Wajiro-Higashi,Higashi-Ku,Fukuoka,811-0295,Japan
bDepartmentofInformationandCommunicationEngineering,FukuokaInstituteofTechnology(FIT),3-30-1Wajiro-Higashi,Higashi-Ku,
Fukuoka,811-0295,Japan
A R T I C L E I N F O A B S T R A C T
Keywords: By enabling 5G technology, IoT networks can improve the performance of connected IoT
5G devices. However, handover, ping-pong effect and load balancing are critical issues because
SDN of massive and unplaned deployment of small cells. The handover operation in 5G wireless
Handover networks is complicated because there are many radio access techniques and technologies.
Networkslicing
Therefore,themobilitymanagementisrequiredtoprovideQoSforvariousapplications.Inthis
IoT
paper,wepresentafuzzy-basedsystemforhandoverdecisionin5Gwirelessnetworksconsid-
eringdifferentnetworkslicingparameters.WeimplementtwoFuzzy-basedHandoverDecision
Models (FHDM): FHDM1 and FHDM2. We evaluate the proposed models by simulations. For
FHDM1,SliceDelay(SD),SliceBandwidth(SB),andSliceLoad(SL)arethreeinputparameters
and Handover Decision (HD) is the output parameter. For FHDM2, Slice Reliability (SR) is a
newconsideredparameter,soithasfourinputparametersandtheoutputparameterisHDthe
sameasFHDM1.Wefoundfromsimulationresultsthattheconsideredparametershavedifferent
effectsonHD.Forbothmodels,theHDvalueincreasesasSDandSLvaluesincreasewhileHD
valueisdecreasingwhenSBandSRvaluesincrease.Theresultsofthesimulationindicatethat
although FHDM2 is more complex than FHDM1, it performs better HD since considers four
input parameters. From the simulation results of FHDM2, when we changed SD value form
10%to90%,wefoundthattheHDvalueisincreasedby50%whenSRis50%andSLis90%.
ThisindicatesthatwhenauserisconnectingwiththepresentslicethathasbadQoS,itshould
handovertoanotherslicewithbetterQoS.
1. Introduction
The5thGeneration(5G)mobilecommunicationisbecomingchallengingandcomplicatedbytherapidgrowthofmobiledevices.
Therefore,thedevelopmentofnetworktechnologiesandnetworkdevicesareexpectedtosatisfyusersQualityofService(QoS)[1–
4].MobilitymanagementisthecriticaloperationforimprovingQoSandprovidinguninterruptedservicestouserson5Gwireless
networks. Also, users require a seamless handover with high efficiency, low latency, and high data rates when they move with
differentmobility[5].
∗ Correspondingauthor.
E-mailaddresses: bd21201@bene.fit.ac.jp(P.Ampririt),mgm23108@bene.fit.ac.jp(S.Higashi),qafzezi@bene.fit.ac.jp(E.Qafzezi),makoto.ikd@acm.org
(M.Ikeda),kt-matsuo@fit.ac.jp(K.Matsuo),barolli@fit.ac.jp(L.Barolli).
https://doi.org/10.1016/j.iot.2023.100870
Received30March2023;Receivedinrevisedform14June2023;Accepted4July2023
Availableonline10July2023
2542-6605/©2023ElsevierB.V.Allrightsreserved.

P.Ampriritetal. InternetofThings23(2023)100870
NetworkSlicing(NS)isa5Gwirelessnetworktechnologyusedtomeetconsumers’QoSdemands.TheNSisauniquetechnology
thatcreatesnewapplicationservicesoverthesamephysicalinfrastructureutilizingSoftware-DefinedNetworks(SDNs)andNetwork
FunctionVirtualization(NFV).Itcansupportdependablenetworkservicesondemandwithlessresourceusage.Therefore,theNS
isveryimportantforhandoverin5Gwirelessnetworks.Inter-slicehandoverisanewtypeofhandoverthatconsidermultipleslice
servicesratherthanjusttheUserEquipment(UE)physicalmobilitywhenperforminghandover[6].
Because traditional networks have complicated reconfiguration and they are difficult to manage, SDN is one of the new
approaches that can improve network performance to face new difficulties and challenging problems in 5G wireless networks.
Therearemanyissuesanduserdemands,thereforetechnologiessuitablefor5Gwirelessnetworksneedtobedeveloped.
Designingandengineering5Gwirelessnetworksisnotaneasytaskbecauserequiretheoptimizationofmanyparameters.In[7],
theauthorsdesignaframeworkconsideringNSforultra-lowlatencyscenarios.However,theseparametersareoftenuncorrelated
andthereforeatrade-offonthesolutionsisrequiredintheoptimizationprocess.Theseparametersincludeconnectivity,coverage,
Quality of Service (QoS), the network cost and so on. Also, there are different approaches for traffic control and engineering in
5GwirelessnetworkssuchasCallAdmissionControl(CAC),SelectionofRadioAccessTechnologies(RATc)andhandover.During
theseprocesses,therearemorethantwouncorrelatedparametersforoptimization,thustheproblembecomesanNP-hardproblem,
whichisaproblemthatcannotbesolvedinpolynomialtime.Recently,therearedifferentapproachessuchasmachinelearning,
AI,softcomputingandevolutionary-basedalgorithmswhicharecapableofsolvingNP-hardproblems.
Inourpreviouswork[8–10],wepresentedsomeFuzzy-basedsystemsforCACin5Gwirelessnetworks.Inordertomakethe
handoverdecisionin5Gwirelessnetworksarerequiredmanyuncorrelatedparameters,whichmakestheproblemNP-Hard.Also,
the decision should be done in real-time. For this reason, intelligent and heuristic approaches should be considered. Therefore,
inthispaper,weproposeaFuzzy-basedHandoverDecisionSystem(FHDS).WepresentandcomparetwoFuzzy-basedHandover
DecisionModels(FHDMs):FHDM1andFHDM2.TheFHDM1considersthreeparametersandFHDM2considersfourparametersby
addingSliceReliability(SR)asanewparameter.
Thecontributionsofthisworkareasfollows.
• Weinvestigatedandproposeddifferentparametersforhandoverdecisionin5Gwirelessnetworks.
• Weproposeandimplementanintelligentsystemforhandoverdecisionin5GwirelessnetworksbasedonFL.
• Weimplementtwomodelstoevaluatetheproposedsystem.
• Wecomparethesimulationresultsforbothmodelsfordifferentscenarios.
• FHDS2canprovidebetterhandoverdecision,becauseitconsiders4inputparameters.
The rest of the paper is organized as follows. Section 2 present Related Work. In Section 3, we introduce 5G-IoT networks. A
description of SDN is provided in Section 4. Network Slicing is presented in Section 5. We introduce a short overview of FL in
Section6.InSection7,wepresenttheproposedfuzzy-basedsystemanditsmodels.InSection8,wediscussthesimulationresults
oftwomodels.Section9givesconclusionsandfuturework.
2. Relatedwork
In this section, we present some of handover related work for SDN and 5G wireless networks. We also present some related
workconsideringnetworkslicingandinter-slicehandovermethods.Inordertohaveaneffectiveinter-slicehandoverprocedure,it
isimportanttochooseanappropriatetargetslicepromptlyandtriggerhandovertothetargetslice.
ManyresearchworksconsidertechnologiessuchasSDN,NFV,FuzzyLogic(FL)andintelligentalgorithms.Forexample,inorder
toreducetheprocessingdelayinthehandoverprocedure,theQoScanbeenhancedbyapplyingFLinSDN[11–13].However,in
these papers, the authors consider only conventional input parameters such as Received Signal Strength (RSS), data transmission
rate,batterychargeorpacketlossrateanddelay.
In[14],theslicesserviceresourcesismaintainedduringhandoverprocedureusingthreeheuristicsalgorithms:SimpleAlgorithm,
GreedyHandoverAlgorithmandIntelligentHandoverAlgorithm.Thehandoverprocedurecanmaintaintherequiredservicesfor
eachsliceandtheavailabilityofsliceswhenthehandoverwillbeactivated.Thehandoverproblemisinvestigatedalsoin[15]using
reinforcementlearningtechniques.TheauthorsmaketheassumptionthataseparatesubsetofBSssupportseachslice.Thegoalis
tominimizethelong-termhandovercostswhilemaintaininguserQoS.ThehandovercostisdefinedfromthecostofswitchingNS,
thecostofswitchingBS,thecostofswitchingBSandNS,thecostofcreatinganewNS.
Fore-Health5GUseCases,in[16],theauthorsintroducedtheCloud-Network-SlicingMobilityControl(CNS-MC)approachto
maintainthem-healthUEexperienceduringmobilityprocedure.
ForV2Xenvironment,theauthorsimplementaV2XSliceSelectionFunction(SSF-V2X)asaSDNapplicationtotriggerinter-slice
handoverbyconsideringservicerequirementsandnetworkconstraints[17].Also,in[18],theauthorsproposedainter/intraslice
handovermanagementarchitecturecalledConnectionModeasAService(CMaaS).TheCMaaScontrollerisusedfortheInter-Slice
HandoverandSkippingModeasAService(SMaaS)isusedfortheIntra-SliceHandovertominimizethehandovercost.
In[19],theauthorsconsiderinter-slicinghandoversecurityandreliability.Theyaddresssecurityflawsin5Gnetworkslicing
fromattackdetectionandlocalizationalgorithmsthatlaunchaDistributedDenialofService(DDoS)duringinter-slicingprocedure
tofindtheweaknessespoint.Duringtheinter-slicehandoverphase,thelengthyauthenticationprocessisabusedtostartaDDoS
assault.
2

P.Ampriritetal. InternetofThings23(2023)100870
Fig.1. 5GIoTchallenging.
Fig.2. ComparisonoftraditionalnetworkandSDN.
3. 5G-IoTnetworks
The number of connected devices is rapidly increasing, including Internet of Things (IoT) devices that cause the increasing
demands of applications [20–22]. By enabling 5G technology, such as SDN, NS, Machine-to-Machine (M2M) communications,
massiveMIMOandmillimeter-wave(mmWave)technologies,IoTnetworkscanimprovetheperformanceandreliabilityofconnected
IoTdevices.Also,5G-IoTdeploymentwillgenerateadiverseformoftraffic,reliability,bitrates,energyconsumption,securityand
privacy for improving Quality of Service (QoS) requirements and achieving massive Machine-Type Communication (mMTC) as
shownFig.1[23].
Recently,manyresearchworksdealwithdesignofsystemsappropriatefor5G-IoTnetworks.OneexampleistheutilizationofNS
formanagingalargenumberofheterogeneousIoTnetworkslicesdynamically[24].Also,5G-IoTinfrastructureimplementSDN/NFV
forimprovingloadbalancing,faulttoleranceandcongestionavoidanceinIoTnetwork[25].Inaddition,massivecommunication
interfacesissues(redundantcommunicationcapabilityproblemandwasteenergy)canbeimprovedby5GmassiveMIMO[26].
4. Software-definednetworks(SDNs)
The SDN can optimize and simplify network operation. SDN implements a SDN controller or a logically centralized network
controlintothenetworkarchitecture.ThetraditionalnetworkandSDNtechniquesarecomparedinFig.2.Thetraditionalnetwork
reliesononlyphysicalinfrastructure,makingmanagementandcontroloftrafficnetworkandnetworkdevicesdifficultandcomplex.
Furthermore, because each device requires its own control and operation, the network configuration is hard to configure and
3

P.Ampriritetal. InternetofThings23(2023)100870
Fig.3. OverviewofSDNarchitecture.
reconfigureallnetworkdevicesquickly.Ontheotherhand,SDNbuildsavirtualizedcontrolplanewithsmartmanagement,when
networkmanagersutilizeavirtualizedcontrollertocontrolandaltertheentirenetwork[27–32].TheSDNstructureisshownin
Fig.3andexplainedinfollowing.
• InfrastructureLayerconsistsofnetworkequipments,suchasswitchesandrouters.ItfollowstheSDNcontroller’scommands
andtransfersdataintonetworkdevices.
• SouthboundInterfacesaretheconnectingbridgesbetweentheInfrastructureLayerandtheControlLayer.OpenFlowisthe
mostwidelyusedandrecognizedprotocolinthisinterface.TheprotocolsenabletheControlLayertodesignnewforwarding
planepolicies.
• Control Layer consists of controllers that receive information or policies from the Application Layer and send analyzed
informationorordertothelowerlayer.
• NorthboundInterfacesoffervariousApplicationProgrammingInterfaces(APIs).
• ApplicationLayergathersnetworkinformationfromthecontrollerfordecision-makingandcreatesaconceptualrepresenta-
tionofthenetwork.
Byenablingnewservices,theSDNcancontrolandimprovethenetworkperformance.TheSDNcanadapttotrafficcongestion
situations,enablinguserstoquicklymanageandallocateresourcesacrossthecontrolplane.Mobilitymanagementbetweenradio
accesstechnologiessuchas5G,4G,andWifibecomessimplerandfaster[33].The5Ghandoverprocedurecanbestraightforward
andthedelaycanbeminimizedbyimplementingSDN[34].Also,SDNhasbeenappliedindifferentnetworkingscenarios,including
commercial and industrial networks. Nevertheless, the complete network architecture must be modified in order to use the SDN
controllerandprotocol.
5. Networkslicing
The NS separates a single hardware service into several logical network services known as ‘‘Slices’’. Thus, the virtual logical
networksareundisturbedfromotherslicesbecauseeachofthemislogicallyindependent.Asaresult,NSprovidesenhancedQoS
andflexibilitytousersservicedemandscomparedtotraditionalnetworks.Inaddition,becauseofthenon-interferingofotherslices,
thesecurityanddependabilityofslicescanbeenhanced[35–38].
TheNextGenerationMobileNetworks(NGMN)isdeveloping5GNSconceptasshowninFig.4.Therearethreeprimarylayers
totheNSprocedure[39–41].
• Service Instance Layer provises end to end services or commercial services offered by an application provider or mobile
networkoperator.
• Network Slice Instance Layer comprises various network resources and functions that give Service Instances, which are
optimizednetworkcharacteristicsbyfollowinguserrequirements.
• ResourceLayerconsistsofbothphysicalandlogicalcomponentsthataremanagedbytheNetworkSliceInstancelayer.
4

P.Ampriritetal. InternetofThings23(2023)100870
Fig.4. NGMNNSconcept.
Fig.5. StructureofFuzzyLogicController(FLC).
6. OverviewofFuzzylogic(FL)
AFLsystemconsiderscompleteintervalstatementsbetweenFalse(0)andTrue(1)todescribehumanreasoningbyconversion
of vector data (input) into scalar data (output). The FL is employed in several systems, including TV picture correction, aviation
control(RockwellCorp.)andSendaisubwayoperating(Sony)[42–44].
Fig.5showsthestructureofFLC,whichhasfourcomponents.
• Fuzzifier converts the crisp input into identical membership values of the relevant fuzzy sets by using the membership
functions.Themembershipfunctionspecifieshowtogenerateagraphbymappingeachpointinthecrispinputswithadegree
ofmembershiprangingfrom0to1.Ingeneral,asingleinputvariablecanbedescribedbymultiplemembershipfunctions.
• FuzzyRulescouldbegivenbyaprofessionalorcanbetakenfromnumericaldata.AsetofIF-THENexpressionscandescribe
theengineeringrules.Forexample,if𝑥and𝑦arelinguisticvariablesdefinedbythefuzzysetsAandB,theexpressionwillbe
‘‘IF𝑥isA,THEN𝑦isB’’.Thecontrol(input)variableiscalled𝑥,whilethesolution(output)variableiscalled𝑦.Conditional
sentences use the form ‘‘IF... THEN’’. It consists of ‘‘IF’’ (also known as the antecedent) and ‘‘THEN’’ (also known as the
resultant).
• Inference Engine uses these rules to compute a fuzzy output (the results). There are many fuzzy logic inferences such as
Mamdanifuzzyinferenceengine,Takagi–Sugenofuzzyinferenceengine,andsoon.
• Defuzzifierconvertsafuzzyoutput(theresult)intoacrispoutput(theoutcome),whichisusedforcontrol.
7. ProposedFuzzy-basedsystem
Inthissection,wepresentourproposedfuzzy-basedsystem.InFig.6,weshowtheoverviewofourproposedsystem.Eachevolve
basestation(eBS)willgetordersfromtheSDNcontroller,allowingthesestationstocommunicateandrelaydatatoUE.Also,each
eBScontainsanumberofsliceswithvariousservices.Bygatheringthedatabasedonnetworktrafficstatus,theproposedFuzzy-
basedsystemimplementedintheSDNcontrollerwillmanageinter-slicehandover.TheSDNcontrollerwillofferacommunication
channelbetweeneBSandthe5Gcorenetwork.
5

P.Ampriritetal. InternetofThings23(2023)100870
Fig.6. Proposedsystemoverview.
Fig.7. Proposedsystemstructure.
TheproposedsystemiscalledFuzzy-basedHandoverDecisionSystem(FHDS)in5GWirelessNetworks.ThestructureofFHDSis
showninFig.7.WeimplementtwoFuzzy-basedHandoverDecisionModels(FHDMs):FHDM1andFHDM2.TheFHDM1considers
three input parameters: Slice Delay (SD), Slice Bandwidth (SB), Slice Load (SL) and the output parameter is Handover Decision
(HD).InFHDM2,weconsiderSliceReliability(SR)asanewparameter.Thus,FHDM2hasfourinputparameters.
Weexplainfourinputparametersandtheoutputparameterinfollowing.
SliceDelay(SD):Highqueueingandnetworkdelayarecausedbytheslicedelay.Also,theimpactofdelaymayleadtorejection
ofdemands,resultinginlowsliceresourceutilization.Asaconsequence,thehandoverprocedureisrequiredtosatisfytheQoS.
Slice Bandwidth (SB): The available bandwidth for a slice is known as slice bandwidth. The bandwidth resources can affect
thenumberofbytesaslicecantransmitatagiventime.TheSBshouldbeassignedaccordingtothechannelvarietyandvarious
bandwidthneedsoftheservicetypesindifferentslices.ThepossibilityofahandoverwilldecreaseastheSBisincreased.
SliceLoad(SL):Aslicebecomesheavilyloadedwhenitsresourcesareheavilyutilizedbyalargenumberofusers.So,theuser
willhandovertoanotherslicewithalowerloadtohavebetterservice.
SliceReliability(SR):TheSRisderivedfromtheerrorratecausedbynetworktrafficcongestionorsomenetworknodefailures.
Theuserwillmakehandovertoalternativesliceswhenaslicehaslowreliability.
HandoverDecision(HD):TheHDparameterisusedformakingthedecisionforthehandoverprocess.Bymanysimulations,
wefoundthat7Levelsaregoodenoughforoursystem,whereHD1indicatestheextremelylowpossibilityofinter-slicinghandover
andHD7indicatestheextremelyhighpossibilityofinter-slicinghandover.
The membership functions are shown in Fig. 8. The proposed fuzzy system can be used in a wide variety of applications. We
use Delay, Bandwidth, Load and Reliability numbers between 0 and 100% to simply fuzzify them. We consider triangular and
trapezoidalmembershipfunctionsbecausetheyaremoreappropriateforreal-timeoperations.Weshowparametersandtheirterm
6

P.Ampriritetal. InternetofThings23(2023)100870
Fig.8. MembershipfunctionsforFHDM1andFHDM2.
Table1
ParameterandtheirtermsetsforFHDM1andFHDM2.
Parameters Termsets
SliceDelay(SD) Short(So),Intermediate(Id),Long(Ln)
SliceBandwidth(SB) Small(Sl),Medium(Mi),Big(Bi)
SliceLoad(SL) Small(Sa),Intermediate(Ir),Large(Le)
SliceReliability(SR) Low(Lw),Medium(Md),High(Hh)
HandoverDecision(HD) HD1,HD2,HD3,HD4,HD5,HD6,HD7
setsinTable1.TheFuzzyRuleBase(FRB)forFHDM1isshowninTable2andhas27rules.While,theFRBforFHDM2isshown
inTable3andhas81rules.
7

| P.Ampriritetal. |     |     |     |     | InternetofThings23(2023)100870 |     |
| --------------- | --- | --- | --- | --- | ------------------------------ | --- |
Table2
FRBforFHDM1.
| Rule | SD SB SL | HD Rule SD | SB SL HD  | Rule SD | SB SL | HD  |
| ---- | -------- | ---------- | --------- | ------- | ----- | --- |
| 1    | So Sl Sa | HD3 10 Id  | Sl Sa HD4 | 19 Ln   | Sl Sa | HD5 |
| 2    | So Sl Ir | HD4 11 Id  | Sl Ir HD5 | 20 Ln   | Sl Ir | HD6 |
| 3    | So Sl Le | HD5 12 Id  | Sl Le HD6 | 21 Ln   | Sl Le | HD7 |
| 4    | So Mi Sa | HD2 13 Id  | Mi Sa HD3 | 22 Ln   | Mi Sa | HD4 |
| 5    | So Mi Ir | HD3 14 Id  | Mi Ir HD4 | 23 Ln   | Mi Ir | HD5 |
| 6    | So Mi Le | HD4 15 Id  | Mi Le HD5 | 24 Ln   | Mi Le | HD6 |
| 7    | So Bi Sa | HD1 16 Id  | Bi Sa HD2 | 25 Ln   | Bi Sa | HD3 |
| 8    | So Bi Ir | HD2 17 Id  | Bi Ir HD3 | 26 Ln   | Bi Ir | HD4 |
| 9    | So Bi Le | HD3 18 Id  | Bi Le HD4 | 27 Ln   | Bi Le | HD5 |
Table3
FRBforFHDM2.
| Rule SD | SB SL | SR HD  | Rule | SD SB | SL  | SR HD  |
| ------- | ----- | ------ | ---- | ----- | --- | ------ |
| 1 So    | Sl Sa | Lw HD4 | 41   | Id Mi | Ir  | Md HD4 |
| 2 So    | Sl Sa | Md HD3 | 42   | Id Mi | Ir  | Hh HD3 |
| 3 So    | Sl Sa | Hh HD2 | 43   | Id Mi | Le  | Lw HD6 |
| 4 So    | Sl Ir | Lw HD5 | 44   | Id Mi | Le  | Md HD5 |
| 5 So    | Sl Ir | Md HD4 | 45   | Id Mi | Le  | Hh HD4 |
| 6 So    | Sl Ir | Hh HD3 | 46   | Id Bi | Sa  | Lw HD3 |
| 7 So    | Sl Le | Lw HD6 | 47   | Id Bi | Sa  | Md HD2 |
| 8 So    | Sl Le | Md HD5 | 48   | Id Bi | Sa  | Hh HD1 |
| 9 So    | Sl Le | Hh HD4 | 49   | Id Bi | Ir  | Lw HD4 |
| 10 So   | Mi Sa | Lw HD3 | 50   | Id Bi | Ir  | Md HD3 |
| 11 So   | Mi Sa | Md HD2 | 51   | Id Bi | Ir  | Hh HD2 |
| 12 So   | Mi Sa | Hh HD1 | 52   | Id Bi | Le  | Lw HD5 |
| 13 So   | Mi Ir | Lw HD4 | 53   | Id Bi | Le  | Md HD4 |
| 14 So   | Mi Ir | Md HD3 | 54   | Id Bi | Le  | Hh HD3 |
| 15 So   | Mi Ir | Hh HD2 | 55   | Ln Sl | Sa  | Lw HD6 |
| 16 So   | Mi Le | Lw HD5 | 56   | Ln Sl | Sa  | Md HD5 |
| 17 So   | Mi Le | Md HD4 | 57   | Ln Sl | Sa  | Hh HD4 |
| 18 So   | Mi Le | Hh HD3 | 58   | Ln Sl | Ir  | Lw HD7 |
| 19 So   | Bi Sa | Lw HD2 | 59   | Ln Sl | Ir  | Md HD6 |
| 20 So   | Bi Sa | Md HD2 | 60   | Ln Sl | Ir  | Hh HD5 |
| 21 So   | Bi Sa | Hh HD1 | 61   | Ln Sl | Le  | Lw HD7 |
| 22 So   | Bi Ir | Lw HD3 | 62   | Ln Sl | Le  | Md HD7 |
| 23 So   | Bi Ir | Md HD2 | 63   | Ln Sl | Le  | Hh HD6 |
| 24 So   | Bi Ir | Hh HD1 | 64   | Ln Mi | Sa  | Lw HD5 |
| 25 So   | Bi Le | Lw HD4 | 65   | Ln Mi | Sa  | Md HD4 |
| 26 So   | Bi Le | Md HD3 | 66   | Ln Mi | Sa  | Hh HD3 |
| 27 So   | Bi Le | Hh HD2 | 67   | Ln Mi | Ir  | Lw HD6 |
| 28 Id   | Sl Sa | Lw HD5 | 68   | Ln Mi | Ir  | Md HD5 |
| 29 Id   | Sl Sa | Md HD4 | 69   | Ln Mi | Ir  | Hh HD4 |
| 30 Id   | Sl Sa | Hh HD3 | 70   | Ln Mi | Le  | Lw HD7 |
| 31 Id   | Sl Ir | Lw HD6 | 71   | Ln Mi | Le  | Md HD6 |
| 32 Id   | Sl Ir | Md HD5 | 72   | Ln Mi | Le  | Hh HD5 |
| 33 Id   | Sl Ir | Hh HD4 | 73   | Ln Bi | Sa  | Lw HD4 |
| 34 Id   | Sl Le | Lw HD7 | 74   | Ln Bi | Sa  | Md HD3 |
| 35 Id   | Sl Le | Md HD6 | 75   | Ln Bi | Sa  | Hh HD2 |
| 36 Id   | Sl Le | Hh HD5 | 76   | Ln Bi | Ir  | Lw HD5 |
| 37 Id   | Mi Sa | Lw HD4 | 77   | Ln Bi | Ir  | Md HD4 |
| 38 Id   | Mi Sa | Md HD3 | 78   | Ln Bi | Ir  | Hh HD3 |
| 39 Id   | Mi Sa | Hh HD2 | 79   | Ln Bi | Le  | Lw HD6 |
| 40 Id   | Mi Ir | Lw HD5 | 80   | Ln Bi | Le  | Md HD5 |
|         |       |        | 81   | Ln Bi | Le  | Hh HD4 |
8. Simulationresults
In this section, we present the simulation results. We use a PC with these specifications: Processor i5-3570 (3.2 GHz), RAM
(8GB)andSSD(650GB).ThePCrunsLinuxUbuntuOS.WeperformedsimulationsusingFuzzyC,whichisasimulationprogram
writteninCandusesFuzzylibrary[45].
8.1. SimulationresultsofFHDM1
ThesimulationresultsofFHDM1areshowninFig.9.TheyshowtherelationofHDwithSD,SBandSL.TheSDisconsidered
asaconstantparameter.WeincreasetheSBandSLvaluesfrom10%to90%and0to100%,respectively.InFig.9(a),weseethat
8

P.Ampriritetal. InternetofThings23(2023)100870
Fig.9. SimulationresultsofFHDM1.
HDisincreasedwhenSBisdecreasing.TheHDvalueismorethan0.5whenSBis10%andSLvalueismorethan40%.Thismeans
that the UE is connecting to a slice with a high traffic load and less bandwidth, which will have a high handover possibility for
improvingserviceperformance.InFig.9(b),weincreasetheSDto50%.ComparingwithFig.9(a),weseethatHDisincreasingby
13%whenSLis50%andSBis50%.Therefore,theUEneedstofindothersliceswithlowerdelaytoprovidebetterQoS.WhenSB
9

P.Ampriritetal. InternetofThings23(2023)100870
valueis10%,theHDismorethan0.5.So,UEhasahighpossibilitytomakehandovertoanotherslicewhenthepresentslicehas
lowbandwidthandintermediatedelay.However,whenSDisincreasedto90%inFig.9(c),theHDincreasesmuchmorecompared
withFig.9(a)and9(b).IncasewhenSBvalueis90%,theHDisgreaterthan0.5,whenSDvalueis90%andSLvalueisgreater
than60%.
8.2. SimulationresultsofFHDM2
ThesimulationresultsforFHDM2areshowninFigs.10–12.TheyshowtherelationofHDwithSR,whichisconsideredasanew
parameter.WeconsiderSDandSBasconstantparametersandSLhasdifferentvalues.InFig.10,theSDvalueis10%asconstant
parameter and SB has different values: 10%, 50%, 90% (see Fig. 10(a), 10(b) and 10(c)). When SB value is changed from 10%
to 50% and 50% to 90%, the HD values are increased by 15% when SL is 50% and SR is 50%. For low-delay, medium-load and
medium-reliabilityscenarios,thelargeristhesizeofthebandwidth,thelowisthehandoverprobability.IfSLvalueisincreasedto
90%andSRvalueislessthan50%,theHDvaluebecomesmorethan0.5.Thisindicatesthatevenifthepresentslicehasalarger
bandwidthsize,theusershouldmakehandovertohavebetterQoS(seeFig.10(a)and10(b)).InFig.10(c),weseethatthepresent
slicehasbigbandwidthandlowdelaysothereisnotneedforhandover.
WeincreasedtheSDvaluefrom10%to50%inFig.11.WhenwecompareFig.11(a)withFig.10(a),theHDisincreasedby
13%whenSBis10%,SLis50%andSRis50%.Thismeansthepresentslicewithintermediatedelayhasahigherpossibilityto
makehandovercomparedwiththeslicewithlowerdelay.InFig.11(a),thepresentslicewithlowbandwidthsize(SBis10%)has
all HD values greater than 0.5, when SL values are 50% and 90%. In Fig. 11(b), the HD value is increased by 12% for SR 50%,
whenSLvaluesareincreasedfrom10%to50%and50%to90%.ComparingFig.11(c)withFig.11(a)and11(b),theHDvalueis
decreasedby15%whenSRis80%andSLis90%,respectively.
WeincreasedtheSDvalueto90%,asshowninFig.12.ComparingFigs.10and11,wecanseethattheHDvaluesareincreased.
In Fig. 12(a), all HD values are more than 0.5. This means that when the present slice has a high delay and low bandwidth, the
userhasahighpossibilitytomakehandovertoanotherslice.ComparingFig.12(a)withFig.10(c),theHDvalueisincreasedby
50%whenSRis50%andSLis90%.ThisindicatesthatwhenauserisconnectingwiththepresentslicethathasbadQoS,itshould
handovertoanotherslicewithbetterQoS.InFig.12(b)and12(c),weincreasedtheSBvalueto50%and90%.WeseethatHD
valuesaredecreasedcomparedwithFig.12(a).
8.3. Discussion
Inthissubsection,wediscussthesimulationresultsandmakeaqualitativeevaluationconsideringrelatedworkssummarizedin
Tables4and5.
In [11], the authors implement a FL-based algorithm combining with the Multipath Transmission Protocol (MPTCP) in SDN
controller.Theyconsiderthreeparametersforhandoverdecision:RSS,datatransmissionrate,andbatterycharge.Theyclaimthat
theproposedalgorithmcanachieveaseamlesshandover,avoidstheping-pongeffectandreducesunnecessaryhandovers.However,
astheresultofhandoverdecision,aUEmayhandovertoanotherBS,butthedestinationBScannotguaranteethesamesliceQoS
toUE.
In [12], in order to increase the QoS, the authors implement FL in SDN controller, which collects QoS measurements and
dynamically routes service flows to determine suitable paths. The authors consider two parameters: packet loss rate and delay.
However,thereareneededmoreparametersforimprovingQoS.
In[13],inordertoreducehandoverdelaytimeandcomputation,theauthorsimplementaLinearProgramming(LP)technique.
TheproposedtechniquecansatisfyUEwithadelaylessthan1ms,butforperformingmoreefficienthandover,itneedstoconsider
moreparameters.
In[14],thesimulationresultsprovidedbyauthorsshowthatsliceresourcesutilizationisincreased,whilehavinglowcomputing
time,lessnumberofhandoversandlessnumberofdroppedsliceconnectionsbyimplementingthreeheuristicsalgorithms.However,
theproposedheuristicsdonotprovidetheoptimalsolution.Theycanachieveclose-to-optimalsolutions.
In[15],theauthorsusereinforcementlearningtechniquestominimizehandovercostwhilemaintaininguserQoS.Theproposed
approachcanimprovenetworksignalingexchanges/overhead,numberofhandoversandoutageprobability.But,thereareneeded
alotofdataandahighcomputationtimebyusingreinforcementlearning.
In[16],byassuringthateachm-healthcandidatedataflowwillbehandled,theproposedapproachusesaMultipleAttribute
Decision Making (MADM) technique to maximize resource consumption by guaranteeing that each m-health candidate data flow
willbeusedeffectively.TheMADMmethodiseasytoimplement,butitcannotdealwithhumanreasoningandhighcomplexity
approachessuchasAnalyticHierarchyProcess(AHP)andrankreversalphenomena.Forlargenetworksandotherscenarios,there
areneededmachinelearningtechniquestodeterminesliceservicelevelrequirementsmoreprecisely.
Fortheselectionofslices,in[17],theauthorspresentSSF-V2XconsideringthesigmoidfunctiontoevaluateQoSbasedonthe
sliceserviceresourcessuchasslicedelay,slicebandwidthandsliceload.Theproposedapproachshowsbetterdistributionofusers
amongavailableslicesenablingeffectiveresourceusageandloadbalancingprovisioning.But,whenselectingasliceandevaluating
QoS,thereliabilityandsecurityparametersshouldbeconsidered.
In[18],theauthorsshowsasignificantimprovementoverthetraditionalRSSbasedhandoverscheme(lowerhandovercostwith
higheraveragethroughput)byconsideringhandovercostandQoS(SliceDelayandSliceBandwidth).But,theyshouldconsidermore
parametersforevaluatingQoSsuchassecurity,reliabilityandtrafficload.
10

P.Ampriritetal. InternetofThings23(2023)100870
Fig.10. SimulationresultsforFHDM2(SD=10%).
In [19], theauthorsproposea model that can differentiate between regular congestion and anattackby considering Average
Waiting Time (AWT) and Average Switching Rate (ASR). However, the are not considering slice switching patterns and different
kindsofattack.Thus,theproposedmodelcannotpredicttheattackprecisely.
11

P.Ampriritetal. InternetofThings23(2023)100870
Fig.11. SimulationresultsforFHDM2(SD=50%).
Considering merits and demerits of the abovementioned related works, we have proposed an intelligent system based on FL.
In[11,12],theauthorsproposeapproachesbasedonFL.However,inthesepapers,theauthorsconsideronlyconventionalinput
parameters such as RSS, data transmission rate, battery charge or packet loss rate and delay. Different from these related works,
ourresearchisconcentratedonsliceparametersforhandoverdecision.Wehaveimplementedtwomodels(FHDM1andFHDM2),
12

P.Ampriritetal. InternetofThings23(2023)100870
Fig.12. SimulationresultsforFHDM2(SD=90%).
whereFHDM1considersthreeinputparametersandFHDM2fourinoutparameters.FHDS2canprovidebetterhandoverdecision,
becauseitconsiders4inputparameters.
13

P.Ampriritetal. InternetofThings23(2023)100870
Table4
Summaryofrelatedworksconsideringoptimizedparametersandusedapproaches.
References Optimizedparameters Approaches Year
[11] RSS,DataTransmissionRate FLandMPTCP 2018
andBatteryPower
[12] PacketLossRate,Delay FL 2018
[13] HandoverDelayTime LPTechnique 2017
[14] SlicesServiceResources ThreeHeuristicsAlgorithms 2021
(SliceLoad)
[15] HandoverCostsandQoS ReinforcementLearningTechniques 2020
(SliceBandwidth) (Q-learning)
[16] SlicesServiceResourcesandQoS MADM 2022
[17] SlicesServiceResources SSF-V2XConsideringAsigmoidFunction 2019
[18] HandoverCostandQoS CMaaSandSMaaS 2022
(SliceDelayandSliceBandwidth)
[19] SliceSecurityandReliability AttackDetectionandLocalizationAlgorithms 2023
Table5
Summaryofrelatedresearchworksconsideringmeritsanddemerits.
References Merits Demerits
[11] Canavoidtheping-pongeffectandreducesunnecessary DestinationBScannotguaranteethesamesliceQoStoUE.
handovers.
[12] Providedynamicallyroutesserviceflows. Shouldbeconsideredmoreparameters.
[13] Lesshandoverdelaytime. MoreparametersareneededandLPisnotsuitableformore
complexproblems.
[14] Sliceresourcesutilizationisincreased,whilehavinglow Theproposedheuristicsdonotprovidetheoptimalsolution.
computingtime,lessnumberofhandoversanddroppedslice Theycanachieveclose-to-optimalsolutions.
connections.
[15] Networksignalingexchanges/overhead,numberofhandovers Reinforcementlearningneedsalotofdataandcomputation
andoutageareimproved. time.Thus,itcanleadtoanoverloadofstates,whichcan
diminishtheresults.
[16] Maximizessliceresourceutilizationandprovidesslice MADMmethodcannotdealwithnon-mathematicapproaches
services. andhashighcomplexity
[17] Betterdistributionofusersamongavailableslicesenabling NeedstoconsidermoreparametersforevaluatingQoSand
effectiveresourceusageandloadbalancing. selectingslices.
[18] Significantimprovementcomparedwithtraditional NeedstoconsidermoreparametersforevaluatingQoSsuch
RSS-basedhandoverscheme. assecurityandreliability
[19] Candifferentiateregularcongestionfromanattack. Notconsideringsliceswitchingpatternsanddifferentkindof
attacks.
9. Conclusionsandfuturework
In this paper, we presented a Fuzzy-based system for handover in 5G wireless networks considering different network slicing
parameters. We implemented two models: FHDM1 and FHDM2. We evaluated the proposed models by simulations. From the
simulationsresults,weconcludeasfollows.
• TheFHDM2ismorecomplexthanFHDM1,butithasbetterHDsinceithasfourparameters.
• Forbothmodels,theHDvalueincreasesasSDandSLvaluesincreasewhileHDvalueisdecreasingwhenSBandSRvalues
increase.
• ForbetterQoS,amobiledevice(user)connectedtothepresentslice,whichhasahighlatency,lowbandwidth,heavyload,
andalowofreliabilityshouldtomakehandovertoanotherslice.Forexample,intheresultsofFHDM2,theHDvalueismore
overthan86%whenSDis90%,SBis10%,SRis10%andSLis90%.
Infuturework,wewillconsiderotherparametersandperformextensivesimulationstoevaluatetheeffectivenessoftheproposed
system.Wealsowillcomparetheperformanceoftheproposedsystemwithothersystems.Furthermore,weplantoimplementa
testbedandcomparethesimulationresultswithexperimentalresults.
Declarationofcompetinginterest
Theauthorsdeclarethattheyhavenoknowncompetingfinancialinterestsorpersonalrelationshipsthatcouldhaveappeared
toinfluencetheworkreportedinthispaper.
14

P.Ampriritetal. InternetofThings23(2023)100870
Dataavailability
Datawillbemadeavailableonrequest.
References
[1] J.G.Andrews,S.Buzzi,W.Choi,S.V.Hanly,A.Lozano,A.C.K.Soong,J.C.Zhang,Whatwill5Gbe?IEEEJ.Sel.AreasCommun.32(6)(2014)1065–1082,
http://dx.doi.org/10.1109/JSAC.2014.2328098.
[2] K.G.Eze,M.N.Sadiku,S.M.Musa,5Gwirelesstechnology:aprimer,Int.J.Sci.Eng.Technol.7(7)(2018)1581–2277.
[3] E.Hossain,M.Hasan,5Gcellular:keyenablingtechnologiesandresearchchallenges,IEEEInstrum.Meas.Mag.18(3)(2015)11–21,http://dx.doi.org/
10.1109/MIM.2015.7108393.
[4] D.A.Chekired,M.A.Togou,L.Khoukhi,A.Ksentini,5G-slicing-enabledscalableSDNcorenetwork:Towardanultra-lowlatencyofautonomousdriving
service,IEEEJ.Sel.AreasCommun.37(8)(2019)1769–1782,http://dx.doi.org/10.1109/JSAC.2019.2927065.
[5] W.K.Saad,I.Shayea,B.J.Hamza,H.Mohamad,Y.I.Daradkeh,W.A.Jabbar,Handoverparametersoptimisationtechniquesin5Gnetworks,Sensors21
(15)(2021)http://dx.doi.org/10.3390/s21155202,URLhttps://www.mdpi.com/1424-8220/21/15/5202.
[6] M.M. Sajjad, C.J. Bernardos, D. Jayalath, Y.-C. Tian, Inter-slice mobility management in 5G: Motivations, standard principles, challenges, and research
directions,IEEECommun.Stand.Mag.6(1)(2022)93–100,http://dx.doi.org/10.1109/MCOMSTD.0001.2000025.
[7] D.A.Chekired,M.A.Togou,L.Khoukhi,A.Ksentini,5G-slicing-enabledscalableSDNcorenetwork:Towardanultra-lowlatencyofautonomousdriving
service,IEEEJ.Sel.AreasCommun.37(8)(2019)1769–1782.
[8] P.Ampririt,E.Qafzezi,K.Bylykbashi,M.Ikeda,K.Matsuo,L.Barolli,Internationaljournalofdistributedsystemsandtechnologies(IJDST):IFACS-Q3S–A
newadmissioncontrolsystemfor5Gwirelessnetworksbasedonfuzzylogicanditsperformanceevaluation,Int.J.Distrib.Syst.Technol.(IJDST)13(1)
(2022)1–25.
[9] P.Ampririt,S.Ohara,E.Qafzezi,M.Ikeda,K.Matsuo,L.Barolli,Anintegratedfuzzy-basedadmissioncontrolsystem(IFACS)for5Gwirelessnetworks:
Itsimplementationandperformanceevaluation,InternetThings13(2021)100351,http://dx.doi.org/10.1016/j.iot.2020.100351.
[10] P.Ampririt,E.Qafzezi,K.Bylykbashi,M.Ikeda,K.Matsuo,L.Barolli,ApplicationoffuzzylogicforsliceQoSin5Gnetworks:Acomparisonstudyof
twofuzzy-basedschemesforadmissioncontrol,Int.J.Mob.Comput.Multimed.Commun.12(2)(2021)18–35.
[11] D.Yao,X.Su,B.Liu,J.Zeng,AmobilehandovermechanismbasedonfuzzylogicandMPTCPprotocolunderSDNarchitecture*,in:18thInternational
SymposiumonCommunicationsandInformationTechnologies,ISCIT-2018,2018,pp.141–146,http://dx.doi.org/10.1109/ISCIT.2018.8587956.
[12] A.Moravejosharieh,K.Ahmadi,S.Ahmad,Afuzzylogicapproachtoincreasequalityofserviceinsoftwaredefinednetworking,in:2018International
ConferenceonAdvancesinComputing,CommunicationControlandNetworking,ICACCCN-2018,2018,pp.68–73,http://dx.doi.org/10.1109/ICACCCN.
2018.8748678.
[13] J.Lee,Y.Yoo,Handovercellselectionusingusermobilityinformationina5GSDN-basednetwork,in:2017NinthInternationalConferenceonUbiquitous
andFutureNetworks,ICUFN-2017,2017,pp.697–702,http://dx.doi.org/10.1109/ICUFN.2017.7993880.
[14] K.Sevim,T.Tugcu,Handoverwithnetworkslicingin5Gnetworks,in:2021InternationalConferenceonComputer,InformationandTelecommunication
Systems,CITS,2021,pp.1–6,http://dx.doi.org/10.1109/CITS52676.2021.9618576.
[15] Y.Sun,W.Jiang,G.Feng,P.V.Klaine,L.Zhang,M.A.Imran,Y.-C.Liang,Efficienthandovermechanismforradioaccessnetworkslicingbyexploiting
distributedlearning,IEEETrans.Netw.Serv.Manag.17(4)(2020)2620–2633,http://dx.doi.org/10.1109/TNSM.2020.3031079.
[16] F.S.D.Silva,L.M.Schneider,D.Rosário,A.V.Neto,Networkslicingmobilityawarecontroltoassisthandoverdecisionsone-health5Gusecases,in:2022
InternationalWirelessCommunicationsandMobileComputing,IWCMC,2022,pp.1034–1039,http://dx.doi.org/10.1109/IWCMC55113.2022.9825010.
[17] N.Mouawad,R.Naja,S.Tohme,Inter-slicemobilitymanagementsolutioninV2Xenvironment,in:2019InternationalConferenceonWirelessandMobile
Computing,NetworkingandCommunications,WiMob,2019,pp.1–6,http://dx.doi.org/10.1109/WiMOB.2019.8923342.
[18] S.H.Aljbour,A.Y.Alma’aitah,Aninter/intraslicehandoverschemeformobilitymanagementin5Gnetwork,in:202213thInternationalConferenceon
InformationandCommunicationSystems,ICICS,2022,pp.87–92,http://dx.doi.org/10.1109/ICICS55353.2022.9811139.
[19] H.Bisht,M.Patra,S.Kumar,DetectionandlocalizationofDDoSattackduringinter-slicehandoverin5Gnetworkslicing,in:2023IEEE20thConsumer
Communications&NetworkingConference,CCNC,2023,pp.798–803,http://dx.doi.org/10.1109/CCNC51644.2023.10060402.
[20] L. Chettri, R. Bera, A comprehensive survey on internet of things (IoT) toward 5G wireless systems, IEEE Internet Things J. 7 (1) (2020) 16–32,
http://dx.doi.org/10.1109/JIOT.2019.2948888.
[21] N.Gupta,S.Sharma,P.K.Juneja,U.Garg,SDNFV5G-IoT:Aframeworkforthenextgeneration5GenabledIoT,in:2020InternationalConferenceon
AdvancesinComputing,Communication&Materials,ICACCM,2020,pp.289–294,http://dx.doi.org/10.1109/ICACCM50413.2020.9213047.
[22] M.M.Alsulami,N.Akkari,Theroleof5Gwirelessnetworksintheinternet-of-things(IoT),in:20181stInternationalConferenceonComputerApplications
&InformationSecurity,ICCAIS,2018,pp.1–8,http://dx.doi.org/10.1109/CAIS.2018.8471687.
[23] K.Agarwal,K.Agarwal,A.K.Jha,I.Joshi,Intelligenceandinternetofthingswith5Gtechnology:Applicationanddevelopment,in:2022International
ConferenceonElectronicsandRenewableSystems,ICEARS,2022,pp.762–766,http://dx.doi.org/10.1109/ICEARS53579.2022.9752190.
[24] A.M.Escolar,J.M.Alcaraz-Calero,P.Salva-Garcia,J.B.Bernabe,Q.Wang,Adaptivenetworkslicinginmulti-tenant5GIoTnetworks,IEEEAccess9(2021)
14048–14069,http://dx.doi.org/10.1109/ACCESS.2021.3051940.
[25] K.-M.KO,A.M.Mansoor,R.Ahmad,S.-G.Kim,Efficientdeploymentofservicefunctionchains(SFCs)inaself-organizingSDN-NFVnetworkingarchitecture
tosupportIOT,in:2018TenthInternationalConferenceonUbiquitousandFutureNetworks,ICUFN,2018,pp.650–653,http://dx.doi.org/10.1109/ICUFN.
2018.8436674.
[26] L. Xu, The impact of MIMO on IoT network coverage: Case study with smart-BEEM, in: 2018 12th International Conference on Signal Processing and
CommunicationSystems,ICSPCS,2018,pp.1–6,http://dx.doi.org/10.1109/ICSPCS.2018.8631783.
[27] L.E.Li,Z.M.Mao,J.Rexford,Towardsoftware-definedcellularnetworks,in:2012EuropeanWorkshoponSoftwareDefinedNetworking,2012,pp.7–12,
http://dx.doi.org/10.1109/EWSDN.2012.28.
[28] M. Mousa, A.M. Bahaa-Eldin, M. Sobh, Software defined networking concepts and challenges, in: 2016 11th International Conference on Computer
Engineering&Systems,ICCES,IEEE,2016,pp.79–90.
[29] T.Mahmoodi,5GandSoftware-definedNetworking(SDN),in:5GRadioTechnologySeminar.ExploringTechnicalChallengesintheEmerging5GEcosystem,
2015,pp.1–19.
[30] A.A.Barakabitze,A.Ahmad,R.Mijumbi,A.Hines,5GnetworkslicingusingSDNandNFV:Asurveyoftaxonomy,architecturesandfuturechallenges,
Comput.Netw.167,Article106984(2020)1–40.
[31] O.Blial,M.BenMamoun,B.Redouane,AnoverviewonSDNarchitectureswithmultiplecontrollers,J.Comput.Netw.Commun.2016,Article9396525
(2016)1–8,http://dx.doi.org/10.1155/2016/9396525.
[32] M.Alsaeedi,M.M.Mohamad,A.A.Al-Roubaiey,TowardadaptiveandscalableOpenFlow-SDNflowcontrol:Asurvey,IEEEAccess7(2019)107346–107379.
[33] N.Dhruvik,A.J.Karia,A.Khatri,K.M,DesignandimplementationofSDN-basedhandoverin5GmmWave,in:20216thInternationalConferenceon
CommunicationandElectronicsSystems,ICCES,2021,pp.758–762,http://dx.doi.org/10.1109/ICCES51350.2021.9489045.
15

P.Ampriritetal. InternetofThings23(2023)100870
[34] J. Rizkallah, N. Akkari, SDN-based vertical handover decision scheme for 5G networks, in: 2018 IEEE Middle East and North Africa Communications
Conference,MENACOMM,2018,pp.1–6,http://dx.doi.org/10.1109/MENACOMM.2018.8371040.
[35] N.An,Y.Kim,J.Park,D.-H.Kwon,H.Lim,Slicemanagementforqualityofservicedifferentiationinwirelessnetworkslicing,Sensors19(2019)2745,
http://dx.doi.org/10.3390/s19122745.
[36] M.Jiang,M.Condoluci,T.Mahmoodi,Networkslicingmanagement&prioritizationin5Gmobilesystems,in:EuropeanWireless2016;22thEuropean
WirelessConference,VDE,2016,pp.1–6.
[37] J.Chen,M.Tsai,L.Zhao,W.Chang,Y.Lin,Q.Zhou,Y.Lu,J.Tsai,Y.Cai,RealizingdynamicnetworksliceresourcemanagementbasedonSDNnetworks,
in:2019InternationalConferenceonIntelligentComputingandItsEmergingApplications,ICEA,2019,pp.120–125.
[38] X.Li,M.Samaka,H.A.Chan,D.Bhamare,L.Gupta,C.Guo,R.Jain,Networkslicingfor5G:Challengesandopportunities,IEEEInternetComput.21(5)
(2017)20–27.
[39] I.Afolabi,T.Taleb,K.Samdanis,A.Ksentini,H.Flinck,Networkslicingandsoftwarization:Asurveyonprinciples,enablingtechnologies,andsolutions,
IEEECommun.Surv.Tutor.20(3)(2018)2429–2453,http://dx.doi.org/10.1109/COMST.2018.2815638.
[40] N.Alliance,Descriptionofnetworkslicingconcept,NGMN5GP1(1)(2016).
[41] J.Ordonez-Lucena,P.Ameigeiras,D.Lopez,J.J.Ramos-Munoz,J.Lorca,J.Folgueira,Networkslicingfor5GwithSDN/NFV:concepts,architectures,and
challenges,IEEECommun.Mag.55(5)(2017)80–87.
[42] J.Jantzen,TutorialonFuzzyLogic,TechnicalReport,TechnicalUniversityofDenmark,Dept.ofAutomation,1998.
[43] J.M.Mendel,Fuzzylogicsystemsforengineering:atutorial,Proc.IEEE83no.3(3)(1995)345–377,http://dx.doi.org/10.1109/5.364485.
[44] D.A.N.Wulandari,T.Prihatin,A.Prasetyo,N.Merlina,Acomparisontsukamotoandmamdanimethodsinfuzzyinferencesystemfordeterminingnutritional
toddlers,in:20186thInternationalConferenceonCyberandITServiceManagement,CITSM,2018,pp.1–7.
[45] T.Inaba,S.Sakamoto,T.Oda,L.Barolli,M.Takizawa,AnewFACSforcellularwirelessnetworksconsideringQoS:Acomparisonstudyoffuzzycwith
MATLAB,in:201518thInternationalConferenceonNetwork-BasedInformationSystems,2015,pp.338–344.
16