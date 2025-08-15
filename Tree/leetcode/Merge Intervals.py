intervals =[[1,4],[0,4]]
lst = []
i = 0
while i < len(intervals) - 1:
    lst1 = []
    lst1.extend(intervals[i])
    lst1.extend(intervals[i+1])
    if lst1[2] - lst1[1] <= 0 or (lst1[0] <= lst1[2] and lst1[1] >= lst1[3]) or (lst1[2] <= lst[0] and lst[3] >= lst1[1]):
        if lst1[0] <= lst1[2] and lst1[1] >= lst1[3]:
            lst.append([lst1[0],lst1[1]])
        if lst1[2] <= lst[0] and lst[3] >= lst1[1]:
            lst.append([lst1[2],lst1[3]])

        if lst1[2] - lst1[1] <= 0:
            lst.append([lst1[0],lst1[-1]])
        i += 2
        continue
    else:
        if i + 1 == len(intervals) - 1 and i == len(intervals) - 2:
            lst.append(intervals[i])
            lst.append(intervals[i + 1])
        lst.append(intervals[i])
    i += 1
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)
    