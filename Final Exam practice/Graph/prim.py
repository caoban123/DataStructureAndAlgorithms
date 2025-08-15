def prim(adj, n, start):
    dist = [float("inf")] * n
    dist[start] = 0
    visited = [0] * n
    parent = [-1] * n
    d = 0
    for _ in range(n):
        min_cost = float("inf")
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_cost:
                min_cost = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = 1
        d += dist[u]
        for v, w in adj[u]:
            if not visited[v] and dist[v] > w:
                dist[v] = w
                parent[v] = u
    for i in range(n):
        if i != start:
            print(f"{i}    {parent[i]}  --> {dist[i]}")
    return d




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
        adj[v].append((u, w))
    print(prim(adj, n, 0))
    
