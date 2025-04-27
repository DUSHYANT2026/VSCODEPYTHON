from PIL import Image
import numpy as np

def text_to_binary(text):
    return ''.join(format(ord(i), '08b') for i in text)

def binary_to_text(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

def encode_lsb(image_path, secret_text, output_path):
    img = Image.open(image_path)
    pixels = np.array(img)
    
    binary_text = text_to_binary(secret_text + "|||||")  # Add delimiter
    text_index = 0
    
    for row in range(pixels.shape[0]):
        for col in range(pixels.shape[1]):
            for color in range(3):  # RGB channels
                if text_index < len(binary_text):
                    pixels[row][col][color] = (pixels[row][col][color] & 0xFE) | int(binary_text[text_index])
                    text_index += 1
    
    Image.fromarray(pixels).save(output_path)
    return output_path

def decode_lsb(image_path):
    img = Image.open(image_path)
    pixels = np.array(img)
    binary_text = ""
    
    for row in range(pixels.shape[0]):
        for col in range(pixels.shape[1]):
            for color in range(3):
                binary_text += str(pixels[row][col][color] & 1)
    
    # Find the delimiter
    delimiter_index = binary_text.find("00111101011111000111110011111000111110")  # Binary for "|||||"
    if delimiter_index != -1:
        return binary_to_text(binary_text[:delimiter_index])
    return ""

# Example usage
if __name__ == "__main__":
    # Encode
    encode_lsb("original.png", "This is a secret message!", "encoded.png")
    # Decode
    secret = decode_lsb("encoded.png")
    print(f"Decoded message: {secret}")