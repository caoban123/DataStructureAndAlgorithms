# dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
# m, n = len(dungeon), len(dungeon[0])

# # Khởi tạo dp với kích thước m x n. dp[i][j] là lượng máu tối thiểu cần thiết tại ô (i, j)
# dp = [[0] * n for _ in range(m)]

# # Khởi tạo dp[0][0] = 1, vì đây là điểm bắt đầu
# dp[0][0] = max(1, 1 - dungeon[0][0])  # Đảm bảo hiệp sĩ có ít nhất 1 máu

# # Tính toán cho hàng đầu tiên (di chuyển từ trái sang phải)
# for j in range(1, n):
#     dp[0][j] = max(1, dp[0][j-1] - dungeon[0][j])

# # Tính toán cho cột đầu tiên (di chuyển từ trên xuống dưới)
# for i in range(1, m):
#     dp[i][0] = max(1, dp[i-1][0] - dungeon[i][0])

# # Tính toán cho các ô còn lại (di chuyển từ trên xuống dưới và từ trái sang phải)
# for i in range(1, m):
#     for j in range(1, n):
#         dp[i][j] = max(1, min(dp[i-1][j], dp[i][j-1]) - dungeon[i][j])

# # Kết quả là lượng máu tối thiểu cần thiết tại ô (m-1, n-1)
# print(dp)
# a, b, c = map(int,input().split())
# print(a*500 + b * 1000 + c * 1500)
ratings = [1,0,2]
# ratings.sort()
lst = [1] * len(ratings)
x = 1
i = 1
while i < len(lst) - 1:
    if ratings[i - 1] < ratings[i]:
        lst[i] = lst[i - 1] + 1
    if ratings[i + 1] < ratings[i]:
        lst[i] = lst[i + 1] + 1
    i += 1
if ratings[0] > ratings[1]:
    lst[1] += 1
if ratings[-1] > ratings[-2]:
    lst[-1] += 1
j = len(lst) - 2
lst1 = [1] * len(ratings)
while j >= 1:
    if ratings[j - 1] < ratings[j]:
        lst1[j] = lst1[j - 1] + 1
    if ratings[j + 1] < ratings[j]:
        lst1[j] = lst1[j + 1] + 1
    j -= 1
if ratings[0] > ratings[1]:
    lst1[1] += 1
if ratings[-1] > ratings[-2]:
    lst1[-1] += 1
x = 0
lst2 = []
while x < len(lst) :
    if lst1[x] > lst[x]:
        lst2.append(lst1[x])
    elif lst[x] > lst1[x]:
        lst2.append(lst[x])
    else:
        lst2.append(lst[x])
    x += 1
print(lst)
print(lst1)
print(lst2)
