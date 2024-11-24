# Home Federal Savings Bank

def main():
	# asking user for input and calling .lower() method
	given_greeting = input("Greeting: ").lower()

	# checking for beginning with "hello"
	if given_greeting.startswith("hello"):
		print("0$")
	
	# checking for beginning with "h"
	elif given_greeting.startswith("h"):
		print("20$")

	# printing "100$" otherwise
	else:
		print("100$")

if __name__ == "__main__":
	main()