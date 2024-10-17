from typing import List


def twoSum(nums1:List[int], nums2: List[int], k:int):
    start = nums1 if len(nums1)> len(nums2) else nums2
    second = nums2 if len(nums1)< len(nums2) else nums1
    table = {i:i for i in start}
    for n in second:
        diff = k - n
        if diff in table:
            return [table[diff], n]
    return []

print(twoSum([1,2,3,4], [2,3,5,2], 9))