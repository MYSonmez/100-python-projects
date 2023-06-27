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

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice <= 2 and choice >= 0:
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)
    print("Computer chose:")
else:
    print("You typed an invalid number, you lose.")

list = [rock, paper, scissors]
computer_choice_index = random.randint(0,2)
computer_choice = list[computer_choice_index]


if choice <= 2 and choice >= 0:
    print(computer_choice)
    if choice == 0:
        if computer_choice_index == 0:
            print("It's a draw.")
        elif computer_choice_index == 1:
            print("You lose.")
        elif computer_choice_index == 2:
            print("You win!")
            
    elif choice == 1:
        if computer_choice_index == 0:
            print("You win!")
        elif computer_choice_index == 1:
            print("It's a draw.")    
        elif computer_choice_index == 2:
            print("You lose.")

    elif choice == 2:
        if computer_choice_index == 0:
            print("You lose.")
        elif computer_choice_index == 1:
            print("You win!")
        elif computer_choice_index == 2:
            print("It's a draw.")