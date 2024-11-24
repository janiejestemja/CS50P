# Outdated

def main():

	# list with names of months
	months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]	
	# creating a dict with enumerated months as key value pairs
	months_dict = {month: str(number + 1) for number, month in enumerate(months)}

	# setting up infinite loop
	while True:
		# asking user for input forcing it to titlecase
		user_input = input("Date: ").strip().title()

		# trying to split users input into three strings
		try:
			month, day, year = user_input.split("/")

		# handling ValueError
		except ValueError:
			# trying to split users input into two strings
			try:
				month_and_day, year = user_input.split(",")

			# passing by ValueError
			except ValueError:
				pass

			else:
				# trying to split substring month_and_day into two strings
				try:
					month, day = month_and_day.split(" ")

				# passing by ValueError
				except ValueError:
					pass

				else:
					# checking for month being in the month_dict
					if month in months_dict:
						# if so replacing it with associated number
						month = months_dict[month]
						
						# checking the combination of number being a date
						if date_validation(year, month, day):

							# printing the date in requested format
							print(f"{year.strip()}-{month}-{day.strip()}")

							# breaking the infinite loop
							break

					else:
						# reprompting user after all validation checks failed
						continue

		else:
			# checking the combination of number being a date
			if date_validation(year, month, day):
				# printing the date in requested format
				print(f"{year}-{month}-{day}")
				break

			else:
				# reprompting user after all validation checks failed
				continue


def date_validation(year, month, day):
	"""
	Validates dates in a very simplified way.

	Args:
		year (str, int): A number representing a year.
		month (str, int): A number representing a month.
		day (str, int): A number representing a day.

	Returns: 
		bool: Truthvalue of validation of the given date.
	"""

	# trying to typeforcing arguments to int
	try:
		day = int(day)
		month = int(month)
		year = int(year)

	# handling ValueErrors by returning False because validation failed
	except ValueError:
		return False

	else:
		# checking month and day for being in range and returning True if so
		if month in range(1, 13) and day in range(1, 32):
			return True
		else:
			# otherwise returning False because validation failed
			return False

if __name__ == "__main__":
	main()