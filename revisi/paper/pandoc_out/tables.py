table1 = r"""\begin{table*}[t]
\centering
\caption{State-of-the-Art Comparison of DRL-Based Orchestration Frameworks for SDN-IoT Networks}
\label{tab:1}
\scriptsize
\begin{tabular}{lccccccc}
\toprule
Reference & Hybrid/Action Space & Ratio Sizing & Multi Tenant Slicing & Microservices Isolation & Generative Augmentation & Strict Priority SLA Penalty & Physical Validation \\
\midrule
Proposed & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
\cite{b22} & - & - & \checkmark & - & - & - & - \\
\cite{b23} & - & - & \checkmark & - & - & \checkmark & - \\
\cite{b24} & - & - & - & \checkmark & - & \checkmark & \checkmark \\
\cite{b25} & - & - & \checkmark & - & - & - & \checkmark \\
\cite{b26} & - & - & \checkmark & - & - & - & - \\
\cite{b8} & - & - & - & \checkmark & - & - & - \\
\cite{b27} & \checkmark & \checkmark & \checkmark & - & - & - & - \\
\cite{b28} & - & - & \checkmark & - & - & - & - \\
\cite{b10} & - & - & \checkmark & \checkmark & - & - & - \\
\cite{b4} & \checkmark & \checkmark & \checkmark & - & \checkmark & - & - \\
\cite{b29} & \checkmark & \checkmark & - & - & - & - & - \\
\cite{b30} & - & - & \checkmark & - & - & - & - \\
\cite{b31} & - & - & - & \checkmark & - & - & - \\
\cite{b32} & - & - & \checkmark & - & - & - & - \\
\cite{b33} & - & - & \checkmark & - & - & - & - \\
\cite{b34} & - & - & \checkmark & - & \checkmark & - & - \\
\cite{b35} & - & - & \checkmark & - & - & - & \checkmark \\
\cite{b20} & - & - & \checkmark & \checkmark & - & - & \checkmark \\
\cite{b3} & - & - & \checkmark & - & - & - & - \\
\cite{b9} & - & - & - & \checkmark & - & - & \checkmark \\
\cite{b17} & - & - & \checkmark & - & - & - & - \\
\cite{b6} & \checkmark & \checkmark & \checkmark & - & - & - & - \\
\cite{b36} & - & - & \checkmark & - & - & - & - \\
\cite{b14} & - & - & \checkmark & - & - & - & - \\
\cite{b37} & - & - & - & \checkmark & - & - & - \\
\bottomrule
\end{tabular}
\\[2pt]
\footnotesize{*Notes: (\checkmark) indicates the implementation of advanced architecture/algorithm corresponding to the specific column feature; (-) indicates the use of legacy methods, discrete approximations, static environments, unconstrained exploration, or software-only simulations.}
\end{table*}"""

table2 = r"""\begin{table}[htbp]
\centering
\caption{Hyperparameter Settings}
\label{tab:2}
\begin{tabular}{cccccc}
\toprule
Epochs & LR & Batch Size & Optimizer & $\gamma$ & Hidden Layers \\
\midrule
2000 & 0.0003 & 64 & Adam & 0.99 & 256 \\
\bottomrule
\end{tabular}
\end{table}"""

table3 = r"""\begin{table*}[t]
\centering
\caption{Performance Comparison Across Different Resource Allocation Algorithms}
\label{tab:3}
\begin{tabular}{lccccccc}
\toprule
Algorithm & P1 Avg (ms) & P1 Viol (\%) & P2 Avg (ms) & P2 Viol (\%) & P4 Avg (ms) & P4 Viol (\%) & Total Viol (\%) \\
\midrule
Proposed & 11.98 & 49.4 & 9.50 & 32.5 & 2.71 & 0.0 & 27.3 \\
PPO Standard & 11.99 & 49.4 & 9.52 & 33.6 & 3.36 & 42.0 & 41.6 \\
Double DQN & 12.00 & 49.7 & 9.48 & 31.9 & 3.33 & 39.3 & 40.3 \\
DQN & 12.04 & 51.8 & 9.50 & 33.5 & 3.34 & 39.5 & 41.6 \\
Static (Heuristic) & 11.98 & 48.9 & 9.49 & 32.8 & 3.76 & 67.2 & 49.6 \\
\bottomrule
\end{tabular}
\end{table*}"""

with open("body.tex", encoding="utf-8") as f:
    body = f.read()

body = body.replace("%%TABLE1%%", table1)
body = body.replace("%%TABLE2%%", table2)
body = body.replace("%%TABLE3%%", table3)

with open("body_final.tex", "w", encoding="utf-8") as f:
    f.write(body)
print("tables inserted, len:", len(body))
