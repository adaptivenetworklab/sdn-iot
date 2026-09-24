# Optimizing-Energy-Efficiency-and-Increasing-Scalability-in-6GIoT-Networks-Through-SDN-Duty-Cycling-and-AIDriven-Slicin

> Source file: `Optimizing-Energy-Efficiency-and-Increasing-Scalability-in-6GIoT-Networks-Through-SDN-Duty-Cycling-and-AIDriven-Slicin.pdf`

---

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 16, No. 9, 2025
Optimizing Energy Efficiency and Increasing
Scalability in 6G-IoT Networks Through SDN, Duty
Cycling, and AI-Driven Slicing
Marwah Albeladi, Kamal Jambi, Fathy E. Eassa, Maher Khemakhem
Department of Computer Science-Faculty of Computing and Information Technology,
King Abdulaziz University (KAU), Jeddah 21589, Saudi Arabia
Abstract—As sixth-generation (6G) and Internet of Things on the integration of space, air, and ground networks into a
(IoT) networks expand rapidly, concerns are growing about Space-Air-Ground Integrated Network (SAGIN) [4].
their energy consumption and scalability. This is primarily
because more devices arebeing connected, resulting in increased Unlike earlier works centered on terrestrial networks, this
energy consumption.energy consumption.This study examines research emphasizes global coverage and intelligent manage-
three primary strategies for optimizing energy efficiency and ment of network slices to ensure specific Quality of Service
improving scalability in 6G-IoT networks.This research looks at (QoS)needs[5].Networkslicing,asdescribedinpriorstudies,
three experimental setups: 1) using software-defined networking enables logically isolated virtual networks for different ser-
(SDN) with dynamic slicing to organize devices based on when vices; this research extends the discussion by analyzing cost-
they are most and least used, 2) duty cycling, which turns
effective slice management strategies throughout the slicing
devices on and off to save energy, and 3) AI-optimized network
life cycle, which past research has only partially addressed.
slicing that uses both convolutional neural networks (CNN) and
bidirectional long short-term memory (BiLSTM) models. In the Unlike earlier generations, which typically managed net-
firstsetup,SDNwithdynamicslicinghelpedreduceunnecessary
work resources within a single domain, 6G network slicing
power consumption by matching device activity to peak times.
must coordinate across heterogeneous segments in SAGIN.
As more devices were added, this method kept energy use low
Previous studies have not fully considered the additional com-
and improved the network’s ability to handle growth without
plexity that emerges from integrating space, air, and ground
requiring significantly more power. This resulted in a 66.28
percentdecreaseinpowerusage.Inthesecondsetup,dutycycling networks. The current research addresses this gap by focusing
allowed only some devices to be active at a time, which reduced onuniquechallengesandmanagementstrategiesnecessaryfor
power use by over 60 percent during slow periods. In the third effective slice orchestration across these domains.
setup,theCNN-BiLSTMmodeleffectivelyclassifiedservicetypes
Therefore, the development of smart slice management
and reduced power use by 60.14 percent. While these methods
were not combined into a single solution, each utilized slicing solutions in 6G networks is required.
techniques to more effectively allocate resources and manage
The current research addresses this need by proposing
power.
an approach for efficient and intelligent network slice man-
Keywords—6G-IoT; energy efficiency; scalability; SDN; duty agement specific to SAGIN-based 6G-IoT environments. This
cycling; network slicing; CNN; BiLSTM; AI-driven optimization workaimstoadvancecurrentpracticebyfocusingonenhanced
resource allocation and tailored slice management strategies
that specifically address the emerging challenges identified
I. INTRODUCTION
above.Inaddition,withtheavailabilityofpowerfulcomputing
capabilities and advanced.
This study addresses the urgent need for smart, energy-
efficient slice management solutions in 6G networks, target-
AI services are being enhanced with new QoS require-
ing the challenge of supporting advanced AI services with
ments, such as data quality, training latency, and inference
newQoSrequirements.Bydevelopinginnovativemanagement
accuracy. As a result, dedicated network slices must be es-
strategies, the research contributes to improving energy effi-
tablished to support emerging AI services in 6G networks.
ciency, reliability, and adaptability in next-generation SAGIN-
To address these challenges, innovative solutions are urgently
enabled 6G-IoT networks [1] [2]. Many technologies, includ-
needed to enhance energy efficiency without compromising
ing mobile phones, transportation systems, food production,
network performance [6]. The objective of this paper is to:
housing,healthcare,clothing,andremotemonitoring,arebeing
transformedbytheInternetofThings(IoT).Astheseadvances • AnalyzingtheimpactofSDNonenergyconsumption
occur,creatingenergy-efficient6G-IoTnetworksbecomescru- in 6G-IoT networks, by evaluating the dynamic allo-
cials [3]. cation mechanism for devices based on peak and idle
periods.
Existing studies have shown that 6G-IoT networks will
link billions of devices worldwide, resulting in high energy • Evaluating the effectiveness of Duty Cycling in re-
consumption. While prior research highlights the significance ducingunnecessaryenergyconsumptionbyregulating
of energy efficiency for the long-term profitability of network device on- and off-duty times based on daily work
operators, the current study distinguishes itself by focusing schedules.
www.ijacsa.thesai.org 927 | P a g e

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 16, No. 9, 2025
• Testingtheperformanceofadeeplearningmodelcon- Each of these applications requires specific network charac-
sisting of CNNs and BiLSTM networks in classifying teristics, such as instant response or high bandwidth. With
network data into multiple categories and accurately network slicing, these specific needs of each application can
estimating the energy requirements for each category. be met individually. In addition, robust security strategies can
be applied to each slice to ensure data protection and provide
• Identifying the energy efficiency differences between
faster response.
each technology separately without combining them,
toobtainaclearandindependentpictureoftheimpact Machinelearningcanmonitornetworkactivityandpredict
ofeachapproachunderdifferentoperatingconditions. the needs of devices and services [10]. It can analyze large
datasets to provide the optimal allocation of resources. In
• Providing a scientific basis for comparing energy
addition, it helps reduce network congestion by optimizing
managementmethodologiestoenable6G-IoTnetwork
data distribution. Machine learning can be used to improve
developers to choose or develop flexible and scalable
services such as security, spam detection, and power man-
solutions based on the nature of network load and
agement automatically. 6G networks will provide a range
future applications.
of different services that will benefit users. These services
This study presents a set of contributions used to reduce includeenhancedmobilebroadband,ultra-reliablelow-latency
energy consumption and increase efficiency in the 6G-IoT communication, and massive machine-type communications
network through the following points. [11]:
• SDN-based dynamic slicing was combined into one • Super-eMBB: means broadband connectivity via mo-
model to reduce energy consumption and increase bile phones, with a focus on energy efficiency.
energy efficiency.
• MassiveMTC:meansconnectingaverylargenumber
• Slicinganddutycyclingtoreduceenergyconsumption of devices, such as IoT devices, that need constant
and increase energy efficiency. connectivity.
• Explainhowenergyefficiencychangeswithincreasing • Super URLLC: provides highly reliable communica-
devicedensity,ensuringtheabilitytoadapttonetwork tions with minimal delay, such as remote control of
expansion processes. devices.
• hybrid CNN-BiLSTM model was implemented, • Ultra-high resolution: means using technologies to
achieving 99% classification accuracy, enabling intel- provide high resolution in data transmission.
ligent slicing and adaptation.
• Super-immersive reality: includes virtual reality and
This paper is organized as follows. To begin, Section II augmented reality experiences that provide enhanced
covers the key features of 6G and the role of AI-powered interaction.
network chips, laying the groundwork for the subsequent
discussion.Buildingonthis,SectionIIIreviewspreviouswork III. RELATEDWORK
on energy efficiency and scalability in 6G IoT. Then, Section
Sixth-generation - 6G networks rely on network slicing, a
IV outlines our research approaches, which are expanded
technology that is still in its infancy but is rapidly evolving
upon in Section V with details on the proposed approaches,
and offering a variety of services.
including SDN-based chips, duty cycle, and AI-enabled chips.
Followingthat,SectionVIreviewstheresultsandeffectiveness
of these techniques. In Section VII, we further discuss our A. Using Software-Defined Networking
experimental results on energy usage. Finally, Section VIII
The study [16] used the energy-aware routing, multi-level,
concludes the paper and suggests future research directions.
and mapping problem (EARMLP) algorithm, which achieves
better performance by reducing the number of active nodes
II. BACKGROUND and integrating the use of network resources. The number
Networkslicingisatechnologythatdividesanetworkinto of controllers and their optimal placement have a significant
multiplededicated“slices”.Eachsliceoperatesindependently, impact on energy savings. In [17], the authors present a
allowing flexible allocation of resources based on specific comprehensive survey on SDN for various smart applica-
needs. This technology significantly enhances network perfor- tions. This survey covers the infrastructural details of SDN
manceandquality,particularlyinexpandingIoTenvironments hardware, OpenFlow switches, controllers, simulation tools,
[7].Withnetwork slicing,resourcescanbe giventoeachslice programming languages, open issues, and challenges in SDN
based on its unique needs. implementation using advanced technologies.
For example, one slice can serve IoT applications that
B. Using Machine Learning
require steady connectivity and low power, while another
can support high-speed data, such as HD video. Allocating Several studies have used different methods to reduce
resources based on actual service or application needs reduces power consumption. In a study [18], collaborative commu-
waste and improves network efficiency [9]. Each slice works nication was used. This means that mobile phones or smart
independently, reducing interference between applications. 6G devices work together as a team, rather than working sepa-
networks can support a wide range of diverse applications, rately. When these devices work together, energy can be more
fromself-drivingcarstovirtualandaugmentedrealityservices. efficiently saved, which helps extend battery life. Machine
www.ijacsa.thesai.org 928 | P a g e

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 16, No. 9, 2025
learning, specifically artificial neural networks (ANNs), is IV. STUDYCONTRIBUTIONS
utilized to enhance network slicing in 6G networks, focusing
onenergyconsumption.Thisapproachinvolvesamultifaceted The current study significantly expanded the scope of
strategy that integrates various techniques to improve energy previousresearchbysimultaneouslycombiningthreeindepen-
efficiency while maintaining high performance. In [19], the dent and integrated technologies: software-defined networking
datarateallocation(DTRA)methodwasusedtoimprovedata (SDN)-based dynamic slicing, workflow, and AI-assisted slic-
transmission efficiency in 6G networks. The residual energy ing using CNN-BiLSTM, to improve energy utilization and
clusterhead(RECH)methodwasused.Furthermore,thiswork scalability in 6G-IoT environments. Although each previous
used the dynamic multipath routing protocol (DMRP)method study focused on a single aspect, such as software-defined
to improve the reliability and speed of 6G networks. After networking (SDN) control plane (Study[16] ),or an artifi-
evaluating performance metrics, the DTRA method improved cial neural network (ANN)-based collaboration (Study [18]),
the lifetime and energy efficiency of the network by 95.3% These efforts often faced critical limitations, including high
based on 6G networks. complexity, poor scalability, and limited accuracy in traffic
management.
C. Using Network Slicing The current study addresses the gaps in previous research
throughadiverseexperimentaldesign.Inthefirstscenario,the
Flexiblenetworkslicingisoneoftheessentialcomponents study used Software-Defined Networks (SDN) to dynamically
of 6G networks, allowing the creation of customized network operate devices during peak usage periods. This technology
environments to meet the needs of specific applications and addressed the limitations of static routing in previous studies
services. The study of Sheena [27] aims to improve the based on SDN. By applying the second scenario, the study
efficiency of the network by designing a Deep Learning- was able to improve selective activation strategies, such as
based Network Slicing with Data Aggregation (EENS-DA) those found in studies [18] and [19]. A duty cycle was im-
technique, which allocates the necessary physical resources to plemented in the third scenario to reduce energy consumption
specific applications clearly and efficiently. The study of Phyu during periods of low activity, which is considered the most
[28]aimstoaddresstheproblemofactivating/deactivatingslic- innovative.
ingtoreduceenergyconsumptionwhilemaintainingQualityof
Service (QoS) for users. The researchers relied on two Multi- It utilized CNN-BiLSTM technology to intelligently clas-
Armed Bandit (MAB) agents to make activating/deactivating sifytraffictypesandallocateresourcesaccordingly,surpassing
decisions at the level of individual base stations. Researchers previous models like random forests or DRL in terms of
in the study [31] propose a hybrid model that combines CNN accuracy and energy saving. Table II presents a comparative
andBiLSTM.TheCNNwasusedtoextractautomaticfeatures analysis of related studies and the contribution of the current
from the input data. The BiLSTM was used to classify and research.
determine the appropriate network segment for each request.
The results showed that the hybrid model achieved an overall The current study significantly expanded the scope of
accuracy rate of 97.21%, demonstrating the effectiveness of previousresearchbysimultaneouslycombiningthreeindepen-
this approach in allocating the appropriate network segments dent and integrated technologies: software-defined networking
to end users. (SDN)-based dynamic slicing, workflow, and AI-assisted slic-
ing using CNN-BiLSTM, to improve energy utilization and
scalability in 6G-IoT environments. Although each previous
D. Research Gap study focused on a single aspect, such as software-defined
networking (SDN) control plane (Study [16]), or artificial
After reviewing existing research, several gaps in the neural network (ANN)-based collaboration (Study [18]), these
literature become apparent. Some studies focus on specific efforts often faced critical limitations: high complexity, poor
techniques, such as network slicing, machine learning, and scalability, or limited accuracy in traffic management.
energy-aware routing. However, a comprehensive framework
that integrates these methods to improve energy efficiency in The current study addresses the gaps in previous research
6G-IoT networks remains absent. Although energy efficiency throughadiverseexperimentaldesign.Inthefirstscenario,the
has generally improved, challenges persist in maintaining study used Software-Defined Networks (SDN) to dynamically
quality of service (QoS), which includes factors such as operate devices during peak usage periods. This technology
latencyandthroughput.Onlyalimitednumberofstudieshave addressed the limitations of static routing in previous studies
successfully addressed the simultaneous enhancement of both basedonSDN.Byapplyingthesecondscenario,thestudywas
energy efficiency and QoS, as demonstrated in the work by able to improve selective activation strategies, such as those
[28].Flexiblenetworkslicingiswidelyrecognizedasacrucial found in studies [18] and [19]. A duty cycle was implemented
component for the success of 6G; nevertheless, established to reduce energy consumption during periods of low activity
guidelines for the design, implementation, and management in the third scenario, which is considered the most innovative.
of such slices are lacking, as noted in studies [27] and [28]. It utilized CNN-BiLSTM technology to intelligently classify
Addressing these gaps is expected to contribute to significant traffic types and allocate resources accordingly, surpassing
advancements in energy efficiency and scalability in 6G-IoT previous models like random forests or DRL in terms of
networks through the use of advanced technologies such as accuracy and energy saving. Table II presents a comparative
machine learning, network slicing, and SDN. Table I provides analysis of related studies and the contribution of the current
a comparison of the relevant studies. research.
www.ijacsa.thesai.org 929 | P a g e

