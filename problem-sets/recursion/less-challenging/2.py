def baseexp(b, e):
    if e == 0:
        return 1
    return b * baseexp(b, e - 1)

base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))

print(baseexp(base, exp))

