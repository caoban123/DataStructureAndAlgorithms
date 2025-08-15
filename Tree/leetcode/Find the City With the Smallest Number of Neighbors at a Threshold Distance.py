import heapq
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
    adj = {i : [] for i in range(n)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

        
    def dijkstra(u):
        dist = [float("inf")] * n
        dist[u] = 0
        heap = [(0, u)]
        while heap:
            current_dist, u = heapq.heappop(heap)
            if current_dist > dist[u]:
                continue
            for v, w in adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (-dist[v], v))
        cnt = 0
        for i in dist:
            if i <= distanceThreshold and i != 0:
                cnt += 1
        return cnt
    minn = float("inf")
    lst = []
    for i in range(n):
        cnt = dijkstra(i)
        minn = min(cnt, minn)
        lst.append(cnt)
    for i in range(n - 1, -1, -1):
        if lst[i] == minn:
            return i
            
