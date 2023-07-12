'''
Using Collections 
Queue in Python can be implemented using deque class from the collections module.
    Deque is preferred over list in the cases where we need quicker append and pop operations
        from both the ends of container,
        as deque provides an O(1) time complexity for append and pop operations
        as compared to list which provides O(n) time complexity.
            Instead of enqueue and deque, append() and popleft() functions are used.
'''


# Python program to
# demonstrate queue implementation using collections.deque

from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('first in')
q.append('second')
q.append('third')
q.append("last out")

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print("after popLeft() :", q)
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty