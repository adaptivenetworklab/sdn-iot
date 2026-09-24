#!/bin/bash
# debug_and_reset.sh - Debugging & Hard Reset untuk Statistik OVS/TC
# Gunakan script ini SEBELUM memulai pengujian baru

set -e

BRIDGE=${1:-br0}
INTERFACES=("dht11" "camera" "max")
IPS=("192.168.15.238" "192.168.15.239" "192.168.15.240")

echo "=========================================="
echo "  OVS/TC Statistics Debug & Reset Tool"
echo "=========================================="
echo ""

# --- 1. CEK PROSES YANG MASIH JALAN ---
echo "[1] Checking for running processes..."
echo ""

LISTENER_PID=$(pgrep -f "udp_listener_v2.py" || echo "")
SENDER_PID=$(pgrep -f "allport.py" || echo "")
MONITOR_PID=$(pgrep -f "collect_policy" || echo "")

if [ -n "$LISTENER_PID" ]; then
    echo "⚠️  WARNING: UDP Listener still running (PID: $LISTENER_PID)"
    read -p "Kill listener? [y/N]: " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        sudo kill -9 $LISTENER_PID
        echo "✓ Listener killed"
    fi
else
    echo "✓ No listener process found"
fi

if [ -n "$SENDER_PID" ]; then
    echo "⚠️  WARNING: Sender (allport.py) still running (PID: $SENDER_PID)"
    read -p "Kill sender? [y/N]: " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        sudo kill -9 $SENDER_PID
        echo "✓ Sender killed"
    fi
else
    echo "✓ No sender process found"
fi

if [ -n "$MONITOR_PID" ]; then
    echo "⚠️  WARNING: Monitor script still running (PID: $MONITOR_PID)"
    read -p "Kill monitor? [y/N]: " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        sudo kill -9 $MONITOR_PID
        echo "✓ Monitor killed"
    fi
else
    echo "✓ No monitor process found"
fi

echo ""
sleep 2

# --- 2. CEK STATISTIK SAAT INI ---
echo "[2] Current OVS Flow Statistics:"
echo ""

for i in "${!IPS[@]}"; do
    IP=${IPS[$i]}
    NAME=${INTERFACES[$i]}
    
    echo "Interface: $NAME (IP: $IP)"
    STATS=$(sudo ovs-ofctl dump-flows "$BRIDGE" "udp,nw_dst=$IP,tp_dst=9999" 2>/dev/null | grep "n_bytes" || echo "no flow found")
    
    if [[ "$STATS" == "no flow found" ]]; then
        echo "  Status: ✓ No flow exists (CLEAN)"
    else
        PKTS=$(echo "$STATS" | grep -oP 'n_packets=\K[0-9]+' || echo 0)
        BYTES=$(echo "$STATS" | grep -oP 'n_bytes=\K[0-9]+' || echo 0)
        echo "  Packets: $PKTS"
        echo "  Bytes: $BYTES"
        
        if [ "$PKTS" -gt 0 ] || [ "$BYTES" -gt 0 ]; then
            echo "  Status: ⚠️  STALE DATA DETECTED"
        fi
    fi
    echo ""
done

# --- 3. CEK TC DROP STATISTICS ---
echo "[3] Current TC Drop Statistics:"
echo ""

for IF in "${INTERFACES[@]}"; do
    DROPS=$(sudo tc -s filter show dev "$IF" parent ffff: 2>/dev/null | grep -oP 'dropped \K[0-9]+' | head -n 1 || echo 0)
    echo "Interface: $IF"
    echo "  Dropped packets: $DROPS"
    
    if [ "$DROPS" -gt 0 ]; then
        echo "  Status: ⚠️  STALE DROP DATA"
    else
        echo "  Status: ✓ Clean"
    fi
    echo ""
done

# --- 4. HARD RESET ---
echo ""
read -p "Perform HARD RESET of all statistics? [y/N]: " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Reset cancelled. Exiting."
    exit 0
fi

echo ""
echo "[4] Performing Hard Reset..."
echo ""

# Reset OVS Flows
echo "→ Deleting all UDP flows to port 9999..."
for IP in "${IPS[@]}"; do
    sudo ovs-ofctl del-flows "$BRIDGE" "udp,nw_dst=$IP,tp_dst=9999" 2>/dev/null || true
done
echo "✓ OVS flows deleted"

# Re-add flows (opsional, tergantung controller kamu)
echo ""
echo "→ Re-adding clean flows..."
for i in "${!IPS[@]}"; do
    IP=${IPS[$i]}
    PORT=$((i+1))  # Port 1, 2, 4 sesuai kebutuhan
    if [ $PORT -eq 3 ]; then PORT=4; fi  # Skip port 3
    
    sudo ovs-ofctl add-flow "$BRIDGE" "priority=100,udp,nw_dst=$IP,tp_dst=9999,actions=output:$PORT" 2>/dev/null || true
done
echo "✓ Fresh flows installed"

# Reset TC
echo ""
echo "→ Resetting TC filters and qdiscs..."
for IF in "${INTERFACES[@]}"; do
    # Remove ingress qdisc (will remove all filters)
    sudo tc qdisc del dev "$IF" ingress 2>/dev/null || true
    
    # Re-add ingress qdisc
    sudo tc qdisc add dev "$IF" ingress 2>/dev/null || true
    
    # Re-add drop filter if needed (example)
    # Adjust according to your actual TC setup
    # sudo tc filter add dev "$IF" parent ffff: protocol ip prio 50 u32 match u32 0 0 police rate 1mbit burst 100k drop flowid :1
done
echo "✓ TC statistics reset"

# Reset interface statistics (optional - requires interface down/up)
echo ""
read -p "Reset interface statistics? (requires brief interface restart) [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    for IF in "${INTERFACES[@]}"; do
        echo "  Resetting $IF..."
        sudo ip link set "$IF" down 2>/dev/null || true
        sleep 0.5
        sudo ip link set "$IF" up 2>/dev/null || true
    done
    echo "✓ Interface statistics reset"
fi

echo ""
echo "=========================================="
echo "  ✓ RESET COMPLETE"
echo "=========================================="
echo ""
echo "Recommendations:"
echo "1. Wait 5 seconds before starting tests"
echo "2. Start listener first: python3 udp_listener_v2.py"
echo "3. Start sender second: python3 allport.py"
echo "4. Start monitor last: ./collect_policy_4.sh"
echo ""
