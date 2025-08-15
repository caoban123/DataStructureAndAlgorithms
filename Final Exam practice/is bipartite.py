
# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]

# def is_bipartite(matrix):
#     color = [-1] * (n)
#     queue = [0]
#     color[0] = 1
#     while queue:
#         node = queue.pop(0)
#         for v in range(n):
#             if matrix[node][v] != 0: 
#                 if color[v] == -1:
#                     color[v] = 1 - color[node]
#                     queue.append(v)
#                 elif color[v] == color[node]:
#                     return  False
#     return True
# n = 1052
                
# for i in [2,3,5,7]:
#     if n % i == 0:
#         while n % i == 0:
#             print(i)
#             n /= i
# if n != 1:
#     print(n)
# n = 24
# dem = 0
# p = 2
# for i in range(1,25):
#     x = i
#     if x % p == 0:
#         while x % p == 0:
#             dem += 1
#             x /= p
# print(dem)
# n = 5
# def SumSquare(n):
#     sum = 0
#     while n:
#         value = n % 10
#         sum += value**2
#         n //= 10
#     return sum
# seen = []
# def check(n, cnt):
#     if n not in seen:
#         seen.append(n)
#         if n == 1:
#             return cnt
#         else:
#             return check(SumSquare(n), cnt + 1)
#     else:
#         return -1

# for i in range(100):
#     if check(i,1) != -1:
#         n -= 1
#         seen = []
#         if n == 0:
#             print(check(i,1))
#         seen = []
n = int(input())

m = n
n = n ** 2
check = 1
print(n, m)
while m:
    x = n % 10
    y = m % 10
    if x != y:
        check = 0
        break
    n //= 10
    m //= 10
if check:
    print('Automorphic')
else:
    print("not Automorphic")