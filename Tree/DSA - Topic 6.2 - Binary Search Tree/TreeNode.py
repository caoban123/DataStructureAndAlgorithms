class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def insertrecur(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insertrecur(root.left, val)
    else:
        root.right = insertrecur(root.right, val)
    return root
def insertloop(root, val):
    if root is None:
        return TreeNode(val)
    temp = root
    while True:
        if val < temp.val:
            if temp.left is None:
                temp.left = TreeNode(val)
                break
            else:
                temp = temp.left
        else:
            if temp.right is None:
                temp.right = TreeNode(val)
                break
            else:
                temp = temp.right
    return root

def print_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print_tree(root.right, level + 1, "R---")
        print("     " * level + prefix + str(root.val))
        print_tree(root.left, level + 1, "L---")
def find_min(root):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root
def delete(root, val):
    if root is None:
        return root
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        min_node = find_min(root.right)
        root.val = min_node.val
        root.right = delete(root.right, min_node.val)
    return root
def searchBST(root, val):
    if root is None:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    elif val > root.val:
        return searchBST(root.right, val)
    else:
        return root
def preOder(root):
    if root is not None:
        print(root.val, end=" ")
        preOder(root.left)
        preOder(root.right)
def InOder(root):
    if root is not None:
        InOder(root.left)
        print(root.val, end=" ")
        InOder(root.right)
node = [15, 10, 20, 8, 12, 17, 25]
root = None
for i in node:
    root = insertrecur(root, i)
print_tree(root)
delete(root,15)
print("-------------------")
print_tree(root)