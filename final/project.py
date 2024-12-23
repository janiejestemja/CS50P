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

# Directories for button images and plots
BUTTON_IMAGE_DIRECTORY = "btn_img"
PLOT_DIRECTORY = "plots"

# Available color schemes and plot types
COLOR_SCHEMES = ["white", "black"]
PLOT_TYPES = ["scatter", "line", "bar"]
LOAN_MODELS = ["amortizing", "annuity", "bullet"]

# Generate loan-specific plot names
LOAN_PLOT_NAMES = [[f"{loan}_{plot}" for plot in PLOT_TYPES] for loan in LOAN_MODELS]

def main():
    """Main function to run the loan comparison script."""
    parser = argparse.ArgumentParser(description="A script to compare loan repayment plans.")

    # Add arguments for loan parameters
    parser.add_argument("--principal", type=float, help="Loan amount (Principal).")
    parser.add_argument("--interest_rate", type=float, help="Interest rate (A number between 0 and 1).")
    parser.add_argument("--term", type=int, help="Loan term in years.")

    args = parser.parse_args()
    command_line_args = validate_arguments(args)

    if command_line_args:
        principal, interest_rate, term = command_line_args
    else:
        principal, interest_rate, term = get_user_input()

    setup_directories()

    generate_plots(principal, interest_rate, term)
    run_pygame_interface(principal, interest_rate, term)

def validate_arguments(args):
    """Validate command-line arguments and return them as a tuple if valid."""
    validated_args = []
    if args.principal:
        if args.principal <= 0:
            print("Principal must be greater than zero.")
            sys.exit(1)
        validated_args.append(args.principal)
    if args.interest_rate:
        if not 0 < args.interest_rate <= 1:
            print("Interest rate must be between 0 and 1.")
            sys.exit(1)
        validated_args.append(args.interest_rate)
    if args.term:
        if args.term <= 0:
            print("Term must be greater than zero.")
            sys.exit(1)
        validated_args.append(args.term)

    return validated_args if len(validated_args) == 3 else None

def get_user_input():
    """Prompt the user to input loan parameters and validate them."""
    def prompt_input(prompt, input_type, condition, error_message):
        while True:
            try:
                value = input_type(input(prompt))
                if condition(value):
                    return value
                else:
                    print(error_message)
            except ValueError:
                print(f"Invalid input. Expected {input_type.__name__}.")

    principal = prompt_input("Principal: ", float, lambda x: x > 0, "Principal must be greater than zero.")
    interest_rate = prompt_input("Interest rate (0 < rate <= 1): ", float, lambda x: 0 < x <= 1, "Interest rate must be between 0 and 1.")
    term = prompt_input("Term (years): ", int, lambda x: x > 0, "Term must be greater than zero.")

    return principal, interest_rate, term

def setup_directories():
    """Ensure necessary directories for button images and plots exist."""
    if not os.path.exists(BUTTON_IMAGE_DIRECTORY):
        os.makedirs(BUTTON_IMAGE_DIRECTORY)
        create_button_images()
    else:
        plot_btn_imgs = ["print_white.png"]
        for plot in PLOT_TYPES + LOAN_MODELS:
            for color in COLOR_SCHEMES:
                plot_btn_imgs.append(f"{plot}_{color}.png")

        # Get all files in the directory
        files = [file for file in os.listdir(BUTTON_IMAGE_DIRECTORY) if os.path.isfile(os.path.join(BUTTON_IMAGE_DIRECTORY, file))]

        missing_btns = [btn_img_name for btn_img_name in plot_btn_imgs if btn_img_name not in files]

        if len(missing_btns) > 0:
            create_button_images()

    if not os.path.exists(PLOT_DIRECTORY):
        os.makedirs(PLOT_DIRECTORY)

def create_button_images():
    """Generate button images for GUI interaction."""
    for text, width, height in [("print", 200, 100)] + [(name, 200, 100) for name in PLOT_TYPES]:
        for color, bg_color, text_color in zip(COLOR_SCHEMES, ["white", "black"], ["black", "white"]):
            image = create_text_image(text.capitalize(), width, height, bg_color, text_color, border_color=text_color)
            image.save(os.path.join(BUTTON_IMAGE_DIRECTORY, f"{text}_{color}.png"))

    for text, width, height in [(name, 300, 100) for name in LOAN_MODELS]:
        for color, bg_color, text_color in zip(COLOR_SCHEMES, ["white", "black"], ["black", "white"]):
            image = create_text_image(text.capitalize(), width, height, bg_color, text_color, border_color=text_color)
            image.save(os.path.join(BUTTON_IMAGE_DIRECTORY, f"{text}_{color}.png"))

