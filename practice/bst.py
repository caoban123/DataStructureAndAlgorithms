class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
# def print_tree(root, level=0, prefix="Root:"):
    # if root is not None:
    #     print_tree(root.right, level + 1, "R---")
    #     print("     " * level + prefix + str(root.val))
    #     print_tree(root.left, level + 1, "L---")
def new_node(data):
    return Node(data)
def insert(root, data):
    if not root:
        return new_node(data)
    else:
        if data < root.val:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
        return root
def search(root, data):
    if not root:
        return None
    if root.val == data:
        return root
    if data < root.val:
        return search(root.left, data)
    else:
        return search(root.right, data)
def find_max(root):
    if root is None:
        return
    while root.right:
        root = root.right
    return root
def delete(root, data):
    if not root:
        return root
    if data < root.val:
        root.left = delete(root.left, data)
    elif data > root.val:
        root.right = delete(root.right, data)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        max_value = find_max(root.left)
        root.val = max_value.val
        root.left = delete(root.left, max_value.val)
    return root
def print_tree(root, level = 0, prefix = "Root: "):
    if root:
        print_tree(root.right, level + 1, "R--")
        print("      " * level + prefix + str(root.val))
        print_tree(root.left, level + 1, "L--")
def preoder(root):
    if root:
        print(root.val,end = " ")
        preoder(root.left)
        preoder(root.right)
def inoder(root):
    if root:
        inoder(root.left)
        print(root.val,end = " ")
        inoder(root.right)
def postoder(root):
    if root:
        postoder(root.left)
        postoder(root.right)
        print(root.val,end = " ")
def leveloder(root):
    if root:
        queue = [root]
        while queue:
            x = queue.pop(0)
            print(x.val, end = " ")
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)
def height(root):
    if not root:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))
def count(root):
    if not root:
        return 0
    return 1 + count(root.left) + count(root.right)
def sum_node(root):
    if not root:
        return 0
    return root.val + sum_node(root.left) + sum_node(root.right)
def count_leaf(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaf(root.left) + count_leaf(root.right)
def count_less(root, x):
    if not root:
        return 0
    if root.val < x:
        return 1 + count_less(root.left, x) + count_less(root.right, x)
    else:
        return count_less(root.left, x) + count_less(root.right, x)
def count_greater(root, x):
    if not root:
        return 0
    if root.val > x:
        return 1 + count_greater(root.left, x) + count_greater(root.right, x)
    else:
        return count_greater(root.left, x) + count_greater(root.right, x)
root = new_node(30)
nodes = [40, 24, 58, 48, 26, 11, 13]
for node in nodes:
    insert(root,node)
print_tree(root)
delete(root, 24)
print("--------------------")
print_tree(root)
preoder(root)
print()
inoder(root)
print()
postoder(root)
print()
leveloder(root)
print()
print(height(root))
print(count(root))
print(sum_node(root))
print(count_leaf(root))
print(count_less(root, 50))
print(count_greater(root, 100))