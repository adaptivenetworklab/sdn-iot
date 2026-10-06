"""Reproduce selected V2 final runs through run_v3.py and compare with the archive.

Arguments are rebuilt from each archived run JSON ("args"), so the rerun uses the
exact V2 configuration; only --out differs. The evaluation CSVs (_eval,
_eval_diurnal, _eval_flash) are compared byte for byte and row by row with the
copies in sdn-iot-archive/final-v2-raw-csv.zip. Nothing in scripts/ or
results/final-v2/ is written.

Note: these runs read the test split again (--allow-test, as in V2). They only
reproduce numbers that already exist; they produce no new test result.

    python scripts_v3/verify_v2_repro.py run       # launch in parallel, then compare
    python scripts_v3/verify_v2_repro.py compare   # compare existing outputs only
"""
import io
import json
import subprocess
import sys
import time
import zipfile
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT.parent / "sdn-iot-archive" / "final-v2-raw-csv.zip"
OUT = ROOT / "results" / "v3" / "verify"
V2_SOURCE = (ROOT / "scripts" / "train_online.py").read_text(encoding="utf-8")
RUNS = [("dqn_aug_subsample_safetyoff", "dqn_aug_subsample_train_safetyoff_seed0"),
        ("ddqn_full_safetyon", "ddqn_full_train_safetyon_seed1"),
        ("ddqn_real_only_safetyoff", "ddqn_real_only_train_safetyoff_seed2")]
SUFFIXES = ("_eval.csv", "_eval_diurnal.csv", "_eval_flash.csv")


def argv_from_v2(cell, stem):
    """CLI arguments equivalent to the archived run's parsed arguments."""
    args = json.loads((ROOT / "results" / "final-v2" / cell / f"{stem}.json")
                      .read_text(encoding="utf-8"))["args"]
    argv = []
    for key, val in args.items():
        if key == "out" or val is None or val is False:
            continue
        flag = "--" + key.replace("_", "-")
        assert f'"{flag}"' in V2_SOURCE, f"{flag} is not an option of train_online.py"
        if val is True:
            argv.append(flag)
        elif isinstance(val, list):
            for v in val:
                argv += [flag, str(v)]
        else:
            argv += [flag, str(val)]
    return argv + ["--out", str(OUT / cell)], args


def run():
    procs = []
    for cell, stem in RUNS:
        argv, _ = argv_from_v2(cell, stem)
        log = open(OUT / f"{stem}.log", "w", encoding="utf-8")
        t0 = time.time()
        p = subprocess.Popen([sys.executable, str(ROOT / "scripts_v3" / "run_v3.py"), *argv],
                             cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
        procs.append((stem, p, t0, log))
        print(f"started {stem} pid {p.pid}", flush=True)
    for stem, p, t0, log in procs:
        rc = p.wait()
        log.close()
        print(f"finished {stem}: exit {rc}, {(time.time() - t0) / 60:.1f} min", flush=True)


def compare():
    z = zipfile.ZipFile(ARCHIVE)
    all_same = True
    for cell, stem in RUNS:
        new_args = json.loads((OUT / cell / f"{stem}.json").read_text(encoding="utf-8"))["args"]
        _, old_args = argv_from_v2(cell, stem)
        diff = {k for k in old_args if k != "out" and old_args[k] != new_args.get(k)}
        print(f"{stem}: argumen berbeda dari V2: {sorted(diff) or 'tidak ada'}")
        for suf in SUFFIXES:
            old = z.read(f"results/final-v2/{cell}/{stem}{suf}")
            new = (OUT / cell / f"{stem}{suf}").read_bytes()
            a, b = pd.read_csv(io.BytesIO(old)), pd.read_csv(io.BytesIO(new))
            same_rows = len(a) == len(b) and list(a.columns) == list(b.columns)
            bad = [] if not same_rows else [i for i in range(len(a)) if not a.iloc[i].equals(b.iloc[i])]
            ok = old == new and same_rows and not bad
            all_same &= ok
            print(f"  {suf:18s} byte-identik={old == new}  baris {len(a)} vs {len(b)}  "
                  f"baris berbeda={len(bad) if same_rows else 'struktur beda'}"
                  + (f" (pertama: {bad[:5]})" if bad else ""))
    print("SEMUA IDENTIK" if all_same else "ADA PERBEDAAN")
    return 0 if all_same else 1


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    mode = sys.argv[1] if len(sys.argv) > 1 else "run"
    if mode == "run":
        run()
    sys.exit(compare())
