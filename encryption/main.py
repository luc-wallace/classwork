from string import ascii_lowercase

plaintext = input("Enter plaintext: ").lower()

for i in range(26):
    ciphertext = ""

    for char in plaintext: 
        if char in ascii_lowercase:
            ciphertext += ascii_lowercase[(ascii_lowercase.index(char) + i) % 26]
        else:
            ciphertext += char

    print(ciphertext)
