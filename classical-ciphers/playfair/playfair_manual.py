import string
##1. Generate the key matrix

def generate_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix_list = []
    
    #Add key letters to the matrix
    for char in key :
        if char.isalpha() and char not in seen:
            seen.add(char)
            matrix_list.append(char)
    
    #Add remaining letters
    for char in string.ascii_uppercase:
        if char == 'J':
            continue
        if char not in seen:
            seen.add(char)
            matrix_list.append(char)
        
    #Converting into 5X5 matrix
    matrix = [matrix_list[i : i+5] for i in range(0, 25, 5)]
    return matrix

#Display the matrix[optional]
def print_matrix(matrix) :
    print("\n Key matrix : ")
    for row in matrix :
        print("".join(row))
        
#Preparing th plaintext
def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])
    
    i = 0
    result = ""
    
    while i < len(text):
        a = text[i]
        
        if i+1 < len(text):
            b = text[i+1]
            
            if(a == b):
                result += a + "X"
                i+=1
            else:
                result+=a + b
                i+=2
        else:
            result += a + "X"
            i+=1
    return result

#Finding the position in matrix
def find_position(matrix, char):
    return None


#Encrypting the pair of the string which we have prepared 
def encrypt_pair(matrix, a, b):
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)
    
    #Majorly we have three cases
    #1. sAme row --  > shift right
    if r1 == r2 :
        c1 = (c1 + 1) % 5
        c2 = (c2 + 1) % 5
        
        return matrix[r1][c1] + matrix[r2][c2]
    #2. same columen -- > shift down
    elif c1 == c2 :
        r1 = (r1 + 1) % 5
        r2 = (r2 + 1) % 5
        
        return matrix[r1][c1] + matrix[r2][c2]
    #Rectangle(box) -> swap the columns
    else:
        return matrix[r1][c2] + matrix[r2][c1]
        
#Now, Encrypting the full text
def encrypt(text, matrix):
    prepared = prepare_text(text)
    pairs= [prepared[i:i+2] for i in range(0, len(prepared) , 2)]
    cipher = ""
    
    for pair in pairs:
        cipher += encrypt_pair(matrix, pair[0] , pair[1])
    return cipher

if __name__ == "__main__":
    key = input("Enter key: ")
    plaintext = input("Enter plaintext: ")

    matrix = generate_matrix(key)
    print_matrix(matrix)

    prepared_text = prepare_text(plaintext)
    print("\nPrepared Text:", prepared_text)

    cipher_text = encrypt(plaintext, matrix)
    print("Cipher Text:", cipher_text)