def quick_sort(lst, left, right):
    if left < right:
        i, j = left, right
        pivot = lst[(left + right) // 2 + 1]
        while i <= j:
            while lst[i] > pivot:
                i += 1
            while lst[j] < pivot:
                j -= 1
            if i <= j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
        if left < j:
            quick_sort(lst, left, j)
        if right > i:
            quick_sort(lst, i, right)
lst =[1,2,3,4,5]
quick_sort(lst,0,len(lst) - 1)
print(lst)