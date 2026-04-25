# Hill Cipher (General n x n)

import numpy as np

# Function to clean text
def clean_text(text):
    return ''.join([c for c in text.upper() if c.isalpha()])


# Convert text to numbers (A=0 ... Z=25)
def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text]


# Convert numbers back to text
def numbers_to_text(nums):
    return ''.join(chr(int(n) + ord('A')) for n in nums)


# Function to take matrix input from user
def get_key_matrix(n):
    print(f"Enter {n*n} values for {n}x{n} key matrix:")
    values = []
    for i in range(n*n):
        values.append(int(input()))
    
    matrix = np.array(values).reshape(n, n)
    return matrix


# Function to find modular inverse of number
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


# Function to find inverse of matrix mod 26
def matrix_mod_inverse(matrix, mod):
    det = int(round(np.linalg.det(matrix)))
    det = det % mod

    inv_det = mod_inverse(det, mod)
    if inv_det is None:
        print("Matrix is not invertible")
        return None

    # Find adjoint matrix
    adj = np.round(det * np.linalg.inv(matrix)).astype(int)
    
    # Apply mod and multiply with inverse determinant
    inv_matrix = (inv_det * adj) % mod
    return inv_matrix


# Encryption function
def encrypt(text, key_matrix):
    text = clean_text(text)
    n = key_matrix.shape[0]

    # padding if needed
    while len(text) % n != 0:
        text += 'X'

    cipher = ""

    for i in range(0, len(text), n):
        block = text[i:i+n]
        vector = np.array(text_to_numbers(block)).reshape(n, 1)

        # matrix multiplication
        result = np.dot(key_matrix, vector) % 26

        cipher += numbers_to_text(result.flatten())

    return cipher


# Decryption function
def decrypt(cipher, key_matrix):
    n = key_matrix.shape[0]

    inv_matrix = matrix_mod_inverse(key_matrix, 26)
    if inv_matrix is None:
        return ""

    text = ""

    for i in range(0, len(cipher), n):
        block = cipher[i:i+n]
        vector = np.array(text_to_numbers(block)).reshape(n, 1)

        result = np.dot(inv_matrix, vector) % 26

        text += numbers_to_text(result.flatten())

    return text


# Main program
if __name__ == "__main__":
    print("Hill Cipher (General n x n)")

    text = input("Enter plaintext: ")
    n = int(input("Enter size of key matrix (e.g. 2 or 3 or 4): "))

    key_matrix = get_key_matrix(n)

    print("\nKey Matrix:")
    print(key_matrix)

    encrypted = encrypt(text, key_matrix)
    print("\nEncrypted Text:", encrypted)

    decrypted = decrypt(encrypted, key_matrix)
    print("Decrypted Text:", decrypted)