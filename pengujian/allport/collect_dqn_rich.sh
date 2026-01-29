#!/bin/bash
set -e

BRIDGE=${1:-br0}
DURATION=${2:-3600}
INTERVAL=${3:-1}

# kapasitas link (Mbps) untuk utilization (%)
LINK_CAP_Mbps=${4:-10000}

P1=1
P2=2
P4=4

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DELAY_LOG="$BASE_DIR/delay_log.csv"

OUT="$SCRIPT_DIR/dataset_dqn_rich.csv"
LOG="$SCRIPT_DIR/dataset_dqn_rich.log"

echo "[START] $(date -u +"%Y-%m-%dT%H:%M:%SZ") bridge=$BRIDGE duration=$DURATION interval=$INTERVAL" > "$LOG"

echo "timestamp,\
rx_mbps_p1,tx_mbps_p1,rx_pps_p1,tx_pps_p1,avg_rx_pkt_bytes_p1,util_rx_pct_p1,drop_p1,delay_ms_p1,last_payload_bytes_p1,\
rx_mbps_p2,tx_mbps_p2,rx_pps_p2,tx_pps_p2,avg_rx_pkt_bytes_p2,util_rx_pct_p2,drop_p2,delay_ms_p2,last_payload_bytes_p2,\
rx_mbps_p4,tx_mbps_p4,rx_pps_p4,tx_pps_p4,avg_rx_pkt_bytes_p4,util_rx_pct_p4,drop_p4,delay_ms_p4,last_payload_bytes_p4" > "$OUT"


