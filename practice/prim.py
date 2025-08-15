def prim(n, adj, start):
    dist = [float("inf")] * (n + 1)
    visited = [0] * (n + 1)
    parent = [-1] * (n + 1)
    dist[start] = 0
    d = 0
    for _ in range(n):
        min_cost = float("inf")
        u = -1
        for i in range(1, n + 1):
            if not visited[i] and dist[i] < min_cost:
                
                min_cost = dist[i]
                u = i
        print(u, end = " ")
        if u == -1:
            break
        visited[u] = 1
        d += dist[u]
        for v in range(1, n + 1):
            if adj[u][v] != 0 and not visited[v] and adj[u][v] < dist[v]:
                dist[v] = adj[u][v]
                parent[v] = u
    print("Các cạnh trong cây khung nhỏ nhất:")
    for v in range(1, n + 1):
        if parent[v] != -1:
            print(f"{parent[v]} - {v} (weight = {adj[parent[v]][v]})")
    print(d)







if __name__ == "__main__":
    n = int(input())
    adj = [[0] * (n + 1)]
    for i in range(1, n + 1):
        row = [0] + list(map(int, input().split()))
        adj.append(row)
    start = int(input())
    prim(n, adj, start)
    print(adj)