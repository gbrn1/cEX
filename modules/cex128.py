import base64
import hashlib
import binascii
from modules import caeser

class cex128:
    def __init__(self, passwd):
        self.password = passwd

    def encrypt(self, text):
        psswd = self.password
        sum_ = 0
        for char in psswd:
            sum_ += ord(char)
        salt = base64.b64encode(psswd.encode())
        caeserc = caeser.caeser(sum_)
        text = caeserc.enc(text)[::-1]
        encoded = b""
        for c in text:  
            encoded += base64.b64encode(c.encode()) + salt
        encoded = binascii.hexlify(base64.b64encode(encoded))
        return encoded.decode()

    def decrypt(self, encrypted):
        psswd = self.password
        sum_ = 0
        for char in psswd:
            sum_ += ord(char)
        salt = base64.b64encode(psswd.encode())
        caeserc = caeser.caeser(sum_)
        text1 = base64.b64decode(binascii.unhexlify(encrypted))
        chrs = text1.split(salt)
        text2 = ""
        for c in chrs:
            text2 += base64.b64decode(c).decode()
        decoded = caeserc.dec(text2[::-1])
        return decoded
