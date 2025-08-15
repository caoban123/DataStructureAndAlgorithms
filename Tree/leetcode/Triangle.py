triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
numRows = len(triangle)
lst = []

n = 1
for i in range(numRows):
    lst.append([0] * n)
    n += 1
lst[0][0] = triangle[0][0]
for i in range(1,len(lst)):
    lst[i][0] = lst[i - 1][0]  + triangle[i][0]
    lst[i][-1] = lst[i - 1][-1]  + triangle[i][-1]
for i in range(1,len(lst)):
    for j in range(1,len(lst[i]) - 1):
        lst[i][j] = min(lst[i - 1][j] + triangle[i][j],lst[i - 1][j - 1] + triangle[i][j] )
print(min(lst[-1]))