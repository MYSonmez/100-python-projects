# Higher Lower Game

import random
import art
import game_data
import os

data = game_data.data
logo = art.logo
vs = art.vs


def clear():
    os.system("cls")


def winner():
    if followers(a) > followers(b):
        return "A"
    else:
        return "B"


def random_compare():
    return random.choice(data)


def name(x):
    return x["name"]


def followers(x):
    return x["follower_count"]


def description(x):
    return x["description"]


def country(x):
    return x["country"]


a = random_compare()
b = random_compare()

print(logo)

is_not_wrong = True
score = 0

while is_not_wrong:
    print(f"Compare A: {name(a)}, a {description(a)}, from {country(a)}.")
    print(vs)
    print(f"Compare B: {name(b)}, a {description(b)}, from {country(b)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if guess == winner():
        score += 1
        a = b
        b = random_compare()
        clear()
        print(logo)
        print(f"You're right! Current score: {score}")
    else:
        is_not_wrong = False
        clear()
        print(f"Sorry, that's wrong. Final score {score}.")