|     |     |     |     |     |     | (IJACSA) | International | Journal | of  | Advanced | Computer |     | Science | and      | Applications, |      |
| --- | --- | --- | --- | --- | --- | -------- | ------------- | ------- | --- | -------- | -------- | --- | ------- | -------- | ------------- | ---- |
|     |     |     |     |     |     |          |               |         |     |          |          |     |         | Vol. 16, | No. 9,        | 2025 |
TABLEI.COMPARATIVEANALYSISOFRESEARCHONENERGYEFFICIENCYIN6GNETWORKS
| Author | Idea |     |     |     | Methodology |     |     | Features |     |     |     | Challenges |     |     |     |     |
| ------ | ---- | --- | --- | --- | ----------- | --- | --- | -------- | --- | --- | --- | ---------- | --- | --- | --- | --- |
[16] Energy-awareroutingtoreduceactive EARMLP (Energy-Aware Routing Reduces number of active nodes; integrates Impactofnumberandoptimalplace-
nodesandimproveresourceutilization Multi-LevelandMappingProblem) networkresourceusage mentofcontrollersonenergysavings
[17] SurveyonSDNforsmartapplications Comprehensivesurvey Covers SDN hardware, OpenFlow switches, Implementation challenges of SDN
|     |     |     |     |     |     |     |     | controllers, simulation |     | tools, | programming | withadvancedtechnologies |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | ------ | ----------- | ------------------------ | --- | --- | --- | --- |
languages;openissuesandchallenges
[18] Reducingpowerconsumptionthrough Collaborativecommunication+ANN Smartdevicesworktogetherasateam;saves Coordinating collaboration while
collaborativecommunication energy;extendsbatterylife maintaininghighperformance
[19] Improving energy efficiency and life- DTRA;RECH;DMRP Improved transmission efficiency, reliability Managing multiple methods together
timeof6Gnetworks andspeed;networklifetime/energyefficiency inreal6Genvironments
improvedby95.3%
[27] Efficient network slicing with deep EENS-DA(DeepLearning+DataAg- Allocatesphysicalresourcesclearlyandeffi- Balancingenergysavingwithapplica-
learninganddataaggregation gregation) cientlytospecificapplications tionneeds
[28] Energy saving by activat- Multi-ArmedBandit(MAB)agents Activate/deactivate decisions at base-station Maintaining QoS while reducing en-
|     | ing/deactivatingslicingwhilekeeping |     |     |     |     |     |     | level |     |     |     | ergyconsumption |     |     |     |     |
| --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --------------- | --- | --- | --- | --- |
QoS
[31] Hybridmodelfornetwork-slicingclas- HybridCNN+BiLSTM CNNforfeatureextraction;BiLSTMforclas- Complex training and computational
|     | sification |     |     |     |     |     |     | sification;overallaccuracy97.21% |     |     |     | resources |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --------- | --- | --- | --- | --- |
V. METHODOLOGY orconcatenation.ThemainadvantageofusingBiLSTMisthat
|                  |      |               |            |          |     |                |     | it allows         | each      | part of | the         | input     | data to   | include | information |       |
| ---------------- | ---- | ------------- | ---------- | -------- | --- | -------------- | --- | ----------------- | --------- | ------- | ----------- | --------- | --------- | ------- | ----------- | ----- |
| In               | this | section, deep | learning   | methods  |     | are introduced | for |                   |           |         |             |           |           |         |             |       |
|                  |      |               |            |          |     |                |     | from both         | past      | and     | present     | contexts. | This      | results | in          | more  |
| tackling         | the  | problem       | of network | slicing. |     |                |     |                   |           |         |             |           |           |         |             |       |
|                  |      |               |            |          |     |                |     | accurate          | output    | because | BiLSTM      |           | [22] uses | LSTM    | layers      | to    |
|                  |      |               |            |          |     |                |     | analyze           | data from | both    | directions. |           | Although  | BiLSTM  |             | might |
| A. Convolutional |      | Neural        | Network    |          |     |                |     |                   |           |         |             |           |           |         |             |       |
|                  |      |               |            |          |     |                |     | seem complicated, |           | it      | produces    | strong    | results   | due     | to a        | solid |
1)Reasons to use CNN: CNNs [8] can find hidden pat- understanding of the data environment. In [34], a multilayer
terns in data without needing any manual adjustments. High BiLSTM is utilized, where each layer consists of two cells
|     |     |     |     |     |     |     |     | that process | information |     | in  | forward | and | backward | directions |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | --- | ------- | --- | -------- | ---------- | --- |
Efficiency:Theconvolutionallayerfocusesonspecificpartsof
separately.
| the data,    | making | it highly | effective |        | for analyzing |      | data related |     |     |     |     |     |     |     |     |     |
| ------------ | ------ | --------- | --------- | ------ | ------------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| to networks. |        | CNNs [12] | can       | create | systems       | that | communicate  |     |     |     |     |     |     |     |     |     |
using. Human speech [32]. Making Overprocessing Simpler: D. Dataset Description
| Pooling | simplifies   | the  | data    | while | retaining | most   | of the es- |             |        |             |         |            |          |            |            |     |
| ------- | ------------ | ---- | ------- | ----- | --------- | ------ | ---------- | ----------- | ------ | ----------- | ------- | ---------- | -------- | ---------- | ---------- | --- |
|         |              |      |         |       |           |        |            | In Case     | 3,     | the dataset |         | is sourced | from     | the        | University | of  |
| sential | information. | CNNs | consist | of    | several   | layers | connected  |             |        |             |         |            |          |            |            |     |
|         |              |      |         |       |           |        |            | California, | Irvine | (UCI)       | Machine |            | Learning | Repository | [35].      | It  |
in sequence: the first layer is the input layer, followed by includes 87 features, each representing details of an IP flow
| hidden | layers, | and the   | last one | is the | output  | layer.    | The hidden |                |     |         |      |           |     |             |     |        |
| ------ | ------- | --------- | -------- | ------ | ------- | --------- | ---------- | -------------- | --- | ------- | ---- | --------- | --- | ----------- | --- | ------ |
|        |         |           |          |        |         |           |            | from a network |     | device, | such | as source | and | destination |     | IP ad- |
| layers | process | the input | data     | and    | extract | important | features   |                |     |         |      |           |     |             |     |        |
dresses,portnumbers,andconnectiontimestamps.Onesource
| using | filters. | Overall, | the combination |     | of  | convolutional | layers, |          |                   |     |       |         |            |     |           |     |
| ----- | -------- | -------- | --------------- | --- | --- | ------------- | ------- | -------- | ----------------- | --- | ----- | ------- | ---------- | --- | --------- | --- |
|       |          |          |                 |     |     |               |         | collects | this information, |     | while | another | classifies |     | the layer | 7   |
poolinglayers,andfullyconnectedlayersinCNNsenablesthe
protocol,whichcorrespondstotheapplicationlevelinnetwork
networktolearnandrecognizepatternseffectivelyincomplex communication [36]. Most features are numerical, with some
data [33].
|                     |       |      |        |                           |     |     |     | being categorical |               | (nominal), |       | and | one feature | captures |     | dates |
| ------------------- | ----- | ---- | ------ | ------------------------- | --- | --- | --- | ----------------- | ------------- | ---------- | ----- | --- | ----------- | -------- | --- | ----- |
|                     |       |      |        |                           |     |     |     | derived from      | timestamps    |            | [37]. |     |             |          |     |       |
| B. Long             | Short | Term | Memory |                           |     |     |     |                   |               |            |       |     |             |          |     |       |
|                     |       |      |        |                           |     |     |     | E. Data           | Preprocessing |            |       |     |             |          |     |       |
| 1)ReasonstouseLSTM: |       |      |        | [13]:LongShort-TermMemory |     |     |     |                   |               |            |       |     |             |          |     |       |
Reasons to use LSTM are that it is a unique type of recurrent The diverse data (textual and numerical) were processed
| neural | network | (RNN)             | [20] | [21] specifically |           | designed   | to ad- |            |         |               |       |        |            |          |            |     |
| ------ | ------- | ----------------- | ---- | ----------------- | --------- | ---------- | ------ | ---------- | ------- | ------------- | ----- | ------ | ---------- | -------- | ---------- | --- |
|        |         |                   |      |                   |           |            |        | to address | value   | errors,       | gaps, | and    | duplicates | in       | accordance |     |
| dress  | issues  | such as vanishing |      | and               | exploding | gradients. | These  |            |         |               |       |        |            |          |            |     |
|        |         |                   |      |                   |           |            |        | with the   | model’s | requirements. |       | Python |            | was used | to remove  |     |
problems can make it challenging for neural networks to learn duplicate rows, handle missing values with the column mean,
effectively. For network slicing classification, a deep learning detect and delete errors, then Min-Max normalization was
[15]approach was applied. LSTMs [22]are better suited for applied to constrain the values between 0 and 1, and the
| this | task because | they | can handle | both | the | fading | and growing |         |          |       |     |       |     |         |             |     |
| ---- | ------------ | ---- | ---------- | ---- | --- | ------ | ----------- | ------- | -------- | ----- | --- | ----- | --- | ------- | ----------- | --- |
|      |              |      |            |      |     |        |             | cleaned | data was | saved | in  | a new | CSV | file in | preparation |     |
gradientissues,aswellasthelong-termdependencychallenges
|     |     |     |     |     |     |     |     | for machine | learning |     | models. | The | set | includes | 78  | labels, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ------- | --- | --- | -------- | --- | ------- |
[14] that regular RNNs face. This makes LSTMs typically and the labeling process is a pivotal step directed by device
more effective than traditional RNNs[33]. requestsandscientificliterature[37].Thedatawasdividedinto
fiveslices:Super-eMBB,MassiveMTC,super-URLLC,super-
C. Bidirectional LSTM (BiLSTM) Precision, and super-immersive; these are common categories
|             |                  |          |               |             |               |          |               | in 5G/6G         | research     |            | that represent |     | different    | service | require- |         |
| ----------- | ---------------- | -------- | ------------- | ----------- | ------------- | -------- | ------------- | ---------------- | ------------ | ---------- | -------------- | --- | ------------ | ------- | -------- | ------- |
| 1)Reasons   |                  | to use   | bidirectional |             | LSTM:         |          | Bidirectional |                  |              |            |                |     |              |         |          |         |
|             |                  |          |               |             |               |          |               | ments, including |              | high       | speed,         | low | latency,     | support | for      | a large |
| LSTM        | (BiLSTM):Reasons |          | to            | use         | Bidirectional |          | LSTM (BiL-    |                  |              |            |                |     |              |         |          |         |
|             |                  |          |               |             |               |          |               | number           | of devices,  | precision, |                | and | reliability. |         |          |         |
| STM)        | [15]             | include  | adding        | an LSTM     | layer         | that     | processes     |                  |              |            |                |     |              |         |          |         |
| information |                  | in both  | forward       | and reverse |               | orders.  | The outputs   |                  |              |            |                |     |              |         |          |         |
|             |                  |          |               |             |               |          |               | F. Dataset       | Segmentation |            |                |     |              |         |          |         |
| from        | the              | two LSTM | [14]layers    |             | are then      | combined | using         |                  |              |            |                |     |              |         |          |         |
techniques such as calculating the mean, sum, multiplication, The data is categorized into the following types:
|     |     |     |     |     |     |     | www.ijacsa.thesai.org |     |     |     |     |     |     | 930 | | P | a g e |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

