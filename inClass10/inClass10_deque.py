"""

"""

from collections import deque
d = deque()
d.append(9)
print(f'Starting with adding 9 to the queue {d}')
d.appendleft(8)
print(f'Add 8 to the left of the queue {d}')

d.clear()
print(f'Clear the queue using (.clear()) {d}')
d.extend('1')
print(f'Use extend to add 1 {d}')
d.extendleft('234')
print(f'Use extend to add to the queue {d} ...  [1] is the first in')
d.pop()  # removes the far-right (first in)
print(f'')