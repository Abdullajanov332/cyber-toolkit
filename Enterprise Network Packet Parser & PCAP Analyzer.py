"""
Cyber Security Toolkit - Enterprise Network Packet Parser
Author: @abdullajaanov
Role: Chief Cyber Architect
"""

import logging
from scapy.all import rdpcap, sniff, IP, TCP, UDP, Packet

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NetworkParser")

class EnterpriseNetworkAnalyzer:
    """High-fidelity deep packet inspection (DPI) subsystem."""
    
    def __init__(self) -> None:
        print("[+] @abdullajaanov Deep Packet Inspection Engine Layer Active.")

    @staticmethod
    def extract_telemetry(packet: Packet) -> str:
        """Parses network layer metadata and maps telemetry payload."""
        if not packet.haslayer(IP):
            return "Non-IP Layer 2 Traffic"

        ip_layer = packet[IP]
        protocol = "UNKNOWN"
        
        if packet.haslayer(TCP): protocol = "TCP"
        elif packet.haslayer(UDP): protocol = "UDP"

        return f"[{protocol}] {ip_layer.src} -> {ip_layer.dst} | Length: {packet.len} bytes"

    def packet_ingress_callback(self, packet: Packet) -> None:
        """Callback handler engineered for live high-throughput sniffing."""
        telemetry = self.extract_telemetry(packet)
        print(f"[@abdullajaanov Sniffer] {telemetry}")

    def ingest_pcap(self, pcap_path: str) -> None:
        """Parses static PCAP data capturing baseline structures."""
        logger.info(f"Ingesting binary storage dump: {pcap_path}")
        try:
            packets = rdpcap(pcap_path)
            for idx, packet in enumerate(packets[:10]):
                print(f"Frame #{idx}: {self.extract_telemetry(packet)}")
        except Exception as e:
            logger.error(f"Failed to extract PCAP details: {e}")

if __name__ == "__main__":
    analyzer = EnterpriseNetworkAnalyzer()
    print("[*] To run live network sniffer, evoke: sniff(prn=analyzer.packet_ingress_callback, count=10)")