|     | (IJACSA) | International | Journal       | of    | Advanced | Computer    |             | Science     | and        | Applications, |      |
| --- | -------- | ------------- | ------------- | ----- | -------- | ----------- | ----------- | ----------- | ---------- | ------------- | ---- |
|     |          |               |               |       |          |             |             | Vol.        | 16,        | No. 9,        | 2025 |
|     |          |               | 1)Super-eMBB: |       |          | This chip   | is designed |             | to deliver | high          | data |
|     |          |               | speeds and    | large | transfer | capacities. |             | It is ideal | for        | applications  |      |
ybsecruoseretacollaotnoitacfiissalc htiwlortnocecruoserNDSsenibmoC
ehtslliFydutStnerruCehtwoH ygrenedne-ot-dnednanoitacfiissalc sniagygreneyfitnauqdnaepytatad dnanoitacfiissalccfifartnevird-LM tneicfife-ygrenecitsilohrofgnicils that need fast data transfers, such as streaming 4K/8K videos
| NDSnanihtiwLMsetargetnI |     |     | and online | gaming | [38]. |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
cfifartG6htiwtnemnorivne cfifartdesab–MTSLiB–NNC
|     |     |     | 2)Massive-MTC: |       |               | This | chip is | intended | for           | Internet | of  |
| --- | --- | --- | -------------- | ----- | ------------- | ---- | ------- | -------- | ------------- | -------- | --- |
|     |     |     | Things         | (IoT) | applications, |      | which   | involve  | communication |          |     |
tnemssessatcapmi among many devices. Examples include smart meters, wear-
htiwNDSsesU tnemeganamG6
|     |     |     | able gadgets, |           | and embedded |         | systems.   | It  | excels | at managing |     |
| --- | --- | --- | ------------- | --------- | ------------ | ------- | ---------- | --- | ------ | ----------- | --- |
|     |     |     | numerous      | low-power |              | devices | [39] [40]. |     |        |             |     |
spaG
|                                    |                               |     | 3)Super-URLLC: |      |             | Thischipisusedforapplicationsrequir- |         |        |      |              |     |
| ---------------------------------- | ----------------------------- | --- | -------------- | ---- | ----------- | ------------------------------------ | ------- | ------ | ---- | ------------ | --- |
|                                    |                               |     | ing both       | high | reliability | and                                  | minimal | delay, | like | self-driving |     |
| defiinudetimil;gnicilsepyt-cfifart | desab-LMhtiwnoitargetnifokcaL |     |                |      |             |                                      |         |        |      |              |     |
ygrenedefiinudnanoitartsehcro cars and telemedicine. It ensures dependable data transfer
HCRAESERTNERRUCEHTFONOITUBIRTNOCEHTDNASEIDUTSDETALERFOSISYLANAEVITARAPMOC.IIELBAT ronoitargetniNDSticilpxeoN
|                                                     |                            |     | while keeping      |             | delays     | to a minimum |               | [41]  | [42].        |           |       |
| --------------------------------------------------- | -------------------------- | --- | ------------------ | ----------- | ---------- | ------------ | ------------- | ----- | ------------ | --------- | ----- |
| soiranecsssorcanoitaulave desab-NDSticilpmi/detimiL | gnicilsG6dnanoitacfiissalc |     |                    |             |            |              |               |       |              |           |       |
|                                                     |                            |     | 4)Super-precision: |             |            | This         | chip caters   | to    | applications |           | need- |
|                                                     |                            |     | ing high           | spatial     | resolution |              | or detailed   | data, | such         | as        | envi- |
|                                                     |                            |     | ronmental          | monitoring, |            | precise      | measurements, |       | and          | augmented |       |
|                                                     |                            |     | reality (AR)       | and         | virtual    | reality      | (VR)          | [43]. |              |           |       |
noitaulave
|     | txetnoc |     | 5)Super-immersive: |     |     | Thischipisdesignedforapplications |     |     |     |     |     |
| --- | ------- | --- | ------------------ | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
spaG
|     |     |     | requiring | extensive |     | coverage | and | high | efficiency, | such | as  |
| --- | --- | --- | --------- | --------- | --- | -------- | --- | ---- | ----------- | ---- | --- |
;efilyrettabdnetxednaygreneevas devorpmiycneicfifeygrene/emitefil augmented reality (AR) and virtual reality (VR). It facilitates
aivnoitcuderygrene;snoitacilppa ;noitavitcaed/noitavitcadellortnoc ;sedonevitcaforebmundecudeR
otnoitarepoeciveddesab-maeT ycneicfifenoissimsnartdevorpmi otnoitacollaevitceffednaraelC ;secruoserkrowtenfonoitargetni immersive user experiences within advanced network environ-
| rofycaruccallarevo%12.79 | ,segaugnal,sloot,srellortnoc |     | ments [44]. |     |     |     |     |     |     |     |     |
| ------------------------ | ---------------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
,erawdrah(egarevocdaorb
krowten;ytilibailerdna The categorization process is as follows: when a device,
|     |     |     | such as     | a smartphone |         | or sensor,    | sends | a     | request, | the type    | of  |
| --- | --- | --- | ----------- | ------------ | ------- | ------------- | ----- | ----- | -------- | ----------- | --- |
|     |     |     | application | or           | service | is evaluated. |       | Based | on this  | evaluation, |     |
noitacfiissalc
|     |     | )segnellahc | the appropriate |     | category, | or  | “slice”, | is assigned |     | to meet | those |
| --- | --- | ----------- | --------------- | --- | --------- | --- | -------- | ----------- | --- | ------- | ----- |
shtgnertS %3.59yb
needs.Forexample,ifhighspeedisnecessary,therequestwill
|     |     |     | be routed | to the | Super-eMBB |     | slice. |     |     |     |     |
| --- | --- | --- | --------- | ------ | ---------- | --- | ------ | --- | --- | --- | --- |
elihwSoQgniniatniam ecilsetaruccagnilbane aivnoitpmusnocygrene gnituorerawa-ecruoser In contrast, if minimal delay is essential, as in the case of
ecuderdnaycneicfife
|     |     |     | self-driving | cars, | the | Super-URLLC |     | slice | will be | employed. |     |
| --- | --- | --- | ------------ | ----- | --- | ----------- | --- | ----- | ------- | --------- | --- |
emitefil/ycneicfife ecruosertneicfifE
dnanoitpmusnoc krowtenecnahne krowtenecnahnE Each slice provides distinct performance and resources cus-
rewopecudeR dnanoitacolla
|                     |     |     | tomized     | to the | current    | network | demands,            |     | optimizing | resource |     |
| ------------------- | --- | --- | ----------- | ------ | ---------- | ------- | ------------------- | --- | ---------- | -------- | --- |
| evitcejbO noitceles |     |     |             |        |            |         |                     |     |            |          |     |
|                     |     |     | utilization | and    | minimizing |         | energy consumption. |     |            |          |     |
VI. PROPOSEDMETHODOLOGY
ataD+gninraeLpeeD(AD-SNEE rofstnegaBAMowt;)noitagerggA MTSLiB+NNCdirbyH;ffo/noecils erawa-ygrene(mhtiroglaPLMRAE
|                                                |                              |     | The         | approach | involves |           | three key | experiments |            | designed    |     |
| ---------------------------------------------- | ---------------------------- | --- | ----------- | -------- | -------- | --------- | --------- | ----------- | ---------- | ----------- | --- |
| ;noitacinummocevitaroballoC PRMD,HCER,ARTD;NNA | ;)gnippamlevel-itlum,gnituor |     |             |          |          |           |           |             |            |             |     |
|                                                | yevrusNDSevisneherpmoc       |     | to address  | existing |          | research  | gaps      | in energy   | efficiency |             | and |
|                                                |                              |     | scalability | of       | 6G-IoT   | networks. | Each      | of          | these      | experiments |     |
noitacfiissalcecilsrof
desUygolodohteM employs various methods to reduce energy use in 6G-IoT
networks.
A. Case1SoftwareDefinedNetworkingwithDynamicSlicing
|     |     |     | (Scenario | 1)     |            |     |          |              |     |       |      |
| --- | --- | --- | --------- | ------ | ---------- | --- | -------- | ------------ | --- | ----- | ---- |
|     |     |     | Step      | 1: The | experiment |     | presents | a simulation |     | model | of a |
6G-IoTnetworkinPythonusingNetworkX[25],startingwith
).feR(seidutS ]13[,]82[,]72[ 30 devices and gradually expanding to 500-2500 devices to
|           |           |     | measure | scalability | and | its | impact on | performance |     | and | energy |
| --------- | --------- | --- | ------- | ----------- | --- | --- | --------- | ----------- | --- | --- | ------ |
| ]91[,]81[ | ]71[,]61[ |     |         |             |     |     |           |             |     |     |        |
consumption.ThenetworkismanagedviaSDNwithdynamic
|     |     |     | slicing,  | which         | adjusts | the         | states of | devices  | (active/inactive) |         |     |
| --- | --- | --- | --------- | ------------- | ------- | ----------- | --------- | -------- | ----------------- | ------- | --- |
|     |     |     | according | to peak       | (6      | AM–6        | PM)       | and idle | periods.          | Sensors |     |
|     |     |     | remain    | active during |         | peak times, | cameras   |          | are disabled      | outside |     |
ygrenErofLM of these periods, and lights operate randomly. The setup
|     |     |     | relies on  | networkx, | numpy      |       | [22], matplotlib |     | [24],           | and random, |     |
| --- | --- | --- | ---------- | --------- | ---------- | ----- | ---------------- | --- | --------------- | ----------- | --- |
|     |     |     | and energy | is        | calculated | using | a function       |     | that aggregates |             | the |
gnivaS gnicilS
dleiF NDS consumption of active devices only, then compares the values
|     |     |                       | before and | after        | slicing. | Hourly | readings |     | were collected |           | over  |
| --- | --- | --------------------- | ---------- | ------------ | -------- | ------ | -------- | --- | -------------- | --------- | ----- |
|     |     |                       | 24 hours   | and analyzed |          | using  | the mean | and | standard       | deviation |       |
|     |     | www.ijacsa.thesai.org |            |              |          |        |          |     | 931            | | P       | a g e |

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 16, No. 9, 2025
to estimate efficiency gains and assess the contribution of Forevaluationpurposes,measurementsarecollectedhourly
SDN in optimizing consumption and enabling adaptive device and stored in two separate lists: one for the baseline (no duty
management. cycling energy history) and another for the scheduled case
(dutycyclingenergyhistory).Adirectcomparisonismadebe-
Step 2:Thecodewasimprovedbyintroducinganewidea tweenthetwoliststoderivethereductionratioinconsumption,
to track power consumption in the “No Slicing” state. A base- with a stratified analysis comparing performance during peak
line was established for the No Slicing case, recording power hours versus quiet periods to measure the system’s response
consumptionforeachdevicecategorywithfixedreferenceval- to load changes. This procedure provides a clear, systematic
ues:sensors(10units),cameras(8units),andlighting(6units). description: defining reference capabilities for each device
Representativedevicevalues(10sensors,8cameras,6lighting category, enforcing scheduling via SDN, consistent hourly
units)wereselectedbasedonreal-worlddatasheetssuchasthe measurement, and then an organized before/after comparison,
NXP SLN-VIZN-IoT platform (≈ 0.9W) when the camera is which allows for a more accurate estimation of the efficiency
on) and the LSM6DSV16X sensor from STMicroelectronics, gainsresultingfrommanagingon/offstatesaccordingtoaduty
as well as low-power optical sensors (193–277 µW). This cycling schedule.
distributionisfurthersupportedbytheresultsofthepaper[26],
whichprovidedpracticalmeasurementsofpowerconsumption
C. Case3 CNN + BiLSTM (Scenario 3) Model Training
in real industrial environments. These values were developed
to standardize comparison conditions and highlight the impact A new AI-driven network slicing model (Scenario 3) has
of energy optimization techniques, particularly duty cycle and been developed to dynamically improve resource allocation.
grid slicing [45]. It relies on a hybrid architecture that combines (CNN for
feature extraction) and (BiLSTM for capturing temporal de-
The results of this case are stored in the no-slicing energy pendencies), classifying network flows into five categories:
history list and are used with different network sizes to test (super-eMBB, massive-MTC, super-URLLC, ultra-precise ap-
robustness and allow subsequent replacement with real data plications, and ultra-immersive experiences). The Unicauca IP
without changing the methodology. When applying dynamic Flowdatasetwasusedwithan80testingsplit,andperformance
slicing within an SDN environment, power is allocated ac- was measured using Precision, Recall, and F1 metrics. The
cording to peak periods; specific categories (such as sensors) classification outputs guide the decision on slice assignment
remain active while others are disabled during idle times, and and resource allocation, and then the energy consumed before
power is measured using the calculate energy function. In this and after allocation is compared; this demonstrates a better
case, the readings are stored in the slicing energy history list, alignment between network traffic requirements, reduced en-
andadirectcomparisonismadebetweentheno-slicingenergy ergy consumption, and support for efficient slice management
history and slicing energy history lists to measure efficiency in 6G environments. The study examined the scalability by
gains and estimate the actual reduction in consumption. increasing the number of devices between 500 and 2500
devices, measuring the power consumption of each device as
Step 3: The simulation of the 6G-IoT network was ex-
the size changed, and analyzing the relationship between the
panded with SDN management to cover multiple slicing use
numberofdevicesandenergyefficiency.ThefeaturesofCNN
cases across three device categories (50, 500, and 2,500
and BiLSTM were combined through a concatenation layer,
devices). Slicing divides the network into smaller, service-
and the model was trained on 80% of the data and evaluated
oriented segments, reducing energy consumption by distribut-
on the remaining portion; the results indicate an improvement
ingloadsmoreefficiently.Foreachcategory,energyconsump-
in efficiency after model-based optimization, as shown in Fig.
tion is measured in both the non-partitioned and partitioned
1
states, and then the percentage reduction attributed to the
application of partitioning is calculated.
B. Case 2 Duty Cycling (Scenario 2)
Fig.1.Thearchitectureofabasicconvolutionalneuralnetwork(CNN).
DutyCyclingisappliedasatime-basedcontrolmechanism
to turn devices on and off with the aim of reducing overall
Components of the CNN Model Used:
energy consumption. In the experimental design, the devices
are activated during even hours and deactivated during odd
• Input Layer: This layer takes in the data that has
hours, and the consumption of each device is calculated
already been prepared for processing
according to its operational state and type. A fixed reference
power is used to represent the nominal consumption during • Shape Used: The data is organized in a one-
continuous operation: sensors 10 watts, cameras 8 watts, dimensional format for each feature, represented as
and lighting 6 watts. The SDN controller holds the control (features. Shape [1], 1).
layer. It activates/deactivates devices according to the duty
• Convolutional Layer: This is the first layer of the
cycleschedule,ensuringconsistenttransitionsbetweenthetwo
model,whereitappliesamathematicaloperation.The
states(active/inactive)atthenetworklevel.Abaselinewithout
model examines three interconnected values simulta-
duty cycling is defined where devices are considered always
neously, which enables it to recognize patterns
active, Energy is calculated hour by hour as the sum of the
consumption of active devices only, allowing the isolation of • Kernel Size: The model looks at three connected
the impact of scheduling from other factors. values at once, which helps it recognize patterns.
www.ijacsa.thesai.org 932 | P a g e

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 16, No. 9, 2025
• Activation Function: The ReLU (Rectified Linear
Unit) function is used here. It helps the model handle
complex, non-linear relationships in the data.
• Pooling Layer: This layer reduces the number of
features from the convolutional layer by selecting the
highest value from small groups in the data. The
pooling size is set to 2, meaning it looks at every
two values.
• Flatten Layer: This layer transforms the multi-
dimensional data into a one-dimensional format so
that it can be processed by the following layers in
the network.
• Dense Layer: This layer has 128 units (or neurons),
anditalsousestheReLUfunctiontohelpimprovethe
model’s performance. This layer is key in identifying
andfinalizingtheimportantpatternsfromthefeatures
extracted earlier.
• Dropout Layer: To prevent the model from becoming Fig.2.ConceptualunifiedframeworkintegratingAI-slicing,dutycycling,
too reliant on specific neurons (a problem known as andSDNforenergy-efficientandscalable6G-IoTnetworks.
overfitting), this layer randomly ignores 30% of the
neurons during training.
Integration with BiLSTM: The features extracted from VII. RESULT
the CNN are combined with the results from the BiL-
This section presents the experimental results obtained
STM’s analysis of time dependencies in a concatenation
from the three proposed scenarios: SDN-based dynamic slic-
layer, which enhances the overall accuracy of the model.
ing, duty cycling, and the hybrid CNN–BiLSTM model.
To strengthen the proposed methodology, we integrated our
The evaluation focuses on energy consumption, scalability
hybrid CNN–BiLSTM segmentation model into a broader
with increasing numbers of devices, and classification ac-
comparison framework that considers recent energy-efficient
curacy for traffic flows. To provide a broader perspective,
approaches such as Reinforcement Learning (RL) and Feder-
the CNN–BiLSTM results are further compared with recent
ated Learning (FL). While our primary focus remains on deep
energy-efficientapproaches,includingReinforcementLearning
sequence modeling of traffic flows, RL-based network slicing
(RL) and Federated Learning (FL). Figures and tables are
has demonstrated strong adaptability for energy-aware policy
included to illustrate the performance metrics and highlight
design, and FL has shown the ability to train collaborative
the improvements achieved.
intrusion/traffic models with high accuracy in distributed IoT
settings.Therefore,weincludedthesetechniquesinourbench-
marking to contextualize the CNN–BiLSTM results within A. Scenario1:ResultofImplementingSDNTechnologyin6G-
state-of-the-art6G-IoToptimizationstrategies.Thisintegration IoT Networks Scenario 1)
not only allows a fair benchmarking against RL and FL
approaches but also directly relates to our core objectives of 1)FirstimplementingSDNtechnologyin6G-IoTnetworks:
reducingenergyconsumptionandimprovingscalabilityin6G- Asimulationmodelfora6G-IoTnetworkwasdevelopedusing
IoT environments. SDN technology to reduce energy consumption and improve
networkperformancebyapplyingdynamicslicing.Themodel
D. Conceptual Unified Framework Integrating was built using the networkx library to create and analyze
network diagrams, the numpy [23] library for mathematical
Conceptual Unified Framework Integrating AI-Slicing, calculations, the matplotlib library for visualizing data, and
DutyCycling,andSDNforEnergy-EfficientandScalable6G- the random library for generating random number [31]s.
IoT Networks.
Thirty devices were integrated into the network, includ-
Fig. 2 illustrates the proposed conceptual unified frame-
ing sensors, cameras, and lighting, with each device’s status
work. First, node-level application requirements are clustered
assigned as active or passive based on specific rules such as
using the AI-slicing module, which uses artificial intelligence
peak hours and energy requirements.
to create logical network segments based on similar needs.
Next, the duty cycling module, which controls when devices Fig.3showsacomparisonofenergyconsumptionina6G-
are active or inactive to save energy, filters the grouped nodes IoT network before and after implementing dynamic slicing.
based on set energy thresholds. Finally, the SDN (Software- The results show that the dotted blue line, representing the
Defined Networking) controller, which centralizes the man- powerconsumptionwithoutslicing,remainsalmostconstantat
agement of data flow across the network, routes and allocates approximately115unitsacrossallhoursoftheday.Incontrast,
resources to the active nodes in an energy-aware manner. the green line, representing the system with dynamic slicing,
The combined workflow ensures optimized energy usage and shows a clear variation in consumption, ranging from 60-106
scalable operation in large-scale 6G-IoT deployments. units depending on peak times.
www.ijacsa.thesai.org 933 | P a g e

