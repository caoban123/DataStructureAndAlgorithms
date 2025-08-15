n = list(map(int,input().split()))
l = 0
r = len(n) - 1
Water = 0
while l < r:
    Area = min(n[l],n[r]) * (r - l)
    Water = max(Water,Area)
    if n[l] < n[r]:
        l += 1
    else:
        r -= 1
print(Water)