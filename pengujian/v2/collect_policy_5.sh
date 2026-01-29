#!/bin/bash
# collect_policy_v9_demand.sh - Monitor SDN-IoT dengan Demand Utilization > 100%
set -e

# --- 1. KONFIGURASI ---
BRIDGE=${1:-br0}
DURATION=${2:-3600}
INTERVAL=${3:-1}
LINK_CAP_Mbps=${4:-10000}

# IP Tujuan sesuai script pengirim allport.py
P1_IP="192.168.15.238"; P2_IP="192.168.15.239"; P4_IP="192.168.15.240"
IF_P1="dht11"; IF_P2="camera"; IF_P4="max"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DELAY_LOG="$BASE_DIR/delay_log.csv"
OUT="$SCRIPT_DIR/dataset_dqn_rich.csv"

# --- 2. HEADER CSV ---
echo "timestamp,rx_mbps_p1,demand_mbps_p1,rx_pps_p1,tx_pps_p1,avg_pkt_p1,util_demand_p1,drop_p1,loss_pct_p1,delay_ms_p1,payload_p1,prio_p1,rate_p1,burst_p1,rx_mbps_p2,demand_mbps_p2,rx_pps_p2,tx_pps_p2,avg_pkt_p2,util_demand_p2,drop_p2,loss_pct_p2,delay_ms_p2,payload_p2,prio_p2,rate_p2,burst_p2,rx_mbps_p4,demand_mbps_p4,rx_pps_p4,tx_pps_p4,avg_pkt_p4,util_demand_p4,drop_p4,loss_pct_p4,delay_ms_p4,payload_p4,prio_p4,rate_p4,burst_p4" > "$OUT"

# --- 3. FUNGSI HELPER ---

# Mengambil statistik dari OpenFlow berdasarkan IP Tujuan
get_clean_ovs_stats () {
    local flow_stats=$(sudo ovs-ofctl dump-flows "$1" "udp,nw_dst=$2,tp_dst=9999" 2>/dev/null | grep "n_bytes")
    echo "$(echo "$flow_stats" | grep -oP 'n_packets=\K[0-9]+' || echo 0) $(echo "$flow_stats" | grep -oP 'n_bytes=\K[0-9]+' || echo 0) 0 0"
}

get_tc_drops () {
    local drp=$(sudo tc -s filter show dev "$1" parent ffff: 2>/dev/null | grep -oP 'dropped \K[0-9]+' | head -n 1 || echo 0)
    echo "${drp:-0}"
}

# Perhitungan Utilisasi Demand (Beban vs Limit)
calc_demand_metrics () {
    python3 -c "
import sys
try:
    # d = [rxb, rxb_o, txb, txb_o, rxp, rxp_o, txp, txp_o, interval, link_cap, rate_limit, drops, fallback_size]
    d = list(map(float, sys.argv[1:]))
    interval, rate_limit, drops, fallback_size = d[8], d[10], d[11], d[12]
    
    rx_bytes = (d[0] - d[1])
    rx_pps = (d[4] - d[5]) / interval
    rx_mbps = (rx_bytes * 8.0) / (interval * 1000000.0)
    
    # Estimasi ukuran paket (penting untuk menghitung beban drop)
    avg_size = (rx_bytes / (d[4] - d[5])) if (d[4] - d[5]) > 0 else fallback_size
    
    # Hitung Demand = Data Berhasil + (Data yang Di-drop)
    demand_mbps = rx_mbps + ((drops * avg_size * 8.0) / (interval * 1000000.0))
    
    # Hitung UTILISASI terhadap RATE LIMIT (bukan terhadap link capacity)
    # Konversi rate_limit dari kbps ke Mbps
    cap = (rate_limit / 1000.0) if rate_limit > 0 else 1.0
    util_demand = (demand_mbps / cap) * 100.0
    
    total_pkts = rx_pps + (drops / interval)
    loss_pct = ((drops / interval) / total_pkts * 100.0) if total_pkts > 0 else 0
    
    print(f'{rx_mbps:.4f},{demand_mbps:.4f},{rx_pps:.2f},0,{avg_size:.2f},{util_demand:.2f},{loss_pct:.2f}')
except:
    print('0,0,0,0,0,0,0')
" "$@"
}

# --- 4. MAIN LOOP ---
# Inisialisasi statistik lama agar delta akurat
read p1_rxp_o p1_rxb_o _ _ <<< $(get_clean_ovs_stats "$BRIDGE" "$P1_IP"); p1_drp_o=$(get_tc_drops "$IF_P1")
read p2_rxp_o p2_rxb_o _ _ <<< $(get_clean_ovs_stats "$BRIDGE" "$P2_IP"); p2_drp_o=$(get_tc_drops "$IF_P2")
read p4_rxp_o p4_rxb_o _ _ <<< $(get_clean_ovs_stats "$BRIDGE" "$P4_IP"); p4_drp_o=$(get_tc_drops "$IF_P4")

