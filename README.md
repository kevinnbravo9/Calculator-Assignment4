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