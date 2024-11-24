# Tip Calculator 

def main():
    # asking user twice for input and calling helperfunctions
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # calculating result
    tip = dollars * percent

    # printing the result
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """
    Removes '$' prefix of a str containing a number.

    Parameters:
    d (str): A str containing a number with '$' as prefix.

    Returns:
    float: A float containing the value in the given str.
    """
    return float(d.removeprefix("$"))


def percent_to_float(p):
    """
    Removes '%' suffix of a str containing a number.

    Parameters: 
    p (str): A str containing a number with '%' as suffix.

    Returns:
    float: A float containing the value of the given str.
    """
    return float(p.removesuffix("%")) * 0.01


main()
