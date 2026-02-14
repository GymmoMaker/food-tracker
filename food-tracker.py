import csv
from config import DATA_DIR

inventory_file = DATA_DIR / "inventory.csv"
consumption_file = DATA_DIR / "consumption.csv"

def add_to_inventory():
    name = input("What is the name of your food?")
    purchase = "01-01-2026" #dummy variable for now
    expiration = input("What is the expiration date of your food?")
    state = input("What is the state of your food?")

    with open(inventory_file, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            existing_ids = [int(row['ID']) for row in reader]
            next_id = max(existing_ids) + 1 if existing_ids else 1
    
    new_row = {
            'ID': str(next_id),
            'Name': name,
            'Purchase': purchase,
            'Expiration': expiration,
            'State': state
        }

    with open(inventory_file, 'a', newline='') as csv_file:
        fieldnames = ['ID', 'Name', 'Purchase', 'Expiration', 'State']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writerow(new_row)

def remove_from_inventory():
    return 1

def add_to_consumption():
    return 1

def display_expiration():
    return 1


def display_inventory():
    with open(inventory_file) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            print(f'\t{row['Name']} is currently {row['State']} and will expire on {row['Expiration']}.')

def main():
    print("Welcome to the food tracker. What would you like to do?")
    print("Press 1 for adding food to inventory.")
    print("Press 2 for removing food from inventory")
    print("Press 3 for adding food to consumption.")
    print("Press 4 for displaying expiration warnings.")
    print("Press 5 for displaying current inventory.")
    sheet = input()

    if sheet == "1":
        add_to_inventory()
    if sheet == "2":
        remove_from_inventory()
    if sheet == "3":
        add_to_consumption()
    if sheet == "4":
        display_expiration()
    if sheet == "5":
        display_inventory()

if __name__ == "__main__":
    main()
