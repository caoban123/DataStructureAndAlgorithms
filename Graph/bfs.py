from collections import deque

# adj = {}
# def add_edge(x, y):
#     if x not in adj:
#         adj[x] = []
#     if y not in adj:
#         adj[y] = []
#     adj[x].append(y)
#     adj[y].append(x)
# n, m = map(int, input().split())
# for i in range(m):
#     u, v = map(int, input().split())
#     add_edge(u, v)

def bfs(adj, start):
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        print(node, end = " ")
        if node not in visited:
            visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
graph = {
    "A" : ["B","D", "C"],
    "B" : ["A", "E"],
    "C" : ["A", "F"],
    "D" : ["A","F"],
    "E" : ["B","G"],
    "F" : ["C","D", "H"],
    "G" : ["E","H", 'I'],
    "H" : ["F","G","J"],
    "I" : ["G", "J"],
    "J" : ["H","I"]
}
bfs(graph, "A")