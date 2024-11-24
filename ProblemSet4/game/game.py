# Guessing Game

from random import randint

def main():
    # infinite loop to reprompt the user
    while True:

        # trying to ask user for input and typeforcing the input to int
        try:
            level = int(input("Level: "))

        # passing by ValueError to repromt user
        except ValueError:
            pass

        else:
            # otherweise generating a random number between one and the users input
            solution = randint(1, level)

            # exiting the input loop
            break

    # gameloop
    while True:

        # trying to typeforce users input 
        try:
            guess = int(input("Guess: "))
        
        # handling ValueError to reprompt user if typeforcing failed
        except ValueError:
            pass
        
        else:
            # otherwise giving the user hints
            if guess > solution:
                print("Too small!")

            elif guess < solution:
                print("Too large!")

            # in the case of the user guessed the randomly generated number 
            # printing the success and exiting the gameloop
            else:
                print("Just right!")
                break

if __name__ == "__main__":
    main()