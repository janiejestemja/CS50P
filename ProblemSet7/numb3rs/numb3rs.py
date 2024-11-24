# NUMB3RS

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """ 
    Simplified validation of IPv4 Adresses.

    Args:
        ip (str): A str potentially containing valid IPv4 Adress.
    
    Returns:
        bool: Result of validation.
    """

    # trying to extract substrings into a list
    try: 
        elements = list(ip.split("."))

    # handling exception
    except (ValueError, TypeError):
        return False

    else: 
        # trying to typeforce elements in the list
        try:
            numb3rs = list()

            for element in elements:
                numb3rs.append(int(element))

        # handling exception
        except ValueError:
            return False 

        else:
            # checking for correct length
            if len(numb3rs) == 4:

                # checking accepted ranges for numbers in the adress
                for numb3r in numb3rs:
                    if numb3r > 255:
                        return False

                    elif numb3r < 0:
                        return False

                    else:
                        # returning true after all checks were passed
                        return True
            else:
                # otherwise returning false
                return False


if __name__ == "__main__":
    main()