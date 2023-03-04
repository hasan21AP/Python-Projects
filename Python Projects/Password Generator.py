import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&")

def generate_password():

    length_password = int(input("How long the password you would to be: "))

    random.shuffle(characters)
    password = []

    for x in range(length_password):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)
    print(f"Your password is: {password}")


generate_password()