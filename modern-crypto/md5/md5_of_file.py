import hashlib
file_path = "D:\\SEM_6\\ICS\\Information_-_Cybersecurity-ICS-\\modern-crypto\\md5\\md5_of_string.py"
obj = hashlib.md5()
try:
    with open (file_path, "rb") as file:
        chunk = file.read(4096)
        if chunk == b"":
            print("File is empty")
        else:
            obj.update(chunk)
    print("MD5 Hash:", obj.hexdigest())
except:
    print("File not found")          