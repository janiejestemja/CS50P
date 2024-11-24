# Making Faces

# Slightly Smiling Face
# 🙂

# Slightly Frowning Face
# 🙁 

def main():
	 # asking user for input and calling twice .replace() method
	user_input = input().replace(":)", "🙂").replace(":(", "🙁")
	print(user_input)

if __name__ == "__main__":
	main()