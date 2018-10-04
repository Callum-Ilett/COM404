print("""Where are you looking for the battery
[1]Bedroom
[2]Bathroom
[3]Lab
[4]Somewhere else\n""")

location = int(input())

if(location == 1):
    print("Ok moving to bedroom")
    choice = input("""You have moved to the bedroom, where would you like to look in the bedroom
    1)Under the bed
    2)Somewhere else\n\n""")

    if (choice) == 1:
        print("Found some socks but no battery")
    else:
        print("found some mess but no battery")

if(location == 2):
    print("Bathroom")

if (location == 3):
    print("In the lab")

if(location == 4):
    print("Somewhere else")

else:
    print("Please select an option using the numbers 1, 2 or 3")
