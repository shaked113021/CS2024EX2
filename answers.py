# EX2 Q1

# using main function to aid readability of program
def main():
    operators = {}  # hold operators dynamically to allow for extension

    # register add operator
    def add_operator(num1: float | int, num2: float | int) -> str:
        return f"Sum of {num1} and {num2} is {num1 + num2}"
    operators['+'] = add_operator

    # register multiply operator
    def multiply_operator(num1: float | int, num2: float | int) -> str:
        return f"Product of {num1} and {num2} is {num1 + num2}"
    operators['*'] = multiply_operator

    # as long as program loop returns True, Execute again
    while program_loop(operators):
        pass


# Executes as long as num1 and num2 are both not -1
# returns True if another iteration is required
def program_loop(operators_dict: dict) -> bool:
    print('please enter two numbers, input -1 twice to quit')
    # get two numbers from user
    num1 = input_decimal('first number')
    num2 = input_decimal('second number')

    # if both num1 and num2 are -1, end execution
    if num1 == num2 == -1:
        return False

    # get input from user for operator and execute it
    operator_input_message = f"please enter an operator, can be ({','.join(operators_dict.keys())}): "
    operator = input(operator_input_message)
    operation_result = execute_operator(operators_dict, operator, num1, num2)

    # as long as operator is invalid, try again
    while operation_result is None:
        operator = input(f"Invalid Operator! {operator_input_message}")
        operation_result = execute_operator(operators_dict, operator, num1, num2)

    # executing succeeded, print result
    print(operation_result)
    return True  # Run another iteration after this


def is_valid_decimal(candidate: str) -> bool:
    """
    Checks if given string is a valid decimal number, valid characters are digits(1-9), minus sign('-')
     as first character and a decimal dot
    :param candidate: a string to check
    :return: type bool. True if is valid decimal, False otherwise
    """
    for index, char in enumerate(candidate):
        if (index != 0 and char == '-') or (char not in ['.', '-'] and not char.isdigit()):
            return False
    return True


def input_decimal(argument_name: str) -> float | int:
    """
    A function that tries to get a decimal value from stdin
    Tries continuously until input is valid
    :param argument_name: the display name of the argument requested
    :return: decimal value entered
    """
    input_str = f"Please enter a decimal value for {argument_name}: "  # define a generic input string for reuse

    # as long as input is invalid, get new input from user
    num_input = input(input_str)
    while not is_valid_decimal(num_input):
        print("Invalid Input! allowed chars are numeric(1-9), minus sign('-') and a decimal dot('.')")
        num_input = input(f"Try again. {input_str}")

    # Check if input given contains a decimal dot. if it is, cast to a float and return
    # Otherwise cast to int and return
    if '.' in num_input:
        return float(num_input)
    return int(num_input)


def execute_operator(operators_dict: dict, operator: str, num1: float | int, num2: float | int) -> str | None:
    """
    Execute code attached to given operator
    :param operators_dict: dictionary of operators with their callbacks
    :param operator: operator string
    :param num1: left hand argument
    :param num2: right hand argument
    :return: result of operator as a string if operator exist, None otherwise
    """
    # Retrieve callback from a dictionary with a default value of None
    callback = operators_dict.setdefault(operator, None)
    if callback is None:
        return None
    return callback(num1, num2)


if __name__ == '__main__':
    main()
# EX2 Q2
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
# EX2 Q3
def print_upper_triangle(matrix: [[]]) -> None:
    """
    Prints the upper triangle of a matrix
    :param matrix: a matrix in size n * n which contains chars
    :return: None
    """
    PRINTED_COLUMN_SIZE = 5  # num of chars in column
    if not isinstance(matrix, list):
        raise TypeError('Expected matrix to be a list')

    number_of_rows = len(matrix)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('One or more of the elements in given list is not a list.')
        if len(row) != number_of_rows:
            raise ValueError('Expected number of rows and columns in matrix to be the same')

    for row_index, row in enumerate(matrix):
        print((' ' * PRINTED_COLUMN_SIZE) * row_index, end='')
        for column_index in range(row_index, len(row)):
            spaces_at_end = PRINTED_COLUMN_SIZE - len(str(row[column_index]))
            print(row[column_index], end=(' ' * spaces_at_end))
        print()
# EX2 Q4
# Entry Point
def main():
    num_stars_input = input('Please enter a positive even number for starting amount of stars: ')
    while not num_stars_input.isnumeric() or int(num_stars_input) % 2 != 0:
        num_stars_input = input("Invalid Input! input must be a positive even number. please try again: ")

    num_stars = int(num_stars_input)
    del num_stars_input
    print_star_pattern(num_stars)


