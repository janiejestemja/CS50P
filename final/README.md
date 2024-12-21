# Loan Comparison Tool

This project is a Python-based tool for analyzing and comparing different types of loans. The tool provides an easy way to visualize repayment schedules and calculate the costs associated with various loan types. It includes both a command-line interface (CLI) and a graphical user interface (GUI) built with `pygame`.

---

## Features

- **Three Loan Types:**
  - Amortizing Loan
  - Annuity Loan
  - Bullet Loan

- **Repayment Visualization:**
  - Tabulated outputs for time periods, remaining balances, interest payments, repayments, and installments.
  - Clear and structured formatting using the `tabulate` library.

- **CLI Options:**
  - Input principal amount, interest rate, and loan term via command-line arguments using `argparse`.

- **GUI (pygame):**
  - View loan repayment schedules interactively.
  - Buttons for switching between loan types and different visualizations.

- **Unit Testing:**
  - Comprehensive test coverage using `pytest` for core logic functions.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Command-Line Interface (CLI)

Run the script with the following arguments:

- `--principal` (float): The total amount of the loan.
- `--interest_rate` (float): Annual interest rate as a decimal (e.g., 0.05 for 5%).
- `--term` (int): Loan term in years.

Example:
```bash
python loan_tool.py --principal 100000 --interest_rate 0.05 --term 10
```

If arguments are not provided, the program will prompt the user for input interactively.

### Graphical User Interface (GUI)

Navigate between loan types and visualizations using the on-screen buttons.

---

## Loan Types Explained

### Amortizing Loan
An amortizing loan has equal repayments over the term of the loan, with the principal gradually paid off while interest payments decrease.

### Annuity Loan
An annuity loan has constant installments (principal + interest), with the principal portion increasing and interest decreasing over time.

### Bullet Loan
A bullet loan requires interest payments during the term and a lump-sum principal repayment at the end.

---

## Testing

Run the unit tests using `pytest`:
```bash
pytest
```

Unit tests are provided for the core logic functions, ensuring correctness for each loan type's repayment calculations.

---

## Dependencies

- Python 3.10+
- `pytest`
- `argparse`
- `pillow`
- `tabulate`
- `pyfiglet`
- `pygame`
- `numpy`
- `matplotlib`
- `seaborn`
- `pandas`

---

## Project Structure

```
.
├── project.py             # Main script
├── test_project.py        # Unit tests
├── plots/                 # Saved plots
├── btn_img/               # GUI assets (Button Images)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Future Improvements

- Add more detailed visualizations (e.g., matplotlib or seaborn plots).
- Implement localization support for multiple languages.
- Expand unit tests for edge cases and invalid inputs.
- Improve GUI responsiveness and aesthetics.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Acknowledgments

Special thanks to contributors and libraries that made this project possible!

