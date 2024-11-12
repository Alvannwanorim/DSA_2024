from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0 
        r = len(nums) - 1
        res = []
        while l <= r:
            left = nums[l] * nums[l]
            right = nums[r] * nums[r]
            if left < right:
                res.append(right)
                r -= 1
            else:
                res.append(left)
                l += 1
        return res[::-1]