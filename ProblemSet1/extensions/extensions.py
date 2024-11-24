# File Extensions

def main():
	# defining valid extensions 
	accepted_extensions = {
	"gif":"image/gif",
	"jpg":"image/jpeg",
	"jpeg": "image/jpeg",
	"png": "image/png",
	"pdf": "application/pdf",
	"txt": "text/plain",
	"zip": "application/zip",
	}
	# getting user input forced to lowercase
	user_input = input("Filename: ").lower()
	# splitting user input into filename and extension
	filename, extension = user_input.rsplit(".", maxsplit=1)

	# checking if extension is an accepted extension
	if extension in accepted_extensions:
		# printing the mime type associated with it
		print(accepted_extensions[extension])

	else:
		# printing default otherwise
		print("application/octet-stream")

if __name__ == "__main__":
	main()