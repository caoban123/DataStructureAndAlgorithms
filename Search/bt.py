def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        value = lst[i]
        while j >= 0 and value < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = value
    return lst
def linear_search(lst, x):
    insertion_sort(lst)
    for i in range(len(lst)):
        if lst[i] > x:
            return -1
        if lst[i] == x:
            return i
    return -1
lst = [5, 4, 3, 2, 1]
x = 3
result = linear_search(lst, x)
if result != -1:
    print(f"Element {x} found at index {result}")
else:
    print(f"Element {x} not found in the list")