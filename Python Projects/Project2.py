def names():

    name_input = input("Enter your firstname and lastname: ")

    (firstname,lastname) = name_input.split(" ")

    print(f"First Name: {firstname}")
    print(f"Last Name: {lastname}")

names()

