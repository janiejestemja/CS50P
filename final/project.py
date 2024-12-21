import sys
import os
import argparse
from PIL import Image, ImageDraw, ImageFont
from tabulate import tabulate
from pyfiglet import Figlet
import pygame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

color_names = ["white", "black"]
plot_types = ["scatter", "line", "bar"]
loan_models = ["amortizing", "annuity", "bullet"]
btn_img_dir = "btn_img"
plots_dir = "plots"
# Create a list to store plot names
plot_names = [[f"{loan}_{plot}" for plot in plot_types] for loan in loan_models]

def main():
    parser = argparse.ArgumentParser(description="A script to compare loan repayment plans.")

    # Add arguments with custom file check
    parser.add_argument("--principal", type=float, help="Loan amount (Principal).")
    parser.add_argument("--interest_rate", type=float, help="Interest rate (A number between 0 and 1).")
    parser.add_argument("--term", type=int, help="Loan term in years.")

    args = parser.parse_args()

    # Extracting command-line arguments
    command_line_args = []
    if args.principal:
        if args.principal <= 0:
            print("Principal is expected to be a number greater than zero.")
            sys.exit(1)
        command_line_args.append(args.principal)
    if args.interest_rate:
        if args.interest_rate <= 0:
            print("Interest rate is expected to be a value greater than zero.")
            sys.exit(1)
        elif args.interest_rate > 1:
            print("Interest rate is expected to be a value less than one.")
            sys.exit(1)
        command_line_args.append(args.interest_rate)
    if args.term:
        if args.term <= 0:
            print("Term is expected to be a value greater than zero.")
            sys.exit(1)
        command_line_args.append(args.term)

    args = parser.parse_args()

    # Checking if all necessary commandline arguments are provided
    if len(command_line_args) == 3:
        principal = command_line_args[0]
        interest_rate = command_line_args[1]
        term = command_line_args[2]
    # Calling for user input if not
    else:
        principal, interest_rate, term = get_input()

    if not os.path.exists(btn_img_dir):
        os.makedirs(btn_img_dir)  # Create the directory
        print(f"Directory '{btn_img_dir}' created.")

    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)  # Create the directory
        print(f"Directory '{plots_dir}' created.")


    create_btn_images(plot_types, loan_models)

    make_plots(principal, interest_rate, term)

    pygame_runner(principal, interest_rate, term)

def get_input():
    def get_valid_input(prompt, input_type, condition, error_message):
        while True:
            try:
                user_input = input_type(input(prompt))
            except ValueError:
                print(f"{error_message} ({input_type.__name__}).")
                continue
            if not condition(user_input):
                print(error_message)
            else:
                return user_input

    # Kapital
    principal = get_valid_input(
        "Principal: ",
        float,
        lambda x: x > 0,
        "Kapital is expected to be a floating point number greater than zero."
    )

    # Zinssatz
    interest_rate = get_valid_input(
        "Interest rate: ",
        float,
        lambda x: 0 < x <= 1,
        "Zinssatz is expected to be a floating point number between 0 and 1."
    )

    # Laufzeit
    term = get_valid_input(
        "Laufzeit: ",
        int,
        lambda x: x > 0,
        "Laufzeit is expected to be a positive integer."
    )

    return [principal, interest_rate, term]

def print_loan_plan(plan_type, principal, interest_rate, term_length):
    """
    Prints the detailed loan plan for the specified loan type.

    This function generates a loan repayment plan based on the loan type
    (Amortizing, Annuity, or Bullet) and prints it in a formatted table.

    :param plan_type: The loan type (0 for Amortizing, 1 for Annuity, 2 for Bullet).
    :type plan_type: int
    :param principal: The principal amount of the loan.
    :type principal: float
    :param interest_rate: The annual interest rate of the loan.
    :type interest_rate: float
    :param term_length: The duration of the loan in years.
    :type term_length: int
    """
    match plan_type:
        case 0:
            print(tabulate(amortizing_loan(principal, interest_rate, term_length, printing=True), headers="firstrow", tablefmt="grid"))
        case 1:
            print(tabulate(annuity_loan(principal, interest_rate, term_length, printing=True), headers="firstrow", tablefmt="grid"))
        case 2:
            print(tabulate(bullet_loan(principal, interest_rate, term_length, printing=True), headers="firstrow", tablefmt="grid"))
        case _:
            raise ValueError("Invalid loan plan type. Valid options are 0, 1, or 2.")

