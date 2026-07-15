class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length_nums = len(nums)
        for i in range(length_nums):
                if nums[i] in nums[i+1:]:
                    return True
        return False
