class KeyManager:
    def __init__(self):
        self.keys = {}
    
    def generate_key(self, key_name):
        import secrets
        self.keys[key_name] = secrets.token_hex(16)
        return self.keys[key_name]
    
    def rotate_key(self, key_name):
        if key_name in self.keys:
            old_key = self.keys[key_name]
            self.keys[key_name] = secrets.token_hex(16)
            return old_key, self.keys[key_name]
        else:
            raise ValueError("Key not found.")
    
    def get_key(self, key_name):
        return self.keys.get(key_name, None)
    
    def delete_key(self, key_name):
        if key_name in self.keys:
            del self.keys[key_name]
        else:
            raise ValueError("Key not found.")