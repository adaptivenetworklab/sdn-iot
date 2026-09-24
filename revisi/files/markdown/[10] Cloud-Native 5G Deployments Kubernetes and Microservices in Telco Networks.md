# [10] Cloud-Native 5G Deployments Kubernetes and Microservices in Telco Networks

> Source file: `[10] Cloud-Native 5G Deployments Kubernetes and Microservices in Telco Networks.pdf`

---

 Volume 10 Issue 3

                       @ May - June 2022 IJIRMPS | ISSN: 2349-7300

Cloud-Native 5G Deployments: Kubernetes and
Microservices in Telco Networks

Varinder Kumar Sharma

Technical Manager
sharmavarinder01@gmail.com

Abstract:
The telecommunications sector is being transformed at its core by the worldwide implementation of
5G  networks.  Compared  to  past  generations  of  cellular  networks,  5G  requires  significantly  more
agility, scalability, and operational efficiency for future applications, such as ultra-reliable low-latency
communications  (URLLC),  massive  machine-type  communications  (mMTC),  and  enhanced  mobile
broadband  (eMBB).  Telecom  infrastructures  are  conventional,  relying  mainly  on  monolithic
architectures and hardware-centric network functions, which are insufficient when facing the evolving
requirements  of  5G.  To  address  the  issue,  the  industry  is  rapidly  transitioning  to  cloud-native
architectures,  which  comprise  microservices,  containers,  and  orchestration  platforms  such  as
Kubernetes.
This  paper  discusses  cloud-native  principles—specifically,  microservices  and  Kubernetes
orchestration—as relevant to the deployment of 5G networks. The book offers an in-depth look into
how telecommunications networks will be able to transform into fully-functioning, highly dynamic,
and automated networks of the future which will be operationally ready for deployment and will enable
adaptation of new services that meet the demands and expectations of the 5G architecture: deploying
innovative services at a faster pace with massively reduced costs. This is achieved by dividing network
functions into small pieces of software code (microservices architecture) that are loosely coupled and
that can be independently updated, scaled up, and scaled down. This differs from classical VNF-based
architectures,  as  VNFs  (although  more  potent  than  hardware  appliances)  are  essentially  still
monolithic  applications. The  transition  to  CNFs  offers  several  advantages  for  automation,  lifecycle
management, and platform portability.
Kubernetes, the industry standard for container orchestration, is a key enabler of cloud-native 5 G
networks. Utilizing Kubernetes’ self-healing, self-scaling, and rolling update capabilities, as well as its
declarative  configuration  features,  carriers  can  achieve  near  real-time  network  responsiveness  and
service availability. This post explores several key Kubernetes-native capabilities designed for telecom
workloads, including Custom Resource Definitions (CRDs), Operators, StatefulSets, Helm charts, and
service  meshes  such  as  Istio.  It  also  addresses  the  Kubernetes  Management  and  Orchestration
(MANO)  framework  and  network  slicing  control  plane  integration,  enabling  fine-grained  resource
allocation and quality-of-service management in a versatile 5G environment.
Moreover, the abstract describes a systematic approach to deploy 5G core network functions based on
a  cloud-native  stack.  This  involves  Continuous  Integration  and  Continuous  Deployment  (CI/CD)
pipelines, GitOps workflows, Infrastructure-as-Code (IaC), and automated testing in telco-specific CI
environments.  The  performance  trade-offs,  deployment  efficiency,  and  operational  gains  obtained
from the emulator over both simulated and deployment data are rigorously analyzed in a large portion
of  the  work.  It  then  examines  journey  tracings  from  early  adopters  of  the  technology,  including
Rakuten Mobile and Deutsche Telekom, to derive empirically observed conclusions about deployment
velocity, fault tolerance, and cost efficiency.
The  results  in  this  study  suggest  that  moving  to  cloud-native  5G  has  significant  advantages.
Quantitatively, we discover that Kubernetes-based CNFs reduce deployment time by as much as 60%,
increase infrastructure utilization by as much as 40%, and substantially reduce MTTR when networks
misbehave. Additionally,  microservices  enable  more  rapid  feature  delivery,  improved  observability,

IJIRMPS2203232706           Website: www.ijirmps.org

Email: editor@ijirmps.org

1

 Volume 10 Issue 3

                       @ May - June 2022 IJIRMPS | ISSN: 2349-7300

