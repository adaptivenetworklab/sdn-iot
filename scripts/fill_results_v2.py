"""Fill the generated blocks of docs/experiments/08-results-v2.md. No result number is typed by hand.

    python scripts/fill_results_v2.py

Blocks copied verbatim from results/analysis-v2/report.md (written by the frozen analyze_v2.py):
primer, eksploratif, iqm, poi, sekunder, skenario, sensitivitas.
Blocks computed here:
  integrity  - run count, commit, split, device, steps from every run's JSON; retries from run.log
  ckpt       - POST HOC, EXPLORATORY: where the val probe placed the selected checkpoint
Blocks copied verbatim from results/analysis-v2/fidelity_c4.md (scripts/fidelity_c4.py):
c4_marginal, c4_disc, c4_desc.
"""

import json
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "experiments" / "08-results-v2.md"
ANA = ROOT / "results" / "analysis-v2"
RUNS = ROOT / "results" / "final-v2"
SECTIONS = {"primer": "Primer", "eksploratif": "Eksploratif", "iqm": "IQM", "poi": "Probability",
            "sekunder": "Sekunder", "skenario": "Skenario", "sensitivitas": "Sensitivitas"}


C4 = {"c4_marginal": "Marginal", "c4_disc": "Discriminator", "c4_desc": "Deskriptif"}


def report_sections(path=ANA / "report.md", sections=SECTIONS):
    parts = re.split(r"^## ", path.read_text(encoding="utf-8"), flags=re.M)[1:]
    out = {}
    for name, prefix in sections.items():
        hit = [p for p in parts if p.startswith(prefix)]
        assert len(hit) == 1, f"section {prefix!r} not found exactly once"
        out[name] = hit[0].split("\n", 1)[1].strip()
    return out


def integrity():
    metas = [json.loads(p.read_text()) for p in RUNS.glob("*/*.json")]
    key = pd.DataFrame([{"commit": m["git_commit"][:7], "eval_phase": m["args"]["eval_phase"],
                         "device": m["args"]["device"], "steps": m["args"]["steps"]} for m in metas])
    log = (RUNS / "run.log").read_text(encoding="utf-8")
    rows = key.value_counts().reset_index(name="runs")
    fails = RUNS / "failures.log"
    return (rows.to_markdown(index=False) + "\n\n"
            f"Eval CSV: {len(list(RUNS.glob('*/*_seed*_eval.csv')))}. "
            f"Baris `RETRIED` di run.log: {log.count('(RETRIED)')}; `FAILED`: {log.count('(FAILED)')}; "
            f"failures.log: {'ada' if fails.exists() else 'tidak ada'}.")


def ckpt():
    runs = pd.read_csv(ANA / "per_run.csv")
    cur = pd.read_csv(ANA / "curves.csv")
    first, last = cur.probe.min(), cur.probe.max()
    rows = []
    for cell, g in runs.dropna(subset=["best_val_step"]).groupby("cell"):
        c = cur[cur.cell == cell]
        p1 = c[c.probe == first].step.iloc[0]
        rows.append({"cell": cell, "n": len(g),
                     "seed dgn checkpoint di probe pertama": int((g.best_val_step == p1).sum()),
                     "median best_val_step": g.best_val_step.median(),
                     f"mean val_viol probe {first}": c[c.probe == first].val_viol.mean(),
                     f"mean val_viol probe {last}": c[c.probe == last].val_viol.mean()})
    return pd.DataFrame(rows).to_markdown(index=False, floatfmt=".2f")


def main():
    blocks = (report_sections() | report_sections(ANA / "fidelity_c4.md", C4)
              | {"integrity": integrity(), "ckpt": ckpt()})
    text = DOC.read_text(encoding="utf-8")
    for name, body in blocks.items():
        pat = re.compile(rf"(<!-- BEGIN GENERATED {name} -->\n).*?(<!-- END GENERATED {name} -->)", re.S)
        assert pat.search(text), f"block {name} missing in {DOC.name}"
        text = pat.sub(lambda m: m[1] + body + "\n" + m[2], text)
    DOC.write_text(text, encoding="utf-8")
    print(f"filled {len(blocks)} blocks -> {DOC}")


if __name__ == "__main__":
    main()
