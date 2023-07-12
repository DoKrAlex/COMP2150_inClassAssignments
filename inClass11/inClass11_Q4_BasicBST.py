from BST_util import *

class BST_Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

# function to insert for a new BST

def insert(root, data):
    if root is None:
        root = BST_Node(data)
        return root
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right= insert(root.right, data)
    return root

def show(root):  # inorder pattern
    if root:
        show(root.left)
        print(root.data)
        show(root.right)

#  write codes here...
b1 = BST_Node(50)
b1 = insert(b1, 20)
b1 = insert(b1, 30)
b1 = insert(b1, 40)
b1 = insert(b1, 60)
b1 = insert(b1, 70)
b1 = insert(b1, 80)

print("calling show() recursive")
show(b1)
print('\nin_order: ')
inorder(b1)
print('\npre_order: ')
pre_order(b1)
print('\npostorder: ')
postorder(b1)

x = minValueNode(b1)
print("\nThe BST min is ", x)
y = maxiValueNode(b1)
print("The BST max is ", y)
