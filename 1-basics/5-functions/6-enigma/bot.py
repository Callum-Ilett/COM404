def run():
  character = input("Please enter a character to display")
  total = int(input("Please enter total number of characters"))
  number = int(input("Please enter a whole number"))
  string = str(character * total)

  for pos in range(1, len(string) + 1):

    if(pos % number == 0):
      print(string[pos-1], end="")
    else:
      print("-", end="")

run()
