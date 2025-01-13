from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        # Extract IP details
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        # Map protocol number to name
        protocol_name = {1: "ICMP", 6: "TCP", 17: "UDP"}.get(protocol, "Other")

        print(f"\n[Packet Captured]")
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol_name}")

        # Check if payload exists and print
        if protocol_name == "TCP" and TCP in packet:
            print(f"Payload: {bytes(packet[TCP].payload)}")
        elif protocol_name == "UDP" and UDP in packet:
            print(f"Payload: {bytes(packet[UDP].payload)}")
        elif protocol_name == "ICMP" and ICMP in packet:
            print(f"Payload: {bytes(packet[ICMP].payload)}")
        else:
            print(f"Payload: {bytes(packet.payload)}")
    else:
        print("Non-IP packet detected.")

def main():
    print("Starting packet sniffer...")
    print("Press Ctrl+C to stop.\n")

    # Start packet sniffing
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
