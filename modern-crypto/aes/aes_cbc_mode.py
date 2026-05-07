from Crypto.Cipher import AES
import base64


# -------------------------
# Get AES Key
# -------------------------
def get_key():

    while True:

        user_key = input(
            "Enter AES key (16/24/32 chars): "
        )

        key = user_key.encode()

        if len(key) in [16, 24, 32]:
            return key

        else:
            print("Invalid key length!\n")


# -------------------------
# Encrypt using CTR
# -------------------------
def encrypt_ctr():

    message = input("\nEnter message: ")

    key = get_key()

    # Create cipher object
    cipher = AES.new(key, AES.MODE_CTR)

    # Convert to bytes
    data = message.encode()

    # Encrypt
    ciphertext = cipher.encrypt(data)

    # Store nonce + ciphertext
    encrypted_data = cipher.nonce + ciphertext

    # Convert to readable text
    encoded_data = base64.b64encode(
        encrypted_data
    ).decode()

    print("\nEncrypted Message:")
    print(encoded_data)


# -------------------------
# Decrypt using CTR
# -------------------------
def decrypt_ctr():

    encoded_data = input(
        "\nEnter encrypted message: "
    )

    key = get_key()

    try:

        # Convert base64 to bytes
        encrypted_data = base64.b64decode(
            encoded_data
        )

        # Extract nonce
        nonce = encrypted_data[:8]

        # Extract ciphertext
        ciphertext = encrypted_data[8:]

        # Create cipher object
        cipher = AES.new(
            key,
            AES.MODE_CTR,
            nonce=nonce
        )

        # Decrypt
        plaintext = cipher.decrypt(
            ciphertext
        )

        print("\nDecrypted Message:")
        print(plaintext.decode())

    except:
        print("\nDecryption Failed!")


# -------------------------
# Main Menu
# -------------------------
def main():

    while True:

        print("\n===== AES CTR MODE =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        if choice == '1':
            encrypt_ctr()

        elif choice == '2':
            decrypt_ctr()

        elif choice == '3':
            break

        else:
            print("Invalid choice!")


main()