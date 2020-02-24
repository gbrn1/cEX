class caeser:
    def __init__(self, shift):
        self.shift = shift

    def enc(self, plain):
        encoded = ""
        for c in plain:
	        encoded += chr(ord(c)+self.shift)
        return encoded

    def dec(self, encoded):
        plain = ""
        for c in encoded:
            plain += chr(ord(c)-self.shift)
        return plain
        
        
