def check(n, m, k, river):

    dp = [0] * (n + 1) 
    r = river + 'L'
    Mark = -1
    for i in range(n + 1):
        if r[i] == 'C':
            dp[i] = 0
        elif Mark + m >= i:
            dp[i] = 1
            if r[i] == 'L':
                Mark = i
        elif dp[i-1] == 1 and k > 0:
            dp[i] = 1
            k -= 1
            if r[i] == 'L':
                Mark = i
    return dp[n] 

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        river = input().strip()
        if check(n, m, k, river):
            print("YES")
        else:
            print("NO")
#def game():
#   a = list(map(int,input().split()))
#   n = a[0]
#   l = a[1]
#   w = a[2]
#   s = input() + "L"
#   dp = ["NO"] * (n + 1)
#   markL = -1
#   for i in range(n + 1):
#     if s[i] == "C":
#       dp[i] = "NO"
#     elif (markL + l >= i):
#       dp[i] = "YES"
#       if s[i] == "L":
#         markL = i
#     elif (dp[i - 1] == "YES" and w > 0):
#   dp[i] = "YES"
#   w -= 1
#   if s[i] == "L":
#     markL = i
#   print(dp[n])
 
# n = int(input())
# for i in range(n):
#   game()
