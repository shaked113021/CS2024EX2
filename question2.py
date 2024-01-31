from typing import Callable


# Entry point for program
def main():
    command_executor = BinaryOperatorCommandExecutor()

    command_executor.register(BinaryOperatorCommand('|', 'OR', or_gate))
    command_executor.register(BinaryOperatorCommand('&', 'AND', and_gate))
    command_executor.register(BinaryOperatorCommand('^', 'XOR', xor_gate))
    command_executor.register(BinaryOperatorCommand('~', 'NAND', nand_gate))

    first_digit = input_binary_digit("first digit")
    second_digit = input_binary_digit("second digit")

    logical_gate_input_message = (f"Enter the symbol for the logical gate("
                                  f"{','.join(command_executor.get_registered_operator_symbols())}): ")
    logical_gate = input(logical_gate_input_message)

    logical_input_result = command_executor.execute(logical_gate, first_digit, second_digit)
    while logical_input_result is None:
        print("Invalid Input! Please try again")
        logical_gate = input(logical_gate_input_message)
        logical_input_result = command_executor.execute(logical_gate, first_digit, second_digit)

    print(logical_input_result)


class BinaryOperatorCommand:

    def __init__(self, symbol: str, name: str, callback: Callable[[int, int], int]):
        self.symbol = symbol
        self.name = name
        self.callback = callback


class BinaryOperatorCommandExecutor:

    def __init__(self):
        self._registeredCommands: {str, BinaryOperatorCommand} = {}

    def get_registered_operator_symbols(self):
        return self._registeredCommands.keys()

    def register(self, binary_operator_command: BinaryOperatorCommand):
        self._registeredCommands[binary_operator_command.symbol] = binary_operator_command
        return self

    def execute(self, command_symbol: str, left_arg: int, right_arg: int) -> str | None:
        # Get command from dictionary
        command: BinaryOperatorCommand = self._registeredCommands.setdefault(command_symbol, None)

        if command is None:
            return None

        return (f"Operation {command.name}: {left_arg} {command.symbol} {right_arg} gives: "
                f"{command.callback(left_arg, right_arg)}")


def validate_binary_digit(digit: str):
    return digit in ['0', '1']


def input_binary_digit(argument_name: str) -> int:
    input_message = f"Please enter a binary digit(0, 1) for {argument_name}: "
    user_input = input(input_message)
    while not validate_binary_digit(user_input):
        print("Invalid Input! try again")
        user_input = input(input_message)

    return int(user_input)


# region Logic gate functions
def xor_gate(left_arg: int, right_arg: int) -> int:
    """
    Calculate xor on two input that must be 0 or 1
    :param left_arg: int, 0 or 1
    :param right_arg: int, 0 or 1
    :return: if arguments are the same 0, otherwise 1
    """
    allowed_values = [0, 1]
    # check that the arguments have the right type and value
    if (not isinstance(left_arg, int)) or (not isinstance(right_arg, int)):
        raise TypeError(f"Expected arguments to be of type ('int', 'int')  got ({type(left_arg)}, {type(right_arg)})")
    if left_arg not in allowed_values:
        raise ValueError(f"left_arg have invalid value. expected 0 or 1, got {left_arg}")
    if right_arg not in allowed_values:
        raise ValueError(f"right_arg have invalid value. expected 0 or 1, got {right_arg}")

    # if values equal return 0. otherwise return 1
    if left_arg == right_arg:
        return 0
    return 1


def nand_gate(left_arg: int, right_arg: int) -> int:
    """
    Calculate NAND on given inputs
    :param left_arg: int, must be 1 or 0
    :param right_arg: int, must be 1 or 0
    :return: 0 if both arguments are 1, 1 otherwise
    """
    allowed_values = [0, 1]
    # check that the arguments have the right type and value
    if (not isinstance(left_arg, int)) or (not isinstance(right_arg, int)):
        raise TypeError(f"Expected arguments to be of type ('int', 'int')  got ({type(left_arg)}, {type(right_arg)})")
    if left_arg not in allowed_values:
        raise ValueError(f"left_arg have invalid value. expected 0 or 1, got {left_arg}")
    if right_arg not in allowed_values:
        raise ValueError(f"right_arg have invalid value. expected 0 or 1, got {right_arg}")

    # if both are 1 return 0, otherwise return 1
    if left_arg == 1 and right_arg == 1:
        return 0
    return 1


def and_gate(left_arg: int, right_arg: int) -> int:
    """
    Gets two integers with either a 1 or 0 value, calculates their 'and' value
    :param left_arg: either a 1 or a 0
    :param right_arg:  either a 1 or a 0
    :return: 1 if both args equal 1. 0 otherwise
    """
    allowed_values = [0, 1]
    # check that the arguments have the right type and value
    if (not isinstance(left_arg, int)) or (not isinstance(right_arg, int)):
        raise TypeError(f"Expected arguments to be of type ('int', 'int')  got ({type(left_arg)}, {type(right_arg)})")
    if left_arg not in allowed_values:
        raise ValueError(f"left_arg have invalid value. expected 0 or 1, got {left_arg}")
    if right_arg not in allowed_values:
        raise ValueError(f"right_arg have invalid value. expected 0 or 1, got {right_arg}")

    if left_arg == right_arg == 1:
        return 1
    return 0


def or_gate(left_arg: int, right_arg: int) -> int:
    """
    Takes two integers either 1 or 0 each, calculates their or value
    :param left_arg: integer either 1 or a 0
    :param right_arg: integer either 1 or a 0
    :return: 1 if at least one of the arguments are 1, 0 otherwise
    """
    allowed_values = [0, 1]
    # check that the arguments have the right type and value
    if (not isinstance(left_arg, int)) or (not isinstance(right_arg, int)):
        raise TypeError(f"Expected arguments to be of type ('int', 'int')  got ({type(left_arg)}, {type(right_arg)})")
    if left_arg not in allowed_values:
        raise ValueError(f"left_arg have invalid value. expected 0 or 1, got {left_arg}")
    if right_arg not in allowed_values:
        raise ValueError(f"right_arg have invalid value. expected 0 or 1, got {right_arg}")

    if left_arg == 1 or right_arg == 1:
        return 1
    return 0

# endregion


if __name__ == '__main__':
    main()
