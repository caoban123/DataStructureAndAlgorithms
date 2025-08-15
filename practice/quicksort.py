def quicksort(lst, left, right):
    if left < right:
        i = left
        j = right
        pivot = lst[(left + right) // 2 + 1]
        while i <= j:
            while lst[i] < pivot:
                i += 1
            while lst[j] > pivot:
                j -= 1
            if i <= j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
        if left < j:
            quicksort(lst,left, j)
        if right > i:
            quicksort(lst,i, right)
lst = [5,4,3,2,1]
quicksort(lst, 0, len(lst) - 1)
print(lst)

                
         