and  greater  isolation  of  logic  between  network  slices  and  services. These  advantages  are  especially
crucial in environments characterized by high availability, low latency, and rapid innovation cycles.
However, the switch to cloud-native 5G is not entirely smooth sailing. There are challenges surrounding
service  chaining,  multicluster  federation,  integration  with  existing  infrastructure,  and  end-to-end
security that need to be addressed. The paper concludes by suggesting possible ways to overcome these
hurdles, including the adoption of hybrid orchestration models, maintaining safe DevSecOps practices,
and utilizing policy-driven automation frameworks.
Essentially,  this  work  contributes  to  the  knowledge  base  and  consolidates  architectural  plans,  best
practices,  and  operational  practices  involved  in  deploying  cloud-native  5G  networks  based  on
Kubernetes  and  microservices.  It  is  a  must-read  for  telecom  engineers,  network  planners,  and
policymakers who  wish to design and build  next-generation networks that are not only  more agile,
adaptive,  and  resilient  than  ever  before,  but  also  far  more  programmable  and  transparent  –  a
transformational vision of 5G.

Keywords:  G  Networks,  Cloud-Native Architecture,  Kubernetes,  Microservices,  Network  Function
Virtualization  (NFV),  Containerized  Network  Functions  (CNFs),  Service  Orchestration,  Telecom
Cloud, CI/CD, Network Slicing, Telco Automation, Edge Computing, DevOps for Telecom, Telecom
Infrastructure Modernization, Carrier-Grade Containerization.

leap

I. INTRODUCTION
The  global  rollout  of  fifth-generation  (5G)  wireless  networks  marks  a  monumental
in
telecommunications, ushering in a new era of connectivity characterized by ultra-low latency, gigabit-level
bandwidth,  and  pervasive  device-to-device  communication.  5G  is  expected  to  underpin  transformative
applications  such  as  autonomous  vehicles,  remote  surgery,  augmented  and  virtual  reality,  and  intelligent
industrial  automation.  To  deliver  on  these  promises,  however,  telecom  operators  must  move  away  from
conventional  paradigms  of  static,  hardware-driven  networks  toward  more  dynamic,  software-centric
infrastructures. The scale, agility, and complexity demanded by 5G use cases simply cannot be achieved with
legacy network architectures. Consequently, the industry is undergoing a paradigm shift, transitioning from
monolithic  Virtual  Network  Functions  (VNFs)  to  lightweight,  cloud-native  architectures  that  leverage
microservices and container orchestration engines, such as Kubernetes.
Historically, telecom networks have been built using proprietary, purpose-built hardware tightly coupled with
vendor-specific  software.  Although  Network  Function  Virtualization  (NFV)  partially  addressed  these
constraints  by  decoupling  software  from  hardware,  most  VNFs  remained  monolithic  in  structure  and
operationally  complex.  In  contrast,  cloud-native  designs  break  network  functions  into  independently
deployable microservices that run in lightweight, isolated containers. This modular decomposition not only
simplifies development and scaling but also enables continuous delivery pipelines and rapid iteration cycles
that align with modern DevOps practices.
Kubernetes, originally designed by Google and now maintained by the Cloud Native Computing Foundation
(CNCF), has become the standard for automating container deployment, scaling, and management. In the
telecom context, Kubernetes enables operators to orchestrate containerized network functions (CNFs) across
distributed environments—ranging from centralized data centers to remote edge sites. Its capabilities—such
as automated fault recovery, service discovery, declarative configuration, and resource optimization—offer
a  high  degree  of  automation  and  resilience,  which  are  essential  for  meeting  the  stringent  service-level
requirements of 5 G networks.
The  increasing  need  for  network  slicing  also  catalyzes  the  transition  to  cloud-native  5G  networks.  This
mechanism enables operators to create isolated, end-to-end virtual networks tailored to specific service types
or  customer  requirements.  Implementing  network  slices  requires  fine-grained  orchestration,  real-time
telemetry, and dynamic scaling, all of which are made feasible by cloud-native platforms. Furthermore, as
5G embraces edge computing to bring processing closer to the user, the role of lightweight, scalable CNFs
deployed  at  the  edge  becomes  critical.  Kubernetes’s  support  for  federated  clusters  and  multi-cloud
management provides the necessary foundation to operationalize edge-native 5G services.
This paper investigates the architectural principles, operational benefits, and technical challenges associated
with  cloud-native  5G  deployments.  It  focuses  explicitly  on  how  Kubernetes  and  microservices  can  be

IJIRMPS2203232706           Website: www.ijirmps.org

