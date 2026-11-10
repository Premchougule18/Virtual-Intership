import random
import string


def generate_password():

    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be positive.")
        return

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for i in range(length):

        password += random.choice(characters)

    print("\nGenerated Password:", password)


generate_password()