def print_loan_overview(principal, interest_rate, term_length):
    """
    Prints an overview of the loan details for different loan types.

    This function calculates and prints an overview table showing the differences
    between Amortizing, Annuity, and Bullet loans based on the provided parameters.

    :param principal: The principal amount of the loan.
    :type principal: float
    :param interest_rate: The annual interest rate of the loan.
    :type interest_rate: float
    :param term_length: The duration of the loan in years.
    :type term_length: int
    """
    loan_functions = [amortizing_loan, annuity_loan, bullet_loan]
    loan_types = ["Amortizing loan", "Annuity loan", "Bullet loan"]
    headers = ["Loan type", "Interest", "Repayment", "Installments", "Premium"]

    # Extract the relevant values for each loan type
    values = [func(principal, interest_rate, term_length, short=True) for func in loan_functions]

    premiums = [
        f"{0:.2f}",
        f"{values[1][0] - values[0][0]:,.2f}",
        f"{values[2][0] - values[0][0]:,.2f}"
    ]

    # Add premium values to each loan type's data
    for value, premium in zip(values, premiums):
        value.append(premium)

    # Add loan type names to the values list
    for loan_type, value in zip(loan_types, values):
        value.insert(0, loan_type)

    # Printing the overview table
    print(tabulate(values, headers=[header.capitalize() for header in headers], tablefmt="grid"))

def make_plots(principal: float, interest_rate: float, term_length: int):
    """
    Generates and saves plots for different loan types.

    This function creates scatter, line, and bar plots for three types of loans:
    Amortizing, Annuity, and Bullet, based on the loan parameters.

    :param principal: The principal amount of the loan.
    :type principal: float
    :param interest_rate: The annual interest rate of the loan.
    :type interest_rate: float
    :param term_length: The duration of the loan in years.
    :type term_length: int
    """

    # Helper function to generate different types of plots
    def create_plot(plot_type, x, *args, dataframe, name):
        """
        Creates a plot based on the plot type (scatter, line, or bar).

        :param plot_type: The type of plot (e.g., 'scatter', 'line', 'bar').
        :param x: The x-axis data column.
        :param args: The y-axis data columns.
        :param dataframe: The data to plot.
        :param name: The name of the plot.
        """
        plt.figure(figsize=(10, 6))
        for arg in args:
            if plot_type == "line":
                sns.lineplot(x=x, y=arg, label=arg.capitalize(), data=dataframe, alpha=0.75)
            elif plot_type == "scatter":
                sns.scatterplot(x=x, y=arg, label=arg.capitalize(), data=dataframe, alpha=0.5)
            elif plot_type == "bar":
                sns.barplot(x=x, y=arg, label=arg.capitalize(), data=dataframe, alpha=0.5)

        plt.title((name + "plot").capitalize())
        plt.xlabel(x.capitalize())
        plt.ylabel("Currency")
        plt.legend(loc="upper left")
        plt.grid(True)
        plt.savefig(os.path.join(plots_dir, f"{name}plot.png"))

    # Load the loan data into DataFrames
    amortizing_df = pd.DataFrame(amortizing_loan(principal, interest_rate, term_length, to_dict=True))
    annuity_df = pd.DataFrame(annuity_loan(principal, interest_rate, term_length, to_dict=True))
    bullet_df = pd.DataFrame(bullet_loan(principal, interest_rate, term_length, to_dict=True))

    # Generate the plots for each loan type and plot type
    for loan_type, plot_names_for_loan in zip(loan_models, plot_names):
        for plot_name, plot_type in zip(plot_names_for_loan, plot_types):
            if loan_type == "amortizing":
                create_plot(plot_type, "year", "interest", "repayment", "installment", dataframe=amortizing_df, name=plot_name)
            elif loan_type == "annuity":
                create_plot(plot_type, "year", "interest", "repayment", "installment", dataframe=annuity_df, name=plot_name)
            elif loan_type == "bullet":
                create_plot(plot_type, "year", "interest", "repayment", "installment", dataframe=bullet_df, name=plot_name)

