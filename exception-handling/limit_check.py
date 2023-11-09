while True:
    num = int(input("Enter a number above 0: "))
    if num >= 0:
        break
    print("Invalid number!")


print(f"Valid data: {num}")
