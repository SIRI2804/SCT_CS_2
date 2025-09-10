from PIL import Image

# 🔐 Encrypt the image
def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)              # Open image
    pixels = img.load()                       # Access pixels
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]            # Get RGB values
            # Apply XOR with key to encrypt
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)                     # Save encrypted image
    print(f"✅ Image encrypted and saved as {output_path}")


# 🔓 Decrypt the image (same as encryption, XOR twice = original)
def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Apply XOR again with the same key
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"✅ Image decrypted and saved as {output_path}")


if __name__ == "__main__":
    # File paths
    input_file = r"C:\Users\siri2\PycharmProjects\SkillCraftTechnologyproject\OIP.jpeg"
    encrypted_file = r"C:\Users\siri2\PycharmProjects\SkillCraftTechnologyproject\encrypted.png"
    decrypted_file = r"C:\Users\siri2\PycharmProjects\SkillCraftTechnologyproject\decrypted.png"

    # Encryption key (can be any integer between 1 and 255)
    key = 123

    # Run encryption and decryption
    encrypt_image(input_file, encrypted_file, key)
    decrypt_image(encrypted_file, decrypted_file, key)