END=$(( $(date +%s) + DURATION ))
while [ "$(date +%s)" -lt "$END" ]; do
    TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    
    # Ambil statistik terbaru
    read p1_rxp p1_rxb _ _ <<< $(get_clean_ovs_stats "$BRIDGE" "$P1_IP"); p1_drp=$(get_tc_drops "$IF_P1")
    read p2_rxp p2_rxb _ _ <<< $(get_clean_ovs_stats "$BRIDGE" "$P2_IP"); p2_drp=$(get_tc_drops "$IF_P2")
    read p4_rxp p4_rxb _ _ <<< $(get_clean_ovs_stats "$BRIDGE" "$P4_IP"); p4_drp=$(get_tc_drops "$IF_P4")

    # Hitung jumlah drop dalam interval ini
    d1=$((p1_drp-p1_drp_o)); d2=$((p2_drp-p2_drp_o)); d4=$((p4_drp-p4_drp_o))
    [ $d1 -lt 0 ] && d1=0; [ $d2 -lt 0 ] && d2=0; [ $d4 -lt 0 ] && d4=0

    # Ambil Config QoS saat ini
    read prio1 r1 b1 <<< $(sudo ovs-vsctl get interface "$IF_P1" external_ids:priority ingress_policing_rate ingress_policing_burst 2>/dev/null | tr -d '"\n')
    read prio2 r2 b2 <<< $(sudo ovs-vsctl get interface "$IF_P2" external_ids:priority ingress_policing_rate ingress_policing_burst 2>/dev/null | tr -d '"\n')
    read prio4 r4 b4 <<< $(sudo ovs-vsctl get interface "$IF_P4" external_ids:priority ingress_policing_rate ingress_policing_burst 2>/dev/null | tr -d '"\n')

    # Estimasi ukuran paket dari log delay
    read dy1 pl1 <<< $(tail -n 5 "$DELAY_LOG" 2>/dev/null | grep "dht11" | tail -n 1 | awk -F',' '{print $6, $5}' || echo "0 150")
    read dy2 pl2 <<< $(tail -n 5 "$DELAY_LOG" 2>/dev/null | grep "camera" | tail -n 1 | awk -F',' '{print $6, $5}' || echo "0 1200")
    read dy4 pl4 <<< $(tail -n 5 "$DELAY_LOG" 2>/dev/null | grep "max" | tail -n 1 | awk -F',' '{print $6, $5}' || echo "0 150")

    # Kalkulasi Metrik Demand & Util
    m1=$(calc_demand_metrics "$p1_rxb" "$p1_rxb_o" 0 0 "$p1_rxp" "$p1_rxp_o" 0 0 "$INTERVAL" "$LINK_CAP_Mbps" "${r1:-0}" "$d1" "${pl1:-150}")
    m2=$(calc_demand_metrics "$p2_rxb" "$p2_rxb_o" 0 0 "$p2_rxp" "$p2_rxp_o" 0 0 "$INTERVAL" "$LINK_CAP_Mbps" "${r2:-0}" "$d2" "${pl2:-1200}")
    m4=$(calc_demand_metrics "$p4_rxb" "$p4_rxb_o" 0 0 "$p4_rxp" "$p4_rxp_o" 0 0 "$INTERVAL" "$LINK_CAP_Mbps" "${r4:-0}" "$d4" "${pl4:-150}")

    # Output terminal
    u1=$(echo $m1 | cut -d',' -f6); dem1=$(echo $m1 | cut -d',' -f2); l1=$(echo $m1 | cut -d',' -f7)
    u2=$(echo $m2 | cut -d',' -f6); dem2=$(echo $m2 | cut -d',' -f2); l2=$(echo $m2 | cut -d',' -f7)
    u4=$(echo $m4 | cut -d',' -f6); dem4=$(echo $m4 | cut -d',' -f2); l4=$(echo $m4 | cut -d',' -f7)

    # Simpan ke CSV
    echo "$TS,$m1,$d1,${dy1:-0},${pl1:-0},${prio1:-0},$r1,$b1,$m2,$d2,${dy2:-0},${pl2:-0},${prio2:-0},$r2,$b2,$m4,$d4,${dy4:-0},${pl4:-0},${prio4:-0},$r4,$b4" >> "$OUT"

    printf "[%s] | Traffic Demand Mode (Target Limit: %s kbps)\n" "$TS" "$r4"
    printf "  P1 (DHT11)  | Util: %-8s%% | Demand: %-6s Mbps | Drop: %-5s | Loss: %-5s%%\n" "$u1" "$dem1" "$d1" "$l1"
    printf "  P2 (Camera) | Util: %-8s%% | Demand: %-6s Mbps | Drop: %-5s | Loss: %-5s%%\n" "$u2" "$dem2" "$d2" "$l2"
    printf "  P4 (Medical)| Util: %-8s%% | Demand: %-6s Mbps | Drop: %-5s | Loss: %-5s%%\n" "$u4" "$dem4" "$d4" "$l4"
    echo "---------------------------------------------------------------------------------------"

    # Update statistik lama
    p1_rxp_o=$p1_rxp; p1_rxb_o=$p1_rxb; p1_drp_o=$p1_drp
    p2_rxp_o=$p2_rxp; p2_rxb_o=$p2_rxb; p2_drp_o=$p2_drp
    p4_rxp_o=$p4_rxp; p4_rxb_o=$p4_rxb; p4_drp_o=$p4_drp
    sleep "$INTERVAL"
done