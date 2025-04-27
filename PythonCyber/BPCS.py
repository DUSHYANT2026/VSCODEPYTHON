import numpy as np
from PIL import Image
import math

from LSB import binary_to_text, text_to_binary

def calculate_complexity(block):
    changes = 0
    for i in range(len(block)-1):
        for j in range(len(block[0])-1):
            if block[i][j] != block[i][j+1]:
                changes += 1
            if block[i][j] != block[i+1][j]:
                changes += 1
    max_changes = 2 * (len(block)-1) * (len(block[0])-1)
    return changes / max_changes if max_changes > 0 else 0

def bpcs_encode(image_path, secret_text, output_path, threshold=0.3):
    img = Image.open(image_path)
    pixels = np.array(img)
    binary_text = text_to_binary(secret_text + "|||||")
    text_index = 0
    
    block_size = 8
    for i in range(0, pixels.shape[0], block_size):
        for j in range(0, pixels.shape[1], block_size):
            for c in range(3):  # RGB channels
                block = pixels[i:i+block_size, j:j+block_size, c]
                if block.shape[0] == block_size and block.shape[1] == block_size:
                    complexity = calculate_complexity(block)
                    if complexity > threshold and text_index < len(binary_text):
                        # Embed data in LSB
                        for x in range(block_size):
                            for y in range(block_size):
                                if text_index < len(binary_text):
                                    pixels[i+x][j+y][c] = (pixels[i+x][j+y][c] & 0xFE) | int(binary_text[text_index])
                                    text_index += 1
    
    Image.fromarray(pixels).save(output_path)
    return output_path

def bpcs_decode(image_path, threshold=0.3):
    img = Image.open(image_path)
    pixels = np.array(img)
    binary_text = ""
    
    block_size = 8
    for i in range(0, pixels.shape[0], block_size):
        for j in range(0, pixels.shape[1], block_size):
            for c in range(3):
                block = pixels[i:i+block_size, j:j+block_size, c]
                if block.shape[0] == block_size and block.shape[1] == block_size:
                    complexity = calculate_complexity(block)
                    if complexity > threshold:
                        for x in range(block_size):
                            for y in range(block_size):
                                binary_text += str(pixels[i+x][j+y][c] & 1)
    
    delimiter_index = binary_text.find("00111101011111000111110011111000111110")
    if delimiter_index != -1:
        return binary_to_text(binary_text[:delimiter_index])
    return ""

# Example usage
if __name__ == "__main__":
    # Encode
    bpcs_encode("original.png", "BPCS secret message!", "bpcs_encoded.png")
    # Dec