get_port_stats () {
  local bridge=$1
  local port=$2

  # output: rx_pkts rx_bytes tx_pkts tx_bytes rx_drop
  local block
  block=$(sudo ovs-ofctl dump-ports "$bridge" 2>/dev/null | awk -v p="$port" '
    $1=="port" && ($2==p":" || $2==p || $2 ~ p":") {flag=1; print; next}
    flag==1 {print; if ($1=="tx") {flag=0}}
  ')

  local rx_pkts rx_bytes tx_pkts tx_bytes rx_drop

  rx_pkts=$(echo "$block" | sed -n 's/.*rx pkts=\([0-9]\+\).*/\1/p' | head -n 1)
  rx_bytes=$(echo "$block" | sed -n 's/.*rx pkts=.*bytes=\([0-9]\+\).*/\1/p' | head -n 1)

  tx_pkts=$(echo "$block" | sed -n 's/.*tx pkts=\([0-9]\+\).*/\1/p' | head -n 1)
  tx_bytes=$(echo "$block" | sed -n 's/.*tx pkts=.*bytes=\([0-9]\+\).*/\1/p' | head -n 1)

  rx_drop=$(echo "$block" | sed -n 's/.*rx pkts=.*drop=\([0-9]\+\).*/\1/p' | head -n 1)

  rx_pkts=${rx_pkts:-0}
  rx_bytes=${rx_bytes:-0}
  tx_pkts=${tx_pkts:-0}
  tx_bytes=${tx_bytes:-0}
  rx_drop=${rx_drop:-0}

  echo "$rx_pkts $rx_bytes $tx_pkts $tx_bytes $rx_drop"
}

get_delay_and_payload () {
  local devid="$1"

  if [ ! -f "$DELAY_LOG" ]; then
    echo "0 0"
    return
  fi

  # delay_log format v2:
  # timestamp,device_id,src_ip,seq,payload_bytes,delay_ms,type
  tail -n 800 "$DELAY_LOG" | awk -F',' -v d="$devid" '
    $2==d { last_delay=$6; last_bytes=$5 }
    END {
      if (last_delay=="") last_delay="0";
      if (last_bytes=="") last_bytes="0";
      gsub(/[^0-9\.\-]/,"",last_delay);
      gsub(/[^0-9]/,"",last_bytes);
      print last_delay, last_bytes
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

calc_pps () {
  local cur=$1
  local prev=$2
  local interval=$3

  python3 - <<PY
cur=float("$cur"); prev=float("$prev"); interval=float("$interval")
print((cur-prev)/interval)
PY
}

calc_avg_pkt_bytes () {
  local dbytes=$1
  local dpkts=$2

  python3 - <<PY
dbytes=float("$dbytes"); dpkts=float("$dpkts")
if dpkts <= 0:
    print(0)
else:
    print(dbytes/dpkts)
PY
}

calc_util_pct () {
  local rx_mbps=$1
  local cap=$2

  python3 - <<PY
rx=float("$rx_mbps"); cap=float("$cap")
if cap <= 0:
    print(0)
else:
    print((rx/cap)*100.0)
PY
}


# init prev stats
read p1_rxpk_prev p1_rx_prev p1_txpk_prev p1_tx_prev p1_drop_prev <<< $(get_port_stats "$BRIDGE" "$P1")
read p2_rxpk_prev p2_rx_prev p2_txpk_prev p2_tx_prev p2_drop_prev <<< $(get_port_stats "$BRIDGE" "$P2")
read p4_rxpk_prev p4_rx_prev p4_txpk_prev p4_tx_prev p4_drop_prev <<< $(get_port_stats "$BRIDGE" "$P4")

START=$(date +%s)
END=$((START + DURATION))

echo "[INFO] Delay log path: $DELAY_LOG" | tee -a "$LOG"
echo "[INFO] Output dataset : $OUT" | tee -a "$LOG"

while [ "$(date +%s)" -lt "$END" ]; do
  TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

  read p1_rxpk p1_rx p1_txpk p1_tx p1_drop <<< $(get_port_stats "$BRIDGE" "$P1")
  read p2_rxpk p2_rx p2_txpk p2_tx p2_drop <<< $(get_port_stats "$BRIDGE" "$P2")
  read p4_rxpk p4_rx p4_txpk p4_tx p4_drop <<< $(get_port_stats "$BRIDGE" "$P4")

  # mbps
  p1_rx_mbps=$(calc_mbps "$p1_rx" "$p1_rx_prev" "$INTERVAL")
  p1_tx_mbps=$(calc_mbps "$p1_tx" "$p1_tx_prev" "$INTERVAL")
  p2_rx_mbps=$(calc_mbps "$p2_rx" "$p2_rx_prev" "$INTERVAL")
  p2_tx_mbps=$(calc_mbps "$p2_tx" "$p2_tx_prev" "$INTERVAL")
  p4_rx_mbps=$(calc_mbps "$p4_rx" "$p4_rx_prev" "$INTERVAL")
  p4_tx_mbps=$(calc_mbps "$p4_tx" "$p4_tx_prev" "$INTERVAL")

  # pps
  p1_rx_pps=$(calc_pps "$p1_rxpk" "$p1_rxpk_prev" "$INTERVAL")
  p1_tx_pps=$(calc_pps "$p1_txpk" "$p1_txpk_prev" "$INTERVAL")
  p2_rx_pps=$(calc_pps "$p2_rxpk" "$p2_rxpk_prev" "$INTERVAL")
  p2_tx_pps=$(calc_pps "$p2_txpk" "$p2_txpk_prev" "$INTERVAL")
  p4_rx_pps=$(calc_pps "$p4_rxpk" "$p4_rxpk_prev" "$INTERVAL")
  p4_tx_pps=$(calc_pps "$p4_txpk" "$p4_txpk_prev" "$INTERVAL")

  # avg packet size rx
  p1_avg_rx_pkt=$(calc_avg_pkt_bytes "$((p1_rx - p1_rx_prev))" "$((p1_rxpk - p1_rxpk_prev))")
  p2_avg_rx_pkt=$(calc_avg_pkt_bytes "$((p2_rx - p2_rx_prev))" "$((p2_rxpk - p2_rxpk_prev))")
  p4_avg_rx_pkt=$(calc_avg_pkt_bytes "$((p4_rx - p4_rx_prev))" "$((p4_rxpk - p4_rxpk_prev))")

  # utilization rx (%)
  p1_util=$(calc_util_pct "$p1_rx_mbps" "$LINK_CAP_Mbps")
  p2_util=$(calc_util_pct "$p2_rx_mbps" "$LINK_CAP_Mbps")
  p4_util=$(calc_util_pct "$p4_rx_mbps" "$LINK_CAP_Mbps")

  # drop delta
  p1_drop_delta=$((p1_drop - p1_drop_prev))
  p2_drop_delta=$((p2_drop - p2_drop_prev))
  p4_drop_delta=$((p4_drop - p4_drop_prev))

  # delay + payload bytes (from delay_log.csv v2)
  read delay_p1 last_bytes_p1 <<< $(get_delay_and_payload "dht11")
  read delay_p2 last_bytes_p2 <<< $(get_delay_and_payload "camera")
  read delay_p4 last_bytes_p4 <<< $(get_delay_and_payload "max")

  echo "$TS,\
$p1_rx_mbps,$p1_tx_mbps,$p1_rx_pps,$p1_tx_pps,$p1_avg_rx_pkt,$p1_util,$p1_drop_delta,$delay_p1,$last_bytes_p1,\
$p2_rx_mbps,$p2_tx_mbps,$p2_rx_pps,$p2_tx_pps,$p2_avg_rx_pkt,$p2_util,$p2_drop_delta,$delay_p2,$last_bytes_p2,\
$p4_rx_mbps,$p4_tx_mbps,$p4_rx_pps,$p4_tx_pps,$p4_avg_rx_pkt,$p4_util,$p4_drop_delta,$delay_p4,$last_bytes_p4" >> "$OUT"

  # update prev
  p1_rxpk_prev=$p1_rxpk; p1_rx_prev=$p1_rx; p1_txpk_prev=$p1_txpk; p1_tx_prev=$p1_tx; p1_drop_prev=$p1_drop
  p2_rxpk_prev=$p2_rxpk; p2_rx_prev=$p2_rx; p2_txpk_prev=$p2_txpk; p2_tx_prev=$p2_tx; p2_drop_prev=$p2_drop
  p4_rxpk_prev=$p4_rxpk; p4_rx_prev=$p4_rx; p4_txpk_prev=$p4_txpk; p4_tx_prev=$p4_tx; p4_drop_prev=$p4_drop

  rows=$(($(wc -l < "$OUT") - 1))
  echo "[PROGRESS] ts=$TS rows=$rows dht11_delay=$delay_p1 cam_delay=$delay_p2 max_delay=$delay_p4" | tee -a "$LOG"

  sleep "$INTERVAL"
done

echo "[DONE] Saved -> $OUT" | tee -a "$LOG"
