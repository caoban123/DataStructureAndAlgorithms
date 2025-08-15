class Heap: 
    def __init__(self):
        self.heap = []
    def left(self, index):
        return index * 2 + 1
    def right(self, index):
        return index * 2 + 2
    def parent(self, index):
        return (index - 1) // 2
    def heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    def heapify_down(self, index):
        left = self.left(index)
        right = self.right(index)
        smallest = index
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if index != smallest:
            self.heap[smallest] , self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)
    def extract_min(self):
        if not self.heap:
            return
        min_value = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self.heapify_down(0)
        return min_value
    
if __name__ == "__main__":
    qheap = Heap()
    qheap.insert(5)
    qheap.insert(4)
    qheap.insert(3)
    print(qheap.extract_min())
    print(qheap.extract_min())
    print(qheap.extract_min())
