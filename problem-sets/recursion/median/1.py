def print_numbers(n):
    if n == -1:
        return
    print(n)
    return print_numbers(n - 1)

limit = int(input("Enter limit: "))
print_numbers(limit)

