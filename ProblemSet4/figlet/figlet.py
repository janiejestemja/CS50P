# Frank, Ian and Glens's letters

import sys
from random import choice
from pyfiglet import Figlet

def main():
	# assinging figlet variable per instructions in hints-section
	figlet = Figlet()

	# checking for invalid number of command line arguments (cla)
	if len(sys.argv) != 1 and len(sys.argv) != 3:
		sys.exit("Error: Unexpected number of commandlinearguments (expects none or two)")
	
	# checking for valid number of cla's
	if len(sys.argv) == 1:
		# picking a random font
		font = choice(figlet.getFonts())

	# checking for valid number of cla's 
	if len(sys.argv) == 3:
		# checking for first cla being neither "-f" nor "--font"
		if sys.argv[1] != "-f" and sys.argv[1] != "--font":

			# exiting via sys.exit
			sys.exit("Error: first commandlineargument should be either '-f' or '--font'.")

		# checking for second cla not being in fonts provided by pyfiglet
		elif sys.argv[2] not in figlet.getFonts():

			# exiting via sys.exit
			sys.exit("Error: chosen font not found.")

		else:
			# otherwise defining font as defined in cla
			font = sys.argv[2]

	# asking user for input
	user_input = input("Input: ")
	
	# setting font per instructions in hint section
	figlet.setFont(font=font)
	
	# printing users input formatted per pyfiglet
	print(figlet.renderText(user_input))

if __name__ == "__main__":
	main()