import re

text = open("../main.tex", encoding="utf-8").read()
entries = re.findall(r"\\bibitem\{(b\d+)\} (.*)", text)
print("total entries:", len(entries))
seen = {}
for key, body in entries:
    sig = body[:60]
    seen.setdefault(sig, []).append(key)
for sig, keys in seen.items():
    if len(keys) > 1:
        print(keys, "->", sig)
