#!/bin/bash
# collect_final_v13.sh - Interval 10 Detik dengan Total Packet Stats
set -e

# --- 1. KONFIGURASI ---
BRIDGE="br0"
INTERVAL=10
OUT_CSV="dataset_dqn_final.csv"
DELAY_LOG="/home/ovs/sdn-iot/pengujian/delay_log.csv"

# Definisi Interface & IP (P1=dht11, P2=camera, P4=max)
IF_NAMES=("dht11" "camera" "max")
IF_IPS=("192.168.15.238" "192.168.15.239" "192.168.15.240")
IF_KEYS=("p1" "p2" "p4")

# --- 2. HEADER CSV ---
HEADER="timestamp"
for p in "${IF_KEYS[@]}"; do
    HEADER+=",rx_mbps_$p,tx_mbps_$p,rx_pps_$p,tx_pps_$p,avg_rx_pkt_bytes_$p,util_rx_pct_$p,drop_$p,delay_ms_$p,last_payload_bytes_$p,priority_tag_$p,policing_rate_kbps_$p,policing_burst_kbps_$p"
done
echo "$HEADER" > "$OUT_CSV"

# --- 3. FUNGSI HELPER ---
get_rx_stats() {
    local stats=$(sudo ovs-ofctl dump-flows "$1" "udp,nw_dst=$2,tp_dst=9999" 2>/dev/null | grep "n_bytes")
    local p=$(echo "$stats" | grep -oP 'n_packets=\K[0-9]+' || echo 0)
    local b=$(echo "$stats" | grep -oP 'n_bytes=\K[0-9]+' || echo 0)
    echo "$p $b"
}

get_tx_stats() {
    local stats=$(sudo ovs-vsctl get interface "$1" statistics 2>/dev/null)
    local p=$(echo "$stats" | grep -oP 'tx_packets=\K[0-9]+' || echo 0)
    local b=$(echo "$stats" | grep -oP 'tx_bytes=\K[0-9]+' || echo 0)
    echo "$p $b"
}

get_drops() {
    echo $(sudo tc -s filter show dev "$1" parent ffff: 2>/dev/null | grep -oP 'dropped \K[0-9]+' | head -n 1 || echo 0)
}

