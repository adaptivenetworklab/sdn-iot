#!/bin/bash
# collect_policy_v11_throughput.sh - Utilisasi Berdasarkan Received Mbps
set -e

# --- 1. KONFIGURASI ---
BRIDGE=${1:-br0}
DURATION=${2:-3600}
INTERVAL=${3:-1}

# IP Sensor sesuai allport.py
P1_IP="192.168.15.238"; P2_IP="192.168.15.239"; P4_IP="192.168.15.240"
IF_P1="dht11"; IF_P2="camera"; IF_P4="max"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DELAY_LOG="$BASE_DIR/delay_log.csv"
OUT="$SCRIPT_DIR/dataset_dqn_rich.csv"

# --- 2. HEADER CSV ---
echo "timestamp,rx_mbps_p1,demand_mbps_p1,rx_pps_p1,util_rx_p1,drop_p1,loss_pct_p1,rx_mbps_p2,demand_mbps_p2,rx_pps_p2,util_rx_p2,drop_p2,loss_pct_p2,rx_mbps_p4,demand_mbps_p4,rx_pps_p4,util_rx_p4,drop_p4,loss_pct_p4" > "$OUT"

# --- 3. FUNGSI HELPER ---

get_clean_ovs_stats () {
    local flow_stats=$(sudo ovs-ofctl dump-flows "$1" "udp,nw_dst=$2,tp_dst=9999" 2>/dev/null | grep "n_bytes")
    echo "$(echo "$flow_stats" | grep -oP 'n_packets=\K[0-9]+' || echo 0) $(echo "$flow_stats" | grep -oP 'n_bytes=\K[0-9]+' || echo 0)"
}

get_tc_drops () {
    echo $(sudo tc -s filter show dev "$1" parent ffff: 2>/dev/null | grep -oP 'dropped \K[0-9]+' | head -n 1 || echo 0)
}

calc_throughput_metrics () {
    python3 -c "
import sys
try:
    # d = [rxp, rxp_o, rxb, rxb_o, interval, rate_limit, drops, fallback_size]
    d = list(map(float, sys.argv[1:]))
    interval, rate_limit, drops, fallback_size = d[4], d[5], d[6], d[7]
    
    rx_packets = (d[0] - d[1])
    rx_bytes = (d[2] - d[3])
    
    rx_pps = rx_packets / interval
    rx_mbps = (rx_bytes * 8.0) / (interval * 1000000.0)
    
    # Estimasi ukuran paket
    avg_size = (rx_bytes / rx_packets) if rx_packets > 0 else fallback_size
    
    # Demand tetap dihitung untuk info beban
    demand_mbps = rx_mbps + ((drops * avg_size * 8.0) / (interval * 1000000.0))
    
    # --- RUMUS BARU: UTILISASI BASED ON RECEIVED ---
    # Konversi rate_limit (kbps) ke Mbps
    cap_mbps = (rate_limit / 1000.0) if rate_limit > 0 else 1.0
    util_rx = (rx_mbps / cap_mbps) * 100.0
    
    total_sent_pps = rx_pps + (drops / interval)
    loss_pct = ((drops / interval) / total_sent_pps * 100.0) if total_sent_pps > 0 else 0
    
    print(f'{rx_mbps:.4f},{demand_mbps:.4f},{rx_pps:.2f},{util_rx:.2f},{loss_pct:.2f}')
except:
    print('0,0,0,0,0')
" "$@"
}

# --- 4. MAIN LOOP ---
read p1_rxp_o p1_rxb_o <<< $(get_clean_ovs_stats "$BRIDGE" "$P1_IP")
p1_drp_o=$(get_tc_drops "$IF_P1")
read p2_rxp_o p2_rxb_o <<< $(get_clean_ovs_stats "$BRIDGE" "$P2_IP")
p2_drp_o=$(get_tc_drops "$IF_P2")
read p4_rxp_o p4_rxb_o <<< $(get_clean_ovs_stats "$BRIDGE" "$P4_IP")
p4_drp_o=$(get_tc_drops "$IF_P4")

while true; do
    TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    
    read p1_rxp p1_rxb <<< $(get_clean_ovs_stats "$BRIDGE" "$P1_IP"); p1_drp=$(get_tc_drops "$IF_P1")
    read p2_rxp p2_rxb <<< $(get_clean_ovs_stats "$BRIDGE" "$P2_IP"); p2_drp=$(get_tc_drops "$IF_P2")
    read p4_rxp p4_rxb <<< $(get_clean_ovs_stats "$BRIDGE" "$P4_IP"); p4_drp=$(get_tc_drops "$IF_P4")

    d1=$((p1_drp-p1_drp_o)); d2=$((p2_drp-p2_drp_o)); d4=$((p4_drp-p4_drp_o))
    [ $d1 -lt 0 ] && d1=0; [ $d2 -lt 0 ] && d2=0; [ $d4 -lt 0 ] && d4=0

    # Mengambil nilai rate langsung dari OVS
    r1=$(sudo ovs-vsctl get interface "$IF_P1" ingress_policing_rate 2>/dev/null || echo 0)
    r2=$(sudo ovs-vsctl get interface "$IF_P2" ingress_policing_rate 2>/dev/null || echo 0)
    r4=$(sudo ovs-vsctl get interface "$IF_P4" ingress_policing_rate 2>/dev/null || echo 0)

    # Kalkulasi
    m1=$(calc_throughput_metrics "$p1_rxp" "$p1_rxp_o" "$p1_rxb" "$p1_rxb_o" "$INTERVAL" "$r1" "$d1" "150")
    m2=$(calc_throughput_metrics "$p2_rxp" "$p2_rxp_o" "$p2_rxb" "$p2_rxb_o" "$INTERVAL" "$r2" "$d2" "1200")
    m4=$(calc_throughput_metrics "$p4_rxp" "$p4_rxp_o" "$p4_rxb" "$p4_rxb_o" "$INTERVAL" "$r4" "$d4" "150")

    echo "$TS,$m1,$d1,$m2,$d2,$m4,$d4" >> "$OUT"

    # LOG TERMINAL
    printf "[%s] | Throughput Mode (Util = Recv/Rate)\n" "$TS"
    a1=$(echo $m1 | tr ',' ' '); printf "  P1 (DHT11)  | Recv: %-7s pps (%-6s Mbps) | Util: %-8s%% | Demand: %-6s Mbps | Drop: %-6s\n" $(echo $a1 | awk '{print $3, $1, $4, $2}') "$d1"
    a2=$(echo $m2 | tr ',' ' '); printf "  P2 (Camera) | Recv: %-7s pps (%-6s Mbps) | Util: %-8s%% | Demand: %-6s Mbps | Drop: %-6s\n" $(echo $a2 | awk '{print $3, $1, $4, $2}') "$d2"
    a4=$(echo $m4 | tr ',' ' '); printf "  P4 (Medical)| Recv: %-7s pps (%-6s Mbps) | Util: %-8s%% | Demand: %-6s Mbps | Drop: %-6s\n" $(echo $a4 | awk '{print $3, $1, $4, $2}') "$d4"
    echo "-------------------------------------------------------------------------------------------------------"

    p1_rxp_o=$p1_rxp; p1_rxb_o=$p1_rxb; p1_drp_o=$p1_drp
    p2_rxp_o=$p2_rxp; p2_rxb_o=$p2_rxb; p2_drp_o=$p2_drp
    p4_rxp_o=$p4_rxp; p4_rxb_o=$p4_rxb; p4_drp_o=$p4_drp
    sleep "$INTERVAL"
done