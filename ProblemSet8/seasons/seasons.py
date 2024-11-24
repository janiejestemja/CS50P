# Seasons of Love

import sys
import re
from inflect import engine
from datetime import date 


def main():
    """
    Prompt the user for a date and calculate the difference in minutes from the current date.

    Validates the user input, ensuring the date is in the correct format (YYYY-MM-DD).
    If the input is valid, it calculates the time difference in minutes and converts 
    it to words. If the input is invalid, the program exits with an error message.

    Raises:
        SystemExit: If the input is not in the correct format or if the date is invalid.
    """
    s = input("Date: ").strip()
    date_today = date.today()

    if match := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", s):

        try:
            a_date = date(
            year = int(match.group(1)), 
            month = int(match.group(2)), 
            day = int(match.group(3)), 
            )

        except ValueError:
            sys.exit("Invalid input")

        else:
            try:
                _ = func(date_today, a_date)
            except ValueError:
                sys.exit("Invalid input.")
            else:
                print(func(date_today, a_date))
    else:
        sys.exit("Invalid input.")


def func(date_today, a_date):
    """
    Calculate the difference in minutes between two dates and return it as a string in words.

    The function takes two `date` objects, calculates the difference in minutes between 
    them, and converts the result to a word string. It raises an error if the difference 
    is negative or if the input types are not `datetime.date`.

    Args:
        date_today (datetime.date): The current date.
        a_date (datetime.date): The date to compare against the current date.

    Returns:
        str: The difference in minutes expressed in words.

    Raises:
        ValueError: If either of the input values are not `datetime.date` or if `a_date` is in the future.
    """
    # input validation
    teda = date(year=1, month=1, day=1)
    if type(date_today) != type(teda) or type(a_date) != type(teda):
        raise ValueError("func only accepts arguments of type datetime.date")
    p = engine()
    delta = date_today - a_date 
    if delta.days < 0:
        raise ValueError("given date is in the future.")
    return p.number_to_words(delta.days * 24 * 60, andword="") + " minutes."


if __name__ == "__main__":
    main()