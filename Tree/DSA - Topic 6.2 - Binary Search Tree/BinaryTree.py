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
def preOrder(root, lst):
    if root:
        lst.append(root.val)
        preOrder(root.left, lst)
        preOrder(root.right, lst)
        return lst
def inOrder(root, lst):
    if root:
        inOrder(root.left, lst)
        lst.append(root.val)
        inOrder(root.right, lst)
        return lst
def postOrder(root, lst):
    if root:
        postOrder(root.left, lst)
        postOrder(root.right, lst)
        lst.append(root.val)
        return lst
#(a) Write a function that counts the number of items in a binary tree.
def count(root):
    if root is None:
        return 0
    else:
        return 1 + count(root.left) + count(root.right)
#(b)Write a function that returns the sum of all the keys in a binary tree.
def sum_node(root):
    if root is None:
        return 0
    else:
        return root.val + sum_node(root.left) + sum_node(root.right)
#(c) Write a function that returns the maximum value of all the keys in a binary tree. 
# Assume all values are nonnegative; return -1 if the tree is empty.

def max_node(root):
    if root is None:
        return -1
    else:
        left_max = max_node(root.left)
        right_max = max_node(root.right)
        return max(root.val, left_max, right_max)
#(d) The height of a tree is the maximum number of nodes on a path from the root to a
# leaf node. Write a C function that returns the height of a binary tree.
def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1
#(e) The cost of a path in a tree is sum of the keys of the nodes participating in that path. 
# Write a C function that returns the cost of the most expensive path from the root to a leaf node.
def cost(root):
    if root is None:
        return 0
    else:
        left_cost = cost(root.left)
        right_cost = cost(root.right)
        return max(left_cost, right_cost) + root.val
node = [30, 40, 24, 58, 48, 26, 11, 13]
root = None
for i in node:
    root = insert(root, i)
# print("Binary Search Tree:")
# print_tree(root)
# preOrder_list = preOrder(root, [])
# inOrder_list = inOrder(root, [])
# postOrder_list = postOrder(root, [])
# print("\nTraversal Results:")
# print("PreOrder:", preOrder_list)
# print("InOrder:", inOrder_list)
# print("PostOrder:", postOrder_list)

# print("\nCount of nodes in the tree:", count(root))
# print("Sum of all keys in the tree:", sum_node(root))
# print("Maximum value in the tree:", max_node(root))
# print("Height of the tree:", height(root))
# print("Cost of the most expensive path from root to leaf:", cost(root))
print_tree(root)
# delete(root,40)
print("-------------------")
print_tree(root)



    