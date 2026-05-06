def clean_text(text):
    # Converts text to uppercase and removes non-alphabetic characters
    return ''.join(char for char in text.upper() if char.isalpha())


def encrypt(text, key):
    result = ""
    base = ord('A')

    for char in text:
        # Convert character to number
        x = ord(char) - base

        # Apply shift
        shifted = (x + key) % 26

        # Convert back to character
        result += chr(shifted + base)

    return result


def decrypt(text, key):
    result = ""
    base = ord('A')

    for char in text:
        # Convert character to number
        x = ord(char) - base

        # Apply reverse shift
        shifted = (x - key) % 26

        # Convert back to character
        result += chr(shifted + base)

    return result


def get_valid_text():
    while True:
        text = input("Enter text: ")

        # Check if input contains only alphabets and spaces
        if any(char.isalpha() for char in text):
            return clean_text(text)
        else:
            print("Invalid input! Please enter alphabetic text only.")


def get_valid_key():
    while True:
        try:
            key = int(input("Enter shift key: "))
            return key
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():

    while True:
        print("\n===== Caesar Cipher Menu =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            text = get_valid_text()
            key = get_valid_key()

            encrypted = encrypt(text, key)

            print("Encrypted Text:", encrypted)

        elif choice == '2':
            text = get_valid_text()
            key = get_valid_key()

            decrypted = decrypt(text, key)

            print("Decrypted Text:", decrypted)

        elif choice == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()