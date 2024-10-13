# Tree Traversal

from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None


def inorderTraversal(root: Node) -> None:
    if root is None:
        return 
    
    inorderTraversal(root.left)
    print(root.data, end = " ")
    inorderTraversal(root.right)

def preorderTraversal(root: Node) -> None:
    if root is None:
        return
    
    print(root.data, end=" ")
    preorderTraversal(root.left)
    preorderTraversal(root.right)

def postorderTraversal(root: Node) -> None:
    if root is None:
        return
    
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.data, end=" ")

def levelorderTraversal(root: Node) -> None:
    if not root:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder: ")
    inorderTraversal(root)
    print()
    print("Preorder: ")
    preorderTraversal(root)
    print()
    print("Postorder: ")
    postorderTraversal(root)
    print()
    print("Levelorder: ")
    levelorderTraversal(root)
    
