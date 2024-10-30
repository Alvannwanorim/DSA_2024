from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.query = []
        total = 0
        for n in nums:
            total += n
            self.query.append(total)

    def sumRange(self, left: int, right: int) -> int:
        # print(self.query)
        r = self.query[right]
        l = self.query[left - 1] if left > 0 else 0
        return r - l
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)