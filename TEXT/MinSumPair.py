def  MinimumAbsoluteSumPair(lst):
    left = 0
    right = len(lst) - 1
    minn = float('inf')
    while left < right:
        val = abs(lst[left] + lst[right])
        if val < minn:
            left_index = left
            right_index = right
            minn = val
        if abs(lst[left] + lst[right - 1]) < minn:
            right -= 1
        elif abs(lst[left + 1] + lst[right]) < minn:
            left += 1
        else:
            left += 1
            right -= 1
    return left_index, right_index


n = 7
lst = [-2, 0, 1, 2]
print(MinimumAbsoluteSumPair(lst))
