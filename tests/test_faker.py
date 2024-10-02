from faker import Faker
import pytest
from calculator.engine.calculator import MathEngine  # Use MathEngine
from decimal import Decimal

fake = Faker()

@pytest.mark.parametrize("operation, op_func", [
    ('addition', MathEngine().addition),
    ('subtraction', MathEngine().subtraction),
    ('multiplication', MathEngine().multiplication),
    ('division', MathEngine().division)
])
def test_faker_operations(operation, op_func):
    a = Decimal(fake.random_number(digits=2))
    b = Decimal(fake.random_number(digits=2) + 1)  # Avoid divide by zero
    if operation == 'division' and b == 0:
        b = Decimal(1)  # To avoid divide by zero

    result = op_func(a, b)
    assert isinstance(result, Decimal)
