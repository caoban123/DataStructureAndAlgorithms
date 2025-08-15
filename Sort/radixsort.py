def get_digit(num, index_digit):
    return (num // 10 ** index_digit) % 10
def radix_sort(lst):
    if not lst:
        return lst
    max_num = max(lst)
    max_digit = len(str(max_num))
    for i in range(max_digit):
        buckets = [[] for _ in range(10)]
        for num in lst:
            diget = get_digit(num, i)
            buckets[diget].append(num)
        lst.clear()
        for bucket in buckets:
            lst.extend(bucket)
lst = [5,4,3,2,1]
radix_sort(lst)
print(lst)
        