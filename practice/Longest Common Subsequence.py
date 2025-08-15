text1 ="oxcpqrsvwf"
text2 ="shmtulqrypy"
lst = []
board = [[0] * len(text1) for _ in range(len(text2))]
for i in range(len(text2)):
    for j in range(len(text1)):
        if text1[j] == text2[i]:
            board[i][j] = 1
            lst.append((i, j))
# visited = [0] * len(lst)
# maxx = float("-inf")
# def 
for i in board:
    print(i)