from modules import cex128
import hashlib
import getpass
import platform
import os
import time

ext = ".cex"

path = os.path.realpath('')

if platform.system() == 'Windows': # Verify operational system
    os.system('cls')
else:
    os.system('clear')

print('[*] Setting up files...')

time.sleep(1)

try:
    if not os.path.isdir('data'):
        os.system('mkdir data')
    os.chdir('data')
    if not os.path.isdir('encrypted'):
        os.system('mkdir encrypted')
except:
    pass

confirm1 = getpass.getpass(prompt="[+] Create a password: ",stream="*")

confirm2 = getpass.getpass(prompt='[+] Confirm password: ', stream="*")

if confirm1 == confirm2:
    if len(confirm1) < 8:
        con = input('[!] Your password is not secure.\nAre you sure you wanna continue (y/N): ')
        if con.lower() != 'y':
            quit()
    passw = hashlib.md5(confirm1.encode()).hexdigest()
    time.sleep(0.5)

else:
    print("[-] Passwords dont match!")
    quit()

extension = input("[+] Extension for your encrypted files (ex: .secret): ")
if extension != "":
    if '.' not in extension:
        extension = '.'+ext
    ext = extension

print("\n[*] Writing config file...")

with open(path+"\\data\\config.dat","w+") as config:
    dat = "password=%s\nextension=%s"%(passw,ext)
    config.write(dat)
    config.close()
time.sleep(3)
print('\n[*] Creating hello_world')

time.sleep(2)

hw = 'hello_world'+ext

with open(path+"\\data\\encrypted\\"+hw, "w") as first:
    hello_world = cex128.cex128(passw).encrypt("hello world")
    first.write(hello_world)
    first.close()

print('[+] Cex successfuly configured!')