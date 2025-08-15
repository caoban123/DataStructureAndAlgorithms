
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def insert(root, val):
    if root is None:
        return TreeNode(val)
    else:
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root
def print_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print_tree(root.right, level + 1, "R---")
        print("     " * level + prefix + str(root.val))
        print_tree(root.left, level + 1, "L---")
def is_empty(root):
    if root:
        return False
    return True
def find_value(root, value):
    if root is None:
        return False
    if root.val == value:
        return True
    elif value < root.val:
        return find_value(root.left, value)
    else:
        return find_value(root.right, value)
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
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        min_value = find_min(root.right)
        root.val = min_value.val
        root.right = delete(root.right, min_value.val)
    return root

        





node = [10,6,7,8,4,3,5]
root = None
# dem = 0
for i in node:
    root = insert(root, i)
    # if dem % 2 == 0:
    #     print(f"{dem / 2} : ")
    #     print_tree(root)
    # root = insert(root, i)
    # dem += 1
print_tree(root)
# delete(root,40)
# print("-------------------")
# print_tree(root)
# # print(is_empty(root))
# # print("Binary Search Tree:")
# # print_tree(root)
# # print(find_value(root, 10))
# # delete(root,2)
# # print_tree(root)

        

