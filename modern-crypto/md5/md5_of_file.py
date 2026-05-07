from hashlib import md5

# Static file path
file_path = "D:\\SEM_6\\ICS\\Information_-_Cybersecurity-ICS-\\modern-crypto\\md5\\md5_of_string.py"

# Create MD5 hash object
md5_hash = md5()

try:
    # Open file in binary mode
    with open(file_path, "rb") as file:

        # Read file in small chunks
        while True:
            chunk = file.read(4096)

            # Stop when file ends
            if chunk == b"":
                break

            # Update MD5 hash with chunk data
            md5_hash.update(chunk)

    # Print final MD5 hash
    print("MD5 Hash:", md5_hash.hexdigest())

except FileNotFoundError:
    print("File not found!")

except Exception as e:
    print("Error:", e)