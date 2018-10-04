import math
print(""""What shape would you like to caluclate the volume for:
[1]Cylinder
[2]Cone""")

shape = int(input("\nPlease use integer values e.g 1 or 2:"))

radius = float(input("Please enter the radius"))
height = float(input("Please enter in a height"))

if (shape == 1):
    volume = round(math.pi * radius**2 * height,2)
    print("The volume for a cylinder is", volume)

elif(shape == 2):
    volume = round((math.pi * radius**2 * height)/3, 2)
    print("The volume for a cone is", volume)

else:
    print("That is not a valid choice please press 1 or 2")
