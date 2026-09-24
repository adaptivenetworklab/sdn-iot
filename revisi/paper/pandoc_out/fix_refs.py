import re

with open("draft_step1.tex", encoding="utf-8") as f:
    text = f.read()

marker = "\\textsc{References}"
idx = text.index(marker)
head = text[:idx]
tail = text[idx + len(marker):]

# In the references tail, each entry is its own paragraph starting with \cite{bN}
tail2, n = re.subn(r"\\cite\{b(\d+)\} ", lambda m: "\\bibitem{b" + m.group(1) + "} ", tail)

with open("draft_step2.tex", "w", encoding="utf-8") as f:
    f.write(head + tail2)
print("bibitem entries fixed:", n)
