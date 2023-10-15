print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction=input("Which way you want to go? left or right\n").lower()
if direction=="left":
  desicion=input('There is a lake ahead and in the middle there is an Island If you want to swim type "swim" or type "wait" to wait for a boat for a boat?\n').lower()
  if desicion=="wait":
    door=input('In the Island there is a house with three different coloured doors type "red" "yellow" or "blue" to choose the respective coloured door you wish to enter?\n').lower()  
    if door=="yellow":
      print("You win! You found the treasure")
    elif door=="blue":
      print("Fell into fire, Game over!!!")
    elif door=="red":
      print("Eaten by Monster, Game over!!!")
    else:
      print("Invalid choice, Game over!!!")
  elif desicion=="swim":
    print("Crocodiles ahead, Game over!!!")
  else:
    print("Invalid choice, Game over!!!")
elif direction=="right":
  print("Fell into a hole, Game over!!!")
else:
  print("Invalid choice, Game over!!!")
      
  
  

