from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

# Function to analyze and display packet information
def analyze_packet(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        # Protocol name mapping
        protocol_name = {1: "ICMP", 6: "TCP", 17: "UDP"}.get(proto, "Other")

        print(f"\nPacket Captured:")
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol_name}")

        # Check for specific protocol layers
        if proto == 6 and TCP in packet:  # TCP
            tcp_layer = packet[TCP]
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
        elif proto == 17 and UDP in packet:  # UDP
            udp_layer = packet[UDP]
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")
        elif proto == 1 and ICMP in packet:  # ICMP
            print("ICMP Packet Detected")

        # Print payload if available
        if packet.payload:
            print(f"Payload: {bytes(packet.payload).decode('utf-8', errors='replace')}")

# Main function to capture packets
def start_sniffer():
    print("Starting packet sniffer. Press Ctrl+C to stop.")
    try:
        sniff(prn=analyze_packet, store=False)
    except KeyboardInterrupt:
        print("\nSniffer stopped.")

if __name__ == "__main__":
    start_sniffer()