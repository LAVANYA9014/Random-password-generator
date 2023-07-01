import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt the user to specify the length of the password
password_length = int(input("Enter the length of the password: "))

# Generate and print the password
password = generate_password(password_length)
print("Generated password:", password)
