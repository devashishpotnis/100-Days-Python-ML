import json
import os

FILE_NAME = "expenses.json"

# Load data
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Save data
def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

# Add expense
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc.): ")
    note = input("Enter note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")

# View expenses
def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']}")

# Total expense
def total_expense():
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses)
    print(f" Total Expense: ₹{total}")

# Filter by category
def filter_category():
    category = input("Enter category to filter: ")
    expenses = load_expenses()

    filtered = [e for e in expenses if e["category"].lower() == category.lower()]

    if not filtered:
        print("No records found.")
        return

    for exp in filtered:
        print(f"₹{exp['amount']} | {exp['note']}")

# Menu
def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Filter by Category")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            filter_category()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()