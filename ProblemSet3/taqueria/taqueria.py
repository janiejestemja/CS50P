# Felipes Taqueria

def main():
	# initialising total with zero.
	total = 0

	# setting up infinite loop for multiline input
	while True:
		# trying to ask user for input
		try:
			item = input("Item: ").title()

		# handling EOFError by printing a new line and breaking the loop
		except EOFError:
			print("")
			break

		else:
			# calculating new total by calling helper_func
			total = total + helper_func(item)

			# printing the current total
			print(f"Total: {total}")

def helper_func(item):
	"""
	Checks if an item is on the given menu and returns the price.

	Args:
		item (str): A potential name of an item on the given menu.

	Returns:
		float: Price of the item if on the menu otherwise zero.
	"""

	# definition of the menu as a dict.
	menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

	# returning price associated with the item if it is on the menu
	if item in menu:
		return menu[item]

	else:
		# otherwise returning zero
		return 0


if __name__ == "__main__":
	main()