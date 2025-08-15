board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
x = board.copy()
vecx = (1, 0, -1, 0)

vecy = (0, 1, 0, -1)
def dfs(z, word, i, j, k):
    if k == len(word):
        return True
    temp = z[i][j]
    z[i][j] = "#"
    for d in range(4):
        ni = i + vecx[d]
        nj = j + vecy[d]
        if 0 <= ni < len(z) and 0 <= nj < len(z[0]) and z[ni][nj] == word[k]:
            if dfs(z, word, ni, nj, k + 1):
                return True
    z[i][j] = temp
    return False
    
lst = []
for word in words:
    found = False
    x = [row.copy() for row in board]
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == word[0]:
                found = dfs(x, word, i, j, 1)
                if found:
                    lst.append(word)
                    break
        if found:
            break

print(lst) # ["eat","oath"]

        

