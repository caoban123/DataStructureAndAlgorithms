def prim(n, graph):
    dist = [float("inf")] * n
    dist[0] = 0
    visited = [0] * n
    parent = [-1] * n
    for _ in range(n):
        u = -1
        min_cost = float("inf")
        for i in range(n):
            if not visited[i] and dist[i] < min_cost:
                u = i
                min_cost = dist[i]
        if u == -1:
            break
        visited[u] = 1
        for v in range(n):
            if graph[u][v] != 0 and not visited[v] and dist[v] > graph[u][v]:
                dist[v] = graph[u][v]
                parent[v] = u

    print("Edge   Weight")
    for v in range(n):
        if parent[v] != -1:
            print(f"{parent[v]} - {v}   {graph[v][parent[v]]}")
    

    

     



if __name__ == "__main__":
    n = int(input())
    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    prim(n, graph)
    


# 0
# 5
# 0 0 8 3 0
# 0 0 6 0 0
# 8 6 0 4 0
# 3 0 4 0 5
# 0 0 0 5 0