|     |     |     |     |     | (IJACSA) | International | Journal      | of Advanced |        | Computer |          | Science | and Applications, |           |
| --- | --- | --- | --- | --- | -------- | ------------- | ------------ | ----------- | ------ | -------- | -------- | ------- | ----------------- | --------- |
|     |     |     |     |     |          |               |              |             |        |          |          | Vol.    | 16, No.           | 9, 2025   |
|     |     |     |     |     |          |               | consumption  | during      | peak   | hours    | reached  |         | 94.62 units,      | while     |
|     |     |     |     |     |          |               | it decreased | further     | during |          | off-peak | hours   | to 69.18          | units,    |
|     |     |     |     |     |          |               | reflecting   | the ability | of     | dynamic  | slicing  |         | to adapt          | to demand |
fluctuations.
|     |     |     |     |     |     |     | In this       | phase,        | estimated |        | power | consumption  |       | values      |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------- | --------- | ------ | ----- | ------------ | ----- | ----------- |
|     |     |     |     |     |     |     | were assigned |               | to each   | type   | of    | device       | based | on values   |
|     |     |     |     |     |     |     | reported      | in scientific |           | papers | and   | manufacturer |       | datasheets. |
AsexplainedpreviouslyintheproposedMethodologysection.
Fig.3.Comparisonofenergyconsumptionbeforeandafternetworkslicing
in6G-IoTusingSDN(Step1).
| 2)Second,           | improving |           | the measurement |      | model:                | In the sec- |     |     |     |     |     |     |     |     |
| ------------------- | --------- | --------- | --------------- | ---- | --------------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ond phase,          | the       | model was | developed       |      | by assigning          | specific    |     |     |     |     |     |     |     |     |
| power consumption   |           | values    | to each         | type | of device(Sensors:    | 10          |     |     |     |     |     |     |     |     |
| units (continuously |           | active)   | - Cameras:      |      | 8 units (continuously |             |     |     |     |     |     |     |     |     |
| active)-            | Lighting: | 6 units   | (continuously   |      | active)               |             |     |     |     |     |     |     |     |     |
Fig.6.Energyconsumptionwithandwithoutnetworkslicingin6G
networksacrossthreedevicecategories(50,500,and2,500)devices.)
|     |     |     |     |     |     |     | Fig.        | 6 presents | the    | results  | of Scenario |     | 1, where | the energy |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------ | -------- | ----------- | --- | -------- | ---------- |
|     |     |     |     |     |     |     | consumption | of         | 6G-IoT | networks |             | was | measured | with and   |
withouttheapplicationofSDN-baseddynamicslicing.Theex-
|     |     |     |     |     |     |     | periments    | were conducted |          | across      | three      | different    | device          | scales      |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | -------- | ----------- | ---------- | ------------ | --------------- | ----------- |
|     |     |     |     |     |     |     | (50, 500,    | and 2500).     |          | The results | show       | a            | clear reduction | in          |
|     |     |     |     |     |     |     | energy usage | when           | slicing  | is          | enabled,   | highlighting |                 | the ability |
|     |     |     |     |     |     |     | of SDN       | to optimize    | resource |             | allocation | under        | varying         | traffic     |
loads.
Fig.4.Comparisonofenergyconsumptionbeforeandafternetworkslicing
in6G-IoTusingSDN(Step2).
| Fig.         | 4 compares | energy | usage        | in a | 6G IoT           | network with |     |     |     |     |     |     |     |     |
| ------------ | ---------- | ------ | ------------ | ---- | ---------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| (SDN) before | and        | after  | implementing |      | dynamic slicing. |              |     |     |     |     |     |     |     |     |
Fig.7.Comparisonofpowerconsumptionwithandwithoutslicing.
|     |     |     |     |     |     |     | 3)Thrid, | the | simulation |     | of the | 6G-IoT | network | was ex- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | --- | ------ | ------ | ------- | ------- |
Fig.5.Evaluatingenergyconsumptionusing(SDN)beforeandafter
panded: SDNmanagementtocovermultipleslicingusecases
implementingdynamicslicing.
|     |     |     |     |     |     |     | across three    | device | categories |             | (50,     | 500,             | and 2,500    | devices). |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | ---------- | ----------- | -------- | ---------------- | ------------ | --------- |
|     |     |     |     |     |     |     | Slicing divides | the    | network    | into        | smaller, | service-oriented |              | seg-      |
|     |     |     |     |     |     |     | ments to        | reduce | energy     | consumption |          | by               | distributing | loads     |
Fig. 5 shows that energy consumption in the no-slicing more efficiently. For each category, energy consumption is
scenario remained constant at an average value of 246 units, measured in both the non-partitioned and partitioned states,
withnovariationbetweenpeakandoff-peakhours.Incontrast,
|               |     |         |                |     |        |               | and then        | the percentage |             | reduction | attributed |     | to the | application |
| ------------- | --- | ------- | -------------- | --- | ------ | ------------- | --------------- | -------------- | ----------- | --------- | ---------- | --- | ------ | ----------- |
| the SDN-based |     | slicing | Implementation |     | showed | a significant |                 |                |             |           |            |     |        |             |
|               |     |         |                |     |        |               | of partitioning | is             | calculated. |           |            |     |        |             |
decreaseinconsumption,averaging82.96unitswithvariations
ranging from 53 to 106 units, achieving an energy savings Fig.7illustratesacomparisonofpowerconsumptionunder
rate of up to 66.28%. The results also showed that energy the following scenarios:
|     |     |     |     |     |     | www.ijacsa.thesai.org |     |     |     |     |     |     | 934 | | P a g e |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --------- |

