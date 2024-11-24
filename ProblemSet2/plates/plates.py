# Vanity Plates

def main():
    
    # asking user for input 
    plate = input("Plate: ")
    
    # printing either "Valid" or "Invalid" depending of the return value of is_valid
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """
    Checks simplified for validity of a str to be accepted as a vanity plate in Massachusetts
    
    Args:
        s (str): a str representing a potential vanity plate

    Returns: 
        bool: Truthvalue of the question if str is a valid vanity plate
    """

    # lengthcheck
    if not len(s) in range(2, 7) or not s.isalnum():
        return False

    # first two letters check
    if not s[0:2].isalpha():
        return False

    # numbers check
    for i in range(1, len(s)):
        # check if character is a number
        if s[i - 1].isnumeric() and s[i].isalpha():
            return False

    # check if first number is zero
    for i in range(1, len(s)):
        if s[i - 1].isalpha() and s[i] == "0":
            return False

    # because all checks went through just return true
    return True


if __name__ == "__main__":
	main()