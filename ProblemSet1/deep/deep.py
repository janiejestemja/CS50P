# Deep Thought

def main():
	# asking user for input and forcing it to lowercase
	user_input = input("What is the Answer to the Great Qestion of Life, the Universe, and Everything?: ").lower()
	# cecking disjunction of conditions 
	if user_input == "42" or user_input == "forty two" or user_input == "forty-two":
		# printing yes if a condition is met
		print("Yes")

	else:
		# printing no otherwise
		print("No")

if __name__ == "__main__":
	main()