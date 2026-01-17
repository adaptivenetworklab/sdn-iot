#!/bin/bash

BRIDGE=${1:-br0}
DURATION=${2:-3600}   # default 1 jam
INTERVAL=${3:-1}      # default 1 detik

P1=1
P2=2
P4=4

OUT="dataset_dqn.csv"
LOG="dataset_dqn.log"
DELAY_LOG="/home/ovs/pengujian/delay_log.csv"

echo "[START] $(date -u +"%Y-%m-%dT%H:%M:%SZ") bridge=$BRIDGE duration=$DURATION interval=$INTERVAL" > "$LOG"

# CSV header
echo "timestamp,rx_mbps_p1,tx_mbps_p1,drop_p1,delay_ms_p1,rx_mbps_p2,tx_mbps_p2,drop_p2,delay_ms_p2,rx_mbps_p4,tx_mbps_p4,drop_p4,delay_ms_p4" > "$OUT"

# =========================
# Helpers
# =========================
clean_num() {
  # ambil angka valid aja (support negative & decimal)
  # kalau kosong / invalid -> 0
  local v="$1"
  if [[ "$v" =~ ^-?[0-9]+([.][0-9]+)?$ ]]; then
    echo "$v"
  else
    echo "0"
  fi
}

clean_float() {
  # hilangkan newline/spasi
  echo "$1" | tr -d '\r\n ' 
}

get_port_stats() {
  local bridge=$1
  local port=$2

  # ambil blok "port X:" sampai baris "tx ..."
  local block
  block=$(sudo ovs-ofctl dump-ports "$bridge" 2>/dev/null | awk -v p="$port" '
    $1=="port" && ($2==p":" || $2==p || $2 ~ p":") {flag=1; print; next}
    flag==1 {print; if ($1=="tx") {flag=0}}
  ')

  local rx_bytes tx_bytes rx_drop
  rx_bytes=$(echo "$block" | sed -n 's/.*rx pkts=.*bytes=\([0-9]\+\).*/\1/p' | head -n 1)
  tx_bytes=$(echo "$block" | sed -n 's/.*tx pkts=.*bytes=\([0-9]\+\).*/\1/p' | head -n 1)
  rx_drop=$(echo "$block" | sed -n 's/.*rx pkts=.*drop=\([0-9]\+\).*/\1/p' | head -n 1)

  rx_bytes=${rx_bytes:-0}
  tx_bytes=${tx_bytes:-0}
  rx_drop=${rx_drop:-0}

  echo "$rx_bytes $tx_bytes $rx_drop"
}

# ambil delay terakhir per device_id (field4 harus angka)
get_delay_ms() {
  local devid="$1"

  if [ ! -f "$DELAY_LOG" ]; then
    echo "0"
    return
  fi

  # format delay_log.csv: timestamp,device_id,src_ip,delay_ms
  local last
  last=$(tail -n 500 "$DELAY_LOG" 2>/dev/null | awk -F',' -v d="$devid" '
    $2==d && $4 ~ /^-?[0-9]+(\.[0-9]+)?$/ {last=$4}
    END{print last}
  ')

  last=$(clean_num "$last")
  echo "$last"
}

calc_mbps() {
  local cur=$1
  local prev=$2
  local interval=$3

  python3 - <<PY
cur=float("$cur")
prev=float("$prev")
interval=float("$interval")
mbps=((cur-prev)*8.0)/(interval*1000000.0)
print(mbps)
PY
}

# =========================
# Init prev
# =========================
read p1_rx_prev p1_tx_prev p1_drop_prev <<< "$(get_port_stats "$BRIDGE" "$P1")"
read p2_rx_prev p2_tx_prev p2_drop_prev <<< "$(get_port_stats "$BRIDGE" "$P2")"
read p4_rx_prev p4_tx_prev p4_drop_prev <<< "$(get_port_stats "$BRIDGE" "$P4")"

START=$SECONDS
END=$((SECONDS + DURATION))

# =========================
# Loop
# =========================
while [ $SECONDS -lt $END ]; do
  TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

  read p1_rx p1_tx p1_drop <<< "$(get_port_stats "$BRIDGE" "$P1")"
  read p2_rx p2_tx p2_drop <<< "$(get_port_stats "$BRIDGE" "$P2")"
  read p4_rx p4_tx p4_drop <<< "$(get_port_stats "$BRIDGE" "$P4")"

  # Throughput Mbps
  p1_rx_mbps=$(calc_mbps "$p1_rx" "$p1_rx_prev" "$INTERVAL")
  p1_tx_mbps=$(calc_mbps "$p1_tx" "$p1_tx_prev" "$INTERVAL")

  p2_rx_mbps=$(calc_mbps "$p2_rx" "$p2_rx_prev" "$INTERVAL")
  p2_tx_mbps=$(calc_mbps "$p2_tx" "$p2_tx_prev" "$INTERVAL")

  p4_rx_mbps=$(calc_mbps "$p4_rx" "$p4_rx_prev" "$INTERVAL")
  p4_tx_mbps=$(calc_mbps "$p4_tx" "$p4_tx_prev" "$INTERVAL")

  # Clean float output dari python
  p1_rx_mbps=$(clean_float "$p1_rx_mbps")
  p1_tx_mbps=$(clean_float "$p1_tx_mbps")
  p2_rx_mbps=$(clean_float "$p2_rx_mbps")
  p2_tx_mbps=$(clean_float "$p2_tx_mbps")
  p4_rx_mbps=$(clean_float "$p4_rx_mbps")
  p4_tx_mbps=$(clean_float "$p4_tx_mbps")

  # Drop delta
  p1_drop_delta=$((p1_drop - p1_drop_prev))
  p2_drop_delta=$((p2_drop - p2_drop_prev))
  p4_drop_delta=$((p4_drop - p4_drop_prev))

  # Delay per device_id
  delay_p1=$(get_delay_ms "dht11")
  delay_p2=$(get_delay_ms "camera")
  delay_p4=$(get_delay_ms "max")

  # Final safety
  delay_p1=$(clean_num "$delay_p1")
  delay_p2=$(clean_num "$delay_p2")
  delay_p4=$(clean_num "$delay_p4")

  # ✅ write 1 row = 1 state (PASTI 13 kolom)
  printf "%s,%.6f,%.6f,%d,%.3f,%.6f,%.6f,%d,%.3f,%.6f,%.6f,%d,%.3f\n" \
    "$TS" \
    "$p1_rx_mbps" "$p1_tx_mbps" "$p1_drop_delta" "$delay_p1" \
    "$p2_rx_mbps" "$p2_tx_mbps" "$p2_drop_delta" "$delay_p2" \
    "$p4_rx_mbps" "$p4_tx_mbps" "$p4_drop_delta" "$delay_p4" \
    >> "$OUT"

  # update prev
  p1_rx_prev=$p1_rx; p1_tx_prev=$p1_tx; p1_drop_prev=$p1_drop
  p2_rx_prev=$p2_rx; p2_tx_prev=$p2_tx; p2_drop_prev=$p2_drop
  p4_rx_prev=$p4_rx; p4_tx_prev=$p4_tx; p4_drop_prev=$p4_drop

  # progress log setiap 10 detik
  ELAPSED=$((SECONDS - START))
  if (( ELAPSED % 10 == 0 )); then
    echo "[PROGRESS] elapsed=${ELAPSED}s rows=$(wc -l < $OUT)" | tee -a "$LOG"
  fi

  sleep "$INTERVAL"
done

echo "[DONE] Saved -> $OUT" | tee -a "$LOG"
