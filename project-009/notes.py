# # DICTIONARIES

# a_dictionary = {
#     key: value,
#     key_2: value_2
# }


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Function"])
## OUTPUT // A piece of code that you can easily call over and over again. (the value of "Function")


# Adding New Items to Dictionary
programming_dictionary["Loop"] ="The action of doing something over and over again"


# Create an Empty Dictionary
empty_dictionary = {}


# Edit an Item in Dictionary
programming_dictionary["Bug"] = "A mouth in your computer"


# Loop Through a Dictionary
for key in programming_dictionary:
    print(key) # OUTPUT // key
    print(programming_dictionary[key]) # OUTPUT // the value of key



#########################################
    
# NESTING


capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}


# Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


# Nesting Dictionary in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}


# Nesting Dictionaries in Lists
travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
