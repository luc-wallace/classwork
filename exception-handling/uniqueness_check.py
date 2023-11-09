usernames = []

while True:
    if len(usernames) > 0:
        print(f"Usernames: {', '.join(usernames)}")
    username = input("Enter a unique username: ")
    if username not in usernames:
        usernames.append(username)
        continue
    print(f"{username} is already taken!")
