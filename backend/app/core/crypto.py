import rsa

class CryptoManager:
    def __init__(self):
        self.public_key, self.private_key = rsa.newkeys(512)

    def encrypt(self, message):
        return rsa.encrypt(message.encode(), self.public_key)

    def decrypt(self, encrypted_message):
        return rsa.decrypt(encrypted_message, self.private_key).decode()

    def sign(self, message):
        return rsa.sign(message.encode(), self.private_key, 'SHA-256')

    def verify(self, message, signature):
        return rsa.verify(message.encode(), signature, self.public_key)