# Silent Auction Program

import os
import art


def clear():
    os.system("cls")


logo = art.logo

print(logo)

name = input("What is your name?: ")
bid = int(input("What is your bid? $"))

bidders = {name: bid}

x = input("Are there any other bidders? Type 'yes' or 'no'.")

while x == "yes":
    clear()
    new_name = input("What is your name?: ")
    new_bid = int(input("What is your bid? $"))
    x = input("Are there any other bidders? Type 'yes' or 'no'.")
    bidders[new_name] = new_bid
    final_bidders = bidders


offer = 0

if x == "no":
    clear()
    for bidder in final_bidders:
        if final_bidders[bidder] > offer:
            winner = bidder
            offer = final_bidders[bidder]

print(f"The winner is {winner} with a bid of ${offer}")
