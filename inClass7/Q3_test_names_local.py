'''
 This program demonstrates the properties of import (names_local), and using
    locals( ) to return the dictionary of the current local symbol table and the local symbol
table.
'''
import textwrap
from Q3_names_local import *
# have to enter the following explicitly
from Q3_names_local import _version, _show_version
names = ["Brianna", "Nicholas", "Julia", "Veronica", "Christian", "Jimmy", "Tyler",
"Hanna", "Jazmin"]
dnames = ', '.join(locals())  # construct the symbol table.
print('with textwrap to display python symbol,,\n',textwrap.fill(dnames))
show_names(names)
_show_version()