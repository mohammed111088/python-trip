Drinks_list = {
    "coffee": 2.5,
    "cappuccino": 5,
    "mocha": 4.2,
    "latte": 3,
    "espresso": 4.3,
    "water": 1
}
print("==========================\n")
print("Welcome to Coffee Machine")
print("==========================\n")
drinks_names = list(Drinks_list.keys())
drink = input(f"What do you want to drink? {drinks_names} ").lower()

if drink not in Drinks_list:
    print(f"Sorry, we cannot make your drink '{drink}'")

else:
    money = float(input(f"Please put the money in the pocket ({Drinks_list[drink]}$): "))

    if money < Drinks_list[drink]:
        print(f"the money is not enough, we cannot make your drink, here is your money({money})")

    elif money == Drinks_list[drink]:
        print(f"Done, here is your {drink}. Enjoy!")

    else:
        change = money - Drinks_list[drink]
        print(f"Done, please take your change ({change}), and here is your {drink}. Enjoy!")