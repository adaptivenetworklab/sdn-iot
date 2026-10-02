#!/usr/bin/env bash
# Equal-budget hyperparameter search for protocol v2, sections 2.4 and 2.7.
#
# The first tuning round was launched from an inline shell that was never
# committed, so the 64 runs behind the selected configurations had no tracked
# driver. This is that driver.
#
# Every method gets the same step ceiling, the same probe cadence, the same
# number of probes, the same evaluation split and the same number of seeds.
# Trains on train, selects on val, never touches test. Safety layer off so a
# hyperparameter effect is not confounded with it.
#
#   bash scripts/run_tuning.sh [OUT_DIR] [PARALLEL] [SEEDS] [STEPS]
#
# Re-running skips finished runs, so it is safe after a power loss. The guard
# keys on the per-seed eval file: the previous round used a seed-blind guard and
# silently skipped 18 of 64 runs.

set -u
cd "$(dirname "$0")/.."

OUT=${1:-results/tuning-v2}
PAR=${2:-12}
SEEDS=${3:-2}
STEPS=${4:-300000}

# One line on purpose: this is interpolated into a job line and xargs splits on
# newlines, so a wrapped value would be executed as three truncated commands.
COMMON="--phase train --eval-phase val --safety off --device cpu --steps $STEPS --episode-len 50 --eval-every 25000 --probe-episodes 20 --eval-episodes 20 --random-init-alloc --capacity 12.0"

# Half-fraction of 2^4, so each main effect is still estimable from 8 runs.
PPO_GRID="
3e-4 0.01 clip 19.0106
3e-4 0.01 tanh 1.0
3e-4 0.0  clip 1.0
3e-4 0.0  tanh 19.0106
1e-4 0.01 clip 1.0
1e-4 0.01 tanh 19.0106
1e-4 0.0  clip 19.0106
1e-4 0.0  tanh 1.0
"

DQN_GRID="
3e-4 500  21 30000
3e-4 500  11 100000
3e-4 2000 21 100000
3e-4 2000 11 30000
1e-4 500  21 100000
1e-4 500  11 30000
1e-4 2000 21 30000
1e-4 2000 11 100000
"

JOBS=$(mktemp)

emit() {          # emit <config-dir> <algo> <extra args...>
    local dir="$OUT/$1" algo="$2"; shift 2
    local s
    for ((s = 0; s < SEEDS; s++)); do
        # Seed-aware guard: the stem includes the seed, so a finished seed 0 can
        # never mask an unfinished seed 1. The second pattern catches the arms
        # whose stem carries a suffix after the seed (_init-bc, _res0.25) --
        # with only the first pattern those 32 runs looked unfinished forever and
        # would be redone and overwritten on every resume.
        if compgen -G "$dir"/*_seed"$s"_eval.csv > /dev/null; then continue; fi
        if compgen -G "$dir"/*_seed"$s"_*_eval.csv > /dev/null; then continue; fi
        echo "python scripts/train_online.py --algo $algo --seed $s --out '$dir' $COMMON $*" >> "$JOBS"
    done
}

while read -r lr ent param rs; do
    [ -z "${lr:-}" ] && continue
    for algo in ppo sdhppo; do
        emit "${algo}_lr${lr}_ent${ent}_${param}_rs${rs}" "$algo" \
             --lr "$lr" --ent-coef "$ent" --action-param "$param" --reward-scale "$rs"
    done
    # Family (e): the two residual arms, same space and same budget as PPO.
    # residual-bound stays at its default 0.25 and is NOT part of the grid.
    emit "bcsdhppo_lr${lr}_ent${ent}_${param}_rs${rs}" sdhppo \
         --lr "$lr" --ent-coef "$ent" --action-param "$param" --reward-scale "$rs" \
         --actor-init bc
    emit "ressdhppo_lr${lr}_ent${ent}_${param}_rs${rs}" sdhppo \
         --lr "$lr" --ent-coef "$ent" --action-param "$param" --reward-scale "$rs" \
         --residual on
done <<< "$PPO_GRID"

while read -r lr ts bins ed; do
    [ -z "${lr:-}" ] && continue
    for algo in dqn ddqn; do
        emit "${algo}_lr${lr}_ts${ts}_b${bins}_ed${ed}" "$algo" \
             --lr "$lr" --target-sync "$ts" --bins "$bins" --eps-decay "$ed" --reward-scale 19.0106
    done
done <<< "$DQN_GRID"

N=$(wc -l < "$JOBS")
echo "$N runs queued (parallel $PAR) -> $OUT"
if [ "$N" -eq 0 ]; then rm -f "$JOBS"; exit 0; fi

# DRY=1 prints the job list and runs nothing. Used to check that the queue is
# what it should be before committing hours of CPU to it.
if [ "${DRY:-0}" = 1 ]; then cat "$JOBS"; rm -f "$JOBS"; exit 0; fi

mkdir -p "$OUT"
xargs -a "$JOBS" -P "$PAR" -I CMD bash -c CMD >> "$OUT/run.log" 2>&1
rm -f "$JOBS"
echo "done; log at $OUT/run.log"
