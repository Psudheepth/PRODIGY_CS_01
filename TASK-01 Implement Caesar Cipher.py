def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char) + shift_amount
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                encrypted_text += chr(char_code)
            elif char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                encrypted_text += chr(char_code)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def print_banner():
    print("=" * 50)
    print(" " * 15 + "Caesar Cipher")
    print("=" * 50)

def get_choice():
    print("\nChoose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    while True:
        choice = input("Enter your choice (1/2): ")
        if choice in ['1', '2']:
            return choice
        print("Invalid choice. Please enter '1' for encryption or '2' for decryption.")

def get_message():
    return input("Enter your message: ")

def get_shift():
    while True:
        try:
            shift = int(input("Enter the shift value (an integer from 1 to 25): "))
            if -10 <= shift <= 25:
                return shift
            else:
                print("Shift value must be between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the shift value.")

def main():
    print_banner()
    choice = get_choice()

    if choice == '1':
        print("\n--- Encryption ---")
    elif choice == '2':
        print("\n--- Decryption ---")

    message = get_message()
    shift = get_shift()
    
    if choice == '1':
        result = encrypt(message, shift)
        print("\nOriginal message: {}".format(message))
        print("Encrypted message: {}".format(result))
    elif choice == '2':
        result = decrypt(message, shift)
        print("\nEncrypted message: {}".format(message))
        print("Decrypted message: {}".format(result))
    
    print("=" * 50)

if __name__ == "__main__":
    main()
