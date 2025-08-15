# nums = [5,4,0,2,0,1,0,1,0]
# MAX = 0
# for i in range(len(nums)):
#     if i > max:
#         return False
#     MAX = max(MAX,i + nums[i])
#     if MAX >= len(nums) - 1:
#         return True
    
# return False
arr = [3,0,2,1,2]
def Find(arr,start):
    if start < 0 or start >= len(arr) or arr[start] == -1:
        return False
    if arr[start] == 0:
        return True
    jump_distance = arr[start]
    arr[start] = -1 
    return Find(arr, start + jump_distance) or Find(arr, start - jump_distance)
print(Find(arr,2))

    
    