from math import gcd
from sympy import isprime


# -------------------------------
# VALIDATION
# -------------------------------

def get_positive_int(prompt):
    while True:
        val = input(prompt)

        if not val.isdigit():
            print("Enter valid positive integer.")
            continue

        val = int(val)

        if val <= 0:
            print("Number must be positive.")
            continue

        return val


# -------------------------------
# EXTENDED EUCLIDEAN
# -------------------------------

# def extended_gcd(a, b):
#     x0, x1 = 1, 0
#     y0, y1 = 0, 1

#     while b != 0:
#         q = a // b

#         a, b = b, a % b

#         x0, x1 = x1, x0 - q * x1
#         y0, y1 = y1, y0 - q * y1

#     return a, x0, y0

def mod_inverse(e, phi):

    n = phi
    b = e

    t1 = 0
    t2 = 1

    while b > 0:

        q = n // b
        r = n % b

        t3 = t1 - q * t2

        t1 = t2
        t2 = t3

        n = b
        b = r

    if n != 1:
        return None

    if t1 < 0:
        t1 += phi

    return t1
# ------------------------------- 
# KEY GENERATION
# -------------------------------

def generate_keys():

    while True:

        p = get_positive_int("Enter prime p: ")

        if not isprime(p):
            print("p is not prime.")
            continue

        q = get_positive_int("Enter prime q: ")

        if not isprime(q):
            print("q is not prime.")
            continue

        if p == q:
            print("p and q must be different.")
            continue

        break

    n = p * q
    phi = (p - 1) * (q - 1)

    while True:

        e = get_positive_int("Enter e: ")

        if e <= 1 or e >= phi:
            print("e must satisfy 1 < e < phi")
            continue

        if gcd(e, phi) != 1:
            print("gcd(e, phi) must be 1")
            continue

        break

    d = mod_inverse(e, phi)

    print("\nPublic Key:", (e, n))
    print("Private Key:", (d, n))

    return e, d, n


# -------------------------------
# ENCRYPTION
# -------------------------------

def encrypt(e, n):

    msg = input("Enter message: ")

    cipher = [pow(ord(c), e, n) for c in msg]

    print("Encrypted:", cipher)

    return cipher


# -------------------------------
# DECRYPTION
# -------------------------------

def decrypt(d, n):

    try:
        cipher = list(map(int, input(
            "Enter cipher values: ").split()))

    except:
        print("Invalid input")
        return

    message = ''.join(chr(pow(c, d, n)) for c in cipher)

    print("Decrypted Message:", message)


# -------------------------------
# MAIN MENU
# -------------------------------

def main():

    e = d = n = None

    while True:

        print("\n1.Generate Keys")
        print("2.Encrypt")
        print("3.Decrypt")
        print("4.Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            e, d, n = generate_keys()

        elif choice == '2':

            if e is None:
                print("Generate keys first!")
            else:
                encrypt(e, n)

        elif choice == '3':

            if d is None:
                print("Generate keys first!")
            else:
                decrypt(d, n)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice")


main()