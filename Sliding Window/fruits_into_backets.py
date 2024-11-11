import collections
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = collections.defaultdict(int)
        res = 0 
        l = 0 
        total = 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1
            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                l += 1
                total -= 1
                if not count[f]:
                    del count[f]
            res = max(res, total)
        return res
