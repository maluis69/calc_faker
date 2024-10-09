from .command import Command

class DivideCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            raise ValueError("DivideCommand requires exactly 2 arguments.")
        if args[1] == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return args[0] / args[1]
