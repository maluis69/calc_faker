import logging
from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Application started")

def repl():
    logging.info("Starting REPL loop")
    commands = {
        'add': AddCommand(),
        'subtract': SubtractCommand(),
        'multiply': MultiplyCommand(),
        'divide': DivideCommand(),
    }

    while True:
        try:
            # Prompt for user input
            user_input = input("> ").strip().split()
            
            if not user_input:
                continue  # Skip empty input

            command_name = user_input[0]
            args = user_input[1:]

            if command_name == 'exit':
                logging.info("Exiting REPL")
                print("Goodbye!")
                break

            if command_name in commands:
                try:
                    args = list(map(float, args))
                    result = commands[command_name].execute(*args)
                    logging.info(f"Command: {command_name}, Args: {args}, Result: {result}")
                    print(f"Result: {result}")
                except Exception as e:
                    logging.error(f"Error executing {command_name} with args {args}: {e}")
                    print(f"Error: {e}")
            else:
                logging.warning(f"Unknown command: {command_name}")
                print("Unknown command. Type 'exit' to quit.")
        except KeyboardInterrupt:
            logging.info("Exiting REPL (KeyboardInterrupt)")
            print("\nGoodbye!")
            break

# Start the REPL
repl()
