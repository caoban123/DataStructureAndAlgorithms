class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
def new_node(data: int)-> Node:
    return Node(data)
def get_height(root):
    if not root:
        return 0
    return root.height
def balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)
def right_rotation(root):
    new_root = root.left
    temp = new_root.right
    new_root.right = root
    root.left = temp
    root.height = 1 + max(get_height(root.left) , get_height(root.right))
    new_root.height = 1 + max(get_height(new_root.left) , get_height(new_root.right))
    return new_root
def left_rotation(root):
    new_root = root.right
    temp = new_root.left
    new_root.left = root
    root.right = temp
    root.height = 1 + max(get_height(root.left) , get_height(root.right))
    new_root.height = 1 + max(get_height(new_root.left) , get_height(new_root.right))
    return new_root



def insert_node(root: Node, data: int)-> Node:
    if not root:
        return Node(data)
    if data < root.key:
        root.left = insert_node(root.left, data)
    elif data > root.key:
        root.right = insert_node(root.right, data)
    else:
        return root
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balanced = balance(root)
    if balanced > 1 and data < root.left.key:
        return right_rotation(root)
    elif balanced > 1 and data > root.left.key:
        root.left = left_rotation(root.left)
        return right_rotation(root)
    elif balanced < -1 and data > root.right.key:
        return left_rotation(root)
    elif balanced < -1 and data < root.right.key:
        root.right = right_rotation(root.right)
        return left_rotation(root)
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
    if not root:
        return 0
    if data < root.key:
        root.left = delete_node(root.left, data)
    elif data > root.key:
        root.right = delete_node(root.right, data)
    else:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        max_value = get_max_value_node(root.left)
        root.key = max_value.key
        root.left = delete_node(root.left, max_value.key)
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balanced = balance(root)
    if balanced > 1 and balance(root.left) >= 0:
        return right_rotation(root)
    elif balanced > 1 and balance(root.left) < 0:
        root.left = left_rotation(root.left)
        return right_rotation(root)
    elif balanced < -1 and balance(root.right) <= 0:
        return left_rotation(root)
    elif balanced < -1 and balanced(root.right) > 0:
        root.right = right_rotation(root.right)
        return left_rotation(root)
    return root
def print_tree(root: Node, level=0, prefix="Root:")-> None:
    if root is not None:
        print_tree(root.right, level + 1, "R---")
        print("     " * level + prefix + str(root.key))
        print_tree(root.left, level + 1, "L---")
lst = [i for i in range(30)]

root = None
for i in lst:
    root = insert_node(root, i) 
print_tree(root)

    
