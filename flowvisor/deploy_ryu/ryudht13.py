from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet, ipv4, udp
import json
import requests

INFLUX_ENDPOINT = "http://192.168.10.58:5000/sensor"

class SensorPacketHandler(app_manager.RyuApp):
    # GANTI KE VERSION 1.3
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(SensorPacketHandler, self).__init__(*args, **kwargs)

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # 1. Install Table-Miss Flow (Standar OF 1.3 - Wajib biar switch ga bengong)
        # Default: Drop semua paket yang tidak dikenal (atau kirim ke controller jika diinginkan)
        # Disini kita fokus ke rule spesifik kamu aja dulu.
        
        # 2. Rule Khusus: Match in_port=1 -> Kirim ke Controller
        match = parser.OFPMatch(in_port=1)
        
        # Action: Output ke Controller. 
        # OFPCML_NO_BUFFER = Kirim seluruh paket, jangan dipotong (biar JSON kebaca)
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        
        # Di OF 1.3, Actions dibungkus dalam Instructions
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
        
        mod = parser.OFPFlowMod(
            datapath=datapath,
            priority=1,      # Kasih priority dikit biar lebih tinggi dari default
            match=match,
            instructions=inst # Pakai instructions, bukan actions langsung
        )
        datapath.send_msg(mod)
        self.logger.info("✅ Flow Mod installed: Port 1 -> Controller")

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        
        # PERUBAHAN PENTING DI SINI:
        # Di OF 1.3, msg.in_port TIDAK ADA. Harus ambil dari msg.match['in_port']
        try:
            in_port = msg.match['in_port']
        except KeyError:
            return # Skip jika tidak ada info port

        if in_port != 1:
            # self.logger.debug("🔃 Packet dropped: not from port 1 (got port %s)", in_port)
            return 

        pkt = packet.Packet(msg.data)
        udp_pkt = pkt.get_protocol(udp.udp)
        ip_pkt = pkt.get_protocol(ipv4.ipv4)

        if udp_pkt and ip_pkt and udp_pkt.dst_port == 9999:
            try:
                # Decode data payload
                payload_str = msg.data.decode(errors='ignore')
                
                # Cari kurung kurawal pembuka JSON
                json_start = payload_str.find('{')
                if json_start != -1:
                    raw_json = payload_str[json_start:]
                    # Bersihkan karakter null atau sampah di akhir string (kadang ada di UDP)
                    raw_json = raw_json.strip('\x00')
                    
                    json_data = json.loads(raw_json)
                    self.logger.info("📥 Received JSON from port 1: %s", json_data)
                    self.send_to_influx(json_data)
                else:
                    self.logger.warning("⚠️ Payload detected but no JSON found")

            except Exception as e:
                self.logger.error("❌ Failed to decode JSON payload: %s", str(e))

    def send_to_influx(self, data):
        try:
            res = requests.post(INFLUX_ENDPOINT, json=data, timeout=2) # Tambah timeout biar ga hang
            if res.status_code == 200:
                self.logger.info("✅ Data sent to InfluxDB")
            else:
                self.logger.warning("⚠️ Failed to send. Status code: %s", res.status_code)
        except Exception as e:
            self.logger.error("❌ Error sending to InfluxDB: %s", str(e))
