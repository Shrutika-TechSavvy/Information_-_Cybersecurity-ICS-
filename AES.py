from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Key must be 16, 24, or 32 bytes long
key = get_random_bytes(16)

# -------- Encryption --------
def encrypt(plain_text):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return cipher.iv, ciphertext

# -------- Decryption --------
def decrypt(iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plain_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plain_text.decode()

# -------- Usage --------
message = "Hello AES Encryption!"

iv, encrypted = encrypt(message)
print("Encrypted:", encrypted)

decrypted = decrypt(iv, encrypted)
print("Decrypted:", decrypted)
