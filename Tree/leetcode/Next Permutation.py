class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        permutations = sorted(set(itertools.permutations(nums)))
        current_tuple = tuple(nums)
        if current_tuple in permutations:
            current_index = permutations.index(current_tuple)
            if current_index + 1 < len(permutations):
                
                next_tuple = permutations[current_index + 1]

                for i in range(len(nums)):
                    nums[i] = next_tuple[i]
            else:
                
                nums.sort()
