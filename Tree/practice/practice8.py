def bellman_ford(n, graph, start):
    dist = [float("inf")] * n
    dist[start] = 0
    parent = [-1] * n
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if graph[u][v] != 0 and dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
                    parent[v] = u
    for u in range(n):
        for v in range(n):
            if graph[u][v] != 0 and dist[u] + graph[u][v] < dist[v]:
                return None
    for v in range(n):
        if v == start:
            continue
        path = []
        x = v
        while x != -1:
            path.append(x)
            x = parent[x]
        path.reverse()
        print(f" The shortest path from {start} to {v}  {dist[v]}", "->".join(map(str, path))) 
    
    


if __name__ == "__main__":
    start = int(input())
    n = int(input())
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    bellman_ford(n, graph, start)