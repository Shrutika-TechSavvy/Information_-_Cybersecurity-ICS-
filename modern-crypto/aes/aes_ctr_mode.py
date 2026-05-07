from Crypto.Cipher import AES
import base64


# -------------------------
# Get AES Key From User
# -------------------------
def get_key():

    while True:

        user_key = input(
            "Enter AES key (16 / 24 / 32 characters): "
        )

        key = user_key.encode()

        # Valid AES key lengths
        if len(key) in [16, 24, 32]:
            return key

        else:
            print("\nInvalid key length!")
            print("Key must be 16, 24, or 32 characters.\n")


# -------------------------
# Encrypt Message
# -------------------------
def encrypt_message():

    # User enters message
    message = input("\nEnter message to encrypt: ")

    # User enters key
    key = get_key()

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CTR)

    # Convert message to bytes
    data = message.encode()

    # Encrypt message
    ciphertext = cipher.encrypt(data)

    # Store nonce + ciphertext
    encrypted_data = cipher.nonce + ciphertext

    # Convert bytes to readable text
    encoded_data = base64.b64encode(
        encrypted_data
    ).decode()

    print("\nEncrypted Message:")
    print(encoded_data)


# -------------------------
# Decrypt Message
# -------------------------
def decrypt_message():

    # User enters encrypted text
    encoded_data = input(
        "\nEnter encrypted message: "
    )

    # User enters key
    key = get_key()

    try:

        # Convert base64 string to bytes
        encrypted_data = base64.b64decode(
            encoded_data
        )

        # Extract nonce
        nonce = encrypted_data[:8]

        # Extract ciphertext
        ciphertext = encrypted_data[8:]

        # Create AES cipher object
        cipher = AES.new(
            key,
            AES.MODE_CTR,
            nonce=nonce
        )

        # Decrypt ciphertext
        decrypted_data = cipher.decrypt(
            ciphertext
        )

        print("\nDecrypted Message:")
        print(decrypted_data.decode())

    except:
        print("\nDecryption Failed!")
        print("Wrong key or invalid encrypted data.")


# -------------------------
# Main Menu
# -------------------------
def main():

    while True:

        print("\n===== AES CTR MODE =====")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        # Encrypt
        if choice == '1':
            encrypt_message()

        # Decrypt
        elif choice == '2':
            decrypt_message()

        # Exit
        elif choice == '3':

            print("\nExiting Program...")
            break

        else:
            print("\nInvalid Choice!")


# Run Program
main()