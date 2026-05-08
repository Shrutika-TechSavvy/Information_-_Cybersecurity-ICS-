import math


# ---------------- HELPER FUNCTIONS ----------------

# Convert text to numbers
def text_to_numbers(text):
    return [ord(ch) - 65 for ch in text]


# Convert numbers to text
def numbers_to_text(nums):
    return "".join(chr(n + 65) for n in nums)


# Build key matrix
def build_key_matrix(key):
    key = key.upper().replace(" ", "")

    nums = text_to_numbers(key)

    # Find matrix size
    n = math.ceil(math.sqrt(len(nums)))

    # Padding with X
    while len(nums) < n * n:
        nums.append(23)   # X = 23

    # Create matrix
    matrix = []

    for i in range(0, n*n, n):
        matrix.append(nums[i:i+n])

    return matrix


# Build plaintext matrix
def build_plain_matrix(text, n):
    text = text.upper().replace(" ", "")

    nums = text_to_numbers(text)

    # Padding
    while len(nums) % n != 0:
        nums.append(23)

    matrix = []

    for i in range(0, len(nums), n):
        matrix.append(nums[i:i+n])

    return matrix


# Matrix multiplication
def multiply(P, K):

    result = []

    for row in P:
        new_row = []
        for col in range(len(K)):
            value = 0
            for k in range(len(K)):
                value += row[k] * K[k][col]
            new_row.append(value % 26)
        result.append(new_row)
    return result


# Convert matrix to text
def matrix_to_text(matrix):

    nums = []

    for row in matrix:
        nums.extend(row)

    return numbers_to_text(nums)


# Display matrix
def display_matrix(matrix):

    for row in matrix:
        print(row)


# ---------------- ENCRYPTION ----------------

def hill_cipher_encrypt():

    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")

    # Validations
    if not plaintext.isalpha():
        print("Plaintext should contain only alphabets")
        return

    if not key.isalpha():
        print("Key should contain only alphabets")
        return

    # Build matrices
    K = build_key_matrix(key)

    n = len(K)

    P = build_plain_matrix(plaintext, n)

    # Multiply
    C = multiply(P, K)

    # Convert to text
    ciphertext = matrix_to_text(C)

    # Output
    print("\nKey Matrix:")
    display_matrix(K)

    print("\nPlaintext Matrix:")
    display_matrix(P)

    print("\nCipher Matrix:")
    display_matrix(C)

    print("\nCiphertext:", ciphertext)


# ---------------- MENU ----------------

while True:

    print("\n===== HILL CIPHER MENU =====")
    print("1. Encrypt")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        hill_cipher_encrypt()

    elif choice == "2":
        print("Exiting...")
        break

    else:
        print("Invalid choice")