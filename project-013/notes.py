## DEBUGGING EXERCISES

# 1
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it") # (i never reach 20)
my_function()

# solution
def my_function():
  for i in range(1, 21): # (the range should be (1, 21) or line 13 should be "if i == 19")
    if i == 20:
      print("You got it")
my_function()


# 2
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6) # (index 6 doesn't exist)
print(dice_imgs[dice_num])

# solution
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) # (the range must be (0, 5))
print(dice_imgs[dice_num])


# 3
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994: # (the ranges doesn't contain 1994)
    print("You are a Gen Z.")

# solution
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994: # (there must be an equals here or line 42)
    print("You are a Gen Z.")


# 4
age = input("How old are you?")
if age > 18:
    print("You can drive at age {age}.")

# solution
age = int(input("How old are you?")) # (to compare "age" variable with numbers it must be an integer)
if age > 18:
    print(f"You can drive at age {age}.") # (print statement should be indented and there must be an "f string" here)


# 5
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: ")) # (there is an extra equals in this line and it makes this line "False")
total_words = pages * word_per_page
print(total_words)

# solution
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


# 6
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(
        new_item
    )  # (this code adds "the last new_item value (26)" to the b_list)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])


# solution
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(
            new_item
        )  # (now the code is indented and it adds every new_item value)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])


# Debbuging Tips

# tip 1: try to identify the bug
# tip 2: repdroduce the bug
# tip 3: pretend to be a computer
# tip 4: use print statement to see what is the issue
# tip 5: run often your code
# tip 6: use a debugger
# tip 7: ask "stackoverflow"