from commands.command import Command  # Correct relative import

class AddCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            raise ValueError("AddCommand requires exactly 2 arguments.")
        return args[0] + args[1]
    