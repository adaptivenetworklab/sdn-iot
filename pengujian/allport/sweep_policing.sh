#!/bin/bash
# Sweep driver: varies ingress_policing_rate per OVS interface on a schedule.
#
# Run this ALONGSIDE collect_policy.sh. That collector already reads
# ingress_policing_rate from ovs-vsctl every interval (collect_policy.sh:101),
# so it records whatever this script sets -- no change to the collector is
# needed, and the two logs join on timestamp.
#
#   terminal 1:  ./collect_policy.sh br0 7200 1 10000
#   terminal 2:  ./sweep_policing.sh single
#
# Why this exists: the previous campaign left ingress_policing_rate at
# 1000000 kbps on every port for the whole run, so the dataset contains zero
# information about what the control action does. See
# docs/experiments/02-blocker-no-action-variance.md
#
# Requires sudo ovs-vsctl. Restores the original rates on exit.

set -uo pipefail

BRIDGE=${BRIDGE:-br0}
MODE=${1:-single}          # single | joint
DWELL=${DWELL:-60}         # seconds held at each setting
REPEATS=${REPEATS:-3}      # passes over the grid
SETTLE=${SETTLE:-5}        # seconds discarded after a change (marked in log)
SEED=${SEED:-42}

IF_P1="dht11"
IF_P2="camera"
IF_P4="max"
IFACES=("$IF_P1" "$IF_P2" "$IF_P4")

# Grid in kbps. Measured traffic is ~3.8-4.6 Mbps per port, so this brackets
# the operating point: starved -> matched -> unconstrained.
GRID=(1000 2000 3000 4000 5000 6000 8000 10000 15000 1000000)

# Burst tracks the old fixed ratio (burst = 10% of rate), floored so small
# rates stay deliverable.
burst_for () {
  local rate=$1
  local b=$(( rate / 10 ))
  [ "$b" -lt 100 ] && b=100
  echo "$b"
}

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLAN_LOG="$SCRIPT_DIR/sweep_plan.csv"

declare -A ORIG_RATE ORIG_BURST

save_original () {
  for i in "${IFACES[@]}"; do
    ORIG_RATE[$i]=$(sudo ovs-vsctl get interface "$i" ingress_policing_rate 2>/dev/null | tr -dc '0-9')
    ORIG_BURST[$i]=$(sudo ovs-vsctl get interface "$i" ingress_policing_burst 2>/dev/null | tr -dc '0-9')
    ORIG_RATE[$i]=${ORIG_RATE[$i]:-0}
    ORIG_BURST[$i]=${ORIG_BURST[$i]:-0}
  done
  echo "[INFO] original rates: p1=${ORIG_RATE[$IF_P1]} p2=${ORIG_RATE[$IF_P2]} p4=${ORIG_RATE[$IF_P4]}"
}

restore () {
  echo
  echo "[INFO] restoring original policing rates"
  for i in "${IFACES[@]}"; do
    sudo ovs-vsctl set interface "$i" \
      ingress_policing_rate="${ORIG_RATE[$i]}" \
      ingress_policing_burst="${ORIG_BURST[$i]}" 2>/dev/null
  done
  echo "[DONE] plan log -> $PLAN_LOG"
}
trap restore EXIT INT TERM

set_rate () {
  local ifname=$1 rate=$2
  local burst; burst=$(burst_for "$rate")
  sudo ovs-vsctl set interface "$ifname" \
    ingress_policing_rate="$rate" \
    ingress_policing_burst="$burst"
}

# Randomised visit order, seeded for reproducibility. Order is randomised so a
# slow drift in the testbed (thermal, background load, clock) cannot be
# mistaken for an effect of the rate.
shuffled () {
  local salt=$1; shift
  printf '%s\n' "$@" | python3 -c "
import sys, random
random.seed($SEED + $salt)
xs = [l.strip() for l in sys.stdin if l.strip()]
random.shuffle(xs)
print('\n'.join(xs))
"
}

log_row () {
  echo "$1,$2,$3,$4,$5,$6,$7" >> "$PLAN_LOG"
}

read_rates () {
  local r1 r2 r4
  r1=$(sudo ovs-vsctl get interface "$IF_P1" ingress_policing_rate | tr -dc '0-9')
  r2=$(sudo ovs-vsctl get interface "$IF_P2" ingress_policing_rate | tr -dc '0-9')
  r4=$(sudo ovs-vsctl get interface "$IF_P4" ingress_policing_rate | tr -dc '0-9')
  echo "${r1:-0} ${r2:-0} ${r4:-0}"
}

save_original

if [ ! -f "$PLAN_LOG" ]; then
  echo "ts_utc,phase,pass,target_iface,rate_p1_kbps,rate_p2_kbps,rate_p4_kbps" > "$PLAN_LOG"
fi

UNCONSTRAINED=1000000

echo "[START] mode=$MODE dwell=${DWELL}s repeats=$REPEATS settle=${SETTLE}s"

if [ "$MODE" = "single" ]; then
  # Phase A -- vary ONE port, hold the others unconstrained. Isolates the
  # direct effect of rate on that port's own delay.
  total=$(( ${#IFACES[@]} * ${#GRID[@]} * REPEATS * DWELL ))
  echo "[INFO] phase A estimated duration: $((total / 60)) min"

  for (( pass=1; pass<=REPEATS; pass++ )); do
    for target in "${IFACES[@]}"; do
      for i in "${IFACES[@]}"; do set_rate "$i" "$UNCONSTRAINED"; done
      while read -r rate; do
        set_rate "$target" "$rate"
        sleep "$SETTLE"
        ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
        read -r r1 r2 r4 <<< "$(read_rates)"
        log_row "$ts" "A_single" "$pass" "$target" "$r1" "$r2" "$r4"
        echo "[SET] pass=$pass target=$target rate=${rate}kbps (p1=$r1 p2=$r2 p4=$r4)"
        sleep "$(( DWELL - SETTLE ))"
      done < <(shuffled "$pass" "${GRID[@]}")
    done
  done

elif [ "$MODE" = "joint" ]; then
  # Phase B -- all ports constrained together. Tests whether constraining one
  # slice affects the others, which is the coupling the simulator needs.
  JOINT=(1000 2000 4000 6000 10000 1000000)
  total=$(( ${#JOINT[@]} * REPEATS * DWELL ))
  echo "[INFO] phase B estimated duration: $((total / 60)) min"

  for (( pass=1; pass<=REPEATS; pass++ )); do
    while read -r rate; do
      for i in "${IFACES[@]}"; do set_rate "$i" "$rate"; done
      sleep "$SETTLE"
      ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
      read -r r1 r2 r4 <<< "$(read_rates)"
      log_row "$ts" "B_joint" "$pass" "all" "$r1" "$r2" "$r4"
      echo "[SET] pass=$pass all ports rate=${rate}kbps"
      sleep "$(( DWELL - SETTLE ))"
    done < <(shuffled "$(( pass + 1000 ))" "${JOINT[@]}")
  done

else
  echo "[ERROR] unknown mode '$MODE' (expected: single | joint)" >&2
  exit 2
fi

echo "[DONE] sweep complete"
