from collections import deque


def bfs(n, u):
    queue = deque([u])
    visited[u] = 1
    while queue:
        x = queue.popleft()
        print(x, end = " ")
        for v in range(n):
            if not visited[v] and adj[x][v]:
                queue.append(v)
                visited[v] = 1
def dfs1(n, u):
    stack = [u]
    while stack:
        x = stack[-1]
        if not visited[x]:
            print(x , end = " ")
            visited[x] = 1
        found = False
        for v in range(n):
            if adj[x][v] == 1 and not visited[v]:
                stack.append(v)
                found = True
                break
        if not found:
            stack.pop()

def dfs(n, u):
    visited[u] = True
    print(u, end = " ")
    for i in range(n):
        if not visited[i] and adj[u][i] == 1:
            dfs(n, i)




if __name__ == "__main__":
    n = int(input())
    adj = []
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        adj.append(row)
    start = int(input())
    visited = [0] * n
    dfs1(n, start)
