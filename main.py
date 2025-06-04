from PIL import Image
import os

def create_test_image(filename="original.png"):
    """Create a simple 100x100 red image to work with."""
    img = Image.new("RGB", (100, 100), color=(255, 0, 0))
    img.save(filename)
    print(f"[+] Test image '{filename}' created.")

def encrypt_image(input_path, output_path, key):
    """Encrypt image by shifting RGB values."""
    if not os.path.isfile(input_path):
        print(f"[-] ERROR: Input file '{input_path}' not found.")
        return False
    
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save(output_path)
    print(f"[+] Image encrypted and saved to: {output_path}")
    return True

def decrypt_image(input_path, output_path, key):
    """Decrypt image by reversing RGB shift."""
    if not os.path.isfile(input_path):
        print(f"[-] ERROR: Input file '{input_path}' not found.")
        return False
    
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_path)
    print(f"[+] Image decrypted and saved to: {output_path}")
    return True

if __name__ == "__main__":
    original_image = "original.png"
    encrypted_image = "encrypted.png"
    decrypted_image = "decrypted.png"
    key = 50

    if not os.path.isfile(original_image):
        create_test_image(original_image)
    else:
        print(f"[i] Found existing image: {original_image}")

    if encrypt_image(original_image, encrypted_image, key):
        decrypt_image(encrypted_image, decrypted_image, key)
