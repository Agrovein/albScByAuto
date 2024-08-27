from scapy.all import sniff, IP
import gzip
import io

# Define the target IP address
TARGET_IP = "5.188.125.42"

# Function to process packets
def process_packet(packet):
    # Check if the packet has an IP layer and the source or destination IP matches the target
    if IP in packet:
        ip_layer = packet[IP]
        if ip_layer.src == TARGET_IP or ip_layer.dst == TARGET_IP:
            # Extract the payload
            payload = bytes(packet[IP].payload)
            
            print(f"Packet from {ip_layer.src} to {ip_layer.dst}")
            
            # Print raw payload
            print("Raw payload:")
            print(payload)
            
            # Attempt to decode as UTF-8
            try:
                utf8_payload = payload.decode('utf-8')
                print("UTF-8 decoded payload:")
                print(utf8_payload)
            except UnicodeDecodeError:
                print("Payload is not valid UTF-8")

            # Print hex dump
            print("Hex dump of payload:")
            print(payload.hex())
            
            # Attempt to decompress with gzip
            try:
                with gzip.open(io.BytesIO(payload), 'rb') as f:
                    decompressed_payload = f.read()
                    print("Gzip decompressed payload:")
                    print(decompressed_payload)
            except (OSError, IOError):
                print("Payload is not gzip compressed")
            
            print("-" * 40)

# Capture packets
print(f"Sniffing packets to/from {TARGET_IP}...")
sniff(filter=f"ip host {TARGET_IP}", prn=process_packet)
