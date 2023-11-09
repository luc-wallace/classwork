while True:
    s = input("Enter a string 9 characters long: ")
    if len(s) == 9:
        break
    print("Invalid input!")

print(f"Valid data: {s}")
