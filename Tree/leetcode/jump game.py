def canJump(nums) -> bool:
    if nums.count(0) == 0:
        return True
    MAX = 0
    for i in range(len(nums)):
        if i > MAX:
            return False
        MAX = max(MAX,i + nums[i])
        if MAX >= len(nums) - 1:
            return True
    return False

