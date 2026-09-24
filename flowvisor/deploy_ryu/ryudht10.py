from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, DEAD_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.packet import packet, ipv4, udp
from ryu.lib import hub  # Wajib untuk threading
import json
import requests
import time

# ==============================================================================
# 1. OBAT ANTI-CRASH (MONKEY PATCH) - WAJIB ADA DI ATAS
# ==============================================================================
# Ini menyuntikkan atribut OFPET_EXPERIMENTER ke library OF 1.0
# supaya error "AttributeError" yang kemarin hilang selamanya.
if not hasattr(ofproto_v1_0, 'OFPET_EXPERIMENTER'):
    ofproto_v1_0.OFPET_EXPERIMENTER = 0xffff
# ==============================================================================

INFLUX_ENDPOINT = "http://192.168.111.129:5000/sensor"

class SensorPacketHandler(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(SensorPacketHandler, self).__init__(*args, **kwargs)
        self.datapaths = {}
        # Menjalankan thread terpisah untuk monitoring traffic (Throughput)
        self.monitor_thread = hub.spawn(self._monitor)

    # ==========================================================================
    # BAGIAN MONITORING TRAFFIC (Untuk Grafana)
    # ==========================================================================
    def _monitor(self):
        while True:
            for dp in self.datapaths.values():
                self._request_stats(dp)
            hub.sleep(1) # Cek setiap 1 detik

    def _request_stats(self, datapath):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        # Syntax OF 1.0 untuk minta stats semua port
        req = parser.OFPPortStatsRequest(datapath, 0, ofproto.OFPP_NONE)
        datapath.send_msg(req)

    @set_ev_cls(ofp_event.EventOFPPortStatsReply, MAIN_DISPATCHER)
    def _port_stats_reply_handler(self, ev):
        body = ev.msg.body
        dpid = ev.msg.datapath.id

        for stat in body:
            port_num = stat.port_no
            
            # Filter: Abaikan port Local/Controller (biasanya angkanya besar > 65000)
            if port_num > 65000:
                continue

            # Bungkus data throughput
            traffic_data = {
                "type": "traffic_stats", # Penanda buat database
                "dpid": dpid,
                "port": port_num,
                "rx_bytes": stat.rx_bytes, # Data Penting buat Grafana
                "tx_bytes": stat.tx_bytes,
                "timestamp": time.time()
            }
            # Kirim ke InfluxDB
            self.send_to_influx(traffic_data)

    # ==========================================================================
    # BAGIAN PACKET IN (Sensor Data JSON)
    # ==========================================================================
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        self.logger.info("✅ Switch Connected (OF 1.0): %016x", datapath.id)

        # HATI-HATI: Pastikan Port Raspi kamu benar-benar '1'
        # Cek pakai: sudo ovs-ofctl show br0
        match = parser.OFPMatch(in_port=1) 
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER)]
        
        mod = parser.OFPFlowMod(
            datapath=datapath,
            match=match,
            cookie=0,
            command=ofproto.OFPFC_ADD,
            idle_timeout=0,
            hard_timeout=0,
            priority=100, # Priority tinggi biar menang lawan rule default
            flags=ofproto.OFPFF_SEND_FLOW_REM,
            actions=actions
        )
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        in_port = msg.in_port # Cara ambil port di OF 1.0

        if in_port != 1:
            # self.logger.debug("Packet drop from port %s", in_port)
            return

        pkt = packet.Packet(msg.data)
        udp_pkt = pkt.get_protocol(udp.udp)

        if udp_pkt and udp_pkt.dst_port == 9999:
            try:
                payload_str = msg.data.decode(errors='ignore')
                json_start = payload_str.find('{')
                if json_start != -1:
                    raw_json = payload_str[json_start:].strip('\x00')
                    json_data = json.loads(raw_json)
                    
                    # Tambahin tipe biar backend tau ini data sensor
                    json_data['type'] = "sensor_data" 
                    
                    self.logger.info("📥 Received JSON from port 1: %s", json_data)
                    self.send_to_influx(json_data)
            except Exception as e:
                self.logger.error("❌ Failed to decode JSON: %s", str(e))

    # ==========================================================================
    # BAGIAN ERROR HANDLER (Supaya Log Bersih)
    # ==========================================================================
    @set_ev_cls(ofp_event.EventOFPErrorMsg, [MAIN_DISPATCHER, CONFIG_DISPATCHER])
    def error_msg_handler(self, ev):
        msg = ev.msg
        self.logger.warning("⚠️ Switch Error: type=0x%02x code=0x%02x", msg.type, msg.code)
        # Dengan Monkey Patch di atas, kode ini tidak akan bikin crash lagi.

    # ==========================================================================
    # FUNGSI KIRIM KE API (Async/Non-Blocking)
    # ==========================================================================
    def send_to_influx(self, data):
        # Pakai hub.spawn biar Ryu gak nungguin (loading) saat kirim data
        hub.spawn(self._post_request, data)

    def _post_request(self, data):
        try:
            requests.post(INFLUX_ENDPOINT, json=data, timeout=1)
        except Exception:
            pass # Silent error biar log gak penuh spam connection error
            
    # Detect Switch Connection State
    @set_ev_cls(ofp_event.EventOFPStateChange, [MAIN_DISPATCHER, DEAD_DISPATCHER])
    def _state_change_handler(self, ev):
        datapath = ev.datapath
        if ev.state == MAIN_DISPATCHER:
            if datapath.id not in self.datapaths:
                self.datapaths[datapath.id] = datapath
        elif ev.state == DEAD_DISPATCHER:
            if datapath.id in self.datapaths:
                del self.datapaths[datapath.id]
