from menu import menu


def greeting():
	"""
	Prints a greeting message to the user.
	"""
	print("Hello Aaron, this is your budget tracker.")

def main():
	"""
	Greets the user and runs the budget tracker.
	"""
	greeting()
	print (f"your choice was {menu('what\'s your name')}")

if __name__ == "__main__":
	main()
