from game_data import data
import random
from art import logo, vs
import os

def clear():
    os.system('cls')

def format_data(celebrity):
    return f"{celebrity["name"]}, a {celebrity["description"]}, from {celebrity["country"]}."


def check_answer(answer, followers_A, followers_B):
    if followers_A > followers_B:
        return answer == "a"
    else:
        return answer == "b"
    
print(logo)   
score = 0    
game_should_continue = True
celebrity_B = random.choice(data)

while game_should_continue:
    celebrity_A = celebrity_B
    celebrity_B = random.choice(data)
                      
    while celebrity_A == celebrity_B:
        celebrity_B = random.choice(data)

    print(f"Compare A: {format_data(celebrity_A)}")
    print(vs)
    print(f"Against B: {format_data(celebrity_B)}.")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    followers_A = celebrity_A["follower_count"]
    followers_B = celebrity_B["follower_count"]

    is_correct = check_answer(answer, followers_A, followers_B)

    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")