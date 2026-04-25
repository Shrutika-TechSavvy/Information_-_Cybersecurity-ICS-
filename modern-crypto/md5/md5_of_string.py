import hashlib
def generate_md5(text, encoding = "utf-8", errors = "strict"):
    #Validation : type check
    if not isinstance(text, str):
        raise TypeError("Input must be of string...")
    #Validation : empty string
    if text == "":
        raise ValueError("Input string cannot be empty...")
    
    try:
        byte_data = text.encode(encoding, errors = errors)
    except UnicodeEncodeError as e:
        print("Encoding error : ", e)

    md5 = hashlib.md5()
    md5.update(byte_data)
    return md5.hexdigest()