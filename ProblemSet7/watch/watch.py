# Watch on YouTube

import re

def main():
    print(parse(input("HTML: ").strip()))

def parse(s):
    """
    Extracts a url leading to a youtube video from html code containing one.

    Args:
        s (str): The html code block as a str.
    
    Returns:
        str: Another version of the url leading to the same content.
    """
    # applying re.search per its documentation
    if matches := re.search( 
        r"<iframe .*src=(?:'|\")https?://(?:www\.)?youtube\.com/embed/(.*)(?:'|\").*></iframe>", 
        s, re.IGNORECASE
        ):
        # returning reformatted url
        return "https://youtu.be/" + matches.group(1)

if __name__ == "__main__":
    main()