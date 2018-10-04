print("""Where are you looking for the battery
[1]Bedroom
[2]Bathroom
[3]Lab
[4]Somewhere else\n""")

location = int(input())

if(location == 1):
    print("""You have moved to the bedroom, where would you like to look in the bedroom
    1)Under the bed
    2)Somewhere else\n""")
    choice = int(input())

    if (choice == 1):
        print("Found some socks but no battery")

    elif(choice == 2):
        print("found some mess but no battery")

    else:
        print("Please type 1 or 2")

elif(location == 2):
    print("""You have moved to the bathroom, where would you like to look in the bathroom
    1)Bathtub
    2)Somewhere else\n""")
    choice = int(input())

    if (choice == 1):
        print("Found a rubber duck but no battery")
    elif (choice == 2):
        print("It's wet but no battery")
    else:
        print("Please type 1 or 2")

elif (location == 3):
    print("""You have moved to the lab, where would you like to look in the lab
    1)On the table
    2)Somewhere else\n""")
    choice = int(input())

    if(choice == 1):
        print("Found the battery")

    elif(choice == 2):
        print("Found some tools but no battery")
    
    else:
        print("Please type 1 or 2")

elif(location == 4):
    print("Somewhere else")

else:
    print("Please select an option using the numbers 1, 2, 3 or 4")
