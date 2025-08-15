class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
def new_node(data: int)-> Node:
    return Node(data)
def get_height(root: Node)-> int:
    if not root:
        return 0
    return root.height
def get_balance(root: Node)-> int:
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)
def right_rotate(root: Node)-> Node:
    new_root = root.left
    temp = new_root.right
    new_root.right = root
    root.left = temp
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    return new_root
def left_rotate(root: Node)-> Node:
    new_root = root.right
    temp = new_root.left
    new_root.left = root
    root.right = temp
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    return new_root
def insert_node(root: Node, data: int)-> Node:
    if not root:
        return new_node(data)
    if data < root.key:
        root.left = insert_node(root.left, data)
    elif data > root.key:
        root.right = insert_node(root.right, data)
    else:
        return root
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    if balance > 1 and data < root.left.key:
        return right_rotate(root)
    if balance < -1 and data > root.right.key:
        return left_rotate(root)
    if balance > 1 and data > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and data < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root
def search_node(root: Node, data: int)-> Node:
    if root is None or root.key == data:
        return root
    elif data < root.key:
        return search_node(root.left, data)
    else:
        return search_node(root.right, data)
def get_max_value_node(root: Node)-> Node:
    if root is None:
        return None
    while root.right is not None:
        root = root.right
    return root
def delete_node(root: Node, data: int)-> Node:
    if root is None:
        return None
    if data < root.key:
        root.left = delete_node(root.left, data)
    elif data > root.key:
        root.right = delete_node(root.right, data)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = get_max_value_node(root.left)
        root.key = temp.key
        root.left = delete_node(root.left, temp.key)
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root
def nlr(root: Node)-> None:
    if root is None:
        return
    print(root.key, end = " ")
    nlr(root.left)
    nlr(root.right)
def lnr(root: Node)-> None:
    if root is None:
        return
    lnr(root.left)
    print(root.key, end = " ")
    lnr(root.right)
def lrn(root: Node)-> None:
    if root is None:
        return
    lrn(root.left)
    lrn(root.right)
    print(root.key, end = " ")
def level_order(root: Node)-> None:
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.key, end = " ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
def print_tree(root: Node, level=0, prefix="Root:")-> None:
    if root is not None:
        print_tree(root.right, level + 1, "R---")
        print("     " * level + prefix + str(root.key))
        print_tree(root.left, level + 1, "L---")

lst = [8, 6, 5, 7, 10, 9]

root = None
for i in lst:
    root = insert_node(root, i) 
print_tree(root)
print("Preorder traversal:")
nlr(root)
print("\nInorder traversal:")
lnr(root)
print("\nPostorder traversal:")
lrn(root)
print()
delete_node(root, 8)
print_tree(root)
print("\nLevel order traversal:")
level_order(root) 



    




