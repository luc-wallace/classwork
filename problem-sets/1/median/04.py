from math import pi

radius = float(input("Enter radius: "))

circle_area = radius**2 * pi
sphere_volume = radius**3 * (4 / 3) * pi

print(f"Circle area: {circle_area:.2f}")
print(f"Sphere volume: {sphere_volume:.2f}")
