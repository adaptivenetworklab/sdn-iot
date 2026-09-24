#!/bin/bash

BRIDGE=${1:-br0}
PORT=${2:-2}
DURATION=${3:-3600}
INTERVAL=${4:-1}

CSV="ovs_port_${PORT}.csv"
LOG="ovs_port_${PORT}.log"
PNG="ovs_port_${PORT}_throughput.png"

echo "timestamp,port,rx_bytes,tx_bytes" > "$CSV"
echo "[START] $(date -u +"%Y-%m-%dT%H:%M:%SZ") bridge=$BRIDGE port=$PORT" > "$LOG"

echo "[INFO] Logging OVS port stats..."
echo " Bridge  : $BRIDGE"
echo " Port    : $PORT"
echo " Duration: $DURATION seconds"
echo " Interval: $INTERVAL seconds"
echo " Output  : $CSV"
echo " Log     : $LOG"
echo

START=$SECONDS
END=$((SECONDS + DURATION))

while [ $SECONDS -lt $END ]; do
    TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    # Ambil 2 baris: rx line + tx line
    BLOCK=$(sudo ovs-ofctl dump-ports "$BRIDGE" 2>/dev/null | awk -v p="$PORT" '
        $1=="port" && ($2==p":" || $2==p || $2 ~ p":") {flag=1; print; next}
        flag==1 {print; if ($1=="tx") {flag=0}}
    ')

    # Parse rx/tx bytes
    RX=$(echo "$BLOCK" | sed -n 's/.*rx pkts=.*bytes=\([0-9]\+\).*/\1/p' | head -n 1)
    TX=$(echo "$BLOCK" | sed -n 's/.*tx pkts=.*bytes=\([0-9]\+\).*/\1/p' | head -n 1)

    if [[ -z "$RX" || -z "$TX" ]]; then
        echo "[WARN] $TS Failed to parse port=$PORT" | tee -a "$LOG"
        RX=0
        TX=0
    else
        echo "[OK] $TS rx=$RX tx=$TX" >> "$LOG"
    fi

    echo "$TS,$PORT,$RX,$TX" >> "$CSV"
    sleep "$INTERVAL"
done

echo "[INFO] Logging done. Plotting..." | tee -a "$LOG"

python3 plot.py "$CSV" "$INTERVAL" "$PNG" | tee -a "$LOG"

echo "[DONE] Graph saved: $PNG" | tee -a "$LOG"
