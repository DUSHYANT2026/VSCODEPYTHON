def autokey_cipher(text, key, mode='encrypt'):
    result = []
    key = key.lower()
    key_sequence = list(key)
    
    if mode == 'encrypt':
        key_sequence += [c.lower() for c in text if c.isalpha()]
    else:  # For decrypt, we'll build the key as we go
        pass  # Placeholder for the else block logic
    
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = ord(key_sequence[key_index]) - ord('a')
            if mode == 'decrypt':
                shift = -shift
                # For decryption, we need to add the decrypted char to key sequence
                decrypted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
                key_sequence.append(decrypted_char)
            
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
    text = "ATTACK AT DAWN"
    key = "QUEENLY"
    
    encrypted = autokey_cipher(text, key)
    decrypted = autokey_cipher(encrypted, key, 'decrypt')
    
    print(f"Original:  {text}")
    print(f"Key:       {key}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")