# def interchangesort(lst):
#     for i in range(len(lst) - 1):
#         for j in range(i + 1, len(lst)):
#             if lst[i] > lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
# def bubblesort(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst) - i - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
# def heapify(lst, n, i):
#     left = 2 * i + 1
#     right = 2 * i + 2
#     largest = i
#     if left < n and lst[left] > lst[largest]:
#         largest = left
#     if right < n and lst[right] > lst[largest]:
#         largest = right
#     if largest != i:
#         lst[i], lst[largest] = lst[largest], lst[i]
#         heapify(lst, n, largest)
# def heapsort(lst):
#     n = len(lst) - 1
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(lst, n, lst[i])
#     for i in range(n - 1, 0, -1):
#         lst[i], lst[0] = lst[0], lst[i]
#         heapify(lst, i, 0)
# def merge(lst, left, middle, right):
#     lst1 = lst[left : middle + 1]
#     lst2 = lst[middle + 1 : right + 1]
#     i = 0
#     j = 0
#     while i < len(lst1) and j < len(lst2):
#         if lst1[i] < lst2[j]:
#             lst[left] = lst1[i]
#             left += 1
#             i += 1
#         else:
#             lst[left] = lst2[j]
#             left += 1
#             j += 1
#     while i < len(lst1):
#         lst[left] = lst1[i]
#         left += 1
#         i += 1
#     while j < len(lst2):
#         lst[left] = lst2[j]
#         left += 1
#         j += 1

# def mergesort(lst, left, right):
#     if left >= right:
#         return
#     middle = (left + right) // 2
#     mergesort(lst, left, middle)
#     mergesort(lst, middle + 1, right)
#     merge(lst, left, middle, right)
# def intertionsort(lst):
#     for i in range(1, len(lst)):
#         j = i - 1
#         key = lst[i]
#         while j >= 0 and lst[j] > key:
#             lst[j + 1] = lst[j]
#             j -= 1
#         lst[j + 1] = key
# def selectionsort(lst):
#     for i in range(len(lst) - 1):
#         min_index = i
#         for j in range(i + 1, len(lst)):
#             if lst[j] < lst[min_index]:
#                 min_index = j
#         lst[i], lst[min_index] = lst[min_index], lst[i]
# def quicksort(lst, left, right):
#     if left < right:
#         i, j = left, right
#         pivot = lst[(left + right) // 2 + 1]
#         while i <= j:
#             while lst[i] < pivot:
#                 i += 1
#             while lst[j] > pivot:
#                 j -= 1
#             if i <= j:
#                 lst[i], lst[j] = lst[j], lst[i]
#                 i += 1
#                 j -= 1
#         if left < j:
#             quicksort(lst, left, j)
#         if right > i:
#             quicksort(lst, i, right)
# def get_digit(num, i):
#     return (num // (10 ** i)) % 10
# def radixsort(lst):
#     max_num = max(lst)
#     n = len(str(max_num))
#     for i in range(n):
#         buckets = [[] for _ in range(10)]
#         for num in lst:
#             num_digit = get_digit(num, i)
#             buckets[num_digit].append(num)
#         lst.clear()
#         for bucket in buckets:
#             lst.extend(bucket)
# def countsort(lst):
#     if not lst:
#         return []
#     max_num = max(lst)
#     min_num = min(lst)
#     range_size = max_num - min_num + 1
#     dp = [0] * range_size
#     for num in lst:
#         dp[num - min_num] += 1
#         print(num - min_num)
#     lst.clear()
#     for i in range(range_size):
#         lst.extend([i + min_num] * dp[i])
#         print(i + min_num)
def insertionsortrev(lst):
    for i in range(1, len(lst)):
        j = i - 1
        key = lst[i]
        while j >= 0 and lst[j] < key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


def radixsort(lst):
    n = len(lst)
    max_num = max(lst)
    leng = len(str(max_num))
    for i in range(leng):
        buckets = [[] for _ in range(10)]
        for num in lst:
            get_index = (num // 10 ** i) % 10
            buckets[get_index].append(num)
        lst.clear()
        for bucket in buckets:
            lst.extend(bucket)






lst = [5,4,3,2,6,1]
# interchangesort(lst)
# bubblesort(lst)
# heapsort(lst)
# mergesort(lst, 0, len(lst) - 1)
# insertionsort(lst)
# selectionsort(lst)
# quicksort(lst, 0, len(lst) - 1) 
# radixsort(lst)
# intertionsortrev(lst)
print(lst)

