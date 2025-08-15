def duplicate(lst):
    list_of_dup = []
    appear = []
    for i in range(len(lst)):
        if lst[i] not in appear:
            appear.append(lst[i])
        else:
            list_of_dup.append(lst[i])
    return list_of_dup
lst = [1, 2, 3, 4, 5, 1, 2]
print(duplicate(lst))