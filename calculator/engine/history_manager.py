"""
This module manages the history of calculations.
"""

class HistoryManager:
    """Manages the history of all calculations."""

    def __init__(self):
        """Initialize an empty history."""
        self._history = []

    def add_record(self, a, b, operation, result):
        """Add a record of a calculation to the history."""
        entry = f"{a} {operation} {b} = {result}"
        self._history.append(entry)

    def get_last(self):
        """Get the last calculation from the history."""
        return self._history[-1] if self._history else None

    def get_all(self):
        """Retrieve the full calculation history."""
        return self._history

    def clear(self):
        """Clear the calculation history."""
        self._history = []
        