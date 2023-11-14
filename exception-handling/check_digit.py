number = int(input("Please enter a 9-digit number: "))

z9 = number % 10
number = number // 10
z8 = number % 10
number = number // 10
z7 = number % 10
number = number // 10
z6 = number % 10
number = number // 10
z5 = number % 10
number = number // 10
z4 = number % 10
number = number // 10
z3 = number % 10
number = number // 10
z2 = number % 10
number = number // 10
z1 = number

total = z1 + 2 * z2 + 3 * z3 + 4 * z4 + 5 * z5 + 6 * z6 + 7 * z7 + 8 * z8 + 9 * z9
checkdigit = total % 11
print(f"Check digit: {checkdigit}")
