# CS50 P-Shirt

import os
import sys
from PIL import Image, ImageOps

def main():

    # checking for amount of command line arguments (cla)
    if len(sys.argv) != 3:
        sys.exit("Unexpected amount of command line arguments(expecting 2)")

    # definition of accepted extension
    accepted_extensions = [".jpg", ".jpeg", ".png"]

    # setting empty string to extranct extension
    im_extension = ""

    # looping through accepted extensions
    for extension in accepted_extensions:
        # checking for similar endings in per cla given filenames
        if sys.argv[1].endswith(extension) and sys.argv[2].endswith(extension):
            # concatenation of extension to previously empty str
            im_extension = im_extension + extension

    # checking for string being still empty
    if im_extension == "":
        # exiting because of different extentions
        sys.exit("Input and Output have different extensions.")


    # checking supposed filelocation
    source_image = os.path.join(os.getcwd(), sys.argv[1])

    # checking for existence
    if not os.path.exists(source_image):
        sys.exit("File location not found.")
    
    # checking for being a file
    if not os.path.isfile(source_image):
        sys.exit("Path does not lead to a file.")

    # defintion of path to output
    output_image = os.path.join(os.getcwd(), sys.argv[2])
    
    # locating path to current directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # locating the shirt.png file
    p_shirt_loc = os.path.join(dir_path, "shirt.png")
    
    # if shirt not found exiting the programm
    if not os.path.exists(p_shirt_loc):
        sys.exit("Sorry, out of P-Shirts (file 'shirt.png' not found by os).")

    # trying to find the image file
    try:
        with Image.open(source_image) as im:
            imported_im = im.convert("RGBA")

    # handling excepting
    except OSError:
        sys.exit("Trouble opening the inputted image.")

    # trying to find the shirt
    try: 
        with Image.open(p_shirt_loc) as im:
            shirt = im.convert("RGBA")

    # handling exception
    except FileNotFoundError:
        sys.exit("Sorry, out of P-Shirts (file 'shirt.png' not found by Pil).")

    # fitting image sizes
    imported_im = ImageOps.fit(imported_im,(shirt.size))

    # putting on the shirt
    imported_im.paste(shirt, shirt)

    # conversion to RGB because alpha is not needed anymore
    im = imported_im.convert("RGB")
    
    # saving manipulated file
    im.save(output_image)
    
    # closing closet (or the path to the shirt.png...)
    shirt.close()


if __name__ == "__main__":
    main()