class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        prod = [1 for _ in range(len_nums)]
        strt_prod = 1
        end_prod = 1
        for i in range(1,len_nums):
            strt_prod *= nums[i-1]
            end_prod *= nums[len_nums-i]
            prod[i] *= strt_prod
            prod[len_nums-i-1] *= end_prod
            
        return prod

