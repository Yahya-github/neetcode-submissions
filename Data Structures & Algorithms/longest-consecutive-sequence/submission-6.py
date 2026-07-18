class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        koh = 0
        nums.sort()
        cur_range = 1
        pre_num = nums[0]
        for i in nums:
            if cur_range > koh:
                koh = cur_range
            if i - 1 == pre_num:
                cur_range += 1
            elif i == pre_num:
                continue
            else:
                cur_range = 1
            pre_num = i
        if cur_range > koh:
            koh = cur_range
        return koh