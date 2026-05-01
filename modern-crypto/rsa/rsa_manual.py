# -------------------------------
# VALIDATION FUNCTIONS
# -------------------------------

def get_positive_int(prompt):
    while True:
        val = input(prompt)
        if not val.isdigit():
            print("❌ Enter a valid positive integer (no letters/decimals).")
            continue
        val = int(val)
        if val <= 0:
            print("❌ Number must be positive.")
            continue
        return val


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# -------------------------------
# GCD & EXTENDED EUCLIDEAN
# -------------------------------

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while b != 0:
        q = a // b
        a, b = b, a % b

        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return a, x0, y0


def mod_inverse(e, phi):
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        return None
    return x % phi


# -------------------------------
# FAST EXPONENTIATION
# -------------------------------

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod

        base = (base * base) % mod
        exp //= 2

    return result


# -------------------------------
# RSA KEY GENERATION
# -------------------------------

def generate_keys():
    while True:
        p = get_positive_int("Enter prime number p: ")
        if not is_prime(p):
            print(" p is not prime.")
            continue

        q = get_positive_int("Enter prime number q: ")
        if not is_prime(q):
            print(" q is not prime.")
            continue

        if p == q:
            print(" p and q should be different.")
            continue

        break

    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = get_positive_int("Enter e (1 < e < phi and gcd(e, phi)=1): ")
        if e <= 1 or e >= phi:
            print(" e must be between 1 and phi.")
            continue
        if gcd(e, phi) != 1:
            print(" gcd(e, phi) must be 1.")
            continue
        break

    d = mod_inverse(e, phi)

    print("\n Keys Generated:")
    print("Public Key (e, n):", (e, n))
    print("Private Key (d, n):", (d, n))

    return e, d, n


# -------------------------------
# ENCRYPTION
# -------------------------------

def encrypt(e, n):
    msg = input("Enter message to encrypt: ")
    cipher = [mod_exp(ord(c), e, n) for c in msg]
    print("Encrypted Message:", cipher)
    return cipher


# -------------------------------
# DECRYPTION
# -------------------------------

def decrypt(d, n):
    try:
        cipher = list(map(int, input("Enter cipher numbers (space-separated): ").split()))
    except:
        print("Invalid cipher input.")
        return

    message = ''.join(chr(mod_exp(c, d, n)) for c in cipher)
    print(" Decrypted Message:", message)


# -------------------------------
# MENU SYSTEM
# -------------------------------

def main():
    print("====== RSA Algorithm ======")

    e = d = n = None

    while True:
        print("\nMenu:")
        print("1. Generate Keys")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Exit")

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
            print("Invalid choice.")


# -------------------------------
# RUN PROGRAM
# -------------------------------

main()