# THE TIP CALCULATOR

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?\n$"))
tip_percentage = int(input("What persentage tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))


amount = round(
    (total_bill / people) * (1 + (tip_percentage / 100)), 2
)

print(f"Each person should pay: ${amount}")