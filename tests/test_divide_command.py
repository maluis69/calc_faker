import pytest
from commands.divide_command import DivideCommand

def test_divide_command():
    divide_command = DivideCommand()

    # Basic test cases
    assert divide_command.execute(10, 2) == 5
    assert divide_command.execute(9, 3) == 3
    assert divide_command.execute(5.5, 2.2) == 2.5

    # Division by zero
    with pytest.raises(ZeroDivisionError):
        divide_command.execute(10, 0)

    # Error cases (fewer than 2 arguments)
    with pytest.raises(ValueError):
        divide_command.execute(10)  # Not enough arguments

    # Error cases (more than 2 arguments)
    with pytest.raises(ValueError):
        divide_command.execute(1, 2, 3)