"""
  The name of the module (test_empty), which is being executed is always '__main__'
  Other modules are named after the filename
  What is import sys?  what is in sys?
  https://docs.python.org/3/library/sys.html
"""
import Q1_main as e1  # this import
import sys  # sys is a system specific parameters and functions
import Q2_fix_long_string as f1

#  import textwrap  # python build-in module used for wrapping and formatting plain text

# This makes the long path string easier to read
# __name__ is a special variable
# since we are running the program from this module (as level 0 indentation)
# The interpreter assigns the value __main__ to this variable __name__ to indicate the program starting point
print(f'what is the name ? {__name__}')  # print __main__

print(f"run sys,path for the module search paths")
print(sys.path)  # shows the list if directories that python (the interpreter) will search for the module

print(f'The imported file name = {e1.__name__}.py')

print(f'print the str in e1: {e1.str}')

# use the textwrap(variable) to reduce the string length for ease of reading
#  sp = sorted(sys.path)
#  dnames = ', '.join(sp)
#  print('without textwrap..\n', dnames)
#  print('with textwrap..\n', textwrap.fill(dnames))

# Q2 function
print('--' * 50)
# use the textwrap(variable) to reduce the string length for ease of reading
#  sptr = sorted(sys.path)
#  f1.fix_string(sptr)
f1.fix_string(sorted(sys.path))  # use this for function call
#   sp = sorted (sys.path)
#   dnames = ', '.join(sp)

#   print('without textwrap..\n', dnames)
#   print('with textwrap..\n', textwrap.fill(dnames))
