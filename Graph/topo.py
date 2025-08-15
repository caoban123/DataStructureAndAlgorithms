adj = {}
n, m = map(int, input().split())
lst = []
def add_edge(x, y):
    if x not in adj:
        adj[x] = []
    if y not in adj:
        adj[y] = []
    adj[x].append(y)

for i in range(m):
    u, v = map(int, input().split())
    if u not in lst:
        lst.append(u)
    if v not in lst:
        lst.append(v)
    add_edge(u, v)
visited = [False] * (n + 1)
topo = []

def dfs(a):
    visited[a] = True
    for i in adj[a]:
        if not visited[i]:
            dfs(i)
    topo.append(a)
lst.sort()
for i in lst:
    if not visited[i]:
        dfs(i)

print(*topo[::-1])
