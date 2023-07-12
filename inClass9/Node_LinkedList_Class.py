"""
    Use the following two classes (Node, and LinkedList) for your HW5 assignment
"""


# Node class
class Node:
    # to generate node objects Node(number)
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

    def __str__(self):
        return f'{self.data} ->  {self.next}'


# Linked List class contains a Node object
class LinkedList:
    # head should be first node of the linkedlist
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(f'{temp.data}'" ->", end=" ")
            temp = temp.next
        print('none')

    def __str__(self):
        # self.printList()
        return f'{self.printList()}'


def mainA():
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)
    llist.head.next.next = Node(3)
    print(Node(1))
    print(Node(2))
    print(Node(3))
    print("connect the nodes first, second, third")
    print("\nHW5-a add node(9) to the after the head of the current linkedList")
    print("Before ")
    llist.__str__()
    llist.head.next = Node(9)
    print("After:   ")
    llist.__str__()


mainA()


def mainB():
    print("\nHW5-b---------- insert node(9) between node(1) and node(2)")
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)
    llist.head.next.next = Node(3)
    print("Before ")
    llist.__str__()
    node_new = Node(9)
    node_new.next = llist.head.next
    llist.head.next = node_new
    print("HW5-b---------")
    print("After:   ")
    llist.__str__()


mainB()


def mainC():
    print("\nHW5-c------------- replace node(7) and node (8) with node(5)")
    llist = LinkedList()
    llist.head = Node(7)
    llist.head.next = Node(8)
    llist.head.next.next = Node(3)
    print("Before ")
    llist.__str__()
    node_new = Node(5)
    node_new.next = llist.head.next.next
    llist.head = node_new
    print("HW5-C ----- result---c--- ------")
    print("After:   ")
    llist.__str__()


mainC()


def mainD():
    print("\nHW5-d -----add to the end of the list ---------start------")
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)
    print("Before ")
    llist.__str__()
    llist.head.next.next = Node(3)
    print("HW5-D ----- result---c--- ------")
    print("After:   ")
    llist.__str__()


mainD()


def mainE():
    print("\nHW5-e -----add to the start of the list ---------start------")
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)
    print("Before ")
    llist.__str__()
    new_node = Node(3)
    new_node.next = llist.head
    llist.head = new_node
    print("HW5-e ----- result---c--- ------")
    print("After:   ")
    llist.__str__()


mainE()


def mainF():
    print("\nHW5 -f ---------------- combine two linkedLists -----")
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)

    temp = LinkedList()
    temp.head = Node(3)
    temp.head.next = Node(4)
    print("Before \nlist -->")
    llist.__str__()
    print("temp -->")
    temp.__str__()

    temp.head.next.next = llist.head.next
    llist.head.next = temp.head
    print("After:   \nlist -->")
    llist.__str__()


mainF()


def mainG():
    print("\nHW5 -g ---------------- split one linkedLists into two -----")
    llist = LinkedList()
    llist.head = Node(1)
    llist.head.next = Node(2)
    llist.head.next.next = Node(3)
    print("Before ")
    llist.__str__()
    list2 = LinkedList()
    list2.head = Node(llist.head.data)
    llist.head = llist.head.next
    list2.head.next = llist.head.next
    llist.head.next = None

    print("After:   \nlist -->")
    llist.__str__()
    print("List2 -->")
    list2.__str__()


mainG()
