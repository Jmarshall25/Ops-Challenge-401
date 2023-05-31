#!/usr/bin/env python3

# Script: Ops 401 Class 31 Part 1/3
# Author: Jordan Marshall
# Date of latest revision: 30Msy2023
# Purpose: Malware  Detection
# Help from class demo and ChatGPT
# When checked in ChatGPT it said that os.popen was deprecated and to use subprocess instead but I want to get a little bit more understanding with using that. From the class example I got os.popen. 

# Import Libraries
 from sys import platform
 import os, time

# Linux Function
def LinuxSearch():
    SelectFile = input("Which file are you looking for? ")
    WhichDirectory = input("Which directory do you want to search? ")
    # Count files searched
    os.system("ls " + str(WhichDirectory) + " | echo \"Searched $(wc -l) files.\"")
    # Count files found
    os.system("find " + str(WhichDirectory) + ' -name ' + str(SelectFile) + "  -print | echo \"Found $(grep -c /) files that matched:\"")
    print("")
    os.system("find " + str(WhichDirectory) + ' -name ' + str(SelectFile))
    print("")
    
# Windows Function
def WindowsSearch():
    SelectFile = input("Which file are you looking for? ")
    WhichDirectory = input("Which directory do you want to search? ")
    # Count files searched
    Search = os.popen("dir /a:-d /s /b " + str(WhichDirectory) + " | find /c \"\\\"").read()
    print("Files searched: " + Search)
    # Count files found
    Found = os.popen("dir /b/s " + str(WhichDirectory) + "\\" + str(SelectFile) +. " | find /c \"\\\"").read()
    print("Files found: " + Found)
    os.system("dir /b/s " + str(WhichDirectory) + "\\" + str(SelectFile))

# Main 

# Select Function
if platform == "linux" or platform == "linux2":
    print("This is a Linux machine.")
    LinuxSearch()
elif platform == "win10":
  print("This is a Windows machine.")
  WindowsSearch()
  
# End


  
