import math 
radius = int(input("Enter the radius of the sphere: "))
diameter = radius * 2
circumference = 2 * math.pi * radius
surface_area = 4 * math.pi * radius ** 2
volume = (4/3) * math.pi * radius ** 3

print("Diameter of the sphere is:", diameter)
print("Circumference of the sphere is:", circumference)
print("Surface area of the sphere is:", surface_area)
print("Volume of the sphere is:", volume)
