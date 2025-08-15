#Heap sort
def heapify(n, lst, index):
    left = 2 * index + 1
    right = 2 * index + 2
    largest = index
    if left < n and lst[left] > lst[largest]:
        largest = left
    if right < n and lst[right] > lst[largest]:
        largest = right
    if largest != index:
        lst[largest] , lst[index] = lst[index], lst[largest]
        print(lst)
        heapify(n, lst, largest)
    else:
        print(lst)
def heap_sort(lst):
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, lst, i)
    for i in range(n - 1, -1, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(i, lst, 0)
#quicksort
def quicksort(lst, left, right):
    if left < right:
        pivot = lst[(left + right) // 2]
        i, j = left, right
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
            quicksort(lst, left, j)
        if i < right:
            quicksort(lst, i, right)
#mergesort

def merge(lst, left, middle, right):
    x = lst[left: middle + 1]
    y = lst[middle + 1: right + 1]
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
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

    

def mergesort(lst, left, right):
    if left >= right:
        return
    middle = (left + right) // 2
    mergesort(lst, left, middle)
    mergesort(lst, middle + 1, right)
    merge(lst, left, middle, right)
#bubblesort
def bubblesort(lst):
    n = len(lst)
    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap = True
        if not swap:
            break
#insertionsort
def insertionsort(lst):
    for i in range(len(lst)):
        j = i - 1
        value = lst[i]
        while j >= 0 and lst[j] > value:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = value
#interchangesort
def interchangesort(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
#selectionsort
def selectionsort(lst):
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[min_index], lst[i] = lst[i], lst[min_index]


def test_sort(algorithm, lst):
    temp = lst.copy()
    if algorithm.__name__ in ['quicksort', 'mergesort']:
        algorithm(temp, 0, len(temp) - 1)
    else:
        algorithm(temp)
    print(f"{algorithm.__name__}: {temp}")




                


# lst = [5, 4, 3, 2, 1]
# test_sort(heap_sort, lst)
# test_sort(quicksort, lst)
# test_sort(mergesort, lst)
# test_sort(bubblesort, lst)
# test_sort(insertionsort, lst)
# test_sort(interchangesort, lst)
# test_sort(selectionsort, lst)
lst = [12,3,17,8,4,25,6,1,10]
heap_sort(lst)