from Crypto.Cipher import AES # type: ignore
from Crypto.Util.Padding import pad, unpad # type: ignore
from Crypto.Random import get_random_bytes # type: ignore
import base64

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_text = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    iv = cipher.iv
    return base64.b64encode(iv + ciphertext).decode()

def aes_decrypt(ciphertext, key):
    data = base64.b64decode(ciphertext)
    iv = data[:AES.block_size]
    ciphertext = data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    return unpad(decrypted, AES.block_size).decode()

# Example usage
if __name__ == "__main__":
    key = get_random_bytes(16)  # AES-128 (16 bytes), can also use 24 or 32 bytes
    plaintext = "Top secret message"
    
    encrypted = aes_encrypt(plaintext, key)
    decrypted = aes_decrypt(encrypted, key)
    
    print(f"Original:  {plaintext}")
    print(f"Key:       {key.hex()}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")