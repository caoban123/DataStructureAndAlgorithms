n, m = map(int,input().split())
adj = {}
adj_r = {}
for i in range(1, n + 1):
    adj[i] = []
    adj_r[i] = []
def add_edge(x, y):
    adj[x].append(y)
    adj_r[y].append(x)

for i in range(m):
    u, v = map(int, input().split())
    add_edge(u, v)
def dfs1(i):
    visited[i] = True
    for j in adj[i]:
        if not visited[j]:
            dfs1(j)
    stack.append(i)

def dfs2(i):
    visited[i] = True
    print(i, end = " ")
    for j in adj_r[i]:
        if not visited[j]:
            dfs2(j)

def SCC():
    global visited
    global stack
    visited = [False] * (n + 1)
    stack = []
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)
    visited = [False] * (n + 1)
    cnt = 0
    save = []
    while stack:
        i = stack.pop()
        
        if not visited[i]:
            save.append(i)
            dfs2(i)
            cnt += 1
            print()
    if cnt == 1:
        print("YES")
    else:
        print("NO")
        print(*reversed(save))
if __name__ == "__main__":
    SCC()
    