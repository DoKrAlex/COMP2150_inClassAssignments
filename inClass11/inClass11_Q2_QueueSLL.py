#  program to demonstrate implementing Queue using a singly linked list
# based implementation of queue

# A linked list (LL) node
# to store a queue entry
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# A class to represent a queue

# The queue,
#   front (aka head) stores the front node of LL and
#   rear (aka tail)  stores the last node of LL
class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    # Method (enQueue(...) to add an item to the queue rear
    def enQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # Method (DeQueue(...) to remove an item from the queue front
    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None

    def display(self):
        iternode = self.front

        while (iternode != None):
            print(iternode.data, "->", end=" ")
            iternode = iternode.next
        print('none')
        return


# Driver Code  Write codes here....
if __name__ == '__main__':
    q = Queue()
    q.enQueue("first")
    q.enQueue("second")
    q.enQueue("third")
    q.enQueue("last")
    q.display()

    print('\nRemove/Dequeue the first value (FIFO) ')
    q.DeQueue()
    q.display()

    print("The queue's first value is now: ", str(q.front.data))
    print("The queue's last value is now: ", str(q.rear.data))

    print("\nAdd a list of numbers to the queue")
    for x in range(10):
        q.enQueue(x)
    q.display()

    print(f"The queue's last value is now: {q.rear.data}")
