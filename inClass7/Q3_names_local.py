#  Not all objects are imported with ‘*’. For this exercise, create two modules
# (Q3_names_local.py, Q3_test_names_local.py)

_version = 1.0
def show_names(names):
    for i in names:
       print(i, end= ', ')
def _show_version():
    print(_version)