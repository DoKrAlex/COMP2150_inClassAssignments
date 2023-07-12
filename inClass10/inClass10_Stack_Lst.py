"""
This inClass assignment focuses on Stack.

Stack Operations:

push() : Insert a new element into stack i.e just inserting a new element at the beginning of the linked list.
pop() : Return top element of the Stack i.e simply deleting the first element from the linked list.
peek(): Return the top element.
display(): Print all elements in Stack.
"""

class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def __repr__(self):
        return repr(self.data)


# initialization
stack = Stack()

print("Is the stack empty?: ", stack.is_empty())  # True

# Add items
stack.push('First')
stack.push('Second')
stack.push('Third')
stack.push('Last')

print(stack)

print("Is the stack empty?: ", stack.is_empty())  # False


# Remove item
last_item = stack.pop()  # Default far right (last)
print(f'Pop the last item in the stack, "{last_item}"')  # last

print(f'The updated stack is now "{stack}"')

'''
Results: 
Is the stack empty?:  True
['First', 'Second', 'Third', 'Last']
Is the stack empty?:  False
Pop the last item in the stack, "Last"
The updated stack is now "['First', 'Second', 'Third']"
'''