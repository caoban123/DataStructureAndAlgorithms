def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]
def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x == y:
        return False
    else:
        if size[x] > size[y]:
            parent[y] = x
            size[x] += 1
        else:
            parent[x] = y
            size[y] += 1
        return True
def kruskal(edges, n):
    mst = []
    for e in edges:
        if len(mst) == n - 1:
            break
        if union(e[0], e[1]):
            mst.append(e)
    if len(mst) != n - 1:
        return "do thi khong lien thong"
    return mst


if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    parent = [i for i in range(n)]
    size = [1 for i in range(n)]
    edges.sort(key = lambda x: x[2])
    print(kruskal(edges, n))



# 5 5
# 0 2 8
# 0 3 3
# 1 2 6
# 2 3 4
# 3 4 5