from pycipher import Caesar
#Encryption function
def encrypt(text, key) : 
    cipher = Caesar(key)
    return cipher.encipher(text)

def decrypt(text, key):
    cipher = Caesar(key)
    return cipher.decipher(text)

if __name__ == "__main__":
    print("Welcome to the Caeser Cipher CLI!")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    text = input("Enter the text: ")
    key = int(input("Enter the key (number of positions to shift): "))

    if choice == 'E':
        result = encrypt(text, key)
        print(f"Encrypted text: {result}")
    elif choice == 'D':
        result = decrypt(text, key)
        print(f"Decrypted text: {result}")
    else:
        print("Invalid choice! Please select either E or D.")