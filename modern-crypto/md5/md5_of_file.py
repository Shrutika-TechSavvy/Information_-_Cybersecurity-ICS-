import hashlib
def md5_file(filepath):
    md5 = hashlib.md5()
    with open(filepath, "rb") as f :
        #read the file in chunks so that we don't load the entire file in memory , in such a way we can hash large files
        for chunk in iter(lambda : f.read(4096), b""):
            md5.update(chunk)
    return md5.hexdigest()

if __name__ == "__main__":
    file_path = "D:\\SEM_6\\ICS\\Information_-_Cybersecurity-ICS-\\modern-crypto\\md5\\md5_of_string.py"
    print("MD5 hash of the file is : ", md5_file(file_path))