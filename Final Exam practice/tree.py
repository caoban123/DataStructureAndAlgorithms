class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
class avl:
    def new_node(self, value):
        return TreeNode(value)
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    def update_height(self, root):
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
    def right_rotate(self, root):
        new_root = root.left
        temp = new_root.right
        new_root.right = root
        root.left = temp

        self.update_height(root)
        self.update_height(new_root)
        
        return new_root
    def left_rotate(self, root):
        new_root = root.right
        temp = new_root.left
        new_root.left = root
        root.right = temp

        self.update_height(root)
        self.update_height(new_root)

        return new_root
    def adjust_tree(self, root):
        self.update_height(root)
        balanced = self.get_balance(root)
        if balanced > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        elif balanced < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root
    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        else:
            if value < root.value:
                root.left = self.insert(root.left, value)
            elif value > root.value:
                root.right = self.insert(root.right, value)
            else:
                return root
        root = self.adjust_tree(root)
        return root
    def find_max(self, root):
        if not root:
            return None
        while root.right:
            root = root.right
        return root
    def delete(self, root, value):
        if not root:
            return
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            max_value = self.find_max(root.left)
            root.value = max_value.value
            root.left = self.delete(root.left, max_value.value)
        return self.adjust_tree(root)
    def print_tree(self, root, level = 0, prefix=  "Root:"):
        if root is not None:
            self.print_tree(root.right, level + 1, "R---")
            print("     " * level + prefix + str(root.value))
            self.print_tree(root.left, level + 1, "L---")
    def is_full(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if root.left and not root.right:
            return False
        if root.right and not root.left:
            return False
        return self.is_full(root.left) and self.is_full(root.right)
    def is_complete(self, root):
        if not root:
            return True
        queue = [root]
        check_null = False
        while queue:
            cur = queue.pop(0)
            if not cur:
                    check_null = True
            else:
                if check_null:
                    return False
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)
        return True
    def get_depth(self, root):
        if not root:
            return 0
        return 1 + max(self.get_depth(root.left), self.get_depth(root.right))
    def is_perfect_util(self, root, depth, level = 1):
        if not root:
            return True
        if not root.left and not root.right:
            return level == depth
        if not root.right or not root.left:
            return False
        return self.is_perfect_util(root.left, depth, level + 1) and self.is_perfect_util(root.right, depth, level + 1)
    def is_perfect(self, root):
        depth = self.get_depth(root)
        return self.is_perfect_util(root, depth)
    def find_common_ancestor(self, root, x, y):
        if not root:
            return None
        if x < root.value and y < root.value:
            return self.find_common_ancestor(root.left, x, y)
        elif x > root.value and y > root.value:
            return self.find_common_ancestor(root.right, x, y)
        else:
            return root.value
# def build_bst_from_preorder(preorder):
#     index = [0]
#     def build(minv = float("-inf"), maxv = float("inf")):
#         if index[0] >= len(preorder):
#             return None
#         val = preorder[index[0]]
#         if not minv < val < maxv:
#             return None
#         node = TreeNode(val)

#         index[0] += 1
#         node.left = build(minv, val)
#         node.right = build(val, maxv)

#         return node
#     return build()        
# def build_bst_from_postpreorder(postorder):
#     index = [len(postorder) - 1]
#     def build(minv = float("-inf"), maxv = float("inf")):
#         if index[0] < 0:
#             return None
#         val = postorder[index[0]]
#         if not minv < val < maxv:
#             return None
#         node = TreeNode(val)
#         index[0] -= 1
#         node.right = build(val, maxv)
#         node.left = build(minv, val)
#         return node
#     return build()

# def build_bst_from_preorder(preorder):
#     index = [0]
#     def build(minv = float("-inf"), maxv = float("inf")):
#         if index[0] >= len(preorder):
#             return None
#         val = preorder[index[0]]
#         if not minv < val < maxv:
#             return None
#         node = TreeNode(val)
#         index[0] += 1
#         node.left = build(minv, val)
#         node.right = build(val, maxv)

#         return node
#     return build()
# def build_bst_from_inorder_preorder(inorder, preorder):
#     if not inorder or not preorder:
#         return None
#     rootv = preorder[0]
#     root = TreeNode(rootv)
#     idx = inorder.index(rootv)
#     root.left = build_bst_from_inorder_preorder(inorder[:idx], preorder[1 : idx + 1])
#     root.right = build_bst_from_inorder_preorder(inorder[idx + 1:], preorder[idx + 1:])
#     return root
# def buid_bst_from_inorder_postorder(inorder, postorder):
#     if not inorder or not postorder:
#         return None
#     rootv = postorder[-1]
#     root = TreeNode(rootv)
#     idx = inorder.index(rootv)

#     root.right = buid_bst_from_inorder_postorder(inorder[idx + 1:], postorder[idx : -1])
#     root.left = buid_bst_from_inorder_postorder(inorder[: idx], postorder[:idx])
# def build_bst_from_inorder_preorder(inorder, preorder):
#     if not inorder or not preorder:
#         return None
#     rootv = preorder[0]
#     root = TreeNode(rootv)
#     idx = inorder.index(rootv)
#     root.left = build_bst_from_inorder_preorder(inorder[:idx], preorder[1: idx + 1])
#     root.right = build_bst_from_inorder_preorder(inorder[idx + 1:], preorder[idx + 1:])
#     return root
# def build_bst_from_inorder_postorder(inorder, postorder):
#     if not inorder or not postorder:
#         return None
#     rootv = postorder[-1]
#     root = TreeNode(rootv)
#     idx = inorder.index(rootv)
#     root.right = build_bst_from_inorder_postorder(inorder[idx + 1:], postorder[idx : -1])
#     root.left = build_bst_from_inorder_postorder(inorder[:idx], postorder[:idx])
#     return root

def print_tree(root, level = 0, prefix=  "Root:"):
    if root is not None:
        print_tree(root.right, level + 1, "R---")
        print("     " * level + prefix + str(root.value))
        print_tree(root.left, level + 1, "L---")



nodes = [10,6,7,8,4,3,5]
inorder   = [2, 3, 4, 5, 7, 8, 9]
postorder = [2, 4, 3, 7, 9, 8, 5]
preorder = [5, 3, 2, 4, 8, 7, 9]
avl_tree = avl()
root = None
for node in nodes:
    root = avl_tree.insert(root, node)
avl_tree.insert(root, 11)


avl_tree.print_tree(root)
print(avl_tree.is_full(root))
print(avl_tree.is_complete(root))
print(avl_tree.is_perfect(root))
print(avl_tree.find_common_ancestor(root,3,5))

root1 = build_bst_from_preorder(preorder)
print_tree(root1)
root2 = build_bst_from_postpreorder(postorder)
print_tree(root2)
root3 = build_bst_from_inorder_preorder(inorder, preorder)
print_tree(root3)
root4 = build_bst_from_inorder_postorder(inorder, postorder)
print_tree(root4)
        
        
        





