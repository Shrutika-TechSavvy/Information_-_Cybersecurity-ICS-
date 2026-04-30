from Crypto.Cipher import AES
from Crypto.Random import get_random__bytes

def encrypt_file(key, in_filename, out_filename):
    #Read file data
    with open(in_filename , 'rb') as f :
        data = f.read()
        #Create AES cipher object
        cipher = AES.new(key, AES.MODE_GCM)
        #Encrypt data
        ciphertext , tag = cipher.encrypt_and_digest(data)
    
