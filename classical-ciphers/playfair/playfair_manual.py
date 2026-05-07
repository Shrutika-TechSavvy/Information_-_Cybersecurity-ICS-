''' 
Pseudocode
1. Create a 5x5 matrix , where two list are used  ie used and letters, first of all the key leteere are put in list ,while the j is replaced with the i and then the othre alphabets remainng are added in list, the the 5x5 matrix is generated 
2. Preparing the text, ie the string can be any type, full of double characters so prepare such that the even length string with no consecutive same characters, logic os to add filling letter X 
3. Findin the position of the character gien from entire matrix, O(n^2)
4. Encrypting tha pair function, where u have given one pair ir the characters, u have to encrypt this, by finding the position of each character then useing 3 cases , find the corresponding encrypting pairs and return the encrypted pais
5. Encrytpion function, where first the string is prepared and in loop the pairs are encryted and added to result string
6. Decrypting the pair function, where u have given one pair ir the characters, u have to decrypt this, by finding the position of each character then useing 3 cases , find the corresponding decrypting pairs and return the decrypted pais
7. Decrytpion function, where first the string is prepared and in loop the pairs are decrypted and added to result string
8. menu driven program, where user can choose to encrypt or decrypt the message, and then the corresponding function is called


'''
import string
import re

#Generate the 5 X 5 matrix
def generate_matrix(key):
    key = key.upper().replace("J", "I")
    used = []
    letters = []
    
    for ch in key :
        if ch not in used : 
            used.append(ch)
            letters.append(ch)
    
    for ch in string.ascii_uppercase:
        if ch not in used:
            if ch != 'J':
                used.append(ch)
                letters.append(ch)
    
    #Creating the 5 by 5 matrix
    matrix= []
    for i in range(0, 25, 5):
        matrix.append(letters[i:i+5])
    return matrix

def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = re.sub(r'[^A-Z]', '', text)
    i=0
    result =""
    while i < len(text):
        first = text[i]
        if i+1<len(text):
            second= text[i+1]
            if first == second :
                result+= first + 'X'
                i+=1
            else:
                result+=first+second
                i+=2
        else:
            result+= first + 'X'
            i+=1
    return result

                
            
def find_position(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    
def encrypt_pair(matrix, a, b):
    #Here we are going to encrypt the pairs
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)
    #Case 1
    if r1 == r2:
        return matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
    #Case 2
    elif c1 == c2:
        return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
    else:
        #case 3
        return matrix[r1][c2] + matrix[r2][c1]
    
def decrypt_pair(matrix, a, b):
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)
    #Case 1
    if r1 == r2:
        return matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
    #Case 2
    elif c1 == c2:
        return matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
    else:
        #case 3
        return matrix[r1][c2] + matrix[r2][c1]
def encrypt(matrix, text):
    result = ""
    prepared_text = prepare_text(text)
    for i in range(0, len(prepared_text), 2):
        a = prepared_text[i]
        b = prepared_text[i+1]
        encrypted_pair = encrypt_pair(matrix, a, b)
        result += encrypted_pair
    return result

def decrypt(matrix, text):

    result = ""

    text = text.upper().replace("J", "I")
    text = re.sub(r'[^A-Z]', '', text)

    for i in range(0, len(text), 2):

        a = text[i]
        b = text[i+1]

        decrypted_pair = decrypt_pair(matrix, a, b)

        result += decrypted_pair

    return result

def menu():
    while True:
        print("1. Encrypt:")
        print("2. Decrypt:")
        print("3. Exit:")
        ch = input("Enter your choice:")
        
        if ch == '1':
            key = input("Enter the key : ")
            matrix = generate_matrix(key)
            print("Genrated matrix : ")
            for row in matrix:
                print(row)
            text = input("Enter the text to encrypt : ")
            encrypted_text = encrypt(matrix, text)  
            print("Encrypted text : ", encrypted_text)
        elif ch == '2':
            key = input("Enter the key : ")
            matrix = generate_matrix(key)
            print("Genrated matrix : ")
            for row in matrix:
                print(row)
            text = input("Enter the text to decrypt : ")
            decrypted_text = decrypt(matrix, text)  
            print("Decrypted text : ", decrypted_text)
        
        elif ch == '3':
            print("Exiting the program...")
            break
        
if __name__ == "__main__":
    menu()