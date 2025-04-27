def vigenere_cipher(text, key, mode='encrypt'):
    result = []
    key = key.lower()
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            if mode == 'decrypt':
                shift = -shift
            
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            result.append(new_char)
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

# Example usage
if __name__ == "__main__":
    text = "ATTACKATDAWN"
    key = "LEMON"
    
    encrypted = vigenere_cipher(text, key)
    decrypted = vigenere_cipher(encrypted, key, 'decrypt')
    
    print(f"Original:  {text}")
    print(f"Key:       {key}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")