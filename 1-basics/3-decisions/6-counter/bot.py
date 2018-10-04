num1 = int(input("Please enter a number"))
num2 = int(input("Please enter a number"))
num3 = int(input("Please enter a number"))

odd_numbers = 0
even_numbers = 0

if(num1 % 2 == 0):
    even_numbers += 1
else:
    odd_numbers += 1

if(num2 % 2 == 0):
    even_numbers += 1
else:
    odd_numbers += 1

if(num3 % 2 == 0):
    even_numbers += 1
else:
    odd_numbers += 1

print("\nOdd numbers:",odd_numbers)
print("Even numbers:",even_numbers)
