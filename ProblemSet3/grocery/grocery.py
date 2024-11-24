# Grocery List

def main():

	# defining an empty dict
	grocery_dict = dict()

	# initiating an infinte loop for multiline-input by exploitation of EOFError
	while True:

		# trying to get user input
		try:
			item = input("Item: ")
		
		# handling EOFError
		except EOFError:

			# printing a new line
			print(f"\n")

			# looping through the sorted dictionary
			for key in sorted(grocery_dict):

				# printing for every key in the dictionary the value of the key 
				# and the associated value
				print(grocery_dict[key], key.upper())

			# breaking the loop 
			break

		else:
			# if the user input is not in the dict yet, appending it to it and initialise it with the value of one.
			if item not in grocery_dict:
				grocery_dict[item] = 1
			
			# if the user input is already in the dict adding one to it's count
			else:
				grocery_dict[item] += 1

if __name__ == "__main__":
	main()