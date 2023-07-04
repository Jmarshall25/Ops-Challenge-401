# !/usr/bin/env python3
# Script: OPS 401 Class 02 Ops Challenge Solution
# Author: Jordan Marshall 
# Purpose: Ops Challenge:  Web Application Fingerprinting
# Attributes to Ademola

# Main

import subprocess

def main():
    target = input("Please enter a URL or IP address: ")
    port = input("Please enter a port number: ")

    print("\n[+] Performing banner grabbing with netcat...")
    netcat = subprocess.run(["nc", "-v", "-n", "-w2", target, port], capture_output=True, text=True)
    print(netcat.stdout)

    print("\n[+] Performing banner grabbing with telnet...")
    telnet = subprocess.run(["telnet", target, port], capture_output=True, text=True)
    print(telnet.stdout)

    print("\n[+] Performing banner grabbing with nmap on all well-known ports...")
    nmap = subprocess.run(["nmap", "-p-", "-sV", target], capture_output=True, text=True)
    print(nmap.stdout)

if __name__ == "__main__":
    main()
# End
