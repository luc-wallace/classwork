bitStream = open("Trees.jpeg", "rb")
count = 0
try:
    print("Reading byte by byte contents of image file")
    bitPattern = bitStream.read(1)
    while bitPattern:
        count = count + 1
        print(count, ord(bitPattern))
        bitPattern = bitStream.read(1)
finally:
    bitStream.close()