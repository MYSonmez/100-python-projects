# Coffee Machine

import data

MENU = data.MENU

water = 300
milk = 200
coffee = 100


def money_given():
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


choice = input("What would you like? (espresso/latte/cappuccino): ")

while choice != "off":
    money = 0
    if choice == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}gr")
        print(f"Money: ${money}\n")

    else:
        if coffee >= MENU[choice]["ingredients"]["coffee"]:
            if water >= MENU[choice]["ingredients"]["water"]:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))

                money = money_given()

                if money_given() >= MENU[choice]["cost"]:
                    if choice == "espresso":
                        water -= 50
                        coffee -= 18
                        money -= 1.5

                    elif choice == "latte":
                        water -= 200
                        milk -= 150
                        coffee -= 24
                        money -= 2.5

                    elif choice == "cappuccino":
                        water -= 250
                        milk -= 100
                        coffee -= 24
                        money -= 3.0

                    refund_money = money_given() - money
                    print(f"Here is ${refund_money} in change.")
                    print(f"Here is your {choice} ☕️. Enjoy!\n")
                else:
                    print(f"Sorry that's not enough money. {money_given()} refunded.\n")
            else:
                print("Sorry that's not enough water.\n")
        else:
            print("Sorry that's not enough coffee.\n")

    choice = input("What would you like? (espresso/latte/cappuccino): ")
