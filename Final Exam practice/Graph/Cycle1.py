
# def dfs(u, visited):
#     visited[u] = 1
#     for v in adj[u]:
#         if not visited[v]:
#             if dfs(v, visited):
#                 return True
#         elif visited[v] == 1:
#             return True
#     visited[u] = 2
#     return False
def bfs(n, adj, degree):
    queue = []
    for key in adj:
        if degree[key] == 0:
            queue.append(key)
    cnt = 0
    while queue:
        u = queue.pop(0)
        cnt += 1
        for v in adj[u]:
            degree[v] -= 1
            if degree[v] == 0:
                queue.append(v) 
    return not cnt == n
if __name__ == "__main__":
    n, m = map(int, input().split())
    adj = {}
    visited = [0] * (n + 1)
    degree = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        degree[v] += 1
    # print(dfs(0, visited))
    print(degree)
    print(bfs(n, adj, degree))