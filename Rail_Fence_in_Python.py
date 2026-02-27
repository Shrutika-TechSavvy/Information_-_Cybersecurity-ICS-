# Hardcoded message and number of rails
text = "HELLOWORLD"
rails = 3

# Create empty rails
fence = [[] for _ in range(rails)]

row = 0
direction = 1  # 1 means moving down, -1 means moving up

# Place characters in zig-zag
for char in text:
    fence[row].append(char)
    row += direction

    # Change direction if we hit top or bottom
    if row == 0 or row == rails - 1:
        direction *= -1

# Read row by row to create cipher text
cipher = ""
for rail in fence:
    cipher += "".join(rail)

print("Encrypted text:", cipher)

#Encrypted text: HOLELWRDLO