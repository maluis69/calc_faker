import sys
from decimal import Decimal, InvalidOperation  # Import InvalidOperation
from calculator.engine.calculator import MathEngine  # Import MathEngine directly

def main():
    engine = MathEngine()  # Instantiate MathEngine
    try:
        a = Decimal(sys.argv[1])
        b = Decimal(sys.argv[2])
        operation = sys.argv[3].lower()

        if operation == "add":
            result = engine.addition(a, b)
        elif operation == "subtract":
            result = engine.subtraction(a, b)
        elif operation == "multiply":
            result = engine.multiplication(a, b)
        elif operation == "divide":
            result = engine.division(a, b)
        else:
            print(f"Unknown operation: {operation}")
            return

        print(f"The result of {a} {operation} {b} is equal to {result}")

    except InvalidOperation:
        print(f"Invalid number input: {sys.argv[1]} or {sys.argv[2]} is not a valid number.")
    except ZeroDivisionError:
        print(f"An error occurred: Cannot divide by zero")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
