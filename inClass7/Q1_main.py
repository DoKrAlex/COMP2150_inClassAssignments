#  Q1)  Create two modules (empty.py and test_empty.py) files.  The empty file is a “shell”
# nothing.  The test_empty module is the main module.  You will import the empty file
# into the test_empty.py and check it out..
'''
A module used (imported) by test_Module.py to test __name__ ( a special variable), sys.path
(empty,py search path)
'''

print(f'File __name__ = {__name__}')
if __name__ == "__main__":
    print("empty is being run directly")  #you can run this module (empty.py) from this py file
else:
    print("empty is being imported")
str = " I am in Q1_main.py "
# end of empty.py file