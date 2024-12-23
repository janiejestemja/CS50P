# Loan Comparison Tool

#### Video Demo:  <URL HERE>

## Description
A Python-based tool to compare different loan repayment plans (Amortizing, Annuity, and Bullet) with visualization and an interactive GUI. The tool supports graphical plots and terminal-based summaries for better insights into loan repayment schedules.

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Output](#output)
6. [Directory Structure](#drectory-structure)
7. [Design Choices](#design-choices)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgments](#acknowledgments)

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
├── test_project.py         # Unit tests (for business logic)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Design Choices

### CLI and Interactive Mode

- Instead of enforcing exclusive usage of a CLI, the project includes an **iteractive mode** that prompts users for one input at a time. 
- **Benefits**:
  - Experienced users can run the program quickly by passing all necessary variables as command-line arguments.
  - New or less informed users can run the program without needing to consult documentation or instructions, thanks to the clear and concise prompts in interactive mode.
- **Design Philosophy**:
  - The prompts in the interactive mode are intentionally designed to be **short, simple, and self-explanatory**, lowering the barrier to entry for less technical users.
- This dual-mode approach balances **usability** for casual users and **efficiency** for power users.

### GUI Design

- The GUI was designed with simplicity and usability in mind:
  - Users can easily **toggle between loan models** and **plot types**, allowing them to explore various scenarios quickly.
  - Visual summaries provide immediate, at-a-glance comparisons.
- **Animations**:
  - Animations were added to enhance user engagement and make the application more visually appealing.
  - Care was taken to ensure animations do not overwhelm or distract from the core functionality by keeping them subtle and non-intrusive.

### Choice of Libraries

- The selection of libraries was driven by specific project requirements and design goals:
  - **`pygame`**:
    - Chosen for its lightweight nature and suitability for creating dynamic, interactive GUIs.
    - Its simplicity enabled rapid prototyping and customization for the application's needs.
  - **`seaborn`**:
    - Used for creating visually appealing and easily interpretable plots.
    - Its high-level API makes it straightforward to generate polished visuals for comparisons.
  - **`pyfiglet`**:
    - Adds a fun and engaging aesthetic for terminal outputs, aligning with the goal of making the application approachable.
  - **`tabulate`**:
    - Generates clean and structured tables in the terminal, improving the clarity of textual output for users who prefer CLI interaction.

### Code Structure and Modularity

- The project was structured to emphasize **modularity** and **reusability**:
  - Each loan model (e.g., amortizing, annuity, and bullet) is implemented as a standalone function, making it easy to debug, test, and extend.
  - The **`formatter` decorator** adds a layer of flexibility by allowing the same function to support multiple output formats (e.g., dictionaries, tables, or raw data).
  - Separation of concerns was maintained by keeping GUI-related code, CLI logic, and core computations in distinct sections of the codebase.

### User Experience (UX)

- The design prioritizes a balance between functionality and simplicity:
  - **Input Validation**: Both CLI and interactive modes include thorough validation to prevent invalid inputs, ensuring a smooth user experience.
  - **Directory Management**: The application automatically creates required directories (e.g., for button images or plots) if they do not exist, reducing setup complexity for the user.
  - **Defaults and Prompts**: Prompts are crafted to guide users intuitively, while defaults are avoided to encourage deliberate input.

### Trade-offs and Constraints

- **Library Choices**:
  - While `pygame` was chosen for simplicity and flexibility, it is not as feature-rich as more specialized GUI frameworks like `Tkinter` or `PyQt`. However, the trade-off was deemed acceptable for the project's scope.
- **Interactive vs. CLI**:
  - The addition of an interactive mode increased development time but was necessary to make the application more accessible to a broader audience.

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

