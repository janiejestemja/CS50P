# Bitcoin Price Index

import requests
import sys

def main():
    # checking length of command line arguments (cla)
    if len(sys.argv) != 2:
        # exiting via sys.exit 
        sys.exit("No command line argument provided(expecting a floating point number).")
    
    # trying to typeforce cla to float
    try:
        float(sys.argv[1])

    # handling ValueError
    except ValueError:
        # exiting via sys.exit
        sys.exit("Unexpected command line argument provided(expecting a floating point number).")

    else: 
        # trying to do a request per requests documentation
        try: 
            r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        
        # handling exeptions per requests documentation
        except requests.exceptions.RequestException:
            sys.exit("Something went wrong while getting the request.")
        
        else: 
            # trying to decode the response expected in json
            try: 
                r = r.json()
            
            # handling exeptions per requests documentation
            except requests.exceptions.JSONDecodeError:
                sys.exit("Decoding of the response failed.")

            else:
                # assigning a variable to the value in the response we are interested in
                rate_float = r["bpi"]["USD"]["rate_float"]

                # calculating and printing the result of current bitcoin rate multiplied by the number given as cla
                print(f"${rate_float * float(sys.argv[1]):,.4f}")


if __name__ == "__main__":
    main()