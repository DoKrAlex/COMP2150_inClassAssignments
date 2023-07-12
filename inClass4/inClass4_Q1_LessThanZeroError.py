# Define a custom exception type
class LessThanZeroError(Exception):
    def __init__(self, value):
        self.value = value


try:
    my_num = int(input('Enter number: '))  # variable for user input

    if my_num < 0:
        e1 = LessThanZeroError(my_num)  # e1 is an LessThanZeroError object
        raise LessThanZeroError(f'You entered my_num: {e1.value}, it must be greater than 0!')

except ValueError:
    print('Your entered number is: NAN')
except LessThanZeroError as ex:  # ex variable captures and displays the raised message from line 11
    print(f'less than zero')
    print(f'{ex}')
else:
    print(f'Entered value is {my_num}')
finally:
    print(f'Done')

''' ~ results:
Enter number: a
Your entered number is: NAN
Done
......
Enter number: -9
You entered my_num: -9, it must be greater than 0!
Done
.....
Enter number: 8
Entered value is 8
Done
'''
