import pytest
from commands.add_command import AddCommand

def test_add_command():
    add_command = AddCommand()

    # Basic test cases
    assert add_command.execute(2, 3) == 5
    assert add_command.execute(-1, 5) == 4
    assert add_command.execute(0, 0) == 0
    assert add_command.execute(10.5, 5.5) == 16.0
    
    # Error cases (fewer than 2 arguments)
    with pytest.raises(ValueError):
        add_command.execute(2)  # Not enough arguments
    
    # Error cases (more than 2 arguments)
    with pytest.raises(ValueError):
        add_command.execute(1, 2, 3)
