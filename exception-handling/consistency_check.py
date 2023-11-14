months = (
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
)
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

while True:
    month = input("Enter the month: ").lower()
    if month not in months:
        print("Invalid month!")
        continue

    day = int(input("Enter day of the month: "))
    if 1 <= day <= days[months.index(month)]:
        break
    print("Invalid day of month!")

print(f"Valid data: {day} of {month}")
