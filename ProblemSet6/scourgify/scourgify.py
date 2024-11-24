# Scourgify 

import sys
import os
import csv

def main():

    # checking for amount of command line arguments (cla)
    if len(sys.argv) != 3:
        sys.exit("Unexpected amount of commandlinearguments")
    
    # checking extensions of the names 
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("fileendings are not correct.")

    # setting path to input
    in_csv = os.path.join(os.getcwd(), sys.argv[1])

    # checking if path exists
    if not os.path.exists(in_csv):
        sys.exit("File location not found.")
    
    # checking if path leads to a file
    if not os.path.isfile(in_csv):
        sys.exit("Path does not lead to a file.")

    # setting path to output
    out_csv = os.path.join(os.getcwd(), sys.argv[2])

    # setting up a temporary list 
    temporary_list = []

    # trying to open the input file
    try:
        with open(in_csv) as f:
            reader = csv.DictReader(f)

            # appending data in file to the temporary list
            for element in reader:
                temporary_list.append(element)

    # handling exception
    except FileNotFoundError:
        sys.exit("input file could not be read.")

    # setting up empty list for output
    final_list = []

    # looping through temporary list
    for element in temporary_list:

        # extracting first and last names
        last, first = element["name"].split(", ")

        # extracting the house
        house = element["house"]

        # setting up dict per element
        student = {
            # injecting extracted information
            "first": first,
            "last": last,
            "house": house
        }

        # appending dict to final list
        final_list.append(student)

    # writing outputfile per csv module documentation
    with open(out_csv, "w") as f:
        fieldnames = ["first", "last", "house"]
        
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for student in final_list:
            writer.writerow(student)

if __name__ == "__main__":
    main()