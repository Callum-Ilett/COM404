direction = input("Please enter a direction I should move in using WASD:").upper()

if (direction == "W"):
  print("Moving forward")

elif (direction == "A"):
  print("Moving Left")

elif (direction == "S"):
  print("Moving Backwards")
  
elif (direction == "D"):
  print("Moving right")
  
else:
  print("Sorry I don't know what direction that is, try using WASD")
