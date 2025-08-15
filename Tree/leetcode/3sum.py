lst = list(map(int,input().split()))
lst.sort()
n = []
for i in range(len(lst) - 2):
    if i > 0 and lst[i] == lst[i-1]:
        continue
    l = i + 1
    r = len(lst) - 1
    while l < r:
        total = lst[i] + lst[r] + lst[l]
        if total > 0:
            r -= 1
        elif total < 0:
            l += 1
        else:
            n.append([lst[i],lst[r],lst[l]])
            while l < r and lst[l] == lst[l  + 1]:
                l += 1
            while l < r and lst[r] == lst[r - 1]:
                r -= 1
            l += 1
            r-= 1
            
print(n)