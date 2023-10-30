a = float(input("Enter side 1 length: "))
b = float(input("Enter side 2 length: "))
c = float(input("Enter side 3 length: "))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(f"Area of triangle: {area:.2f}")
