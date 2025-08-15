class MinHeap:
    def __init__(self):
        self.heap = []
    def parent(self, index):
        return (index - 1) // 2
    def left(self, index):
        return 2 * index + 1
    def right(self, index):
        return 2 * index + 2
    def heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)
    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)
    def print(self):
        print(self.heap)
    def heapify_down(self, index):
        smallest = index
        left = self.left(index)
        right = self.right(index)
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)
    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
h = MinHeap()
h.insert(4)
h.insert(2)
h.insert(7)
h.insert(6)
print(h.extract_min())
h.print()