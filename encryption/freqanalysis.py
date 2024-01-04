from string import ascii_lowercase
from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.gutenberg.org/cache/epub/72354/pg72354-images.html")
soup = BeautifulSoup(res.text, "html.parser")

frequency = {c: 0 for c in ascii_lowercase}

for char in data:
    if char in frequency:
        frequency[char] += 1

num_letters = len([char for char in data if char in ascii_lowercase])

for k, v in frequency.items():
    print(f"{k}: {v} ({v / num_letters * 100:.2f}%)")