def formatter(function):
    """
    A decorator to format the output of a loan calculation function.

    This decorator provides extended functionality for loan calculation functions.
    It can:
    - Format the results into a dictionary, table, or simple summary.
    - Calculate sums for repayment schedules.
    - Format the output for printing with `tabulate` library.

    :param function: The loan calculation function to be wrapped.
    :type function: Callable
    :param kwargs: Optional keyword arguments that control the behavior:
        - `to_dict`: If True, returns the results as a dictionary with headers as keys.
        - `printing`: If True, formats the results into a printable table.
        - `short`: If True, returns only the summed totals for repayments and installments.
    :type kwargs: dict
    :return: A formatted result based on the keyword arguments provided:
        - A dictionary if `to_dict` is True.
        - A printable table if `printing` is True.
        - A list of summed totals if `short` is True.
    :rtype: list, dict, or zip
    :raises NotImplementedError: If more than one keyword argument is provided.
    """
    # Definition of wrapper function
    def wrapper(*args, **kwargs):

        if len(kwargs) > 1:
            raise NotImplementedError("Max one keyword argument allowed.")

        table = function(*args)
        # Definition of headers for a table
        headers = ["year", "remaining_balance", "interest", "repayment", "installment"]

        if kwargs.get("to_dict", False):
            return {header: column for header, column in zip(headers, table)}

        if kwargs.get("printing", False):
            # Formatting for tabulate...
            for i, column in enumerate(table):
                if i <= 1:
                    column.append(0)
                # Calculation of sums
                else:
                    column.append(sum(column))

            # Convert all numbers to formatted strings
            formatted_table = [table[0]]
            for column in table[1:]:
                formatted_table.append([f"{x:,.2f}" for x in column])

            # Further formatting for tabulate
            formatted_table[0][-1] = "Totals"
            formatted_table[1][-1] = " "

            # Inserting headers
            for column, header in zip(formatted_table, headers):
                column.insert(0, header.capitalize())

            # Returning table ready for print
            return zip(*formatted_table)

        if kwargs.get("short", False):
            return [sum(column) for i, column in enumerate(function(*args)) if not i <= 1]

        # End of Wrapper function
        return table

    return wrapper

@formatter
def amortizing_loan(principal: float, interest_rate: float, term: int, **kwargs) -> list:
    """
    Calculate the repayment schedule for an amortizing loan.

    :param principal: The total amount of the loan
    :type principal: float
    :param interest_rate: The annual interest rate (as a decimal, e.g., 0.05 for 5%)
    :type interest_rate: float
    :param term: The loan term in years
    :type term: int
    :return: A list containing:
             - time_periods: List of time periods (1 through term)
             - remaining_balances: List of remaining balances after each payment
             - interests: List of interest payments for each period
             - repayments: List of repayment amounts (principal portions)
             - installments: List of total installments (principal + interest)
    :rtype: list
    """

    time_periods = [t + 1 for t in range(term)]
    repayments = [principal / term for _ in range(len(time_periods))]
    remaining_balances = [principal - sum(repayments[:i]) for i in range(len(repayments))]
    interests = [remaining_balance * interest_rate for remaining_balance in remaining_balances]
    installments = [repayment + interest for repayment, interest in zip(repayments, interests)]

    return [time_periods, remaining_balances, interests, repayments, installments]

def get_annuity_factor(interest_rate, term):
    return (pow((1 + interest_rate), term) * interest_rate) / (pow((1 + interest_rate), term) -1)

@formatter
def annuity_loan(principal: float, interest_rate: float, term: int, **kwargs) -> list:
    """
    Calculate the repayment schedule for an annuity loan.

    :param principal: The total amount of the loan
    :type principal: float
    :param interest_rate: The annual interest rate (as a decimal, e.g., 0.05 for 5%)
    :type interest_rate: float
    :param term: The loan term in years
    :type term: int
    :return: A list containing:
             - time_periods: List of time periods (1 through term)
             - remaining_balances: List of remaining balances after each payment
             - interests: List of interest payments for each period
             - repayments: List of repayment amounts (principal portions)
             - installments: List of total installments (constant payments)
    :rtype: list
    """
    time_periods = [t + 1 for t in range(term)]
    annuity = principal * get_annuity_factor(interest_rate, term)
    installments = [annuity for _ in range(term)]
    repayments = [(annuity - principal * interest_rate) * pow(1 + interest_rate, i) for i in range(term)]
    interests = [annuity - repayment for repayment in repayments]
    remaining_balances = [principal - sum(repayments[:i]) for i in range(len(repayments))]

    return [time_periods, remaining_balances, interests, repayments, installments]

@formatter
def bullet_loan(principal: float, interest_rate: float, term: int, **kwargs) -> list:
    """
    Calculate the repayment schedule for a bullet loan.

    :param principal: The total amount of the loan
    :type principal: float
    :param interest_rate: The annual interest rate (as a decimal, e.g., 0.05 for 5%)
    :type interest_rate: float
    :param term: The loan term in years
    :type term: int
    :return: A list containing:
             - time_periods: List of time periods (1 through term)
             - remaining_balances: List of remaining balances (unchanged until final payment)
             - interests: List of interest payments for each period
             - repayments: List of repayment amounts (0 until final payment)
             - installments: List of total installments (interest-only until final payment)
    :rtype: list
    """
    time_periods = [t + 1 for t in range(term)]
    interests = [principal * interest_rate for _ in range(term)]
    installments = [interest for interest in interests]
    installments[-1] = principal + principal * interest_rate
    repayments = [0 for _ in range(term)]
    repayments[-1] = principal
    remaining_balances = [principal for _ in range(term)]

    return [time_periods, remaining_balances, interests, repayments, installments]