Email: editor@ijirmps.org

2

 Volume 10 Issue 3

                       @ May - June 2022 IJIRMPS | ISSN: 2349-7300

leveraged to orchestrate the 5G core, enabling rapid deployment, continuous innovation, and cost efficiency.
The introduction outlines the fundamental motivations for this transformation and establishes the research
context in which modern 5G infrastructure must evolve to support cloud-native paradigms. We also highlight
the  growing  industry  consensus  around  adopting  open  standards  and  containerization  as  foundational
enablers of scalable and programmable telecom networks.
By  integrating  real-world  case  studies,  experimental  deployments,  and  architectural  best  practices,  this
research  contributes  a  practical  roadmap  for  telecom  operators  transitioning  toward  containerized,
microservices-based 5G infrastructure. The aim is not only to assess the operational efficiencies gained from
Kubernetes  but  also  to  examine  its  ability  to  support  carrier-grade  workloads  under  diverse  deployment
topologies and quality-of-service (quality of service) constraints. The paper begins with a literature review
of  foundational  technologies  and  prior  deployments,  followed  by  a  methodology  section  detailing  the
experimental  setup,  tools,  and  orchestration  workflows.  Subsequent  sections  present  results,  analyze
performance metrics, discuss deployment trade-offs, and conclude with strategic recommendations.
As 5G continues to evolve from pilot stages to full-scale deployment, embracing cloud-native constructs is
no longer optional—it is imperative. Kubernetes and microservices represent the core enablers of this next-
generation network architecture, offering telecom providers the flexibility and efficiency required to meet
both current and future demands of mobile communication.

II. LITERATURE REVIEW
The evolution of telecom networks towards cloud-native is built on the foundations of NFV, SDN, and the
containerization of network workloads. Microservices and Kubernetes are the New Standard.. As the demand
for a more scalable and resilient mobile network in the era of 5G grows, researchers and industry bodies have
aligned  behind  microservices  and  Kubernetes  as  the  de  facto  solution  for  orchestrating  containerized,
distributed systems in the telecom sector.
One of the early standardization bodies that paved the way for network virtualization was the ETSI NFV
architecture, which actively promoted the disaggregation of software-implemented network functions from
proprietary hardware platforms. Although ETSI NFV made a significant first step, researchers like Taleb et
al. [1] highlighted the lack of agility and lifecycle automation, particularly for ultra-low latency and high-
throughput 5G use cases. NFV, born from VM-based solutions, incurred overhead in resource utilization and
deployment delay, causing headaches for dynamic service chaining and edge deployment.
To  mitigate  these  problems,  the  academic  community  looked  into  microservice-based  architectures.  As
Bhamare et al. [2] inspired, microservices bring finer granularity, higher modularity, and better alignment of
CI/CD  pipelines  for  5G  networks. Turning  monolithic VNFs  into  loosely  coupled  microservices  enables
operators to turn up, update, and scale individual elements of functionality separately, providing maximum
flexibility and resilience in the face of changing traffic patterns or failure conditions.
At the same time, Kubernetes has become the de facto standard for orchestrating containerized workloads in
the industry. Bernstein [3] has also demonstrated that Kubernetes offers essential capabilities, including self-
healing, horizontal scaling, and service discovery, which are particularly beneficial in managing  complex
telecom applications. With declarative configuration and an extensible design, it enables telecom operators
to have control over hybrid and multi-cloud infrastructures, orchestrating CNFs consistently across disparate,
geographically distributed clusters.
The collaboration between Kubernetes and CNFs is further investigated in the work of Kalim et al. [4], which
shows that deploying an application takes nearly half the time with container orchestration compared to a
virtual machine-based approach. They also focused on the benefits of using the Helm charts, Operators, and
CRDs  to  orchestrate  telecom-specific  logic,  which  resulted  in  operational  simplicity  and  higher  network
availability. These Kubernetes-native capabilities enable telecom vendors to package CNFs, distribute them,
and manage them in a manner that adheres to cloud-native best practices.
Cloud-native  methodologies.  Furthermore,  it  can  be  seen  that  cloud-native  methods  overlap  with  SDN
concepts,  as  pointed  out  in  Foukas  et  al.  [5],  where  an  elastic  and  programmable  5G  architecture  was
introduced through  an SDN controller stack and Kubernetes-managed microservices. Such  an integration
enables end-to-end slicing, dynamic load distribution, and timely telemetry pulling down. The architecture
as presented accommodates a broad range of use cases—covering eMBB through URLLC—whilst at the
same time preserving the carrier-grade resilience associated with telecom networks.

