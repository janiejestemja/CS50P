# Math Interpreter

def main():
	# asking user for input and splitting it into three variables
	x, y, z = input("Expression: ").strip().split(" ", maxsplit=2)
	
	# printing formatted result of interpreter function
	print(f"{interpreter(x, y, z):2}")

def interpreter(x, y, z):
	"""
	A basic calculator covering addition, subtraction, multiplication and division
	
	Args:
		x (int): is an integer
		y (chr): is str(+), str(-), str(*), or str(/)
		z (int): is an integer and not 0 if y = str(/)

	Returns:
		float: an interpretation of the given arguments rounded to the 
		first decimal point.
	"""
	
	# typeforcing x and y
	x = int(x)
	z = int(z)

	# matching y to operant
	match y:
		# handling multiplication
		case "*":
			return round(float(x * z), 1)
		# handling division
		case "/":
			return round(float(x / z), 1)
		# handling addition
		case "+":
			return round(float(x + z), 1)
		# handling subtraction
		case "-":
			return round(float(x - z), 1)
		# catch all for not defined operants
		case _ :
			raise ValueError("Operant not recogniced by interpreter.")

if __name__ == "__main__":
	main()