from collections import deque
#vô hướng

# n, m = map(int, input().split())
# adj = {}
# parent = [0] * 1000
# def add_edge(x, y):
#     if x not in adj:
#         adj[x] = []
#     if y not in adj:
#         adj[y] = []
#     adj[x].append(y)
#     adj[y].append(x)

# for i in range(m):
#     u, v = map(int, input().split())
#     add_edge(u, v)

# visited = [False] * (100)
# def bfs(i):
#     queue = deque([i])
#     while queue:
#         u = queue.popleft()
#         visited[u] = True
#         for v in adj[u]:
#             if not visited[v]:
#                 visited[v] = True
#                 parent[v] = u
#                 queue.append(v)
#             elif parent[u] != v:

#                 return True
#     return False
# def dfs(i, par):
#     visited[i] = True
#     for child in adj[i]:
#         if not visited[child]:
#             if dfs(child, i):
#                 return True
#         elif par != child:
#             return True
#     return False

# if dfs(1,0):
#     print('YES')
# else:
#     print('NO')

#vo huong
n, m = map(int, input().split())
adj = {}
for i in range(1, n + 1):
    adj[i] = []
dem = [0] * 1000
def add_edge(x, y):
    adj[x].append(y)
    dem[y] += 1

for i in range(m):
    u, v = map(int, input().split())
    add_edge(u, v)

color = [0] * 1000

def dfs(i):
    color[i] = 1
    for child in adj[i]:
        if color[child] == 0:
            if dfs(child):
                return True
        elif color[i] == 1:
            return True
    color[i] = 2
def bfs():
    queue = deque([])
    for i in range(1, n + 1):
        if dem[i] == 0:
            queue.append(i)
    cnt = 0
    while queue:
        u = queue.popleft()
        cnt += 1
        for v in adj[u]:
            dem[v] -= 1
            if dem[v] == 0:
                queue.append(v)
    print(cnt)
    return cnt == n
# for i in range(1, n + 1):
#     if color[i] == 0:
#         if dfs(i):
#             print("YES")


if bfs():
    print("YES")
else:
    print("NO")

