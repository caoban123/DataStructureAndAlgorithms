n = int(input())
parent = [0] * 1000
size = [0] * 1000
def make_set(n):
    for i in range(n+1):
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
    if a != b:
        if size[a] < size[b]:
            parent[a] = b
            size[b] += size[a]
        else:
            parent[b] = a
            size[a] += size[b]

make_set(n)
union(1,4)
union(1,5)
union(2,3)
union(1,2)
print(find_parent(3))
