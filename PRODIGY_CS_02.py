from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    """Encrypts an image by modifying its pixel values."""
    try:
        # Open the image
        image = Image.open(input_path)
        image_array = np.array(image)
        
        # Encrypt by applying the key to each pixel
        encrypted_array = (image_array + key) % 256  # Ensure pixel values remain in [0, 255]
        encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
        
        # Save the encrypted image
        encrypted_image.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(input_path, output_path, key):
    """Decrypts an encrypted image using the same key."""
    try:
        # Open the encrypted image
        image = Image.open(input_path)
        image_array = np.array(image)
        
        # Decrypt by reversing the encryption process
        decrypted_array = (image_array - key) % 256  # Ensure pixel values remain in [0, 255]
        decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
        
        # Save the decrypted image
        decrypted_image.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Image Encryption Tool")
    print("=====================")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Choose an option (1/2): ").strip()
    
    if choice not in ['1', '2']:
        print("Invalid choice! Please select 1 or 2.")
        return
    
    input_path = input("Enter the path to the input image: ").strip()
    output_path = input("Enter the path to save the output image: ").strip()
    try:
        key = int(input("Enter a numeric key for encryption/decryption: ").strip())
    except ValueError:
        print("Invalid key! Please enter an integer.")
        return
    
    if choice == '1':
        encrypt_image(input_path, output_path, key)
    else:
        decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
