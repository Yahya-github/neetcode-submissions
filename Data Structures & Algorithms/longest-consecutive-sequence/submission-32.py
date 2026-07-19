class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        koh = 0
        cur_range = 1
        dict_nums = {}
        for i in nums_set:
            if cur_range > koh:
                koh = cur_range
            if i - 1 in dict_nums:
                if i+1 in dict_nums:
                    cur_range = dict_nums[i-1][0] + dict_nums[i+1][0] + 1
                    dict_nums[i-1][0], dict_nums[i+1][0] = cur_range, cur_range
                else:
                    (dict_nums[i-1])[0] += 1
                    dict_nums[i] = dict_nums[i-1]
                    cur_range = dict_nums[i-1][0]  
            elif i+1 in dict_nums:
                dict_nums[i+1][0] += 1
                dict_nums[i] = dict_nums[i+1]
                cur_range = dict_nums[i+1][0]
            else:
                dict_nums[i] = [1]
                cur_range = 1
        if cur_range > koh:
            koh = cur_range
        print(dict_nums)
        return koh