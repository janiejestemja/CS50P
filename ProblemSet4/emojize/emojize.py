# Emojize

import emoji

def main():
	# using emoji per emoji documentation passing user input directly as an argument
	print("Output:", emoji.emojize(input("Input: ")))

if __name__ == "__main__":
	main()