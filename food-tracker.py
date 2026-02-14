add_to_inventory():

remove_from_inventory():

add_to_consumption():

def main():
    print("Welcome to the food tracker. What would you like to do?")
    print("Press 1 for adding food to inventory.")
    print("Press 2 for removing food from inventory")
    print("Press 3 for adding food to consumption.")
    sheet = input()

    if sheet == 1:
        add_to_inventory()
    if sheet == 2:
        remove_from_inventory()
    if sheet == 3:
        add_to_consumption()

if __name__ == "__main__":
    main()
