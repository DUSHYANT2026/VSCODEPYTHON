from Crypto.Cipher import DES # type: ignore
from Crypto.Util.Padding import pad, unpad # type: ignore
import base64

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)
    encrypted = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted).decode()

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(ciphertext))
    return unpad(decrypted, DES.block_size).decode()

# Example usage
if __name__ == "__main__":
    key = b'8bytekey'  # DES requires 8 byte key
    plaintext = "Secret message"
    
    encrypted = des_encrypt(plaintext, key)
    decrypted = des_decrypt(encrypted, key)
    
    print(f"Original:  {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")