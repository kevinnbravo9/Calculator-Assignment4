# Project 4 Calculator

## Description

This project is a command-line calculator application developed in Python. The calculator uses a modular object-oriented design and provides a REPL interface that allows users to perform calculations continuously until they choose to exit.

The calculator supports addition, subtraction, multiplication, and division. It also maintains a history of successful calculations and provides special commands for help, history, and exiting the application.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- REPL command-line interface
- Calculation history
- Help command
- Exit command
- Input validation
- Division-by-zero error handling
- LBYL and EAFP error-handling approaches
- CalculationFactory for creating calculations
- Unit and parameterized testing with pytest
- 100% test coverage
- GitHub Actions continuous integration

## Project Structure

- `app/calculator/` - Handles the calculator REPL and user commands
- `app/calculation/` - Contains calculation management and CalculationFactory
- `app/operation/` - Contains arithmetic operations
- `tests/` - Contains unit and parameterized tests
- `main.py` - Entry point for the application

## Setup

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the calculator with:

```bash
python3 main.py
```

The calculator accepts commands using this format:

```text
<operation> <num1> <num2>
```

Examples:

```text
add 5 3
subtract 10 4
multiply 5 3
divide 10 2
```

Special commands:

- `help` - Displays instructions for using the calculator
- `history` - Displays calculations performed during the session
- `exit` - Exits the calculator

## Testing

Run the tests with:

```bash
pytest
```

Run the tests with coverage:

```bash
pytest --cov=app --cov-branch --cov-fail-under=100
```

The project is configured to require 100% test coverage.

## Continuous Integration

GitHub Actions automatically runs the test suite and checks test coverage when changes are pushed to the repository or submitted through a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.