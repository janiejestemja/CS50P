# Fuel Gauge

def main():
	# starting infinite loop 
	while True:
		# asking for user input splitting it into nominator and denominator
		nominator, denominator = input("Fraction: ").strip().split("/")

		# trying to call helper_func
		try:
			result = helper_fuc(nominator, denominator)

		# handling exceptions 
		except (ValueError, ZeroDivisionError):
			pass

		else:
			# checking for returned type from function call if succeeded
			if type(result) == str():
				# printing the returned result as is if it is a str
				print(result)
			else:
				# otherwise printing out formatted returned result
				print(f"{result}%")


def helper_fuc(nominator, denominator):
	"""
	Calclutates a percentage out of division of a nominator and denominater 
	and handles possible ValueErrors as well as the ZeroDivisionError.

	Args: 
		nominator (int): A number.
		denominator (int): A number.

	Returns: 
		int: Integer between 1 and 99 representing the perce
		str: Either "F" if result > 99 or "E" if result < 1.

	Raises:
		ValueError: If one of the passed arguements is None 
		or passed arguments are not of type int.
		ZeroDivisionError: If denominator is zero.
	"""

	# checking arguments for None
	if nominator is None or denominator is None:
		raise ValueError("Given fraction is incomplete.")

	# trying typeforcing to int
	try:
		nominator = int(nominator)
		denominator = int(denominator)

	# handling exception
	except ValueError:
		raise ValueError("Given variables are not recognized as integers.")

	else:
		# trying division
		try:
			result = nominator / denominator

		# handling ZeroDivisionError
		except ZeroDivisionError:
			raise ZeroDivisionError("We do not divide through zero.")

		else:
			# multiplying result of division by 100
			result = result * 100

			# checking for result > 99
			if result > 99:
				return "F"

			# checking for result < 1
			elif result < 1:
				return "E"

			# otherwise return rounded result.
			else:
				return round(result)


if __name__ == "__main__":
	main()