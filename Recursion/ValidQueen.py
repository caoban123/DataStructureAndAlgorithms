N = 4

a = [0] * (N + 1)

cot = [True] * (N*2)

d1 = [True] * (N*2)

d2 = [True] * (N*2)
chess = [[0] * (N + 1) for i in range(N + 1)]
def inkq():
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            chess[i][j] = 0
    for i in range(1, N + 1):
        chess[i][a[i]] = 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(chess[i][j], end="")
        print()
    print()

def Try(i):
    for j in range(1, N + 1):
        if cot[j] == 1 and d1[i - j + N] == 1 and d2[i + j - 1] == 1:
            cot[j] = d1[i - j + N] = d2[i + j - 1] = False
            a[i] = j
            if i == N:
                inkq()
            else:
                Try(i + 1)
            cot[j] = d1[i - j + N] = d2[i + j - 1] = True
Try(1)

            
