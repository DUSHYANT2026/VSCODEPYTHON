def rc4(key, plaintext):
    # Key-scheduling algorithm (KSA)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    # Pseudo-random generation algorithm (PRGA)
    i = j = 0
    ciphertext = []
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        ciphertext.append(char ^ k)
    
    return bytes(ciphertext)

# Example usage
if __name__ == "__main__":
    key = b'SecretKey'
    plaintext = b'Message to encrypt'
    
    encrypted = rc4(key, plaintext)
    decrypted = rc4(key, encrypted)
    
    print(f"Original:  {plaintext}")
    print(f"Key:       {key.decode()}")
    print(f"Encrypted: {encrypted.hex()}")
    print(f"Decrypted: {decrypted.decode()}")