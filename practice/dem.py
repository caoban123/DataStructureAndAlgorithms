import time
import random

def measure_time(sort_func, lst):
    start = time.time()
    sort_func(lst)
    end = time.time()
    return (end - start) * 1000  # ms
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
def quicksort(arr):
    def _quicksort(lst, left, right):
        if left < right:
            i, j = left, right
            pivot = lst[(left + right) // 2]
            while i <= j:
                while lst[i] < pivot:
                    i += 1
                while lst[j] > pivot:
                    j -= 1
                if i <= j:
                    lst[i], lst[j] = lst[j], lst[i]
                    i += 1
                    j -= 1
            _quicksort(lst, left, j)
            _quicksort(lst, i, right)
    _quicksort(arr, 0, len(arr)-1)
 


sizes = [1000, 10000, 100000, 1000000]
for size in sizes:
    arr = [random.randint(0, size) for _ in range(size)]
    for sort_func in [insertion_sort, heapsort, quicksort]:
        copy = arr.copy()
        t = measure_time(sort_func, copy)
        print(f"{sort_func.__name__} với n={size}: {t:.2f}ms")


