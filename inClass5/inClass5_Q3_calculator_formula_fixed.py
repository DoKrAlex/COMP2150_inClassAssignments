class FormulaError(Exception): pass


# Function parsing 1st and 3rd elements input as numbers
def parse_input(user_input):
    input_list = user_input.split()
    if len(input_list) != 3:
        raise FormulaError(
            'Input does not consist of three elements')  # Raises where there are a insufficient amount of elements input by the user
    n1, op, n2 = input_list
    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError as ex:
        raise FormulaError(
            'The first and third input value must be numbers')  # Raises when there is in exception with n1 and/or n2
    return n1, op, n2


# Function for calculating result from user inputs and verifying 2nd element as an operator
def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 / n2
    raise FormulaError('{0} is not a valid operator'.format(op))  # Raises when there is an exce


# Function for user input and raising the error message when an exception is presented
while True:
    user_input = input('>>> ')
    if user_input == 'quit':
        break
    try:  # tries the result for any exceptions
        n1, op, n2 = parse_input(user_input)
        result = calculate(n1, op, n2)
        print(result)
    except FormulaError as e:  # Will raise the statements from lines 13 and 26 when applicable
        print(f'Formula error: {e}')

'''
>>> 3.0 + 2.0
5.0
>>> a + b
Formula error: The first and third input value must be numbers
>>> 2 a 3
Formula error: a is not a valid operator
>>> 2 a
Formula error: Input does not consist of three elements
>>> quit
'''
