categories = {
    "a radio wave": 3 * 10**9,
    "a microwave": 3 * 10**12,
    "infrared light": 4.3 * 10**14,
    "visible light": 7.5 * 10**14,
    "ultraviolet light": 3 * 10**17,
    "an x-ray": 3 * 10**19,
    "a gamma ray": 0,
}

frequency = float(input("Enter frequency of EM wave: "))

lower_bound = 0
for name, bound in categories.items():
    if frequency > bound:
        if bound == 0:
            break
        lower_bound = bound
        continue
    break


print(f"The wave is {name}.")
