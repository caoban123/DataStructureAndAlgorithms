edges = [[1,2],[1,3],[2,3]]
n = max(max(i) for i in edges)
parent = [0] * 10000
size = [0] * 10000
def make_set(n):
    for i in range(1, n + 1):
        parent[i] = i
        size[i] = 1
def find_parent(i):
    if i == parent[i]:
        return i
    parent[i] = find_parent(parent[i])
    return parent[i]
def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a!=b:
        if size[a] < size[b]:
            parent[a] = b
            size[b] += size[a]
        else:
            parent[b] = a
            size[a] += size[b]
        return True
    return False

make_set(n)
for edge in edges:
    if union(edge[0], edge[1]):
        continue
    else:
        print(edge)
        break

        
