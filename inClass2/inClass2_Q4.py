#Question 4
def count(st, x):
    char = 0
    st = st.split()
    for i in range(len(st)):
        if (st[i] == x):
            char = char + 1
    return(char)


st = "This is very hot and humid in Memphis"
x = input('Enter the character that you want to count in the string:\n')

print('there are', count(st,x), 'char in the string')
