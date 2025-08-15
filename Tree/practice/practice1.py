class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def print_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print_tree(root.right, level + 1, "R---")
        print("     " * level + prefix + str(root.data))
        print_tree(root.left, level + 1, "L---")
def create_tree(data):
    return Node(data)
def insert_node(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert_node(root.left, data)
        elif data > root.data:
            root.right = insert_node(root.right, data)
        return root
def search_node(root, data):
    if root is None:
        return "NO"
    if data == root.data:
        return "YES"
    if data < root.data:
        return search_node(root.left, data)
    elif data > root.data:
        return search_node(root.right, data)
def find_max(root):
    if root is None:
        return None
    cur = root 
    while cur.right is not None:
        cur = cur.right
    return cur
def delete_node(root, data):
    if root is None:
        return None
    if data < root.data:
        root.left = delete_node(root.left, data)
    elif data > root.data:
        root.right = delete_node(root.right, data)
    else:
        if root.right is None:
            return root.left
        elif root.left is None:
            return root.right
        max_value = find_max(root.left)
        root.data = max_value.data
        root.left = delete_node(root.left, max_value.data)
    return root
def preorder(root: Node) -> None:
    if root is None:
        return None
    else:
        print(root.data, end = " ")
        preorder(root.left)
        preorder(root.right)
def preorder1(root):
    if root is None:
        return None
    else:
        stack = [root]
        while stack:
            x = stack.pop()
            print(x.data, end = " ")
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)
            
            
def inorder(root: Node) -> None:
    if root is None:
        return None
    else:
        preorder(root.left)
        print(root.data, end = " ")
        preorder(root.right)
# def inorder1(root):
#     if root is None:
#         return None
#     else:
#         stack = [root.left]
#         while stack:
#             x = stack.pop()
#             print(x.data, end = " ")
#             if x.right:
#                 stack.append(x.right)
#             if x.left:
#                 stack.append(x.left)
def postorder(root: Node) -> None:
    if root is None:
        return None
    else:
        preorder(root.left)
        preorder(root.right)
        print(root.data, end = " ")
def leveloder(root):
    if not root:
        return
    else:
        queue = [root]
        while queue:
            x = queue.pop()
            print(x.data, end = " ")
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)
def height(root: Node)-> int:
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))
def sum_nodes(root: Node)-> int:
    if root is None:
        return 0
    else:
        return root.data + sum_nodes(root.left) + sum_nodes(root.right)
def count_nodes(root: Node)-> int:
    if root is None:
        return 0
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)
def count_less(root: Node, x: int)-> int:
    if root is None:
        return 0
    else:
        if root.data < x:
            return 1 + count_less(root.left, x) + count_less(root.right, x)
        else:
            return count_less(root.left, x) + count_less(root.right, x)
node = [40, 24, 58, 48, 26, 11, 13]
root = create_tree(30)
for data in node:
    insert_node(root, data)
print_tree(root)
print("--------------------")
delete_node(root, 24)
delete_node(root, 48)
print_tree(root)
leveloder(root)
print(search_node(root, 14))
print(height(root))
print(sum_nodes(root))
print(count_nodes(root))
print(count_less(root,27))
print()

preorder(root)

            


