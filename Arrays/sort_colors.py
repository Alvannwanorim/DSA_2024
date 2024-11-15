from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = 0
        c1 = 0
        c2 = 0

        for n in nums:
            if n == 0:
                c0 += 1
            if n == 1:
                c1 += 1
            if n == 2:
                c2 += 1

        index = 0

        for i in range(c0):
            nums[index] = 0
            index += 1

        for i in range(c1):
            nums[index] = 1
            index += 1
        for i in range(c2):
            nums[index] = 2
            index += 1
        
        return nums
