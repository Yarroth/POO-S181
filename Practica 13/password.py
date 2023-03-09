import string
import random

class PasswordGenerator:
    def __init__(self, length=8, include_uppercase=False, include_special=False):
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_special = include_special

    def generate_password(self):
        characters = string.ascii_lowercase
        if self.include_uppercase:
            characters += string.ascii_uppercase
        if self.include_special:
            characters += string.punctuation
        password = ''.join(random.choice(characters) for i in range(self.length))
        return password
