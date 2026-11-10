expenses = []


def add_expense():

    name = input("Enter expense name: ")

    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():

    print("\n======= EXPENSES =======")

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:

        print(expense["name"], ":", expense["amount"])


def total_expenses():

    total = sum(expense["amount"] for expense in expenses)

    print("Total Expenses:", total)


while True:

    print("\n===== EXPENSE TRACKER =====")

    print("1. Add Expense")

    print("2. View Expenses")

    print("3. Total Expenses")

    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")