def check(num, cnt):
    if cnt == 0:
        return num
    lst = []
    while num:
        lst.append(num % 10)
        num //= 10
    lst.reverse()
    new_num = ""
    count = 1
    i = 0
    while i < len(lst) - 1:
        if lst[i] == lst[i + 1]:
            count += 1
        else:
            new_num += str(count) + str(lst[i])
            count = 1  
        i += 1
    new_num += str(count) + str(lst[i])
    cnt -= 1
    return check(int(new_num), cnt)
print(check(1,0))
