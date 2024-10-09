import pytest
from unittest import mock
from calculator.main import repl

def test_add_operation():
    # Mock input to simulate the REPL inputs
    with mock.patch('builtins.input', side_effect=['add 5 3', 'exit']):
        with mock.patch('builtins.print') as mock_print:
            # Run the REPL
            repl()

            # Check if the output was printed correctly
            mock_print.assert_any_call('Result: 8.0')
