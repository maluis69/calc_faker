from .command import Command

class SubtractCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            raise ValueError("SubtractCommand requires exactly 2 arguments.")
        return args[0] - args[1]
    