def pygame_runner(principal, interest_rate, term):
    # Defintion of colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Setting screen bounds
    width = 1200
    height = 700

    # Initialising figlet
    figlet = Figlet()
    font = "small"
    figlet.setFont(font=font)

    # Initialising screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Plots")
    screen.fill(black)

    # Setting framerates and durations
    clock = pygame.time.Clock()
    fps = 60
    precision = 60
    duration = 3
    frames = duration * fps

    # Section for Buttons
    print_btn = BasicBtn(0, 600, pygame.image.load(
        os.path.join(btn_img_dir, "print_white.png")
        ).convert_alpha())

    plot_btn_imgs = []
    for plot in plot_types:
        temp_btn_imgs = []
        for color in color_names:
            btn_name = os.path.join(btn_img_dir, f"{plot}_{color}.png")
            temp_btn_imgs.append(pygame.image.load(btn_name).convert_alpha())
        plot_btn_imgs.append(temp_btn_imgs)

    plot_btns = []
    for i, row in enumerate(plot_btn_imgs):
        btn = ExtraBtn(0, 200 + i * 100, row, plot_types[i])
        if i == 0:
            btn.state = True
        plot_btns.append(btn)

    loan_btn_imgs = []
    for loan_name in loan_models:
        temp_btn_imgs = []
        for color in color_names:
            btn_name = os.path.join(btn_img_dir, f"{loan_name}_{color}.png")
            temp_btn_imgs.append(pygame.image.load(btn_name).convert_alpha())
        loan_btn_imgs.append(temp_btn_imgs)

    loan_btns = []
    for i, row in enumerate(loan_btn_imgs):
        btn = ExtraBtn(300 + i * 300, height - 100, row, loan_models[i])
        if i == 0:
            btn.state = True
        loan_btns.append(btn)

    # Section for plots
    file_names = []
    for pref in loan_models:
        temp_row = []
        for plot_pref in plot_types:
            temp_row.append(pref + "_" + plot_pref)
        file_names.append(temp_row)

    plots = []
    for column in file_names:
        temp_row = []
        for plot_name in column:
            temp_row.append(
                pygame.image.load(
                    os.path.join(plots_dir, f"{plot_name}plot.png")
                    ).convert_alpha()
            )
        plots.append(temp_row)

    loan_index = 0
    plot_index = 0

    def draw_plot(loan_index=0, plot_index=0):
        screen.blit(plots[loan_index][plot_index], (200, 0))


    # Starting animation loop
    frame = 0
    while frame <= frames:

        # Ticking clock
        clock.tick(fps)

        # Draw left sidebar
        pygame.draw.rect(screen, black, (0, 0, 200, height))
        # Draw bar at the bottom
        pygame.draw.rect(screen, black, (200, height - 100, width, height))

        # Do animation
        # Draw 50 NEW points per frame.
        for i in range(50):
            progress = frame / frames + i / 50 / frames
            for j in range(0, 200, 10):
                # Drawing outer circles
                pygame.draw.circle(
                    screen,
                    white,
                    circle(progress, 200 - j, 200 - j),
                    radius=1,
                )
                progress = frame / frames + i / 50 / frames
                pygame.draw.circle(
                    screen,
                    white,
                    circle(progress, 200 - j, 200 - j, offset=True),
                    radius=1,
                )

        # Section for Buttons
        if print_btn.draw(screen):
            print("Print")
            print(figlet.renderText(loan_models[loan_index].capitalize()))
            print_loan_plan(loan_index, principal, interest_rate, term)
            print(figlet.renderText("Overview"))
            print_loan_overview(principal, interest_rate, term)

        for i, btn in enumerate(plot_btns):
            if btn.draw(screen):
                plot_index = i
                btn_state = btn.get_state()
                if btn_state == False:
                    # Deactivate other buttons
                    for other_btn in plot_btns:
                        if btn == other_btn:
                            continue
                        else:
                            if other_btn.get_state():
                                other_btn.set_state(False)
                    # Set Button to active
                    btn.set_state(True)
                elif btn_state == True:
                    if plot_index != i:
                        btn.set_state(False)
                # Prints for debugging
                print("Button Index: ", i)
                print("Button Name: ", btn.get_name())
                print("Button State: ", btn.get_state())

        for i, btn in enumerate(loan_btns):
            if btn.draw(screen):
                loan_index = i
                btn_state = btn.get_state()
                if btn_state == False:
                    # Deactivate other buttons
                    for other_btn in loan_btns:
                        if btn == other_btn:
                            continue
                        else:
                            if other_btn.get_state():
                                other_btn.set_state(False)
                    # Set Button to active
                    btn.set_state(True)

                elif btn_state == True:
                    if loan_index != i:
                        btn.set_state(False)
                # Prints for debugging
                print("Button Index: ", i)
                print("Button Name: ", btn.get_name())
                print("Button State: ", btn.get_state())

        # Draw plot
        draw_plot(loan_index, plot_index)

        # Updating animation by flipping the screen
        pygame.display.flip()

        # Counting frames
        frame += 1

        if frame > frames:
            frame = 0

        # Listening for the quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


