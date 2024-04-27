import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images=[rock,paper,scissors]
print("Welcome to the Rock, Paper, Scissors Game!")
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
num=random.randint(0,2)
print(f"Computer choice is {num}")
if choice>2 or choice<0:
  print("Invalid Number!!!")
  exit(0)
print(game_images[choice])
print(game_images[num])

if num>choice or (choice==2 and num==0):
  print("Computer win!")
elif choice>num or (choice==0 and num==2):
  print("You win!")
else:
  print("Draw!")
