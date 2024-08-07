import json
from datetime import datetime

# File to store expenses
EXPENSE_FILE = 'expenses.json'

# Load existing expenses from file
def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    try:
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        category = input("Enter the category (e.g., Food, Transportation, Entertainment): ")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        expense = {
            'amount': amount,
            'description': description,
            'category': category,
            'date': date
        }
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

# Display expenses
def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} - {expense['category']}: ${expense['amount']} - {expense['description']}")

# Display monthly summary
def display_monthly_summary(expenses):
    monthly_summary = {}
    
    for expense in expenses:
        month = expense['date'][:7]  # Extract "YYYY-MM" from the date
        monthly_summary[month] = monthly_summary.get(month, 0) + expense['amount']
    
    if not monthly_summary:
        print("No expenses recorded.")
        return

    print("Monthly Summary:")
    for month, total in monthly_summary.items():
        print(f"{month}: ${total:.2f}")

# Display category-wise summary
def display_category_summary(expenses):
    category_summary = {}

    for expense in expenses:
        category = expense['category']
        category_summary[category] = category_summary.get(category, 0) + expense['amount']
    
    if not category_summary:
        print("No expenses recorded.")
        return

    print("Category-wise Summary:")
    for category, total in category_summary.items():
        print(f"{category}: ${total:.2f}")

# Main function to run the Expense Tracker
def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. View Monthly Summary")
        print("4. View Category-wise Summary")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            display_monthly_summary(expenses)
        elif choice == '4':
            display_category_summary(expenses)
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
