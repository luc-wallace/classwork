while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if len(username) > 0 and len(password) > 0:
        break

    print("Username or password must not be blank!")
