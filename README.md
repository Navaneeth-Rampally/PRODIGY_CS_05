# PRODIGY_CS_05
Network Packet Analyzer

Task5: Network packet analyzer


This project is a simple Packet Sniffer Tool developed in Python using the scapy library.
It captures and analyzes live network packets, providing insights into network traffic.
The tool is designed for educational purposes to help users understand how network packets work and analyze key data such as source and destination IPs, protocols, and payloads.

Features
Real-time Packet Capture:

Continuously captures network packets from the active network interface.
Processes packets dynamically as they are received.
Protocol Analysis:

Identifies commonly used protocols such as TCP, UDP, and ICMP.
Provides information about the packet type for further analysis.
Payload Inspection:

Displays the payload (if available) for supported protocols.
Helps in understanding the data being transmitted.
Lightweight and Extensible:

Designed for simplicity and ease of use.
Can be extended to include additional protocol analysis or filtering capabilities.
How It Works
Packet Capture:

The sniff() function from scapy is used to capture live packets.
It processes each packet using the packet_callback function.
Packet Details Extraction:

Extracts key information such as:
Source IP Address: The originating address of the packet.
Destination IP Address: The recipient address of the packet.
Protocol: Identifies the protocol (TCP, UDP, ICMP, etc.) used in the packet.
Payload Analysis:

Extracts and displays the payload of packets if available, offering insights into the data being transmitted.
Supports protocols like TCP, UDP, and ICMP.
User-Friendly Console Output:

Presents packet details in a readable format for quick analysis.
Installation
Prerequisites
Python 3.x
scapy library (Install it using pip).
Setup
Clone the repository:
bash
Copy code
git clone <repository-url>
cd <repository-folder>
Install the required library:
bash
Copy code
pip install scapy
Usage
Run the script with administrator/root privileges (required for packet sniffing):
bash
Copy code
sudo python3 network_packet_analyzer.py
Observe the live packet capture and analysis in the console.
Press Ctrl+C to stop the sniffer.
Example Output
yaml
Copy code
[Packet Captured]
Source IP: 192.168.0.105
Destination IP: 93.184.216.34
Protocol: TCP
Payload: b'GET / HTTP/1.1\\r\\nHost: example.com\\r\\n\\r\\n'
Code Highlights
Protocol Mapping: The protocol number from the packet header is mapped to human-readable names (e.g., TCP, UDP, ICMP):

python
Copy code
protocol_name = {1: "ICMP", 6: "TCP", 17: "UDP"}.get(protocol, "Other")
Payload Extraction: Extracts payload data for TCP, UDP, and ICMP packets using protocol-specific layers:

python
Copy code
if protocol_name == "TCP" and TCP in packet:
    print(f"Payload: {bytes(packet[TCP].payload)}")
Ethical Use
This tool is strictly intended for educational purposes. Unauthorized use of packet sniffing tools on networks you do not own or have explicit permission to analyze is illegal and unethical. Always ensure you have proper authorization before using this tool.
