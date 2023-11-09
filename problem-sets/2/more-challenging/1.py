pos = input("Enter position: ")

col_even = ("abcdefgh".index(pos[0]) + 1) % 2 == 0
row_even = (int(pos[1])) % 2 == 0

if row_even == col_even:
    print("The square is black.")
else:
    print("The square is white.")
