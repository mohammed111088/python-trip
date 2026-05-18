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


def calculate_price(person_choose):

    for category_items in menu.values():
        if person_choose in category_items:
            return category_items[person_choose]["price"]


def take_order():

    cart = []

    while True:

        person_choose = input("\nChoose your order: ").lower().strip()
        if check_order(person_choose):
            cart.append(person_choose)

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

    for item in cart:
        price = calculate_price(item)
        total += price
        print(f"{item: <15} | {price} SAR")
    print(f"\nTOTAL = {total} SAR")


def start_cafe():

    show_menu()

    cart = take_order()

    show_bill(cart)


start_cafe()