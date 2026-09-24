#!/bin/bash
set -e

BRIDGE=${1:-br0}
DURATION=${2:-3600}
INTERVAL=${3:-1}

P1=1
P2=2
P4=4

# ✅ auto detect base dir (sdn-iot/pengujian)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"  # .../pengujian
DELAY_LOG="$BASE_DIR/delay_log.csv"

OUT="$SCRIPT_DIR/dataset_dqn.csv"
LOG="$SCRIPT_DIR/dataset_dqn.log"

echo "[START] $(date -u +"%Y-%m-%dT%H:%M:%SZ") bridge=$BRIDGE duration=$DURATION interval=$INTERVAL" > "$LOG"

echo "timestamp,rx_mbps_p1,tx_mbps_p1,drop_p1,delay_ms_p1,rx_mbps_p2,tx_mbps_p2,drop_p2,delay_ms_p2,rx_mbps_p4,tx_mbps_p4,drop_p4,delay_ms_p4" > "$OUT"

get_port_stats () {
  local bridge=$1
  local port=$2

  local block=$(sudo ovs-ofctl dump-ports "$bridge" 2>/dev/null | awk -v p="$port" '
    $1=="port" && ($2==p":" || $2==p || $2 ~ p":") {flag=1; print; next}
    flag==1 {print; if ($1=="tx") {flag=0}}
  ')

  local rx_bytes=$(echo "$block" | sed -n 's/.*rx pkts=.*bytes=\([0-9]\+\).*/\1/p' | head -n 1)
  local tx_bytes=$(echo "$block" | sed -n 's/.*tx pkts=.*bytes=\([0-9]\+\).*/\1/p' | head -n 1)
  local rx_drop=$(echo "$block" | sed -n 's/.*rx pkts=.*drop=\([0-9]\+\).*/\1/p' | head -n 1)

  rx_bytes=${rx_bytes:-0}
  tx_bytes=${tx_bytes:-0}
  rx_drop=${rx_drop:-0}

  echo "$rx_bytes $tx_bytes $rx_drop"
}

get_delay_ms () {
  local devid="$1"

  if [ ! -f "$DELAY_LOG" ]; then
    echo "0"
    return
  fi

  # ambil delay terbaru utk device_id
  tail -n 500 "$DELAY_LOG" | awk -F',' -v d="$devid" '
    $2==d {last=$4}
    END {
      if (last=="") print "0";
      else {
        gsub(/[^0-9\.\-]/,"",last);
        print last
      }
    }'
}

calc_mbps () {
  local cur=$1
  local prev=$2
  local interval=$3

  python3 - <<PY
cur=float("$cur"); prev=float("$prev"); interval=float("$interval")
print(((cur-prev)*8.0)/(interval*1000000.0))
PY
}

read p1_rx_prev p1_tx_prev p1_drop_prev <<< $(get_port_stats "$BRIDGE" "$P1")
read p2_rx_prev p2_tx_prev p2_drop_prev <<< $(get_port_stats "$BRIDGE" "$P2")
read p4_rx_prev p4_tx_prev p4_drop_prev <<< $(get_port_stats "$BRIDGE" "$P4")

START=$(date +%s)
END=$((START + DURATION))

echo "[INFO] Delay log path: $DELAY_LOG" | tee -a "$LOG"
echo "[INFO] Output dataset : $OUT" | tee -a "$LOG"

while [ "$(date +%s)" -lt "$END" ]; do
  TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

  read p1_rx p1_tx p1_drop <<< $(get_port_stats "$BRIDGE" "$P1")
  read p2_rx p2_tx p2_drop <<< $(get_port_stats "$BRIDGE" "$P2")
  read p4_rx p4_tx p4_drop <<< $(get_port_stats "$BRIDGE" "$P4")

  p1_rx_mbps=$(calc_mbps "$p1_rx" "$p1_rx_prev" "$INTERVAL")
  p1_tx_mbps=$(calc_mbps "$p1_tx" "$p1_tx_prev" "$INTERVAL")

  p2_rx_mbps=$(calc_mbps "$p2_rx" "$p2_rx_prev" "$INTERVAL")
  p2_tx_mbps=$(calc_mbps "$p2_tx" "$p2_tx_prev" "$INTERVAL")

  p4_rx_mbps=$(calc_mbps "$p4_rx" "$p4_rx_prev" "$INTERVAL")
  p4_tx_mbps=$(calc_mbps "$p4_tx" "$p4_tx_prev" "$INTERVAL")

  p1_drop_delta=$((p1_drop - p1_drop_prev))
  p2_drop_delta=$((p2_drop - p2_drop_prev))
  p4_drop_delta=$((p4_drop - p4_drop_prev))

  delay_p1=$(get_delay_ms "dht11")
  delay_p2=$(get_delay_ms "camera")
  delay_p4=$(get_delay_ms "max")

  echo "$TS,$p1_rx_mbps,$p1_tx_mbps,$p1_drop_delta,$delay_p1,$p2_rx_mbps,$p2_tx_mbps,$p2_drop_delta,$delay_p2,$p4_rx_mbps,$p4_tx_mbps,$p4_drop_delta,$delay_p4" >> "$OUT"

  p1_rx_prev=$p1_rx; p1_tx_prev=$p1_tx; p1_drop_prev=$p1_drop
  p2_rx_prev=$p2_rx; p2_tx_prev=$p2_tx; p2_drop_prev=$p2_drop
  p4_rx_prev=$p4_rx; p4_tx_prev=$p4_tx; p4_drop_prev=$p4_drop

  rows=$(($(wc -l < "$OUT") - 1))
  echo "[PROGRESS] ts=$TS rows=$rows delay(dht11)=$delay_p1 delay(camera)=$delay_p2 delay(max)=$delay_p4" | tee -a "$LOG"

  sleep "$INTERVAL"
done

echo "[DONE] Saved -> $OUT" | tee -a "$LOG"