# --- 4. INISIALISASI ---
declare -A PREV_RX_P PREV_RX_B PREV_TX_P PREV_TX_B PREV_DRP
for name in "${IF_NAMES[@]}"; do
    idx=$(echo ${IF_NAMES[@]/$name//} | cut -d/ -f1 | wc -w | xargs)
    ip=${IF_IPS[$idx]}
    read PREV_RX_P[$name] PREV_RX_B[$name] <<< $(get_rx_stats "$BRIDGE" "$ip")
    read PREV_TX_P[$name] PREV_TX_B[$name] <<< $(get_tx_stats "$name")
    PREV_DRP[$name]=$(get_drops "$name")
done

echo "------------------------------------------------------------------------------------------------"
echo " Monitoring Started | Interval: $INTERVAL detik | Output: $OUT_CSV"
echo "------------------------------------------------------------------------------------------------"

# --- 5. LOOP UTAMA ---
while true; do
    # Tunggu di awal atau akhir loop
    sleep "$INTERVAL"
    
    TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    ROW="$TS"
    
    echo ""
    echo "[$TS] - Window 10 Seconds"
    printf "%-12s | %-10s | %-12s | %-12s | %-8s\n" "Interface" "Util (%)" "Recv(Total)" "Drop(Total)" "Rate(Mbps)"
    echo "-------------|------------|--------------|--------------|----------"

    for i in "${!IF_NAMES[@]}"; do
        NAME=${IF_NAMES[$i]}
        IP=${IF_IPS[$i]}
        
        # Ambil data terbaru
        read CUR_RX_P CUR_RX_B <<< $(get_rx_stats "$BRIDGE" "$IP")
        read CUR_TX_P CUR_TX_B <<< $(get_tx_stats "$NAME")
        CUR_DRP=$(get_drops "$NAME")
        
        POL_RATE=$(sudo ovs-vsctl get interface "$NAME" ingress_policing_rate || echo 0)
        PRIO=$(sudo ovs-vsctl get interface "$NAME" external_ids:priority | tr -d '"' || echo 0)
        POL_BURST=$(sudo ovs-vsctl get interface "$NAME" ingress_policing_burst || echo 0)

        # Kalkulasi via Python (menghitung delta dan rate)
        RES=$(python3 -c "
import sys
try:
    d = list(map(float, sys.argv[1:]))
    interval, rate_kbps = d[10], d[11]
    
    # Delta (Total paket dalam 10 detik)
    rx_pkts_total = d[0] - d[1]
    rx_bytes_total = d[2] - d[3]
    tx_pkts_total = d[4] - d[5]
    tx_bytes_total = d[6] - d[7]
    drops_total = max(0, d[8] - d[9])
    
    # Rate (Per detik)
    rx_pps = rx_pkts_total / interval
    rx_mbps = (rx_bytes_total * 8) / (interval * 1000000.0)
    tx_pps = tx_pkts_total / interval
    tx_mbps = (tx_bytes_total * 8) / (interval * 1000000.0)
    
    avg_rx = rx_bytes_total / rx_pkts_total if rx_pkts_total > 0 else 0
    rate_mbps = rate_kbps / 1000.0
    util = (rx_mbps / rate_mbps * 100.0) if rate_mbps > 0 else 0
    
    # Output order: rx_mbps, tx_mbps, rx_pps, tx_pps, avg_rx, util, drops_total, rx_pkts_total
    print(f'{rx_mbps:.4f},{tx_mbps:.4f},{rx_pps:.2f},{tx_pps:.2f},{avg_rx:.2f},{util:.2f},{int(drops_total)},{int(rx_pkts_total)}')
except Exception as e:
    print('0,0,0,0,0,0,0,0')
" "$CUR_RX_P" "${PREV_RX_P[$NAME]}" "$CUR_RX_B" "${PREV_RX_B[$NAME]}" \
  "$CUR_TX_P" "${PREV_TX_P[$NAME]}" "$CUR_TX_B" "${PREV_TX_B[$NAME]}" \
  "$CUR_DRP" "${PREV_DRP[$NAME]}" "$INTERVAL" "$POL_RATE")

        # Parsing hasil Python untuk terminal
        UTIL=$(echo $RES | cut -d',' -f6)
        TOTAL_DROP=$(echo $RES | cut -d',' -f7)
        TOTAL_RECV=$(echo $RES | cut -d',' -f8)
        RATE_MBPS=$(echo $RES | cut -d',' -f1)

        # Print ke Terminal
        printf "%-12s | %-10s | %-12s | %-12s | %-8s\n" "$NAME" "$UTIL" "$TOTAL_RECV" "$TOTAL_DROP" "$RATE_MBPS"

        # Simpan ke CSV (hanya kolom yang didefinisikan di header awal)
        # Note: Kita ambil 7 nilai pertama dari RES (sampai drop) + delay log data
        CSV_VALS=$(echo $RES | cut -d',' -f1-7)
        
        DELAY_DATA=$(tail -n 20 "$DELAY_LOG" 2>/dev/null | grep "$NAME" | tail -n 1 || echo "0,0,0,0,0,0")
        LAST_DELAY=$(echo "$DELAY_DATA" | awk -F',' '{print $6}' || echo 0)
        LAST_PAYLOAD=$(echo "$DELAY_DATA" | awk -F',' '{print $5}' || echo 0)

        ROW+=",$CSV_VALS,$LAST_DELAY,$LAST_PAYLOAD,$PRIO,$POL_RATE,$POL_BURST"

        # Update History
        PREV_RX_P[$NAME]=$CUR_RX_P; PREV_RX_B[$NAME]=$CUR_RX_B
        PREV_TX_P[$NAME]=$CUR_TX_P; PREV_TX_B[$NAME]=$CUR_TX_B
        PREV_DRP[$NAME]=$CUR_DRP
    done

    echo "$ROW" >> "$OUT_CSV"
done