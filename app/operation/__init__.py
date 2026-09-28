"""Arithmetic operations for the calculator."""

from abc import ABC, abstractmethod


class Operation(ABC):
    """Abstract base class for calculator operations."""

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """Perform an arithmetic operation."""
        pass  # pragma: no cover


class Add(Operation):
    """Perform addition."""

    def execute(self, a: float, b: float) -> float:
        return a + b


class Subtract(Operation):
    """Perform subtraction."""

    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiply(Operation):
    """Perform multiplication."""

    def execute(self, a: float, b: float) -> float:
        return a * b


class Divide(Operation):
    """Perform division."""

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b