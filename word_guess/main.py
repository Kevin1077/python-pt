from random import *
from art import *
from word import *

word=(choice(word_list))
print(word)

masked_word="_"*len(word)
print(masked_word)

game_over=False
correct_letter=[]
life=len(stages)-1

while not game_over:
 guess=(input("Guess a letter\n")).lower()

 display=""
 for letter in word:
    if letter==guess and letter not in correct_letter:
       display+=letter
       print("Correct guess!\n")
       correct_letter.append(letter)

    elif letter in correct_letter:
        display+=letter


    else :
       display+="_"

 print(display)

 if guess not in word:
     life-=1
     print(f"You have  {life} life left\n")
     if life==0:
         print("You Lose\nGame Over!!!")
         print(logo)
         exit(0)
 if display==word:
    print("You win")
    game_over=True

 print(stages[life])

print(logo)
