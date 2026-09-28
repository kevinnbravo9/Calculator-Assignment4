"""Command-line calculator with REPL and calculation history."""

from app.calculation import CalculationFactory


class Calculator:
    """Manage calculator commands, calculations, and history."""

    def __init__(self):
        """Initialize an empty calculation history."""
        self.history = []

    def show_help(self):
        """Display instructions for using the calculator."""
        print("Calculator Help:")
        print("Use: <operation> <num1> <num2>")
        print("Operations: add, subtract, multiply, divide")
        print("Commands: help, history, exit")

    def show_history(self):
        """Display calculations performed during the session."""
        if not self.history:  # LBYL
            print("No calculations performed yet.")
            return

        print("Calculation History:")
        for index, calculation in enumerate(self.history, start=1):
            print(f"{index}. {calculation}")

    def process_calculation(self, command):
        """Validate and process a calculation command."""
        parts = command.split()

        # LBYL: check the expected format before processing.
        if len(parts) != 3:
            print(
                "Invalid input. Please follow the format: "
                "<operation> <num1> <num2>"
            )
            return

        operation_name, first_number, second_number = parts

        # EAFP: attempt conversion and handle failure.
        try:
            a = float(first_number)
            b = float(second_number)
            calculation = CalculationFactory.create_calculation(
                operation_name, a, b
            )
            result = calculation.perform()
        except ValueError as error:
            print(error)
            return

        self.history.append(calculation)
        print(f"Result: {calculation}")

    def run(self):
        """Run the calculator REPL."""
        print("Welcome to the calculator!")
        print("Type 'help' for instructions.")

        while True:
            command = input(">> ").strip()

            if command.lower() == "exit":
                print("Exiting calculator. Goodbye!")
                break

            if command.lower() == "help":
                self.show_help()
                continue

            if command.lower() == "history":
                self.show_history()
                continue

            self.process_calculation(command)