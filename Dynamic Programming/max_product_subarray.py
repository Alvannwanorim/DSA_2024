from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min, cur_max = 1, 1
        res = max(nums)

        for n in nums:
            temp = n * cur_min
            cur_min = min(n * cur_min, n * cur_max, n)
            cur_max = max(temp, n * cur_max, n)
            res = max(res, cur_max)
        return res
