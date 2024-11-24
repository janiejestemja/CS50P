# Home Federal Savings Bank

def main():
	# asking user for input
	given_greeting = input("Greeting: ")
	# passing users input to value function and printing out 
	# formatted result
	print(f"{value(given_greeting)}$")

def value(greeting):
	"""
	Assigns a value to a string depending on what is starts with. 

	Args:
		greeting (str): A potential greeting.

	Returns:
		int: 0, 20, 100.

	Raises:
		ValueError: In case the argument is not a str.
	"""
	# checking type of argument and raising exception if not a str
	if type(greeting) != type(str()):
		raise ValueError("expecting a str()")
	
	# forcing argument to lowercase
	greeting = greeting.lower()

	# checking start of string and returning the respectively assigned value
	if greeting.startswith("hello"):
		return 0
	elif greeting.startswith("h"):
		return 20
	else:
		return 100

if __name__ == "__main__":
	main()