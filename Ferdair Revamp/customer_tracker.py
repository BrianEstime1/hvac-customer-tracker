import csv 
 
def add_customer():
    name = input("Customer name: ")
    phone = input("Phone: ")
    address = input("Address: ")
    with open("customers.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, address, ""])
    print(f"{name} added successfully!\n")

def view_customers():
    print("\n--- Customer List ---")
    with open("customers.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()

def search_customer():
    name = input("Enter customer name to search: ")
    found = False
    with open("customers.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            # search by the name field ( assuming name is the first column)
            if name.lower() in row[0].lower():
                print("Match found:", row)
                found = True
    if not found:
        print("Customer not found.\n")

while True:
    print("=== HVAC Customer Tracker ===")
    print("1. Add customer")
    print("2. View customers")
    print("3. Search customer")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        view_customers()
    elif choice == "3":
        search_customer()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.\n")