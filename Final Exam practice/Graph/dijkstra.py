class MinHeap:
    def __init__(self):
        self.heap = []
    def left(self, index):
        return 2 * index + 1
    def right (self, index):
        return 2 * index + 2
    def parent(self, index):
        return (index - 1) // 2
    def heapify_up(self, index):
        while index >= 0 and self.heap[self.parent(index)][0] > self.heap[index][0]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)
    def heappush(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    def heapify_down(self, index):
        left = self.left(index)
        right = self.right(index)
        smallest = index
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)
    def heappop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return min_value

def dijkstra(adj, n, start):
    dist = [float("inf")] * n
    dist[start] = 0
    parent = [-1] * n
    heap = MinHeap()
    heap.heappush((0, start))
    while heap.heap:
        current_dist, u = heap.heappop()
        if current_dist > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > w + current_dist:
                dist[v] = w + current_dist
                parent[v] = u
                heap.heappush((dist[v], v))
    for i in range(n):
        if i != start:
            end = i
            path = []
            while end != start:
                path.append(end)
                end = parent[end]
            path.reverse()
            print(str(start), end = "--> ")
            print("--> ".join(map(str, path)), dist[i]) 

        



if __name__ == "__main__":
    n, m = map(int, input().split())
    adj = {}
    for _ in range(m):
        u, v, w = map(int, input().split())
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append((v, w))
    dijkstra(adj, n, 0)