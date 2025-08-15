n, m = map(int, input().split())
adj = {}
dscanh = []
for i in range(1, n + 1):
    adj[i] = []
def add_edge(a, b):
    adj[a].append(b)
    adj[b].append(a)
    dscanh.append([a,b])

for _ in range(m):
    u, v = map(int, input().split())
    add_edge(u, v)

visited = [False] * 1000
def dfs(i):
    visited[i] = True
    for neighbor in adj[i]:
        if not visited[neighbor]:
            dfs(neighbor)
def dfs2(i, s, t):
    visited[i] = True
    for neighbor in adj[i]:
        if (i == s and neighbor == t) or (i == t and neighbor == s):
            continue
        if not visited[neighbor]:
            dfs2(neighbor, s, t)
def canhcau():
    global visited
    ans = 0
    tplt = 0
    visited = [False] * 1000
    for i in range(1, n + 1):
        if not visited[i]:
            tplt += 1
            dfs(i)
    for x, y in dscanh:
        visited = [False] * 1000
        dem = 0
        for j in range(1, n + 1):
            if not visited[j]:
                dem += 1
                dfs2(j, x, y)
        if dem > tplt:
            ans += 1
    print(ans)


        
def dinhtru():
    global visited
    ans = 0
    tplt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            tplt += 1
            dfs(i)
    for i in range(1, n + 1):
        visited = [False] * 1000
        visited[i] = True
        cnt = 0
        for j in range(1, n + 1):
            if not visited[j]:
                cnt += 1
                dfs(j)
        if cnt > tplt:
            ans += 1
    print(ans)
    
canhcau()

