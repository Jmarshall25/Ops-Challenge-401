#!/usr/bin/env python3

# Script: Ops 401 Class 06 Part 1/3
# Author: Jordan Marshall
# Date of latest revision: 23Apr2023
# Purpose: Recursive Encryption and Decryption
# Help from class demo and ChatGPT; would like more help understanding later in remo 

# Main

from cryptography.fernet import Fernet
import os

def load_key():
    # Load the previously generated key, or generate a new one if one does not exist.
    try:
        return open("key.key", "rb").read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        return key

def encrypt_file(filename, key):
    # Encrypt a file using Fernet symmetric encryption.
    with open(filename, "rb") as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(filename, "wb") as f:
        f.write(encrypted)

def decrypt_file(filename, key):
    # Decrypt a file using Fernet symmetric encryption.
    with open(filename, "rb") as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    with open(filename, "wb") as f:
        f.write(decrypted)

def encrypt_message(message, key):
    # Encrypt a message using Fernet symmetric encryption.
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    print(encrypted.decode())

def decrypt_message(message, key):
    # Decrypt a message using Fernet symmetric encryption.
    fernet = Fernet(key)
    decrypted = fernet.decrypt(message.encode())
    print(decrypted.decode())

def encrypt_folder(folder_path, key):
    # Recursively encrypts a single folder and all its contents.
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            filename = os.path.join(root, file)
            encrypt_file(filename, key)

def decrypt_folder(folder_path, key):
    # Recursively decrypts a single folder that was encrypted by this tool.
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            filename = os.path.join(root, file)
            decrypt_file(filename, key)

# Load the encryption key
key = load_key()

# Prompt the user for the desired mode
mode = input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt a folder\n6. Decrypt a folder\n")

# Perform the selected mode
if mode == "1":
    # Encrypt a file
    filename = input("Enter the path to the file you want to encrypt: ")
    encrypt_file(filename, key)
    print("File encrypted.")
elif mode == "2":
    # Decrypt a file
    filename = input("Enter the path to the file you want to decrypt: ")
    decrypt_file(filename, key)
    print("File decrypted.")
elif mode == "3":
    # Encrypt a message
    message = input("Enter the message you want to encrypt: ")
    encrypt_message(message, key)
elif mode == "4":
    # Decrypt a message
    message = input("Enter the message you want to decrypt: ")
    decrypt_message(message, key)
elif mode == "5":
    # Encrypt a folder
    folder_path = input("Enter the path to the folder you want to encrypt: ")
    encrypt_folder(folder_path, key)
    print("Folder encrypted.")
elif mode == "6":
    # Decrypt a folder
    folder_path = input("Enter the path to the folder you want to decrypt: ")
    decrypt_folder(folder_path, key)
    print("Folder decrypted

      
# End
