#  Q2)  Continue from Q1, move the last four lines of code into a module as a function, and call
# the function in test_main_or_import to display the nicer printout results

import textwrap

def fix_string(str):
    #  do a textwrap(variable) to reduce the string length for ease of read

    print(f'running fix_string(...) in the "{__name__}" module')
    #  sp = sorted(sys.path)
    dnames = ', '.join(str)

    print('without textwrap..\n', dnames)
    print('with textwrap..\n', textwrap.fill(dnames))
