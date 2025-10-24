"""Command-line utility for logging HVAC customers into a CSV file."""

import csv
from pathlib import Path
from typing import Dict, List


CSV_FILE = Path("customers.csv")
CSV_HEADERS = ["Name", "Phone", "Address", "Notes"]
PHONE_MIN_DIGITS = 10


def ensure_csv_file() -> None:
    """Create the CSV file with headers if it is missing or empty."""
    if not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0:
        try:
            with CSV_FILE.open("w", newline="") as file:
                csv.writer(file).writerow(CSV_HEADERS)
        except OSError as err:
            print(f"Unable to prepare customer storage: {err}\n")


def read_customers() -> List[Dict[str, str]]:
    ensure_csv_file()
    try:
        with CSV_FILE.open("r", newline="") as file:
            return list(csv.DictReader(file))
    except (OSError, csv.Error) as err:
        print(f"Could not read customers: {err}\n")
        return []


def prompt_non_empty(label: str) -> str:
    while True:
        value = input(label).strip()
        if value:
            return value
        print("This field cannot be blank. Please try again.")


def prompt_phone() -> str:
    while True:
        raw = input("Phone: ").strip()
        digits_only = "".join(ch for ch in raw if ch.isdigit())
        if len(digits_only) >= PHONE_MIN_DIGITS:
            return raw
        print(f"Phone number must include at least {PHONE_MIN_DIGITS} digits. Try again.")


def add_customer() -> None:
    print("\n--- Add Customer ---")
    name = prompt_non_empty("Customer name: ")
    phone = prompt_phone()
    address = prompt_non_empty("Address: ")
    notes = input("Notes (optional): ").strip()

    ensure_csv_file()
    try:
        with CSV_FILE.open("a", newline="") as file:
            csv.writer(file).writerow([name, phone, address, notes])
    except OSError as err:
        print(f"Failed to save customer: {err}\n")
        return

    print(f"{name} added successfully!\n")


def format_table(rows: List[Dict[str, str]]) -> str:
    widths = {header: len(header) for header in CSV_HEADERS}
    for row in rows:
        for header in CSV_HEADERS:
            widths[header] = max(widths[header], len(row.get(header, "")))

    def build_line(parts: List[str]) -> str:
        return " | ".join(
            f"{part:<{widths[header]}}" for part, header in zip(parts, CSV_HEADERS)
        )

    header_line = build_line(CSV_HEADERS)
    divider = "-+-".join("-" * widths[header] for header in CSV_HEADERS)
    body_lines = [build_line([row.get(header, "") for header in CSV_HEADERS]) for row in rows]
    return "\n".join([header_line, divider, *body_lines])


def view_customers() -> None:
    print("\n--- Customer List ---")
    customers = read_customers()
    if not customers:
        print("No customers recorded yet.\n")
        return
    print(format_table(customers))
    print()


def search_customer() -> None:
    print("\n--- Search Customers ---")
    term = input("Enter name, phone, or address: ").strip().lower()
    if not term:
        print("Search term cannot be empty.\n")
        return

    matches = []
    for customer in read_customers():
        blob = " ".join(customer.get(header, "") for header in CSV_HEADERS).lower()
        if term in blob:
            matches.append(customer)

    if matches:
        print(format_table(matches))
        print()
    else:
        print("No matching customers found.\n")


def main() -> None:
    actions = {
        "1": add_customer,
        "2": view_customers,
        "3": search_customer,
    }

    while True:
        print("\n" + "=" * 40)
        print("HVAC CUSTOMER TRACKER".center(40))
        print("=" * 40)
        print("1. Add customer")
        print("2. View all customers")
        print("3. Search customer")
        print("4. Exit")
        print("=" * 40)

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "4":
            print("\nGoodbye! 👋\n")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("\n❌ Invalid choice. Please enter 1-4.\n")


if __name__ == "__main__":
    main()
