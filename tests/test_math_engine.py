"""
Test suite for the MathEngine class.

This module contains unit tests for the MathEngine class, which performs basic arithmetic
operations (addition, subtraction, multiplication, division) and manages calculation history.
Each test ensures that the operations return the expected results and that history
management functions as intended.
"""

from decimal import Decimal
import pytest
from calculator.engine.calculator import MathEngine

@pytest.fixture
def engine_fixture():
    """Fixture for creating a new instance of MathEngine."""
    return MathEngine()

def test_addition(engine_fixture):
    """Test the addition operation.
    
    This test ensures that the addition method correctly sums two numbers.
    """
    result = engine_fixture.addition(Decimal('5'), Decimal('3'))
    assert result == Decimal('8')

def test_subtraction(engine_fixture):
    """Test the subtraction operation.
    
    This test ensures that the subtraction method correctly subtracts one number from another.
    """
    result = engine_fixture.subtraction(Decimal('5'), Decimal('3'))
    assert result == Decimal('2')

def test_multiplication(engine_fixture):
    """Test the multiplication operation.
    
    This test ensures that the multiplication method correctly multiplies two numbers.
    """
    result = engine_fixture.multiplication(Decimal('5'), Decimal('3'))
    assert result == Decimal('15')

def test_division(engine_fixture):
    """Test the division operation.
    
    This test ensures that the division method correctly divides two numbers.
    """
    result = engine_fixture.division(Decimal('9'), Decimal('3'))
    assert result == Decimal('3')

def test_divide_by_zero(engine_fixture):
    """Test division by zero.
    
    This test ensures that a ZeroDivisionError is raised when attempting to divide by zero.
    """
    with pytest.raises(ZeroDivisionError):
        engine_fixture.division(Decimal('5'), Decimal('0'))

def test_history(engine_fixture):
    """Test the calculation history.
    
    This test ensures that the history correctly stores all operations performed.
    """
    engine_fixture.addition(Decimal('2'), Decimal('3'))
    engine_fixture.subtraction(Decimal('5'), Decimal('2'))
    history = engine_fixture.get_full_history()
    assert len(history) == 2
    assert "2 add 3 = 5" in history
    assert "5 subtract 2 = 3" in history

def test_clear_history(engine_fixture):
    """Test clearing the history.
    
    This test ensures that the history is properly cleared after calling clear_history()."""
    engine_fixture.addition(Decimal('2'), Decimal('3'))
    engine_fixture.clear_history()
    assert engine_fixture.get_full_history() == []

def test_get_last_empty_history(engine_fixture):
    """Test get_last when history is empty.
    
    This test ensures that get_last returns None when the history is empty.
    """
    engine_fixture.clear_history()  # Clear the history
    last_entry = engine_fixture.get_last_result()  # This should return None
    assert last_entry is None
    