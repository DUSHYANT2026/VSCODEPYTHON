from Crypto.Cipher import DES3 # type: ignore
from Crypto.Util.Padding import pad # type: ignore
import time

class ANSIX931:
    def __init__(self, seed=None):
        self.key = b'8bytekey' + b'16bytekey1234'  # 24-byte key for 3DES
        if seed is None:
            seed = int(time.time())
        self.V = seed.to_bytes(8, 'big')  # 64-bit seed
        self.DT = bytes(8)  # 64-bit date/time
    
    def generate(self):
        cipher = DES3.new(self.key, DES3.MODE_ECB)
        # Update DT
        self.DT = (int.from_bytes(self.DT, 'big') + 1).to_bytes(8, 'big')
        # I = Encrypt(DT)
        I = cipher.encrypt(self.DT)
        # R = Encrypt(I XOR V)
        R_input = bytes([i ^ v for i, v in zip(I, self.V)])
        R = cipher.encrypt(R_input)
        # V = Encrypt(R XOR I)
        V_input = bytes([r ^ i for r, i in zip(R, I)])
        self.V = cipher.encrypt(V_input)
        return int.from_bytes(R, 'big')
    
    def random(self):
        return self.generate() / (2**64 - 1)

# Example usage
if __name__ == "__main__":
    rng = ANSIX931()
    
    print("10 random numbers from ANSI X9.31:")
    for _ in range(10):
        print(rng.random())