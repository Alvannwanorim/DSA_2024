from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] != 0 and nums[l] == 0:
                nums[r], nums[l] = nums[l], nums[r]
            if nums[l] != 0:
                l += 1
            r += 1