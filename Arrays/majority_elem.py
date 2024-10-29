from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        res, maxCount = 0, 0

        for n in nums:
            counts[n] = 1+ counts.get(n,0)
            if counts[n] >= maxCount:
                maxCount= counts[n]
                res = n
        return res