import pytest
from commands.multiply_command import MultiplyCommand

def test_multiply_command():
    multiply_command = MultiplyCommand()

    # Basic test cases
    assert multiply_command.execute(3, 4) == 12
    assert multiply_command.execute(-1, 5) == -5
    assert multiply_command.execute(0, 5) == 0
    assert multiply_command.execute(2.5, 2) == 5.0

    # Error cases (fewer than 2 arguments)
    with pytest.raises(ValueError):
        multiply_command.execute(3)  # Not enough arguments

    # Error cases (more than 2 arguments)
    with pytest.raises(ValueError):
        multiply_command.execute(1, 2, 3)
