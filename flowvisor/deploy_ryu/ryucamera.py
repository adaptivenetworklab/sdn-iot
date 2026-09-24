from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.packet import packet, ipv4, udp
import json
import requests

# =========================
# CONFIG
# =========================
INFLUX_ENDPOINT = "http://192.168.111.129:5003/camera"  # API Database
CAMERA_UDP_PORT = 9999
ALLOWED_IN_PORT = 2  # port kamera masuk ke OVS

class CameraPacketHandler(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(CameraPacketHandler, self).__init__(*args, **kwargs)
        self.logger.info("📷 Camera Metadata UDP Handler Started")

    # =========================
    # FLOW RULE
    # =========================
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # Semua trafik dari port kamera diarahkan ke controller
        match = parser.OFPMatch(in_port=ALLOWED_IN_PORT)
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER)]

        mod = parser.OFPFlowMod(
            datapath=datapath,
            match=match,
            command=ofproto.OFPFC_ADD,
            priority=100,
            actions=actions
        )
        datapath.send_msg(mod)

        self.logger.info("✅ Flow installed: port %s → controller", ALLOWED_IN_PORT)

    # =========================
    # PACKET IN
    # =========================
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        in_port = msg.in_port

        if in_port != ALLOWED_IN_PORT:
            return

        pkt = packet.Packet(msg.data)
        ip_pkt = pkt.get_protocol(ipv4.ipv4)
        udp_pkt = pkt.get_protocol(udp.udp)

        # Filter UDP ke port 9999
        if not (ip_pkt and udp_pkt and udp_pkt.dst_port == CAMERA_UDP_PORT):
            return

        try:
            # extract JSON dari payload mentah
            raw_payload = msg.data.decode(errors="ignore")
            json_start = raw_payload.find("{")

            if json_start == -1:
                self.logger.warning("⚠️ No JSON found in payload")
                return

            json_data = json.loads(raw_payload[json_start:])

            self.logger.info("📥 Camera Metadata Received:")
            self.logger.info("   Camera ID  : %s", json_data.get("camera_id"))
            self.logger.info("   Timestamp  : %s", json_data.get("timestamp"))
            self.logger.info("   Person Cnt : %s", json_data.get("person_count"))
            self.logger.info("   Image Name : %s", json_data.get("image_name"))
            self.logger.info("   Image Hash : %s", json_data.get("image_hash"))

            self.send_to_influx(json_data)

        except Exception as e:
            self.logger.error("❌ Packet parse error: %s", str(e))

    # =========================
    # SEND TO API DB
    # =========================
    def send_to_influx(self, data):
        try:
            res = requests.post(INFLUX_ENDPOINT, json=data, timeout=5)
            if res.status_code == 200:
                self.logger.info("✅ Metadata forwarded to API DB (Influx)")
            else:
                self.logger.warning("⚠️ API DB response: %s | %s", res.status_code, res.text)
        except Exception as e:
            self.logger.error("❌ Failed sending to API DB: %s", str(e))
