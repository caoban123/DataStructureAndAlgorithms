n = input()
l = 0
r = 0
Max = 0
lst = []
while r < len(n):
    if n[r] not in lst:
        lst.append(n[r])
        Max = max(Max,len(lst))
        r += 1
    else:
        lst.pop(0)
        l += 1
print(Max)