from collections import deque
adj = {}

def add_path(x, y):
    if x not in adj:
        adj[x] = []
    if y not in adj:
        adj[y] = []
    adj[x].append(y)
    adj[y].append(x)

n, m = map(int, input().split())

for _ in range(m):
    x, y = map(int, input().split())
    add_path(x, y)
visited = [False] * (n + 1)
parent = [-1] * (n + 1)
def bfs(node):
    queue = deque([node])
    visited[node] = True
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
def path (s, t):
    global parent, visited
    bfs(s)
    if not visited[t]:
        print("No path found")
        return
    path_list = []
    while t != -1:
        path_list.append(t)
        t = parent[t]
    path_list.reverse()
    print(*path_list)

s, t = map(int, input().split())

path(s, t)

