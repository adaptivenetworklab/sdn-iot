#!/bin/bash

BRIDGE=${1:-br0}
PORT=${2:-2}
DURATION=${3:-3600}     # default 1 jam
INTERVAL=${4:-1}        # polling tiap 1 detik

CSV="ovs_port_${PORT}.csv"
PNG="ovs_port_${PORT}_throughput.png"

echo "timestamp,port,rx_bytes,tx_bytes" > "$CSV"

echo "[INFO] Logging OVS port stats..."
echo " Bridge  : $BRIDGE"
echo " Port    : $PORT"
echo " Duration: $DURATION seconds"
echo " Interval: $INTERVAL seconds"
echo " Output  : $CSV"
echo

END=$((SECONDS + DURATION))

while [ $SECONDS -lt $END ]; do
    TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    LINE=$(sudo ovs-ofctl dump-ports "$BRIDGE" 2>/dev/null | grep -E "port ${PORT}:" -A 1 | tail -n 1)

    RX=$(echo "$LINE" | sed -n 's/.*rx bytes=\([0-9]*\).*/\1/p')
    TX=$(echo "$LINE" | sed -n 's/.*tx bytes=\([0-9]*\).*/\1/p')

    if [[ -z "$RX" || -z "$TX" ]]; then
        RX=0
        TX=0
    fi

    echo "$TS,$PORT,$RX,$TX" >> "$CSV"
    sleep "$INTERVAL"
done

echo
echo "[INFO] Done logging. Now plotting..."

python3 plot_ovs_csv.py "$CSV" "$INTERVAL" "$PNG"

echo "[DONE] Graph saved to $PNG"
