while True:
    num = int(input("Enter a number between 1 and 100: "))
    if 1 <= num <= 100:
        break
    print("Invalid number!")


print(f"Valid data: {num}")
