def insertion_sort(lst):
    n = len(lst)
    for i in range(1, len(lst)):
        j = i - 1
        value = lst[i]
        while j >= 0 and value < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = value
lst = [5,4,1,3,2,1]

insertion_sort(lst)

print(lst)