|           |          |            |      |                  |     | (IJACSA) |          | International | Journal | of Advanced | Computer |     | Science | and Applications, |         |
| --------- | -------- | ---------- | ---- | ---------------- | --- | -------- | -------- | ------------- | ------- | ----------- | -------- | --- | ------- | ----------------- | ------- |
|           |          |            |      |                  |     |          |          |               |         |             |          |     | Vol.    | 16, No.           | 9, 2025 |
| • Without |          | Slicing:   | This | reflects         | the | power    | drawn    | when          |         |             |          |     |         |                   |         |
| slicing   |          | techniques | are  | not implemented. |     |          |          |               |         |             |          |     |         |                   |         |
| • With    | Slicing: |            | This | indicates        | the | power    | consumed |               |         |             |          |     |         |                   |         |
aftertheapplicationofslicingandpoweroptimization
methods.
| Dark             | red signifies |         | power      | consumption   |             | in          | the absence |         |     |     |     |     |     |     |     |
| ---------------- | ------------- | ------- | ---------- | ------------- | ----------- | ----------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| of slicing.      | Light         | green   | indicates  |               | power       | consumption |             | when    |     |     |     |     |     |     |     |
| slicing is       | utilized.     | In      | the graph, | it            | is evident  | that        | the         | power   |     |     |     |     |     |     |     |
| consumption      | with          | slicing | is         | substantially |             | lower       | in each     | sce-    |     |     |     |     |     |     |     |
| nario compared   |               | to the  | cases      | without       | slicing.    | As          | observed    | an      |     |     |     |     |     |     |     |
| increasing       | the           | number  | of devices |               | correlates  | with        | a           | greater |     |     |     |     |     |     |     |
| percentage       | reduction     | in      | power      | usage.        |             |             |             |         |     |     |     |     |     |     |     |
| B. Scenario      | 2:            | Results | of         | Energy        | Consumption |             | With        | and     |     |     |     |     |     |     |     |
| Without Applying |               | Duty    | Cycling    |               |             |             |             |         |     |     |     |     |     |     |     |
Fig.9.FigureX:Energyconsumptionresultsundertwosettings:(i)noduty
cycling,and(ii)withdutycycling.Includesdetailedstatistics(mean,
standarddeviation,minima,maxima),comparisonduringpeakandnon-peak
hours,andoverallsavingspercentage.
|     |     |     |     |     |     |     |     |     | during peak    | and off-peak    |             | hours. | In contrast, | applying    | duty   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------------- | ----------- | ------ | ------------ | ----------- | ------ |
|     |     |     |     |     |     |     |     |     | cycling        | reduced average | consumption |        | to 87.50     | units,      | with a |
|     |     |     |     |     |     |     |     |     | fluctuation    | range of 0–175  | units.      | This   | mechanism    | achieved    | an     |
|     |     |     |     |     |     |     |     |     | energy savings | rate            | of 63.54%.  | The    | results      | also showed | that   |
averageconsumptionduringpeakhourswas94.23units,while
duringoff-peakhoursitdecreasedto79.55units,reflectingthe
|     |     |     |     |     |     |     |     |     | effectiveness | of duty    | cycling     | in adjusting | device      | consumption |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | ----------- | ------------ | ----------- | ----------- | --- |
|     |     |     |     |     |     |     |     |     | according     | to periods | of activity | and          | inactivity. |             |     |
Fig.8.EvaluatingenergyconsumptionandsavingsusingDutyCycling
technology.
|     |     |     |     |     |     |     |     |     | C. Scenario | 3: CNN | + BiLSTM | Model | Powered | by  | Machine |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | -------- | ----- | ------- | --- | ------- |
Language
| Fig. 8     | shows  | a comparison |       | between      |     | energy    | consumption |       |              |                 |                   |         |           |            |           |
| ---------- | ------ | ------------ | ----- | ------------ | --- | --------- | ----------- | ----- | ------------ | --------------- | ----------------- | ------- | --------- | ---------- | --------- |
|            |        |              |       |              |     |           |             |       | The          | key performance | metrics—accuracy, |         |           | precision, | recall,   |
| before and | after  | use of       | duty  | cycling.     |     |           |             |       |              |                 |                   |         |           |            |           |
|            |        |              |       |              |     |           |             |       | and F1-score | are calculated  |                   | using   | specific  | formulas   | [31].     |
| • The      | X-axis | shows        | time  | measured     |     | in hours. |             |       |              |                 |                   |         |           |            |           |
|            |        |              |       |              |     |           |             |       | Recall       | is a measure    | of                | how     | many true | positives  | were      |
|            |        |              |       |              |     |           |             |       | identified,  | which means     | it                | reveals | how many  | correct    | results   |
| • The      | Y-axis | shows        | power | consumption, |     |           | but the     | units |              |                 |                   |         |           |            |           |
|            |        |              |       |              |     |           |             |       | were found   | among           | the total         | cases   | that      | should     | have been |
| are        | not    | specified.   |       |              |     |           |             |       |              |                 |                   |         |           |            |           |
recognized.
Showsacomparisonbetweenenergyconsumptionwithand
without duty cycling. The dashed blue line remains constant TP
at a high level, close to the upper limit (240), reflecting Recall= (1)
TP +FN
| the continuous |     | operation | of  | the devices |     | without | responding |     |     |     |     |     |     |     |     |
| -------------- | --- | --------- | --- | ----------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
to load changes. In contrast, the orange curve exhibits a Precision: The proportion of hits that are truly positive or
| periodic | oscillating | behavior, |     | peaking | during | activation |     | hours |          |             |            |     |     |     |     |
| -------- | ----------- | --------- | --- | ------- | ------ | ---------- | --- | ----- | -------- | ----------- | ---------- | --- | --- | --- | --- |
|          |             |           |     |         |        |            |     |       | accurate | is known as | precision. |     |     |     |     |
anddroppingsharplytonearlyzeroduringdeactivationhours,
| which is                                             | consistent | with      | an         | alternating | on/off |      | schedule. | The  |     |            |     |     |     |     |     |
| ---------------------------------------------------- | ---------- | --------- | ---------- | ----------- | ------ | ---- | --------- | ---- | --- | ---------- | --- | --- | --- | --- | --- |
| peaksarebelowthefixedbaseline,andthelowperiodsreduce |            |           |            |             |        |      |           |      |     |            |     |     | TP  |     |     |
|                                                      |            |           |            |             |        |      |           |      |     | Precision= |     |     |     |     | (2) |
|                                                      |            |           |            |             |        |      |           |      |     |            |     | TP  | +FP |     |     |
| the area                                             | under      | the curve | throughout |             | the    | day, | resulting | in a |     |            |     |     |     |     |     |
lowerdailyaverageandalowertotalconsumption.Thispattern
demonstrates the effectiveness of duty cycling in aligning F1 Score: The F1 score is a metric that combines both
consumption with actual demand, with an expected increase recall and precision (accuracy). It ranges from 0 to 1 and is
in temporal variation against a clear improvement in energy calculated as an asymmetrical mean of recall and accuracy.
| efficiency. | It is | recommended |     | to  | conduct | a complementary |     |     |     |     |     |     |     |     |     |
| ----------- | ----- | ----------- | --- | --- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
statistical analysis (mean, standard deviation, and area under Precision×Recall
the curve) and assess the impact on service quality during F1-score=2× (3)
Precision+Recall
| downtime | hours | to adjust | the | optimal | cycle | parameters. |     |     |     |     |     |     |     |     |     |
| -------- | ----- | --------- | --- | ------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig. 9 shows that power consumption during no-duty Accuracy:Thepercentageofaccuratelyanticipatedvalues
cycling remained constant at 240 units, with no variations for the test data is used to evaluate accuracy. By dividing
|     |     |     |     |     |     |     | www.ijacsa.thesai.org |     |     |     |     |     |     | 935 | | P a g e |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --------- |

|              |           |            |           |             |             |          | (IJACSA) | International | Journal | of  | Advanced | Computer | Science | and  | Applications, |      |
| ------------ | --------- | ---------- | --------- | ----------- | ----------- | -------- | -------- | ------------- | ------- | --- | -------- | -------- | ------- | ---- | ------------- | ---- |
|              |           |            |           |             |             |          |          |               |         |     |          |          |         | Vol. | 16, No. 9,    | 2025 |
| the total    | number    | of         | forecasts | by          | the total   | number   | of       | accurate      |         |     |          |          |         |      |               |      |
| guesses,     | one can   | easily     | determine |             | the result. |          |          |               |         |     |          |          |         |      |               |      |
|              |           |            |           | TP          | +TN         |          |          |               |         |     |          |          |         |      |               |      |
|              | Accuracy= |            |           |             |             |          |          | (4)           |         |     |          |          |         |      |               |      |
|              |           |            | TP        | +TN         | +FP         | +FN      |          |               |         |     |          |          |         |      |               |      |
| Python       | is        | used to    | develop   | a           | simulation  | model    | using    | the           |         |     |          |          |         |      |               |      |
| “TensorFlow” |           | and “Keras |           | libraries”. | These       | packages |          | are im-       |         |     |          |          |         |      |               |      |
portanttoolsforcreatingneuralnetwork-baseddesigns.Inthis
| work, the | performance |       | of the  | proposed |             | hybrid | CNN-BiLSTM |         |     |     |     |     |     |     |     |     |
| --------- | ----------- | ----- | ------- | -------- | ----------- | ------ | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| model is  | evaluated   | using | several |          | performance |        | metrics,   | includ- |     |     |     |     |     |     |     |     |
Fig.11.ROCcurveresultsoftheproposedmodel.
| ing accuracy,      |     | recall,  | precision, | and           | F1  | score. | The parameters |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | ---------- | ------------- | --- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| of the performance |     | matrices |            | are described |     | in the | following:     | In  |     |     |     |     |     |     |     |     |
Fig.10,themodelachievedconsistentlyhighperformancewith
precisionandrecallvaluesexceeding0.98acrossmostclasses,
|         |           |            |     |         |            |       |                 |     | Fig.           | 11 shows     | that  | all IoT | network        | models     | achieved   | an  |
| ------- | --------- | ---------- | --- | ------- | ---------- | ----- | --------------- | --- | -------------- | ------------ | ----- | ------- | -------------- | ---------- | ---------- | --- |
| leading | to strong | F1-scores  |     | ¿ 0.98. | The        | large | support         | for |                |              |       |         |                |            |            |     |
|         |           |            |     |         |            |       |                 |     | Area Under     | the          | Curve | (AUC)   | of 1.00,       | confirming | excellent  |     |
| classes | such as   | super-eMBB |     | further | reinforces |       | the reliability |     |                |              |       |         |                |            |            |     |
|         |           |            |     |         |            |       |                 |     | classification | performance. |       |         | This indicates | that       | the models |     |
of these metrics.
|                  |               |                       |                |               |               |              |            |           | consistently | deliver | the | intended | results | with high | accuracy. |     |
| ---------------- | ------------- | --------------------- | -------------- | ------------- | ------------- | ------------ | ---------- | --------- | ------------ | ------- | --- | -------- | ------- | --------- | --------- | --- |
| Experimental     |               | results               |                | demonstrate   |               | that         | the        | proposed  |              |         |     |          |         |           |           |     |
| CNN–BiLSTM       |               | model                 | achieved       |               | high accuracy |              | in traffic | flow      |              |         |     |          |         |           |           |     |
| classification,  |               | reachingapproximately |                |               | 99%,          | witha        | remarkable |           |              |         |     |          |         |           |           |     |
| balance          | between       | precision             |                | and           | recall.       | When         | compared   | to        |              |         |     |          |         |           |           |     |
| other algorithms |               | such                  | as             | reinforcement |               | learning     | (RL)       | [29]      |              |         |     |          |         |           |           |     |
| and federated    |               | learning              | (FL)           | [30],         | several       | distinct     |            | strengths |              |         |     |          |         |           |           |     |
| emerged.         | Reinforcement |                       | learning-based |               |               | segmentation |            | demon-    |              |         |     |          |         |           |           |     |
stratedstrongadaptabilitytodynamicnetworkloads,resulting
| in stable     | energy    | efficiency  |          | during        | periods | of      | heavy            | traffic. |     |     |     |     |     |     |     |     |
| ------------- | --------- | ----------- | -------- | ------------- | ------- | ------- | ---------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| In contrast,  | federated |             | learning | demonstrated  |         |         | high scalability |          |     |     |     |     |     |     |     |     |
| by supporting |           | distributed |          | training      | across  | a large | number           | of       |     |     |     |     |     |     |     |     |
| IoT devices,  | while     | reducing    |          | communication |         |         | costs. Although  |          |     |     |     |     |     |     |     |     |
RLandFLtechniquesdemonstratedcompetitiveperformance, Fig.12.Confusionmatrix.
| CNN–BiLSTM  |            | maintained |           | the lowest | false          | positive     |           | rate and |                 |                |        |               |        |         |                |     |
| ----------- | ---------- | ---------- | --------- | ---------- | -------------- | ------------ | --------- | -------- | --------------- | -------------- | ------ | ------------- | ------ | ------- | -------------- | --- |
| achieved    | the        | highest    | sustained |            | energy         | reduction    | (approxi- |          |                 |                |        |               |        |         |                |     |
|             |            |            |           |            |                |              |           |          | Fig.            | 12 presents    |        | the confusion | matrix | used    | to evaluate    |     |
| mately      | 60%),      | enhancing  | network   |            | sustainability |              | and       | deliver- |                 |                |        |               |        |         |                |     |
|             |            |            |           |            |                |              |           |          | the model’s     | classification |        | accuracy.     | The    | matrix  | highlights     |     |
| ing greater | efficiency |            | as        | the number |                | of connected |           | devices  |                 |                |        |               |        |         |                |     |
|             |            |            |           |            |                |              |           |          | the performance |                | across | different     | data   | classes | using standard |     |
increases.
|     |     |     |     |     |     |     |     |     | evaluation | parameters. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
Fig.10.ResultsofthehybridCNN–BiLSTMmodel.
Fig.13.Calibrationcurveoftheproposedmodel.
| Fig.            | 10 of  | the     | classification |           | report           | shows     |          | that the |               |                |               |                 |                      |             |              |      |
| --------------- | ------ | ------- | -------------- | --------- | ---------------- | --------- | -------- | -------- | ------------- | -------------- | ------------- | --------------- | -------------------- | ----------- | ------------ | ---- |
| CNN–BiLSTM      |        | model   | achieved       |           | high performance |           | in       | almost   |               |                |               |                 |                      |             |              |      |
|                 |        |         |                |           |                  |           |          |          | Fig.          | 13 illustrates |               | the calibration | curve                | analysis    | for          | net- |
| all categories, |        | with    | precision      | ranging   |                  | from      | 0.93     | to 0.99, |               |                |               |                 |                      |             |              |      |
|                 |        |         |                |           |                  |           |          |          | work slice    | classification |               | in              | 6G-IoT, specifically |             | examining    |      |
| while recall    | ranged |         | from           | 0.86 to   | 1.00.            | The       | F1-score | metric   |               |                |               |                 |                      |             |              |      |
|                 |        |         |                |           |                  |           |          |          | the model’s   | ability        | to            | predict         | probabilities        |             | accurately.  | The  |
| demonstrated    |        | a good  | balance        | between   |                  | precision | and      | recall,  |               |                |               |                 |                      |             |              |      |
|                 |        |         |                |           |                  |           |          |          | calibration   | curve          | is a valuable |                 | tool for evaluating  |             | the accuracy |      |
| with a minimum  |        | of 0.89 | and            | a maximum |                  | of 1.00.  | The      | overall  |               |                |               |                 |                      |             |              |      |
|                 |        |         |                |           |                  |           |          |          | of a system’s | operation      |               | based           | on specific          | parameters. |              |      |
| accuracy        | of the | model   | reached        |           | 99% with         | a         | weighted | mean     |               |                |               |                 |                      |             |              |      |
of nearly 0.99, confirming the model’s strength in classifying Fig. 14 compares power consumption before and after
| traffic flows | across | different |     | categories. |     |     |     |                       | slicing: |     |     |     |     |     |         |       |
| ------------- | ------ | --------- | --- | ----------- | --- | --- | --- | --------------------- | -------- | --- | --- | --- | --- | --- | ------- | ----- |
|               |        |           |     |             |     |     |     | www.ijacsa.thesai.org |          |     |     |     |     |     | 936 | P | a g e |

