"""
  This program builds a Queue class has the basic Queue functions

    - enqueue( data)
    - dequeue (data)
    - peek (data)
    - __repr__(self)
"""


class Queue:
    def __init__(self):
        self.data = []  # list type data.

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def enqueue(self, value):  # insert at Position 0
        self.data.insert(0, value)

    def dequeue(self):
        return self.data.pop()

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        return

    def __repr__(self):
        return repr(self.data)


# write codes
# Initialize
queue = Queue()

# Driver Code  Write codes here....
if __name__ == '__main__':
    print(f"Queue is_empty? ", queue.is_empty())
    print(f"Peek the queue: ", queue.peek())
    queue.enqueue("first")
    queue.enqueue("second")
    queue.enqueue("third")
    queue.enqueue("last")
    print(f'The queue is: {queue}')

    print(queue.is_empty())  # False
    print("The front is", queue.peek())  # 1

    # Remove item
    first_item = queue.dequeue()
    print("Dequeue the first item: ", first_item)  # 1

    print(queue)
