n, m = map(int, input().split())

adj = {}

for i in range(1, n + 1):
    adj[i] = []
for i in range(m):
    u, v, w = map(int, input().split())
    adj[u].append([v, w])
    adj[v].append([u, w])
print(adj)
used = [0] * 1000
def prim(u):
    mst = []
    d = 0
    used[u] = True
    while len(mst) < n - 1:
        min_w = float("inf")
        for v in range(1, n + 1):
            if used[v]:
                for edge in adj[v]:
                    if not used[edge[0]] and edge[1] < min_w:
                        min_w = edge[1]
                        x = edge[0]
                        y = v

        mst.append([x, y, min_w])
        d += min_w
        used[x] = True
    print(d)
    for edge in mst:
        print(edge[0], edge[1], edge[2])

prim(1)

