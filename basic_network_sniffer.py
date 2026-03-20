from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def process_packet(packet):
    """
    Callback function that processes each captured packet.
    """
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        
        proto_name = "Other"
        if protocol == 6:
            proto_name = "TCP"
        elif protocol == 17:
            proto_name = "UDP"
        elif protocol == 1:
            proto_name = "ICMP"

        print(f"\n[+] Packet Captured:")
        print(f"    Source IP:      {src_ip}")
        print(f"    Destination IP: {dst_ip}")
        print(f"    Protocol:       {proto_name}")

        if Raw in packet:
            payload = packet[Raw].load
            # Print only the first 50 bytes to avoid flooding the console
            print(f"    Payload:        {payload[:50]}...")
        else:
            print(f"    Payload:        None")

print("Starting network sniffer... Press Ctrl+C to stop.")
print("Waiting for network traffic...")

try:
    sniff(filter="ip", prn=process_packet, store=False)
except KeyboardInterrupt:
    print("\nSniffing stopped.")

# Start sniffing. 
# filter="ip" ensures we only capture IP packets.
# prn specifies the function to run for each packet.
# store=False keeps RAM usage low by not saving packets in memory.