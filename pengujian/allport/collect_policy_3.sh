#!/bin/bash
# collect_policy_final.sh - Optimized for Real Kernel Drop Detection
set -e

# --- 1. Konfigurasi ---
BRIDGE=${1:-br0}
DURATION=${2:-3600}
INTERVAL=${3:-1}
LINK_CAP_Mbps=${4:-10000}

# Mapping Interface (Sesuaikan dengan setup SDN-IoT kamu)
IF_P1="dht11"    # Port 1
IF_P2="camera"   # Port 2
IF_P4="max"      # Port 4 (Heart Rate)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DELAY_LOG="$BASE_DIR/delay_log.csv"
OUT="$SCRIPT_DIR/dataset_dqn_rich.csv"

# --- 2. HEADER (37 KOLOM) ---
HEADER="timestamp,"
HEADER+="rx_mbps_p1,tx_mbps_p1,rx_pps_p1,tx_pps_p1,avg_rx_pkt_bytes_p1,util_rx_pct_p1,drop_p1,delay_ms_p1,last_payload_bytes_p1,priority_tag_p1,policing_rate_kbps_p1,policing_burst_kbps_p1,"
HEADER+="rx_mbps_p2,tx_mbps_p2,rx_pps_p2,tx_pps_p2,avg_rx_pkt_bytes_p2,util_rx_pct_p2,drop_p2,delay_ms_p2,last_payload_bytes_p2,priority_tag_p2,policing_rate_kbps_p2,policing_burst_kbps_p2,"
HEADER+="rx_mbps_p4,tx_mbps_p4,rx_pps_p4,tx_pps_p4,avg_rx_pkt_bytes_p4,util_rx_pct_p4,drop_p4,delay_ms_p4,last_payload_bytes_p4,priority_tag_p4,policing_rate_kbps_p4,policing_burst_kbps_p4"

echo "$HEADER" > "$OUT"

# --- 3. Fungsi Helper ---

# Fungsi untuk mengambil throughput & packets
get_ovs_stats () {
    local ifname=$1
    local stats=$(sudo ovs-vsctl get interface "$ifname" statistics 2>/dev/null | tr -d '{}"')
    local rxp=$(echo "$stats" | grep -oP 'rx_packets=\K[0-9]+' || echo 0)
    local rxb=$(echo "$stats" | grep -oP 'rx_bytes=\K[0-9]+' || echo 0)
    local txp=$(echo "$stats" | grep -oP 'tx_packets=\K[0-9]+' || echo 0)
    local txb=$(echo "$stats" | grep -oP 'tx_bytes=\K[0-9]+' || echo 0)
    echo "$rxp $rxb $txp $txb"
}

# Fungsi KRUSIAL: Mengambil real drops dari Linux Kernel TC
get_tc_drops () {
    local ifname=$1
    # Mengambil filter ingress (ffff:) dan mencari angka dropped
    local drp=$(sudo tc -s filter show dev "$ifname" parent ffff: 2>/dev/null | grep -oP 'dropped \K[0-9]+' | head -n 1 || echo 0)
    echo "${drp:-0}"
}

get_delay_and_payload () {
    local devid="$1"
    if [ ! -f "$DELAY_LOG" ]; then echo "0 0"; return; fi
    tail -n 10 "$DELAY_LOG" | grep "$devid" | tail -n 1 | awk -F',' '{print $6, $5}' | tr -d '\r' || echo "0 0"
}

get_qos_cfg () {
    local ifname=$1
    local prio=$(sudo ovs-vsctl get interface "$ifname" external_ids:priority 2>/dev/null | tr -d '"' || echo 0)
    local rate=$(sudo ovs-vsctl get interface "$ifname" ingress_policing_rate 2>/dev/null || echo 0)
    local burst=$(sudo ovs-vsctl get interface "$ifname" ingress_policing_burst 2>/dev/null || echo 0)
    echo "${prio:-0} ${rate:-0} ${burst:-0}"
}

calc_metrics () {
    python3 -c "
import sys
try:
    d = list(map(float, sys.argv[1:]))
    interval, link_cap, rate_limit = d[8], d[9], d[10]
    rx_mbps = ((d[0]-d[1])*8.0)/(interval*1000000.0)
    tx_mbps = ((d[2]-d[3])*8.0)/(interval*1000000.0)
    rx_pps = (d[4]-d[5])/interval
    tx_pps = (d[6]-d[7])/interval
    avg = (d[0]-d[1])/(d[4]-d[5]) if (d[4]-d[5])>0 else 0
    # Gunakan rate_limit sebagai basis utilitas jika ada
    cap = (rate_limit/1000.0) if rate_limit>0 else link_cap
    util = (rx_mbps/cap)*100.0 if cap>0 else 0
    print(f'{rx_mbps:.4f},{tx_mbps:.4f},{rx_pps:.2f},{tx_pps:.2f},{avg:.2f},{util:.2f}')
except: print('0,0,0,0,0,0')
" "$@"
}

