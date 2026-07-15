import math

radius = float(input("What is the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 3)}cm")

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 4)}cm²")