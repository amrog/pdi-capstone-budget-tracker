from budget_tracker import (
    set_budget,
    get_expense_details,
    view_expenses,
    calculate_total,
    compare_with_budget,
)


def greeting():
    """
    Prints a greeting message to the user.
    """
    name = input("What is your name: ").strip()
    print(f"Welcome to the Budget Tracker {name}!")


def menu():
    """
    Displays a menu of options and gets user input.

    Args:
        None
    Returns:
        str: The user's choice from the menu.
    """
    prompt = "what's your choice"

    print("\nBudget Tracker Menu:")
    print("1. Set Budget")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Total Expenses")
    print("5. Compare with Budget")
    print("Q. Quit")

    while True:  # Loop until valid input is received
        choice = input(f"{prompt}: ").strip().upper()
        if choice in ["1", "2", "3", "4", "5", "Q"]:
            #            return choiceAa
            #        choice = input(f"{prompt}: ").strip()
            #        if len(choice) == 1 and '1' <= choice <= '6':
            return choice
        else:
            print(f"Invalid choice: {choice}. Please enter a number between 1 and 6.")



def expense_tracker():
    expenses = []
    budget = 0
    
    while True:
        choice = menu()
        if choice == "1":
            budget = set_budget()
            print(f"Budget set to ${budget:.2f}")
        elif choice == "2":
            description, amount = get_expense_details()
            if amount > budget:
                print(f"Expense amount ${amount:.2f} is greater than the budget ${budget:.2f}. Please try again.")
                continue
            expenses.append((description, amount))
            print(f"Added expense: {description} ${amount:,.2f}, there are now {len(expenses)} expenses.")

        elif choice == "3":
            view_expenses(expenses)
        elif choice == "4":
            total = calculate_total(expenses)
            print(f"\nYou have {len(expenses)} expenses, totalling ${total:.2f}")
        elif choice == "5":
            compare_with_budget(total, budget)
        elif choice == "Q":
            print("Goodbye!")
            break


def main():
    """
    Greets the user and runs the budget tracker.
    """
    greeting()
    expense_tracker()


if __name__ == "__main__":
    main()
