import hashlib

text = "Hello world !!!"
#Encode string t bytes , then hash
md5_hash = hashlib.md5(text.encode())
#Get the hexadecimal representation
print("md5 hex representationn:", md5_hash.hexdigest()) 