from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        max1, max2 = nums[-1], nums[-2]
        min1, min2 = nums[0], nums[1]

        return (max1 * max2) - (min1 * min2)


class Solution2:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max2 = 0
        min1 = min2 = float("inf")

        for n in nums:
            if n > max2:
                if n > max1:
                    max1 , max2 = n, max1
                else:
                    max2 = n
            if n < min2:
                if n < min1:
                    min1, min2 = n, min1
                else:
                    min2 = n
        
        return (max1 * max2) - (min2 * min1)