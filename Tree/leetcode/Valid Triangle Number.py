
def check_triangle(x, y, z):
    if x + y > z:
        return True
    return False
def triangle_number(nums):
    nums.sort()
    n = len(nums)
    count = 0
    for i in range(n - 1, 1, -1):
        left = 0
        right = i - 1
        while left < right:
            if check_triangle(nums[left], nums[right], nums[i]):
                print(nums[left], nums[right], nums[i])
                count += right - left
                right -= 1
            else:
                left += 1
    return count
nums = [2, 2, 3, 4]
print(triangle_number(nums))

