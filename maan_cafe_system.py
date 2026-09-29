import time

menu = {

    "drinks": {

        "coffee": {"price": 12, "temperature": True},
        "cappuccino": {"price": 18, "temperature": True},
        "latte": {"price": 17, "temperature": True},
        "espresso": {"price": 10},
        "mocha": {"price": 19, "temperature": True},
        "americano": {"price": 15, "temperature": True},
        "tea": {"price": 8, "temperature": True},
        "green tea": {"price": 9, "temperature": True},
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

    while True:
        try:
            quantity = int(input("How many do you want? "))

            if quantity <= 0:
                print("Please enter a positive number!")
            else:
                break
        except ValueError:
            print("Please enter a number!")

    return quantity


def add_temperature():

    while True:
        temperature = input("Hot or Cold? ").lower().strip()

        if temperature == "hot" or temperature == "cold":
            return temperature
        else:
            print("Please enter Hot or Cold!")


def calculate_price(person_choose):

    for category_items in menu.values():
        if person_choose in category_items:
            return category_items[person_choose]["price"]


def take_order():

    cart = {}
    while True:
        while True:
            person_choose = input("\nChoose your order: ").lower().strip()

            if check_order(person_choose):

                temperature = None

                for category_items in menu.values():
                    if person_choose in category_items:
                        temperature = category_items[person_choose].get("temperature", False)
                cart_key = person_choose

                if temperature:
                    temperature = add_temperature()
                    cart_key = person_choose + " " + temperature

                if cart_key in cart:
                    quantity = add_quantity()
                    cart[cart_key]["quantity"] += quantity

                else:
                    quantity = add_quantity()
                    cart[cart_key] = {"quantity": quantity,
                                        "temperature": temperature
                                      }

                print(f"{person_choose} added to cart!")
                break

            else:
                print("Sorry, we do not have this item!")

        while True:
            more = input("Anything else? (yes/no): ").lower()

            if more == "yes":
                break
            elif more == "no":
                return cart
            else:
                print("Please enter yes or no!")


def show_bill(cart):

    total = 0

    print("\n========= YOUR BILL =========")

    for item, item_info in cart.items():

        quantity = item_info["quantity"]
        item_name = item
        temperature = item_info["temperature"]

        if item_info["temperature"]:
            item_name = item.replace(" " + item_info["temperature"], "")
            display_name = f"{item_name} ({temperature})"
        else:
            display_name = item_name

        price = calculate_price(item_name)
        total += price * quantity
        item_total = price * quantity
        print(f"{display_name} x{quantity} | {item_total} SAR")

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