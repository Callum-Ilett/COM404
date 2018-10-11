number = int(input("What is the number to work out the factorial for"))

result = 1
for num in range(number,0, -1): 
    result *= num 

print("The factorial of %i is %i"%(number,result))
