"""
This module contains basic mathematical operations such as add, subtract, multiply, and divide.
"""

from decimal import Decimal

class Operation:
    """A class containing all basic mathematical operations."""

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        "Returns the sum of two numbers"
        return a + b

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        "Returns the difference of two numbers"
        return a - b

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        "Returns the product of two numbers"
        return a * b

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        "Returns the quotient of two numbers"
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    