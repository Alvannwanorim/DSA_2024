from collections import Counter
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = [0,0]
        for n in nums:
            if count[n] > 1:
                res[0] = n
                break
        for i in range(1, len(nums) + 1):
            if i not in count:
                res[1] = i
                break
        return res

        