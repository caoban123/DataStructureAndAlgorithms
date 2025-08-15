import heapq

n, m, s, t = map(int, input().split())
edge = {}
pre = [0] * 1000
for i in range(m):
    u, v, w = map(int, input().split())
    if u not in edge:
        edge[u] = []
    edge[u].append((v, w))
    if v not in edge:
        edge[v] = []
    edge[v].append((u, w))

def dijkstra(s, t):
    dist = {u: float('inf') for u in edge}
    dist[s] = 0
    heap = [(0, s)]
    while heap:
        kc, u = heapq.heappop(heap)
        if dist[u] < kc:
            continue
        for v, w in edge[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
                pre[v] = u
    path = []
    while True:
        path.append(t)
        if t == s:
            break
        t = pre[t]
    path.reverse()
    print('->'.join(map(str, path)))
    return dist
print(dijkstra(s, t)) 
