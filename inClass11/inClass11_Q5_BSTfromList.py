"""
The inorder, insert(..) methods are defined outside to BST_Node Class

"""
from randomNumLst import ranGen
from BST_util import *


# A class to store a BST node
class BST_Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        # self.count = 0

    def insert(self, data):
        if data == self.data:  # skip (return) if new data exist already in the tree
            return
        # Recursively call the insert method to add the data to the leaf
        if data < self.data:
            # Add to left subtree
            if self.left:  # keep calling insert(data) until none (leaf)
                self.left.insert(data)
            else:  # at leaf add the BST_Node(data)
                self.left = BST_Node(data)
        # Recursively callthe insert method to add the data to the leaf
        else:
            # Add to right subtree
            if self.right:  # keep calling insert(data) until none (leaf)
                self.right.insert(data)
            else:
                self.right = BST_Node(data)

    def search_element(self, elem, count):  # complexity of O(log n)

        count += 1
        if self is None:
            return -1, count + 1
        if self.data == elem:
            print(f'find {elem} at {count}')
            return
        elif elem < self.data:
            # if yes, element would be on the left
            if self.left:
                return self.left.search_element(elem, count), count + 1
            else:
                return False
        else:
            # if yes, element would be on the right

            if self.right:
                return self.right.search_element(elem, count), count + 1
            else:
                return False

    def deleteNode(self, rt, key):
        # Base Case
        if rt is None:
            return rt

        # If the key to be deleted is smaller than the root's key then it is in  left subtree
        if key < rt.data:
            rt.left = rt.deleteNode(rt.left, key)

        # If the data to be delete # is greater than the root's data then it lies in right (successor) subtree

        elif (key > rt.data):
            rt.right = rt.deleteNode(rt.right, key)

        # If key is same as root's key, then this is the root node to be deleted
        else:
            # BST_Node with only one child or no child
            if rt.left is None:
                temp = rt.right
                rt = None
                return temp

            elif rt.right is None:
                temp = rt.left
                rt = None
                return temp

            # BST_Node with two children: Get the smallest of successor (smallest in the right subtree)
            temp = minValueNode(rt.right)

            # Copy the inorder successor's
            # content to this node
            rt.data = temp.data

            # Delete the inorder successor
            rt.right = rt.deleteNode(rt.right, temp.data)

        return rt

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def lst_to_BST(lst_elem):
    if len(lst_elem) > 1:
        # start with ls[0] as root
        root_node = BST_Node(lst_elem[0])

        for x in lst_elem:
            root_node.insert(x)
        return root_node
    else:
        return print("Insufficient number of elements")


if __name__ == '__main__':
    key1 = [15, 10, 20, 8, 70, 12, 16, 25, -3, 23, 67, 12, 99, -5, -2]
    key3 = [60, 55, 100, 45, 57, 67, 107, 101]  # sample for lecture slide
    key4 = ["Maria", "Adam", "Justin", "Doug", "Amanda", 'Nicholas', 'Hana', 'Greese', 'Joseph', 'Noah', 'Alicia',
            'Chance', 'Ken', 'Larry', 'Oliver']
    key2 = ranGen(100)
    Key_used = key2

    x = lst_to_BST(Key_used)

# add codes here...
    x.display()
    inorder(x)
    print()

    print('-' * 50)
    print("Original list:\n", Key_used)
    print("inorder")
    inorder(x)
    print("\npreorder")
    pre_order(x)
    print("\npost_order")
    postorder(x)

    print("\ndelete 75 from the list")
    x.deleteNode(x, 75)
    x.display()

    search = x.search_element(65, count=0)
    print("search history ", search)

