def clean_text(text):
    #Converts text to uppercase and removes the non-alphabetic characters
    return ''.join(char for char in text.upper() if char.isalpha())    

def encrypt(text, key):
    result = ""
    base = ord('A')
    for char in text :
        #Convert characters to numbers 
        x = ord(char) - base
        #Applying the shift with modulo 26
        shifted  = ( x + key ) % 26
        #Convert back to characters
        result += chr(shifted + ord('A'))
    return result
    
def decrypt(text, key):
    result = ""
    base = ord('A')
    for char in text :
        #Convert characters to numbers 
        x = ord(char) - base
        #Applying the reverse shift with modulo 26
        shifted  = ( x - key ) % 26
        #Convert back to characters
        result += chr(shifted + ord('A'))
    return result
        
def main():
    print("Caesar Cipher")
    text = input("Enter text: ")
    key = int(input("Enter shift key: "))

    # Clean the input
    text = clean_text(text)

    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)

    print("\nEncrypted:", encrypted)
    print("Decrypted:", decrypted)
    
if __name__ == "__main__" : 
    main()