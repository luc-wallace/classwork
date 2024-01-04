def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

num = int(input("Enter a number: "))
print(sum_natural(num))