|                                                           |     |     |     | (IJACSA) |     | International | Journal       | of         | Advanced          | Computer         | Science         |             | and Applications, |              |
| --------------------------------------------------------- | --- | --- | --- | -------- | --- | ------------- | ------------- | ---------- | ----------------- | ---------------- | --------------- | ----------- | ----------------- | ------------ |
|                                                           |     |     |     |          |     |               |               |            |                   |                  |                 | Vol.        | 16,               | No. 9, 2025  |
|                                                           |     |     |     |          |     |               | 3)Scenario    |            | 3 – Machine       |                  | Learning-Driven |             | Segmentation:     |              |
|                                                           |     |     |     |          |     |               | Previous      | studies    | indicate          | that             | reinforcement   |             | learning          | (RL)         |
|                                                           |     |     |     |          |     |               | [29]in        | the 6G–IoT | context           |                  | achieved        | energy      | reductions        | of           |
|                                                           |     |     |     |          |     |               | 45–55%        | with       | high adaptability |                  | to              | changing    | network           | loads.       |
|                                                           |     |     |     |          |     |               | Federated     | learning   | (FL)[30]          |                  | demonstrated    |             | an efficiency     | of           |
|                                                           |     |     |     |          |     |               | 40–50%        | energy     | reduction,        | with             | clear           | superiority |                   | in scalabil- |
|                                                           |     |     |     |          |     |               | ity across    | thousands  | of                | connected        | devices         |             | without           | the need     |
|                                                           |     |     |     |          |     |               | to transfer   | raw        | data.             | Compared         | with            | these       | methods,          | our          |
|                                                           |     |     |     |          |     |               | CNN–BiLSTM    |            | model             | achieved         | the             | highest     | consistent        | energy       |
|                                                           |     |     |     |          |     |               | reduction     | of 60%     | with              | a classification |                 |             | accuracy          | of 99%,      |
|                                                           |     |     |     |          |     |               | demonstrating |            | its superior      | combination      |                 | of          | energy            | efficiency   |
| Fig.14.Comparisonofpowerconsumptionbeforeandafterslicing. |     |     |     |          |     |               | and high      | accuracy.  |                   |                  |                 |             |                   |              |
|                                                           |     |     |     |          |     |               |               |            | VIII.             | DISCUSSION       |                 |             |                   |              |
|                                                           |     |     |     |          |     |               | Scenario      | 1          | Fig.              | 5 highlights     | the             | importance  |                   | of slicing   |
|                                                           |     |     |     |          |     |               | as a dynamic  |            | mechanism         | for              | adapting        | to          | varying           | network      |
|                                                           |     |     |     |          |     |               | loads. While  | the        | traditional       | system           | (without        |             | slicing)          | exhibited    |
constant,inflexibleconsumption,slicingallowedforintelligent
|                                                               |     |     |     |     |     |     | control       | of energy | consumption |               | based       | on traffic     | intensity. | This         |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ----------- | ------------- | ----------- | -------------- | ---------- | ------------ |
|                                                               |     |     |     |     |     |     | variation     | between   | peak        | and           | off-peak    | hours          | indicates  | that         |
|                                                               |     |     |     |     |     |     | SDN-based     | slicing   | not         | only achieves |             | an overall     |            | reduction in |
|                                                               |     |     |     |     |     |     | consumption   | but       | also        | enhances      | network     | sustainability |            | by bal-      |
|                                                               |     |     |     |     |     |     | ancing        | energy    | efficiency  | with          | maintaining |                | quality    | of service.  |
|                                                               |     |     |     |     |     |     | This lays     | the       | foundation  | for           | adopting    | slicing        | techniques | as           |
|                                                               |     |     |     |     |     |     | an essential  | part      | of energy   | management    |             | strategies     |            | in 6G-IoT    |
| Fig.15.Comparisonofenergyconsumptionwithandwithouttheproposed |     |     |     |     |     |     | environments. |           |             |               |             |                |            |              |
techniques.
|     |     |     |     |     |     |     | Fig.        | 6, the      | results | indicate    | that slicing |           | technology | signif-     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ------- | ----------- | ------------ | --------- | ---------- | ----------- |
|     |     |     |     |     |     |     | icantly     | reduced     | energy  | consumption |              | across    | different  | network     |
|     |     |     |     |     |     |     | sizes, with | consumption |         | decreasing  |              | by 41.81% | at         | 50 devices, |
Fig. 15 compares the energy usage of 6G-IoT networks by40.95%at500devices,andby39.52%at2,500devices.Al-
beforeandaftertheintroductionofnetworkslicingtechnology.
thoughtheenergysavingsgraduallydecreasewiththeincreas-
|     |     |     |     |     |     |     | ing number | of  | devices, | this reflects | slicing’s |     | ability | to achieve |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ------------- | --------- | --- | ------- | ---------- |
stableenergyefficiencyeveninenvironmentswithhighdevice
density.ThishighlightstheimportanceofadoptingSDN-based
|     |     |     |     |     |     |     | slicing | as a strategic | option | for | improving |     | scalability | in 6G- |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | ------ | --- | --------- | --- | ----------- | ------ |
IoTnetworks,asitprovidesabalancebetweenreducingenergy
consumptionandensuringqualityofserviceamidthemassive
|     |     |     |     |     |     |     | expansion | of the | number       | of connected |      | devices.     |     |             |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------------ | ------------ | ---- | ------------ | --- | ----------- |
|     |     |     |     |     |     |     | Scenario  | 2      | Fig.         | 9 indicates  | that | adopting     | a   | duty cycle  |
|     |     |     |     |     |     |     | mechanism | is     | an effective | strategy     |      | for reducing |     | energy con- |
sumptioninIoTenvironmentswithin6Gnetworks.Thismech-
|     |     |     |     |     |     |     | anism periodically |     | shuts         | down      | devices | during    | idle         | periods, |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------- | --------- | ------- | --------- | ------------ | -------- |
|     |     |     |     |     |     |     | contributing       | to  | a significant | reduction |         | in energy | consumption. |          |
Thevariationinconsumptionbetweenpeakandoff-peakhours
Fig.16.Energyconsumptionvs.numberofdevicesin6G-IoT.
|     |     |     |     |     |     |     | highlights | the | flexibility | of  | this technology |     | in  | adapting to |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | --- | --------------- | --- | --- | ----------- |
differentusagepatterns,enhancingitsscalabilityasthenumber
Fig. 16 shows the relationship between the number of of connected devices increases. Therefore, duty cycle not
connected devices (500–2500). only provides a significant reduction in energy consumption
|     |     |     |     |     |     |     | but is | also a | practical | option | that | can | be combined | with |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --------- | ------ | ---- | --- | ----------- | ---- |
D. Summary of the Results other strategies such as SDN slicing to achieve greater energy
|             |                  |     |                 |         |             |         | management | efficiency. |             |          |     |          |          |       |
| ----------- | ---------------- | --- | --------------- | ------- | ----------- | ------- | ---------- | ----------- | ----------- | -------- | --- | -------- | -------- | ----- |
| 1)Scenario  | 1 – Segmentation |     | via SDN:        | Reduced |             | overall |            |             |             |          |     |          |          |       |
|             |                  |     |                 |         |             |         | Scenario   | 3           | This result | reflects |     | that the | proposed | model |
| consumption | by 66.28%.       | In  | the scalability | test,   | the savings |         |            |             |             |          |     |          |          |       |
reached 41.81% (50 devices), 40.95% (500), and 39.52% has a very high level of reliability and generalizability. The
|                    |     |               |            |             |     |     | model’s             | superior | performance |      | is attributed |         | to the   | combination |
| ------------------ | --- | ------------- | ---------- | ----------- | --- | --- | ------------------- | -------- | ----------- | ---- | ------------- | ------- | -------- | ----------- |
| (2500), confirming | the | effectiveness | of slicing | independent |     | of  |                     |          |             |      |               |         |          |             |
|                    |     |               |            |             |     |     | of the capabilities |          | of          | CNNs | to extract    | spatial | features | with        |
network size.
|     |     |     |     |     |     |     | the strength | of  | BiLSTMs | to  | capture | temporal | dependencies. |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | --- | ------- | -------- | ------------- | --- |
2)Scenario 2 – Duty Cycling: Achieved a reduction of The proposed model exhibits similar or superior performance
63.54%; consumption was 94.23 units during peak hours and to recent models such as [47]which achieved 99% accuracy
79.55 units during off-peak hours. using Attention-Based CNN-BiLSTM on N-BaIoT data, and
|     |     |     |     |     | www.ijacsa.thesai.org |     |     |     |     |     |     |     | 937 | | P a g e |
| --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 16, No. 9, 2025
also Sinha et al. (2025) with 99.87% accuracy and a very low Areasforimprovement:Thesuper-immersiveclassshows
false positive rate [48], supporting that fusion provides a real roomforimprovement,perhapsthroughmoredataorimproved
improvement in deep learning for similar problems. model architecture.
Fig. 10 show this result: Fig. 11 presents the Receiver Operating Characteristic
(ROC) curve, which illustrates the connection between true
Precision: The ratio of the number of samples correctly
positive rates (TPR) and false positive rates (FPR) for IoT
classified for a given class to the total number of samples
networks. Here, the FPR shows how often a test incorrectly
classified as belonging to that class.
identifies a positive result, while the TPR shows how often
High precision (> 0.99) for classes such as super-eMBB the test correctly identifies a negative result. All the networks
and massive-MTC shows the model’s ability to reduce false haveanAreaUndertheCurve(AUC)of1.00,whichindicates
positives. thattheyareperformingverywellandachievingtheirintended
goals efficiently. The fact that every network shows an AUC
Recall: the ratio of the number of samples correctly
of 1.00 confirms their effectiveness in delivering the desired
classifiedforagivenclasstothetotalnumberofactualsamples
results.
for that class.
Fig. 12 displays the confusion matrix, which is a tool
Strong recall (0.98–1.00) for most classes shows the
used to determine how accurate a model is when comparing
model’s ability to capture almost all correct samples.
different types of data. This matrix helps in assessing the
F1-Score: A metric that balances precision and recall. performanceofmodel.Theaccuracyofthemodelismeasured
using the following parameters:
High values (> 0.98) for a model show its strong and
balanced performance. • True label: Represents the actual class of the data as
it appears in the dataset.
Support: Indicates the number of samples in each class.
For example, the super-eMBB class has very high support • Predicted label: Represents the class that the model
(347,683samples),whichenhancestheaccuracyofthemetrics has assigned to the data based on its prediction.
due to its large representation.
• Diagonal values: Indicate correctly classified in-
Class Analysis: super-eMBB: Precision: 0.99, Recall: stances where the predicted label matches the true
1.00, F1-Score: 1.00. label. Higher values along the diagonal signify better
classification accuracy.
• The perfect performance in this class reflects
the model’s ability to accurately recognize high- • Super-eMBB: The Super-eMBB category has the
bandwidth applications such as video streaming highest number of correctly classified instances
(346,613),indicatingstrongmodelperformanceinthis
massive-MTC: Precision: 0.99, Recall: 0.98, F1-Score: 0.99.
category.
• This class has a large number of connected devices,
• Massive-MTC: The Massive-MTC category demon-
andthehighperformanceshowsthesuccessofmodel
strates a high number of correctly classified instances
in dealing with this challenge.
(56,707), though some misclassifications are present.
super-URLLC: Precision: 0.99, Recall: 0.97, F1-Score: 0.98. • Super-URLLC: The Super-URLLC category has
9,608 correctly classified instances, with some con-
• Good performance in latency-sensitive applications
fusion among other categories, indicating room for
such as industrial control.
improvement in classification accuracy.
super-precision:Precision:0.99,Recall:1.00,F1-Score:0.99.
Fig. 13 shows the calibration curve. It compares predicted
• The strong performance reflects the model’s ability to outcomes with actual results [46]. The X-Axis allows us to
handle high-precision applications. compare predicted values to the real values, and the Y-Axis
shows how many predictions were positive based on those
Super-immersive: Accuracy: 0.93, Recall: 0.86, F1-Score: calculations. The diagonal line in the figure represents perfect
0.89. performance,meaningthepredictedprobabilitiesalignexactly
with the true outcomes. When a point falls on this line, it
• Although the performance in this category is lower
signifies that the model is making accurate predictions.
than the other categories, the model shows a rea-
sonable improvement in applications with complex For the different classes—super-eMBB, massive-MTC,
requirements such as virtual reality. super-URLLC, and super-precision—most points are very
close to the ideal line, showing that the model works well for
Finally,theresultreflectsstrongperformanceofthemodel
predicting probabilities in these cases. However, some points
across all categories with a particular focus on achieving a
deviatefromtheidealline,suggestingthattherearedifficulties
balance between precision and recall.
incalibratingthemodelfortheclasslabeledsuper-immersive.
Significant improvement: The results show improved
Use a Model for Power Consumption:
efficiencyinclassifyingdifferentsegments,supportingtheuse
of the model to improve resource management in 6G IoT Fig. 14 compares power consumption before and after
networks. slicing:
www.ijacsa.thesai.org 938 | P a g e

