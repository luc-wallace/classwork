try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("data.txt file not found, empty file created")
    open("data.txt", "w")
else:
    data = file.read()
    print(f"File data: {data}")
    file.close()
