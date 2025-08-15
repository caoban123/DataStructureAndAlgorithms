def merge(lst, left, middle, right):
    x = lst[left : middle + 1]
    y = lst[middle + 1 : right + 1]
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            lst[left] = x[i]
            left += 1
            i += 1
        else:
            lst[left] = y[j]
            left += 1
            j += 1
    while i < len(x):
        lst[left] = x[i]
        left += 1
        i += 1
    while j < len(y):
        lst[left] = y[j]
        left += 1
        j += 1
    
def merge_sort(lst, left, right):
    if left >= right:
        return
    middle = (left + right) // 2
    merge_sort(lst, left, middle)
    merge_sort(lst, middle + 1, right)
    merge(lst, left, middle, right)

lst = [1.5, 5,4,3,2,1]
merge_sort(lst, 0, len(lst) - 1)
print(lst)
