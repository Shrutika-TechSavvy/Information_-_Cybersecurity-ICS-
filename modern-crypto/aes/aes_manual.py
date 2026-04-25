from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

#key must be 16, 24 or 32 bytes
key = get_random_bytes(16)

#Data to encrypt
data = b"Hello, This is AES encryption"
#Create cipher object
cipher = AES.new(key, AES.MODE_CBC)

#Encrypt(with padding)
ciphertext = cipher.encrypt(pad(data, AES.block_size))

print("Cipher text :", ciphertext)

#Decrypt
cipher_dec = AES.new(key, AES.MODE_CBC, iv = cipher.iv)
plaintext = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)

print("Decrypted text :", plaintext)