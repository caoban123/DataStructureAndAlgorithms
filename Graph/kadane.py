n = int(input())
arr = list(map(int, input().split()))
min_pfs = 0
pos_min_pfs = 0
pfs = 0
rs = 0
l, r = 1, 1
for i in range(0, n):
    pfs += arr[i]
    if pfs - min_pfs > rs:
        rs = pfs - min_pfs
        l, r = pos_min_pfs, i
    if pfs < min_pfs:
        min_pfs = pfs
        pos_min_pfs = i + 1
        pfs=0
for i in range(l, r + 1):
    print(arr[i], end = " ")