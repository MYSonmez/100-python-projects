# Password Generator 


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


choiced_random_letters = random.choices(letters, k=nr_letters)

total_letter = ""

for letter in choiced_random_letters:
  total_letter += letter

choiced_random_numbers = random.choices(numbers, k=nr_numbers)

total_number = ""

for number in choiced_random_numbers:
  total_number += number

choiced_random_symbols = random.choices(symbols, k=nr_symbols)

total_symbol = ""

for symbol in choiced_random_symbols:
  total_symbol += symbol

password = (total_letter + total_number + total_symbol)

password_list = list(password)
random.shuffle(password_list)

result = ""

for char in password_list:
  result += char

print(f"Your password is: {result}")



# Another Way

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
