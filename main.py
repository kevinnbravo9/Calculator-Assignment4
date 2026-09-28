"""Entry point for the command-line calculator."""

from app.calculator import Calculator


def main():
    """Start the calculator application."""
    calculator = Calculator()
    calculator.run()


if __name__ == "__main__":
    main()