import hashlib

def compute_md5(input_string):
    # Create MD5 hash object
    md5_hash = hashlib.md5()
    
    # Encode string to bytes and update hash
    md5_hash.update(input_string.encode('utf-8'))
    
    # Return hexadecimal digest
    return md5_hash.hexdigest()

# Test inputs
test_inputs = [
    "Hello",
    "SecureData",
    "MD5HashExample",
    "123456"
]

for text in test_inputs:
    print("Input:", text)
    print("MD5 Hash:", compute_md5(text))
    print()