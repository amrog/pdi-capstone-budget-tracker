from budget_tracker import set_budget, add_expense, view_expenses, calculate_total, compare_with_budget

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
    prompt = 'what\'s your choice'

    print("\nBudget Tracker Menu:")
    print("1. Set Budget")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Total Expenses")
    print("5. Compare with Budget")
    print("Q. Quit")

    while True:  # Loop until valid input is received
        choice = input(f"{prompt}: ").strip().upper()
        if choice in ['1', '2', '3', '4', '5', 'Q']:
#            return choice
#        choice = input(f"{prompt}: ").strip()
#        if len(choice) == 1 and '1' <= choice <= '6':
            return choice
        else:
            print(f"Invalid choice: {choice}. Please enter a number between 1 and 6.")

def main():
    """
    Greets the user and runs the budget tracker.
    """
    greeting()
    print (f"your choice was {menu()}")

if __name__ == "__main__":
	main()
