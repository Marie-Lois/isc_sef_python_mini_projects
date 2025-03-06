import random
import string
lengths = int(input("Enter password length: "))
def generate_password(length = lengths):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) 
    for i in range(length))
    return password
print(" Your random password:", generate_password())
