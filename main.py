from menu import menu


def greeting():
	"""
	Prints a greeting message to the user.
	"""
	print("Hello Aaron, this is your budget tracker.")

def menu(prompt):
    """
    Displays a menu of options and gets user input.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        str: The user's choice from the menu.
    """
    print("\nBudget Tracker Menu:")
    print("1. Set Budget")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Total Expenses")
    print("5. Compare with Budget")
    print("6. Quit")

    while True:  # Loop until valid input is received
        choice = input(f"{prompt}: ")
        if choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def main():
	"""
	Greets the user and runs the budget tracker.
	"""
	greeting()
	print (f"your choice was {menu('what\'s your name')}")

if __name__ == "__main__":
	main()
