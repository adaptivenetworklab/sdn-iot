import re

with open("draft.tex", encoding="utf-8") as f:
    body = f.read()

body = re.sub(r"\{\[\}(\d+)\{\]\}", lambda m: "\\cite{b" + m.group(1) + "}", body)

def eq_repl(m):
    content = m.group(1).strip()
    content = re.sub(r"\\#\(\d+\)\s*$", "", content).strip()
    num = m.group(2)
    return "\\begin{equation}\\label{eq:" + num + "}\n" + content + "\n\\end{equation}"

pattern = re.compile(r"\\\[\\begin\{array\}\{r\}\n(.*?)\\#\((\d+)\)\n\\end\{array\}\\\]", re.DOTALL)
body2, n = pattern.subn(eq_repl, body)
print("equation blocks converted:", n)

with open("draft_step1.tex", "w", encoding="utf-8") as f:
    f.write(body2)
