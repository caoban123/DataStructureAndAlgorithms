class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def get_height(root):
    return root.height if root else 0
def get_balance(root):
    return get_height(root.left) - get_height(root.right) if root else 0
def update_height(root):
    root.height = 1 + max(get_height(root.left), get_height(root.right))
def right_rotation(root):
    new_root = root.left
    temp = new_root.right
    new_root.right = root
    root.left = temp

    update_height(root)
    update_height(new_root)
    return new_root
def left_rotation(root):
    new_root = root.right
    temp = new_root.left
    new_root.left = root
    root.right = temp

    update_height(root)
    update_height(new_root)
    return new_root
def adjust_tree(root):
    update_height(root)
    balanced = get_balance(root)
    if balanced > 1:
        if get_balance(root.left) >= 0:
            return right_rotation(root)
        else:
            root.left = left_rotation(root.left)
            return right_rotation(root)
    elif balanced < -1:
        if get_balance(root.right) <= 0:
            return left_rotation(root)
        else:
            root.right = right_rotation(root.right)
            return left_rotation(root)
    return root
def insert(root, value):
    if not root:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        elif value > root.value:
            root.right = insert(root.right, value)
        else:
            return root
    return adjust_tree(root)
def find_max(root):
    if not root:
        return root
    cur = root
    while cur.right:
        cur = cur.right
    return cur
def delete(root, value):
    if not root:
        return root
    else:
        if value < root.value:
            root.left = delete(root.left, value)
        elif value > root.value:
            root.right = delete(root.right, value)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            maxv = find_max(root.left)
            root.value = maxv.value
            root.left = delete(root.left, maxv.value)

        return adjust_tree(root)
def print_tree(root, level = 0, prefix=  "Root:"):
    if root is not None:
        print_tree(root.right, level + 1, "R---")
        print("     " * level + prefix + str(root.value))
        print_tree(root.left, level + 1, "L---")
def summ(root, a, b):
    if not root:
        return 0
    if a <= root.value <= b:
        return root.value + summ(root.left, a, b) + summ(root.right, a, b)
    else:
        return summ(root.left, a, b) + summ(root.right, a, b)
    
def postorderiterative(root):
    lst = []
    stack = [root]
    while stack:
        node = stack.pop()
        lst.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return lst[::-1]
nodes = [4, 6, 1, 7, 8, 9, 2, 3, 0, 5]
root = None
for node in nodes:
    root = insert(root, node)

print_tree(root)
print("-------------------")
delete(root,2)
print_tree(root)

