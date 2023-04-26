#!/usr/bin/env python3

# Script: Ops 401 Class 1 Solution
# Author: Jordan Marshall
# Date of latest revision: 18Apr23
# Purpose: Uptime Sensor

# Main

# Import Libraries
import os, time, datetime

# Perform ping
target = "8.8.8.8"
response = os.system("ping -c 1" + target)

# Check Host Status 
if response == 0:
    print("Network is up")
else:
    print("Network Error")
    
# Wait Three Seconds
time.sleep(3)

# End
