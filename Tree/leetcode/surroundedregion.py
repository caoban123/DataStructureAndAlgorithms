board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

n, m = len(board), len(board[0])

visited = [[0] * m for i in range(n)]

dx = (1, 0, -1, 0)

dy = (0, 1, 0, -1)
def dfs(i, j):
    visited[i][j] = 1
    board[i][j] = "T"
    for z in range(4):
        x = i + dx[z]
        y = j + dy[z]
        if 0 <= x < n and 0 <= y < m and board[x][y] == "O" and visited[x][y] == 0:
            board[x][y] = "T"
            dfs(x, y)
    
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and board[i][j] == "O" and (i == 0 or i == n - 1 or j == 0 or j == m - 1):
            dfs(i, j)
for i in range(n):
    for j in range(m):
        if board[i][j] == "O":
            board[i][j] = "X"
        elif board[i][j] == "T":
            board[i][j] = "0"
print(board)

