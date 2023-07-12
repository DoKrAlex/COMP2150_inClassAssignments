"""
This inClass assignment focuses on stack - dequeue.
"""

from collections import deque

s = deque()
s.append('First')
s.append('Second')
s.append('Third')
s.append('Last')

print(s)
print(f'Pop the stack (LIFO) : {s.pop()}')

print(f'Print after a popLeft() : {s.popleft()}')
print(s)

s.append('Extra one')
s.append('Extra two')
print(s)

'''
Results:

deque(['First', 'Second', 'Third', 'Last'])
Pop the stack (LIFO) : Last
Print after a popLeft() : First
deque(['Second', 'Third'])
deque(['Second', 'Third', 'Extra one', 'Extra two'])
'''