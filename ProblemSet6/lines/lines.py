# Lines of Code

import os
import sys

def main():
    # checking for amount of command line arguments (cla)
    if len(sys.argv) != 2: 
        sys.exit("Unexpected amount of commandlinearguments.")
    
    # checking supposed filelocation
    sup_f_loc = os.path.join(os.getcwd(), sys.argv[1])

    # checking for existence 
    if not os.path.exists(sup_f_loc):
        sys.exit("File location not found.")
    
    # checking for being a file
    if not os.path.isfile(sup_f_loc):
        sys.exit("Path does not lead to a file.")

    # trying to open the file
    try:   
        with open(sup_f_loc) as f:
            reader = f.readlines()

    # handling exception
    except FileNotFoundError:
        sys.exit("File not found.")

    else:
        # setting up counter
        count = 0
        # looping through lines in the file
        for line in reader:
            # filtering empty lines and lines starting with '#'
            if line.strip() == "" or line.strip().startswith("#"):
                continue
            # otherwise incrementing counter
            else:
                count += 1
                
        # printing the count
        print(count)

if __name__ == "__main__":
    main()