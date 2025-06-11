import random
import art

from game_data import data


def generating_random_question():
   return random.randint(1, len(data)+1)

def play_game(rand_num1, rand_num2):
        play = True
        score = 0
        while play:
            if rand_num1 == rand_num2:
                rand_num2 = generating_random_question()
            print(f"Compare A: {data[rand_num1]["name"]}, a {data[rand_num1]['description']} from {data[rand_num1]['country']}\n")
            print(art.vs)
            print(f"\nAgainst B: {data[rand_num2]["name"]}, a {data[rand_num2]['description']} from {data[rand_num2]['country']}\n")
            guess = input("Who has more followers? Type 'A' or 'B':\n").lower()

            followers1 = data[rand_num1]['follower_count']
            followers2 = data[rand_num2]['follower_count']

            if (guess == 'a' and followers1 > followers2 ) or (guess == 'b' and followers1 < followers2 ):
                score += 1
                rand_num1 = rand_num2
                rand_num2 = generating_random_question()
            else:
                print(f"Sorry, that's wrong. Final score: {score}\n")
                break


print(art.logo)
num1 = generating_random_question()
num2 = generating_random_question()

play_game(num1, num2)