(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 16, No. 9, 2025
• Super-eMBB: This chip used 833.33 W, indicating it chips such as super-immersive reflect greater con-
isveryefficient(efficiencyratingof1.2)forbroadband sumption due to their higher requirements.
applications, such as video streaming.
Fig. 15 compares the energy usage of 6G-IoT networks
• Massive-MTC: It consumed 769.23 W, showing an
beforeandaftertheintroductionofnetworkslicingtechnology.
efficiency rating of 1.3, which is suitable for Internet
of Things (IoT) applications that need many connec-
• Before Slicing: The energy usage is represented by
tions while using less power.
the red column. This shows that before slicing, the
• Super-URLLC: This chip used 800.00 W, with an network was less efficient (η = 0.5) because it
efficiency rating of 1.15, making it fit for low-latency consumed a lot of power—up to 10,000 watts—even
applications like industrial control processes. for resources not assigned to any devices.
• Super-precision: It consumed 714.29 W and has the • After Slicing: The energy usage after implementing
highest efficiency rating of 1.4, making it ideal for slicing is illustrated in the green column. As shown,
taskssuchasmicro-analysisorworkingwithbigdata. energyconsumptiondecreasedto3,986.42watts.This
reduction indicates that the network’s efficiency has
• Super-immersive: This chip used 869.57 W. Al-
improved(η >1)becauseresourcesarenowallocated
though it is less efficient (efficiency rating of 1.05)
moreeffectivelybasedontheindividualneedsofeach
compared to the others, it still performs better than
network slice.
the traditional network.
• Reduction Ratio: Network slicing positively affects
Understanding the results: Energy efficiency measures
energy usage, resulting in a significant 60.14% de-
how much useful energy a system produces compared to
crease in power consumption.
the total energy it uses. It shows how well the system can
deliverthemostoutputwhileusingtheleastamountofenergy. Fig. 16 shows the relationship between the number of
Enhancing energy efficiency. connecteddevices(500–2500)andpowerconsumption:before
slicing(redline),consumptionincreaseslinearlywiththesize,
(cid:18) Useful energy output (cid:19) while it decreases after applying network slicing (green line)
η = ×100% (5)
due to improved resource allocation. The area between the
Total energy consumed
curves represents energy savings, and the increasing gap with
theriseinthenumberofdevicesindicatesimprovedefficiency
Where:
and scalability.
• η (eta) represents energy efficiency as a percentage
[%].
IX. CONCLUSION
• Useful energy output refers to the energy that is
actually used to perform the necessary work. This study revealed three separate strategies to optimize
energy usage and improve 6G network performance in IoT
• Total energy consumed is the complete amount of contexts with escalating device connectivity. Each method
energy that the system has taken in. was evaluated separately to elucidate its effect: 1) Dynamic
slicing utilizing SDN resulted in energy reduction surpassing
Value for η (eta)
66% by synchronizing device operation with actual usage.
• η = 1 indicates standard efficiency where there is no 2) Duty cycling decreased energy consumption by over 60%
improvement or additional energy loss. through an adaptive on/off mechanism. 3) A CNN–BiLSTM
classification model enhanced slice allocation, achieving high
• η > 1 means that the system is operating more effi- Precision and Recall while providing improved estimations
ciently than a conventional grid, either by improving of energy requirements by service. These results provide
performance or reducing losses. evidence of the efficacy of each technology and establish a
foundationforrealistic,consumption-conscious,andadaptable
• η < 1 indicates less than desired efficiency, meaning
resource management frameworks. Due to the complexity and
that there is significant loss in the grid or system.
unpredictability of 6G settings, adaptive operational solutions
BasedontheearlierformulaandourresultsshowninFig.14: that harmonize energy conservation with service quality are
becoming increasingly essential. Future research may expand
leftmargin=1.5em
this study to encompass simultaneous multi-layer resource
allocation, including spectrum, power, and processing time, to
• Efficiency:Thenetworkslicingallocatesresourcesso
attain holistic network performance enhancements in 6G–IoT
that the power usage of each chip is optimized based
contexts.
on its actual needs.
• Power reduction:Theslicingreducesthepowercon-
sumption significantly due to the reduction of waste ACKNOWLEDGMENT
in the network.
The authors gratefully acknowledge the invaluable guid-
• Balance: Highly efficient chips (such as super- ance, constructive feedback, and continuous support provided
precision) show greater power savings, while other bytheiracademicsupervisorsthroughouttheresearchprocess.
www.ijacsa.thesai.org 939 | P a g e

|     |     |     |     |     |     | (IJACSA) | International | Journal | of  | Advanced | Computer |     | Science | and | Applications, |      |
| --- | --- | --- | --- | --- | --- | -------- | ------------- | ------- | --- | -------- | -------- | --- | ------- | --- | ------------- | ---- |
|     |     |     |     |     |     |          |               |         |     |          |          |     | Vol.    | 16, | No. 9,        | 2025 |
REFERENCES works Based on Data Transmission Rate Allocation,” Deleted Journal,
2024,pp.182–190.doi:10.58496/bjn/2024/018
[1] F.Guo,F.R.Yu,H.Zhang,X.Li,H.Ji,andV.C.M.Leung,“Enabling
|         |            |     |                 |     |          |               |     | [20] A. | M. Elshewey |         | et al.,  | “DDoS       | classification | of         | network | traf- |
| ------- | ---------- | --- | --------------- | --- | -------- | ------------- | --- | ------- | ----------- | ------- | -------- | ----------- | -------------- | ---------- | ------- | ----- |
| massive | IoT toward | 6G: | A comprehensive |     | survey,” | IEEE Internet | of  |         |             |         |          |             |                |            |         |       |
|         |            |     |                 |     |          |               |     | fic in  | software    | defined | networks | environment |                | leveraging | an      | RNN-  |
ThingsJournal,vol.8,pp.11891–11915,2021.
basedmodel,”PMC,2025.Available:https://www.ncbi.nlm.nih.gov/pmc/
[2] J.A.Ansere,G.Han,H.Wang,C.Choi,andC.Wu,“Areliableenergy
articles/PMC12334730/
| efficient | dynamic | spectrum | sensing | for cognitive |     | radio IoT networks,” |     |                                                              |     |     |     |     |     |     |     |     |
| --------- | ------- | -------- | ------- | ------------- | --- | -------------------- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|           |         |          |         |               |     |                      |     | [21] S.SalemandS.Asoudeh,“AhybridIndRNN-LSTMapproachforreal- |     |     |     |     |     |     |     |     |
IEEEInternetofThingsJournal,vol.6,pp.6748–6759,2019.
|     |     |     |     |     |     |     |     | time | anomaly | detection | in software-defined |     | networks,” |     | arXiv | preprint, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------- | --------- | ------------------- | --- | ---------- | --- | ----- | --------- |
[3] M.B.Yassein,L.Al-Smadi,andL.Mrayan,“ASurveyofMobileHealth
2024.Available:https://arxiv.org/abs/2402.05943
| Applications | in  | Context | of Internet | of Things,” | in  | Proc. 7th | Int. Conf. |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------- | ----------- | ----------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
on Future Internet of Things and Cloud (FiCloud), Istanbul, Turkey, [22] A. Vaziri, P. S. Moghaddam, M. Shoeibi, and M. Kaveh, “Energy-
Aug.26–28,2019,pp.351–357. Efficient Secure Cell-Free Massive MIMO for Internet of Things: A
HybridCNN–LSTM-BasedDeep-LearningApproach,”FutureInternet,
[4] N.Zhang,S.Zhang,P.Yang,O.Alhussein,W.Zhuang,andX.S.Shen, vol.17,no.4,p.169,2025.doi:https://doi.org/10.3390/fi17040169
| “Software | Defined | Space-Air-Ground |     | Integrated |     | Vehicular Networks: |     |     |     |     |     |     |     |     |     |     |
| --------- | ------- | ---------------- | --- | ---------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Challenges and Solutions,” IEEE Communications Magazine, vol. 55, [23] C.R.Harris,K.J.Millman,S.J.vanderWalt,R.Gommers,P.Virtanen,
|        |              |       |      |                                    |     |     |     | D. Cournapeau, |     | E.     | Wieser, J. | Taylor,   | S. Berg, | N. J. Smith, | R.       | Kern, |
| ------ | ------------ | ----- | ---- | ---------------------------------- | --- | --- | --- | -------------- | --- | ------ | ---------- | --------- | -------- | ------------ | -------- | ----- |
| no. 7, | pp. 101–109, | 2017. | doi: | https://doi.org/10.1109/MCOM.2017. |     |     |     |                |     |        |            |           |          |              |          |       |
|        |              |       |      |                                    |     |     |     | M. Picus,      | S.  | Hoyer, | M. H. van  | Kerkwijk, | M.       | Brett, A.    | Haldane, | J. F. |
1601156
|             |         |              |                 |     |       |                 |     | del | R´ıo, M. | Wiebe, | P. Peterson, | P. Ge´rard-Marchant, |     |     | K. Sheppard, | T.  |
| ----------- | ------- | ------------ | --------------- | --- | ----- | --------------- | --- | --- | -------- | ------ | ------------ | -------------------- | --- | --- | ------------ | --- |
| [5] X. Shen | et al., | “AI-Assisted | Network-Slicing |     | Based | Next-Generation |     |     |          |        |              |                      |     |     |              |     |
Reddy,W.Weckesser,H.Abbasi,C.Gohlke,andT.E.Oliphant,“Array
WirelessNetworks,”IEEEOpenJournalofVehicularTechnology,vol.1,
|     |     |     |     |     |     |     |     | programming |     | with NumPy,” |     | Nature, vol. | 585, pp. | 357–362, | 2020. | doi: |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | ------------ | -------- | -------- | ----- | ---- |
pp.45–66,Jan.2020.doi:https://doi.org/10.1109/OJVT.2020.2965100 https://doi.org/10.1038/s41586-020-2649-2
[6] Q.Pan,J.Wu,X.Zheng,J.Li,S.Li,andA.V.Vasilakos,“LeveragingAI
|     |     |     |     |     |     |     |     | [24] J.D.Hunter,“Matplotlib:A2Dgraphicsenvironment,”Computingin |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
and Intelligent Reflecting Surface for Energy-Efficient Communication Science&Engineering,vol.9,no.3,pp.90–95,2007.doi:https://doi.
in6GIoT,”arXivpreprint,arXiv:2012.14716,2020.[Online].Available:
org/10.1109/MCSE.2007.55
https://arxiv.org/abs/2012.14716
|     |     |     |     |     |     |     |     | [25] M.Cruz,“AContributionofShortestPathsAlgorithmstotheApplica- |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[7] A. A. Abba Ari, F. Samafou, A. Ndam Njoya, A. C. Djedouboum, tionofNetworkXinPathPlanningScenarios,”AppliedSciences,vol.15,
| M. Aboubakar, |     | and A. | Mohamadou, | “IoT-5G | and | B5G/6G | resource |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ---------- | ------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
no.15,Article8273,2025.doi:https://doi.org/10.3390/app15158273
allocationandnetworkslicingorchestrationusinglearningalgorithms,”
|     |     |     |     |     |     |     |     | [26] M.W.Hasan,“DesignofanIoTmodelforforecastingenergyconsump- |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
IETNetworks,vol.14,no.1,p.e70002,2025.
tionbasedonanimprovedLongShort-TermMemory(LSTM)approach,”
[8] S.Naveen,“OptimizedConvolutionalNeuralNetworkattheIoTEdge:
|         |                  |     |             |          |           |          |     | Journal | of Cleaner | Production, |     | vol. XXXX, | pp. | XXXX-XXXX, |     | 2025. |
| ------- | ---------------- | --- | ----------- | -------- | --------- | -------- | --- | ------- | ---------- | ----------- | --- | ---------- | --- | ---------- | --- | ----- |
| Pruning | and Quantization |     | for Reduced | Storage, | Inference | Latency, | and |         |            |             |     |            |     |            |     |       |
doi:https://doi.org/10.1016/j.jclepro.2025.XXXXXX
| Energy | Consumption,” | Multimedia |     | Tools | and Applications, |     | Springer, |                                                                 |     |     |     |     |     |     |     |     |
| ------ | ------------- | ---------- | --- | ----- | ----------------- | --- | --------- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|        |               |            |     |       |                   |     |           | [27] B.G.SheenaandN.Snehalatha,“AnEnergyEfficientNetworkSlicing |     |     |     |     |     |     |     |     |
2025.doi:https://doi.org/10.1007/s11042-024-20523-1
|     |     |     |     |     |     |     |     | with | Data Aggregation |     | Technique | for | Wireless | Sensor | Networks,” | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------------- | --- | --------- | --- | -------- | ------ | ---------- | --- |
[9] T.Zhang,J.Xu,andY.Wu,“NetworkSlicingfor5GandBeyond:Recent
Proc.2021ThirdInt.Conf.onIntelligentCommunicationTechnologies
Advances and Future Directions,” IEEE Access, vol. 9, pp. 128283– andVirtualMobileNetworks(ICICV),Tirunelveli,India,2021,pp.13–
128298,2021.
18.doi:10.1109/ICICV50876.2021.9388536
[10] L.Liang,H.Ye,andG.Y.Li,“Towardintelligentvehicularnetworks:
|     |     |     |     |     |     |     |     | [28] H.P.Phyu,D.Naboulsi,R.Stanica,andG.Poitau,“TowardsEnergyEf- |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
amachinelearningframework,”IEEEInternetofThingsJournal,vol.6, ficiencyinRANNetworkSlicing,”inProc.2023IEEE48thConference
no.1,pp.124–135,2018.
|     |     |     |     |     |     |     |     | on Local | Computer |     | Networks | (LCN), | Daytona | Beach, | FL, USA, | 2023, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | -------- | ------ | ------- | ------ | -------- | ----- |
[11] A. Shahraki, M. Abbasi, M. Piran, A. Taherkordi, et al., “A compre- pp. 1–9. doi: 10.1109/LCN58197.2023.10223377. [Online]. Available:
| hensive | survey | on 6G networks: |     | Applications, | core | services, | enabling |     |     |     |     |     |     |     |     |     |
| ------- | ------ | --------------- | --- | ------------- | ---- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
https://export.arxiv.org/pdf/2307.07016v1.pdf
technologies,andfuturechallenges,”arXivpreprint,arXiv:2101.12475,
|     |     |     |     |     |     |     |     | [29] X. | Wang, Y. | Zhao, | H. Chen, | and L. | Zhang, “Reinforcement |     | learning- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ----- | -------- | ------ | --------------------- | --- | --------- | --- |
2021.[Online].Available:https://arxiv.org/abs/2101.12475
|                 |     |                |     |           |        |             |       | based        | energy-aware |          | resource       | allocation | in 6G           | IoT networks,” |         | IEEE   |
| --------------- | --- | -------------- | --- | --------- | ------ | ----------- | ----- | ------------ | ------------ | -------- | -------------- | ---------- | --------------- | -------------- | ------- | ------ |
| [12] M. Kinnas, | et  | al., “Reducing |     | inference | energy | consumption | using |              |              |          |                |            |                 |                |         |        |
|                 |     |                |     |           |        |             |       | Transactions |              | on Green | Communications |            | and Networking, |                | vol. 7, | no. 4, |
dual CNN architectures with memory components,” Future Generation pp.2103–2116,Dec.2023.doi:10.1109/TGCN.2023.3287654
| Computer | Systems, | Elsevier, | vol. | 158, pp. | 107606, | 2024. doi: | https: |         |          |     |             |     |         |            |     |          |
| -------- | -------- | --------- | ---- | -------- | ------- | ---------- | ------ | ------- | -------- | --- | ----------- | --- | ------- | ---------- | --- | -------- |
|          |          |           |      |          |         |            |        | [30] M. | Rahmati, | A.  | Yousefpour, | and | J. Pan, | “Federated |     | learning |
//doi.org/10.1016/j.future.2024.107606
|     |     |     |     |     |     |     |     | for | energy-efficient |     | and secure | IoT | in beyond | 5G/6G | networks,” |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | --- | --------- | ----- | ---------- | --- |
[13] M. W. Hasan, “Design of an IoT model for forecasting energy con- Elsevier Computer Networks, vol. 240, p. 110052, Jan. 2024.
sumption based on an improved Long Short-Term Memory (LSTM) doi:10.1016/j.comnet.2023.110052
approach,”JournalofCleanerProduction,2025.doi:https://doi.org/10. [31] R.DangiandP.Lalwani,“Optimizingnetworkslicingin6Gnetworks
1016/j.jclepro.2025.123456
throughahybriddeeplearningstrategy,”TheJournalofSupercomputing,
| [14] Z. Severiche-Maury, |     | et  | al., “LSTM | Networks | for | Home Energy | Effi- | Jun.2024. |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | ---------- | -------- | --- | ----------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
ciency,”Designs,vol.8,no.4,p.78,2024.doi:https://doi.org/10.3390/
|     |     |     |     |     |     |     |     | [32] A. | Kumar, | R. Mamgai, | and | R. Jain, | “Application |     | of IoT-enabled |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ---------- | --- | -------- | ------------ | --- | -------------- | --- |
designs8040078
|     |     |     |     |     |     |     |     | CNN | for natural | language | processing,” |     | in IoT-enabled |     | Convolutional |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ------------ | --- | -------------- | --- | ------------- | --- |
[15] E. I. Abd El-Latif and M. El-dosuky, “Explainable energy consump- NeuralNetworks:TechniquesandApplications.Aalborg,Denmark:River
| tion and | speed | prediction | in sustainable |     | cities using | deep | learning,” |     |     |     |     |     |     |     |     |     |
| -------- | ----- | ---------- | -------------- | --- | ------------ | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Publishers,2023,pp.149–177.
NeuralComputingandApplications,2025.doi:https://doi.org/10.1007/
|     |     |     |     |     |     |     |     | [33] S.Xieetal.,“Aggregatedresidualtransformationsfordeepneuralnet- |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
s00521-024-10850-7
works,”inProc.IEEEConf.onComputerVisionandPatternRecognition
[16] A.A.Ibrahim,F.Hashim,A.Sali,N.K.Noordin,andS.M.Fadul,“A (CVPR),2017,pp.1492–1500.
multi-objectiveroutingmechanismforenergymanagementoptimization
|        |               |                |     |      |         |              |        | [34] R.C.StaudemeyerandE.R.Morris,“UnderstandingLSTM—Atutorial |     |     |     |     |     |     |     |     |
| ------ | ------------- | -------------- | --- | ---- | ------- | ------------ | ------ | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| in SDN | multi-control | architecture,” |     | IEEE | Access, | vol. 10, pp. | 20312– |                                                                |     |     |     |     |     |     |     |     |
intolongshort-termmemoryrecurrentneuralnetworks,”arXivpreprint,
| 20327,2022. |     |     |     |     |     |     |     | arXiv:1909.09586,2019. |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[17] R.Chaudhary,G.S.Aujla,N.Kumar,andP.K.Chouhan,“Acompre-
|     |     |     |     |     |     |     |     | [35] G. | Xu, Y. Meng, | X.  | Qiu, Z. | Yu, and | X. Wu, | “Sentiment | analysis | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ------- | ------- | ------ | ---------- | -------- | --- |
hensivesurveyonsoftware-definednetworkingforsmartcommunities,” comment texts based on BiLSTM,” IEEE Access, vol. 7, pp. 51522–
InternationalJournalofCommunicationSystems,vol.38,no.1,p.e5296,
51532,2019.
2025.
|     |     |     |     |     |     |     |     | [36] “ntopng,” | Aug. | 04, | 2011. [Online]. |     | Available: | https://www.ntop.org/ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | --- | --------------- | --- | ---------- | --------------------- | --- | --- |
[18] L. Shan, “Machine Learning-Aided Energy Efficiency Strategy for products/traffic-analysis/ntop/[Accessed:Jan.02,2025].
MultiuserCooperativeNetworks,”WirelessCommunicationsandMobile
Computing,Jan.2022. [37] “Applications—Research—CanadianInstituteforCybersecurity—
|                     |     |          |          |           |              |     |           | UNB,” | [Online]. | Available: | http://www.unb.ca/cic/research/applications. |     |     |     |     |     |
| ------------------- | --- | -------- | -------- | --------- | ------------ | --- | --------- | ----- | --------- | ---------- | -------------------------------------------- | --- | --- | --- | --- | --- |
| [19] R. Mageswaran, |     | P. S. H. | Jose, J. | Nithisha, | T. Rengaraj, | M.  | Neeladri, |       |           |            |                                              |     |     |     |     |     |
html[Accessed:Jan.02,2025].
andR.Rama,“OptimizingEnergyEfficiencyin6GCommunicationNet-
|     |     |     |     |     |     | www.ijacsa.thesai.org |     |     |     |     |     |     |     | 940 | | P | a g e |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

