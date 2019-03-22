class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new_data):
        new_node = Node(new_data)

        if self.value:
            if new_data < self.value:
                if self.left is None:
                    self.left = new_node
                else:
                    self.left.insert(new_data)
            elif new_data > self.value:
                if self.right is None:
                    self.right = new_node
                else:
                    self.right.insert(new_data)
        else:
            self.value = new_data

    def levelorderTraversal(self, root):
        record = []
        queue = []

        queue.append(root)

        while queue:
            pop_node = queue.pop(0)
            record.append(pop_node.value)
            if pop_node.left is not None:
                queue.append(pop_node.left)
            if pop_node.right is not None:
                queue.append(pop_node.right)
        return record

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

    def postorderTraversal(self, root):
        record = []

        if root:
            record = self.postorderTraversal(root.left)
            record += self.postorderTraversal(root.right)
            record.append(root.value)
        return record

root = Node(6)
root.insert(8)
root.insert(4)
root.insert(5)
root.insert(9)
root.insert(7)
root.insert(3)
print("Level Order Traversal:", root.levelorderTraversal(root))
print("Inorder Traversal:", root.inorderTraversal(root))
print("Preorder Traversal:", root.preorderTraversal(root))
print("Postorder Traversal:", root.postorderTraversal(root))
