def most_frequency_number(lst):
    maxx = float("-inf")
    for i in range(len(lst) - 1):
        max_count = 1
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                max_count += 1
        if max_count > maxx:
            maxx = max_count
            num = [lst[i]]
        elif max_count == maxx:
            num.append(lst[i])
    return num if maxx > 1 else None
lst = [1, 2, 3, 4, 5, 1, 2]
print(most_frequency_number(lst))
