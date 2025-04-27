import random

def generate_key():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

def substitution_cipher(text, key, mode='encrypt'):
    result = []
    for char in text.lower():
        if char in key:
            if mode == 'encrypt':
                result.append(key[char])
            else:  # decrypt
                result.append([k for k, v in key.items() if v == char][0])
        else:
            result.append(char)
    return ''.join(result)

# Example usage
if __name__ == "__main__":
    key = generate_key()
    print("Substitution Key:", key)
    
    plaintext = "hello world"
    encrypted = substitution_cipher(plaintext, key)
    decrypted = substitution_cipher(encrypted, key, 'decrypt')
    
    print(f"Original:  {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")