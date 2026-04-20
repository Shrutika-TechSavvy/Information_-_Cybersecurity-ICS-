from secretpy import Zigzag

class RailFence:
    def __init__(self, key):
        self.key = key

    def encrypt1(self, text):
        return Zigzag.encrypt(self, text, self.key)

    def decrypt(self, text, key):
        return Zigzag.decrypt(self, text, key)

if __name__ == "__main__":
    text = "HELLO WORLD!!"
    key = 3
    rail_fence = RailFence(key)
    encrypted = rail_fence.encrypt1(text)
    print(f"Encrypted: {encrypted}")
    decrypted = rail_fence.decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")
    
