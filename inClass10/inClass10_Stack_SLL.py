"""
This inClass assignment focuses on Stack.

Stack Operations:

push() : Insert a new element into stack i.e just inserting a new element at the beginning of the linked list.
pop() : Return top element of the Stack i.e simply deleting the first element from the linked list.
peek(): Return the top element.
display(): Print all elements in Stack.
"""


class Node:
    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    # head is default NULL
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # Method to add data to the stack
    # adds to the start (head) of the stack
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    # Remove element that is the current head (start of the stack)
    def pop(self):

        if self.is_empty():
            return None

        else:
            # Removes the head node and makes the preceding one the new head
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    # Returns the head node data
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    # Prints out the stack
    def display(self):
        internode = self.head
        if self.is_empty():
            print("Stack Underflow --- empty")
        else:
            while (internode != None):
                print(internode.data, "->", end=" ")
                internode = internode.next
            print('none')
            return


# Driver code
MyStack = Stack()

MyStack.push("First")
MyStack.push('Second')
MyStack.push('Third')
MyStack.push('Last')

# Display stack elements
MyStack.display()

# Print top element of stack
print("\nTop element is: ", MyStack.peek())

# Delete top elements of stack
print(f'Pop the stack!: {MyStack.pop()}')

# Display stack elements
print('\nThe new stack after popping is: ')
MyStack.display()

# Print top element of stack
print("\nTop element is: ", MyStack.peek())

'''
Results:
Last -> Third -> Second -> First -> none

Top element is:  Last
Pop the stack!: Last

The new stack after popping is: 
Third -> Second -> First -> none

Top element is:  Third
'''