from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for n, i in count.items():
            freq[i].append(n)
        
        for i in range(len(nums), -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res
