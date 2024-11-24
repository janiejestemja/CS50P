# Regular, um, Expressions

import re

def main():
    print(count(input("Text: ")))

def count(s):
    """
    Counts occurences of 'um'. 

    Args:
        s (str): A str potentially containing multiple 'um's.

    Returns:
        int: Number of occurences of 'um'.
    """

    # enforcing lowercase
    string = s.lower()
    # application of re.findall per it's documentation
    if matches := re.findall(r"(\bum\b)", string, re.IGNORECASE):
        # returning the length of matches to count the occurences of 'um'
        return len(matches)
    # otherwise returning zero because there are no occurences of 'um'
    else:
        return 0


if __name__ == "__main__":
    main()