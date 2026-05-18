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

    print("================MENU=================")

    for category_name, category_items in menu.items():
        print(f"\n===== {category_name} ======")

        for item_name, item_info in category_items.items():
            print(f"{item_name: <15} | {item_info['price']: <3} SAR")

    print("======================================")

def check_order(person_choose):

    for category_items in menu.values():




