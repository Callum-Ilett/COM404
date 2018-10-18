def sum_ages_of_friends(Applejack, Rainbowdash, Buttershine):
  total = Applejack + Rainbowdash + Buttershine
  return total

def calc_avg_age_of_friends(Applejack, Rainbowdash, Buttershine):
  avg = (Applejack + Rainbowdash + Buttershine) / 3
  return avg

def run():
  friend_1 = int(input("How old is Applejack:"))
  friend_2 = int(input("How old is Rainbowdash:"))
  friend_3 = int(input("How old is Buttershine:"))

  print("""
[1]Average
[2]Sum
  """)

  mode = int(input("What would you like to choose"))

  if(mode == 1):
    avg = calc_avg_age_of_friends(friend_1, friend_2, friend_3)
    print("Average age is:", int(avg))
  
  elif(mode == 2):
    total = sum_ages_of_friends(friend_1, friend_2, friend_3)
    print("Sum of ages is:", total)

  else:
    print("Please enter the number 1 or 2")

run()

