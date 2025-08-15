nums = list(map(int,input().split()))
nums.sort()
target = int(input())
n = []
for i in range(len(nums) - 3):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    for j in range(i+1,len(nums) - 2):
        if nums[j] == nums[j - 1] and j > i + 1:
            continue
        l = j + 1
        r = len(nums) - 1
        while l < r:
            total = nums[i] + nums[j] + nums[r] + nums[l]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                n.append([nums[i],nums[j],nums[r],nums[l]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums [r - 1]:
                    r -= 1
                l += 1
                r -= 1
for i in n:
    i.sort()
print(n)