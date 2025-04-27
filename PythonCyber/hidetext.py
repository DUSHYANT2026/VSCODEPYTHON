from PIL import Image
import numpy as np

from LSB import binary_to_text, text_to_binary

def hide_text_in_image(image_path, text, output_path):
    img = Image.open(image_path)
    pixels = np.array(img)
    
    # Add length prefix and delimiter
    text_with_metadata = f"{len(text):04d}{text}"
    binary_data = text_to_binary(text_with_metadata)
    
    data_index = 0
    for row in pixels:
        for pixel in row:
            for i in range(3):  # R, G, B
                if data_index < len(binary_data):
                    pixel[i] = (pixel[i] & 0xFE) | int(binary_data[data_index])
                    data_index += 1
    
    Image.fromarray(pixels).save(output_path)
    return output_path

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    pixels = np.array(img)
    
    binary_data = ""
    for row in pixels:
        for pixel in row:
            for i in range(3):
                binary_data += str(pixel[i] & 1)
    
    # Extract length prefix
    length = int(binary_data[:32], 2)  # First 32 bits (4 bytes) for length
    text_binary = binary_data[32:32+length*8]
    
    return binary_to_text(text_binary)

# Example usage
if __name__ == "__main__":
    # Hide text
    hide_text_in_image("original.png", "This is hidden in the image!", "text_in_image.png")
    # Extract text
    secret = extract_text_from_image("text_in_image.png")
    print(f"Extracted text: {secret}")