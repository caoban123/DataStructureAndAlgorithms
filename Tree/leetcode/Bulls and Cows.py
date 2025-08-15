secret = "1234"
guess = "0111"
bulls = 0
cows = 0
i = 0
lst1 = []
lst2 = []
while i < len(secret):
    if secret[i] == guess[i]:
        bulls += 1
    else:
        lst1.append(secret[i])
        lst2.append(guess[i])
    i += 1
# dic = dict()
# for i in lst:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1
# for value in dic.values():
#     if value > 1:
#         cows += value / 2
# if bulls == 0:
#     cows -= 1
while len(lst1) != 0:
    digit = lst1.pop(0)
    for i in range(len(lst2)):
        if digit == lst2[i]:
            lst2.pop(i)
            cows += 1
            break
print(str(bulls)  +"A" + str(int(cows)) + "B")





