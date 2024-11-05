import scapy.all as scp

# Implement your ICMP sender here
packet = scp.IP(dst="receiver",ttl=1)/scp.ICMP()
scp.send(packet)






