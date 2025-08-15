matrix = [[1,2,3],[4,5,6],[7,8,9]]
x = len(matrix) * len(matrix[0])
n = len(matrix)
m = len(matrix[0])
lst = matrix[0]
i = 0
j = len(matrix[0]) - 1
check = -1
while x > len(lst):
    check *= -1
    n -= 1
    m -= 1
    for _ in range(n):
        i += check
        lst.append(matrix[i][j])
        if len(lst) == x:
            break
    for _ in range(m):
        j -= check
        lst.append(matrix[i][j])
        if len(lst) == x:
            break
print(lst)
