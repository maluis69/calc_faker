import pytest
from faker import Faker
from decimal import Decimal
from calculator.engine.calculator import MathEngine  # Use MathEngine

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of records to generate")

@pytest.fixture
def num_records(request):
    return request.config.getoption("--num_records")

@pytest.fixture
def generate_test_data(num_records):
    data = []
    engine = MathEngine()  # Use MathEngine for calculations
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2) + 1)
        operation = fake.random_element(elements=("addition", "subtraction", "multiplication", "division"))
        if operation == 'division' and b == 0:
            b = Decimal(1)  # Avoid divide by zero
        result = getattr(engine, operation)(a, b)
        data.append((a, b, operation, result))
    return data
