#def menu(a):
 #   return input(a)


def set_budget():
    """Allows the user to set a monthly budget."""
    while True:
        try:
            budget = float(input("Enter your monthly budget: "))
            if budget > 0:
                return budget
            else:
                print("Budget must be a positive number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_expense():
    """Allows the user to add a new expense."""
    description = input("Enter expense description: ")
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount > 0:
                return description, amount
            else:
                print("Expense amount must be a positive number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def view_expenses(expenses):
    """Displays all recorded expenses."""
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nYour expenses:")
        for description, amount in expenses:
            print(f"- {description}: ${amount:.2f}")

def calculate_total(expenses):
    """Calculates the total of all expenses."""
    return sum(amount for _, amount in expenses)

def compare_with_budget(total, budget):
    """Compares total expenses with the set budget."""
    remaining = budget - total
    if remaining >= 0:
        print(f"\nYou are ${remaining:.2f} under budget.")
    else:
        print(f"\nYou are ${-remaining:.2f} over budget.")
