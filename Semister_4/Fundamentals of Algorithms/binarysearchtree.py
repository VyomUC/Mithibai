class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class BST:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value, root=None):
        if root is None:
            root = self.root
        if root.value > value:
            if root.left is None:
                root.left = Node(value, parent=root)
            else:
                self.insert(value, root.left)
        else:
            if root.right is None:
                root.right = Node(value, parent=root)
            else:
                self.insert(value, root.right)

    def delete(self, root, value):
        if root is None:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.findMinValueNode(root.right)

            # Copy the inorder successor's content to this node
            root.value = temp.value

            # Delete the inorder successor
            root.right = self.delete(root.right, temp.value)
        return root

    def findMinValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=' ')
            self.inorder(root.right)

b = BST(5)
b.insert(8)
b.insert(10)
b.insert(3)
b.insert(1)
b.insert(6)
b.insert(4)
b.insert(7)
b.insert(9)
b.insert(12)

print("Before deletion")
b.inorder(b.root)
b.delete(b.root, 9)
print("\nAfter deletion")
b.inorder(b.root)