# Fuel Gauge

def main():
	# setting up infinite loop
	while True:
		# asking for input
		fraction = input("Fraction: ").strip()

		try:
			# trying conversion 
			percentage = convert(fraction)

		# passing by exceptions
		except (ValueError, ZeroDivisionError):
			pass
		# priting result
		else:
			print(gauge(percentage))

def convert(fraction):
	"""
	Converts a fraction to a number.

	Args:
		fraction (str): A str in X/Y format where X an Y are integers.

	Returns:
		int: Nearest int between 0 and 100, inclusive.

	Raises:
		ValueError: If X is greater than Y.
		ZeroDivisionError: If Y is zero.
	"""
	# splitting input into nominator and denominator
	nominator, denominator = fraction.split("/")

	# trying typoforcing input
	try:
		nominator = int(nominator)
		denominator = int(denominator)
	# handling exception
	except ValueError:
		raise ValueError("given variables are not recognized as integers.")

	else:
		# trying division
		try:
			result = nominator / denominator

		# handling exception
		except ZeroDivisionError:
			raise ZeroDivisionError("we do not divide through zero.")

		else:
			# multiplying number by hundret, rounding to nearest int and returning result
			result = result * 100
			return round(result)

def gauge(percentage):
	"""
	Represents a fuel-gauge.

	Args:
		percentage (int/float): A number.

	Returns:
		str: A str representing the output of a fuel-gauge.
	"""
    
	# chcking for fullness and emptyness
	if percentage > 99:
		return "F"

	elif percentage < 1:
		return "E"

	# if neither full nor empty printing percentage per formatstring.
	else:
		return f"{percentage}%"


if __name__ == "__main__":
	main()