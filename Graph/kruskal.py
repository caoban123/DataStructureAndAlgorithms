n, m = map(int, input().split())
edge = []
for i in range(m):
    u, v, w = map(int, input().split())
    edge.append((u, v, w))

edge.sort(key = lambda x: x[2])
parent = [0] * 1000
sz = [0] * 1000
for i in range(1, n + 1):
    parent[i] = i
    sz[i] = 1

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:
        if sz[x] < sz[y]:
            parent[x] = y
            sz[y] += sz[x]
        else:
            parent[y] = x
            sz[x] += sz[y]
        return True

def kruskal():
    mst = []
    d = 0
    for i in range(m):
        if len(mst) == n - 1:
            break
        e = edge[i]
        if union(e[0], e[1]):
            mst.append(e)
            d += e[2]
    if len(mst) != n - 1:
        print("Do thi khong lien thong")
    else:
        print("Trong so cua do thi lien thong nho nhat:", d)
        print(*mst)

kruskal()

