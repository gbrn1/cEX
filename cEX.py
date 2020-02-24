#! python3
#! Version 0.2 by gbn1
#! https://github.com/gbrn1/cEX
from modules import cex128
from modules import banners
import os
import time
import getpass
import hashlib
import platform

class MAIN:
    def __init__(self):
        self.config_file = "config.dat"
        os.chdir("data")
    
    def clear(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def get_password(self):
        q = input("[*] Do you wanna use the configured password (Y/n): ")
        if q.lower() == "n":
            passw = hashlib.md5(getpass.getpass("Password: ").encode()).hexdigest()
        elif q.lower() == 'y' or q == "":
            with open(self.config_file,"r") as conf:
                text = conf.readlines()[0]
                passw = text.split('=')[1]
        else:
            quit
        return passw.replace("\n",'')

    def get_extension(self):
        with open(self.config_file,"r") as conf:
            text = conf.readlines()[1]
            ext = text.split('=')[1].replace('\n','')
        return ext

    def read_file(self, file_name):
        with open(file_name, 'r') as read:
            encrypted = read.read()
            passw = self.get_password()
            text = cex128.cex128(passw).decrypt(encrypted)
            print(text)
            print()

    def encrypt_file(self, file_name):
        with open(file_name, "r") as raw_file:
            passw = self.get_password()
            ext = self.get_extension()
            encrypted_text = cex128.cex128(passw).encrypt(raw_file.read())
            enc_name = "encrypted/" + os.path.realpath(file_name).split("\\")[-1].split(".")[0] + ext
            with open(enc_name, "w") as encrypted_file:
                encrypted_file.write(encrypted_text)
                print("[+] Writed encrypted file: %s\n"%enc_name)
                encrypted_file.close()
            raw_file.close()
        q = input("Do you wanna delete the uncrypted file (Y/n): ")
        if q.lower() == 'y':
            os.remove(file_name)
            print('[*] FIle removed!\n')

    def encrypt(self, text):
        passw = self.get_password()
        encrypted = cex128.cex128(passw).encrypt(text)
        print("Encrypted text: %s\n" %encrypted)

    def decrypt(self, text):
        passw = self.get_password()
        decrypted = cex128.cex128(passw).decrypt(text)
        print("Decrypted text: %s\n" %decrypted)
            

    def menu(self):
        self.clear()
        banners.banner()
        options = ["[1] Read encrypted file", "[2] Encrypt file", "[3] Encrypt text", "[4] Decrypt text", "\n[99] Exit"]
        while 1:
            for o in options:
                print(o)
            cmd = input("Choose a option: ")
            if cmd == "1":
                fn = input("File to read: ")
                if os.path.isfile(fn):
                    self.read_file(fn)
                else:
                    print("[-] File not found!")
            elif cmd == "2":
                fn = input("File to encrypt: ")
                if os.path.isfile(fn):
                    self.encrypt_file(fn)
                else:
                    print("[-] File not found!")
            elif cmd == "3":
                text = input("Text to encrypt: ")
                self.encrypt(text)
            elif cmd == "4":
                text = input("Text to decrypt: ")
                self.decrypt(text)
            elif cmd == "99":
                quit()
            else:
                print("Invalid option!")

m = MAIN()
m.menu()
