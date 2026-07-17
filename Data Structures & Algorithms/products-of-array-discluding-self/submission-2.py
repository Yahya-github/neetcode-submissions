class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_pre = [1 for _ in nums]
        prod_suf = prod_pre.copy()
        len_nums = len(nums)
        for i in range(1,len_nums):
            prod_pre[i] *= nums[i-1] * prod_pre[i-1]
            prod_suf[len_nums-1-i] *= nums[len_nums-i] * prod_suf[len_nums-i]
        return [i * j for i, j in zip(prod_pre,prod_suf)]

