with open("body_final.tex", encoding="utf-8") as f:
    body = f.read()
with open("refs.tex", encoding="utf-8") as f:
    refs = f.read()

preamble = r"""\documentclass[conference]{IEEEtran}
\IEEEoverridecommandlockouts
\usepackage{cite}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{textcomp}
\usepackage{xcolor}
\usepackage{booktabs}
\def\BibTeX{{\rm B\kern-.05em{\sc i\kern-.025em b}\kern-.08em
    T\kern-.1667em\lower.7ex\hbox{E}\kern-.125emX}}
\begin{document}

\title{SDH-PPO Driven Resource Orchestration for IoT-Aware Multi-Tenant Network Slicing in Microservices-Based SDN}

\author{\IEEEauthorblockN{1\textsuperscript{st} Given Name Surname}
\IEEEauthorblockA{\textit{dept. name of organization (of Aff.)} \\
\textit{name of organization (of Aff.)}\\
City, Country \\
email address or ORCID}
}

\maketitle

\begin{abstract}
The evolution toward 6G networks and the proliferation of the Internet of Things (IoT) require adaptive resource orchestration to handle traffic heterogeneity. Multi-tenant network slicing and microservices-based Software-Defined Networking (SDN) architectures offer essential traffic isolation, but introduce orchestration complexity and queueing latency that risk violating Service Level Agreements (SLAs). Conventional Deep Reinforcement Learning (DRL) approaches, such as Deep Q-Networks (DQN), fail to address microservice volatility due to the limitations of discrete action spaces. Meanwhile, standard Proximal Policy Optimization (PPO) is prone to convergence failures and sampling inefficiencies in dynamic environments. To bridge the operational gap between theoretical simulation and physical deployment, this study proposes SDH-PPO (Safe-Driven Hybrid Proximal Policy Optimization). This framework employs a hybrid action space for continuous bandwidth adjustment and discrete port selection, and integrates the Enhanced Optimization Wasserstein Generative Adversarial Network (EO-WGAN) to synthesize extreme network variances prior to agent deployment. Validation on a physical Raspberry Pi 5-based edge computing infrastructure shows that SDH-PPO reduces the total SLA violation rate to 27.3\%, representing a 47.6\% performance improvement over the baseline model. Notably, the agent achieves a 0.0\% violation rate for critical traffic (highest priority) with a latency of 2.71 ms, demonstrating its reliability in maintaining spectrum stability under fluctuating network traffic conditions.
\end{abstract}

\begin{IEEEkeywords}
Reinforcement Learning, Software-Defined Networking (SDN), Internet of Things (IoT), Resource Optimization, Multi-Tenant, Network Slicing, Microservice, Orchestration
\end{IEEEkeywords}

"""

closing = r"""

\begin{thebibliography}{41}
""" + refs + r"""
\end{thebibliography}

\end{document}
"""

with open("../main.tex", "w", encoding="utf-8") as f:
    f.write(preamble + body + closing)
print("main.tex written")
