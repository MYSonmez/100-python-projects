# # CONDITIONAL OPERATORS


# == (equals to)
# != (not eguals to)
# > (greater than)
# < (less than)
# >= (greater than or equals to )
# <= (less than or equals to)
# % (gives remainder)


# # IF/ELIF/ELSE


# age = int(input("How old are you? "))

# if age >= 18:
#     print("Congratulations, you can get your driver's licence.")
# else:
#     print(f"Sorry, you have to wait {18 - age} years to get your driver's licence.")


# height = int(input("What is your height in cm? "))
# bill = 0

# if 200 > height > 120:
 
#     print("You can ride!")
 
#     age = int(input("What is your age? "))
  
#     if age >= 18:
#         bill = 12
#         print("Adult tickets are 12$")
#     elif 12 <= age < 18 :
#         bill = 10
#         print("Young tickets are 10$")
#     elif age < 12:
#         bill = 5
#         print("Childeren tickents are 5$")

#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         print(f"Pay ${bill + 3}")
#     else:
#         print(f"Pay ${bill}")
# else:
#     print("You can't ride :(")


# # A:

# print("Welcome to Python Pizza Deliveries!")

# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0

# if size == "S":
#     bill = 15
#     if add_pepperoni == "Y":
#         bill += 2
#     if extra_cheese == "Y":
#         bill += 1
#     print(f"Your final bill is ${bill}")

# elif size == "M":
#     bill = 20
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
#     print(f"Your final bill is ${bill}")

# else:
#     bill = 25
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
#     print(f"Your final bill is ${bill}")


# # B:

# print("Welcome to Python Pizza Deliveries!")

# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0

# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# else:
#     bill = 25


# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1
    
# print(f"Your final bill is ${bill}")



# # LOGICAL OPERATORS (and-or-not)

# a = 10

# print(a > 9 and a < 2) # OUTPUT // False
# print(a > 9 and a < 17) # OUTPUT // True
# print(a > 9 or a < 1) # OUTPUT // True
# print(a > 15 or a < 5) # OUTPUT // False
# print(not a > 9) # OUTPUT // False