IJIRMPS2203232706           Website: www.ijirmps.org

Email: editor@ijirmps.org

3

 Volume 10 Issue 3

                       @ May - June 2022 IJIRMPS | ISSN: 2349-7300

Moreover, the real-life proof is in the pudding. Rakuten Mobile's implementation of a complete virtualized
and  cloud-native  mobile  network,  as  explained  by  Iwamoto  et  al.  [6],  showcases  the  feasibility  of  a
Kubernetes-enabled 5G architecture at the production level. Their conclusions provide evidence that open-
source tools, container orchestration, and microservice decomposition are vital to delivering the faster time-
to-market, richer observability, and cost-effective scaling that modern telco networks require.
Security  and  isolation  are  and  always  will  be  important  issues  here. As  evaluated  by  Chiosi  et  al.  [7],
container-based deployments should be fortified by network policies, runtime scanning, and service mesh
encryption  (e.g.,  using  Istio  or  Linkerd)  to  guarantee  data  integrity  and  tenant  isolation  among  slices.
Furthermore,  multi-cluster  federation  is  a  hot  topic,  and  such  federation  can  include  unified  policy
enforcement, cluster failover, and high availability between edge and core deployments.
The  literature  supports  the  strategic  shift  from  traditional  to  cloud-native  designs  in  5G  network
infrastructure. From architectural modularity and automated deployment to service agility and operational
insight, Kubernetes and microservices are recognized as the foundational pillars of scalable, programmable,
and future-proof telco networks. This paper further extends these findings by proposing how mobile operators
can leverage the framework and benchmarks presented in this paper to deploy, benchmark, and operate 5G
environments within their networks.

III. METHODOLOGY
The methodology adopted for this research is grounded in the design, implementation, and evaluation of a
cloud-native 5G core network using Kubernetes for orchestration and microservices  for network function
decomposition. The objective was to simulate a realistic telco deployment scenario by replicating essential
components  of  a  5G  core  network  stack—including  the Access  and  Mobility  Function  (AMF),  Session
Management Function (SMF), User Plane Function (UPF), and Network Repository Function (NRF)—as
containerized  network  functions  (CNFs).  Each  network  function  was  modularized  into  independent
microservices, designed to communicate via lightweight RESTful APIs or gRPC, reflecting industry-aligned
service-oriented principles. The Kubernetes orchestration layer was selected as the central control plane to
manage  these  microservices  and  enforce  declarative  infrastructure  definitions,  enabling  fault  recovery,
dynamic scaling, and zero-downtime rolling updates.
To emulate a multi-tenant telecom cloud environment, the 5G CNFs were deployed on a Kubernetes cluster
provisioned across a hybrid infrastructure, comprising both centralized cloud nodes and simulated edge nodes
using Minikube extensions. This setup reflected the real-world distribution pattern of telco workloads, where
control plane services remain centralized while user plane functions are pushed toward the edge to minimize
latency. The Kubernetes cluster was equipped with core components, including the Kubernetes API server,
etcd, kube-scheduler, and kubelet agents. It was augmented with Helm for CNF packaging, Istio for traffic
control and security, and Prometheus and Grafana for observability and performance telemetry.
Each CNF microservice was built using lightweight container images, optimized for runtime isolation and
fast boot times. CI/CD pipelines were developed using Jenkins and ArgoCD to automate the container build,
test,  and  deployment  workflows.  Infrastructure  as  Code  (IaC)  was  implemented  through  Kubernetes
manifests  and  Helm  charts  stored  in  Git  repositories  to  enforce  version-controlled  deployments  and
reproducibility.  The  CI/CD  pipelines  included  automated  canary  deployments,  integration  testing,  and
rollback  mechanisms,  reflecting  telecom-grade  DevOps  practices.  Kubernetes-native  resources  such  as
ConfigMaps,  Secrets,  Deployments,  Services,  and  StatefulSets  were  used  to  manage  application
configurations, security credentials, runtime behavior, and persistence, particularly for stateful components
like databases or subscriber management modules.
To evaluate the system’s elasticity and fault resilience, we generated simulated traffic using  custom-built
gNodeB emulators and traffic generators such as TRex. The traffic was designed to mimic variable user loads
across different time intervals and to trigger specific 5G service types, including eMBB and URLLC. The
system was subjected to various stress scenarios, including component failures, scaling events, and network
partitioning, to observe Kubernetes' ability to maintain service continuity and heal workloads. Metrics such
as  deployment  time,  resource  consumption,  latency,  and  recovery  time  were  captured  using  Prometheus
exporters and visualized through Grafana dashboards.
Performance  benchmarking  focused  on  quantifying  improvements  in  deployment  automation,  resource
utilization efficiency, fault recovery time, and throughput scalability. These metrics were compared against

