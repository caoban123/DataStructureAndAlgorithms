# def recursion(n):
#     if n == 1:
#         return 1
#     else:
#         return n + 1 / recursion(n - 1)

# print(recursion(3))
# def TowersofHanoi(n, a, b, c):
#     if n == 1:
#         print("Move disk 1 from", a, "to", c)
#     else:
#         TowersofHanoi(n - 1, a, c, b)
#         print("Move disk", n, "from", a, "to", c)
#         TowersofHanoi(n - 1, b, a, c)
# TowersofHanoi(3, 'A', 'B', 'C')

n = int(input())

d1 = [1] * (2 * n)
d2 = [1] * (2 * n)
cot = [1] * (2 * n)
a = [0] * (n + 1)
chess = [[0] * (n + 1) for i in range(n + 1)]

def inkq():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            chess[i][j] = 0
    for i in range(1, n + 1):
        chess[i][a[i]] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(chess[i][j], end="")
        print()
    print()
def Try(i):
    for j in range(1, n + 1):
        if d1[i - j + n] == 1 and d2[i + j - 1] == 1 and cot[j] == 1:
            d1[i - j + n] = 0
            d2[i + j - 1] = 0
            cot[j] = 0
            a[i] = j
            if i == n:
                inkq()
            else:
                Try(i + 1)
            d1[i - j + n] = 1
            d2[i + j - 1] = 1
            cot[j] = 1
Try(1)