# --- 4. Main Loop ---
# Initial Values
read p1_rxp_o p1_rxb_o p1_txp_o p1_txb_o <<< $(get_ovs_stats "$IF_P1"); p1_drp_o=$(get_tc_drops "$IF_P1")
read p2_rxp_o p2_rxb_o p2_txp_o p2_txb_o <<< $(get_ovs_stats "$IF_P2"); p2_drp_o=$(get_tc_drops "$IF_P2")
read p4_rxp_o p4_rxb_o p4_txp_o p4_txb_o <<< $(get_ovs_stats "$IF_P4"); p4_drp_o=$(get_tc_drops "$IF_P4")

END=$(( $(date +%s) + DURATION ))
while [ "$(date +%s)" -lt "$END" ]; do
    TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    
    # Ambil Config & Stats Baru
    read prio1 rate1 burst1 <<< $(get_qos_cfg "$IF_P1"); read p1_rxp p1_rxb p1_txp p1_txb <<< $(get_ovs_stats "$IF_P1"); p1_drp=$(get_tc_drops "$IF_P1")
    read prio2 rate2 burst2 <<< $(get_qos_cfg "$IF_P2"); read p2_rxp p2_rxb p2_txp p2_txb <<< $(get_ovs_stats "$IF_P2"); p2_drp=$(get_tc_drops "$IF_P2")
    read prio4 rate4 burst4 <<< $(get_qos_cfg "$IF_P4"); read p4_rxp p4_rxb p4_txp p4_txb <<< $(get_ovs_stats "$IF_P4"); p4_drp=$(get_tc_drops "$IF_P4")

    # Hitung Metrik
    m1=$(calc_metrics "$p1_rxb" "$p1_rxb_o" "$p1_txb" "$p1_txb_o" "$p1_rxp" "$p1_rxp_o" "$p1_txp" "$p1_txp_o" "$INTERVAL" "$LINK_CAP_Mbps" "$rate1")
    m2=$(calc_metrics "$p2_rxb" "$p2_rxb_o" "$p2_txb" "$p2_txb_o" "$p2_rxp" "$p2_rxp_o" "$p2_txp" "$p2_txp_o" "$INTERVAL" "$LINK_CAP_Mbps" "$rate2")
    m4=$(calc_metrics "$p4_rxb" "$p4_rxb_o" "$p4_txb" "$p4_txb_o" "$p4_rxp" "$p4_rxp_o" "$p4_txp" "$p4_txp_o" "$INTERVAL" "$LINK_CAP_Mbps" "$rate4")

    # Delay & Delta Drop
    read d1 b1 <<< $(get_delay_and_payload "dht11"); drop1=$((p1_drp - p1_drp_o))
    read d2 b2 <<< $(get_delay_and_payload "camera"); drop2=$((p2_drp - p2_drp_o))
    read d4 b4 <<< $(get_delay_and_payload "max"); drop4=$((p4_drp - p4_drp_o))

    # Log Baris Final
    echo "$TS,$m1,$drop1,${d1:-0},${b1:-0},$prio1,$rate1,$burst1,$m2,$drop2,${d2:-0},${b2:-0},$prio2,$rate2,$burst2,$m4,$drop4,${d4:-0},${b4:-0},$prio4,$rate4,$burst4" >> "$OUT"

    # Update state lama
    p1_rxp_o=$p1_rxp; p1_rxb_o=$p1_rxb; p1_txp_o=$p1_txp; p1_txb_o=$p1_txb; p1_drp_o=$p1_drp
    p2_rxp_o=$p2_rxp; p2_rxb_o=$p2_rxb; p2_txp_o=$p2_txp; p2_txb_o=$p2_txb; p2_drp_o=$p2_drp
    p4_rxp_o=$p4_rxp; p4_rxb_o=$p4_rxb; p4_txp_o=$p4_txp; p4_txb_o=$p4_txb; p4_drp_o=$p4_drp

    echo "[PROGRESS] $TS | Real Drops: P1=$drop1 P2=$drop2 P4=$drop4 | Util P1: $(echo $m1 | cut -d',' -f6)%"
    sleep "$INTERVAL"
done