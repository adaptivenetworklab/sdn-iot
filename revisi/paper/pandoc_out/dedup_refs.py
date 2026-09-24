import re

with open("../main.tex", encoding="utf-8") as f:
    text = f.read()

# Find all bibitem entries with their start positions, in document order
entries = list(re.finditer(r"\\bibitem\{(b\d+)\} (.*)", text))
order = [m.group(1) for m in entries]  # e.g. ['b1','b2',...,'b41']
bodies = {m.group(1): m.group(2) for m in entries}

# Identify duplicates by first-60-char signature; keep first occurrence
sig_to_first = {}
drop = set()
merge_to = {}  # dup_key -> keep_key
for key in order:
    sig = bodies[key][:60]
    if sig in sig_to_first:
        keep = sig_to_first[sig]
        drop.add(key)
        merge_to[key] = keep
    else:
        sig_to_first[sig] = key

print("dropping duplicates:", merge_to)

# Build new sequential numbering for the kept keys, in original order
kept_order = [k for k in order if k not in drop]
old_to_new = {}
for i, k in enumerate(kept_order, start=1):
    old_to_new[k] = f"b{i}"
# duplicates map to the SAME new number as their kept counterpart
for dup, keep in merge_to.items():
    old_to_new[dup] = old_to_new[keep]

# Replace all \cite{bN} tokens using old_to_new mapping
def cite_repl(m):
    key = m.group(1)
    new_key = old_to_new.get(key, key)
    return "\\cite{" + new_key + "}"

text2 = re.sub(r"\\cite\{(b\d+)\}", cite_repl, text)

# Now rebuild the bibliography block: remove dropped \bibitem paragraphs, renumber kept ones
biblio_start = text2.index("\\begin{thebibliography}")
biblio_end = text2.index("\\end{thebibliography}") + len("\\end{thebibliography}")
biblio_block = text2[biblio_start:biblio_end]

parts = re.split(r"(?=\\bibitem\{b\d+\})", biblio_block)
new_parts = [parts[0]]  # header before first bibitem (contains \begin{thebibliography}{N})
for p in parts[1:]:
    m = re.match(r"\\bibitem\{(b\d+)\} (.*)", p, re.DOTALL)
    if not m:
        new_parts.append(p)
        continue
    key = m.group(1)
    if key in drop:
        continue  # drop this whole entry
    new_key = old_to_new[key]
    new_entry = p.replace("\\bibitem{" + key + "}", "\\bibitem{" + new_key + "}", 1)
    new_parts.append(new_entry)

new_biblio_block = "".join(new_parts)
new_biblio_block = re.sub(r"\\begin\{thebibliography\}\{\d+\}", "\\\\begin{thebibliography}{" + str(len(kept_order)) + "}", new_biblio_block)

text3 = text2[:biblio_start] + new_biblio_block + text2[biblio_end:]

with open("../main.tex", "w", encoding="utf-8") as f:
    f.write(text3)

print("kept refs:", len(kept_order), "dropped:", len(drop))
