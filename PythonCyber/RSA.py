from Crypto.PublicKey import RSA # type: ignore
from Crypto.Cipher import PKCS1_OAEP # type: ignore
import base64

def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(message, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted = cipher.encrypt(message.encode())
    return base64.b64encode(encrypted).decode()

def rsa_decrypt(encrypted_message, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted.decode()

# Example usage
if __name__ == "__main__":
    private_key, public_key = generate_rsa_keys()
    message = "Secret RSA message"
    
    encrypted = rsa_encrypt(message, public_key)
    decrypted = rsa_decrypt(encrypted, private_key)
    
    print(f"Original:  {message}")
    print(f"Public Key:\n{public_key.decode()}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")