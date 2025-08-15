def enhancedMergesort(a, left, right):
    while len(a) > 1:
        new_lst = []
        i = 0
        while i < len(a):
            if i + 1 < len(a):
                x = a[i] + a[i + 1]
                new_lst.append(insertionSort(x))
                i += 2
            else:
                new_lst.append(a[i])
                i += 1
        a = new_lst
    return new_lst
def insertionSort(a):
    for i in range(1, len(a)):
        j = i - 1
        value = a[i]
        while j >= 0 and value < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value
    return a

lst = [5, 4, 3, 2, 1]
lst = [[i] for i in lst]
print(enhancedMergesort(lst, 0, len(lst) - 1)[0])
