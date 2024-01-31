
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
