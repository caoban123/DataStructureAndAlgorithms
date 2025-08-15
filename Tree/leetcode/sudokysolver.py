board = [[".",".",".",".",".",".",".",".","."],
         [".","9",".",".","1",".",".","3","."],
         [".",".","6",".","2",".","7",".","."],
         [".",".",".","3",".","4",".",".","."],
         ["2","1",".",".",".",".",".","9","8"],
         [".",".",".",".",".",".",".",".","."],
         [".",".","2","5",".","6","4",".","."],
         [".","8",".",".",".",".",".","1","."],
         [".",".",".",".",".",".",".",".","."]]
rows = {i: set() for i in range(9)}
cols = {j: set() for j in range(9)}
squares = {(i, j): set() for i in range(3) for j in range(3)}
lst = []
for i in range(9):
    for j in range(9):
        if board[i][j] != '.':
            num = (board[i][j])
            if i not in rows:
                rows[i] = set()
            if j not in cols:
                cols[j] = set()
            if (i // 3, j // 3) not in squares:
                squares[(i // 3, j // 3)] = set()
            rows[i].add(num)
            cols[j].add(num)
            squares[(i // 3, j // 3)].add(num)
        else:
            lst.append((i,j))


def backtrack(index):
    if index == len(lst):
        return True
    i, j = lst[index]
    for num in map(str, range(1, 10)):
        if num not in rows[i] and num not in cols[j] and num not in squares[(i // 3, j // 3)]:
            board[i][j] = num
            rows[i].add(num)
            cols[j].add(num)
            squares[(i // 3 , j // 3)].add(num)
            if backtrack(index + 1):
                return True
            board[i][j] = "."
            rows[i].remove(num)
            cols[j].remove(num)
            squares[(i // 3, j // 3)].remove(num)
    return False

backtrack(0)
for row in board:
    print(row)