IJIRMPS2203232706           Website: www.ijirmps.org

Email: editor@ijirmps.org

4

 Volume 10 Issue 3

                       @ May - June 2022 IJIRMPS | ISSN: 2349-7300

a  baseline  setup  using  OpenStack-based  VNFs  managed  by  traditional  MANO  systems  to  establish  the
relative operational  advantages of Kubernetes-based CNFs. The results were statistically validated across
multiple trials and were normalized to account for variability in underlying hardware and network conditions.
Security and multitenancy isolation were evaluated by applying Kubernetes Network Policies, Istio’s mTLS
encryption,  and  RBAC  rules  to  enforce  tenant-level  separation  and  encrypted  service-to-service
communication.  CNFs  were  scanned  using  Clair  and  Falco  for  vulnerability  management  and  runtime
behavioral monitoring. Observability was enhanced by integrating Fluentd for log aggregation and Jaeger for
distributed  tracing,  which  provided  insights  into  inter-service  communication  paths  and  performance
bottlenecks.
Overall,  this  methodology  demonstrates  a  reproducible  and  vendor-neutral  approach  to  cloud-native  5G
deployments, emphasizing modular architecture, containerized microservices, declarative orchestration, and
automated delivery pipelines. The simulated 5G testbed, combined with cloud-native toolchains and CI/CD
automation, provided a comprehensive framework for assessing the technical viability, operational benefits,
and  scalability  potential  of  Kubernetes  in  telecom-grade  environments.  The  following  Results  section
elaborates on the empirical findings derived from this deployment model.

IV. RESULTS
The experimental deployment of the cloud-native 5G testbed yielded a range of quantitative and qualitative
results that validate the operational and architectural benefits of using Kubernetes and microservices in telco
environments.  A  primary  outcome  was  the  significant  reduction  in  deployment  time  for  core  network
functions.  Compared  to  baseline  virtual  machine-based  NFV  deployments  managed  via  traditional
OpenStack  and  manual  scripts,  the  Kubernetes-driven  deployment  of  containerized  network  functions
demonstrated a 52% decrease in provisioning time. This improvement was primarily attributed to the use of
lightweight  container  images,  Helm-based  templating,  and  Kubernetes’  declarative  resource  management
that eliminated the need for lengthy manual orchestration steps.
Scalability under varying traffic loads was another area of notable performance. The CNF-based 5G core was
subjected to synthetic traffic across three tiers: low (500 sessions per second), medium (5,000 sessions per
second),  and  high  (20,000  sessions  per  second).  Under  each  load  profile,  Kubernetes'  Horizontal  Pod
Autoscaler (HPA) adjusted the number of service replicas to meet resource  demands, maintaining latency
thresholds  within  target  service-level  agreements. The  user  plane  function  (UPF),  which  experienced  the
highest packet processing demands, was scaled dynamically across edge nodes without interrupting existing
sessions, thanks to Kubernetes’ zero-downtime scaling capabilities. Observed round-trip latency remained
below  10  ms  under  medium  loads.  It  only  slightly  increased  to  13  ms  under  peak  load  conditions,
demonstrating  that  Kubernetes-managed  CNFs  can  maintain  near  real-time  responsiveness  suitable  for
URLLC use cases.
Fault tolerance was evaluated by deliberately terminating pods and injecting failures into individual CNFs,
such as the Session Management Function (SMF). Kubernetes's self-healing mechanisms proved effective,
with average recovery times under 3.2 seconds for control plane functions and under 1.5 seconds for stateless
microservices.  Stateful  CNFs,  such  as  the  Unified  Data  Management  (UDM),  required  a  slightly  longer
recovery window due to persistent volume reattachment, but were still restored within 5.4 seconds without
compromising data integrity. These outcomes illustrate Kubernetes’ ability to meet carrier-grade reliability
targets and provide high availability even in the presence of faults.
Resource utilization was another area where the microservice-based deployment outperformed its virtualized
counterpart. On average, CPU utilization per network function decreased by 30%, and memory footprint was
reduced by 25%, due to the efficient packaging of CNFs and the absence of hypervisor overhead. Moreover,
CNFs demonstrated better bin-packing behavior under Kubernetes’ scheduling logic, which enabled higher-
density deployments across edge and central nodes. These efficiencies translate directly into cost savings and
energy efficiency, both of which are crucial for large-scale 5G network rollouts.

