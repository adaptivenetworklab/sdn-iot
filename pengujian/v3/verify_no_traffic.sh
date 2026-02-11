#!/bin/bash
# verify_no_traffic.sh - Verifikasi bahwa TIDAK ADA traffic ghost packets
# Jalankan script ini SETELAH reset dan SEBELUM memulai listener/sender

BRIDGE=${1:-br0}
DURATION=${2:-30}  # Monitor selama 30 detik
INTERFACES=("dht11" "camera" "max")
IPS=("192.168.15.238" "192.168.15.239" "192.168.15.240")

echo "=========================================="
echo "  Ghost Packet Verification Test"
echo "=========================================="
echo "Duration: $DURATION seconds"
echo "Bridge: $BRIDGE"
echo ""
echo "This test will monitor for $DURATION seconds."
echo "If ANY packets are detected, there's a problem."
echo ""
read -p "Press Enter to start verification..."

# Capture initial state
declare -A INIT_PKTS INIT_BYTES INIT_DROPS

for i in "${!IPS[@]}"; do
    NAME=${INTERFACES[$i]}
    IP=${IPS[$i]}
    
    # Get initial OVS stats
    STATS=$(sudo ovs-ofctl dump-flows "$BRIDGE" "udp,nw_dst=$IP,tp_dst=9999" 2>/dev/null | grep "n_bytes" || echo "")
    
    if [ -n "$STATS" ]; then
        INIT_PKTS[$NAME]=$(echo "$STATS" | grep -oP 'n_packets=\K[0-9]+' || echo 0)
        INIT_BYTES[$NAME]=$(echo "$STATS" | grep -oP 'n_bytes=\K[0-9]+' || echo 0)
    else
        INIT_PKTS[$NAME]=0
        INIT_BYTES[$NAME]=0
    fi
    
    # Get initial TC drops
    INIT_DROPS[$NAME]=$(sudo tc -s filter show dev "$NAME" parent ffff: 2>/dev/null | grep -oP 'dropped \K[0-9]+' | head -n 1 || echo 0)
done

echo ""
echo "Initial State Captured. Monitoring..."
echo ""
printf "%-12s | %-10s | %-10s | %-10s\n" "Interface" "Packets" "Bytes" "Drops"
echo "-------------|------------|------------|------------"

for NAME in "${INTERFACES[@]}"; do
    printf "%-12s | %-10s | %-10s | %-10s\n" "$NAME" "${INIT_PKTS[$NAME]}" "${INIT_BYTES[$NAME]}" "${INIT_DROPS[$NAME]}"
done

# Monitor for changes
echo ""
echo "Waiting $DURATION seconds for any traffic..."
sleep "$DURATION"

# Check final state
echo ""
echo "Final State:"
echo ""
printf "%-12s | %-10s | %-10s | %-10s | %-10s\n" "Interface" "Δ Packets" "Δ Bytes" "Δ Drops" "Status"
echo "-------------|------------|------------|------------|------------"

GHOST_DETECTED=0

for i in "${!IPS[@]}"; do
    NAME=${INTERFACES[$i]}
    IP=${IPS[$i]}
    
    # Get final OVS stats
    STATS=$(sudo ovs-ofctl dump-flows "$BRIDGE" "udp,nw_dst=$IP,tp_dst=9999" 2>/dev/null | grep "n_bytes" || echo "")
    
    if [ -n "$STATS" ]; then
        FINAL_PKTS=$(echo "$STATS" | grep -oP 'n_packets=\K[0-9]+' || echo 0)
        FINAL_BYTES=$(echo "$STATS" | grep -oP 'n_bytes=\K[0-9]+' || echo 0)
    else
        FINAL_PKTS=0
        FINAL_BYTES=0
    fi
    
    FINAL_DROPS=$(sudo tc -s filter show dev "$NAME" parent ffff: 2>/dev/null | grep -oP 'dropped \K[0-9]+' | head -n 1 || echo 0)
    
    # Calculate deltas
    DELTA_PKTS=$((FINAL_PKTS - INIT_PKTS[$NAME]))
    DELTA_BYTES=$((FINAL_BYTES - INIT_BYTES[$NAME]))
    DELTA_DROPS=$((FINAL_DROPS - INIT_DROPS[$NAME]))
    
    # Determine status
    if [ $DELTA_PKTS -gt 0 ] || [ $DELTA_BYTES -gt 0 ] || [ $DELTA_DROPS -gt 0 ]; then
        STATUS="⚠️  GHOST!"
        GHOST_DETECTED=1
    else
        STATUS="✓ Clean"
    fi
    
    printf "%-12s | %-10s | %-10s | %-10s | %-10s\n" "$NAME" "$DELTA_PKTS" "$DELTA_BYTES" "$DELTA_DROPS" "$STATUS"
done

echo ""
echo "=========================================="

if [ $GHOST_DETECTED -eq 1 ]; then
    echo "  ❌ GHOST PACKETS DETECTED!"
    echo "=========================================="
    echo ""
    echo "Troubleshooting steps:"
    echo "1. Check for zombie processes:"
    echo "   ps aux | grep -E 'allport|udp_listener'"
    echo ""
    echo "2. Check for other UDP traffic to port 9999:"
    echo "   sudo tcpdump -i any 'udp port 9999' -c 10"
    echo ""
    echo "3. Check OVS flows manually:"
    echo "   sudo ovs-ofctl dump-flows $BRIDGE"
    echo ""
    echo "4. Re-run debug_and_reset.sh and try again"
    exit 1
else
    echo "  ✓ NO GHOST PACKETS - SYSTEM CLEAN"
    echo "=========================================="
    echo ""
    echo "You can now safely start your test:"
    echo "1. Terminal 1: python3 udp_listener_v2.py"
    echo "2. Terminal 2: python3 allport.py"
    echo "3. Terminal 3: ./collect_policy_4.sh"
    exit 0
fi
