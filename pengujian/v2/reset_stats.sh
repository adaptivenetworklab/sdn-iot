#!/bin/bash
# reset_stats.sh - Reset Total Statistik OVS dan Policing (TC)

# --- 1. KONFIGURASI ---
BRIDGE="br0"
IFS_IOT=("dht11" "camera" "max")
# IP Tujuan sesuai sensor
IP_DHT="192.168.15.238"
IP_CAM="192.168.15.239"
IP_MED="192.168.15.240"

echo "[*] Memulai Hard Reset Statistik..."

# --- 2. RESET INGRESS POLICING (Mengenolkan Drop) ---
# Kita set ke 0 dulu untuk menghapus filter di kernel, lalu kembalikan ke 1000
echo "[>] Mereset konter Drop pada interface..."
for iface in "${IFS_IOT[@]}"; do
    sudo ovs-vsctl set interface "$iface" ingress_policing_rate=0 ingress_policing_burst=0
    sudo ovs-vsctl set interface "$iface" ingress_policing_rate=1000 ingress_policing_burst=100
    echo "    - $iface: Reset OK"
done

# --- 3. RESET OPENFLOW FLOWS (Mengenolkan Recv) ---
echo "[>] Menghapus semua OpenFlow Flows di $BRIDGE..."
sudo ovs-ofctl del-flows "$BRIDGE"

# --- 4. MEMASANG KEMBALI FLOW FILTER ---
echo "[>] Memasang kembali aturan filter UDP 9999..."
# Filter untuk masing-masing sensor agar n_packets mulai dari 0
sudo ovs-ofctl add-flow "$BRIDGE" "priority=200,udp,nw_dst=$IP_DHT,tp_dst=9999,actions=normal"
sudo ovs-ofctl add-flow "$BRIDGE" "priority=200,udp,nw_dst=$IP_CAM,tp_dst=9999,actions=normal"
sudo ovs-ofctl add-flow "$BRIDGE" "priority=200,udp,nw_dst=$IP_MED,tp_dst=9999,actions=normal"

echo "[*] Reset Selesai! Statistik sekarang benar-benar 0."
echo "[!] Pastikan script pengirim di Raspberry Pi sudah dimatikan (killall python3)."
