from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
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
# Encrypt using CBC
# -------------------------
def encrypt_cbc():

    message = input("\nEnter message: ")

    key = get_key()

    # Create cipher object
    cipher = AES.new(key, AES.MODE_CBC)

    # Convert message to bytes
    data = message.encode()

    # Pad data
    padded_data = pad(data, AES.block_size)

    # Encrypt
    ciphertext = cipher.encrypt(padded_data)

    # Store IV + ciphertext
    encrypted_data = cipher.iv + ciphertext

    # Convert to readable text
    encoded_data = base64.b64encode(
        encrypted_data
    ).decode()

    print("\nEncrypted Message:")
    print(encoded_data)


# -------------------------
# Decrypt using CBC
# -------------------------
def decrypt_cbc():

    encoded_data = input(
        "\nEnter encrypted message: "
    )

    key = get_key()

    try:

        # Convert base64 to bytes
        encrypted_data = base64.b64decode(
            encoded_data
        )

        # Extract IV
        iv = encrypted_data[:16]

        # Extract ciphertext
        ciphertext = encrypted_data[16:]

        # Create cipher object
        cipher = AES.new(
            key,
            AES.MODE_CBC,
            iv=iv
        )

        # Decrypt
        decrypted_data = cipher.decrypt(
            ciphertext
        )

        # Remove padding
        plaintext = unpad(
            decrypted_data,
            AES.block_size
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

        print("\n===== AES CBC MODE =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        if choice == '1':
            encrypt_cbc()

        elif choice == '2':
            decrypt_cbc()

        elif choice == '3':
            break

        else:
            print("Invalid choice!")


main()