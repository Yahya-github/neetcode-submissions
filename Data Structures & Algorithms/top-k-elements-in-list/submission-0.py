class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        FREQ = {}
        for i in nums:
            if i in FREQ:
                FREQ[i] += 1
            else:
                FREQ[i] = 1
        FREQ = sorted(list(FREQ.items()), key = lambda x: x[1], reverse=True)
        return [FREQ[i][0] for i in range(k)]