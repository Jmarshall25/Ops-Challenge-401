#!/usr/bin/env python3

# Script: Ops 401 Class 1 Solution
# Author: Jordan Marshall
# Date of latest revision: 18Apr23
# Purpose: Uptime Sensor
# Help from class example

# Main

# Import Libraries
import smtplib
import datetime, time, os
from getpass import getpass

# Variables
up = "Network is active"
down = "Network is down"
last = 0
ping_result = 0
email = imput("Please provide your email address:")
password = getpass("Please provide your password:")
ip = input("Provide an IP address:")

# Function up alert

def send_upAlert():
    now = datetime.datetime.now()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email,password)
    message = "Your server is up"
    s.sendmail("alertsystem@bot.com, email, message)
    s.quit()
    
# Function down alert

def send_downAlert():
    now = datetime.datetime.now()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email,password)
    message = "Your server is down"
    s.sendmail("alertsystem@bot.com, email, message)
    s.quit()
    
# Ping test

def ping_test():

    if ((ping_result != last) and (ping_result == up)):
        last = up
        send_upAlert()
    elif ((ping_result != last) and (ping_result == down)):
        last = down
        send_downAlert()
        
    response = os.system("ping -c +! " + ip)
    if response == 0:
        ping_result = up
    else:
        ping_result = down
        
# Infinite loop

while True:
    ping_test()
    time.sleep(2)

# End
