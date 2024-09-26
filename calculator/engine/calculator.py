"""
This module defines the MathEngine class for performing basic arithmetic operations
and managing calculation history.
"""

from decimal import Decimal
from calculator.engine.history_manager import HistoryManager


class MathEngine:
    """A Math Engine to perform basic operations and manage calculation history."""

    def __init__(self):
        self.history = HistoryManager()

    def compute(self, a: Decimal, b: Decimal, operation_name: str) -> Decimal:
        """Perform an operation and store the result in history."""
        from calculator.engine.operations import Operation  # pylint: disable=import-outside-toplevel
        operation = getattr(Operation, operation_name)
        result = operation(a, b)
        self.history.add_record(a, b, operation_name, result)
        return result

    def addition(self, x: Decimal, y: Decimal) -> Decimal:
        """Add two numbers."""
        return self.compute(x, y, "add")

    def subtraction(self, x: Decimal, y: Decimal) -> Decimal:
        """Subtract two numbers."""
        return self.compute(x, y, "subtract")

    def multiplication(self, x: Decimal, y: Decimal) -> Decimal:
        """Multiply two numbers."""
        return self.compute(x, y, "multiply")

    def division(self, x: Decimal, y: Decimal) -> Decimal:
        """Divide two numbers with zero-division handling."""
        return self.compute(x, y, "divide")

    def get_last_result(self):
        """Retrieve the most recent result from history."""
        return self.history.get_last()

    def get_full_history(self):
        """Retrieve the full history of calculations."""
        return self.history.get_all()

    def clear_history(self):
        """Clear the history of calculations."""
        self.history.clear()
