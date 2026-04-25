import math

# Convert text → numbers (A=0 ... Z=25)
def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text]


# Convert numbers → text
def numbers_to_text(numbers):
    return "".join(chr(n + ord('A')) for n in numbers)


# Build square key matrix from user input
def build_key_matrix(key_text):
    key_text = key_text.upper().replace(" ", "")
    nums = text_to_numbers(key_text)

    # find size of square matrix
    n = math.ceil(math.sqrt(len(nums)))

    # pad with 'X' if needed
    while len(nums) < n*n:
        nums.append(ord('X') - ord('A'))

    # take exactly n*n elements
    nums = nums[:n*n]

    # convert into matrix
    key_matrix = []
    for i in range(0, n*n, n):
        key_matrix.append(nums[i:i+n])

    return key_matrix


# Convert plaintext → matrix (rows of size n)
def build_plain_matrix(text, n):
    text = text.upper().replace(" ", "")
    nums = text_to_numbers(text)

    # pad so length is multiple of n
    while len(nums) % n != 0:
        nums.append(ord('X') - ord('A'))

    matrix = []
    for i in range(0, len(nums), n):
        matrix.append(nums[i:i+n])

    return matrix


# Matrix multiplication (mod 26)
def multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0]*cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 26

    return result


# Convert matrix → text
def matrix_to_text(matrix):
    nums = []
    for row in matrix:
        nums.extend(row)
    return numbers_to_text(nums)


# ---------------- MAIN ----------------

plaintext = input("Enter plaintext: ")
key_text = input("Enter key: ")

# Step 1: build key matrix
K = build_key_matrix(key_text)
n = len(K)

print("\nKey Matrix:")
for row in K:
    print(row)

# Step 2: build plaintext matrix
P = build_plain_matrix(plaintext, n)

print("\nPlaintext Matrix:")
for row in P:
    print(row)

# Step 3: multiply P × K
C = multiply(P, K)

print("\nCipher Matrix:")
for row in C:
    print(row)

# Step 4: convert to text
ciphertext = matrix_to_text(C)

print("\nCiphertext:", ciphertext)