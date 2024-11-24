# camelCase

def main():
	# asking for user input and stripping whitespace
	camel_cased_variable = input("camelCase: ").strip()
	
	# looping through caracters in user input
	for character in camel_cased_variable:

		# if character is lower printing charcter
		if character.islower():
			print(character, end="")

		# if character is upper replacing it with the 
		# same character in lower prefixed with an underscore
		elif character.isupper():
			print("_" + character.lower(), end="")

		# catch all where character gets printed
		else:
			print(character, end="")
			
	# printing new line
	print("")

if __name__ == "__main__":
	main()