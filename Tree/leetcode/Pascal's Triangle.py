triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
lst = []
n = 1
for i in range(numRows):
    lst.append([0] * n)
    n += 1
for i in lst:
    i[0] = 1
    i[-1] = 1
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 1:
            continue
        else:
            lst[i][j] = lst[i-1][j] +lst[i-1][j-1]
