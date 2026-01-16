from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, DEAD_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.packet import packet, ipv4, udp
from ryu.lib import hub
import json
import requests
import time

# --- MONKEY PATCH OF 1.0 ---
if not hasattr(ofproto_v1_0, 'OFPET_EXPERIMENTER'):
    ofproto_v1_0.OFPET_EXPERIMENTER = 0xffff

# --- KONFIGURASI ---
INFLUX_ENDPOINT = "http://192.168.111.129:5001/sensor-max"

class SensorPacketHandler(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(SensorPacketHandler, self).__init__(*args, **kwargs)
        self.datapaths = {}
        self.monitor_thread = hub.spawn(self._monitor)

    # --- MONITORING TRAFFIC ---
    def _monitor(self):
        while True:
            for dp in self.datapaths.values():
                self._request_stats(dp)
            hub.sleep(1)

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

            # Traffic Stats di-generate oleh Ryu, jadi timestamp ini adalah Server Side Time
            traffic_data = {
                "type": "traffic_stats",
                "dpid": dpid,
                "port": port_num,
                "rx_bytes": stat.rx_bytes,
                "tx_bytes": stat.tx_bytes,
                "timestamp": time.time() # Ryu Timestamp
            }
            self.send_to_influx(traffic_data)

    # --- PACKET IN (SENSOR) ---
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        
        self.logger.info("✅ Switch Connected: %016x", datapath.id)

        match = parser.OFPMatch(in_port=4)
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

        if in_port != 4: return

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
                    
                    # [BARU] INJEKSI WAKTU RYU (SERVER SIDE TIMESTAMP)
                    # Kita masukkan waktu saat Ryu memproses paket ini
                    json_data['ryu_timestamp'] = time.time()
                    
                    self.logger.info("📥 Processing JSON from port 4")
                    self.send_to_influx(json_data)
            except Exception as e:
                self.logger.error("❌ Decode Error: %s", str(e))

    def send_to_influx(self, data):
        hub.spawn(self._post_request, data)

    def _post_request(self, data):
        try:
            requests.post(INFLUX_ENDPOINT, json=data, timeout=0.5)
        except Exception:
            pass

    @set_ev_cls(ofp_event.EventOFPStateChange, [MAIN_DISPATCHER, DEAD_DISPATCHER])
    def _state_change_handler(self, ev):
        datapath = ev.datapath
        if ev.state == MAIN_DISPATCHER:
            if datapath.id not in self.datapaths:
                self.datapaths[datapath.id] = datapath
        elif ev.state == DEAD_DISPATCHER:
            if datapath.id in self.datapaths:
                del self.datapaths[datapath.id]
