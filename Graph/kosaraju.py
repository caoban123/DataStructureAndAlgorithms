n, m = map(int,input().split())
adj = {}
adj_r = {}
for i in range(1, n + 1):
    adj[i] = []
    adj_r[i] = []
def add_edge(x,y):
    if x not in adj :
        adj[x] = []
    if  y not in adj_r:
        adj_r[y] = []
    adj[x].append(y)
    adj_r[y].append(x)
for i in range(m):
    u, v = map(int, input().split())
    add_edge(u, v)
print(adj)
print(adj_r)
def dfs1(i):
    visited[i] = 1
    for neighbor in adj[i]:
        if not visited[neighbor]:
            dfs1(neighbor)
    topo.append(i)
def dfs2(i):
    visited[i] = 1
    print(i, end = " ")
    for neighbor in adj_r[i]:
        if not visited[neighbor]:
            dfs2(neighbor)
def SCC():
    global visited 
    global topo
    visited = [0] * (n + 1)
    topo = []
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)
    visited = [0] * (n + 1)
    scc_count = 0
    while topo:
        i = topo.pop()
        if not visited[i]:
            scc_count += 1
            print(f"{scc_count} is:", end = " ")
            dfs2(i)
            print()
    print("Number of SCCs:", scc_count)
if __name__ == "__main__":
    SCC()




