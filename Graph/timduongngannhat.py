from collections import deque
m, n = map(int,input().split())
map = [list(map(str,input())) for i in range(m)]
vec1 = [1, 0, 0, -1]
vec2 = [0, 1, -1, 0]
dp = [[0] * m for i in range(n)]
for i in range(m):
    for j in range(n):
        if map[i][j] == 'A':
            x1, y1 = i, j
        if map[i][j] == 'B':
            x2, y2 = i, j
def bfs(i, j):
    queue = deque([(i, j)])
    map[i][j] = 'x'
    dp[i][j] = 0
    print(i , j)
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + vec1[k]
            ny = y + vec2[k]
            if 0 <= nx < n and 0 <= ny < m and map[nx][ny]!= 'x':
                print(nx, ny)
                dp[nx][ny] = dp[x][y] + 1
                if map[nx][ny] == 'B':
                    return 
                queue.append((nx, ny))
                map[nx][ny] = 'x'
    return False
bfs(x1, y1)
if dp[x2][y2] == 0:
    print("Khong co duong di")
else:
    print(dp[x2][y2])
