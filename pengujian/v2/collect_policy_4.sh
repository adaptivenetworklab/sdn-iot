#!/bin/bash
# collect_policy_final_v5.sh - Monitor SDN-IoT dengan Autotune Burst & Real-time Log
set -e

# --- 1. KONFIGURASI ---
BRIDGE=${1:-br0}
DURATION=${2:-3600}
INTERVAL=${3:-1}
LINK_CAP_Mbps=${4:-10000}

# Nama Interface sesuai riset
IF_P1="dht11"; IF_P2="camera"; IF_P4="max"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DELAY_LOG="$BASE_DIR/delay_log.csv"
OUT="$SCRIPT_DIR/dataset_dqn_rich.csv"

# --- 2. HEADER CSV (37 KOLOM) ---
# Menambah kolom loss_pct di setiap port
HEADER="timestamp,"
HEADER+="rx_mbps_p1,tx_mbps_p1,rx_pps_p1,tx_pps_p1,avg_rx_pkt_bytes_p1,util_rx_pct_p1,drop_p1,loss_pct_p1,delay_ms_p1,last_payload_bytes_p1,priority_tag_p1,policing_rate_kbps_p1,policing_burst_kbps_p1,"
HEADER+="rx_mbps_p2,tx_mbps_p2,rx_pps_p2,tx_pps_p2,avg_rx_pkt_bytes_p2,util_rx_pct_p2,drop_p2,loss_pct_p2,delay_ms_p2,last_payload_bytes_p2,priority_tag_p2,policing_rate_kbps_p2,policing_burst_kbps_p2,"
HEADER+="rx_mbps_p4,tx_mbps_p4,rx_pps_p4,tx_pps_p4,avg_rx_pkt_bytes_p4,util_rx_pct_p4,drop_p4,loss_pct_p4,delay_ms_p4,last_payload_bytes_p4,priority_tag_p4,policing_rate_kbps_p4,policing_burst_kbps_p4"
echo "$HEADER" > "$OUT"

# --- 3. FUNGSI HELPER ---

# Autotune Burst: Mengkalibrasi "ember" agar pas dengan karakteristik IoT
apply_autotune_burst() {
    local ifname=$1
    local rate=$(sudo ovs-vsctl get interface "$ifname" ingress_policing_rate 2>/dev/null || echo 0)
    if [ "$rate" -gt 0 ]; then
        local burst=$(( (rate / 10) + 12 ))
        sudo ovs-vsctl set interface "$ifname" ingress_policing_burst="$burst"
    fi
}

get_ovs_stats () {
    local ifname=$1
    local stats=$(sudo ovs-vsctl get interface "$ifname" statistics 2>/dev/null | tr -d '{}"')
    echo "$(echo "$stats" | grep -oP 'rx_packets=\K[0-9]+' || echo 0) $(echo "$stats" | grep -oP 'rx_bytes=\K[0-9]+' || echo 0) $(echo "$stats" | grep -oP 'tx_packets=\K[0-9]+' || echo 0) $(echo "$stats" | grep -oP 'tx_bytes=\K[0-9]+' || echo 0)"
}

get_tc_drops () {
    local drp=$(sudo tc -s filter show dev "$1" parent ffff: 2>/dev/null | grep -oP 'dropped \K[0-9]+' | head -n 1 || echo 0)
    echo "${drp:-0}"
}

get_delay_payload () {
    tail -n 10 "$DELAY_LOG" 2>/dev/null | grep "$1" | tail -n 1 | awk -F',' '{print $6, $5}' || echo "0 0"
}

get_qos_cfg () {
    local ifname=$1
    echo "$(sudo ovs-vsctl get interface "$ifname" external_ids:priority 2>/dev/null | tr -d '"' || echo 0) $(sudo ovs-vsctl get interface "$ifname" ingress_policing_rate 2>/dev/null || echo 0) $(sudo ovs-vsctl get interface "$ifname" ingress_policing_burst 2>/dev/null || echo 0)"
}

calc_metrics_with_loss () {
    python3 -c "
import sys
try:
    d = list(map(float, sys.argv[1:]))
    interval, link_cap, rate_limit, drops = d[8], d[9], d[10], d[11]
    rx_mbps = ((d[0]-d[1])*8.0)/(interval*1000000.0)
    tx_mbps = ((d[2]-d[3])*8.0)/(interval*1000000.0)
    rx_pps = (d[4]-d[5])/interval
    tx_pps = (d[6]-d[7])/interval
    avg = (d[0]-d[1])/(d[4]-d[5]) if (d[4]-d[5])>0 else 0
    cap = (rate_limit/1000.0) if rate_limit>0 else link_cap
    util = (rx_mbps/cap)*100.0 if cap>0 else 0
    # Kalkulasi Loss Rate %
    total_pkts = rx_pps + (drops/interval)
    loss_pct = ( (drops/interval) / total_pkts * 100.0 ) if total_pkts > 0 else 0
    print(f'{rx_mbps:.4f},{tx_mbps:.4f},{rx_pps:.2f},{tx_pps:.2f},{avg:.2f},{util:.2f},{loss_pct:.2f}')
except: print('0,0,0,0,0,0,0')
" "$@"
}

# --- 4. MAIN LOOP ---
read p1_rxp_o p1_rxb_o p1_txp_o p1_txb_o <<< $(get_ovs_stats "$IF_P1"); p1_drp_o=$(get_tc_drops "$IF_P1")
read p2_rxp_o p2_rxb_o p2_txp_o p2_txb_o <<< $(get_ovs_stats "$IF_P2"); p2_drp_o=$(get_tc_drops "$IF_P2")
read p4_rxp_o p4_rxb_o p4_txp_o p4_txb_o <<< $(get_ovs_stats "$IF_P4"); p4_drp_o=$(get_tc_drops "$IF_P4")

