# Number Guessing Game

from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

correct_answer = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    remaining_guess = 10
elif difficulty == "hard":
    remaining_guess = 5

print(f"\nYou have {remaining_guess} tries to guess the number.\n")
guess = int(input("Make a guess: "))
remaining_guess -= 1

while remaining_guess > 0 and guess != correct_answer:
    if guess < correct_answer:
        print("Too low.")
    elif guess > correct_answer:
        print("Too high.")
    print("Guess again.")
    print(f"You have {remaining_guess} attempts remaining to guess the number.\n")
    guess = int(input("Make a guess: "))
    remaining_guess -= 1


if guess == correct_answer:
    print(f"\nYou got it. The answer was {correct_answer}.")
else:
    if guess < correct_answer:
        print("Too low.")
    elif guess > correct_answer:
        print("Too high.")
    print("\nYou've run out of guesses, you lose.")
    print(f"The answer was {correct_answer}.")
