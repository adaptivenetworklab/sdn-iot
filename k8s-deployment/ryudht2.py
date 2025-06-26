from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.packet import packet, ethernet, ipv4, udp
import json
import requests

INFLUX_ENDPOINT = "http://10.0.1.148:5000/sensor"

class SensorPacketHandler(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(SensorPacketHandler, self).__init__(*args, **kwargs)

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # Hanya match untuk in_port 1
        match = parser.OFPMatch(in_port=1)
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER)]
        mod = parser.OFPFlowMod(
            datapath=datapath,
            match=match,
            cookie=0,
            command=ofproto.OFPFC_ADD,
            idle_timeout=0,
            hard_timeout=0,
            priority=0,
            flags=0,
            actions=actions
        )
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        in_port = msg.in_port  # ✅ Ambil nilai in_port dari pesan

        if in_port != 1:
            self.logger.debug("🔃 Packet dropped: not from port 1 (got port %s)", in_port)
            return  # ❌ Abaikan selain port 1

        pkt = packet.Packet(msg.data)
        udp_pkt = pkt.get_protocol(udp.udp)
        ip_pkt = pkt.get_protocol(ipv4.ipv4)

        if udp_pkt and ip_pkt and udp_pkt.dst_port == 9999:
            try:
                payload_str = msg.data.decode(errors='ignore')
                json_start = payload_str.find('{')
                if json_start != -1:
                    json_data = json.loads(payload_str[json_start:])
                    self.logger.info("📥 Received JSON from port 1: %s", json_data)
                    self.send_to_influx(json_data)
                else:
                    self.logger.warning("⚠️ Payload tidak valid: %s", payload_str)

            except Exception as e:
                self.logger.error("❌ Failed to decode JSON payload: %s", str(e))

    def send_to_influx(self, data):
        try:
            res = requests.post(INFLUX_ENDPOINT, json=data)
            if res.status_code == 200:
                self.logger.info("✅ Data sent to InfluxDB")
            else:
                self.logger.warning("⚠️  Failed to send. Status code: %s", res.status_code)
        except Exception as e:
            self.logger.error("❌ Error sending to InfluxDB: %s", str(e))

