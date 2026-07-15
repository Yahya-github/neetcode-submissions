class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for _ in nums:
            if nums.pop() in nums:
                return True

        return False