#!/bin/bash

BRIDGE=${1:-br0}
DURATION=${2:-3600}   # 1 jam
INTERVAL=${3:-1}      # 1 detik

P1=1
P2=2
P4=4

OUT="dataset_dqn.csv"
LOG="dataset_dqn.log"

echo "[START] $(date -u +"%Y-%m-%dT%H:%M:%SZ") bridge=$BRIDGE duration=$DURATION interval=$INTERVAL" > "$LOG"

# CSV header rapi (1 baris = 1 state)
echo "timestamp,rx_mbps_p1,tx_mbps_p1,drop_p1,delay_ms_p1,rx_mbps_p2,tx_mbps_p2,drop_p2,delay_ms_p2,rx_mbps_p4,tx_mbps_p4,drop_p4,delay_ms_p4" > "$OUT"

get_port_stats() {
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

# ambil delay terakhir per device_id dari delay_log.csv
get_delay_ms() {
  local devid="$1"
  # ambil last delay_ms dari device tersebut
  tail -n 200 /home/ovs/pengujian/delay_log.csv 2>/dev/null | awk -F',' -v d="$devid" '$2==d {last=$4} END{print last}'
}

# init prev
read p1_rx_prev p1_tx_prev p1_drop_prev <<< $(get_port_stats "$BRIDGE" "$P1")
read p2_rx_prev p2_tx_prev p2_drop_prev <<< $(get_port_stats "$BRIDGE" "$P2")
read p4_rx_prev p4_tx_prev p4_drop_prev <<< $(get_port_stats "$BRIDGE" "$P4")

START=$SECONDS
END=$((SECONDS + DURATION))

while [ $SECONDS -lt $END ]; do
  TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

  read p1_rx p1_tx p1_drop <<< $(get_port_stats "$BRIDGE" "$P1")
  read p2_rx p2_tx p2_drop <<< $(get_port_stats "$BRIDGE" "$P2")
  read p4_rx p4_tx p4_drop <<< $(get_port_stats "$BRIDGE" "$P4")

  # throughput Mbps (delta bytes)
  p1_rx_mbps=$(python3 - <<PY
print((($p1_rx-$p1_rx_prev)*8)/($INTERVAL*1_000_000))
PY
)
  p1_tx_mbps=$(python3 - <<PY
print((($p1_tx-$p1_tx_prev)*8)/($INTERVAL*1_000_000))
PY
)
  p2_rx_mbps=$(python3 - <<PY
print((($p2_rx-$p2_rx_prev)*8)/($INTERVAL*1_000_000))
PY
)
  p2_tx_mbps=$(python3 - <<PY
print((($p2_tx-$p2_tx_prev)*8)/($INTERVAL*1_000_000))
PY
)
  p4_rx_mbps=$(python3 - <<PY
print((($p4_rx-$p4_rx_prev)*8)/($INTERVAL*1_000_000))
PY
)
  p4_tx_mbps=$(python3 - <<PY
print((($p4_tx-$p4_tx_prev)*8)/($INTERVAL*1_000_000))
PY
)

  # drop delta (lebih meaningful)
  p1_drop_delta=$((p1_drop - p1_drop_prev))
  p2_drop_delta=$((p2_drop - p2_drop_prev))
  p4_drop_delta=$((p4_drop - p4_drop_prev))

  # delay per device (mapping device_id -> port)
  delay_p1=$(get_delay_ms "dht11")
  delay_p2=$(get_delay_ms "camera")
  delay_p4=$(get_delay_ms "max")

  echo "$TS,$p1_rx_mbps,$p1_tx_mbps,$p1_drop_delta,$delay_p1,$p2_rx_mbps,$p2_tx_mbps,$p2_drop_delta,$delay_p2,$p4_rx_mbps,$p4_tx_mbps,$p4_drop_delta,$delay_p4" >> "$OUT"

  # update prev
  p1_rx_prev=$p1_rx; p1_tx_prev=$p1_tx; p1_drop_prev=$p1_drop
  p2_rx_prev=$p2_rx; p2_tx_prev=$p2_tx; p2_drop_prev=$p2_drop
  p4_rx_prev=$p4_rx; p4_tx_prev=$p4_tx; p4_drop_prev=$p4_drop

  # log progress tiap 10 detik
  ELAPSED=$((SECONDS - START))
  if (( ELAPSED % 10 == 0 )); then
    echo "[PROGRESS] elapsed=${ELAPSED}s rows=$(wc -l < $OUT)" | tee -a "$LOG"
  fi

  sleep "$INTERVAL"
done

echo "[DONE] Saved -> $OUT" | tee -a "$LOG"
