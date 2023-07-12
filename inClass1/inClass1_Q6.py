#Question 6
#6a
print(f'\n\na. print-oriented (brute force)')
print('hello', end = ' ')
print('hello', end = ' ')
print('hello', end = ' ')
print('hello', end = ' ')
print('hello')

#6b
print(f'\n\nb. using a repetition operator (*)')
print('hello' * 5)

#6c
print(f'\n\nc. using a for loop with range(x)')
h = 'hello'
for a in range(5):
    print(h, end = " ")
print()

#6d
print(f'\n\nd. create a function to print five times (same a 3.) with n times')
def function(str, n):
    while n > 0:
        print(str, end = ' ')
        n -= 1
        function('hello', 5)
#6e
print(f'\n\ne. use a range(len(str)')
s = 'hello'
for a in range(5):
    print(s, end = ' ')
print()
for b in range(len(s)):
    print(s, end = ' ')
print()

#6f
print(f'\n\nf. using repetition operator twice')
print(* 'hello ' * 5)

#6g
print(f'\ng. using .join(str) to convert to a string')
print(' '.join('hello ') * 5)