from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand

def repl():
    commands = {
        'add': AddCommand(),
        'subtract': SubtractCommand(),
        'multiply': MultiplyCommand(),
        'divide': DivideCommand(),
    }
    
    while True:
        user_input = input("> ").strip().split()
        if not user_input:
            continue
        command_name = user_input[0]
        args = list(map(float, user_input[1:]))  # convert arguments to float
        
        if command_name == 'exit':
            print("Exiting the calculator.")
            break
        elif command_name in commands:
            try:
                result = commands[command_name].execute(*args)
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Unknown command. Type 'menu' to see available commands.")

if __name__ == "__main__":
    repl()

