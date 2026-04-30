from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# =============================
# 🔹 INPUT HANDLING
# =============================

def menu():
    print("\n=== AES Tool ===")
    print("1. Encrypt")
    print("2. Decrypt")
    return input("Choose option: ").strip()


def get_mode():
    mode = input("Enter mode (ECB/CBC/CTR/GCM): ").upper().strip()
    if mode not in ["ECB", "CBC", "CTR", "GCM"]:
        raise ValueError("Invalid mode selected")
    return mode


def get_key():
    key = input("Enter key (16/24/32 chars): ").encode()
    if len(key) not in [16, 24, 32]:
        raise ValueError("Invalid key length")
    return key


def get_plaintext():
    return input("Enter plaintext: ")


def get_encrypted_input(mode):
    data = {}

    if mode == "CBC":
        data["iv"] = input("IV: ")

    if mode in ["CTR", "GCM"]:
        data["nonce"] = input("Nonce: ")

    if mode == "GCM":
        data["tag"] = input("Tag: ")

    data["ciphertext"] = input("Ciphertext: ")
    return data


# =============================
# 🔹 DATA PROCESSING
# =============================

def clean_input(text):
    # You can extend this later (strip, normalize, etc.)
    return text.strip()


def to_bytes(text):
    return text.encode('utf-8')


def to_string(byte_data):
    return byte_data.decode('utf-8')


# =============================
# 🔹 ENCODING UTILITIES
# =============================

def encode_dict(data):
    return {k: base64.b64encode(v).decode() for k, v in data.items()}


def decode_dict(data):
    return {k: base64.b64decode(v) for k, v in data.items()}


# =============================
# 🔹 CRYPTO CORE
# =============================

def encrypt_ecb(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return {"ciphertext": cipher.encrypt(pad(data, 16))}


def encrypt_cbc(data, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return {
        "iv": iv,
        "ciphertext": cipher.encrypt(pad(data, 16))
    }


def encrypt_ctr(data, key):
    cipher = AES.new(key, AES.MODE_CTR)
    return {
        "nonce": cipher.nonce,
        "ciphertext": cipher.encrypt(data)
    }


def encrypt_gcm(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return {
        "nonce": cipher.nonce,
        "tag": tag,
        "ciphertext": ciphertext
    }


def decrypt_ecb(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(data["ciphertext"]), 16)


def decrypt_cbc(data, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=data["iv"])
    return unpad(cipher.decrypt(data["ciphertext"]), 16)


def decrypt_ctr(data, key):
    cipher = AES.new(key, AES.MODE_CTR, nonce=data["nonce"])
    return cipher.decrypt(data["ciphertext"])


def decrypt_gcm(data, key):
    cipher = AES.new(key, AES.MODE_GCM, nonce=data["nonce"])
    return cipher.decrypt_and_verify(data["ciphertext"], data["tag"])


# =============================
# 🔹 MODE DISPATCHER
# =============================

def encrypt_dispatch(data, key, mode):
    if mode == "ECB":
        return encrypt_ecb(data, key)
    elif mode == "CBC":
        return encrypt_cbc(data, key)
    elif mode == "CTR":
        return encrypt_ctr(data, key)
    elif mode == "GCM":
        return encrypt_gcm(data, key)


def decrypt_dispatch(data, key, mode):
    if mode == "ECB":
        return decrypt_ecb(data, key)
    elif mode == "CBC":
        return decrypt_cbc(data, key)
    elif mode == "CTR":
        return decrypt_ctr(data, key)
    elif mode == "GCM":
        return decrypt_gcm(data, key)


# =============================
# 🔹 WORKFLOWS
# =============================

def encryption_flow():
    mode = get_mode()
    key = get_key()
    text = clean_input(get_plaintext())

    data_bytes = to_bytes(text)
    encrypted = encrypt_dispatch(data_bytes, key, mode)
    encoded = encode_dict(encrypted)

    print("\n--- Encrypted Output ---")
    for k, v in encoded.items():
        print(f"{k}: {v}")


def decryption_flow():
    mode = get_mode()
    key = get_key()

    enc_input = get_encrypted_input(mode)
    decoded = decode_dict(enc_input)

    try:
        decrypted = decrypt_dispatch(decoded, key, mode)
        print("\nDecrypted:", to_string(decrypted))
    except Exception as e:
        print("Decryption failed:", str(e))


# =============================
# 🔹 MAIN
# =============================

def main():
    try:
        choice = menu()

        if choice == "1":
            encryption_flow()
        elif choice == "2":
            decryption_flow()
        else:
            print("Invalid option")

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()