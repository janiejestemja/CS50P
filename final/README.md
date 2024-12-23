# Loan Comparison Tool

A Python-based tool to compare different loan repayment plans (Amortizing, Annuity, and Bullet) with visualization and an interactive GUI. The tool supports graphical plots and terminal-based summaries for better insights into loan repayment schedules.

---

## Features

- Compare repayment schedules for three loan models:
  - **Amortizing Loan**
  - **Annuity Loan**
  - **Bullet Loan**
- Generate plots for:
  - Repayment over time
  - Interest trends
  - Total installments
- Interactive graphical user interface (GUI) built with `pygame`.
- Detailed terminal output of loan schedules and overviews.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.13+
- Required Python packages:
  - `pygame`
  - `Pillow`
  - `tabulate`
  - `pyfiglet`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `pandas`

You can install dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd <repository-folder>
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Command-Line Interface (CLI)

Run the script using the following command:

```bash
python project.py --principal <amount> --interest_rate <rate> --term <years>
```

Example:

```bash
python project.py --principal 100000 --interest_rate 0.05 --term 10
```

### Interactive Mode

If you omit the CLI arguments, the tool will prompt you for:
- Principal amount
- Interest rate (as a decimal between 0 and 1)
- Loan term (in years)

### GUI Mode

After the inputs, the GUI displays:
- Buttons to toggle between different loan models and plot types.
- Dynamic visualizations for each loan plan.

---

## Output

1. **Plots**: Saved to the `plots` directory.
   - Scatter, Line, and Bar plots for Amortizing, Annuity, and Bullet loans.
2. **Button Images**: Generated in the `btn_img` directory.
3. **Terminal Output**: Detailed tables showing repayment schedules and an overview.

---

## Directory Structure

```plaintext
project-folder/
├── btn_img/                # Auto-generated button images
├── plots/                  # Generated plots
├── project.py              # Main script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Contributing

Feel free to fork this project and create pull requests for improvements or new features.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- **Libraries Used:**
  - `pygame` for GUI.
  - `Pillow` for button image generation.
  - `matplotlib` and `seaborn` for plots.
  - `tabulate` for terminal tables.
  - `pyfiglet` for stylish terminal text.
