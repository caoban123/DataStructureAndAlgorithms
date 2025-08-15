n, m = map(int, input().split())
adj = {}

def add_edge(x, y):
    if x not in adj:
        adj[x] = []
    if y not in adj:
        adj[y] = []
    adj[x].append(y)
    adj[y].append(x)

for _ in range(m):
    u, v = map(int, input().split())
    add_edge(u, v)

def euler(i):
    st = []
    path = []
    st.append(i)
    while st:
        x = st[-1]
        if len(adj[x]) != 0:
            y = adj[x][0]
            st.append(y)
            adj[x].remove(y)
            adj[y].remove(x)
        else:
            st.pop()
            path.append(x)
    return path[::-1]

print(' '.join(map(str, euler(2))))