# Basic Button class for pygame
class BasicBtn():
	def __init__(self, x, y, image, scale=1):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		# Get mouse position
		pos = pygame.mouse.get_pos()

		# Check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		# Draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

# Extra Button class for pygame
class ExtraBtn():
    def __init__(self, x, y, images, name="Button", scale=1):
        width = images[0].get_width()
        height = images[0].get_height()
        imgs = []
        for image in images:
            imgs.append(pygame.transform.scale(image, (int(width * scale), int(height * scale))))

        self.images = imgs
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

        self.state = False
        self.name = name

    def set_state(self, boolean):
        self.state = boolean

    def get_state(self):
        return self.state

    def get_name(self):
        return self.name

    def draw(self, surface):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        if self.state:
            surface.blit(self.images[1], (self.rect.x, self.rect.y))
        else:
            surface.blit(self.images[0], (self.rect.x, self.rect.y))

        return action

# Creating Images for buttons
def create_btn_images(plot_names, loan_names):
    text = "print"
    image = create_text_image(
        text=text.capitalize(),
        width=200,
        height=100,
        bg_color="white",
        text_color="black",
        border_color="black",
        border_thickness=5
    )
    filename = os.path.join(btn_img_dir, f"{text}_white.png")
    image.save(filename)  # Save the image

    for text in plot_names:
        image = create_text_image(
            text=text.capitalize(),
            width=200,
            height=100,
            bg_color="white",
            text_color="black",
            border_color="black",
            border_thickness=5
        )
        filename = os.path.join(btn_img_dir, f"{text}_white.png")
        image.save(filename)  # Save the image

        image = create_text_image(
            text=text.capitalize(),
            width=200,
            height=100,
            bg_color="black",
            text_color="white",
            border_color="white",
            border_thickness=5
        )
        filename = os.path.join(btn_img_dir, f"{text}_black.png")
        image.save(filename)  # Save the image

    for text in loan_names:
        image = create_text_image(
            text=text.capitalize(),
            width=300,
            height=100,
            bg_color="white",
            text_color="black",
            border_color="black",
            border_thickness=5
        )
        filename = os.path.join(btn_img_dir, f"{text}_white.png")
        image.save(filename)  # Save the image

        image = create_text_image(
            text=text.capitalize(),
            width=300,
            height=100,
            bg_color="black",
            text_color="white",
            border_color="white",
            border_thickness=5
        )
        filename = os.path.join(btn_img_dir, f"{text}_black.png")
        image.save(filename)  # Save the image


# Creates an Image
def create_text_image(text, width, height, bg_color, text_color, border_color, border_thickness):
    # Create a frame
    img = Image.new("RGB", (width, height), color=border_color)
    draw = ImageDraw.Draw(img)

    # Inner rectangle for the main content
    inner_rect = [
        border_thickness,
        border_thickness,
        width - border_thickness,
        height - border_thickness
    ]
    draw.rectangle(inner_rect, fill=bg_color)

    font = ImageFont.load_default(height//2)

    # Add the text
    draw.text((width//10, height//4), text, fill=text_color, font=font)

    return img

# (kind of not a) Circle for animations
def circle(progress, width, height, offset=False):
    if offset:
        return [
            width // 2 + height // 2 * np.cos(2 * np.pi * progress + np.pi),
            height // 2 + height // 2 * np.cos(2 * np.pi * progress + np.pi),
        ]
    else:
        return [
            width // 2 + height // 2 * np.sin(2 * np.pi * progress),
            height // 2 - height // 2 * np.sin(2 * np.pi * progress),
        ]

if __name__ == "__main__":
    main()
