# Pizza Py

import os
import sys 
import csv
from tabulate import tabulate

def main():
    # checking for amount of command line arguments (cla)
    if len(sys.argv) != 2: 
        sys.exit("Unexpected amount of commandlinearguments.")

    # checking for file name extension
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Unexpected fileending.")

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
            reader = csv.DictReader(f)

            # printing formatted output
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))
    
    # handling exception
    except FileNotFoundError:
        sys.exit("File not found.")

if __name__ == "__main__":
    main()