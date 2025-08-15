class MinHeap:
    def __init__(self):
        self.heap = []
    def left(self, index):
        return 2 * index + 1
    def right(self, index):
        return 2 * index + 2
    def parent(self, index):
        return (index - 1) // 2
    def heapify_up(self, index):
        while index > 0 and self.heap[index][0] < self.heap[self.parent(index)][0]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)
    def insert(self, current_dist, v):
        self.heap.append((current_dist, v))
        self.heapify_up(len(self.heap) - 1)
    def heapify_down(self, index):
        smallest = index
        left = self.left(index)
        right = self.right(index)
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)
    def heappop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        temp = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        return temp
# def dijkstra(n, graph, start):
#     dist = [float("inf")] * n
#     dist[start] = 0
#     heapq = MinHeap()
#     heapq.insert(0, start)
#     parent = [-1] * n
#     while heapq:
#         popped = heapq.heappop()
#         if popped is None:
#             break
#         current_dist, u = popped
#         if current_dist > dist[u]:
#             continue
#         for v in range(n):
#             if graph[u][v] != 0 and dist[v] > current_dist + graph[u][v]:
#                 dist[v] = current_dist + graph[u][v]
#                 heapq.insert(dist[v], v)
#                 parent[v] = u
#     for v in range(n):
#         if v == start:
#             continue
#         path = []
#         x = v
#         while x != -1:
#             path.append(x)
#             x = parent[x]
#         path.reverse()
#         print(f" The shortest path from {start} to {v}  {dist[v]}", "->".join(map(str, path))) 

    
def dijkstra(n, graph, start):
    dist = [float("inf")] * n
    dist[start] = 0
    heapq = MinHeap()
    heapq.insert(0, start)
    parent = [-1] * n
    while heapq:
        popped = heapq.heappop()
        if popped is None:
            break
        current_dist, u = popped
        if current_dist > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > current_dist + w:
                dist[v] = current_dist + w
                heapq.insert(dist[v], v)
                parent[v] = u
    for v in range(n):
        if v == start:
            continue
        path = []
        x = v
        while x != -1:
            path.append(x)
            x = parent[x]
        path.reverse()
        print(f" The shortest path from {start} to {v}  {dist[v]}", "->".join(map(str, path))) 

# if __name__ == "__main__":
#     start = int(input())
#     n = int(input())
#     graph = []
#     for i in range(n):
#         row = list(map(int, input().split()))
#         graph.append(row)
#     dijkstra(n, graph, start)


# 5
# 0 0 8 3 0
# 0 0 6 0 0
# 8 6 0 4 0
# 3 0 4 0 5
# 0 0 0 5 0

if __name__ == "__main__":
    n, m, start = map(int, input().split())
    edges = []
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    dic = {i : [] for i in range(n)}
    for edge in edges:
        dic[edge[0]].append((edge[1], edge[2]))
        dic[edge[1]].append((edge[0],edge[2]))
    dijkstra(n ,dic , start)


# 5 5
# 0 2 8
# 0 3 3
# 1 2 6
# 2 3 4
# 3 4 5