class Node:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None
        self.height = 1
class AVL:
    def new_node(self, data):
        return Node(data)
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    def right_rotate(self, root):
        new_root = root.left
        temp = new_root.right
        new_root.right = root
        root.left = temp
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left),self.get_height(new_root.right))
        return new_root
    def left_rotate(self,root):
        new_root = root.right
        temp = new_root.left
        new_root.left = root
        root.right = temp
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left),self.get_height(new_root.right))
        return new_root
    def insert(self, root, data):
        if not root:
            return Node(data)
        else:
            if data < root.key:
                root.left = self.insert(root.left, data)
            elif data > root.key:
                root.right = self.insert(root.right, data)
            root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
            balanced = self.get_balance(root)
            if balanced > 1 and data < root.left.key:
                return self.right_rotate(root)
            if balanced > 1 and data > root.left.key:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
            if balanced < -1 and data > root.right.key:
                return self.left_rotate(root)
            if balanced < -1 and data < root.right.key:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
            return root
    def search(self, root, data):
        if not root:
            return None
        else:
            if data == root.key:
                return root
            else:
                if data < root.key:
                    return self.search(root.left)
                else:
                    return self.search(root.right)
    def get_max_value(self, root):
        if not root:
            return None
        else:
            while root.right:
                root = root.right
            return root
    def delete(self, root, data):
        if not root:
            return None
        else:
            if data < root.key:
                root.left = self.delete(root.left, data)
            elif data > root.key:
                root.right = self.delete(root.right, data)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                max_value = self.get_max_value(root.left)
                root.key = max_value.key
                root.left = self.delete(root.left, max_value.key)
            root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
            balanced = self.get_balance(root)
            if balanced > 1 and self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            if balanced > 1 and self.get_balance(root.left) < 0:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
            if balanced < -1 and self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            if balanced < - 1 and self.get_balance(root.right) > 0:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
            return root
    def print_tree(self, root, level = 0, prefix = "root: "):
        if not root:
            return 
        self.print_tree(root.right, level + 1, "R---")
        print("     " * level + prefix + str(root.key))
        self.print_tree(root.left, level + 1, "L---")
    def is_full(self, root):
        if not root:
            return True
        else:
            if root.left is None and root.right is None:
                return True
            elif root.left and root.right:
                return self.is_full(root.left) and self.is_full(root.right)
            return False
    def is_complete(self, root):
        if root is None:
            return True
        check_null = 0
        queue = [root]
        while queue:
            current_node = queue.pop(0)
            if current_node == None:
                    check_null = 1
            else:
                if check_null:
                    return False
                else:
                        queue.append(current_node.left)
                        queue.append(current_node.right)
        return True
    def get_depth(self, root):
        if root is None:
            return 0
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        return max(left_depth, right_depth) + 1
    def is_perfect_util(self, root, depth, level = 1):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return depth == level
        if root.left is None or root.right is None:
            return False
        return self.is_perfect_util(root.left, depth, level + 1) and self.is_perfect_util(root.right, depth, level + 1)
    def is_perfect(self,root):
        depth = self.get_depth(root)
        return self.is_perfect_util(root, depth)
    def print_special_nodes(self, root):
        if root is None:
            return
        else:
            if  root.left and root.right and root.right.key % root.left.key == 0:
                print(root.key)
            self.print_special_nodes(root.left)
            self.print_special_nodes(root.right)

    def find_common_ancestor(self, root, x, y):
        if not root:
            return None
        else:
            if x < root.key and y < root.key:
                return self.find_common_ancestor(root.left, x, y)
            if x > root.key and y > root.key:
                return self.find_common_ancestor(root.right, x, y)
            return root.key


    
            
tree1 = AVL()
root = tree1.new_node(8)
nodes = [6, 5, 7, 10, 9, 5.5, 90]
for node in nodes:
    root = tree1.insert(root, node)
tree1.delete(root, 8)
# tree1.delete(root,5.5)
tree1.print_tree(root)
print(tree1.is_full(root))
print(tree1.is_complete(root))
print(tree1.is_perfect(root))
tree1.print_special_nodes(root)
print(tree1.find_common_ancestor(root, 6, 90))




                
            


        
    

