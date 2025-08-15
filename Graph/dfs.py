adj = {}

def add_edge(x, y):
    if x not in adj:
        adj[x] = []
    if y not in adj:
        adj[y] = []
    adj[x].append(y)
    adj[y].append(x)
n, m = map(int, input().split())
for i in range(m):
    u, v = map(int, input().split())
    add_edge(u, v)
visited = [False] * (n + 1)
parent = [-1] * (n + 1)
def dfs(node):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            parent[neighbor] = node
            dfs(neighbor)
def path(s, t):
    global visited, parent
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    dfs(s)
    if not visited[t]:
        print("No path found")
        return
    list_path = []
    while t != -1:
        list_path.append(t)
        t = parent[t]
    list_path.reverse()
    print("-->".join(map(str, list_path)))

s, t = map(int, input().split())

path(s, t)