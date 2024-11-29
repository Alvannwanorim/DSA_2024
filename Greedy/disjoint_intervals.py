from typing import List


def disjoint_intervals(nums: List[List[int]]):
    nums.sort(key= lambda x: x[1])
    print(nums)
    count = 1
    prev_s, prev_e = nums[0]
    for s,e in nums:
        if s <= prev_e:
            continue
        else:
            prev_s, prev_e = s, e 
            count += 1
    return count
print(disjoint_intervals([[1,2],[2,10],[4,6]]))