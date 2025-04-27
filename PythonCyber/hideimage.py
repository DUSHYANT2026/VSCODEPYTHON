from PIL import Image
import numpy as np

def hide_image_in_image(cover_path, secret_path, output_path, bits=2):
    cover = Image.open(cover_path)
    secret = Image.open(secret_path).resize(cover.size)
    
    cover_arr = np.array(cover)
    secret_arr = np.array(secret)
    
    # Clear lower bits in cover image
    cover_arr = (cover_arr >> bits) << bits
    
    # Take upper bits from secret image
    secret_bits = secret_arr >> (8 - bits)
    
    # Combine them
    stego_arr = cover_arr | secret_bits
    
    Image.fromarray(stego_arr).save(output_path)
    return output_path

def extract_image_from_image(stego_path, output_path, bits=2):
    stego = Image.open(stego_path)
    stego_arr = np.array(stego)
    
    # Extract the hidden bits and scale them up
    extracted_arr = (stego_arr & ((1 << bits) - 1)) << (8 - bits)
    
    Image.fromarray(extracted_arr).save(output_path)
    return output_path

# Example usage
if __name__ == "__main__":
    # Hide image
    hide_image_in_image("cover.png", "secret.png", "stego.png")
    # Extract image
    extract_image_from_image("stego.png", "extracted_secret.png")
    print("Image hidden and extracted successfully!")