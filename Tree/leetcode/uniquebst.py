n = 3
dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 2
for i in range(3,n + 1):
    for root in range(1, i + 1):
        left = root - 1
        right = i - root