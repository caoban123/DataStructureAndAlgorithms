
board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '8', '.', '.', '.', '3', '9'],
    ['4', '.', '6', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '6', '.', '2', '9', '.', '.'],
    ['.', '6', '.', '5', '4', '9', '.', '.', '.'],
    ['.', '.', '.', '8', '6', '.', '.', '7', '2'],
    ['.', '.', '.', '4', '8', '7', '.', '.', '6']
]

rows = [[] for _ in range(9)]
columns = [[] for _ in range(9)]
squares = [[] for _ in range(9)]

for i in range(9):
    for j in range(9):
        if board[i][j] == ".":
            continue
        num = board[i][j]
        if num in rows[i]:
            return False
        rows[i].append(num)
        if num in columns[j]:
            return False
        columns[j].append(num)
        if num in squares[(i // 3) * 3 + j // 3]:
            return False
        squares[(i // 3) * 3 + j // 3].append(num)

return True