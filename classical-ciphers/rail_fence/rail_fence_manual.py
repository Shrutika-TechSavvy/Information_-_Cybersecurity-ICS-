# Function to validate rails
def validate_rails(rails):
    return rails > 1


# Function to encrypt text
def encrypt_rail_fence(text, rails):

    rail = [['\n' for _ in range(len(text))] for _ in range(rails)]

    row = 0
    direction = 1

    # Fill zig-zag pattern
    for col in range(len(text)):
        rail[row][col] = text[col]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    # Read row-wise
    encrypted = ""

    for i in range(rails):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                encrypted += rail[i][j]

    return encrypted


# Function to decrypt text
def decrypt_rail_fence(cipher, rails):

    rail = [['\n' for _ in range(len(cipher))] for _ in range(rails)]

    row = 0
    direction = 1

    # Mark positions
    for col in range(len(cipher)):
        rail[row][col] = '*'

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    # Fill cipher text
    index = 0

    for i in range(rails):
        for j in range(len(cipher)):
            if rail[i][j] == '*':
                rail[i][j] = cipher[index]
                index += 1

    # Read zig-zag pattern
    result = ""
    row = 0
    direction = 1

    for col in range(len(cipher)):

        result += rail[row][col]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return result


# Function to take user input
def get_input():

    text = input("Enter the text: ").strip()

    if text == "":
        print("Invalid input! String cannot be empty.")
        return None, None

    try:
        rails = int(input("Enter number of rails: "))

        if not validate_rails(rails):
            print("Invalid rails! Rails must be greater than 1.")
            return None, None

    except ValueError:
        print("Invalid input! Enter a valid number.")
        return None, None

    return text, rails


# Main menu function
def menu():

    while True:

        print("\n===== Rail Fence Cipher =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':

            text, rails = get_input()

            if text is not None:
                encrypted = encrypt_rail_fence(text, rails)
                print("Encrypted Text:", encrypted)

        elif choice == '2':

            text, rails = get_input()

            if text is not None:
                decrypted = decrypt_rail_fence(text, rails)
                print("Decrypted Text:", decrypted)

        elif choice == '3':

            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


# Main function
def main():
    menu()


# Driver Code
main()