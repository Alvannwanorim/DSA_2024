from typing import List


def highest_products(nums:List[int]):
    nums.sort()
    max_one = nums[-1] * nums[-2] * nums[-3]
    max_two = nums[0] * nums[1] * nums[-1]
    return max(max_one, max_two)

print(highest_products([-2,-3,-1, 0,0, 2,3,4]))
print(highest_products([0,0,4,5,2,3,4]))