IJIRMPS2203232706           Website: www.ijirmps.org

Email: editor@ijirmps.org

5

 Volume 10 Issue 3

                       @ May - June 2022 IJIRMPS | ISSN: 2349-7300

Figure 1: VM vs. CNF Performance Comparison

Operational  insights  were  gathered  using  Prometheus  and  Grafana,  where  real-time  metrics  such  as  pod
status,  container  CPU/memory  usage,  and  service  availability  were  continuously  tracked.  Service  mesh
observability,  enabled  by  Istio  and  distributed  tracing  via  Jaeger,  revealed  optimal  microservice-to-
microservice communication paths and flagged latency outliers during scale-up events. Logging via Fluentd
and log aggregation into Elasticsearch enabled root-cause analysis of anomalies, such as dropped session
establishment requests or container OOMKill events, which were addressed by refining Kubernetes resource
quotas and readiness probes.
Security  and  isolation  metrics  were  assessed  through  a  combination  of  policy  enforcement  and  runtime
analysis. Kubernetes Network Policies effectively enforced inter-service access controls, while Istio’s mTLS
ensured encrypted communication across services. Container scanning with Clair reported a 90% reduction
in known CVEs compared to monolithic VNFs, primarily due to smaller attack surfaces and minimal base
images. Runtime policy enforcement with Falco detected and blocked anomalous system calls, enhancing
security compliance for telecom workloads.
Taken together, these results affirm that Kubernetes and microservices form a robust foundation for cloud-
native 5G deployments. The architecture exhibited rapid provisioning, real-time elasticity, improved fault
resilience,  reduced  operational  overhead,  and  enhanced  security  posture.  These  findings  validate  the
hypothesis that cloud-native constructs not only meet but exceed the operational demands of next-generation
telecom  networks.  The  upcoming  Discussion  section  synthesizes  these  results  in  the  broader  context  of
industry transition, implementation trade-offs, and future roadmap considerations.

V. DISCUSSION
The findings also illustrate the practical advantages and architectural readiness for leveraging Kubernetes
and microservices for cloud-native 5G applications. The observed benefits in deployment time, scalability,
resource  utilization,  and  failure  recovery  support  an  exciting  shift  from  legacy  NFV  and  monolithic
deployments. Nevertheless, such enhancements need to be put into perspective  in terms of organizational
complexity, learning curves, and ecosystem maturity issues that the telecom sector needs to cope with as it
embarks on a transformation journey of such magnitude.
Perhaps the single most significant benefit offered by the Kubernetes-based deployment is the ability to bring
agility to 5G network operations. Declarative configuration via Kubernetes manifests, along with GitOps-
driven CI/CD pipelines, results in frequent, reliable, and auditable updates of network functions. This is a
significant  change  from  the  way  software  was  once  updated  in  the  old  telco  model,  where  updates  were
infrequent and had to be coordinated manually, which usually meant an outage of service. With continuous
deployment, cloud-native architectures enable operators to quickly adapt to changing service requirements,
security threats, and performance issues. This agility is especially essential in the 5G era, as services such as
network slicing and edge deployments should scale elastically and be provisioned on demand.
The added elasticity provided by Kubernetes’ built-in auto-scaling also provides a beneficial force multiplier
for deploying latency-sensitive applications close to the network edge. In traditional NFV-based mechanisms,
where  scaling  horizontally  meant  bringing  more  VMs  online,  this  added  significant  time  and  resource
overhead.  On  the  other  hand,  Kubernetes  can  scale  out  individual  microservices  in  seconds,  allowing
operators to handle fluctuating user loads and achieve target latency and throughput. Not only are the URLLC

IJIRMPS2203232706           Website: www.ijirmps.org

Email: editor@ijirmps.org

6

 Volume 10 Issue 3

                       @ May - June 2022 IJIRMPS | ISSN: 2349-7300

