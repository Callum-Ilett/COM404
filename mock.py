#Question 1
# last_petal = input("What happens when the last petal falls?")
# print("My dear Bella when the last petal falls", last_petal)

#Question 2
# fear = input("Have you fear in your heart")

# if(fear == "yes"):
#   print("Fear is the path to the dark side. You cannot be a Jedi apprentice.")
# else:
#   print("The force is strong in you. You may be a Jedi apprentice.")

#Question 3
# num_zones = int(input("How many zones must I cross?"))
# print("Crossing zones...")

# for zone in range(num_zones, 0, -1):
#   print("... crossed zone", zone)
# print("Crossed all zones.  Jumanji!")

#Question 4

# def visit(ghost): 
#   if(ghost == "Ghost of Christmas Past"):
#     print("Humbug! I care not for these days of past celebration")

#   elif(ghost == "Ghost of Christmas Present"):
#     print("Humbug! I care not for their suffering.")

#   else:
#     print("Please no more. I will change my ways. ")

# # The following are calls to the function for testing purposes 
# visit("Ghost of Christmas Past") 
# visit("Ghost of Christmas Present") 
# visit("Ghost of Christmas Future")

#Question 5
# health = 100
# MAX_ITERATIONS = 5

# print("Your health is "+str(health)+ "%. Escape is in progress... \n")

# for counter in range(MAX_ITERATIONS):
#   print("…Oh dear, who is that?")
#   response = input()

#   if(response == "Smiler's Bot"):
#     health -= 20
#     print("Time to jam out of here! \n")

#   elif(response == "Hacker"):
#     health += 20
#     print("Yay! Better follow this one! \n")

#   else:
#     print("Phew, just another emoji! \n")

# print("Escaped! Health is " + str(health) + "%")

#Question 6

# def is_league_united(hero_1, hero_2):
#   if(hero_1 == "Superman" and hero_2 == "Wonder Woman"):
#     return True

#   elif(hero_2 == "Superman" and hero_1 == "Wonder Woman"):
#     return True

#   else:
#     return False

# def decide_plan(hero_1, hero_2):
#   united = is_league_united(hero_1, hero_2)

#   if(united):
#     print("Time to save the world!")
#   else:
#     print("We must unite the league!")

# def run():
#   user_hero_1 = input("Enter the name of the 1st hero")
#   user_hero_2 = input("Enter the name of the 2nd hero")
#   print("")

#   choice = input("League or plan?").lower()

#   if(choice == "league"):
#     print(is_league_united(user_hero_1, user_hero_2))

#   elif(choice == "plan"):
#     decide_plan(user_hero_1, user_hero_2)

#   else:
#     print("Invalid command. Please try again")

# run()

#Question 7

def under(word):
  print(word)
  print("*" * len(word))

def over(word):
  print("*" * len(word))
  print(word)

def both(word):
  print("*" * len(word))
  print(word)
  print("*" * len(word))

def grid(word):
  rows = int(input("How many rows?"))
  columns = int(input("How many columns?"))

  for row in range(rows):
    for column in range(columns):
        print(both(word), end=" ")
    print()

user_word = input("Please enter a word")

print("""
[1]Under
[2]Over
[3]Both
[4]Grid""")

choice = int(input("Choose an option using the number keys, 1 to 4"))
print("")

if(choice == 1):
  under(user_word)

elif(choice == 2):
  over(user_word)

elif(choice == 3):
  both(user_word)

else:
  grid(user_word)