def create_text_image(text, width, height, bg_color, text_color, border_color, border_thickness=5):
    """Create a text-based image for buttons."""
    image = Image.new("RGB", (width, height), border_color)
    draw = ImageDraw.Draw(image)
    inner_rect = [border_thickness, border_thickness, width - border_thickness, height - border_thickness]
    draw.rectangle(inner_rect, fill=bg_color)

    font = ImageFont.load_default(height//2)

    # Add the text
    draw.text((width//10, height//4), text, fill=text_color, font=font)

    return image


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

def generate_plots(principal, interest_rate, term):
    """Generate and save plots for different loan types."""
    def plot_data(plot_type, dataframe, name):
        plt.figure(figsize=(10, 6))
        for column in dataframe.columns[2:]:
            if plot_type == "line":
                sns.lineplot(x=dataframe.columns[0], y=column, label=column.capitalize(), data=dataframe, alpha=0.75)
            elif plot_type == "scatter":
                sns.scatterplot(x=dataframe.columns[0], y=column, label=column.capitalize(), data=dataframe, alpha=0.5)
            elif plot_type == "bar":
                sns.barplot(x=dataframe.columns[0], y=column, label=column.capitalize(), data=dataframe, alpha=0.5)

        plt.title(f"{name.replace('_', ' ').title()} Plot")
        plt.grid(True)
        plt.savefig(os.path.join(PLOT_DIRECTORY, f"{name}_plot.png"))

    amortizing_df = pd.DataFrame(amortizing_loan(principal, interest_rate, term, to_dict=True))
    annuity_df = pd.DataFrame(annuity_loan(principal, interest_rate, term, to_dict=True))
    bullet_df = pd.DataFrame(bullet_loan(principal, interest_rate, term, to_dict=True))

    for loan_type, plot_names in zip(LOAN_MODELS, LOAN_PLOT_NAMES):
        for plot_name, plot_type in zip(plot_names, PLOT_TYPES):
            dataframe = locals()[f"{loan_type}_df"]
            plot_data(plot_type, dataframe, plot_name)


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

def run_pygame_interface(principal, interest_rate, term):
    """Run the Pygame GUI interface for visualizing loan data."""

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

    loan_index = 0
    plot_index = 0

    # Section for Buttons
    print_btn = BasicBtn(0, 600, pygame.image.load(
        os.path.join(BUTTON_IMAGE_DIRECTORY, "print_white.png")
        ).convert_alpha())

    plot_btn_imgs = []
    for plot_type in PLOT_TYPES:
        temp_btn_imgs = []
        for color in COLOR_SCHEMES:
            btn_name = os.path.join(BUTTON_IMAGE_DIRECTORY, f"{plot_type}_{color}.png")
            temp_btn_imgs.append(pygame.image.load(btn_name).convert_alpha())
        plot_btn_imgs.append(temp_btn_imgs)

    plot_btns = []
    for i, row in enumerate(plot_btn_imgs):
        btn = ExtraBtn(0, 200 + i * 100, row, PLOT_TYPES[i])
        if i == 0:
            btn.state = True
        plot_btns.append(btn)

    loan_btn_imgs = []
    for loan_model in LOAN_MODELS:
        temp_btn_imgs = []
        for color in COLOR_SCHEMES:
            btn_name = os.path.join(BUTTON_IMAGE_DIRECTORY, f"{loan_model}_{color}.png")
            temp_btn_imgs.append(pygame.image.load(btn_name).convert_alpha())
        loan_btn_imgs.append(temp_btn_imgs)

    loan_btns = []
    for i, row in enumerate(loan_btn_imgs):
        btn = ExtraBtn(300 + i * 300, height - 100, row, LOAN_MODELS[i])
        if i == 0:
            btn.state = True
        loan_btns.append(btn)

    plots = []
    for column in LOAN_PLOT_NAMES:
        temp_row = []
        for plot_name in column:
            temp_row.append(
                pygame.image.load(
                    os.path.join(PLOT_DIRECTORY, f"{plot_name}_plot.png")
                    ).convert_alpha()
            )
        plots.append(temp_row)


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
                    circle(progress, 200, 200),
                    radius=1,
                )
                progress = frame / frames + i / 50 / frames
                pygame.draw.circle(
                    screen,
                    white,
                    circle(progress, 200, 200, offset=True),
                    radius=1,
                )

        # Section for Buttons
        if print_btn.draw(screen):
            print(figlet.renderText(LOAN_MODELS[loan_index].capitalize()))
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
