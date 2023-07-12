# inClass9

# Node class
class Node:
    def __init__(self, data):
        self.data = data  # assign data
        self.next = None  # initialize next as null
    def __str__(self):
        return f'{self.data} -> {self.next}'

# Linked List class contain a Node object
class LinkedList:
    # head should be first node of the linkedList
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(f'{temp.data}'" ->", end = " ")
            temp = temp.next
        print('none')


    def __str__(self):
        #  self.printList()
        return(f'{self.printList()}')

    def append(self, new_data):
        # 1. create a new node
        # 2. put in the data
        # 3. set next as None (last node)
        new_node = Node(new_data)

        # 4. if the linked list is empty, then make the it the new node as head
        if self.head is None:
            self.head = new_node
            return

        # 55. else traverse (start from the head) till the last node (when None)
        last = self.head
        while last.next:  # inch-worm to the last node (from the head)
            last = last.next

        last.next = new_node




if __name__ == '__main__':

    #  start with the empty list
    first = LinkedList()
    #  make three nodes, first.head has the Node(1) object
    first.head = Node(1)
    second = Node(2)
    third = Node(3)
    print(first.head)
    print(second)
    print(third)

    print('connect the nodes first, second, third')

    first.head.next = second

    second.next = third

    first.printList()
    first.head.next = Node(9)
    first.printList()

    print('\n\ncreating a new linked list from a list \n')
    lst = [11, 22, 33, 44, 55, 66]
    print(lst)
    lnk_from_lst = LinkedList()
    for x in lst:
        lnk_from_lst.append(x)
    print(lnk_from_lst)
