# # def cnt(n):
# #     cnt = 0
# #     while n:
# #         cnt += 1
# #         n //= 10
# #     return cnt

# # # num = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
# # num = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
# # n = 3749
# # countdig = cnt(n) - 1
# # lst = []
# # while n:
# #     dig = n % 10
# #     lst.append(dig)
# #     n //= 10
# # lst.reverse()
# # s = ""
# # i = 0
# # while i < len(lst):
# #     numb = lst[i] * (10 ** countdig)
# #     if numb == 400:
# #         s += "CD"
# #         i += 1
# #         countdig -= 1
# #         continue
# #     if numb == 40:
# #         s += "XL"
# #         i += 1
# #         countdig -= 1
# #         continue
# #     if numb == 4:
# #         s += "IV"
# #         i += 1
# #         countdig -= 1
# #         continue
# #     if numb == 9:
# #         s += "IX"
# #         i += 1
# #         countdig -= 1
# #         continue
# #     if numb == 900:
# #         s += "CM"
# #         i += 1
# #         countdig -= 1
# #         continue
# #     for key,value in num.items():
# #         while numb > 0:
# #             if numb - value < 0:
# #                 break
# #             else:
# #                 s += key
# #                 numb -= value
# #         if numb == 0:
# #             break
# #     i += 1
# #     countdig -= 1
# # print(s)



# # def intToRoman(num: int) -> str:
# #         value_symbol = {1000:"M",900:"CM",
# #         500:"D",400:"CD",
# #         100:"C",90:"XC",
# #         50:"L",40:"XL",
# #         10:"X",9:"IX",
# #         5:"V",4:"IV",
# #         1:"I"
# #         }
# #         res = []
# #         for value,symbol in value_symbol.items():
# #             if num == 0: break
# #             count = num // value
# #             if count == 0 : continue
# #             res.append(symbol*count)
# #             num -= count * value
# #         return "".join(res)

# # print(intToRoman(1994))

# # a = input().split()
# # print(a)

# def check(num, cnt):
#     if cnt == 0:
#         return num
#     s = ""
#     lst = []
#     num = int(num)
#     # Tách các chữ số và đưa vào danh sách lst
#     while num:
#         digit = num % 10
#         lst.append(digit)
#         num //= 10
#     lst.reverse()
    
#     i = 0
#     # Duyệt qua lst và đếm các chữ số liên tiếp
#     while i < len(lst):
#         x = lst[i]
#         count = 1
#         while i + 1 < len(lst) and x == lst[i + 1]:
#             count += 1
#             i += 1
#         s += str(count) + str(x)
#         i += 1

#     # Giảm cnt và gọi đệ quy với chuỗi mới s
#     cnt -= 1
#     return check(s, cnt)

# print(check(1,3))
# a ="aBcDeF"
# a = list(a)
# lst1 = []
# lst2 = []
# for i in a:
#     if i.islower():
#         lst1.append(i)
#     else:
#         lst2.append(i)
# print(lst1)
# print(lst2)
# s = ""
# for i in lst1:
#     s += i
# for i in lst2:
#     s += i
# print(s)
# n = 5
# for i in range(n):
#     for j in range(i,n - 1):
#         print(" ",end = " ")
#     for j in range(n - i,n + 1):
#         print("*",end = " ")
#     print()
# lst = ["s","d","",None,"da"]
# lst1 = [i for i in lst if i is not None and i != ""]
# print(lst1)
s = "hello-every-body"
s = s.replace("-"," ")
print(s)