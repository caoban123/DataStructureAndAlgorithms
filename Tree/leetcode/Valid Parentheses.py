def check(s):    
    x = {')':'(',']':'[','}':'{'}
    stack = []
    for i in s:
        if i in x:
            if stack is None:
                return False
            else:
                top = stack.pop()
                if top != x[i]:
                    return False
        else:
            stack.append(i)
    return True

s = input()
print(check(s))