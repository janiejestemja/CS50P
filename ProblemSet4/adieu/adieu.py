# Adieu, Adieu

from inflect import engine 

def main():
    # assigning variable p per inflect documentation
    p = engine()

    # defining empty list 
    names = []

    # starting infinte loop for multiline input
    while True:
        
        # trying to get user input
        try:
            name = input("")

        # handling EOFError
        except EOFError:
            # assign formatted_names variable per inflect documentation
            formatted_names = p.join(names)
            # breaking the input loop
            break

        else:
            # appending the line inputted by the user to the list
            names.append(name)

    print("Adieu, adieu, to", formatted_names)


if __name__ == "__main__":
    main()
