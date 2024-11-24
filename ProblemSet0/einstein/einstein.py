# Einstein

# E = mc²

def main(): 
	# aksing user for input 
	mass = int(input("mass: "))
	# printing the result of calculation
	print(mass * pow(300_000_000, 2)) # assuming c = 300_000_000

if __name__ == "__main__": 
	main()