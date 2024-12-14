def caesar_cipher(text, shift, mode):
    result = ""
    if mode.lower() == "decrypt":
        shift = -shift  # Reverse the shift for decryption
    
    for char in text:
        if char.isalpha():  # Only process alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            # Perform the shift
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            # Non-alphabetic characters are not changed
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    print("=====================")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
        return
    
    text = input("Enter the text: ").strip()
    try:
        shift = int(input("Enter the shift value: ").strip())
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return
    
    result = caesar_cipher(text, shift, mode)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
