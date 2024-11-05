import scapy.all as scp

#Implement your ICMP receiver here

scp.sniff(filter="icmp",prn = lambda x: x.show(),count = 1)




