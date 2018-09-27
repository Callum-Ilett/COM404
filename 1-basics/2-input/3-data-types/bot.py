#Ask the user for delattr
name = input("What is your name?")
age = int(input("What is your age"))
weight = float(input("What is your weight in Kg"))
height = float(input("What is your height in cm"))

bmi = weight/(height*height)
print(bmi)
