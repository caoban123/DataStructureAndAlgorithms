class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def new_node(data: int) -> Node:
    return Node(data)
def insert(root: Node, data: int) -> Node:
    if root is None:
        return Node(data)
    else:
        if data < root.key:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print_tree(root.right, level + 1, "R--- ")
        print(" " * (level * 4) + prefix + str(root.key))
        print_tree(root.left, level + 1, "L--- ")
def search(root: Node, data: int) -> Node:
    if root is None:
        return None
    if root.key == data:
        return root
    else:
        if data < root.key:
            return search(root.left, data)
        else:
            return search(root.right, data)
def find_max(root):
    if root is None:
        return None
    else:
        while root.right is not None:
            root = root.right
    return root
def delete(root: Node, data: int) -> Node:
    if root is None:
        return None
    if data < root.key:
        root.left = delete(root.left, data)
    elif data > root.key:
        root.right = delete(root.right, data)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        max_value = find_max(root.left)
        root.key = max_value.key
        root.left = delete(root.left, max_value.key)
    return root
def preorder(root: Node) -> None:
    if root is None:
        return None
    else:
        print(root.key, end = " ")
        preorder(root.left)
        preorder(root.right)
def inorder(root: Node) -> None:
    if root is None:
        return None
    else:
        preorder(root.left)
        print(root.key, end = " ")
        preorder(root.right)
def postorder(root: Node) -> None:
    if root is None:
        return None
    else:
        preorder(root.left)
        preorder(root.right)
        print(root.key, end = " ")
def level_order(root: Node) -> None:
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0) 
        print(node.key, end=' ') 
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


    

root = new_node(3)
insert(root, 2)
insert(root, 5)
insert(root, 4)
insert(root, 6)
print_tree(root)
delete(root, 5)
print("------------------")
print_tree(root)
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
level_order(root)

