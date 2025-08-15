nums = [5,7,7,8,8,10] 
target = 6
if nums.count(target) < 2:
    lst = [-1,-1]
    print(lst)
i = 0
j = len(nums) - 1
while True:
    if nums[i] == target:
        break
    i += 1
while True:
    if nums[j] == target:
        break
    j -= 1

