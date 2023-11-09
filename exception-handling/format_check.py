import re

pattern = re.compile("(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d\d\d\d")

while True:
    s = input("Enter a string in the format DD/MM/YYYY ")
    if pattern.match(s):
        break
    print("Invalid input!")

print(f"Valid data: {s}")
