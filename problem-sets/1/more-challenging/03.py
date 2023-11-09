import math

G = 9.8
height = float(input("Enter height object was dropped from in metres: "))
speed = math.sqrt(2 * G * height)

print(f"The object will be travelling at {speed:.2f}m/s when it hits the ground.")
