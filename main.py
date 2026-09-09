def add_quantity():

    while True:
        try:
            quantity = int(input("How many do you want? "))
            break
        except ValueError:
            print("Please enter a number!")

    return quantity

add_quantity()
