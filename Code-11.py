#!/usr/bin/env python3

# Jordan Marshall
# Port Scanner
# Attributes to demo code and Sierra Maldonado

# Utilize the scapy tool
from scapy.all import IP, sr1, TCP

# Define host Ip
IP_add = input("Please type in a IP address: ")
# define port range or specific set of ports to scan
port_range = [22, 23, 80, 443, 3389]
# IP address ' 45.33.32.156 ' - test IP
source_port = int(input("Enter source port number: "))

   
# Main
   
# Test each port in the specified range using for a loop
for dsp_port in port_range:
    response = sr1(IP(dst=IP_add)/TCP(sport=source_port, dport=dsp_port, flags="S"), timeout=1, verbose=0)
# If flag Ox12 received, send a RST packet. Se1()
    if (response.haslayer(TCP)):
        if (response.getlayer(TCP).flags == 0x12):
            answer = ("Open")
            print(f"Port {dsp_port} is {answer}")
            
    # If Ox14 received, notfiy if close
    elif (response.haslayer(TCP)):
        if (response.getlayer(TCP).flags == 0x14):
                answer = ("Closed")
                print(f"Port {dsp_port} is {answer}")
                
    # If no flag was received 
    else:
        answer = (f"No respose received from {IP_add}")
        print(f"Port {dsp_port} is {answer}")
        
# End
