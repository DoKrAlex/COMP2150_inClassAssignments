#Question 5
def count(st, x):
    # Count variable
    char = 0
    for i in range(len(st)):
        # Checking character in string
        if (st[i] == x):
            char = char + 1
    return (char)

st = "It is very hot and humid in Memphis in the Summer but not in Seattle"
x = input('Enter the character that you want to count in the string:\n')
print('there are', count(st,x), f'char \"{x}\" in the string')
x = input('try a different char, enter 9 to exit\n')
while x != '9':
    print('there are', count(st, x), f'char \"{x}\" in the string')
    x = input('try a different char, enter 9 to exit\n')
print('done')