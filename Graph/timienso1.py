n, m = map(int, input().split())
lst = [list(map(int , input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = (1, 0, 0, -1)
dy = (0, 1, -1, 0)
def bfs(i, j):
    visited[i][j] = True
    for z in range(4):
        x = i + dx[z]
        y = j + dy[z]
        if 0 <= x < n and 0 <= y < m and not visited[x][y] and lst[x][y] == 1:
            bfs(x, y) 
        
cnt = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1 and not visited[i][j]:
            cnt += 1
            bfs(i,j)
print(cnt)
