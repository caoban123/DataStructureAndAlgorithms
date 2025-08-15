class MaxHeap:
    def __init__(self):
        self.heap = []
    def left(self, i):
        return 2 * i + 1
    def right(self, i):
        return 2 * i + 2
    def parent(self, i):
        return (i - 1) // 2
    def heapify_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap) - 1)
    def print(self):
        print(self.heap)
    def heapify_down(self, i):
        largest = i
        left = self.left(i)
        right = self.right(i)
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.heapify_down(largest)
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return max_value
    def delete(self, i):
        if i < 0 or i >= len(self.heap):
            return
        self.heap[i] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(i)
h = MaxHeap()
h.insert(4)
h.insert(2)
h.insert(7)
h.print()
h.extract_max()
h.print()
h.delete(0)
h.print()


    
