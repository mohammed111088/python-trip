import time

menu = {

    "drinks": {

        "coffee": {"price": 12},
        "cappuccino": {"price": 18},
        "latte": {"price": 17},
        "espresso": {"price": 10},
        "mocha": {"price": 19},
        "americano": {"price": 15},
        "tea": {"price": 8},
        "green tea": {"price": 9},
        "hot chocolate": {"price": 16},
        "water": {"price": 3},
        "orange juice": {"price": 14},
        "iced coffee": {"price": 18}

    },

    "desserts": {

        "croissant": {"price": 11},
        "cheesecake": {"price": 22},
        "brownie": {"price": 15},
        "donut": {"price": 9},
        "cookie": {"price": 7},
        "muffin": {"price": 10},
        "apple pie": {"price": 18},
        "tiramisu": {"price": 24},
        "pancake": {"price": 20},
        "waffle": {"price": 21}

    },

    "food": {

        "burger": {"price": 28},
        "pizza": {"price": 35},
        "sandwich": {"price": 19},
        "french fries": {"price": 13},
        "fried chicken": {"price": 30},
        "salad": {"price": 17},
        "pasta": {"price": 26},
        "hot dog": {"price": 16},
        "shawarma": {"price": 18},
        "nuggets": {"price": 14}

    }

}
print("============\nWELCOME TO THE MAAN COFFE\n============")


def show_menu():

    print("\n=========== MENU ===========")

    for category_name, category_items in menu.items():
        print(f"\n--- {category_name.upper()} ---")

        for item_name, item_info in category_items.items():
            print(f"{item_name: <15} | {item_info['price']: >3} SAR")

    print("======================================")


def check_order(person_choose):

    for category_items in menu.values():

        if person_choose in category_items:
            return True

    return False


def add_quantity():

    quantity = int(input("How many do you want? "))

    return quantity


def calculate_price(person_choose):

    for category_items in menu.values():
        if person_choose in category_items:
            return category_items[person_choose]["price"]


def take_order():

    cart = {}

    while True:

        person_choose = input("\nChoose your order: ").lower().strip()
        if check_order(person_choose):

            if person_choose in cart:
                quantity = add_quantity()
                cart[person_choose] += quantity
            else:
                quantity = add_quantity()
                cart[person_choose] = quantity

            print(f"{person_choose} added to cart!")

        else:
            print("Sorry, we do not have this item!")

        more = input("Anything else? (yes/no): ").lower()
        if more == "no":
            break
    return cart


def show_bill(cart):

    total = 0

    print("\n========= YOUR BILL =========")

    for item, quantity in cart.items():

            price = calculate_price(item)
            total += price * quantity
            item_total = price * quantity

            print(f"{item} x{quantity} | {item_total} SAR")

    print(f"\nTOTAL = {total} SAR")
    return total


def payment(total):
    while True:

        payment_method = input("how would you like to pay: card/cash? ").lower().strip()

        if payment_method == "card":
            print("Please wait ...")
            time.sleep(5)
            print("Payment successful!")
            break

        elif payment_method == "cash":
            while True:
                try:
                    money = float(input("Enter cash amount: "))
                    break
                except ValueError:
                    print("Please enter a number!")

            while money < total:
                print("Sorry, not enough money!")
                try:
                    money = float(input("Enter cash amount: "))
                except ValueError:
                    print("Please enter a number!")

            if money == total:
                print("Payment successful!")
                break
            elif money > total:
                change = money - total
                print(f"Done please take your change{change} SAR")
                break

        else:
            print("Sorry, try again!")


def start_cafe():

    show_menu()

    cart = take_order()
    if not cart:
        print("Thank you")
        return

    total = show_bill(cart)

    payment(total)


start_cafe()