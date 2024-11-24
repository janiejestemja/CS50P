# Just setting up my twttr

def main():
	# asking user for input
	user_input = input("Input: ")

	print(shorten(user_input))

def shorten(word):
	"""
	Shortens a word by ommiting vowels.

	Args:
		word (str): A word or multiple.

	Returns:
		str: A str containing the word without vowels
	"""
	# definition of vowels
	vowels = ["a", "e", "i", "o", "u"]

	# setting empty str as output 
	output = ""
	# looping through characters in users input
	for character in word:
		# concatenation of character to output-str if not in vowels
		if character.lower() not in vowels:
			output = output + character
		# otherwise continuation of the loop
		else:
			continue
	
	# returning output after looping through all characters
	return output

if __name__ == "__main__":
	main()