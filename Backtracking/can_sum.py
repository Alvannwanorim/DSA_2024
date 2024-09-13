from typing import List
def can_sum(target: int, nums: List[int]):
    if target ==0:
        return True
    if target < 0 :
        return False
    for n in nums: 
        return can_sum(target - n, nums)

print(can_sum(7, [4, 9, 5,4,6]))
