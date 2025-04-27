def caesar_cipher(text, shift, mode='encrypt'):
    """
    Implement the Caesar cipher for encryption or decryption.
    
    Parameters:
    text (str): The input text to process
    shift (int): The number of positions to shift each character
    mode (str): 'encrypt' or 'decrypt' (default is 'encrypt')
    
    Returns:
    str: The processed text
    """
    result = []
    
    # If decrypting, reverse the shift
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isupper():
            # Shift uppercase characters
            result.append(chr((ord(char) + shift - 65) % 26 + 65))
        elif char.islower():
            # Shift lowercase characters
            result.append(chr((ord(char) + shift - 97) % 26 + 97))
        else:
            # Leave other characters unchanged
            result.append(char)
    
    return ''.join(result)

# Example usage
if __name__ == "__main__":
    print("Caesar Cipher Program")
    print("---------------------")
    
    while True:
        print("\nOptions:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            encrypted = caesar_cipher(text, shift, 'encrypt')
            print(f"Encrypted text: {encrypted}")
        elif choice == '2':
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            decrypted = caesar_cipher(text, shift, 'decrypt')
            print(f"Decrypted text: {decrypted}")
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")