# inf = float("inf")
# X =[[5,6,3],[9,4,1],[2,8,7]]
# Y = [[inf] * len(X[0]) for _ in range(len(X))]
# Z = [[2, 4, 9], [3, 5, 16], [8, 14, inf], [12, inf, inf]]

# lst = []

# def sortt(X, Y, lst):
#     for i in range(len(X)):
#         for j in range(len(X[0])):
#             add(Y, X[i][j])
#     while True:
#         x = get_min(Y)
#         if x != inf:
#             lst.append(x)
#         else:
#             break
#     return lst
    
# def get_min(X):
#     min_value = X[0][0]
#     X[0][0] = inf
#     i, j = 0, 0
#     while True:
#         down = X[i + 1][j] if i + 1 < len(X) else inf
#         right = X[i][j + 1] if j + 1 < len(X[0]) else inf
#         if down == right:
#             break
#         elif down < right:
#             X[i][j] = down
#             i += 1
#         elif down > right:
#             X[i][j] = right
#             j += 1
#         X[i][j] = inf

#     return min_value
# def add(X, value):
#     X[-1][-1] = value
#     i, j = len(X) - 1, len(X[0]) - 1
#     while True:
#         max_i = i
#         max_j = j
#         if X[i - 1][j] > X[max_i][max_j] and i - 1 >= 0:
#             max_j = j
#             max_i = i - 1
#         if X[i][j - 1] > X[max_i][max_j] and j - 1 >= 0:
#             max_i = i
#             max_j = j - 1
#         if max_i == i and max_j == j:
#             break
#         X[i][j], X[max_i][max_j] = X[max_i][max_j], X[i][j]
#         i, j = max_i, max_j
# def search(Z, target):
#     i = 0
#     j = len(Z[0]) - 1
#     while True:
#         if i > len(Z) - 1 or j < 0:
#             break
#         elif target > Z[i][j]:
#             i += 1
#         elif target < Z[i][j]:
#             j -= 1
#         else:
#             return True
#     return False
# print(search(Z, 14))

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# print(gcd(19,5))
# Mat1 = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# Mat2 = [[10,11,12],
#         [13,14,15],
#         [16,17,18]]

# def dot(Mat1, Mat2):
#     Mat = [[0] * len(Mat1) for _ in range(len(Mat1))]
#     for i in range(len(Mat1)):
#         for j in range(len(Mat1)):
#             for k in range(len(Mat1)):
#                 Mat[i][j] += Mat1[i][k] * Mat2[k][j]
#     return Mat
# def identity_matrix(n):
#     return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
# def matrix_power(Mat, k):
#     if k == 1:
#         return Mat
#     if k == 0:
#         return identity_matrix(len(Mat))
#     return dot(Mat, matrix_power(Mat, k - 1))
# print(matrix_power(Mat1, 3))
# def count(t):
#     maxx = float("-inf")
#     for i in t:
#         if i - 1 not in t:
#             cnt = 1
#             while i + 1 in t:
#                 cnt += 1
#                 i += 1
#             maxx = max(cnt, maxx)
#     return maxx
# print(count([1, 2, 1, 2, 1, 2])) 
# Hàm mã hóa chuỗi x thành số nguyên
# def encode(x):
#     total = 0
#     for i, c in enumerate(x):
#         total += (ord(c) - ord('a') + 1) * (i + 1)
#     return total

# # Hàm băm: bảng băm có kích thước 23
# def hash_func(x):
#     return (11 * encode(x) + 5) % 23

# # Dò bậc 2 để xử lý đụng độ
# def insert_quadratic_probing(keys, size=23):
#     table = [None] * size
#     for key in keys:
#         h = hash_func(key)
#         i = 0
#         while table[(h + i * i) % size] is not None:
#             i += 1
#         table[(h + i * i) % size] = key
#     return table

# # Danh sách khóa cần chèn
# keys = ["cat", "dog", "owl", "bat", "rat", "ant", "bee", "cow", "fox", "pig", "hen"]

# # Chèn vào bảng băm
# hash_table = insert_quadratic_probing(keys)

# # In bảng kết quả
# for i, val in enumerate(hash_table):
#     print(f"{i:2}: {val}")
# def count(t):
#     def heapify(t, n, i):
#         left = 2 * i + 1
#         right = 2 * i + 2
#         largest = i
#         if left < n and t[left] > t[largest]:
#             largest = left
#         if right < n and t[right] > t[largest]:
#             largest = right
#         if i != largest:
#             t[i], t[largest] = t[largest], t[i]
#             heapify(t, n, largest)
#     def heap_sort(t):
#         n = len(t)
#         for i in range(n // 2 - 1, -1, -1):
#             heapify(t, n, i)
#         for i in range(n - 1, 0, -1):
#             t[i], t[0] = t[0], t[i]
#             heapify(t, i, 0)
#     heap_sort(t)

#     cnt = 1
#     maxx = 1
#     for i in range(1,len(t)):
#         if t[i] - 1 == t[i - 1]:
#             cnt += 1
#         else:
#             maxx = max(maxx, cnt)
#             cnt = 1
#     maxx = max(maxx, cnt)
#     return maxx
# print(count([7, 6, 1, 8]))
# def quicksort(lst, left, right):
#     if left < right:
#         i, j = left, right
#         pivot = lst[(left + right) // 2 + 1]
#         while i <= j:
#             while lst[i] < pivot:
#                 i += 1
#             while lst[j] > pivot:
#                 j -= 1
#             if i <= j:
#                 lst[i], lst[j] = lst[j], lst[i]
#                 i += 1
#                 j -= 1
#         if left < j:
#             quicksort(lst, left, j)
#         if i < right:
#             quicksort(lst, i, right)
        
# lst = [5,4,3,2,1]
# quicksort(lst, 0, len(lst) - 1)
# print(lst)

# def merge(lst, left, mid, right):
#     x = lst[left : mid + 1]
#     y = lst[mid + 1: right + 1]
#     i = 0
#     j = 0
#     while i < len(x) and j < len(y):
#         if x[i] < y[j]:
#             lst[left] = x[i]
#             i += 1
#         else:
#             lst[left] = y[j]
#             j += 1
#         left += 1
#     while i < len(x):
#         lst[left] = x[i]
#         i += 1
#         left += 1
#     while j < len(y):
#         lst[left] = y[j]
#         j += 1
#         left += 1
    

# def mergesort(lst, left, right):
#     if left >= right:
#         return
#     mid = (left + right) // 2
#     mergesort(lst, left, mid)
#     mergesort(lst, mid + 1, right)
#     merge(lst, left, mid, right)
# lst = [5,4,3,2,1]
# mergesort(lst, 0, len(lst) - 1)
# print(lst)
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end = "")
    for j in range(1, i + 1):
        print(j, end = "")
    for j in range(i - 1, 0, -1):
        print(j, end = "")
    print()


