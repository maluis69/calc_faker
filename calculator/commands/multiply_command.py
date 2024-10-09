from .command import Command

class MultiplyCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            raise ValueError("MultiplyCommand requires exactly 2 arguments.")
        return args[0] * args[1]