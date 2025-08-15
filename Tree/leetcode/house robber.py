nums = [2,7,9,3,1]
dp = [0] * len(nums)
dp[0] = nums[0]
dp[1] = nums[1]
for i in range(2,len(nums)):
    dp[i] = max(dp[i],nums[i] + dp[i - 2])