echo "Starting monitoring for $DURATION seconds..."

END=$(( $(date +%s) + DURATION ))
while [ "$(date +%s)" -lt "$END" ]; do
    TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    
    # Update Autotune
    apply_autotune_burst "$IF_P1"; apply_autotune_burst "$IF_P2"; apply_autotune_burst "$IF_P4"
    
    # Ambil Config QoS & Stats Baru
    read p1_rxp p1_rxb p1_txp p1_txb <<< $(get_ovs_stats "$IF_P1"); p1_drp=$(get_tc_drops "$IF_P1")
    read p2_rxp p2_rxb p2_txp p2_txb <<< $(get_ovs_stats "$IF_P2"); p2_drp=$(get_tc_drops "$IF_P2")
    read p4_rxp p4_rxb p4_txp p4_txb <<< $(get_ovs_stats "$IF_P4"); p4_drp=$(get_tc_drops "$IF_P4")

    # Delta Drops
    d1=$((p1_drp - p1_drp_o)); d2=$((p2_drp - p2_drp_o)); d4=$((p4_drp - p4_drp_o))
    [ $d1 -lt 0 ] && d1=0; [ $d2 -lt 0 ] && d2=0; [ $d4 -lt 0 ] && d4=0

    # Get QoS Config
    read prio1 r1 b1 <<< $(get_qos_cfg "$IF_P1")
    read prio2 r2 b2 <<< $(get_qos_cfg "$IF_P2")
    read prio4 r4 b4 <<< $(get_qos_cfg "$IF_P4")

    # Kalkulasi Metrik (dengan Loss Rate)
    # Args: rxb, rxb_o, txb, txb_o, rxp, rxp_o, txp, txp_o, interval, link_cap, rate_limit, drops
    m1=$(calc_metrics_with_loss "$p1_rxb" "$p1_rxb_o" "$p1_txb" "$p1_txb_o" "$p1_rxp" "$p1_rxp_o" "$p1_txp" "$p1_txp_o" "$INTERVAL" "$LINK_CAP_Mbps" "$r1" "$d1")
    m2=$(calc_metrics_with_loss "$p2_rxb" "$p2_rxb_o" "$p2_txb" "$p2_txb_o" "$p2_rxp" "$p2_rxp_o" "$p2_txp" "$p2_txp_o" "$INTERVAL" "$LINK_CAP_Mbps" "$r2" "$d2")
    m4=$(calc_metrics_with_loss "$p4_rxb" "$p4_rxb_o" "$p4_txb" "$p4_txb_o" "$p4_rxp" "$p4_rxp_o" "$p4_txp" "$p4_txp_o" "$INTERVAL" "$LINK_CAP_Mbps" "$r4" "$d4")

    # Ambil data individu untuk terminal
    # format calc_metrics_with_loss: rx_mbps,tx_mbps,rx_pps,tx_pps,avg,util,loss_pct
    u1=$(echo $m1 | cut -d',' -f6); l1=$(echo $m1 | cut -d',' -f7); pps1=$(echo $m1 | cut -d',' -f3)
    u2=$(echo $m2 | cut -d',' -f6); l2=$(echo $m2 | cut -d',' -f7); pps2=$(echo $m2 | cut -d',' -f3)
    u4=$(echo $m4 | cut -d',' -f6); l4=$(echo $m4 | cut -d',' -f7); pps4=$(echo $m4 | cut -d',' -f3)

    # Delay & Payload dari log eksternal
    read dy1 pl1 <<< $(get_delay_payload "dht11")
    read dy2 pl2 <<< $(get_delay_payload "camera")
    read dy4 pl4 <<< $(get_delay_payload "max")

    # Simpan ke CSV
    # Structure: TS, m1(7 cols), d1(drops), dy1, pl1, prio1, r1, b1, ...
    echo "$TS,$m1,$d1,${dy1:-0},${pl1:-0},$prio1,$r1,$b1,$m2,$d2,${dy2:-0},${pl2:-0},$prio2,$r2,$b2,$m4,$d4,${dy4:-0},${pl4:-0},$prio4,$r4,$b4" >> "$OUT"

    # LOG KE TERMINAL
    printf "[%s] | Intv: %ss\n" "$TS" "$INTERVAL"
    printf "  P1 (DHT11)  | Util: %-6s%% | Recv: %-7s pps | Drop: %-5s | Loss: %-5s%%\n" "$u1" "$pps1" "$d1" "$l1"
    printf "  P2 (Camera) | Util: %-6s%% | Recv: %-7s pps | Drop: %-5s | Loss: %-5s%%\n" "$u2" "$pps2" "$d2" "$l2"
    printf "  P4 (Medical)| Util: %-6s%% | Recv: %-7s pps | Drop: %-5s | Loss: %-5s%%\n" "$u4" "$pps4" "$d4" "$l4"
    echo "---------------------------------------------------------------------------------------"

    # Update Old Stats
    p1_rxp_o=$p1_rxp; p1_rxb_o=$p1_rxb; p1_txp_o=$p1_txp; p1_txb_o=$p1_txb; p1_drp_o=$p1_drp
    p2_rxp_o=$p2_rxp; p2_rxb_o=$p2_rxb; p2_txp_o=$p2_txp; p2_txb_o=$p2_txb; p2_drp_o=$p2_drp
    p4_rxp_o=$p4_rxp; p4_rxb_o=$p4_rxb; p4_txp_o=$p4_txp; p4_txb_o=$p4_txb; p4_drp_o=$p4_drp
    sleep "$INTERVAL"
done