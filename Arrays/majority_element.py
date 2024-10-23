from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums)//2 
        table = {}
        for n in nums:
            if n in table:
                table[n] += 1
            else:
                table[n] = 1
            if table[n] > limit:
                return n
        