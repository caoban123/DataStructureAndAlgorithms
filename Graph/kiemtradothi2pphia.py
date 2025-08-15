from collections import deque

n, m = map(int, input().split())
adj = {}
for i in range(1, n + 1):
    adj[i] = []
def add_edge(a, b):
    adj[a].append(b)
    adj[b].append(a)

for i in range(m):
    u, v = map(int, input().split())
    add_edge(u, v)
color = [-1] * 1000
def bfs(u):
    queue = deque([u])
    color[u] = "RED"
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if color[neighbor] == -1:
                color[neighbor] = "BLUE" if color[node] == "RED" else "RED"
                queue.append(neighbor)
            else:
                if color[neighbor] == color[node]:
                    return False
    return True

check = True
for i in range(1, n + 1):
    if color[i] == -1:
        if not bfs(i):
            check = False
            break

if check:
    print("YES")
else:
    print("NO")


