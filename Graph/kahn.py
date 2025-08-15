from collections import deque
n, m = map(int, input().split())
adj = {}
dem = [0] * (n + 1)
lst = []
def add_edge(x, y):
    if x not in adj:
        adj[x] = []
    if y not in adj:
        adj[y] = []
    adj[x].append(y)
    dem[y] += 1


for i in range(m):
    u, v = map(int, input().split())
    if u not in lst:
        lst.append(u)
    if v not in lst:
        lst.append(v)
    add_edge(u, v)

topo = []
def bfs():
    queue = deque([])
    for i in lst:
        if dem[i] == 0:
            queue.append(i)
    while queue:
        u = queue.popleft()
        topo.append(u)
        for v in adj[u]:
            dem[v] -= 1
            if  dem[v] == 0:
                queue.append(v)
bfs()
print(*topo)



