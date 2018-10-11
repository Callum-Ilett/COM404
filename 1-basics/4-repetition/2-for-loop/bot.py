amount = int(input("How many robots should I display?"))

if (amount < 10):
  print("Here I go:")
  for i in range(amount):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|\n")

elif (amount > 10):
  print("Here I go:")
  for i in range(10):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")

else:
  print("That is not a valid number")
