from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, res = 0, float('inf')
        total = 0
        found = False
        for r in range(len(nums)):
            total += nums[r]
            
            while total >= target:
                found = True
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
                
        return res if found else 0
            