n = list(map(int,input().split()))
n.sort() 
lst = []
for i in range(len(n) - 2):
    if i > 0 and n[i] == n[i - 1]:
        continue
    l = i + 1  
    r = len(n) - 1  
    while l < r:
        total = n[i] + n[l] + n[r]
        lst.append(total) 
       
        while l < r and l > i + 1 and n[l] == n[l - 1]:
            l += 1
        
        while l < r and r < len(n) - 1 and n[r] == n[r + 1]:
            r -= 1
        x = r
        r -= 1
        while l < r:
            total = n[i] + n[l] + n[r]
            lst.append(total) 
            r -= 1
            while l < r and r < len(n) - 1 and n[r] == n[r + 1]:
                r -= 1
        r = x
        y = l
        l += 1
        while l < r:
            total = n[i] + n[l] + n[r]
            lst.append(total)
            l += 1
            while l < r and l > i + 1 and n[l] == n[l - 1]:
                l += 1
        l = y 
        l += 1
        r -= 1
target = int(input())
closest_sum = lst[0] 
Min = abs(closest_sum - target)

for i in lst:
    check = target - i
    if abs(check) < Min:
        Min = abs(check)
        closest_sum = i
print(closest_sum)

