def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_message += new_char
        else:
            encrypted_message += char
    return encrypted_message

def caesar_cipher_decrypt(encrypted_message, shift):
    return caesar_cipher_encrypt(encrypted_message, -shift)

def main():
    print("Caesar Cipher")
    choice = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice! Please enter 'e' to encrypt or 'd' to decrypt.")
        return
    
    message = input("Enter the message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid shift value! Please enter an integer.")
        return

    if choice == 'e':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    else:
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
