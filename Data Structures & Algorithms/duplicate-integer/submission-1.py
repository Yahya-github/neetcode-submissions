class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        verif_list = nums.copy()
        for _ in verif_list:
            if verif_list.pop() in verif_list:
                return True
        return False