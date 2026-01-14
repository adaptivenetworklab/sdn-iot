#!/usr/bin/env python3

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet, ipv4, udp

import json
import requests


class PayloadBasedDHT11_OF10(app_manager.RyuApp):
    """
    OpenFlow 1.0 SDN Controller
    - Packet-In UDP dst 9999
    - Inspect JSON payload
    - Forward to Flask API (/sensor) -> InfluxDB writer
    """

    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    # ===== Konfigurasi =====
    OVS_UDP_PORT = 9999
    API_ENDPOINT = "http://192.168.111.129:5004/sensor"
    API_TIMEOUT = 1

    def __init__(self, *args, **kwargs):
        super(PayloadBasedDHT11_OF10, self).__init__(*args, **kwargs)
        self.logger.info("[INIT] Ryu OF1.0 Payload-Based DHT11 Controller started")
        self.logger.info(f"[INIT] Filter UDP dst port: {self.OVS_UDP_PORT}")
        self.logger.info(f"[INIT] API endpoint: {self.API_ENDPOINT}")

    # ==============================
    # Install flow helper (OF1.0)
    # ==============================
    def add_flow(self, datapath, match, actions, priority=1):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        mod = parser.OFPFlowMod(
            datapath=datapath,
            match=match,
            cookie=0,
            command=ofproto.OFPFC_ADD,
            idle_timeout=0,
            hard_timeout=0,
            priority=priority,
            flags=ofproto.OFPFF_SEND_FLOW_REM,
            actions=actions
        )
        datapath.send_msg(mod)

    # ==============================
    # Switch connect (OF1.0)
    # ==============================
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        self.logger.info(f"[SWITCH] Connected dpid={datapath.id}")

        # 1) Default: send all unmatched to controller
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER)]
        self.add_flow(datapath, match, actions, priority=0)

        # 2) Rule khusus UDP dst port 9999 -> controller (priority lebih tinggi)
        match_udp_9999 = parser.OFPMatch(
            dl_type=0x0800,   # IPv4
            nw_proto=17,      # UDP
            tp_dst=self.OVS_UDP_PORT
        )
        actions_udp_9999 = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER)]
        self.add_flow(datapath, match_udp_9999, actions_udp_9999, priority=10)

        self.logger.info("[FLOW] Installed: table-miss + UDP:9999 -> controller")

    # ==============================
    # Packet-In handler
    # ==============================
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg

        pkt = packet.Packet(msg.data)

        eth = pkt.get_protocol(ethernet.ethernet)
        ip4 = pkt.get_protocol(ipv4.ipv4)
        udp_seg = pkt.get_protocol(udp.udp)

        if eth is None or ip4 is None or udp_seg is None:
            return

        # Filter hanya UDP dst port 9999
        if udp_seg.dst_port != self.OVS_UDP_PORT:
            return

        payload_bytes = self._extract_udp_payload(msg.data)
        if payload_bytes is None:
            self.logger.warning("[WARN] Cannot extract UDP payload")
            return

        payload_str = payload_bytes.decode("utf-8", errors="ignore").strip()

        # Harus JSON
        try:
            data = json.loads(payload_str)
        except Exception:
            self.logger.warning(f"[WARN] Payload not JSON: {payload_str}")
            return

        # ===== Payload-based logic (DHT11 only for now) =====
        # Raspi kamu kirim:
        # {"Temperature": 25, "Humidity": 80}
        #
        # API kamu expect lowercase:
        # {"temperature": ..., "humidity": ...}
        #
        # Jadi kita normalize biar aman.
        if "Temperature" in data and "Humidity" in data:
            forward_obj = {
                "temperature": data["Temperature"],
                "humidity": data["Humidity"]
            }
        elif "temperature" in data and "humidity" in data:
            forward_obj = {
                "temperature": data["temperature"],
                "humidity": data["humidity"]
            }
        else:
            self.logger.warning(f"[WARN] Unrecognized IoT JSON format: {data}")
            return

        self.logger.info(
            f"[DHT11] From {ip4.src}:{udp_seg.src_port} -> API {forward_obj}"
        )

        # Forward ke Flask API
        self._post_to_api(forward_obj)

    # ==============================
    # Extract UDP payload (manual)
    # ==============================
    def _extract_udp_payload(self, raw_bytes):
        """
        Ethernet header = 14 bytes
        IPv4 header len = IHL * 4
        UDP header = 8 bytes
        payload = remaining bytes
        """
        try:
            if len(raw_bytes) < 14 + 20 + 8:
                return None

            ip_offset = 14
            ihl = raw_bytes[ip_offset] & 0x0F
            ip_header_len = ihl * 4

            udp_offset = ip_offset + ip_header_len
            payload_offset = udp_offset + 8

            if payload_offset > len(raw_bytes):
                return None

            return raw_bytes[payload_offset:]
        except Exception:
            return None

    # ==============================
    # Post to API
    # ==============================
    def _post_to_api(self, obj):
        try:
            r = requests.post(self.API_ENDPOINT, json=obj, timeout=self.API_TIMEOUT)
            self.logger.info(f"[API] POST -> {r.status_code} | {r.text}")
        except Exception as e:
            self.logger.error(f"[API-ERROR] Failed POST to {self.API_ENDPOINT}: {e}")
