# RSA with:
# 1. Prime checking
# 2. GCD
# 3. Extended Euclidean Algorithm (for d)
# 4. Fast Modular Exponentiation

# -------------------------------
# Check if number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# -------------------------------
# GCD using Euclidean Algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# -------------------------------
# Extended Euclidean Algorithm
# returns gcd, x, y such that: ax + by = gcd
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd_val, x, y


# -------------------------------
# Modular inverse using Extended Euclid
def mod_inverse(e, phi):
    gcd_val, x, y = extended_gcd(e, phi)
    if gcd_val != 1:
        return None
    return x % phi   # make positive


# -------------------------------
# Fast Modular Exponentiation
# (base^exp) % mod efficiently
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:          # if exponent is odd
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2

    return result


# -------------------------------
# INPUT SECTION

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

if not is_prime(p) or not is_prime(q):
    print("Invalid! Both must be prime.")
    exit()

n = p * q
phi = (p - 1) * (q - 1)

e = int(input("Enter e (coprime with phi): "))

if gcd(e, phi) != 1:
    print("Invalid e! Not coprime.")
    exit()

# Find d using Extended Euclidean
d = mod_inverse(e, phi)

print("\nPublic Key:", (e, n))
print("Private Key:", (d, n))


# -------------------------------
# Encryption
def encrypt(message, e, n):
    return [mod_exp(ord(char), e, n) for char in message]


# Decryption
def decrypt(cipher, d, n):
    return ''.join([chr(mod_exp(num, d, n)) for num in cipher])


# -------------------------------
# MESSAGE

msg = input("\nEnter message: ")

cipher = encrypt(msg, e, n)
print("Encrypted:", cipher)

plain = decrypt(cipher, d, n)
print("Decrypted:", plain)