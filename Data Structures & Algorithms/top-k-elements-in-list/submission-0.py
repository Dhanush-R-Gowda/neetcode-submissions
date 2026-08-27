class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        result = sorted(d, key=d.get, reverse=True)
        return result[:k]