# Meal Time

def main():
	# asking for user input, stripping whitespace, calling convert()
	number_of_hours = convert(input("Time:").strip())

	# checking for breakfast time between 7 and 8 o'clock
	if 8 >= number_of_hours >= 7: 
		print("breakfast time")

	# checking for breakfast time between 12 and 13 o'clock
	elif 13 >= number_of_hours >= 12:
		print("lunch time")

	# checking for breakfast time between 18 and 19 o'clock
	elif 19 >= number_of_hours >= 18:
		print("dimmer time")



def convert(time):
	"""
	Converts a str containing a time to a floating point value.

	Args:
		time (str): a str containing a time formatted like "%H:%M".

	Returns:
		float: a floating point value representing the given time
		as floating point number of hours.
	"""

	# splitting time into hours and minutes
	hours, minutes = time.split(":")

	# return calculated floating point reprepresentation of given time
	return float(int(hours) + int(minutes) / 60)


if __name__ == "__main__":
	main()