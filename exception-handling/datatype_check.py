while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid number!")
    else:
        break

print(f"Valid data: {num}")
