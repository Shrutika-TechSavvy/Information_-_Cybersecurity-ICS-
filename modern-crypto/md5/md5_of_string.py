import hashlib

# Take input from user
text = input("Enter a string: ")

# Convert string into bytes
encoded_text = text.encode()

# Apply MD5 hashing
md5_hash = hashlib.md5(encoded_text)

# Convert hash into readable hexadecimal format
result = md5_hash.hexdigest()

# Print final hash
print("MD5 Hash:", result)