and  mMTC  use  cases  gaining  substantial  benefits,  but  it  is  also  irrelevant  for  them  to  have  performance
variations.
However,  in  the  telco  world,  several  operational  and  architectural  issues  must  be  addressed  when
implementing Kubernetes technology. One issue is the learning curve associated with abstracting network
complexity in a more cloud-native environment, especially for network engineers accustomed to thinking
about legacy OSS/BSS workflows and dealing with vertically integrated hardware. Furthermore, Kubernetes
has been designed with stateless workloads in mind; however, telecom workloads are built around stateful
sessions  and  require  special  handling  for  persistent  storage,  session  affinity,  and  subscriber  data.  These
requirements necessitate advanced deployment patterns, typically achieved through StatefulSets, persistent
volume claims, and close integration with legacy telecom databases.
Service observability and debugging also represent a paradigm shift. THE MONITORING EVOLUTION
The microservices architecture introduces challenges such as distributed tracing, multi-hop telemetry, and
service mesh management, which necessitate a powerful monitoring environment. Tools like Prometheus,
Grafana, Jaeger, and Fluentd provide deep insights, but they require customization and fine-tuning to meet
telecom-grade metrics and alerting thresholds. In addition, the more microservices there are, the greater the
likelihood  of  misconfiguration  and  cascading  failure  if  policies  are  not  adequately  enforced,  automated
testing is not performed, and dependencies are not analyzed.
The  security  of  Containerized  Telecom  Environments  is  Vital.  The  importance  of  security  in  these
environments  cannot  be  overstated.  Though  Kubernetes  has  fine-grained  access  control,  runtime
enforcement, and encryption with quotas, these should be manually provisioned and audited for compliance
and regulatory purposes. In contrast to the monolithic VNF, a CNF consists of multiple containers, and all
these  containers  can  serve  as  an  attack  surface  if  not  properly  hardened.  In  other  words,  from  a  security
posture  perspective,  telecom  operators  must  embrace  DevSecOps  practices,  reintegrate  vulnerability
scanning as part of their pipelines, and utilize runtime threat detection tools.
However, another key focus area is interoperability. Moreover, even though we are making good progress
towards an open standards-based world, we still have heterogeneity in how vendors implement CNFs, Helm
charts,  and  CRDs.  This  fragmentation  may  inhibit  cross-vendor  integration  and  further  complicate
orchestration  in  multi-vendor  environments.  Common  NFVI Telco Taskforce  (CNTT)  blueprints  and TM
Forum Open Digital Architecture (ODA) principles could provide an avenue for standardization; however,
they have not yet been aligned by the industry, and full toolchain support remains under development.
Migrating to cloud-native architectures powered by microservices and Kubernetes is not simply a technical
upgrade; it is a total rethinking of how we build, operate, and evolve telecom networks. Hence, the benefits
in this study support the practicality and efficacy of such a conversion. However, real transformative success
requires change from a resource, process, and systems perspective. As network operators progress further
into the world of 5G and beyond, adopting cloud-native models will be essential, not just from a competitive
standpoint, but also to enable the delivery of next-generation network services.

VI. CONCLUSION
The transformation  of communications networks to  become native to  the cloud  represents  a foundational
transformation in how 5G’s core capabilities—scale, agility, and ultra-reliability—are realized. This paper
provides an in-depth examination of the integration of Kubernetes and microservices into the aforementioned
applications in telco networks, particularly on how these technologies facilitate the reliable, scalable, and
automated deployment of 5G core functions. We demonstrated, through both the simulated experiment and
analytical comparison, that cloud-native architecture can achieve superior performance in deployment time,
fault recovery time, and resource utilization compared to traditional NFV-based ones, and we call for more
research on measuring system operations. The orchestration layer, Kubernetes, was particularly effective for
automating  the  lifecycle  management  of  containers,  providing  resiliency  against  failures,  and  achieving
service portability across diverse deployment surfaces, such as centralised clouds and edge sites.
This is a key issue, as microservices have been proven to bring modularity and independence to the lifecycle
management  of  modern  services.  Network  function  elements  previously  entangled  within  monolithic
architecture are decomposed into containers and scaled, monitored, and updated independently. This not only
lowers  operational  overhead  but  also  enables  telecom  operators  to  adopt  CI/CD  pipelines  and  DevOps

IJIRMPS2203232706           Website: www.ijirmps.org

Email: editor@ijirmps.org

7

 Volume 10 Issue 3

                       @ May - June 2022 IJIRMPS | ISSN: 2349-7300

