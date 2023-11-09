t = float(input("Enter temperature in celcius: "))
v = float(input("Enter wind velocity in kilometres per hour: "))
chill = 13.12 + 0.6215 * t - 11.37 * (v**0.16) + 0.3965 * t * (v**0.16)

print(f"Wind chill: {chill:.2f} °C")
