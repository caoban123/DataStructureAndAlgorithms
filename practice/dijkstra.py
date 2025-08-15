import heapq

def dijkstra(n, adj, start):
    dist = [float("inf")] * (n)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > dist[u]:
            continue
        for v in range(n):
            if dist[v] > dist[u] + adj[u][v] and adj[u][v] != 0:
                dist[v] = dist[u] + adj[u][v]
                heapq.heappush(heap,(dist[v],v))
        result = []
    for i in range(n ):
        if i == start:
            continue
        result.append(-1 if dist[i] == float('inf') else dist[i])
    print(result)

if __name__ == "__main__":
    n = int(input())
    adj = []
    for i in range(n):
        row = list(map(int, input().split()))
        adj.append(row)
    start = int(input())
    dijkstra(n, adj, start)