import re

with open("draft_step2.tex", encoding="utf-8") as f:
    text = f.read()

start = text.index("\\section{I. INTRODUCTION}")
refstart = text.index("\\bibitem{b1}")
body = text[start:refstart].strip()
refs = text[refstart:].strip()

# --- Figures: turn raw includegraphics + bold caption into proper figure floats ---
fig_meta = {
    "1": ("fig1_architecture.png", "SDN IoT Architecture."),
    "2": ("fig2_framework.png", "SDH-PPO Framework."),
    "3": ("fig3_tsne.png", "t-SNE Visualization."),
    "4": ("fig4_port_delay_track.png", "Port Delay Track."),
    "5": ("fig5_dqn_convergence.png", "DQN Convergence \\& Reward Progress."),
    "6": ("fig6_ddqn_convergence.png", "DDQN Convergence \\& Reward Progress."),
    "7": ("fig7_ppo_convergence.png", "PPO Convergence \\& Reward Progress."),
    "8": ("fig8_sdh_ppo_convergence.png", "SDH-PPO (Proposed) Convergence \\& Reward Progress."),
}

def fig_block(imgnum, figfile, caption):
    return (
        "\\begin{figure}[htbp]\n\\centering\n"
        f"\\includegraphics[width=\\columnwidth]{{figures/{figfile}}}\n"
        f"\\caption{{{caption}}}\n\\label{{fig:{imgnum}}}\n"
        "\\end{figure}\n"
    )

# pattern A: includegraphics on its own line, caption bold on next non-empty line
pat_a = re.compile(
    r"\\includegraphics\[[^\]]*\]\{paper/pandoc_out/media/image(\d+)\.png\}\n\n\\textbf\{Fig\. \d+\.\} ([^\n]*)"
)
def repl_a(m):
    num, cap = m.group(1), m.group(2)
    figfile, fixed_cap = fig_meta[num]
    return fig_block(num, figfile, fixed_cap)
body, na = pat_a.subn(repl_a, body)

# pattern B: includegraphics immediately followed by caption on same line (Fig 7/8 case)
pat_b = re.compile(
    r"\\includegraphics\[[^\]]*\]\{paper/pandoc_out/media/image(\d+)\.png\}\\textbf\{Fig\. \d+\.\} ([^\n]*)"
)
def repl_b(m):
    num, cap = m.group(1), m.group(2)
    figfile, fixed_cap = fig_meta[num]
    return fig_block(num, figfile, fixed_cap)
body, nb = pat_b.subn(repl_b, body)

print("figures converted (pattern A/B):", na, nb)

# --- Remove the 3 raw longtable table blocks, replace with placeholders ---
table_pat = re.compile(
    r"TABLE (I{1,3})\n\n\\textsc\{[^}]*\}\n\n\{\\def\\LTcaptype\{none\}.*?\\end\{longtable\}\n\}\n?",
    re.DOTALL
)
matches = table_pat.findall(body)
print("table blocks found:", matches)
counter = [0]
def table_repl(m):
    counter[0] += 1
    return f"%%TABLE{counter[0]}%%\n"
body, nt = table_pat.subn(table_repl, body)
print("table blocks replaced:", nt)

with open("body.tex", "w", encoding="utf-8") as f:
    f.write(body)
with open("refs.tex", "w", encoding="utf-8") as f:
    f.write(refs)
print("done")
