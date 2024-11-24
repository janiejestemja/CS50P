# CS50 Shirtificate

from fpdf import FPDF, XPos, YPos, Align

def main():
    """
    Prompt the user for their name and generate a CS50 shirtificate.

    The function asks for the user's name, then calls `make_shirtificate()` 
    to create a PDF with a personalized message.
    """
    name = input("Name: ").strip()
    make_shirtificate(name)

def make_shirtificate(name):
    """
    Create a PDF shirtificate with the provided name.

    This function generates a "shirtificate" PDF using the `fpdf` library. 
    The PDF contains the title "CS50 Shirtificate" and a message with the 
    user's name indicating they took CS50. The PDF is saved as "shirtificate.pdf".

    Args:
        name (str): The name of the person to include on the shirtificate.

    Raises:
        RuntimeError: If there is an error creating or saving the PDF.
    """
    shirt_print = name + " took CS50"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", "UI", 36)
    pdf.cell(
        w=200, h=47, text="CS50 Shirtificate", 
        align=Align.C, center=True, 
        new_x=XPos.LEFT, new_y=YPos.NEXT,
        )
    pdf.image(
        "shirtificate.png", w=200, keep_aspect_ratio=True
    )
    pdf.set_x(0)
    pdf.set_y(47)
    pdf.set_font("Helvetica", "", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(
        w=200, h=140, text=shirt_print, 
        align=Align.C, center=True, 
        new_x=XPos.LEFT, new_y=YPos.NEXT,
        )

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
