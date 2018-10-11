amount = int(input("How many robots"))
num_displayed = 0

if(amount < 10):
  while(num_displayed < 10):
    print("%i)#########"%(num_displayed))
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")
    num_displayed += 1

elif (amount >= 10):
  while(num_displayed != 10):
    print("%i)#########"%(num_displayed))
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")
    num_displayed += 1
  
else:
  print("Invalid")
  
