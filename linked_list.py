class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    ## new node is inserted at the beginning of the list
    def insertFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    ## insert a new node after a given previous node
    def insertAfter(self, pre_node, new_data):
        if pre_node == None:
            print("The given previous node is not in the list.")
            return
        new_node = Node(new_data)
        new_node.next = pre_node.next
        pre_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while (current.next != None):
                current = current.next

            current.next = new_node

    def delete(self, target):
        current = self.head

        ## handle the special case that the first node is to be deleted
        if self.head != None and self.head.value == target:
            self.head = self.head.next
            return current

        while (current != None):
            if current.value == target:
                break
            pre = current
            current = current.next

        ## If current is None, the target is not in the list
        if current == None:
            return None

        pre.next = current.next
        current = None

    def print_list(self):
        if self.head == None:
            print("The list is empty!")
        else:
            current = self.head

            while (current != None):
                print(current.value)
                current = current.next

llist = LinkedList()
llist.insertFront(15)
llist.insertFront(12)
llist.append(1)
llist.insertFront(3)
llist.append(2)
llist.insertAfter(llist.head.next, 6)
llist.delete(3)
llist.delete(8)
llist.insertFront(10)
llist.delete(1)
llist.insertAfter(llist.head.next.next, 17)
llist.print_list()

