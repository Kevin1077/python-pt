import random

def play(attempt1, rand_num):
    while attempt1 != 0:
        print(f"You have {attempt1} attempts remaining to guess the number\n")
        guess = int(input("Make a guess: \n"))
        if guess < rand_num:
            attempt1 -= 1
            if attempt1 == 0:
                print("You've run out of guesses.\n")
            else:
                print("Too low.\nGuess again.\n")

        elif guess > rand_num:
            attempt1 -= 1
            if attempt1 == 0:
                print("You've run out of guesses.\n")
            else:
                print("Too high.\nGuess again.\n")
        else:
            print(f"You got it! The answer was {rand_num}")
            break











print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")

random_number = random.randint(1,100)

choice = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

if choice == "easy":
    attempt = 10
    play(attempt, random_number)

else:
    attempt = 5
    play(attempt, random_number)
