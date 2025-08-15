from collections import deque

n, m = map(int, input().split())

map = [list(map(str,input())) for i in range(n)]

vec1 = [1, 0, 0, -1]
vec2 = [0, 1, -1, 0]
visited = [[False] * m for i in range(n)]

def dfs(i, j):
    print(i, j)
    visited[i][j] = True
    for k in range(4):
        i1 = i + vec1[k]
        j1 = j + vec2[k]
        if 0 <= i1 < n and 0 <= j1 < m and map[i1][j1] == 'x' and not visited[i1][j1]:
            dfs(i1, j1)
def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        print(x, y)
        for k in range(4):
            i1 = x + vec1[k]
            j1 = y + vec2[k]
            if 0 <= i1 < n and 0 <= j1 < m and map[i1][j1] == 'x' and not visited[i1][j1]:
                
                queue.append((i1, j1))
                visited[i1][j1] = True
count = 0
for i in range(n):
    for j in range(m):
        if map[i][j] == 'x' and not visited[i][j]:
            print(f"Thanh phan lien thong thu {count + 1}: ")
            bfs(i, j)
            count += 1

print(count)

