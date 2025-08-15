lst = []
def ans(candidates,target,lst1):
    if target == 0:
        lst.append(lst1)
        return
    if target < 0:
        return
    for i in candidates:
        ans(candidates,target - i,lst1 + [i])



candidates = [2,3,5]
target = 8
ans(candidates,8,[])
for i in lst:
    i.sort()
lst2 = []
for i in lst:
    if i not in lst2:
        lst2.append(i)
print(lst2)



        