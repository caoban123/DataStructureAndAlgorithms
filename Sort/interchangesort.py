def interchange_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
lst = [5,4,3,2,1]

interchange_sort(lst)

print(lst)