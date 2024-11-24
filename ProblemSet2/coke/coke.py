# Choke Machine

def main():
	# defining valid denominations as a list
	valid_denominations = [5, 10, 25]

	# initialising price of a coke
	amount_due = 50

	# looping until price is payed
	while amount_due > 0:

		# printing current amount due
		print(f"Amount due: {amount_due}")

		# typeforcing inserted coin to int
		inserted_coin = int(input("Insert coin: "))

		# checking if inserted coin is valid
		if inserted_coin in valid_denominations:
			# subtracting inserted amount from current due
			amount_due = amount_due - inserted_coin

	# checking if amount due is payed
	if amount_due <= 0:
		# printing change owed even if it is zero
		print(f"Change owed: {-1 * amount_due}")

if __name__ == "__main__":
	main()