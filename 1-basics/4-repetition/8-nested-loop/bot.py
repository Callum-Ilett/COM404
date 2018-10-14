columns = int(input("How many columns should I have?"))
rows = int(input("How many rows should I have?"))

for count in range(rows):
    for number in range(columns):
        print(":-)", end=" ")
    print()
