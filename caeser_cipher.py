#The program implementing the Caeser Cipher cryptography algorithm , asymmetric
def normalize_shift(shift):
    if not isinstance(shift, int):
        raise TypeError("Shift must be integer !!!!");
    return shift % 26     #handles negative & large shifts

def caeser_cipher_encrypt(text, shift_value):
    if not isinstance(text, str):
        raise TypeError ("Text must be string")
    shift_value = normalize_shift(shift_value)
       

    result =[]
    for char in text:
        if char.isupper():
            result.append( chr((ord(char) -65 + shift_value) % 26 + 65))
        elif char.islower():
            result.append( chr((ord(char) -97 + shift_value) % 26 + 97))
        else :
            result.append(char)
    return "".join(result)    #list + join is used for faster memory usage

def caeser_cipher_decrypt (text, shift_value):
    shift_value = normalize_shift(shift_value)
    return caeser_cipher(text, - shift_value)

#Example
text = "Hello World !!!!!"
encrypted = caeser_cipher_encrypt(text, 3)
decrypted = caeser_cipher_decrypt(text, 3)
print("The Text to be encrypted : ")
print(text)