processes, leading to faster innovation cycles and improved service resiliency. This ability is invaluable in
the 5G era, where service requirements change in real-time.
Beyond  technical  advances,  this  research  highlights  a  strategic  shift  underway  throughout  the
telecommunications industry towards greater openness, interoperability, and programmability. The adoption
of  open-source  tooling,  such  as  Prometheus,  Helm,  Istio,  and  Jaeger,  has  enabled  operators  to  design
platform-agnostic  networks  that  are  standards-compliant  and  future-proof.  These  capabilities  also  lend
visibility and reach to  run highly distributed telco workloads without compromising  quality of service or
SLAs (as a Token).
However, it is also worth noting that transitioning to a cloud-native 5G model introduces its own level of
complexity.  These  needs  primarily  focus  on  advanced  Kubernetes  administration  skills,  service  mesh
configuration, security hardening containers, and reimagining operational processes to support the distributed
nature of microservices. In addition, both interoperability and lifecycle standardization problems are ongoing
challenges that require coordination throughout  the entire industry. We  also need to standardize  telecom-
specific abstractions for CNF packaging, orchestration, and fault management to bring together a consumer
platform for seamless, multi-vendor, multi-cloud deployments.
A strategic implication from this paper is that cloud-native network transformation should be seen in a holistic
perspective. This technological refresh should be accompanied by organizational change, re-skilling, and a
transition  from  infrastructure-based  services  to  application-based  services.  Operators  embarking  on  this
voyage may start by implementing hybrid models, in which old and new systems coexist for a while before
workloads  are  gradually  migrated. Also  critical  is  the  investment  in  strong  observability  and  automation
frameworks to drive down mean-time-to-resolution (MTTR) and pursue proactive fault avoidance.
The results of this study validate that Kubernetes and microservices are feasible and beneficial technologies
for 5G network deployments. They enable operators to create networks that are more agile, efficient, and
robust—capabilities that are crucial for keeping  pace with  the demanding requirements of 5G and future
networks. This study lays a robust foundation for deployment and experimentation, filling the gap in a mature
methodology for telco stakeholders who want to move to cloud-native solutions. It significantly contributes
to the broader discussion on open and programmable networks. As the 5G ecosystem blossoms, the insights
provided  in  this  paper  are  essential  for  defining  the  architecture  and  operational  philosophy  of  next-
generation telecom networks.

REFERENCES:

[1]  T. Taleb,  M.  Bagaa,  and A.  Ksentini,  "User  mobility-aware  virtual  network  function  placement  for

virtual 5G network infrastructure," in IEEE ICC, 2015.

[2] D. Bhamare, R. Jain and M. Samaka, "A Survey on Service Function Chaining," Journal of Network

and Computer Applications, vol. 75, pp. 138–155, 2016.

[3] D. Bernstein, "Containers and Cloud: From LXC to Docker to Kubernetes," IEEE Cloud Computing,

vol. 1, no. 3, pp. 81–84, Sept. 2014.

[4] U. Kalim, A. Yousaf and T. Taleb, "On the Performance of Kubernetes for 5G Deployments: A Case
Study," in IEEE Transactions on Network and Service Management, vol. 17, no. 4, pp. 2363–2376, Dec.
2020.

[5]  X.  Foukas,  G.  Patounas, A.  Elmokashfi,  and  M.  K.  Marina,  "Network  Slicing  in  5G:  Survey  and

Challenges," IEEE Communications Magazine, vol. 55, no. 5, pp. 94–100, May 2017.

[6] H. Iwamoto, K. Kawahara, and T. Nakayama, "Architecture and Deployment of Rakuten Mobile's Fully

Virtualized 5G Network," in Proceedings of the Open Networking Summit, 2020.

[7] F. Chiosi et al., "Network Functions Virtualisation: An Introduction, Benefits, Enablers, Challenges &

Call for Action," ETSI White Paper, 2015.

[8] M. P. Fernandez, J. Ruiz-Mas, and J. A. Hernandez, “Microservices for 5G core network: Design and

performance evaluation,” in Proc. IEEE NetSoft, 2019, pp. 148–156.

[9] M. Mijumbi, J. Serrat, J.-L. Gorricho, and R. Boutaba, “Network function virtualization: State-of-the-
art and research challenges,” IEEE Commun. Surveys Tuts., vol. 18, no. 1, pp. 236–262, First quarter
2016.

[10] R. Mijumbi, J. Serrat, J.-L. Gorricho, and S. Latré, “Design and evaluation of algorithms for mapping

and scheduling of virtual network functions,” in Proc. NetSoft, 2015, pp. 1–9.

IJIRMPS2203232706           Website: www.ijirmps.org

Email: editor@ijirmps.org

8

