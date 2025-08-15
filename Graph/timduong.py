from collections import deque

n, m = map(int, input().split())

map = [list(map(str,input())) for i in range(n)]

vec1 = [1, 0, 0, -1]
vec2 = [0, 1, -1, 0]
visited = [[False] * m for i in range(n)]
dp = [[0] * m for i in range(n)]
def dfs(i, j):
    if map[i][j] == 'B':
        return True
    map[i][j] = 'x'
    print(i, j)
    for k in range(4):
        nx = i + vec1[k]
        ny = j + vec2[k]
        if 0 <= nx < n and 0 <= ny < m and map[nx][ny] != 'x':
            if dfs(nx, ny):
                return True
    return False
def bfs(i , j):
    queue = deque([(i, j)])
    map[i][j] = 'x'
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + vec1[k]
            ny = y + vec2[k]
            if 0 <= nx < n and 0 <= ny < m and map[nx][ny] != 'x':
                if map[nx][ny] == 'B':
                    return True
                print(nx, ny)
                queue.append((nx, ny))
                map[nx][ny] = 'x'
    return False
for i in range(n):
    for j in range(m):
        if map[i][j] == 'A':
            x1 = i
            y1 = j
        elif map[i][j] == 'B':
            x2 = i
            y2 = j
print(bfs(x1,y1))

