def heapify(lst, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    while left < n and lst[left] > lst[largest]:
        largest = left
    while right < n and lst[right] > lst[largest]:
        largest = right
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)
def heap_sort(lst):
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    return lst
lst = [5,4,3,2,1]
print(heap_sort(lst))
