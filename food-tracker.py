import csv
from datetime import date
from datetime import datetime
from config import DATA_DIR

inventory_file = DATA_DIR / "inventory.csv"
consumption_file = DATA_DIR / "consumption.csv"

def add_to_inventory():
    name = input("What is the name of your food?\n")
    purchase = get_date("What is the purchase date of your food?\n")
    expiration = get_date("What is the expiration date of your food?\n")
    state = input("What is the state of your food?\n")    
    new_row = {
            'ID': str(calculate_id()),
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

def calculate_id():
    with open(inventory_file, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            existing_ids = [int(row['ID']) for row in reader]
            return max(existing_ids) + 1 if existing_ids else 1

def get_date(question):
    while True:
        try:
            date = input(question)
            date = datetime.strptime(date, "%Y-%m-%d")
            return date.date()
        except ValueError:
            print("Enter a date according to the format YYYY-MM-DD.")

def main():
    print("Welcome to the food tracker. What would you like to do?\n")
    print("Press 1 for adding food to inventory.\n")
    print("Press 2 for removing food from inventory.\n")
    print("Press 3 for adding food to consumption.\n")
    print("Press 4 for displaying expiration warnings.\n")
    print("Press 5 for displaying current inventory.\n")
    sheet = input()
    print()

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
