def display_box(name):
  print("*" * (len(name) + 10))
  print("* Hello", name, "*")
  print("*" * (len(name) + 10))

def display_lcase(word):
  print(word.lower())

def display_ucase(word):
  print(word.upper())

def display_mirrored(word):
  print(word,"|", end=" ")
  for letter in range(len(word), 0, -1):
    print(word[letter-1], end="")

def display_repeat(word):
  count = int(input("How many times should I repeat the word:"))
  # print(word * count)

  for i in range(1, count +1):
    if(i % 2 == 0):
      display_lcase(word)
    else:
      display_ucase(word)

def run():
  user_word = input("Please enter a word:")

  print("""
[1]Display In ascii box
[2]Display lowercase
[3]Display upper case
[4]Display display_mirrored
[5]Display repeated""")
  print()

  choice = int(input("What would you like to do:"))

  if (choice == 1):
    display_box(user_word)
  elif (choice == 2):
    display_lcase(user_word)
  elif (choice == 3):
    display_ucase(user_word)
  elif (choice == 4):
    display_mirrored(user_word)
  elif (choice == 5):
    display_repeat(user_word)
  else:
    print("Please choos a number from 1 to 5")
  
run()

    
