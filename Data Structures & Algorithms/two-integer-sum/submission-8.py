class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_nums = []
        for i in range(len(nums)):
            i_nums.append((nums[i], i))
        i_nums.sort(key = lambda x: x[0])
        mini = 0
        maxi = len(nums) - 1
        for _ in range(maxi):
            verif = i_nums[mini][0] + i_nums[maxi][0]
            if verif < target:
                mini += 1
            elif verif > target:
                maxi -= 1
            else:
                return sorted([i_nums[mini][1],i_nums[maxi][1]])
        return []