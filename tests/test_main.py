import subprocess
import os
import sys

def test_add_operation():
    # Get the absolute path to main.py inside the calculator/ directory
    main_path = os.path.join(os.getcwd(), "calculator", "main.py")
    result = subprocess.run([sys.executable, main_path, '5', '3', 'add'], capture_output=True, text=True, env={"PYTHONPATH": os.getcwd()})
    assert "The result of 5 add 3 is equal to 8" in result.stdout

def test_divide_by_zero():
    main_path = os.path.join(os.getcwd(), "calculator", "main.py")
    result = subprocess.run([sys.executable, main_path, '1', '0', 'divide'], capture_output=True, text=True, env={"PYTHONPATH": os.getcwd()})
    assert "An error occurred: Cannot divide by zero" in result.stdout

def test_invalid_input():
    main_path = os.path.join(os.getcwd(), "calculator", "main.py")
    result = subprocess.run([sys.executable, main_path, 'a', '3', 'add'], capture_output=True, text=True, env={"PYTHONPATH": os.getcwd()})
    assert "Invalid number input" in result.stdout

def test_unknown_operation():
    main_path = os.path.join(os.getcwd(), "calculator", "main.py")
    result = subprocess.run([sys.executable, main_path, '5', '3', 'unknown'], capture_output=True, text=True, env={"PYTHONPATH": os.getcwd()})
    assert "Unknown operation" in result.stdout
