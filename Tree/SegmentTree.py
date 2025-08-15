class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)
    def build(self, data, node, left, right):
        if left == right:
            self.tree[node] = data[left]
        else:
            mid = (left + right) // 2
            self.build(data, 2 * node + 1, left, mid)
            self.build(data, 2 * node + 2, mid + 1, right)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    def update(self, node, val, pos, left, right):
        if left == right:
            self.tree[node] = val
        else:
            mid = (left + right) // 2
            if pos <= mid:
                self.update(2 * node + 1, val, pos, left, mid)
            else:
                self.update(2 * node + 2, val, pos, mid + 1, right)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    def query(self, node, tl, tr, l, r):
        if l > r: return 0
        if tr == r and tl == l:
            return self.tree[node]
        else:
            tm = (tl + tr) // 2
            s1 = self.query(2 * node + 1, tl, tm, l, min(tm, r))
            s2 = self.query(2 * node + 2, tm + 1, tr, max(tm + 1, l), r)
            return s1 + s2
        
data = [1, 2, 3, 4, 5]

segment_tree = SegmentTree(data)
print(segment_tree.tree)  # Print the segment tree
segment_tree.update(0, 10, 0, 0, segment_tree.n - 1)  # Update the first element to 10
print(data)  
print(segment_tree.tree)  # Print the updated segment tree
print(segment_tree.query(0, 0, segment_tree.n - 1, 0, 2))  # Query the sum from index 0 to 2

        




