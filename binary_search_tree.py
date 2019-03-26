class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def insert(self, new_data):
        new_node = Node(new_data)

        if self.value:
            if self.value > new_data:
                if self.left is None:
                    self.left = new_node
                    new_node.parent = self
                else:
                    self.left.insert(new_data)

            elif self.value < new_data:
                if self.right is None:
                    self.right = new_node
                    new_node.parent = self
                else:
                    self.right.insert(new_data)
        else:
            self.value = new_data

    def findMin(self):
        if self.value:
            current = self
            while (current.left is not None):
                current = current.left
            return current

    def findMax(self):
        if self.value:
            current = self
            while (current.right is not None):
                current = current.right
            return current

    def search(self, target):
        if target == self.value:
            return self
        elif target < self.value:
            if self.left is None:
                return None
            return self.left.search(target)
        elif target > self.value:
            if self.right is None:
                return None
            return self.right.search(target)

    def predecessor(self, target):
        x = self.search(target)
        if x:
            if x.left is not None:
                return x.left.findMax()
            else:
                current = x.parent
                while True:
                    if current is None:
                        return None
                    if current.value < x.value:
                        return current
                    current = current.parent
        else:
            print(str(target) + " is not in the tree")
            return -1


    def successor(self, target):
        x = self.search(target)
        if x:
            if x.right is not None:
                return x.right.findMin()
            else:
                current = x.parent
                while True:
                    if current is None:
                        return None
                    if current.value > x.value:
                        return current
                    current = current.parent
        else:
            print(str(target) + " is not in the tree")
            return -1

    def delete(self, target):
        x = self.search(target)
        if x:
            ## if the deleting node is the root
            if x == self:
                ## Case 1: x is a leaf
                if x.left is None and x.right is None:
                    self.value = None

                ## Case 2.1: x has only left child
                elif x.right is None:
                    x.left.parent = None
                    self.value = x.left.value
                    self.right = x.left.right
                    self.left = x.left.left

                ## Case 2.2: x has only right child
                elif x.left is None:
                    x.right.parent = None
                    self.value = x.right.value
                    self.left = x.right.left
                    self.right = x.right.right

                ## Case 3: x has two children
                else:
                    if self.successor(target):
                        y = self.successor(target)
                    else:
                        y = self.predecessor(target)

                    ## special case: the right child of x is directly the successor of x
                    ## which means the right child of x doesn't have left child
                    if x.right == y:
                        y.parent = None
                        self.value = y.value
                        self.right = y.right
                        self.left.parent = y
                    else:
                        if y.right:
                            y.right.parent = y.parent
                        y.parent.left = y.right
                        y.parent = None
                        self.value = y.value
                        y.left = x.left
                        y.right = x.right

            else:
                ## Case 1: x is a leaf
                if x.left is None and x.right is None:
                    if x.parent.left == x:
                        x.parent.left = None
                    elif x.parent.right == x:
                        x.parent.right = None

                ## Case 2.1: x has only left child
                elif x.right is None:
                    if x.parent.left == x:
                        x.parent.left = x.left
                        x.left.parent = x.parent
                    elif x.parent.right == x:
                        x.parent.right = x.left
                        x.left.parent = x.parent

                ## Case 2.2: x has only right child
                elif x.left is None:
                    if x.parent.left == x:
                        x.parent.left = x.right
                        x.right.parent = x.parent
                    elif x.parent.right == x:
                        x.parent.right = x.right
                        x.right.parent = x.parent

                ## Case 3: x has two children
                else:
                    y = self.successor(target)

                    ## special case: the right child of x is directly the successor of x
                    ## which means the right child of x doesn't have left child
                    if x.right == y:
                        if x.parent.left == x:
                            y.parent = x.parent
                            x.parent.left = y
                        elif x.parent.right == x:
                            y.parent = x.parent
                            x.parent.right = y

                        y.left = x.left
                        x.left.parent = y
                    else:
                        if y.right:
                            y.right.parent = y.parent
                        y.parent.left = y.right

                        if x.parent.left == x:
                            x.parent.left = y
                        elif x.parent.right == x:
                            x.parent.right = y
                        y.parent = x.parent
                        y.left = x.left
                        x.left.parent = y
                        y.right = x.right
                        x.right.parent = y
        else:
            print(str(target) + " is not in the tree")
            return -1

    def inorderTraversal(self, root):
        record = []

        if root:
            record = self.inorderTraversal(root.left)
            record.append(root.value)
            record += self.inorderTraversal(root.right)
        return record

    def preorderTraversal(self, root):
        record = []

        if root:
            record = [root.value]
            record += self.preorderTraversal(root.left)
            record += self.preorderTraversal(root.right)
        return record


bst = Node(15)
bst.insert(4)
bst.insert(5)
bst.insert(20)
bst.insert(17)
bst.insert(25)
bst.insert(26)
bst.insert(21)
bst.insert(23)
bst.insert(18)
# print(bst.root.value)
# print(bst.inorderTraversal(bst.root))
# print(bst.findMin().value)
# print(bst.findMax().value)
# print(bst.search(5).value)
# print(bst.predecessor(15).value)
# print(bst.predecessor(17).value)
# print(bst.successor(20).value)
# print(bst.successor(5).value)
bst.delete(15)
bst.delete(17)
bst.delete(4)
print(bst.inorderTraversal(bst))
print(bst.preorderTraversal(bst))