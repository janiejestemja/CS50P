# Just setting up my twttr

def main():
	# definition of vowels
	vowels = ["a", "e", "i", "o", "u"]

	# asking user for input
	user_input = input("Input: ")

	# setting empty str as output 
	output = ""
	# looping through characters in users input
	for character in user_input:
		# concatenation of character to output-str if not in vowels
		if character.lower() not in vowels:
			output = output + character
		# otherwise continuation of the loop
		else:
			continue
	# printing output after looping through all characters
	print("Output: ", output)

if __name__ == "__main__":
	main()