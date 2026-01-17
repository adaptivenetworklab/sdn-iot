from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, DEAD_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.packet import packet, ipv4, udp
from ryu.lib import hub  # Wajib untuk threading monitoring
import json
import requests
import time

# ==============================================================================
# 1. OBAT ANTI-CRASH (MONKEY PATCH OF 1.0)
# ==============================================================================
if not hasattr(ofproto_v1_0, 'OFPET_EXPERIMENTER'):
    ofproto_v1_0.OFPET_EXPERIMENTER = 0xffff

# ==============================================================================
# KONFIGURASI ENDPOINT
# ==============================================================================
# Pastikan Port 5000 (Sesuai influx-api-all.py)
INFLUX_ENDPOINT = "http://192.168.111.129:5000/sensor"

class SensorPacketHandler(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(SensorPacketHandler, self).__init__(*args, **kwargs)
        self.datapaths = {}
        # Menjalankan thread terpisah untuk monitoring traffic (RX/TX)
        self.monitor_thread = hub.spawn(self._monitor)

    # ==========================================================================
    # BAGIAN MONITORING TRAFFIC (RX/TX)
    # ==========================================================================
    def _monitor(self):
        while True:
            for dp in self.datapaths.values():
                self._request_stats(dp)
            hub.sleep(1) # Cek setiap 1 detik

    def _request_stats(self, datapath):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        req = parser.OFPPortStatsRequest(datapath, 0, ofproto.OFPP_NONE)
        datapath.send_msg(req)

    @set_ev_cls(ofp_event.EventOFPPortStatsReply, MAIN_DISPATCHER)
    def _port_stats_reply_handler(self, ev):
        body = ev.msg.body
        dpid = ev.msg.datapath.id

        for stat in body:
            port_num = stat.port_no
            if port_num > 65000: continue

            # Traffic Stats: Tidak perlu inject ryu_timestamp karena API mengabaikan latency untuk tipe ini
            traffic_data = {
                "type": "traffic_stats", 
                "dpid": dpid,
                "port": port_num,
                "rx_bytes": stat.rx_bytes,
                "tx_bytes": stat.tx_bytes,
                "timestamp": time.time()
            }
            self.send_to_influx(traffic_data)

    # ==========================================================================
    # BAGIAN PACKET IN (Sensor Data JSON - PORT 1)
    # ==========================================================================
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        self.logger.info("✅ Switch Connected (OF 1.0): %016x", datapath.id)

        # Match Port 1 (DHT11)
        match = parser.OFPMatch(in_port=1)
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER)]
        
        mod = parser.OFPFlowMod(
            datapath=datapath, match=match, cookie=0,
            command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
            priority=100, flags=ofproto.OFPFF_SEND_FLOW_REM, actions=actions
        )
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        in_port = msg.in_port 

        if in_port != 1: return # Pastikan hanya dari Port 1

        pkt = packet.Packet(msg.data)
        udp_pkt = pkt.get_protocol(udp.udp)

        if udp_pkt and udp_pkt.dst_port == 9999:
            try:
                payload_str = msg.data.decode(errors='ignore')
                json_start = payload_str.find('{')
                if json_start != -1:
                    raw_json = payload_str[json_start:].strip('\x00')
                    json_data = json.loads(raw_json)
                    
                    json_data['type'] = "sensor_data" 
                    
                    # [QoS INJECTION - MISSING LINK YANG SAYA TAMBAHKAN]
                    current_time = time.time()
                    json_data['ryu_timestamp'] = current_time
                    
                    self.logger.info("✅ PACKET-IN (DHT): Injecting Timestamp %s", current_time)
                    self.logger.info("📥 Processing JSON from port 1: %s", json_data)
                    
                    self.send_to_influx(json_data)
            except Exception as e:
                self.logger.error("❌ Failed to decode JSON: %s", str(e))

    def send_to_influx(self, data):
        hub.spawn(self._post_request, data)

    def _post_request(self, data):
        try:
            requests.post(INFLUX_ENDPOINT, json=data, timeout=0.5)
        except Exception as e:
            print(f"❌ API SEND ERROR: {e}") 

    @set_ev_cls(ofp_event.EventOFPStateChange, [MAIN_DISPATCHER, DEAD_DISPATCHER])
    def _state_change_handler(self, ev):
        datapath = ev.datapath
        if ev.state == MAIN_DISPATCHER:
            if datapath.id not in self.datapaths:
                self.datapaths[datapath.id] = datapath
        elif ev.state == DEAD_DISPATCHER:
            if datapath.id in self.datapaths:
                del self.datapaths[datapath.id]