def print_star_pattern(num_stars: int):
    """
    prints out a pattern of stars(*) and @ sign using the following the pattern: num_stars, num_stars-2, num_stars-4 ... 2
    :param num_stars: num of stars to be printed
    :return:
    """
    # start with a given value and decrement by 2 each time until we reach 0
    for star_times in range(num_stars, 0, -2):
        print(('*' * star_times) + '@', end='')
    print()


if __name__ == '__main__':
    main()
# EX2 Q5
def main():
    candidate = input('Please enter a string to be evaluated as palindrome: ')
    print(f"{candidate} is {'' if is_palindrome(candidate) else 'not '}a palindrome")


def is_palindrome(candidate: str, left_index: int=0, right_index: int=-1) -> bool:
    """
    Gets a string and checks if it is a palindrome
    :param candidate: a string to be checked
    :param left_index: the index of the left char to compare
    :param right_index: the index of the right index to compare. -1 is used to indicate the right-most character
    :return:
    """

    # checks if we given the default value for right index. if it was given, set the right index to the last element
    if right_index == -1:
        right_index = len(candidate) -1

    # an empty string is a palindrome by definition
    if candidate == '':
        return True

    # base condition. if we reached the middle values and they are equal, return true
    if left_index == right_index:
        return True
    if left_index == right_index - 1:
        return candidate[left_index] == candidate[right_index]

    # step. recursively call is palindrome on candidate while moving the indices toward the middle
    return (candidate[right_index] == candidate[left_index]) and is_palindrome(candidate, left_index + 1, right_index - 1)


if __name__ == '__main__':
    main()
# EX2 Q6
def find_minimum_index(to_check: list, start_index: int) -> int:
    minimum_index = start_index
    length_of_list = len(to_check)
    for index in range(minimum_index + 1, length_of_list):
        if to_check[index] < to_check[minimum_index]:
            minimum_index = index
    return minimum_index


def selection_sort(to_sort: list):
    # Check type of argument
    if not isinstance(to_sort, list):
        raise TypeError('Expected to_sort to be of type\'list\'')
    length_of_list = len(to_sort)
    for current_index in range(length_of_list):
        # find minimum
        minimum_index = find_minimum_index(to_sort, current_index)
        # swap, nicer way to write it in python
        if minimum_index != current_index:
            to_sort[current_index], to_sort[minimum_index] = to_sort[minimum_index], to_sort[current_index]

# EX2 Q7
def merge_lists_not_efficient(list_a: list, list_b: list) -> list:
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise TypeError("Expected arguments to be lists")
    # copy of list_a, with b appended
    extended_list = [value for value in list_a]
    extended_list.extend(list_b)
    selection_sort(extended_list)
    return extended_list
# EX2 Q8
# wrapping all list as a queue like structure
# wrapping all list as a queue like structure
class _ListQueueIterator:
    """Wrap lists like a walkable queue for easier linear access"""
    def __init__(self, to_walk: list):
        self._to_walk = to_walk
        self._to_walk_length = len(to_walk)
        self._current_index = 0

    def is_at_end(self) -> bool:
        """Check if last value was polled"""
        return self._current_index == self._to_walk_length

    def peek(self):
        """take current value but don't move forward, return None at end"""
        if self._current_index < self._to_walk_length:
            return self._to_walk[self._current_index]
        else:
            return None

    def poll(self):
        """return current value and move forward"""
        if self._current_index < self._to_walk_length:
            return_value = self.peek()
            self._current_index += 1
            return return_value
        else:
            return None


def merge_efficient(list_a, list_b) -> list:
    """
    Take in to lists and merges them together
    :param list_a: first list to be merged must be sortd
    :param list_b: second list to be merged must be sorted
    :return: new list made of the given lists in
    """
    if not isinstance(list_a, list):
        raise TypeError('Expected list_a to be of type\'list\'')
    if not isinstance(list_b, list):
        raise TypeError('Expected list_b to be of type\'list\'')
    list_a_iterator = _ListQueueIterator(list_a)
    list_b_iterator = _ListQueueIterator(list_b)
    merged_list = []

    # appending values from list_a and list_b until reaches the end of one of them
    while (not list_a_iterator.is_at_end()) and (not list_b_iterator.is_at_end()):
        # current value in list_a is smaller
        if list_a_iterator.peek() < list_b_iterator.peek():
            merged_list.append(list_a_iterator.poll())
        # current value in list_b is smaller
        elif list_b_iterator.peek() < list_a_iterator.peek():
            merged_list.append(list_b_iterator.poll())
        # values are equal
        else:
            merged_list.append(list_a_iterator.poll())
            merged_list.append(list_b_iterator.poll())

    # append remaining items of list_a
    while not list_a_iterator.is_at_end():
        merged_list.append(list_a_iterator.poll())

    # append remaining items of list_b
    while not list_b_iterator.is_at_end():
        merged_list.append(list_b_iterator.poll())

    return merged_list

