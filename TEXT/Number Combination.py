def NumberCombination(n):
    lst = [i for i in range(1, n + 1)]
    ans = []
    def bt(summ, x):
        if summ == n:
            x.sort()
            if x not in ans:
                ans.append(x)
            return
        else:
            for i in lst:
                if summ + i <= n:
                    bt(summ + i, x + [i])
                else:
                    break
    bt(0, [])
    return ans
lst = NumberCombination(4)  
print(lst)
