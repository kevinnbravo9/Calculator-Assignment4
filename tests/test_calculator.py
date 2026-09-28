"""Tests for the command-line calculator."""

from unittest.mock import patch

from app.calculator import Calculator


def test_calculator_initial_history():
    calculator = Calculator()
    assert calculator.history == []


def test_show_help(capsys):
    calculator = Calculator()
    calculator.show_help()

    output = capsys.readouterr().out
    assert "Calculator Help:" in output
    assert "add, subtract, multiply, divide" in output
    assert "help, history, exit" in output


def test_empty_history(capsys):
    calculator = Calculator()
    calculator.show_history()

    output = capsys.readouterr().out
    assert "No calculations performed yet." in output


def test_calculation_and_history(capsys):
    calculator = Calculator()

    calculator.process_calculation("add 5 3")
    calculator.show_history()

    output = capsys.readouterr().out
    assert "Result: AddCalculation: 5.0 Add 3.0 = 8.0" in output
    assert "Calculation History:" in output
    assert "1. AddCalculation: 5.0 Add 3.0 = 8.0" in output
    assert len(calculator.history) == 1


def test_invalid_format(capsys):
    calculator = Calculator()
    calculator.process_calculation("add 5")

    output = capsys.readouterr().out
    assert "Invalid input." in output
    assert calculator.history == []


def test_invalid_number(capsys):
    calculator = Calculator()
    calculator.process_calculation("add hello 3")

    output = capsys.readouterr().out
    assert "could not convert string to float" in output
    assert calculator.history == []


def test_invalid_operation(capsys):
    calculator = Calculator()
    calculator.process_calculation("power 5 2")

    output = capsys.readouterr().out
    assert "Unknown operation" in output
    assert calculator.history == []


def test_division_by_zero(capsys):
    calculator = Calculator()
    calculator.process_calculation("divide 10 0")

    output = capsys.readouterr().out
    assert "Cannot divide by zero." in output
    assert calculator.history == []


def test_run_commands(capsys):
    calculator = Calculator()

    commands = [
        "help",
        "history",
        "add 5 3",
        "history",
        "exit",
    ]

    with patch("builtins.input", side_effect=commands):
        calculator.run()

    output = capsys.readouterr().out

    assert "Welcome to the calculator!" in output
    assert "Calculator Help:" in output
    assert "No calculations performed yet." in output
    assert "Result: AddCalculation: 5.0 Add 3.0 = 8.0" in output
    assert "Calculation History:" in output
    assert "Exiting calculator. Goodbye!" in output