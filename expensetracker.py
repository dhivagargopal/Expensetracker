import json
import csv
from datetime import datetime
import os

DATA_FILE = "expenses.json"

# ------------------- Data Handling -------------------
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

# ------------------- Core Features -------------------
def add_expense():
    try:
        amount = float(input("Enter amount: $"))
        category = input("Enter category (Food, Travel, etc.): ").strip()
        note = input("Enter note (optional): ").strip()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        expenses = load_expenses()
        expenses.append({
            "amount": amount,
            "category": category,
            "note": note,
            "date": date
        })
        save_expenses(expenses)
        print("✅ Expense added successfully!\n")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.\n")

def view_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    total = sum(exp["amount"] for exp in expenses)
    print(f"💰 Total Expenses: ${total:.2f}")
    print("By Category:")
    category_totals = {}
    for exp in expenses:
        category_totals[exp["category"]] = category_totals.get(exp["category"], 0) + exp["amount"]

    for category, amt in category_totals.items():
        print(f"  - {category}: ${amt:.2f}")
    print()

def export_to_csv():
    expenses = load_expenses()
    if not expenses:
        print("No expenses to export.\n")
        return

    filename = f"expenses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["amount", "category", "note", "date"])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"📄 Expenses exported to {filename}\n")

# ------------------- CLI Menu -------------------
def main():
    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Export to CSV")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            export_to_csv()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