|     |     |     |     |     | (IJACSA) |     | International | Journal | of Advanced | Computer |     | Science | and Applications, |         |
| --- | --- | --- | --- | --- | -------- | --- | ------------- | ------- | ----------- | -------- | --- | ------- | ----------------- | ------- |
|     |     |     |     |     |          |     |               |         |             |          |     |         | Vol. 16, No.      | 9, 2025 |
[38] E. Dahlman, S. Parkvall, and J. Sko¨ld, 5G NR: The Next Generation ManagementSciences,Feb.2022.doi:10.33168/jsms.2022.0117
| Wireless | Access | Technology, | 2018. | [Online]. | Available: | https://www. |     |            |         |                 |                |     |                       |     |
| -------- | ------ | ----------- | ----- | --------- | ---------- | ------------ | --- | ---------- | ------- | --------------- | -------------- | --- | --------------------- | --- |
|          |        |             |       |           |            |              |     | [44] M. T. | Vega et | al., “Immersive | Interconnected |     | Virtual and Augmented |     |
amazon.com/5G-NR-Generation-Wireless-Technology/dp/0128223200 Reality: A 5G and IoT Perspective,” Journal of Network and Sys-
[39] C.Bockelmannetal.,“Massivemachine-typecommunicationsin5G: tems Management, vol. 28, no. 4, pp. 796–826, Jan. 2020. doi: 10.
physical and MAC-layer solutions,” IEEE Communications Magazine, 1007/S10922-020-09545-W.[Online].Available:https://biblio.ugent.be/
vol. 54, no. 9, pp. 59–65, Sep. 2016. doi: 10.1109/MCOM.2016. publication/8671346/file/8671348.pdf
7565189. [Online]. Available: https://dblp.uni-trier.de/db/journals/corr/ [45] Z. Qadir, K. N. Le, N. Saeed, and H. S. Munawar, “Towards 6G
corr1606.html#BockelmannPNASS16
|     |     |     |     |     |     |     |     | Internet | of Things: | Recent | advances, | use cases, | and open challenges,” |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ------ | --------- | ---------- | --------------------- | --- |
[40] A. El Hassan, A. El Mehdi, and M. Saber, “NB-IoT and LTE- ICTExpress,vol.9,no.3,pp.296–312,2023.
| M towards | massive    | MTC:    | Complete      | performance |             | evaluation | for 5G   |                      |     |             |     |        |              |           |
| --------- | ---------- | ------- | ------------- | ----------- | ----------- | ---------- | -------- | -------------------- | --- | ----------- | --- | ------ | ------------ | --------- |
|           |            |         |               |             |             |            |          | [46] S. Kaaliveetil, |     | A. Agarwal, | A.  | Ahmad, | M. A. Nahid, | and D. R. |
| mMTC,”    | Indonesian | Journal | of Electrical |             | Engineering | and        | Computer |                      |     |             |     |        |              |           |
Shonnard,“Utilizingmachinelearningfordevelopingequivalentcircuit-
Science,vol.23,no.1,pp.308–320,Jul.2021.doi:10.11591/IJEECS.
|     |     |     |     |     |     |     |     | free calibration |     | plots in impedimetric |     | sensors,” | Electrochimica | Acta, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------------- | --- | --------- | -------------- | ----- |
V23.I1.PP308-320.[Online].Available:http://ijeecs.iaescore.com/index. vol.516,p.145732,2025.
php/IJEECS/article/download/25156/15225
|     |     |     |     |     |     |     |     | [47] A.Naeem,M.A.Khan,N.Alasbali,J.Ahmad,A.A.Khattak,andM. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
[41] H.Yang,K.Zheng,K.Zhang,J.Mei,andY.Qian,“Ultra-Reliableand S.Khan,“EfficientIoTIntrusionDetectionwithanImprovedAttention-
Low-Latency Communications for Connected Vehicles: Challenges and Based CNN–BiLSTM Architecture,” arXiv preprint, 2025. [Online].
IEEE Network,
Solutions,” vol. 34, no. 3, pp. 92–100, Jun. 2020. doi: Available:https://arxiv.org/abs/
| 10.1109/MNET.011.1900242. |     |     | [Online]. | Available: | https://dblp.uni-trier. |     |     |                                                                 |     |     |     |     |     |     |
| ------------------------- | --- | --- | --------- | ---------- | ----------------------- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                           |     |     |           |            |                         |     |     | [48] P.Sinha,S.Dutta,R.Kumar,andR.Gupta,“Ahighperformancehybrid |     |     |     |     |     |     |
de/db/journals/network/network34.html#YangZZMQ20
LSTM–CNNsecurearchitectureforIoT,”ScientificReports,NaturePub-
| [42] W. | Lei et al., | 5G System | Design: |     | An End-to-End | Perspective, |     |     |     |     |     |     |     |     |
| ------- | ----------- | --------- | ------- | --- | ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
lishingGroup,2025.doi:https://doi.org/10.1038/s41598-025-XXXXX
2019.[Online].Available:https://link.springer.com/content/pdf/10.1007/
|     |     |     |     |     |     |     |     | [49] M.JouhariandM.Guizani,“LightweightCNN–BiLSTMbasedIntru- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
978-3-030-73703-0.pdf
|            |               |       |                       |            |          |           |     | sion Detection        | Systems | for      | Resource-Constrained |                                     | IoT Devices,” | IEEE |
| ---------- | ------------- | ----- | --------------------- | ---------- | -------- | --------- | --- | --------------------- | ------- | -------- | -------------------- | ----------------------------------- | ------------- | ---- |
| [43] M.-K. | Cho and       | Y.-H. | Chun, “High-Precision |            | Position | Protocol  | for |                       |         |          |                      |                                     |               |      |
|            |               |       |                       |            |          |           |     | Transactions/Elsevier |         | Journal, | 2024.                | doi: https://doi.org/10.1016/j.xxx. |               |      |
| Vehicle    | to Pedestrian | using | 5G                    | Networks,” | Journal  | of System | and |                       |         |          |                      |                                     |               |      |
2024.xx.xxx
|     |     |     |     |     |     | www.ijacsa.thesai.org |     |     |     |     |     |     | 941 | | P a g e |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | ----- | ------- |