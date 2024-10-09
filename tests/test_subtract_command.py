import pytest
from commands.subtract_command import SubtractCommand

def test_subtract_command():
    subtract_command = SubtractCommand()

    # Basic test cases
    assert subtract_command.execute(5, 2) == 3
    assert subtract_command.execute(10, 5) == 5
    assert subtract_command.execute(0, 5) == -5
    assert subtract_command.execute(3.5, 1.5) == 2.0

    # Error cases (fewer than 2 arguments)
    with pytest.raises(ValueError):
        subtract_command.execute(5)  # Not enough arguments

    # Error cases (more than 2 arguments)
    with pytest.raises(ValueError):
        subtract_command.execute(1, 2, 3)
