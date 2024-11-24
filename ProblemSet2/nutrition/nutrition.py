# Nutrition Facts

def main():
	# asking user for input and forcing it to lowercase
	fruit_name = input("Item: ").strip().lower()

	if calories_of_fruit(fruit_name):
		print(f"Calories: {calories_of_fruit(fruit_name)}")

def calories_of_fruit(fruit_name):
	"""
	Checks in a dictionary containing fruits and their calories per portion
	(source: "https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/raw-fruits-poster-text-version-accessible-version").
	
	Args:
		fruit_name (str): a str that might or might not be a fruit name.

	Returns:
		calories (int/None): colories per portion of the fruit and None if fruit is not found in dictionary.
	"""
	fruit_calories_per_portion = {
	"apple": 130,
	"avocado": 50, 
	"banana": 110,
	"cantaloupe": 50,
	"grapefruit": 60,
	"grapes": 90,
	"honeydow melon": 50,
	"kiwifruit": 90,
	"lemon": 15,
	"lime": 20,
	"nectarine": 60,
	"orange": 80,
	"peach": 60,
	"pear": 100,
	"pineapple": 50,
	"pums": 70,
	"strawberries": 50,
	"sweet cherries": 100,
	"tangerine": 50,
	"watermelon": 80,
	}

	# if fruit is in dictionary returning the corresponding calories per poriton
	if fruit_name in fruit_calories_per_portion:
		return fruit_calories_per_portion[fruit_name]
	# otherwise return None
	else:
		return None

if __name__ == "__main__":
	main()