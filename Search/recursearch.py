def linear_search_recur(lst, index, x):
    if not lst or index >= len(lst):
        return -1
    if lst[index] == x:
        return index
    else:
        return linear_search_recur(lst, index + 1, x)
lst = [1, 2, 3, 4, 5]
x = 3
index = 0
result = linear_search_recur(lst, index, x)
if result != -1:
    print(f"Element {x} found at index {result}")
else:
    print(f"Element {x} not found in the list")
